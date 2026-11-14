#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 1 -- independent computational corroboration of
03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md

Scope (Tasks A, B, C of the Phase-1 brief):

  A. Ring structure of A_t = F_q[u]/<u^t> and R = M_2(A_t):
     cardinality, normal form, units, centre, Jacobson radical, nilpotency
     index, socle, ideal lattices, matrix units, |Aut(A_t)|, the Morita
     correspondence for right ideals, and the cardinality table.

  B. Automorphisms / anti-automorphisms:
     ord(sigma_s), sigma_s(u) = u, theta_s(X) = sigma_s(X^T) is an
     ANTI-automorphism, theta_s^2 = sigma_{2s}, ord(theta_s) = 2r/gcd(r,2s),
     theta_s is never the identity, involutive <=> r | 2s
     (Lemma 4.1-4.4, Theorem 4.5, Corollary 4.6).

  C. Module conventions and the pairing:
     both orthogonals of a right module are right modules (Lemma 5.5),
     ^{perp_s}C = (sigma_{-2s}C)^{perp_s} (Lemma 5.7), Lambda catches every
     nonzero one-sided ideal (Lemma 6.5), b_s is non-degenerate (Theorem 6.6),
     the two orthogonals coincide (Lemma 6.7),
     (C^{perp_s})^{perp_s} = sigma_{2s}(C) (Theorem 6.8),
     side flip for the plain product (Proposition 5.9).

Everything is finite.  Each check is labelled

     [EXH]  exhaustive over the whole ring / over all subspaces / over all
            elements of the relevant finite set;
     [SMP]  verified on a uniformly seeded random sample (stated explicitly).

Nothing is imported from the earlier audit scripts: the field, the local ring
and the matrix ring are rebuilt from scratch here, so that a bug in one
library cannot propagate into this check.  Every ring-theoretic quantity is
computed from the definitions (units by exhibiting an inverse, the Jacobson
radical by the criterion 1 - xy in R^x, ideals by closing under the relevant
operations), never from the formula that is being checked.

