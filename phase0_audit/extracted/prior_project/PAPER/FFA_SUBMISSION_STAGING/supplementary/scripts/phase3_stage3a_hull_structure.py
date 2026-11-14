#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 3 -- STAGE 3A:  Galois hull structure and dimension theory
================================================================

For a right cyclic code C <= R_n (equivalently a right ideal of R_n, under the
standing right-module convention) the Galois hull is

        Hull_s(C) = C  n  C^{perp_s},        C^{perp_s} = {y : B_s(C,y) = 0},
        B_s(x,y) = sum_e theta_s(x_e) y_e.

Everything below is computed by at least two independent routes:

  route D  (definition)   C^{perp_s} by F_q-linear algebra on the pairing b_s,
                          hull = intersection of two F_q-subspaces;
  route A  (annihilator)  C^{perp_s} = rev(ann_r(theta_s(C)))  (Stage 2C P-2.7),
                          annihilators computed as kernels of the multiplication
                          maps (brute force, never via im/ker/Morita);
  route M  (Morita)       Hull = I_W with W = W(C) n W(C^{perp_s}), using
                          im / ker on B^2 and the column convention -- a route
                          that never mentions the pairing;
  route N  (numerical)    dim Hull = 4tn - dim(C + C^{perp_s})
                                   = dim C - rank(psi_C)
                                   = 2 dim_{F_q}(W(C) n W(C^{perp_s})).

Reused from Stage 2C (`phase2_stage2c_galois_duality.py`): the rings
(A_t, B, R, R_n), iota, sigma_k, theta_s, rev, the pairing, annihilators,
im/ker/I_W, the CRT components and the Smith normal form.  Nothing in that
file is modified; it is imported.

