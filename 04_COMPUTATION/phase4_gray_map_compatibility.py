#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 4 -- GRAY MAP COMPATIBILITY AND FINITE-FIELD CODE CONSTRUCTION
====================================================================

Independent computational corroboration of
03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md

Scope (Tasks A-H of the Phase-4 brief):

  A. Candidate "Gray maps"  phi_A : A_t -> F_q^t ,  phi_R : R -> F_q^{4t} ,
     phi_n : R^n -> F_q^{4tn}  (R = M_2(A_t)).  The coefficient expansion is
     the BASELINE candidate and is treated as a hypothesis, never as an
     automatic Gray map: additivity, F_q-linearity, bijectivity, behaviour
     under ring multiplication and under the cyclic shift T are each measured.

  B. Weight structure: ring-Hamming w_H, entry weight w_ent, coefficient
     weight w_coef (= Hamming weight of the image), rank weight w_rank, and
     the homogeneous weight w_hom (constructed from the generating character
     of the Frobenius ring R, exact rational arithmetic).

  C. (central) The finite-field form transported by phi_n:
        <u,v>_s^hat := b_s(phi_n^{-1}(u), phi_n^{-1}(v)),
     its Gram matrix, non-degeneracy, and the correspondence
        y in C^{perp_s}   <=>   phi_n(y) in phi_n(C)^{perp_hat_s}
     with the target orthogonality DEFINED (not assumed Euclidean).

  D. Hull compatibility: phi_n(Hull_s(C)) = phi_n(C) cap phi_n(C)^{perp_hat_s},
     for principal AND non-principal hulls (the O-3.1 witnesses included).

  E. Structure of the image codes phi_n(C) <= F_q^{4tn}: length, dimension,
     quasi-cyclic index, cyclicity, and distance behaviour.

  F. Quantum-relevant sufficient conditions (recorded, NOT used to build
     CSS/EA codes -- out of scope for this phase).

  G. Two independent routes for every critical identity, [EXH]/[SMP] labels,
     and negative controls.

Nothing here is imported from the Phase-4 document: every quantity is
recomputed from the definitions.  The ring, the pairing and the code
enumeration ARE reused from the Phase-1/2/3 scripts (they are themselves
independently verified there), so that Phase 4 cannot silently disagree with
Phases 0-3B.

Every check is labelled
     [EXH]  exhaustive over the stated finite set;
     [SMP]  verified on a uniformly seeded random sample (stated explicitly).
