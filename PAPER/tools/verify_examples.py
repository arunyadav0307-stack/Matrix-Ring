#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_examples.py -- recompute the numeric claims of the worked examples.

The manuscript's Examples 1-13 each quote numbers (ring sizes, ideal
dimensions, submodule counts, hull dimensions, quantum parameters).  Every one
of those numbers comes from a Phase log, and every one was at some point
transcribed by hand.  This script recomputes the ones that are cheap enough to
recompute, from the same library the Phase scripts use, so that a reader (or a
later revision) can check the transcription instead of trusting it.

Checks performed
----------------
  ex:crt          (q,t,n)=(4,2,2)  # B-submodules of B^2 (= number of codes)
                                   dim m, dim m^2, dim ann_{B^2}(m)
  ex:witnessA     (q,t,n)=(9,2,3)  dim m, dim m^2, dim m^3, dim ann_{B^2}(m)
  ex:witnessB     (q,t,n)=(4,2,4)  dim m .. dim m^4,          dim ann_{B^2}(m)
  ex:nonreflexive (q,t,n)=(8,1,2)  # nonzero codes; # with sigma_2(C) = C
  tab:headline    every row: route bookkeeping (K, c, h_E) and the
                  entanglement-assisted Singleton defect
  tab:cert        every row against supplementary/parameter_tables/
                  certified_codes.csv, with the defect recomputed

Usage
-----
    python3 tools/verify_examples.py            # from anywhere
    python3 tools/verify_examples.py --fast     # skip the slow BFS checks

Exit status 0 if every check passes, 1 otherwise.

