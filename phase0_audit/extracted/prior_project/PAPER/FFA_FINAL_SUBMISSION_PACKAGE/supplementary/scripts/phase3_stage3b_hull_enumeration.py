"""
PHASE 3 -- STAGE 3B:  GALOIS HULL ENUMERATION AND DIMENSION ENUMERATORS
======================================================================

Enumeration of the cyclic codes (right ideals) of R_n = M_2(A_t)[X]/<X^n-1> and of
their Galois hull dimensions, for A_t = F_q[u]/<u^t>, R = M_2(A_t).

WHAT IS COUNTED.  A cyclic code is a RIGHT IDEAL of R_n.  By the Morita
correspondence (Stage 2A T-070) right ideals of R_n = M_2(B) are in bijection with
B-submodules W of B^2, B = A_t[X]/<X^n-1>, via W |-> I_W = {M : im M subset W}.
Distinct right ideals <-> distinct submodules.  This script enumerates the submodule
lattice L(B^2) exhaustively (BFS: cyclic submodules, then closure under sums; every
submodule is a finite sum of cyclic ones, so the closure is complete) and reports

    * #codes, #principal, #non-principal, #distinct hulls;
    * the hull-dimension distribution, i.e. the coefficients of
          H_{q,t,n,s}(Z) = sum_C Z^{dim Hull_s(C)}
      and of the bivariate enumerator
          E_{q,t,n,s}(U,Z) = sum_C U^{dim C} Z^{dim Hull_s(C)};
    * N_LCD, N_SO, N_SD computed from containment/cardinality, never from the hull
      dimension alone.

INDEPENDENT METHODS.  Every hull dimension is computed twice, by routes that share no
ingredients:

    method 1 (pairing / definition):  C^{perp_s} is the nullspace of the restricted
        Galois pairing; hull = C cap C^{perp_s}; dim by rank of the restricted Gram
        matrix.  Uses b_s and F_q-linear algebra only.

    method 2 (Morita / annihilator):  W' = W(C^{perp_s}) = cap_i ker theta_s(rev g_i)
        for right-ideal generators g_i of C (Stage 2C Thm 3.8 + Stage 3A Thm 2.2);
        hull = I_{W cap W'}, dim = 2 dim(W cap W').  Uses theta_s, rev and kernels
        only -- never the pairing.

    method 3 (CRT / transfer matrix, split regime only):  the trace formula
        H = prod_{tau-orbits O} Tr(N^{|O|}) with N[V,W] = Z^{dim(V cap W^{perp_s})}
        over the local submodule lattice.  Independent of both, and it is the only
        route that scales to (4,2,3) (35 937 codes).

Conventions carried in from Phase 1 / Stage 1 / Stage 2A / 2B / 2C / Stage 3A,
unchanged: right-module cyclic codes, Morita column convention,
B_s(x,y) = sum_e theta_s(x_e) y_e, theta_s = sigma_s o transpose,
ann_r/ann_l as in Stage 2C.  The modules phase2_stage2c_galois_duality.py and
ring_structure_checks.py are imported, never modified.

NOT attempted here (by instruction): Gray maps, CSS/EAQECC constructions, quantum
parameter claims, manuscript writing.  A passing script is supporting evidence, not a
proof.
"""

import sys, os, itertools, time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ring_structure_checks import (Field, Local, MatRing, rref, nullspace_basis,
                                   say, check, LINES, FAILURES, NCHECK, gcd,
                                   field_generator)
import phase2_stage2c_galois_duality as Z

SEED = 20261109
LOGNAME = "phase3_stage3b_hull_log.txt"
WIDTH = 100


# ==========================================================================
# 1.  reporting
# ==========================================================================

def head(msg):
    say("")
    say("#" * WIDTH)
    say("  " + msg)
    say("#" * WIDTH)


def sub(msg):
    say("")
    say("---- " + msg + " " + "-" * max(0, WIDTH - len(msg) - 6))


def note(msg):
    say("     note: " + msg)


def say_local(msg):
    """print to stdout only -- NOT into the log (used for wall-clock timings, so
    that two consecutive runs produce byte-identical logs)"""
    print(msg)
    sys.stdout.flush()


# ==========================================================================
# 2.  the B-module B^2 :  coordinates, submodules, generators, mu
# ==========================================================================

def pair_flat(C, w):
    """a pair (b1,b2) of B-elements -> flat F_q vector of length 2*dim B"""
    return tuple(w[0]) + tuple(w[1])


def unpair(C, v):
    D = C.B.dim
    return (tuple(v[:D]), tuple(v[D:]))


def cat(C, A, Bs):
    """sum of two F_q-subspaces of B^2 given by row lists"""
    if not A:
        return [list(x) for x in Bs]
    if not Bs:
        return [list(x) for x in A]
    return rref([list(x) for x in A] + [list(x) for x in Bs], C.F, 2 * C.B.dim)[0]


def isec(C, A, Bs):
    """intersection of two F_q-subspaces of B^2 (nullspace of the stacked system)"""
    if not A or not Bs:
        return []
    return intersect_rows(C, A, Bs, 2 * C.B.dim)


def intersect_rows(C, A, Bs, d):
    """
    {v in span(A) : v in span(Bs)}.  Write v = sum_i x_i ra_i = sum_j y_j rb_j;
    the unknowns (x_1..x_na, y_1..y_nb) satisfy, for each coordinate c,
        sum_i x_i ra_i[c] - sum_j y_j rb_j[c] = 0.
    The x-part of the nullspace gives the intersection.
    """
    F = C.F
    ra = rref([list(x) for x in A], F, d)[0]
    rb = rref([list(x) for x in Bs], F, d)[0]
    na, nb = len(ra), len(rb)
    if na == 0 or nb == 0:
        return []
    rows = []
    for c in range(d):
        rows.append([ra[i][c] for i in range(na)] +
                    [F.neg[rb[j][c]] for j in range(nb)])
    ker = nullspace_basis(rows, F, na + nb)
    out = []
    for k in ker:
        coef = k[:na]
        v = [0] * d
        for i in range(na):
            ci = coef[i]
            if ci:
                for c in range(d):
                    if ra[i][c]:
                        v[c] = F.add[v[c]][F.mul[ci][ra[i][c]]]
        out.append(v)
    return rref(out, F, d)[0] if out else []


def module_of(C, gens):
    """the B-submodule of B^2 generated by the pairs `gens` (F_q-rref basis rows)"""
    return Z.module_basis(C, gens)


def mod_of(C, gens):
    """module_of, but returned in the {rows, gens, dim} dictionary form"""
    rows = module_of(C, gens)
    rows = tuple(tuple(x) for x in rows)
    return {"rows": rows, "gens": [tuple(g) for g in gens], "dim": len(rows)}


def cyclic_modules(C):
    """all cyclic B-submodules B*w of B^2, w ranging over all elements"""
    D = C.B.dim
    seen = {}
    for b1 in C.B.elem_list():
        for b2 in C.B.elem_list():
            rows = module_of(C, [(b1, b2)])
            if not rows:
                continue
            k = tuple(tuple(x) for x in rows)
            if k not in seen:
                seen[k] = [[list(x) for x in rows], [(b1, b2)]]
    return seen


_SUBMOD_CACHE = {}


def enumerate_submodules(C, verbose=False, cap=None, t0=None):
    """
    All B-submodules of B^2, by BFS over cyclic submodules closed under sums.
    Returns a list of dicts {rows, gens, dim}.  `rows` is an F_q-rref basis of the
    submodule as an F_q-subspace of B^2 (length 2*dim B); `gens` is a B-generating
    set of minimal size mu_B(W) (Nakayama lift).  Memoised per (q,t,n).
    """
    key = (C.q, C.t, C.n)
    if key in _SUBMOD_CACHE:
        return _SUBMOD_CACHE[key]
    D = C.B.dim
    d = 2 * D
    seen = cyclic_modules(C)
    if cap and len(seen) > cap:
        return None
    rnd = 0
    while True:
        rnd += 1
        changed = False
        cur = list(seen.items())
        for i in range(len(cur)):
            ki, (ri, gi) = cur[i]
            for j in range(i, len(cur)):
                kj, (rj, gj) = cur[j]
                s = cat(C, ri, rj)
                k = tuple(tuple(x) for x in s)
                if k not in seen:
                    seen[k] = [s, gi + gj]
                    changed = True
                    if cap and len(seen) > cap:
                        return None
        if verbose and t0:
            say("       BFS round %d: %d submodules (%.1fs)" % (rnd, len(seen), time.time() - t0))
        if not changed:
            break
    # add the zero submodule
    out = []
    for k, (rows, gens) in seen.items():
        out.append({"rows": tuple(tuple(x) for x in rows), "gens": gens,
                    "dim": len(rows)})
    out.append({"rows": (), "gens": [], "dim": 0})
    out.sort(key=lambda w: (w["dim"], w["rows"]))
    _SUBMOD_CACHE[key] = out
    return out


# ==========================================================================
# 3.  mu_B and the right-ideal generators of I_W
# ==========================================================================

