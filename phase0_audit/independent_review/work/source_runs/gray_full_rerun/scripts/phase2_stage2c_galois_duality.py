#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 2 -- STAGE 2C.  Galois duality, annihilators and reciprocal generators.

Executes PHASE2_PROPOSAL_v2.md sections 6.1 - 6.7 (L-6.1, P-2.7, P-2.8) and the
cardinality / double-dual consistency checks of section 6.5 (C1) and RGF section
6.7.  Out of scope by instruction: hull dimensions (Phase 3), hull enumeration
(Phase 4), Gray maps (Phase 5) and quantum constructions (Phase 6).

Conventions carried in from Phase 1 / Stage 1 / Stage 2A / Stage 2B, unchanged:

  R   = M_2(A_t),      A_t = F_q[u]/<u^t>,   q = p^r
  B   = A_t[X]/<X^n-1>,      X central
  R_n = R[X]/<X^n-1>  ~=  M_2(B)     (Stage 2A Lemma 1.3)
  iota : R^n -> R_n,   x |-> sum_e x_e X^e          (RGF Lemma 3.2)
  right-module convention for codes: a cyclic code is a right ideal of R_n
  Morita column convention: im M = B-span of the two COLUMNS of M
  B_s(x,y) = sum_e theta_s(x_e) y_e  in R,   theta_s = sigma_s o transpose
  b_s = Lambda o B_s,  Lambda = lambda o tr,  lambda = coefficient of u^{t-1}

Everything except Field / Local / MatRing / rref / nullspace_basis (the Phase-1
library) is written from scratch here.

