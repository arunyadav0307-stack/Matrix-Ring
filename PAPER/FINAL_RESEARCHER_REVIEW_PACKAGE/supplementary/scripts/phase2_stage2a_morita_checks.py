#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 2 -- STAGE 2A: MORITA CORRESPONDENCE AND GENERATOR NUMBERS
================================================================

Companion script for `03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md`.

Scope (Stage 2A only -- see the document, section 0):

  Task A  the Morita correspondence between right ideals of S = M_2(B) and
          B-submodules W of P = B^2 (columns), the left-ideal and two-sided
          variants, and the dictionary with the Stage-1 cyclic-code
          representation;
  Task B  the generator-number identity  mu_S(I_W) = ceil(mu_B(W)/2)  via
          L-2.3a (set equality), L-2.3b (counting), L-2.3c (realisability);
  Task C  the individual principality criterion
          I_W principal <=> mu_B(W) <= 2;
  Task D  computational verification of all of the above.

NOT in this script: CRT/Hensel (P-2.4), the global principality claim
(P-2.6), the wild-case classification, duals/annihilators (P-2.7/P-2.8),
hulls, Gray maps, quantum constructions, C-2.1, manuscript.

Conventions fixed in section 1 of the companion document
--------------------------------------------------------
  * P = B^2 is a RIGHT B-module; its elements are COLUMNS (v_1, v_2)^T.
  * S = M_2(B) acts on P by LEFT multiplication on columns, so
    S = End_B(P_B) with the USUAL matrix product; a right ideal I of S is
    closed under M |-> MN (N acts first).
  * For a B-submodule W of P:  I_W = {M in S : im M subset W}
    = {M in S : both columns of M lie in W}.
  * For a right ideal I of S:  W(I) = sum_{M in I} im M.
  * mu_B(W), mu_S(I) are minimal numbers of generators, mu(0) = 0.

Everything below is computed from these definitions.  In particular:

  * `SMat.principal(x)` computes span_{F_q}{x N : N in S} by multiplying x
    against the F_q-basis {E_jl b} of S -- it does NOT use the (true, but
    not-yet-assumed) description of xS by the image of x.
  * minimal generator numbers are computed by THREE independent methods
    (lattice BFS over sums of cyclics/principals; brute-force scan over
    k-tuples; Nakayama on the semisimple quotient) and the three are
    cross-checked against each other before any of them is compared with
    ceil(mu_B(W)/2).

Log: phase2_stage2a_morita_log.txt   (written to the CURRENT directory).
Run: cd 04_COMPUTATION && python3 phase2_stage2a_morita_checks.py