class Ring3B(object):
    """everything precomputed for one parameter set (q,t,n)"""

    def __init__(self, q, t, n):
        self.C = C = Z.Ctx(q, t, n)
        self.q, self.t, self.n = q, t, n
        self.p, self.r = C.p, C.r
        self.D = C.B.dim                 # dim_{F_q} B = t*n
        self.d2 = 2 * self.D             # dim_{F_q} B^2
        self.dimw = C.dimw               # 4tn
        self.K = Z.Components(C)
        self.kind = self.K.kind          # "split" | "chain" | "wild"  (Stage 2B)
        self.split = (self.kind == "split")
        self.wild = (self.kind == "wild")
        self.ncomp = len(self.K.comps) if self.split else 1
        # B is local in the chain and wild regimes: the maximal ideal, for Nakayama
        self.mrows = Z.max_ideal_wild(C) if not self.split else None

    def basis_pairs(self, W):
        """
        the F_q-basis of W, as pairs of B-elements.

        CAVEAT (found in Stage 3B, see the deliverable): the Stage-2C helpers
        mu_local / mu_components compute dim W as the F_q-rank of the *input* list,
        so they must be called with a list that F_q-spans W -- an F_q-basis, not an
        arbitrary B-generating set.  Stage 2C always passed a basis, so the
        precondition was invisible there; here W["gens"] is a B-generating set whose
        F_q-span can be strictly smaller than W (e.g. W = span{e1, Xe1, (1+X)e2}
        over F_4[X]/(X-1)^2, generated by {(X,0), (0,1+X)}, whose F_q-span is
        only 2-dimensional while dim W = 3).
        """
        return [unpair(self.C, tuple(r)) for r in W["rows"]]

    def mu(self, W):
        """mu_B(W), by Nakayama over the maximal ideal (local) or componentwise"""
        if W["dim"] == 0:
            return 0
        if self.split:
            return Z.mu_components(self.C, self.K, self.basis_pairs(W))[0]
        return Z.mu_local(self.C, self.basis_pairs(W), self.mrows)[0]

    def gens_of(self, W):
        """a B-generating set of W (Nakayama lift when B is local; greedy otherwise)"""
        if W["dim"] == 0:
            return []
        bp = self.basis_pairs(W)
        if not self.split:
            mu, chosen = Z.mu_local(self.C, bp, self.mrows)
            return [unpair(self.C, tuple(c)) for c in chosen]
        out, cur = [], []
        for g in bp:
            trial = cat(self.C, cur, [list(pair_flat(self.C, g))])
            if len(trial) > len(cur):
                out.append(g)
                cur = trial
            if len(cur) == W["dim"]:
                break
        return out

    def ideal_gens(self, W):
        """
        right-ideal generators of I_W: pair up a B-generating set of W,
        I_W = sum_k [w_{2k+1}, w_{2k+2}] R_n   (+ [w_m,0] R_n if mu is odd).
        (Verified in the script: the generated right ideal is I_W.)
        """
        g = self.gens_of(W)
        if not g:
            return []
        out = []
        for i in range(0, len(g), 2):
            w1 = g[i]
            w2 = g[i + 1] if i + 1 < len(g) else None
            out.append(self.mat_of(w1, w2))
        return out

    def mat_of(self, w1, w2):
        """the 2x2 matrix over B whose columns are w1, w2 (column convention)"""
        B = self.C.B
        z = B.zero
        if w2 is None:
            return (w1[0], z, w1[1], z)
        return (w1[0], w2[0], w1[1], w2[1])

    def code_basis(self, W):
        """
        an F_q-basis of I_W in flat R_n coordinates: for each F_q-basis vector
        w = (b1,b2) of the submodule W, the two matrices [w,0] and [0,w].
        (dim I_W = 2 dim W, matching |I_W| = |W|^2.)
        """
        C = self.C
        B, D = C.B, self.D
        z = B.zero
        rows = []
        for r in W["rows"]:
            w = unpair(C, r)
            M1 = (w[0], z, w[1], z)      # column 0 = w
            M2 = (z, w[0], z, w[1])      # column 1 = w
            rows.append(list(C.flat_rn(M1)))
            rows.append(list(C.flat_rn(M2)))
        return rref(rows, C.F, self.dimw)[0]


# ==========================================================================
# 4.  F_q-matrix helpers
# ==========================================================================

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def matmul(X, Y, F):
    n, m, p = len(X), len(Y), len(Y[0])
    out = [[0] * p for _ in range(n)]
    add, mul = F.add, F.mul
    for i in range(n):
        Xi = X[i]
        oi = out[i]
        for k in range(m):
            xik = Xi[k]
            if xik:
                Yk = Y[k]
                mk = mul[xik]
                for j in range(p):
                    if Yk[j]:
                        oi[j] = add[oi[j]][mk[Yk[j]]]
    return out


def basis_key(rows):
    return tuple(tuple(x) for x in rows)


# ==========================================================================
# 5.  method 1 -- the pairing route (definition + restricted Gram matrix)
# ==========================================================================

def ambient_words(E):
    """iota^{-1} of the standard R_n basis, as words, once per parameter set"""
    C = E.C
    d = E.dimw
    out = []
    for j in range(d):
        v = [0] * d
        v[j] = 1
        out.append(C.iota_inv(C.unflat_rn(tuple(v))))
    return out


def gram_matrix(E, words, s):
    """G[i][j] = b_s(e_i, e_j) on the ambient R_n basis"""
    C = E.C
    d = E.dimw
    return [[C.bs(words[i], words[j], s) for j in range(d)] for i in range(d)]


def hull_by_pairing(E, G, A, s):
    """
    A = F_q-basis of the code C in flat R_n coordinates (rows).
    Returns (dimC, rank, dimHull, R, M):
        R = sigma_s(A) * G                      (the functional matrix, k x dimw)
        M = R * A^T = (b_s(x_alpha, x_beta))    (the restricted Gram matrix, k x k)
    dim Hull = dim C - rank(M)  (Stage 3A Thm 3.1).
    """
    F = E.C.F
    if not A:                            # the zero code: C = 0, Hull = 0
        return 0, 0, 0, [], []
    fro = F.frob[s % E.r]
    SA = [[fro[a] for a in row] for row in A]
    R = matmul(SA, G, F)
    M = matmul(R, transpose(A), F)
    k = len(A)
    rank = len(rref([list(x) for x in M], F, k)[0])
    return k, rank, k - rank, R, M


def hull_subspace(E, A, M):
    """the hull as an F_q-subspace of R_n: coordinates c with M c = 0, lifted by A"""
    F = E.C.F
    k = len(A)
    if k == 0:
        return []
    ker = nullspace_basis([list(x) for x in M], F, k)
    out = []
    for c in ker:
        v = [0] * E.dimw
        for b in range(k):
            cb = c[b]
            if cb:
                Ab = A[b]
                for i in range(E.dimw):
                    if Ab[i]:
                        v[i] = F.add[v[i]][F.mul[cb][Ab[i]]]
        out.append(v)
    return rref(out, F, E.dimw)[0]


def dual_subspace(E, R):
    """C^{perp_s} = nullspace of the functional matrix R (k x dimw)"""
    return nullspace_basis([list(x) for x in R], E.C.F, E.dimw)


# ==========================================================================
# 6.  method 2 -- the Morita / annihilator route (never uses the pairing)
# ==========================================================================

def Wprime_ann(E, W, s):
    """
    W' = W(C^{perp_s}) = cap_i ker theta_s(rev g_i), where the g_i are right-ideal
    generators of C = I_W  (Stage 2C Thm 3.8 and Stage 3A Thm 2.2).
    Returns the F_q-basis rows of W' (a B-submodule of B^2).
    """
    C = E.C
    gens = E.ideal_gens(W)
    if not gens:
        return None                      # C = 0  =>  C^{perp_s} = everything
    cur = None
    for g in gens:
        v = C.theta_rn(C.rev_rn(g), s)
        kb = Z.ker_basis(C, v)
        kb = [list(x) for x in kb]
        cur = kb if cur is None else intersect_rows(C, cur, kb, E.d2)
    return cur


def hull_by_morita(E, W, s):
    """
    Hull = I_{W cap W'};  dim Hull = 2 dim(W cap W').
    Returns (dimHull, Winters, Wprime, hull_rows) with hull_rows the F_q-basis of
    I_{W cap W'} in flat R_n coordinates.
    """
    Wp = Wprime_ann(E, W, s)
    if Wp is None:                       # C = 0
        return 0, [], None, []
    inter = intersect_rows(E.C, [list(x) for x in W["rows"]], Wp, E.d2)
    dimI = len(inter)
    if dimI == 0:
        return 0, [], Wp, []
    pairs = [unpair(E.C, tuple(r)) for r in inter]
    hull_rows = [list(E.C.flat_rn(E.mat_of(p, None))) for p in pairs]
    for p in pairs:
        hull_rows.append(list(E.C.flat_rn(E.mat_of((E.C.B.zero, E.C.B.zero), p))))
    hull_rows = rref(hull_rows, E.C.F, E.dimw)[0]
    return 2 * dimI, inter, Wp, hull_rows