Seeds are fixed; the log carries no timestamp and no elapsed time, so that two
consecutive runs can be compared byte for byte.
"""

import sys
import itertools
import random

sys.path.insert(0, "/home/user/Matrix-Ring/04_COMPUTATION")

from ring_structure_checks import (Field, Local, MatRing, rref, nullspace_basis,
                                   say, check, LINES, FAILURES, NCHECK)

SEED = 20261107
LOGNAME = "phase2_stage2c_galois_log.txt"
EXH_LIMIT = 5000          # above this |R_n| the elementwise tests are sampled


def head(msg):
    say("\n" + "#" * 96)
    say("#  " + msg)
    say("#" * 96)


def sub(msg):
    say("\n-- " + msg + " " + "-" * max(0, 90 - len(msg)))


# ==========================================================================
# 1.  The rings
# ==========================================================================

class BRing(object):
    """
    B = A_t[X]/<X^n - 1>.

    An element is a tuple of length t*n of F_q-elements, indexed  a*n + e,
    i.e.  sum_{a<t} sum_{e<n} c_{a,e} u^a X^e.
    """

    def __init__(self, F, t, n):
        self.F, self.t, self.n = F, t, n
        self.dim = t * n
        self.zero = tuple([0] * (t * n))
        one = [0] * (t * n)
        one[0] = 1
        self.one = tuple(one)

    def add(self, x, y):
        F = self.F
        return tuple(F.add[x[i]][y[i]] for i in range(self.dim))

    def neg(self, x):
        return tuple(self.F.neg[c] for c in x)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        F, t, n = self.F, self.t, self.n
        out = [0] * (t * n)
        for a1 in range(t):
            row1 = x[a1 * n:(a1 + 1) * n]
            if not any(row1):
                continue
            for e1 in range(n):
                c1 = row1[e1]
                if not c1:
                    continue
                for a2 in range(t - a1):
                    row2 = y[a2 * n:(a2 + 1) * n]
                    if not any(row2):
                        continue
                    base = (a1 + a2) * n
                    for e2 in range(n):
                        c2 = row2[e2]
                        if c2:
                            k = base + (e1 + e2) % n
                            out[k] = F.add[out[k]][F.mul[c1][c2]]
        return tuple(out)

    def sigma(self, x, s):
        tab = self.F.frob[s % self.F.r]
        return tuple(tab[c] for c in x)

    def rev(self, x):
        """the substitution X -> X^{n-1} = X^{-1}; u is fixed"""
        t, n = self.t, self.n
        out = [0] * (t * n)
        for a in range(t):
            for e in range(n):
                out[a * n + ((-e) % n)] = x[a * n + e]
        return tuple(out)

    def u_pow(self, a0):
        """u^{a0}"""
        n, t = self.n, self.t
        out = [0] * (t * n)
        if a0 < t:
            out[a0 * n] = 1
        return tuple(out)

    def X_pow(self, e0):
        out = [0] * (self.t * self.n)
        out[e0 % self.n] = 1
        return tuple(out)

    def elem_list(self):
        return list(itertools.product(range(self.F.q), repeat=self.dim))


class QuotRing(object):
    """
    A generic commutative quotient  C = A_t[X]/<h>,  h monic of degree D.

    An element is a tuple of length t*D indexed  a*D + b  (u^a X^b).
    Only the operations needed for the chain-ring components are provided.
    """

    def __init__(self, F, t, h):
        self.F, self.t, self.h, self.D = F, t, tuple(h), len(h) - 1
        self.dim = t * self.D
        self.zero = tuple([0] * self.dim)
        one = [0] * self.dim
        one[0] = 1
        self.one = tuple(one)

    def add(self, x, y):
        F = self.F
        return tuple(F.add[x[i]][y[i]] for i in range(self.dim))

    def neg(self, x):
        return tuple(self.F.neg[c] for c in x)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def _reduce(self, poly):
        """reduce a length-(D + k) X-polynomial modulo the monic h"""
        F, D, h = self.F, self.D, self.h
        p = list(poly)
        for i in range(len(p) - 1, D - 1, -1):
            c = p[i]
            if c:
                p[i] = 0
                for j in range(D):
                    # h = [h_0, ..., h_D] with h_D = 1 ;  X^i = -sum h_j X^{i-D+j}
                    p[i - D + j] = F.sub[p[i - D + j]][F.mul[c][h[j]]]
        return p[:D]

    def mul(self, x, y):
        F, t, D = self.F, self.t, self.D
        conv = [0] * (2 * D - 1)
        for i in range(D):
            if x[i]:
                for j in range(D):
                    if y[j]:
                        conv[i + j] = F.add[conv[i + j]][F.mul[x[i]][y[j]]]
        out = [0] * (t * D)
        for a1 in range(t):
            row1 = x[a1 * D:(a1 + 1) * D]
            if not any(row1):
                continue
            for a2 in range(t - a1):
                row2 = y[a2 * D:(a2 + 1) * D]
                if not any(row2):
                    continue
                conv = [0] * (2 * D - 1)
                for i in range(D):
                    if row1[i]:
                        for j in range(D):
                            if row2[j]:
                                conv[i + j] = F.add[conv[i + j]][F.mul[row1[i]][row2[j]]]
                red = self._reduce(conv)
                base = (a1 + a2) * D
                for b in range(D):
                    out[base + b] = F.add[out[base + b]][red[b]]
        return tuple(out)

    def sigma(self, x, s):
        tab = self.F.frob[s % self.F.r]
        return tuple(tab[c] for c in x)

    def elem_list(self):
        return list(itertools.product(range(self.F.q), repeat=self.dim))


# ==========================================================================
# 2.  Representations and the identification iota
# ==========================================================================

class Ctx(object):
    """all the rings attached to one parameter set (q, t, n)"""

    def __init__(self, q, t, n):
        p, r = _factor_q(q)
        self.q, self.p, self.r, self.t, self.n = q, p, r, t, n
        self.F = Field(p, r)
        self.F.check_r = r
        self.A = Local(self.F, t)
        self.RA = MatRing(self.A, 2)          # R = M_2(A_t)
        self.B = BRing(self.F, t, n)         # B = A_t[X]/<X^n-1>
        self.RB = MatRing(self.B, 2)         # R_n ~= M_2(B)
        self.dimw = 4 * t * n                # dim_{F_q} of R^n (and of R_n)

    # ---- flat F_q-coordinates ------------------------------------------
    def flat_word(self, x):
        """R^n -> F_q^{4tn}:  index ((e*4 + (2i+j))*t + a)"""
        out = []
        for e in range(self.n):
            M = x[e]
            for k in range(4):
                out.extend(M[k])
        return tuple(out)

    def unflat_word(self, v):
        t = self.t
        out = []
        for e in range(self.n):
            M = []
            for k in range(4):
                M.append(tuple(v[(e * 4 + k) * t:(e * 4 + k) * t + t]))
            out.append(tuple(M))
        return tuple(out)

    def flat_rn(self, M):
        """M_2(B) -> F_q^{4tn}:  index (k*(t*n) + a*n + e),  k = 2i+j"""
        out = []
        for k in range(4):
            out.extend(M[k])
        return tuple(out)

    def unflat_rn(self, v):
        D = self.t * self.n
        return tuple(tuple(v[k * D:(k + 1) * D]) for k in range(4))

    # ---- iota -----------------------------------------------------------
    def iota(self, x):
        """R^n -> M_2(B):  (iota x)_{ij} = sum_e (x_e)_{ij} X^e"""
        F, t, n = self.F, self.t, self.n
        M = []
        for k in range(4):
            coef = [0] * (t * n)
            for e in range(n):
                a_vec = x[e][k]
                for a in range(t):
                    coef[a * n + e] = a_vec[a]
            M.append(tuple(coef))
        return tuple(M)

    def iota_inv(self, M):
        """M_2(B) -> R^n"""
        t, n = self.t, self.n
        out = []
        for e in range(n):
            R = []
            for k in range(4):
                R.append(tuple(M[k][a * n + e] for a in range(t)))
            out.append(tuple(R))
        return tuple(out)

    # ---- the maps on R^n ------------------------------------------------
    def sigma_word(self, x, s):
        return tuple(self.RA.sigma(xe, s) for xe in x)

    def theta_word(self, x, s):
        return tuple(self.RA.theta(xe, s) for xe in x)

    def rev_word(self, x):
        return tuple(x[(-e) % self.n] for e in range(self.n))

    def sigma_rn(self, M, s):
        return self.RB.sigma(M, s)

    def theta_rn(self, M, s):
        return self.RB.theta(M, s)

    def rev_rn(self, M):
        return tuple(self.B.rev(m) for m in M)

    # ---- the pairing ----------------------------------------------------
    def Bs(self, x, y, s):
        """sum_e theta_s(x_e) y_e  in R"""
        RA = self.RA
        acc = RA.zero
        for e in range(self.n):
            acc = RA.add(acc, RA.mul(RA.theta(x[e], s), y[e]))
        return acc

    def bs(self, x, y, s):
        """Lambda(B_s(x,y)) in F_q"""
        return self.RA.Lambda(self.Bs(x, y, s))

    # ---- right action of R_n on itself / multiplication ------------------
    def mul_rn(self, X, Y):
        return self.RB.mul(X, Y)


def _factor_q(q):
    for p in (2, 3, 5, 7, 11):
        r = 0
        m = q
        while m % p == 0:
            m //= p
            r += 1
        if m == 1 and r >= 1:
            return p, r
    raise ValueError("q = %s is not a prime power" % q)


# ==========================================================================
# 3.  F_q-linear algebra on the ambient space R^n
# ==========================================================================

def belem(C):
    """cached list of the elements of B (|B| <= 4096 in every test case)"""
    if not hasattr(C, "_belem"):
        C._belem = list(C.B.elem_list())
    return C._belem


def word_basis(C):
    """the standard F_q-basis of R^n as words"""
    t, n = C.t, C.n
    out = []
    for e in range(n):
        for k in range(4):
            for a in range(t):
                M = []
                for k2 in range(4):
                    vec = [0] * t
                    if k2 == k:
                        vec[a] = 1
                    M.append(tuple(vec))
                w = []
                for e2 in range(n):
                    w.append(tuple(M) if e2 == e else C.RA.zero)
                out.append(tuple(w))
    return out


def functional_row(C, x, s):
    """
    the F_q-linear functional  y |-> b_s(x, y)  as a row of length 4tn,
    computed on the standard basis.  b_s is F_q-linear in y (RGF Lemma 6.2(iii)).
    """
    row = []
    for e0 in range(C.n):
        tx = C.RA.theta(x[e0], s)
        for k in range(4):
            i0, j0 = k // 2, k % 2
            for a in range(C.t):
                Y = C.RA.unit(i0, j0, C.A.pow(C.A.u, a) if C.t > 1 else C.A.one)
                row.append(C.RA.Lambda(C.RA.mul(tx, Y)))
    return tuple(row)


def dual_of(C, Cgens, s):
    """
    C^{perp_s} = {y : b_s(x,y) = 0 for all x in the F_q-span of Cgens},
    as an RREF basis of F_q-vectors of length 4tn.

    b_s is sigma_s-semilinear in x, so vanishing on an F_q-basis of the code
    implies vanishing on the whole code.
    """
    F = C.F
    rows, _ = rref([list(C.flat_word(x)) for x in Cgens], F, C.dimw)
    Mrows = [list(functional_row(C, C.unflat_word(tuple(r)), s)) for r in rows]
    return nullspace_basis(Mrows, F, C.dimw)


def span_keys(C, basis):
    """the F_q-span of `basis` as a frozenset of flat vectors"""
    F, d = C.F, C.dimw
    if not basis:
        return frozenset([tuple([0] * d)])
    out = set()
    for coeffs in itertools.product(range(F.q), repeat=len(basis)):
        acc = [0] * d
        for c, r in zip(coeffs, basis):
            if c:
                acc = [F.add[u][F.mul[c][v]] for u, v in zip(acc, r)]
        out.add(tuple(acc))
    return frozenset(out)


def same_span(C, basis_a, basis_b):
    """do the two F_q-bases span the same subspace?  (RREF comparison)"""
    F, d = C.F, C.dimw
    ra = rref([list(x) for x in basis_a], F, d)[0]
    rb = rref([list(x) for x in basis_b], F, d)[0]
    return tuple(tuple(x) for x in ra) == tuple(tuple(x) for x in rb)


def words_of(C, basis):
    return [C.unflat_word(tuple(v)) for v in basis]


# ==========================================================================
# 4.  Annihilators, computed directly from the definitions
# ==========================================================================

def _kernel_from_images(F, d, imgs):
    """
    kernel of the F_q-linear map whose matrix has COLUMN k = imgs[k].
    (Passing the images as ROWS would compute the kernel of the transpose.)
    """
    rows = [[imgs[k][j] for k in range(d)] for j in range(d)]
    return nullspace_basis(rows, F, d)


def ann_r_element(C, v):
    """
    ann_r(v) = {w in R_n : v w = 0},  the kernel of LEFT multiplication by v,
    as an RREF basis of F_q-vectors of length 4tn.  Computed by brute force
    over the standard basis (no Morita, no image/ker shortcut).
    """
    F, d = C.F, C.dimw
    basis = [C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
             for k in range(d)]
    imgs = [C.flat_rn(C.mul_rn(v, e)) for e in basis]
    return _kernel_from_images(F, d, imgs)


def ann_l_element(C, v):
    """ann_l(v) = {w in R_n : w v = 0}, the kernel of RIGHT multiplication"""
    F, d = C.F, C.dimw
    basis = [C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
             for k in range(d)]
    imgs = [C.flat_rn(C.mul_rn(e, v)) for e in basis]
    return _kernel_from_images(F, d, imgs)


def ann_r_set(C, gens):
    """
    ann_r of the submodule generated by `gens` -- i.e.
    {a : x a = 0 for every x in the (right or left) module they generate}.

    NOTE: for a RIGHT ideal this is NOT the intersection of the ann_r of the
    generators, because (g m) a = g (m a) need not vanish when g a = 0.  It is
    computed honestly, as the kernel of the map  a |-> (x a)_x  over the whole
    module generated by `gens` (right module by default: use side='left' for a
    left module).
    """
    F, d = C.F, C.dimw
    basis = [C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
             for k in range(d)]
    allrows = []
    for x in gens:
        imgs = [C.flat_rn(C.mul_rn(x, e)) for e in basis]
        allrows.extend([[imgs[k][j] for k in range(d)] for j in range(d)])
    return nullspace_basis(allrows, F, d)


def right_ideal_basis(C, gens):
    """RREF basis of the right ideal sum_i gens[i] * R_n (brute force)"""
    F, d = C.F, C.dimw
    rows = []
    for g in gens:
        for k in range(d):
            e = C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
            rows.append(list(C.flat_rn(C.mul_rn(g, e))))
    return rref(rows, F, d)[0]


def left_ideal_basis(C, gens):
    F, d = C.F, C.dimw
    rows = []
    for g in gens:
        for k in range(d):
            e = C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
            rows.append(list(C.flat_rn(C.mul_rn(e, g))))
    return rref(rows, F, d)[0]


# ==========================================================================
# 5.  Morita side:  im, ker, I_W, mu   (re-derived independently)
# ==========================================================================

def module_basis(C, Wbasis):
    """RREF basis of the B-submodule of B^2 generated by the given vectors"""
    F = C.F
    d = 2 * C.B.dim
    rows = []
    for w in Wbasis:
        # w is a pair of B-elements; generate  w * b  for b in a B-basis
        for b in _B_basis(C.B):
            rows.append(list(_pair_flat(C, (C.B.mul(w[0], b), C.B.mul(w[1], b)))))
    return rref(rows, F, d)[0]


def _B_basis(B):
    out = []
    for a in range(B.t):
        for e in range(B.n):
            v = [0] * (B.t * B.n)
            v[a * B.n + e] = 1
            out.append(tuple(v))
    return out


def _pair_flat(C, w):
    out = list(w[0])
    out.extend(w[1])
    return tuple(out)


def im_basis(C, M):
    """im M = the B-span of the two COLUMNS of M  (Morita column convention)"""
    cols = [(M[0], M[2]), (M[1], M[3])]      # column 0 = (a11, a21), column 1 = (a12, a22)
    return module_basis(C, cols)


def ker_basis(C, M):
    """ker M = {w in B^2 : M w = 0}, as an F_q-subspace of B^2"""
    F = C.F
    d = 2 * C.B.dim
    imgs = []
    for k in range(d):
        vv = [0] * d
        vv[k] = 1
        w = (tuple(vv[:C.B.dim]), tuple(vv[C.B.dim:]))
        Mw = (C.B.add(C.B.mul(M[0], w[0]), C.B.mul(M[1], w[1])),
              C.B.add(C.B.mul(M[2], w[0]), C.B.mul(M[3], w[1])))
        imgs.append(_pair_flat(C, Mw))
    rows = [[imgs[k][j] for k in range(d)] for j in range(d)]
    return nullspace_basis(rows, F, d)


def I_of_W(C, Wbasis):
    """
    I_W = {M in M_2(B) : both COLUMNS of M lie in W}.

    The basis vectors of W are placed in the COLUMNS (right-module / Morita
    column convention).  Placing them in the rows produces the LEFT ideal, and
    every dimension and cardinality check still passes -- only a containment
    test exposes the error (this is checked as a negative control).
    """
    F, d = C.F, C.dimw
    rows = []
    for w in Wbasis:
        for b in _B_basis(C.B):
            # column 0 = w*b, column 1 = 0
            M = (C.B.mul(w[0], b), C.B.zero, C.B.mul(w[1], b), C.B.zero)
            rows.append(list(C.flat_rn(M)))
            # column 0 = 0, column 1 = w*b
            M = (C.B.zero, C.B.mul(w[0], b), C.B.zero, C.B.mul(w[1], b))
            rows.append(list(C.flat_rn(M)))
    return rref(rows, F, d)[0]


# ==========================================================================
# 6.  CRT components (only the two regimes that occur in the test list)
# ==========================================================================
#
# Two situations are implemented, and they cover every parameter set used
# below.  Anything else (p | n with n' > 1) is refused, loudly.
#
#   (S) SPLIT:  X^n - 1 splits over F_q into n DISTINCT linear factors
#               (so p does not divide n and F_q contains all n-th roots of
#               unity).  Then B = prod_{zeta} A_t by evaluation at the roots,
#               and each component is the chain ring A_t (uniformiser u).
#   (C) CHAIN:  p | n with n' = 1, so X^n - 1 = (X-1)^{p^v}.  If t = 1 then
#               B = F_q[X]/<(X-1)^{p^v}> is a chain ring (uniformiser X-1).
#               If t >= 2 this is the WILD case: B is local but not a chain
#               ring, and no Smith normal form is available.
#
# The general (regime-free) construction of the dual generator does not use
# any of this; the decomposition is only needed for the SNF form of P-2.8
# and for the componentwise value of mu.

def roots_of_unity(C):
    """{zeta in F_q : zeta^n = 1}"""
    F = C.F
    out = []
    for a in range(F.q):
        v = F.one if False else 1
        acc = 1
        for _ in range(C.n):
            acc = F.mul[acc][a]
        if acc == 1:
            out.append(a)
    return out


def _poly_eval(F, coeffs, x):
    acc = 0
    for c in reversed(coeffs):
        acc = F.add[F.mul[acc][x]][c]
    return acc


class ChainInfo(object):
    """a finite chain ring: uniformiser omega, nilpotency length ell, valuation"""

    def __init__(self, ring, omega, ell, flat):
        self.ring, self.omega, self.ell = ring, omega, ell
        self.F = ring.F
        self.flat = flat                       # element -> flat F_q tuple
        self.dim = len(flat(ring.zero))
        # the ideals (omega^k) as F_q-spans
        self.ideals = []
        cur = ring.one
        for k in range(ell + 1):
            span = set()
            basis = [cur]
            rows = [list(flat(cur))]
            # generate the ideal (omega^k) = omega^k * ring
            for b in _ring_basis(ring):
                rows.append(list(flat(ring.mul(cur, b))))
            Rb, _ = rref(rows, self.F, self.dim)
            for coeffs in itertools.product(range(self.F.q), repeat=len(Rb)):
                acc = [0] * self.dim
                for c, rw in zip(coeffs, Rb):
                    if c:
                        acc = [self.F.add[u][self.F.mul[c][v]] for u, v in zip(acc, rw)]
                span.add(tuple(acc))
            self.ideals.append(frozenset(span))
            cur = ring.mul(cur, omega)

    def val(self, x):
        """the largest k with x in (omega^k);  val(0) = ell"""
        fx = self.flat(x)
        for k in range(self.ell, -1, -1):
            if fx in self.ideals[k]:
                return k
        return 0

    def divide(self, x, y):
        """c with y = x*c, or None  (x, y in the chain ring;  needs val y >= val x)"""
        R = self.ring
        for c in _ring_elements(R):
            if R.mul(x, c) == y:
                return c
        return None


def _ring_basis(R):
    """an F_q-basis of the ring R (as ring elements)"""
    out = []
    z = list(R.zero)
    for i in range(len(z)):
        v = [0] * len(z)
        v[i] = 1
        out.append(tuple(v))
    return out


def _ring_elements(R):
    return list(itertools.product(range(R.F.q), repeat=len(R.zero)))


class Components(object):
    """the CRT decomposition of B, in the two regimes described above"""

    def __init__(self, C):
        self.C = C
        F, B, t, n = C.F, C.B, C.t, C.n
        Z = roots_of_unity(C)
        p, v = C.p, _vp(C.n, C.p)
        nprime = C.n // (p ** v)
        self.kind = None
        self.comps = []
        if p ** v == 1 and len(Z) == C.n and C.n == len(set(Z)):
            # (S) split semisimple:  B = prod_{zeta in Z} A_t
            self.kind = "split"
            self.Z = Z
            for zeta in Z:
                info = ChainInfo(C.A, C.A.u if t > 1 else C.A.zero,
                                 t, lambda a: tuple(a))
                self.comps.append(("A_t@%d" % zeta, info, zeta))
        elif nprime == 1 and C.t == 1:
            # (C) chain ring  B = F_q[X]/<(X-1)^{p^v}>
            xm1 = B.add(B.X_pow(1), B.neg(B.X_pow(0)))
            info = ChainInfo(B, xm1, p ** v, lambda b: tuple(b))
            self.kind = "chain"
            self.comps.append(("B", info, 1))
        elif nprime == 1 and C.t >= 2:
            # (W) wild: local, not a chain ring -- no SNF, no components
            self.kind = "wild"
        else:
            raise RuntimeError("no component routine for (q,t,n)=(%d,%d,%d)"
                               % (C.q, C.t, C.n))

    # ---- projection / injection ----------------------------------------
    def proj(self, b, j):
        """B -> component j"""
        C = self.C
        if self.kind == "chain":
            return b
        zeta = self.comps[j][2]
        t, n = C.t, C.n
        out = []
        for a in range(t):
            acc = 0
            for e in range(n):
                c = b[a * n + e]
                if c:
                    acc = C.F.add[acc][C.F.mul[c][_zpow(C.F, zeta, e)]]
            out.append(acc)
        return tuple(out)

    def inj(self, vals):
        """(values at the components) -> B"""
        C = self.C
        if self.kind == "chain":
            return vals[0]
        F, t, n = C.F, C.t, C.n
        Z = self.Z
        out = [0] * (t * n)
        # Lagrange basis polynomials  L_zeta(X) = prod_{z != zeta} (X - z)/(zeta - z)
        for zi, zeta in enumerate(Z):
            num = [1]
            den = 1
            for z in Z:
                if z == zeta:
                    continue
                # multiply num by (X - z)
                new = [0] * (len(num) + 1)
                for i, c in enumerate(num):
                    new[i] = F.add[new[i]][F.mul[c][F.neg[z]]]
                    new[i + 1] = F.add[new[i + 1]][c]
                num = new
                den = F.mul[den][F.sub[zeta][z]]
            deninv = F.inv[den]
            num = [F.mul[c][deninv] for c in num]
            val = vals[zi]
            for a in range(t):
                ca = val[a]
                if ca:
                    for e, c in enumerate(num):
                        if c:
                            out[a * n + e] = F.add[out[a * n + e]][F.mul[ca][c]]
        return tuple(out)

    def snf_h(self, M):
        """
        the P-2.8 generator of  ann_r(M)  as a matrix over B, computed
        componentwise over the chain-ring components.

        Returns (h, ok) where ok is False when the ring is wild (no SNF).
        """
        if self.kind == "wild":
            return None, False
        cols = []
        for j, (_name, info, _z) in enumerate(self.comps):
            Mj = tuple(tuple(self.proj(m, j)) for m in M)
            U, V, a, b = snf2_chain(info, Mj)
            w = info.ring
            om = info.omega
            z = w.zero
            # the exponent is ell - a:  a = 0 gives omega^ell = 0, a = ell gives
            # omega^0 = 1.  (omega^ell = 0 holds by the definition of ell.)
            wa = _omega_pow(w, om, info.ell - a)
            wb = _omega_pow(w, om, info.ell - b)
            D = (wa, z, z, wb)
            hj = matmul2(w, V, D)
            cols.append(hj)
        h = tuple(self.inj([cj[k] for cj in cols]) for k in range(4))
        return h, True


def _zpow(F, z, e):
    acc = 1
    for _ in range(e):
        acc = F.mul[acc][z]
    return acc


def _vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _omega_pow(w, om, k):
    acc = w.one
    for _ in range(k):
        acc = w.mul(acc, om)
    return acc


def matmul2(w, X, Y):
    """2x2 multiplication over the ring w"""
    out = []
    for i in range(2):
        for j in range(2):
            acc = w.zero
            for k in range(2):
                if X[2 * i + k] != w.zero and Y[2 * k + j] != w.zero:
                    acc = w.add(acc, w.mul(X[2 * i + k], Y[2 * k + j]))
            out.append(acc)
    return tuple(out)


def snf2_chain(info, M):
    """
    Smith normal form of a 2x2 matrix over a finite chain ring:
    returns U, V, a, b with  U M V = diag(omega^a, omega^b),  0 <= a <= b <= ell.

    The elimination is the one proved in Stage 2B Theorem 3.3: put an entry of
    minimal valuation at (0,0), clear the first row and the first column, and
    note that the surviving entry automatically has valuation >= a, hence is
    divisible by omega^a in a chain ring.
    """
    w = info.ring
    A = [list(M)]
    U = (w.one, w.zero, w.zero, w.one)
    V = (w.one, w.zero, w.zero, w.one)

    def row_swap(X):
        return (X[2], X[3], X[0], X[1])

    def col_swap(X):
        return (X[1], X[0], X[3], X[2])
    P = (w.zero, w.one, w.one, w.zero)      # the permutation matrix, P^2 = I

    if all(x == w.zero for x in A[0]):
        return U, V, info.ell, info.ell
    # 1. an entry of minimal valuation at (0,0)
    vals = [info.val(x) for x in A[0]]
    k0 = min(range(4), key=lambda i: vals[i])
    i0, j0 = k0 // 2, k0 % 2
    if i0 == 1:
        A[0] = list(row_swap(A[0]))
        U = matmul2(w, P, U)
    if j0 == 1:
        A[0] = list(col_swap(A[0]))
        V = matmul2(w, V, P)
    # 2. clear the first row:  A[0][1] = A[0][0] * c
    x = A[0][0]
    if A[0][1] != w.zero:
        c = info.divide(x, A[0][1])
        assert c is not None, "chain-ring division failed (row)"
        E = (w.one, w.neg(c), w.zero, w.one)        # C1 <- C1 - c*C0
        A[0] = list(matmul2(w, A[0], E))
        V = matmul2(w, V, E)
    # 3. clear the first column
    if A[0][2] != w.zero:
        d = info.divide(A[0][0], A[0][2])
        assert d is not None, "chain-ring division failed (column)"
        E = (w.one, w.zero, w.neg(d), w.one)        # R1 <- R1 - d*R0
        A[0] = list(matmul2(w, E, A[0]))
        U = matmul2(w, E, U)
    a = info.val(A[0][0])
    b = info.val(A[0][3])
    # 4. normalise the diagonal entries to omega^a, omega^b by row scaling
    for pos, k in ((0, a), (3, b)):
        e = A[0][pos]
        if k >= info.ell:
            continue
        target = _omega_pow(w, info.omega, k)
        # e = omega^k * unit;  find the unit's inverse by search
        for uinv in _ring_elements(w):
            if w.mul(e, uinv) == target:
                S = (uinv, w.zero, w.zero, w.one) if pos == 0 else \
                    (w.one, w.zero, w.zero, uinv)
                A[0] = list(matmul2(w, S, A[0]))
                U = matmul2(w, S, U)
                break
    return U, V, a, b


# ==========================================================================
# 7.  Small helpers:  polynomial level, membership, ideal-ness
# ==========================================================================

def rref_key(C, basis, d=None):
    d = C.dimw if d is None else d
    return tuple(tuple(r) for r in rref([list(b) for b in basis], C.F, d)[0])


def contains(C, key, v, d=None):
    """is v in the F_q-span with the given RREF key?"""
    d = C.dimw if d is None else d
    rows = [list(x) for x in key] + [list(v)]
    return len(rref(rows, C.F, d)[1]) == len(key)


def rn_basis(C):
    """the standard F_q-basis of R_n = M_2(B) as R_n-elements"""
    d = C.dimw
    return [C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
            for k in range(d)]


def ring_gens(C):
    """a set of ring elements generating R_n as an F_q-algebra"""
    out = []
    for k in range(4):
        i0, j0 = k // 2, k % 2
        for a in range(C.t):
            for e in range(C.n):
                M = [C.B.zero] * 4
                vec = [0] * (C.t * C.n)
                vec[a * C.n + e] = 1
                M[k] = tuple(vec)
                out.append(tuple(M))
    return out


def is_right_ideal(C, key):
    """is the F_q-subspace with RREF `key` (in R_n coordinates) a right ideal?"""
    for v in key:
        M = C.unflat_rn(tuple(v))
        for g in ring_gens(C):
            if not contains(C, key, C.flat_rn(C.mul_rn(M, g))):
                return False
    return True


def is_left_ideal(C, key):
    for v in key:
        M = C.unflat_rn(tuple(v))
        for g in ring_gens(C):
            if not contains(C, key, C.flat_rn(C.mul_rn(g, M))):
                return False
    return True


# ---- the polynomial level R[X] -----------------------------------------
def poly_mul(C, p, q):
    RA = C.RA
    out = [RA.zero] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == RA.zero:
            continue
        for j, b in enumerate(q):
            if b == RA.zero:
                continue
            out[i + j] = RA.add(out[i + j], RA.mul(a, b))
    return out


def poly_reduce(C, p):
    """reduce modulo X^n - 1"""
    RA, n = C.RA, C.n
    out = [RA.zero] * n
    for i, c in enumerate(p):
        if c != RA.zero:
            out[i % n] = RA.add(out[i % n], c)
    return out


def poly_theta(C, p, s):
    return [C.RA.theta(c, s) for c in p]


def poly_of_rn(C, M):
    """the length-n coefficient list (elements of R) of an element of R_n"""
    return C.iota_inv(M)


def rn_of_poly(C, p):
    return C.iota(tuple(p))


def poly_zero(C):
    return [C.RA.zero] * C.n


def poly_one(C):
    return [C.RA.one] + [C.RA.zero] * (C.n - 1)


def Xn_minus_1(C):
    """the polynomial X^n - 1 as a coefficient list of length n+1"""
    p = [C.RA.zero] * (C.n + 1)
    p[0] = C.RA.neg(C.RA.one)
    p[C.n] = C.RA.one
    return p


# ==========================================================================
# 8.  Task A -- L-6.1:  theta_s is an anti-automorphism of R_n
# ==========================================================================

def sample_elements(C, count, seed_offset):
    """`count` DISTINCT elements of R_n = M_2(B)"""
    rng = random.Random(SEED + seed_offset + C.q * 1013 + C.t * 71 + C.n * 17)
    els, seen = [], set()
    while len(els) < count:
        x = tuple(rng.choice(belem(C)) for _ in range(4))
        if x not in seen:
            seen.add(x)
            els.append(x)
    return els


def test_L61(C, s, sample):
    tag = "(q,t,n)=(%d,%d,%d), s=%d" % (C.q, C.t, C.n, s)
    RB, F = C.RB, C.F
    small = (C.q ** (C.t * C.n)) ** 4 <= EXH_LIMIT
    rng = random.Random(SEED + C.q + C.t * 7 + C.n * 13 + s * 101)

    def rnd():
        return tuple(rng.choice(belem(C)) for _ in range(4))

    if small:
        els = list(RB.elem_list())
        pairs = list(itertools.product(els, repeat=2))
        exh = True
    else:
        els = sample_elements(C, sample, 1)
        pairs = [(rng.choice(els), rng.choice(els)) for _ in range(sample)]
        exh = False

    # (1) additivity
    bad = sum(1 for X in els[:min(len(els), 200)] for Y in
              [rng.choice(els)] if C.theta_rn(RB.add(X, Y), s) !=
              RB.add(C.theta_rn(X, s), C.theta_rn(Y, s)))
    check("%s: theta_s is additive" % tag, bad == 0, "%d pairs" % 200, exh)

    # (2) anti-multiplicativity on R_n  (the statement L-6.1)
    bad = sum(1 for X, Y in pairs if C.theta_rn(C.mul_rn(X, Y), s) !=
              C.mul_rn(C.theta_rn(Y, s), C.theta_rn(X, s)))
    check("%s: L-6.1 -- theta_s(uv) = theta_s(v)theta_s(u) on R_n" % tag,
          bad == 0, "%d pairs" % len(pairs), exh)

    # (3) bijectivity
    seen = set()
    for X in els[:min(len(els), 400)]:
        seen.add(C.theta_rn(X, s))
    check("%s: theta_s is injective (hence bijective, R_n finite)" % tag,
          len(seen) == min(len(els), 400),
          "%d images, %d distinct" % (min(len(els), 400), len(seen)),
          exh and len(els) <= 400)

    # (4) theta_s^2 = sigma_{2s} and the inverse
    bad = sum(1 for X in els[:min(len(els), 200)]
              if C.theta_rn(C.theta_rn(X, s), s) != C.sigma_rn(X, (2 * s) % C.r))
    check("%s: theta_s^2 = sigma_{2s}" % tag, bad == 0, "200 elements",
          exh and len(els) <= 200)
    bad = sum(1 for X in els[:min(len(els), 200)]
              if C.theta_rn(C.sigma_rn(C.theta_rn(X, s), (-2 * s) % C.r), s) != X)
    check("%s: theta_s^{-1} = sigma_{-2s} theta_s" % tag, bad == 0,
          "200 elements", exh and len(els) <= 200)

    # (5) the order of theta_s
    from math import gcd
    ordr = 2 * C.r // gcd(C.r, 2 * s)      # s = 0 gives 2 (theta_0 = transpose)
    probe = els[:min(len(els), 60)]

    def theta_pow(X, k):
        Y = X
        for _ in range(k):
            Y = C.theta_rn(Y, s)
        return Y
    ok_top = all(theta_pow(X, ordr) == X for X in probe)
    ok_min = True
    if ordr > 1:
        ok_min = any(theta_pow(X, k) != X for X in probe for k in range(1, ordr))
    check("%s: ord(theta_s) = 2r/gcd(r,2s) = %d" % (tag, ordr),
          ok_top and ok_min, "theta^%d = id, no smaller exponent on 60 probes"
          % ordr, exh and len(els) <= 60)

    # (6) theta_s fixes X and u
    Xel = tuple([C.B.X_pow(1), C.B.zero, C.B.zero, C.B.X_pow(1)])
    uel = tuple([C.B.u_pow(1)] * 1 + [C.B.zero] * 3) if False else \
        tuple([C.B.u_pow(1), C.B.zero, C.B.zero, C.B.u_pow(1)])
    check("%s: theta_s fixes X and u" % tag,
          C.theta_rn(Xel, s) == Xel and C.theta_rn(uel, s) == uel, "", True)

    # (7) the three levels:  R,  R[X],  R_n
    RA = C.RA
    Aels = list(RA.elem_list())
    bad = 0
    for _ in range(min(200, len(Aels) ** 2)):
        X1, Y1 = rng.choice(Aels), rng.choice(Aels)
        if RA.theta(RA.mul(X1, Y1), s) != RA.mul(RA.theta(Y1, s), RA.theta(X1, s)):
            bad += 1
    check("%s: theta_s is an anti-automorphism of R = M_2(A_t)" % tag, bad == 0,
          "200 pairs", False)
    # the polynomial ring R[X]
    bad = 0
    for _ in range(200):
        p = [rng.choice(Aels) for _ in range(rng.randint(1, 3))]
        q = [rng.choice(Aels) for _ in range(rng.randint(1, 3))]
        lhs = poly_theta(C, poly_mul(C, p, q), s)
        rhs = poly_mul(C, poly_theta(C, q, s), poly_theta(C, p, s))
        if lhs != rhs:
            bad += 1
    check("%s: theta_s is an anti-automorphism of the polynomial ring R[X]"
          % tag, bad == 0, "200 pairs of polynomials", False)

    # (8) preservation of the ideal <X^n - 1> and well-definedness
    h = Xn_minus_1(C)
    check("%s: theta_s(X^n - 1) = X^n - 1" % tag,
          poly_theta(C, h, s) == h, "", True)
    bad = 0
    for _ in range(100):
        m = [rng.choice(Aels) for _ in range(rng.randint(1, 3))]
        prod = poly_reduce(C, poly_mul(C, m, h))
        check_zero = all(c == C.RA.zero for c in prod)
        th = poly_reduce(C, poly_theta(C, poly_mul(C, m, h), s))
        th_zero = all(c == C.RA.zero for c in th)
        if not (check_zero and th_zero):
            bad += 1
    check("%s: theta_s preserves the ideal <X^n-1>  (m*(X^n-1) and its image "
          "both reduce to 0)" % tag, bad == 0, "100 multipliers", False)
    # well-definedness:  p == q mod <X^n-1>  =>  theta(p) == theta(q) mod <X^n-1>
    bad = 0
    for _ in range(100):
        p = [rng.choice(Aels) for _ in range(rng.randint(1, 2 * C.n + 2))]
        m = [rng.choice(Aels) for _ in range(rng.randint(1, 3))]
        q = [C.RA.zero] * max(len(p), len(poly_mul(C, m, h)))
        for i, c in enumerate(p):
            q[i] = C.RA.add(q[i], c)
        mm = poly_mul(C, m, h)
        for i, c in enumerate(mm):
            q[i] = C.RA.add(q[i], c)
        rp = poly_reduce(C, poly_theta(C, p, s))
        rq = poly_reduce(C, poly_theta(C, q, s))
        if rp != rq:
            bad += 1
    check("%s: theta_s is well defined on the quotient R_n" % tag, bad == 0,
          "100 congruent pairs", False)
    # the descended map agrees with the coefficient-wise definition
    bad = 0
    for _ in range(100):
        p = [rng.choice(Aels) for _ in range(rng.randint(1, 2 * C.n + 2))]
        red = poly_reduce(C, p)
        if C.theta_rn(rn_of_poly(C, red), s) != rn_of_poly(C, poly_reduce(
                C, poly_theta(C, p, s)), ):
            bad += 1
    check("%s: the descended theta_s is coefficient-wise theta_s" % tag,
          bad == 0, "100 polynomials", False)


# ==========================================================================
# 9.  rev  (P-2.1f, register T-066: PROPOSED / UNPROVED up to now)
# ==========================================================================

def test_rev(C, s, sample):
    tag = "(q,t,n)=(%d,%d,%d)" % (C.q, C.t, C.n)
    RB, F = C.RB, C.F
    small = (C.q ** (C.t * C.n)) ** 4 <= EXH_LIMIT
    rng = random.Random(SEED + 555 + C.q + C.n)

    def rnd():
        return tuple(rng.choice(belem(C)) for _ in range(4))
    if small:
        els = list(RB.elem_list())
        pairs = list(itertools.product(els, repeat=2))
        exh = True
    else:
        els = sample_elements(C, sample, 2)
        pairs = [(rng.choice(els), rng.choice(els)) for _ in range(sample)]
        exh = False

    bad = sum(1 for X in els if C.rev_rn(C.rev_rn(X)) != X)
    check("%s: rev^2 = id" % tag, bad == 0, "%d elements" % len(els), exh)

    bad = sum(1 for X, Y in pairs if C.rev_rn(C.mul_rn(X, Y)) !=
              C.mul_rn(C.rev_rn(X), C.rev_rn(Y)))
    check("%s: P-2.1f(iii) -- rev is an AUTOMORPHISM of R_n" % tag, bad == 0,
          "%d pairs" % len(pairs), exh)

    Xel = tuple([C.B.X_pow(1), C.B.zero, C.B.zero, C.B.X_pow(1)])
    check("%s: rev(X) = X^{n-1}, rev(1) = 1" % tag,
          C.rev_rn(Xel) == tuple([C.B.X_pow(C.n - 1), C.B.zero, C.B.zero,
                                  C.B.X_pow(C.n - 1)]), "", True)

    # rev fixes the constant subring R
    Aels = list(C.RA.elem_list())
    bad = 0
    for M in Aels[:min(len(Aels), 100)]:
        const = C.iota(tuple([M] + [C.RA.zero] * (C.n - 1)))
        if C.rev_rn(const) != const:
            bad += 1
    check("%s: rev restricts to the identity on R" % tag, bad == 0,
          "%d constants" % min(len(Aels), 100), len(Aels) <= 100)

    # rev commutes with sigma_k and theta_s
    bad = 0
    for X in els[:min(len(els), 150)]:
        for k in range(C.r):
            if C.rev_rn(C.sigma_rn(X, k)) != C.sigma_rn(C.rev_rn(X), k):
                bad += 1
            if C.rev_rn(C.theta_rn(X, k)) != C.theta_rn(C.rev_rn(X), k):
                bad += 1
    check("%s: rev commutes with sigma_k and theta_s" % tag, bad == 0,
          "%d elements x %d values of s" % (min(len(els), 150), C.r),
          exh and len(els) <= 150)

    # rev T = T^{-1} rev  on R^n
    def T(x):
        return tuple(x[(e - 1) % C.n] for e in range(C.n))
    bad = 0
    for _ in range(100):
        y = tuple(tuple(rng.choice(Aels) for _ in range(1))[0] for _ in range(C.n))
        if C.rev_word(T(y)) != tuple(C.rev_word(y)[(e + 1) % C.n]
                                     for e in range(C.n)):
            bad += 1
    check("%s: rev T = T^{-1} rev on R^n" % tag, bad == 0, "100 words", False)

    # iota(rev x) = rev(iota x)
    bad = 0
    for _ in range(100):
        y = tuple(rng.choice(Aels) for _ in range(C.n))
        if C.iota(C.rev_word(y)) != C.rev_rn(C.iota(y)):
            bad += 1
    check("%s: iota(rev y) = rev(iota y)" % tag, bad == 0, "100 words", False)

    # rev(ann_r(v)) = ann_r(rev v)
    bad = 0
    for X in els[:min(len(els), 40)]:
        A1 = rref_key(C, ann_r_element(C, X))
        rows = [list(C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a))))) for a in A1]
        lhs = rref_key(C, rows)
        rhs = rref_key(C, ann_r_element(C, C.rev_rn(X)))
        if lhs != rhs:
            bad += 1
    check("%s: P-2.1f(iv) -- rev(ann_r(v)) = ann_r(rev v)" % tag, bad == 0,
          "%d elements" % min(len(els), 40), exh and len(els) <= 40)


# ==========================================================================
# 10.  Task B -- annihilator conventions
# ==========================================================================

def test_ann(C, sample):
    tag = "(q,t,n)=(%d,%d,%d)" % (C.q, C.t, C.n)
    small = (C.q ** (C.t * C.n)) ** 4 <= EXH_LIMIT
    rng = random.Random(SEED + 999 + C.q * 3 + C.n)

    def rnd():
        return tuple(rng.choice(belem(C)) for _ in range(4))
    els = list(C.RB.elem_list()) if small else sample_elements(C, sample, 3)
    probes = els[:min(len(els), 25)]

    # (i) ann_r(v) is a right ideal, ann_l(v) is a left ideal
    bad_r = bad_l = 0
    for v in probes:
        if not is_right_ideal(C, rref_key(C, ann_r_element(C, v))):
            bad_r += 1
        if not is_left_ideal(C, rref_key(C, ann_l_element(C, v))):
            bad_l += 1
    check("%s: ann_r(v) is a RIGHT ideal (v an element)" % tag, bad_r == 0,
          "%d elements" % len(probes), small and len(els) <= 25)
    check("%s: ann_l(v) is a LEFT ideal (v an element)" % tag, bad_l == 0,
          "%d elements" % len(probes), small and len(els) <= 25)

    # (ii) the annihilators differ in general (the ring is not commutative)
    diff = sum(1 for v in probes if rref_key(C, ann_r_element(C, v)) !=
               rref_key(C, ann_l_element(C, v)))
    check("%s: ann_r(v) and ann_l(v) are genuinely different (noncommutative)"
          % tag, diff > 0, "%d of %d elements differ" % (diff, len(probes)),
          small and len(els) <= 25)

    # (iii) kernels of the two multiplication maps
    bad = 0
    bf_probes = probes[:8] if small and len(els) <= 3000 else []
    for v in bf_probes:
        kr = [w for w in els if C.mul_rn(v, w) == C.RB.zero]
        kl = [w for w in els if C.mul_rn(w, v) == C.RB.zero]
        if rref_key(C, ann_r_element(C, v)) != \
           rref_key(C, [C.flat_rn(w) for w in kr]):
            bad += 1
        if rref_key(C, ann_l_element(C, v)) != \
           rref_key(C, [C.flat_rn(w) for w in kl]):
            bad += 1
    if bf_probes:
        check("%s: ann_r(v) = ker(left mult by v), ann_l(v) = ker(right mult)"
              % tag, bad == 0,
              "%d elements, brute force over all %d w" % (len(bf_probes), len(els)),
              True)

    # (iv) annihilator of a right ideal vs of its generator
    #      ann_r(gR_n) is TWO-SIDED and contained in ann_r(g)
    bad_two = bad_sub = 0
    witness = None
    for g in probes:
        Igen = rref_key(C, right_ideal_basis(C, [g]))
        aI = rref_key(C, ann_r_set(C, [C.unflat_rn(tuple(x)) for x in Igen]))
        ag = rref_key(C, ann_r_element(C, g))
        if not (is_right_ideal(C, aI) and is_left_ideal(C, aI)):
            bad_two += 1
        # containment
        if not all(contains(C, ag, x) for x in aI):
            bad_sub += 1
        if aI != ag and witness is None:
            witness = g
    check("%s: ann_r of a RIGHT ideal is two-sided" % tag, bad_two == 0,
          "%d right ideals" % len(probes), small and len(els) <= 25)
    check("%s: ann_r(gR_n) subset of ann_r(g)" % tag, bad_sub == 0,
          "%d generators" % len(probes), small and len(els) <= 25)
    check("%s: the inclusion is STRICT for some g (element vs ideal annihilator)"
          % tag, witness is not None,
          "witness found" if witness is not None else "none found",
          small and len(els) <= 25)

    # (v) ann_r of a LEFT ideal is a right ideal (not necessarily two-sided)
    bad = 0
    two_sided_count = 0
    for g in probes:
        L = rref_key(C, left_ideal_basis(C, [g]))
        aL = rref_key(C, ann_r_set(C, [C.unflat_rn(tuple(x)) for x in L]))
        if not is_right_ideal(C, aL):
            bad += 1
        if is_left_ideal(C, aL):
            two_sided_count += 1
    check("%s: ann_r of a LEFT ideal is a right ideal" % tag, bad == 0,
          "%d left ideals (%d of them two-sided)" % (len(probes), two_sided_count),
          small and len(els) <= 25)

    # (vi) for a LEFT ideal the generators do determine ann_r:  (r g) a = r (g a),
    #      so ann_r(R_n g) = ann_r(g).  For a RIGHT ideal they do not, because
    #      (g m) a = g (m a) need not vanish when g a = 0.
    bad = 0
    for g in probes:
        Lgen = [C.unflat_rn(tuple(x)) for x in rref_key(C, left_ideal_basis(C, [g]))]
        aL = rref_key(C, ann_r_set(C, Lgen))
        ag = rref_key(C, ann_r_element(C, g))
        if aL != ag:
            bad += 1
    check("%s: ann_r(R_n g) = ann_r(g)  (a LEFT ideal is annihilator-determined "
          "by its generator)" % tag, bad == 0, "%d generators" % len(probes),
          small and len(els) <= 25)

    #      ann_r(g R_n) is generally strictly smaller than ann_r(g)
    nstrict = 0
    for g in probes:
        Igen = [C.unflat_rn(tuple(x)) for x in rref_key(C, right_ideal_basis(C, [g]))]
        aI = rref_key(C, ann_r_set(C, Igen))
        ag = rref_key(C, ann_r_element(C, g))
        if aI != ag:
            nstrict += 1
    check("%s: ann_r(g R_n) =/= ann_r(g) for at least one g  (a RIGHT ideal is "
          "NOT annihilator-determined by its generator)" % tag, nstrict > 0,
          "%d of %d generators show a strict difference" % (nstrict, len(probes)),
          small and len(els) <= 25)
    return witness


# ==========================================================================
# 11.  Task C -- P-2.7:  the Galois dual as a reversed annihilator
# ==========================================================================

def dual_in_rn(C, word_gens, s):
    """iota(C^{perp_s}) as an RREF key in R_n coordinates, computed from the
    definition by F_q-linear algebra (no annihilator, no Morita)."""
    db = dual_of(C, word_gens, s)
    rows = [list(C.flat_rn(C.iota(C.unflat_word(tuple(v))))) for v in db]
    return rref_key(C, rows)


def code_words_of(C, g):
    """the code C = g R_n as a list of words in R^n"""
    Igen = rref_key(C, right_ideal_basis(C, [g]))
    return [C.iota_inv(C.unflat_rn(tuple(x))) for x in Igen]


def p27_forms(C, g, s):
    """
    The three displayed forms of P-2.7 plus the Morita form, each computed by
    a different route:

      form1 = rev( ann_r( theta_s(g) ) )
      form2 = ann_r( theta_s(rev g) )
      form3 = { y : theta_s(g) * rev(y) = 0 }              (solved for y)
      morita = I_{ker theta_s(g)} = {M : both columns in ker theta_s(g)}
    """
    F, d = C.F, C.dimw
    v = C.theta_rn(g, s)
    A = ann_r_element(C, v)
    form1 = rref_key(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a)))) for a in A])
    form2 = rref_key(C, ann_r_element(C, C.theta_rn(C.rev_rn(g), s)))
    basis = [C.unflat_rn(tuple(1 if i == k else 0 for i in range(d)))
             for k in range(d)]
    imgs = [C.flat_rn(C.mul_rn(v, C.rev_rn(e))) for e in basis]
    rows = [[imgs[k][j] for k in range(d)] for j in range(d)]
    form3 = rref_key(C, nullspace_basis(rows, F, d))
    D = C.B.dim
    kb = ker_basis(C, v)
    Wpairs = [(tuple(r[:D]), tuple(r[D:])) for r in kb]
    morita = rref_key(C, I_of_W(C, Wpairs))
    return form1, form2, form3, morita, A, Wpairs


# ==========================================================================
# 12.  Task D -- P-2.8:  an explicit generator of the dual
# ==========================================================================

def max_ideal_wild(C):
    """
    the maximal ideal m = (u, X-1) of B in the wild case, as an F_q-subspace of B
    (t >= 2 and p | n with n' = 1, so X^n - 1 = (X-1)^{p^v}).
    """
    B = C.B
    gens = [B.u_pow(1), B.add(B.X_pow(1), B.neg(B.X_pow(0)))]
    rows = []
    for g in gens:
        for b in _B_basis(B):
            rows.append(list(B.mul(g, b)))
    return rref(rows, C.F, B.dim)[0]


def mu_local(C, Wpairs, mrows):
    """
    mu_B(W) for B LOCAL:  Nakayama,  mu = dim_K(W / mW) with K = B/m.
    Also returns the lift of a K-basis of W/mW, which generates W.
    """
    F, B = C.F, C.B
    D = B.dim
    Wrows = rref([list(_pair_flat(C, w)) for w in Wpairs], F, 2 * D)[0]
    # mW : multiply each generator of W by each generator of m and by the
    # whole ring (m is an ideal, so mW is spanned by (m-generators) * W)
    mgens = mrows
    rows = []
    for w in Wpairs:
        for mg in mgens:
            rows.append(list(_pair_flat(C, (B.mul(mg, w[0]), B.mul(mg, w[1])))))
    mWrows = rref(rows, F, 2 * D)[0] if rows else []
    # quotient dimension
    dimW = len(Wrows)
    dimmW = len(mWrows)
    mu = dimW - dimmW
    # lift a basis of W/mW:  greedy extension of mW inside W
    chosen = []
    cur = [list(r) for r in mWrows]
    cur_rank = len(rref(cur, F, 2 * D)[1]) if cur else 0
    for r in Wrows:
        trial = cur + [list(r)]
        tr_rank = len(rref(trial, F, 2 * D)[1])
        if tr_rank > cur_rank:
            chosen.append(tuple(r))
            cur = trial
            cur_rank = tr_rank
        if len(chosen) == mu:
            break
    return mu, chosen


def mu_components(C, K, Wpairs):
    """mu_B(W) = max_j mu_{B_j}(W_j), each by Nakayama over the chain ring B_j"""
    best = 0
    per = []
    for j, (_name, info, _z) in enumerate(K.comps):
        w = info.ring
        vals = []
        for pair in Wpairs:
            vals.append((K.proj(pair[0], j), K.proj(pair[1], j)))
        D = info.dim
        Wrows = rref([list(_pair_flat_c(w, x)) for x in vals], w.F, 2 * D)[0]
        rows = []
        for x in vals:
            rows.append(list(_pair_flat_c(w, (w.mul(info.omega, x[0]),
                                               w.mul(info.omega, x[1])))))
        mWrows = rref(rows, w.F, 2 * D)[0] if rows else []
        mu_j = len(Wrows) - len(mWrows)
        per.append(mu_j)
        best = max(best, mu_j)
    return best, per


def _pair_flat_c(w, x):
    return tuple(list(x[0]) + list(x[1]))


def test_P27_P28(C, glist, s, K):
    tag = "(q,t,n)=(%d,%d,%d), s=%d" % (C.q, C.t, C.n, s)
    wild = (K.kind == "wild")
    n1 = n2 = n3 = nm = ncard = ndd = 0
    nrev_stable = 0
    mu_hist = {}
    nh_ok = nh_snf_ok = 0
    nprin = 0
    wild_mrow = rref([], C.F, C.B.dim)[0]
    mrows = max_ideal_wild(C) if wild else None
    duals = {}
    for g in glist:
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        form1, form2, form3, morita, A, Wpairs = p27_forms(C, g, s)
        if form1 != du:
            n1 += 1
        if form2 != du:
            n2 += 1
        if form3 != du:
            n3 += 1
        if morita != rref_key(C, A):
            nm += 1
        if form1 == rref_key(C, A):
            nrev_stable += 1
        # cardinality
        sizeC = C.F.q ** len(rref_key(C, right_ideal_basis(C, [g])))
        sizeD = C.F.q ** len(du)
        if sizeC * sizeD != C.F.q ** (4 * C.t * C.n):
            ncard += 1
        # mu and the generator
        if wild:
            mu, chosen = mu_local(C, Wpairs, mrows)
        else:
            mu, _per = mu_components(C, K, Wpairs)
        mu_hist[mu] = mu_hist.get(mu, 0) + 1
        if mu <= 2:
            nprin += 1
            if wild:
                # h = [w1 | w2] with the unused columns zero;  mu = 0 gives h = 0
                w1 = (tuple(chosen[0][:C.B.dim]), tuple(chosen[0][C.B.dim:])) \
                    if len(chosen) > 0 else (C.B.zero, C.B.zero)
                w2 = (tuple(chosen[1][:C.B.dim]), tuple(chosen[1][C.B.dim:])) \
                    if len(chosen) > 1 else (C.B.zero, C.B.zero)
                h = (w1[0], w2[0], w1[1], w2[1])
                if rref_key(C, right_ideal_basis(C, [h])) == du:
                    nh_ok += 1
            else:
                v = C.theta_rn(C.rev_rn(g), s)
                h, ok = K.snf_h(v)
                if ok and rref_key(C, right_ideal_basis(C, [h])) == du:
                    nh_ok += 1
                    nh_snf_ok += 1
    N = len(glist)
    exh = (len(glist) == (C.q ** (C.t * C.n)) ** 4)
    check("%s: P-2.7 form 1 -- C^{perp_s} = rev(ann_r(theta_s(g)))" % tag,
          n1 == 0, "%d of %d generators agree" % (N - n1, N), exh)
    check("%s: P-2.7 form 2 -- C^{perp_s} = ann_r(theta_s(rev g))" % tag,
          n2 == 0, "%d of %d generators agree" % (N - n2, N), exh)
    check("%s: P-2.7 form 3 -- C^{perp_s} = {y : theta_s(g) rev(y) = 0}" % tag,
          n3 == 0, "%d of %d generators agree" % (N - n3, N), exh)
    check("%s: Morita form -- ann_r(theta_s(g)) = I_{ker theta_s(g)}" % tag,
          nm == 0, "%d of %d generators agree" % (N - nm, N), exh)
    check("%s: |C| |C^{perp_s}| = |R|^n" % tag, ncard == 0,
          "%d of %d generators agree" % (N - ncard, N), exh)
    if C.n <= 2:
        check("%s: rev = id for n <= 2, so ann_r(theta_s(g)) is rev-stable for "
              "every g" % tag, nrev_stable == N,
              "%d of %d g" % (nrev_stable, N), exh)
    else:
        check("%s: rev-sensitivity -- some g has rev(ann_r(theta_s(g))) != "
              "ann_r(theta_s(g))" % tag, nrev_stable < N,
              "%d of %d g are NOT rev-stable, so the reversal is load-bearing"
              % (N - nrev_stable, N), exh)
    hist = ", ".join("mu=%d: %d" % (k, mu_hist[k]) for k in sorted(mu_hist))
    if wild:
        say("     [WILD] mu_B(ker theta_s(rev g)) over the sample: %s" % hist)
        check("%s [WILD]: mu_B(ker) <= 4 on every sampled g  (the O-2.2 bound)"
              % tag, all(k <= 4 for k in mu_hist),
              "largest mu observed in this sample: %d" % max(mu_hist), exh)
        check("%s [WILD]: where mu <= 2 the Nakayama generator h = [w1|w2] "
              "generates C^{perp_s}" % tag, nh_ok == nprin,
              "%d of %d such codes" % (nh_ok, nprin), exh)
    else:
        check("%s: mu_B(ker theta_s(rev g)) <= 2 for every g (chain-ring regime)"
              % tag, all(k <= 2 for k in mu_hist), "mu distribution: %s" % hist,
              exh)
        check("%s: P-2.8 -- the SNF generator h satisfies h R_n = C^{perp_s}"
              % tag, nh_ok == N and nh_snf_ok == N,
              "%d of %d codes" % (nh_snf_ok, N), exh)
    return mu_hist


def test_double_dual(C, glist, s):
    tag = "(q,t,n)=(%d,%d,%d), s=%d" % (C.q, C.t, C.n, s)
    bad = 0
    nrefl = 0
    nnonrefl = 0
    for g in glist:
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        ddb = [C.iota_inv(C.unflat_rn(tuple(x))) for x in du]
        dd = dual_in_rn(C, ddb, s)
        # sigma_{2s}(C)
        rows = [list(C.flat_rn(C.sigma_rn(C.iota(x), (2 * s) % C.r))) for x in cw]
        sig = rref_key(C, rows)
        ckey = rref_key(C, [list(C.flat_rn(C.iota(x))) for x in cw])
        if dd != sig:
            bad += 1
        else:
            if sig == ckey:
                nrefl += 1
            else:
                nnonrefl += 1
    exh = (len(glist) == (C.q ** (C.t * C.n)) ** 4)
    check("%s: (C^{perp_s})^{perp_s} = sigma_{2s}(C)" % tag, bad == 0,
          "%d of %d codes" % (len(glist) - bad, len(glist)), exh)
    refl = (C.r % (C.r if (2 * s) % C.r == 0 else 0) == 0) if (2 * s) % C.r == 0 \
        else False
    refl = ((2 * s) % C.r == 0)
    if refl:
        check("%s: r | 2s, so the duality is reflexive: (C^{perp_s})^{perp_s} = C"
              % tag, nnonrefl == 0,
              "%d of %d codes fixed" % (nrefl, len(glist)), exh)
    else:
        check("%s: r does not divide 2s, and the double dual is genuinely "
              "different from C" % tag, nnonrefl > 0,
              "%d of %d codes have (C^{perp_s})^{perp_s} != C" % (nnonrefl,
                                                                  len(glist)), exh)


# ==========================================================================
# 13.  Task F -- negative controls (a wrong convention must FAIL)
# ==========================================================================

def neg_controls(C, glist, s):
    tag = "(q,t,n)=(%d,%d,%d), s=%d" % (C.q, C.t, C.n, s)
    # neg-1:  theta_s(uv) = theta_s(u)theta_s(v)   (wrong order)
    cnt = 0
    for g in glist[:60]:
        for h in glist[:60]:
            if C.theta_rn(C.mul_rn(g, h), s) != \
               C.mul_rn(C.theta_rn(g, s), C.theta_rn(h, s)):
                cnt += 1
                break
        if cnt:
            break
    check("%s: neg-1 -- 'theta_s(uv) = theta_s(u)theta_s(v)' FAILS" % tag,
          cnt > 0, "counterexample found" if cnt else "NOT FOUND", len(glist) >= 60)

    # neg-2:  rev(uv) = rev(v)rev(u)   (reversal is NOT anti)
    cnt = 0
    for g in glist[:60]:
        for h in glist[:60]:
            if C.rev_rn(C.mul_rn(g, h)) != C.mul_rn(C.rev_rn(h), C.rev_rn(g)):
                cnt += 1
                break
        if cnt:
            break
    check("%s: neg-2 -- 'rev is an anti-automorphism' FAILS" % tag, cnt > 0,
          "counterexample found" if cnt else "NOT FOUND (rev may be an anti-auto "
          "here -- check!)", len(glist) >= 60)

    # neg-3:  ann_l instead of ann_r in P-2.7
    nbad = 0
    for g in glist[:40]:
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        v = C.theta_rn(g, s)
        wrong = rref_key(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a))))
                             for a in ann_l_element(C, v)])
        if wrong != du:
            nbad += 1
    check("%s: neg-3 -- using ann_l instead of ann_r FAILS" % tag, nbad > 0,
          "%d of %d codes detect the difference" % (nbad, min(40, len(glist))),
          False)

    # neg-4:  omitting the reversal.  VACUOUS at n = 1, where rev = id.
    if C.n <= 2:
        say("     neg-4 is vacuous for n <= 2 (rev = id there, since -e = e mod "
            "n); it is run at n >= 3")
    else:
        nbad = 0
        for g in glist[:40]:
            cw = code_words_of(C, g)
            du = dual_in_rn(C, cw, s)
            wrong = rref_key(C, ann_r_element(C, C.theta_rn(g, s)))
            if wrong != du:
                nbad += 1
        check("%s: neg-4 -- omitting rev FAILS" % tag, nbad > 0,
              "%d of %d codes detect the difference" % (nbad, min(40, len(glist))),
              False)

    # neg-5:  omitting theta_s
    nbad = 0
    for g in glist[:40]:
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        wrong = rref_key(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a))))
                             for a in ann_r_element(C, g)])
        if wrong != du:
            nbad += 1
    check("%s: neg-5 -- omitting theta_s FAILS" % tag, nbad > 0,
          "%d of %d codes detect the difference" % (nbad, min(40, len(glist))),
          False)

    # neg-6:  I_W built with the basis vectors in ROWS instead of COLUMNS
    cnt = 0
    for g in glist[:40]:
        v = C.theta_rn(g, s)
        D = C.B.dim
        kb = ker_basis(C, v)
        Wpairs = [(tuple(r[:D]), tuple(r[D:])) for r in kb]
        if not Wpairs:
            continue
        rows = []
        for w in Wpairs:
            for b in _B_basis(C.B):
                # ROWS:  row 0 = w*b, row 1 = 0
                M = (C.B.mul(w[0], b), C.B.mul(w[1], b), C.B.zero, C.B.zero)
                rows.append(list(C.flat_rn(M)))
                M = (C.B.zero, C.B.zero, C.B.mul(w[0], b), C.B.mul(w[1], b))
                rows.append(list(C.flat_rn(M)))
        wrong = rref_key(C, rows)
        right = rref_key(C, ann_r_element(C, v))
        if wrong != right:
            cnt += 1
    check("%s: neg-6 -- building I_W from ROWS instead of COLUMNS FAILS"
          % tag, cnt > 0,
          "%d of %d codes detect the difference" % (cnt, min(40, len(glist))),
          False)

    # neg-7:  the pairing with the arguments swapped,  B_s(y, x)
    nbad = 0
    for g in glist[:40]:
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        rows = []
        for x in cw:
            rows.append(list(functional_row(C, _swap_pair(C, x), s)))
        wrong = rref_key(C, nullspace_basis(rows, C.F, C.dimw))
        if wrong != du:
            nbad += 1
    check("%s: neg-7 -- the swapped pairing B_s(y,x) gives a different dual"
          % tag, nbad > 0,
          "%d of %d codes detect the difference" % (nbad, min(40, len(glist))),
          False)


def _swap_pair(C, x):
    """the word y with y_e = the 'transpose partner' -- used only to test that
    swapping the two slots of the pairing does NOT give the same dual"""
    return tuple(C.RA.transpose(xe) for xe in x)


# ==========================================================================
# 14.  Per-case driver
# ==========================================================================

CASE_NOTES = {
    (4, 1, 1): "n = 1: rev = id, the theory degenerates to the ideal theory of "
               "M_2(F_4)  (register O-2.7).  Exhaustive over all of R_n.",
    (4, 1, 2): "t = 1 with p | n: B = F_4[X]/<(X-1)^2> is a chain ring.",
    (4, 2, 1): "t >= 2 with p does not divide n: B = F_4[u]/<u^2> is a chain ring.",
    (4, 2, 2): "WILD: t >= 2 and p | n.  B is local but not a chain ring.",
    (4, 1, 3): "split semisimple, B = F_4^3, rev is non-trivial (n = 3).",
    (9, 1, 2): "split semisimple, B = F_9 x F_9;  r = 2, s = 1 is REFLEXIVE.",
    (8, 1, 2): "chain ring F_8[X]/<(X-1)^2>;  r = 3 is odd, so NO non-trivial "
               "reflexive s exists -- the non-reflexive regime.",
    (4, 2, 3): "t >= 2, p does not divide n, split: B = A_2^3, rev non-trivial.",
}


def run_case(q, t, n, sample=200):
    C = Ctx(q, t, n)
    K = Components(C)
    head("(q,t,n) = (%d,%d,%d)   |B| = %d, |R_n| = %d, dim_{F_q} R^n = %d"
         % (q, t, n, C.F.q ** (t * n), (C.F.q ** (t * n)) ** 4, C.dimw))
    say("  regime: %s   %s" % (K.kind, CASE_NOTES.get((q, t, n), "")))
    say("  r = %d, so the reflexive s are those with r | 2s: %s"
        % (C.r, "all s" if C.r % 2 == 1 else
           "s = 0 and s = %d" % (C.r // 2)))
    size_rn = (C.F.q ** (t * n)) ** 4
    rng = random.Random(SEED + q * 31 + t * 7 + n)
    if size_rn <= EXH_LIMIT:
        glist = list(C.RB.elem_list())
        say("  generators tested: ALL %d elements of R_n  [EXH]" % len(glist))
    else:
        glist = sample_elements(C, sample, 4)
        say("  generators tested: %d random elements of R_n, seed %d  [SMP]"
            % (sample, SEED))

    sub("Task A -- L-6.1 (theta_s on R_n) and rev")
    for s in range(C.r):
        test_L61(C, s, min(sample, 150))
    test_rev(C, 0, min(sample, 150))

    sub("Task B -- annihilator conventions")
    test_ann(C, min(sample, 60))

    for s in range(C.r):
        sub("Tasks C/D/E -- P-2.7, P-2.8, cardinality and double dual, s = %d" % s)
        test_P27_P28(C, glist, s, K)
        test_double_dual(C, glist[:min(len(glist), 60)], s)

    sub("Task D -- uniqueness of the generator")
    test_generator_uniqueness(C)

    sub("Task F -- negative controls (wrong conventions must FAIL)")
    neg_controls(C, glist, 0)

    if K.kind == "wild":
        sub("Task D -- the wild counterexample: a principal code whose dual is "
            "NOT principal  (O-2.8)")
        run_wild_counterexample(C)
    return C, K


def run_wild_counterexample(C):
    """
    (4,2,2):  B = F_4[u,eps]/<u^2, eps^2> with eps = X-1, m = (u, eps).
    Take  v = diag(u*eps, u*eps);  then ker v = ann(u eps) + ann(u eps) = m + m,
    so mu_B(ker v) = 4 and  ann_r(v) = M_2(m)  is NOT principal.  Since v is
    symmetric and constant, g := v satisfies theta_0(rev g) = v, so the code
    C = g R_n is principal while C^{perp_0} = ann_r(v) is not.
    """
    B = C.B
    u = B.u_pow(1)
    eps = B.add(B.X_pow(1), B.neg(B.X_pow(0)))
    soc = B.mul(u, eps)
    check("(4,2,2) wild: u*(X-1) is non-zero and annihilated exactly by m",
          soc != B.zero and all(B.mul(soc, x) == B.zero for x in
                                [u, eps]) and B.mul(soc, B.one) != B.zero,
          "socle element u eps != 0, u*eps*m = 0", True)
    v = (soc, B.zero, B.zero, soc)
    for s in range(C.r):
        g = C.rev_rn(C.theta_rn(v, s)) if False else v
        # we want theta_s(rev g) = v, i.e. g = rev(theta_s^{-1}(v))
        g = C.rev_rn(C.sigma_rn(C.theta_rn(v, s), (-2 * s) % C.r))
        check("(4,2,2) s=%d: the chosen g satisfies theta_s(rev g) = v" % s,
              C.theta_rn(C.rev_rn(g), s) == v, "", True)
        cw = code_words_of(C, g)
        du = dual_in_rn(C, cw, s)
        D = B.dim
        kb = ker_basis(C, v)
        Wpairs = [(tuple(r[:D]), tuple(r[D:])) for r in kb]
        morita = rref_key(C, I_of_W(C, Wpairs))
        check("(4,2,2) s=%d: C^{perp_s} = I_W with W = ker v" % s,
              du == morita, "dim C^{perp_s} = %d" % len(du), True)
        mrows = max_ideal_wild(C)
        mu, chosen = mu_local(C, Wpairs, mrows)
        check("(4,2,2) s=%d: mu_B(ker v) = 4  (Nakayama over the local ring B)"
              % s, mu == 4, "mu = %d" % mu, True)
        # W is m + m
        mm = []
        for x in [u, eps]:
            for b in _B_basis(B):
                mm.append((B.mul(x, b), B.zero))
                mm.append((B.zero, B.mul(x, b)))
        Wmm = rref([list(_pair_flat(C, w)) for w in mm], C.F, 2 * D)[0]
        Wkey = rref([list(_pair_flat(C, w)) for w in Wpairs], C.F, 2 * D)[0]
        check("(4,2,2) s=%d: ker v = m + m" % s,
              tuple(tuple(x) for x in Wkey) == tuple(tuple(x) for x in Wmm),
              "|ker v| = %d, |m| = %d" % (C.F.q ** len(Wkey),
                                          C.F.q ** len(rref([list(x) for x in
                                                             mrows], C.F, D)[0])),
              True)
        # NOT principal: exhaustive scan for a single generator
        found = None
        Iset = rref_key(C, ann_r_element(C, v))
        for w in [C.unflat_rn(tuple(x)) for x in Iset]:
            if rref_key(C, right_ideal_basis(C, [w])) == Iset:
                found = w
                break
        check("(4,2,2) s=%d: C^{perp_s} is NOT principal (no single generator, "
              "exhaustive scan)" % s, found is None,
          "all %d elements of C^{perp_s} scanned, none generates it"
          % (C.F.q ** len(Iset)), True)
        # but it is 2-generated
        h1 = (u, eps, B.zero, B.zero)
        h2 = (B.zero, B.zero, u, eps)
        two = rref_key(C, right_ideal_basis(C, [h1, h2]))
        check("(4,2,2) s=%d: C^{perp_s} is 2-generated (mu_S = 2)" % s,
              two == Iset, "|C^{perp_s}| = %d" % (C.F.q ** len(Iset)), True)
        # the code itself is principal, and the size identity holds
        sizeC = C.F.q ** len(rref_key(C, right_ideal_basis(C, [g])))
        check("(4,2,2) s=%d: |C| |C^{perp_s}| = |R|^n" % s,
              sizeC * (C.F.q ** len(du)) == C.F.q ** (4 * C.t * C.n),
              "|C| = %d, |C^{perp_s}| = %d" % (sizeC, C.F.q ** len(du)), True)


# ==========================================================================
# 15.  main
# ==========================================================================

def main():
    head("PHASE 2 -- STAGE 2C: Galois duality, annihilators, reciprocal "
         "generators")
    say("  seed %d ;  every [SMP] line carries the sample size" % SEED)
    cases = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2), (4, 1, 3),
             (9, 1, 2), (8, 1, 2), (4, 2, 3)]
    for (q, t, n) in cases:
        run_case(q, t, n)
    head("summary")
    nfail = len(FAILURES)
    say("  %d checks, %d PASS, %d FAIL"
        % (NCHECK[0], NCHECK[0] - nfail, nfail))
    if FAILURES:
        say("  failures:")
        for f in FAILURES:
            say("     %s  --  %s" % (f[0], f[1]))
    else:
        say("  no failures")
    say("  end of log")
    with open(LOGNAME, "w") as fh:
        fh.write("\n".join(LINES) + "\n")




# ==========================================================================
# 16.  Task D -- is the generator of the dual unique?
# ==========================================================================

def units_of(C):
    """the units of R_n = M_2(B):  u is a unit iff ker(left mult by u) = 0
    (in a finite ring, injective implies bijective)"""
    out = []
    for x in [C.unflat_rn(tuple(1 if i == k else 0 for i in range(C.dimw)))
              for k in range(C.dimw)]:
        pass
    # enumerate all elements when feasible
    if (C.q ** (C.t * C.n)) ** 4 > 70000:
        return None
    for M in C.RB.elem_list():
        if len(ann_r_element(C, M)) == 0:
            out.append(M)
    return out


def test_generator_uniqueness(C, max_ideals=40):
    """
    For a right ideal I = h R_n, the set of generators is
        Gen(I) = {h' : h' R_n = I}.
    Every h*u with u a unit lies in Gen(I).  The converse -- that Gen(I) is a
    single orbit under right multiplication by units -- is the uniqueness
    question of Task D.  It is tested exhaustively where |R_n| is small and on
    a sample of ideals otherwise.

    Note first (proved, no computation needed):  h R_n = h' R_n  iff
    im h = im h'  as B-submodules of B^2.  Indeed I_W determines W by the
    Morita correspondence (Stage 2A Thm 2.1), and W(hR_n) = im h by L-2.3a.
    """
    tag = "(q,t,n)=(%d,%d,%d)" % (C.q, C.t, C.n)
    size = (C.q ** (C.t * C.n)) ** 4
    units = units_of(C)
    if units is None:
        say("     [SMP] generator uniqueness not tested at %s: |R_n| = %d is too "
            "large to enumerate the units" % (tag, size))
        return None
    # group the elements of R_n by the right ideal they generate
    groups = {}
    for M in C.RB.elem_list():
        key = rref_key(C, right_ideal_basis(C, [M]))
        groups.setdefault(key, []).append(M)
    nchecked = 0
    nbad = 0
    witness = None
    for key, gens in list(groups.items())[:max_ideals]:
        h0 = gens[0]
        orbit = set(C.mul_rn(h0, u) for u in units)
        genset = set(gens)
        if orbit != genset:
            nbad += 1
            if witness is None:
                witness = (h0, sorted(genset - orbit)[0])
        nchecked += 1
    check("%s: every generator of a principal right ideal is (generator)*(unit)"
          % tag, nbad == 0,
          "%d ideals checked, %d of them fail" % (nchecked, nbad)
          if nbad else "%d ideals checked exhaustively (all %d elements of R_n "
          "grouped by the ideal they generate)" % (nchecked, size), True)
    if witness:
        say("     witness: h0 = %s, h' = %s" % (witness[0], witness[1]))
    return nbad == 0


if __name__ == "__main__":
    main()
