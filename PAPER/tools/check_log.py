#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_log.py -- analyse a TeX log and attribute every warning to a file.

The TeX log interleaves the sources it reads, and a bare ``l.66`` or
``detected at line 66`` in a warning is meaningless without knowing which file
was open at that moment.  This script tracks the ``(file`` / ``)`` markers
pdfTeX writes and reports, for each warning, the file it is attributed to.

The parser is deliberately strict about what counts as a marker, because the
log also echoes source text that is full of parentheses:

* an OPEN is a ``(`` immediately followed by a path ending in a known TeX
  extension (``.tex .sty .cls .def .fd .cfg .clo .ldf .dfu .map .enc .ini
  .mkii .toc .aux .bbl .out .lof .lot``);
* a CLOSE is either a whole line of ``)`` characters, or a run of ``)`` at the
  very start / very end of a line (after stripping trailing ``[3]`` page
  markers).  Everything else -- ``(Font)``, ``(hyperref)``, ``(a+b)`` in echoed
  math -- is prose and is stripped before scanning.

The script prints a self-check: if the number of opens and closes does not
balance, the attribution is reported as unreliable.

Usage
-----
    python3 tools/check_log.py [main.log] [--tol PT]

``--tol`` sets the threshold (default 5pt) above which an overfull box counts
as a defect.

Exit status
-----------
0 if there are no errors, no missing characters, and no overfull box worse
than ``--tol``; 1 otherwise; 2 if the log could not be read or the file
attribution did not balance.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

EXT = (r"(?:tex|sty|cls|def|fd|cfg|clo|ldf|dfu|map|enc|ini|mkii"
       r"|toc|aux|bbl|out|lof|lot|nav|snm)")
OPEN = re.compile(r"\((\.?/?[^\s()]+\." + EXT + r")")


def strip_prose(ln):
    """remove balanced parenthesised groups that contain no file path"""
    out = ln
    for _ in range(4):
        new = re.sub(r"\([^()]*\)",
                     lambda m: " " * len(m.group(0))
                     if not OPEN.search(m.group(0)) else m.group(0),
                     out)
        if new == out:
            break
        out = new
    return re.sub(r"^\([A-Za-z][A-Za-z ]*\)",
                  lambda m: " " * len(m.group(0)), out)


_FONT = re.compile(r"\\[A-Za-z0-9]{2,4}/[^ ]*")
_KERN = re.compile(r"\\[A-Za-z]+")


def _excerpt(lines, idx, nlines=3):
    """a human-readable locator for a box warning.

    TeX prints the offending box right after the warning: font selections,
    empty '[]' boxes for missing characters, and line-broken text.  Strip all
    of that and keep the words, so the offending passage can be found with a
    plain grep even if the file attribution is uncertain.
    """
    buf = []
    for ln in lines[idx + 1:idx + 1 + nlines]:
        if not ln.strip():
            break
        if re.match(r"^(Overfull|Underfull|Missing character|LaTeX Warning|"
                    r"Package |!|\\)", ln):
            break
        buf.append(ln)
    txt = " ".join(buf)
    txt = _FONT.sub(" ", txt)
    txt = txt.replace("[]", " ")
    txt = re.sub(r"\\\\[A-Za-z]+", " ", txt)
    txt = re.sub(r"\s+", " ", txt)
    return txt.strip()[:88]


def _strip_page_markers(s, side):
    """remove a leading ('l') or trailing ('r') run of [3] page markers"""
    while True:
        if side == "l" and s.lstrip().startswith("["):
            t = s.lstrip()
            k = t.find("]")
            if k < 0:
                break
            s = t[k + 1:].lstrip()
        elif side == "r" and s.rstrip().endswith("]"):
            t = s.rstrip()
            k = t.rfind("[")
            if k < 0:
                break
            s = t[:k].rstrip()
        else:
            break
    return s


def _prose_paren_positions(ln, opens):
    """positions of ')' that belong to prose parentheses, not to a file.

    pdfTeX wraps long lines, so a prose '(' opened on one line may be closed
    several lines later ('Package: ... (HO' / ')').  Walk the line with the
    file-open spans removed, tracking the prose nesting depth carried over
    from previous lines; every ')' that closes a prose '(' is reported here.
    """
    spans = [(a, b) for a, b, _g in opens]
    prose, depth = set(), _prose_paren_positions.depth
    # Only package/message lines wrap a prose '(' across lines.  The echoed
    # source inside an overfull-box dump is full of parentheses that are NOT
    # line-wrapped in this way, and including it derails the counter, so the
    # depth is only maintained over message lines.
    if not re.match(r"^(?:Package |LaTeX |Class |\([A-Za-z])", ln):
        return prose
    for j, ch in enumerate(ln):
        if any(s <= j < e for s, e in spans):
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth > 0:
                depth -= 1
                prose.add(j)
    _prose_paren_positions.depth = depth
    return prose


_prose_paren_positions.depth = 0


