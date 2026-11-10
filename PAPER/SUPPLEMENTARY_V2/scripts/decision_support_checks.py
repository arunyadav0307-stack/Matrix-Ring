"""
DECISION SUPPORT (B3):  what exactly survives, and what exactly breaks, when
the Galois duality is NOT reflexive (r does not divide 2s)?

Notation as in the rest of the project:
    B_s(x,y) = sum_e theta_s(x_e) y_e  in R          (theta_s = sigma_s o transpose)
    b_s(x,y) = Lambda(B_s(x,y))        in F_q        (Lambda = lambda o tr)
    C^perp   = { y : B_s(x,y) = 0 for all x in C }

Proved identities (see 06_AUDIT/PHASE0_PROOF_VERIFICATION.md):

    (I)   theta_s(B_s(x,y)) = B_s(y, sigma_{2s} x)
    (II)  Lambda(theta_s M) = sigma_s(Lambda(M))        [Lambda o sigma_s = sigma_s o Lambda,
                                                         tr(M^T) = tr(M)]
    (III) sigma_s( b_s(x,y) ) = b_s( y, sigma_{2s} x )           from (I)+(II)
    (IV)  b_s(y,x) = sigma_s( b_s( sigma_{-2s} x, y ) )          from (III)

Consequences tested here:

  H1  (III) holds for ALL s                          (identity, no hypothesis)
  H2  b_s(y,x) = sigma_s(b_s(x,y))                <=> sigma_{2s} = id  <=>  r | 2s
                                                      ("sigma_s-Hermitian")
  H3  (IV) holds for ALL s                           (identity, no hypothesis)
  H4  T(y,x) = T(x,y) for T = Tr_{F_q/F_p} o b_s  <=  r | 2s   (Frobenius-invariance
      of the field trace).  T is the F_p-bilinear form whose matrix is the
      commutation matrix in a stabilizer/CSS construction, so H4 is the property
      that makes the standard quantum machinery apply.
  H5  for a code C with basis (g_i): the Gram matrix M_ij = b_s(g_i,g_j) is
      sigma_s-Hermitian (M_ji = sigma_s(M_ij))  <=  r | 2s.

Enumerative consequences (on the cyclic codes of the given (q, n)):

  L1  # LCD codes (Hull = 0)
  L2  of those, # whose dual is again LCD      (needs C^perp n (C^perp)^perp = 0,
                                                i.e. C^perp n sigma_{2s}(C) = 0 --
                                                NOT implied by C n C^perp = 0 when
                                                sigma_{2s} != id)
  L3  # self-orthogonal (C <= C^perp), # self-dual (C = C^perp)
  L4  # reflexive (C^{perp perp} = C)

Run:  python3 -u decision_support_checks.py
"""

import importlib.util
import os
import random
import time

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "gd", os.path.join(HERE, "galois_duality_experiments.py"))
gd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gd)

from matrix_ring_lib import FiniteField, nullspace, row_space_basis


def bs(F, s, x, y, m, n):
    """b_s(x,y) = Lambda(B_s(x,y)) -- an element of F_q (t = 1 here)"""
    return gd.mtrace(F, gd.pair_theta(F, s, x, y, m, n), m)


def field_trace(F, a):
    """Tr_{F_q/F_p}(a) = sum_{i=0}^{r-1} sigma_i(a)"""
    acc = 0
    for i in range(F.r):
        acc = F.add[acc][F.frob[i][a]]
    return acc


def dual_of(F, basis, m, n, s):
    return gd.dual_of(F, basis, m, n, s, gd.pair_theta)


def hull_dim(F, basis, m, n, s):
    """dim Hull = dim C - rank of the Gram matrix G_ij = b_s(c_j, c_i)
    (x = sum a_i c_i is in the hull iff sum_i a_i b_s(c_j, c_i) = 0 for all j)"""
    N = n * m * m
    if not basis:
        return 0
    G = []
    for c in basis:
        G.append([bs(F, s, c, ci, m, n) for ci in basis])
    sols = nullspace(F, G, len(basis))
    return len(sols)


def key(F, basis):
    return gd.subspace_key(basis)


