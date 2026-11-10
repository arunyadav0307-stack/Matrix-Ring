#!/usr/bin/env python3
"""
make_manifest.py -- write SHA-256 manifests.

  python3 tools/make_manifest.py

Writes
  supplementary/MANIFEST.sha256   every file under supplementary/
  SHA256_MANIFEST.md              every file of the manuscript + package,
                                  with a self-hash of the manifest body so
                                  that the manifest itself can be verified.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

SKIP_DIRS = {".git", "__pycache__", ".arena", "Unselected files"}
# LaTeX build artefacts: reproducible from main.tex, not part of the package.
SKIP_FILES = {"SHA256_MANIFEST.md", "MANIFEST.sha256",
              "main.aux", "main.log", "main.toc", "main.out", "main.lof",
              "main.lot", "main.blg", "missfont.log", "build_pass3.log",
              ".build_main.tex"}
SKIP_SUFFIX = (".zip", ".sha256")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk(base):
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for f in sorted(filenames):
            if f in SKIP_FILES or f.endswith(SKIP_SUFFIX):
                continue
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, base)
            out.append((rel, sha256(p), os.path.getsize(p)))
    return out


def main():
    # ---- supplementary manifest (relative to supplementary/, for sha256sum -c)
    sup = os.path.join(ROOT, "supplementary")
    rows = walk(sup)
    with open(os.path.join(sup, "MANIFEST.sha256"), "w") as fh:
        for rel, h, _ in rows:
            fh.write("%s  %s\n" % (h, rel))
    print("supplementary/MANIFEST.sha256 : %d files" % len(rows))

    # ---- full manifest
    full = walk(ROOT)
    body = []
    body.append("# SHA-256 manifest")
    body.append("")
    body.append("Manuscript and supplementary package for")
    body.append("")
    body.append("> Quantum Error-Correcting Codes from Galois Hulls of Cyclic")
    body.append("> Codes over Noncommutative Matrix Rings")
    body.append("")
    body.append("Every file below was hashed with SHA-256 over its full")
    body.append("contents.  Verify with")
    body.append("")
    body.append("```")
    body.append("cd supplementary && sha256sum -c MANIFEST.sha256")
    body.append("```")
    body.append("")
    body.append("for the package, or re-run `python3 tools/make_manifest.py`")
    body.append("to regenerate this file and compare the table.")
    body.append("")
    body.append("| file | size (bytes) | SHA-256 |")
    body.append("|---|---:|---|")
    for rel, h, sz in full:
        body.append("| `%s` | %d | `%s` |" % (rel, sz, h))
    body.append("")
    body.append("Totals: %d files, %d bytes."
                % (len(full), sum(r[2] for r in full)))
    body.append("")
    text = "\n".join(body) + "\n"
    self_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    text += ("\nSelf-hash of this manifest (SHA-256 of everything above this\n"
             "line, UTF-8 encoded): `%s`\n" % self_hash)
    with open(os.path.join(ROOT, "SHA256_MANIFEST.md"), "w") as fh:
        fh.write(text)
    print("SHA256_MANIFEST.md             : %d files, self-hash %s"
          % (len(full), self_hash[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
