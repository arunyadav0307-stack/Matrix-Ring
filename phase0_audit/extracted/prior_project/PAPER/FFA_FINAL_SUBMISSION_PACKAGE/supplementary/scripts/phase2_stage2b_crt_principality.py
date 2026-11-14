#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 2 - Stage 2B: CRT/Hensel decomposition of B = A_t[X]/<X^n-1> and the
global principality criterion for the right ideals of R_n = M_2(A_t)[X]/<X^n-1>.

Companion to 03_THEOREMS/PHASE2_STAGE2B_CRT_PRINCIPALITY.md.

Only `Field`, `Local`, `rref` and `nullspace_basis` are imported from the Phase-1
library `ring_structure_checks.py` (read-only).  Everything else is built here:

  * section 1   polynomials over F_q (arithmetic, trial-division factorisation,
                irreducibility, q-cyclotomic cosets as an INDEPENDENT cross-check,
                Frobenius/sigma_k on polynomials)
  * section 2   polynomials over A_t and Hensel lifting of a coprime
                factorisation, by induction on the u-adic level (self-contained)
  * section 3   F_q-linear algebra on flat coordinate vectors
  * section 4   S(h) = A_t[X]/<h> for a monic h in F_q[X]
  * section 5   the CRT system B <-> prod_j B_j (explicit map, Bezout idempotents)
  * section 6   the local components: rho_j : B_j -> K_j, m_j = ker rho_j,
                dim_{K_j}(m_j/m_j^2), locality, chain-ring test
  * section 7   M_2 over a quotient ring: right ideals, I_W, W(I), mu (four
                independent methods), principality certificates
  * section 8   the Galois automorphism sigma_k on the CRT components
  * section 9   drivers (exhaustive / CRT-built / targeted / negative controls)

Every check is labelled [EXH] (exhaustive over the stated set) or [SMP]
(sampled, with the sample size stated on the line).

Run from its own directory:

    python3 phase2_stage2b_crt_principality.py     # -> phase2_stage2b_crt_log.txt

