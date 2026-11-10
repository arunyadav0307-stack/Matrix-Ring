"""
AUDIT SUPPORT 1:  is the TRACE-valued theta_s-pairing (used in the independent
re-implementation) the same duality as the MATRIX-valued theta_s-pairing used
by galois_duality_experiments.py?

    matrix-valued:   B_s(x,y) = sum_e theta_s(x_e) y_e          in R
    trace-valued:    b_s(x,y) = Lambda(B_s(x,y)) = tr(B_s(x,y)) in A

galois_duality_experiments.dual_of uses ALL m^2 components of B_s (see
pair_rows), i.e. the orthogonal of C is {y : B_s(x,y) = 0 as a matrix}.
The independent re-implementation orthogonalises against b_s, i.e. it uses
{y : tr B_s(x,y) = 0}.  These are a priori DIFFERENT sets.  This script
tests, exhaustively on enumerated cyclic codes, whether they coincide.

AUDIT SUPPORT 2 (for decision U9):  the semilinear isometry properties of
sigma_{2s}.  For every k, sigma_k commutes with the transpose and
Lambda(sigma_k M) = sigma_k Lambda(M), hence

    (E1)  B_s(sigma_k x, sigma_k y) = sigma_k( B_s(x,y) ),
    (E2)  B_s(x,y) = 0   <=>   B_s(sigma_k x, sigma_k y) = 0,
    (E3)  wt(sigma_k x) = wt(x)   (Hamming weight over the alphabet R),
    (E4)  sigma_k(C^perp_s) = (sigma_k C)^perp_s,
    (E5)  Hull_s(sigma_k C) = sigma_k( Hull_s(C) ),
    (E6)  (C^perp_s)^perp_s = sigma_{2s}(C)   [the double-dual theorem]

so all PARAMETER-LEVEL data attached to C^{perp perp} (size, dimension, weight
enumerator, minimum distance, hull dimension) is IDENTICAL to that of C even
when sigma_{2s} != id, i.e. even when the duality is NOT reflexive.
This script verifies E1-E6 on enumerated codes.

Run:  python3 -u audit_pairing_equivalence.py
"""

import importlib.util
import os
import random
import time

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "gd", os.path.join(HERE, "galois_duality_experiments.py"))
gd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gd)

from matrix_ring_lib import FiniteField, nullspace, row_space_basis


# --------------------------------------------------------------------------
def pair_trace(F, s, x, y, m, n):
    """b_s(x,y) = tr( sum_e theta_s(x_e) y_e )  -- a single F_q element"""
    return gd.mtrace(F, gd.pair_theta(F, s, x, y, m, n), m)


def dual_trace(F, basis, m, n, s):
    """orthogonal w.r.t. the TRACE-valued form"""
    N = n * m * m
    rows = []
    for x in basis:
        rows.append([pair_trace(F, s, x, gd.unit_vec(N, j), m, n)
                     for j in range(N)])
    ns = nullspace(F, rows, N)
    return row_space_basis(F, ns, N) if ns else []


def dual_matrix(F, basis, m, n, s):
    """orthogonal w.r.t. the MATRIX-valued form (the supplied definition)"""
    return gd.dual_of(F, basis, m, n, s, gd.pair_theta)


def hull_of(F, basis, m, n, s, dual_fn):
    """Hull(C) = C n C^perp, where C^perp = {y : B_s(c,y) = 0 for all c in C}.

    x = sum_i a_i c_i is in the hull iff  B_s(c_j, x) = 0 for every j, i.e.
    iff  sum_i a_i B_s(c_j, c_i) = 0.  Since B_s takes values in R = M_m(A)
    we impose all m^2 F_q-coordinates, i.e. a must lie in the nullspace of
    the (m^2 * |basis|) x |basis| matrix built from the rows of the F_q-linear
    maps y -> B_s(c_j, y).  (Taking the span of those basis vectors of C that
    happen to lie in C^perp is NOT correct.)"""
    N = n * m * m
    if not basis:
        return []
    G = []
    for c in basis:
        for r in gd.pair_rows(F, gd.pair_theta, c, m, n, s):
            G.append([dot(F, r, ci) for ci in basis])
    sols = nullspace(F, G, len(basis)) if G else [tuple(1 for _ in basis)]
    out = []
    for a in sols:
        v = [0] * N
        for coeff, c in zip(a, basis):
            if coeff:
                v = [F.add[v[i]][F.mul[coeff][c[i]]] for i in range(N)]
        if any(v):
            out.append(tuple(v))
    return row_space_basis(F, out, N) if out else []


def dot(F, row, vec):
    acc = 0
    for a, b in zip(row, vec):
        if a and b:
            acc = F.add[acc][F.mul[a][b]]
    return acc


def in_span(F, basis, v, m, n):
    N = n * m * m
    return gd.subspace_key(gd.span_of(F, list(basis) + [v], N)) == \
        gd.subspace_key(basis)


def key(F, basis):
    return gd.subspace_key(basis)


def wt(F, x, m, n):
    mm = m * m
    return sum(1 for e in range(n) if any(x[e * mm:(e + 1) * mm]))