"""

import sys, os, time, random
from fractions import Fraction
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ring_structure_checks import (say, check, LINES, FAILURES, NCHECK,
                                   Field, Local, MatRing, rref, nullspace_basis)
import phase2_stage2c_galois_duality as Z
import phase3_stage3b_hull_enumeration as S3B

LOGNAME = "phase4_gray_map_log.txt"
SEED = 20261110


def say_local(msg):
    """stdout only: never enters the log (keeps two runs byte-identical)."""
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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ==========================================================================
# 1.  the candidate maps  (Task A)
# ==========================================================================
#
#  A_t = F_q[u]/<u^t> is stored as coefficient tuples (a_0,...,a_{t-1});
#  R = M_2(A_t) as a 4-tuple of A_t elements in the order k = 2i+j
#  ((1,1),(1,2),(2,1),(2,2));  a word x in R^n as an n-tuple of R elements.
#
#  phi_A(a)          = (a_0,...,a_{t-1})                       in F_q^t
#  phi_R(X)          = (phi_A(X_0),...,phi_A(X_3))             in F_q^{4t}
#  phi_n(x)          = (phi_R(x_0),...,phi_R(x_{n-1}))         in F_q^{4tn}
#
#  coordinate index of phi_n:  ((e*4 + k)*t + a)   [= Ctx.flat_word]
#
#  Variants studied in Task A:
#    P        : reverse the t coefficients inside each (e,k) block;
#    phi^rev  = P . phi_n     (Task C shows this transports b_s to the PLAIN
#                              sigma_s-Hermitian form);
#    Bachoc   : (a_0,a_1) -> (a_0 + a_1, a_1) on each A_2 entry (t = 2).


def phi_A(C, a):
    return tuple(a)


def phi_R(C, X):
    return tuple(c for k in range(4) for c in X[k])


def phi_n(C, x):
    return tuple(c for xe in x for c in phi_R(C, xe))


def rev_index(t, n):
    """P: index i of the new vector reads position rev_index[i] of the old."""
    idx = []
    for e in range(n):
        for k in range(4):
            for a in range(t):
                idx.append((e * 4 + k) * t + (t - 1 - a))
    return idx


def apply_perm(u, perm):
    return [u[perm[i]] for i in range(len(perm))]


def all_R_elements(RA):
    """every element of R = M_2(A_t), built by brute force over F_q^{4t}"""
    t, q = RA.t, RA.F.q
    out = []
    for v in range(q ** (4 * t)):
        w = []
        for k in range(4):
            c = []
            for a in range(t):
                w0 = v // (q ** (k * t + a))
                c.append(w0 % q)
            w.append(tuple(c))
        out.append(tuple(w))
    return out


def all_words(C):
    """every word in R^n (only for tiny |R|^n)"""
    N = 4 * C.t * C.n
    q = C.F.q
    out = []
    for v in range(q ** N):
        flat = [(v // (q ** i)) % q for i in range(N)]
        out.append(C.unflat_word(flat))
    return out


def T_shift(C, x):
    """(Tx)_e = x_{e-1 mod n}   (the Phase-1 / Stage-2C convention)"""
    n = C.n
    return tuple(x[(e - 1) % n] for e in range(n))


def rand_word(C, rng):
    return tuple(tuple(tuple(rng.randrange(C.F.q) for _ in range(C.t))
                       for _ in range(4)) for _ in range(C.n))


# --------------------------------------------------------------------------
def task_a_maps(q, t, n, rng, exhaustive_cap=8000):
    """Task A: the candidate maps and their elementary properties."""
    C = Z.Ctx(q, t, n)
    RA, F = C.RA, C.F
    N = 4 * t * n
    sub("(q,t,n) = (%d,%d,%d):  the candidate maps phi_A, phi_R, phi_n" % (q, t, n))
    say("  N = 4tn = %d   |R| = %d   |R^n| = %d" % (N, q ** (4 * t), N and q ** N))

    # ---- A1  phi_A -------------------------------------------------------
    As = []
    for v in range(q ** t):
        As.append(tuple((v // (q ** a)) % q for a in range(t)))
    ok_lin = True
    for a in As:
        for b in As:
            if phi_A(C, RA.A.add(a, b)) != tuple(F.add[phi_A(C, a)[i]][phi_A(C, b)[i]]
                                                 for i in range(t)):
                ok_lin = False
    check("(%d,%d,%d): phi_A is additive (F_q^t)" % (q, t, n), ok_lin,
          "all %d^%d pairs" % (q ** t, 2) if q ** (2 * t) < 2000 else
          "all %d pairs" % (q ** (2 * t)), True)
    ok_hom = all(tuple(F.mul[c][phi_A(C, a)[i]] for i in range(t))
                 == phi_A(C, RA.A.mul(RA.A.scalar(c, RA.A.one), a))
                 for a in As for c in range(q))
    # A_t is F_q[u]/<u^t>: the scalar c acts as c*1 = (c,0,...,0)
    check("(%d,%d,%d): phi_A is F_q-linear" % (q, t, n), ok_hom,
          "all %d x %d" % (q ** t, q), True)
    check("(%d,%d,%d): phi_A is injective (|image| = |A_t|)" % (q, t, n),
          len(set(phi_A(C, a) for a in As)) == q ** t, "%d elements" % (q ** t), True)

    # ---- A2  our phi_R equals the flat coordinate vector -----------------
    ex = all_R_elements(RA) if q ** (4 * t) <= exhaustive_cap else None
    if ex is None:
        ex = [tuple(tuple(rng.randrange(q) for _ in range(t)) for _ in range(4))
              for _ in range(4000)]
        exh = False
    else:
        exh = True
    check("(%d,%d,%d): phi_R agrees with the independent flat coordinate map"
          % (q, t, n),
          all(phi_R(C, X) == tuple(RA.vec(X)) for X in ex),
          "%d elements" % len(ex), exh)
    check("(%d,%d,%d): phi_n = concat of phi_R over positions" % (q, t, n),
          all(phi_n(C, x) == tuple(C.flat_word(x))
              for x in [rand_word(C, rng) for _ in range(200)]),
          "200 words", False)

    # ---- A3  additivity / F_q-linearity / bijectivity of phi_R -----------
    ok_add = ok_hom2 = True
    pairs = [(X, Y) for X in ex[:200] for Y in ex[:200]] if not exh else \
            [(X, Y) for X in ex for Y in ex[:40]]
    for X, Y in pairs:
        Zx = RA.add(X, Y)
        if phi_R(C, Zx) != tuple(F.add[phi_R(C, X)[i]][phi_R(C, Y)[i]]
                                 for i in range(4 * t)):
            ok_add = False
            break
    check("(%d,%d,%d): phi_R additive" % (q, t, n), ok_add,
          "%d pairs" % len(pairs), exh)
    # scalar c in F_q acts on R as the central matrix c*I, so:
    ok_hom2 = True
    cI = [RA.scalar_mat(RA.A.scalar(c, RA.A.one)) for c in range(q)]
    for X in ex[:200]:
        for c in range(q):
            lhs = phi_R(C, RA.mul(cI[c], X))
            if lhs != tuple(F.mul[c][u] for u in phi_R(C, X)):
                ok_hom2 = False
    check("(%d,%d,%d): phi_R is F_q-homogeneous (F_q central)" % (q, t, n),
          ok_hom2, "%d x %d" % (min(200, len(ex)), q), exh)

    if exh:
        check("(%d,%d,%d): phi_R injective (|image| = |R|)" % (q, t, n),
              len(set(phi_R(C, X) for X in ex)) == q ** (4 * t),
              "|R| = %d" % (q ** (4 * t)), True)
        check("(%d,%d,%d): phi_R surjective (image = F_q^{4t})" % (q, t, n),
              len(set(phi_R(C, X) for X in ex)) == q ** (4 * t),
              "|F_q^{4t}| = %d" % (q ** (4 * t)), True)
    else:
        check("(%d,%d,%d): phi_R injective on %d sampled elements "
              "(distinct inputs have distinct images)" % (q, t, n, len(ex)),
              len(set(phi_R(C, X) for X in ex)) == len(set(ex)),
              "%d distinct inputs" % len(set(ex)), False)

    # ---- A4  phi_R is NOT a ring homomorphism (R is noncommutative) -----
    cnt = 0
    tot = 0
    for X in ex[:60]:
        for Y in ex[:60]:
            tot += 1
            if phi_R(C, RA.mul(X, Y)) != phi_R(C, RA.mul(Y, X)):
                cnt += 1
    say("       phi_R(XY) != phi_R(YX) on %d / %d sampled pairs (R is "
        "noncommutative: |R| = %d)" % (cnt, tot, q ** (4 * t)))

    # ---- A5  the transported left/right multiplication matrices ----------
    # M_L(a) :  phi_R(a X) = M_L(a) phi_R(X)   (F_q-linear, a |-> M_L(a) is an
    # injective ring homomorphism R -> M_{4t}(F_q): the left regular rep.)
    def mat_of_left(a):
        cols = []
        for i in range(4 * t):
            e = [0] * (4 * t)
            e[i] = 1
            E = RA.unvec(e)
            cols.append(list(phi_R(C, RA.mul(a, E))))
        # rows of the matrix: M[row][col]
        return [[cols[j][i] for j in range(4 * t)] for i in range(4 * t)]

    def matvec(M, v, F):
        out = []
        for row in M:
            acc = 0
            for j, x in enumerate(row):
                if x and v[j]:
                    acc = F.add[acc][F.mul[x][v[j]]]
            out.append(acc)
        return out

    def matmul_q(A, B, F):
        m, k2, n2 = len(A), len(B), len(B[0])
        out = [[0] * n2 for _ in range(m)]
        for i in range(m):
            for j in range(n2):
                acc = 0
                for l in range(k2):
                    if A[i][l] and B[l][j]:
                        acc = F.add[acc][F.mul[A[i][l]][B[l][j]]]
                out[i][j] = acc
        return out

    sample_a = ex[:12]
    okL = all(matvec(mat_of_left(a), list(phi_R(C, X)), F) ==
              list(phi_R(C, RA.mul(a, X))) for a in sample_a for X in ex[:20])
    check("(%d,%d,%d): phi_R(aX) = M_L(a) phi_R(X)" % (q, t, n), okL,
          "%d x %d" % (len(sample_a), min(20, len(ex))), exh)
    okL2 = all(matmul_q(mat_of_left(a), mat_of_left(b), F) ==
               mat_of_left(RA.mul(a, b)) for a in sample_a for b in sample_a)
    check("(%d,%d,%d): a |-> M_L(a) is multiplicative (ring embedding "
          "R -> M_{4t}(F_q))" % (q, t, n), okL2,
          "%d^2 pairs" % len(sample_a), exh)
    okL3 = all(mat_of_left(RA.add(a, b)) ==
               [[F.add[mat_of_left(a)[i][j]][mat_of_left(b)[i][j]]
                 for j in range(4 * t)] for i in range(4 * t)]
               for a in sample_a for b in sample_a)
    check("(%d,%d,%d): a |-> M_L(a) is additive" % (q, t, n), okL3,
          "%d^2 pairs" % len(sample_a), exh)
    nin = len(set(ex[:400]))
    inj = len(set(tuple(tuple(r) for r in mat_of_left(a))
                  for a in set(ex[:400]))) == nin
    check("(%d,%d,%d): a |-> M_L(a) is injective on %d elements"
          % (q, t, n, nin), inj,
          "%d distinct matrices" % nin, exh)

    # ---- A6  shift compatibility:  phi_n(Tx) = That phi_n(x) -------------
    # That = the rotation by one block of 4t coordinates.
    perm_T = [((N - 4 * t) + i) % N for i in range(N)]  # new[i] = old[perm_T[i]]
    ok_T = True
    for i in range(N):
        e = [0] * N
        e[i] = 1
        w = C.unflat_word(e)
        lhs = list(phi_n(C, T_shift(C, w)))
        rhs = list(C.flat_word(T_shift(C, w)))
        if lhs != [e[perm_T[j]] for j in range(N)]:
            ok_T = False
            break
    check("(%d,%d,%d): phi_n(Tx) = That phi_n(x) on all %d basis words "
          "(That = rotation by 4t)" % (q, t, n, N), ok_T, "all %d" % N, True)
    ok_T2 = all(list(phi_n(C, T_shift(C, w))) ==
                [phi_n(C, w)[perm_T[j]] for j in range(N)]
                for w in [rand_word(C, rng) for _ in range(300)])
    check("(%d,%d,%d): phi_n(Tx) = That phi_n(x) on 300 random words" % (q, t, n),
          ok_T2, "300 words", False)

    # ---- A7  the variant maps -------------------------------------------
    perm_P = rev_index(t, n)
    ok_P = True
    for w in [rand_word(C, rng) for _ in range(300)]:
        u = list(phi_n(C, w))
        v = list(C.flat_word(w))
        if apply_perm(u, perm_P) != apply_perm(v, perm_P):
            ok_P = False
    check("(%d,%d,%d): phi^rev = P.phi_n is well defined (P = reversal inside "
          "each (e,k) block)" % (q, t, n), ok_P, "300 words", False)
    # P and That commute  =>  phi^rev is shift-compatible with the same index
    PT = [perm_T[perm_P[i]] for i in range(N)]
    TP = [perm_P[perm_T[i]] for i in range(N)]
    check("(%d,%d,%d): P commutes with That (so phi^rev has the same "
          "quasi-cyclic index 4t)" % (q, t, n), PT == TP, "N = %d" % N, True)

    if t == 2:
        # Bachoc-type map  (a_0,a_1) -> (a_0+a_1, a_1)  on each A_2 entry
        def phi_B_entry(a):
            return (F.add[a[0]][a[1]], a[1])

        def phi_B(w):
            out = []
            for xe in w:
                for k in range(4):
                    out.extend(phi_B_entry(xe[k]))
            return out

        ok_B = all(len(phi_B(rand_word(C, rng))) == N
                   for _ in range(50))
        check("(%d,%d,%d): Bachoc-type phi_B is a map R^n -> F_q^N" % (q, t, n),
              ok_B, "length %d" % N, False)
        # additivity
        ok_Ba = True
        for _ in range(200):
            x = rand_word(C, rng)
            y = rand_word(C, rng)
            z = tuple(C.RA.add(x[e], y[e]) for e in range(n))
            if phi_B(z) != [F.add[phi_B(x)[i]][phi_B(y)[i]] for i in range(N)]:
                ok_Ba = False
                break
        check("(%d,%d,%d): Bachoc-type phi_B is additive" % (q, t, n), ok_Ba,
              "200 pairs", False)
        ok_BT = all(phi_B(T_shift(C, w)) ==
                    [phi_B(w)[perm_T[j]] for j in range(N)]
                    for w in [rand_word(C, rng) for _ in range(300)])
        check("(%d,%d,%d): Bachoc-type phi_B commutes with the shift"
              % (q, t, n), ok_BT, "300 words", False)
        # the Gram matrix transported by phi_B:  S = [[1,1],[0,1]] acts on the
        # coefficient pair (a_0,a_1) inside each entry, and S has entries in
        # F_p (hence is fixed by sigma_s), so the transported Gram is
        #     S^T H_2 S  on each (e,k) block.
        S = [[1, 1], [0, 1]]
        H2 = hankel_t(2, F)
        STS = matmul_F(matmul_F(transpose_F(S), H2, F), S, F)
        say("       S^T H_2 S = %s   (H_2 = %s)"
            % ([[str(x) for x in r] for r in STS],
               [[str(x) for x in r] for r in H2]))
        check("(%d,%d,%d): the Bachoc map transports b_s to the SAME Hankel "
              "form as the coefficient map  <=>  char F_q = 2"
              % (q, t, n), (STS == H2) == (F.p == 2),
              "p = %d" % F.p, True)
        # the weights: phi_B is NOT a w_coef isometry
        diff = [x for x in [rand_word(C, rng) for _ in range(500)]
                if sum(1 for c in phi_B(x) if c) != w_coef(C, x)]
        say("       #words (of 500) with wt_Ham(phi_B x) != w_coef(x): %d"
            % len(diff))
        check("(%d,%d,%d): the Bachoc map is NOT a w_coef/Hamming isometry"
              % (q, t, n), len(diff) > 0, "%d / 500" % len(diff), False)
        # and it is not a homogeneous-weight isometry either: w_hom takes
        # non-integral values, Hamming weights do not (see Part B)
    return C


# ==========================================================================
# 2.  weights  (Task B)
# ==========================================================================

def w_Hamming(C, x):
    """ring-Hamming weight on R^n: number of nonzero positions"""
    z = C.RA.zero
    return sum(1 for xe in x if xe != z)


def w_entry(C, x):
    """number of nonzero A_t-entries of the matrices x_e"""
    zA = C.RA.A.zero
    return sum(1 for xe in x for k in range(4) if xe[k] != zA)


def w_coef(C, x):
    """number of nonzero F_q coefficients  =  wt_Ham(phi_n(x))"""
    return sum(1 for c in C.flat_word(x) if c != 0)


def w_rank(C, x):
    """sum over positions of the rank of x_e over the residue field F_q"""
    RA, F, t = C.RA, C.F, C.t
    tot = 0
    for xe in x:
        # reduce mod u and take the rank of the 2x2 matrix over F_q
        M = [[xe[0][0], xe[1][0]], [xe[2][0], xe[3][0]]]
        det = F.sub[F.mul[M[0][0]][M[1][1]]][F.mul[M[0][1]][M[1][0]]]
        nz = any(M[i][j] != 0 for i in range(2) for j in range(2))
        tot += 0 if not nz else (2 if det != 0 else 1)
    return tot


def rk_of(C, F, X):
    """rank over F_q of the mod-u reduction of X in M_2(A_t)"""
    M = [[X[0][0], X[1][0]], [X[2][0], X[3][0]]]
    det = F.sub[F.mul[M[0][0]][M[1][1]]][F.mul[M[0][1]][M[1][0]]]
    nz = any(M[i][j] != 0 for i in range(2) for j in range(2))
    return 0 if not nz else (2 if det != 0 else 1)


def tr_fp(F, a):
    """absolute trace F_q -> F_p"""
    s = 0
    for i in range(F.r):
        s = F.add[s][F.frob[i][a]]
    return s


def homogeneous_weights(RA, F, elems, units):
    """
    The homogeneous weight on R = M_2(A_t) built from the generating character.

    R is a Frobenius ring with Frobenius functional Lambda = lambda o tr
    (T-001), so  chi(X) = exp(2 pi i Tr_{F_q/F_p}(Lambda(X))/p)  is a
    generating (left AND right) character of (R,+).  The homogeneous weight is

        w_hom(X) = 1 - (1/|R^x|) sum_{u in R^x} chi(X u),

    normalised so that its average over R is 1 (that normalisation is verified
    below, not assumed).  chi is computed exactly: the sum
    S = sum_u chi(Xu) lies in Q(zeta_p) and is here reduced to an INTEGER by
    the exact rule  S = c_0 - c_{p-1}  valid as soon as the counts
    c_m = #{u in R^x : Tr(Lambda(Xu)) = m} satisfy c_1 = ... = c_{p-2} = c_{p-1}
    (the rationality of the homogeneous weight); that rule is checked each time.
    """
    p = F.p
    out = {}
    rational_ok = True
    for X in elems:
        cnt = [0] * p
        for u in units:
            Xu = RA.mul(X, u)
            cnt[tr_fp(F, RA.Lambda(Xu))] += 1
        if any(cnt[m] != cnt[p - 1] for m in range(1, p - 1)):
            rational_ok = False
        S = cnt[0] - cnt[p - 1]
        out[X] = Fraction(len(units) - S, len(units))
    return out, units, rational_ok


def hom_from_nonunits(RA, F, elems, units, nonunits, sizeR):
    """
    w_hom(X) = 1 - S(X)/|R^x| with S(X) = sum_{u in R^x} chi(Xu), computed as
        S(X) = |R| [X = 0] - sum_{u not in R^x} chi(Xu)
    (character orthogonality), in exact integer arithmetic.  sizeR = |R| must
    be passed in: it is NOT len(elems) when only a sample is evaluated.
    """
    p = F.p
    zero = RA.zero
    out = {}
    rat = True
    for X in elems:
        cnt = [0] * p
        for u in nonunits:
            cnt[tr_fp(F, RA.Lambda(RA.mul(X, u)))] += 1
        if any(cnt[m] != cnt[p - 1] for m in range(1, p - 1)):
            rat = False
        S = (sizeR if X == zero else 0) - (cnt[0] - cnt[p - 1])
        out[X] = Fraction(len(units) - S, len(units))
    return out, rat


_HOM_CACHE = {}


def task_b_weights(q, t, n, rng, char_cap=12000000):
    sub("(q,t,n) = (%d,%d,%d):  weights on R^n" % (q, t, n))
    C = Z.Ctx(q, t, n)
    RA, F = C.RA, C.F
    N = 4 * t * n

    # ---- B1  w_coef is the Hamming weight of the image -------------------
    ws = [rand_word(C, rng) for _ in range(300)]
    check("(%d,%d,%d): wt_Ham(phi_n(x)) = w_coef(x)  (phi_n is a w_coef/"
          "Hamming isometry by construction)" % (q, t, n),
          all(sum(1 for c in C.flat_word(x) if c) == w_coef(C, x) for x in ws),
          "300 words", False)
    check("(%d,%d,%d): d_Ham(phi_n x, phi_n y) = w_coef(x-y)" % (q, t, n),
          all(sum(1 for i in range(N)
                  if C.flat_word(x)[i] != C.flat_word(y)[i])
              == w_coef(C, tuple(RA.sub(x[e], y[e]) for e in range(n)))
              for x in ws[:60] for y in ws[:60]),
          "3600 pairs", False)

    # ---- B2  the inequalities between the weights ------------------------
    if q ** N <= 70000:
        words = all_words(C)
        exh = True
    else:
        words = [rand_word(C, rng) for _ in range(2000)]
        exh = False
    ok1 = ok2 = ok3 = ok4 = True
    sharp_lo = sharp_hi = None
    for x in words:
        h, e_, c_ = w_Hamming(C, x), w_entry(C, x), w_coef(C, x)
        if not (h <= e_ <= 4 * h):
            ok1 = False
        if not (e_ <= c_ <= t * e_):
            ok2 = False
        if not (h <= c_ <= 4 * t * h):
            ok3 = False
        if h > 0 and c_ == h:
            sharp_lo = x
        if h > 0 and c_ == 4 * t * h:
            sharp_hi = x
    check("(%d,%d,%d): w_H <= w_ent <= 4 w_H" % (q, t, n), ok1,
          "%d words" % len(words), exh)
    check("(%d,%d,%d): w_ent <= w_coef <= t w_ent" % (q, t, n), ok2,
          "%d words" % len(words), exh)
    check("(%d,%d,%d): w_H <= wt_Ham(phi_n(x)) <= 4t w_H" % (q, t, n), ok3,
          "%d words" % len(words), exh)
    say("       lower bound attained (w_coef = w_H > 0): %s" %
        ("yes" if sharp_lo is not None else "no"))
    say("       upper bound attained (w_coef = 4t w_H): %s" %
        ("yes" if sharp_hi is not None else "no"))

    # ---- B3  phi_n does NOT preserve the ring-Hamming weight -------------
    mism = [x for x in words if w_Hamming(C, x) > 0 and
            w_coef(C, x) != w_Hamming(C, x)]
    say("       #words with w_coef(x) != w_H(x): %d / %d" % (len(mism), len(words)))
    if mism:
        x = mism[0]
        say("       witness: w_H = %d, w_ent = %d, w_coef = %d, w_rank = %d"
            % (w_Hamming(C, x), w_entry(C, x), w_coef(C, x), w_rank(C, x)))

    # ---- B4  the homogeneous weight on R --------------------------------
    sub("(q,t) = (%d,%d):  the homogeneous weight on R = M_2(A_t)" % (q, t))
    if (q, t) in _HOM_CACHE:
        W0, lbl0 = _HOM_CACHE[(q, t)]
        say("       w_hom depends only on (q,t), not on n: already computed "
            "above for this ring (%s)" % lbl0)
        return C, W0
    sizeR = q ** (4 * t)
    if sizeR > 100000:
        say("       |R| = %d exceeds the enumeration budget: w_hom is NOT "
            "computed for this ring" % sizeR)
        _HOM_CACHE[(q, t)] = (None, "not computed (|R| too large)")
        return C, None
    all_elems = all_R_elements(RA)
    units = [X for X in all_elems if RA.det(X)[0] != 0]
    nonunits = [X for X in all_elems if RA.det(X)[0] == 0]
    if sizeR * len(nonunits) <= char_cap:
        elems = all_elems
        exh = True
        lbl = "all |R| = %d elements (|R^x| = %d)" % (sizeR, len(units))
    else:
        elems = rng.sample(all_elems, 120)
        exh = False
        lbl = ("120 sampled elements (|R| |R\R^x| = %d > budget)"
               % (sizeR * len(nonunits)))
    W, rat = hom_from_nonunits(RA, F, elems, units, nonunits, sizeR)
    check("(%d,%d): the character sums are rational (c_1=...=c_{p-1})" % (q, t),
          rat, lbl, True)
    vals = Counter(W.values())
    if RA.zero in W:
        check("(%d,%d): w_hom(0) = 0" % (q, t), W[RA.zero] == 0, "", exh)
    else:
        say("       (the zero element is not in the sample: w_hom(0) not "
            "re-tested here)")
    # average over R is 1 (only meaningful in the exhaustive run)
    if exh:
        avg = sum(W.values(), Fraction(0)) / len(W)
        check("(%d,%d): mean of w_hom over R is 1 (normalisation)" % (q, t),
              avg == 1, "mean = %s" % avg, True)
    # constant on associate classes?  (Rx = Ry  =>  w_hom(x) = w_hom(y))
    assoc_ok = True
    keys = list(W.keys())
    if exh and len(keys) <= 300:
        for X in keys:
            for c in range(1, q):
                cI = RA.scalar_mat(RA.A.scalar(c, RA.A.one))
                Y = RA.mul(X, cI)
                if W[Y] != W[X]:
                    assoc_ok = False
    check("(%d,%d): w_hom(X) = w_hom(Xc) for c in F_q^x (F_q-homogeneity)"
          % (q, t), assoc_ok, lbl, exh)
    # unit-invariance: w_hom(uX) = w_hom(X) for u a unit  (right associates)
    if exh:
        uinv = all(W[RA.mul(u, X)] == W[X] for X in list(W.keys())[:40]
                   for u in units[:6])
        check("(%d,%d): w_hom(uX) = w_hom(X) for units u (left associates)"
              % (q, t), uinv, "40 x 6", True)
    else:
        ok_u = True
        for X in list(W.keys())[:8]:
            for u in units[:3]:
                Xu = RA.mul(u, X)
                Wu, _ = hom_from_nonunits(RA, F, [Xu], units, nonunits, sizeR)
                if Wu[Xu] != W[X]:
                    ok_u = False
        check("(%d,%d): w_hom(uX) = w_hom(X) for units u (left associates)"
              % (q, t), ok_u, "8 x 3 (weights recomputed)", False)
    say("       the values taken by w_hom:  %s" %
        sorted([(str(k), v) for k, v in vals.items()], key=lambda z: -z[1]))
    # integrality: a necessary condition for any map into Hamming space
    dens = sorted(set(v.denominator for v in W.values()))
    say("       denominators occurring: %s" % dens)
    integral = all(v.denominator == 1 for v in W.values())
    say("       => w_hom is %s" % ("INTEGER valued" if integral else
                                   "NOT integer valued"))
    # triangle inequality (necessary for w_hom to be the weight of a metric
    # pulled back from any Hamming space)
    if exh and len(keys) <= 300:
        tri = all(W[RA.sub(X, Y)] <= W[X] + W[Y]
                  for X in keys[:60] for Y in keys[:60])
        check("(%d,%d): w_hom(X-Y) <= w_hom(X)+w_hom(Y) (triangle inequality, "
              "necessary for a Gray isometry)" % (q, t), tri, "3600 pairs", True)
    # is w_hom a function of (valuation, rank of the reduction)?
    if exh:
        tab = {}
        for X in keys:
            val = 0                       # val(X) = max{v : X in u^v M_2(A_t)}
            while val < t and all(X[k][a] == 0 for k in range(4)
                                  for a in range(val + 1)):
                val += 1
            if val >= t:                  # X = 0
                rk = 0
            else:
                M = [[X[0][val], X[1][val]], [X[2][val], X[3][val]]]
                det = F.sub[F.mul[M[0][0]][M[1][1]]][F.mul[M[0][1]][M[1][0]]]
                rk = 2 if det != 0 else 1
            tab.setdefault((val, rk), set()).add(W[X])
        say("       w_hom by (u-adic valuation, rank of the leading matrix):")
        for k in sorted(tab):
            say("         (val=%2d, rank=%2d) -> %s" %
                (k[0], k[1], sorted(tab[k])))
        # the closed form predicted for R = M_2(F_q) (t = 1):
        #   w(0) = 0,  w(rank 1) = 1 + 1/(q^2-1),  w(rank 2) = 1 - 1/((q-1)^2(q+1))
        if t == 1:
            pred = {0: Fraction(0), 1: 1 + Fraction(1, q * q - 1),
                    2: 1 - Fraction(1, (q - 1) ** 2 * (q + 1))}
            ok_cf = all(W[X] == pred[rk_of(C, F, X)] for X in keys)
            check("(%d,%d): closed form  w_hom(X) = 0 / 1+1/(q^2-1) / "
                  "1-1/((q-1)^2(q+1))  by rank" % (q, t), ok_cf, lbl, exh)
    # ---- structured elements: the value of w_hom on the socle filtration --
    z, one = RA.A.zero, RA.A.one
    def mat(a, b, c, d):
        return (a, b, c, d)
    struct = [("0", mat(z, z, z, z)), ("I", mat(one, z, z, one)),
              ("E11", mat(one, z, z, z))]
    for v in range(1, t):
        uv = RA.A.pow(RA.A.u, v)
        struct.append(("u^%d I" % v, mat(uv, z, z, uv)))
        struct.append(("u^%d E11" % v, mat(uv, z, z, z)))
        struct.append(("u^%d E12" % v, mat(z, uv, z, z)))
    WS, _ = hom_from_nonunits(RA, F, [x for _, x in struct], units, nonunits,
                              sizeR)
    say("       w_hom on structured elements (t = %d):" % t)
    for name, X in struct:
        say("         w_hom(%12s) = %s" % (name, WS[X]))
    check("(%d,%d): w_hom(0) = 0 (exact character sum over |R| = %d)"
          % (q, t, sizeR), WS[mat(z, z, z, z)] == 0, "", True)
    _HOM_CACHE[(q, t)] = (W, lbl)
    return C, W


# ==========================================================================
# 3.  Task C -- the finite-field form transported by phi_n
# ==========================================================================
#
#  b_s(x,y) = Lambda(B_s(x,y)) = lambda( tr( sum_e theta_s(x_e) y_e ) )
#  is sigma_s-semilinear in x and F_q-linear in y (Lemma 6.2), so the form
#  transported by the F_q-linear bijection phi_n is
#
#       <u,v>^hat_s := b_s(phi_n^{-1} u, phi_n^{-1} v)
#                    = sum_{i,j} sigma_s(u_i) J[i][j] v_j ,   J[i][j] = b_s(e_i,e_j).
#
#  The point of Task C is that J is NOT the identity in general (the u-adic
#  reversal inside each entry), so the target orthogonality is a sigma_s-
#  Hermitian form with a Hankel Gram matrix -- and that the SAME pairing
#  becomes the PLAIN sigma_s-Hermitian form after the coefficient reversal P.


def gram_transported(C, s):
    """J[i][j] = b_s(e_i, e_j) for the standard F_q-basis of F_q^{N}."""
    N = 4 * C.t * C.n
    eps = []
    for i in range(N):
        e = [0] * N
        e[i] = 1
        eps.append(C.unflat_word(e))
    J = [[C.bs(eps[i], eps[j], s) for j in range(N)] for i in range(N)]
    return J, eps


def predicted_gram(t, n):
    """I_{4n} (x) H_t :  H_t[a][b] = 1 iff a + b = t-1, one block per (e,k)."""
    N = 4 * t * n
    J = [[0] * N for _ in range(N)]
    for e in range(n):
        for k in range(4):
            base = (e * 4 + k) * t
            for a in range(t):
                J[base + a][base + (t - 1 - a)] = 1
    return J


def hat_form(u, v, J, F, s):
    """<u,v>^hat_s = sum_i sigma_s(u_i) (J v^T)_i"""
    fro = F.frob[s % F.r]
    tot = 0
    m = len(J)
    for i in range(m):
        ui = fro[u[i]]
        if ui == 0:
            continue
        Ji = J[i]
        for j in range(m):
            if Ji[j] and v[j]:
                tot = F.add[tot][F.mul[F.mul[ui][Ji[j]]][v[j]]]
    return tot


def sigma_hat(u, F, s):
    return [F.frob[s % F.r][c] for c in u]


def orth_hat(rows, J, F, N, s):
    """{v in F_q^N : <u,v>^hat_s = 0 for all u in rows} as an F_q-basis"""
    fro = F.frob[s % F.r]
    M = []
    for u in rows:
        us = [fro[c] for c in u]
        row = []
        for j in range(N):
            acc = 0
            for i in range(N):
                if us[i] and J[i][j]:
                    acc = F.add[acc][F.mul[us[i]][J[i][j]]]
            row.append(acc)
        M.append(row)
    return nullspace_basis(M, F, N)


def orth_euclid(rows, F, N):
    return nullspace_basis([list(r) for r in rows], F, N)


def orth_herm(rows, F, N, s):
    """the plain sigma_s-Hermitian form  sum_i sigma_s(u_i) v_i"""
    fro = F.frob[s % F.r]
    return nullspace_basis([[fro[c] for c in r] for r in rows], F, N)


def rows_key(rows, F, N):
    return tuple(tuple(r) for r in rref([list(r) for r in rows], F, N)[0])


# ---- codes and their images ----------------------------------------------

def img_basis(E, C, W):
    """an F_q-basis of phi_n(C) for the code C = I_W  (rows in F_q^{4tn})"""
    N = 4 * C.t * C.n
    rows = []
    for r in E.code_basis(W):
        M = C.unflat_rn(tuple(r))
        w = C.iota_inv(M)
        rows.append(list(C.flat_word(w)))
    return rref(rows, C.F, N)[0]


def img_from_rn_basis(C, rn_rows):
    """phi_n of the F_q-span of rn_rows (rows in flat R_n coordinates)"""
    N = 4 * C.t * C.n
    rows = []
    for r in rn_rows:
        M = C.unflat_rn(tuple(r))
        rows.append(list(C.flat_word(C.iota_inv(M))))
    return rref(rows, C.F, N)[0]


def dual_img(E, C, W, s):
    """
    phi_n(C^{perp_s}) by the INDEPENDENT route:
    C^{perp_s} = I_{W'} with W' = cap_i ker theta_s(rev g_i) (Stage 2C Thm 3.8),
    i.e. the annihilator route, which never uses the transported form.
    """
    Wp = S3B.Wprime_ann(E, W, s)
    N = 4 * C.t * C.n
    if Wp is None:                    # C = 0  =>  C^{perp_s} = R^n
        return [[1 if j == i else 0 for j in range(N)] for i in range(N)]
    return img_basis(E, C, {"rows": [tuple(r) for r in Wp]})



def perm_matrix(perm, N, F):
    """P with (Pu)[i] = u[perm[i]], i.e. P[i][perm[i]] = 1"""
    P = [[0] * N for _ in range(N)]
    for i in range(N):
        P[i][perm[i]] = 1
    return P


def transpose_F(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def matmul_F(A, B, F):
    m, k2, n2 = len(A), len(B), len(B[0])
    out = [[0] * n2 for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        for l in range(k2):
            if Ai[l]:
                Bl = B[l]
                for j in range(n2):
                    if Bl[j]:
                        out[i][j] = F.add[out[i][j]][F.mul[Ai[l]][Bl[j]]]
    return out


def hankel_t(t, F):
    H = [[0] * t for _ in range(t)]
    for a in range(t):
        H[a][t - 1 - a] = 1
    return H


def is_monomial(T, F):
    n = len(T)
    rows = [sum(1 for x in r if x) for r in T]
    cols = [sum(1 for i in range(n) if T[i][j]) for j in range(n)]
    return all(c == 1 for c in rows) and all(c == 1 for c in cols)


def find_block_congruence(t, F, rng, cap=300000):
    """T (t x t over F_q) with T^T H_t T = I_t, or None.  Exhaustive if cheap."""
    H = hankel_t(t, F)
    I = [[1 if i == j else 0 for j in range(t)] for i in range(t)]
    total = F.q ** (t * t)
    if total <= cap:
        for v in range(total):
            T = [[(v // (F.q ** (i * t + j))) % F.q for j in range(t)]
                 for i in range(t)]
            if matmul_F(matmul_F(transpose_F(T), H, F), T, F) == I:
                return T
        return None
    for _ in range(20000):
        T = [[rng.randrange(F.q) for _ in range(t)] for _ in range(t)]
        if matmul_F(matmul_F(transpose_F(T), H, F), T, F) == I:
            return T
    return None


def block_diag_expand(T, t, n, F):
    """I_{4n} (x) T  acting on F_q^{4tn} in the ((e*4+k)*t + a) ordering"""
    N = 4 * t * n
    out = [[0] * N for _ in range(N)]
    for e in range(n):
        for k in range(4):
            base = (e * 4 + k) * t
            for a in range(t):
                for b in range(t):
                    out[base + a][base + b] = T[a][b]
    return out


# ==========================================================================
# 4.  one parameter set  (Tasks C, D, E, F)
# ==========================================================================

def run_case_p4(q, t, n, s_list, rng, dist_cap=4100, code_cap=None,
                do_dist=True, dist_max_codes=120):
    E = S3B.Ring3B(q, t, n)
    C = E.C
    F, N = C.F, 4 * t * n
    head("(q,t,n) = (%d,%d,%d)   kind = %s   N = 4tn = %d   |R^n| = %d"
         % (q, t, n, E.kind, N, q ** N))
    say("  r = [F_q : F_p] = %d ;  reflexivity of b_s  <=>  r | 2s" % C.r)

    # ---- enumerate the codes --------------------------------------------
    t_enum = time.time()
    feasible = (q ** (t * n)) ** 2 <= 200000
    if feasible:
        subs = S3B.enumerate_submodules(E.C)
        lbl_codes = "exhaustive BFS over the submodule lattice of B^2"
        exh_codes = True
    else:
        E1, loc = S3B.local_lattice(q, t)
        import itertools
        all_idx = list(itertools.product(range(len(loc)), repeat=E.ncomp))
        if code_cap and len(all_idx) > code_cap:
            rng.shuffle(all_idx)
            all_idx = all_idx[:code_cap]
            lbl_codes = "CRT product lattice (%d local submodules)^%d, %d SAMPLED"
            lbl_codes = lbl_codes % (len(loc), E.ncomp, len(all_idx))
            exh_codes = False
        else:
            lbl_codes = "CRT product lattice (%d local submodules)^%d, all %d" \
                        % (len(loc), E.ncomp, len(all_idx))
            exh_codes = True
        subs = []
        for tp in all_idx:
            rows = S3B.build_product_submodule(E, loc, tp)
            subs.append(S3B.mod_of(E.C, [S3B.unpair(E.C, tuple(r)) for r in rows]))
    say("  enumeration method : %s" % lbl_codes)
    say_local("       (enumeration took %.1fs)" % (time.time() - t_enum))
    if code_cap and len(subs) > code_cap:
        subs = rng.sample(subs, code_cap)
        exh_codes = False
        say("  #codes examined    : %d  (SAMPLED)" % len(subs))
    else:
        say("  #codes examined    : %d" % len(subs))

    # ---- the shift operators --------------------------------------------
    perm_T = [((N - 4 * t) + i) % N for i in range(N)]     # rotation by 4t
    perm_1 = [(N - 1 + i) % N for i in range(N)]           # rotation by 1
    perm_P = rev_index(t, n)

    for s in s_list:
        refl = (C.r % gcd(C.r, 2 * s)) == 0
        sub("(q,t,n,s) = (%d,%d,%d,%d):   r | 2s  =  %s"
            % (q, t, n, s, refl))

        # ---- C1..C4  the transported form --------------------------------
        J, eps = gram_transported(C, s)
        check("(%d,%d,%d,%d): the transported Gram matrix is J = I_{4n} (x) H_t"
              % (q, t, n, s), J == predicted_gram(t, n),
              "N = %d" % N, True)
        rk = len(rref([list(r) for r in J], F, N)[0])
        check("(%d,%d,%d,%d): J is non-singular (non-degeneracy of the "
              "transported form)" % (q, t, n, s), rk == N,
              "rank %d = N" % rk, True)
        if q ** N <= 70000:
            ws = all_words(C)
            exh = True
        else:
            ws = [rand_word(C, rng) for _ in range(400)]
            exh = False
        ok = all(hat_form(list(phi_n(C, x)), list(phi_n(C, y)), J, F, s)
                 == C.bs(x, y, s) for x in ws[:120] for y in ws[:120])
        check("(%d,%d,%d,%d): <phi_n x, phi_n y>^hat_s = b_s(x,y)"
              % (q, t, n, s), ok, "%d^2 pairs" % min(120, len(ws)), exh)
        # ---- C4  how far is the transported form from the standard one? --
        ident = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
        check("(%d,%d,%d,%d): the transported Gram J is the identity  <=>  t = 1"
              % (q, t, n, s), (J == ident) == (t == 1),
              "t = %d, J = I: %s" % (t, J == ident), True)
        alt = all(J[i][i] == 0 for i in range(N))
        check("(%d,%d,%d,%d): J is alternating  <=>  t is even"
              % (q, t, n, s), alt == (t % 2 == 0),
              "t = %d, alternating: %s" % (t, alt), True)
        # sigma commutes with phi
        ok_s = all(list(phi_n(C, C.sigma_word(x, s))) ==
                   sigma_hat(list(phi_n(C, x)), F, s)
                   for x in [rand_word(C, rng) for _ in range(200)])
        check("(%d,%d,%d,%d): phi_n(sigma_s x) = sigma-hat_s(phi_n x)"
              % (q, t, n, s), ok_s, "200 words", False)

        # ---- C5  the three symmetry notions (they are DIFFERENT) ---------
        #  (a) <v,u> = sigma_s(<u,v>)             <=>  r | 2s
        #  (b) the orthogonality RELATION is symmetric
        #      (<u,v> = 0 <=> <v,u> = 0)          <=>  r | 2s   ("reflexive")
        #  (c) the form is symmetric as a VALUE  (<v,u> = <u,v>)  <=>  r | s
        refl2 = ((2 * s) % C.r) == 0        # r | 2s
        refl1 = (s % C.r) == 0              # r | s
        U = [list(phi_n(C, x)) for x in ws[:50]]
        V = [list(phi_n(C, y)) for y in ws[:50]]
        ok_a = all(hat_form(v, u, J, F, s) ==
                   F.frob[s % C.r][hat_form(u, v, J, F, s)]
                   for u in U for v in V)
        ok_b = all((hat_form(u, v, J, F, s) == 0) ==
                   (hat_form(v, u, J, F, s) == 0) for u in U for v in V)
        ok_c = all(hat_form(v, u, J, F, s) == hat_form(u, v, J, F, s)
                   for u in U for v in V)
        check("(%d,%d,%d,%d): (a) <v,u>^hat = sigma_s(<u,v>^hat)  <=>  r | 2s"
              % (q, t, n, s), ok_a == refl2,
              "r|2s = %s, observed %s" % (refl2, ok_a), exh)
        check("(%d,%d,%d,%d): (b) orthogonality relation symmetric  <=>  r | 2s"
              % (q, t, n, s), ok_b == refl2,
              "r|2s = %s, observed %s" % (refl2, ok_b), exh)
        check("(%d,%d,%d,%d): (c) form symmetric as a value  <=>  r | s"
              % (q, t, n, s), ok_c == refl1,
              "r|s = %s, observed %s" % (refl1, ok_c), exh)

        # ---- C5b  can a linear change of coordinates make J = I ? --------
        # This is a CONGRUENCE question (in the bilinear case r | s):
        #     T^T J T = I .   Only a monomial T preserves the Hamming weight,
        # and no permutation can do it (the u-adic pairing reverses a and
        # t-1-a), so there is a genuine trade-off: standard form vs. weights.
        T_blk = find_block_congruence(t, F, rng)
        if T_blk is not None:
            say("       a per-block congruence T with T^T H_t T = I_t EXISTS "
                "for (q,t) = (%d,%d)" % (q, t))
            mono = is_monomial(T_blk, F)
            say("       T is %s  =>  it %s the Hamming weight"
                % ("monomial" if mono else "NOT monomial",
                   "preserves" if mono else "does NOT preserve"))
            TB = block_diag_expand(T_blk, t, n, F)     # I_{4n} (x) T
            JT = matmul_F(matmul_F(transpose_F(TB), J, F), TB, F)
            check("(%d,%d,%d,%d): (I (x) T)^T J (I (x) T) = I  "
                  "(bilinear case)" % (q, t, n, s), JT == ident,
                  "N = %d" % N, True)
            # does it commute with the block shift?
            ST = perm_matrix(perm_T, N, F)
            ok_comm = matmul_F(TB, ST, F) == matmul_F(ST, TB, F)
            check("(%d,%d,%d,%d): (I (x) T) commutes with the block shift "
                  "That (the image stays quasi-cyclic)" % (q, t, n, s),
                  ok_comm, "N = %d" % N, True)
            # and in the sesquilinear case the requirement is sigma_s(T)^T J T = I
            if s % C.r != 0:
                TBs = [[F.frob[s % C.r][x] for x in row] for row in TB]
                JTs = matmul_F(matmul_F(transpose_F(TBs), J, F), TB, F)
                say("       for s = %d (sigma_s != id) the same T gives "
                    "sigma_s(T)^T J T = I :  %s" % (s, JTs == ident))
        else:
            say("       NO per-block congruence T^T H_t T = I_t exists for "
                "(q,t) = (%d,%d)  (search %s)" % (q, t,
                "exhaustive" if q ** (t * t) <= 300000 else "sampled"))
            if F.p == 2 and t % 2 == 0:
                say("       (proved impossible: J is alternating in "
                    "characteristic 2, the standard form is not)")

        # ---- C6, D1  per-code checks -------------------------------------
        nC = nD = nDim = nE = nQc = nCyc = 0
        euc_mis = herm_mis = 0
        mu_hull_dist = {}
        mu = 0
        witnesses = []
        scan_mu = len(subs) <= 2000
        badC = badD = None
        dist_stats = []
        dist_cand = []
        so_count = 0          # self-orthogonal w.r.t. the transported form
        euc_so_count = 0      # self-orthogonal w.r.t. the Euclidean form
        herm_so_count = 0     # self-orthogonal w.r.t. plain sigma_s-Hermitian
        lcd = 0
        sd = 0
        nonzero = 0
        t_case = time.time()
        for W in subs:
            A = img_basis(E, C, W)                    # phi_n(C)
            k = len(A)
            if k == 0:
                continue
            nonzero += 1
            # --- route 1: the annihilator (no transported form used)
            D1 = dual_img(E, C, W, s)
            # --- route 2: the orthogonal of phi_n(C) for the transported form
            D2 = orth_hat(A, J, F, N, s)
            if rows_key(D1, F, N) == rows_key(D2, F, N):
                nC += 1
            elif badC is None:
                badC = (k, rows_key(D1, F, N), rows_key(D2, F, N))
            if k + len(D2) != N:
                nDim += 1
            # --- hull, route 1 (Morita / annihilator, Stage 3B)
            dimH, inter, Wp, hull_rn = S3B.hull_by_morita(E, W, s)
            H1 = img_from_rn_basis(C, hull_rn) if hull_rn else []
            # --- hull, route 2 (intersection in F_q^N)
            H2 = S3B.intersect_rows(C, A, D2, N) if (A and D2) else []
            if rows_key(H1, F, N) == rows_key(H2, F, N):
                nD += 1
            elif badD is None:
                badD = (k, dimH, len(H2))
            # --- structure of the image (Task E): invariance under the
            # block shift (rotation by 4t) and under the shift by 1

            AT = rref([apply_perm(r, perm_T) for r in A] +
                      [list(x) for x in A], F, N)[0]
            if len(AT) == k:
                nQc += 1
            A1 = rref([apply_perm(r, perm_1) for r in A] +
                      [list(x) for x in A], F, N)[0]
            if len(A1) == k:
                nCyc += 1
            # --- quantum-relevant statistics (Task F)
            if k + len(D2) == N and len(S3B.intersect_rows(C, A, D2, N)) == k:
                so_count += 1
            if len(S3B.intersect_rows(C, A, D2, N)) == 0:
                lcd += 1
            if rows_key(A, F, N) == rows_key(D2, F, N):
                sd += 1
            De = orth_euclid(A, F, N)
            if rows_key(De, F, N) != rows_key(D2, F, N):
                euc_mis += 1
            if len(S3B.intersect_rows(C, A, De, N)) == k:
                euc_so_count += 1
            # self-orthogonality for the PLAIN sigma_s-Hermitian form
            # (Gram = I, no Hankel twist) on the image itself:
            Dh = orth_herm(A, F, N, s)
            if rows_key(Dh, F, N) != rows_key(D2, F, N):
                herm_mis += 1
            if len(S3B.intersect_rows(C, A, Dh, N)) == k:
                herm_so_count += 1
            # ---- Task D: record the NON-PRINCIPAL hulls (mu_B >= 3) ------
            if scan_mu and inter:
                Wh = {"rows": tuple(tuple(r) for r in inter),
                      "dim": len(inter), "gens": []}
                mu = E.mu(Wh)
                if mu >= 3:
                    witnesses.append((W, k, dimH, mu, inter,
                                      rows_key(H1, F, N) == rows_key(H2, F, N)))
            mu_hull_dist[mu if (scan_mu and inter) else 0] = \
                mu_hull_dist.get(mu if (scan_mu and inter) else 0, 0) + 1
            # --- minimum distances (Task E): collected, then sampled
            if do_dist and k > 0 and q ** k <= dist_cap:
                dist_cand.append(A)
            if time.time() - t_case > 900:
                say("       (time cap reached: %d codes processed)" % nonzero)
                say_local("       time cap at %.0fs" % (time.time() - t_case))
                exh_codes = False
                break

        check("(%d,%d,%d,%d): phi_n(C^{perp_s}) = phi_n(C)^{perp_hat_s} "
              "for all codes (2 independent routes)" % (q, t, n, s),
              nC == nonzero, "%d / %d codes" % (nC, nonzero), exh_codes)
        check("(%d,%d,%d,%d): dim phi_n(C) + dim phi_n(C)^{perp_hat_s} = N"
              % (q, t, n, s), nDim == 0, "%d violations" % nDim, exh_codes)
        check("(%d,%d,%d,%d): phi_n(Hull_s(C)) = phi_n(C) cap "
              "phi_n(C)^{perp_hat_s} for all codes" % (q, t, n, s),
              nD == nonzero, "%d / %d codes" % (nD, nonzero), exh_codes)
        check("(%d,%d,%d,%d): the image is invariant under the block shift "
              "That (quasi-cyclic of index 4t)" % (q, t, n, s),
              nQc == nonzero, "%d / %d codes" % (nQc, nonzero), exh_codes)
        say("       #nonzero codes                    : %d" % nonzero)
        say("       #images invariant under shift by 1: %d  (cyclic)" % nCyc)
        say("       #self-orthogonal (transported form): %d" % so_count)
        say("       #self-dual     (transported form)  : %d" % sd)
        say("       #LCD          (transported form)   : %d" % lcd)
        say("       #self-orthogonal (EUCLIDEAN form)   : %d" % euc_so_count)
        say("       #self-orthogonal (plain sigma_s-Hermitian, Gram I): %d"
            % herm_so_count)
        say("       NEGATIVE CONTROL: #codes where the EUCLIDEAN orthogonal "
            "of the image differs from phi_n(C^{perp_s}): %d" % euc_mis)
        say("       NEGATIVE CONTROL: #codes where the plain Hermitian "
            "(Gram I) orthogonal differs from phi_n(C^{perp_s}): %d"
            % herm_mis)
        if scan_mu and mu_hull_dist:
            say("       mu_B(Hull_s(C)) distribution over the codes with a "
                "nonzero hull: %s" % {k: v for k, v in sorted(mu_hull_dist.items()) if k})
        if witnesses:
            say("")
            say("       ---- %d code(s) whose Galois hull is NOT principal "
                "(mu_B >= 3) ----" % len(witnesses))
            for (W, k, dimH, mu, inter, ok) in witnesses:
                say("         dim C = %d, dim Hull = %d, mu_B(Hull) = %d, "
                    "hull compatibility holds: %s" % (k, dimH, mu, ok))
                for g in E.gens_of({"rows": tuple(tuple(r) for r in inter),
                                    "dim": len(inter), "gens": []})[:4]:
                    say("            hull generator (over B): %s"
                        % (tuple(tuple(x) for x in g),))
            check("(%d,%d,%d,%d): hull compatibility holds for EVERY "
                  "non-principal hull (mu_B >= 3) as well"
                  % (q, t, n, s), all(w[5] for w in witnesses),
                  "%d witnesses" % len(witnesses), True)
            say("       => no principality hypothesis is used anywhere in "
                "Task C or Task D")
        if dist_cand:
            sampled = len(dist_cand) > dist_max_codes
            if sampled:
                dist_cand = rng.sample(dist_cand, dist_max_codes)
            for A2 in dist_cand:
                dist_stats.append(min_distances(C, A2))
            eq = sum(1 for a, b in dist_stats if a == b)
            say("       min distances (%s %d codes, |C| <= %d): "
                "d_Ham(image) = ring-Hamming distance on %d of them"
                % ("SAMPLED" if sampled else "all", len(dist_stats),
                   dist_cap, eq))
            say("       examples (d_Ham(phi_n C), ring-Hamming d(C)): %s"
                % dist_stats[:6])
        if badC is not None:
            note("first duality mismatch: dim = %d" % badC[0])
        if badD is not None:
            note("first hull mismatch: dim = %d, dim Hull = %d, "
                 "dim intersection = %d" % badD)
    return E, subs


def min_distances(C, A):
    """(d_Hamming of the image code, ring-Hamming distance of C)"""
    F = C.F
    N = 4 * C.t * C.n
    k = len(A)
    best_img = None
    best_ring = None
    for v in range(F.q ** k):
        coef = [(v // (F.q ** i)) % F.q for i in range(k)]
        if not any(coef):
            continue
        u = [0] * N
        for i, c in enumerate(coef):
            if c:
                Ai = A[i]
                for j in range(N):
                    if Ai[j]:
                        u[j] = F.add[u[j]][F.mul[c][Ai[j]]]
        w = sum(1 for x in u if x)
        if best_img is None or w < best_img:
            best_img = w
        x = C.unflat_word(u)
        wr = w_Hamming(C, x)
        if best_ring is None or wr < best_ring:
            best_ring = wr
    return best_img, best_ring


# ==========================================================================
# 5.  Part G -- summary of the negative controls
# ==========================================================================

def task_g_summary():
    head("PART G -- negative controls (what FAILS, and why)")
    say("  C1  the Euclidean form on F_q^N is NOT the transported form unless")
    say("      t = 1 and r | s:  J = I_{4n} (x) H_t = I  <=>  t = 1, and the")
    say("      sigma_s-twist is trivial  <=>  r | s.  Measured per family above")
    say("      ('#codes where the EUCLIDEAN orthogonal ... differs').")
    say("  C2  the plain sigma_s-Hermitian form (Gram = I, no Hankel twist) is")
    say("      NOT the transported form unless t = 1 (same counter above).")
    say("  C3  phi_n is NOT a ring-Hamming isometry:  w_H(x) <= wt_Ham(phi_n x)")
    say("      <= 4t w_H(x), and both bounds are attained; the count of words")
    say("      with wt_Ham(phi_n x) != w_H(x) is reported per family.")
    say("  C4  NO map into a Hamming space can be an isometry for the")
    say("      homogeneous weight: w_hom takes the non-integral values")
    say("      1 + 1/(q^2-1) and 1 - 1/((q-1)^2(q+1)) on R = M_2(F_q)")
    say("      (verified exhaustively for q = 4, 8, 9), while Hamming weights")
    say("      are integers.")
    say("  C5  the image of a code is NOT in general a cyclic code: it is")
    say("      quasi-cyclic of index 4t and co-index n, and the number of codes")
    say("      whose image IS invariant under the shift by 1 is reported per")
    say("      family (typically a small minority).")
    say("  C6  phi_n is F_q-linear, NOT R-linear: the target F_q^{4tn} carries")
    say("      no R-module structure; what survives is the transported left")
    say("      regular representation a |-> M_L(a), an injective ring")
    say("      homomorphism R -> M_{4t}(F_q) (checked above).")


# ==========================================================================
# 6.  main
# ==========================================================================

CASES_A = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (8, 1, 2), (9, 1, 2),
           (4, 1, 3), (4, 2, 2)]
CASES_B = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (8, 1, 2), (9, 1, 2),
           (4, 1, 3), (4, 2, 2)]
CASES_C = [(4, 1, 1, [0, 1]),
           (4, 1, 2, [0, 1]),
           (4, 2, 1, [0, 1]),
           (8, 1, 2, [0, 1, 2]),
           (9, 1, 2, [0, 1]),
           (4, 1, 3, [0, 1]),
           (9, 2, 1, [0, 1]),
           (4, 2, 2, [0, 1]),
           (4, 2, 3, [0, 1])]


def main():
    t0 = time.time()
    rng = random.Random(SEED)
    say("=" * 78)
    say("PHASE 4 -- GRAY MAP COMPATIBILITY AND FINITE-FIELD CODE CONSTRUCTION")
    say("independent computational corroboration of")
    say("03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md")
    say("=" * 78)
    say("  seed                     : %d" % SEED)
    say("  python                   : %s" % sys.version.split()[0])
    say("  conventions              : A_t = F_q[u]/<u^t>, R = M_2(A_t),")
    say("                             R_n = R[X]/<X^n - 1>, C = I_W a right")
    say("                             ideal of R_n (Morita), word length n;")
    say("                             (Tx)_e = x_{e-1 mod n};")
    say("                             b_s(x,y) = Lambda(sum_e theta_s(x_e) y_e)")
    say("                             with Lambda = lambda o tr, lambda(a) = a_{t-1}.")
    say("  the map under study      : phi_n = coefficient expansion")
    say("                             R^n -> F_q^N,  N = 4tn,")
    say("                             coordinate ((e*4 + k)*t + a).")
    say("  [EXH] = exhaustive over the stated finite set;")
    say("  [SMP] = verified on a seeded random sample.")
    say("  timing lines are written to stdout only, so two runs of this script")
    say("  produce byte-identical logs.")

    say("")
    say("")
    head("PART A -- TASK A: the candidate maps and their properties")
    for (q, t, n) in CASES_A:
        task_a_maps(q, t, n, rng)

    say("")
    say("")
    head("PART B -- TASK B: the weight structure")
    for (q, t, n) in CASES_B:
        task_b_weights(q, t, n, rng)

    say("")
    say("")
    head("PARTS C, D, E, F -- the transported form, hull compatibility, the")
    say("                     image codes, and the quantum-relevant conditions")
    for (q, t, n, sl) in CASES_C:
        run_case_p4(q, t, n, sl, rng,
                     code_cap=400 if (q, t, n) == (4, 2, 3) else None)

    task_g_summary()

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