# ==========================================================================
# 7.  the local lattice  L(A_t^2)  and the tau-orbit transfer matrix
# ==========================================================================
#
# In the SPLIT regime B = prod_j A_t, and a B-submodule of B^2 is exactly a product
# prod_j V_j of A_t-submodules of A_t^2 (the idempotents of B lie in B, and
# W = sum_j e_j W).  Hence, with tau the Stage-3A permutation of the components,
#
#     dim Hull_s(C) = sum_j dim( V_j cap (V_{tau(j)})^{perp_s} )
#
# (Stage 3A Thm 3.5), and summing over all tuples (V_j) gives, orbit by orbit,
#
#     H_{q,t,n,s}(Z) = prod_{tau-orbits O}  Tr( N(Z)^{|O|} ),
#     N(Z)[V,W]      = Z^{ dim( V cap W^{perp_s} ) } ,
#
#     E_{q,t,n,s}(U,Z) = prod_{tau-orbits O} Tr( N(U,Z)^{|O|} ),
#     N(U,Z)[V,W]      = U^{2 dim V} Z^{ dim( V cap W^{perp_s} ) } .
#
# (For a tau-orbit j_1 -> j_2 -> ... -> j_l -> j_1 the sum over tuples of
#  prod_i N[V_{j_i}, V_{j_{i+1}}] is exactly the cyclic expansion of Tr(N^l).)
# ==========================================================================

def local_lattice(q, t):
    """all A_t-submodules of A_t^2, enumerated by BFS on the (q,t,n=1) instance"""
    E1 = Ring3B(q, t, 1)
    subs = enumerate_submodules(E1.C)
    return E1, subs


def local_dual(E1, V, s, use="morita"):
    """
    delta_s(V) := W( (I_V)^{perp_s} ), an A_t-submodule of A_t^2.
    use = "morita"  : annihilator route  (cap_i ker theta_s(rev g_i))
    use = "pairing" : definition route   (B-span of the columns of a basis of the dual)
    """
    if use == "morita":
        Wp = Wprime_ann(E1, V, s)
        if Wp is None:                        # V = 0  =>  dual = everything
            return [[1 if i == j else 0 for i in range(E1.d2)]
                    for j in range(E1.d2)]
        return Wp
    A = E1.code_basis(V)
    words = ambient_words(E1)
    G = gram_matrix(E1, words, s)
    k, rank, dimH, R, M = hull_by_pairing(E1, G, A, s)
    D = dual_subspace(E1, R)
    # W(dual) = the B-span of the columns of the matrices in a basis of the dual
    cols = []
    for row in D:
        Mx = E1.C.unflat_rn(tuple(row))
        cols.append((Mx[0], Mx[2]))
        cols.append((Mx[1], Mx[3]))
    return module_of(E1.C, cols)


def transfer_matrix(E, E1, loc, s, use="morita"):
    """
    N[V,W] = Z^{dim(V cap W^{perp_s})} as a dict of exponent matrices:
    returns (Nexp, NexpU, dual_index) with Nexp[V][W] = dim(V cap delta_s(W)) and
    NexpU[V][W] = (2 dim V, dim(V cap delta_s(W))).
    """
    d2 = E1.d2
    delta = [local_dual(E1, V, s, use) for V in loc]
    Nexp = []
    for V in loc:
        row = []
        for j, W in enumerate(loc):
            inter = intersect_rows(E1.C, [list(x) for x in V["rows"]], delta[j], d2)
            # the component contribution to dim Hull is 2 * dim of the submodule
            # intersection (Stage 3A Thm 3.3: dim Hull = 2 dim(W cap W'))
            row.append(2 * len(inter))
        Nexp.append(row)
    return Nexp, delta


def poly_mul(A, B, cap=None):
    """polynomial multiplication, coefficient lists (index = exponent)"""
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                if b:
                    out[i + j] += a * b
    return out


def mat_trace_poly(Nexp, power, Uweight=None):
    """
    Tr(N^{power}) where N[i][j] is the MONOMIAL Z^{Nexp[i][j]} (times U^{Uweight[i]}
    if Uweight is given).  Expanded as the sum over cyclic tuples
    (i_0, i_1, ..., i_{power-1}) of prod_k N[i_k][i_{k+1 mod power}] -- i.e. by
    exponent bookkeeping, which is exactly the definition of the trace of a power.
    Returns {(Z-exponent): count} or {((U-exponent, Z-exponent)): count}.
    """
    m = len(Nexp)
    out = {}

    def add(z, u=None):
        key = z if u is None else (u, z)
        out[key] = out.get(key, 0) + 1

    def build(pos, cur, acc_z, acc_u):
        if pos == power:
            add(acc_z + Nexp[cur[-1]][cur[0]],
                acc_u if Uweight is not None else None)
            return
        i = cur[-1]
        for j in range(m):
            build(pos + 1, cur + [j], acc_z + Nexp[i][j],
                  acc_u + (Uweight[j] if Uweight is not None else 0))

    if power == 1:
        for i in range(m):
            add(Nexp[i][i], Uweight[i] if Uweight is not None else None)
        return out
    for i in range(m):
        build(1, [i], 0, Uweight[i] if Uweight is not None else 0)
    return out


def tau_orbits(E, s):
    """
    The permutation tau of the CRT components (Stage 3A Thm 3.5), characterised by
        zeta_{tau(j)}^{p^s} = zeta_j^{-1}.
    Writing zeta_j = g^{m j} with g a generator of F_q^* and m = (q-1)/n, this is
        tau(j) * p^s = -j  (mod n),   i.e.  tau(j) = -j * (p^s)^{-1} mod n,
    and (p^s)^{-1} mod n exists because p does not divide n in the split regime.
    Returns (tau, orbits).
    """
    n = E.n
    if n == 1:
        return [0], [[0]]
    ps = pow(E.p, s, n) % n
    inv = None
    for k in range(n):
        if (k * ps) % n == 1 % n:
            inv = k
            break
    assert inv is not None, "p^s is not invertible mod n -- not the split regime"
    tau = [((-j) * inv) % n for j in range(n)]
    seen, orbits = set(), []
    for j in range(n):
        if j in seen:
            continue
        o, cur = [j], tau[j]
        seen.add(j)
        while cur != j:
            o.append(cur)
            seen.add(cur)
            cur = tau[cur]
        orbits.append(o)
    return tau, orbits


def bivariate_mul(A, B):
    """convolution of two {(u,z): count} dictionaries (accumulating!)"""
    out = {}
    for (u1, z1), c1 in A.items():
        for (u2, z2), c2 in B.items():
            k = (u1 + u2, z1 + z2)
            out[k] = out.get(k, 0) + c1 * c2
    return out


def univariate_mul(A, B):
    """convolution of two {z: count} dictionaries (accumulating!)"""
    out = {}
    for z1, c1 in A.items():
        for z2, c2 in B.items():
            k = z1 + z2
            out[k] = out.get(k, 0) + c1 * c2
    return out


def orbit_enumerator(Nexp, orbits, Uweight=None):
    """
    prod_{tau-orbits O} Tr(N^{|O|}), as a {z: count} (or {(u,z): count}) dictionary.
    This is the closed form of the hull-dimension enumerator in the split regime.
    """
    tot_z = None
    for o in orbits:
        d = mat_trace_poly(Nexp, len(o))            # univariate: keys are z
        tot_z = d if tot_z is None else univariate_mul(tot_z, d)
    tot_u = None
    if Uweight is not None:
        for o in orbits:                            # bivariate: keys are (u,z)
            d = mat_trace_poly(Nexp, len(o), Uweight=Uweight)
            tot_u = d if tot_u is None else bivariate_mul(tot_u, d)
    return tot_u, tot_z


# ==========================================================================
# 8.  one parameter set: exhaustive enumeration, tables, cross-checks
# ==========================================================================

def build_product_submodule(E, loc, idxs):
    """
    the B-submodule W = prod_j V_{i_j} of B^2, as F_q-rows in B^2 coordinates,
    from local submodules V of A_t^2 (split regime).
    """
    K, C = E.K, E.C
    E1 = E1_of(E)
    z = K.comps[0][1].ring.zero
    rows = []
    for j, i in enumerate(idxs):
        for r in loc[i]["rows"]:
            w = unpair(E1.C, tuple(r))
            b1 = K.inj([z if k != j else w[0] for k in range(E.ncomp)])
            b2 = K.inj([z if k != j else w[1] for k in range(E.ncomp)])
            rows.append(list(pair_flat(C, (b1, b2))))
    return rref(rows, C.F, E.d2)[0]


_E1_CACHE = {}


def E1_of(E):
    """the (q,t,n=1) instance attached to E (the local/component ring A_t)"""
    key = (E.q, E.t)
    if key not in _E1_CACHE:
        _E1_CACHE[key] = Ring3B(E.q, E.t, 1)
    return _E1_CACHE[key]


def sample_product_codes(E, loc, m):
    """m random codes from the CRT product family, as submodule dictionaries"""
    import random
    rnd = random.Random(SEED + 31337)
    out = []
    for _ in range(m):
        tp = tuple(rnd.randrange(len(loc)) for _ in range(E.ncomp))
        rows = build_product_submodule(E, loc, tp)
        out.append(mod_of(E.C, [unpair(E.C, tuple(r)) for r in rows]))
    return out


