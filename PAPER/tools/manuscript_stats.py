#!/usr/bin/env python3
"""
manuscript_stats.py -- word / theorem / example / reference counts.

  python3 tools/manuscript_stats.py

Reports, for the manuscript rooted at main.tex:
  * files and total lines
  * word count of the prose (comments, macros and table markup excluded,
    as far as a regular expression can)
  * number of theorem-like environments, split by kind
  * number of \\cite keys (distinct) and bibliography entries
  * number of \\input files
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

THEM = ("theorem", "proposition", "lemma", "corollary", "definition",
        "example", "remark", "conjecture", "openproblem", "assumption")


def strip_comments(t):
    out = []
    for line in t.split("\n"):
        buf, i = [], 0
        while i < len(line):
            if line[i] == "%" and not (i and line[i - 1] == "\\"):
                break
            buf.append(line[i])
            i += 1
        out.append("".join(buf))
    return "\n".join(out)


def files_of(root):
    seen, order, missing = set(), [], []
    stack = ["main.tex"]
    while stack:
        f = stack.pop()
        if f in seen:
            continue
        seen.add(f)
        order.append(f)
        p = os.path.join(root, f)
        if not os.path.exists(p):
            missing.append(f)
            continue
        t = strip_comments(open(p, encoding="utf-8").read())
        for m in re.finditer(r"\\input\{([^}]*)\}", t):
            g = m.group(1).strip()
            if not g.endswith(".tex"):
                g += ".tex"
            if g not in seen:
                stack.append(g)
    return order, missing


def words(t):
    t = strip_comments(t)
    # drop the preamble of main.tex
    if "\\begin{document}" in t:
        t = t.split("\\begin{document}", 1)[1]
    # drop verbatim blocks
    t = re.sub(r"\\begin\{verbatim\*?\}.*?\\end\{verbatim\*?\}", " ", t,
               flags=re.S)
    # drop math
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}.*?"
               r"\\end\{\1\*?\}", " ", t, flags=re.S)
    # drop table rows (they are data, counted separately)
    t = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", " ", t, flags=re.S)
    # drop remaining macros, keeping their brace arguments as words
    t = re.sub(r"\\[A-Za-z@]+\*?(\[[^\]]*\])?", " ", t)
    t = re.sub(r"[{}&\\\\]", " ", t)
    return len([w for w in t.split() if re.search(r"[A-Za-z0-9]", w)])


def main():
    order, missing = files_of(ROOT)
    total_lines = 0
    total_words = 0
    per = []
    for f in order:
        t = open(os.path.join(ROOT, f), encoding="utf-8").read()
        total_lines += len(t.split("\n"))
        w = words(t)
        total_words += w
        per.append((f, len(t.split("\n")), w))

    counts = dict((k, 0) for k in THEM)
    cites = set()
    labels = set()
    for f in order:
        t = strip_comments(open(os.path.join(ROOT, f), encoding="utf-8").read())
        for k in THEM:
            counts[k] += len(re.findall(r"\\begin\{%s\*?\}" % k, t))
        for m in re.finditer(r"\\cite\{([^}]*)\}", t):
            for c in m.group(1).split(","):
                cites.add(c.strip())
        labels |= set(re.findall(r"\\label\{([^}]*)\}", t))

    bib = open(os.path.join(ROOT, "references.bib"), encoding="utf-8").read()
    keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)

    thm_total = sum(counts[k] for k in
                    ("theorem", "proposition", "lemma", "corollary"))
    print("=" * 70)
    print("MANUSCRIPT STATISTICS")
    print("=" * 70)
    print("  input files (incl. main.tex)   : %d" % len(order))
    print("  total lines of .tex            : %d" % total_lines)
    print("  words of prose (approx.)       : %d" % total_words)
    print("-" * 70)
    for k in THEM:
        print("  %-14s : %d" % (k, counts[k]))
    print("-" * 70)
    print("  theorem-like statements        : %d" % thm_total)
    print("  examples                       : %d" % counts["example"])
    print("  labels                         : %d" % len(labels))
    print("  distinct citation keys used    : %d" % len(cites))
    print("  bibliography entries           : %d" % len(keys))
    print("  entries cited                  : %d"
          % len([k for k in keys if k in cites]))
    if missing:
        print("  MISSING FILES                  : %s" % ", ".join(missing))
    print("=" * 70)
    print()
    for f, ln, w in per:
        print("  %-36s %5d lines  %6d words" % (f, ln, w))
    return 0


if __name__ == "__main__":
    sys.exit(main())
