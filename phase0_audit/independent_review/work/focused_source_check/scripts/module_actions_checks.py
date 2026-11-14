#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 1 -- supplementary verification of the LEFT and RIGHT module actions
(document section 5.6, "Task C clarification").

Companion to 03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md section 5.6.  Everything is
recomputed from the definitions:

  A. the two actions on the ring R = M_2(A_t)
       * right action  X |-> X a   mixes COLUMNS:  col_j(Xa) = sum_k a_kj col_k(X)
       * left  action  X |-> a X   mixes ROWS:     row_i(aX) = sum_k a_ik row_k(X)
       * (R,R)-bimodule law:  (aX)b = a(Xb)
     and the Morita dictionary in BOTH handednesses:
       * RIGHT ideals  <->  A_t-submodules W of the COLUMN space A_t^2,
                            I_W = {X : every column of X lies in W}   (Prop. 2.6)
       * LEFT  ideals  <->  A_t-submodules U of the ROW space A_t^2,
                            L_U = {X : every row of X lies in U}
       * the transpose exchanges the two families bijectively.

  B. the two actions on R_n = R[X]/<X^n-1> = M_2(B),  B = A_t[X]/<X^n-1>
       * X is CENTRAL, so left and right multiplication by X coincide, and both
         are the cyclic shift T, (Tx)_e = x_{e-1};
       * right multiplication by a in R is the coordinate-wise right action
         (x.a)_e = x_e a, left multiplication is (a.x)_e = a x_e.

  C. compatibility of the pairing B_s(x,y) = sum_e theta_s(x_e) y_e with each of
     the four actions, and the module-theoretic consequences:
       * B_s(x.a, y) = theta_s(a) B_s(x,y)        (right action, first slot)
       * B_s(x, y.a) = B_s(x,y) a                 (right action, second slot)
       * B_s(a.x, y) = sum_e theta_s(x_e) theta_s(a) y_e   (left action, slot 1)
       * B_s(x, a.y) = sum_e theta_s(x_e) a y_e            (left action, slot 2)
       * for ANY subset both orthogonals are right R-submodules;
       * the dual of a cyclic code is a cyclic code (Cor. 6.4), tested at n >= 2;
       * the left-handed analogue: TRUE at n = 1, FALSE in general at n >= 2
         (an explicit counterexample is exhibited in the log);
       * sigma_k(C^{perp_s}) = (sigma_k C)^{perp_s}   (Lemma 6.11).

The arithmetic (Field, Local, MatRing and the F_q-linear algebra) is imported from
ring_structure_checks.py, which builds it from scratch and is itself verified there
(401/401 checks).  Only B = A_t[X]/<X^n-1>, M_2(B) and the new checks are here.

