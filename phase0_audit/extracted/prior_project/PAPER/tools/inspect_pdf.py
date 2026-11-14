#!/usr/bin/env python3
"""Programmatic inspection of a built PDF (Phase 8B, task D).

Checks the things a human would look for when proof-reading a PDF, using
measurements from the PDF itself rather than the eye:

  G1  page geometry: size, orientation, and whether any ink falls outside the
      printable area (clipping) or collides with the trim edge
  G2  overlapping text: two spans whose rectangles intersect by more than a
      token amount, which indicates overprinting
  G3  fonts: every font embedded, and what kind (Type1 / TrueType / etc.)
  G4  unresolved glyphs: PyMuPDF substitutes U+FFFD for a glyph it cannot map
  G5  the inventory of numbered environments (Theorems, Propositions, ...,
      Examples) actually rendered on the pages
  G6  the inventory of quantum-code tuples [[n,k,d;c]]_q and [[n,k,d]]_q
  G7  the bibliography: entries rendered, and how many carry a DOI
  G8  structural landmarks: title, abstract, TOC, section headings, tables,
      appendices

Optionally compares two PDFs (--compare) inventory by inventory.

Usage:  python3 tools/inspect_pdf.py PDF [--compare OTHER.pdf]
"""
import argparse
import re
import sys


LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
             "\ufb03": "ffi", "\ufb04": "ffl", "\ufb05": "ft",
             "\ufb06": "st", "\u2011": "-"}


def norm(t):
    """Undo hyphenation and fold presentation ligatures.

    pdfTeX 1.40.11 wrote 'fi' as the single glyph U+FB01; 1.40.26 writes the
    two characters.  Without folding, a pure text comparison between the two
    PDFs reports hundreds of phantom differences.
    """
    t = re.sub(r"-\n\s*", "", t)
    for k, v in LIGATURES.items():
        t = t.replace(k, v)
    return t


def spans(doc):
    out = []
    for pno, page in enumerate(doc, 1):
        for blk in page.get_text("dict")["blocks"]:
            for line in blk.get("lines", []):
                for sp in line.get("spans", []):
                    out.append((pno, sp["bbox"], sp["text"], sp["font"],
                                sp["size"]))
    return out


def geometry(doc):
    print("G1  page geometry")
    bad = []
    sizes = {}
    for pno, page in enumerate(doc, 1):
        r = page.rect
        sizes[(round(r.width), round(r.height))] = \
            sizes.get((round(r.width), round(r.height)), 0) + 1
        for blk in page.get_text("dict")["blocks"]:
            if blk["type"] != 0:
                continue
            for line in blk["lines"]:
                for sp in line["spans"]:
                    x0, y0, x1, y1 = sp["bbox"]
                    if (x0 < 8 or y0 < 8 or x1 > r.width - 8
                            or y1 > r.height - 8):
                        if sp["text"].strip():
                            bad.append((pno, round(x0, 1), round(y0, 1),
                                        round(x1, 1), round(y1, 1),
                                        sp["text"].strip()[:50]))
    for s, n in sorted(sizes.items()):
        print("    size %.0f x %.0f pt (%d pages)" % (s[0], s[1], n))
    print("    page size uniform: %s" % ("yes" if len(sizes) == 1 else "NO"))
    print("    ink outside a 8 pt bleed: %d" % len(bad))
    for b in bad[:10]:
        print("      p%-3d (%7.1f,%7.1f)-(%7.1f,%7.1f)  %s"
              % (b[0], b[1], b[2], b[3], b[4], b[5]))
    return len(bad)


def overlaps(doc):
    print("G2  overlapping text spans")
    n = 0
    for pno, page in enumerate(doc, 1):
        sp = [(s["bbox"], s["text"].strip())
              for blk in page.get_text("dict")["blocks"] if blk["type"] == 0
              for line in blk["lines"] for s in line["spans"]
              if s["text"].strip()]
        for i in range(len(sp)):
            for j in range(i + 1, len(sp)):
                a, b = sp[i][0], sp[j][0]
                ox = min(a[2], b[2]) - max(a[0], b[0])
                oy = min(a[3], b[3]) - max(a[1], b[1])
                # Maths builds composite symbols from stacked glyphs
                # (e.g. '~' over '=' for \cong, a subscript tucked under an
                # 'R').  Only flag overlaps between real runs of text.
                if ox > 1.5 and oy > 1.5 and len(sp[i][1]) > 2 \
                        and len(sp[j][1]) > 2:
                    n += 1
                    if n <= 8:
                        print("      p%-3d %r / %r  (%.1f x %.1f pt)"
                              % (pno, sp[i][1][:28], sp[j][1][:28], ox, oy))
    print("    overlapping pairs: %d" % n)
    return n


def fonts(doc):
    print("G3  fonts")
    seen = {}
    for pno, page in enumerate(doc, 1):
        for f in page.get_fonts(full=True):
            xref, ext, ftype, base = f[0], f[1], f[2], f[3]
            seen.setdefault(base, [ext, ftype, 0])
            seen[base][2] += 1
    notemb = [(b, v) for b, v in seen.items()
              if v[0] in ("n/a", "")]
    print("    distinct fonts: %d" % len(seen))
    for b in sorted(seen):
        ext, ftype, cnt = seen[b]
        print("      %-34s %-10s %-6s (%d pages)"
              % (b, ext or "embedded", ftype, cnt))
    print("    fonts with no embedded file: %d" % len(notemb))
    return len(notemb)


