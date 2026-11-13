#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INDEPENDENT AUDIT CHECKS (Phase 0 independent self-audit).

This script deliberately does NOT import matrix_ring_lib.py.  Finite fields,
ring arithmetic, linear algebra, code enumeration and all pairing/duality
computations are re-implemented from scratch here, so that the earlier results
are tested by an independent code path.

Coverage
  A. sigma_s / theta_s  (exhaustive where affordable)
  B. Lambda and pairing non-degeneracy (Gram rank, own Gaussian elimination)
  C. independent code enumeration (4 different methods, no Morita/CRT counting)
  D. all duality/hull/reflexivity properties on the independent code lists
  E. sharp a-priori predictions and their verification
  F. the squarefree hypothesis of the enumeration formula (counterexample)

Run:  python3 -u independent_audit_checks.py
Log:  independent_audit_log.txt
"""
import itertools
import random
import time

LINES = []
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    LINES.append(str(s))


# --------------------------------------------------------------------------
# finite field F_{p^r}, built from scratch (search order: descending, i.e.
# different from the one used in matrix_ring_lib.py)
# --------------------------------------------------------------------------
class Field(object):
    def __init__(self, p, r):
        self.p, self.r, self.q = p, r, p ** r

        def digits(x):
            return [(x // p ** i) % p for i in range(r)]

        def val(d):
            return sum(d[i] * p ** i for i in range(r))

        def pmul(a, b):
            out = [0] * (2 * r - 1) if r > 1 else [0]
            for i in range(r):
                if a[i]:
                    for j in range(r):
                        out[i + j] = (out[i + j] + a[i] * b[j]) % p
            return out

        def pmod(a, g):                      # a mod g (monic, degree r)
            a = list(a) + [0] * (2 * r)
            for i in range(len(a) - 1, r - 1, -1):
                if a[i]:
                    c = a[i]
                    for j in range(r + 1):
                        a[i - r + j] = (a[i - r + j] - c * g[j]) % p
            return a[:r]

        irr = None
        for lead in range(p ** r - 1, 0, -1):        # descending search
            g = digits(lead) + [1]                   # monic of degree r
            ok = True
            # trial division by all monic polys of degree <= r//2
            for d in range(1, r // 2 + 1):
                    for c in range(p ** d):
                        h = digits(c) + [1]
                        if len(h) < d + 1:
                            h = h + [0] * (d + 1 - len(h))
                        h = h[:d + 1]
                        # divide g by h
                        rem = list(g) + [0] * (2 * r)
                        for i in range(r, d - 1, -1):
                            if rem[i]:
                                c2 = rem[i]
                                for j in range(d + 1):
                                    rem[i - d + j] = (rem[i - d + j] - c2 * h[j]) % p
                        if all(x == 0 for x in rem[:d]):
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                irr = g
                break
        if irr is None:
            raise RuntimeError("no irreducible found")
        self.irr = irr
        q = self.q
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        self.neg = [0] * q
        for a in range(q):
            da = digits(a)
            self.neg[a] = val([(-x) % p for x in da])
            for b in range(q):
                db = digits(b)
                self.add[a][b] = val([(da[i] + db[i]) % p for i in range(r)])
                self.mul[a][b] = val(pmod(pmul(da, db), irr))
        self.zero, self.one = 0, 1
        self.frob = []
        for s in range(r):
            tab = [0] * q
            for a in range(q):
                x = a
                for _ in range(p ** s):
                    x = self.mul[x][a] if False else x
                # a^(p^s) by repeated multiplication
                res, base, e = 1, a, p ** s
                while e:
                    if e & 1:
                        res = self.mul[res][base]
                    base = self.mul[base][base]
                    e >>= 1
                tab[a] = res
            self.frob.append(tab)
        self.inv = [0] * q
        for a in range(1, q):
            for b in range(1, q):
                if self.mul[a][b] == 1:
                    self.inv[a] = b
                    break

    def frob_k(self, a, s):
        return self.frob[s % self.r][a]

    def pow(self, a, e):
        res, base = 1, a
        while e:
            if e & 1:
                res = self.mul[res][base]
            base = self.mul[base][base]
            e >>= 1
        return res


# --------------------------------------------------------------------------
# linear algebra over F_q (own implementation)
# --------------------------------------------------------------------------
def rref(F, rows, ncols):
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
        inv = F.inv[M[row][col]]
        M[row] = [F.mul[inv][x] for x in M[row]]
        for i in range(len(M)):
            if i != row and M[i][col]:
                c = M[i][col]
                M[i] = [F.add[M[i][j]][F.neg[F.mul[c][M[row][j]]]] for j in range(ncols)]
        piv.append(col)
        row += 1
        if row == len(M):
            break
    out = [tuple(r) for r in M[:row]]
    return out, piv


def nullspace(F, rows, ncols):
    R, piv = rref(F, rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, pc in enumerate(piv):
            v[pc] = F.neg[R[i][f]]
        basis.append(tuple(v))
    return basis


def in_span(F, R, piv, v, ncols):
    w = list(v)
    for i, pc in enumerate(piv):
        c = w[pc]
        if c:
            for j in range(ncols):
                w[j] = F.add[w[j]][F.neg[F.mul[c][R[i][j]]]]
    return all(x == 0 for x in w)


def rank(F, rows, ncols):
    R, piv = rref(F, rows, ncols)
    return len(piv)


# --------------------------------------------------------------------------
# A_t = F_q[u]/<u^t>   and   R = M_m(A_t)
# element of A_t : tuple of t field elements
# matrix         : flat tuple of m*m elements of A_t  (index i*m+j)
# --------------------------------------------------------------------------
class Local(object):
    def __init__(self, F, t):
        self.F, self.t = F, t
        self.zero = tuple([0] * t)
        self.one = (1,) + tuple([0] * (t - 1))

    def add(self, a, b):
        F = self.F
        return tuple(F.add[a[i]][b[i]] for i in range(self.t))

    def neg(self, a):
        return tuple(self.F.neg[x] for x in a)

    def mul(self, a, b):
        F = self.F
        t = self.t
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
        F = self.F
        return tuple(F.frob[s % F.r][x] for x in a)


class MatRing(object):
    def __init__(self, A, m):
        self.A, self.m, self.t, self.F = A, m, A.t, A.F
        self.d = m * m * A.t                       # dim over F_q
        z = A.zero
        self.zero = tuple([z] * (m * m))
        one = A.one
        self.one = tuple([one if (i == j) else z for i in range(m) for j in range(m)])

    def idx(self, i, j):
        return i * self.m + j

    def add(self, X, Y):
        A = self.A
        return tuple(A.add(X[k], Y[k]) for k in range(self.m * self.m))

    def neg(self, X):
        return tuple(self.A.neg(x) for x in X)

    def mul(self, X, Y):
        A = self.A
        m = self.m
        out = []
        for i in range(m):
            for j in range(m):
                acc = A.zero
                for k in range(m):
                    if X[self.idx(i, k)] != A.zero and Y[self.idx(k, j)] != A.zero:
                        acc = A.add(acc, A.mul(X[self.idx(i, k)], Y[self.idx(k, j)]))
                out.append(acc)
        return tuple(out)

    def transpose(self, X):
        m = self.m
        return tuple(X[self.idx(j, i)] for i in range(m) for j in range(m))

    def sigma(self, X, s):
        return tuple(self.A.sigma(x, s) for x in X)

    def theta(self, X, s):
        return self.sigma(self.transpose(X), s)

    def trace(self, X):
        A = self.A
        acc = A.zero
        for i in range(self.m):
            acc = A.add(acc, X[self.idx(i, i)])
        return acc

    def Lambda(self, X):
        return self.trace(X)[self.t - 1]

    def unit(self, i, j, c=None):
        A = self.A
        z = A.zero
        c = A.one if c is None else c
        return tuple([c if (self.idx(a, b) == self.idx(i, j)) else z
                      for a in range(self.m) for b in range(self.m)])

    def vec(self, X):
        out = []
        for k in range(self.m * self.m):
            out.extend(X[k])
        return tuple(out)

    def unvec(self, v):
        t = self.t
        return tuple(tuple(v[k * t + l] for l in range(t)) for k in range(self.m * self.m))


# --------------------------------------------------------------------------
# R^n and the theta-pairing
# --------------------------------------------------------------------------
class Ambient(object):
    def __init__(self, R, n):
        self.R, self.n = R, n
        self.d = R.d
        self.N = n * R.d

    def coords(self, x):
        v = []
        for X in x:
            v.extend(self.R.vec(X))
        return tuple(v)

    def uncoords(self, v):
        R = self.R
        return tuple(R.unvec(tuple(v[i * R.d:(i + 1) * R.d])) for i in range(self.n))

    def pair_theta(self, x, y, s):
        R = self.R
        acc = R.zero
        for i in range(self.n):
            acc = R.add(acc, R.mul(R.theta(x[i], s), y[i]))
        return acc

    def pair_plain(self, x, y):
        R = self.R
        acc = R.zero
        for i in range(self.n):
            acc = R.add(acc, R.mul(x[i], y[i]))
        return acc

    def dual(self, gens, s, plain=False):
        """F_q-basis of {y : <x,y>_s = 0 for all x in gens} (own elimination)."""
        F, R, N, d = self.R.F, self.R, self.N, self.R.d
        basis = [self.uncoords(tuple(1 if i == j else 0 for i in range(N)))
                 for j in range(N)]
        rows = []
        for x in gens:
            vals = [self.pair_plain(x, e) if plain else self.pair_theta(x, e, s)
                    for e in basis]
            vecs = [R.vec(v) for v in vals]
            for k in range(d):
                rows.append(tuple(vecs[j][k] for j in range(N)))
        return nullspace(F, rows, N)

    def hull(self, gens, s):
        """gens: F_q-coordinate vectors.  Returns span(C) cap C^{perp_s}."""
        F, N = self.R.F, self.N
        Cb, _ = rref(F, list(gens), N)
        if not Cb:
            return []
        D = self.dual([self.uncoords(v) for v in gens], s)
        Db, _ = rref(F, list(D), N) if D else ([], [])
        if not Db:
            return []
        E = nullspace(F, list(Db), N)          # dot-functionals killing span(D)
        M = []
        for l in E:
            row = []
            for c in Cb:
                acc = 0
                for j in range(N):
                    if l[j] and c[j]:
                        acc = F.add[acc][F.mul[l[j]][c[j]]]
                row.append(acc)
            M.append(tuple(row))
        ker = nullspace(F, M, len(Cb))
        return [tuple(sum2(F, [scal(F, a, ci) for a, ci in zip(k, Cb)], N))
                for k in ker]


def sum2(F, vs, N):
    out = [0] * N
    for v in vs:
        for j in range(N):
            out[j] = F.add[out[j]][v[j]]
    return out


def scal(F, c, v):
    return tuple(F.mul[c][x] for x in v)


# --------------------------------------------------------------------------
say("=" * 78)
say("INDEPENDENT AUDIT CHECKS  (standalone implementation, no matrix_ring_lib)")
say("run: %s   python: %d.%d" % (time.strftime("%Y-%m-%d %H:%M:%S"),
                                 __import__("sys").version_info[0],
                                 __import__("sys").version_info[1]))
say("=" * 78)

PRED = []        # (label, predicted, observed)

# ==========================================================================
say("")
say("=" * 78)
say("A.  sigma_s and theta_s")
say("=" * 78)
for (p, r) in [(2, 2), (2, 3), (3, 2)]:
    F = Field(p, r)
    A = Local(F, 1)
    R = MatRing(A, 2)
    # enumerate all matrices (q^4 of them)
    mats = []
    for vals in itertools.product(range(F.q), repeat=4):
        mats.append(tuple((v,) for v in vals))
    say("")
    say("q = %d (p=%d, r=%d): |M_2(F_q)| = %d" % (F.q, p, r, len(mats)))
    for s in range(1, r):
        ok_add = ok_mul = True
        # additivity / multiplicativity of sigma_s : exhaustive for q<=9
        if len(mats) ** 2 <= 70000:
            for X in mats:
                for Y in mats:
                    if R.sigma(R.add(X, Y), s) != R.add(R.sigma(X, s), R.sigma(Y, s)):
                        ok_add = False
                    if R.sigma(R.mul(X, Y), s) != R.mul(R.sigma(X, s), R.sigma(Y, s)):
                        ok_mul = False
            lab = "EXHAUSTIVE over all %d^2 pairs" % len(mats)
        else:
            rnd = random.Random(7)
            for _ in range(4000):
                X = rnd.choice(mats)
                Y = rnd.choice(mats)
                if R.sigma(R.add(X, Y), s) != R.add(R.sigma(X, s), R.sigma(Y, s)):
                    ok_add = False
                if R.sigma(R.mul(X, Y), s) != R.mul(R.sigma(X, s), R.sigma(Y, s)):
                    ok_mul = False
            lab = "4000 random pairs (sampled)"
        wit = next((X for X in mats if R.sigma(X, s) != X), None)
        say("   sigma_%d : additive=%s multiplicative=%s  [%s]" % (s, ok_add, ok_mul, lab))
        say("              nontrivial=%s  witness %s -> %s"
            % (wit is not None, wit, R.sigma(wit, s) if wit else None))
        # theta anti-multiplicativity
        ok_anti = True
        if len(mats) ** 2 <= 70000:
            for X in mats:
                for Y in mats:
                    if R.theta(R.mul(X, Y), s) != R.mul(R.theta(Y, s), R.theta(X, s)):
                        ok_anti = False
            lab2 = "EXHAUSTIVE over all %d^2 pairs" % len(mats)
        else:
            rnd = random.Random(11)
            for _ in range(4000):
                X = rnd.choice(mats)
                Y = rnd.choice(mats)
                if R.theta(R.mul(X, Y), s) != R.mul(R.theta(Y, s), R.theta(X, s)):
                    ok_anti = False
            lab2 = "4000 random pairs (sampled)"
        # theta^2 = sigma_{2s}
        ok_sq = all(R.theta(R.theta(X, s), s) == R.sigma(X, 2 * s) for X in mats)
        ok2 = all(R.sigma(X, 2 * s) == X for X in mats)
        say("   theta_%d : anti-multiplicative=%s  [%s]" % (s, ok_anti, lab2))
        say("              theta^2 = sigma_{2s} on all %d elements: %s ; "
            "sigma_{2s}=id (r|2s): %s" % (len(mats), ok_sq, ok2))

# ==========================================================================
say("")
say("=" * 78)
say("B.  Lambda and pairing non-degeneracy (Gram rank, own elimination)")
say("=" * 78)
for (p, r, t) in [(2, 2, 1), (2, 3, 1), (3, 2, 1), (2, 2, 2)]:
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    amb0 = Ambient(R, 1)
    bas = []
    for k in range(R.d):
        v = [0] * R.d
        v[k] = 1
        bas.append(R.unvec(tuple(v)))
    G = [[R.Lambda(R.mul(a, b)) for b in bas] for a in bas]
    rk = rank(F, G, R.d)
    say("   q=%d t=%d m=2 : Gram rank of (X,Y)->Lambda(XY) = %d / %d"
        % (F.q, t, rk, R.d))
    for n in (1, 2, 3):
        if R.d * n > 24:
            continue
        amb = Ambient(R, n)
        N = amb.N
        basis = [amb.uncoords(tuple(1 if i == j else 0 for i in range(N)))
                 for j in range(N)]
        for s in range(1, r):
            G2 = []
            for x in basis:
                row = []
                for y in basis:
                    row.append(R.Lambda(amb.pair_theta(x, y, s)))
                G2.append(tuple(row))
            rk2 = rank(F, G2, N)
            say("      n=%d s=%d : Gram rank of Lambda(<x,y>_s) = %d / %d  "
                "(non-degenerate: %s)" % (n, s, rk2, N, rk2 == N))

# ==========================================================================
say("")
say("=" * 78)
say("C.  INDEPENDENT enumeration of the cyclic codes")
say("=" * 78)


def enumerate_subspaces_rref(F, dim):
    """all subspaces of F_q^dim, by canonical RREF (independent of Morita)."""
    out = {0: [tuple()], dim: [tuple(tuple(1 if i == j else 0 for j in range(dim))
                                     for i in range(dim))]}
    for k in range(1, dim):
        forms = []
        for piv in itertools.combinations(range(dim), k):
            free = [c for c in range(dim) if c not in piv]
            # rows: row a has pivot piv[a], free entries at columns > piv[a] not in piv
            slots = []
            for a in range(k):
                for c in free:
                    if c > piv[a]:
                        slots.append((a, c))
            for fill in itertools.product(range(F.q), repeat=len(slots)):
                M = [[0] * dim for _ in range(k)]
                for (a, c), v in zip(slots, fill):
                    M[a][c] = v
                for a in range(k):
                    M[a][piv[a]] = 1
                forms.append(tuple(tuple(row) for row in M))
        out[k] = forms
    return out


def right_ideals_by_bruteforce(F, m, t):
    """right ideals of M_m(A_t) found by enumerating ALL F_q-subspaces of the
    ambient vector space and testing closure under right multiplication by the
    matrix units.  No Morita, no CRT."""
    A = Local(F, t)
    R = MatRing(A, m)
    dim = R.d
    subs = enumerate_subspaces_rref(F, dim)
    ideals = []
    units = [R.unit(i, j) for i in range(m) for j in range(m)]
    total = 0
    for k in sorted(subs):
        for S in subs[k]:
            total += 1
            Rb, piv = rref(F, list(S), dim)
            good = all(in_span(F, Rb, piv, R.vec(R.mul(R.unvec(b), u)), dim)
                       for b in S for u in units)
            if good:
                ideals.append((k, Rb))
    return R, ideals, total


say("")
say("-- C1: right ideals of M_2(F_q), found by brute-force subspace filtering --")
say("   (prediction from Morita: q + 3  =  1 + (q+1) + 1)")
for (p, r) in [(2, 1), (2, 2), (2, 3), (3, 2)]:
    F = Field(p, r)
    R, ideals, total = right_ideals_by_bruteforce(F, 2, 1)
    cnt = len(ideals)
    PRED.append(("q=%d: #right ideals of M_2(F_q)" % F.q, F.q + 3, cnt))
    dims = {}
    for k, _ in ideals:
        dims[k] = dims.get(k, 0) + 1
    say("   q=%2d : %d subspaces scanned, %d right ideals (predicted %d) %s ; "
        "dims %s" % (F.q, total, cnt, F.q + 3, "OK" if cnt == F.q + 3 else "MISMATCH",
                     sorted(dims.items())))

say("")
say("-- C2: t = 2, submodules of A^2 over A = F_q[u]/<u^2> (brute force) --")
F4 = Field(2, 2)
A2 = Local(F4, 2)
# A^2 as an F_q-space of dimension 2t = 4 ; submodule = subspace closed under u
subs = enumerate_subspaces_rref(F4, 4)
cnt2 = 0
dims2 = {}
for k in sorted(subs):
    for S in subs[k]:
        Rb, piv = rref(F4, list(S), 4)
        ok = True
        for b in S:
            x = A2.unvec(b) if False else (tuple(b[0:2]), tuple(b[2:4]))
            ux = tuple(A2.mul((0, 1), c) for c in x)
            v = tuple(ux[0]) + tuple(ux[1])
            if not in_span(F4, Rb, piv, v, 4):
                ok = False
                break
        if ok:
            cnt2 += 1
            dims2[k] = dims2.get(k, 0) + 1
say("   q=4 t=2 m=2 : %d A-submodules of A^2 (dims %s)" % (cnt2, sorted(dims2.items())))
PRED.append(("q=4,t=2: #A-submodules of A^2 (= #right ideals of M_2(A))", 33, cnt2))


# ---- B = F_q[X]/<X^n-1> (cyclic convolution) -----------------------------
class Quotient(object):
    def __init__(self, F, n):
        self.F, self.n = F, n
        self.zero = tuple([0] * n)
        self.one = (1,) + tuple([0] * (n - 1))

    def add(self, a, b):
        F = self.F
        return tuple(F.add[a[i]][b[i]] for i in range(self.n))

    def mul(self, a, b):
        F = self.F
        n = self.n
        out = [0] * n
        for i in range(n):
            if a[i]:
                for j in range(n):
                    if b[j]:
                        k = (i + j) % n
                        out[k] = F.add[out[k]][F.mul[a[i]][b[j]]]
        return tuple(out)

    def elements(self):
        return itertools.product(range(self.F.q), repeat=self.n)

    def vec(self, a):
        return tuple(a)


def enumerate_submodules(B):
    """all B-submodules of B^2, by BFS over cyclic submodules + sums.
    Independent of the Gaussian-binomial counting formula."""
    F, n = B.F, B.n
    dim = 2 * n                     # dim of B^2 over F_q
    be = list(B.elements())
    seen = {}
    for v in itertools.product(be, repeat=2):
        gens = [tuple(B.mul(b, v[i]) for i in range(2)) for b in be]
        rows = [tuple(g[0]) + tuple(g[1]) for g in gens]
        Rb, _ = rref(F, rows, dim)
        seen[tuple(sorted(Rb))] = Rb
    changed = True
    while changed:
        changed = False
        cur = list(seen.values())
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                Rb, _ = rref(F, list(cur[i]) + list(cur[j]), dim)
                k = tuple(sorted(Rb))
                if k not in seen:
                    seen[k] = Rb
                    changed = True
    return list(seen.values()), dim


# ==========================================================================
say("")
say("-- C3: q=2, n=3 -- DIRECT SCAN of all |R^n| = 4096 vectors --")
F2 = Field(2, 1)
A_2 = Local(F2, 1)
R2 = MatRing(A_2, 2)
amb2 = Ambient(R2, 3)
N2 = amb2.N
units2 = [R2.unit(i, j) for i in range(2) for j in range(2)]
seen = {}
for bits in itertools.product(range(2), repeat=N2):
    if not any(bits):
        continue
    v = tuple(bits)
    # right ideal generated by v: closure under shift and right multiplication
    gens = [v]
    changed = True
    while changed:
        changed = False
        Rb, piv = rref(F2, gens, N2)
        for g in Rb:
            x = amb2.uncoords(g)
            # shift
            sh = tuple([x[-1]] + list(x[:-1]))
            cand = amb2.coords(sh)
            if not in_span(F2, Rb, piv, cand, N2):
                gens.append(cand)
                changed = True
            for u in units2:
                y = tuple(R2.mul(x[i], u) for i in range(3))
                cand = amb2.coords(y)
                if not in_span(F2, Rb, piv, cand, N2):
                    gens.append(cand)
                    changed = True
        if changed:
            Rb, piv = rref(F2, gens, N2)
    Rb, piv = rref(F2, gens, N2)
    seen[tuple(sorted(Rb))] = Rb
codes35 = [tuple()] + list(seen.values())
say("   #cyclic codes (right ideals) found by direct scan : %d" % len(codes35))
PRED.append(("q=2,n=3: #cyclic codes (direct scan)", 35, len(codes35)))

# ==========================================================================
say("")
say("-- C4/C5/C6: B-submodules of B^2, B = F_q[X]/<X^n-1> (BFS, no counting formula) --")
for (p, r, n, expect, note) in [(2, 2, 3, 343, "squarefree (gcd(n,p)=1)"),
                                (3, 2, 2, 144, "squarefree (gcd(n,p)=1)"),
                                (2, 2, 2, None, "NOT squarefree: X^2-1=(X+1)^2")]:
    F = Field(p, r)
    B = Quotient(F, n)
    submods, dim = enumerate_submodules(B)
    cnt = len(submods)
    if expect is not None:
        PRED.append(("q=%d,n=%d: #B-submodules of B^2" % (F.q, n), expect, cnt))
        say("   q=%d n=%d : %d submodules (predicted %d) %s   [%s]"
            % (F.q, n, cnt, expect, "OK" if cnt == expect else "MISMATCH", note))
    else:
        naive = (1 + (F.q + 1) + 1) ** 2
        say("   q=%d n=%d : %d submodules   [%s]" % (F.q, n, cnt, note))
        say("      naive 'product of subspace counts' formula would give %d  ->  "
            "the squarefree hypothesis is ESSENTIAL (%d != %d)" % (naive, cnt, naive))
        PRED.append(("q=4,n=2: #B-submodules (non-squarefree)", 33, cnt))

# ==========================================================================
say("")
say("=" * 78)
say("D.  duality / hull / reflexivity on the independently enumerated codes")
say("=" * 78)


def check_list(F, R, amb, codes, s, label, plain_also=True):
    """codes: list of F_q-coordinate bases (as produced by the enumerations)."""
    N = amb.N

    def dualc(L):
        return amb.dual([amb.uncoords(v) for v in L], s)

    def dualc_plain(L):
        return amb.dual([amb.uncoords(v) for v in L], s, plain=True)

    def hullc(L):
        return amb.hull(L, s)          # hull takes coordinate vectors

    units = [R.unit(i, j) for i in range(R.m) for j in range(R.m)]
    cnt = dict(right=0, size=0, dualright=0, hullright=0, dd=0, refl=0,
               plain_size=0, total=len(codes))
    for C in codes:
        Cc, pivc = rref(F, list(C), N) if C else ([], [])

        def memc(v):
            if not Cc:
                return not any(v)
            return in_span(F, Cc, pivc, v, N)
        if all(memc(amb.coords(tuple(R.mul(amb.uncoords(x)[i], u)
                                     for i in range(amb.n))))
               for x in C for u in units):
            cnt["right"] += 1
        D = dualc(C)
        Dc, pivd = rref(F, list(D), N) if D else ([], [])

        def memd(v):
            if not Dc:
                return not any(v)
            return in_span(F, Dc, pivd, v, N)
        if all(memd(amb.coords(tuple(R.mul(amb.uncoords(y)[i], u)
                                     for i in range(amb.n))))
               for y in D for u in units):
            cnt["dualright"] += 1
        if len(C) + len(D) == N:
            cnt["size"] += 1
        DD = dualc(D) if D else \
            [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
        DDr, pivdd = rref(F, list(DD), N) if DD else ([], [])
        Csig = rref(F, [amb.coords(tuple(R.sigma(amb.uncoords(x)[i], 2 * s)
                                         for i in range(amb.n))) for x in C], N)[0] if C else []
        if tuple(sorted(DDr)) == tuple(sorted(Csig)):
            cnt["dd"] += 1
        Ccan = tuple(sorted(rref(F, list(C), N)[0])) if C else tuple()
        DDcan = tuple(sorted(DDr)) if DDr else tuple()
        if Ccan == DDcan:
            cnt["refl"] += 1
        H = hullc(C)
        Hc, pivh = rref(F, list(H), N) if H else ([], [])

        def memh(v):
            if not Hc:
                return not any(v)
            return in_span(F, Hc, pivh, v, N)
        if all(memh(amb.coords(tuple(R.mul(amb.uncoords(z)[i], u)
                                     for i in range(amb.n))))
               for z in H for u in units):
            cnt["hullright"] += 1
        if plain_also:
            P = dualc_plain(C)
            if len(C) + len(P) == N:
                cnt["plain_size"] += 1
    say("   %s" % label)
    say("      codes %d | right module %d | size formula %d | dual right %d | "
        "hull right %d" % (cnt["total"], cnt["right"], cnt["size"],
                           cnt["dualright"], cnt["hullright"]))
    say("      double dual = sigma_{2s}(C) : %d/%d" % (cnt["dd"], cnt["total"]))
    say("      REFLEXIVE (C^perp)^perp = C : %d/%d" % (cnt["refl"], cnt["total"]))
    if plain_also:
        say("      plain product size formula : %d/%d" % (cnt["plain_size"], cnt["total"]))
    return cnt


say("")
say("-- D1: n = 1, codes from the brute-force enumeration (C1) --")
say("   prediction: #reflexive = 2 + (p^g + 1) with g = gcd(r, 2s)")
for (p, r) in [(2, 2), (2, 3), (3, 2)]:
    F = Field(p, r)
    R, ideals, _ = right_ideals_by_bruteforce(F, 2, 1)
    amb = Ambient(R, 1)
    codes = [b for (k, b) in ideals]
    for s in range(1, r):
        if (2 * s) % r == 0:                       # sigma_{2s} = id
            pred = len(codes)
        else:
            g = __import__("math").gcd(r, 2 * s)   # fixed field F_{p^g}
            pred = 2 + (p ** g + 1)                # 0, lines over F_{p^g}, all
        cnt = check_list(F, R, amb, codes, s,
                         "q=%d, n=1, s=%d : %d codes" % (F.q, s, len(codes)))
        PRED.append(("q=%d,n=1,s=%d: #reflexive" % (F.q, s), pred, cnt["refl"]))

say("")
say("-- D2: t = 2 (q=4), codes from C2 --")
F4b = Field(2, 2)
A4b = Local(F4b, 2)
Rt2 = MatRing(A4b, 2)
ambt2 = Ambient(Rt2, 1)
# rebuild the 32 codes as right ideals of M_2(A) from the A-submodules of A^2
subs = enumerate_subspaces_rref(F4b, 4)
codes_t2 = []
for k in sorted(subs):
    for S in subs[k]:
        Rb, piv = rref(F4b, list(S), 4)
        ok = True
        for b in S:
            x = (tuple(b[0:2]), tuple(b[2:4]))
            ux = tuple(A4b.mul((0, 1), c) for c in x)
            v = tuple(ux[0]) + tuple(ux[1])
            if not in_span(F4b, Rb, piv, v, 4):
                ok = False
                break
        if not ok:
            continue
        gens = []
        for w in Rb:
            for j in range(2):
                vv = [0] * Rt2.d
                for i in range(2):
                    for l in range(2):
                        # MatRing.vec order: index = (i*m+j)*t + l
                        vv[(i * 2 + j) * 2 + l] = w[i * 2 + l]
                gens.append(tuple(vv))
        codes_t2.append(rref(F4b, gens, Rt2.d)[0] if gens else [])
cnt_t2 = check_list(F4b, Rt2, ambt2, codes_t2, 1,
                    "q=4, t=2, n=1, s=1 : %d codes" % len(codes_t2))
PRED.append(("q=4,t=2,n=1: #reflexive (= all, r|2s)", len(codes_t2), cnt_t2["refl"]))

say("")
say("-- D3: q=2, n=3, s=0 (validation only; sigma_0 = id) --")
cnt35 = check_list(F2, R2, amb2, codes35, 0,
                   "q=2, n=3, s=0 : %d codes (direct scan)" % len(codes35))

# ==========================================================================
say("")
say("=" * 78)
say("E.  predictions vs observations")
say("=" * 78)
allok = True
for lab, pred, obs in PRED:
    ok = (pred == obs)
    allok = allok and ok
    say("   %-55s predicted %-8s observed %-8s %s"
        % (lab, pred, obs, "OK" if ok else "*** MISMATCH ***"))
say("")
say("   ALL PREDICTIONS CONFIRMED: %s" % allok)
say("")
say("   [elapsed %.1f s]" % (time.time() - T0))
with open("independent_audit_log.txt", "w") as fh:
    fh.write("\n".join(LINES) + "\n")
say("   log written to independent_audit_log.txt")
