#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 2 -- STAGE 1 verification: cyclic-code definitions and the shift structure.

Companion to 03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md, authorised by
PHASE2_PROPOSAL_v2.md sections 1-2 (P-2.1).  SCOPE: definitions, the cyclic
shift, left/right action conventions, centrality of X, and sigma_k/theta_s
compatibility.  Explicitly OUT of scope here: P-2.3 (generator numbers),
CRT/Hensel (P-2.4), principality (P-2.5/P-2.6), duals and annihilators
(P-2.7/P-2.8 -- hence L-6.1, "theta_s is an anti-automorphism of R_n", is NOT
tested here), hulls, Gray maps, quantum, and the enumeration conjecture C-2.1.

Everything is recomputed from the definitions.  The arithmetic (Field, Local,
MatRing) and the F_q-linear algebra (rref, span_of, enumerate_subspaces) are
imported from ring_structure_checks.py (401/401 there); B = A_t[X]/<X^n-1>,
M_2(B) and every check below are built here.

  Part 0  representation: iota, cyclic convolution, X^n = 1, centrality of X.
  Part 1  the shift: T^n = 1, T = right AND left multiplication by X, T is a
          Hamming isometry, F_q-linearity, right/left R-linearity, R_n-linearity,
          and a negative control showing what centrality buys.
  Part 2  the equivalence {right ideals of R_n} <-> {T-invariant right
          R-submodules of R^n}: both directions, round trip, negative controls
          showing that BOTH conditions are needed, and a brute-force census over
          ALL F_q-subspaces at (q,t,n) = (4,1,1).
  Part 3  automorphism compatibility: sigma_k and theta_s versus T, versus the
          right and the left action, semilinearity, and the side-swapping rule
          theta_s rho_a = lambda_{theta_s(a)} theta_s, with negative controls
          proving that this is NOT ordinary commutation.
  Part 4  the boundary case n = 1.

