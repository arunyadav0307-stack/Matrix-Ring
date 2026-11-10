#!/usr/bin/env python3
"""Minimal mktexlsr: write ls-R filename databases for a TeX Live tree.

This environment's TeX tree has no `mktexlsr` script (it lives in
texk/texlive/, not texk/kpathsea/), so the database is generated here.  The
format is exactly what kpathsea expects -- `ls -R` output with directory
headers:

    % ls-R -- filename database for kpathsea; do not change this line.

    ./:
    subdir
    file

    ./subdir:
    ...
"""
import os
import sys

SKIP = {'.git', '__pycache__'}


def blocks(tree):
    out = ["% ls-R -- filename database for kpathsea; do not change this line.",
           ""]
    for dirpath, dirnames, filenames in os.walk(tree):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        rel = os.path.relpath(dirpath, tree).replace(os.sep, '/')
        out.append("./" + ("" if rel == "." else rel + ":"))
        out.extend(sorted(dirnames))
        out.extend(sorted(filenames))
        out.append("")
    return "\n".join(out) + "\n"


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '/home/user/texlive2024'
    for t in sys.argv[2:] or ['texmf-dist']:
        tree = os.path.join(root, t)
        open(os.path.join(tree, 'ls-R'), 'w').write(blocks(tree))
        print('wrote %s/ls-R' % tree)


if __name__ == '__main__':
    main()