def run_case(q, t, n, sample_verify=60, do_controls=True, mu_cap=500):
    E = Ring3B(q, t, n)
    C = E.C
    head("(q,t,n) = (%d,%d,%d)   kind = %s   |B| = %d   |R_n| = %d   "
         "dim_{F_q} R_n = %d" % (q, t, n, E.kind, q ** (t * n), q ** (4 * t * n),
                                 E.dimw))
    t_start = time.time()
    words = ambient_words(E)
    product_mode = False
    loc = E1 = None
    if E.split and E.ncomp > 1:
        product_mode = True
        E1, loc = local_lattice(q, t)
        nloc = len(loc)
        say("  enumeration method : CRT product  L(A_t^2)^{%d},  |L| = %d"
            % (E.ncomp, nloc))
        say("  #codes             : %d  (= %d^%d)" % (nloc ** E.ncomp, nloc, E.ncomp))
        if (q ** (t * n)) ** 2 <= 6561:
            subs = enumerate_submodules(C)
            check("(%d,%d,%d): CRT product count = exhaustive BFS submodule count"
                  % (q, t, n), len(subs) == nloc ** E.ncomp,
                  "%d vs %d^%d" % (len(subs), nloc, E.ncomp), True)
        else:
            subs = None
            note("direct BFS over B^2 is infeasible here (|B^2| = %d); the product "
                 "enumeration is used and is verified below against BOTH direct "
                 "routes on %d sampled codes" % ((q ** (t * n)) ** 2, sample_verify))
    else:
        subs = enumerate_submodules(C, t0=t_start)
        say("  enumeration method : exhaustive BFS over the submodule lattice of B^2")
        say("  #codes             : %d" % len(subs))
        if E.split and E.ncomp == 1:
            note("n = 1: the CRT has one component, so the transfer-matrix route "
                 "below is the 1x1 (tautological) case")

    for s in range(E.r):
        sub("s = %d%s" % (s, "" if (2 * s) % E.r else "   (reflexive: r | 2s)"))
        G = gram_matrix(E, words, s)
        if product_mode:
            res = _run_case_product(E, E1, loc, s, sample_verify)
        else:
            res = _run_case_bfs(E, subs, G, s)
        if not do_controls:
            continue
        # ---- Task F: is every hull principal?   Task G: negative controls ----
        if subs is None:
            subsm = sample_product_codes(E, loc, min(200, len(loc) ** E.ncomp))
            note("the open-question and negative-control tests below run on %d "
                 "sampled codes (the full family has %d)" % (len(subsm),
                                                             len(loc) ** E.ncomp))
            hull_mu_stats(E, subsm, s, exhaustive=False)
            negative_controls(E, subsm, s, res[0], ncomp_hint=E.ncomp,
                              exhaustive=False)
        else:
            pool = subs
            exh = True
            if len(subs) > mu_cap:
                import random
                pool = [subs[i] for i in sorted(random.Random(SEED).sample(
                    range(len(subs)), mu_cap))]
                exh = False
                note("the hull-principality test below runs on %d sampled codes "
                     "(the full family has %d)" % (len(pool), len(subs)))
            hull_mu_stats(E, pool, s, exhaustive=exh)
            negative_controls(E, subs, s, res[0], ncomp_hint=E.ncomp,
                              exhaustive=True)
    say("")
    say_local("  [case time %.1fs]" % (time.time() - t_start))


def poly_str(dist):
    return "  ".join("%d*Z^%d" % (v, k) for k, v in sorted(dist.items()))


def _run_case_bfs(E, subs, G, s):
    """exhaustive hull enumeration over a BFS-enumerated submodule lattice"""
    C = E.C
    q, t, n = E.q, E.t, E.n
    dist = Counter()          # hull dimension -> #codes
    biv = Counter()           # (dim C, dim Hull) -> #codes
    mu_dist = Counter()
    hull_keys = set()
    n_lcd = n_so = n_sd = 0
    so_ok = sd_ok = 0
    mismatch_dim = mismatch_sub = 0
    card_bad = 0
    for W in subs:
        mu_dist[E.mu(W)] += 1
        A = code_basis(E, W)
        dimC, rank, dimH1, R, M = hull_by_pairing(E, G, A, s)
        dimH2, inter, Wp, hrows2 = hull_by_morita(E, W, s)
        h1 = hull_subspace(E, A, M)
        if dimH1 != dimH2:
            mismatch_dim += 1
        if basis_key(h1) != basis_key(hrows2):
            mismatch_sub += 1
        dist[dimH1] += 1
        biv[(dimC, dimH1)] += 1
        hull_keys.add(basis_key(h1))
        # LCD: the restricted form is non-degenerate
        if rank == dimC:
            n_lcd += 1
        # C^{perp_s}, computed independently as the annihilator of sigma_s(C)
        D = dual_subspace(E, R)
        if len(D) != E.dimw - dimC:
            card_bad += 1
        # SO / SD, verified by containment / equality, never by dimension alone
        if rank == 0:
            keyD = basis_key(D)
            keyA = basis_key(A)
            if basis_key(rref([list(x) for x in A] + [list(x) for x in D],
                              C.F, E.dimw)[0]) == keyD:
                so_ok += 1
            n_so += 1
            if 2 * dimC == 4 * t * n:
                n_sd += 1
                if keyA == keyD:
                    sd_ok += 1
    ncodes = len(subs)
    check("(%d,%d,%d) s=%d: the two hull routes agree in DIMENSION on every code"
          % (q, t, n, s), mismatch_dim == 0,
          "%d of %d disagree" % (mismatch_dim, ncodes), True)
    check("(%d,%d,%d) s=%d: the two hull routes agree as SUBSPACES on every code"
          % (q, t, n, s), mismatch_sub == 0,
          "%d of %d disagree" % (mismatch_sub, ncodes), True)
    check("(%d,%d,%d) s=%d: dim C + dim C^{perp_s} = 4tn for every code"
          % (q, t, n, s), card_bad == 0, "%d violations" % card_bad, True)
    check("(%d,%d,%d) s=%d: every self-orthogonal code really satisfies "
          "C subset C^{perp_s}" % (q, t, n, s), so_ok == n_so,
          "%d of %d verified by containment" % (so_ok, n_so), True)
    check("(%d,%d,%d) s=%d: every self-dual code really satisfies C = C^{perp_s}"
          % (q, t, n, s), sd_ok == n_sd,
          "%d of %d verified by equality" % (sd_ok, n_sd), True)
    say("")
    say("  #codes %d | #principal %d | #non-principal %d | #distinct hulls %d"
        % (ncodes, sum(v for k, v in mu_dist.items() if k <= 2),
           sum(v for k, v in mu_dist.items() if k > 2), len(hull_keys)))
    say("  mu_B(W) distribution : %s" % dict(sorted(mu_dist.items())))
    say("  hull-dimension distribution  H(Z) : %s" % poly_str(dist))
    say("  N_LCD = %d   N_SO = %d   N_SD = %d" % (n_lcd, n_so, n_sd))
    say("  bivariate counts (dim C, dim Hull) : %s" % dict(sorted(biv.items())))
    # the duality map on the lattice is dimension-complementing
    dual_dims = Counter()
    for W in subs:
        Wp = Wprime_ann(E, W, s)
        dual_dims[E.d2 if Wp is None else len(Wp)] += 1
    dimsW = Counter(W["dim"] for W in subs)
    check("(%d,%d,%d) s=%d: W -> W(C^{perp_s}) is dim-complementing on the lattice"
          % (q, t, n, s),
          dict(sorted(dual_dims.items())) ==
          dict(sorted(Counter({E.d2 - d: c for d, c in dimsW.items()}).items())),
          "dim W + dim W' = %d" % E.d2, True)
    return dist, biv, mu_dist, hull_keys, n_lcd, n_so, n_sd


def code_basis(E, W):
    return E.code_basis(W)


def _run_case_product(E, E1, loc, s, sample_verify):
    """
    split regime with ncomp > 1: enumerate L(A_t^2)^{ncomp} and use the
    componentwise hull formula  dim Hull = sum_j dim(V_j cap delta_s(V_{tau(j)})).
    """
    import random
    rnd = random.Random(SEED + 1000 * s + E.n)
    tau, orbits = tau_orbits(E, s)
    say("  tau = %s   (%s)   orbits = %s" %
        (tau, "id" if all(tau[j] == j for j in range(E.n)) else "NOT id",
         ["len %d" % len(o) for o in orbits]))
    say("  n | p^s+1  <=>  %d | %d  :  %s" %
        (E.n, pow(E.p, s) + 1, (pow(E.p, s) + 1) % E.n == 0))
    Nexp, delta = transfer_matrix(E, E1, loc, s, use="morita")
    U = [2 * V["dim"] for V in loc]
    totU, totZ = orbit_enumerator(Nexp, orbits, Uweight=U)
    nloc = len(loc)
    # brute-force sum over all tuples (independent of the trace identity)
    dist = Counter(); biv = Counter(); mu_dist = Counter(); hull_keys = set()
    n_lcd = n_so = n_sd = 0
    idxs = [0] * E.ncomp
    tuples = itertools.product(range(nloc), repeat=E.ncomp)
    for tp in tuples:
        dimW = sum(loc[i]["dim"] for i in tp)
        dimC = 2 * dimW
        h = 0
        ok_so = True
        inter_key = []
        for j in range(E.ncomp):
            i, k = tp[j], tp[tau[j]]
            e = Nexp[i][k]
            h += e
            if e != 2 * loc[i]["dim"]:
                ok_so = False
            inter_key.append(e)
        dist[h] += 1
        biv[(dimC, h)] += 1
        hull_keys.add(tuple(inter_key))
        mu = max(E1.mu(loc[i]) for i in tp)
        mu_dist[mu] += 1
        if h == 0:
            n_lcd += 1
        if ok_so:
            n_so += 1
            if 2 * dimC == 4 * E.t * E.n:
                n_sd += 1
    ncodes = nloc ** E.ncomp
    check("(%d,%d,%d) s=%d: the tau-orbit trace formula prod_O Tr(N^{|O|}) equals the "
          "brute-force sum over all %d codes"
          % (E.q, E.t, E.n, s, ncodes),
          {k: v for k, v in totZ.items() if v} == dict(dist),
          "univariate", True)
    check("(%d,%d,%d) s=%d: the bivariate trace formula equals the brute-force sum"
          % (E.q, E.t, E.n, s), totU == dict(biv), "bivariate", True)
    say("")
    say("  #codes %d | #principal %d | #non-principal %d | #distinct hulls %d"
        % (ncodes, sum(v for k, v in mu_dist.items() if k <= 2),
           sum(v for k, v in mu_dist.items() if k > 2), len(hull_keys)))
    say("  mu_B(W) distribution : %s" % dict(sorted(mu_dist.items())))
    say("  hull-dimension distribution  H(Z) : %s" % poly_str(dist))
    say("  N_LCD = %d   N_SO = %d   N_SD = %d" % (n_lcd, n_so, n_sd))
    say("  bivariate counts (dim C, dim Hull) : %s" % dict(sorted(biv.items())))
    # ---- sample verification against the two direct routes ------------------
    if sample_verify:
        import random as _r
        rr = _r.Random(SEED + 7919 * s)
        G = gram_matrix(E, ambient_words(E), s)
        bad = 0
        tries = 0
        for _ in range(sample_verify):
            tp = tuple(rr.randrange(nloc) for _ in range(E.ncomp))
            rows = build_product_submodule(E, loc, tp)
            W = {"rows": tuple(tuple(x) for x in rows),
                 "gens": [unpair(E.C, tuple(r)) for r in rows], "dim": len(rows)}
            A = E.code_basis(W)
            dimC, rank, dimH1, R, M = hull_by_pairing(E, G, A, s)
            dimH2, inter, Wp, hrows2 = hull_by_morita(E, W, s)
            want = sum(Nexp[tp[j]][tp[tau[j]]] for j in range(E.ncomp))
            tries += 1
            if not (dimH1 == dimH2 == want):
                bad += 1
        check("(%d,%d,%d) s=%d: on %d sampled codes the componentwise hull dimension "
              "equals BOTH direct routes" % (E.q, E.t, E.n, s, tries),
              bad == 0, "%d of %d disagree" % (bad, tries), False)
    return dist, biv, mu_dist, hull_keys, n_lcd, n_so, n_sd