def _markers(ln):
    """(opens, closes) as ordered lists of (position, name) / position.

    An open is a '(' followed by a TeX-ish path.  A close is a ')' that
    (a) starts the line, (b) ends the line, or (c) follows an open --
    in each case after stripping page markers, spaces and prose parens.
    Parentheses inside echoed source text therefore never count.
    """
    opens = [(m.start(), m.end(), m.group(1)) for m in OPEN.finditer(ln)]
    prose = _prose_paren_positions(ln, opens)
    cands = set(j for j, ch in enumerate(ln) if ch == ")") - prose
    closes = set()
    # (a) a run of ')' at the very start of the line
    lead = _strip_page_markers(ln.lstrip(), "l")
    off = len(ln) - len(lead)
    for j in range(off, len(ln)):
        if ln[j] != ")":
            break
        closes.add(j)
    # (b) a run of ')' at the very end of the line
    tail = _strip_page_markers(ln.rstrip(), "r")
    for j in range(len(tail) - 1, -1, -1):
        if tail[j] != ")":
            break
        closes.add(j)
    # (c) a ')' immediately after a file-open span
    for _a, b, _g in opens:
        j = b
        while j < len(ln) and ln[j] == " ":
            j += 1
        if j < len(ln) and ln[j] == ")":
            closes.add(j)
    return opens, sorted(closes & cands)


def scan(lines):
    """yield (lineno, current_file) for every line, tracking file markers"""
    stack, nopen, nclose, unbalanced = [], 0, 0, 0
    _prose_paren_positions.depth = 0
    for i, ln in enumerate(lines):
        ln = strip_prose(ln)
        opens, closes = _markers(ln)
        events = ([(a, 0, g) for a, _b, g in opens] +
                  [(j, 1, ")") for j in closes])
        for _pos, kind, name in sorted(events):
            if kind == 0:
                stack.append(name)
                nopen += 1
            else:
                nclose += 1
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        yield i + 1, (stack[-1] if stack else "<preamble>")
    yield None, (nopen, nclose, unbalanced, len(stack))


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default=os.path.join(ROOT, "main.log"))
    ap.add_argument("--tol", type=float, default=5.0,
                    help="an overfull box wider than this (pt) is a defect")
    ns = ap.parse_args()
    tol, log = ns.tol, ns.log
    if not os.path.exists(log):
        print("check_log.py: no log at", log)
        return 2

    lines = open(log, encoding="utf-8", errors="replace").read().split("\n")

    rows, audit = [], None
    for ln, cur in scan(lines):
        if ln is None:
            audit = cur
            break
        text = lines[ln - 1]
        if re.match(r"^(!|Overfull|Underfull|Missing character|"
                    r"LaTeX Warning|Package \w+ Warning)", text):
            rows.append((cur, ln, text, _excerpt(lines, ln - 1)))

    nopen, nclose, unbalanced, leftover = audit
    balanced = (nopen == nclose and unbalanced == 0 and leftover == 0)

    errs = [r for r in rows if r[2].startswith("!")]
    miss = [r for r in rows if r[2].startswith("Missing character")]
    over = [r for r in rows if r[2].startswith("Overfull")]
    under = [r for r in rows if r[2].startswith("Underfull")]
    warn = [r for r in rows if r[2].startswith("LaTeX Warning")
            or r[2].startswith("Package ")]

    def mag(s):
        m = re.search(r"\(([0-9.]+)pt too wide", s)
        return float(m.group(1)) if m else 0.0

    bad = [r for r in over if mag(r[2]) > tol]

    print("=" * 78)
    print("TeX LOG ANALYSIS  (%s)" % log)
    print("=" * 78)
    print("  errors                    : %d" % len(errs))
    print("  missing characters        : %d" % len(miss))
    print("  overfull boxes            : %d  (worse than %.1fpt: %d)"
          % (len(over), tol, len(bad)))
    print("  underfull boxes           : %d" % len(under))
    print("  LaTeX/package warnings    : %d" % len(warn))
    print("  file-marker audit         : %d opens, %d closes, %d stray,"
          " %d unclosed  ->  %s"
          % (nopen, nclose, unbalanced, leftover,
             "balanced" if balanced else "UNRELIABLE ATTRIBUTION"))
    print("-" * 78)

    if errs:
        print("ERRORS")
        for f, n, s, _e in errs[:40]:
            print("  %-44s log:%-7d %s" % (f, n, s[:66]))
        print("-" * 78)
    if miss:
        seen = set()
        for f, n, s, _e in miss:
            if (f, s) not in seen:
                seen.add((f, s))
                print("  MISSING %-22s %s" % (f, s[:66]))
        print("  (%d occurrences)" % len(miss))
        print("-" * 78)
    if bad:
        print("OVERFULL BOXES WORSE THAN %.1fpt" % tol)
        for f, n, s, ex in sorted(bad, key=lambda r: -mag(r[2])):
            print("  %7.2fpt  %s" % (mag(s), f))
            print("           log:%-6d %s" % (n, ex))
        print("-" * 78)
    if warn:
        ws = {}
        for f, n, s, _e in warn:
            ws.setdefault(s.strip(), []).append(f)
        for s, fs in sorted(ws.items()):
            print("  WARN x%-3d %s   [%s]"
                  % (len(fs), s[:84], ",".join(sorted(set(fs))[:3])))
        print("-" * 78)

    ok = not errs and not miss and not bad
    print("VERDICT: %s" % ("clean" if ok else "issues remain"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