Only `Field`, `Local`, `MatRing`, `rref`, `say`, `check`, `LINES`,
`FAILURES`, `NCHECK` are imported from the Phase-1 library
`ring_structure_checks.py` (reused read-only); the ring
B = A_t[X]/<X^n-1> and every module/ideal routine below is built here.
"""

import os
import sys
import time
import itertools
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ring_structure_checks import (Field, Local, MatRing, rref,
                                   say, check, LINES, FAILURES, NCHECK)

SEED = 20261105          # all sampling is deterministic
T0 = time.time()

# budgets (reported in the log; changing one changes the log)
EXH_S = 70000            # exhaustive over S when |S| <= this
EXH_IDEALSCAN = 60000    # exhaustive x-scan inside I for mu_S = 1 when |I| <= this
EXH_PAIRS_MU = 128       # exhaustive pair scan for "W is 2-generated" when |W| <= this
EXH_PAIRS_LAT = 400      # exhaustive over pairs of submodules for lattice identities
EXH_L2C_PAIRS = 20000    # exhaustive over (w_1,w_2) in L-2.3c when |B^2|^2 <= this
SAMPLE = 4000            # sampled pairs / tuples elsewhere
ELEM_BUDGET = 5000       # enumerate the elements of a submodule when |W| <= this
ELEM_CAP = 300000        # never materialise a ring/module larger than this


# ==========================================================================
# 1.  The commutative ring  B = A_t[X]/<X^n - 1>   as an F_q-algebra
# ==========================================================================

class BRing(object):
    """B = A_t[X]/<X^n-1>;  element = n-tuple of elements of A_t.

    A_t element = t-tuple of F_q elements (u-adic coefficients), so an
    element of B is already written over F_q, which is what the linear
    algebra below uses.
    """

    def __init__(self, F, t, n):
        self.F, self.t, self.n = F, t, n
        self.A = Local(F, t)
        A = self.A
        self.q = F.q
        self.p = F.p
        self.dim = t * n                       # dim_{F_q} B
        self.zero = tuple([A.zero] * n)
        self.one = tuple([A.one] + [A.zero] * (n - 1))
        self.X = tuple([A.zero, A.one] + [A.zero] * (n - 2)) if n > 1 else self.one
        self.u = tuple([A.u] + [A.zero] * (n - 1))
        self.eps = None                        # X - 1 (only used for reporting)
        if n > 1:
            self.eps = self.sub(self.X, self.one)
        # monomials u^i X^j (they span B over F_q)
        self.mons = []
        for i in range(t):
            ui = tuple([1 if k == i else 0 for k in range(t)])
            for j in range(n):
                e = [A.zero] * n
                e[j] = ui
                self.mons.append((i, j, tuple(e)))
        self.elems = list(itertools.product(A.elem_list(), repeat=n))
        self.index = dict((e, i) for i, e in enumerate(self.elems))
        self.size = len(self.elems)

    # ---- ring operations -------------------------------------------------
    def add(self, a, b):
        A = self.A
        return tuple(A.add(a[i], b[i]) for i in range(self.n))

    def neg(self, a):
        return tuple(self.A.neg(x) for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        """cyclic convolution:  (ab)_e = sum_{i+j = e mod n} a_i b_j."""
        A, n = self.A, self.n
        out = [A.zero] * n
        for i in range(n):
            ai = a[i]
            if ai == A.zero:
                continue
            for j in range(n):
                bj = b[j]
                if bj == A.zero:
                    continue
                e = (i + j) % n
                out[e] = A.add(out[e], A.mul(ai, bj))
        return tuple(out)

    def pow(self, a, e):
        res, base = self.one, a
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def is_nilpotent(self, a):
        x = a
        for _ in range(self.size + 1):
            if x == self.zero:
                return True
            x = self.mul(x, a)
        return False

    # ---- F_q-vector structure -------------------------------------------
    def vec(self, a):
        out = []
        for blk in a:
            out.extend(blk)
        return tuple(out)

    def from_vec(self, coords):
        A, t, n = self.A, self.t, self.n
        return tuple(tuple(coords[k * t:(k + 1) * t]) for k in range(n))


class Lin(object):
    """F_q-linear algebra on coordinate vectors (subspaces = RREF keys)."""

    def __init__(self, F, dim):
        self.F, self.dim = F, dim

    def span(self, vecs):
        rows = [list(v) for v in vecs if any(v)]
        if not rows:
            return ()
        M, piv = rref(rows, self.F, self.dim)
        return tuple(tuple(r) for r in M)

    def sum(self, k1, k2):
        return self.span(list(k1) + list(k2))

    def dim(self, key):
        return len(key)

    def size(self, key):
        return self.F.q ** len(key)

    def contains(self, key, v):
        if not any(v):
            return True
        return self.span(list(key) + [v]) == key

    def elements(self, key):
        F, d = self.F, self.dim
        out = []
        for coef in itertools.product(range(F.q), repeat=len(key)):
            acc = [0] * d
            for c, row in zip(coef, key):
                if c:
                    for i in range(d):
                        acc[i] = F.add[acc[i]][F.mul[c][row[i]]]
            out.append(tuple(acc))
        return out


class PMod(object):
    """P = B^2 as a right B-module; elements are columns (v_1, v_2)^T."""

    def __init__(self, Br):
        self.B = Br
        self.dim = 2 * Br.dim
        self.LA = Lin(Br.F, self.dim)
        self.elems = list(itertools.product(Br.elems, repeat=2))
        self.zero = (Br.zero, Br.zero)
        self.e1 = (Br.one, Br.zero)
        self.e2 = (Br.zero, Br.one)

    def vec(self, v):
        return self.B.vec(v[0]) + self.B.vec(v[1])

    def from_vec(self, coords):
        B = self.B
        d = B.dim
        return (B.from_vec(coords[:d]), B.from_vec(coords[d:]))

    def act(self, v, b):
        """right action: v . b = (v_1 b, v_2 b)."""
        B = self.B
        return (B.mul(v[0], b), B.mul(v[1], b))

    def addv(self, v, w):
        B = self.B
        return (B.add(v[0], w[0]), B.add(v[1], w[1]))

    def gen(self, seeds):
        """the B-submodule generated by `seeds` (a list of elements of P)."""
        vecs = []
        for v in seeds:
            for (i, j, m) in self.B.mons:
                vecs.append(self.vec(self.act(v, m)))
        return self.LA.span(vecs)

    def key_elems(self, key):
        return [self.from_vec(c) for c in self.LA.elements(key)]


class SMat(object):
    """S = M_2(B);  element = flat 4-tuple (m11, m12, m21, m22)."""

    def __init__(self, Br):
        self.B = Br
        self.dim = 4 * Br.dim
        self.LA = Lin(Br.F, self.dim)
        self.size = Br.size ** 4
        # the element list is materialised only when it is small enough to
        # enumerate (|S| = |B|^4);  everything else works with bases only.
        self.elems = (list(itertools.product(Br.elems, repeat=4))
                      if self.size <= ELEM_CAP else None)
        B = Br
        self.zero = (B.zero, B.zero, B.zero, B.zero)
        self.one = (B.one, B.zero, B.zero, B.one)

    def vec(self, x):
        out = []
        for e in x:
            out.extend(self.B.vec(e))
        return tuple(out)

    def from_vec(self, coords):
        B = self.B
        d = B.dim
        return tuple(B.from_vec(coords[k * d:(k + 1) * d]) for k in range(4))

    def add(self, x, y):
        B = self.B
        return tuple(B.add(x[i], y[i]) for i in range(4))

    def mul(self, x, y):
        """(xy)_{ik} = sum_j x_{ij} y_{jk}."""
        B = self.B
        a11, a12, a21, a22 = x
        b11, b12, b21, b22 = y
        return (B.add(B.mul(a11, b11), B.mul(a12, b21)),
                B.add(B.mul(a11, b12), B.mul(a12, b22)),
                B.add(B.mul(a21, b11), B.mul(a22, b21)),
                B.add(B.mul(a21, b12), B.mul(a22, b22)))

    def transpose(self, x):
        return (x[0], x[2], x[1], x[3])

    def e_jl(self, j, l, b):
        z = self.B.zero
        out = [z, z, z, z]
        out[2 * j + l] = b
        return tuple(out)

    def col(self, x, j):
        """j-th column, as an element of P (j = 0, 1)."""
        return (x[2 * j], x[2 * j + 2]) if j == 0 else (x[1], x[3])

    def row(self, x, i):
        """i-th row, as an element of P (i = 0, 1)."""
        return (x[2 * i], x[2 * i + 1])

    def mat_with_cols(self, w1, w2):
        return (w1[0], w2[0], w1[1], w2[1])

    def gens_as_fq_algebra(self):
        """F_q-basis of S: {E_jl * u^i X^j}."""
        out = []
        for j in (0, 1):
            for l in (0, 1):
                for (i, jj, m) in self.B.mons:
                    out.append(self.e_jl(j, l, m))
        return out

    def principal(self, x):
        """span_{F_q}{x N : N in S} -- computed by direct multiplication
        against the F_q-basis of S, with no use of im(x)."""
        vecs = []
        for N in self.gens_as_fq_algebra():
            vecs.append(self.vec(self.mul(x, N)))
        return self.LA.span(vecs)

    def left_principal(self, x):
        vecs = []
        for N in self.gens_as_fq_algebra():
            vecs.append(self.vec(self.mul(N, x)))
        return self.LA.span(vecs)

    def product_span(self, k1, k2):
        """span of the set of products MN, M in span(k1), N in span(k2)."""
        vecs = []
        for c1 in self.LA.elements(k1):
            M = self.from_vec(c1)
            for c2 in self.LA.elements(k2):
                vecs.append(self.vec(self.mul(M, self.from_vec(c2))))
        return self.LA.span(vecs)


# ==========================================================================
# 2.  The Morita dictionary:  W |-> I_W   and   I |-> W(I)
# ==========================================================================

def I_of_W(S, Wkey):
    """{M in S : both columns lie in W}, as an F_q-subspace of S.

    Built from an F_q-basis of W: the matrices with one column in W and the
    other column zero span I_W over F_q.
    """
    vecs = []
    for c in Wkey:
        w = (S.B.from_vec(c[:S.B.dim]), S.B.from_vec(c[S.B.dim:2 * S.B.dim]))
        vecs.append(S.vec(S.mat_with_cols(w, (S.B.zero, S.B.zero))))
        vecs.append(S.vec(S.mat_with_cols((S.B.zero, S.B.zero), w)))
    if not vecs:
        return ()
    return S.LA.span(vecs)


def W_of_I(S, P, Ikey):
    """sum_{M in I} im M, as a B-submodule of P.

    im M is the B-span of the two columns of M, and the projection of I onto
    either column is already a B-submodule; so W(I) is generated by the
    columns of an F_q-basis of I.
    """
    seeds = []
    for c in Ikey:
        M = S.from_vec(c)
        seeds.append(S.col(M, 0))
        seeds.append(S.col(M, 1))
    return P.gen(seeds)


# ==========================================================================
# 3.  Lattices and minimal generator numbers
# ==========================================================================

def cyclic_submodules(P):
    """all distinct cyclic B-submodules of P (each = vB for some v)."""
    seen = {}
    for v in P.elems:
        k = P.gen([v])
        seen[k] = k
    return sorted(seen)


def principal_right_ideals(S, exhaustive=True, budget=EXH_S, rng=None):
    """all distinct principal right ideals xS (x ranges over S, or a sample)."""
    seen = {}
    pool = S.elems
    if not exhaustive:
        pool = [S.elems[rng.randrange(S.size)] for _ in range(SAMPLE)]
    for x in pool:
        k = S.principal(x)
        seen[k] = k
    return sorted(seen)


def principal_left_ideals(S):
    seen = {}
    for x in S.elems:
        k = S.left_principal(x)
        seen[k] = k
    return sorted(seen)


def lattice_levels(LA, generators, maxnodes=20000):
    """BFS: subobjects = sums of the given 'cyclic' pieces.

    Returns (levels, nodes) where levels[key] = minimal number of pieces
    whose sum is `key` -- i.e. the minimal number of generators of the
    subobject in the relevant sense.
    """
    zero = ()
    levels = {zero: 0}
    frontier = [zero]
    while frontier:
        nxt = []
        for Wk in frontier:
            for Ck in generators:
                Uk = LA.sum(Wk, Ck)
                if Uk not in levels:
                    levels[Uk] = levels[Wk] + 1
                    nxt.append(Uk)
                    if len(levels) > maxnodes:
                        return levels, False
        frontier = nxt
    return levels, True


def mu_by_brute_force_P(P, Wkey, upto=3):
    """minimal k such that some k-tuple of elements of W generates W (B-side).

    Exhaustive for k = 1 (all elements) and for k = 2 when |W| is small;
    otherwise None (the lattice BFS and Nakayama cover those cases).
    """
    LA = P.LA
    if not Wkey:                      # the zero submodule: generated by 0 elements
        return 0
    els = P.key_elems(Wkey)
    for v in els:
        if P.gen([v]) == Wkey:
            return 1
    if len(els) <= EXH_PAIRS_MU:
        for a in els:
            for b in els:
                if P.gen([a, b]) == Wkey:
                    return 2
    return None


def mu_by_brute_force_S(S, Ikey, upto=1):
    """minimal k <= upto such that some k elements generate the right ideal.

    Exhaustive x-scan over I (x in I suffices: xS subset I forces x in I).
    """
    if not Ikey:
        return 0
    if S.LA.size(Ikey) > EXH_IDEALSCAN:
        return None
    for c in S.LA.elements(Ikey):
        x = S.from_vec(c)
        if S.principal(x) == Ikey:
            return 1
    return None


# ---- Nakayama ------------------------------------------------------------

def nilradical_B(Br):
    """the nilradical of B as an F_q-subspace (B is commutative here)."""
    LA = Lin(Br.F, Br.dim)
    vecs = [Br.vec(b) for b in Br.elems if Br.is_nilpotent(b)]
    return LA.span(vecs)


def quotient_map(LA, sub_key):
    """a map v -> canonical representative of v + span(sub_key).

    Returns (reduce, dim_quotient)."""
    d = LA.dim
    basis = list(sub_key)
    if not basis:
        return (lambda v: v), d
    # rref of sub_key gives pivots; kill the pivot coordinates
    M, piv = rref([list(r) for r in basis], LA.F, d)
    piv = list(piv)

    def red(v):
        v = list(v)
        for idx, col in enumerate(piv):
            if v[col]:
                f = v[col]
                row = M[idx]
                v = [LA.F.sub[v[i]][LA.F.mul[f][row[i]]] for i in range(d)]
        return tuple(v)
    return red, d - len(piv)


def mu_via_nakayama(LA, key, radical_key, act_gens, max_k=6):
    """mu of the module `key` via the semisimple quotient:  mu(M) =
    mu(M/MJ) over the quotient ring, computed by brute force on M/MJ.

    `act_gens` is a list of F_q-linear maps (as functions on coordinate
    vectors) generating the action of the ring on the module.
    """
    red, dq = quotient_map(LA, radical_key)
    # quotient space of the module: reduce the basis and keep a maximal
    # independent family (never enumerate the whole module)
    Vbasis = []
    cur = ()
    for c in key:
        r = red(c)
        if any(r) and not LA.contains(cur, r):
            Vbasis.append(r)
            cur = LA.span(list(cur) + [r])
    # build the quotient element list
    Vel = []
    F = LA.F
    for coef in itertools.product(range(F.q), repeat=len(Vbasis)):
        acc = [0] * LA.dim
        for c, row in zip(coef, Vbasis):
            if c:
                for i in range(LA.dim):
                    acc[i] = F.add[acc[i]][F.mul[c][row[i]]]
        Vel.append(tuple(acc))
    Vkey = LA.span(Vel)
    if not Vbasis:                    # the quotient is zero
        return 0
    # action of the ring on the quotient: (v + MJ) . a = red(v . a)
    def orbit(seeds):
        vecs = []
        for v in seeds:
            for f in act_gens:
                vecs.append(red(f(v)))
        return LA.span(vecs)
    for k in range(1, max_k + 1):
        if k == 1:
            for v in Vel:
                if orbit([v]) == Vkey:
                    return 1
        elif k == 2 and len(Vel) ** 2 <= 400000:
            for a in Vel:
                for b in Vel:
                    if orbit([a, b]) == Vkey:
                        return 2
        else:
            return None
    return None


# ==========================================================================
# 4.  Ring-level sanity of the model
# ==========================================================================

def field_params(q):
    return {2: (2, 1), 4: (2, 2), 8: (2, 3), 9: (3, 2), 3: (3, 1)}[q]


def ring_sanity(Br, tag):
    F, A = Br.F, Br.A
    ok = True
    ok &= check("%s: |B| = q^{tn}" % tag, Br.size == Br.q ** (Br.t * Br.n),
                "|B|=%d" % Br.size)
    # commutativity and the two defining relations, exhaustively
    bad = 0
    for a in Br.elems:
        for b in Br.elems:
            if Br.mul(a, b) != Br.mul(b, a):
                bad += 1
                break
        if bad:
            break
    check("%s: B is commutative" % tag, bad == 0,
          "exhaustive over all %d^2 pairs" % Br.size, exhaustive=(Br.size ** 2 <= 70000))
    check("%s: X^n = 1 in B" % tag, Br.pow(Br.X, Br.n) == Br.one, "")
    check("%s: u^t = 0 in B" % tag, Br.pow(Br.u, Br.t) == Br.zero, "")
    # {u^i X^j} spans B over F_q
    LA = Lin(F, Br.dim)
    k = LA.span([Br.vec(m) for (i, j, m) in Br.mons])
    check("%s: {u^i X^j : i<t, j<n} spans B over F_q" % tag,
          len(k) == Br.dim, "dim=%d" % len(k))
    return ok


# ==========================================================================
# 5.  One ring: the full Stage-2A check list
# ==========================================================================

def run_ring(q, t, n, do_ideals=True, do_dictionary=True, rng=None,
             phase1_count=None):
    F = Field(*field_params(q))
    Br = BRing(F, t, n)
    P = PMod(Br)
    S = SMat(Br)
    tag = "(%d,%d,%d)" % (q, t, n)
    rng = rng or __import__("random").Random(SEED)

    say("")
    say("#" * 96)
    say("#  B = A_t[X]/<X^n-1> at (q,t,n) = %s      |B| = %d,  |B^2| = %d,  |S| = %d"
        % (tag, Br.size, len(P.elems), S.size))
    say("#" * 96)

    ring_sanity(Br, tag)

    # ---------------- Jacobson radical / Nakayama data ---------------------
    Jkey = nilradical_B(Br)
    Jdim = len(Jkey)
    redB, dq = quotient_map(Lin(F, Br.dim), Jkey)
    say("  nilradical J(B): dim = %d, |J| = %d,  B/J(B) has |B/J| = %d"
        % (Jdim, F.q ** Jdim, F.q ** dq))
    # B/J(B) is reduced (no nonzero nilpotents) -- i.e. semisimple
    Jels = set(Lin(F, Br.dim).elements(Jkey))
    nb = 0
    for b in Br.elems:
        if all(c == 0 for c in redB(Br.vec(b))):   # b in J(B): zero in B/J
            continue
        # nilpotent in the quotient?
        x = b
        isnil = False
        for _ in range(Br.size + 1):
            if all(c == 0 for c in redB(Br.vec(x))):
                isnil = True
                break
            x = Br.mul(x, b)
        if isnil:
            nb += 1
    check("%s: B/J(B) is reduced (J(B) = nilradical)" % tag, nb == 0,
          "%d nonzero nilpotents in B/J" % nb)
    # JS = M_2(J(B))
    JSkey = S.LA.span([S.vec(S.e_jl(j, l, Br.from_vec(c)))
                       for c in Jkey for j in (0, 1) for l in (0, 1)])
    check("%s: M_2(J(B)) is a two-sided ideal of S" % tag,
          is_two_sided(S, JSkey), "dim = %d" % len(JSkey))

    # ---------------- submodule lattice and mu_B ---------------------------
    t0 = time.time()
    cyc = cyclic_submodules(P)
    sub_lv, complete = lattice_levels(P.LA, cyc)
    nsub = len(sub_lv)
    print("       (submodule lattice built in %.1f s)" % (time.time() - t0))
    say("  submodule lattice: %d submodules of B^2 (%d cyclic), enumerated %s"
        % (nsub, len(cyc), "exhaustively" if complete else "PARTIALLY"))
    if phase1_count is not None:
        check("%s: #submodules of B^2 equals the Phase-1 cyclic-code count" % tag,
              nsub == phase1_count, "%d vs %d" % (nsub, phase1_count))
    distB = Counter(sub_lv.values())
    say("  mu_B distribution: %s" % sorted(distB.items()))

    # mu_B by brute force (k <= 2) on small submodules -- independent method 2
    bf_muB = {}
    nbf = 0
    for Wk, lv in sub_lv.items():
        if P.LA.size(Wk) <= ELEM_BUDGET:
            m = mu_by_brute_force_P(P, Wk)
            if m is not None:
                bf_muB[Wk] = m
                nbf += 1
    badmu = [k for k, m in bf_muB.items() if m != sub_lv[k] and sub_lv[k] <= 2]
    check("%s: mu_B from brute-force k-tuple scan agrees with the lattice BFS" % tag,
          not badmu, "%d submodules checked exhaustively for k<=2" % nbf)

    # mu_B via Nakayama -- independent method 3
    actB = []
    LA_B = Lin(F, Br.dim)
    for b in Br.elems:
        bb = b

        def f(v, bb=bb):
            w = P.from_vec(v)
            return P.vec(P.act(w, bb))
        actB.append(f)
    nk_muB = {}
    for Wk, lv in sub_lv.items():
        # radical part: W . J(B)
        WJ = P.LA.span([])
        vecs = []
        for c in Wk:
            w = P.from_vec(c)
            for cc in Jkey:
                vecs.append(P.vec(P.act(w, Br.from_vec(cc))))
        WJ = P.LA.span(vecs)
        m = mu_via_nakayama(P.LA, Wk, WJ, actB)
        if m is not None:
            nk_muB[Wk] = m
    badnk = [k for k, m in nk_muB.items() if m != sub_lv[k]]
    check("%s: mu_B from Nakayama on B/J(B) agrees with the lattice BFS" % tag,
          not badnk, "%d submodules compared" % len(nk_muB))

    # ---------------- right-ideal lattice and mu_S -------------------------
    if do_ideals and S.size <= EXH_S:
        t0 = time.time()
        prin = principal_right_ideals(S, exhaustive=True)
        print("       (principal-ideal scan took %.1f s)" % (time.time() - t0))
        say("  principal right ideals: %d (scan over all |S| = %d elements)"
            % (len(prin), S.size))
        t0 = time.time()
        id_lv, complete2 = lattice_levels(S.LA, prin)
        print("       (right-ideal lattice built in %.1f s)" % (time.time() - t0))
        say("  right-ideal lattice: %d right ideals, enumerated %s"
            % (len(id_lv), "exhaustively" if complete2 else "PARTIALLY"))
        distS = Counter(id_lv.values())
        say("  mu_S distribution: %s" % sorted(distS.items()))
        check("%s: #right ideals = #submodules of B^2 (Morita bijection)" % tag,
              len(id_lv) == nsub, "%d vs %d" % (len(id_lv), nsub))

        # mu_S by brute force x-scan (independent method 2)
        npass = 0
        badS = []
        for Ik, lv in id_lv.items():
            m = mu_by_brute_force_S(S, Ik)
            if m is not None:
                npass += 1
                if m != lv:
                    badS.append(Ik)
        check("%s: mu_S from the exhaustive x-scan agrees with the ideal lattice BFS"
              % tag, not badS, "%d right ideals scanned" % npass)

        # mu_S via Nakayama (independent method 3)
        actS = []
        for N in S.gens_as_fq_algebra():
            def g(v, N=N):
                return S.vec(S.mul(S.from_vec(v), N))
            actS.append(g)
        badS2 = []
        nnk = 0
        for Ik, lv in id_lv.items():
            vecs = []
            for c in Ik:
                M = S.from_vec(c)
                for cc in JSkey:
                    vecs.append(S.vec(S.mul(M, S.from_vec(cc))))
            IJ = S.LA.span(vecs)
            m = mu_via_nakayama(S.LA, Ik, IJ, actS)
            if m is not None:
                nnk += 1
                if m != lv:
                    badS2.append(Ik)
        check("%s: mu_S from Nakayama on S/J(S) agrees with the ideal lattice BFS"
              % tag, not badS2, "%d right ideals compared" % nnk)

        # ---------------- Task A: the dictionary ---------------------------
        bad = 0
        for Wk in sub_lv:
            Ik = I_of_W(S, Wk)
            if W_of_I(S, P, Ik) != Wk:
                bad += 1
        check("%s: W(I_W) = W for every submodule W" % tag, bad == 0,
              "%d submodules" % nsub)

        bad = 0
        for Ik in id_lv:
            Wk = W_of_I(S, P, Ik)
            if I_of_W(S, Wk) != Ik:
                bad += 1
        check("%s: I_{W(I)} = I for every right ideal I" % tag, bad == 0,
              "%d right ideals" % len(id_lv))

        # every I_W is a right ideal (closure under right multiplication)
        bad = 0
        for Wk in sub_lv:
            if not is_right_ideal(S, I_of_W(S, Wk)):
                bad += 1
        check("%s: every I_W is a right ideal (IS subset I)" % tag, bad == 0,
              "%d submodules" % nsub)

        # cardinality / dimension
        bad = 0
        for Wk in sub_lv:
            Ik = I_of_W(S, Wk)
            if len(Ik) != 2 * len(Wk) or S.LA.size(Ik) != P.LA.size(Wk) ** 2:
                bad += 1
        check("%s: dim I_W = 2 dim W and |I_W| = |W|^2" % tag, bad == 0,
              "%d submodules" % nsub)

        # lattice operations
        Ws = sorted(sub_lv)
        pairs = (list(itertools.combinations(Ws, 2)) if len(Ws) ** 2 <= EXH_PAIRS_LAT ** 2
                 else [(Ws[rng.randrange(len(Ws))], Ws[rng.randrange(len(Ws))])
                       for _ in range(SAMPLE)])
        exh_pairs = len(Ws) ** 2 <= EXH_PAIRS_LAT ** 2
        badsum = badint = 0
        for (W1, W2) in pairs:
            if I_of_W(S, P.LA.sum(W1, W2)) != S.LA.sum(I_of_W(S, W1), I_of_W(S, W2)):
                badsum += 1
            if I_of_W(S, meet(P.LA, W1, W2)) != meet(S.LA, I_of_W(S, W1), I_of_W(S, W2)):
                badint += 1
        check("%s: I_{W1+W2} = I_{W1} + I_{W2}" % tag, badsum == 0,
              "%d pairs" % len(pairs), exhaustive=exh_pairs)
        check("%s: I_{W1 cap W2} = I_{W1} cap I_{W2}" % tag, badint == 0,
              "%d pairs" % len(pairs), exhaustive=exh_pairs)

        badinc = 0
        for (W1, W2) in pairs:
            sub = all(P.LA.contains(W2, c) for c in W1)
            if sub != all(S.LA.contains(I_of_W(S, W2), c) for c in I_of_W(S, W1)):
                badinc += 1
        check("%s: W1 subset W2  <=>  I_{W1} subset I_{W2}" % tag, badinc == 0,
              "%d pairs" % len(pairs), exhaustive=exh_pairs)

        # ---------------- Task B: the identity -----------------------------
        bad = []
        for Wk, lvB in sub_lv.items():
            Ik = I_of_W(S, Wk)
            if Ik not in id_lv:
                bad.append(("not-in-lattice", Wk))
                continue
            if id_lv[Ik] != -(-lvB // 2):
                bad.append((lvB, id_lv[Ik]))
        check("%s: mu_S(I_W) = ceil(mu_B(W)/2) for every W" % tag, not bad,
              "%d submodules; mu_B distribution %s" % (nsub, sorted(distB.items())),
              exhaustive=True)

        # L-2.3a: sum_i x_i S = I_{sum im x_i}
        bad = 0
        for x in S.elems:
            Wp = P.gen([S.col(x, 0), S.col(x, 1)])
            if S.principal(x) != I_of_W(S, Wp):
                bad += 1
        check("%s: L-2.3a with k = 1: xS = I_{im x} for every x in S" % tag,
              bad == 0, "all %d elements of S" % S.size)
        # k = 2 (sampled if too many)
        pool = S.elems
        exh2 = S.size ** 2 <= EXH_L2C_PAIRS
        if not exh2:
            pool = [(S.elems[rng.randrange(S.size)], S.elems[rng.randrange(S.size)])
                    for _ in range(SAMPLE // 4)]
            pairs2 = pool
        else:
            pairs2 = list(itertools.product(S.elems, repeat=2))
        bad = 0
        for (x, y) in pairs2:
            Wp = P.gen([S.col(x, 0), S.col(x, 1), S.col(y, 0), S.col(y, 1)])
            if S.LA.sum(S.principal(x), S.principal(y)) != I_of_W(S, Wp):
                bad += 1
        check("%s: L-2.3a with k = 2: xS + yS = I_{im x + im y}" % tag, bad == 0,
              "%d pairs" % len(pairs2), exhaustive=exh2)

        # L-2.3c: im[w1|w2] = B w1 + B w2
        exh3 = len(P.elems) ** 2 <= EXH_L2C_PAIRS
        if exh3:
            pairs3 = list(itertools.product(P.elems, repeat=2))
        else:
            pairs3 = [(P.elems[rng.randrange(len(P.elems))],
                       P.elems[rng.randrange(len(P.elems))]) for _ in range(SAMPLE)]
        bad = 0
        for (w1, w2) in pairs3:
            M = S.mat_with_cols(w1, w2)
            if P.gen([S.col(M, 0), S.col(M, 1)]) != P.gen([w1, w2]):
                bad += 1
        check("%s: L-2.3c: im[w1|w2] = Bw1 + Bw2" % tag, bad == 0,
              "%d pairs" % len(pairs3), exhaustive=exh3)

        # L-2.3b: min # of <=2-generated summands = ceil(mu_B/2)
        two_gen = set(k for k, v in sub_lv.items() if v <= 2)
        lv2, _ = lattice_levels(P.LA, sorted(two_gen))
        bad = [k for k, v in sub_lv.items()
               if k in lv2 and lv2[k] != -(-v // 2)]
        check("%s: L-2.3b: min #(<=2-generated summands) = ceil(mu_B/2)" % tag,
              not bad, "%d submodules" % len(sub_lv))

        # ---------------- Task C: principality -----------------------------
        bad = []
        nprin = 0
        for Wk, lvB in sub_lv.items():
            Ik = I_of_W(S, Wk)
            is_principal = (Ik in prin)
            if is_principal != (lvB <= 2):
                bad.append((lvB, is_principal))
            if is_principal:
                nprin += 1
        check("%s: I_W principal <=> mu_B(W) <= 2" % tag, not bad,
              "%d principal / %d non-principal of %d" % (nprin, nsub - nprin, nsub))

        # ---------------- left and two-sided ideals ------------------------
        lprin = principal_left_ideals(S)
        lid_lv, _ = lattice_levels(S.LA, lprin)
        check("%s: #left ideals = #right ideals" % tag,
              len(lid_lv) == len(id_lv), "%d vs %d" % (len(lid_lv), len(id_lv)))
        bad = 0
        for Ik in id_lv:
            Tk = S.LA.span([S.vec(S.transpose(S.from_vec(c))) for c in Ik])
            if Tk not in lid_lv:
                bad += 1
        check("%s: I right ideal => I^T left ideal (transpose)" % tag, bad == 0,
              "%d right ideals" % len(id_lv))
        bad = 0
        for Lk in lid_lv:
            Tk = S.LA.span([S.vec(S.transpose(S.from_vec(c))) for c in Lk])
            if Tk not in id_lv:
                bad += 1
        check("%s: L left ideal => L^T right ideal (transpose)" % tag, bad == 0,
              "%d left ideals" % len(lid_lv))
        # two-sided ideals = M_2(J), J an ideal of B
        idealsB = enumerate_ideals_B(Br)
        twosided = set(k for k in id_lv if k in lid_lv)
        mJ = set()
        for Jk in idealsB:
            mJ.add(S.LA.span([S.vec(S.e_jl(j, l, Br.from_vec(c)))
                              for c in Jk for j in (0, 1) for l in (0, 1)]))
        check("%s: two-sided ideals of S are exactly M_2(J), J an ideal of B" % tag,
              twosided == mJ, "%d two-sided, %d ideals of B"
              % (len(twosided), len(idealsB)))
        # two-sided ideals <-> W = J (+) J
        bad = 0
        for Jk in idealsB:
            Wk = P.LA.span([P.vec((Br.from_vec(c), Br.zero)) for c in Jk] +
                           [P.vec((Br.zero, Br.from_vec(c))) for c in Jk])
            if Wk not in sub_lv:
                bad += 1
        check("%s: W = J (+) J is a submodule of B^2 for every ideal J of B" % tag,
              bad == 0, "%d ideals" % len(idealsB))
        say("  ideals of B: %d ;  two-sided ideals of S: %d"
            % (len(idealsB), len(twosided)))

        # ---------------- boundary cases (reported explicitly) -------------
        say("  boundary cases:")
        zero_k = ()
        full_k = P.gen([P.e1, P.e2])            # W = B^2
        for (nm, Wk) in [("W = 0", zero_k), ("W = B^2", full_k)]:
            Ik = I_of_W(S, Wk)
            say("    %-10s mu_B = %d, mu_S = %d, ceil(mu_B/2) = %d"
                % (nm, sub_lv[Wk], id_lv[Ik], -(-sub_lv[Wk] // 2)))
        # one submodule of each mu_B value
        seen_mu = {}
        for Wk, lv in sub_lv.items():
            if lv not in seen_mu:
                seen_mu[lv] = Wk
        for lv in sorted(seen_mu):
            Wk = seen_mu[lv]
            Ik = I_of_W(S, Wk)
            say("    mu_B = %d : |W| = %d, dim W = %d, mu_S = %d, |I_W| = %d"
                % (lv, P.LA.size(Wk), len(Wk), id_lv[Ik], S.LA.size(Ik)))
    else:
        say("  (|S| = %d > %d: right-ideal lattice not enumerated exhaustively)"
            % (S.size, EXH_S))
        sub_lv = sub_lv
        id_lv = None
        prin = None

    # ---------------- Stage-1 dictionary ---------------------------------
    if do_dictionary:
        run_dictionary(Br, P, S, sub_lv, id_lv, tag, rng)

    return dict(Br=Br, P=P, S=S, sub_lv=sub_lv, id_lv=id_lv, prin=prin,
                distB=Counter(sub_lv.values()) if sub_lv else None)


def nullspace_basis(rows, F, ncols):
    """basis of {y in F^ncols : rows . y = 0}."""
    M, piv = rref([list(r) for r in rows], F, ncols)
    piv = list(piv)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        y = [0] * ncols
        y[fc] = 1
        for i, pc in enumerate(piv):
            y[pc] = F.neg[M[i][fc]]
        out.append(tuple(y))
    return out


def meet(LA, k1, k2):
    """intersection of two subspaces, by solving sum c_i A_i - sum d_j B_j = 0."""
    if not k1 or not k2:
        return ()
    F, d = LA.F, LA.dim
    n1, n2 = len(k1), len(k2)
    # equations indexed by the ambient coordinate i:
    #   sum_j c_j A_j[i] - sum_l d_l B_l[i] = 0
    rows = [[k1[j][i] for j in range(n1)] + [F.neg[k2[l][i]] for l in range(n2)]
            for i in range(d)]
    out = []
    for y in nullspace_basis(rows, F, n1 + n2):
        acc = [0] * d
        for ci, r in zip(y[:n1], k1):
            if ci:
                for i in range(d):
                    acc[i] = F.add[acc[i]][F.mul[ci][r[i]]]
        out.append(tuple(acc))
    return LA.span(out)


def is_right_ideal(S, Ik):
    """Ik is a right ideal: for every basis element M and every F_q-algebra
    generator N of S, MN lies in Ik (F_q-bilinearity does the rest)."""
    for c in Ik:
        M = S.from_vec(c)
        for N in S.gens_as_fq_algebra():
            if not S.LA.contains(Ik, S.vec(S.mul(M, N))):
                return False
    return True


def is_two_sided(S, Ik):
    return is_right_ideal(S, Ik) and is_left_ideal(S, Ik)


def is_left_ideal(S, Ik):
    for c in Ik:
        M = S.from_vec(c)
        for N in S.gens_as_fq_algebra():
            if not S.LA.contains(Ik, S.vec(S.mul(N, M))):
                return False
    return True


def minimal_generators(P, Wk, muB):
    """a generating set of W of the minimum possible size muB.

    The candidate pool is the whole submodule when it is small and the F_q
    -basis otherwise (a basis of W generates W as a B-module, so searching
    its subsets is sound; it is exhaustive for the pool that is used).
    """
    if muB == 0:
        return []
    basis = [P.from_vec(c) for c in Wk]
    pool = (P.key_elems(Wk) if P.LA.size(Wk) <= 256 else basis)
    for k in range(1, muB + 1):
        if len(pool) ** k > 4000000:
            break
        for sub in itertools.combinations(pool, k):
            if P.gen(list(sub)) == Wk:
                return list(sub)
    return basis


def enumerate_ideals_B(Br):
    """all ideals of the commutative ring B (BFS over principal ideals)."""
    LA = Lin(Br.F, Br.dim)
    prin = {}
    for b in Br.elems:
        k = LA.span([Br.vec(Br.mul(b, m)) for (i, j, m) in Br.mons])
        prin[k] = k
    lv, _ = lattice_levels(LA, sorted(prin))
    return sorted(lv)


# ==========================================================================
# 6.  Stage-1 dictionary:  R_n = M_2(A_t)[X]/<X^n-1>  ==  M_2(B)
# ==========================================================================

def run_dictionary(Br, P, S, sub_lv, id_lv, tag, rng):
    """Verify that the Stage-1 cyclic-code correspondence (right ideals of
    R_n <-> T-invariant right R-submodules of R^n) and the Morita
    correspondence (right ideals of M_2(B) <-> B-submodules of B^2) are the
    same correspondence, once R_n is identified with M_2(B) by iota.

    The Stage-1 side is computed in its own representation: C = iota^{-1}(I)
    is a subset of R^n = M_2(A_t)^n, its Morita transform for R = M_2(A_t) is
    the A_t-submodule C . A_t^2 of (A_t^2)^n, and only then is the result
    regrouped into B^2 = (A_t^n)^2.
    """
    F, t, n = Br.F, Br.t, Br.n
    A = Br.A
    MR = MatRing(A, 2)                     # R = M_2(A_t)
    Rels = list(itertools.product(A.elem_list(), repeat=4))   # M_2(A_t)
    Rn = list(itertools.product(Rels, repeat=n))              # R^n
    say("")
    say("  -- Stage-1 dictionary: R_n = M_2(A_t)[X]/<X^n-1>  ==  M_2(B) --")
    say("     |R^n| = %d, |R| = %d, #right ideals of R_n = %s"
        % (len(Rn), len(Rels), (len(id_lv) if id_lv is not None else "n/a")))

    def iota(x):
        """iota((M_0,...,M_{n-1})) = sum_k M_k X^k  in M_2(B)."""
        acc = [Br.zero] * 4
        for k in range(n):
            Mk = x[k]
            for idx in range(4):
                blk = [A.zero] * n
                blk[k] = Mk[idx]
                acc[idx] = Br.add(acc[idx], tuple(blk))
        return tuple(acc)

    seen = set()
    for x in Rn:
        seen.add(iota(x))
    check("%s: Stage-1 iota: R^n -> M_2(B) is bijective" % tag,
          len(seen) == len(Rn) == S.size, "%d elements" % len(Rn))

    def mul_Rn(x, y):
        out = [MR.zero] * n
        for i in range(n):
            for j in range(n):
                e = (i + j) % n
                out[e] = MR.add(out[e], MR.mul(x[i], y[j]))
        return tuple(out)

    exh = len(Rn) ** 2 <= 300000
    pairs = (list(itertools.product(Rn, repeat=2)) if exh else
             [(Rn[rng.randrange(len(Rn))], Rn[rng.randrange(len(Rn))])
              for _ in range(SAMPLE)])
    bad = 0
    for (x, y) in pairs:
        if iota(mul_Rn(x, y)) != S.mul(iota(x), iota(y)):
            bad += 1
    check("%s: iota is a ring homomorphism (convolution <-> matrix product)" % tag,
          bad == 0, "%d pairs" % len(pairs), exhaustive=exh)

    if id_lv is None:
        return

    # --- the two correspondences agree ------------------------------------
    def colj(Mk, j):
        """j-th column of a 2x2 matrix over A_t, as a pair of A_t elements."""
        return (Mk[2 * j], Mk[2 * j + 2]) if j == 0 else (Mk[1], Mk[3])

    def regroup(cols):
        """(A_t^2)^n -> (A_t^n)^2 = B^2 :  transpose the list of pairs."""
        return (tuple([cols[k][0] for k in range(n)]),
                tuple([cols[k][1] for k in range(n)]))

    def Tshift(x):
        return tuple([x[(k - 1) % n] for k in range(n)])

    cost = len(Rn) * len(id_lv)
    ideals = sorted(id_lv)
    exh_i = cost <= 200000
    if not exh_i:
        ideals = ideals[:6]
    badW = badT = badR = 0
    nT = nR = 0
    all_seeds = True
    for Ik in ideals:
        C = [x for x in Rn if S.LA.contains(Ik, S.vec(iota(x)))]
        # C is a right R-submodule of R^n and is T-invariant  (Stage 1, Thm 4.1)
        for x in C:
            nT += 1
            if not S.LA.contains(Ik, S.vec(iota(Tshift(x)))):
                badT += 1
        pairsR = (list(itertools.product(C, Rels)) if len(C) * len(Rels) <= 20000
                  else [(C[rng.randrange(len(C))], Rels[rng.randrange(len(Rels))])
                        for _ in range(min(2000, 10 * len(C)))])
        for (x, a) in pairsR:
            nR += 1
            xa = tuple(MR.mul(x[k], a) for k in range(n))
            if not S.LA.contains(Ik, S.vec(iota(xa))):
                badR += 1
        # Morita transform of C for R = M_2(A_t):  C . A_t^2 subset (A_t^2)^n
        seeds_all = []
        for x in C:
            for j in (0, 1):
                seeds_all.append(regroup([colj(x[k], j) for k in range(n)]))
        seeds = seeds_all
        if len(seeds_all) > 200:                  # keep the run finite
            all_seeds = False
            step = len(seeds_all) // 100
            seeds = seeds_all[::step][:200]
        # A_t-span (close under u), then B-span (= T-invariance + A_t-span)
        uvecs = []
        for v in seeds:
            w = v
            for i in range(t):
                uvecs.append(P.vec(w))
                w = P.act(w, Br.u)
        Wk = P.gen([P.from_vec(c) for c in P.LA.span(uvecs)])
        if Wk != W_of_I(S, P, Ik):
            badW += 1
    check("%s: C = iota^{-1}(I) is T-invariant (Stage-1 side)" % tag,
          badT == 0, "%d elements, %d ideals" % (nT, len(ideals)), exhaustive=exh_i)
    check("%s: C = iota^{-1}(I) is a right R-submodule of R^n" % tag,
          badR == 0, "%d (x,a) pairs" % nR,
          exhaustive=(len(C) * len(Rels) <= 20000))
    check("%s: Morita W(I) = regroup(iota^{-1}(I) . A_t^2)  (same correspondence)"
          % tag, badW == 0, "%d right ideals" % len(ideals),
          exhaustive=(exh_i and all_seeds))


# ==========================================================================
# 7.  Targeted run at the in-scope wild case (q,t,n) = (4,2,2)
# ==========================================================================

def run_wild_422():
    """B = F_4[u,eps]/<u^2, eps^2>  (|B| = 256): the wild case.

    No full lattice enumeration is possible (|B^2| = 65536, |S| = 2^32);
    instead a targeted list of submodules is analysed with the elementary
    certificates:  mu_B(W) >= dim_K(W/mW) (images of generators span the
    quotient) and mu_S(I) >= ceil(dim_q(I/IJ) / (4 dim_q K)).
    """
    F = Field(2, 2)
    Br = BRing(F, 2, 2)
    P = PMod(Br)
    S = SMat(Br)
    tag = "(4,2,2)"
    say("")
    say("#" * 96)
    say("#  WILD CASE (q,t,n) = (4,2,2):  B = F_4[u,eps]/<u^2,eps^2>")
    say("#  |B| = %d, |B^2| = %d, |S| = %d  (no exhaustive lattice enumeration)"
        % (Br.size, len(P.elems), S.size))
    say("#" * 96)

    ring_sanity(Br, tag)
    Jkey = nilradical_B(Br)
    LA_B = Lin(F, Br.dim)
    redB, dq = quotient_map(LA_B, Jkey)
    say("  J(B) = m: dim = %d, |m| = %d ; B/m has |B/m| = %d (= F_4)"
        % (len(Jkey), F.q ** len(Jkey), F.q ** dq))
    mels = [Br.from_vec(c) for c in LA_B.elements(Jkey)]
    # m = (u, eps)  -- the IDEAL generated by u and eps, i.e. closed under B
    span_ue = LA_B.span([Br.vec(Br.mul(g, m))
                         for g in (Br.u, Br.eps) for (i, j, m) in Br.mons])
    check("%s: J(B) = (u, eps)" % tag, span_ue == Jkey,
          "dim %d" % len(Jkey))
    # m^2
    m2 = LA_B.span([Br.vec(Br.mul(a, b)) for a in mels for b in mels])
    say("  m^2: dim = %d, |m^2| = %d ;  dim_{F_4}(m/m^2) = %d"
        % (len(m2), F.q ** len(m2), len(Jkey) - len(m2)))
    check("%s: dim_{B/m}(m/m^2) = 2 (so m is not principal)" % tag,
          len(Jkey) - len(m2) == 2, "dim = %d" % (len(Jkey) - len(m2)))

    Kdim = dq                                  # dim_{F_q}(B/m) = 1 here
    # the submodules to analyse
    WW = [
        ("W = 0", []),
        ("W = B^2", [P.e1, P.e2]),
        ("W = e_1 B", [P.e1]),
        ("W = m e_1 + B e_2", [(Br.u, Br.zero), (Br.eps, Br.zero), P.e2]),
        ("W = m (+) m  <-- the wild submodule",
         [(Br.u, Br.zero), (Br.eps, Br.zero), (Br.zero, Br.u), (Br.zero, Br.eps)]),
        ("W = m e_1 + m e_2 with a twist",
         [(Br.u, Br.eps), (Br.eps, Br.zero), (Br.u, Br.zero)]),
    ]
    for (nm, seeds) in WW:
        Wk = P.gen(seeds)
        # mu_B lower bound: dim over K of W/mW
        vecs = []
        for c in Wk:
            w = P.from_vec(c)
            for cc in Jkey:
                vecs.append(P.vec(P.act(w, Br.from_vec(cc))))
        Wm = P.LA.span(vecs)
        dquot = len(Wk) - len(Wm)              # dim_{F_q}
        muB_low = -(-dquot // Kdim)            # ceil(dim_{F_q}(W/mW) / dim_{F_q} K)
        muB_up = len(seeds)
        # mu_S: exhibit ceil(muB_up/2) generators from the packing construction
        k = -(-len(seeds) // 2)
        gens = []
        for i in range(k):
            w1 = seeds[2 * i] if 2 * i < len(seeds) else P.zero
            w2 = seeds[2 * i + 1] if 2 * i + 1 < len(seeds) else P.zero
            gens.append(S.mat_with_cols(w1, w2))
        Ik = I_of_W(S, Wk)
        span_gens = S.LA.span([])
        for g in gens:
            span_gens = S.LA.sum(span_gens, S.principal(g))
        muS_up_ok = (span_gens == Ik) if gens else (Ik == ())
        # mu_S lower bound via I / I J(S)
        JSkey = S.LA.span([S.vec(S.e_jl(j, l, Br.from_vec(c)))
                           for c in Jkey for j in (0, 1) for l in (0, 1)])
        vecs = []
        for c in Ik:
            M = S.from_vec(c)
            for cc in JSkey:
                vecs.append(S.vec(S.mul(M, S.from_vec(cc))))
        IJ = S.LA.span(vecs)
        dI = len(Ik) - len(IJ)                 # dim_{F_q} of I/IJ
        # a 1-generated module over S/J(S) = M_2(K) has dim_{F_q} <= 4 dim_{F_q} K
        muS_low = -(-dI // (4 * Kdim)) if dI else 0
        say("  %-38s |W|=%-7d dim W=%d  mu_B in [%d,%d]  mu_S in [%d,%d]"
            % (nm, P.LA.size(Wk), len(Wk), muB_low, muB_up, muS_low, k))
        check("%s: %s generators do generate I_W (upper bound)" % (tag, nm),
              muS_up_ok, "%d generator(s)" % k)
        check("%s: %s lower bounds match the identity" % (tag, nm),
              (muB_low == muB_up) and (muS_low == k) and (k == -(-muB_up // 2)),
              "mu_B = %d, mu_S = %d, ceil(mu_B/2) = %d" % (muB_up, k, -(-muB_up // 2)))
        if muB_up > 2:
            check("%s: %s is NOT principal (mu_B = %d > 2)" % (tag, nm, muB_up),
                  muS_low >= 2,
                  "certificate: dim_{F_q}(I/IJ) = %d > 4 dim_{F_q}(K) = %d"
                  % (dI, 4 * Kdim))


# ==========================================================================
# 8.  Where projectivity is used (L-2.3a): a non-projective P
# ==========================================================================

def run_projectivity_counterexample():
    """Over B = F_2[eps]/<eps^2> take P' = B (+) k with k = B/(eps).

    P' is NOT projective, and for S' = End_B(P') the analogue of L-2.3a
    FAILS: there is x in S' with  x S'  strictly contained in  I_{im x}.
    So the projectivity hypothesis in the *general* form of the lemma (P an
    arbitrary module, S = End_B(P)) is not removable.  For the module Stage
    2A uses, P = B^2, the lemma holds -- and it is proved in the companion
    document by column packing, with no projectivity at all.
    """
    say("")
    say("#" * 96)
    say("#  PART: WHERE PROJECTIVITY IS USED IN L-2.3a")
    say("#  B = F_2[eps]/<eps^2>,  P' = B (+) k,  k = B/(eps)   (P' NOT projective)")
    say("#" * 96)
    F = Field(2, 1)
    Br = BRing(F, 1, 2)             # B = F_2[X]/<X^2-1> = F_2[eps]/<eps^2>
    eps = Br.eps
    check("proj: B = F_2[eps]/<eps^2> with eps^2 = 0",
          Br.size == 4 and Br.mul(eps, eps) == Br.zero and eps != Br.zero,
          "|B| = %d" % Br.size)

    def bar(b):
        """the quotient map B -> B/(eps), i.e. evaluation at X = 1.

        Here t = 1, so B/(eps) = F_2 and bar(b) is the sum of the
        coefficients of b (the image of X is 1)."""
        acc = 0
        for blk in b:
            acc = F.add[acc][blk[0]]
        return acc

    Pels = [(b, m) for b in Br.elems for m in (0, 1)]
    zero = (Br.zero, 0)

    def Bof(c):
        """the scalar c in F_2 as an element of B (constant polynomial)."""
        return tuple([(c,)] + [Br.A.zero] * (Br.n - 1))

    def act(v, a):
        """right action of B on P' = B (+) k."""
        return (Br.mul(v[0], a), (v[1] * bar(a)) % 2)

    def padd(v, w):
        return (Br.add(v[0], w[0]), (v[1] + w[1]) % 2)

    # P' is a right B-module
    ok = all(act(act(v, a), b) == act(v, Br.mul(a, b))
             for v in Pels for a in Br.elems for b in Br.elems)
    ok &= all(act(padd(v, w), a) == padd(act(v, a), act(w, a))
              for v in Pels for w in Pels for a in Br.elems)
    check("proj: P' = B (+) k is a right B-module (axioms verified)", ok,
          "all %d x %d^2 triples" % (len(Pels), Br.size))

    # k is not projective: B -> k has no B-linear section.  A section sigma
    # is determined by sigma(1) = b0 with eps.b0 = 0 (B-linearity w.r.t. eps),
    # and must satisfy bar(b0) = 1.
    cands = [b for b in Br.elems if Br.mul(b, eps) == Br.zero and bar(b) == 1]
    check("proj: k is not projective (B -> k has no B-linear section)",
          not cands, "%d candidates b0 with eps b0 = 0 and bar(b0) = 1" % len(cands))

    # S' = End_B(P')
    def build(im_e, im_f):
        def f(v):
            return padd(act(im_e, v[0]), act(im_f, Bof(v[1])))
        return f

    maps = []
    for im_e in Pels:
        for im_f in Pels:
            if act(im_f, eps) != zero:      # eps . f = 0  =>  eps . im(f) = 0
                continue
            f = build(im_e, im_f)
            if all(f(act(v, b)) == act(f(v), b) for v in Pels for b in Br.elems):
                maps.append(f)
    say("  |End_B(P')| = %d" % len(maps))
    # closed under composition
    ok = all(all(build(f((1, 0)) if False else f(Pels[1]), f(Pels[2]))(v) is not None
                 for v in Pels) for f in maps[:4])
    def compose(f, g):
        return lambda v: f(g(v))
    inclosed = 0
    for f in maps:
        for g in maps:
            h = compose(f, g)
            if any(h(act(v, b)) != act(h(v), b) for v in Pels for b in Br.elems):
                inclosed += 1
    check("proj: S' = End_B(P') is closed under composition",
          inclosed == 0, "%d x %d pairs" % (len(maps), len(maps)))

    def in_end(f):
        return all(f(act(v, b)) == act(f(v), b) for v in Pels for b in Br.elems)

    # x : (b,m) |-> (eps b, 0)
    def x_map(v):
        return (Br.mul(v[0], eps), 0)
    check("proj: x : (b,m) |-> (eps b, 0) is B-linear", in_end(x_map), "")
    im_x = set(x_map(v) for v in Pels)
    xS = set(tuple(x_map(h(v)) for v in Pels) for h in maps)
    I_imx = [g for g in maps if all(g(v) in im_x for v in Pels)]
    say("  |x S'| = %d ,  |I_{im x}| = %d ,  |im x| = %d"
        % (len(xS), len(I_imx), len(im_x)))
    check("proj: xS' is STRICTLY contained in I_{im x} (L-2.3a fails for P')",
          len(xS) < len(I_imx), "%d < %d" % (len(xS), len(I_imx)))

    # explicit witness g : (b,m) |-> (eps.m, 0)
    def g_map(v):
        return (Br.mul(eps, Bof(v[1])), 0)
    is_endo = in_end(g_map)
    in_I = all(g_map(v) in im_x for v in Pels)
    in_xS = any(all(g_map(v) == x_map(h(v)) for v in Pels) for h in maps)
    check("proj: witness g in I_{im x} but g not in xS'",
          is_endo and in_I and not in_xS,
          "g B-linear: %s ; im g subset im x: %s ; g in xS': %s"
          % (is_endo, in_I, in_xS))
    # why it cannot lift: any h with xh = g needs h(f) to have a unit part
    need = [v for v in Pels if False]
    h_bad = 0
    for h in maps:
        if all(x_map(h(v)) == g_map(v) for v in Pels):
            h_bad += 1
    check("proj: no h in S' satisfies x o h = g (the lift does not exist)",
          h_bad == 0, "%d candidates found" % h_bad)

    # the same lemma DOES hold for the free module P = B^2 actually used here
    P = PMod(Br)
    S = SMat(Br)
    bad = 0
    for x in S.elems:
        Wp = P.gen([S.col(x, 0), S.col(x, 1)])
        if S.principal(x) != I_of_W(S, Wp):
            bad += 1
    check("proj: for the FREE module P = B^2 the identity xS = I_{im x} holds",
          bad == 0, "all %d x in M_2(B)" % S.size)


# ==========================================================================
# 9.  main
# ==========================================================================

# (q, t, n, expected Phase-1 count of cyclic codes or None)
PLAN = [
    (2, 1, 1, None),
    (2, 1, 2, None),
    (2, 2, 1, None),
    (4, 1, 1, 7),
    (9, 1, 1, 12),
    (2, 1, 3, None),
    (2, 3, 1, None),
    (8, 1, 1, 11),
    (4, 1, 2, 33),
    (4, 2, 1, 33),
    (2, 2, 2, None),      # wild model  F_2[u,eps]/<u^2,eps^2>
]

PLAN_TARGETED = [
    (4, 1, 3, 343),       # B = F_4^3 : submodule lattice exhaustive, ideals targeted
]


def run_targeted(q, t, n, phase1_count):
    """submodule lattice exhaustive; mu_S by exhibited generators + the
    semisimple-quotient lower bound (no scan over S)."""
    import random
    rng = random.Random(SEED)
    F = Field(*field_params(q))
    Br = BRing(F, t, n)
    P = PMod(Br)
    S = SMat(Br)
    tag = "(%d,%d,%d)" % (q, t, n)
    say("")
    say("#" * 96)
    say("#  B = A_t[X]/<X^n-1> at (q,t,n) = %s   |B| = %d, |B^2| = %d, |S| = %d"
        % (tag, Br.size, len(P.elems), S.size))
    say("#  (|S| too large for an exhaustive ideal scan: submodules exhaustive,")
    say("#   mu_S by exhibited generators + Nakayama lower bound)")
    say("#" * 96)
    ring_sanity(Br, tag)
    cyc = cyclic_submodules(P)
    sub_lv, complete = lattice_levels(P.LA, cyc)
    say("  submodule lattice: %d submodules (%s), mu_B distribution %s"
        % (len(sub_lv), "exhaustive" if complete else "PARTIAL",
           sorted(Counter(sub_lv.values()).items())))
    if phase1_count is not None:
        check("%s: #submodules equals the Phase-1 cyclic-code count" % tag,
              len(sub_lv) == phase1_count, "%d vs %d" % (len(sub_lv), phase1_count))
    Jkey = nilradical_B(Br)
    redB, dq = quotient_map(Lin(F, Br.dim), Jkey)
    Kdim = dq
    JSkey = S.LA.span([S.vec(S.e_jl(j, l, Br.from_vec(c)))
                       for c in Jkey for j in (0, 1) for l in (0, 1)])
    # build ceil(mu_B/2) generators for each W by packing a minimal generating set
    bad_up = bad_low = 0
    muS_vals = Counter()
    for Wk, muB in sub_lv.items():
        gens = minimal_generators(P, Wk, muB)
        assert len(gens) == muB and P.gen(gens) == Wk, (len(gens), muB)
        packed = []
        k = -(-len(gens) // 2)
        for i in range(k):
            w1 = gens[2 * i] if 2 * i < len(gens) else P.zero
            w2 = gens[2 * i + 1] if 2 * i + 1 < len(gens) else P.zero
            packed.append(S.mat_with_cols(w1, w2))
        Ik = I_of_W(S, Wk)
        span = ()
        for g in packed:
            span = S.LA.sum(span, S.principal(g))
        if span != Ik:
            bad_up += 1
        # lower bound from I / I J(S)
        vecs = []
        for c in Ik:
            M = S.from_vec(c)
            for cc in JSkey:
                vecs.append(S.vec(S.mul(M, S.from_vec(cc))))
        IJ = S.LA.span(vecs)
        dI = len(Ik) - len(IJ)
        low = -(-dI // (4 * Kdim)) if dI else 0
        if low > k:
            bad_low += 1
        muS_vals[k if low == k else "?"] += 1
    check("%s: ceil(mu_B/2) packed generators do generate I_W" % tag,
          bad_up == 0, "%d submodules" % len(sub_lv))
    check("%s: the Nakayama lower bound never exceeds ceil(mu_B/2)" % tag,
          bad_low == 0, "%d submodules" % len(sub_lv))
    say("  mu_S (= ceil(mu_B/2), certified above and below): %s"
        % sorted(muS_vals.items()))


def main():
    import random
    say("PHASE 2 -- STAGE 2A: MORITA CORRESPONDENCE AND GENERATOR NUMBERS")
    say("script: phase2_stage2a_morita_checks.py")
    print("date:   %s (UTC)" % time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    say("seed:   %d   (all sampling is deterministic)" % SEED)
    say("python: %s" % sys.version.split()[0])
    say("document: 03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md")
    say("")
    say("Conventions: P = B^2 columns (right B-module); S = M_2(B) = End_B(P_B)")
    say("             acts by LEFT multiplication; I_W = {M : im M subset W};")
    say("             W(I) = sum_{M in I} im M;  mu(0) = 0;  principal <=> mu <= 1.")
    say("")
    say("Every right ideal xS is computed as span_{F_q}{xN : N in the F_q-basis")
    say("of S} -- never from im(x).  Minimal generator numbers come from three")
    say("independent methods (lattice BFS, brute-force scan, Nakayama).")

    rng = random.Random(SEED)
    for (q, t, n, cnt) in PLAN:
        run_ring(q, t, n, do_ideals=True, do_dictionary=True, rng=rng,
                 phase1_count=cnt)
    for (q, t, n, cnt) in PLAN_TARGETED:
        run_targeted(q, t, n, cnt)
    run_wild_422()
    run_projectivity_counterexample()

    say("")
    say("=" * 96)
    say("SUMMARY")
    say("=" * 96)
    say("  %d checks, %d PASS, %d FAIL"
        % (NCHECK[0], NCHECK[0] - len(FAILURES), len(FAILURES)))
    print("  elapsed %.1f s" % (time.time() - T0))
    if FAILURES:
        say("  FAILURES:")
        for (nm, det) in FAILURES:
            say("    - %s : %s" % (nm, det))
    else:
        say("  no failures")
    say("  end of log")

    with open("phase2_stage2a_morita_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