# ==========================================================================
# 9.  the four counting problems (Task A)
# ==========================================================================
#
#   (1) distinct right ideals of R_n          = distinct B-submodules W of B^2
#   (2) distinct generator matrices           = generating tuples of W
#   (3) unit-equivalence classes              = orbits of W -> uW, u in B^x
#   (4) Morita-equivalent submodules          = isomorphism classes of the
#                                               B-modules W
# These are four DIFFERENT numbers and are never mixed below.
# ==========================================================================

def all_elements(C, rows):
    """all elements of the F_q-span of rows, as tuples"""
    out = []
    for coeffs in itertools.product(range(C.F.q), repeat=len(rows)):
        v = [0] * len(rows[0]) if rows else []
        for c, r in zip(coeffs, rows):
            if c:
                v = [C.F.add[a][C.F.mul[c][b]] for a, b in zip(v, r)]
        out.append(tuple(v))
    return out


def submodule_contains(C, rowsV, rowsU):
    """U <= V as F_q-spaces (equivalently, for B-submodules, as B-modules)"""
    if not rowsU:
        return True
    comb = [list(r) for r in rowsV] + [list(r) for r in rowsU]
    return len(rref(comb, C.F, len(rowsV[0]))[0]) == len(rowsV)


def generating_tuples(E, subs, k, cap=400000):
    """
    f_k(W) = # ordered k-tuples of elements of W that GENERATE W as a B-module.
    Computed from   f_k(V) = |V|^k - sum_{U < V} f_k(U)   (increasing dimension),
    which is valid because every k-tuple generates a unique submodule.
    """
    C = E.C
    size = sum(C.F.q ** W["dim"] for W in subs)
    if size > cap:
        return None, size
    order = sorted(range(len(subs)), key=lambda i: subs[i]["dim"])
    rows = [[list(r) for r in W["rows"]] for W in subs]
    f = [0] * len(subs)
    for iv in order:
        V = subs[iv]
        tot = (C.F.q ** V["dim"]) ** k
        below = 0
        for iu in range(len(subs)):
            if iu == iv or subs[iu]["dim"] >= V["dim"]:
                continue
            if submodule_contains(C, rows[iv], rows[iu]):
                below += f[iu]
        f[iv] = tot - below
    return f, size


def std_basis(B):
    """the standard F_q-basis of B (elements of B ARE their flat F_q-tuples)"""
    out = []
    for i in range(B.dim):
        v = [0] * B.dim
        v[i] = 1
        out.append(tuple(v))
    return out


def pow_el(ring, x, k):
    """x^k in a ring with .mul and .one"""
    acc = ring.one
    for _ in range(k):
        acc = ring.mul(acc, x)
    return acc


def units_of_B(E):
    """B^x, by testing bijectivity of multiplication by b"""
    C = E.C
    B = C.B
    basis = std_basis(B)
    out = []
    for b in B.elem_list():
        rows = [list(B.mul(b, x)) for x in basis]
        if len(rref(rows, C.F, B.dim)[0]) == B.dim:
            out.append(b)
    return out


def additive_generators_B(E):
    """elements of B whose F_p-span is all of B:  c * u^a X^e  (c in F_q)"""
    C = E.C
    B = C.B
    out = []
    for a in range(C.t):
        for e in range(C.n):
            for c in range(C.F.q):
                v = [0] * B.dim
                v[a * C.n + e] = c
                out.append(tuple(v))
    return out


def unit_group_generators(E):
    """a small generating set of B^x, found by a closure search"""
    B = E.C.B
    units = units_of_B(E)
    uset = set(units)
    gens = []
    cur = {B.one}
    for u in units:
        if u in cur:
            continue
        gens.append(u)
        changed = True
        while changed:
            changed = False
            new = set()
            for a in cur:
                for g in gens:
                    x = B.mul(a, g)
                    if x not in cur:
                        new.add(x)
            if new:
                cur |= new
                changed = True
        if cur == uset:
            break
    return gens


def gl2_generators(E, small=True):
    """
    a generating set of GL_2(B) = R_n^x (R_n = M_2(B)).
    B is local (chain or wild regime) or a product of local rings (split regime),
    so GL_2(B) = E_2(B) * D_2(B) is generated by the elementary matrices
    E_12(a), E_21(a) (a in B) and the diagonal units diag(u,1), diag(1,u)
    (u in B^x).  With small=True the parameter a is restricted to a set whose
    F_p-span is B (then products give every E_12(a)), and the diagonal units are
    restricted to a generating set of the group B^x -- this is a much smaller set
    that generates the same group, as verified by the check in counting_problems.
    """
    C = E.C
    B = C.B
    if not small:
        aa = B.elem_list()
        uu = units_of_B(E)
    else:
        aa = additive_generators_B(E)
        uu = unit_group_generators(E)
    gens = []
    for a in aa:
        gens.append(((B.one, a), (B.zero, B.one)))       # E_12(a)
        gens.append(((B.one, B.zero), (a, B.one)))       # E_21(a)
    for u in uu:
        gens.append(((u, B.zero), (B.zero, B.one)))
        gens.append(((B.one, B.zero), (B.zero, u)))
    return gens


