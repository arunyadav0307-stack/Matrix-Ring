#!/usr/bin/env python3
"""
make_package.py -- build the shipped archive.

  python3 tools/make_package.py [label]

With no argument the label defaults to today's date, giving
``MatrixRingManuscript_YYYYMMDD.zip``.  Pass a label to override it, e.g.

  python3 tools/make_package.py 20261109_Phase8A

Contents: everything in PAPER/ except the LaTeX build artefacts (which
compile/build.sh regenerates), __pycache__, and any previously built archive.
The archive's SHA-256 is written to a sidecar ``<archive>.sha256`` that is
deliberately NOT inside the archive, so that the hash is checkable against the
archive as shipped.
"""

import datetime
import hashlib
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

SKIP_DIRS = {".git", "__pycache__", ".arena", "Unselected files", ".texlive"}
SKIP_NAMES = {
    "main.aux", "main.log", "main.out", "main.toc", "main.lof", "main.lot",
    "main.blg", "missfont.log", "build_pass3.log", ".build_main.tex",
}
# .sha256 sidecars are kept only inside supplementary/ (where they are a
# deliverable); the top-level ones belong to archives that are not shipped
# inside this one.
SKIP_SUFFIX = (".zip",)
ALLOW_DOTFILES = {".gitignore"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build(label, out_dir):
    prefix = "MatrixRingManuscript_%s" % label
    arc = os.path.join(out_dir, prefix + ".zip")
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in SKIP_DIRS and not d.startswith("."))
        if os.path.relpath(dirpath, ROOT) == ".":
            dirnames[:] = [d for d in dirnames]
        is_root = os.path.relpath(dirpath, ROOT) == "."
        for f in sorted(filenames):
            if f in SKIP_NAMES:
                continue
            if f.endswith(SKIP_SUFFIX):
                continue
            if f.endswith(".sha256") and is_root:
                continue
            if f.startswith(".") and f not in ALLOW_DOTFILES:
                continue
            files.append(os.path.join(dirpath, f))
    if os.path.exists(arc):
        os.remove(arc)
    with zipfile.ZipFile(arc, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            z.write(p, prefix + "/" + rel)
    h = sha256(arc)
    with open(arc + ".sha256", "w") as fh:
        fh.write("%s  %s\n" % (h, os.path.basename(arc)))
    # integrity check
    with zipfile.ZipFile(arc) as z:
        bad = z.testzip()
    assert bad is None, bad
    total = sum(os.path.getsize(p) for p in files)
    print("archive     : %s" % arc)
    print("entries     : %d" % (len(files) + 1))
    print("uncompressed: %d bytes" % total)
    print("file        : %d bytes" % os.path.getsize(arc))
    print("sha256      : %s" % h)
    print("unzip -t    : no errors")


def main():
    label = sys.argv[1] if len(sys.argv) > 1 else \
        datetime.date.today().strftime("%Y%m%d")
    build(label, ROOT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
