#!/usr/bin/env python3
"""
build_parameter_tables.py
=========================

Build the machine-readable CSV tables of
PAPER/supplementary/parameter_tables/ by PARSING the committed computation
log, not by transcribing it by hand.  Every row therefore carries the line
number of the log it came from.

Usage:  python3 tools/build_parameter_tables.py
"""

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
LOG = os.path.join(ROOT, "supplementary", "logs",
                   "phase7_extended_search_log.txt")
OUT = os.path.join(ROOT, "supplementary", "parameter_tables")


def readlines(p):
    with open(p) as fh:
        return fh.read().split("\n")


def write(name, header, rows):
    path = os.path.join(OUT, name)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print("  %-34s %4d rows" % (name, len(rows)))


def section(lines, start_pat, end_pat=None, start_after=0):
    s = None
    for i, l in enumerate(lines):
        if s is None and re.search(start_pat, l):
            s = i + start_after
        elif s is not None and end_pat and re.search(end_pat, l):
            return s, i
    return (s, len(lines)) if s is not None else (0, 0)


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    lines = readlines(LOG)
    print("parsing %s (%d lines)" % (LOG, len(lines)))

    # ---------------------------------------------------------- census ----
    a, b = section(lines, r"^PART 2\.", r"^PART 3\.")
    rows = []
    pat = re.compile(r"^\s+\((4|8|9),(\d+),(\d+)\)\s*\|\s*([^|]*)\|\s*([^|]*)"
                     r"\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)"
                     r"\|\s*([^|]*)\|(.*)$")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        method = m.group(11).strip()
        method = re.sub(r"\s*\[\d+s\]", "", method).strip()
        rows.append([m.group(1), m.group(2), m.group(3),
                     m.group(4).strip(), m.group(7).strip(),
                     m.group(9).strip(), method, i + 1])
    write("family_census.csv",
          ["q", "t", "n", "N", "regime", "n_codes_or_dash", "method",
           "log_line"], rows)

    # ------------------------------------------------- family scan --------
    a, b = section(lines, r"^PART 3\.", r"^PART 4\.")
    rows = []
    pat = re.compile(r"^\s+\((4|8|9),(\d+),(\d+)\)\s*\|\s*(\d+)\s*\|\s*"
                     r"(\d+)\s*\(\s*(\S+)\s*\)\s*\|\s*(\d+)\s+(\d+)\s*\|\s*"
                     r"(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        rows.append([m.group(1), m.group(2), m.group(3), m.group(4),
                     m.group(5), m.group(6), m.group(7), m.group(8),
                     m.group(9), m.group(10), m.group(11), m.group(12),
                     i + 1])
    write("family_scan.csv",
          ["q", "t", "n", "N", "codes_enumerated", "codes_total", "SO", "DC",
           "EA_candidates", "distances_computed", "deep_searches", "best_d",
           "log_line"], rows)

    # -------------------------------------------- entanglement budget -----
    a, b = section(lines, r"^\s+d \| min c \| code", r"^\s+\(d\)")
    rows = []
    pat = re.compile(r"^\s+(\d+)\s*\|\s*(\d+)\s*\|\s*\[\[([0-9,;\s]+?)\]\]_(\d)"
                     r"\s*\|\s*\((\d+),(\d+),(\d+)\) N=(\d+)\s*\|\s*(\d+)\s+"
                     r"(\d+)\s*\|\s*(.+?)\s*$")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        rows.append([m.group(1), m.group(2), "[[%s]]_%s" % (m.group(3),
                     m.group(4)), m.group(5), m.group(6), m.group(7),
                     m.group(8), m.group(9), m.group(10), m.group(11), i + 1])
    write("entanglement_budget.csv",
          ["d", "min_c", "code", "q", "t", "n", "N", "k", "h_E", "method",
           "log_line"], rows)

    # ------------------------------------------------ pareto frontier -----
    a, b = section(lines, r"^\s+q t n  N \| kind", r"^\s+\(e\)")
    rows = []
    pat = re.compile(r"^\s+(\d)\s+(\d)\s+(\d)\s+(\d+)\s*\|\s*(SO|DC|EA)\s*\|"
                     r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*\|\s*(\S+)\s+(\S+)"
                     r"\s*\|\s*(\d+)\s*\|\s*(yes|>= \d+)")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        exact = m.group(13)
        d = m.group(8)
        rows.append([m.group(1), m.group(2), m.group(3), m.group(4),
                     m.group(5), m.group(6), m.group(7), d, m.group(9),
                     "exact" if exact == "yes" else
                     "proved lower bound d " + exact.replace(">= ", ">= "),
                     m.group(12), i + 1])
    write("pareto_frontier.csv",
          ["q", "t", "n", "N", "route", "k", "K", "d", "c", "distance_status",
           "EA_Singleton_defect", "log_line"], rows)

    # -------------------------------------------------- certification -----
    a, b = section(lines, r"PART 6\.\s+TASK E: INDEPENDENT CERTIFICATION",
                   r"^PART 6\.\s+TASK E: THE CHARACTERISTIC")
    rows = []
    pat = re.compile(r"^\s+\((\d+),(\d+),(\d+),\s*(\d+),(SO|DC|EA)\)\s*\|\s*"
                     r"(\d+)\s+(\d+)\s+(\S+)\s+(\d+)\s*\|\s*(\S+)\s*\|\s*"
                     r"(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*"
                     r"(\d+)")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        d = m.group(8)
        if m.group(5) == "EA":
            code = "[[%s,%s,%s;%s]]_%s" % (m.group(4), m.group(7), d,
                                           m.group(9), m.group(1))
        else:
            code = "[[%s,%s,%s]]_%s" % (m.group(4), m.group(7), d,
                                        m.group(1))
        rows.append([code, m.group(1), m.group(2), m.group(3), m.group(4),
                     m.group(5), m.group(6), m.group(7), d, m.group(9),
                     m.group(10), m.group(11), m.group(12), m.group(13),
                     m.group(14), m.group(15), i + 1])
    write("certified_codes.csv",
          ["code", "q", "t", "n", "N", "route", "k", "K", "d", "c",
           "M1", "M2", "M3_lower_bound", "all_methods_agree",
           "F_p_abelian", "EA_Singleton_defect", "log_line"], rows)

    # ----------------------------------------------- non-principal --------
    a, b = section(lines, r"D3\.\s+NEW mu_B", r"^PART 6\.")
    rows = []
    pat = re.compile(r"^\s+\((\d+),(\d+),(\d+),(\d)\)\s*\|\s*(\d+)\s*\|\s*"
                     r"(\S+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*$")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        best = m.group(9)
        mm = re.search(r"dim Hull = (\d+), mu_B\(Hull\) = (\d+)", best)
        rows.append([m.group(1), m.group(2), m.group(3), m.group(4),
                     m.group(5), m.group(8),
                     mm.group(1) if mm else "", mm.group(2) if mm else "",
                     i + 1])
    write("nonprincipal_witnesses.csv",
          ["q", "t", "n", "s", "N", "n_W_with_mu_ge_3", "dim_Hull",
           "mu_B_of_Hull", "log_line"], rows)

    # ------------------------------------------ best-known comparison -----
    a, b = section(lines, r"^\s+code found here", r"^\s+the comparison is")
    rows = []
    pat = re.compile(r"^\s+\[\[([0-9,;\s]+?)\]\]_(\d)\s*\|\s*(SO|DC|EA)\s*\|\s*"
                     r"\[\[([0-9,\s]+?)\]\]_(\d)\s*\(([^)]*)\)\s*\|\s*(.+?)\s*$")
    for i in range(a, b):
        m = pat.match(lines[i])
        if not m:
            continue
        rows.append(["[[%s]]_%s" % (m.group(1), m.group(2)), m.group(3),
                     "[[%s]]_%s" % (m.group(4), m.group(5)),
                     m.group(6).strip(), m.group(7).strip(), i + 1])
    write("comparison_grassl_q4.csv",
          ["our_code", "route", "best_known", "bounds_lower_upper", "gap",
           "log_line"], rows)

    # ------------------------------- the q=9 rows retrieved by hand -------
    # codetables.de, retrieved 2026-11-04.  The site prints the PRIME in the
    # code label, so q=9 appears as [[N,K]]_3.
    q9 = [
        ["[[24,8,4]]_9", "SO", "[[24,8]]_9", "6..8", "2 below", ""],
        ["[[24,12,3]]_9", "DC", "[[24,12]]_9", "5..6", "2 below", ""],
        ["[[16,8,3]]_9", "DC", "[[16,8]]_9", "4..4", "1 below", ""],
    ]
    write("comparison_grassl_q9.csv",
          ["our_code", "route", "best_known", "bounds_lower_upper", "gap",
           "log_line"], q9)

    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