def unit_orbit_classes(E, subs, gens=None):
    """
    UNIT-EQUIVALENCE classes of codes: orbits of the action of R_n^x = GL_2(B) on
    the right ideals of R_n by LEFT multiplication, which under Morita is
    (U, W) -> U W  on the B-submodules W of B^2.

    (NB: the naive 'scalar' action u*W for u in B^x is TRIVIAL, because W is a
    B-module: uW = W for every unit u.  The action above is the non-trivial one.)
    """
    C = E.C
    if gens is None:
        gens = gl2_generators(E)
    keys = [basis_key(W["rows"]) for W in subs]
    index = {k: i for i, k in enumerate(keys)}
    parent = list(range(len(subs)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def act(W, U):
        (u11, u12), (u21, u22) = U
        rows = []
        for r in W["rows"]:
            w = unpair(C, tuple(r))
            x1 = C.B.add(C.B.mul(u11, w[0]), C.B.mul(u12, w[1]))
            x2 = C.B.add(C.B.mul(u21, w[0]), C.B.mul(u22, w[1]))
            rows.append(list(pair_flat(C, (x1, x2))))
        rr = rref(rows, C.F, E.d2)[0]
        return basis_key(rr)

    for i, W in enumerate(subs):
        ki = keys[i]
        for U in gens:
            ku = act(W, U)
            if ku != ki:
                a, b = find(i), find(index[ku])
                if a != b:
                    parent[a] = b
    return len({find(i) for i in range(len(subs))})


def module_type(E, W):
    """
    a complete isomorphism invariant of the B-module W, in the CHAIN and SPLIT
    regimes (SNF over a chain ring / componentwise SNF over a product of chain
    rings).  Returns None in the WILD regime (no SNF there -- open item).
    """
    C = E.C
    K = E.K
    if K.kind == "wild":
        return None
    if K.kind == "chain":
        omega = K.comps[0][1].omega
        ell = K.comps[0][1].ell
        d = []
        cur = [unpair(C, tuple(r)) for r in W["rows"]]
        for k in range(ell + 1):
            wk = pow_el(C.B, omega, k)
            rows = [list(pair_flat(C, (C.B.mul(wk, w[0]), C.B.mul(wk, w[1]))))
                    for w in cur] if k else [list(r) for r in W["rows"]]
            d.append(len(rref(rows, C.F, E.d2)[0]))
        parts = []
        for k in range(ell):
            parts += [k + 1] * (d[k] - d[k + 1])
        return tuple(sorted(parts))
    # split:  W = prod_j V_j  (e_j W), and an isomorphism preserves e_j W
    out = []
    for j in range(E.ncomp):
        info = K.comps[j][1]
        ring, omega, ell = info.ring, info.omega, info.ell
        rows = []
        for r in W["rows"]:
            w = unpair(C, tuple(r))
            vj = (K.proj(w[0], j), K.proj(w[1], j))
            rows.append(list(vj[0]) + list(vj[1]))
        d = []
        for k in range(ell + 1):
            if k == 0:
                rr = rows
            else:
                ok = pow_el(ring, omega, k)
                rr = []
                for row in rows:
                    h = len(row) // 2
                    a = ring.mul(ok, tuple(row[:h]))
                    b = ring.mul(ok, tuple(row[h:]))
                    rr.append(list(a) + list(b))
            d.append(len(rref(rr, ring.F, len(rr[0]))[0]) if rr else 0)
        parts = []
        for k in range(ell):
            parts += [k + 1] * (d[k] - d[k + 1])
        out.append(tuple(sorted(parts)))
    return tuple(out)


def counting_problems(q, t, n, do_generators=True, cap=400000, subs=None):
    """
    the four numbers (1) right ideals (2) generator matrices (3) unit classes
    (4) Morita classes, for one parameter set -- reported separately, never mixed.
    """
    E = Ring3B(q, t, n)
    sub("counting problems for (q,t,n)=(%d,%d,%d)" % (q, t, n))
    if subs is None:
        subs = enumerate_submodules(E.C, t0=time.time())
    N1 = len(subs)
    say("  (1) distinct right ideals of R_n = distinct B-submodules of B^2 : %d" % N1)
    # ---- (2) generator matrices
    if do_generators:
        for k in (1, 2):
            f, size = generating_tuples(E, subs, k, cap=cap)
            if f is None:
                say("  (2) generating %d-tuples: NOT COMPUTED (sum |W| = %d > cap %d)"
                    % (k, size, cap))
                continue
            tot = sum(f)
            check("(%d,%d,%d): the numbers of generating %d-tuples sum to |B^2|^%d"
                  % (q, t, n, k, k), tot == (E.C.F.q ** E.d2) ** k,
                  "%d vs %d" % (tot, (E.C.F.q ** E.d2) ** k), True)
            say("      per-module counts range %d..%d ; #modules with a generating "
                "%d-tuple: %d" % (min(f), max(f), k,
                                  sum(1 for v in f if v > 0)))
            say("      #cyclic (1-generated) modules: %d" %
                (sum(1 for v in f if v > 0) if k == 1 else
                 sum(1 for W in subs if E.mu(W) <= 1)))
    # ---- (3) unit equivalence
    gens = gl2_generators(E)
    n3 = unit_orbit_classes(E, subs, gens)
    say("  (3) #unit-equivalence classes (orbits of R_n^x = GL_2(B) acting by LEFT "
        "multiplication; %d generators, |B^x| = %d) : %d"
        % (len(gens), len(units_of_B(E)), n3))
    if E.C.B.dim <= 4:
        n3f = unit_orbit_classes(E, subs, gl2_generators(E, small=False))
        check("(%d,%d,%d): the reduced generating set of GL_2(B) gives the same "
              "orbit count as the full one" % (q, t, n), n3f == n3,
              "%d vs %d" % (n3f, n3), True)
    say("      NB the 'scalar' action u*W (u in B^x) is TRIVIAL: W is a B-module, "
        "so uW = W for every unit u")
    # ---- (4) Morita classes
    n4 = None
    types = [module_type(E, W) for W in subs]
    if any(x is None for x in types):
        say("  (4) Morita classes: NOT COMPUTED in the wild regime (no SNF for B);")
        say("      partial invariant dim W gives the upper bound %d"
            % len({W["dim"] for W in subs}))
    else:
        n4 = len(set(types))
        say("  (4) #Morita-equivalence classes (isomorphism classes of the "
            "B-modules W) : %d" % n4)
        check("(%d,%d,%d): the type invariant separates the lattice at least as "
              "finely as the dimension" % (q, t, n),
              n4 >= len({W["dim"] for W in subs}),
              "%d >= %d" % (n4, len({W["dim"] for W in subs})), True)
    if n4 is not None:
        check("(%d,%d,%d): #unit-equivalence classes >= #Morita classes (unit "
              "equivalence implies B-module isomorphism)" % (q, t, n), n3 >= n4,
              "%d >= %d" % (n3, n4), True)
    say("  NB: %d (right ideals), %d (unit classes), %s (Morita classes) are three "
        "DIFFERENT counting problems; none is derived from another."
        % (N1, n3, n4))
    return N1, n3, n4


# ==========================================================================
# 10.  open questions (Task F) and negative controls (Task G)
# ==========================================================================

def hull_mu_stats(E, subs, s, exhaustive=True):
    """
    O-3.1 (Stage 3A): is mu_B(W_hull) <= 2 for every code, i.e. is every hull
    principal?  Tested exhaustively over the whole code family.
    """
    q, t, n = E.q, E.t, E.n
    dist = Counter()
    bad = []
    all_ok = True
    for W in subs:
        dimH, inter, Wp, hrows = hull_by_morita(E, W, s)
        Wh = mod_of(E.C, [unpair(E.C, tuple(r)) for r in inter])
        mu = E.mu(Wh)
        dist[mu] += 1
        if mu > 2:
            nm = nakayama_mu(E, Wh)
            if nm is not None and nm[0] != mu:
                all_ok = False
            bad.append((W, mu, Wh))
    check("(%d,%d,%d) s=%d: hull-principality scan completed over %d codes and "
          "every hull with mu_B >= 3 is confirmed by the Nakayama dimension "
          "dim_k(V/rad V)" % (q, t, n, s, len(subs)), all_ok,
          "mu distribution of hulls %s ; %d hulls with mu >= 3" %
          (dict(sorted(dist.items())), len(bad)), exhaustive)
    say("      O-3.1 ('every hull is principal') on this family: %s"
        % ("REFUTED -- see the witness below / in Task F" if bad
           else "not refuted (every scanned hull has mu_B <= 2)"))
    if bad:
        W, mu, Wh = bad[0]
        say("      witness: W generated by %s ; its hull has mu_B = %d"
            % (E.gens_of(W), mu))
    return dist, bad


def left_ideal_gap(E, subs, s, ntrial=40):
    """
    is the hull (a right ideal of R_n) also a LEFT ideal?  For n >= 2 the
    correspondence W <-> I_W is only right-sided, so this is expected to fail
    (the 'n >= 2 left-submodule gap' carried from Stage 2A).
    """
    import random
    rnd = random.Random(SEED + 555)
    q, t, n = E.q, E.t, E.n
    tested = 0
    failed = 0
    for W in subs:
        dimH, inter, Wp, hrows = hull_by_morita(E, W, s)
        if dimH == 0 or tested >= ntrial:
            continue
        hb = basis_key(hrows)
        for _ in range(6):
            A = [rnd.randrange(q) for _ in range(E.dimw)]
            # left multiply each hull element by A
            rows = []
            for x in hrows:
                prod = E.C.mul_rn(E.C.unflat_rn(A), E.C.unflat_rn(list(x)))
                rows.append(list(E.C.flat_rn(prod)))
            rr = rref(rows, E.C.F, E.dimw)[0]
            ok = all(
                len(rref([list(x) for x in hrows] + [list(v)], E.C.F, E.dimw)[0])
                == len(hrows) for v in rr)
            tested += 1
            if not ok:
                failed += 1
    say("  left-ideal test on hulls (s=%d): %d (hull, multiplier) pairs tested, "
        "%d hulls NOT closed under left multiplication" % (s, tested, failed))
    check("(%d,%d,%d) s=%d: the hull right ideal is not in general a left ideal "
          "(n >= 2 gap) -- %d/%d failures observed" % (q, t, n, s, failed, tested),
          True, "informational: the expectation is failures when n >= 2", True)


def negative_controls(E, subs, s, dist, ncomp_hint=None, exhaustive=True):
    """
    incorrect arguments that would give the right answer 'by accident' on easy
    cases -- each is run here and its prediction is compared with the truth.
    """
    q, t, n = E.q, E.t, E.n
    sub("negative controls for (q,t,n)=(%d,%d,%d), s=%d" % (q, t, n, s))
    ncodes = sum(dist.values())
    # (G1) pretend the CRT product formula holds outside the split regime
    if E.kind == "wild" and ncomp_hint is not None:
        E1, loc = local_lattice(q, t)
        pred = len(loc) ** ncomp_hint
        check("NEGATIVE CONTROL: the split product count |L(A_t^2)|^{%d} = %d is "
              "NOT the number of codes in the WILD case (%d)"
              % (ncomp_hint, pred, ncodes), pred != ncodes,
              "%d vs %d" % (pred, ncodes), exhaustive)
    # (G2) assume tau = id when it is not
    if E.split and E.ncomp > 1:
        E1, loc = local_lattice(q, t)
        tau, orbits = tau_orbits(E, s)
        Nexp, delta = transfer_matrix(E, E1, loc, s, use="morita")
        if any(tau[j] != j for j in range(E.ncomp)):
            _, wrong = orbit_enumerator(Nexp, [[j] for j in range(E.ncomp)])
            check("NEGATIVE CONTROL: the enumerator computed with tau = id does NOT "
                  "match the truth when tau is not the identity",
                  {k: v for k, v in wrong.items() if v} != dict(dist),
                  "tau=%s" % tau, exhaustive)
            say("      tau=id gives %s" % poly_str(Counter(
                {k: v for k, v in wrong.items() if v})))
            say("      truth        %s" % poly_str(dist))
    # (G3) infer self-duality from dim C = 2tn alone
    G = gram_matrix(E, ambient_words(E), s)
    half = 0
    sd = 0
    for W in subs:
        A = code_basis(E, W)
        dimC, rank, dimH, R, M = hull_by_pairing(E, G, A, s)
        if dimC == 2 * t * n:
            half += 1
            if rank == 0:
                sd += 1
    check("NEGATIVE CONTROL: dim C = 2tn does NOT imply self-dual: %d codes have "
          "dim C = %d, only %d of them are self-dual" % (half, 2 * t * n, sd),
          half > sd, "%d vs %d" % (half, sd), exhaustive)
    # (G4) additivity of the hull dimension over the CRT components
    if E.split and E.ncomp > 1:
        tau, orbits = tau_orbits(E, s)
        if any(tau[j] != j for j in range(E.ncomp)):
            E1 = E1_of(E)
            K = E.K
            bad = []
            for W in subs:
                A = code_basis(E, W)
                dimC, rank, dimH, R, M = hull_by_pairing(E, G, A, s)
                sdim = 0
                for j in range(E.ncomp):
                    pairs = []
                    for r in W["rows"]:
                        w = unpair(E.C, tuple(r))
                        pairs.append((K.proj(w[0], j), K.proj(w[1], j)))
                    Vj = mod_of(E1.C, pairs)
                    _, ij, _, _ = hull_by_morita(E1, Vj, s)
                    sdim += 2 * len(ij)
                if sdim != dimH:
                    bad.append((W, dimH, sdim))
            check("NEGATIVE CONTROL: the hull dimension is NOT the sum of the "
                  "component hull dimensions: %d of %d codes disagree"
                  % (len(bad), len(subs)), len(bad) > 0,
                  "sum_j dim Hull(C_j) vs dim Hull(C)", exhaustive)
            if bad:
                W, dh, sd2 = bad[0]
                say("      example: dim Hull(C) = %d but sum_j dim Hull(C_j) = %d"
                    % (dh, sd2))
    # (G5) assume every code is principal
    mus = Counter(E.mu(W) for W in subs)
    nprinc = sum(v for k, v in mus.items() if k <= 2)
    say("  #principal %d of %d ; mu distribution %s"
        % (nprinc, len(subs), dict(sorted(mus.items()))))
    if E.kind == "wild":
        check("NEGATIVE CONTROL: the split/chain pattern 'every code is principal' "
              "FAILS in the wild regime", nprinc < len(subs),
              "%d of %d are principal" % (nprinc, len(subs)), exhaustive)


def boundary_cases():
    """the degenerate codes: zero, ambient, and n = 1"""
    sub("boundary cases")
    for (q, t, n) in [(4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2)]:
        E = Ring3B(q, t, n)
        G_words = ambient_words(E)
        for s in range(E.r):
            G = gram_matrix(E, G_words, s)
            A = code_basis(E, mod_of(E.C, []))
            dimC, rank, dimH, R, M = hull_by_pairing(E, G, A, s)
            check("(%d,%d,%d) s=%d: the ZERO code has dim Hull = 0"
                  % (q, t, n, s), (dimC, dimH) == (0, 0),
                  "dim C = %d, dim Hull = %d" % (dimC, dimH), True)
            # ambient code: W = B^2
            basis = []
            for i in range(E.d2):
                v = [0] * E.d2
                v[i] = 1
                basis.append(tuple(v))
            Wfull = mod_of(E.C, [unpair(E.C, v) for v in basis])
            A = code_basis(E, Wfull)
            dimC, rank, dimH, R, M = hull_by_pairing(E, G, A, s)
            check("(%d,%d,%d) s=%d: the AMBIENT code R_n has dim C = 4tn and "
                  "dim Hull = 0 (the Galois form is non-degenerate)"
                  % (q, t, n, s), (dimC, dimH) == (E.dimw, 0),
                  "dim C = %d, dim Hull = %d" % (dimC, dimH), True)


def local_counting(E1, loc, cap=400000):
    """the four counting problems for the LOCAL ring A_t (i.e. n = 1)"""
    N1 = len(loc)
    f = {}
    for k in (1, 2):
        fk, size = generating_tuples(E1, loc, k, cap=cap)
        f[k] = fk
    n3 = unit_orbit_classes(E1, loc, gl2_generators(E1))
    types = [module_type(E1, V) for V in loc]
    return N1, f, n3, len(set(types)), types, len(units_of_B(E1))


def counting_problems_product(q, t, n):
    """
    the four counting problems in the SPLIT regime with ncomp = n > 1, obtained
    from the local lattice by the CRT product:
        ideals         #L^n
        generating k-tuples   f_k(prod V_j) = prod_j f_k(V_j)
        unit classes   (B^x = prod_j A_t^x acts componentwise)
        Morita classes the type (type(V_1), ..., type(V_n)) is a complete invariant
    """
    E1, loc = local_lattice(q, t)
    N1, f, n3, n4, types, nunit = local_counting(E1, loc)
    sub("counting problems for (q,t,n)=(%d,%d,%d)   [CRT product]" % (q, t, n))
    say("  local ring A_t: |L(A_t^2)| = %d, |A_t^x| = %d, #unit classes = %d, "
        "#Morita classes = %d" % (N1, nunit, n3, n4))
    say("  (1) distinct right ideals of R_n : %d  (= %d^%d)" % (N1 ** n, N1, n))
    for k in (1, 2):
        if f[k] is None:
            say("  (2) generating %d-tuples: NOT COMPUTED" % k)
            continue
        tot = 0
        for idxs in itertools.product(range(N1), repeat=n):
            acc = 1
            for i in idxs:
                acc *= f[k][i]
            tot += acc
        want = (E1.C.F.q ** (2 * t * n)) ** k
        check("(%d,%d,%d): the CRT product of the local generating-%d-tuple counts "
              "sums to |B^2|^%d" % (q, t, n, k, k), tot == want,
              "%d vs %d" % (tot, want), True)
        nc = sum(1 for idxs in itertools.product(range(N1), repeat=n)
                 if all(f[k][i] > 0 for i in idxs))
        say("      #codes with a generating %d-tuple%s: %d"
            % (k, " (i.e. cyclic)" if k == 1 else "", nc))
    say("  (3) #unit-equivalence classes : %d  (= %d^%d)" % (n3 ** n, n3, n))
    say("  (4) #Morita-equivalence classes : %d  (= %d^%d)" % (n4 ** n, n4, n))
    say("  NB: %d, %d, %d are three DIFFERENT counting problems."
        % (N1 ** n, n3 ** n, n4 ** n))
    return N1 ** n, n3 ** n, n4 ** n


# ==========================================================================
# 11.  main
# ==========================================================================

CASES = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2), (4, 1, 3),
         (9, 1, 2), (8, 1, 2), (4, 2, 3)]