NOT attempted here (by instruction): hull enumeration, Gray maps, quantum
(CSS / EAQECC) constructions, quantum parameter claims, manuscript writing.
A passing script is supporting evidence, not a proof.
"""

import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ring_structure_checks import (Field, Local, MatRing, rref, nullspace_basis,
                                   say, check, LINES, FAILURES, NCHECK, gcd,
                                   field_generator)
import phase2_stage2c_galois_duality as Z

SEED = 20261108
EXH_LIMIT = 5000          # above this |R_n| the elementwise tests are sampled
LOGNAME = "phase3_stage3a_hull_log.txt"
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
    say("  " + "-" * 4 + " " + msg + " " + "-" * max(0, WIDTH - 8 - len(msg)))


# ==========================================================================
# 2.  F_q-linear algebra on the two ambient spaces
# ==========================================================================
#
# Two coordinate systems are in use, exactly as in Stage 2C:
#   * "rn"    : R_n = M_2(B) as an F_q-vector space of dimension 4tn
#               (C.flat_rn / C.unflat_rn)
#   * "pairs" : B^2 as an F_q-vector space of dimension 2tn  (Z._pair_flat)
# A subspace is always carried as an RREF tuple of rows, so that equality of
# subspaces is equality of tuples.

def dot(F, u, v):
    acc = 0
    for a, b in zip(u, v):
        if a and b:
            acc = F.add[acc][F.mul[a][b]]
    return acc


def rref_rows(C, rows, d=None):
    d = C.dimw if d is None else d
    return tuple(tuple(x) for x in rref([list(v) for v in rows], C.F, d)[0])


def rank_of(C, rows, d=None):
    d = C.dimw if d is None else d
    return len(rref([list(v) for v in rows], C.F, d)[1])


def sum_basis(C, A, B, d=None):
    return rref_rows(C, list(A) + list(B), d)


def intersect_basis(C, A, B, d=None):
    """
    A basis of  span(rows A) n span(rows B),  by the orthogonality trick:

        x = c*A lies in span(B)  <=>  x is orthogonal to every vector of
        null(B) = {n : <b,n> = 0 for all b in B}.

    (rowspace(B) and nullspace(B) are orthogonal complements for the standard
    dot product), so the coefficient vectors c are the nullspace of the
    matrix  (<A_i, n_j>)_{j,i}.  No enumeration is involved.
    """
    d = C.dimw if d is None else d
    F = C.F
    A = [list(a) for a in A]
    B = [list(b) for b in B]
    if not A or not B:
        return ()
    Nb = nullspace_basis(B, F, d)
    rows = [[dot(F, A[i], n) for i in range(len(A))] for n in Nb]
    K = nullspace_basis(rows, F, len(A))
    out = []
    for c in K:
        v = [0] * d
        for i, ci in enumerate(c):
            if ci:
                v = [F.add[u][F.mul[ci][w]] for u, w in zip(v, A[i])]
        out.append(v)
    return rref_rows(C, out, d)


# ==========================================================================
# 3.  the hull, by four independent routes
# ==========================================================================

def code_basis(C, gens):
    """the right ideal  C = sum_i g_i R_n  as an RREF basis (rn coordinates)"""
    return Z.right_ideal_basis(C, gens)


def dual_basis_def(C, Ckey, s):
    """
    iota(C^{perp_s}) computed FROM THE DEFINITION of the pairing:
    C^{perp_s} = {y in R^n : b_s(x,y) = 0 for all x in a basis of C}, using the
    functional rows of Stage 2C  (which are built from b_s directly).
    """
    F, d = C.F, C.dimw
    words = [C.iota_inv(C.unflat_rn(tuple(v))) for v in Ckey]
    db = Z.dual_of(C, words, s)
    return rref_rows(C, [C.flat_rn(C.iota(C.unflat_word(tuple(v)))) for v in db])


def dual_basis_annrev(C, gens, s):
    """
    C^{perp_s} = rev( ann_r( theta_s(C) ) ) = rev( inter_i ann_r(theta_s(g_i)) ).

    theta_s(C) is a LEFT ideal (theta_s is an anti-automorphism), and a left
    ideal's right annihilator IS the intersection of the annihilators of its
    generators (Stage 2C Lemma 2.2) -- which is why this is legitimate.
    """
    tg = [C.theta_rn(g, s) for g in gens]
    A = Z.ann_r_set(C, tg)
    return rref_rows(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a)))) for a in A])


def morita_WC(C, gens):
    """W(C) = sum_i im g_i  <= B^2   (Morita column convention)"""
    rows = []
    for g in gens:
        rows.extend(Z.im_basis(C, g))
    return rref_rows(C, rows, d=2 * C.B.dim)


def morita_WD(C, gens, s):
    """
    W(C^{perp_s}) = inter_i ker theta_s(rev g_i)   (equivalently
    rev( inter_i ker theta_s(g_i) ) -- both are computed and compared).
    """
    d = 2 * C.B.dim
    rows = None
    for g in gens:
        v = C.theta_rn(C.rev_rn(g), s)
        K = Z.ker_basis(C, v)
        rows = K if rows is None else intersect_basis(C, rows, K, d)
    return rows if rows is not None else ()


def morita_WD_twisted(C, gens, s):
    """rev( inter_i ker theta_s(g_i) ) -- the second form of W(C^{perp_s})"""
    d = 2 * C.B.dim
    rows = None
    for g in gens:
        K = Z.ker_basis(C, C.theta_rn(g, s))
        rows = K if rows is None else intersect_basis(C, rows, K, d)
    if rows is None:
        return ()
    out = []
    for r in rows:
        w = (tuple(r[:C.B.dim]), tuple(r[C.B.dim:]))
        rw = (C.B.rev(w[0]), C.B.rev(w[1]))
        out.append(Z._pair_flat(C, rw))
    return rref_rows(C, out, d)


def hull_all_routes(C, gens, s):
    """
    Returns a dictionary with the hull (rn coordinates) and the Morita data,
    computed by every route.  `Ckey` is the RREF basis of C itself.
    """
    F, d = C.F, C.dimw
    Ckey = code_basis(C, gens)
    Ddef = dual_basis_def(C, Ckey, s)
    Dann = dual_basis_annrev(C, gens, s)
    hull_D = intersect_basis(C, Ckey, Ddef)
    hull_A = intersect_basis(C, Ckey, Dann)
    WC = morita_WC(C, gens)
    WD = morita_WD(C, gens, s)
    WDt = morita_WD_twisted(C, gens, s)
    Wint = intersect_basis(C, WC, WD, d=2 * C.B.dim)
    hull_M = Z.rref_key(C, Z.I_of_W(C, [(tuple(r[:C.B.dim]), tuple(r[C.B.dim:]))
                                        for r in Wint]))
    # dimension bookkeeping
    dimC = len(Ckey)
    dimD = len(Ddef)
    dimsum = len(sum_basis(C, Ckey, Ddef))
    dim_hull = len(hull_D)
    # rank of the restricted pairing matrix  M[i][j] = b_s(x_i, x_j),
    # for an F_q-basis (x_i) of C.  (b_s is F_q-linear in the second slot and
    # sigma_s-semilinear in the first, so the F_q-span of the functionals
    # y |-> b_s(x,y), x in C, has the same dimension as the span of the rows
    # of M -- sigma_s is a bijection.  Hence dim Hull = dim C - rank M.)
    words = [C.iota_inv(C.unflat_rn(tuple(v))) for v in Ckey]
    M = [[C.bs(xi, xj, s) for xj in words] for xi in words]
    rankM = rank_of(C, M, d=len(Ckey))
    return dict(Ckey=Ckey, Ddef=Ddef, Dann=Dann, hull_D=hull_D, hull_A=hull_A,
                hull_M=hull_M, WC=WC, WD=WD, WDt=WDt, Wint=Wint,
                dimC=dimC, dimD=dimD, dimsum=dimsum, dimhull=dim_hull,
                rankpsi=rankM,
                dimWint=len(Wint), dimWD=len(WD), dimWC=len(WC))


# ==========================================================================
# 4.  Task A -- structure of the hull
# ==========================================================================

def tags(C, s):
    return "(q,t,n)=(%d,%d,%d), s=%d" % (C.q, C.t, C.n, s)


def exhaustive(C):
    return (C.q ** (C.t * C.n)) ** 4 <= EXH_LIMIT


def test_taskA(C, glist, s):
    """
    A1  F_q-linearity of the dual and of the hull (proved: c in F_q is central
        in R_n, so B_s(x, c y) = c B_s(x,y)).
    A2  the hull is a right R_n-submodule.
    A3  the hull is NOT always a left R_n-submodule (witness exhibited).
    A4  shift-invariance in word coordinates (cyclic).
    A5  Hull_s(sigma_k C) = sigma_k Hull_s(C).
    A6  theta_s(Hull) = theta_s(C) n rev(ann_l(sigma_{2s}(C))), a LEFT ideal.
    A7  rev(Hull) = rev(C) n ann_r(theta_s(C)).
    A8  the Euclidean / transpose-Euclidean / Hermitian distinction.
    """
    F, d = C.F, C.dimw
    tag = tags(C, s)
    exh = exhaustive(C)

    # ---- A1  F_q-linearity ---------------------------------------------
    ok = True
    ntest = 0
    for g in glist[:8]:
        R = hull_all_routes(C, [g], s)
        for v in R["Ddef"][:4]:
            M = C.unflat_rn(tuple(v))
            for c in range(1, F.q):
                cM = tuple(tuple(F.mul[c][x] for x in m) for m in M)
                if not Z.contains(C, R["Ddef"], C.flat_rn(cM)):
                    ok = False
                ntest += 1
    check("%s: C^{perp_s} is an F_q-subspace (c*y, c in F_q^*)" % tag, ok,
          "%d scalar multiples of dual basis vectors tested" % ntest, exh)

    # ---- A2  right R_n-submodule ---------------------------------------
    bad = 0
    nz = 0
    notleft = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        hk = R["hull_D"]
        if not Z.is_right_ideal(C, hk):
            bad += 1
        if hk:
            nz += 1
            if not Z.is_left_ideal(C, hk):
                notleft += 1
    check("%s: Hull_s(C) is a right R_n-submodule (a cyclic code)" % tag,
          bad == 0, "%d of %d codes fail closure" % (bad, len(glist)), exh)

    # ---- A3  not in general a left submodule ---------------------------
    if nz:
        check("%s: Hull_s(C) is NOT always a left submodule" % tag, notleft > 0,
              "%d of %d nonzero hulls are not left ideals" % (notleft, nz), exh)
    else:
        say("     note: no nonzero hull occurred among the %d sampled codes at "
            "%s, so the 'not a left ideal' witness cannot be exhibited here "
            "(the check is skipped rather than passed vacuously)" % (len(glist), tag))

    # ---- A4  shift invariance ------------------------------------------
    def T(w):
        return tuple(w[(e - 1) % C.n] for e in range(C.n))

    ok = True
    for g in glist[:10]:
        R = hull_all_routes(C, [g], s)
        for v in R["hull_D"][:5]:
            w = C.iota_inv(C.unflat_rn(tuple(v)))
            tw = C.iota(T(w))
            if not Z.contains(C, R["hull_D"], C.flat_rn(tw)):
                ok = False
    check("%s: Hull_s(C) is shift-invariant (T(Hull) = Hull)" % tag, ok,
          "10 codes x 5 hull vectors", exh)

    # ---- A5  sigma_k-equivariance --------------------------------------
    bad = 0
    for g in glist[:12]:
        R = hull_all_routes(C, [g], s)
        for k in range(C.r):
            gk = C.sigma_rn(g, k)
            Rk = hull_all_routes(C, [gk], s)
            sh = rref_rows(C, [C.flat_rn(C.sigma_rn(C.unflat_rn(tuple(v)), k))
                               for v in R["hull_D"]])
            if sh != Rk["hull_D"]:
                bad += 1
    check("%s: Hull_s(sigma_k C) = sigma_k Hull_s(C) for every k" % tag,
          bad == 0, "12 codes x %d values of k" % C.r, False)

    # ---- A6  theta_s of the hull ---------------------------------------
    bad = 0
    for g in glist[:12]:
        R = hull_all_routes(C, [g], s)
        th = rref_rows(C, [C.flat_rn(C.theta_rn(C.unflat_rn(tuple(v)), s))
                           for v in R["hull_D"]])
        left = Z.left_ideal_basis(C, [C.theta_rn(g, s)])
        Al = Z.ann_l_element(C, C.sigma_rn(g, 2 * s))
        other = rref_rows(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a)))) for a in Al])
        want = intersect_basis(C, left, other)
        if th != want:
            bad += 1
    check("%s: theta_s(Hull) = theta_s(C) n rev(ann_l(sigma_2s C))" % tag,
          bad == 0, "12 codes; both sides computed independently", False)

    # ---- A7  rev of the hull -------------------------------------------
    bad = 0
    for g in glist[:12]:
        R = hull_all_routes(C, [g], s)
        rh = rref_rows(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(v))))
                           for v in R["hull_D"]])
        revC = Z.right_ideal_basis(C, [C.rev_rn(g)])
        Ar = Z.ann_r_set(C, [C.theta_rn(g, s)])
        want = intersect_basis(C, revC, Ar)
        if rh != want:
            bad += 1
    check("%s: rev(Hull_s(C)) = rev(C) n ann_r(theta_s(C))" % tag, bad == 0,
          "12 codes", False)

    # ---- A8  Euclidean / transpose-Euclidean / Hermitian ----------------
    # (i) B_0 is the TRANSPOSE-Euclidean form, not the classical Euclidean one
    # the four matrix units E_{ij} (with u-degree 0 and X-degree 0); the
    # witness needs an off-diagonal one, since x^T y = x y whenever x is a
    # multiple of a diagonal matrix unit.
    ks = [k * (C.t * C.n) for k in range(4)]
    found = None
    for k1 in ks:
        for k2 in ks:
            v1 = C.unflat_rn(tuple(1 if i == k1 else 0 for i in range(d)))
            v2 = C.unflat_rn(tuple(1 if i == k2 else 0 for i in range(d)))
            x = C.iota_inv(v1)
            y = C.iota_inv(v2)
            Bt = C.Bs(x, y, 0)                  # sum_e theta_0(x_e) y_e = sum x_e^T y_e
            Eu = C.RA.zero                      # sum_e x_e y_e
            for e in range(C.n):
                Eu = C.RA.add(Eu, C.RA.mul(x[e], y[e]))
            if Bt != Eu:
                found = (k1, k2)
                break
        if found:
            break
    check("%s: B_0 = sum x_e^T y_e differs from the Euclidean sum x_e y_e"
          % tag, found is not None,
          "witness: basis vectors %s" % (found,) if found else
          "**the two forms coincide -- no witness**", found is not None)

    # (ii) the form is sigma_s-Hermitian exactly when r | 2s
    refl = (2 * s) % C.r == 0
    bad = 0
    npair = 0
    # NB: random AMBIENT pairs, not basis vectors of a code -- for the latter
    # the identity can hold accidentally (the violating term
    # Lambda((x - sigma_2s x) sigma_s y) may vanish on a structured sample).
    rng = random.Random(SEED + 1000 * s + 17)
    def rnd_word():
        return tuple(tuple(tuple(rng.randrange(C.q) for _ in range(C.t))
                           for _ in range(4)) for _ in range(C.n))
    for _ in range(60):
        x = rnd_word()
        y = rnd_word()
        lhs = C.bs(y, x, s)
        a = C.bs(x, y, s)
        acc = a
        for _ in range(C.p ** s - 1):
            acc = F.mul[acc][a]
        if lhs != acc:
            bad += 1
        npair += 1
    if refl:
        check("%s: b_s(y,x) = sigma_s(b_s(x,y))  (r | 2s: Hermitian)" % tag,
              bad == 0, "%d pairs, %d violations" % (npair, bad), False)
    else:
        check("%s: b_s is NOT sigma_s-Hermitian (r does not divide 2s)" % tag,
              bad > 0, "%d of %d pairs violate Hermiticity" % (bad, npair), False)


# ==========================================================================
# 5.  Task B -- the hull formula
# ==========================================================================

def test_taskB(C, glist, s):
    """
    B1  (principal)  Hull = C n rev(ann_r(theta_s(g))):  three routes agree
        and both inclusions are checked elementwise where feasible.
    B2  (non-principal, two generators) the intersection formula
        rev( inter_i ann_r(theta_s(g_i)) ) agrees with the definition route.
    B3  the single-generator formula FAILS for a genuinely non-principal code
        (justifying the intersection form).
    B4  the role of rev / ann_l / theta_s: each removal is detected.
    """
    F, d = C.F, C.dimw
    tag = tags(C, s)
    exh = exhaustive(C)

    # ---- B1  three routes agree (principal) ----------------------------
    bad = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        if not (R["hull_D"] == R["hull_A"] == R["hull_M"]):
            bad += 1
    check("%s: hull by definition = hull by annihilator/rev = hull by Morita"
          % tag, bad == 0, "%d codes, 3 independent routes" % len(glist), exh)

    # ---- B1'  both inclusions, elementwise ------------------------------
    bad = 0
    small = C.dimw <= 12 and len(glist) > 0
    if small:
        for g in glist[:6]:
            R = hull_all_routes(C, [g], s)
            S = Z.span_keys(C, R["hull_D"])
            CD = intersect_basis(C, R["Ckey"], R["Ddef"])
            if len(S) > 4000:
                bad = -1
                break
            if S != Z.span_keys(C, CD):
                bad += 1
    if bad == -1 or not small:
        say("     note: elementwise inclusion check skipped at %s (the hull is "
            "too large to enumerate)" % tag)
    else:
        check("%s: both inclusions, elementwise (enumerated hull)" % tag,
              bad == 0, "6 codes, hulls enumerated as sets", True)

    # ---- B2  non-principal: two generators ------------------------------
    bad = 0
    bad_single = 0
    nnon = 0
    for i in range(min(15, len(glist) // 2)):
        g1 = glist[2 * i]
        g2 = glist[2 * i + 1]
        Ck = code_basis(C, [g1, g2])
        R2 = hull_all_routes(C, [g1, g2], s)
        # is it genuinely non-principal?  compare with the principal hulls
        R1a = hull_all_routes(C, [g1], s)
        R1b = hull_all_routes(C, [g2], s)
        if Ck != R1a["Ckey"] and Ck != R1b["Ckey"]:
            nnon += 1
            # using only ONE generator must give a different (wrong) hull
            h_only1 = intersect_basis(C, Ck, dual_basis_annrev(C, [g1], s))
            if h_only1 == R2["hull_D"]:
                bad_single += 1
        if not (R2["hull_D"] == R2["hull_A"] == R2["hull_M"]):
            bad += 1
    check("%s: non-principal (2 generators): the three routes agree" % tag,
          bad == 0, "15 two-generator codes", exh)
    if nnon:
        check("%s: for a non-principal code the 1-generator formula is WRONG"
              % tag, bad_single < nnon,
              "%d of %d non-principal codes detect the omission" %
              (nnon - bad_single, nnon), exh)
    else:
        say("     note: no genuinely non-principal 2-generator code appeared in "
            "this sample, so the omission test is not exhibited here")

    # ---- B4  rev / ann_l / theta_s --------------------------------------
    nrev = 0
    nann = 0
    nth = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        # (a) drop rev:  C n ann_r(theta_s(g))
        norev = intersect_basis(C, R["Ckey"],
                                Z.ann_r_set(C, [C.theta_rn(g, s)]))
        if norev != R["hull_D"]:
            nrev += 1
        # (b) ann_l instead of ann_r
        Arl = Z.ann_l_element(C, C.theta_rn(C.rev_rn(g), s))
        wrong = rref_rows(C, [C.flat_rn(C.unflat_rn(tuple(a))) for a in Arl])
        if intersect_basis(C, R["Ckey"], wrong) != R["hull_D"]:
            nann += 1
        # (c) drop theta_s:  C n rev(ann_r(g))
        noth = intersect_basis(C, R["Ckey"],
                               rref_rows(C, [C.flat_rn(C.rev_rn(C.unflat_rn(tuple(a))))
                                             for a in Z.ann_r_set(C, [g])]))
        if noth != R["hull_D"]:
            nth += 1
    say("     removal sensitivity at %s: dropping rev changes the hull for %d "
        "of %d codes; using ann_l for %d; dropping theta_s for %d"
        % (tag, nrev, len(glist), nann, nth))
    return dict(nrev=nrev, nann=nann, nth=nth, n=len(glist))


# ==========================================================================
# 6.  Task C -- dimension
# ==========================================================================

def fp_basis(C):
    """an F_p-basis of F_q in field elements"""
    F = C.F
    w = field_generator(F)
    out = []
    x = 1
    for _ in range(C.r):
        out.append(x)
        x = F.mul[x][w]
    return out


def fp_coords(C):
    """lookup: a in F_q  ->  its r coordinates in an F_p-basis"""
    F = C.F
    basis = fp_basis(C)
    table = {}
    for coeffs in itertools.product(range(C.p), repeat=C.r):
        a = 0
        for c, b in zip(coeffs, basis):
            if c:
                a = F.add[a][F.mul[b][c]]
        table[a] = list(coeffs)
    return table


def fp_dim(C, rows, d=None):
    """
    dim_{F_p} of the F_p-span of the F_q-vectors `rows`, computed honestly:
    the F_p-span is generated by {b * v : b in an F_p-basis of F_q, v in rows},
    and each F_q coordinate is expanded into r F_p coordinates, so the ambient
    F_p-dimension is r * d.
    """
    d = C.dimw if d is None else d
    F = C.F
    table = fp_coords(C)
    basis = fp_basis(C)
    Fp = Field(C.p, 1)
    out = []
    for v in rows:
        for b in basis:
            row = []
            for a in v:
                row.extend(table[F.mul[b][a]])
            out.append(row)
    if not out:
        return 0
    return len(rref(out, Fp, d * C.r)[1])


def span_set(C, rows, d):
    """the F_q-span of `rows` (of length d) enumerated as a set"""
    F = C.F
    if not rows:
        return frozenset([tuple([0] * d)])
    out = set()
    for coeffs in itertools.product(range(F.q), repeat=len(rows)):
        acc = [0] * d
        for c, r in zip(coeffs, rows):
            if c:
                acc = [F.add[u][F.mul[c][v]] for u, v in zip(acc, r)]
        out.add(tuple(acc))
    return frozenset(out)


def is_principal(C, hk):
    """
    Is the right ideal `hk` principal?  Decided by an EXHAUSTIVE search for a
    single generator (no Morita, no mu):  for every x in the hull, compare
    x R_n with the hull.
    """
    if not hk:
        return True                      # {0} = 0 * R_n
    hk = tuple(tuple(v) for v in hk)
    for v in span_set(C, hk, C.dimw):
        x = C.unflat_rn(tuple(v))
        gen = tuple(tuple(u) for u in Z.right_ideal_basis(C, [x]))
        if gen == hk:
            return True
    return False


def test_taskC(C, glist, s, K):
    """
    C0  the correct scalar field: dim_{F_p} Hull = r * dim_{F_q} Hull.
    C1  dim Hull = 4tn - dim(C + C^{perp_s})   (sum formula)
        dim Hull = dim C - rank(psi_C)         (kernel / rank formula)
    C2  Morita:  Hull = I_{W n W'},  dim Hull = 2 dim_{F_q}(W n W'),
        and |I_W| = |W|^2 verified by enumeration where feasible.
    C4  the hull is even-dimensional; mu_B(W_hull) and its principality.
    C5  in the chain-ring regime: Hull = g R_n n h R_n with h the P-2.8
        Smith-normal-form generator of the dual (Stage 2C).
    """
    F, d = C.F, C.dimw
    tag = tags(C, s)
    exh = exhaustive(C)

    rets = [hull_all_routes(C, [g], s) for g in glist]

    # ---- C0  scalar field ----------------------------------------------
    if C.dimw * C.r <= 40:
        bad = 0
        for R in rets[:8]:
            if R["hull_D"] and fp_dim(C, R["hull_D"]) != C.r * len(R["hull_D"]):
                bad += 1
        check("%s: dim_{F_p} Hull = r * dim_{F_q} Hull" % tag, bad == 0,
              "8 codes, F_p-rank computed directly (r = %d)" % C.r, True)
    else:
        say("     note: the F_p-rank check is skipped at %s (ambient F_p "
            "dimension %d is too large)" % (tag, C.dimw * C.r))

    # ---- C1  the three numerical formulas ------------------------------
    bad_sum = 0
    bad_rank = 0
    bad_mor = 0
    for R in rets:
        if R["dimhull"] != C.dimw - R["dimsum"]:
            bad_sum += 1
        if R["dimhull"] != R["dimC"] - R["rankpsi"]:
            bad_rank += 1
        if R["dimhull"] != 2 * R["dimWint"]:
            bad_mor += 1
    check("%s: dim Hull = 4tn - dim(C + C^{perp_s})" % tag, bad_sum == 0,
          "%d codes, %d violations" % (len(rets), bad_sum), exh)
    check("%s: dim Hull = dim C - rank(psi_C)  (restricted pairing)" % tag,
          bad_rank == 0, "%d codes, %d violations" % (len(rets), bad_rank), exh)
    check("%s: dim Hull = 2 dim_{F_q}(W(C) n W(C^{perp_s}))  (Morita)" % tag,
          bad_mor == 0, "%d codes, %d violations" % (len(rets), bad_mor), exh)

    # ---- C2  Morita, as sets, and |I_W| = |W|^2 -------------------------
    bad = 0
    for R in rets:
        if R["hull_M"] != R["hull_D"]:
            bad += 1
    check("%s: Hull = I_{W n W'} (Morita, columns)" % tag, bad == 0,
          "%d codes" % len(rets), exh)

    if C.dimw <= 12 and len(rets) > 0:
        bad = 0
        ndone = 0
        for R in rets[:6]:
            IW = Z.I_of_W(C, [(tuple(r[:C.B.dim]), tuple(r[C.B.dim:]))
                              for r in R["Wint"]])
            n1 = len(span_set(C, IW, C.dimw))
            n2 = len(span_set(C, R["Wint"], 2 * C.B.dim)) ** 2
            if n1 != n2 or n1 != len(span_set(C, R["hull_D"], C.dimw)):
                bad += 1
            ndone += 1
        check("%s: |I_W| = |W|^2 = |Hull| for W = W(hull)  (enumerated)" % tag,
              bad == 0, "%d codes, sets enumerated" % ndone, True)
    else:
        say("     note: |I_W| = |W|^2 enumeration skipped at %s (too large)" % tag)

    # ---- C4  parity and principality of the hull ------------------------
    odd = 0
    for R in rets:
        if R["dimhull"] % 2:
            odd += 1
    check("%s: dim_{F_q} Hull_s(C) is always even (Morita)" % tag, odd == 0,
          "%d codes, %d with odd dimension" % (len(rets), odd), exh)

    if K.kind in ("split", "chain"):
        mu_hist = {}
        nchk = 0
        bad = 0
        nprin = 0
        for R in rets:
            Wp = [(tuple(r[:C.B.dim]), tuple(r[C.B.dim:])) for r in R["Wint"]]
            mu = 0 if not Wp else Z.mu_components(C, K, Wp)[0]
            mu_hist[mu] = mu_hist.get(mu, 0) + 1
            # principality decided by an EXHAUSTIVE search for a generator,
            # independent of mu  (only where the hull is small enough)
            if C.q ** R["dimhull"] <= 3000:
                princ = is_principal(C, R["hull_D"])
                if princ != (mu <= 2):
                    bad += 1
                nchk += 1
                if princ:
                    nprin += 1
        say("     mu_B(W_hull) distribution over %d codes: %s"
            % (len(rets), dict(sorted(mu_hist.items()))))
        if nchk:
            check("%s: the hull is principal iff mu_B(W_hull) <= 2" % tag,
                  bad == 0,
                  "%d codes, principality by exhaustive generator search; %d "
                  "principal" % (nchk, nprin), True)
        else:
            say("     note: principality search skipped at %s (hulls too large "
                "to enumerate)" % tag)

    # ---- C5  SNF / explicit generator of the dual -----------------------
    if K.kind in ("split", "chain"):
        bad = 0
        nog = 0
        for g in glist[:15]:
            v = C.theta_rn(C.rev_rn(g), s)
            h, ok = K.snf_h(v)
            if not ok:
                continue
            R = hull_all_routes(C, [g], s)
            Ch = Z.right_ideal_basis(C, [h])
            want = intersect_basis(C, R["Ckey"], Ch)
            if want != R["hull_D"]:
                bad += 1
            else:
                nog += 1
        check("%s: Hull = g R_n n h R_n, h the P-2.8 SNF generator" % tag,
              bad == 0, "15 codes, %d verified" % nog, False)
    else:
        say("     [WILD] no Smith normal form at %s: the dual generator (when "
            "it exists) comes from Nakayama, and the hull is computed by the "
            "Morita route only" % tag)


# ==========================================================================
# 7.  Task C3 -- CRT components and the Galois permutation
# ==========================================================================

def proj_M(K, C, M, j):
    """M_2(B) -> M_2(A_t)   (or M_2(B) -> M_2(B) in the chain case)"""
    return tuple(tuple(K.proj(m, j)) for m in M)


def crt_permutation(C, K, s):
    """
    The permutation tau of the CRT components with

        (C^{perp_s})_j  =  (C_{tau(j)})^{perp_s}   (componentwise dual).

    Derivation:  (a) multiplication is componentwise, so
    ann_r(v)_j = ann_r(v_j);  (b) rev is the substitution X -> X^{-1}, which
    sends the component of zeta to the component of zeta^{-1} (call that rho);
    (c) sigma_s sends the component of zeta to the component of zeta^{p^s}
    (call that pi).  Hence (C^{perp_s})_j = ann_r(theta_s(g)_{pi^{-1}(rho(j))}),
    i.e. tau = pi^{-1} o rho, characterised by  zeta_{tau(j)}^{p^s} = zeta_j^{-1}.

    In the split case this is  tau = id  <=>  n | p^s + 1.
    Returns None when the ring has no component decomposition (wild).
    """
    if K.kind == "split":
        Zs = K.Z
        ps = C.p ** s
        out = []
        for j in range(len(Zs)):
            zinv = C.F.inv[Zs[j]]
            found = None
            for k, z in enumerate(Zs):
                acc = 1
                for _ in range(ps):
                    acc = C.F.mul[acc][z]
                if acc == zinv:
                    found = k
                    break
            out.append(found)
        return out
    if K.kind == "chain":
        return [0]
    return None


def test_C3(C, glist, s, K):
    """
    C3  the CRT behaviour of the hull.  In a chain-ring component regime:
        (i)  (C^{perp_s})_j = (C_{tau(j)})^{perp_s}  (componentwise);
        (ii) Hull_s(C)_j = C_j n (C_{tau(j)})^{perp_s}, hence
             dim Hull = sum_j dim (C_j n (C_{tau(j)})^{perp_s});
        (iii) when tau = id (equivalently n | p^s + 1 in the split case) the
             hull DOES decompose: Hull_s(C)_j = Hull_s(C_j);
        (iv) when tau != id the naive componentwise formula
             dim Hull = sum_j dim Hull_s(C_j) FAILS for some code -- it is
             exhibited here, and it is the reason (ii) is the correct formula.
    """
    tag = tags(C, s)
    tau = crt_permutation(C, K, s)
    if tau is None:
        say("     no CRT component decomposition available at %s (kind = %s): "
            "the component analysis of Task C3 does not apply here -- a genuine "
            "limitation, recorded as such" % (tag, K.kind))
        return None
    if K.kind == "chain":
        say("     the CRT decomposition is TRIVIAL at %s (B is a chain ring, a "
            "single component): the component analysis of Task C3 carries no "
            "information and is therefore not tested here -- the chain-ring "
            "route is the Smith normal form, tested above (C5)" % tag)
        return None
    ncomp = len(tau)
    tid = all(tau[j] == j for j in range(ncomp))
    C1 = Z.Ctx(C.q, C.t, 1)          # the component context: M_2(A_t), n = 1
    say("     tau = %s   (tau = id: %s)%s"
        % (tau, tid,
           ";  n | p^s+1  <=>  %d | %d" % (C.n, C.p ** s + 1) if K.kind == "split"
           else ""))

    ncode = min(20, len(glist))
    bad_dual = 0
    bad_dim = 0
    bad_naive = 0
    bad_exact = 0
    for i in range(ncode):
        g = glist[i]
        R = hull_all_routes(C, [g], s)
        tot_exact = 0
        tot_naive = 0
        for j in range(ncomp):
            gj = proj_M(K, C, g, j)
            Cj = Z.right_ideal_basis(C1, [gj])
            gt = proj_M(K, C, g, tau[j])
            Ct = Z.right_ideal_basis(C1, [gt])
            Dt = dual_basis_def(C1, Ct, s)
            # (i) the component of the dual is the dual of the tau(j) component
            Dj_true = rref_rows(C1, [C1.flat_rn(proj_M(K, C, C.unflat_rn(tuple(v)), j))
                                     for v in R["Ddef"]])
            if Dj_true != Dt:
                bad_dual += 1
            # (ii) the component of the hull
            Hj_true = rref_rows(C1, [C1.flat_rn(proj_M(K, C, C.unflat_rn(tuple(v)), j))
                                     for v in R["hull_D"]])
            Hj_want = intersect_basis(C1, Cj, Dt)
            if Hj_true != Hj_want:
                bad_exact += 1
            tot_exact += len(Hj_want)
            # (iii) the naive componentwise hull
            Dj = dual_basis_def(C1, Cj, s)
            tot_naive += len(intersect_basis(C1, Cj, Dj))
        if tot_exact != R["dimhull"]:
            bad_dim += 1
        if tot_naive != R["dimhull"]:
            bad_naive += 1
    check("%s: (C^{perp_s})_j = (C_tau(j))^{perp_s} componentwise" % tag,
          bad_dual == 0, "%d codes x %d components" % (ncode, ncomp), False)
    check("%s: Hull_s(C)_j = C_j n (C_tau(j))^{perp_s}" % tag, bad_exact == 0,
          "%d codes x %d components" % (ncode, ncomp), False)
    check("%s: dim Hull = sum_j dim (C_j n (C_tau(j))^{perp_s})" % tag,
          bad_dim == 0, "%d codes" % ncode, False)
    if tid:
        check("%s: tau = id, so the hull decomposes: dim Hull = sum_j "
              "dim Hull_s(C_j)" % tag, bad_naive == 0, "%d codes" % ncode, False)
    else:
        check("%s: tau != id, so the NAIVE componentwise hull formula "
              "sum_j dim Hull_s(C_j) FAILS" % tag, bad_naive > 0,
              "%d of %d codes detect the failure" % (bad_naive, ncode), False)
    return dict(tau=tau, tid=tid, bad_naive=bad_naive, n=ncode)


# ==========================================================================
# 8.  Tasks D and E -- regimes, LCD, self-orthogonal, self-dual
# ==========================================================================

def test_taskDE(C, glist, s):
    tag = tags(C, s)
    refl = (2 * s) % C.r == 0
    rets = [hull_all_routes(C, [g], s) for g in glist]

    # ---- D1  dimension of the hull of the dual (proved: always equal) ----
    bad = 0
    for R in rets:
        HD = intersect_basis(C, R["Ddef"], dual_basis_def(C, R["Ddef"], s))
        if len(HD) != R["dimhull"]:
            bad += 1
    check("%s: dim Hull_s(C^{perp_s}) = dim Hull_s(C)  (all s)" % tag, bad == 0,
          "%d codes" % len(rets), exhaustive(C))

    # ---- D2  Hull(sigma_2s C) = sigma_2s Hull(C) ------------------------
    bad = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        R2 = hull_all_routes(C, [C.sigma_rn(g, 2 * s)], s)
        sh = rref_rows(C, [C.flat_rn(C.sigma_rn(C.unflat_rn(tuple(v)), 2 * s))
                           for v in R["hull_D"]])
        if sh != R2["hull_D"]:
            bad += 1
    check("%s: Hull_s(sigma_2s C) = sigma_2s Hull_s(C)  (all s)" % tag,
          bad == 0, "%d codes" % len(glist), exhaustive(C))

    # ---- D3  reflexive regime: hull of the dual = hull ------------------
    if refl:
        bad = 0
        for R in rets:
            HD = intersect_basis(C, R["Ddef"], dual_basis_def(C, R["Ddef"], s))
            if HD != R["hull_D"]:
                bad += 1
        check("%s: r | 2s, so Hull_s(C^{perp_s}) = Hull_s(C) as subspaces"
              % tag, bad == 0, "%d codes" % len(rets), exhaustive(C))
    else:
        # the same statement in the NON-reflexive regime: equivalent to the
        # inclusion Hull_s(C) <= sigma_2s(C);  recorded as a CONJECTURE.
        nz = 0
        inc_bad = 0
        set_bad = 0
        for R in rets:
            if not R["hull_D"]:
                continue
            nz += 1
            HD = intersect_basis(C, R["Ddef"], dual_basis_def(C, R["Ddef"], s))
            if HD != R["hull_D"]:
                set_bad += 1
            s2C = rref_rows(C, [C.flat_rn(C.sigma_rn(C.unflat_rn(tuple(x)), 2 * s))
                                for x in R["Ckey"]])
            if not all(Z.contains(C, s2C, tuple(v)) for v in R["hull_D"]):
                inc_bad += 1
        if nz == 0:
            say("     note: no nonzero hull at %s, so the non-reflexive "
                "inclusion test could not be run on this sample" % tag)
        else:
            check("%s [CONJECTURE; r does not divide 2s]: Hull_s(C) is "
                  "contained in sigma_2s(C)" % tag, inc_bad == 0,
                  "%d nonzero hulls tested, %d violations" % (nz, inc_bad),
                  exhaustive(C))
            check("%s: Hull_s(C^{perp_s}) = Hull_s(C) on this sample "
                  "(no counterexample found)" % tag, set_bad == 0,
                  "%d of %d nonzero hulls differ" % (set_bad, nz), exhaustive(C))

    # ---- E1  LCD -------------------------------------------------------
    bad = 0
    nlcd = 0
    for R in rets:
        is_lcd = (R["dimhull"] == 0)
        complement = (R["dimsum"] == C.dimw)
        Wzero = (R["dimWint"] == 0)
        if is_lcd != complement or is_lcd != Wzero:
            bad += 1
        if is_lcd:
            nlcd += 1
    check("%s: LCD <=> hull = 0 <=> C + C^{perp_s} = R_n <=> W n W' = 0" % tag,
          bad == 0, "%d codes, %d LCD" % (len(rets), nlcd), exhaustive(C))

    # ---- E2  self-orthogonal / self-dual --------------------------------
    bad_so = 0
    bad_sd = 0
    bad_imp = 0
    nso = nsd = 0
    for g, R in zip(glist, rets):
        v = C.theta_rn(C.rev_rn(g), s)
        vg = C.mul_rn(v, g)
        zero = C.RB.zero
        so_prod = (vg == zero)                       # theta_s(rev g) * g = 0
        so_set = (R["dimhull"] == R["dimC"])         # C <= C^{perp_s}
        if so_prod != so_set:
            bad_so += 1
        if so_set:
            nso += 1
            sd = (R["dimhull"] == R["dimC"] and 2 * R["dimC"] == C.dimw)
            sd_set = (tuple(tuple(x) for x in R["Ckey"]) == R["Ddef"])
            if sd != sd_set:
                bad_sd += 1
            if sd_set:
                nsd += 1
                # self-dual  =>  sigma_2s(C) = C
                Ck = tuple(tuple(x) for x in R["Ckey"])
                s2C = rref_rows(C, [C.flat_rn(C.sigma_rn(C.unflat_rn(tuple(x)), 2 * s))
                                    for x in Ck])
                if s2C != Ck:
                    bad_imp += 1
    check("%s: C <= C^{perp_s}  <=>  theta_s(rev g) * g = 0" % tag,
          bad_so == 0, "%d codes, %d self-orthogonal" % (len(rets), nso),
          exhaustive(C))
    if nso:
        check("%s: C = C^{perp_s}  <=>  self-orthogonal and 2 dim C = 4tn"
              % tag, bad_sd == 0, "%d self-orthogonal codes, %d self-dual"
              % (nso, nsd), exhaustive(C))
    else:
        say("     note: no self-orthogonal code in this sample, so the "
            "self-dual criterion is not exercised here (%s)" % tag)
    if nsd:
        check("%s: self-dual implies C is sigma_2s-stable" % tag, bad_imp == 0,
              "%d self-dual codes" % nsd, exhaustive(C))
    say("     census at %s: LCD %d, self-orthogonal %d, self-dual %d  (%d codes)"
        % (tag, nlcd, nso, nsd, len(rets)))
    return dict(nlcd=nlcd, nso=nso, nsd=nsd)


# ==========================================================================
# 9.  negative controls -- a wrong convention must FAIL
# ==========================================================================

def neg_controls(C, glist, s, K, tau):
    """
    Each control is a plausible-looking but WRONG statement.  The control
    passes only if a counterexample is found in the sample.
    """
    tag = tags(C, s)
    exh = exhaustive(C)
    n = len(glist)

    # neg-1  drop the reversal
    k = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        wrong = intersect_basis(C, R["Ckey"], Z.ann_r_set(C, [C.theta_rn(g, s)]))
        if wrong != R["hull_D"]:
            k += 1
    if k:
        check("neg-1 %s: omitting rev changes the hull" % tag, True,
              "%d of %d codes detect it" % (k, n), exh)
    else:
        say("     neg-1 %s is VACUOUS here: rev = id for n <= 2, so omitting "
            "it cannot change anything (the control is skipped, not passed)" % tag)

    # neg-2  ann_l instead of ann_r
    k = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        Al = Z.ann_l_element(C, C.theta_rn(C.rev_rn(g), s))
        wrong = intersect_basis(C, R["Ckey"], Al)
        if wrong != R["hull_D"]:
            k += 1
    check("neg-2 %s: ann_l instead of ann_r is wrong" % tag, k > 0,
          "%d of %d codes detect it" % (k, n), exh)

    # neg-3  Morita with ROWS instead of COLUMNS
    k = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        Wp = [(tuple(r[:C.B.dim]), tuple(r[C.B.dim:])) for r in R["Wint"]]
        rows = []
        for w in Wp:
            for b in Z._B_basis(C.B):
                M = (C.B.mul(w[0], b), C.B.mul(w[1], b), C.B.zero, C.B.zero)
                rows.append(list(C.flat_rn(M)))
                M = (C.B.zero, C.B.zero, C.B.mul(w[0], b), C.B.mul(w[1], b))
                rows.append(list(C.flat_rn(M)))
        wrong = rref_rows(C, rows)
        if wrong != R["hull_M"]:
            k += 1
    check("neg-3 %s: I_W built from ROWS instead of COLUMNS is wrong" % tag,
          k > 0, "%d of %d codes detect it" % (k, n), exh)

    # neg-4  the hull is always two-sided
    k = 0
    tot = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        if not R["hull_D"]:
            continue
        tot += 1
        if not Z.is_left_ideal(C, R["hull_D"]):
            k += 1
    if tot:
        check("neg-4 %s: the hull is NOT always two-sided" % tag, k > 0,
              "%d of %d nonzero hulls are not left ideals" % (k, tot), exh)
    else:
        say("     neg-4 %s: no nonzero hull in the sample -- control not "
            "exhibited here" % tag)

    # neg-5  Hull_s(sigma_k C) = Hull_s(C)  (wrong: it is sigma_k Hull_s(C))
    k = 0
    for g in glist[:12]:
        R = hull_all_routes(C, [g], s)
        for kk in range(1, C.r):
            R2 = hull_all_routes(C, [C.sigma_rn(g, kk)], s)
            if R2["hull_D"] != R["hull_D"]:
                k += 1
                break
    if k:
        check("neg-5 %s: Hull_s(sigma_k C) differs from Hull_s(C)" % tag, True,
              "%d of 12 codes detect it" % k, False)
    else:
        say("     neg-5 %s: every sampled code has a sigma_k-invariant hull "
            "here, so this control is not exhibited" % tag)

    # neg-6  the Euclidean pairing  sum_e x_e y_e  (no transpose, no sigma_s)
    def euclid_dual(C, Ckey):
        rows = []
        for v in Ckey:
            x = C.iota_inv(C.unflat_rn(tuple(v)))
            row = []
            for e0 in range(C.n):
                for kk in range(4):
                    i0, j0 = kk // 2, kk % 2
                    for a in range(C.t):
                        Y = C.RA.unit(i0, j0,
                                      C.A.pow(C.A.u, a) if C.t > 1 else C.A.one)
                        row.append(C.RA.Lambda(C.RA.mul(x[e0], Y)))
            rows.append(row)
        return nullspace_basis(rows, C.F, C.dimw)
    k = 0
    for g in glist:
        R = hull_all_routes(C, [g], s)
        De = rref_rows(C, [C.flat_rn(C.iota(C.unflat_word(tuple(v))))
                           for v in euclid_dual(C, R["Ckey"])])
        if De != R["Ddef"]:
            k += 1
    if k:
        check("neg-6 %s: the Euclidean form sum x_e y_e gives a different dual"
              % tag, True, "%d of %d codes detect it" % (k, n), False)
    else:
        say("     neg-6 %s: the Euclidean and the B_s dual coincided for all %d "
            "sampled codes, so this control is not exhibited here (it is a "
            "weak detector: many codes are both transpose- and sigma-stable)"
            % (tag, n))

    # neg-7  dim Hull is independent of s  (checked across s, at the end)
    return k


def neg_control_naive_crt(C, glist, s, K, tau):
    """neg-8: the naive componentwise hull when tau != id (see test_C3)."""
    if tau is None or all(tau[j] == j for j in range(len(tau))):
        return
    say("     neg-8 %s: the naive componentwise hull formula is already shown "
        "to fail by the tau != id test above" % tags(C, s))


# ==========================================================================
# 10.  the wild regime: can the hull itself be non-principal?
# ==========================================================================

def run_wild_hull(C, s, tries=60):
    """
    In the wild regime (p | n and t >= 2) mu_B(W) can be as large as 4, so a
    right ideal need not be principal (Stage 2A Thm 4.1 / Stage 2B).  The
    Stage-2C counterexample shows the DUAL can be non-principal; here we ask
    the sharper question for the HULL, whose W is an intersection
    W(C) n W(C^{perp_s}) and therefore usually smaller.
    """
    tag = tags(C, s)
    mrows = Z.max_ideal_wild(C)
    best = None
    for i in range(tries):
        g = Z.sample_elements(C, 1, seed_offset=90001 + i)[0]
        R = hull_all_routes(C, [g], s)
        Wp = [(tuple(r[:C.B.dim]), tuple(r[C.B.dim:])) for r in R["Wint"]]
        mu = 0 if not Wp else Z.mu_local(C, Wp, mrows)[0]
        if best is None or mu > best[0]:
            best = (mu, g, R)
    mu, g, R = best
    say("     [WILD] largest mu_B(W_hull) found over %d sampled codes at %s: %d"
        % (tries, tag, mu))
    if mu >= 3:
        ok = not is_principal(C, R["hull_D"]) if C.q ** R["dimhull"] <= 3000 \
            else None
        check("%s [WILD]: a hull with mu_B = %d is NOT principal" % (tag, mu),
              ok is True, "dim Hull = %d, |Hull| = %d, generator search %s"
              % (R["dimhull"], C.q ** R["dimhull"],
                 "exhaustive" if ok is not None else "skipped (too large)"),
              ok is not None)
    else:
        say("     [WILD] no hull with mu_B(W_hull) >= 3 was found in this "
            "sample, so a non-principal HULL is not exhibited here (the "
            "non-principal DUAL of Stage 2C is, and it is the same "
            "obstruction: M_2(m) at (4,2,2))")


# ==========================================================================
# 11.  driver
# ==========================================================================

class NoComponents(object):
    kind = "none"


CASE_NOTES = {
    (4, 1, 1): "split, n = 1: R_n = M_2(F_4); the theory degenerates to the "
               "ideal theory of M_2(F_4) (O-2.7).  Exhaustive where possible.",
    (4, 1, 2): "chain: t = 1 with p | n; B = F_4[X]/<(X-1)^2> is a chain ring.",
    (4, 2, 1): "chain: t >= 2 with p does not divide n; B = F_4[u]/<u^2>.",
    (4, 2, 2): "WILD: t >= 2 and p | n; B is local but not a chain ring.",
    (4, 1, 3): "split semisimple, B = F_4^3, n = 3: rev is non-trivial and "
               "tau != id for s = 0.",
    (9, 1, 2): "split semisimple, B = F_9 x F_9; r = 2, both s reflexive.",
    (8, 1, 2): "chain ring F_8[X]/<(X-1)^2>; r = 3 is odd, so NO non-trivial "
               "reflexive s exists -- the non-reflexive regime.",
    (4, 2, 3): "split, t >= 2, B = A_2^3; rev non-trivial, tau != id for s = 0.",
}



def conjecture_probe(C, s, tries=300):
    """
    A dedicated, larger test of the two equivalent statements

        (a)  Hull_s(C)  <=  sigma_2s(C),
        (b)  Hull_s(C^{perp_s}) = Hull_s(C)      (as subspaces),

    which are equivalent because the two hulls always have the same dimension
    (proved).  Only meaningful when r does not divide 2s: for r | 2s one has
    sigma_2s = id and both are immediate.  No proof is known to us; the status
    recorded in the register is CONJECTURE.
    """
    if (2 * s) % C.r == 0:
        return
    tag = tags(C, s)
    gl = Z.sample_elements(C, tries, seed_offset=77000 + s)
    nz = 0
    inc_bad = 0
    set_bad = 0
    for g in gl:
        R = hull_all_routes(C, [g], s)
        if not R["hull_D"]:
            continue
        nz += 1
        s2C = rref_rows(C, [C.flat_rn(C.sigma_rn(C.unflat_rn(tuple(x)), 2 * s))
                            for x in R["Ckey"]])
        if not all(Z.contains(C, s2C, tuple(v)) for v in R["hull_D"]):
            inc_bad += 1
        HD = intersect_basis(C, R["Ddef"], dual_basis_def(C, R["Ddef"], s))
        if HD != R["hull_D"]:
            set_bad += 1
    if nz == 0:
        say("     note: no nonzero hull among %d dedicated probes at %s"
            % (tries, tag))
        return
    check("%s [CONJECTURE, dedicated probe]: Hull_s(C) <= sigma_2s(C)" % tag,
          inc_bad == 0, "%d nonzero hulls out of %d codes, %d violations"
          % (nz, tries, inc_bad), False)
    check("%s [CONJECTURE, dedicated probe]: Hull_s(C^{perp_s}) = Hull_s(C)"
          % tag, set_bad == 0, "%d nonzero hulls, %d differ" % (nz, set_bad),
          False)


def run_case(q, t, n, sample=40):
    head("case (q,t,n) = (%d,%d,%d)%s" % (q, t, n, "   --   " + CASE_NOTES[(q, t, n)]
                                          if (q, t, n) in CASE_NOTES else ""))
    C = Z.Ctx(q, t, n)
    try:
        K = Z.Components(C)
    except RuntimeError:
        K = NoComponents()
        say("  no component routine for this (q,t,n); component-dependent "
            "checks are recorded as not applicable")
    say("  |B| = %d, |R_n| = %d, dim_{F_q} R_n = %d, r = %d, regimes: %s"
        % (C.q ** (C.t * C.n), (C.q ** (C.t * C.n)) ** 4, C.dimw, C.r, K.kind))

    fixed = Z.sample_elements(C, 12, seed_offset=555)
    for s in range(C.r):
        sub("s = %d   (r = %d, 2s mod r = %d, reflexive: %s)"
            % (s, C.r, (2 * s) % C.r, (2 * s) % C.r == 0))
        glist = Z.sample_elements(C, sample, seed_offset=1000 + 137 * s)
        test_taskA(C, glist, s)
        test_taskB(C, glist, s)
        test_taskC(C, glist, s, K)
        tau_d = test_C3(C, glist, s, K)
        test_taskDE(C, glist, s)
        neg_controls(C, glist, s, K,
                     tau_d["tau"] if tau_d else None)

    # ---- cross-s: is the hull dimension s-dependent? --------------------
    varying = 0
    detail = []
    for g in fixed:
        dims = []
        for s in range(C.r):
            R = hull_all_routes(C, [g], s)
            dims.append(R["dimhull"])
        if len(set(dims)) > 1:
            varying += 1
            if len(detail) < 3:
                detail.append(dims)
    if C.r > 1:
        if varying:
            check("(q,t,n)=(%d,%d,%d): dim Hull_s(C) depends on s" % (q, t, n),
                  True, "%d of 12 fixed codes vary; e.g. %s"
                  % (varying, detail), False)
        else:
            say("     note: no s-dependence of dim Hull was observed among the "
                "12 fixed codes at (q,t,n)=(%d,%d,%d)" % (q, t, n))

    for s in range(C.r):
        conjecture_probe(C, s)

    if K.kind == "wild":
        sub("wild regime: is the HULL itself ever non-principal?")
        for s in range(C.r):
            run_wild_hull(C, s)


def main():
    head("PHASE 3 -- STAGE 3A:  Galois hull structure and dimension theory")
    say("  seed %d ;  every [SMP] line carries the sample size" % SEED)
    say("  hull by four routes: pairing definition / annihilator+reversal / "
        "Morita im-ker / numerical identities")
    cases = [(4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2), (4, 1, 3),
             (9, 1, 2), (8, 1, 2), (4, 2, 3)]
    for (q, t, n) in cases:
        run_case(q, t, n)
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


if __name__ == "__main__":
    main()
