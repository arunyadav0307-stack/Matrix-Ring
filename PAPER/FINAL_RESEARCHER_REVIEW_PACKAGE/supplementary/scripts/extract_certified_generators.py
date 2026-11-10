#!/usr/bin/env python3
"""
extract_certified_generators.py
===============================

Supplementary script for the manuscript

    "Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
     over Noncommutative Matrix Rings".

WHAT IT DOES
------------
It re-runs the *deterministic* parts of the Phase-7 search that produce the
28 certified codes of Appendix A (the census, the family scan, and the
certification stage), and writes, for each certified code, a JSON file
containing

    * the family (q,t,n) and the route (SO / DC / EA),
    * the Gray-image generator matrix  A  (a k x N matrix over F_q) of the
      image code D = phi_n(C),
    * a generator matrix of the Euclidean dual D^{perp_E},
    * the invariants (k, h_E, K, d, c) and the status of the distance.

The script does not re-implement anything: it imports
`phase7_extended_search` and calls, in the same order as that script's own
`main()`, the functions `part2_census()`, `part3_search()` and
`part6_certification()`.  The pseudo-random sampling is driven by the same
`SEED` and by a single `random.Random(SEED)` instance consumed in the same
order, so the codes produced here are the very codes whose parameters appear
in the committed log `phase7_extended_search_log.txt`.

The generator matrices are the *image* generators produced by
`P4.img_basis`, i.e. the rows of A span D = phi_n(C) as an F_q-subspace of
F_q^N.  Elements of F_q are written as integers 0..q-1 in the internal
ordering of `matrix_ring_lib`; see that file for the encoding.

WHY THE MATRICES ARE CARRIED THROUGH, NOT RE-SELECTED
-----------------------------------------------------
An earlier version of this project certified a *re-selected* code with the
same invariants instead of the code the search had actually found.  That
defect was found and fixed: `part6_certification` receives the row produced
by `part3_search`, whose key "A" is the image basis of the exact code.  This
script serialises that same object.

USAGE
-----
    cd PAPER/supplementary/scripts
    python3 extract_certified_generators.py [outdir]

`outdir` defaults to ../generator_matrices.  The script needs the repository
scripts directory (04_COMPUTATION) on the path; it locates it automatically
relative to this file, or via the environment variable MATRIX_RING_COMP.

Runtime: about 6-8 minutes, about 400 MB RSS.  Pure Python standard library.
"""

import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def find_comp():
    env = os.environ.get("MATRIX_RING_COMP")
    if env and os.path.isdir(env):
        return env
    here = HERE
    for _ in range(8):
        cand = os.path.join(here, "04_COMPUTATION")
        if os.path.isdir(cand) and os.path.exists(
                os.path.join(cand, "phase7_extended_search.py")):
            return cand
        here = os.path.dirname(here)
    raise SystemExit("cannot locate 04_COMPUTATION/ ; set MATRIX_RING_COMP")


COMP = find_comp()
sys.path.insert(0, COMP)

import phase7_extended_search as P7          # noqa: E402


def code_name(r):
    q, N, kind = r["q"], r["N"], r["kind"]
    if kind == "EA":
        return "[[%d,%d,%s;%d]]_%d" % (N, r["K"], r["d"], r["c"], q)
    return "[[%d,%d,%s]]_%d" % (N, r["K"], r["d"], q)


def safe(s):
    return (str(s).replace("[", "").replace("]", "")
            .replace(";", "-").replace(",", "_").replace(" ", ""))


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, "..", "generator_matrices")
    outdir = os.path.abspath(outdir)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    sys.stderr.write("extract_certified_generators: importing %s\n" % COMP)
    sys.stderr.write("seed = %d\n" % P7.SEED)
    sys.stderr.write("running PART 2 (census) ...\n")
    sys.stderr.flush()

    rng = random.Random(P7.SEED)
    table = P7.part2_census()
    counts = {}
    for row in table:
        if row[2] is not None:
            counts[row[0]] = row[2]

    sys.stderr.write("running PART 3 (family scan) ...\n")
    sys.stderr.flush()
    all_rows, all_stats = P7.part3_search(rng, counts)

    sys.stderr.write("running PART 6 (certification) ...\n")
    sys.stderr.flush()
    picks = P7.part6_certification(all_rows)

    sys.stderr.write("writing %d generator matrices to %s\n"
                     % (len(picks), outdir))
    index = []
    for i, r in enumerate(picks):
        name = code_name(r)
        fn = "%02d_%s_(%d,%d,%d)_%s.json" % (
            i + 1, safe(name), r["q"], r["t"], r["n"], r["kind"])
        rec = {
            "index": i + 1,
            "code": name,
            "q": r["q"], "t": r["t"], "n": r["n"], "N": r["N"],
            "route": r["kind"],
            "k": r["k"], "K": r["K"], "d": r["d"], "c": r["c"],
            "h_E": r["hE"], "exact": bool(r["exact"]),
            "distance_method": r["method"],
            "generator_matrix_A": r["A"],
            "generator_matrix_Euclidean_dual": r["De"],
            "notes": ("rows of A span the Gray image D = phi_n(C) in F_q^N; "
                      "rows of the second matrix span D^{perp_E}.  Field "
                      "elements are integers 0..q-1 in the internal ordering "
                      "of matrix_ring_lib.py."),
        }
        with open(os.path.join(outdir, fn), "w") as fh:
            json.dump(rec, fh, indent=1)
        index.append({"file": fn, "code": name, "family":
                      [r["q"], r["t"], r["n"]], "route": r["kind"],
                      "k": r["k"], "K": r["K"], "d": r["d"], "c": r["c"],
                      "h_E": r["hE"], "exact": bool(r["exact"])})
    with open(os.path.join(outdir, "INDEX.json"), "w") as fh:
        json.dump({"script": os.path.basename(__file__),
                   "seed": P7.SEED,
                   "n_codes": len(index),
                   "codes": index}, fh, indent=1)
    sys.stderr.write("done\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