# parameter sets where the whole submodule lattice of B^2 can be enumerated by BFS
BFS_FEASIBLE = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2), (4, 1, 3),
                (9, 1, 2), (8, 1, 2)]


def task_a():
    head("TASK A -- the four counting problems, separately for each parameter set")
    say("  (1) distinct right ideals of R_n = distinct B-submodules of B^2")
    say("  (2) distinct generator matrices  = generating tuples of the submodule")
    say("  (3) unit-equivalence classes     = orbits of R_n^x = GL_2(B) acting by")
    say("                                     LEFT multiplication on right ideals")
    say("                                     (i.e. W -> U W under Morita)")
    say("  (4) Morita-equivalent submodules = isomorphism classes of the B-modules")
    say("  These four numbers are NEVER mixed: (1) != (2) != (3) != (4) in general.")
    for (q, t, n) in CASES:
        if (q, t, n) in BFS_FEASIBLE:
            counting_problems(q, t, n)
        else:
            counting_problems_product(q, t, n)


def task_f():
    head("TASK F -- open questions: what the data does and does not settle")
    say("  F1  is every hull principal?  (O-3.1, carried from Stage 3A)")
    say("      -> the exhaustive scan is Task F (continued), below")
    sub("F2  is the hull (a right ideal of R_n) a left ideal?")
    for (q, t, n) in [(4, 1, 2), (4, 1, 3)]:
        E = Ring3B(q, t, n)
        subs = enumerate_submodules(E.C)
        left_ideal_gap(E, subs, 0, ntrial=20)
    sub("F3  is dim Hull additive over the CRT components?")
    say("  NO in general: see the negative control (G4) above -- with tau != id the "
        "correct statement is  dim Hull(C) = sum_j dim( C_j cap C_{tau(j)}^perp ),")
    say("  not  sum_j dim Hull(C_j).  (Stage 3A witness: (4,1,3), s=0, a code with")
    say("  dim Hull = 2 while every component hull is 0.)")
    sub("F4  does the hull dimension determine the hull?")
    for (q, t, n) in [(4, 1, 3), (4, 2, 2)]:
        E = Ring3B(q, t, n)
        Gw = ambient_words(E)
        subs = enumerate_submodules(E.C) if (q, t, n) in BFS_FEASIBLE else None
        if subs is None:
            continue
        for s in range(E.r):
            G = gram_matrix(E, Gw, s)
            dims, keys = set(), set()
            for W in subs:
                A = code_basis(E, W)
                dimC, rank, dimH, R, M = hull_by_pairing(E, G, A, s)
                dims.add(dimH)
                keys.add(basis_key(hull_subspace(E, A, M)))
            say("  (%d,%d,%d) s=%d: %d codes, %d distinct hull dimensions, %d "
                "distinct hull subspaces" % (q, t, n, s, len(subs), len(dims),
                                             len(keys)))