# --------------------------------------------------------------------------
def check_case(p, r, m, n, slist, seed=20261104):
    F = FiniteField(p, r)
    print()
    print("=" * 78)
    print("q = p^r = %d^%d = %d ,  m = %d ,  n = %d ,  N = dim_Fq R^n = %d"
          % (p, r, F.q, m, n, n * m * m))
    print("=" * 78)
    codes, _ = gd.enumerate_ideals_morita(F, m, n, verbose=False, limit=5000,
                                          seed=seed)
    print("codes enumerated: %d" % len(codes))
    N = n * m * m

    # ---- 1. trace-valued vs matrix-valued orthogonal ----------------------
    for s in slist:
        agree = 0
        sizes_ok_t = 0
        sizes_ok_m = 0
        for C in codes:
            Dt = dual_trace(F, C, m, n, s)
            Dm = dual_matrix(F, C, m, n, s)
            if key(F, Dt) == key(F, Dm):
                agree += 1
            if len(C) + len(Dt) == N:
                sizes_ok_t += 1
            if len(C) + len(Dm) == N:
                sizes_ok_m += 1
        print("  s = %d : trace-dual == matrix-dual for %d/%d codes ; "
              "size formula: trace %d/%d , matrix %d/%d"
              % (s, agree, len(codes), sizes_ok_t, len(codes),
                 sizes_ok_m, len(codes)))

    # ---- 2. the sigma_{2s} isometry properties ----------------------------
    rnd = random.Random(seed)
    for s in slist:
        k = (2 * s) % r
        e1 = e2 = e3 = 0
        trials = 0
        for _ in range(300):
            x = tuple(rnd.randrange(F.q) for _ in range(N))
            y = tuple(rnd.randrange(F.q) for _ in range(N))
            sx = gd.rn_sigma(F, k, x)
            sy = gd.rn_sigma(F, k, y)
            lhs = gd.pair_theta(F, s, sx, sy, m, n)
            rhs = gd.rn_sigma(F, k, gd.pair_theta(F, s, x, y, m, n))
            trials += 1
            if tuple(lhs) == tuple(rhs):
                e1 += 1
            if (not any(gd.pair_theta(F, s, x, y, m, n))) == \
               (not any(gd.pair_theta(F, s, sx, sy, m, n))):
                e2 += 1
            if wt(F, sx, m, n) == wt(F, x, m, n):
                e3 += 1
        print("  s = %d , k = 2s mod r = %d :  (E1) B(sx,sy)=s(B(x,y)) %d/%d ; "
              "(E2) B=0 preserved %d/%d ; (E3) weight preserved %d/%d"
              % (s, k, e1, trials, e2, trials, e3, trials))

        # (E4) sigma_k(C^perp) = (sigma_k C)^perp ; (E5) hull equivariance ;
        # (E6) double dual = sigma_{2s}(C)
        e4 = e5 = e6 = 0
        for C in codes:
            sC = row_space_basis(F, [gd.rn_sigma(F, k, c) for c in C], N) \
                if C else []
            D = dual_matrix(F, C, m, n, s)
            sD = row_space_basis(F, [gd.rn_sigma(F, k, d) for d in D], N) \
                if D else []
            DsC = dual_matrix(F, sC, m, n, s)
            if key(F, sD) == key(F, DsC):
                e4 += 1
            HC = hull_of(F, C, m, n, s, dual_matrix)
            HsC = hull_of(F, sC, m, n, s, dual_matrix)
            sHC = row_space_basis(F, [gd.rn_sigma(F, k, h) for h in HC], N) \
                if HC else []
            if key(F, HsC) == key(F, sHC):
                e5 += 1
            DD = dual_matrix(F, D, m, n, s)
            if key(F, DD) == key(F, sC):
                e6 += 1
        print("      (E4) sigma_k(C^perp) = (sigma_k C)^perp : %d/%d"
              % (e4, len(codes)))
        print("      (E5) Hull(sigma_k C) = sigma_k Hull(C)   : %d/%d"
              % (e5, len(codes)))
        print("      (E6) (C^perp)^perp = sigma_{2s}(C)       : %d/%d"
              % (e6, len(codes)))
        refl = sum(1 for C in codes
                   if key(F, dual_matrix(F, dual_matrix(F, C, m, n, s),
                                         m, n, s)) == key(F, C))
        print("      reflexive (C^perp^perp = C)              : %d/%d"
              % (refl, len(codes)))


def main():
    print("AUDIT: trace-valued vs matrix-valued theta_s duality, and the")
    print("       sigma_{2s} isometry properties (decision U9)")
    print("run: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    # NOTE: the Morita enumerator requires X^n - 1 squarefree; in char 2 this
    # forces n odd (X^2 - 1 = (X+1)^2 is a repeated root), hence n = 3 below.
    check_case(2, 2, 2, 3, [1])          # q = 4, n = 3   (343 codes)
    check_case(2, 3, 2, 3, [1, 2])       # q = 8, n = 3   (737 codes)
    check_case(3, 2, 2, 2, [1])          # q = 9, n = 2   (144 codes)
    check_case(3, 2, 2, 4, [1])          # q = 9, n = 4   (1200 sampled)
    print()
    print("done")


if __name__ == "__main__":
    main()