Usage:  cd 04_COMPUTATION && python3 phase2_stage1_shift_checks.py
Log:    04_COMPUTATION/phase2_stage1_shift_log.txt     (seed is fixed: 20261104)
"""

import itertools
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ring_structure_checks import (Field, Local, MatRing, rref,
                                   enumerate_subspaces,
                                   check, say, LINES, FAILURES, NCHECK)

SEED = 20261104

# sampling budgets (change only together with the log: they are reported there)
AMB_EXH = 20000      # exhaust over R^n when q^(4tn) <= this
RING_EXH = 20000     # exhaust over R   when q^(4t)  <= this
BUDGET_PAIRS = 20000 # sampled (x, a) pairs elsewhere
FULL_PAIRS = 70000   # exhaust over (x, a) pairs when the product is <= this
SAMPLE = 500         # sample size for R^n when not exhaustive
SAMPLE_R = 400       # sample size for R when not exhaustive
SAMPLE_S = 200       # sample size for R_n when not exhaustive


# ==========================================================================
# B = A_t[X]/<X^n - 1>   and   S = M_2(B) = R_n      (built from scratch)
# ==========================================================================

class PolyQuot(object):
    """B = A_t[X]/<X^n - 1>;  an element is an n-tuple of elements of A_t."""

    def __init__(self, A, n):
        self.A, self.n, self.t, self.F, self.q = A, n, A.t, A.F, A.F.q
        self.zero = tuple([A.zero] * n)
        self.one = tuple([A.one] + [A.zero] * (n - 1))
        self.X = tuple([A.zero, A.one] + [A.zero] * (n - 2)) if n > 1 else self.one
        self.u = tuple([A.u] + [A.zero] * (n - 1))

    def add(self, a, b):
        A = self.A
        return tuple(A.add(a[i], b[i]) for i in range(self.n))

    def neg(self, a):
        return tuple(self.A.neg[x] for x in a)

    def mul(self, a, b):
        """cyclic convolution:  coef of X^e is sum_{i+j = e mod n} a_i b_j"""
        A, n = self.A, self.n
        out = [A.zero] * n
        for i in range(n):
            if a[i] != A.zero:
                for j in range(n):
                    if b[j] != A.zero:
                        e = (i + j) % n
                        out[e] = A.add(out[e], A.mul(a[i], b[j]))
        return tuple(out)

    def pow(self, a, e):
        res, base = self.one, a
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def sigma(self, a, s):
        return tuple(self.A.sigma(x, s) for x in a)

    def vec(self, a):
        out = []
        for x in a:
            out.extend(x)
        return tuple(out)

    def elem_list(self):
        return list(itertools.product(self.A.elem_list(), repeat=self.n))


class Mat2B(object):
    """S = M_2(B) = R_n;  an element is a 4-tuple of B-elements, row-major."""

    def __init__(self, B):
        self.B, self.n, self.t, self.F, self.q = B, B.n, B.t, B.F, B.F.q
        self.d = 4 * B.n * B.t                 # dim_{F_q} of R_n (and of R^n)
        z, o = B.zero, B.one
        self.zero = (z, z, z, z)
        self.one = (o, z, z, o)
        self.XI = (B.X, z, z, B.X)             # X * I_2
        self.uI = (B.u, z, z, B.u)

    def unit(self, i, j, c=None):
        B = self.B
        c = B.one if c is None else c
        return tuple([c if (a == i and b == j) else B.zero
                      for a in range(2) for b in range(2)])

    def add(self, X, Y):
        B = self.B
        return tuple(B.add(X[k], Y[k]) for k in range(4))

    def neg(self, X):
        return tuple(self.B.neg(x) for x in X)

    def mul(self, X, Y):
        B = self.B
        out = []
        for i in range(2):
            for j in range(2):
                acc = B.zero
                for k in range(2):
                    xk, yk = X[2 * i + k], Y[2 * k + j]
                    if xk != B.zero and yk != B.zero:
                        acc = B.add(acc, B.mul(xk, yk))
                out.append(acc)
        return tuple(out)

    def pow(self, X, e):
        res, base = self.one, X
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def sigma(self, X, s):
        return tuple(self.B.sigma(x, s) for x in X)

    def transpose(self, X):
        return (X[0], X[2], X[1], X[3])

    def theta(self, X, s):
        return self.sigma(self.transpose(X), s)

    def vec(self, X):
        out = []
        for x in X:
            out.extend(x)
        return tuple(out)

    def flat(self, Z):
        """Z as a flat F_q-coordinate vector of length dim = 4 n t"""
        out = []
        for b in Z:
            for a in b:
                out.extend(a)
        return tuple(out)

    def unflat(self, v):
        w = self.B.t * self.B.n               # F_q-coordinates per B entry
        bs = [tuple(v[k * w:(k + 1) * w]) for k in range(4)]
        return tuple(tuple(tuple(b[j * self.B.t:(j + 1) * self.B.t])
                           for j in range(self.B.n)) for b in bs)

    def elem_list(self):
        return list(itertools.product(self.B.elem_list(), repeat=4))


# ==========================================================================
# the ambient package for one (p, r, t, n)
# ==========================================================================

class Amb(object):
    """everything needed for one parameter set, built from scratch."""

    def __init__(self, p, r, t, n, seed=SEED):
        self.p, self.r, self.t, self.n = p, r, t, n
        self.q = p ** r
        self.seed = seed
        self.F = Field(p, r)
        self.A = Local(self.F, t)
        self.R = MatRing(self.A, 2)            # R = M_2(A_t)
        self.B = PolyQuot(self.A, n)           # B = A_t[X]/<X^n-1>
        self.S = Mat2B(self.B)                 # R_n = M_2(B)
        self.d = 4 * t * n                     # dim_{F_q} R^n
        self.rng = random.Random(seed)
        self._all_R = None
        self._cI = {}
        self._pairs = None
        self._xs = None
        self._as = None
        self._zs = None
        # F_q-algebra generators of R: the four matrix units, plus uI when t > 1
        self.Rgens = [self.R.unit(i, j) for i in range(2) for j in range(2)]
        if t > 1:
            self.Rgens.append(self.R.scalar_mat(self.A.u))
        # F_q-algebra generators of R_n: the embedded ones, plus X*I
        self.Sgens = [self.emb(a) for a in self.Rgens] + [self.S.XI]
        # the two families of operators on R^n
        self.ops_right = [self._mk_right(a) for a in self.Rgens]
        self.ops_left = [self._mk_left(a) for a in self.Rgens]
        self.ops_T = [self.T]

    def _mk_right(self, a):
        return lambda x, a=a: self.right_action(x, a)

    def _mk_left(self, a):
        return lambda x, a=a: self.left_action(x, a)

    # ----- scalars -------------------------------------------------------
    def scalar_R(self, c):
        """c in F_q  ->  c*I in R"""
        if c not in self._cI:
            self._cI[c] = self.R.scalar_mat(self.A.scalar(c, self.A.one))
        return self._cI[c]

    # ----- the coefficient representation --------------------------------
    def emb(self, a):
        """a in R = M_2(A_t) -> the same matrix with constant polynomial entries"""
        n, z = self.n, self.A.zero
        return tuple(tuple([x] + [z] * (n - 1)) for x in a)

    def coef(self, Z, e):
        """the R-valued coefficient of X^e in Z in M_2(B)"""
        return tuple(Z[k][e] for k in range(4))

    def iota(self, x):
        """iota(x) = sum_e emb(x_e) (X I)^e   -- computed by ring multiplication"""
        S, n, R = self.S, self.n, self.R
        out, Xpow = S.zero, S.one
        for e in range(n):
            if x[e] != R.zero:
                out = S.add(out, S.mul(self.emb(x[e]), Xpow))
            Xpow = S.mul(Xpow, S.XI)
        return out

    def iota_fast(self, x):
        """the same map by rearrangement: (iota x)_{ij,e} = (x_e)_{ij}"""
        n = self.n
        cols = [[self.A.zero] * n for _ in range(4)]
        for e in range(n):
            for k in range(4):
                cols[k][e] = x[e][k]
        return tuple(tuple(c) for c in cols)

    def iota_inv(self, Z):
        return tuple(self.coef(Z, e) for e in range(self.n))

    # ----- vectors in R^n -------------------------------------------------
    def right_action(self, x, a):
        """(x . a)_e = x_e a"""
        R = self.R
        return tuple(R.mul(x[e], a) for e in range(self.n))

    def left_action(self, x, a):
        """(a . x)_e = a x_e"""
        R = self.R
        return tuple(R.mul(a, x[e]) for e in range(self.n))

    def scalar_mult(self, c, x):
        """c in F_q acts through cI in Z(R)"""
        return self.right_action(x, self.scalar_R(c))

    def T(self, x):
        """(Tx)_e = x_{e-1 mod n}   (the Phase-1 convention)"""
        n = self.n
        return tuple(x[(e - 1) % n] for e in range(n))

    def Tinv(self, x):
        n = self.n
        return tuple(x[(e + 1) % n] for e in range(n))

    def vadd(self, x, y):
        R = self.R
        return tuple(R.add(x[e], y[e]) for e in range(self.n))

    def vsig(self, x, k):
        R = self.R
        return tuple(R.sigma(x[e], k) for e in range(self.n))

    def vtheta(self, x, s):
        R = self.R
        return tuple(R.theta(x[e], s) for e in range(self.n))

    def vec(self, x):
        """x in R^n as a flat F_q-coordinate vector of length dim = 4tn"""
        out = []
        for v in x:                       # v is in R: 4 entries of A_t
            for a in v:                   # a is in A_t: t entries of F_q
                out.extend(a)
        return tuple(out)

    def unvec(self, v):
        dR = 4 * self.t                   # F_q-coordinates per entry of R
        coords = [tuple(v[e * dR:(e + 1) * dR]) for e in range(self.n)]
        return tuple(tuple(tuple(c[k * self.t:(k + 1) * self.t]) for k in range(4))
                     for c in coords)

    def weight(self, x):
        return sum(1 for e in range(self.n) if x[e] != self.R.zero)

    # ----- pools ----------------------------------------------------------
    def all_R(self):
        if self._all_R is None:
            self._all_R = self.R.elem_list()
        return self._all_R

    def xs(self):
        """(pool of elements of R^n, exhaustive?)"""
        if self._xs is None:
            allR = self.all_R()
            if len(allR) ** self.n <= AMB_EXH:
                self._xs = ([tuple(v) for v in itertools.product(allR, repeat=self.n)],
                            True)
            else:
                pool = []
                seen = set()
                while len(pool) < SAMPLE and len(seen) < len(allR) ** self.n:
                    v = self.rand_vec()
                    if v not in seen:
                        seen.add(v)
                        pool.append(v)
                self._xs = (pool, False)
        return self._xs

    def as_(self):
        """(pool of elements of R, exhaustive?)"""
        if self._as is None:
            allR = self.all_R()
            if len(allR) <= RING_EXH:
                self._as = (allR, True)
            else:
                self._as = ([self.rng.choice(allR) for _ in range(SAMPLE_R)], False)
        return self._as

    def zs(self):
        """(pool of elements of R_n, exhaustive?)"""
        if self._zs is None:
            if self.q ** (4 * self.t * self.n) <= AMB_EXH:
                self._zs = (self.S.elem_list(), True)
            else:
                self._zs = ([self.rand_S() for _ in range(SAMPLE_S)], False)
        return self._zs

    def pairs(self, budget=BUDGET_PAIRS):
        """(list of (x, a) in R^n x R, exhaustive?)"""
        if self._pairs is not None:
            return self._pairs
        xs, exh_x = self.xs()
        as_, exh_a = self.as_()
        if exh_x and exh_a and len(xs) * len(as_) <= FULL_PAIRS:
            self._pairs = ([(x, a) for x in xs for a in as_], True)
        else:
            self._pairs = ([(self.rng.choice(xs), self.rng.choice(as_))
                            for _ in range(budget)], False)
        return self._pairs

    # ----- random elements -------------------------------------------------
    def rand_R(self):
        A = self.A
        el = A.elem_list()
        return tuple(el[self.rng.randrange(len(el))] for _ in range(4))

    def rand_vec(self):
        return tuple(self.rand_R() for _ in range(self.n))

    def rand_S(self):
        B = self.B
        el = B.elem_list()
        return tuple(el[self.rng.randrange(len(el))] for _ in range(4))


# ==========================================================================
# F_q-linear algebra: subspaces of R^n  and right ideals of R_n
# ==========================================================================

def closure(amb, seeds, ops):
    """smallest F_q-subspace of R^n containing seeds and closed under ops.

    Returns (RREF basis as a tuple of tuples, F_q-dimension).
    """
    d, F = amb.d, amb.F
    rows = [list(amb.vec(x)) for x in seeds]
    while True:
        Bm, _ = rref(rows, F, d)
        cur = [amb.unvec(tuple(b)) for b in Bm]
        new = [list(b) for b in Bm]
        for x in cur:
            for op in ops:
                new.append(list(amb.vec(op(x))))
        B2, _ = rref(new, F, d)
        if len(B2) == len(Bm):
            return tuple(tuple(b) for b in B2), len(B2)
        rows = new


def is_closed(amb, rows, ops):
    """is the F_q-span of `rows` (R^n coordinates) closed under ops?"""
    F, d = amb.F, amb.d
    Bm, _ = rref([list(b) for b in rows], F, d)     # a basis of the span
    for b in Bm:
        v = amb.unvec(tuple(b))
        for op in ops:
            w = amb.vec(op(v))
            M, _ = rref(list(Bm) + [list(w)], F, d)
            if len(M) != len(Bm):
                return False
    return True


def canon_v(amb, vecs_in_S):
    """RREF basis (in R_n coordinates) of the F_q-span of elements of R_n"""
    Bm, _ = rref([list(amb.S.flat(Z)) for Z in vecs_in_S], amb.F, amb.d)
    return tuple(tuple(b) for b in Bm)


def right_ideal(amb, seeds):
    """smallest right ideal of R_n containing seeds: (basis, dim)"""
    S, d, F = amb.S, amb.d, amb.F
    rows = [list(S.flat(Z)) for Z in seeds]
    while True:
        Bm, _ = rref(rows, F, d)
        cur = [S.unflat(tuple(b)) for b in Bm]
        new = [list(b) for b in Bm]
        for Z in cur:
            for G in amb.Sgens:
                new.append(list(S.flat(S.mul(Z, G))))
        B2, _ = rref(new, F, d)
        if len(B2) == len(Bm):
            return tuple(tuple(b) for b in B2), len(B2)
        rows = new


def is_right_ideal(amb, basis_rows_in_S):
    for b in basis_rows_in_S:
        Z = amb.S.unflat(tuple(b))
        for G in amb.Sgens:
            W = amb.S.mul(Z, G)
            M, _ = rref(list(basis_rows_in_S) + [list(amb.S.flat(W))], amb.F, amb.d)
            if len(M) != len(basis_rows_in_S):
                return False
    return True


# ==========================================================================
# Part 0 -- representation, convolution, centrality
# ==========================================================================

def part0(amb, tag):
    say("")
    say("-" * 90)
    say("Part 0  representation: iota, convolution, X^n = 1, centrality of X   %s" % tag)
    say("-" * 90)
    S, R, B, A, F = amb.S, amb.R, amb.B, amb.A, amb.F
    n = amb.n

    # 0.1  iota
    xs, exh = amb.xs()
    ok_bij = ok_fast = True
    seen = set()
    for x in xs:
        Z = amb.iota(x)
        seen.add(Z)
        if amb.iota_fast(x) != Z:
            ok_fast = False
        if amb.iota_inv(Z) != x:
            ok_bij = False
    # NB: |image| is compared with the number of DISTINCT vectors in the pool --
    # a sampled pool may repeat a vector, which says nothing about iota.
    check("iota: iota_inv(iota(x)) = x   (two-sided inverse on the pool)",
          ok_bij, "N=%d" % len(xs), exhaustive=exh)
    check("iota is injective on the pool (|image| = #distinct vectors tested)",
          len(seen) == len(set(xs)), "N=%d distinct" % len(set(xs)), exhaustive=exh)
    check("iota: the polynomial definition agrees with (iota x)_{ij,e} = (x_e)_{ij}",
          ok_fast, "N=%d" % len(xs), exhaustive=exh)
    if exh:
        check("iota is surjective (|image| = q^(4tn) = |R^n|)",
              len(seen) == amb.q ** (4 * amb.t * n),
              "q^(4tn)=%d" % amb.q ** (4 * amb.t * n), exhaustive=True)

    # 0.2  multiplication in B is the cyclic convolution
    bp = B.elem_list()
    stride = max(1, len(bp) // 40)
    pairs = [(bp[i], bp[j])
             for i in range(0, len(bp), stride) for j in range(0, len(bp), stride)]
    full = (stride == 1)
    conv_ok = True
    for (a, b) in pairs:
        c = B.mul(a, b)
        for e in range(n):
            acc = A.zero
            for i in range(n):
                for j in range(n):
                    if (i + j) % n == e:
                        acc = A.add(acc, A.mul(a[i], b[j]))
            if acc != c[e]:
                conv_ok = False
    check("B: multiplication is the cyclic convolution (coef_e = sum_{i+j=e mod n} a_i b_j)",
          conv_ok, "%d pairs" % len(pairs), exhaustive=full)
    check("B is commutative", all(B.mul(a, b) == B.mul(b, a) for (a, b) in pairs),
          "%d pairs" % len(pairs), exhaustive=full)

    # 0.3  X^n = 1
    check("B: X^n = 1", B.pow(B.X, n) == B.one, "n=%d" % n, exhaustive=True)
    check("R_n: (X I)^n = I", S.pow(S.XI, n) == S.one, "n=%d" % n, exhaustive=True)

    # 0.4  centrality of X in R_n  (the load-bearing fact of Stage 1)
    zs, exhZ = amb.zs()
    ok_c = all(S.mul(S.XI, Z) == S.mul(Z, S.XI) for Z in zs)
    check("R_n: (X I) Z = Z (X I) for all Z   [centrality of X]", ok_c,
          "N=%d" % len(zs), exhaustive=exhZ)

    # 0.5  emb: R -> R_n is an injective ring homomorphism, and iota is
    #      additive and R-linear on BOTH sides (used by the equivalence)
    ap, exhA = amb.as_()
    ap = ap[:60]
    check("emb: R -> R_n is a ring homomorphism (additive and multiplicative)",
          all(amb.emb(R.add(a, b)) == S.add(amb.emb(a), amb.emb(b))
              and amb.emb(R.mul(a, b)) == S.mul(amb.emb(a), amb.emb(b))
              for a in ap for b in ap), "N=3600", exhaustive=False)
    check("emb: R -> R_n is injective",
          len(set(amb.emb(a) for a in ap)) == len(ap),
          "N=%d" % len(ap), exhaustive=False)
    prs, exhP = amb.pairs(budget=4000)
    check("iota is additive:  iota(x+y) = iota(x) + iota(y)",
          all(amb.iota(amb.vadd(x, y)) == S.add(amb.iota(x), amb.iota(y))
              for (x, y) in [(x, prs[(3 * i) % len(prs)][0]) for i, (x, a) in enumerate(prs)]),
          "N=%d" % len(prs), exhaustive=False)
    check("iota is RIGHT R-linear:  iota(x.a) = iota(x) emb(a)",
          all(amb.iota(amb.right_action(x, a)) == S.mul(amb.iota(x), amb.emb(a))
              for (x, a) in prs), "N=%d" % len(prs), exhaustive=False)
    check("iota is LEFT  R-linear:  iota(a.x) = emb(a) iota(x)",
          all(amb.iota(amb.left_action(x, a)) == S.mul(amb.emb(a), amb.iota(x))
              for (x, a) in prs), "N=%d" % len(prs), exhaustive=False)

    # 0.6  the operator statement "XT = TX": L_X and R_X commute (associativity)
    #      and coincide (centrality)
    zs2 = zs[:200]
    check("operators: L_X R_X = R_X L_X  (associativity, no centrality needed)",
          all(S.mul(S.XI, S.mul(Z, S.XI)) == S.mul(S.mul(S.XI, Z), S.XI)
              for Z in zs2), "N=%d" % len(zs2), exhaustive=False)
    check("operators: L_X = R_X  (this IS centrality)",
          all(S.mul(S.XI, Z) == S.mul(Z, S.XI) for Z in zs2), "N=%d" % len(zs2),
          exhaustive=False)

    # 0.7  R_n is generated, as a ring, by R and X: the right ideal generated by
    #      1 is everything (sanity for the closure computations of Part 2)
    _, d1 = right_ideal(amb, [S.one])
    check("R_n: the right ideal generated by 1 is all of R_n (dim = 4tn)",
          d1 == amb.d, "dim=%d, 4tn=%d" % (d1, amb.d), exhaustive=True)


# ==========================================================================
# Part 1 -- the shift
# ==========================================================================

def part1(amb, tag, extra_exh=False):
    say("")
    say("-" * 90)
    say("Part 1  the shift T: T^n = 1, T = multiplication by X, linearity    %s" % tag)
    say("-" * 90)
    S, R, F = amb.S, amb.R, amb.F
    n = amb.n
    xs, exh = amb.xs()

    # 1.1  T^n = id, T bijective
    ok_n = all(_Tpow(amb, x, n) == x for x in xs)
    check("T^n = id", ok_n, "N=%d" % len(xs), exhaustive=exh)
    check("T is a bijection (T^{-1} is a two-sided inverse)",
          all(amb.Tinv(amb.T(x)) == x and amb.T(amb.Tinv(x)) == x for x in xs),
          "N=%d" % len(xs), exhaustive=exh)

    # 1.2  T = right multiplication by X, and (using centrality) = left
    ok_r = ok_l = True
    for x in xs:
        Z = amb.iota(x)
        if amb.iota_inv(S.mul(Z, S.XI)) != amb.T(x):
            ok_r = False
        if amb.iota_inv(S.mul(S.XI, Z)) != amb.T(x):
            ok_l = False
    check("T = RIGHT multiplication by X:  iota(Tx) = iota(x) (X I)", ok_r,
          "N=%d" % len(xs), exhaustive=exh)
    check("T = LEFT  multiplication by X:  iota(Tx) = (X I) iota(x)  [needs centrality]",
          ok_l, "N=%d" % len(xs), exhaustive=exh)

    # an extra exhaustive run where the pool was sampled but the ambient is small
    if extra_exh and not exh:
        allR = amb.all_R()
        big = [tuple(v) for v in itertools.product(allR, repeat=n)]
        ok_all = True
        for x in big:
            Z = amb.iota(x)
            if amb.iota_inv(S.mul(Z, S.XI)) != amb.T(x):
                ok_all = False
                break
        check("T = right multiplication by X   [EXH over all of R^n]", ok_all,
              "N=%d = q^(4tn)" % len(big), exhaustive=True)

    # 1.3  Hamming isometry
    check("T is a Hamming isometry (wt(Tx) = wt(x))",
          all(amb.weight(amb.T(x)) == amb.weight(x) for x in xs),
          "N=%d" % len(xs), exhaustive=exh)

    # 1.4  F_q-linearity
    sub = xs[:200]
    ok_add = all(amb.T(amb.vadd(x, y)) == amb.vadd(amb.T(x), amb.T(y))
                 for x in sub for y in xs[:40])
    elems = list(range(F.q))
    ok_sc = all(amb.T(amb.scalar_mult(c, x)) == amb.scalar_mult(c, amb.T(x))
                for x in sub for c in elems)
    check("T is F_q-linear: T(x+y) = Tx + Ty", ok_add,
          "N=%d x %d" % (len(sub), min(len(xs), 40)), exhaustive=False)
    check("T is F_q-linear: T(c x) = c T(x) for every c in F_q  (c acts as cI)",
          ok_sc, "N=%d x q" % len(sub), exhaustive=False)

    # 1.5  R-linearity, on both sides
    prs, exhP = amb.pairs()
    tagP = "all %d pairs" % len(prs) if exhP else "%d sampled pairs (seed %d)" % (len(prs), SEED)
    check("T is RIGHT R-linear:  T(x.a) = (Tx).a",
          all(amb.T(amb.right_action(x, a)) == amb.right_action(amb.T(x), a)
              for (x, a) in prs), tagP, exhaustive=exhP)
    check("T is LEFT  R-linear:  T(a.x) = a.(Tx)",
          all(amb.T(amb.left_action(x, a)) == amb.left_action(amb.T(x), a)
              for (x, a) in prs), tagP, exhaustive=exhP)

    # 1.6  R_n-linearity of T (right needs centrality, left is free)
    zs, _ = amb.zs()
    zz = zs[:200]
    check("T is RIGHT R_n-linear:  T(Z W) = T(Z) W  [needs centrality]",
          all(S.mul(S.mul(Z, W), S.XI) == S.mul(S.mul(Z, S.XI), W)
              for Z in zz for W in zz[:40]),
          "N=%d" % (len(zz) * min(len(zz), 40)), exhaustive=False)
    check("T is LEFT  R_n-linear:  T(W Z) = W T(Z)  [associativity alone]",
          all(S.mul(S.mul(W, Z), S.XI) == S.mul(W, S.mul(Z, S.XI))
              for Z in zz for W in zz[:40]),
          "N=%d" % (len(zz) * min(len(zz), 40)), exhaustive=False)

    # 1.7  negative control: for a NON-central Y, right multiplication by Y is not
    #      right R-linear; for Y = X I it is.  This is exactly what centrality buys.
    Y = S.unit(0, 0)                                    # E_11, not central
    prs2, _ = amb.pairs(budget=2000)
    bad_Y = sum(1 for (x, a) in prs2
                if amb.iota_inv(S.mul(amb.iota(amb.right_action(x, a)), Y))
                != amb.right_action(amb.iota_inv(S.mul(amb.iota(x), Y)), a))
    bad_X = sum(1 for (x, a) in prs2
                if amb.iota_inv(S.mul(amb.iota(amb.right_action(x, a)), S.XI))
                != amb.right_action(amb.iota_inv(S.mul(amb.iota(x), S.XI)), a))
    check("[neg] non-central Y = E_11: R_Y(x.a) != R_Y(x).a  (mismatch expected)",
          bad_Y > 0, "mismatches %d/%d" % (bad_Y, len(prs2)), exhaustive=False)
    check("[neg] control: Y = X I (central): no mismatch, R_X is right R-linear",
          bad_X == 0, "mismatches %d/%d" % (bad_X, len(prs2)), exhaustive=False)


def _Tpow(amb, x, e):
    y = x
    for _ in range(e):
        y = amb.T(y)
    return y


# ==========================================================================
# Part 2 -- the equivalence
# ==========================================================================

def part2(amb, tag, census=False):
    say("")
    say("-" * 90)
    say("Part 2  right ideals of R_n  <->  T-invariant right R-submodules     %s" % tag)
    say("-" * 90)
    S, F = amb.S, amb.F
    n = amb.n
    ops_both = amb.ops_right + amb.ops_T
    trials = 25

    # 2.1  (<=): the closure under (right R, T) is the right ideal generated
    ok = True
    det = []
    for _ in range(trials):
        seeds = [amb.rand_vec() for _ in range(2)]
        Cb, dC = closure(amb, seeds, ops_both)
        Jb, dJ = right_ideal(amb, [amb.iota(x) for x in seeds])
        if canon_v(amb, [amb.iota(amb.unvec(tuple(b))) for b in Cb]) != Jb:
            ok = False
            det.append("dimC=%d dimJ=%d" % (dC, dJ))
    check("(<=)  closure under (right R-action, T)  ==  right ideal generated in R_n",
          ok, "trials=%d %s" % (trials, "; ".join(det[:3])), exhaustive=False)

    # 2.2  (=>): a right ideal pulls back to a right R-submodule closed under T
    ok = True
    for _ in range(trials):
        seeds = [amb.rand_S() for _ in range(2)]
        Jb, _ = right_ideal(amb, seeds)
        pre = [amb.iota_inv(S.unflat(tuple(b))) for b in Jb]
        rows = [list(amb.vec(x)) for x in pre]
        if not (is_closed(amb, rows, amb.ops_right) and is_closed(amb, rows, amb.ops_T)):
            ok = False
    check("(=>)  a right ideal of R_n pulls back to a right R-submodule closed under T",
          ok, "trials=%d" % trials, exhaustive=False)

    # 2.3  round trip
    ok = True
    for _ in range(trials):
        seeds = [amb.rand_vec() for _ in range(2)]
        Cb, _ = closure(amb, seeds, ops_both)
        Jb, _ = right_ideal(amb, [amb.iota(x) for x in seeds])
        back, _ = closure(amb, [amb.iota_inv(S.unflat(tuple(b))) for b in Jb], ops_both)
        if back != Cb:
            ok = False
    check("round trip:  C -> right ideal of R_n -> pullback  =  C", ok,
          "trials=%d" % trials, exhaustive=False)

    # 2.4  ideal -> pullback -> ideal
    ok = True
    for _ in range(trials):
        seeds = [amb.rand_S() for _ in range(2)]
        Jb, _ = right_ideal(amb, seeds)
        back = [amb.iota(amb.iota_inv(S.unflat(tuple(b)))) for b in Jb]
        if canon_v(amb, back) != Jb:
            ok = False
    check("round trip:  J -> pullback -> right ideal  =  J", ok,
          "trials=%d" % trials, exhaustive=False)

    # 2.5  negative controls: BOTH conditions are needed
    if n >= 2:
        def as_ideal_rows(basis_rows):
            return [list(S.flat(amb.iota(amb.unvec(tuple(b))))) for b in basis_rows]

        # (a) right R-submodule, not T-invariant
        e1 = [R_zero(amb)] * n
        e1[0] = amb.R.one
        C0, _ = closure(amb, [tuple(e1)], amb.ops_right)
        t_inv = is_closed(amb, C0, amb.ops_T)
        is_ideal = is_right_ideal(amb, as_ideal_rows(C0))
        check("[neg] right R-submodule, NOT T-invariant  =>  not a right ideal",
              (not t_inv) and (not is_ideal),
              "T-invariant=%s, right ideal=%s" % (t_inv, is_ideal), exhaustive=False)

        # (b) T-invariant F_q-subspace, not a right R-module
        v = amb.rand_vec()
        D, _ = closure(amb, [v], amb.ops_T)
        d_R = is_closed(amb, D, amb.ops_right)
        d_I = is_right_ideal(amb, as_ideal_rows(D))
        check("[neg] T-invariant F_q-subspace, NOT a right R-module  =>  not a right ideal",
              (not d_R) and (not d_I),
              "right R-module=%s, right ideal=%s" % (d_R, d_I), exhaustive=False)

        # (c) T-invariant LEFT R-submodule: T-invariant by Part 1, but not a right ideal
        e11 = [R_zero(amb)] * n
        e11[0] = amb.R.unit(0, 0)
        E, _ = closure(amb, [tuple(e11)], amb.ops_left + amb.ops_T)
        e_R = is_closed(amb, E, amb.ops_right)
        e_I = is_right_ideal(amb, as_ideal_rows(E))
        check("[neg] T-invariant LEFT R-submodule need not be a right ideal",
              (not e_R) and (not e_I),
              "right R-module=%s, right ideal=%s" % (e_R, e_I), exhaustive=False)

    # 2.6  brute-force census over ALL F_q-subspaces of R^n (only at (4,1,1))
    if census:
        subs = enumerate_subspaces(F, amb.d)
        cnt_R = cnt_T = cnt_both = 0
        dims = []
        for key in subs:
            rows = [list(v) for v in sorted(key)]
            r_ok = is_closed(amb, rows, amb.ops_right)
            t_ok = is_closed(amb, rows, amb.ops_T)
            if r_ok:
                cnt_R += 1
            if t_ok:
                cnt_T += 1
            if r_ok and t_ok:
                cnt_both += 1
                Bd, _ = rref([list(v) for v in rows], F, amb.d)
                dims.append(len(Bd))
        dims = sorted(dims)
        check("[census] all F_q-subspaces: #(T-invariant right R-submodules) = q+3",
              cnt_both == amb.q + 3,
              "count=%d, q+3=%d, F_q-dims=%s" % (cnt_both, amb.q + 3, dims),
              exhaustive=True)
        check("[census] at n=1: T = id, so every right R-submodule is T-invariant",
              cnt_R == cnt_both,
              "#right R-submodules=%d, #T-invariant=%d" % (cnt_R, cnt_both),
              exhaustive=True)


def R_zero(amb):
    return amb.R.zero


# ==========================================================================
# Part 3 -- sigma_k and theta_s versus T and the two actions
# ==========================================================================

def part3(amb, tag, s_list, k_list):
    say("")
    say("-" * 90)
    say("Part 3  sigma_k and theta_s: T, the two sides, semilinearity        %s" % tag)
    say("-" * 90)
    R, F = amb.R, amb.F
    xs, exh = amb.xs()
    prs, exhP = amb.pairs()
    tagP = "all %d pairs" % len(prs) if exhP else "%d sampled pairs (seed %d)" % (len(prs), SEED)
    elems = list(range(F.q))
    sub = xs[:150]

    # 3.1  commutation with T (plain commutation of maps on R^n)
    for k in k_list:
        check("T sigma_%d = sigma_%d T  (plain commutation)" % (k, k),
              all(amb.T(amb.vsig(x, k)) == amb.vsig(amb.T(x), k) for x in xs),
              "N=%d" % len(xs), exhaustive=exh)
    for s in s_list:
        check("T theta_%d = theta_%d T  (plain commutation)" % (s, s),
              all(amb.T(amb.vtheta(x, s)) == amb.vtheta(amb.T(x), s) for x in xs),
              "N=%d" % len(xs), exhaustive=exh)

    # 3.2  sigma_k preserves the side (ring automorphism)
    for k in k_list:
        check("sigma_%d rho_a = rho_{sigma_%d(a)} sigma_%d   (right action preserved)"
              % (k, k, k),
              all(amb.vsig(amb.right_action(x, a), k)
                  == amb.right_action(amb.vsig(x, k), R.sigma(a, k))
                  for (x, a) in prs), tagP, exhaustive=exhP)
        check("sigma_%d lambda_a = lambda_{sigma_%d(a)} sigma_%d   (left action preserved)"
              % (k, k, k),
              all(amb.vsig(amb.left_action(x, a), k)
                  == amb.left_action(amb.vsig(x, k), R.sigma(a, k))
                  for (x, a) in prs), tagP, exhaustive=exhP)

    # 3.3  theta_s SWAPS the side (anti-automorphism) -- and is NOT a commutation
    for s in s_list:
        check("theta_%d rho_a = lambda_{theta_%d(a)} theta_%d   (SIDE SWAP, right action)"
              % (s, s, s),
              all(amb.vtheta(amb.right_action(x, a), s)
                  == amb.left_action(amb.vtheta(x, s), R.theta(a, s))
                  for (x, a) in prs), tagP, exhaustive=exhP)
        check("theta_%d lambda_a = rho_{theta_%d(a)} theta_%d   (SIDE SWAP, left action)"
              % (s, s, s),
              all(amb.vtheta(amb.left_action(x, a), s)
                  == amb.right_action(amb.vtheta(x, s), R.theta(a, s))
                  for (x, a) in prs), tagP, exhaustive=exhP)
        bad = sum(1 for (x, a) in prs
                  if amb.vtheta(amb.right_action(x, a), s)
                  != amb.right_action(amb.vtheta(x, s), R.theta(a, s)))
        check("[neg] theta_%d rho_a != rho_{theta_%d(a)} theta_%d   (NOT commutation)"
              % (s, s, s), bad > 0,
              "mismatches %d/%d" % (bad, len(prs)), exhaustive=exhP)
        check("[neg] theta_%d is not the identity (test is non-vacuous)" % s,
              any(amb.vtheta(x, s) != x for x in xs), "N=%d" % len(xs), exhaustive=exh)

    # 3.4  semilinearity over F_q
    for k in k_list:
        check("sigma_%d is sigma_%d-semilinear:  sigma_k(c x) = sigma_k(c) sigma_k(x)"
              % (k, k),
              all(amb.vsig(amb.scalar_mult(c, x), k)
                  == amb.scalar_mult(F.frob_k(c, k), amb.vsig(x, k))
                  for x in sub for c in elems),
              "N=%d x q" % len(sub), exhaustive=False)
        if any(F.frob_k(c, k) != c for c in elems):
            bad = sum(1 for x in sub for c in elems
                      if amb.vsig(amb.scalar_mult(c, x), k)
                      != amb.scalar_mult(c, amb.vsig(x, k)))
            check("[neg] sigma_%d is NOT F_q-linear (c -> sigma_k(c) is non-trivial)" % k,
                  bad > 0, "mismatches %d" % bad, exhaustive=False)
    for s in s_list:
        check("theta_%d is sigma_%d-semilinear:  theta_s(c x) = sigma_s(c) theta_s(x)"
              % (s, s),
              all(amb.vtheta(amb.scalar_mult(c, x), s)
                  == amb.scalar_mult(F.frob_k(c, s), amb.vtheta(x, s))
                  for x in sub for c in elems),
              "N=%d x q" % len(sub), exhaustive=False)
        if any(F.frob_k(c, s) != c for c in elems):
            bad = sum(1 for x in sub for c in elems
                      if amb.vtheta(amb.scalar_mult(c, x), s)
                      != amb.scalar_mult(c, amb.vtheta(x, s)))
            check("[neg] theta_%d is NOT F_q-linear (c -> sigma_s(c) is non-trivial)" % s,
                  bad > 0, "mismatches %d" % bad, exhaustive=False)

    # 3.5  the Phase-1 inputs on R (L-6.1 -- theta_s on R_n -- is out of scope here)
    as_, _ = amb.as_()
    ap = as_[:60]
    for k in k_list:
        check("R: sigma_%d is a ring automorphism (Phase 1, Lemma 4.2)" % k,
              all(R.sigma(R.mul(a, b), k) == R.mul(R.sigma(a, k), R.sigma(b, k))
                  for a in ap for b in ap), "N=3600", exhaustive=False)
    for s in s_list:
        check("R: theta_%d is an anti-automorphism (Phase 1, Lemma 4.3)" % s,
              all(R.theta(R.mul(a, b), s) == R.mul(R.theta(b, s), R.theta(a, s))
                  for a in ap for b in ap), "N=3600", exhaustive=False)
        check("R: theta_%d^2 = sigma_%d (Phase 1, Lemma 4.4)" % (s, 2 * s),
              all(R.theta(R.theta(a, s), s) == R.sigma(a, 2 * s) for a in ap),
              "N=%d" % len(ap), exhaustive=False)
        k0 = 1 % amb.r
        check("R: sigma_%d theta_%d = theta_%d sigma_%d (Phase 1, 4.7)" % (k0, s, s, k0),
              all(R.sigma(R.theta(a, s), k0) == R.theta(R.sigma(a, k0), s) for a in ap),
              "N=%d" % len(ap), exhaustive=False)


# ==========================================================================
# Part 4 -- the boundary case n = 1
# ==========================================================================

def part4(amb, tag):
    say("")
    say("-" * 90)
    say("Part 4  boundary case n = 1                                        %s" % tag)
    say("-" * 90)
    S = amb.S
    xs, exh = amb.xs()
    check("n=1: T = id", all(amb.T(x) == x for x in xs), "N=%d" % len(xs),
          exhaustive=exh)
    check("n=1: X = 1 in B, hence X I = I in R_n", S.XI == S.one, "", exhaustive=True)
    check("n=1: iota is the coefficient embedding (R_1 = R)",
          all(amb.iota(x) == amb.emb(x[0]) for x in xs), "N=%d" % len(xs),
          exhaustive=exh)
    check("n=1: the two R-actions are the two actions of R on itself",
          all(amb.right_action(x, a) == (amb.R.mul(x[0], a),)
              and amb.left_action(x, a) == (amb.R.mul(a, x[0]),)
              for x in xs[:100] for a in amb.as_()[0][:60]),
          "N=%d" % (min(len(xs), 100) * 60), exhaustive=False)


# ==========================================================================
# main
# ==========================================================================

def main():
    say("=" * 90)
    say("PHASE 2 - STAGE 1 verification: cyclic-code definitions and the shift structure")
    say("companion to 03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md")
    say("seed = %d  (all sampling deterministic)  |EXH|/|SMP| labels are per check" % SEED)
    say("=" * 90)

    sets = [
        # (p, r, t, n)  ->  (q, t, n)      |R^n| = q^(4tn)        comment
        (2, 2, 1, 1),   # (4, 1, 1)              256     exhaustive + subspace census
        (2, 2, 1, 2),   # (4, 1, 2)            65536     extra exhaustive T = X-mult
        (2, 2, 1, 3),   # (4, 1, 3)         16.7M
        (3, 2, 1, 1),   # (9, 1, 1)             6561     exhaustive
        (3, 2, 1, 2),   # (9, 1, 2)           43M
        (2, 2, 2, 1),   # (4, 2, 1)            65536     t = 2
        (2, 2, 2, 2),   # (4, 2, 2)            4.3G      wild: p|n and t >= 2
        (2, 3, 1, 2),   # (8, 1, 2)           16.7M      r = 3
    ]

    for (p, r, t, n) in sets:
        amb = Amb(p, r, t, n)
        tag = "(q,t,n)=(%d,%d,%d)" % (amb.q, t, n)
        say("")
        say("=" * 90)
        say("PARAMETER SET %s   dim_Fq R^n = %d   |R^n| = %d"
            % (tag, amb.d, amb.q ** (4 * t * n)))
        say("=" * 90)
        ks = list(range(r))
        part0(amb, tag)
        part1(amb, tag, extra_exh=(p, r, t, n) in [(2, 2, 1, 2), (2, 2, 2, 1)])
        part2(amb, tag, census=(p, r, t, n) == (2, 2, 1, 1))
        part3(amb, tag, ks, ks)
        if n == 1:
            part4(amb, tag)

    say("")
    say("=" * 90)
    if FAILURES:
        say("RESULT: %d of %d checks FAILED" % (len(FAILURES), NCHECK[0]))
        for f in FAILURES:
            say("   FAIL: %s   %s" % f)
    else:
        say("RESULT: all %d checks PASSED." % NCHECK[0])
    say("=" * 90)
    with open("phase2_stage1_shift_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\nlog written to phase2_stage1_shift_log.txt")


if __name__ == "__main__":
    main()