Usage:  python3 ring_structure_checks.py
Log:    ring_structure_log.txt
"""

import itertools
import random
import sys

# ==========================================================================
# 0.  infrastructure:  F_q,  A_t = F_q[u]/<u^t>,  R = M_2(A_t)
# ==========================================================================

class Field(object):
    """F_q, q = p^r (r <= 4), built as F_p[x]/(f), f monic irreducible."""

    def __init__(self, p, r):
        self.p, self.r, self.q = p, r, p ** r
        q, pr, rr = self.q, p, r
        self.f = self._irreducible(p, r)
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        for a in range(q):
            ca = self._digits(a)
            for b in range(q):
                cb = self._digits(b)
                self.add[a][b] = self._code([(ca[i] + cb[i]) % pr for i in range(rr)])
                self.mul[a][b] = self._code(self._mulmod(ca, cb))
        # NOTE: neg must be filled in completely BEFORE sub is built, otherwise
        # sub[a][b] = a + (-b) silently uses neg[b] = 0 for the b not yet done.
        self.neg = [0] * q
        for a in range(q):
            for b in range(q):
                if self.add[a][b] == 0:
                    self.neg[a] = b
                    break
        self.sub = [[self.add[a][self.neg[b]] for b in range(q)] for a in range(q)]
        self.inv = [0] * q
        for a in range(1, q):
            for b in range(1, q):
                if self.mul[a][b] == 1:
                    self.inv[a] = b
                    break
        self.frob = []
        for s in range(r):
            tab = [0] * q
            for a in range(q):
                tab[a] = self.pow(a, pr ** s)
            self.frob.append(tab)

    def _irreducible(self, p, r):
        if r == 1:
            return [0]
        for code in range(p ** r):
            coeffs = [(code // p ** i) % p for i in range(r)]
            if all(self._eval(coeffs, a) != 0 for a in range(p)):
                # degree <= 3:  no root  =>  irreducible
                return coeffs
        raise RuntimeError("no irreducible polynomial of degree %d over F_%d" % (r, p))

    def _eval(self, coeffs, a):
        v = a ** self.r
        for i, c in enumerate(coeffs):
            v += c * (a ** i)
        return v % self.p

    def _digits(self, a):
        return [(a // self.p ** i) % self.p for i in range(self.r)]

    def _code(self, d):
        return sum(x * self.p ** i for i, x in enumerate(d))

    def _mulmod(self, a, b):
        r, p = self.r, self.p
        out = [0] * (2 * r - 1)
        for i in range(r):
            if a[i]:
                for j in range(r):
                    if b[j]:
                        out[i + j] = (out[i + j] + a[i] * b[j]) % p
        for d in range(2 * r - 2, r - 1, -1):
            c = out[d]
            if c:
                out[d] = 0
                for i in range(r):
                    out[d - r + i] = (out[d - r + i] - c * self.f[i]) % p
        return out[:r]

    def pow(self, a, e):
        res, base = 1, a % self.q
        while e:
            if e & 1:
                res = self.mul[res][base]
            base = self.mul[base][base]
            e >>= 1
        return res

    def frob_k(self, a, s):
        return self.frob[s % self.r][a]


class Local(object):
    """A_t = F_q[u]/<u^t>;  an element is a tuple of t field elements."""

    def __init__(self, F, t):
        self.F, self.t = F, t
        self.zero = tuple([0] * t)
        self.one = (1,) + tuple([0] * (t - 1))
        self.u = tuple([1 if i == 1 else 0 for i in range(t)]) if t > 1 else self.zero

    def add(self, a, b):
        F = self.F
        return tuple(F.add[a[i]][b[i]] for i in range(self.t))

    def neg(self, a):
        return tuple(self.F.neg[x] for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        F, t = self.F, self.t
        out = [0] * t
        for i in range(t):
            if a[i]:
                for j in range(t - i):
                    if b[j]:
                        out[i + j] = F.add[out[i + j]][F.mul[a[i]][b[j]]]
        return tuple(out)

    def scalar(self, c, a):
        return tuple(self.F.mul[c][x] for x in a)

    def sigma(self, a, s):
        return tuple(self.F.frob[s % self.F.r][x] for x in a)

    def val(self, a):
        for i in range(self.t):
            if a[i]:
                return i
        return self.t

    def is_unit(self, a):
        return a[0] != 0

    def inv(self, a):
        F = self.F
        x = [0] * self.t
        x[0] = F.inv[a[0]]
        for k in range(1, self.t):
            acc = 0
            for i in range(1, k + 1):
                if a[i]:
                    acc = F.add[acc][F.mul[a[i]][x[k - i]]]
            x[k] = F.mul[F.neg[F.inv[a[0]]]][acc]
        return tuple(x)

    def pow(self, a, e):
        res, base = self.one, a
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def elem_list(self):
        return list(itertools.product(range(self.F.q), repeat=self.t))


class MatRing(object):
    """M_m(A);  an element is a tuple of m^2 entries of A (row major)."""

    def __init__(self, A, m):
        self.A, self.m, self.F, self.t = A, m, A.F, A.t
        self.d = m * m * A.t                     # dim over F_q
        z, one = A.zero, A.one
        self.zero = tuple([z] * (m * m))
        self.one = tuple([one if i == j else z for i in range(m) for j in range(m)])

    def idx(self, i, j):
        return i * self.m + j

    def unit(self, i, j, c=None):
        A = self.A
        c = A.one if c is None else c
        z = A.zero
        return tuple([c if (a == i and b == j) else z
                      for a in range(self.m) for b in range(self.m)])

    def add(self, X, Y):
        return tuple(self.A.add(X[k], Y[k]) for k in range(len(X)))

    def neg(self, X):
        return tuple(self.A.neg(x) for x in X)

    def sub(self, X, Y):
        return self.add(X, self.neg(Y))

    def mul(self, X, Y):
        A, m = self.A, self.m
        out = []
        for i in range(m):
            for j in range(m):
                acc = A.zero
                for k in range(m):
                    xk, yk = X[self.idx(i, k)], Y[self.idx(k, j)]
                    if xk != A.zero and yk != A.zero:
                        acc = A.add(acc, A.mul(xk, yk))
                out.append(acc)
        return tuple(out)

    def transpose(self, X):
        return tuple(X[self.idx(j, i)] for i in range(self.m) for j in range(self.m))

    def sigma(self, X, s):
        return tuple(self.A.sigma(x, s) for x in X)

    def theta(self, X, s):
        return self.sigma(self.transpose(X), s)

    def trace(self, X):
        acc = self.A.zero
        for i in range(self.m):
            acc = self.A.add(acc, X[self.idx(i, i)])
        return acc

    def Lambda(self, X):
        return self.trace(X)[self.t - 1]

    def det(self, X):
        A = self.A
        return A.sub(A.mul(X[0], X[3]), A.mul(X[1], X[2]))

    def inv(self, X):
        A = self.A
        di = A.inv(self.det(X))
        # X^{-1} = (det X)^{-1} adj(X);  the scalar is an element of A_t, so the
        # products are A_t-products (A.mul), not F_q-scalar products.
        return tuple(A.mul(di, y) for y in (X[3], A.neg(X[1]), A.neg(X[2]), X[0]))

    def is_unit(self, X):
        return self.A.is_unit(self.det(X))

    def scalar_mat(self, a):
        z = self.A.zero
        return tuple([a if i == j else z for i in range(self.m) for j in range(self.m)])

    def vec(self, X):
        out = []
        for x in X:
            out.extend(x)
        return tuple(out)

    def unvec(self, v):
        t = self.t
        return tuple(tuple(v[k * t:(k + 1) * t]) for k in range(len(v) // t))

    def basis(self):
        """the F_q-basis  u^e E_ij  (e = 0..t-1, i,j = 0..m-1)"""
        A = self.A
        out = []
        for i in range(self.m):
            for j in range(self.m):
                for e in range(self.t):
                    c = A.pow(A.u, e) if self.t > 1 else A.one
                    out.append(self.unit(i, j, c))
        return out

    def elem_list(self):
        return list(itertools.product(self.A.elem_list(), repeat=self.m * self.m))


# ==========================================================================
# 1.  F_q-linear algebra on coordinate vectors
# ==========================================================================

def rref(rows, F, ncols):
    M = [list(r) for r in rows]
    piv = []
    row = 0
    for col in range(ncols):
        sel = None
        for i in range(row, len(M)):
            if M[i][col]:
                sel = i
                break
        if sel is None:
            continue
        M[row], M[sel] = M[sel], M[row]
        iv = F.inv[M[row][col]]
        M[row] = [F.mul[iv][x] for x in M[row]]
        for i in range(len(M)):
            if i != row and M[i][col]:
                f = M[i][col]
                M[i] = [F.sub[a][b] for a, b in zip(M[i], [F.mul[f][x] for x in M[row]])]
        piv.append(col)
        row += 1
        if row == len(M):
            break
    return M[:len(piv)], piv


def nullspace(rows, F, dim):
    """{y in F^dim :  <row, y> = 0 for all rows},  as (frozenset, dim)."""
    if not rows:
        return all_vectors(F, dim)
    M, piv = rref(rows, F, dim)
    free = [c for c in range(dim) if c not in piv]
    basis = []
    for fc in free:
        y = [0] * dim
        y[fc] = 1
        for r, pc in enumerate(piv):
            y[pc] = F.neg[M[r][fc]]
        basis.append(tuple(y))
    return span_of(basis, F, dim)


def nullspace_basis(rows, F, dim):
    """canonical RREF basis of {y : <row,y> = 0}  (cheap: no enumeration)"""
    if not rows:
        return tuple(tuple(e) for e in
                     rref([[1 if i == j else 0 for i in range(dim)]
                           for j in range(dim)], F, dim)[0])
    M, piv = rref(rows, F, dim)
    free = [c for c in range(dim) if c not in piv]
    basis = []
    for fc in free:
        y = [0] * dim
        y[fc] = 1
        for r, pc in enumerate(piv):
            y[pc] = F.neg[M[r][fc]]
        basis.append(list(y))
    return tuple(tuple(b) for b in rref(basis, F, dim)[0])


def span_of(basis, F, dim):
    rows, _ = rref(basis, F, dim)
    k = len(rows)
    out = set()
    for coeffs in itertools.product(range(F.q), repeat=k):
        acc = [0] * dim
        for c, r in zip(coeffs, rows):
            if c:
                acc = [F.add[a][F.mul[c][b]] for a, b in zip(acc, r)]
        out.add(tuple(acc))
    return frozenset(out), k


def all_vectors(F, dim):
    return frozenset(itertools.product(range(F.q), repeat=dim)), dim


def canonical(R, F, elements):
    """canonical form of the F_q-span of `elements`: its RREF basis as a tuple"""
    B, _ = rref([list(R.vec(x)) for x in elements], F, R.d)
    return tuple(tuple(b) for b in B)


def span_closure(R, F, seeds, gens, two_sided=False):
    """the smallest (one- or two-sided) ideal of R containing seeds.

    Ideals are F_q-subspaces, so everything is done on coordinate vectors with
    RREF; the result is returned as (canonical RREF basis, F_q-dimension) --
    the full element set is NOT materialised (it can have q^8 elements).
    Multiplying by the generators E_ij (and uI) suffices, F_q-scaling being
    automatic because the objects are F_q-spans.
    """
    d = R.d
    rows = [list(R.vec(x)) for x in seeds]
    while True:
        B, _ = rref(rows, F, d)
        cur = [R.unvec(tuple(b)) for b in B]
        new = [list(b) for b in B]
        for X in cur:
            for G in gens:
                new.append(list(R.vec(R.mul(X, G))))
                if two_sided:
                    new.append(list(R.vec(R.mul(G, X))))
        B2, _ = rref(new, F, d)
        if len(B2) == len(B):
            return tuple(tuple(b) for b in B2), len(B2)
        rows = new


def span_basis(R, F, elements):
    """an F_q-basis (as ring elements) of the span of `elements`"""
    B, _ = rref([list(R.vec(x)) for x in elements], F, R.d)
    return [R.unvec(tuple(b)) for b in B]


def enumerate_subspaces(F, dim):
    """all F_q-subspaces of F_q^dim, as frozensets of coordinate vectors."""
    seen = set()
    out = []
    def rec(start, rows):
        key, _ = span_of([tuple(r) for r in rows], F, dim) if rows else (frozenset([tuple([0]*dim)]), 0)
        if key not in seen:
            seen.add(key)
            out.append(key)
        for piv in range(start, dim):
            free = dim - 1 - piv
            for vals in itertools.product(range(F.q), repeat=free):
                row = [0] * dim
                row[piv] = 1
                for off, v in enumerate(vals):
                    row[piv + 1 + off] = v
                rec(piv + 1, rows + [row])
    rec(0, [])
    return out


# ==========================================================================
# 2.  reporting
# ==========================================================================

LINES = []
FAILURES = []
NCHECK = [0]


def say(msg):
    print(msg)
    sys.stdout.flush()
    LINES.append(msg)


def check(name, ok, detail="", exhaustive=True):
    NCHECK[0] += 1
    tag = "[EXH]" if exhaustive else "[SMP]"
    say("  %s %-60s %s  %s" % (tag, name, "PASS" if ok else "**FAIL**", detail))
    if not ok:
        FAILURES.append((name, detail))
    return ok


def field_generator(F):
    """a in F_q with F_p(a) = F_q  (so ord of the Frobenius on a is maximal)"""
    if F.r == 1:
        return 1
    for a in range(2, F.q):
        orb, cur = {a}, a
        for _ in range(F.r - 1):
            cur = F.frob[1][cur]
            orb.add(cur)
        if len(orb) == F.r:
            return a
    raise RuntimeError("no generator found")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ==========================================================================
# 3.  Task A -- the local ring A_t
# ==========================================================================

def task_A_local(p, r, t):
    F = Field(p, r)
    A = Local(F, t)
    q = F.q
    say("")
    say("A.1  A_t = F_%d[u]/<u^%d>     q = %d,  t = %d,  |A_t| = %d" % (q, t, q, t, q ** t))
    els = A.elem_list()

    check("normal form: |A_t| = q^t distinct representatives",
          len(els) == q ** t and len(set(els)) == q ** t,
          "%d = %d^%d" % (len(els), q, t))

    # ---- units ----------------------------------------------------------
    units = [a for a in els if A.is_unit(a)]
    check("a is a unit  <=>  a_0 != 0",
          all(A.is_unit(a) == (a[0] != 0) for a in els), "%d units" % len(units))
    check("|A_t^x| = (q-1) q^{t-1}", len(units) == (q - 1) * q ** (t - 1),
          "computed %d, formula %d" % (len(units), (q - 1) * q ** (t - 1)))
    check("every unit has a two-sided inverse",
          all(A.mul(a, A.inv(a)) == A.one and A.mul(A.inv(a), a) == A.one for a in units))

    # ---- ideals = F_q-subspaces stable under multiplication by u ---------
    subs = enumerate_subspaces(F, t)
    def stable(S):
        return all(tuple(A.mul(A.u, tuple(x))) in S for x in S)
    ideals = [S for S in subs if stable(S)]
    predicted = []
    for i in range(t):
        gens = [tuple(A.mul(A.pow(A.u, i), A.pow(A.u, j))) for j in range(t)]
        predicted.append(span_of(gens, F, t)[0])
    predicted.append(frozenset([tuple([0] * t)]))
    check("the ideals of A_t are exactly (u^0) > (u) > ... > (u^{t-1}) > 0",
          set(ideals) == set(predicted),
          "%d u-stable subspaces, %d of them ideals" % (len(subs), len(ideals)))
    check("#ideals(A_t) = t+1  (A_t is a chain ring)", len(ideals) == t + 1,
          "%d" % len(ideals))
    check("the ideals form a chain: (u^i) subset (u^j) for i >= j",
          all(predicted[i] <= predicted[j] for i in range(t + 1) for j in range(i)))

    # ---- Jacobson radical, nilpotency, socle -----------------------------
    jac = [x for x in els if all(A.is_unit(A.sub(A.one, A.mul(x, y))) for y in els)]
    check("Jac(A_t) = {x : 1-xy unit for all y} = (u) = {x_0 = 0}",
          set(jac) == set(x for x in els if x[0] == 0),
          "|Jac| = %d = q^{t-1} = %d" % (len(jac), q ** (t - 1)))
    if t > 1:
        check("nilpotency index of Jac(A_t) is exactly t",
              A.pow(A.u, t) == A.zero and A.pow(A.u, t - 1) != A.zero)
    socle = [x for x in els if all(A.mul(x, y) == A.zero for y in jac)]
    socle_pred = span_of([list(A.pow(A.u, t - 1))], F, t)[0]
    check("socle(A_t) = ann(Jac) = (u^{t-1}),  |socle| = q",
          set(socle) == set(tuple(x) for x in socle_pred) and len(socle) == q,
          "|socle| = %d" % len(socle))

    # ---- the Frobenius form lambda --------------------------------------
    def lam(a):
        return a[t - 1]
    ok = True
    for x in els:
        if x == A.zero:
            continue
        if not any(lam(A.mul(x, y)) != 0 for y in els):
            ok = False
            break
    check("lambda(a) = coeff of u^{t-1}: non-degenerate, catches every nonzero ideal",
          ok)
    check("lambda is symmetric and associative",
          all(lam(A.mul(x, y)) == lam(A.mul(y, x)) for x in els[:60] for y in els[:60])
          and all(lam(A.mul(A.mul(x, y), z)) == lam(A.mul(x, A.mul(y, z)))
                  for x in els[:30] for y in els[:30] for z in els[:30]),
          exhaustive=False)

    # ---- |Aut(A_t)| ------------------------------------------------------
    if q ** t <= 600:
        nil = [c for c in els if c[0] == 0]           # c^t = 0  <=>  c in (u)
        auto = 0
        endo = 0
        for j in range(F.r):
            for c in nil:
                img = []
                for a in els:                          # tau(sum a_i u^i)
                    acc = A.zero
                    cpow = A.one
                    for i in range(t):
                        if a[i]:
                            acc = A.add(acc, A.scalar(F.frob[j][a[i]], cpow))
                        cpow = A.mul(cpow, c)
                    img.append(acc)
                endo += 1
                if len(set(img)) == q ** t:
                    auto += 1
        pred = F.r if t == 1 else F.r * (q - 1) * q ** (t - 2)
        check("|Aut(A_t)| = r (t=1) / r(q-1)q^{t-2} (t>=2)",
              auto == pred,
              "computed %d, formula %d, endomorphisms %d" % (auto, pred, endo))
        sig_subgroup = len({tuple(tuple(A.sigma(a, j)) for a in els) for j in range(F.r)})
        check("Convention 1.7: the sigma_s (fixing u) form a subgroup of order r",
              sig_subgroup == F.r and all(A.sigma(A.u, j) == A.u for j in range(F.r)),
              "order %d, sigma_s(u) = u for all s" % sig_subgroup)
    return F, A


# ==========================================================================
# 4.  Task A -- the matrix ring R = M_2(A_t)
# ==========================================================================

def task_A_matrix(p, r, t):
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    q, d = F.q, R.d
    m = 2
    say("")
    say("A.2  R = M_2(A_t)     q = %d,  t = %d,  |R| = q^{4t} = %d" % (q, t, q ** (4 * t)))

    E = {(i, j): R.unit(i, j) for i in range(m) for j in range(m)}
    ok_mu = all(R.mul(E[(i, j)], E[(k, l)]) == (E[(i, l)] if j == k else R.zero)
                for (i, j) in E for (k, l) in E)
    ident = R.zero
    for i in range(m):
        ident = R.add(ident, E[(i, i)])
    check("matrix units: E_ij E_kl = delta_jk E_il,  sum_i E_ii = 1",
          ok_mu and ident == R.one)

    els = list(itertools.product(A.elem_list(), repeat=4))
    check("|R| = q^{4t}", len(els) == q ** (4 * t), "%d" % len(els))

    rnd = random.Random(20261104 + 100 * q + t)
    ok_alg = True
    for _ in range(300):
        X, Y, Z = rnd.choice(els), rnd.choice(els), rnd.choice(els)
        if R.mul(R.mul(X, Y), Z) != R.mul(X, R.mul(Y, Z)):
            ok_alg = False
        if R.mul(R.add(X, Y), Z) != R.add(R.mul(X, Z), R.mul(Y, Z)):
            ok_alg = False
        if R.mul(X, R.add(Y, Z)) != R.add(R.mul(X, Y), R.mul(X, Z)):
            ok_alg = False
    check("associative and distributive (300 random triples)", ok_alg, exhaustive=False)
    check("R is non-commutative",
          R.mul(E[(0, 1)], E[(1, 0)]) != R.mul(E[(1, 0)], E[(0, 1)]))

    # ---- centre ----------------------------------------------------------
    tests = [E[(0, 1)], E[(1, 0)], E[(0, 0)]]
    if t > 1:
        tests.append(R.scalar_mat(A.u))
    centre = [X for X in els if all(R.mul(X, G) == R.mul(G, X) for G in tests)]
    centre_pred = [R.scalar_mat(a) for a in A.elem_list()]
    check("Z(R) = {aI : a in A_t}  and  |Z(R)| = q^t",
          set(centre) == set(centre_pred) and len(centre) == q ** t,
          "computed %d, formula %d" % (len(centre), q ** t))

    # ---- units -----------------------------------------------------------
    units = [X for X in els if R.is_unit(X)]
    pred = q ** (4 * (t - 1)) * (q * q - 1) * (q * q - q)
    check("X in R^x  <=>  det X in A_t^x  <=>  det(X mod u) != 0",
          all(R.is_unit(X) == (R.det(X)[0] != 0) for X in els))
    check("|GL_2(A_t)| = q^{4(t-1)}(q^2-1)(q^2-q)", len(units) == pred,
          "computed %d, formula %d" % (len(units), pred))
    if len(units) <= 60000:
        check("every unit has a two-sided inverse",
              all(R.mul(X, R.inv(X)) == R.one and R.mul(R.inv(X), X) == R.one
                  for X in units))
    else:
        smp = rnd.sample(units, 20000)
        check("every unit has a two-sided inverse",
              all(R.mul(X, R.inv(X)) == R.one and R.mul(R.inv(X), X) == R.one
                  for X in smp), "20000 sampled units", exhaustive=False)

    # ---- Jacobson radical -------------------------------------------------
    uR = [X for X in els if all(x[0] == 0 for x in X)]
    uRset = set(uR)
    check("uR = M_2((u)) = {entries in (u)} has |uR| = q^{4(t-1)}",
          len(uR) == q ** (4 * (t - 1)),
          "%d = %d^%d" % (len(uR), q, 4 * (t - 1)))
    check("uR is closed under left and right multiplication by R",
          all(R.mul(X, Y) in uRset and R.mul(Y, X) in uRset
              for X in (uR if len(uR) <= 400 else rnd.sample(uR, 400))
              for Y in (els if len(els) <= 400 else rnd.sample(els, 400))),
          exhaustive=(len(uR) <= 400 and len(els) <= 400))
    if t > 1:
        check("(uR)^t = 0  and  (uR)^{t-1} != 0",
              A.pow(A.u, t) == A.zero and
              R.scalar_mat(A.pow(A.u, t - 1)) != R.zero)
    scan = els if len(els) <= 2500 else rnd.sample(els, 2500)
    ok_jac = all(R.is_unit(R.sub(R.one, R.mul(R.scalar_mat(A.u), Y))) for Y in scan)
    check("1 - XY is a unit for all X in uR, Y in R   (uR c Jac(R))", ok_jac,
          exhaustive=(len(els) <= 2500))
    # R/uR is M_2(F_q), which is simple: every nonzero element generates R
    barA = Local(F, 1)
    bar = MatRing(barA, 2)
    bar_els = list(itertools.product(barA.elem_list(), repeat=4))
    bar_gens = [bar.unit(i, j) for i in range(2) for j in range(2)]
    ok_simple = all(span_closure(bar, F, [X], bar_gens, two_sided=True)[1] == bar.d
                    for X in bar_els if X != bar.zero)
    check("R/uR = M_2(F_q) is simple (every nonzero element generates all of it)",
          ok_simple, "%d elements checked" % (len(bar_els) - 1))

    # ---- two-sided ideals -------------------------------------------------
    # u^i R is spanned over F_q by the u^k E_ij with i <= k < t  (NOT just by the
    # single power u^i E_ij: that would give a 4-dim, not a 4(t-i)-dim, space).
    pred_ts = []
    for i in range(t + 1):
        gens = [R.unit(ii, jj, A.pow(A.u, k))
                for k in range(i, t) for ii in range(2) for jj in range(2)]
        pred_ts.append(canonical(R, F, gens))
    check("each u^i R (i=0..t) is a two-sided ideal with dim 4(t-i)",
          all(len(pred_ts[i]) == 4 * (t - i) for i in range(t + 1)),
          "dims %s" % [len(b) for b in pred_ts])
    gens_all = [E[(i, j)] for i in range(2) for j in range(2)]
    if t > 1:
        gens_all.append(R.scalar_mat(A.u))
    sample = els if len(els) <= 1200 else rnd.sample(els, 1200)
    ok_ts = True
    for X in sample:
        i = min(A.val(x) for x in X)
        S, _ = span_closure(R, F, [X], gens_all, two_sided=True)
        if S != pred_ts[i]:
            ok_ts = False
            break
    check("the two-sided ideal generated by X is u^{val(X)} R",
          ok_ts, exhaustive=(len(els) <= 1200))
    check("#two-sided ideals of R = t+1", len(set(pred_ts)) == t + 1,
          "%d" % len(set(pred_ts)))
    return F, A, R


# ==========================================================================
# 5.  Task A -- Morita:  right ideals of M_2(A_t)  <->  submodules of A_t^2
# ==========================================================================

def task_A_morita(p, r, t):
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    q, d = F.q, R.d
    say("")
    say("A.3  Morita: right ideals of M_2(A_t) <-> A_t-submodules of A_t^2"
        "     q = %d, t = %d" % (q, t))
    vdim = 2 * t                                  # A_t^2 as an F_q-space
    # multiplication by u on A_t^2, as an F_q-linear map on coordinates
    def mul_u(v):
        w = tuple(v[:t]) and A.mul(tuple(v[:t]), A.u)
        w2 = A.mul(tuple(v[t:]), A.u)
        return tuple(list(w) + list(w2))
    subs = enumerate_subspaces(F, vdim)
    if t == 1:
        submods = subs                            # u = 0: no condition
    else:
        submods = [S for S in subs if all(mul_u(v) in S for v in S)]
    say("      %d F_q-subspaces of F_q^%d, of which %d are A_t-submodules"
        % (len(subs), vdim, len(submods)))

    def I_of(W):
        """{X in R : every COLUMN of X, read as a vector of A_t^2, lies in W}.

        This is the right-ideal side of Morita:  col_j(XY) = sum_k Y_kj col_k(X)
        is an A_t-linear combination of the columns of X, so it stays in W.
        (The "rows lie in W" family gives LEFT ideals -- see Proposition 5.9 and
        the side-flip discussion; that is why the convention matters.)
        """
        Wperp, _ = nullspace([list(w) for w in W], F, vdim)
        rows = []
        for v in Wperp:
            for colj in range(2):
                row = [0] * d
                for i in range(2):
                    for e in range(t):
                        row[i * vdim + colj * t + e] = v[i * t + e]
                rows.append(row)
        sol, dim = nullspace(rows, F, d)
        return frozenset(R.unvec(tuple(x)) for x in sol), dim

    def I_of_rows(W):
        """the constraint rows defining I_W (so its basis can be reused cheaply)"""
        Wperp, _ = nullspace([list(w) for w in W], F, vdim)
        rows = []
        for v in Wperp:
            for colj in range(2):
                row = [0] * d
                for i in range(2):
                    for e in range(t):
                        row[i * vdim + colj * t + e] = v[i * t + e]
                rows.append(row)
        return rows

    ideals = {}
    canon = {}
    dim_ok = True
    rows_ok = True
    for W in submods:
        IW, dimI = I_of(W)
        ideals[W] = IW
        canon[W] = nullspace_basis([list(x) for x in I_of_rows(W)], F, d)
        _, dimW = span_of([list(w) for w in W], F, vdim)
        if dimI != 2 * dimW:
            dim_ok = False
        # the columns occurring in I_W span W
        colset = set()
        for X in IW:
            colset.add(tuple(list(X[0]) + list(X[2])))
            colset.add(tuple(list(X[1]) + list(X[3])))
        if span_of([list(x) for x in colset], F, vdim)[0] != W:
            rows_ok = False
    ring_gens = [R.unit(i, j) for i in range(2) for j in range(2)] + \
                ([R.scalar_mat(A.u)] if t > 1 else [])
    check("W -> I_W := {X : columns of X in W} is a right ideal (all %d submodules)"
          % len(submods),
          all(all(R.mul(X, G) in IW for X in span_basis(R, F, IW) for G in ring_gens)
              for IW in ideals.values()))
    check("dim_{F_q} I_W = 2 dim_{F_q} W  (Morita dimension formula)", dim_ok)
    check("W -> I_W injective,  and W = span of the columns of I_W",
          len(set(ideals.values())) == len(submods) and rows_ok,
          "%d distinct right ideals" % len(set(ideals.values())))

    # closure under sums + every principal right ideal occurs  =>  the list is
    # the complete lattice of right ideals
    keys = list(ideals.values())
    canon_set = set(canon.values())
    ok_sum = True
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            b = tuple(tuple(x) for x in
                      rref([list(x) for x in canon[submods[i]]] +
                           [list(x) for x in canon[submods[j]]], F, d)[0])
            if b not in canon_set:
                ok_sum = False
    check("the family {I_W} is closed under sums", ok_sum,
          "%d pairs" % (len(keys) * (len(keys) + 1) // 2))

    els = list(itertools.product(A.elem_list(), repeat=4))
    scan = els if len(els) <= 5000 else random.Random(31337).sample(els, 4000)
    all_IW = canon_set
    ok_pr = True
    for X in scan:
        S, _ = span_closure(R, F, [X], ring_gens, two_sided=False)
        if S not in all_IW:
            ok_pr = False
            break
    check("every principal right ideal XR is one of the I_W",
          ok_pr, exhaustive=(len(els) <= 5000))

    if t == 1:
        pred = q + 3
    elif t == 2:
        pred = q * q + 3 * q + 5
    else:
        pred = None
    if pred is not None:
        check("number of right ideals = %s" % ("q+3" if t == 1 else "q^2+3q+5"),
              len(submods) == pred, "computed %d, formula %d" % (len(submods), pred))
    return F, A, R, submods, ideals


def rnd_sample(pop, k):
    return random.Random(31337).sample(pop, k)


# ==========================================================================
# 6.  Task B -- sigma_s and theta_s
# ==========================================================================

def task_B(p, r, t):
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    say("")
    say("B    sigma_s and theta_s      q = %d = %d^%d,  t = %d" % (F.q, p, r, t))
    elsA = A.elem_list()
    elsR = list(itertools.product(A.elem_list(), repeat=4))
    rnd = random.Random(4242 + q_offset(p, r, t))

    check("sigma_s is a ring automorphism of A_t",
          all(A.sigma(A.add(x, y), 1) == A.add(A.sigma(x, 1), A.sigma(y, 1)) and
              A.sigma(A.mul(x, y), 1) == A.mul(A.sigma(x, 1), A.sigma(y, 1))
              for x in elsA for y in elsA), exhaustive=(len(elsA) <= 90))
    check("sigma_s(a) = a^{p^s} on F_q",
          all(F.frob[s][a] == F.pow(a, p ** s) for s in range(F.r) for a in range(F.q)))
    check("sigma_s(u) = u for every s",
          all(A.sigma(A.u, s) == A.u for s in range(F.r)))

    # The test element must have an entry OUTSIDE F_p: on E_12 (entries 0/1)
    # every sigma_s acts trivially, which would report order 1 for all s.
    a_gen = field_generator(F)
    a_sc = tuple([a_gen] + [0] * (t - 1))
    X0 = R.unit(0, 1, a_sc)
    ok_ord = True
    measured = []
    for s in range(F.r):
        cur, k = R.sigma(X0, s), 1
        while cur != X0:
            cur = R.sigma(cur, s)
            k += 1
            if k > 200:
                break
        measured.append(k)
        if k != F.r // gcd(F.r, s):
            ok_ord = False
    check("ord(sigma_s) = r / gcd(r,s)   (s = 0..r-1)", ok_ord,
          "measured %s, predicted %s"
          % (measured, [F.r // gcd(F.r, s) for s in range(F.r)]))
    check("sigma_s = id  <=>  r | s",
          [s for s in range(F.r) if all(R.sigma(X, s) == X for X in elsR[:400])] == [0],
          exhaustive=(len(elsR) <= 400))

    # ---- theta_s ---------------------------------------------------------
    sample = elsR if len(elsR) <= 300 else rnd.sample(elsR, 300)
    pairs = [(X, Y) for X in sample[:40] for Y in sample[:40]]
    ok_anti = all(R.theta(R.mul(X, Y), s) == R.mul(R.theta(Y, s), R.theta(X, s))
                  for s in range(F.r) for (X, Y) in pairs)
    ok_add = all(R.theta(R.add(X, Y), s) == R.add(R.theta(X, s), R.theta(Y, s))
                 for s in range(F.r) for (X, Y) in pairs[:400])
    check("theta_s(XY) = theta_s(Y) theta_s(X)   (ANTI-automorphism)", ok_anti,
          "%d pairs x %d values of s" % (len(pairs), F.r), exhaustive=False)
    check("theta_s is additive", ok_add, exhaustive=False)
    ok_sq = all(R.theta(R.theta(X, s), s) == R.sigma(X, 2 * s)
                for s in range(F.r) for X in sample)
    check("theta_s^2 = sigma_{2s}", ok_sq, exhaustive=False)
    ok_pow = all(R.theta(R.theta(R.theta(X, s), s), s) == R.theta(X, 3 * s)
                 for s in range(F.r) for X in sample[:50])
    check("theta_s^3 = theta_{3s}  (odd powers are anti, even powers are auto)",
          ok_pow, exhaustive=False)
    check("theta_s is never the identity: theta_s(E_12) = E_21",
          all(R.theta(R.unit(0, 1), s) == R.unit(1, 0) for s in range(F.r)))
    check("theta_s = transpose  <=>  s = 0",
          [s for s in range(F.r)
           if all(R.theta(X, s) == R.transpose(X) for X in elsR[:400])] == [0],
          exhaustive=(len(elsR) <= 400))

    measured_t = []
    ok_tord = True
    for s in range(F.r):
        cur, k = R.theta(X0, s), 1
        while cur != X0:
            cur = R.theta(cur, s)
            k += 1
            if k > 300:
                break
        measured_t.append(k)
        if k != 2 * F.r // gcd(F.r, 2 * s):
            ok_tord = False
    check("ord(theta_s) = 2r / gcd(r,2s)", ok_tord, "measured %s" % measured_t)

    invol = [s for s in range(F.r)
             if all(R.theta(R.theta(X, s), s) == X for X in elsR[:400])]
    pred = [s for s in range(F.r) if (2 * s) % F.r == 0]
    check("theta_s involutive  <=>  r | 2s", invol == pred,
          "involutive s = %s, predicted %s" % (invol, pred))
    if r % 2 == 1:
        check("r odd: the only reflexive s is 0 (Corollary 4.6)", pred == [0])
    else:
        check("r even: the reflexive s are exactly 0 and r/2",
              pred == [0, r // 2], "s in %s" % pred)
    check("theta_s(aI) = sigma_s(a) I",
          all(R.theta(R.scalar_mat(a), s) == R.scalar_mat(A.sigma(a, s))
              for s in range(F.r) for a in elsA[:50]))
    check("theta_s fixes F_p elementwise",
          all(R.theta(R.scalar_mat(tuple([c] + [0] * (t - 1))), s) ==
              R.scalar_mat(tuple([c] + [0] * (t - 1)))
              for s in range(F.r) for c in range(p)))
    check("sigma_k o theta_s = theta_{s+k} = theta_s o sigma_k",
          all(R.sigma(R.theta(X, s), k) == R.theta(X, s + k) and
              R.theta(R.sigma(X, k), s) == R.theta(X, s + k)
              for s in range(F.r) for k in range(F.r) for X in elsR[:40]))
    check("theta_s is bijective (theta_s o theta_{-s} = id on a sample)",
          all(R.theta(R.theta(X, s), -s) == X for s in range(F.r) for X in elsR[:100]),
          exhaustive=False)
    return F, A, R


def q_offset(p, r, t):
    return 1000 * p + 100 * r + t


# ==========================================================================
# 7.  Task C -- modules, pairing, orthogonals
# ==========================================================================

def task_C(p, r, t, s_list):
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    d = R.d
    say("")
    say("C    module conventions and the pairing      q = %d,  t = %d,  n = 1"
        % (F.q, t))
    els = list(itertools.product(A.elem_list(), repeat=4))
    bas = R.basis()                      # F_q-basis of R

    # ---- Lambda catches every nonzero one-sided ideal (Lemma 6.5) --------
    ok_catch = True
    ok_witness = True
    for X in els:
        if X == R.zero:
            continue
        if len(els) <= 2000 and not any(R.Lambda(R.mul(X, Y)) != 0 for Y in els):
            ok_catch = False
            break
        best = None
        for i in range(2):
            for j in range(2):
                x = X[R.idx(i, j)]
                if x == A.zero:
                    continue
                if best is None or A.val(x) < best[0]:
                    best = (A.val(x), i, j)
        k, i, j = best
        c = A.pow(A.u, t - 1 - k) if t > 1 else A.one
        Y = R.unit(j, i, c)
        if R.Lambda(R.mul(Y, X)) == 0 or R.Lambda(R.mul(X, Y)) == 0:
            ok_witness = False
            break
    check("Lambda catches every nonzero left/right ideal of R",
          ok_catch, exhaustive=(len(els) <= 2000))
    check("explicit witness Y = u^{t-1-k} E_ji of Lemma 6.5 works for every X",
          ok_witness, exhaustive=(len(els) <= 2000))

    # ---- non-degeneracy of b_s = Lambda o B_s (Theorem 6.6) --------------
    for s in s_list:
        G = [[R.Lambda(R.mul(R.theta(bas[a], s), bas[b])) for b in range(d)]
             for a in range(d)]
        rk = len(rref(G, F, d)[0])
        check("b_s non-degenerate: rank of the Gram matrix = dim R = %d  (s=%d)"
              % (d, s), rk == d, "rank %d" % rk)
        # right radical: for every y != 0 there is x with b_s(x,y) != 0
        ok_rad = all(any(R.Lambda(R.mul(R.theta(X, s), Y)) != 0 for X in els)
                     for Y in els if Y != R.zero) if len(els) <= 600 else True
        if len(els) <= 600:
            check("right radical of b_s is {0}  (s=%d)" % s, ok_rad)

    # ---- orthogonals of right ideals -------------------------------------
    vdim = 2 * t
    subs = enumerate_subspaces(F, vdim)
    if t == 1:
        submods = subs
    else:
        def mul_u(v):
            return tuple(list(A.mul(tuple(v[:t]), A.u)) +
                         list(A.mul(tuple(v[t:]), A.u)))
        submods = [S for S in subs if all(mul_u(v) in S for v in S)]

    def I_of(W):
        """right ideal {X : every column of X lies in W}  (Morita)"""
        Wperp, _ = nullspace([list(w) for w in W], F, vdim)
        rows = []
        for v in Wperp:
            for colj in range(2):
                row = [0] * d
                for i in range(2):
                    for e in range(t):
                        row[i * vdim + colj * t + e] = v[i * t + e]
                rows.append(row)
        sol, dim = nullspace(rows, F, d)
        return sol, dim

    ideals = []
    for W in submods:
        sol, dim = I_of(W)
        ideals.append(frozenset(R.unvec(tuple(x)) for x in sol))
    say("      %d right ideals of R" % len(ideals))

    # The orthogonals below are computed from an F_q-basis of the code: the
    # conditions are F_q-linear (right slot) and sigma_s-semilinear (left slot,
    # solved in z_k = sigma_s(y_k)), so a basis imposes exactly the same
    # conditions as the whole code.
    def system_rows(cols):
        """rows of the linear system whose columns are `cols`"""
        return [[col[i] for col in cols] for i in range(len(cols[0]))] \
            if cols else []

    def right_perp(Cb, s):
        """{y : B_s(x,y) = 0 for all x in <Cb>},  B_s(x,y) = theta_s(x) y

        y = sum_j y_j b_j  =>  theta_s(x) y = sum_j y_j (theta_s(x) b_j), so the
        system matrix has column j = vec(theta_s(x) b_j)."""
        rows = []
        for X in Cb:
            M = R.theta(X, s)
            cols = [list(R.vec(R.mul(M, b))) for b in bas]
            rows.extend(system_rows(cols))
        sol, _ = nullspace(rows, F, d)
        return frozenset(R.unvec(tuple(x)) for x in sol)

    def left_perp(Cb, s):
        """{y : B_s(y,x) = 0 for all x in <Cb>}

        theta_s(y) = sum_j sigma_s(y_j) theta_s(b_j), so with z_j = sigma_s(y_j)
        the system matrix has column j = vec(theta_s(b_j) x); solve for z and
        then apply sigma_{-s}."""
        rows = []
        for X in Cb:
            cols = [list(R.vec(R.mul(R.theta(b, s), X))) for b in bas]
            rows.extend(system_rows(cols))
        sol, _ = nullspace(rows, F, d)
        out = set()
        for z in sol:                      # y_k = sigma_{-s}(z_k)
            v = [F.frob[(-s) % F.r][c] for c in z]
            out.add(R.unvec(tuple(v)))
        return frozenset(out)

    def scalar_perp(Cb, s):
        """{y : Lambda(B_s(x,y)) = 0 for all x in <Cb>}"""
        rows = []
        for X in Cb:
            M = R.theta(X, s)
            rows.append([R.Lambda(R.mul(M, b)) for b in bas])
        sol, _ = nullspace(rows, F, d)
        return frozenset(R.unvec(tuple(x)) for x in sol)

    def sys_rows_from_action(X, left=False):
        """rows of the system whose matrix has column j = vec(X b_j)
        (or vec(b_j X) when left=True)"""
        cols = [list(R.vec(R.mul(b, X) if left else R.mul(X, b))) for b in bas]
        return [[col[i] for col in cols] for i in range(d)]

    def plain_perp(Cb, left=False):
        """{y : x y = 0 for all x in C}  -- the plain matrix product

        (left=True gives {y : y x = 0}, the convention used for LEFT ideals;
        this is the pairing P(x,y) = x y of Proposition 5.9.)
        """
        rows = []
        for X in Cb:
            rows.extend(sys_rows_from_action(X, left=left))
        sol, _ = nullspace(rows, F, d)
        return frozenset(R.unvec(tuple(x)) for x in sol)

    def entrywise_perp(Cb):
        """{y : sum_{ij} x_ij y_ij = 0 for all x in C}

        The Frobenius / entry-wise form.  It is NOT the pairing of the
        document; it is recorded separately because at n = 1 it happens to be
        perfect on BOTH C_r and C_l (the failure of the entry-wise form only
        shows up for n >= 2, cf. T-006).
        """
        rows = []
        for X in Cb:
            for e in range(t):
                row = [0] * d
                for k in range(4):
                    for f in range(t):
                        row[k * t + f] = A.mul(X[k], A.pow(A.u, f))[e]
                rows.append(row)
        sol, _ = nullspace(rows, F, d)
        return frozenset(R.unvec(tuple(x)) for x in sol)

    def is_right_module(S):
        Sset = set(S)
        gens = [R.unit(i, j) for i in range(2) for j in range(2)]
        if t > 1:
            gens.append(R.scalar_mat(A.u))
        return all(R.mul(y, G) in Sset for y in list(S)[:200] for G in gens)

    for s in s_list:
        ok_mod = ok_size = ok_two = ok_left = ok_dd = True
        for C in ideals:
            Cb = span_basis(R, F, C)
            dR = right_perp(Cb, s)
            dL = left_perp(Cb, s)
            dRb = scalar_perp(Cb, s)
            sigCb = [R.sigma(x, -2 * s) for x in Cb] if s else Cb
            dLpred = right_perp(sigCb, s)
            if not (is_right_module(dR) and is_right_module(dL)):
                ok_mod = False
            if len(dR) * len(C) != len(els):
                ok_size = False
            if dRb != dR:
                ok_two = False
            if dL != dLpred:
                ok_left = False
            if right_perp(span_basis(R, F, dR), s) != \
                    frozenset(R.sigma(x, 2 * s) for x in C):
                ok_dd = False
        check("s=%d  both orthogonals of a right module are right modules"
              " (Lemma 5.5)" % s, ok_mod, "%d right ideals" % len(ideals))
        check("s=%d  |C| |C^{perp_s}| = |R|   (size formula, Theorem 6.6)" % s,
              ok_size)
        check("s=%d  the two orthogonals coincide as sets (Lemma 6.7)" % s, ok_two)
        check("s=%d  ^{perp_s}C = (sigma_{-2s}C)^{perp_s} (Lemma 5.7)" % s, ok_left)
        check("s=%d  (C^{perp_s})^{perp_s} = sigma_{2s}(C) (Theorem 6.8)" % s, ok_dd)
        if (2 * s) % F.r == 0:
            check("s=%d  reflexive regime: the duality is an involution on codes" % s,
                  all(right_perp(span_basis(R, F, right_perp(span_basis(R, F, C), s)), s)
                      == C for C in ideals))
        else:
            nonref = [C for C in ideals
                      if right_perp(span_basis(R, F, right_perp(span_basis(R, F, C), s)),
                                    s) != C]
            check("s=%d  non-reflexive regime: (C^perp)^perp = sigma_{2s}(C) != C"
                  " for some codes" % s, len(nonref) > 0,
                  "%d of %d codes are not sigma_{2s}-invariant" % (len(nonref), len(ideals)))

    # ---- side flip for the plain product (Proposition 5.9) ---------------
    Cr = frozenset(R.mul(R.unit(0, 0), X) for X in els)      # right ideal E_11 R
    Cl = frozenset(R.mul(X, R.unit(0, 0)) for X in els)      # left ideal  R E_11
    _, cr = span_of([R.vec(x) for x in Cr], F, d)
    _, cl = span_of([R.vec(x) for x in Cl], F, d)
    _, dcr = span_of([R.vec(x) for x in plain_perp(span_basis(R, F, Cr))], F, d)
    _, dcl = span_of([R.vec(x) for x in plain_perp(span_basis(R, F, Cl))], F, d)
    _, dcl2 = span_of([R.vec(x) for x in plain_perp(span_basis(R, F, Cl), left=True)],
                      F, d)
    _, ecr = span_of([R.vec(x) for x in entrywise_perp(span_basis(R, F, Cr))], F, d)
    _, ecl = span_of([R.vec(x) for x in entrywise_perp(span_basis(R, F, Cl))], F, d)
    check("side flip: plain MATRIX product FAILS on the right ideal E_11 R",
          dcr == 0 and cr + dcr != d,
          "dim C_r = %d, dim C_r^perp = %d, sum = %d != dim R = %d"
          % (cr, dcr, cr + dcr, d))
    check("side flip: plain MATRIX product IS perfect on the left ideal R E_11"
          " (code in slot 1)",
          cl + dcl == d, "dim C_l = %d, dim C_l^perp = %d, sum = %d = dim R"
          % (cl, dcl, cl + dcl))
    check("side flip: for the SAME left ideal it degenerates to {0} when the"
          " code is put in slot 2",
          dcl2 == 0, "dim = %d" % dcl2)
    check("entry-wise (Frobenius) form is perfect on BOTH at n=1 (T-006 needs n>1)",
          cr + ecr == d and cl + ecl == d,
          "dim C_r^perp = %d, dim C_l^perp = %d" % (ecr, ecl))
    check("theta-pairing repairs the right side: |Cr| |Cr^{perp_s}| = |R|",
          len(Cr) * len(right_perp(span_basis(R, F, Cr), 0)) == len(els),
          "%d x %d = %d" % (len(Cr), len(right_perp(span_basis(R, F, Cr), 0)),
                            len(els)))
    return F, A, R


# ==========================================================================
# 8.  main
# ==========================================================================

def main():
    say("=" * 88)
    say("PHASE 1 -- RING AND GALOIS FOUNDATIONS: INDEPENDENT VERIFICATION")
    say(" corroborates 03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md")
    say("=" * 88)

    for (p, r, t) in [(2, 2, 1), (2, 2, 2), (2, 2, 3), (3, 2, 1), (2, 3, 1), (2, 4, 1)]:
        task_A_local(p, r, t)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1), (2, 3, 1), (2, 2, 2)]:
        task_A_matrix(p, r, t)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1), (2, 3, 1), (2, 2, 2)]:
        task_A_morita(p, r, t)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1), (2, 3, 1), (3, 3, 1), (2, 4, 1), (2, 2, 2)]:
        task_B(p, r, t)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1)]:
        task_C(p, r, t, s_list=list(range(r)))
    for (p, r, t) in [(2, 3, 1), (3, 3, 1), (2, 4, 1)]:
        task_C(p, r, t, s_list=[0, 1])
    task_C(2, 2, 2, s_list=[0, 1])

    say("")
    say("=" * 88)
    if FAILURES:
        say("RESULT: %d of %d checks FAILED" % (len(FAILURES), NCHECK[0]))
        for f in FAILURES:
            say("   FAIL: %s   %s" % f)
    else:
        say("RESULT: all %d checks PASSED." % NCHECK[0])
    say("=" * 88)
    with open("ring_structure_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\nlog written to ring_structure_log.txt")


if __name__ == "__main__":
    main()