def unresolved(doc):
    print("G4  unresolved glyphs")
    bad = []
    for pno, page in enumerate(doc, 1):
        t = page.get_text()
        if "\ufffd" in t:
            for i, line in enumerate(t.splitlines()):
                if "\ufffd" in line:
                    bad.append((pno, i + 1, line.strip()[:70]))
    print("    pages containing U+FFFD: %d" % len(bad))
    for b in bad[:10]:
        print("      p%-3d line %d: %s" % b)
    return len(bad)


ENVS = ("Theorem", "Lemma", "Proposition", "Corollary", "Definition",
        "Remark", "Example", "Conjecture")


def inventory(doc):
    flat = re.sub(r"\s+", " ", norm("\n".join(p.get_text() for p in doc)))

    print("G5  numbered environments rendered")
    items = {}
    for env in ENVS:
        nums = sorted({float(x) for x in
                       re.findall(r"%s\s+(\d+\.\d+)" % env, flat)})
        items[env] = nums
        print("    %-12s %3d  %s"
              % (env, len(nums),
                 " ".join("%g" % n for n in nums[:40])
                 + (" ..." if len(nums) > 40 else "")))
    print("    TOTAL        %3d"
          % sum(len(v) for v in items.values()))

    # In the PDF the subscript q of [[n,k,d]]_q is a separate span, so the
    # extracted text reads '[[24, 8, 4]]9'.  Match the tuple without the _q.
    ea = sorted({re.sub(r"\s+", "", m) for m in
                 re.findall(r"\[\[(\d+\s*,\s*\d+\s*,\s*\d+\s*;"
                            r"\s*\d+)\s*\]\]", flat)})
    st = sorted({re.sub(r"\s+", "", m) for m in
                 re.findall(r"\[\[(\d+\s*,\s*\d+\s*,\s*\d+)\s*\]\]",
                            flat)} - set(ea))
    print("G6  quantum-code tuples rendered")
    print("    [[n,k,d;c]]_q distinct: %d" % len(ea))
    for t in ea:
        print("      [[%s]]" % t)
    print("    [[n,k,d]]_q distinct: %d" % len(st))
    for t in st:
        print("      [[%s]]" % t)

    print("G7  bibliography")
    entries = re.findall(r"\[(\d+)\]", flat)
    print("    numbered entries rendered: %d" % len(set(entries)))
    print("    DOIs rendered: %d"
          % len(set(re.findall(r"doi[:\s]*10\.\d{4,9}/", flat))))

    print("G8  landmarks")
    for name, pat in [("title", r"Quantum Error-Correcting Codes from Galois"),
                      ("abstract", r"\bAbstract\b"),
                      ("keywords", r"\bKey words\b|\bKeywords\b"),
                      ("contents/TOC", r"\bContents\b"),
                      ("References", r"\bReferences\b")]:
        print("    %-16s %s" % (name, "present" if re.search(pat, flat)
                                else "ABSENT"))
    tabs = sorted(set(re.findall(r"Table\s+(\d+):", flat)), key=int)
    print("    tables: %s" % ", ".join(tabs))
    return flat


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--compare", default=None)
    a = ap.parse_args()

    import pymupdf
    doc = pymupdf.open(a.pdf)
    print("=" * 78)
    print("PDF INSPECTION  %s" % a.pdf)
    print("=" * 78)
    d = doc
    print("pages          : %d" % d.page_count)
    print("PDF version    : %s" % d.metadata.get("format"))
    print("producer       : %s" % d.metadata.get("producer"))
    print("title          : %r" % (d.metadata.get("title") or ""))
    print("author         : %r" % (d.metadata.get("author") or ""))
    print("-" * 78)

    n_bad = 0
    n_bad += geometry(d)
    n_bad += overlaps(d)
    n_bad += fonts(d)
    n_bad += unresolved(d)
    flat = inventory(d)

    if a.compare:
        other = pymupdf.open(a.compare)
        oflat = re.sub(r"\s+", " ", norm(
            "\n".join(p.get_text() for p in other)))
        print("-" * 78)
        print("COMPARISON against %s" % a.compare)
        mine, theirs = set(), set()
        for env in ENVS:
            mine |= {(env, n) for n in
                     re.findall(r"%s\s+(\d+\.\d+)" % env, flat)}
            theirs |= {(env, n) for n in
                       re.findall(r"%s\s+(\d+\.\d+)" % env, oflat)}
        print("  env numbers only in modern : %s"
              % sorted(x[0] + " " + x[1] for x in mine - theirs))
        print("  env numbers only in other  : %s"
              % sorted(x[0] + " " + x[1] for x in theirs - mine))
        ea = lambda t: {x.replace(" ", "") for x in re.findall(
            r"\[\[(\d+,\s*\d+,\s*\d+;\s*\d+)\]\]", t)}
        sa = lambda t: {x.replace(" ", "") for x in re.findall(
            r"\[\[(\d+,\s*\d+,\s*\d+)\]\]", t)}
        print("  EA tuples only in modern   : %s" % sorted(ea(flat) - ea(oflat)))
        print("  EA tuples only in other    : %s" % sorted(ea(oflat) - ea(flat)))
        print("  stab tuples only in modern : %s"
              % sorted(sa(flat) - sa(oflat)))
        print("  stab tuples only in other  : %s"
              % sorted(sa(oflat) - sa(flat)))
        c = lambda t: set(re.findall(r"\{(\w+)\}|\[(\d+)\]", t))
        print("  citation keys/refs: modern=%d other=%d"
              % (len(re.findall(r"\[\d+\]", flat)),
                 len(re.findall(r"\[\d+\]", oflat))))

    print("-" * 78)
    print("issues found: %d" % n_bad)
    return 0


if __name__ == "__main__":
    sys.exit(main())
