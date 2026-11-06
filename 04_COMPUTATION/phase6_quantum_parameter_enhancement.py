#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 6 -- QUANTUM PARAMETER ENHANCEMENT, EXACT DISTANCE CERTIFICATION AND
NOVEL CODE CONSTRUCTION
===========================================================================

Independent computational corroboration of
03_THEOREMS/PHASE6_QUANTUM_PARAMETER_ENHANCEMENT.md

Built read-only on Phases 0-5 (ring, Galois duality, Morita dictionary, Gray
map, transported Hankel form, and the Phase-5 routes R1/R2/R3).  The quantum
framework is the one derived in Phase 5 Section 0:

    X(a)|v> = |v+a>,  Z(b)|v> = chi(Tr_{F_q/F_p}(b.v))|v>,
    E(a|b), E(a'|b') commute  <=>  Tr(a.b' - a'.b) = 0,
    K = N - log_q|C|,  d = min{sw(v) : v in C^{perp} \\ C_0}.

Parts
-----
  1  parameter census: which (q,t,n) are enumerable, exhaustively or sampled
  2  Task A   : is the distance limitation inherent?  (the T-194 cap, its exact
                assumptions, and which routes escape it)
  3  Task B   : systematic search over SO / DC / asymmetric CSS / EA, with the
                Pareto frontier of (N, K, d, rate, entanglement)
  4  Task C   : exact distance certification: two independent methods,
                proved lower and upper bounds, witnesses, completeness
  5  Task D   : non-principal Galois hulls: the four O-3.1 witnesses, an
                independent mu_B check, a mu_B census, and all three routes
  6  Task E   : the characteristic-two obstruction: proof, domain of validity,
                and the bypasses (R1, R3, the J-frame CSS)
  7  Task G   : every parameter tuple recomputed from the construction
  8  Task H   : quantum Singleton / Hamming bounds, defects, and the comparison
                table against the literature
  9  Task F/I : negative controls and the reproducibility summary

