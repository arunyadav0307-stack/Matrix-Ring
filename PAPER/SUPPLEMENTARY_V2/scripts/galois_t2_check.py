#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TASK 1 -- EXTENSION TO t = 2 (a NON-FIELD local alphabet).

All the proofs in 03_THEOREMS/PAIRING_COMPLETE_PROOFS.md are uniform in the
nilpotency exponent t.  This script tests the case t = 2 with a NONTRIVIAL
Galois parameter, which the main experiment (t = 1 only) does not cover:

    q = 4 (p = 2, r = 2),  A = F_4[u]/<u^2>,  R = M_2(A),  n = 1,  s = 1.

Ambient size |R| = 4^8 = 65536, so brute force over R^n is impossible; the
cyclic codes (right ideals of R_1 = R) are enumerated through the Morita
correspondence  right ideals of M_m(A)  <->  A-submodules of A^m,  and the
A-submodules of A^2 are enumerated exhaustively (|A^2| = 256).

Everything is exact arithmetic (Python 3, standard library).
"""
import sys
import time
import itertools
import random

from matrix_ring_lib import (FiniteField, LocalRing, MatrixRing, Ambient,
                             rref, nullspace, row_space_basis, in_span,
                             _intersect_clean)

LINES = []


def say(s=""):
    print(s, flush=True)
    LINES.append(str(s))


def main():
    say("t = 2 CHECK  (q = 4, A = F_4[u]/<u^2>, R = M_2(A), n = 1, s = 1)")
    say("run: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    t0 = time.time()
    F = FiniteField(2, 2)
    q = F.q
    T = 2
    m = 2
    n = 1
    A = LocalRing(F, T)
    R = MatrixRing(A, m)
    amb = Ambient(R, n)
    N = amb.dim                      # = n * t * m^2 = 8
    say("")
    say("q = %d, t = %d, m = %d, n = %d ; N = dim_{F_q} R^n = %d ; |R^n| = %d"
        % (q, T, m, n, N, q ** N))

    # ---------------- sigma_1 -------------------------------------------
    say("")
    say("-- sigma_1 (Frobenius on the F_4-coefficients, u fixed) --")
    ok_add = ok_mul = True
    elems = list(A.elements())
    for a in elems:
        for b in elems:
            if A.frobenius(A.add(a, b), 1) != A.add(A.frobenius(a, 1),
                                                    A.frobenius(b, 1)):
                ok_add = False
            if A.frobenius(A.mul(a, b), 1) != A.mul(A.frobenius(a, 1),
                                                    A.frobenius(b, 1)):
                ok_mul = False
    wit = next(a for a in elems if A.frobenius(a, 1) != a)
    say("   additive = %s ; multiplicative = %s ; nontrivial: %s -> %s"
        % (ok_add, ok_mul, wit, A.frobenius(wit, 1)))
    say("   (u is fixed: sigma_1(u) = u : %s)"
        % (A.frobenius((0, F.one), 1) == (0, F.one)))

    # ---------------- theta_1 -------------------------------------------
    RB = R.basis_elements()
    RBAS = list(R.elements())          # |M_2(A)| = 16^4 = 65536
    say("-- theta_1 = sigma_1 o transpose  (|M_2(A)| = %d) --" % len(RBAS))
    say("   additivity: checked on all sums of basis elements")
    ok_add_theta = all(
        R.entrywise(lambda z: A.frobenius(z, 1))(
            R.transpose(R.add(a, b)))
        == R.add(R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(a)),
                 R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(b)))
        for a in RB for b in RB)
    say("      theta_1(X+Y) = theta_1(X) + theta_1(Y) : %s" % ok_add_theta)
    rnd = random.Random(20261104)
    ok_anti = True
    for _ in range(5000):
        a = rnd.choice(RBAS)
        b = rnd.choice(RBAS)
        lhs = R.entrywise(lambda z: A.frobenius(z, 1))(
            R.transpose(R.mul(a, b)))
        rhs = R.mul(R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(b)),
                    R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(a)))
        if lhs != rhs:
            ok_anti = False
    say("   theta_1(AB) = theta_1(B) theta_1(A) : %s  [5000 uniformly random "
        "pairs, seed 20261104 -- SAMPLED, not exhaustive]" % ok_anti)
    ok_sq = True
    for a in RBAS:
        th = R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(a))
        th2 = R.entrywise(lambda z: A.frobenius(z, 1))(R.transpose(th))
        if th2 != a:
            ok_sq = False
    say("   theta_1^2 = identity on all %d matrices (2s = 2 = 0 mod r): %s"
        % (len(RBAS), ok_sq))

    # ---------------- Lambda --------------------------------------------
    say("-- Lambda = lambda o tr, lambda = coefficient of u^{t-1} --")
    bas = R.basis_elements()
    G = [[amb.Lambda(R.mul(a, b)) for b in bas] for a in bas]
    rk, _ = rref(F, G, len(bas))
    say("   Gram matrix of (X,Y) -> Lambda(XY) on M_2(F_4[u]/<u^2>): "
        "rank %d / %d" % (len(rk), len(bas)))
    say("   Lambda(XY) = Lambda(YX) for all pairs: %s"
        % all(amb.Lambda(R.mul(a, b)) == amb.Lambda(R.mul(b, a))
              for a in bas for b in bas))

    # ---------------- enumerate the A-submodules of A^m ------------------
    say("-- enumeration of the cyclic codes (right ideals of R) --")
    elemsA = list(A.elements())
    vecs = list(itertools.product(elemsA, repeat=m))     # |A^m| = 256
    seen = {}

    def flat(w):
        out = []
        for comp in w:
            out.extend(comp)
        return tuple(out)

    # the ZERO submodule must be seeded explicitly (it is a right ideal too);
    # without it the count comes out one short (32 instead of 33).
    seen = {tuple(): []}
    for v in vecs:
        if not any(flat(v)):
            continue
        gens = [tuple(A.mul(a, v[i]) for i in range(m)) for a in elemsA]
        cur = row_space_basis(F, [flat(g) for g in gens], m * T)
        seen[tuple(sorted(cur))] = cur
    subs = list(seen.values())
    changed = True
    while changed:
        changed = False
        cur = list(subs)
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                s = row_space_basis(F, list(cur[i]) + list(cur[j]), m * T)
                k = tuple(sorted(s))
                if k not in seen:
                    seen[k] = s
                    subs.append(s)
                    changed = True
    say("   #A-submodules of A^%d = %d  (= #right ideals of M_%d(A))"
        % (m, len(subs), m))
    dims = {}
    for W in subs:
        dims[len(W)] = dims.get(len(W), 0) + 1
    say("   F_q-dimension distribution (dim W : #) : %s"
        % sorted(dims.items()))

    # build the right ideals
    ideals = []
    for W in subs:
        gens = []
        for w in W:                       # w : m blocks of t coefficients
            for j in range(m):            # column position
                v = [0] * N
                for i in range(m):
                    for l in range(T):
                        v[l * m * m + i * m + j] = w[i * T + l]
                gens.append(tuple(v))
        ideals.append(row_space_basis(F, gens, N) if gens else [])
    say("   #right ideals = %d ; F_q-dim distribution : %s"
        % (len(ideals),
           sorted((d, sum(1 for b in ideals if len(b) == d))
                  for d in sorted(set(len(b) for b in ideals)))))

    # ---------------- checks ---------------------------------------------
    rbas = R.basis_elements()
    for s in (1,):
        say("-- per-code checks, s = %d (all %d codes) --" % (s, len(ideals)))
        cnt = dict(right=0, size=0, dualright=0, hullright=0, dd=0, dd_eq=0,
                   plain_size=0, plain_right=0, plain_left=0)
        for C in ideals:
            rb, piv = rref(F, C, N) if C else ([], [])

            def mem(v, rb=rb, piv=piv):
                if not rb:
                    return not any(v)
                return in_span(F, rb, piv, v, N)
            if all(mem(amb.vec(amb.right_mult(amb.unvec(x), b)))
                   for x in C for b in rbas):
                cnt["right"] += 1
            D = row_space_basis(F, amb.dual(C, "theta", s), N)
            rbd, pivd = rref(F, D, N) if D else ([], [])

            def memd(v, rbd=rbd, pivd=pivd):
                if not rbd:
                    return not any(v)
                return in_span(F, rbd, pivd, v, N)
            if all(memd(amb.vec(amb.right_mult(amb.unvec(y), b)))
                   for y in D for b in rbas):
                cnt["dualright"] += 1
            if len(C) + len(D) == N:
                cnt["size"] += 1
            H = _intersect_clean(F, C, D, N) if (C and D) else []
            rbh, pivh = rref(F, H, N) if H else ([], [])

            def memh(v, rbh=rbh, pivh=pivh):
                if not rbh:
                    return not any(v)
                return in_span(F, rbh, pivh, v, N)
            if all(memh(amb.vec(amb.right_mult(amb.unvec(z), b)))
                   for z in H for b in rbas):
                cnt["hullright"] += 1
            DD = row_space_basis(F, amb.dual(D, "theta", s), N)
            Csig = row_space_basis(
                F, [amb.vec(tuple(tuple(tuple(
                        A.frobenius(X[i][j], (2 * s) % 2) for j in range(m))
                        for i in range(m)) for X in amb.unvec(x)))
                    for x in C], N) if C else []
            if tuple(sorted(DD)) == tuple(sorted(Csig)):
                cnt["dd"] += 1
            if tuple(sorted(DD)) == tuple(sorted(C)):
                cnt["dd_eq"] += 1
            P = amb.dual(C, "dot", s)
            if len(C) + len(P) == N:
                cnt["plain_size"] += 1
            rbp, pivp = rref(F, P, N) if P else ([], [])

            def memp(v, rbp=rbp, pivp=pivp):
                if not rbp:
                    return not any(v)
                return in_span(F, rbp, pivp, v, N)
            if all(memp(amb.vec(amb.right_mult(amb.unvec(y), b)))
                   for y in P for b in rbas):
                cnt["plain_right"] += 1
            if all(memp(amb.vec(amb.left_mult(amb.unvec(y), b)))
                   for y in P for b in rbas):
                cnt["plain_left"] += 1
        say("      C right R-submodule ................ %d/%d"
            % (cnt["right"], len(ideals)))
        say("      C^{perp_s} right R-submodule ....... %d/%d"
            % (cnt["dualright"], len(ideals)))
        say("      |C|.|C^{perp_s}| = |R|^n ........... %d/%d"
            % (cnt["size"], len(ideals)))
        say("      Hull_s(C) right R-submodule ........ %d/%d"
            % (cnt["hullright"], len(ideals)))
        say("      (C^{perp_s})^{perp_s} = sigma_{2s}(C) %d/%d"
            % (cnt["dd"], len(ideals)))
        say("      (C^{perp_s})^{perp_s} = C .......... %d/%d"
            % (cnt["dd_eq"], len(ideals)))
        say("      PLAIN dual: right module %d/%d ; left module %d/%d ; "
            "size formula %d/%d"
            % (cnt["plain_right"], len(ideals), cnt["plain_left"],
               len(ideals), cnt["plain_size"], len(ideals)))
    say("")
    say("   [elapsed %.1f s]" % (time.time() - t0))
    with open("galois_t2_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    say("   log written to galois_t2_log.txt")


if __name__ == "__main__":
    main()