def check_case(p, r, m, n, slist, seed=20261104):
    F = FiniteField(p, r)
    N = n * m * m
    print()
    print("=" * 78)
    print("q = %d^%d = %d ,  m = %d ,  n = %d ,  N = %d" % (p, r, F.q, m, n, N))
    print("=" * 78)
    codes, _ = gd.enumerate_ideals_morita(F, m, n, verbose=False, limit=5000,
                                          seed=seed)
    print("cyclic codes enumerated: %d" % len(codes))
    rnd = random.Random(seed)

    for s in slist:
        k2 = (2 * s) % r
        km2 = (-2 * s) % r
        reflexive_param = (k2 == 0)
        print()
        print("  s = %d :  2s mod r = %d   ->   r | 2s : %s"
              % (s, k2, reflexive_param))

        # ---------- H1 - H4 on random vectors -----------------------------
        h1 = h2 = h3 = h4 = 0
        T = 300
        for _ in range(T):
            x = tuple(rnd.randrange(F.q) for _ in range(N))
            y = tuple(rnd.randrange(F.q) for _ in range(N))
            bxy = bs(F, s, x, y, m, n)
            byx = bs(F, s, y, x, m, n)
            s2x = gd.rn_sigma(F, k2, x)
            sm2x = gd.rn_sigma(F, km2, x)
            # H1: sigma_s(b(x,y)) = b(y, sigma_{2s} x)
            if F.frob[s % r][bxy] == bs(F, s, y, s2x, m, n):
                h1 += 1
            # H2: b(y,x) = sigma_s(b(x,y))
            if byx == F.frob[s % r][bxy]:
                h2 += 1
            # H3: b(y,x) = sigma_s(b(sigma_{-2s} x, y))
            if byx == F.frob[s % r][bs(F, s, sm2x, y, m, n)]:
                h3 += 1
            # H4: Tr(b(y,x)) = Tr(b(x,y))
            if field_trace(F, byx) == field_trace(F, bxy):
                h4 += 1
        print("      H1  sigma_s(b(x,y)) = b(y, sigma_{2s}x)        : %3d/%d"
              % (h1, T))
        print("      H2  b(y,x) = sigma_s(b(x,y))   [Hermitian]     : %3d/%d"
              % (h2, T))
        print("      H3  b(y,x) = sigma_s(b(sigma_{-2s}x, y))       : %3d/%d"
              % (h3, T))
        print("      H4  Tr(b(y,x)) = Tr(b(x,y))  [F_p-symmetric]   : %3d/%d"
              % (h4, T))

        # ---------- H5 on enumerated codes --------------------------------
        h5 = 0
        for C in codes:
            ok = True
            for i in range(len(C)):
                for j in range(len(C)):
                    if bs(F, s, C[j], C[i], m, n) != \
                       F.frob[s % r][bs(F, s, C[i], C[j], m, n)]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                h5 += 1
        print("      H5  Gram matrix of C is sigma_s-Hermitian      : %3d/%d codes"
              % (h5, len(codes)))

        # ---------- L5, L6 -------------------------------------------------
        # L5: is  dim Hull(C^perp) = dim Hull(C)  ?  (if so, "C is LCD" is
        #     equivalent to "C^perp is LCD" in BOTH regimes -- note
        #     Hull(C^perp) = C^perp n (C^perp)^perp = C^perp n sigma_{2s}(C))
        # L6: do the two 35-code (resp. 6-code) families coincide, i.e. is
        #     "Gram matrix of C is sigma_s-Hermitian"  <=>  "sigma_{2s}(C) = C"
        #     (equivalently <=> C is reflexive)?
        h5set = set()
        reflset = set()
        hull_equal = 0
        maxdiff = 0
        for idx, C in enumerate(codes):
            herm = True
            for i in range(len(C)):
                for j in range(len(C)):
                    if bs(F, s, C[j], C[i], m, n) != \
                       F.frob[s % r][bs(F, s, C[i], C[j], m, n)]:
                        herm = False
                        break
                if not herm:
                    break
            D = dual_of(F, C, m, n, s)
            isrefl = (key(F, dual_of(F, D, m, n, s)) == key(F, C))
            if herm:
                h5set.add(idx)
            if isrefl:
                reflset.add(idx)
            hc = hull_dim(F, C, m, n, s)
            hd = hull_dim(F, D, m, n, s)
            if hc == hd:
                hull_equal += 1
            maxdiff = max(maxdiff, abs(hc - hd))
        print("      L5  dim Hull(C^perp) = dim Hull(C)            : %3d/%d codes"
              "   (max |diff| = %d)" % (hull_equal, len(codes), maxdiff))
        print("      L6  {Hermitian Gram} = {reflexive}            : %s"
              "   (|H|=%d, |R|=%d, |H n R|=%d)"
              % (h5set == reflset, len(h5set), len(reflset),
                 len(h5set & reflset)))

        # ---------- L1 - L4 ------------------------------------------------
        lcd = lcd_dual = so = sd = refl = 0
        for C in codes:
            hd = hull_dim(F, C, m, n, s)
            D = dual_of(F, C, m, n, s)
            DD = dual_of(F, D, m, n, s)
            sC = row_space_basis(F, [gd.rn_sigma(F, k2, c) for c in C], N) \
                if C else []
            if hd == 0:
                lcd += 1
                if hull_dim(F, D, m, n, s) == 0:
                    lcd_dual += 1
            if hd == len(C):
                so += 1
            if key(F, C) == key(F, D):
                sd += 1
            if key(F, DD) == key(F, C):
                refl += 1
            # sanity: double-dual formula
            assert key(F, DD) == key(F, sC), "double-dual formula failed!"
        print("      L1  LCD (Hull = 0)                            : %3d/%d"
              % (lcd, len(codes)))
        print("      L2  LCD whose dual is LCD                     : %3d/%d"
              % (lcd_dual, lcd if lcd else 1))
        print("      L3  self-orthogonal / self-dual               : %3d / %3d"
              % (so, sd))
        print("      L4  reflexive (C^{perp perp} = C)             : %3d/%d"
              % (refl, len(codes)))
        print("      (assertion '(C^perp)^perp = sigma_{2s}(C)' held for "
              "all %d codes)" % len(codes))


def main():
    print("DECISION SUPPORT (B3): reflexive (r | 2s) vs general Galois regime")
    print("run: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print("NOTE: the Morita enumerator needs X^n - 1 squarefree; in char 2 this")
    print("      forces n odd.")
    check_case(2, 2, 2, 3, [1])        # q = 4,  r = 2,  r | 2s
    check_case(3, 2, 2, 2, [1])        # q = 9,  r = 2,  r | 2s
    check_case(2, 3, 2, 3, [1, 2])     # q = 8,  r = 3,  r does NOT divide 2s
    check_case(3, 3, 2, 1, [1, 2])     # q = 27, r = 3,  r does NOT divide 2s
    print()
    print("done")


if __name__ == "__main__":
    main()