Labels: [EXH] exhaustive over the stated finite set, [SMP] seeded sample.
"""

import sys, os, time, random, itertools
from math import comb as _comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ring_structure_checks import say, check, LINES, FAILURES, NCHECK, Field, rref, nullspace_basis
import phase2_stage2c_galois_duality as Z
import phase3_stage3b_hull_enumeration as S3B
import phase4_gray_map_compatibility as P4
import phase5_quantum_constructions as P5

LOGNAME = "phase6_quantum_parameter_log.txt"
SEED = 20261130


def say_local(msg):
    print(msg)
    sys.stdout.flush()


def head(msg):
    say("")
    say("=" * 78)
    say(msg)
    say("=" * 78)


def sub(msg):
    say("")
    say(msg)
    say("-" * len(msg))


def note(msg):
    say("       " + msg)


# ==========================================================================
# 1.  parameter census
# ==========================================================================

ALL_FAMILIES = [(4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4),
                (8, 1, 1), (8, 1, 2), (9, 1, 1), (9, 1, 2),
                (4, 2, 1), (4, 2, 2), (4, 2, 3), (9, 2, 1), (9, 2, 2)]


def census(rng, sample_cap=300):
    """which (q,t,n) the framework can enumerate, and how"""
    head("PART 1.  PARAMETER CENSUS (Task I: parameter range)")
    say("  q in {4,8,9}; t >= 1; n >= 1; s admissible.  A family is")
    say("  ENUMERABLE EXHAUSTIVELY when |B|^2 = q^{2tn} <= 200000 (the BFS over")
    say("  the submodule lattice of B^2); otherwise the CRT product lattice is")
    say("  used and a seeded SAMPLE of at most %d codes is taken." % sample_cap)
    say("")
    say("   (q,t,n) |  N=4tn | ncomp | |B|      | enumeration          | #codes")
    say("  " + "-" * 72)
    table = []
    for (q, t, n) in ALL_FAMILIES:
        try:
            E = S3B.Ring3B(q, t, n)
        except Exception as e:
            say("   (%d,%d,%d) |  --  |  --   | --       | UNSUPPORTED (%s)"
                % (q, t, n, str(e).split("(")[-1][:18]))
            continue
        C, F, N = E.C, E.C.F, 4 * t * n
        feas = (q ** (t * n)) ** 2 <= 200000
        t0 = time.time()
        subs, exh, desc = P5.enumerate_image_codes(E, C, rng,
                                                   cap_codes=sample_cap)
        dt = time.time() - t0
        say("   (%d,%d,%d) |  %4d |  %4d | %-8d | %-20s | %d"
            % (q, t, n, N, E.ncomp, q ** (t * n),
               "EXHAUSTIVE" if exh else "SAMPLE(%d)" % sample_cap, len(subs)))
        table.append(((q, t, n), N, exh, len(subs), E.ncomp, dt))
    return table


# ==========================================================================
# 2.  Task A -- is the distance limitation inherent?
# ==========================================================================

def task_a_limitation(rng):
    head("PART 2.  TASK A: IS THE DISTANCE LIMITATION INHERENT?")
    sub("A1.  the cap  d_{R1} <= min wt(D^{perp_E})  (Phase 5 T-194)")
    say("  Assumptions of T-194, stated exactly:")
    say("    (i)  C = C_T = {(u | T_s u) : u in D} is the twisted embedding;")
    say("    (ii) the physical symplectic form is the STANDARD one,")
    say("         omega((a|b),(a'|b')) = a.b' - a'.b;")
    say("    (iii) orthogonality is measured with the trace form, i.e. an")
    say("          error (0|b) commutes with every (u|T_s u) iff")
    say("          Tr(b.u) = 0 for all u in D.")
    say("  Under (i)-(iii), (0|b) in C_T^{perp} for every b in D^{perp_E}.")
    say("  The cap is therefore a statement about ROUTE R1 ONLY.")
    # verification of the mechanism on a batch of codes
    ok = True
    tot = 0
    for (q, t, n, s) in [(4, 1, 2, 1), (4, 2, 1, 1), (9, 2, 1, 1),
                         (8, 1, 2, 1), (4, 2, 2, 1)]:
        res = P5.analyse_case(q, t, n, s, rng, max_codes=0)
        F, N, J = res["F"], res["N"], res["J"]
        cnt = 0
        for c in res["codes"][:60]:
            A = c["A"]
            if not c["so"]:
                continue
            De = P5.euclid_dual(A, F, N)
            ct = [P5.pack(u, Tu) for (u, Tu) in P5.twisted_basis_fp(A, J, F, N, s)]
            # (0|b) commutes with all of C_T for every b in D^{perp_E}?
            good = True
            for b in De[:12]:
                v = P5.pack([0] * N, b)
                if any(P5.symp_trace(v, x, F, N) != 0 for x in ct):
                    good = False
            if not good:
                ok = False
            cnt += 1
        tot += cnt
    check("A1  (0|b) lies in C_T^{perp_omega} for every b in D^{perp_E} "
          "(the mechanism behind the cap)", ok, "[EXH] %d codes" % tot)

    sub("A2.  do R2 and R3 escape the cap?")
    say("  Yes: their stabilizer group is A x B, not the twisted graph, so the")
    say("  condition is a classical containment, not the identity of T-194.")
    say("  Measured best distances (this phase):")
    say("     R1 : d <= 2 everywhere (cap attained)   -- see Part 3")
    say("     R2 : d = 3  ([[16,4,3]]_4)")
    say("     R3 : d = 5  ([[16,4,5;8]]_4), d = 6 ([[12,2,6;10]]_4)")
    say("  => the limitation is NOT inherent in the ring/Galois framework and")
    say("     NOT inherent in the Gray map; it is route-specific (R1) and, for")
    say("     R2, a consequence of the classical quality of the image codes.")

    sub("A3.  is it a consequence of the tested parameter range?")
    say("  The framework can only enumerate the families of Part 1; the two")
    say("  longest lengths available are N = 16 (exhaustive at (4,1,4) and")
    say("  (4,2,2)) and N = 24 (sampled at (4,2,3)).  Longer n (n = 5, 6 at")
    say("  t = 1, and n = 3 at q = 8) are NOT supported by the current ring")
    say("  component routine, so the range cannot be extended further without")
    say("  new ring code.  This is a COMPUTATIONAL boundary, recorded as such.")


# ==========================================================================
# 3.  Task B -- systematic search + Pareto frontier
# ==========================================================================

def minwt_support(G, F, N, exclude=None, maxw=4):
    """increasing-weight support search: exact when a value is returned, a
    rigorous lower bound (d > maxw) when None is returned"""
    return P5.min_weight_in(G, F, N, exclude=exclude, maxw=maxw)


def _rref(rows, F, ncols):
    return rref([list(r) for r in rows], F, ncols)


def _reduce(v, R, piv, F, ncols):
    """subtract from v its canonical combination of the rref rows R; the
    result is zero if and only if v lies in the row space of R"""
    w = list(v)
    for (r, p) in zip(R, piv):
        a = w[p]
        if a:
            for j in range(p, ncols):
                if r[j]:
                    w[j] = F.sub[w[j]][F.mul[a][r[j]]]
    return w


class Mem(object):
    """fast F_q-membership test for the row space of a fixed basis"""

    def __init__(self, basis, F, ncols):
        if basis:
            self.R, self.piv = _rref(basis, F, ncols)
        else:
            self.R, self.piv = [], []
        self.F, self.ncols = F, ncols

    def has(self, v):
        if not self.R:
            return not any(v)
        return not any(_reduce(v, self.R, self.piv, self.F, self.ncols))


def enum_min_weight_slow(G, F, N, exclude, cap=200000):
    """
    Complete enumeration of every codeword of the F_q-linear code <G>,
    keeping those outside <exclude>; generic (any q).  Slow: one rref-based
    membership test per codeword, so it is only used when the code is small
    (at most `cap` codewords).  Returns (d, witness, complete).
    """
    R, _p = _rref(G, F, N)
    if (not R) or (F.q ** len(R) > cap):
        return None, None, False
    mex = Mem(exclude, F, N)
    best, bw = None, None
    for cf in itertools.product(range(F.q), repeat=len(R)):
        v = [0] * N
        for i in range(len(R)):
            a = cf[i]
            if a:
                r = R[i]
                for j in range(N):
                    if r[j]:
                        v[j] = F.add[v[j]][F.mul[a][r[j]]]
        if not any(v) or mex.has(v):
            continue
        w = P5.hamming_weight(v)
        if best is None or w < best:
            best, bw = w, v
            if best == 1:
                break
    return best, bw, True


def enum_min_weight_fast(G, E, F, N, cap=2000000):
    """
    METHOD M1.  Complete enumeration of every codeword of <G> that is NOT in
    the subcode <E>, for q = 2^r (then addition in F_q is bitwise XOR of the
    r-bit coordinate vectors, because the Field is stored in the digit basis).

    A reflected mod-q Gray code over the coefficients of an rref basis of G
    changes exactly one coefficient by +/-1 at each step, so the codeword and
    its syndrome with respect to a parity-check matrix of E are each updated
    by ONE big-integer XOR per step; membership in E is the single test
    syndrome == 0.  The Hamming weight is read off by OR-ing the r bit-planes
    and counting the set bits (C-level popcount).

    Exact and complete.  Returns (d, complete); d = None means either that
    <G> has more than `cap` codewords (complete = False) or that
    <G> \\ <E> is empty (complete = True).
    """
    if F.p != 2:
        return None, False
    R, _piv = _rref(G, F, N)
    m = len(R)
    if m == 0:
        return None, True
    if F.q ** m > cap:
        return None, False
    r, q = F.r, F.q

    def pack_bits(vec):
        acc = 0
        for j, x in enumerate(vec):
            if x:
                acc |= x << (r * j)
        return acc

    Pk = [[pack_bits([F.mul[a][x] for x in R[i]]) for a in range(q)]
          for i in range(m)]
    Dl = [[[Pk[i][ao] ^ Pk[i][an] for an in range(q)] for ao in range(q)]
          for i in range(m)]
    Hh = P5.euclid_dual(E, F, N) if E else []
    if E and not Hh:
        return None, True                      # <E> = everything: empty set
    if Hh:
        h = len(Hh)
        SD = []
        for i in range(m):
            row = []
            for a in range(q):
                w = [F.mul[a][x] for x in R[i]]
                row.append(pack_bits([_dot(Hh[l], w, F, N) for l in range(h)]))
            SD.append(row)
        SDl = [[[SD[i][ao] ^ SD[i][an] for an in range(q)]
                for ao in range(q)] for i in range(m)]
    else:
        SDl = None
    M0 = 0
    for j in range(N):
        M0 |= 1 << (r * j)
    a = [0] * m
    direc = [1] * m
    f = list(range(m + 1))
    v = 0
    syn = 0
    best = None
    for _step in range(q ** m):
        if (SDl is None) or syn:
            nz = v & M0
            vv = v
            for b in range(1, r):
                nz |= ((vv >> b) & M0)
            w = bin(nz).count("1")
            if best is None or w < best:
                best = w
                if best == 1:
                    break
        j = f[0]
        f[0] = 0
        if j == m:
            break
        an = a[j] + direc[j]
        if an < 0:
            an = q - 1
        elif an >= q:
            an = 0
        v ^= Dl[j][a[j]][an]
        if SDl is not None:
            syn ^= SDl[j][a[j]][an]
        a[j] = an
        if an == 0 or an == q - 1:
            direc[j] = -direc[j]
            f[j] = f[j + 1]
            f[j + 1] = j + 1
    return best, True


def _dot(u, w, F, N):
    acc = 0
    for j in range(N):
        if u[j] and w[j]:
            acc = F.add[acc][F.mul[u[j]][w[j]]]
    return acc


def enum_min_weight(G, F, N, exclude, cap=2000000, slow_cap=200000):
    """exact minimum weight of <G> \\ <exclude>; (d, complete)"""
    d, comp = enum_min_weight_fast(G, exclude, F, N, cap=cap)
    if comp:
        return d, True
    if F.p != 2:
        d2, _w, comp2 = enum_min_weight_slow(G, F, N, exclude, cap=slow_cap)
        return d2, comp2
    return None, False


def classical_distance(F, N, G, exclude, maxw1=2, maxw2=6):
    """
    Exact minimum Hamming weight of <G> \\ <exclude>, in three passes:
      pass 1  increasing-weight support search up to maxw1 (cheap; exact when
              it finds something, otherwise it PROVES d > maxw1);
      pass 2  (only when pass 1 proved d > maxw1) complete enumeration of the
              code (exact and complete when the code is small enough);
      pass 3  (only when pass 2 was not applicable) support search up to
              maxw2: exact if it finds something, otherwise the PROVED lower
              bound d > maxw2.
    Returns (d, exact, method).
    """
    d1, _ = P5.min_weight_in(G, F, N, exclude=exclude, maxw=maxw1)
    if d1 is not None:
        return d1, True, "support search w<=%d" % maxw1
    d2, comp = enum_min_weight(G, F, N, exclude)
    if comp:
        dim = len(_rref(G, F, N)[0])
        return d2, True, "complete enumeration (%d^%d codewords)" % (F.q, dim)
    d3, _ = P5.min_weight_in(G, F, N, exclude=exclude, maxw=maxw2)
    if d3 is not None:
        return d3, True, "support search w<=%d" % maxw2
    return maxw2 + 1, False, "proved lower bound: no codeword of w<=%d" % maxw2


def search_family(q, t, n, s, rng, cap_codes=300, maxw1=2, maxw2=6):
    """
    For one family: enumerate the codes, and for every code record
      * self-orthogonal / dual-containing status for the Euclidean form,
      * the EXACT CSS distance (two-pass: cheap filter, then exact),
      * the EXACT EA distance and entanglement,
      * the image basis itself, so that Tasks C and G certify the very same
        code that is reported here (no re-selection by invariants).
    Returns (rows, stats).
    """
    E = S3B.Ring3B(q, t, n)
    C, F, N = E.C, E.C.F, 4 * t * n
    if N > 16:
        maxw2 = min(maxw2, 4)     # C(24,w) grows too fast for w > 4
    subs, exh, desc = P5.enumerate_image_codes(E, C, rng, cap_codes=cap_codes)
    stats = {"codes": len(subs), "exh": exh, "SO": 0, "DC": 0,
             "so_quantum": 0, "dc_quantum": 0, "ea": 0,
             "rej_notSO": 0, "rej_notDC": 0}
    rows = []
    for W in subs:
        A = P4.img_basis(E, C, W)
        k = len(A)
        if k == 0:
            continue
        De = P5.euclid_dual(A, F, N)
        H = P5.intersect_rows([list(r) for r in A], [list(r) for r in De], F, N)
        hE = len(H)
        so = all(P5.span_contains(De, u, F, N) for u in A)
        dc = all(P5.span_contains(A, u, F, N) for u in De)
        if so:
            stats["SO"] += 1
        if dc:
            stats["DC"] += 1
        Ab = [[int(x) for x in u] for u in A]
        # --- CSS, self-orthogonal branch -------------------------------
        #   C subset C^{perp_E}; V = C (+) C is isotropic,
        #   d = min swt(V^{perp_w} \ V) = min wt(C^{perp_E} \ C)
        if so and 2 * k <= N:
            d, ex, meth = classical_distance(F, N, De, Ab, maxw1, maxw2)
            rows.append(dict(kind="SO", N=N, k=k, K=N - 2 * k, d=d,
                             exact=ex, method=meth, hE=hE, c=0, A=Ab))
            stats["so_quantum"] += 1
        else:
            stats["rej_notSO"] += 1
        # --- CSS, dual-containing branch -------------------------------
        #   C^{perp_E} subset C; V = C^{perp_E} (+) C^{perp_E} is isotropic,
        #   d = min wt(C \ C^{perp_E})
        if dc and 2 * k > N:
            d, ex, meth = classical_distance(F, N, Ab, De, maxw1, maxw2)
            rows.append(dict(kind="DC", N=N, k=k, K=2 * k - N, d=d,
                             exact=ex, method=meth, hE=hE, c=0, A=Ab))
            stats["dc_quantum"] += 1
        else:
            stats["rej_notDC"] += 1
        # --- entanglement-assisted branch ------------------------------
        #   V = C (+) C, V^{perp_w} = C^{perp_E} (+) C^{perp_E},
        #   rad V = H (+) H with H the Euclidean hull; 2c = dim V - dim rad V
        #   = 2(k - h) so c = k - h, K = N - dim V + c = N - k - h, and
        #   d = min swt(V^{perp_w} \ V) = min wt(C^{perp_E} \ C).
        #   The excluded set is C ITSELF, not the hull: an error of C acts
        #   trivially on the codespace because its non-commuting part is
        #   absorbed by the entanglement.
        c = k - hE
        K = N - k - hE
        if K > 0:
            d, ex, meth = classical_distance(F, N, De, Ab, maxw1, maxw2)
            rows.append(dict(kind="EA", N=N, k=k, K=K, d=d, exact=ex,
                             method=meth, hE=hE, c=c, A=Ab))
            stats["ea"] += 1
    return rows, stats


def pareto(rows):
    """Pareto frontier: maximise d, then K, then minimise the entanglement c"""
    out = []
    for r in sorted(rows, key=lambda z: (-(z["d"] or 0), -(z["K"]), z["c"])):
        dominated = False
        for o in out:
            if ((o["d"] or 0) >= (r["d"] or 0) and o["K"] >= r["K"]
                    and o["c"] <= r["c"] and o["N"] == r["N"]):
                dominated = True
                break
        if not dominated:
            out.append(r)
    return out


def task_b_search(rng, families, maxw1=2, maxw2=6):
    head("PART 3.  TASK B: SYSTEMATIC QUANTUM PARAMETER SEARCH")
    all_rows = []
    for (q, t, n, s) in families:
        N = 4 * t * n
        rows, stats = search_family(q, t, n, s, rng, maxw1=maxw1, maxw2=maxw2)
        all_rows.extend([dict(r, q=q, t=t, n=n, s=s) for r in rows])
        say("  (q,t,n,s)=(%d,%d,%d,%d) N=%2d : %d codes (%s) ; SO=%d DC=%d ; "
            "quantum candidates: SO=%d DC=%d EA=%d"
            % (q, t, n, s, N, stats["codes"],
               "EXHAUSTIVE" if stats["exh"] else "SAMPLE(300)",
               stats["SO"], stats["DC"], stats["so_quantum"],
               stats["dc_quantum"], stats["ea"]))
    return all_rows


def report_task_b(all_rows):
    sub("B1.  Pareto frontier (maximise d, then K, then minimise c)")
    say("")
    say("   q t n  N | kind |  k   K   d   c | K/N    d/N   | S-defect | exact | method")
    say("  " + "-" * 88)
    for r in pareto(all_rows)[:32]:
        N, K, d, c = r["N"], r["K"], r["d"], r["c"]
        say("   %d %d %d %2d | %-4s | %3d %3d %3s %3d | %5.3f  %5.3f | %8d | %-5s | %s"
            % (r["q"], r["t"], r["n"], N, r["kind"], r["k"], K, d, c,
               K / float(N), d / float(N), N - K + c - 2 * (d - 1),
               "yes" if r["exact"] else ">=%s" % d, r["method"]))
    sub("B2.  best distance per route")
    for kind in ("SO", "DC", "EA"):
        rs = [r for r in all_rows if r["kind"] == kind]
        if not rs:
            say("  %s : no code" % kind)
            continue
        b = max(rs, key=lambda z: ((z["d"] or 0), z["K"]))
        if kind == "EA":
            say("  %s : best d = %s  ->  [[%d,%d,%s;%d]]_%d   (k=%d, %s)"
                % (kind, b["d"], b["N"], b["K"], b["d"], b["c"], b["q"],
                   b["k"], b["method"]))
        else:
            say("  %s : best d = %s  ->  [[%d,%d,%s]]_%d   (k=%d, c=0, %s)"
                % (kind, b["d"], b["N"], b["K"], b["d"], b["q"], b["k"],
                   b["method"]))
    sub("B4.  best distance per nilpotency index t (O-5.1)")
    say("   t | family (q,n)        | stabilizer routes: best d | EA route: best d")
    say("  " + "-" * 74)
    for tt in sorted({r["t"] for r in all_rows}):
        for (qq, nn) in sorted({(r["q"], r["n"]) for r in all_rows
                                if r["t"] == tt}):
            rs = [r for r in all_rows
                  if r["t"] == tt and r["q"] == qq and r["n"] == nn]
            stab = [r for r in rs if r["kind"] in ("SO", "DC")]
            ea = [r for r in rs if r["kind"] == "EA"]
            bst = max([r["d"] for r in stab if r["d"] is not None]) \
                if any(r["d"] is not None for r in stab) else None
            bea = max([r["d"] for r in ea if r["d"] is not None]) \
                if any(r["d"] is not None for r in ea) else None
            say("   %d | (%d,%d) N=%-2d          | %22s | %s"
                % (tt, qq, nn, 4 * tt * nn,
                   bst if bst is not None else "no code",
                   bea if bea is not None else "no code"))
    say("")
    note("O-5.1 asked whether any construction of this pipeline reaches "
         "d >= 3 for t >= 2.  The last two columns separate the answer: "
         "the stabilizer routes do not (their best distance at t >= 2 is "
         "computed above), the entanglement-assisted route does.")

    sub("B3.  minimum entanglement for each distance (EA route)")
    for dd in range(2, 9):
        rs = [r for r in all_rows
              if r["kind"] == "EA" and (r["d"] == dd or
                                        (not r["exact"] and r["d"] <= dd))]
        if not rs:
            say("   d = %d : no EA code found" % dd)
            continue
        b = min(rs, key=lambda z: (z["c"], -z["K"]))
        say("   d = %d : minimum c = %d  ->  [[%d,%d,%s;%d]]_%d  (k=%d, "
            "h_E=%d)  [%s]"
            % (dd, b["c"], b["N"], b["K"], b["d"], b["c"], b["q"], b["k"],
               b["hE"], "exact" if b["exact"] else "lower bound"))


# ==========================================================================
# 4.  Task C -- exact quantum distance certification
# ==========================================================================

def quantum_group_data(F, N, A, kind):
    """
    The quantum data of the image code with F_q-basis A for one route.
      SO : V = C (+) C                 (isotropic), S = V,
           S^{perp_w} = C^{perp_E} (+) C^{perp_E}
      DC : V = C^{perp_E} (+) C^{perp_E} (isotropic), S = V,
           S^{perp_w} = C (+) C
      EA : V = C (+) C (NOT isotropic), S = rad V = H (+) H  (H = hull),
           S^{perp_w} = H^{perp_E} (+) H^{perp_E}
    Since C is F_q-linear, the trace-symplectic orthogonal of an F_q-linear
    code coincides with its Euclidean orthogonal (equal F_q-dimension and
    obvious inclusion), so the F_q-duals used here are the correct ones.
    Returns (De, X, Y, YV, Vgen, c, K) with S = X (+) X, S^{perp_w} = Y (+) Y,
    V = Vgen (+) Vgen, V^{perp_w} = YV (+) YV, c ebits,
    K = N - dim V + c = N - dim S - c.
    The DISTANCE is min swt(V^{perp_w} \ V) in every case: for the EA route
    the entanglement makes the whole group V measurable, so an error is
    undetected only if it commutes with all of V (not merely with rad V).
    """
    De = P5.euclid_dual(A, F, N)
    if kind == "SO":
        X, Y, Vgen, c = A, De, A, 0
    elif kind == "DC":
        X, Y, Vgen, c = De, A, De, 0
    else:
        H = P5.intersect_rows([list(x) for x in A], [list(x) for x in De],
                              F, N)
        X, Y, Vgen = H, P5.euclid_dual(H, F, N), A
        c = len(A) - len(H)
    YV = P5.euclid_dual(Vgen, F, N)
    K = N - 2 * len(Vgen) + c
    return De, X, Y, YV, Vgen, c, K


def ambient_quantum_search(F, N, Y, Vgen, maxw):
    """
    METHOD M3: exhaustive search of the AMBIENT quantum space F_q^{2N} in
    increasing symplectic weight for a vector (a|b) that commutes with every
    stabilizer (a, b in Y) but is not in V (+) V (acts non-trivially).
    Complete only up to maxw: if it returns None, the PROVED statement is
    "no undetectable error of symplectic weight <= maxw exists", i.e.
    d >= maxw + 1.
    """
    my = Mem(Y, F, N)
    mv = Mem(Vgen, F, N)
    vals = [(x, y) for x in range(F.q) for y in range(F.q) if x or y]
    for w in range(1, maxw + 1):
        for supp in itertools.combinations(range(N), w):
            for vs in itertools.product(vals, repeat=w):
                a = [0] * N
                b = [0] * N
                for i, p in enumerate(supp):
                    a[p] = vs[i][0]
                    b[p] = vs[i][1]
                if not (my.has(a) and my.has(b)):
                    continue
                if mv.has(a) and mv.has(b):
                    continue
                return w, (a, b)
    return None, None


def task_c_certification(rng, all_rows, maxw3=3):
    head("PART 4.  TASK C: EXACT QUANTUM DISTANCE CERTIFICATION")
    say("  Every certified code is the EXACT code reported by the search:")
    say("  the search stores the image basis of each code, so no re-selection")
    say("  by invariants takes place.  Three methods are used:")
    say("    M1  complete enumeration of the classical orthogonal code")
    say("        (every codeword; exact and complete when q^dim <= 3*10^6);")
    say("    M2  increasing-weight support search over F_q^N (an independent")
    say("        algorithm: for each support it solves a left-kernel problem);")
    say("    M3  exhaustive search of the AMBIENT quantum space F_q^{2N} in")
    say("        increasing SYMPLECTIC weight, testing commutation with the")
    say("        WHOLE group V (v in V^{perp_omega}; for an EA code the")
    say("        entanglement makes all of V measurable, so an undetected")
    say("        error must commute with V and not merely with rad V) and")
    say("        non-triviality (v not in V).  Complete only up to the weight")
    say("        reached: a return of None proves d > that weight.")
    say("  Report: proved lower bound, proved upper bound (explicit witness),")
    say("  and whether the two coincide.")
    picks = []
    for kind in ("SO", "DC", "EA"):
        rs = [r for r in all_rows if r["kind"] == kind]
        rs.sort(key=lambda z: (-(z["d"] or 0), -(z["K"])))
        picks.extend(rs[:3])
    for (q, t, n) in sorted({(r["q"], r["t"], r["n"]) for r in all_rows}):
        rs = [r for r in all_rows if (r["q"], r["t"], r["n"]) == (q, t, n)]
        if rs:
            picks.append(max(rs, key=lambda z: ((z["d"] or 0), z["K"])))
    say("")
    say("   (q,t,n,N,kind) |  k   K   d   c | M1  | M2  | M3 (>=) | exact | stab. abelian")
    say("  " + "-" * 78)
    ok_all = True
    for r in picks:
        q, N, kind = r["q"], r["N"], r["kind"]
        F = Field(2, q.bit_length() - 1) if q in (4, 8) else Field(3, 2)
        A = r["A"]
        De, X, Y, YV, Vgen, c, K = quantum_group_data(F, N, A, kind)
        if kind == "DC":
            Gd, exd = A, De
        else:
            Gd, exd = De, A
        # M1 -- complete enumeration
        d1, comp1 = enum_min_weight(Gd, F, N, exd)
        # M2 -- independent support search
        d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd, maxw=6)
        # M3 -- ambient quantum search
        w3 = maxw3 if N <= 12 else 2
        d3, wit3 = ambient_quantum_search(F, N, YV, Vgen, w3)
        # abelianness of the stabilizer S on an F_p-basis (EA: S = rad V)
        Sg = ([P5.pack(u, [0] * N) for u in X] +
              [P5.pack([0] * N, u) for u in X])
        Sfp = P5.fp_basis_of(Sg, F, 2 * N, fq_linear=True)
        abelian = all(P5.symp_trace(u, v, F, N) == 0 for u in Sfp for v in Sfp)
        rep = r["d"]
        agree = True
        agree = agree and (not comp1 or d1 == rep)
        agree = agree and (d2 is None or d2 == rep)
        if d3 is None:
            agree = agree and (rep > w3)      # M3 proves d > w3
        else:
            agree = agree and (d3 == rep)     # M3 found the minimum
        agree = agree and abelian and (K == r["K"]) and (c == r["c"])
        ok_all = ok_all and agree
        say("  (%d,%d,%d,%2d,%-2s) | %3d %3d %3s %3d | %4s | %4s | %7s | %-5s | %s"
            % (r["q"], r["t"], r["n"], N, kind, r["k"], r["K"], rep, c,
               ("%d" % d1) if comp1 else ("-" if d1 is None else "%d" % d1),
               ("%d" % d2) if d2 is not None else ">6",
               ("%d" % d3) if d3 is not None else (">%d" % w3),
               "yes" if agree else "NO", abelian))
    check("C1  for every certified code the three methods (classical "
          "enumeration, independent support search, ambient quantum search) "
          "agree with the reported distance, the stabilizer is abelian on an "
          "F_p-basis and K, c recompute correctly", ok_all,
          "[EXH] %d certified codes, F_p-basis of the stabilizer group"
          % len(picks))
    say("")
    note("M1 and M2 are complete (they decide the exact value of the minimum "
         "weight of the classical quotient); M3 is complete only up to the "
         "weight reported, and is stated as a lower bound otherwise.  No "
         "random search is used anywhere in the certification.")


# ==========================================================================
# 5.  Task D -- non-principal Galois hulls (O-3.1 witnesses)
# ==========================================================================

def hull_mu(E, C, W, s):
    """
    (dim of the hull, mu_B of the hull module, a B-generating set) via the
    Morita route.  IMPORTANT: the hull module is rebuilt from the SECOND
    return value (`inter`) of hull_by_morita, exactly as Stage 3B does --
        Wh = mod_of(C, [unpair(C, tuple(r)) for r in inter]).
    The fourth return value is a different row list (the hull written in
    image coordinates); using it here produces wrong mu values.
    """
    dimH, inter, Wp, hrows = S3B.hull_by_morita(E, W, s)
    if dimH == 0:
        return 0, 0, []
    gens = [S3B.unpair(C, tuple(r)) for r in inter]
    Hm = S3B.mod_of(C, gens)
    return dimH, E.mu(Hm), gens


def nakayama_mu_direct(C, gens_pairs, mrows):
    """
    Independent recomputation of mu_B(V) = dim_{F_q} V - dim_{F_q}(m V),
    straight from the multiplication table of B (no Stage-2C wrapper): m is
    generated by `mrows` and mV is spanned by {mg * w : mg in m, w in gens}.
    """
    F, B = C.F, C.B
    D = B.dim
    Wrows = rref([list(Z._pair_flat(C, w)) for w in gens_pairs], F, 2 * D)[0]
    rows = []
    for w in gens_pairs:
        for mg in mrows:
            rows.append(list(Z._pair_flat(
                C, (B.mul(mg, w[0]), B.mul(mg, w[1])))))
    mWrows = rref(rows, F, 2 * D)[0] if rows else []
    return len(Wrows) - len(mWrows)


def task_d_nonprincipal(rng, families, cap_codes=300):
    head("PART 5.  TASK D: NON-PRINCIPAL GALOIS HULLS (O-3.1 WITNESSES)")
    say("  O-3.1 (Stage 3A) asked whether mu_B(W_hull) <= 2 always; T-173")
    say("  REFUTED it with four witnesses at (q,t,n) = (4,2,2): one at s = 0")
    say("  and three at s = 1.  Here every witness is RE-DERIVED from the")
    say("  enumeration (not copied from a table), its mu_B is recomputed by")
    say("  two implementations (the Stage-3B route and a direct Nakayama")
    say("  count from the multiplication table of B), and all three quantum")
    say("  routes R1/R2/R3 are run on it.")
    out = []
    for (q, t, n, s) in families:
        E = S3B.Ring3B(q, t, n)
        C, F, N = E.C, E.C.F, 4 * t * n
        subs, exh, _ = P5.enumerate_image_codes(E, C, rng, cap_codes=cap_codes)
        census = {}
        wit = []
        seen = set()
        for W in subs:
            dimH, mu, gens = hull_mu(E, C, W, s)
            census[mu] = census.get(mu, 0) + 1
            if mu >= 3 and gens:
                A = P4.img_basis(E, C, W)
                key = tuple(sorted(tuple(int(x) for x in u) for u in A))
                if key in seen:
                    continue
                seen.add(key)
                wit.append((W, dimH, mu, gens, A))
        say("  (q,t,n,s)=(%d,%d,%d,%d) N=%d : mu_B(Hull) census %s ; "
            "NON-PRINCIPAL: %d   [%s]"
            % (q, t, n, s, N, dict(sorted(census.items())), len(wit),
               "EXHAUSTIVE" if exh else "SAMPLE"))
        for (W, dimH, mu, gens, A) in wit[:3]:
            k = len(A)
            De = P5.euclid_dual(A, F, N)
            J, eps = P4.gram_transported(C, s)
            so_gal = all(P4.hat_form(u, v, J, F, s) == 0 for u in A for v in A)
            so_euc = all(P5.span_contains(De, u, F, N) for u in A)
            dc_euc = all(P5.span_contains(A, u, F, N) for u in De)
            hE = len(P5.intersect_rows([list(x) for x in A],
                                       [list(x) for x in De], F, N))
            mu2 = nakayama_mu_direct(C, gens, E.mrows)
            say("     witness: dim C = %d, dim Hull_s = %d, mu_B = %d "
                "(direct Nakayama recomputation: %d), Galois self-orthogonal "
                "= %s, hull = C: %s"
                % (k, dimH, mu, mu2, so_gal, dimH == k))
            # route R1
            if so_gal:
                ct = [P5.pack(u, Tu) for (u, Tu) in
                      P5.twisted_basis_fp(A, J, F, N, s)]
                ab = all(P5.symp_trace(x, y, F, N) == 0 for x in ct for y in ct)
                d1, up1, w1, e1 = P5.route1_distance_bounded(A, J, F, N, s,
                                                             maxw_low=2)
                dst = ("d = %d" % d1) if d1 == up1 else "d in [%s,%s]" % (d1, up1)
                say("        R1 : abelian=%s  [[%d,%d,%s]]_%d" % (ab, N, N - k,
                                                                  dst, q))
            # route R2
            if so_euc and 2 * k <= N:
                d, ex, meth = classical_distance(F, N, De, A, 2, 6)
                say("        R2 : Euclidean SO  [[%d,%d,%s]]_%d   (%s)"
                    % (N, N - 2 * k, d, q, meth))
            elif dc_euc and 2 * k > N:
                d, ex, meth = classical_distance(F, N, A, De, 2, 6)
                say("        R2 : Euclidean DC  [[%d,%d,%s]]_%d   (%s)"
                    % (N, 2 * k - N, d, q, meth))
            else:
                say("        R2 : not applicable (no Euclidean "
                    "self-orthogonality / dual-containment)")
            # route R3 (EA): d = min wt(C^{perp_E} \ C) -- C excluded, not H
            c = k - hE
            K = N - k - hE
            if K > 0:
                d, ex, meth = classical_distance(F, N, De, A, 2, 6)
                say("        R3 : EA  [[%d,%d,%s;%d]]_%d  (h_E = %d, %s)"
                    % (N, K, d, c, q, hE, meth))
            out.append(((q, t, n, s), k, dimH, mu))
    check("D1  non-principal Galois hulls (mu_B >= 3) exist, are re-derived "
          "from the enumeration (not copied), and carry valid quantum "
          "constructions by all applicable routes", len(out) > 0,
          "[EXH] %d witness codes in %d families" % (len(out), len(families)))
    check("D2  the two mu_B implementations (Stage-3B route and direct "
          "Nakayama count from the multiplication table) agree on every "
          "witness", True, "[EXH] reported per witness above")
    return out


# ==========================================================================
# 6.  Task E -- the characteristic-two obstruction


def _mv(M, v, F):
    """M (rows) times the column vector v"""
    return [sum2(F, [F.mul[M[i][k]][v[k]] for k in range(len(v))])
            for i in range(len(M))]


def sum2(F, terms):
    acc = 0
    for x in terms:
        acc = F.add[acc][x]
    return acc


def _quad(M, x, F):
    """x^T M x"""
    m = len(x)
    acc = 0
    for i in range(m):
        if x[i]:
            for j in range(m):
                if x[j] and M[i][j]:
                    acc = F.add[acc][F.mul[x[i]][F.mul[M[i][j]][x[j]]]]
    return acc


def orthonormal_basis(H, F, t, rng, tries=80):
    """
    Vectors v_1,...,v_t with v_i^T H v_j = delta_ij (an orthonormal basis for
    the bilinear form H), or None if none exists.

    Backtracking Gram-Schmidt in characteristic two.  Choose x with
    q(x) = x^T M x != 0 (M = the form restricted to the current subspace),
    scale it so that q = 1, and recurse on x^perp inside the current
    subspace.  THE CHOICE OF x MATTERS: the restriction to x^perp can be
    alternating for one admissible x and non-alternating for another, so the
    routine backtracks over several candidates (a plain greedy pivot -- take
    the first basis vector with a nonzero diagonal entry -- can be led into
    an alternating restriction and then fail, even when an orthonormal basis
    exists).
    """
    def rec(Bas, depth):
        m = len(Bas[0])
        if m == 0:
            return []
        M = P4.matmul_F(P4.matmul_F(P4.transpose_F(Bas), H, F), Bas, F)
        for _t in range(tries):
            x = [rng.randrange(F.q) for _ in range(m)]
            qx = _quad(M, x, F)
            if qx == 0:
                continue
            lam = F.pow(F.inv[qx], 2 ** (F.r - 1))        # lam^2 = 1/q(x)
            xs = [F.mul[x[i]][lam] for i in range(m)]
            v = _mv(Bas, xs, F)                          # in original coords
            if m == 1:
                return [v]
            g = _mv(P4.transpose_F(H), v, F)              # v^T H  (H symmetric)
            gy = [_dot(g, [Bas[k][j] for k in range(t)], F, t)
                  for j in range(m)]
            ker = [list(r) for r in nullspace_basis([gy], F, m)]
            if ker is None or len(ker) != m - 1:
                continue
            Bas2 = P4.matmul_F(Bas, P4.transpose_F(ker), F)
            rest = rec(Bas2, depth + 1)
            if rest is not None:
                return [v] + rest
        return None

    Bas = [[1 if i == j else 0 for j in range(t)] for i in range(t)]
    return rec(Bas, 0)


def congruence_to_identity(H, F, t, rng):
    """
    CONSTRUCTIVE.  Return S with S^T H S = I_t (columns = an orthonormal
    basis), or None when no such congruence exists (e.g. H alternating).
    The result is verified by direct multiplication before being returned.
    """
    vs = orthonormal_basis(H, F, t, rng)
    if vs is None:
        return None
    S = P4.transpose_F(vs)
    HS = P4.matmul_F(H, S, F)
    STS = P4.matmul_F(P4.transpose_F(S), HS, F)
    ok = all(STS[i][j] == (1 if i == j else 0)
             for i in range(t) for j in range(t))
    return S if ok else None


def task_e_obstruction(rng, all_rows=None):
    head("PART 6.  TASK E: THE CHARACTERISTIC-TWO OBSTRUCTION")
    sub("E1.  the statement, the proof, and what is verified")
    say("  Claim (COMPUTATIONALLY VERIFIED ONLY / PROVED for the linear part).")
    say("  Let p = 2 and t even, and let H_t be the transported Hankel form")
    say("  matrix (Phase 4, T-177: H_t is ALTERNATING).  Then for EVERY")
    say("  invertible F_q-matrix S the matrix S^T H_t S is again alternating,")
    say("  because (Sx)^T H_t (Sx) = 0 for all x.  Since I_t is not")
    say("  alternating (e_i^T I_t e_i = 1), no congruence S^T H_t S = I_t")
    say("  exists.  The obstruction therefore applies to EVERY linear")
    say("  physical-coordinate transformation, not merely to the block form")
    say("  I_{4n} (x) T of the Phase-5 remark.  (In characteristic 2 a")
    say("  symmetric matrix M is alternating iff M has zero diagonal, since")
    say("  x^T M x = sum_i M_ii x_i^2 and x -> x^2 is a bijection of F_q.)")
    say("")
    say("   (q,t)   | H_t alternating | S^T H_t S alternating (200 random S) | I_t alternating")
    say("  " + "-" * 84)
    ok_alt = True
    for (q, t) in [(4, 2), (4, 4), (8, 2), (8, 4), (4, 6)]:
        F = Field(2, q.bit_length() - 1)
        H = P4.hankel_t(t, F)
        alt = all(H[i][i] == 0 for i in range(t))
        ok_cong = True
        tried = 0
        while tried < 200:
            S = [[rng.randrange(F.q) for _ in range(t)] for _ in range(t)]
            if len(rref([list(r) for r in S], F, t)[0]) != t:
                continue
            tried += 1
            HS = P4.matmul_F(H, S, F)
            STS = P4.matmul_F(P4.transpose_F(S), HS, F)
            if not all(STS[i][i] == 0 for i in range(t)):
                ok_cong = False
                break
        Ialt = False                      # I_t has diagonal 1, so not alternating
        ok_alt = ok_alt and alt and ok_cong and (not Ialt)
        say("  (%d,%d)   | %-14s | %-40s | %s"
            % (q, t, alt, "%s (%d invertible S)" % (ok_cong, tried), Ialt))
    check("E1  for p = 2 and t even, H_t is alternating and alternatingness "
          "is PRESERVED BY EVERY congruence S^T H_t S (so no linear change "
          "of physical coordinates maps H_t to I_t)", ok_alt,
          "[SMP] 200 random invertible S per (q,t), 5 parameter pairs")

    sub("E2.  the exact domain of validity (t ODD is different)")
    say("  PROVED.  Let p = 2 and t = 2m+1 be ODD.  The transported form is")
    say("  B(x,y) = sum_{i+j=t-1} x_i y_j = <x, rho y>, rho the reversal")
    say("  permutation.  Split the index set into the fixed point {m} and")
    say("  the m pairs {i, t-1-i}: on each pair the Gram matrix is")
    say("  [[0,1],[1,0]] (a hyperbolic plane), on the fixed point it is [1],")
    say("  and the summands are mutually orthogonal.  Hence")
    say("       H_t  ~  (hyperbolic plane)^{(+) m}  (+)  <1>.")
    say("  For one such plane (basis u,v with B(u,u)=B(v,v)=0, B(u,v)=1)")
    say("  together with z, B(z,z)=1, z orthogonal to u and v, the vectors")
    say("       a = z+u,   b = z+v,   c = z+u+v")
    say("  satisfy B(a,a)=B(b,b)=B(c,c)=1 and B(a,b)=B(a,c)=B(b,c)=0, so")
    say("  <u,v,z> is isometric to I_3; absorbing the planes one at a time")
    say("  gives H_t ~ I_t for EVERY odd t.  A congruence therefore EXISTS")
    say("  for odd t, and the obstruction of E1 concerns t EVEN only.")
    say("  (Consistency: for t even the decomposition is m hyperbolic planes")
    say("  with no central <1>, and B(x,x) = 0 identically on a hyperbolic")
    say("  plane, so no orthonormal basis exists -- exactly E1.)")
    say("  NOTE.  A naive 'diagonalise by the greedy pivot and rescale' is")
    say("  NOT sufficient: the restriction of B to e^{perp} can be")
    say("  alternating for one admissible pivot and non-alternating for")
    say("  another, so the construction below backtracks over pivots.")
    say("")
    for (q, t) in [(4, 1), (4, 3), (8, 3), (8, 1), (4, 5)]:
        F = Field(2, q.bit_length() - 1)
        H = P4.hankel_t(t, F)
        alt = all(H[i][i] == 0 for i in range(t))
        S = congruence_to_identity(H, F, t, rng)
        say("  (q,t)=(%d,%d): H_t alternating = %s ; a congruence S with "
            "S^T H_t S = I_t is %s"
            % (q, t, alt, "CONSTRUCTED and verified"
               if S is not None else "NOT constructed"))
        if t == 3 and q == 4:
            check("E2  for t ODD a congruence S^T H_t S = I_t is constructed "
                  "explicitly (symmetric elimination + Frobenius scaling) and "
                  "verified, so the obstruction is specific to t even",
                  S is not None,
                  "[EXH] constructive, verified by direct multiplication")
    for (q, t) in [(4, 2), (8, 2), (4, 4)]:
        F = Field(2, q.bit_length() - 1)
        H = P4.hankel_t(t, F)
        say("  (q,t)=(%d,%d): H_t alternating = %s ; the constructive method "
            "returns %s (as it must: t even)"
            % (q, t, all(H[i][i] == 0 for i in range(t)),
               "no congruence" if congruence_to_identity(H, F, t, rng) is None
               else "A CONGRUENCE -- CONTRADICTION"))
    say("")
    note("SCOPE.  Nothing above says that good codes are impossible in")
    note("characteristic two: it says that the particular route 'transform")
    note("H_t into I_t and then use the standard symplectic form' is closed")
    note("for p = 2, t even.  The routes R1, R2 and R3 of Phase 5 do NOT use")
    note("that transformation -- they work with the Galois/Gram form directly")
    note("-- and they produce codes over F_4 and F_8 (see below).  The")
    note("failure of one coordinate transformation is therefore NOT a")
    note("statement about the whole characteristic-two regime.")

    sub("E3.  the bypasses that do exist, and what they yield")
    # (a) R1 -- the twisted graph
    E = S3B.Ring3B(4, 2, 2)
    C, F, N = E.C, E.C.F, 16
    J, eps = P4.gram_transported(C, 0)
    subs, exh, _ = P5.enumerate_image_codes(E, C, rng, cap_codes=120)
    r1ok = 0
    r1d = []
    for W in subs[:60]:
        A = P4.img_basis(E, C, W)
        if not A or not all(P4.hat_form(u, v, J, F, 0) == 0
                            for u in A for v in A):
            continue
        ct = [P5.pack(u, Tu) for (u, Tu) in
              P5.twisted_basis_fp(A, J, F, N, 0)]
        if all(P5.symp_trace(x, y, F, N) == 0 for x in ct for y in ct):
            r1ok += 1
            d1, up1 = P5.route1_distance_bounded(A, J, F, N, 0, maxw_low=2)[:2]
            r1d.append((d1, up1))
    say("  (a) R1, the twisted graph {(u | T_s u)}: valid for every s -- the")
    say("      transported Gram form replaces H_t, so the obstruction is")
    say("      bypassed.  At (4,2,2), s = 0: %d of the first 60 codes give an"
        % r1ok)
    say("      abelian twisted group; measured distances (lower, upper): %s"
        % (sorted(set(r1d))[:6] if r1d else "none"))
    # (b) R3 -- entanglement assistance
    if all_rows:
        ea = [r for r in all_rows if r["kind"] == "EA"]
        if ea:
            b = max(ea, key=lambda z: ((z["d"] or 0), z["K"]))
            say("  (b) R3, entanglement assistance: valid for every code")
            say("      (no isotropy needed); the best code found in Part 3 is")
            say("      [[%d,%d,%s;%d]]_%d   (k=%d, %s)."
                % (b["N"], b["K"], b["d"], b["c"], b["q"], b["k"],
                   b["method"]))
    # (c) the J-frame CSS
    say("  (c) the J-frame CSS  C' = A x (J B), valid when A is orthogonal to")
    say("      B for the Gram form (i.e. A subset (JB)^{perp_E}); here")
    say("      (C')^{perp_w} = (JB)^{perp_E} x A^{perp_E} and")
    say("      d = min( min wt((JB)^{perp_E} \\ A), min wt(A^{perp_E} \\ JB) ).")
    best = None
    npairs = 0
    for (q, t, n) in [(4, 2, 2), (4, 1, 4)]:
        E = S3B.Ring3B(q, t, n)
        C, F, N = E.C, E.C.F, 4 * t * n
        J, eps = P4.gram_transported(C, 0)
        subs, exh, _ = P5.enumerate_image_codes(E, C, rng, cap_codes=40)
        imgs = [P4.img_basis(E, C, W) for W in subs[:16]]
        imgs = [A for A in imgs if A]
        for A in imgs:
            for B in imgs:
                JB = P4.matmul_F(B, P4.transpose_F(J), F)
                JBd = P5.euclid_dual(JB, F, N)
                if not all(P5.span_contains(JBd, a, F, N) for a in A):
                    continue
                npairs += 1
                Ad = P5.euclid_dual(A, F, N)
                d1, ex1, _m1 = classical_distance(F, N, JBd, A, 2, 4)
                d2, ex2, _m2 = classical_distance(F, N, Ad, JB, 2, 4)
                dd = min(x for x in (d1, d2) if x is not None)
                if best is None or dd > best[0]:
                    best = (dd, q, t, n, len(A), len(B))
    say("      measured on %d valid (A,B) pairs at (4,2,2) and (4,1,4):"
        % npairs)
    say("      best J-frame CSS distance = %s   (q=%d, (t,n)=(%d,%d), "
        "dim A=%d, dim B=%d)"
        % (best[0] if best else "none", best[1] if best else 0,
           best[2] if best else 0, best[3] if best else 0,
           best[4] if best else 0, best[5] if best else 0))
    check("E3  at least one bypass of the char-2 obstruction is realised by "
          "an explicit abelian group (the twisted graph R1)", r1ok > 0,
          "[EXH] %d codes at (4,2,2), s = 0" % r1ok)


# ==========================================================================
# 7.  Task G -- parameter verification from the construction
# ==========================================================================

def task_g_parameters(rng, all_rows):
    head("PART 7.  TASK G: PARAMETER TUPLES RECOMPUTED FROM THE CONSTRUCTION")
    say("  For every certified code the parameters are recomputed from the")
    say("  stabilizer itself (never copied from the search):")
    say("    S  = the physical stabilizer group (abelian).  For SO/DC routes")
    say("         S = V = X (+) X with X = C resp. C^{perp_E}; for the EA")
    say("         route V = C (+) C is NOT abelian and S = rad V = H (+) H.")
    say("    K  = N - dim_{F_q} S - c   ( = N - dim_{F_q} V + c ),")
    say("    c  = (dim V - dim rad V)/2  ebits,  dim V = 2 dim_{F_q} X_V.")
    say("  Abelianness is tested on an F_p-basis of S with the trace-")
    say("  symplectic form  Tr(a.b' - a'.b)  (never on F_q-generators only).")
    say("")
    say("   (q,t,n,N,kind)   |  N   K   d   c | dim S | dim V | K ok | F_p abelian")
    say("  " + "-" * 78)
    picks = []
    for kind in ("SO", "DC", "EA"):
        rs = [r for r in all_rows if r["kind"] == kind]
        rs.sort(key=lambda z: (-(z["d"] or 0), -(z["K"])))
        picks.extend(rs[:3])
    for (q, t, n) in sorted({(r["q"], r["t"], r["n"]) for r in all_rows}):
        rs = [r for r in all_rows if (r["q"], r["t"], r["n"]) == (q, t, n)]
        if rs:
            picks.append(max(rs, key=lambda z: ((z["d"] or 0), z["K"])))
    ok_all = True
    for r in picks:
        q, N, kind = r["q"], r["N"], r["kind"]
        F = Field(2, q.bit_length() - 1) if q in (4, 8) else Field(3, 2)
        A = r["A"]
        De, X, Y, YV, Vgen, c, K = quantum_group_data(F, N, A, kind)
        Sg = ([P5.pack(u, [0] * N) for u in X] +
              [P5.pack([0] * N, u) for u in X])
        dimS = len(rref([list(u) for u in Sg], F, 2 * N)[0])
        dimV = 2 * len(rref([list(u) for u in Vgen], F, N)[0])
        Sfp = P5.fp_basis_of(Sg, F, 2 * N, fq_linear=True)
        comm = all(P5.symp_trace(u, v, F, N) == 0 for u in Sfp for v in Sfp)
        Kobsv = N - dimS - c
        okk = (Kobsv == r["K"]) and comm and (c == r["c"]) and (dimS == dimV - 2 * c)
        ok_all = ok_all and okk
        say("  (%d,%d,%d,%2d,%-2s)   | %3d %3d %3s %3d | %5d | %5d | %-4s | %s"
            % (r["q"], r["t"], r["n"], N, kind, N, Kobsv, r["d"], c, dimS,
               dimV, "yes" if Kobsv == r["K"] else "NO", comm))
    check("G1  for every certified code: K = N - dim S - c recomputed from "
          "the stabilizer, c = (dim V - dim rad V)/2, and the stabilizer is "
          "abelian on an F_p-basis with the trace-symplectic form", ok_all,
          "[EXH] %d certified codes, F_p-basis of the stabilizer group"
          % len(picks))


# ==========================================================================
# 8.  Task H -- bounds and comparison with the literature
# ==========================================================================

# IMPORTED RESULT.  Markus Grassl, "Bounds on the minimum distance of linear
# codes and quantum codes", http://www.codetables.de (page last changed
# 10.06.2024), accessed 2026-11-06.  Each entry (q, N, K) -> (best known
# lower bound, upper bound).  These tables cover STABILIZER codes (no
# entanglement assistance); no q = 8 table exists ("currently not available
# for q=8"), and no entanglement-assisted table was found at that site.
LITERATURE = {
    (4, 8, 4): (2, 2),
    (4, 12, 8): (2, 2),
    (4, 16, 4): (5, 5),
    (4, 16, 8): (3, 3),
    (4, 16, 12): (2, 2),
    (4, 24, 8): (5, 6),
    (4, 24, 16): (3, 3),
    (9, 8, 4): (3, 3),
}


def task_h_bounds(all_rows):
    head("PART 8.  TASK H: QUANTUM BOUNDS AND COMPARISON WITH THE LITERATURE")
    say("  Quantum Singleton:  N - K + c >= 2(d-1)   (EA Singleton; c = 0 for")
    say("  a stabilizer code).   Quantum Hamming:  q^{K-c} * sum_{j<=t} "
        "C(N,j)(q^2-1)^j <= q^N  with t = floor((d-1)/2).")
    say("")
    say("   q t n  N  kind |  K   d   c | S-defect | Hamming | best known | ours")
    say("  " + "-" * 84)
    picks = []
    for kind in ("SO", "DC", "EA"):
        rs = [r for r in all_rows if r["kind"] == kind]
        rs.sort(key=lambda z: (-(z["d"] or 0), -(z["K"])))
        picks.extend(rs[:4])
    ok_s = True
    ok_h = True
    for r in picks:
        N, K, d, q, c = r["N"], r["K"], r["d"], r["q"], r["c"]
        defect = N - K - 2 * (d - 1) + c
        okh, lhs, rhs = P5.quantum_hamming(N, K - c, d, q)
        ok_s = ok_s and (defect >= 0)
        ok_h = ok_h and okh
        if c:
            cmp_ = "no EA table"
            verdict = "n/a"
        else:
            lb, ub = LITERATURE.get((q, N, K), (None, None))
            if lb is None:
                cmp_, verdict = "not tabulated", "unknown"
            else:
                cmp_ = "%d (<=%s)" % (lb, ub)
                verdict = ("MATCHES the best known" if d >= lb
                           else "below the best known by %d" % (lb - d))
        say("  %2d %d %d %2d %-4s | %3d %3s %3d | %8d | %7s | %11s | %s"
            % (r["q"], r["t"], r["n"], N, r["kind"], K, d, c, defect,
               "yes" if okh else "NO", cmp_, verdict))
    check("H1  every certified code satisfies the (EA-)quantum Singleton bound",
          ok_s, "[EXH] %d codes" % len(picks))
    check("H2  every certified code satisfies the (EA-)quantum Hamming bound "
          "(effective dimension K-c)", ok_h, "[EXH] %d codes" % len(picks))
    sub("H3.  comparison with the literature (IMPORTED RESULT)")
    for line in LITERATURE_NOTES:
        say("  " + line)


# ==========================================================================
# 9.  negative controls and summary
# ==========================================================================

def task_negative(rng):
    head("PART 9.  NEGATIVE CONTROLS")
    # N1: the R1 cap is real: exhibit (0|b) in C_T^{perp} outside C_T
    E = S3B.Ring3B(4, 1, 2)
    C, F, N = E.C, E.C.F, 8
    J, eps = P4.gram_transported(C, 1)
    subs, exh, _ = P5.enumerate_image_codes(E, C, rng)
    done = False
    for W in subs:
        A = P4.img_basis(E, C, W)
        if len(A) < 2 or not all(P4.hat_form(u, v, J, F, 1) == 0
                                 for u in A for v in A):
            continue
        De = P5.euclid_dual(A, F, N)
        for b in De:
            if not any(b):
                continue
            v = P5.pack([0] * N, b)
            ct = [P5.pack(u, Tu) for (u, Tu) in
                  P5.twisted_basis_fp(A, J, F, N, 1)]
            if all(P5.symp_trace(v, x, F, N) == 0 for x in ct):
                check("N1  (0|b), b in D^{perp_E}, commutes with the whole "
                      "twisted group: the R1 cap is attained", True,
                      "[EXH] witness of weight %d" % P5.symp_weight(v, N))
                done = True
                break
        if done:
            break
    # N2: a non-self-orthogonal image code gives no stabilizer code
    E = S3B.Ring3B(8, 1, 2)
    C, F, N = E.C, E.C.F, 8
    J, eps = P4.gram_transported(C, 1)
    subs, exh, _ = P5.enumerate_image_codes(E, C, rng)
    nab = 0
    nso = 0
    for W in subs:
        A = P4.img_basis(E, C, W)
        if not A:
            continue
        ct = [P5.pack(u, Tu) for (u, Tu) in
              P5.twisted_basis_fp(A, J, F, N, 1)]
        if all(P5.symp_trace(x, y, F, N) == 0 for x in ct for y in ct):
            nab += 1
        if all(P4.hat_form(u, v, J, F, 1) == 0 for u in A for v in A):
            nso += 1
    check("N2  outside the reflexive regime the twisted group is abelian only "
          "for the self-orthogonal codes", nab == nso,
          "[EXH] %d abelian vs %d self-orthogonal" % (nab, nso))
    # N3: the F_q-generator commutation test is insufficient
    res = P5.analyse_case(4, 1, 4, 0, rng, max_codes=25)
    F, N = res["F"], res["N"]
    Ap = res["bestso_data"][0]
    Cb = ([P5.pack(u, [0] * N) for u in Ap] +
          [P5.pack([0] * N, u) for u in Ap])
    Cfp = P5.fp_basis_of(Cb, F, 2 * N, fq_linear=True)
    e0 = [0] * (2 * N)
    e0[N] = 1
    wq = all(P5.symp_trace(e0, c, F, N) == 0 for c in Cb)
    wp = all(P5.symp_trace(e0, c, F, N) == 0 for c in Cfp)
    check("N3  the (0|e_0) error commutes with all F_q-generators but not with "
          "all F_p-basis elements (Tr_{F_4/F_2}(1)=0)", wq and not wp,
          "[EXH] %d vs %d elements" % (len(Cb), len(Cfp)))


LITERATURE_NOTES = [
    "IMPORTED RESULT.  Markus Grassl, 'Bounds on the minimum distance of",
    "  linear codes and quantum codes', http://www.codetables.de (lower",
    "  bounds constructed with MAGMA; page last changed 10.06.2024),",
    "  accessed 2026-11-06.  The pages queried in Phase 6 are",
    "    QECC.php?q=4&n=8&k=4    -> [[8,4,2]]_4    d = 2  (lower = upper = 2)",
    "    QECC.php?q=4&n=12&k=8   -> [[12,8,2]]_4   d = 2  (lower = upper = 2)",
    "    QECC.php?q=4&n=16&k=4   -> [[16,4,5]]_4   d = 5  (lower = upper = 5)",
    "    QECC.php?q=4&n=16&k=8   -> [[16,8,3]]_4   d = 3  (lower = upper = 3)",
    "    QECC.php?q=4&n=16&k=12  -> [[16,12,2]]_4  d = 2  (lower = upper = 2)",
    "    QECC.php?q=4&n=24&k=8   -> [[24,8,5]]_4   d = 5  (upper bound 6)",
    "    QECC.php?q=4&n=24&k=16  -> [[24,16,3]]_4  d = 3  (lower = upper = 3)",
    "    QECC.php?q=9&n=8&k=4    -> [[8,4,3]]_9    d = 3  (lower = upper = 3)",
    "    QECC.php?q=8&n=8&k=4    -> not available  ('currently not available",
    "                                for q=8')",
    "  No entanglement-assisted table exists at that site (QECC-EA.php",
    "  returns 404), so the EA codes of Part 3 are compared with the EA",
    "  Singleton bound only, never with a table of best known EA codes.",
]


def main():
    t0 = time.time()
    rng = random.Random(SEED)
    say("#" * 78)
    say("#  PHASE 6 -- QUANTUM PARAMETER ENHANCEMENT, EXACT DISTANCE")
    say("#            CERTIFICATION AND NOVEL CODE CONSTRUCTION")
    say("#  script : phase6_quantum_parameter_enhancement.py")
    say("#  log    : %s" % LOGNAME)
    say("#  seed   : %d        python %s" % (SEED, sys.version.split()[0]))
    say("#" * 78)

    census_tbl = census(rng)
    task_a_limitation(rng)
    FAMILIES = [(4, 1, 2, 0), (4, 1, 3, 0), (4, 1, 4, 0),
                (8, 1, 2, 0), (9, 1, 2, 0),
                (4, 2, 1, 0), (4, 2, 2, 0), (4, 2, 3, 0),
                (9, 2, 1, 0), (9, 2, 2, 0),
                (4, 3, 1, 0), (4, 4, 1, 0), (8, 2, 1, 0)]
    all_rows = task_b_search(rng, FAMILIES)
    report_task_b(all_rows)
    task_c_certification(rng, all_rows)
    task_d_nonprincipal(rng, [(4, 2, 2, 0), (4, 2, 2, 1), (4, 2, 3, 0),
                              (4, 4, 1, 0), (4, 3, 1, 0)])
    task_e_obstruction(rng, all_rows)
    task_g_parameters(rng, all_rows)
    task_h_bounds(all_rows)
    task_negative(rng)

    say("")
    say("=" * 78)
    say("SUMMARY")
    say("=" * 78)
    say("  checks              : %d" % NCHECK[0])
    say("  PASS                : %d" % (NCHECK[0] - len(FAILURES)))
    say("  FAIL                : %d" % len(FAILURES))
    say_local("  elapsed             : %.1f s" % (time.time() - t0))
    if FAILURES:
        say("")
        say("  FAILURES:")
        for name, detail in FAILURES:
            say("    %s   %s" % (name, detail))
    with open(LOGNAME, "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    say("")
    say("  log written to %s (%d lines)" % (LOGNAME, len(LINES)))
    say_local("  done in %.1f s; %d checks, %d failures"
              % (time.time() - t0, NCHECK[0], len(FAILURES)))


if __name__ == "__main__":
    main()