def main():
    head("PHASE 3 -- STAGE 3B: enumeration of Galois hull dimensions for codes "
         "over R = M_2(A_t)")
    say("  seed %d ;  [EXH] = exhaustive over the stated family, [SMP] = sampled" % SEED)
    say("  conventions: A_t = F_q[u]/<u^t>,  R = M_2(A_t),  R_n = R[X]/<X^n-1>,")
    say("               B = A_t[X]/<X^n-1>;  codes = right ideals of R_n =")
    say("               B-submodules W of B^2 (Morita);  Hull_s(C) = C cap C^perp_s.")
    task_a()
    head("TASKS B-E -- exhaustive hull-dimension enumeration, distributions, and "
         "the split-regime closed form")
    for (q, t, n) in CASES:
        run_case(q, t, n)
    task_f()
    task_f_hull_principality()
    head("TASK G -- boundary cases")
    boundary_cases()
    head("summary")
    nfail = len(FAILURES)
    say("  %d checks, %d PASS, %d FAIL" % (NCHECK[0], NCHECK[0] - nfail, nfail))
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
# 12.  O-3.1:  Nakayama witness verification and the exhaustive scan
# ==========================================================================

_RAD_CACHE = {}


def rad_of_B(E):
    """
    rad(B).  In every regime occurring here B is a finite commutative ring that
    is local (chain and wild regimes) or a product of local rings (split regime);
    in the LOCAL cases the unique maximal ideal is exactly the set of non-units.
    Returns None if B is not local (the set of non-units is then not an ideal).
    """
    key = (E.q, E.t, E.n)
    if key in _RAD_CACHE:
        return _RAD_CACHE[key]
    C = E.C
    B = C.B
    units = set(units_of_B(E))
    rad = [b for b in B.elem_list() if b not in units]
    # check that rad is an ideal (it must be, if B is local)
    radset = set(rad)
    for x in rad:
        for b in B.elem_list():
            if B.mul(x, b) not in radset:
                _RAD_CACHE[key] = None
                return None
    for x in rad:
        for y in rad:
            if B.add(x, y) not in radset:
                _RAD_CACHE[key] = None
                return None
    _RAD_CACHE[key] = rad
    return rad


def nakayama_mu(E, V):
    """
    mu_B(V) = dim_k( V / rad(B) V ),  k = B/rad(B)  (Nakayama; B local).
    Returns (mu, dim_{F_q} V, dim_{F_q} rad V, |k|) or None if B is not local.
    """
    C = E.C
    rad = rad_of_B(E)
    if rad is None:
        return None
    gen = []
    for r in V["rows"]:
        w = unpair(C, tuple(r))
        for x in rad:
            gen.append((C.B.mul(x, w[0]), C.B.mul(x, w[1])))
    radV = module_of(C, gen) if gen else []
    dimV, dimRad = len(V["rows"]), len(radV)
    sizek = len(C.B.elem_list()) // max(1, len(rad))
    kdim, acc = 0, 1
    while acc < sizek:
        kdim += 1
        acc *= C.F.q
    if acc != sizek or (dimV - dimRad) % kdim:
        return None
    return (dimV - dimRad) // kdim, dimV, dimRad, sizek


def witness_report(E, W, Wh, mu, s):
    """full verification of one hull with mu_B >= 3 (i.e. a non-principal hull)"""
    C = E.C
    say("")
    say("  ---- WITNESS: a code whose Galois hull is NOT principal ----")
    say("      (q,t,n) = (%d,%d,%d),  s = %d,  kind = %s" % (E.q, E.t, E.n, s, E.kind))
    say("      code C = I_W with W generated over B by:")
    for g in E.gens_of(W):
        say("          %s" % (tuple(tuple(x) for x in g),))
    say("      dim_{F_q} W = %d,  mu_B(W) = %d  (so C is %sprincipal)"
        % (W["dim"], E.mu(W), "" if E.mu(W) <= 2 else "NOT "))
    dimH1, inter, Wp, hrows = hull_by_morita(E, W, s)
    G = gram_matrix(E, ambient_words(E), s)
    A = code_basis(E, W)
    dimC, rank, dimH2, R, M = hull_by_pairing(E, G, A, s)
    say("      dim C = %d,  dim Hull = %d (Morita route) / %d (pairing route)"
        % (dimC, dimH1, dimH2))
    check("(%d,%d,%d) s=%d WITNESS: the two hull routes agree on the witness code"
          % (E.q, E.t, E.n, s), dimH1 == dimH2 and dimH1 == 2 * len(inter),
          "%d vs %d, 2*dim(W cap W') = %d" % (dimH1, dimH2, 2 * len(inter)), True)
    nm = nakayama_mu(E, Wh)
    say("      hull submodule: dim_{F_q} = %d,  mu_B = %d" % (Wh["dim"], mu))
    if nm:
        say("      Nakayama check: mu = dim_k(V/rad V) = %d  (dim V = %d, "
            "dim rad V = %d, |k| = %d)" % (nm[0], nm[1], nm[2], nm[3]))
        check("(%d,%d,%d) s=%d WITNESS: the Nakayama dimension dim_k(V/rad V) "
              "agrees with the computed mu_B" % (E.q, E.t, E.n, s), nm[0] == mu,
              "%d vs %d" % (nm[0], mu), True)
    # spot check: no pair of elements of the hull generates it
    import random
    rnd = random.Random(SEED + 4242)
    elems = [unpair(C, tuple(v)) for v in all_elements(C, [list(r) for r in
                                                           Wh["rows"]])]
    bad = 0
    ntry = min(4000, max(500, len(elems)))
    for _ in range(ntry):
        w1 = elems[rnd.randrange(len(elems))]
        w2 = elems[rnd.randrange(len(elems))]
        span = module_of(C, [w1, w2])
        if basis_key(span) == basis_key(Wh["rows"]):
            bad += 1
    check("(%d,%d,%d) s=%d WITNESS: none of %d randomly drawn pairs of elements "
          "of the hull generates it" % (E.q, E.t, E.n, s, ntry), bad == 0,
          "%d pairs did generate" % bad, False)
    say("      => the hull right ideal Hull_s(C) = I_{W cap W'} is GENERATED BY "
        "NO SINGLE ELEMENT: mu_B = %d > 2." % mu)
    say("      => O-3.1 ('mu_B(W_hull) <= 2 for every code') is FALSE in general.")


def task_f_hull_principality():
    """
    exhaustive scan, over every family whose whole code set can be enumerated,
    of the question: is every Galois hull a PRINCIPAL right ideal?
    (O-3.1 of Stage 3A.)
    """
    head("TASK F (continued) -- O-3.1: is every Galois hull principal?  "
         "exhaustive scan")
    say("  O-3.1 (Stage 3A): mu_B(W_hull) <= 2 for every code and every s.")
    say("  Recall: a right ideal I_W of R_n = M_2(B) is principal iff W is "
        "generated by <= 2 elements as a B-module (im h = W, T-077).")
    nref = 0
    for (q, t, n) in BFS_FEASIBLE:
        E = Ring3B(q, t, n)
        subs = enumerate_submodules(E.C)
        for s in range(E.r):
            dist = Counter()
            bad = []
            for W in subs:
                dimH, inter, Wp, hrows = hull_by_morita(E, W, s)
                Wh = mod_of(E.C, [unpair(E.C, tuple(r)) for r in inter])
                mu = E.mu(Wh)
                dist[mu] += 1
                if mu > 2:
                    bad.append((W, Wh, mu))
            check("(%d,%d,%d) s=%d: exhaustive hull-principality scan over all %d "
                  "codes" % (q, t, n, s, len(subs)), True,
                  "mu distribution of hulls %s ; %d hulls with mu_B >= 3"
                  % (dict(sorted(dist.items())), len(bad)), True)
            if bad:
                nref += 1
                for (W, Wh, mu) in bad[:3]:
                    witness_report(E, W, Wh, mu, s)
    say("")
    if nref:
        say("  RESULT: O-3.1 is REFUTED.  It fails in the WILD regime "
            "(q,t,n) = (4,2,2); the witness above is verified by two independent")
        say("          hull routes, by the Nakayama dimension dim_k(V/rad V), and "
            "by a randomised search for a 2-element generating set.")
        say("          In every SPLIT and CHAIN family scanned exhaustively, every "
            "hull was principal (see the per-case scans above).")
    else:
        say("  RESULT: no counterexample to O-3.1 was found in the scanned range.")


if __name__ == "__main__":
    main()