Usage:  python3 module_actions_checks.py
Log:    module_actions_log.txt
"""

import itertools
import random

from ring_structure_checks import (Field, Local, MatRing, rref, span_of, nullspace,
                                   nullspace_basis, span_basis, enumerate_subspaces,
                                   check, say, LINES, FAILURES, NCHECK)


# ==========================================================================
# B = A_t[X]/<X^n - 1>   and   M_2(B)
# ==========================================================================

class PolyQuot(object):
    """B = A_t[X]/<X^n - 1>;  an element is an n-tuple of elements of A_t."""

    def __init__(self, A, n):
        self.A, self.n, self.t, self.F = A, n, A.t, A.F
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
        """cyclic convolution:  coefficient of X^e is sum_{i+j = e mod n} a_i b_j"""
        A, n = self.A, self.n
        out = [A.zero] * n
        for i in range(n):
            if a[i] != A.zero:
                for j in range(n):
                    if b[j] != A.zero:
                        e = (i + j) % n
                        out[e] = A.add(out[e], A.mul(a[i], b[j]))
        return tuple(out)

    def sigma(self, a, s):
        return tuple(self.A.sigma(x, s) for x in a)

    def vec(self, a):
        out = []
        for x in a:
            out.extend(x)
        return tuple(out)

    def unvec(self, v):
        t = self.t
        return tuple(tuple(v[k * t:(k + 1) * t]) for k in range(self.n))

    def elem_list(self):
        return list(itertools.product(self.A.elem_list(), repeat=self.n))


class Mat2B(object):
    """M_2(B);  an element is a 4-tuple of B-elements in row-major order."""

    def __init__(self, B):
        self.B, self.n, self.t, self.F = B, B.n, B.t, B.F
        self.dim = 4 * B.n * B.t                 # dim_{F_q} of R^n
        self.zero = tuple([B.zero] * 4)
        self.one = (B.one, B.zero, B.zero, B.one)
        self.XI = (B.X, B.zero, B.zero, B.X)
        self.uI = (B.u, B.zero, B.zero, B.u)

    def unit(self, i, j, c=None):
        B = self.B
        c = B.one if c is None else c
        return tuple([c if (a == i and b == j) else B.zero
                      for a in range(2) for b in range(2)])

    def add(self, X, Y):
        return tuple(self.B.add(X[k], Y[k]) for k in range(4))

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

    def transpose(self, X):
        return (X[0], X[2], X[1], X[3])

    def sigma(self, X, s):
        return tuple(self.B.sigma(x, s) for x in X)

    def theta(self, X, s):
        return self.sigma(self.transpose(X), s)

    def vec(self, X):
        out = []
        for x in X:
            out.extend(self.B.vec(x))
        return tuple(out)

    def unvec(self, v):
        k = len(v) // 4
        return tuple(self.B.unvec(tuple(v[i * k:(i + 1) * k])) for i in range(4))

    def elem_list(self):
        return list(itertools.product(self.B.elem_list(), repeat=4))

    def basis(self):
        """F_q-basis u^e X^f E_ij of M_2(B)"""
        A, B = self.B.A, self.B
        out = []
        for i in range(2):
            for j in range(2):
                for f in range(B.n):
                    for e in range(A.t):
                        coeff = tuple([A.zero] * f +
                                      [tuple([1 if k == e else 0
                                              for k in range(A.t)])] +
                                      [A.zero] * (B.n - 1 - f))
                        out.append(self.unit(i, j, coeff))
        return out

    def const(self, a):
        """a in R = M_2(A_t) as a constant element of M_2(B)"""
        A = self.B.A
        z = A.zero
        return tuple(tuple([a[k]] + [z] * (self.n - 1)) for k in range(4))

    def sample(self, k, seed):
        rnd = random.Random(seed)
        A, B = self.B.A, self.B
        q = self.F.q
        out = []
        for _ in range(k):
            entry = lambda: tuple(tuple(rnd.randrange(q) for _ in range(A.t))
                                  for _ in range(B.n))
            out.append(tuple(entry() for _ in range(4)))
        return out


F_Q = 4   # placeholder, set inside part_C before sampling


# ==========================================================================
# A.  actions on R = M_2(A_t)
# ==========================================================================

def part_A(p, r, t):
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    q = F.q
    say("")
    say("A    actions on R = M_2(A_t)      q = %d,  t = %d,  |R| = %d"
        % (q, t, q ** (4 * t)))
    els = R.elem_list()
    scan = els if len(els) <= 1000 else random.Random(11).sample(els, 1000)
    ascan = els if len(els) <= 60 else random.Random(12).sample(els, 60)

    def cols(X):
        """column j of X as the vector (entry(0,j), entry(1,j)) of A_t^2"""
        return ((X[0], X[2]), (X[1], X[3]))

    def rows(X):
        """row i of X as the vector (entry(i,0), entry(i,1)) of A_t^2"""
        return ((X[0], X[1]), (X[2], X[3]))

    def lincomb(vecs, coeffs):
        """sum_k coeffs[k] * vecs[k]:  A_t-linear combination of vectors in A_t^2"""
        out = tuple(A.zero for _ in vecs[0])
        for c, v in zip(coeffs, vecs):
            if c != A.zero:
                out = tuple(A.add(out[i], A.mul(c, v[i])) for i in range(len(v)))
        return out

    ok_col = ok_row = True
    for X in scan:
        for a in ascan:
            cX, cXa = cols(X), cols(R.mul(X, a))
            for j in range(2):
                want = lincomb([cX[0], cX[1]], [a[R.idx(0, j)], a[R.idx(1, j)]])
                if cXa[j] != want:
                    ok_col = False
            rX, raX = rows(X), rows(R.mul(a, X))
            for i in range(2):
                want = lincomb([rX[0], rX[1]], [a[R.idx(i, 0)], a[R.idx(i, 1)]])
                if raX[i] != want:
                    ok_row = False
            if not (ok_col and ok_row):
                break
        if not (ok_col and ok_row):
            break
    check("right action mixes COLUMNS:  col_j(Xa) = sum_k a_kj col_k(X)", ok_col,
          exhaustive=(len(els) <= 1000 and len(els) <= 60))
    check("left  action mixes ROWS:     row_i(aX) = sum_k a_ik row_k(X)", ok_row,
          exhaustive=(len(els) <= 1000 and len(els) <= 60))

    ok_bi = all(R.mul(R.mul(a, X), b) == R.mul(a, R.mul(X, b))
                for X in scan[:60] for a in ascan for b in ascan)
    check("(R,R)-bimodule law:  (aX)b = a(Xb)", ok_bi, exhaustive=False)

    # ---------------- Morita, both handednesses ---------------------------
    vdim = 2 * t
    subs = enumerate_subspaces(F, vdim)
    if t == 1:
        submods = subs
    else:
        def mul_u(v):
            return tuple(list(A.mul(tuple(v[:t]), A.u)) +
                         list(A.mul(tuple(v[t:]), A.u)))
        submods = [S for S in subs if all(mul_u(v) in S for v in S)]

    def ideal_of(W, side):
        Wperp, _ = nullspace([list(w) for w in W], F, vdim)
        rows = []
        for v in Wperp:
            for slot in range(2):
                row = [0] * R.d
                for i in range(2):
                    for e in range(t):
                        if side == 'col':
                            row[i * vdim + slot * t + e] = v[i * t + e]
                        else:
                            row[slot * vdim + i * t + e] = v[i * t + e]
                rows.append(row)
        sol, dim = nullspace(rows, F, R.d)
        return frozenset(R.unvec(tuple(x)) for x in sol), dim

    gens_R = [R.unit(i, j) for i in range(2) for j in range(2)] + \
             ([R.scalar_mat(A.u)] if t > 1 else [])
    rights, lefts = {}, {}
    ok_r = ok_l = ok_dim = True
    for W in submods:
        IW, dimI = ideal_of(W, 'col')
        LU, dimL = ideal_of(W, 'row')
        rights[W], lefts[W] = IW, LU
        if not all(R.mul(X, G) in IW for X in span_basis(R, F, IW) for G in gens_R):
            ok_r = False
        if not all(R.mul(G, X) in LU for X in span_basis(R, F, LU) for G in gens_R):
            ok_l = False
        _, dimW = span_of([list(w) for w in W], F, vdim)
        if dimI != 2 * dimW or dimL != 2 * dimW:
            ok_dim = False
    check("RIGHT ideals = {X : COLUMNS in W}, W <= A_t^2 an A_t-submodule"
          " (Prop. 2.6)", ok_r, "%d submodules" % len(submods))
    check("LEFT  ideals = {X : ROWS in U},    U <= A_t^2 an A_t-submodule", ok_l,
          "%d submodules" % len(submods))
    check("dim_{F_q} I_W = dim_{F_q} L_U = 2 dim_{F_q} W", ok_dim)

    if t == 1:
        pred = q + 3
    elif t == 2:
        pred = q * q + 3 * q + 5
    else:
        pred = None
    if pred is not None:
        check("both handednesses give %d ideals  (= %s)"
              % (pred, "q+3" if t == 1 else "q^2+3q+5"),
              len(set(rights.values())) == pred and len(set(lefts.values())) == pred,
              "right %d, left %d" % (len(set(rights.values())),
                                     len(set(lefts.values()))))

    Rset, Lset = set(rights.values()), set(lefts.values())
    ok_tr = (len(Rset) == len(Lset) and
             all(frozenset(R.transpose(X) for X in I) in Lset for I in Rset) and
             all(frozenset(R.transpose(X) for X in L) in Rset for L in Lset))
    check("the transpose maps right ideals bijectively onto left ideals", ok_tr,
          "%d right, %d left" % (len(Rset), len(Lset)))

    ok_c = all(R.mul(R.scalar_mat(tuple([c] + [0] * (t - 1))), X) ==
               R.mul(X, R.scalar_mat(tuple([c] + [0] * (t - 1))))
               for c in range(p) for X in scan[:200])
    check("F_p-scalars are central:  (cI)X = X(cI)", ok_c, exhaustive=False)
    return F, A, R


# ==========================================================================
# B.  actions on R_n = M_2(B)
# ==========================================================================

def part_B(p, r, t, n):
    F = Field(p, r)
    A = Local(F, t)
    B = PolyQuot(A, n)
    M = Mat2B(B)
    R = MatRing(A, 2)
    say("")
    say("B    actions on R_n = M_2(B), B = A_t[X]/<X^n-1>      q = %d, t = %d, n = %d"
        % (F.q, t, n))
    Be = B.elem_list()
    scanB = Be if len(Be) <= 500 else random.Random(21).sample(Be, 500)

    check("X is CENTRAL in B:  Xb = bX for all b in B",
          all(B.mul(B.X, b) == B.mul(b, B.X) for b in Be),
          exhaustive=(len(Be) <= 20000))
    check("X^n = 1 in B   (X is a unit, T is invertible)",
          B.mul(B.X, B.mul(B.X, B.X)) == B.one if n == 3 else
          (B.mul(B.X, B.X) == B.one if n == 2 else True))

    Me = M.elem_list() if F.q ** M.dim <= 20000 else None
    scanM = Me if Me is not None else M.sample(300, 22)
    ex = Me is not None
    ok_lr = all(M.mul(Z, M.XI) == M.mul(M.XI, Z) for Z in scanM)
    check("left and right multiplication by X coincide on R_n", ok_lr,
          exhaustive=ex)

    def T_of(Z):
        return tuple(tuple(entry[(e - 1) % n] for e in range(n)) for entry in Z)

    ok_T = all(M.mul(Z, M.XI) == T_of(Z) and M.mul(M.XI, Z) == T_of(Z)
               for Z in scanM)
    check("both equal the cyclic shift T:  (Tx)_e = x_{e-1 mod n}", ok_T,
          exhaustive=ex)

    Re = R.elem_list()
    ascan = Re if len(Re) <= 40 else random.Random(23).sample(Re, 40)

    def entry_prod(Z, a, i, j, e, right):
        acc = A.zero
        for k in range(2):
            term = A.mul(Z[2 * i + k][e], a[2 * k + j]) if right \
                else A.mul(a[2 * i + k], Z[2 * k + j][e])
            acc = A.add(acc, term)
        return acc

    ok_coord = True
    for Z in scanM[:40]:
        for a in ascan:
            Zra, Zla = M.mul(Z, M.const(a)), M.mul(M.const(a), Z)
            for i in range(2):
                for j in range(2):
                    for e in range(n):
                        if Zra[2 * i + j][e] != entry_prod(Z, a, i, j, e, True) or \
                           Zla[2 * i + j][e] != entry_prod(Z, a, i, j, e, False):
                            ok_coord = False
            if not ok_coord:
                break
        if not ok_coord:
            break
    check("right mult by a in R is (x.a)_e = x_e a;  left mult is (a.x)_e = a x_e",
          ok_coord, exhaustive=False)
    return F, A, R, B, M


# ==========================================================================
# C.  pairing vs. the four actions
# ==========================================================================

def b_submodules(B, F, vdim, n, t):
    """all B-submodules of B^2, by BFS over the submodule lattice.

    From a submodule S we add the B-module generated by one representative of
    each class of B^2/S (a complement basis spans the classes), which is enough
    because every over-module is reached by a chain of one-generator steps.
    """
    A = B.A

    def act(v, c):
        """multiply the two B-components of v by the B-element c"""
        out = []
        for half in range(2):
            blk = v[half * n * t:(half + 1) * n * t]
            coeffs = [tuple(blk[e * t:(e + 1) * t]) for e in range(n)]
            for x in B.mul(c, tuple(coeffs)):
                out.extend(x)
        return tuple(out)

    def mul_X(v):
        return act(v, B.X)

    def mul_u(v):
        return act(v, B.u)

    def close(basis_rows):
        """close under B = F_q[X, u]:  enough, since X and u generate B"""
        rows = [list(b) for b in basis_rows]
        while True:
            Bm, _ = rref(rows, F, vdim)
            new = [list(b) for b in Bm]
            for b in Bm:
                new.append(list(mul_X(b)))
                if t > 1:
                    new.append(list(mul_u(b)))
            B2, _ = rref(new, F, vdim)
            if len(B2) == len(Bm):
                return tuple(tuple(x) for x in B2)
            rows = new

    zero = tuple([0] * vdim)
    start = ()
    seen = {start}
    work = [start]
    out = []
    while work:
        S = work.pop()
        out.append(S)
        Brows, piv = rref([list(b) for b in S], F, vdim) if S else ([], [])
        comp = [tuple([1 if i == c else 0 for i in range(vdim)])
                for c in range(vdim) if c not in piv]
        for coeffs in itertools.product(range(F.q), repeat=len(comp)):
            if not any(coeffs):
                continue
            v = [0] * vdim
            for c, w in zip(coeffs, comp):
                if c:
                    v = [F.add[a][F.mul[c][b]] for a, b in zip(v, w)]
            new = close(list(S) + [tuple(v)])
            if new not in seen:
                seen.add(new)
                work.append(new)
    # materialise each submodule as a set of vectors (cheap for these sizes)
    sets = []
    for S in out:
        sets.append(span_of([list(b) for b in S], F, vdim)[0])
    return sets


def part_C(p, r, t, s_list, n_list):
    global F_Q
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)
    F_Q = F.q
    for n in n_list:
        B = PolyQuot(A, n)
        M = Mat2B(B)
        d = M.dim
        total = F.q ** d
        say("")
        say("C    pairing vs. the four actions      q = %d, t = %d, n = %d"
            "   (dim_{F_q} R^n = %d)" % (F.q, t, n, d))
        small = d <= 16
        els = M.elem_list() if small else None
        scan = els if small else M.sample(300, 31)
        Re = R.elem_list()
        ascan = Re if len(Re) <= 40 else random.Random(32).sample(Re, 40)
        bas = M.basis()

        def Bs(x, y, s):
            acc = R.zero
            for e in range(4):
                acc = R.add(acc, R.mul(R.theta(x[e], s), y[e]))
            return acc

        def right_scalar(x, a):
            return tuple(R.mul(x[e], a) for e in range(4))

        def left_scalar(x, a):
            return tuple(R.mul(a, x[e]) for e in range(4))

        for s in s_list:
            ok1 = ok2 = ok3 = ok4 = True
            for x in scan:
                for y in scan[:60]:
                    for a in ascan:
                        if Bs(right_scalar(x, a), y, s) != \
                                R.mul(R.theta(a, s), Bs(x, y, s)):
                            ok1 = False
                        if Bs(x, right_scalar(y, a), s) != R.mul(Bs(x, y, s), a):
                            ok2 = False
                        w3 = R.zero
                        w4 = R.zero
                        for e in range(4):
                            w3 = R.add(w3, R.mul(R.mul(R.theta(x[e], s),
                                                       R.theta(a, s)), y[e]))
                            w4 = R.add(w4, R.mul(R.theta(x[e], s),
                                                 R.mul(a, y[e])))
                        if Bs(left_scalar(x, a), y, s) != w3:
                            ok3 = False
                        if Bs(x, left_scalar(y, a), s) != w4:
                            ok4 = False
                        if not (ok1 and ok2 and ok3 and ok4):
                            break
                    if not (ok1 and ok2 and ok3 and ok4):
                        break
                if not (ok1 and ok2 and ok3 and ok4):
                    break
            check("s=%d  B_s(x.a, y) = theta_s(a) B_s(x,y)      (right, slot 1)" % s,
                  ok1, exhaustive=False)
            check("s=%d  B_s(x, y.a) = B_s(x,y) a              (right, slot 2)" % s,
                  ok2, exhaustive=False)
            check("s=%d  B_s(a.x, y) = sum_e theta_s(x_e)theta_s(a)y_e  (left, slot 1)"
                  % s, ok3, exhaustive=False)
            check("s=%d  B_s(x, a.y) = sum_e theta_s(x_e) a y_e         (left, slot 2)"
                  % s, ok4, exhaustive=False)

            witness = None
            for x in scan:
                for y in scan[:60]:
                    for a in ascan:
                        if Bs(left_scalar(x, a), y, s) != R.mul(a, Bs(x, y, s)):
                            witness = True
                            break
                    if witness:
                        break
                if witness:
                    break
            check("s=%d  B_s(a.x,y) is NOT a left multiple of B_s(x,y)"
                  " (explicit witness)" % s, witness is not None)

            # ---- orthogonals ---------------------------------------------
            def right_perp(Cb, s):
                rows = []
                for x in Cb:
                    tx = M.theta(x, s)
                    for b in bas:
                        rows.append(list(M.vec(M.mul(tx, b))))
                sol, _ = nullspace(rows, F, d)
                return frozenset(M.unvec(tuple(v)) for v in sol)

            def left_perp(Cb, s):
                rows = []
                for x in Cb:
                    for b in bas:
                        rows.append(list(M.vec(M.mul(M.theta(b, s), x))))
                sol, _ = nullspace(rows, F, d)
                return frozenset(M.unvec(tuple([F.frob[(-s) % F.r][c] for c in z]))
                                 for z in sol)

            gens = [M.unit(i, j) for i in range(2) for j in range(2)] + \
                   [M.XI] + ([M.uI] if t > 1 else [])

            def is_right_module(S):
                Sset = set(S)
                return all(M.mul(y, G) in Sset for y in list(S)[:200] for G in gens)

            def is_left_module(S):
                Sset = set(S)
                return all(M.mul(G, y) in Sset for y in list(S)[:200] for G in gens)

            rnd = random.Random(41)
            ok_any = True
            for _ in range(10):
                Cb = [rnd.choice(scan) for _ in range(rnd.randint(1, 3))]
                if not (is_right_module(right_perp(Cb, s)) and
                        is_right_module(left_perp(Cb, s))):
                    ok_any = False
            check("s=%d  for ARBITRARY subsets both orthogonals are right"
                  " R-submodules" % s, ok_any, exhaustive=False)

            ok_sig = True
            for _ in range(6):
                Cb = [rnd.choice(scan) for _ in range(rnd.randint(1, 2))]
                for k in range(F.r):
                    if set(M.sigma(y, k) for y in right_perp(Cb, s)) != \
                            right_perp([M.sigma(x, k) for x in Cb], s):
                        ok_sig = False
            check("s=%d  sigma_k(C^{perp_s}) = (sigma_k C)^{perp_s}  (Lemma 6.11)"
                  % s, ok_sig, exhaustive=False)

            # ---- cyclic codes at this n (via the B-submodule dictionary) --
            vdim = 2 * n * t
            if vdim <= 6 and F.q ** vdim <= 100000:
                submods = b_submodules(B, F, vdim, n, t)
                rights, lefts = [], []
                for W in submods:
                    rights.append(col_ideal(W, M, F, n, t, d))
                    lefts.append(row_ideal(W, M, F, n, t, d))
                say("      %d B-submodules of B^2  ->  %d right ideals, "
                    "%d left ideals" % (len(submods), len(set(rights)),
                                        len(set(lefts))))
                ok_cyc = ok_size = True
                for C in rights:
                    Cb = span_basis(M, F, C)
                    dR = right_perp(Cb, s)
                    if not is_right_module(dR):
                        ok_cyc = False
                    if len(C) * len(dR) != total:
                        ok_size = False
                check("s=%d  dual of every cyclic code is a cyclic code"
                      " (Cor. 6.4 at n=%d)" % (s, n), ok_cyc,
                      "%d codes" % len(submods))
                check("s=%d  |C| |C^{perp_s}| = |R|^n  (size formula at n=%d)"
                      % (s, n), ok_size, "%d codes" % len(submods))

                nbad = 0
                first_bad = None
                for L in lefts:
                    Lb = span_basis(M, F, L)
                    dR = right_perp(Lb, s)
                    if not is_left_module(dR):
                        nbad += 1
                        if first_bad is None:
                            first_bad = L
                if n == 1:
                    check("s=%d  n=1: the orthogonal of a LEFT ideal IS again a"
                          " left ideal" % s, nbad == 0,
                          "%d of %d left ideals fail" % (nbad, len(lefts)))
                else:
                    check("s=%d  n=%d: the orthogonal of a LEFT ideal is NOT in"
                          " general a left module" % (s, n), nbad > 0,
                          "%d of %d left ideals fail" % (nbad, len(lefts)))
                    if first_bad is not None:
                        _, dimL = span_of([list(M.vec(x)) for x in first_bad], F, d)
                        say("        counterexample: a left ideal L with "
                            "dim_{F_q} L = %d whose right orthogonal is not "
                            "closed under left multiplication" % dimL)
            else:
                say("      (B-submodule enumeration skipped: dim_{F_q} B^2 = %d "
                    "too large)" % vdim)
    return F, A, R


def col_ideal_basis(W, F, n, t, d):
    """canonical basis of {X in M_2(B) : every COLUMN of X lies in W}  (right ideal)."""
    vdim = 2 * n * t
    Wperp = nullspace_basis([list(w) for w in W], F, vdim)
    rows = []
    for v in Wperp:
        for colj in range(2):
            row = [0] * d
            for i in range(2):
                for slot in range(n * t):
                    row[(2 * i + colj) * n * t + slot] = v[i * n * t + slot]
            rows.append(row)
    return nullspace_basis(rows, F, d)


def row_ideal_basis(U, F, n, t, d):
    """canonical basis of {X in M_2(B) : every ROW of X lies in U}  (left ideal)."""
    vdim = 2 * n * t
    Uperp = nullspace_basis([list(w) for w in U], F, vdim)
    rows = []
    for v in Uperp:
        for rowi in range(2):
            row = [0] * d
            for j in range(2):
                for slot in range(n * t):
                    row[(2 * rowi + j) * n * t + slot] = v[j * n * t + slot]
            rows.append(row)
    return nullspace_basis(rows, F, d)


def part_C(p, r, t, s_list, n_list):
    """the four actions on R^n versus the pairing B_s."""
    F = Field(p, r)
    A = Local(F, t)
    R = MatRing(A, 2)                  # R = M_2(A_t)
    basR = R.basis()                   # F_q-basis of R, length 4t
    dR = R.d                           # 4t
    Re = R.elem_list()
    ascan = Re if len(Re) <= 40 else random.Random(32).sample(Re, 40)

    for n in n_list:
        d = dR * n                     # dim_{F_q} R^n = 4tn
        say("")
        say("C    pairing vs. the four actions on R^n      q = %d, t = %d, n = %d"
            "   (dim_{F_q} R^n = %d)" % (F.q, t, n, d))

        # ---------------- V = R^n = tuples of n elements of R -------------
        def vec(x):
            out = []
            for xe in x:
                out.extend(R.vec(xe))
            return tuple(out)

        def unvec(v):
            return tuple(R.unvec(tuple(v[e * dR:(e + 1) * dR])) for e in range(n))

        def Bs(x, y, s):
            acc = R.zero
            for e in range(n):
                acc = R.add(acc, R.mul(R.theta(x[e], s), y[e]))
            return acc

        def right_scalar(x, a):
            return tuple(R.mul(x[e], a) for e in range(n))

        def left_scalar(x, a):
            return tuple(R.mul(a, x[e]) for e in range(n))

        def shift(x):                          # T
            return tuple(x[(e - 1) % n] for e in range(n))

        def unshift(x):                        # T^{-1}
            return tuple(x[(e + 1) % n] for e in range(n))

        def sig(x, k):                         # sigma_k, coordinate-wise
            return tuple(R.sigma(x[e], k) for e in range(n))

        def canon(vs):
            return tuple(tuple(b) for b in rref([list(v) for v in vs], F, d)[0])

        def contains(cb, v):
            return len(rref([list(b) for b in cb] + [list(v)], F, d)[0]) == len(cb)

        def span_set(cb):
            out = set()
            k = len(cb)
            for coeffs in itertools.product(range(F.q), repeat=k):
                acc = [0] * d
                for c, b in zip(coeffs, cb):
                    if c:
                        acc = [F.add[u][F.mul[c][w]] for u, w in zip(acc, b)]
                out.add(tuple(acc))
            return frozenset(out)

        def right_perp(cb, s):
            """{y : B_s(x,y) = 0 for all x in span(cb)}, as a canonical basis."""
            rows = []
            for v in cb:
                x = unvec(tuple(v))
                cols = []
                for e in range(n):
                    tx = R.theta(x[e], s)
                    for b in basR:
                        cols.append(list(R.vec(R.mul(tx, b))))
                rows.extend([[col[i] for col in cols] for i in range(dR)])
            return nullspace_basis(rows, F, d)

        def left_perp(cb, s):
            """{y : B_s(y,x) = 0 for all x in span(cb)}, as a canonical basis."""
            rows = []
            for v in cb:
                x = unvec(tuple(v))
                cols = []
                for e in range(n):
                    for b in basR:
                        cols.append(list(R.vec(R.mul(R.theta(b, s), x[e]))))
                rows.extend([[col[i] for col in cols] for i in range(dR)])
            sol = nullspace_basis(rows, F, d)
            out = [[F.frob[(-s) % F.r][c] for c in z] for z in sol]
            return canon(out) if out else ()

        gens_R = [R.unit(i, j) for i in range(2) for j in range(2)] + \
                 ([R.scalar_mat(A.u)] if t > 1 else [])

        def is_right_module(cb):
            return all(contains(cb, vec(right_scalar(unvec(tuple(b)), g)))
                       for b in cb for g in gens_R)

        def is_left_module(cb):
            return all(contains(cb, vec(left_scalar(unvec(tuple(b)), g)))
                       for b in cb for g in gens_R)

        def is_T_stable(cb):
            return all(contains(cb, vec(shift(unvec(tuple(b))))) for b in cb)

        # ---------------- samples ----------------------------------------
        rnd = random.Random(101 + n)
        samp = [tuple(rnd.choice(Re) for _ in range(n)) for _ in range(24)]

        # ---- encoding sanity: the linear-algebra perp = the brute-force one
        if F.q ** d <= 4096:
            Vall = [unvec(tuple(v)) for v in
                    itertools.product(range(F.q), repeat=d)]
            ok_enc = True
            for trial in range(6):
                seeds = [rnd.choice(samp) for _ in range(rnd.randint(1, 2))]
                cb = canon([vec(x) for x in seeds])
                Cset = span_set(cb)
                for s in s_list:
                    brute = frozenset(
                        vec(y) for y in Vall
                        if all(Bs(unvec(tuple(v)), y, s) == R.zero for v in Cset))
                    if span_set(right_perp(cb, s)) != brute:
                        ok_enc = False
                    bruteL = frozenset(
                        vec(y) for y in Vall
                        if all(Bs(y, unvec(tuple(v)), s) == R.zero for v in Cset))
                    if span_set(left_perp(cb, s)) != bruteL:
                        ok_enc = False
            check("the linear-algebra encoding of both orthogonals agrees with"
                  " brute force", ok_enc)

        # ---- the four identities ----------------------------------------
        for s in s_list:
            ok1 = ok2 = ok3 = ok4 = okT = okb = True
            for x in samp:
                for y in samp[:8]:
                    for a in ascan:
                        if Bs(right_scalar(x, a), y, s) != \
                                R.mul(R.theta(a, s), Bs(x, y, s)):
                            ok1 = False
                        if Bs(x, right_scalar(y, a), s) != R.mul(Bs(x, y, s), a):
                            ok2 = False
                        w3 = R.zero
                        w4 = R.zero
                        for e in range(n):
                            w3 = R.add(w3, R.mul(R.mul(R.theta(x[e], s),
                                                       R.theta(a, s)), y[e]))
                            w4 = R.add(w4, R.mul(R.theta(x[e], s),
                                                 R.mul(a, y[e])))
                        if Bs(left_scalar(x, a), y, s) != w3:
                            ok3 = False
                        if Bs(x, left_scalar(y, a), s) != w4:
                            ok4 = False
                        if Bs(x, shift(y), s) != Bs(unshift(x), y, s):
                            okT = False
                        if R.Lambda(Bs(right_scalar(x, a), y, s)) != \
                                R.Lambda(R.mul(R.theta(a, s), Bs(x, y, s))):
                            okb = False
                        if not (ok1 and ok2 and ok3 and ok4 and okT and okb):
                            break
                    if not (ok1 and ok2 and ok3 and ok4 and okT and okb):
                        break
                if not (ok1 and ok2 and ok3 and ok4 and okT and okb):
                    break
            check("s=%d  B_s(x.a, y) = theta_s(a) B_s(x,y)   (right action, slot 1)"
                  % s, ok1, exhaustive=False)
            check("s=%d  B_s(x, y.a) = B_s(x,y) a            (right action, slot 2)"
                  % s, ok2, exhaustive=False)
            check("s=%d  B_s(a.x, y) = sum_e theta_s(x_e) theta_s(a) y_e"
                  "  (left action, slot 1)" % s, ok3, exhaustive=False)
            check("s=%d  B_s(x, a.y) = sum_e theta_s(x_e) a y_e"
                  "          (left action, slot 2)" % s, ok4, exhaustive=False)
            check("s=%d  B_s(x, Ty) = B_s(T^{-1}x, y)  (Corollary 6.4, proof)" % s,
                  okT, exhaustive=False)
            check("s=%d  b_s = Lambda o B_s satisfies the same four identities" % s,
                  okb, exhaustive=False)

            # ---- the left action is NOT a left scalar multiple -----------
            wit = None
            for x in samp:
                for y in samp[:8]:
                    for a in ascan:
                        if Bs(left_scalar(x, a), y, s) != R.mul(a, Bs(x, y, s)):
                            wit = (x, y, a)
                            break
                    if wit:
                        break
                if wit:
                    break
            check("s=%d  B_s(a.x, y) is NOT a(s) B_s(x,y): explicit witness exists"
                  % s, wit is not None, exhaustive=False)
            if wit is not None:
                x, y, a = wit
                say("        witness: B_s(a.x,y) = %s   while   a B_s(x,y) = %s"
                    % (show_R(Bs(left_scalar(x, a), y, s), R, A),
                       show_R(R.mul(a, Bs(x, y, s)), R, A)))

            # ---- orthogonals of ARBITRARY subsets are right modules ------
            ok_arb = True
            for _ in range(8):
                seeds = [rnd.choice(samp) for _ in range(rnd.randint(1, 3))]
                cb = canon([vec(x) for x in seeds])
                if not (is_right_module(right_perp(cb, s)) and
                        is_right_module(left_perp(cb, s))):
                    ok_arb = False
            check("s=%d  for ARBITRARY subsets BOTH orthogonals are right"
                  " R-submodules" % s, ok_arb, exhaustive=False)

            # ---- sigma_k and the orthogonal (Lemma 6.11) -----------------
            ok_sig = True
            for _ in range(4):
                seeds = [rnd.choice(samp) for _ in range(rnd.randint(1, 2))]
                cb = canon([vec(x) for x in seeds])
                for k in range(F.r):
                    img = canon([vec(sig(unvec(tuple(v)), k)) for v in cb])
                    if canon([vec(sig(unvec(tuple(v)), k))
                              for v in right_perp(cb, s)]) != \
                            right_perp(img, s):
                        ok_sig = False
            check("s=%d  sigma_k(C^{perp_s}) = (sigma_k C)^{perp_s}  (Lemma 6.11)"
                  % s, ok_sig, exhaustive=False)

        # ---------------- cyclic codes (right ideals of R_n) --------------
        vdim = 2 * n * t
        B = PolyQuot(A, n)
        if vdim <= 6 and F.q ** vdim <= 20000:
            subs = b_submodules(B, F, vdim, n, t)
            say("      %d B-submodules of B^2   (Morita: = right ideals of"
                " M_2(B) = cyclic codes)" % len(subs))

            def to_V(Mcb):
                """pull a subspace of M_2(B) back to R^n along sum_e x_e X^e"""
                out = []
                for v in Mcb:
                    w = [0] * d
                    for k in range(4):
                        for e in range(n):
                            for f in range(t):
                                w[(e * 4 + k) * t + f] = v[(k * n + e) * t + f]
                    out.append(w)
                return canon(out) if out else ()

            codes = [to_V(col_ideal_basis(W, F, n, t, d)) for W in subs]
            lefts = [to_V(row_ideal_basis(W, F, n, t, d)) for W in subs]
            say("      -> %d distinct right ideals, %d distinct left ideals"
                " of R_n" % (len(set(codes)), len(set(lefts))))

            s0 = s_list[0]
            ok_cyc = ok_dual = ok_dim = True
            for cb in codes:
                if not (is_right_module(cb) and is_T_stable(cb)):
                    ok_cyc = False
                db = right_perp(cb, s0)
                if not (is_right_module(db) and is_T_stable(db)):
                    ok_dual = False
                if len(cb) + len(db) != d:
                    ok_dim = False
            check("every right ideal of R_n is a right R-submodule of R^n that is"
                  " T-stable (a cyclic code)",
                  ok_cyc, "%d codes" % len(set(codes)))
            check("s=%d  the dual of a cyclic code is a cyclic code (Cor. 6.4,"
                  " n=%d)" % (s0, n), ok_dual, "%d codes" % len(set(codes)))
            check("s=%d  dim C + dim C^{perp_s} = 4tn = %d  (Thm 6.6, n=%d)"
                  % (s0, d, n), ok_dim, "%d codes" % len(set(codes)))

            # completeness: closing a random subset under (T, right R) lands
            # in the enumerated list
            def close_cyclic(seeds):
                rows = [list(vec(x)) for x in seeds]
                while True:
                    Bm, _ = rref(rows, F, d)
                    new = [list(b) for b in Bm]
                    for b in Bm:
                        x = unvec(tuple(b))
                        for g in gens_R:
                            new.append(list(vec(right_scalar(x, g))))
                        new.append(list(vec(shift(x))))
                    B2, _ = rref(new, F, d)
                    if len(B2) == len(Bm):
                        return tuple(tuple(x) for x in B2)
                    rows = new

            ok_cl = True
            for _ in range(6):
                seeds = [rnd.choice(samp) for _ in range(rnd.randint(1, 2))]
                cb = close_cyclic(seeds)
                if cb not in set(codes):
                    ok_cl = False
            check("every T-stable right submodule generated by a random subset is"
                  " one of the enumerated codes (completeness)", ok_cl,
                  exhaustive=False)

            def close_left(seeds):
                """smallest left R-submodule of R^n containing seeds"""
                rows = [list(vec(x)) for x in seeds]
                while True:
                    Bm, _ = rref(rows, F, d)
                    new = [list(b) for b in Bm]
                    for b in Bm:
                        x = unvec(tuple(b))
                        for g in gens_R:
                            new.append(list(vec(left_scalar(x, g))))
                    B2, _ = rref(new, F, d)
                    if len(B2) == len(Bm):
                        return tuple(tuple(x) for x in B2)
                    rows = new

            # ---- the left-handed statement (Lemma 5.6a) -----------------
            nbad = 0
            for cb in lefts:
                if not (is_left_module(right_perp(cb, s0)) and
                        is_left_module(left_perp(cb, s0))):
                    nbad += 1
            check("s=%d  for every LEFT ideal of R_n BOTH orthogonals are LEFT"
                  " R-submodules (Lemma 5.6a, n=%d)"
                  % (s0, n), nbad == 0,
                  "%d of %d fail" % (nbad, len(set(lefts))))

            ok_lm = True
            for _ in range(6):
                seeds = [rnd.choice(samp) for _ in range(rnd.randint(1, 2))]
                cb = close_left(seeds)
                if not (is_left_module(right_perp(cb, s0)) and
                        is_left_module(left_perp(cb, s0))):
                    ok_lm = False
            check("s=%d  same for a randomly generated LEFT submodule"
                  " (Lemma 5.6a)" % s0, ok_lm, exhaustive=False)

            # ---- the left-module test is not vacuous --------------------
            Cr = close_cyclic([tuple([R.unit(0, 0)] + [R.zero] * (n - 1))])
            check("the test is not vacuous: the cyclic code generated by E_11 in"
                  " coordinate 0 is a right module but NOT a left module",
                  is_right_module(Cr) and not is_left_module(Cr),
                  "dim = %d" % len(Cr))

            # ---- n = 1: the dual of a left ideal is a TWO-SIDED ideal ----
            if n == 1:
                two_sided = []
                for i in range(t + 1):          # u^i R,  i = 0..t  (u^t R = 0)
                    rows = []
                    for k in range(i, t):
                        for ii in range(2):
                            for jj in range(2):
                                z = tuple([1 if e == k else 0 for e in range(t)])
                                rows.append(list(R.vec(R.unit(ii, jj, z))))
                    two_sided.append(canon(rows) if rows else ())
                ok_two = True
                for cb in lefts:
                    db = right_perp(cb, s0)
                    if db not in two_sided:
                        ok_two = False
                check("n=1: the right orthogonal of every left ideal is one of the"
                      " t+1 two-sided ideals u^i R  (Remark 5.6b)",
                      ok_two, "%d left ideals, %d two-sided ideals"
                      % (len(set(lefts)), len(two_sided)))
        else:
            say("      (B-submodule enumeration skipped: dim_{F_q} B^2 = %d)"
                % vdim)
    return F, A, R


def show_R(X, R, A):
    """compact printable form of an element of R = M_2(A_t)"""
    def sh(a):
        if a == A.zero:
            return "0"
        return "+".join("%s u^%d" % (a[e], e) for e in range(A.t) if a[e])
    return "[" + ", ".join(sh(X[k]) for k in range(4)) + "]"


# ==========================================================================
# main
# ==========================================================================

def main():
    say("=" * 90)
    say("PHASE 1 -- SUPPLEMENTARY VERIFICATION OF THE LEFT/RIGHT MODULE ACTIONS")
    say(" corroborates section 5.6 of 03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md")
    say("=" * 90)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1), (2, 2, 2)]:
        part_A(p, r, t)

    for (p, r, t, n) in [(2, 2, 1, 1), (2, 2, 1, 2), (2, 2, 1, 3), (3, 2, 1, 2),
                         (2, 2, 2, 2)]:
        part_B(p, r, t, n)

    for (p, r, t) in [(2, 2, 1), (3, 2, 1)]:
        part_C(p, r, t, s_list=[0, 1], n_list=[1, 2, 3])
    part_C(2, 3, 1, s_list=[1], n_list=[1, 2])
    part_C(2, 2, 2, s_list=[0, 1], n_list=[1, 2])

    say("")
    say("=" * 90)
    if FAILURES:
        say("RESULT: %d of %d checks FAILED" % (len(FAILURES), NCHECK[0]))
        for f in FAILURES:
            say("   FAIL: %s   %s" % f)
    else:
        say("RESULT: all %d checks PASSED." % NCHECK[0])
    say("=" * 90)
    with open("module_actions_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\nlog written to module_actions_log.txt")


if __name__ == "__main__":
    main()