Requires only the repository's own scripts (no third-party packages).
"""

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.dirname(HERE)
SCRIPTS = os.path.join(PAPER, "supplementary", "scripts")
sys.path.insert(0, SCRIPTS)


def say(msg=""):
    print(msg)
    sys.stdout.flush()


def rec(results, name, got, want):
    ok = (got == want)
    results.append((name, ok, got, want))
    say("    %-46s got %-24s want %-14s %s"
        % (name, got, want, "OK" if ok else "*** MISMATCH ***"))
    return ok


# ==========================================================================
#  ring-theoretic checks  (ex:crt, ex:witnessA, ex:witnessB)
# ==========================================================================

def ring_checks(fast):
    import phase7_extended_search as P7          # noqa: F401
    from ring_structure_checks import rref, nullspace_basis

    def span(F, vecs, dim):
        if not vecs:
            return []
        R, _ = rref([list(v) for v in vecs], F, dim)
        return [tuple(x) for x in R]

    def ideal_closure(S, gens):
        F, D = S.F, S.dim
        eb = []
        for i in range(D):
            e = [0] * D
            e[i] = 1
            eb.append(tuple(e))
        rows = []
        for g in gens:
            for e in eb:
                rows.append(list(S.mul(g, e)))
        return span(F, rows, D)

    def dims_and_ann(crt, maxpow=8):
        S = crt.comps[0]
        F, D = S.F, S.dim
        g = crt.facs[0][0]                       # the irreducible factor
        gu = [0] * D
        for i, c in enumerate(g):
            gu[i] = c
        uv = [0] * D
        uv[S.L] = 1                              # the element u
        gens = [tuple(gu)] + ([tuple(uv)] if S.t > 1 else [])
        m = ideal_closure(S, gens)
        dims, cur = [], m
        while cur and len(dims) < maxpow:
            dims.append(len(cur))
            prods = []
            for a in cur:
                for b in m:
                    p = S.mul(a, b)
                    if any(p):
                        prods.append(p)
            cur = span(F, prods, D)
        rows = []
        for a in m:
            for pos in range(2):
                for k in range(D):
                    p = S.mul(a, tuple(1 if j == k else 0 for j in range(D)))
                    if any(p):
                        row = [0] * (2 * D)
                        for l in range(D):
                            if p[l]:
                                row[pos * D + l] = p[l]
                        rows.append(row)
        return dims, len(nullspace_basis(rows, F, 2 * D)), S.is_chain()

    out = []
    for (q, t, n, want_dims, want_ann, tag) in [
        (4, 2, 2, [3, 1], 2, "ex:crt      B = F_4[u,w]/(u^2,w^2)"),
        (9, 2, 3, [5, 3, 1], 2, "ex:witnessA B = F_9[u,w]/(u^2,w^3)"),
        (4, 2, 4, [7, 5, 3, 1], 2, "ex:witnessB B = F_4[u,w]/(u^2,w^4)"),
    ]:
        say("")
        say("  " + tag + "   at (q,t,n)=(%d,%d,%d)" % (q, t, n))
        crt = P7.crt_of(q, t, n)
        dims, ann, isch = dims_and_ann(crt)
        say("    components=%d, dim B=%d, is_chain=%s, regime=%s"
            % (len(crt.comps), crt.comps[0].dim, isch, crt.regime()))
        rec(out, "%s  dim m, dim m^2, ..." % tag, dims, want_dims)
        rec(out, "%s  dim ann_{B^2}(m)" % tag, ann, want_ann)

    if not fast:
        say("")
        say("  ex:crt  number of B-submodules of B^2 at (4,2,2)")
        crt = P7.crt_of(4, 2, 2)
        subs = P7.submodules_of_sq(crt.comps[0])
        rec(out, "ex:crt  # submodules (= # codes)", len(subs), 1221)

        say("")
        say("  ex:nonreflexive  (8,1,2): codes and sigma_2-stable codes")
        from ring_structure_checks import Field
        C = P7.instance(8, 1, 2).C
        F = C.F
        codes = P7.submodules_via_crt(C)
        say("    # codes enumerated (zero included): %d" % len(codes))
        sig2 = [F.frob[2 % F.r][a] for a in range(F.q)]
        ncols = 2 * C.B.dim

        def sigma2_code(rows):
            if not rows:
                return ()
            R, _ = rref([[sig2[x] for x in r] for r in rows], F, ncols)
            return tuple(tuple(x) for x in R)

        keys = [tuple(tuple(int(x) for x in r) for r in cd["rows"])
                for cd in codes]
        nonzero = [k for k in keys if k]
        stable = [k for k in nonzero if sigma2_code(list(k)) == k]
        rec(out, "ex:nonreflexive  # nonzero codes", len(nonzero), 92)
        rec(out, "ex:nonreflexive  # with sigma_2(C)=C", len(stable), 14)
    return out


# ==========================================================================
#  table checks  (tab:headline, tab:cert)
# ==========================================================================

def _parse_rows(path, label):
    tex = open(path, encoding="utf-8").read()
    blk = tex.split("\\label{%s}" % label)[1].split(r"\end{tabular}")[0]
    rows = []
    for ln in re.split(r"\\\\", blk):
        m = re.search(r"(\$\[\[.*)", ln, re.S)
        if not m:
            continue
        rows.append([c.strip() for c in m.group(1).strip().split("&")])
    return rows


def _num(x):
    return int(re.sub(r"[^0-9]", "", x))


def table_headline():
    rows = _parse_rows(os.path.join(PAPER, "sections", "08_certification.tex"),
                       "tab:headline")
    out = []
    say("")
    say("  tab:headline -- %d rows" % len(rows))
    for r in rows:
        code = r[0].strip("$").strip()
        fam = re.sub(r"\$|\s", "", r[1])
        route = r[2]
        k, hE, K, d, c, sd = [x.strip() for x in r[3:9]]
        N = int(re.match(r"\[\[(\d+)", code).group(1))
        kk, K_, c_, sd_ = int(k), int(K), int(c), int(sd)
        d_ = _num(d)
        hE_ = None if hE == "---" else int(hE)
        errs = []
        if N - K_ + c_ - 2 * (d_ - 1) != sd_:
            errs.append("S-def %d != %d" % (N - K_ + c_ - 2 * (d_ - 1), sd_))
        if route.startswith("R2-SO"):
            if K_ != N - 2 * kk:
                errs.append("K != N-2k")
            if hE_ != kk:
                errs.append("h_E != k")
            if c_:
                errs.append("c != 0")
        elif route.startswith("R2-DC"):
            if K_ != 2 * kk - N:
                errs.append("K != 2k-N")
            if hE_ != N - kk:
                errs.append("h_E != N-k")
            if c_:
                errs.append("c != 0")
        elif route == "R3":
            if K_ != N - kk - hE_:
                errs.append("K != N-k-h_E")
            if c_ != kk - hE_:
                errs.append("c != k-h_E")
        elif route == "R1":
            if K_ != N - kk:
                errs.append("K != N-k")
            if c_:
                errs.append("c != 0")
        rec(out, "tab:headline %-18s %-8s" % (code, fam),
            "consistent" if not errs else "; ".join(errs), "consistent")
    return out


def table_cert():
    import csv
    rows = _parse_rows(os.path.join(PAPER, "sections", "appendix_tables.tex"),
                       "tab:cert")
    csvp = os.path.join(PAPER, "supplementary", "parameter_tables",
                        "certified_codes.csv")
    cert = list(csv.DictReader(open(csvp)))
    out = []
    say("")
    say("  tab:cert -- %d rows against %s" % (len(rows), os.path.basename(csvp)))
    rec(out, "tab:cert  row count", len(rows), len(cert))
    for r, c in zip(rows, cert):
        code = r[0].strip("$").strip()
        fam = re.sub(r"\$|\s", "", r[1])
        route, k, K, d, cc, sd = [x.strip() for x in r[2:8]]
        N = int(c["N"])
        errs = []
        if code != c["code"]:
            errs.append("code")
        if fam != "(%s,%s,%s)" % (c["q"], c["t"], c["n"]):
            errs.append("family")
        for name, got, want in (("route", route, c["route"]), ("k", k, c["k"]),
                                ("K", K, c["K"]), ("d", d, c["d"]),
                                ("c", cc, c["c"]),
                                ("S-def", sd, c["EA_Singleton_defect"])):
            if got != want:
                errs.append("%s %s != %s" % (name, got, want))
        if N - int(c["K"]) + int(c["c"]) - 2 * (int(c["d"]) - 1) != \
                int(c["EA_Singleton_defect"]):
            errs.append("S-def recompute")
        rec(out, "tab:cert %-18s %-8s" % (code, fam),
            "consistent" if not errs else "; ".join(errs), "consistent")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true",
                    help="skip the two slower exhaustive checks "
                         "(the (4,2,2) submodule BFS and the (8,1,2) scan)")
    args = ap.parse_args()

    say("=" * 92)
    say("VERIFICATION OF THE WORKED EXAMPLES AND THE PARAMETER TABLES")
    say("=" * 92)
    res = []
    res += ring_checks(args.fast)
    res += table_headline()
    res += table_cert()

    bad = [r for r in res if not r[1]]
    say("")
    say("=" * 92)
    say("CHECKS: %d     mismatches: %d" % (len(res), len(bad)))
    for name, _ok, got, want in bad:
        say("   MISMATCH  %s : got %s, want %s" % (name, got, want))
    say("=" * 92)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