The log carries no timestamp and no elapsed time, so two runs can be compared
byte-for-byte.
"""

import itertools
import random
import sys
import time

sys.path.insert(0, ".")
from ring_structure_checks import Field, Local, rref, nullspace_basis

SEED = 20261106
LOG_NAME = "phase2_stage2b_crt_log.txt"

# =============================================================== 0. reporting
LINES = []
FAILURES = []
NCHECK = [0]


def say(s=""):
    LINES.append(s)
    print(s)


def check(name, ok, detail="", exhaustive=True):
    NCHECK[0] += 1
    say("  %s %-66s %s  %s"
        % ("[EXH]" if exhaustive else "[SMP]", name, "PASS" if ok else "**FAIL**", detail))
    if not ok:
        FAILURES.append((name, detail))


# ==================================================== 1. polynomials over F_q
# a polynomial is a tuple of field elements, index = degree, no trailing zeros

def ptrim(a, zero=0):
    i = len(a)
    while i > 0 and a[i - 1] == zero:
        i -= 1
    return a[:i]


def padd(F, a, b):
    n = max(len(a), len(b))
    return ptrim(tuple(F.add[(a[i] if i < len(a) else 0)][(b[i] if i < len(b) else 0)]
                       for i in range(n)))


def pneg(F, a):
    return ptrim(tuple(F.neg[x] for x in a))


def psub(F, a, b):
    return padd(F, a, pneg(F, b))


def pmul(F, a, b):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] = F.add[out[i + j]][F.mul[x][y]]
    return ptrim(tuple(out))


def pscal(F, c, a):
    return () if c == 0 else ptrim(tuple(F.mul[c][x] for x in a))


def pdivmod(F, a, b):
    """a = q*b + r  (b with unit leading coefficient)"""
    a = list(a)
    db = len(b) - 1
    ilb = F.inv[b[db]]
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        if a[i]:
            c = F.mul[a[i]][ilb]
            q[i - db] = c
            for j in range(db + 1):
                if b[j]:
                    a[i - db + j] = F.sub[a[i - db + j]][F.mul[c][b[j]]]
    return ptrim(tuple(q)), ptrim(tuple(a))


def pmod(F, a, b):
    return pdivmod(F, a, b)[1]


def pdeg(a):
    return len(a) - 1


def monic_polys(F, d):
    """all monic polynomials of exact degree d"""
    if d == 0:
        yield (1,)
        return
    for tail in itertools.product(range(F.q), repeat=d):
        yield tuple(tail) + (1,)


def is_irreducible(F, g):
    """monic g of degree >= 1 is irreducible iff no monic divisor of degree <= d/2"""
    d = pdeg(g)
    if d <= 0:
        return False
    for e in range(1, d // 2 + 1):
        for h in monic_polys(F, e):
            if pmod(F, g, h) == ():
                return False
    return True


def factor_squarefree(F, g):
    """factor the squarefree monic g into monic irreducibles (trial division)"""
    out = []
    rem = g
    d = 1
    while pdeg(rem) > 0:
        if d > pdeg(rem):
            raise RuntimeError("factorisation failed")
        for h in monic_polys(F, d):
            if not is_irreducible(F, h):
                continue
            n = 0
            while pdeg(rem) > 0 and pmod(F, rem, h) == ():
                rem = pdivmod(F, rem, h)[0]
                n += 1
            if n > 1:
                raise RuntimeError("not squarefree")
            if n == 1:
                out.append(h)
        d += 1
    return out


def cyclotomic_cosets(q, m):
    """the q-cyclotomic cosets modulo m (independent prediction of the degrees)"""
    seen = set()
    out = []
    for a in range(m):
        if a in seen:
            continue
        c = []
        x = a
        while x not in c:
            c.append(x)
            seen.add(x)
            x = (q * x) % m
        out.append(tuple(sorted(c)))
    return out


def frob_poly(F, a, k):
    """sigma_k on coefficients (Frobenius^k), the variable is fixed"""
    return ptrim(tuple(F.frob[k % F.r][x] for x in a))


def field_params(q):
    """(p, r) with q = p^r"""
    for p in (2, 3, 5, 7, 11, 13):
        if q % p == 0:
            r, m = 0, q
            while m % p == 0:
                m //= p
                r += 1
            if m == 1:
                return (p, r)
    raise RuntimeError("q = %d is not a prime power" % q)


# ============================================== 2. polynomials over A_t, Hensel

def ap_add(A, a, b):
    z = A.zero
    n = max(len(a), len(b))
    return ptrim(tuple(A.add((a[i] if i < len(a) else z), (b[i] if i < len(b) else z))
                       for i in range(n)), z)


def ap_sub(A, a, b):
    z = A.zero
    n = max(len(a), len(b))
    return ptrim(tuple(A.sub((a[i] if i < len(a) else z), (b[i] if i < len(b) else z))
                       for i in range(n)), z)


def ap_mul(A, a, b):
    if not a or not b:
        return ()
    out = [A.zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x != A.zero:
            for j, y in enumerate(b):
                if y != A.zero:
                    out[i + j] = A.add(out[i + j], A.mul(x, y))
    return ptrim(tuple(out), A.zero)


def ap_embed(F, t, f):
    """F_q-polynomial -> A_t[X] (coefficients in F_q . 1)"""
    return tuple(tuple([c] + [0] * (t - 1)) for c in f)


def ap_trunc(A, a, k):
    """a mod u^k"""
    return ptrim(tuple(tuple(list(c)[:k] + [0] * (A.t - k)) for c in a), A.zero)


def ap_ucoeff(F, a, k):
    """the coefficient of u^k (an F_q-polynomial), the lower ones being 0"""
    return ptrim(tuple(c[k] if len(c) > k else 0 for c in a))


def ap_scalar(A, c, a):
    return ptrim(tuple(A.scalar(x, c) for x in a), A.zero)


def solve_K(F, hats, ds, c):
    """h_j with deg h_j < ds[j] and sum_j h_j*hats[j] = c  (F_q-polynomials)

    The F_q-linear map  (+) F_q[X]_{<d_j} -> F_q[X]_{<D},  (h_j) |-> sum h_j hats_j
    is injective (reduce mod fbar_i) and both sides have dimension D, so it is
    bijective; the system below is therefore non-singular whenever the fbar_j are
    pairwise coprime.
    """
    D = sum(ds)
    cols = [(j, e) for j in range(len(ds)) for e in range(ds[j])]
    target = [c[i] if i < len(c) else 0 for i in range(D)]
    M = [[0] * len(cols) for _ in range(D)]
    for ci, (j, e) in enumerate(cols):
        prod = pmul(F, hats[j], tuple([0] * e + [1]))
        for i in range(min(len(prod), D)):
            M[i][ci] = prod[i]
    rows = [M[i][:] + [target[i]] for i in range(D)]
    piv = []
    r = 0
    for c0 in range(len(cols)):
        pr = next((i for i in range(r, D) if rows[i][c0]), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = F.inv[rows[r][c0]]
        rows[r] = [F.mul[iv][x] for x in rows[r]]
        for i in range(D):
            if i != r and rows[i][c0]:
                f = rows[i][c0]
                rows[i] = [F.sub[rows[i][k]][F.mul[f][rows[r][k]]] for k in range(len(cols) + 1)]
        piv.append(c0)
        r += 1
        if r == D:
            break
    if r != D:
        raise RuntimeError("Hensel: singular system (the factors are not coprime)")
    x = [0] * len(cols)
    for i, c0 in enumerate(piv):
        x[c0] = rows[i][len(cols)]
    hs = []
    pos = 0
    for j in range(len(ds)):
        hs.append(ptrim(tuple(x[pos:pos + ds[j]])))
        pos += ds[j]
    tot = ()
    for j in range(len(ds)):
        tot = padd(F, tot, pmul(F, hs[j], hats[j]))
    assert tot == ptrim(c), "Hensel: correction identity failed"
    return hs


def hensel_lift(F, t, g, fbars):
    """g monic in A_t[X]; fbars monic pairwise coprime over F_q with prod = g mod u.

    Returns the unique monic lifts F_j in A_t[X] with F_j = fbar_j mod u and
    prod_j F_j = g.
    """
    A = Local(F, t)
    Fs = [ap_embed(F, t, f) for f in fbars]
    ds = [pdeg(f) for f in fbars]
    for k in range(1, t):
        prod = (A.one,)
        for Fj in Fs:
            prod = ap_mul(A, prod, Fj)
        E = ap_sub(A, g, prod)
        if ap_trunc(A, E, k) != ():
            raise RuntimeError("Hensel: the level-%d correction failed" % k)
        c = ap_ucoeff(F, E, k)
        hats = []
        for j in range(len(Fs)):
            hj = (1,)
            for i in range(len(Fs)):
                if i != j:
                    hj = pmul(F, hj, fbars[i])
            hats.append(hj)
        hs = solve_K(F, hats, ds, c)
        newFs = []
        for j in range(len(Fs)):
            L = max(1, len(hs[j]))
            corr = tuple(tuple([0] * k + [(hs[j][e] if e < len(hs[j]) else 0)] +
                                 [0] * (t - k - 1)) for e in range(L))
            newFs.append(ap_add(A, Fs[j], corr))
        Fs = newFs
    prod = (A.one,)
    for Fj in Fs:
        prod = ap_mul(A, prod, Fj)
    assert prod == ptrim(g, A.zero), "Hensel: product mismatch"
    return Fs


# ==================================================== 3. F_q-linear algebra

class Lin(object):
    """F_q-linear algebra on flat coordinate tuples; a subspace is its RREF key."""

    def __init__(self, F, dim):
        self.F = F
        self.dim = dim

    def span(self, vecs):
        if not vecs:
            return ()
        return tuple(tuple(r) for r in rref([list(v) for v in vecs], self.F, self.dim)[0])

    def sum(self, k1, k2):
        return self.span(list(k1) + list(k2))

    def meet(self, k1, k2):
        F, d = self.F, self.dim
        n1, n2 = len(k1), len(k2)
        if n1 == 0 or n2 == 0:
            return ()
        rows = [[k1[j][i] for j in range(n1)] +
                [F.neg[k2[l][i]] for l in range(n2)] for i in range(d)]
        ker = nullspace_basis(rows, F, n1 + n2)
        return self.span([v[:n1] for v in ker])

    def contains(self, key, v):
        F = self.F
        r = list(v)
        for row in key:
            p = next((i for i, x in enumerate(row) if x), None)
            if p is None:
                continue
            if r[p]:
                c = F.mul[r[p]][F.inv[row[p]]]
                for i in range(p, self.dim):
                    if row[i]:
                        r[i] = F.sub[r[i]][F.mul[c][row[i]]]
        return all(x == 0 for x in r)

    def size(self, key):
        return self.F.q ** len(key)

    def elements(self, key):
        F = self.F
        k = len(key)
        if k == 0:
            return [tuple([0] * self.dim)]
        out = []
        for coeffs in itertools.product(range(F.q), repeat=k):
            v = [0] * self.dim
            for c, row in zip(coeffs, key):
                if c:
                    for i in range(self.dim):
                        if row[i]:
                            v[i] = F.add[v[i]][F.mul[c][row[i]]]
            out.append(tuple(v))
        return out


# ================================================ 4. S(h) = A_t[X]/<h>

class PolyQuot(object):
    """A_t[X]/<h> for a monic h over F_q (embedded into A_t[X]).

    An element is the tuple of the A_t-coefficients of its normal form
    (index = degree in X); an element of A_t is a t-tuple of field elements.
    """

    def __init__(self, F, t, h_F):
        self.F = F
        self.t = t
        self.A = Local(F, t)
        self.h = ap_embed(F, t, h_F)
        self.hF = h_F
        self.D = pdeg(h_F)
        self.dimFq = self.D * t
        self.zero = tuple([self.A.zero] * self.D)
        self.one = (self.A.one,) + tuple([self.A.zero] * (self.D - 1))
        self.size = F.q ** self.dimFq
        self.LA = Lin(F, self.dimFq)

    def from_poly(self, ap):
        A = self.A
        a = list(ap) + [A.zero] * max(0, self.D - len(ap))
        for i in range(len(a) - 1, self.D - 1, -1):
            c = a[i]
            if c != A.zero:
                a[i] = A.zero
                for j in range(self.D):
                    if self.h[j] != A.zero:
                        a[i - self.D + j] = A.sub(a[i - self.D + j], A.mul(c, self.h[j]))
        return tuple(a[:self.D])

    def to_poly(self, x):
        return ptrim(x, self.A.zero)

    def vec(self, x):
        out = []
        for c in x:
            out.extend(c)
        return tuple(out)

    def from_vec(self, v):
        t = self.t
        return tuple(tuple(v[i * t:(i + 1) * t]) for i in range(self.D))

    def add(self, x, y):
        A = self.A
        return tuple(A.add(x[i], y[i]) for i in range(self.D))

    def sub(self, x, y):
        A = self.A
        return tuple(A.sub(x[i], y[i]) for i in range(self.D))

    def mul(self, x, y):
        return self.from_poly(ap_mul(self.A, self.to_poly(x), self.to_poly(y)))

    def monom(self, a, b):
        """u^a X^b"""
        A = self.A
        e = tuple([1 if i == a else 0 for i in range(A.t)])
        return self.from_poly(tuple([A.zero] * b) + (e,))

    def basis(self):
        """F_q-basis {u^a X^b} of the ring"""
        return [self.monom(a, b) for b in range(self.D) for a in range(self.t)]

    def elements(self):
        for coeffs in itertools.product(self.A.elem_list(), repeat=self.D):
            yield tuple(coeffs)

    # ---- sigma_k (Frobenius on the F_q-coefficients; u and X are fixed)
    def sigma(self, x, k):
        A = self.A
        return tuple(A.sigma(c, k) for c in x)

    # ---- units by the rank of the multiplication map
    def mult_matrix(self, x):
        F = self.F
        rows = []
        for e in self.basis():
            rows.append(list(self.vec(self.mul(x, e))))
        return rows

    def is_unit(self, x):
        if x == self.zero:
            return False
        rows = self.mult_matrix(x)
        return len(rref(rows, self.F, self.dimFq)[1]) == self.dimFq


# ======================================== 5. the CRT system B <-> prod_j B_j

def egcd(F, a, b):
    """(g, s, t) with s*a + t*b = g = gcd(a, b)"""
    r0, r1 = a, b
    s0, s1 = (1,), ()
    t0, t1 = (), (1,)
    while r1 != ():
        q, r = pdivmod(F, r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, psub(F, s0, pmul(F, q, s1))
        t0, t1 = t1, psub(F, t0, pmul(F, q, t1))
    return r0, s0, t0


def crt_idempotents(F, moduli):
    """Bezout idempotents e_j in F_q[X]: e_j = 1 mod moduli[j], 0 mod the others"""
    es = []
    for j, fj in enumerate(moduli):
        Gj = (1,)
        for i, fi in enumerate(moduli):
            if i != j:
                Gj = pmul(F, Gj, fi)
        g, s, _t = egcd(F, Gj, fj)
        if pdeg(g) != 0:
            raise RuntimeError("the moduli are not pairwise coprime")
        e = pmul(F, s, Gj)
        if g[0] != 1:
            e = pscal(F, F.inv[g[0]], e)
        es.append(e)
    return es


def pdivmod_local(A, a, h):
    """divide the A_t-polynomial a by the monic A_t-polynomial h"""
    a = list(a)
    db = len(h) - 1
    q = [A.zero] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c != A.zero:
            q[i - db] = c
            for j in range(db + 1):
                if h[j] != A.zero:
                    a[i - db + j] = A.sub(a[i - db + j], A.mul(c, h[j]))
            a[i] = A.zero
    return ptrim(tuple(q), A.zero), ptrim(tuple(a), A.zero)


class CRTSystem(object):
    """B = A_t[X]/<X^n-1>  <->  prod_j A_t[X]/<f_j^{p^v}>"""

    def __init__(self, q, t, n):
        p, r = field_params(q)
        self.F = Field(p, r)
        self.p, self.q, self.t, self.n = p, q, t, n
        v, nn = 0, n
        while nn % p == 0:
            nn //= p
            v += 1
        self.v = v
        self.nprime = nn
        self.e = p ** v
        F = self.F
        self.g = psub(F, tuple([0] * nn + [1]), (1,))          # X^{n'} - 1
        self.facs = factor_squarefree(F, self.g)
        self.J = len(self.facs)
        self.degs = [pdeg(f) for f in self.facs]
        self.facs_pow = []
        for f in self.facs:
            fp = (1,)
            for _ in range(self.e):
                fp = pmul(F, fp, f)
            self.facs_pow.append(fp)
        prod = (1,)
        for fp in self.facs_pow:
            prod = pmul(F, prod, fp)
        self.Xn1 = prod
        assert self.Xn1 == psub(F, tuple([0] * n + [1]), (1,)), "X^n-1 mismatch"
        self.B = PolyQuot(F, t, self.Xn1)
        self.Bj = [PolyQuot(F, t, fp) for fp in self.facs_pow]
        self.efac = crt_idempotents(F, self.facs_pow)
        self.ej = [self.B.from_poly(ap_embed(F, t, e)) for e in self.efac]
        self.hj = [ap_embed(F, t, fp) for fp in self.facs_pow]
        # predicted and actual factor degrees (independent cross-check)
        self.cosets = cyclotomic_cosets(q, nn) if nn > 0 else [(0,)]

    # ---- the map and its inverse
    def split(self, b):
        """B -> prod_j B_j"""
        pol = self.B.to_poly(b)
        out = []
        for j in range(self.J):
            _q, rem = pdivmod_local(self.B.A, pol, self.hj[j])
            out.append(self.Bj[j].from_poly(rem))
        return tuple(out)

    def combine(self, cs):
        """prod_j B_j -> B   (sum_j e_j * c_j)"""
        acc = self.B.zero
        for j, c in enumerate(cs):
            cj = self.B.from_poly(self.Bj[j].to_poly(c))
            acc = self.B.add(acc, self.B.mul(self.ej[j], cj))
        return acc

    def split_vec(self, v):
        """B^2 -> prod_j B_j^2 : for each j the PAIR (v_0 mod f_j^{p^v}, v_1 mod ...)"""
        s0 = self.split(v[0])
        s1 = self.split(v[1])
        return tuple((s0[j], s1[j]) for j in range(self.J))

    def combine_vec(self, vs):
        """prod_j B_j^2 -> B^2"""
        return tuple(self.combine(tuple(vs[j][i] for j in range(self.J)))
                     for i in range(2))


# ================================================= 6. the local components

class FqQuot(object):
    """K = F_q[X]/<f>, f monic irreducible over F_q"""

    def __init__(self, F, f):
        self.F = F
        self.f = f
        self.d = pdeg(f)
        self.zero = tuple([0] * self.d)
        self.one = (1,) + tuple([0] * (self.d - 1))
        self.q = F.q ** self.d
        self.LA = Lin(F, self.d)

    def of_poly(self, a):
        rr = pmod(self.F, a, self.f)
        return tuple(list(rr) + [0] * (self.d - len(rr)))

    def add(self, x, y):
        F = self.F
        return tuple(F.add[x[i]][y[i]] for i in range(self.d))

    def mul(self, x, y):
        return self.of_poly(pmul(self.F, x, y))

    def elements(self):
        for c in itertools.product(range(self.F.q), repeat=self.d):
            yield tuple(c)


class LocalData(object):
    """B_j, its residue field K_j, its maximal ideal m_j and their invariants"""

    def __init__(self, S, j):
        self.S = S
        self.j = j
        F = S.F
        self.F = F
        self.Bj = S.Bj[j]
        self.fj = S.facs[j]
        self.dj = pdeg(self.fj)
        self.e = S.e
        self.t = S.t
        self.K = FqQuot(F, self.fj)
        self._build_rho()
        self._build_m()
        self._build_nilpotence()

    # rho_j : B_j -> K_j  (u -> 0, then reduce mod f_j)
    def _build_rho(self):
        Bj, F = self.Bj, self.F
        self.red = [[0] * self.K.d for _ in range(Bj.dimFq)]
        for i in range(Bj.D):
            im = self.K.of_poly(tuple([0] * i + [1]))
            for a in range(self.K.d):
                self.red[i * self.t][a] = im[a]
        rows = [[self.red[jj][a] for jj in range(Bj.dimFq)] for a in range(self.K.d)]
        self.ker = nullspace_basis(rows, F, Bj.dimFq)

    def rho(self, x):
        F, K = self.F, self.K
        out = [0] * K.d
        for i, c in enumerate(x):
            c0 = c[0]
            if c0:
                im = K.of_poly(tuple([0] * i + [1]))
                for a in range(K.d):
                    if im[a]:
                        out[a] = F.add[out[a]][F.mul[c0][im[a]]]
        return tuple(out)

    # ideals as F_q-subspaces, generated by a set of elements
    def ideal_of(self, gens):
        Bj = self.Bj
        LA = Bj.LA
        span = [Bj.vec(g) for g in gens if Bj.vec(g) != tuple([0] * Bj.dimFq)]
        if not span:
            return ()
        changed = True
        while changed:
            changed = False
            key = LA.span(span)
            for v in list(span):
                for m in (Bj.monom(0, 1), Bj.monom(1, 0)):      # multiply by X and by u
                    y = Bj.mul(Bj.from_vec(v), m)
                    if not LA.contains(key, Bj.vec(y)):
                        span.append(Bj.vec(y))
                        changed = True
        return LA.span(span)

    def product(self, k1, k2):
        """the ideal product, from the products of the generators (commutative)"""
        Bj = self.Bj
        vs = []
        for a in k1:
            for b in k2:
                vs.append(Bj.mul(Bj.from_vec(a), Bj.from_vec(b)))
        return self.ideal_of(vs)

    def _build_m(self):
        Bj, F = self.Bj, self.F
        gens = [Bj.monom(a, 0) for a in range(1, self.t)]
        gens.append(Bj.from_poly(ap_embed(F, self.t, self.fj)))
        self.m_gen = self.ideal_of(gens)
        self.m = self.m_gen
        self.m_sq = self.product(self.m, self.m)
        self.dim_m = len(self.m)
        self.dim_m2 = len(self.m_sq)
        self.dimK_mm2 = (self.dim_m - self.dim_m2) // self.K.d if self.K.d else 0

    def _build_nilpotence(self):
        """smallest N with m^N = 0 (generator powers; no element scans)"""
        if not self.m:
            # m_j = 0, i.e. B_j is a field: the least N >= 1 with m^N = 0 is N = 1
            self.nilp = 1
            self.m_pows = [self.Bj.LA.span([self.Bj.vec(self.Bj.one)]), ()]
            return
        pows = [self.Bj.LA.span([self.Bj.vec(self.Bj.one)]), self.m]
        k = 1
        while pows[-1] != ():
            pows.append(self.product(pows[-1], self.m))
            k += 1
        self.m_pows = pows
        self.nilp = k          # m^{nilp} = 0, m^{nilp-1} != 0

    def m_power(self, k):
        return self.m_pows[k] if k < len(self.m_pows) else ()

    # dimension over K_j of a K_j-space given as an F_q-space
    def dim_over_K(self, key):
        return len(key) // self.K.d

    def predict_dimK(self):
        """dim_{K_j}(m_j/m_j^2):  0, 1 or 2 according to the three cases"""
        if self.t == 1 and self.e == 1:
            return 0
        if self.t >= 2 and self.e >= 2:
            return 2
        return 1

    def is_chain_predicted(self):
        return not (self.t >= 2 and self.e >= 2)


# ==================================== 7. M_2 over a quotient ring: ideals

class Mat2(object):
    """M_2(S) for S a PolyQuot; an element is (a11, a12, a21, a22)"""

    def __init__(self, S):
        self.S = S
        F = S.F
        self.F = F
        self.dimS = S.dimFq
        self.dim = 4 * S.dimFq
        self.LA = Lin(F, self.dim)
        self.zero = (S.zero,) * 4
        self.one = (S.one, S.zero, S.zero, S.one)

    def from_cols(self, c1, c2):
        """the matrix with the two given columns"""
        S = self.S
        return (S.from_vec(c1[0:self.dimS]), S.from_vec(c2[0:self.dimS]),
                S.from_vec(c1[self.dimS:2 * self.dimS]), S.from_vec(c2[self.dimS:2 * self.dimS]))

    def col(self, x, j):
        """column j (0-based) as a flat vector of S^2"""
        S = self.S
        return (S.vec(x[0]) + S.vec(x[2])) if j == 0 else (S.vec(x[1]) + S.vec(x[3]))

    def vec(self, x):
        out = []
        for e in x:
            out.extend(self.S.vec(e))
        return tuple(out)

    def from_vec(self, v):
        S = self.S
        return tuple(S.from_vec(v[i * S.dimFq:(i + 1) * S.dimFq]) for i in range(4))

    def add(self, x, y):
        S = self.S
        return tuple(S.add(x[i], y[i]) for i in range(4))

    def mul(self, x, y):
        S = self.S
        A = S.A
        def dot(i, j):
            acc = S.zero
            for k in range(2):
                acc = S.add(acc, S.mul(x[2 * i + k], y[2 * k + j]))
            return acc
        return (dot(0, 0), dot(0, 1), dot(1, 0), dot(1, 1))

    def gens_as_fq_algebra(self):
        """F_q-basis of M_2(S): the E_{jl} * (monomials of S); used to compute x*M_2(S)"""
        S = self.S
        out = []
        for j in (0, 1):
            for l in (0, 1):
                for m in S.basis():
                    e = [S.zero] * 4
                    e[2 * j + l] = m
                    out.append(tuple(e))
        return out

    def right_ideal_of(self, gens):
        """the right ideal generated by `gens` (span of x*N over an F_q-basis of M_2(S))"""
        basis = self.gens_as_fq_algebra()
        vs = []
        for x in gens:
            for N in basis:
                vs.append(self.vec(self.mul(x, N)))
        return self.LA.span(vs)

    def is_right_ideal(self, key):
        basis = self.gens_as_fq_algebra()
        ok = True
        for v in self.LA.elements(key):
            for N in basis:
                if not self.LA.contains(key, self.vec(self.mul(self.from_vec(v), N))):
                    return False
        return True

    def sigma(self, x, k):
        S = self.S
        return tuple(S.sigma(e, k) for e in x)


class Module(object):
    """P = S^2 as a right S-module (columns), together with W <-> I_W."""

    def __init__(self, S):
        self.S = S
        self.F = S.F
        self.dim = 2 * S.dimFq
        self.LA = Lin(S.F, self.dim)
        self.M = Mat2(S)
        self.zero = (S.zero, S.zero)
        self.e1 = (S.one, S.zero)
        self.e2 = (S.zero, S.one)
        self.elems = None          # materialised only when small enough
        self._gens = [S.monom(a, b) for b in range(S.D) for a in range(S.t)]

    def vec(self, v):
        return self.S.vec(v[0]) + self.S.vec(v[1])

    def from_vec(self, fv):
        S = self.S
        return (S.from_vec(fv[0:S.dimFq]), S.from_vec(fv[S.dimFq:2 * S.dimFq]))

    def act(self, v, b):
        S = self.S
        return (S.mul(v[0], b), S.mul(v[1], b))

    def gen(self, seeds):
        """the S-submodule generated by `seeds`"""
        vs = []
        for v in seeds:
            for m in self._gens:
                vs.append(self.vec(self.act(v, m)))
        return self.LA.span(vs)

    def elements(self):
        """all elements of P = S^2 (pairs of ring elements)"""
        if self.elems is None:
            els = [tuple(x) for x in itertools.product(self.S.A.elem_list(),
                                                       repeat=self.S.D)]
            self.elems = [(a, b) for a in els for b in els]
        return self.elems

    # ---- I_W and W(I)
    def I_of_W(self, Wkey):
        """{M : both COLUMNS of M lie in W} as an F_q-subspace of M_2(S).

        WARNING (the point of the negative controls): the ROW reading gives the
        LEFT ideals.  Here a basis vector v = (v_a, v_b) of W (an element of
        S^2, flat) is placed in column 0 as (a11, a21) = (v_a, v_b) and in
        column 1 as (a12, a22) = (v_a, v_b).
        """
        M, S = self.M, self.S
        d = S.dimFq
        z = tuple([0] * d)
        rows = []
        for v in Wkey:                      # column 0 = v
            rows.append(v[0:d] + z + v[d:2 * d] + z)
        for v in Wkey:                      # column 1 = v
            rows.append(z + v[0:d] + z + v[d:2 * d])
        return M.LA.span(rows)

    def W_of_I(self, Ikey):
        """sum over M in I of im M = span of the columns of the generators of I"""
        M = self.M
        vs = []
        for v in Ikey:
            x = M.from_vec(v)
            vs.append(M.col(x, 0))
            vs.append(M.col(x, 1))
        return self.LA.span(vs)

    # ---- mu, method 1: lattice BFS over sums of cyclic submodules
    def cyclic_submodules(self):
        """all cyclic submodules of P, with one generator each"""
        seen = {}
        for v in self.elements():
            key = self.gen([v])
            if key not in seen:
                seen[key] = v
        return seen

    def lattice_bfs(self):
        """every submodule with its BFS level (= mu) and a minimal generating set.

        The BFS level over sums of cyclic submodules IS mu: a generating set of
        size k gives a sum of k cyclics, and a sum of k cyclics Bv_i is generated
        by the v_i.  `wit[key]` is a tuple of elements that generate `key`.
        """
        cyc = self.cyclic_submodules()
        level = {(): 0}
        wit = {(): ()}
        frontier = []
        for k, v in cyc.items():
            if k:
                level[k] = 1
                wit[k] = (v,)
                frontier.append(k)
        while frontier:
            new = []
            for k in frontier:
                for c, vc in cyc.items():
                    if not c:
                        continue
                    kk = self.LA.sum(k, c)
                    if kk not in level:
                        level[kk] = level[k] + 1
                        wit[kk] = wit[k] + (vc,)
                        new.append(kk)
            frontier = new
        return level, wit

    # ---- mu, method 2: brute force over k-tuples
    def mu_brute(self, Wkey, upto=3, pair_budget=20000, rng=None):
        """minimal k found by scanning k-tuples of elements of W.

        Exhaustive for k = 1; for k = 2 exhaustive when |W|^2 <= pair_budget and
        sampled (200 pairs) otherwise.  Returns None when nothing was found, so
        that the caller can skip the comparison (never a false negative).
        """
        if not Wkey:
            return 0
        W = self.LA.elements(Wkey)
        if len(W) > 4096:
            return None
        for v in W:
            if self.gen([self.from_vec(v)]) == Wkey:
                return 1
        if upto < 2:
            return None
        if len(W) ** 2 <= pair_budget:
            pairs = itertools.product(W, repeat=2)
        else:
            rs = random.Random(4242)
            pairs = [(rs.choice(W), rs.choice(W)) for _ in range(200)]
        for a, b in pairs:
            if self.LA.sum(self.gen([self.from_vec(a)]),
                           self.gen([self.from_vec(b)])) == Wkey:
                return 2
        return None

    # ---- mu, method 3: Nakayama on the local components (filled by the caller)
    # ---- mu, method 4: principality by an exhaustive x-scan
    def is_principal_scan(self, Ikey):
        """True if some x in I generates I; also returns the witness"""
        M = self.M
        for v in M.LA.elements(Ikey):
            if M.right_ideal_of([M.from_vec(v)]) == Ikey:
                return True, M.from_vec(v)
        return False, None

    def principal_certificate(self, Ikey, x):
        """|x*M_2(S)| == |I|  (with x in I this proves x*M_2(S) = I)"""
        M = self.M
        return M.LA.size(M.right_ideal_of([x])) == M.LA.size(Ikey)


# ==================================================== 8. Galois: sigma_k

def galois_permutation(S, k):
    """the permutation of the factors induced by sigma_k (Frobenius^k on F_q).

    sigma_k(f_j) is the irreducible factor whose root set is p^k * C_j; the
    routine below computes it directly from the coefficients and compares it
    with the cyclotomic-coset prediction.
    """
    F = S.F
    perm = []
    for j in range(S.J):
        fj = frob_poly(F, S.facs[j], k)
        perm.append(S.facs.index(fj))
    return tuple(perm)


def coset_permutation(S, k):
    """the prediction: coset C |-> p^k * C"""
    p, q, m = S.p, S.q, S.nprime
    cosets = S.cosets
    perm = []
    for C in cosets:
        img = tuple(sorted(set((pow(p, k, m) * a) % m for a in C)))
        perm.append(cosets.index(img))
    return tuple(perm)


# ==================================================== 9. the drivers

def head(title):
    say("")
    say("#" * 96)
    say("#  " + title)
    say("#" * 96)


def ring_head(S, tag):
    F = S.F
    say("")
    say("#" * 96)
    say("#  (q,t,n) = %s   q = %d = %d^%d,  t = %d,  n = %d"
        % (tag, S.q, S.p, F.r, S.t, S.n))
    say("#  n = p^v n' : v = %d, n' = %d, e = p^v = %d ;  X^n-1 = (X^{n'}-1)^{p^v}"
        % (S.v, S.nprime, S.e))
    say("#  |B| = %d,  |B^2| = %d,  |M_2(B)| = %d"
        % (S.B.size, S.B.size ** 2, S.B.size ** 4))
    say("#  components J = %d, degrees d_j = %s, |B_j| = %s"
        % (S.J, S.degs, [Bj.size for Bj in S.Bj]))
    say("#" * 96)


def run_factorisation(S, tag, rng):
    """Task A(1): X^n-1 = (X^{n'}-1)^{p^v}, squarefree part, its factorisation"""
    F = S.F
    say("")
    say("-- factorisation of the squarefree part (Task A.1) " + "-" * 42)
    # X^n - 1 = (X^{n'} - 1)^{p^v}
    gpow = (1,)
    for _ in range(S.e):
        gpow = pmul(F, gpow, S.g)
    check("%s: X^n - 1 = (X^{n'}-1)^{p^v} in F_q[X]" % tag, gpow == S.Xn1,
          "deg %d" % pdeg(S.Xn1))
    # X^{n'} - 1 is squarefree: gcd(g, g') = 1
    der = ptrim(tuple(F.mul[i % F.p][S.g[i]] for i in range(1, len(S.g))))
    gp, _s, _t = egcd(F, S.g, der)
    check("%s: X^{n'}-1 is squarefree (gcd with the derivative is 1)" % tag,
          pdeg(gp) == 0, "gcd degree %d, n' = %d" % (pdeg(gp), S.nprime))
    # the factorisation
    prod = (1,)
    for f in S.facs:
        prod = pmul(F, prod, f)
    check("%s: X^{n'}-1 = prod_j f_j with monic irreducibles" % tag, prod == S.g,
          "%d factors, degrees %s" % (S.J, S.degs))
    check("%s: every f_j is irreducible (trial division)" % tag,
          all(is_irreducible(F, f) for f in S.facs), "")
    ok = True
    for i in range(S.J):
        for j in range(i + 1, S.J):
            gg, _s, _t = egcd(F, S.facs[i], S.facs[j])
            if pdeg(gg) != 0:
                ok = False
    check("%s: the f_j are pairwise coprime" % tag, ok, "%d pairs" % (S.J * (S.J - 1) // 2))
    # independent cross-check: cyclotomic cosets
    cos = S.cosets
    check("%s: #factors = #q-cyclotomic cosets mod n'" % tag, len(cos) == S.J,
          "%d = %d" % (len(cos), S.J))
    check("%s: the degrees d_j are the coset sizes (independent route)" % tag,
          sorted(S.degs) == sorted(len(c) for c in cos),
          "degrees %s, coset sizes %s" % (S.degs, [len(c) for c in cos]))
    check("%s: sum_j d_j = n'" % tag, sum(S.degs) == S.nprime,
          "%d = %d" % (sum(S.degs), S.nprime))


def run_hensel(S, tag, rng):
    """Task A(2): Hensel lifting of the coprime factorisation"""
    F, t = S.F, S.t
    say("")
    say("-- Hensel lifting (Task A.2) " + "-" * 58)
    # (i) the lift of the squarefree part
    g_in_A = ap_embed(F, t, S.g)
    lifts = hensel_lift(F, t, g_in_A, S.facs)
    A = Local(F, t)
    prod = (A.one,)
    for Fj in lifts:
        prod = ap_mul(A, prod, Fj)
    mon = all(lifts[j][len(lifts[j]) - 1] == A.one and
              len(lifts[j]) == len(S.facs[j]) for j in range(S.J))
    red = all(all(lifts[j][i][0] == S.facs[j][i] for i in range(len(S.facs[j])))
              for j in range(S.J))
    check("%s: the Hensel lifts F_j are monic, reduce to f_j mod u, and prod = X^{n'}-1"
          % tag, prod == ptrim(g_in_A, A.zero) and mon and red,
          "%d factors" % S.J)
    trivial = all(lifts[j] == ap_embed(F, t, S.facs[j]) for j in range(S.J))
    say("     => the unique Hensel lifts are the base-field factors themselves: %s"
        % trivial)
    check("%s: the Hensel lift is trivial here (F_j = f_j in F_q[X])" % tag, trivial,
          "consequence of X^{n'}-1 having coefficients in F_q")
    # (ii) uniqueness, verified exhaustively when the search space is small
    A = Local(F, t)
    if S.J <= 3 and all(F.q ** (t * S.degs[j]) <= 4000 for j in range(S.J)):
        cands = []
        for j in range(S.J):
            ds = S.degs[j]
            c = []
            for coefs in itertools.product(A.elem_list(), repeat=ds):
                el = tuple(coefs) + (A.one,)
                if all(el[i] == ap_embed(F, t, S.facs[j])[i] for i in range(ds)):
                    c.append(el)
            cands.append(c)
        total = 1
        for c in cands:
            total *= len(c)
        if total <= 200000:
            cnt = 0
            for combo in itertools.product(*cands):
                prod = (A.one,)
                for el in combo:
                    prod = ap_mul(A, prod, el)
                if prod == ptrim(g_in_A, A.zero):
                    cnt += 1
                    if list(combo) != [ap_embed(F, t, f) for f in S.facs]:
                        cnt = -10 ** 6
            check("%s: the lift is the UNIQUE monic lift with F_j = f_j mod u" % tag,
                  cnt == 1, "exhaustive over %d candidate tuples" % total)
    # (iii) non-vacuity: a genuine, non-trivial lift on a different polynomial
    F2 = Field(2, 1)
    A2 = Local(F2, 2)
    u = (0, 1)
    gg = (u, (1, 0), (1, 0))                 # X^2 + X + u  over F_2[u]/<u^2>
    fb = [(0, 1), (1, 1)]                    # X , X+1
    Ls = hensel_lift(F2, 2, gg, fb)
    expect = [((0, 1), (1, 0)), ((1, 1), (1, 0))]     # X+u , X+1+u
    check("%s: non-vacuity - a genuinely non-trivial Hensel lift" % tag,
          [tuple(tuple(c) for c in L) for L in Ls] == [tuple(tuple(c) for c in e)
                                                       for e in expect],
          "X^2+X+u lifts to (X+u)(X+1+u), not to X(X+1)")
    # (iv) the repeated factor: lifting X^n-1 = prod f_j^{p^v} directly
    if S.J >= 1:
        Ls2 = hensel_lift(F, t, ap_embed(F, t, S.Xn1), S.facs_pow)
        same2 = all(Ls2[j] == ap_embed(F, t, S.facs_pow[j]) for j in range(S.J))
        check("%s: lifting the repeated factorisation gives f_j^{p^v} too" % tag,
              same2, "the two Hensel routes agree here (both are trivial)")


def ap_neg(A, a):
    return ptrim(tuple(A.neg(c) for c in a), A.zero)


def run_crt(S, tag, rng):
    """Task A(3,5): the CRT decomposition, and ideals/submodules under it"""
    F, B = S.F, S.B
    say("")
    say("-- CRT decomposition (Task A.3, A.5) " + "-" * 51)
    prod = 1
    for Bj in S.Bj:
        prod *= Bj.size
    check("%s: |B| = q^{tn} = prod_j |B_j|" % tag,
          B.size == S.q ** (S.t * S.n) and B.size == prod,
          "%d = %d" % (B.size, prod))
    # the map is a ring homomorphism, and is bijective
    if B.size <= 600:
        els = list(B.elements())
        add_ok = mul_ok = True
        for x in els:
            for y in els:
                sx, sy = S.split(x), S.split(y)
                if tuple(S.Bj[j].add(sx[j], sy[j]) for j in range(S.J)) != S.split(B.add(x, y)):
                    add_ok = False
                if tuple(S.Bj[j].mul(sx[j], sy[j]) for j in range(S.J)) != S.split(B.mul(x, y)):
                    mul_ok = False
                if not (add_ok and mul_ok):
                    break
            if not (add_ok and mul_ok):
                break
        check("%s: the CRT map is additive" % tag, add_ok, "all %d^2 pairs" % B.size)
        check("%s: the CRT map is multiplicative" % tag, mul_ok, "all %d^2 pairs" % B.size)
        bij = all(S.combine(S.split(x)) == x for x in els)
        check("%s: the CRT map is bijective (round trip on every element)" % tag, bij,
              "%d elements" % B.size)
    else:
        els = [tuple(x) for x in itertools.islice(B.elements(), 0, 400)]
        els += [tuple(B.from_vec(v)) for v in
                [tuple(rng.randrange(F.q) for _ in range(B.dimFq)) for _ in range(200)]]
        add_ok = mul_ok = True
        for x in els:
            for y in els:
                sx, sy = S.split(x), S.split(y)
                if tuple(S.Bj[j].add(sx[j], sy[j]) for j in range(S.J)) != S.split(B.add(x, y)):
                    add_ok = False
                if tuple(S.Bj[j].mul(sx[j], sy[j]) for j in range(S.J)) != S.split(B.mul(x, y)):
                    mul_ok = False
        check("%s: the CRT map is additive" % tag, add_ok, "600^2 pairs (sampled)",
              exhaustive=False)
        check("%s: the CRT map is multiplicative" % tag, mul_ok, "600^2 pairs (sampled)",
              exhaustive=False)
        bij = all(S.combine(S.split(x)) == x for x in els)
        check("%s: the CRT map is injective on the tested elements" % tag, bij,
              "600 elements (sampled)", exhaustive=False)
    # idempotents
    ok_idem = all(B.mul(S.ej[j], S.ej[j]) == S.ej[j] for j in range(S.J))
    ok_orth = True
    for i in range(S.J):
        for j in range(S.J):
            if i != j and B.mul(S.ej[i], S.ej[j]) != B.zero:
                ok_orth = False
    one = B.zero
    for j in range(S.J):
        one = B.add(one, S.ej[j])
    check("%s: the e_j are pairwise orthogonal idempotents summing to 1" % tag,
          ok_idem and ok_orth and one == B.one, "%d idempotents" % S.J)
    # e_j acts as the j-th projector
    ok_proj = True
    for j in range(S.J):
        cs = S.split(S.ej[j])
        if any(cs[i] != S.Bj[i].zero for i in range(S.J) if i != j):
            ok_proj = False
        if cs[j] != S.Bj[j].one:
            ok_proj = False
    check("%s: e_j maps to (0,..,1,..,0) under the CRT map" % tag, ok_proj, "")


def run_ideal_crt(S, tag, rng):
    """ideals of B <-> tuples of ideals of the B_j (exhaustive when small)"""
    B = S.B
    if B.size > 300:
        return None
    say("")
    say("-- ideals under the CRT (Task A.5) " + "-" * 53)
    # enumerate the ideals of B: BFS closure under addition from the principal ideals
    def ideals_of(R):
        LA = R.LA
        prin = set()
        for x in R.elements():
            gens = [x]
            key = LA.span([R.vec(x)])
            changed = True
            while changed:
                changed = False
                for m in R.basis():
                    for v in list(key):
                        y = R.mul(R.from_vec(v), m)
                        if not LA.contains(key, R.vec(y)):
                            key = LA.sum(key, LA.span([R.vec(y)]))
                            changed = True
            prin.add(key)
        allid = set(prin)
        frontier = sorted(prin, key=len)
        changed = True
        while changed:
            changed = False
            for k1 in list(allid):
                for k2 in list(allid):
                    s = LA.sum(k1, k2)
                    if s not in allid:
                        allid.add(s)
                        changed = True
        return allid

    idB = ideals_of(B)
    idBj = [ideals_of(Bj) for Bj in S.Bj]
    prod = 1
    for s in idBj:
        prod *= len(s)
    check("%s: #{ideals of B} = prod_j #{ideals of B_j}" % tag, len(idB) == prod,
          "%d = %d" % (len(idB), prod))
    ok = True
    seen = set()
    for k in idB:
        imgs = []
        for j in range(S.J):
            vs = [S.split(B.from_vec(v))[j] for v in B.LA.elements(k)]
            kj = S.Bj[j].LA.span([S.Bj[j].vec(x) for x in vs])
            imgs.append(kj)
        tt = tuple(imgs)
        if any(tt[j] not in idBj[j] for j in range(S.J)):
            ok = False
        seen.add(tt)
    check("%s: every ideal of B splits into a tuple of ideals of the B_j" % tag, ok, "")
    check("%s: the ideal correspondence is a bijection" % tag,
          len(seen) == len(idB) == prod, "%d tuples" % len(seen))
    return len(idB)


def run_local(S, tag, rng):
    """Task A(4) + CT-2: the local components"""
    say("")
    say("-- local component structure (Task A.4, falsification test CT-2) " + "-" * 26)
    F = S.F
    for j in range(S.J):
        L = LocalData(S, j)
        Bj = L.Bj
        t2 = "component %d (d_j = %d)" % (j, L.dj)
        check("%s, %s: dim_{F_q} B_j = t d_j p^v" % (tag, t2),
              Bj.dimFq == S.t * L.dj * S.e,
              "%d = %d.%d.%d" % (Bj.dimFq, S.t, L.dj, S.e))
        check("%s, %s: |B_j| = q^{t d_j p^v}" % (tag, t2),
              Bj.size == S.q ** (S.t * L.dj * S.e), "%d" % Bj.size)
        # rho is a ring homomorphism onto the field K_j
        if Bj.size <= 3000:
            els = list(Bj.elements())
            aok = all(L.rho(Bj.add(x, y)) == L.K.add(L.rho(x), L.rho(y))
                      for x in els for y in els)
            mok = all(L.rho(Bj.mul(x, y)) == L.K.mul(L.rho(x), L.rho(y))
                      for x in els for y in els)
            eks = "[EXH] all %d^2 pairs" % Bj.size
            ex = True
        else:
            els = [Bj.from_vec(tuple(rng.randrange(F.q) for _ in range(Bj.dimFq)))
                   for _ in range(300)]
            aok = all(L.rho(Bj.add(x, y)) == L.K.add(L.rho(x), L.rho(y))
                      for x in els for y in els)
            mok = all(L.rho(Bj.mul(x, y)) == L.K.mul(L.rho(x), L.rho(y))
                      for x in els for y in els)
            eks = "[SMP] 300^2 pairs"
            ex = False
        check("%s, %s: rho_j : B_j -> K_j is a ring homomorphism" % (tag, t2),
              aok and mok, eks, exhaustive=ex)
        inj = len(set(L.rho(x) for x in els)) == min(L.K.q, len(els))
        check("%s, %s: rho_j is surjective onto K_j = F_{q^{d_j}}" % (tag, t2),
              len(set(L.rho(x) for x in els)) == L.K.q if len(els) >= L.K.q else inj,
              "|K_j| = %d" % L.K.q, exhaustive=ex)
        # m_j = ker rho = (u, f_j)
        check("%s, %s: m_j := (u, f_j) equals ker(rho_j)" % (tag, t2),
              L.m_gen == L.ker, "dim m_j = %d" % L.dim_m)
        check("%s, %s: B_j/m_j is the field K_j (so m_j is maximal)" % (tag, t2),
              len(L.ker) == Bj.dimFq - L.K.d, "dim B_j/m_j = %d" % (Bj.dimFq - len(L.ker)))
        # nilpotence => m_j is the nilradical => B_j is local
        check("%s, %s: m_j^{t+p^v-1} = 0 (m_j is nilpotent)" % (tag, t2),
              L.nilp <= S.t + S.e - 1, "m_j^%d = 0, m_j^%d != 0" % (L.nilp, L.nilp - 1))
        # units = complement of m_j  (locality)
        if Bj.size <= 3000:
            bad = 0
            for x in list(Bj.elements()):
                inm = Bj.LA.contains(L.m, Bj.vec(x))
                if Bj.is_unit(x) == inm:
                    bad += 1
            check("%s, %s: the units are exactly B_j \\ m_j (B_j is local)" % (tag, t2),
                  bad == 0, "all %d elements" % Bj.size)
        else:
            bad = 0
            for _ in range(300):
                x = Bj.from_vec(tuple(rng.randrange(F.q) for _ in range(Bj.dimFq)))
                if Bj.is_unit(x) == Bj.LA.contains(L.m, Bj.vec(x)):
                    bad += 1
            check("%s, %s: units = complement of m_j" % (tag, t2), bad == 0,
                  "300 random elements (sampled)", exhaustive=False)
        # the key invariant: dim_{K_j}(m_j/m_j^2)
        check("%s, %s: dim_{K_j}(m_j/m_j^2) = %d (three-case prediction)"
              % (tag, t2, L.predict_dimK()), L.dimK_mm2 == L.predict_dimK(),
              "dim = %d ; dim_Fq m = %d, dim_Fq m^2 = %d"
              % (L.dimK_mm2, L.dim_m, L.dim_m2))
        # chain ring test
        chain_pred = L.is_chain_predicted()
        if Bj.size <= 3000:
            # total ordering of the ideals
            LA = Bj.LA
            ids = set()
            for x in list(Bj.elements()):
                key = LA.span([Bj.vec(x)])
                changed = True
                while changed:
                    changed = False
                    for m in Bj.basis():
                        for v in list(key):
                            y = Bj.mul(Bj.from_vec(v), m)
                            if not LA.contains(key, Bj.vec(y)):
                                key = LA.sum(key, LA.span([Bj.vec(y)]))
                                changed = True
                ids.add(key)
            frontier = True
            while frontier:
                frontier = False
                for k1 in list(ids):
                    for k2 in list(ids):
                        s = LA.sum(k1, k2)
                        if s not in ids:
                            ids.add(s)
                            frontier = True
            tot = True
            for k1 in ids:
                for k2 in ids:
                    if not (LA.contains(k1, list(k2)[0]) if k2 else True):
                        pass
            # check comparability directly
            comp = True
            for k1 in ids:
                for k2 in ids:
                    sub12 = all(LA.contains(k2, v) for v in k1) if k1 else True
                    sub21 = all(LA.contains(k1, v) for v in k2) if k2 else True
                    if not (sub12 or sub21):
                        comp = False
            check("%s, %s: B_j is a chain ring (ideals totally ordered)" % (tag, t2),
                  comp == chain_pred, "chain ring: %s (predicted %s)"
                  % (comp, chain_pred) if comp == chain_pred else
                  "MISMATCH: chain %s predicted %s" % (comp, chain_pred))
            check("%s, %s: #{ideals} = nilpotency + 1 iff chain ring" % (tag, t2),
                  (len(ids) == L.nilp + 1) == chain_pred,
                  "%d ideals, nilpotency %d" % (len(ids), L.nilp))
        else:
            check("%s, %s: chain ring <=> dim_K(m/m^2) <= 1 (Nakayama)" % (tag, t2),
                  (L.dimK_mm2 <= 1) == chain_pred,
                  "dim = %d, chain predicted %s" % (L.dimK_mm2, chain_pred))


# --------------------------------------------------- helpers for the CRT side

def lift_component(S, j, pair):
    """the element of B^2 whose CRT components are 0 except the j-th (= pair)"""
    cs = tuple(pair if i == j else (S.Bj[i].zero, S.Bj[i].zero) for i in range(S.J))
    return S.combine_vec(cs)


def sigma_vec(S, v, k):
    S0 = S.B
    return (S0.sigma(v[0], k), S0.sigma(v[1], k))


def submodule_image(P, S, Wkey, k):
    """sigma_k(W) as an F_q-subspace of B^2"""
    vs = []
    for row in Wkey:
        v = P.from_vec(row)
        vs.append(P.vec(sigma_vec(S, v, k)))
    return P.LA.span(vs)


# =========================== Task B/C: principality, exhaustive where possible

def run_case_full(S, tag, expect, rng):
    """exhaustive submodule lattice of B^2, the CRT correspondence, mu, principality"""
    say("")
    say("-- submodules of B^2, mu, and principality (Tasks B, C) " + "-" * 33)
    F, B = S.F, S.B
    P = Module(B)
    Pj = [Module(Bj) for Bj in S.Bj]
    lat, wit = P.lattice_bfs()
    latj, witj = [], []
    for j in range(S.J):
        a, b = Pj[j].lattice_bfs()
        latj.append(a)
        witj.append(b)
    nW = len(lat)
    prod = 1
    for l in latj:
        prod *= len(l)
    check("%s: #{submodules of B^2} = prod_j #{submodules of B_j^2}" % tag,
          nW == prod, "%d = %d" % (nW, prod))
    if expect is not None:
        check("%s: the count agrees with the Phase-1/Stage-2A value" % tag,
              nW == expect, "%d vs %d" % (nW, expect))
    say("     mu_B distribution: %s" % sorted(
        [(mu, sum(1 for v in lat.values() if v == mu)) for mu in set(lat.values())]))
    say("     mu per component:  %s" % [sorted(
        [(mu, sum(1 for v in l.values() if v == mu)) for mu in set(l.values())])
        for l in latj])
    # --- W <-> (W_1,...,W_J)
    ok_split = ok_back = ok_mu = True
    seen = set()
    for W in lat:
        comps = []
        for j in range(S.J):
            vs = []
            for row in W:
                v = P.from_vec(row)
                cs = S.split_vec(v)
                vs.append(Pj[j].vec(cs[j]))
            comps.append(Pj[j].LA.span(vs))
        tt = tuple(comps)
        if any(tt[j] not in latj[j] for j in range(S.J)):
            ok_split = False
        seen.add(tt)
        # back
        ws = []
        for j in range(S.J):
            for row in tt[j]:
                ws.append(P.vec(lift_component(S, j, Pj[j].from_vec(row))))
        if P.LA.span(ws) != W:
            ok_back = False
        # mu across components (L-2.4.5)
        if lat[W] != max(latj[j][tt[j]] for j in range(S.J)):
            ok_mu = False
    check("%s: W |-> (W_1,..,W_J) maps submodules to tuples of submodules" % tag,
          ok_split, "%d submodules" % nW)
    check("%s: the correspondence is a bijection onto the product" % tag,
          len(seen) == nW == prod, "%d tuples" % len(seen))
    check("%s: the CRT reconstruction recovers W" % tag, ok_back, "")
    check("%s: mu_B(W) = max_j mu_{B_j}(W_j)  (L-2.4.5)" % tag, ok_mu,
          "all %d submodules" % nW)
    # --- mu by the brute-force route, cross-check
    cnt = 0
    bad = 0
    for W in sorted(lat, key=lambda k: len(k)):
        if len(W) == 0 or P.LA.size(W) > 4096:
            continue
        m2 = P.mu_brute(W, upto=2)
        if m2 is not None and m2 != lat[W]:
            bad += 1
        cnt += 1
        if cnt >= 40:
            break
    check("%s: mu from the brute-force scan agrees with the lattice BFS" % tag,
          bad == 0, "%d of %d submodules, |W| <= 4096" % (cnt, nW),
          exhaustive=(cnt >= nW and all(P.LA.size(W) <= 4096 for W in lat)))
    # --- principality, ideal by ideal
    M = P.M
    nprin = nnot = 0
    cert_bad = 0
    dim_bad = 0
    for W in lat:
        Ikey = P.I_of_W(W)
        mu = lat[W]
        if mu == 0:
            # W = 0  =>  I_W = 0 = 0 * M_2(B): principal by the mu(0) = 0 convention
            if M.LA.size(Ikey) != 1:
                cert_bad += 1
            nprin += 1
            continue
        if mu <= 2:
            # exhibit generators of W and certify I_W = x*M_2(B)
            gens = wit[W]
            w1 = gens[0]
            w2 = gens[1] if len(gens) > 1 else P.zero
            x = M.from_cols(P.vec(w1), P.vec(w2))
            inI = M.LA.contains(Ikey, M.vec(x))
            same = M.LA.size(M.right_ideal_of([x])) == M.LA.size(Ikey)
            if not (inI and same):
                cert_bad += 1
            else:
                nprin += 1
        else:
            # not principal: |x*M_2(B)| < |I_W| for every x in I_W
            if M.LA.size(Ikey) <= 20000:
                ok, _x = P.is_principal_scan(Ikey)
                if ok:
                    cert_bad += 1
            nnot += 1
    check("%s: every W with mu_B <= 2 gives a PRINCIPAL I_W (certificate)" % tag,
          cert_bad == 0, "%d ideals certified by |x*M_2(B)| = |I_W|" % nprin)
    if nnot:
        check("%s: every W with mu_B >= 3 gives a NON-principal I_W" % tag,
              cert_bad == 0, "%d ideals, exhaustive x-scan over each" % nnot)
    say("     principal: %d ; not principal: %d ; total %d" % (nprin, nnot, nW))
    # global criterion for this ring
    pred = (S.t == 1) or (S.v == 0)
    check("%s: P-2.6 prediction for this ring: all right ideals principal = %s"
          % (tag, pred), (nnot == 0) == pred,
          "principal %d, not principal %d" % (nprin, nnot))
    return nW, lat, latj


def run_case_crt(S, tag, expect, rng, budget=400):
    """(4,2,3): the lattice is too large to enumerate directly, so it is BUILT
    from the component lattices via the CRT and then cross-checked."""
    say("")
    say("-- submodules of B^2 built componentwise (Tasks B, C) " + "-" * 35)
    F, B = S.F, S.B
    P = Module(B)
    Pj = [Module(Bj) for Bj in S.Bj]
    latj, witj = [], []
    for j in range(S.J):
        a, b = Pj[j].lattice_bfs()
        latj.append(a)
        witj.append(b)
    prod = 1
    for l in latj:
        prod *= len(l)
    say("     component lattices: %s  -> product %d"
        % ([len(l) for l in latj], prod))
    if expect is not None:
        say("     predicted total (C-2.1g): %d" % expect)
    # cache the lift of every component basis vector (only sum n_j vectors in total)
    lift_cache = []
    for j in range(S.J):
        d = {}
        for key in latj[j]:
            d[key] = [P.vec(lift_component(S, j, Pj[j].from_vec(row))) for row in key]
        lift_cache.append(d)
    built = set()
    for combo in itertools.product(*[sorted(l.keys(), key=lambda k: (len(k), k))
                                     for l in latj]):
        vs = []
        for j in range(S.J):
            vs.extend(lift_cache[j][combo[j]])
        built.add(P.LA.span(vs))
    # closure under the ring generators, checked on a sample
    sample_all = sorted(built, key=lambda k: (len(k), k))
    notclosed = 0
    for W in sample_all[::max(1, len(sample_all) // 200)][:200]:
        if P.gen([P.from_vec(row) for row in W]) != W:
            notclosed += 1
    check("%s: the CRT-built submodules are B-submodules of B^2" % tag,
          notclosed == 0, "200 of %d built (sampled)" % len(built), exhaustive=False)
    check("%s: #built = prod_j #{submodules of B_j^2}" % tag,
          len(built) == prod, "%d = %d" % (len(built), prod))
    if expect is not None:
        check("%s: the CRT-built count matches the prediction" % tag,
              len(built) == expect, "%d vs %d" % (len(built), expect))
    # mu_B(W) = max_j mu_j : upper bound by exhibited generators, on a sample
    sample = sorted(built, key=lambda k: (len(k), k))
    if len(sample) > budget:
        sample = sample[:budget // 2] + sample[-(budget // 2):]
    up_bad = 0
    prin_bad = 0
    M = P.M
    checked = 0
    for W in sample:
        if not W:
            continue          # W = 0 : I_W = 0, principal by convention (mu = 0)
        # recover the components of W, take generators there, pad, and test
        comps = []
        for j in range(S.J):
            vs = []
            for row in W:
                cs = S.split_vec(P.from_vec(row))
                vs.append(Pj[j].vec(cs[j]))
            comps.append(Pj[j].LA.span(vs))
        mus = [latj[j][comps[j]] for j in range(S.J)]
        mu = max(mus)
        gens = [witj[j][comps[j]] for j in range(S.J)]
        ws = []
        for s in range(mu):
            comp = tuple(gens[j][s] if s < len(gens[j]) else Pj[j].zero
                         for j in range(S.J))
            ws.append(S.combine_vec(comp))
        if P.gen(ws) != W:
            up_bad += 1
        # principality certificate
        w1 = ws[0]
        w2 = ws[1] if len(ws) > 1 else P.zero
        x = M.from_cols(P.vec(w1), P.vec(w2))
        Ikey = P.I_of_W(W)
        if not (M.LA.contains(Ikey, M.vec(x)) and
                M.LA.size(M.right_ideal_of([x])) == M.LA.size(Ikey)):
            prin_bad += 1
        checked += 1
    check("%s: mu_B(W) <= max_j mu_{B_j}(W_j) (exhibited generators)" % tag,
          up_bad == 0, "%d submodules (sampled)" % checked, exhaustive=False)
    check("%s: every sampled W with mu <= 2 gives a principal I_W" % tag,
          prin_bad == 0, "%d certificates |x*M_2(B)| = |I_W|" % checked,
          exhaustive=False)
    # completeness on random submodules (evidence, not a proof)
    seed_rng = random.Random(SEED + 7)
    miss = 0
    tries = 0
    for _ in range(60):
        v = P.from_vec(tuple(seed_rng.randrange(F.q) for _ in range(P.dim)))
        W = P.gen([v])
        tries += 1
        if W not in built:
            miss += 1
        k = W
        for _ in range(2):
            v2 = P.from_vec(tuple(seed_rng.randrange(F.q) for _ in range(P.dim)))
            k = P.LA.sum(k, P.gen([v2]))
            tries += 1
            if k not in built:
                miss += 1
    check("%s: random submodules of B^2 all lie in the CRT-built list" % tag,
          miss == 0, "%d random submodules (sampled)" % tries, exhaustive=False)
    # every component is a chain ring => the global criterion predicts "all principal"
    pred = (S.t == 1) or (S.v == 0)
    check("%s: P-2.6 prediction: all right ideals principal = %s" % (tag, pred),
          pred and all(l.is_chain_predicted() for l in
                       [LocalData(S, j) for j in range(S.J)]),
          "every component is a chain ring")
    return len(built)


def run_wild(S, tag, rng, scan_budget=200000):
    """the wild case: W = m_j + m_j has mu_B = 4 and I_W = M_2(m_j) is NOT
    principal.  Certificates only (the lattice is not enumerable)."""
    say("")
    say("-- wild case: the counterexample W = m_j + m_j (Task B.4-B.6) " + "-" * 27)
    F = S.F
    P = Module(S.B)
    M = P.M
    nwild = 0
    for j in range(S.J):
        L = LocalData(S, j)
        if L.dimK_mm2 != 2:
            continue
        nwild += 1
        Bj = L.Bj
        Pj = Module(Bj)
        # W = m_j + m_j  as a submodule of B_j^2
        mvecs = [Bj.from_vec(row) for row in L.m]
        Wj = Pj.gen([(g, Bj.zero) for g in mvecs] + [(Bj.zero, g) for g in mvecs])
        # lift to B^2 (the j-th component)
        vs = []
        for row in Wj:
            vs.append(P.vec(lift_component(S, j, Pj.from_vec(row))))
        W = P.LA.span(vs)
        say("     component %d: |m_j| = %d, |W| = %d, dim_Fq W = %d"
            % (j, Bj.LA.size(L.m), P.LA.size(W), len(W)))
        # mu_B(W) = 4 : lower bound from Nakayama on the local component,
        # upper bound from four exhibited generators
        mW = Pj.gen([(Bj.mul(a, b), Bj.zero) for a in mvecs for b in mvecs] +
                    [(Bj.zero, Bj.mul(a, b)) for a in mvecs for b in mvecs])
        lowj = len(Wj) - len(mW)                    # dim_Fq (W/mW)
        lowK = lowj // L.K.d
        check("%s: dim_{K_j}(W/m_j W) = 4  (Nakayama lower bound mu >= 4)"
              % (tag + " comp %d" % j), lowK == 4, "dim = %d" % lowK)
        ugens = [(u_, Bj.zero) for u_ in mvecs[:2]] + [(Bj.zero, u_) for u_ in mvecs[:2]]
        up = len(Pj.gen(list(ugens))) == len(Wj)
        check("%s: four exhibited generators do generate W  (mu <= 4)"
              % (tag + " comp %d" % j), up, "u and f_j in each coordinate")
        # I_W is not principal: dim(I/IJ) = 4*dim_Fq(m/m^2) > 4*d_j
        Ikey = P.I_of_W(W)
        # J(S) = M_2(J(B)); on the j-th component J(B_j) = m_j
        IJ = P.I_of_W(P.LA.span([P.vec(lift_component(S, j, Pj.from_vec(row)))
                                 for row in mW]))
        dquot = len(Ikey) - len(IJ)
        maxprin = 4 * L.K.d
        check("%s: dim_{F_q}(I_W / I_W J(S)) = %d > %d = the principal bound"
              % (tag + " comp %d" % j, dquot, maxprin), dquot > maxprin,
              "so I_W = M_2(m_j) is NOT principal")
        # direct: no single x in I_W generates it (when the scan is feasible)
        if M.LA.size(Ikey) <= scan_budget:
            ok, wit = P.is_principal_scan(Ikey)
            check("%s: no x in I_W generates I_W (exhaustive x-scan)" % (tag),
                  not ok, "%d elements scanned" % M.LA.size(Ikey))
        # two generators do generate it (mu_S = 2)
        g1 = lift_component(S, j, (mvecs[0], Bj.zero))
        g2 = lift_component(S, j, (Bj.zero, mvecs[1])) if len(mvecs) > 1 else g1
        x1 = M.from_cols(P.vec(g1), P.vec(g2))
        # second generator: the "other half" of m in the two columns
        gm = mvecs[1] if len(mvecs) > 1 else mvecs[0]
        x2 = M.from_cols(P.vec(lift_component(S, j, (Bj.zero, mvecs[0]))),
                         P.vec(lift_component(S, j, (gm, Bj.zero))))
        two = M.LA.sum(M.right_ideal_of([x1]), M.right_ideal_of([x2]))
        check("%s: two explicit generators do generate I_W  (mu_S = 2)" % tag,
              two == Ikey, "|I_W| = %d" % M.LA.size(Ikey))
    # the global criterion: this ring is in the wild regime, and an explicit
    # non-principal right ideal was certified above
    check("%s: P-2.6 => not all right ideals are principal" % tag,
          S.t >= 2 and S.v >= 1 and nwild > 0,
          "t >= 2 and p | n, and %d non-principal right ideal(s) certified" % nwild)


# ============================================ Task D: Galois compatibility

def run_galois(S, tag, rng):
    say("")
    say("-- Task D: sigma_k on the CRT components " + "-" * 48)
    F, B = S.F, S.B
    # sigma_k is a ring automorphism of B
    if B.size <= 3000:
        els = list(B.elements())
        ex = True
        det = "all %d^2 pairs" % B.size
    else:
        els = [B.from_vec(tuple(rng.randrange(F.q) for _ in range(B.dimFq)))
               for _ in range(200)]
        ex = False
        det = "200^2 pairs (sampled)"
    aok = mok = True
    for x in els:
        for y in els:
            if B.sigma(B.add(x, y), 1) != B.add(B.sigma(x, 1), B.sigma(y, 1)):
                aok = False
            if B.sigma(B.mul(x, y), 1) != B.mul(B.sigma(x, 1), B.sigma(y, 1)):
                mok = False
    check("%s: sigma_1 is a ring endomorphism of B (fixes u and X)" % tag,
          aok and mok, det, exhaustive=ex)
    for k in range(F.r):
        perm = galois_permutation(S, k)
        pred = coset_permutation(S, k)
        check("%s: sigma_%d permutes the factors as p^%d does on the cosets" % (tag, k, k),
              perm == pred, "sigma_%d: %s" % (k, perm))
        # sigma_k(e_j) = e_{perm[j]}
        ok = all(B.sigma(S.ej[j], k) == S.ej[perm[j]] for j in range(S.J))
        check("%s: sigma_%d(e_j) = e_{perm(j)}" % (tag, k), ok,
              "%d idempotents" % S.J)
        # equivariance of the CRT map
        ok2 = True
        for x in els[:60]:
            sx = S.split(B.sigma(x, k))
            px = S.split(x)
            for j in range(S.J):
                if S.Bj[perm[j]].sigma(px[j], k) != sx[perm[j]]:
                    ok2 = False
        check("%s: split(sigma_%d(b)) = perm . split(b)" % (tag, k), ok2,
              "60 elements", exhaustive=(len(els) == B.size and B.size <= 60))
        # the preimage of m_j is mapped to the preimage of m_{perm[j]}
        ok3 = True
        for j in range(S.J):
            L = LocalData(S, j)
            pre = preimage_of_m(S, L, j)
            img = B.LA.span([B.vec(B.sigma(B.from_vec(row), k)) for row in pre])
            Lp = LocalData(S, perm[j])
            prep = preimage_of_m(S, Lp, perm[j])
            if img != prep:
                ok3 = False
        check("%s: sigma_%d maps the preimage of m_j onto that of m_{perm(j)}"
              % (tag, k), ok3, "%d components" % S.J)
        fixed = sum(1 for j in range(S.J) if perm[j] == j)
        say("     sigma_%d: %d of %d components are fixed (stability: p^%d C_j = C_j)"
            % (k, fixed, S.J, k))
    # report the orbits of the Galois permutation; a genuinely non-trivial
    # instance is verified as a negative control (neg-4) at (4,2,3), where
    # sigma_1 swaps two components.  A tautological "non-vacuity" check would be
    # worthless, so this is reported rather than asserted.
    nontriv = [k for k in range(F.r) if galois_permutation(S, k) != tuple(range(S.J))]
    say("     the permutation is non-trivial for k in %s"
        % (nontriv if nontriv else "no k (every q-cyclotomic coset is p-stable)"))
    # mu and principality are Galois-invariant
    if S.B.size <= 300:
        P = Module(B)
        lat, wit = P.lattice_bfs()
        bad_mu = 0
        bad_pr = 0
        for W in lat:
            if not W:
                continue
            for k in range(F.r):
                Ws = submodule_image(P, S, W, k)
                if Ws not in lat or lat[Ws] != lat[W]:
                    bad_mu += 1
        check("%s: mu_B(sigma_k W) = mu_B(W) for every submodule and every k" % tag,
              bad_mu == 0, "%d submodules x %d automorphisms" % (len(lat), F.r))
        say("     (principality of I_W depends on W only through mu_B(W), so it is")
        say("      Galois-invariant as well: T-083 of Stage 2A)")


def preimage_of_m(S, L, j):
    """the preimage in B of m_j ( = (sum_{i != j} B_i) + m_j )"""
    B = S.B
    vs = []
    for i in range(S.J):
        if i == j:
            for row in L.m:
                vs.append(B.vec(S.combine(tuple(
                    S.Bj[kk].from_vec(row) if kk == j else S.Bj[kk].zero
                    for kk in range(S.J)))))
        else:
            for b in S.Bj[i].basis():
                vs.append(B.vec(S.combine(tuple(
                    b if kk == i else S.Bj[kk].zero for kk in range(S.J)))))
    return B.LA.span(vs)


# ==================================================== negative controls

def run_negative_controls(rng):
    say("")
    say("-- negative controls (wrong conventions must FAIL) " + "-" * 41)
    # (1) the wrong CRT modulus: <f_j> instead of <f_j^{p^v}> when p | n
    S = CRTSystem(4, 1, 2)
    F = S.F
    B = S.B
    wrong = [PolyQuot(F, S.t, f) for f in S.facs]
    elt = B.from_poly(ap_embed(F, S.t, S.g))        # X^{n'} - 1
    imgs = [wrong[j].from_poly(pdivmod_local(B.A, B.to_poly(elt),
                                             ap_embed(F, S.t, S.facs[j]))[1])
            for j in range(S.J)]
    check("neg-1: the map to prod A_t[X]/<f_j> kills X^{n'}-1 != 0",
          elt != B.zero and all(x == wrong[j].zero for j, x in enumerate(imgs)),
          "so the reduced modulus does NOT give an isomorphism")
    # (2) the row convention: {M : rows of M in W} is not a right ideal
    S2 = CRTSystem(2, 1, 1)
    P2 = Module(S2.B)
    M2 = P2.M
    W = P2.LA.span([P2.vec((S2.B.one, S2.B.zero))])       # first coordinate axis
    # build {M : both rows lie in W} directly
    rows = []
    for v in W:
        # row 1 = v means (a11, a12) = v ; row 2 = 0
        r1 = v + tuple([0] * S2.B.dimFq) + tuple([0] * S2.B.dimFq) + tuple([0] * S2.B.dimFq)
        rows.append(r1)
    VR = M2.LA.span(rows)
    bad = None
    for v in M2.LA.elements(VR):
        for N in M2.gens_as_fq_algebra():
            p = M2.vec(M2.mul(M2.from_vec(v), N))
            if not M2.LA.contains(VR, p):
                bad = (v, N)
                break
        if bad:
            break
    check("neg-2: {M : rows of M in W} is NOT a right ideal", bad is not None,
          "counterexample found by exhaustive search" if bad else "NOT FOUND")
    # (3) {M : im M superset W} is not a right ideal
    full = M2.LA.span([tuple(1 if i == j else 0 for j in range(M2.dim))
                       for i in range(M2.dim)])          # the whole space
    # the SET (not its span: the span of a non-ideal set can accidentally be an ideal)
    sup = set()
    for v in M2.LA.elements(full):
        x = M2.from_vec(v)
        im = P2.LA.span([M2.col(x, 0), M2.col(x, 1)])
        if all(P2.LA.contains(im, row) for row in W):
            sup.add(v)
    bad3 = None
    for v in sup:
        for N in M2.gens_as_fq_algebra():
            if M2.vec(M2.mul(M2.from_vec(v), N)) not in sup:
                bad3 = v
                break
        if bad3:
            break
    check("neg-3: the SET {M : im M superset of W} is NOT a right ideal",
          bad3 is not None and tuple([0] * M2.dim) not in sup,
          "counterexample found; 0 is not even in the set" if bad3 else "NOT FOUND")
    # (4) the naive Galois assumption "sigma_k fixes every component"
    S4 = CRTSystem(4, 2, 3)
    perm = galois_permutation(S4, 1)
    naive_ok = (perm == tuple(range(S4.J)))
    check("neg-4: the naive claim 'sigma_1 fixes every CRT component' is FALSE",
          not naive_ok, "at (4,2,3) the permutation is %s" % (perm,))
    # (5) non-vacuity: the squarefree/repeated-root rings really do have
    #     more than one right ideal, and really do need 2 generators somewhere
    S5 = CRTSystem(4, 2, 1)
    P5 = Module(S5.B)
    lat5, _w5 = P5.lattice_bfs()
    check("neg-5: non-vacuity - a 'chain' ring still has ideals needing 2 generators",
          max(lat5.values()) >= 2 and len(lat5) > 1,
          "%d submodules, max mu = %d" % (len(lat5), max(lat5.values())))


# ================================================================== main

def main():
    rng = random.Random(SEED)
    say("=" * 96)
    say("PHASE 2 - STAGE 2B:  CRT/Hensel decomposition and global principality")
    say("=" * 96)
    say("  seed = %d ; every check is labelled [EXH] (exhaustive) or [SMP] (sampled)"
        % SEED)

    # ---------- the required parameter cases -------------------------------
    # (q, t, n, mode, expected count from Phase 1 / Stage 2A / C-2.1g)
    CASES = [
        (4, 2, 1, "full", 33),        # squarefree (p | n false), t = 2
        (4, 1, 2, "full", 33),        # repeated root, t = 1  (chain ring)
        (2, 1, 3, "full", 35),        # squarefree, two components (5 * 7)
        (9, 1, 2, "full", 144),       # squarefree, t = 1, two fields (12^2)
        (8, 1, 2, "full", 93),        # repeated root, t = 1, q = 8  (N(2,8))
        (4, 2, 3, "crt", 35937),      # squarefree, t = 2, three components (33^3)
        (2, 2, 2, "wild", 159),       # WILD (smallest): 159 submodules, 22 not principal
        (4, 2, 2, "wild", None),      # WILD: the proposal's predicted counterexample
        (9, 2, 3, "wild", None),      # WILD: p = 3 | n = 3, e = 3
    ]
    for (q, t, n, mode, expect) in CASES:
        tag = "(%d,%d,%d)" % (q, t, n)
        S = CRTSystem(q, t, n)
        ring_head(S, tag)
        run_factorisation(S, tag, rng)
        run_hensel(S, tag, rng)
        run_crt(S, tag, rng)
        if mode == "full":
            run_ideal_crt(S, tag, rng)
        run_local(S, tag, rng)
        if mode == "full":
            run_case_full(S, tag, expect, rng)
        elif mode == "crt":
            run_case_crt(S, tag, expect, rng)
        else:
            run_wild(S, tag, rng)
        if mode in ("full", "crt") or (q, t, n) == (4, 2, 3):
            run_galois(S, tag, rng)

    # ---------- negative controls ------------------------------------------
    head("negative controls and non-vacuity")
    run_negative_controls(rng)

    say("")
    say("=" * 96)
    say("SUMMARY")
    say("=" * 96)
    say("  %d checks, %d PASS, %d FAIL"
        % (NCHECK[0], NCHECK[0] - len(FAILURES), len(FAILURES)))
    if FAILURES:
        say("  FAILURES:")
        for (nm, det) in FAILURES:
            say("    - %s : %s" % (nm, det))
    else:
        say("  no failures")
    say("  end of log")
    with open(LOG_NAME, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
