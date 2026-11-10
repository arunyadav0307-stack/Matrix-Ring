#!/usr/bin/env python3
"""
phase0_feasibility.py  --  PHASE 0 of the research blueprint
=============================================================
Project : Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
          over Noncommutative Matrix Rings
Task    : literature-independent MATHEMATICAL FEASIBILITY TESTS for the
          candidate alphabet  R = M_m(A_t),  A_t = F_q[u]/<u^t>.

The blueprint forbids assuming (a) that the entrywise Frobenius map is a ring
automorphism of M_m(A_t), (b) that a given pairing is non-degenerate, (c) that
commutative duality formulas transfer.  Every one of those is *tested* here by
exhaustive / randomised exact computation.

Experiments
-----------
  E1  (anti-)automorphism tests for  sigma_s (entrywise Frobenius),
      mu_c (u -> cu) and theta = sigma_s o transpose.
  E2  the Frobenius functional  Lambda = lambda o tr  (lambda = coefficient of
      u^{t-1}) is non-degenerate / "ideal catching"  <=>  the F_q-valued trace
      pairing (X,Y) |-> Lambda(XY) is a perfect duality.
  E3  n = 1: exhaustive comparison of LEFT vs RIGHT ideals of R under four
      candidate pairings -- does |C|*|C^perp| = |R| hold, and on which side
      does the dual land?
  E4  length-3 cyclic codes over M_2(F_2): complete enumeration (shift +
      one-sided multiplication closed), duals, hulls, cyclicity of the dual.
  E5  comparison of the complete enumeration with the generator
      parametrisation C = (fh) + u(fg) of Alahmadi-Sboui-Sole-Yemen (2013).

Run:  python3 phase0_feasibility.py
"""
import sys, os, json, time
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from matrix_ring_lib import (FiniteField, LocalRing, MatrixRing, Ambient,
                             row_space_basis, rref, nullspace, _intersect_clean)

OUT = []
def say(s=""):
    print(s, flush=True)
    OUT.append(str(s))

def hr(title):
    say()
    say("=" * 78)
    say(title)
    say("=" * 78)


def make_ring(p, r, t, m):
    F = FiniteField(p, r)
    A = LocalRing(F, t)
    R = MatrixRing(A, m)
    return F, A, R


# --------------------------------------------------------------------------
# E1: automorphism tests
# --------------------------------------------------------------------------
def test_automorphisms(p, r, t, m, trials=400):
    import random
    F, A, R = make_ring(p, r, t, m)
    random.seed(12345)
    els = list(R.elements())
    results = {}
    for s in range(r):
        f = R.entrywise(lambda z: A.frobenius(z, s))
        ok_add = ok_mul = True
        nontrivial = False
        for _ in range(min(trials, len(els) ** 2)):
            X = random.choice(els)
            Y = random.choice(els)
            if f(R.add(X, Y)) != R.add(f(X), f(Y)):
                ok_add = False
            if f(R.mul(X, Y)) != R.mul(f(X), f(Y)):
                ok_mul = False
            if f(X) != X:
                nontrivial = True
        results["sigma_%d" % s] = dict(additive=ok_add, multiplicative=ok_mul,
                                       nontrivial=nontrivial)
    # u-scaling  u -> c u
    if t > 1:
        c = 2 if F.q > 2 else (1 if F.q == 2 else 1)
        cands = [x for x in range(1, F.q)]
        c = cands[0]
        if F.q > 2:
            # pick an element of order > 1 in F_q^*
            for x in range(2, F.q):
                if F.order[x] > 1:
                    c = x
                    break
        f = R.entrywise(lambda z: A.uscale(z, c))
        ok_add = ok_mul = True
        nontrivial = False
        for _ in range(min(trials, len(els) ** 2)):
            X = random.choice(els)
            Y = random.choice(els)
            if f(R.add(X, Y)) != R.add(f(X), f(Y)):
                ok_add = False
            if f(R.mul(X, Y)) != R.mul(f(X), f(Y)):
                ok_mul = False
            if f(X) != X:
                nontrivial = True
        results["mu_c(c=%d)" % c] = dict(additive=ok_add,
                                         multiplicative=ok_mul,
                                         nontrivial=nontrivial)
    # theta = sigma_s o transpose  (expected: ANTI-automorphism)
    for s in range(r):
        def theta(X, s=s):
            return R.transpose(R.entrywise(lambda z: A.frobenius(z, s))(X))
        ok_add = ok_anti = True
        for _ in range(min(trials, len(els) ** 2)):
            X = random.choice(els)
            Y = random.choice(els)
            if theta(R.add(X, Y)) != R.add(theta(X), theta(Y)):
                ok_add = False
            if theta(R.mul(X, Y)) != R.mul(theta(Y), theta(X)):
                ok_anti = False
        results["theta_%d = sigma_%d o transpose" % (s, s)] = dict(
            additive=ok_add, anti_multiplicative=ok_anti)
    return results


# --------------------------------------------------------------------------
# E2: Frobenius functional / trace pairing
# --------------------------------------------------------------------------
def test_frobenius_functional(p, r, t, m):
    F, A, R = make_ring(p, r, t, m)
    amb = Ambient(R, 1)
    basis = R.basis_elements()
    d = len(basis)
    # Gram matrices of (X,Y) |-> Lambda(XY) on a basis; non-degeneracy of a
    # bilinear form is equivalent to invertibility of the Gram matrix.
    G = [[amb.Lambda(R.mul(X, Y)) for Y in basis] for X in basis]
    gr, piv = rref(F, [row[:] for row in G], d)
    right_nondegenerate = (len(piv) == d)
    H = [[amb.Lambda(R.mul(Y, X)) for Y in basis] for X in basis]
    hr_, piv2 = rref(F, [row[:] for row in H], d)
    left_nondegenerate = (len(piv2) == d)
    sym = all(G[i][j] == G[j][i] for i in range(d) for j in range(d))
    return dict(left_nondegenerate=left_nondegenerate,
                right_nondegenerate=right_nondegenerate,
                symmetric=sym, ring_size=F.q ** (m * m * t))


# --------------------------------------------------------------------------
# E3: n = 1 -- left vs right ideals, several pairings
# --------------------------------------------------------------------------
def ideals_of_R(R, side):
    amb = Ambient(R, 1)
    imgs = amb.left_images() if side == "left" else amb.right_images()
    seen = {}
    all_vecs = [amb.vec((X,)) for X in R.elements()]
    principals = []
    for v in all_vecs:
        b = amb.close_under(imgs, [v])
        principals.append(tuple(b))
    codes = set(principals)
    frontier = list(codes)
    while frontier:
        new = set()
        for A_ in frontier:
            for B_ in codes:
                if A_ == B_:
                    continue
                b = amb.close_under(imgs, list(A_) + list(B_))
                b = tuple(b)
                if b not in codes:
                    new.add(b)
        if not new:
            break
        codes |= new
        frontier = list(new)
    return sorted(codes, key=lambda c: (len(c), c)), amb


def side_of(amb, basis):
    """return a string describing on which side the code is a module"""
    if not basis:
        return "two-sided"
    b, piv = rref(amb.F, [list(v) for v in basis], amb.dim)
    right = all(in_span_fast(amb.F, b, piv, amb.apply_lin(imgs, v), amb.dim)
                for v in basis for imgs in amb.right_images())
    left = all(in_span_fast(amb.F, b, piv, amb.apply_lin(imgs, v), amb.dim)
               for v in basis for imgs in amb.left_images())
    if left and right:
        return "two-sided"
    if left:
        return "left"
    if right:
        return "right"
    return "neither (additive/F_q only)"


def _in(amb, basis, v):
    b, piv = rref(amb.F, list(basis), amb.dim)
    return in_span_fast(amb.F, b, piv, v, amb.dim)


def in_span_fast(F, basis, piv, v, ncols):
    v = list(v)
    for row, c in zip(basis, piv):
        if v[c] != 0:
            f = v[c]
            v = [F.sub(v[j], F.mul[f][row[j]]) for j in range(ncols)]
    return all(x == 0 for x in v)


def experiment_E3(p, r, t, m):
    F, A, R = make_ring(p, r, t, m)
    amb = Ambient(R, 1)
    dim = amb.dim
    pairings = [("dot (R-valued)", "dot"), ("dotT (R-valued)", "dotT"),
                ("sigma-inv (R-valued)", "sigmainv"),
                ("theta=sig o T (R-valued)", "theta"),
                ("trace (F_q-valued)", "trace"),
                ("trace-sigma (F_q-valued)", "tracesigma"),
                ("trace-theta (F_q-valued)", "tracetheta")]
    s = 1 if r > 1 else 0
    report = {}
    for side in ("left", "right"):
        codes, _ = ideals_of_R(R, side)
        rows = []
        for c in codes:
            k = len(c)
            entry = dict(dim=k, size=F.q ** k)
            for name, pid in pairings:
                D = amb.dual(list(c), pid, s)
                entry[name] = dict(dual_dim=len(D),
                                   perfect=(k + len(D) == dim),
                                   dual_side=side_of(amb, D))
            rows.append(entry)
        report[side + " ideals"] = dict(count=len(codes), rows=rows)
    report["ambient_dim"] = dim
    report["ring_size"] = F.q ** (m * m * t)
    return report


def print_E3(rep):
    pairings = ["dot (R-valued)", "dotT (R-valued)", "sigma-inv (R-valued)",
                "theta=sig o T (R-valued)", "trace (F_q-valued)",
                "trace-sigma (F_q-valued)", "trace-theta (F_q-valued)"]
    say("ambient F_q-dimension = %d, |R| = %d" % (rep["ambient_dim"],
                                                  rep["ring_size"]))
    for side in ("left ideals", "right ideals"):
        blk = rep[side]
        say()
        say("  --- %s: %d ideals found ---" % (side, blk["count"]))
        say("  %-6s %-12s %s" % ("dim C", "|C|", "".join(
            "%-30s" % p.split(" (")[0] for p in pairings)))
        for row in blk["rows"]:
            cells = []
            for p in pairings:
                e = row[p]
                cells.append("%-30s" % ("%d+%d=%s %s" % (
                    row["dim"], e["dual_dim"],
                    "OK " if e["perfect"] else "BAD",
                    e["dual_side"][:6])))
            say("  %-6d %-12d %s" % (row["dim"], row["size"], "".join(cells)))
    say()
    say("  legend: 'k+d=OK' means dim(C) + dim(C^perp) = dim(R) (perfect")
    say("  duality); the last word is the module side of the dual code.")


# --------------------------------------------------------------------------
# E4: length-3 cyclic codes over M_2(F_2)
# --------------------------------------------------------------------------
def enumerate_cyclic_codes(amb, side):
    """all F_q-subspaces of R^n closed under the cyclic shift and under
    coordinatewise LEFT (side='left') or RIGHT (side='right') multiplication
    by R.  For side='two-sided' both are imposed."""
    if side == "right":
        imgs = [amb.shift_images()] + amb.right_images()
    elif side == "left":
        imgs = [amb.shift_images()] + amb.left_images()
    else:
        imgs = ([amb.shift_images()] + amb.right_images()
                + amb.left_images())
    all_vecs = [amb.vec(v) for v in amb.all_vectors()]
    principals = set()
    for v in all_vecs:
        principals.add(tuple(amb.close_under(imgs, [v])))
    codes = set(principals)
    frontier = list(codes)
    while frontier:
        new = set()
        for A_ in frontier:
            for B_ in codes:
                b = tuple(amb.close_under(imgs, list(A_) + list(B_)))
                if b not in codes:
                    new.add(b)
        if not new:
            break
        codes |= new
        frontier = list(new)
    return sorted(codes, key=lambda c: (len(c), c))


def experiment_E4():
    F, A, R = make_ring(2, 1, 1, 2)          # R = M_2(F_2)
    amb = Ambient(R, 3)                       # length n = 3
    out = dict(ambient_dim=amb.dim, ring_size=16)
    for side in ("right", "left", "two-sided"):
        codes = enumerate_cyclic_codes(amb, side)
        out[side] = dict(count=len(codes),
                         dims=sorted(len(c) for c in codes))
    # duality / hull analysis for the RIGHT convention (the one used by the
    # matrix-ring cyclic-code literature: cyclic code = right ideal)
    codes = enumerate_cyclic_codes(amb, "right")
    rows = []
    s = 0 if amb.F.r == 1 else 1
    for c in codes:
        k = len(c)
        d_trace = amb.dual(list(c), "trace")
        d_dot = amb.dual(list(c), "dot")
        d_theta = amb.dual(list(c), "theta", s)
        d_tth = amb.dual(list(c), "tracetheta", s)
        hull_trace = _intersect_clean(F, list(c), d_trace, amb.dim)
        hull_dot = _intersect_clean(F, list(c), d_dot, amb.dim)
        hull_theta = _intersect_clean(F, list(c), d_theta, amb.dim)
        hull_tth = _intersect_clean(F, list(c), d_tth, amb.dim)
        rows.append(dict(
            dim=k,
            trace_dual_dim=len(d_trace),
            trace_perfect=(k + len(d_trace) == amb.dim),
            dot_dual_dim=len(d_dot),
            dot_perfect=(k + len(d_dot) == amb.dim),
            theta_dual_dim=len(d_theta),
            theta_perfect=(k + len(d_theta) == amb.dim),
            ttheta_dual_dim=len(d_tth),
            ttheta_perfect=(k + len(d_tth) == amb.dim),
            hull_trace_dim=len(hull_trace),
            hull_dot_dim=len(hull_dot),
            hull_theta_dim=len(hull_theta),
            hull_ttheta_dim=len(hull_tth),
            dot_dual_is_right=side_of(amb, d_dot) in ("right", "two-sided"),
            theta_dual_is_right=side_of(amb, d_theta) in ("right", "two-sided"),
            ttheta_dual_is_right=side_of(amb, d_tth) in ("right", "two-sided"),
            hull_ttheta_is_right=side_of(amb, hull_tth) in ("right", "two-sided"),
        ))
    out["right_rows"] = rows
    out["right_codes"] = [list(map(list, c)) for c in codes]
    return out, amb, codes


def print_E4(out):
    say("R = M_2(F_2), length n = 3, ambient F_2-dimension = %d"
        % out["ambient_dim"])
    for side in ("right", "left", "two-sided"):
        say("  %-11s cyclic codes (closed under shift + %s mult): %d"
            % (side, side, out[side]["count"]))
        say("      F_2-dimensions: %s" % out[side]["dims"])
    say()
    say("  Duality / hull table for the RIGHT convention "
        "(cyclic = right ideal):")
    say("  %-5s | %-14s %-14s | %-14s %-14s | %-11s %-11s %-11s %-11s" %
        ("dimC", "dot-dual", "dot perfect?", "theta-dual",
         "theta perfect?", "hull(dot)", "hull(theta)", "hull(tr-th)",
         "hull R-mod"))
    for r in out["right_rows"]:
        say("  %-5d | %-14s %-14s | %-14s %-14s | %-11d %-11d %-11d %-11s" % (
            r["dim"],
            "%d" % r["dot_dual_dim"],
            "OK" if r["dot_perfect"] else "BAD",
            "%d" % r["theta_dual_dim"],
            "OK" if r["theta_perfect"] else "BAD",
            r["hull_dot_dim"], r["hull_theta_dim"], r["hull_ttheta_dim"],
            "yes" if r["hull_ttheta_is_right"] else "NO"))
    say()
    say("  'theta'  = pairing  sum_i theta_s(x_i) y_i  with theta_s = "
        "sigma_s o transpose")
    say("  'tr-th'  = F_q-valued  Lambda(sum_i theta_s(x_i) y_i)")
    nbad = sum(1 for r in out["right_rows"] if not r["dot_perfect"])
    nbad2 = sum(1 for r in out["right_rows"] if not r["theta_perfect"])
    say("  codes with BROKEN duality under the naive Euclidean dot product: "
        "%d / %d" % (nbad, len(out["right_rows"])))
    say("  codes with BROKEN duality under the theta pairing            : "
        "%d / %d" % (nbad2, len(out["right_rows"])))


# --------------------------------------------------------------------------
# E5: comparison with Alahmadi-Sboui-Sole-Yemen, "Cyclic codes over M_2(F_2)"
#     (J. Franklin Inst. 350 (2013) 2837-2847), Thm. 1:
#     every cyclic code is  C = (f h) + u (f g)  with  x^n - 1 = f g h  over F_4.
# --------------------------------------------------------------------------
def experiment_E5(amb, all_right_codes):
    """Check the generator parametrisation of
    Alahmadi - Sboui - Sole - Yemen, 'Cyclic codes over M_2(F_2)',
    J. Franklin Inst. 350 (2013) 2837-2847, Theorem 1:

        every cyclic code of odd length n over A = M_2(F_2) = F_4 + u F_4
        (u^2 = 0) is of the form  C = (f h) + u (f g),  where
        x^n - 1 = f g h  is a factorisation into pairwise coprime
        polynomials over F_4.

    Three readings of the notation are tested:
      A : C = (fh)*R_n + (u*(fg))*R_n        (right ideals, u on the left)
      B : C = (fh)*R_n + ((fg)*u)*R_n        (right ideals, u on the right)
      C : C = { r + u t : r in (fh), t in (f) }   (residue + torsion reading,
          (fh) and (f) = the cyclic codes over F_4 with those generators)
    """
    R = amb.R
    n = amb.n
    one = R.one
    zero = R.zero

    def e(c):
        return (c,)
    W = ((e(0), e(1)), (e(1), e(1)))          # omega, omega^2+omega+1 = 0
    I = R.one
    W2 = R.mul(W, W)
    F4 = [zero, I, W, W2]
    i_mat = ((e(0), e(1)), (e(1), e(0)))      # i^2 = 1, i omega = omega^2 i
    u = R.add(I, i_mat)
    assert R.mul(i_mat, i_mat) == I
    assert R.mul(i_mat, W) == R.mul(W2, i_mat)
    dec = {}
    for a in F4:
        for b in F4:
            M = R.add(a, R.mul(u, b))
            dec.setdefault(M, 1)
    assert len(dec) == 16                     # A = F_4 (+) u F_4 as sets
    assert R.mul(u, u) == zero                # u^2 = 0

    def polymul(p, q):
        res = [zero] * n
        for a in range(n):
            if p[a] == zero:
                continue
            for b in range(n):
                if q[b] == zero:
                    continue
                k = (a + b) % n
                res[k] = R.add(res[k], R.mul(p[a], q[b]))
        return tuple(res)

    # irreducible factors of x^3 - 1 over F_4 : (x+1), (x+omega), (x+omega^2)
    factors = []
    for rt in [I, W, W2]:
        poly = [zero] * n
        poly[0] = rt          # constant term: x + root  (characteristic 2)
        poly[1] = I
        factors.append(tuple(poly))
    prod = factors[0]
    for f in factors[1:]:
        prod = polymul(prod, f)
    assert prod == tuple([zero] * n)          # product = x^3 - 1 == 0 mod x^3-1

    imgs = [amb.shift_images()] + amb.right_images()

    def f4_cyclic_code(gen):
        """cyclic code over F_4 of length n with generator polynomial gen"""
        out = set()
        for coeffs in product(range(4), repeat=n):
            q = tuple(F4[c] for c in coeffs)
            out.add(polymul(gen, q))
        return sorted(out)

    found = {"A": set(), "B": set(), "C": set()}
    for assign in product(range(3), repeat=3):
        parts = []
        for _ in range(3):
            pp = [zero] * n
            pp[0] = I                      # constant polynomial 1
            parts.append(pp)
        for idx, which in enumerate(assign):
            parts[which] = list(polymul(tuple(parts[which]),
                                        tuple(factors[idx])))
        f, g, h = [tuple(p) for p in parts]
        fh = polymul(f, h)
        fg = polymul(f, g)
        # variant A : right ideals, u on the left
        u_fg = tuple(R.mul(u, fg[k]) for k in range(n))
        found["A"].add(tuple(amb.close_under(imgs,
                                             [amb.vec(fh), amb.vec(u_fg)])))
        # variant B : right ideals, u on the right
        fg_u = tuple(R.mul(fg[k], u) for k in range(n))
        found["B"].add(tuple(amb.close_under(imgs,
                                             [amb.vec(fh), amb.vec(fg_u)])))
        # variant C : residue + torsion,  C = { r + u t }
        Rcode = f4_cyclic_code(fh)
        Tcode = f4_cyclic_code(f)
        vecs = []
        for r in Rcode:
            for t in Tcode:
                word = tuple(R.add(r[k], R.mul(u, t[k])) for k in range(n))
                vecs.append(amb.vec(word))
        found["C"].add(tuple(row_space_basis(amb.F, vecs, amb.dim)))

    all_codes = set(tuple(c) for c in all_right_codes)
    res = {}
    for variant in ("A", "B", "C"):
        s = found[variant]
        prof = {}
        for c in s:
            prof[len(c)] = prof.get(len(c), 0) + 1
        res[variant] = dict(distinct_codes=len(s),
                            contained_in_enumeration=s <= all_codes,
                            missing=len(all_codes - s),
                            profile=dict(sorted(prof.items())))
    prof = {}
    for c in all_codes:
        prof[len(c)] = prof.get(len(c), 0) + 1
    res["complete"] = dict(count=len(all_codes), profile=dict(sorted(prof.items())))
    return res


# --------------------------------------------------------------------------
def main():
    t0 = time.time()
    hr("PHASE 0 FEASIBILITY EXPERIMENTS  (exact arithmetic, no assumptions)")
    say("ring family:  R = M_m(A_t),  A_t = F_q[u]/<u^t>,  q = p^r")
    say("run date: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    say("python: %s" % sys.version.split()[0])

    # ---------------- E1
    hr("E1  Automorphism tests on R = M_m(A_t)")
    say("Question: is the entrywise Frobenius  sigma_s(a) = a^(p^s)  (extended")
    say("entrywise to matrices) a ring AUTOMORPHISM?  Is  theta = sigma o")
    say("transpose an ANTI-automorphism?  Is it nontrivial?")
    say()
    for (p, r, t, m) in [(2, 1, 1, 2), (2, 2, 1, 2), (2, 1, 2, 2),
                         (2, 2, 2, 2), (2, 1, 1, 3), (3, 2, 1, 2)]:
        res = test_automorphisms(p, r, t, m)
        say("  q=p^r=%d^%d=%d, t=%d, m=%d, |R|=%d"
            % (p, r, p ** r, t, m, (p ** r) ** (m * m * t)))
        for name, v in res.items():
            if "anti_multiplicative" in v:
                say("      %-32s additive=%-5s anti-mult=%-5s"
                    % (name, v["additive"], v["anti_multiplicative"]))
            else:
                say("      %-32s additive=%-5s mult=%-5s nontrivial=%-5s"
                    % (name, v["additive"], v["multiplicative"],
                       v["nontrivial"]))
    say()
    say("  NOTE: for q = p (r = 1) the *field* Frobenius is the identity, so a")
    say("  nontrivial Galois-type twist needs r >= 2 (q = p^r, s in 1..r-1) or")
    say("  an automorphism moving u (mu_c) or an inner (PGL_m) automorphism.")

    # ---------------- E2
    hr("E2  Frobenius functional  Lambda = lambda o tr  (lambda = coeff of u^(t-1))")
    say("Lambda non-degenerate on both sides  <=>  the F_q-valued pairing")
    say("(X,Y) |-> Lambda(XY) is a perfect duality (Wood 1999: Frobenius ring).")
    say()
    for (p, r, t, m) in [(2, 1, 1, 2), (2, 2, 1, 2), (2, 1, 2, 2),
                         (2, 2, 2, 2), (2, 1, 1, 3), (2, 4, 1, 2)]:
        res = test_frobenius_functional(p, r, t, m)
        say("  q=%d, t=%d, m=%d, |R|=%-6d  left-nondeg=%-5s right-nondeg=%-5s symmetric=%s"
            % (p ** r, t, m, res["ring_size"], res["left_nondegenerate"],
               res["right_nondegenerate"], res["symmetric"]))

    # ---------------- E3
    hr("E3  n = 1: LEFT ideals vs RIGHT ideals under four candidate pairings")
    for (p, r, t, m) in [(2, 1, 1, 2), (2, 2, 1, 2), (2, 1, 2, 2)]:
        say()
        say("### R = M_%d(F_%d[u]/<u^%d>),  |R| = %d"
            % (m, p ** r, t, (p ** r) ** (m * m * t)))
        rep = experiment_E3(p, r, t, m)
        print_E3(rep)

    # ---------------- E4
    hr("E4  Complete enumeration of length-3 cyclic codes over M_2(F_2)")
    out, amb, codes = experiment_E4()
    print_E4(out)

    # ---------------- E5
    hr("E5  Check against Alahmadi-Sboui-Sole-Yemen (2013), Thm. 1")
    say("Their parametrisation: every cyclic code of odd length n over")
    say("M_2(F_2) = F_4 + u F_4  (u^2 = 0) is  C = (f h) + u (f g)  with")
    say("x^n - 1 = f g h  a factorisation into pairwise coprime polynomials")
    say("over F_4.  For n = 3 there are 3^3 = 27 such triples.")
    say()
    res = experiment_E5(amb, codes)
    say("  cyclic codes found by complete enumeration : %d"
        % res["complete"]["count"])
    say("      dimension profile (F_2-dim : #codes): %s"
        % res["complete"]["profile"])
    for variant, label in (("A", "u on the left,  C = (fh)R_n + u(fg)R_n"),
                           ("B", "u on the right, C = (fh)R_n + (fg)u R_n"),
                           ("C", "residue+torsion, C = {r + u t}")):
        v = res[variant]
        say()
        say("  --- reading %s : %s" % (variant, label))
        say("      distinct codes produced      : %d" % v["distinct_codes"])
        say("      dimension profile            : %s" % v["profile"])
        say("      all of them are cyclic codes : %s"
            % v["contained_in_enumeration"])
        say("      cyclic codes NOT produced    : %d" % v["missing"])
    say()
    say("  Interpretation: this is a COMPUTATIONAL OBSERVATION on one fixed")
    say("  parameter set (m = 2, q = 2, t = 1, n = 3, exhaustive over all")
    say("  2^12 ambient vectors).  It is evidence, not a proof, and must be")
    say("  re-derived by hand against the original paper in Phase 1.")

    hr("END OF EXPERIMENTS   (%.1f s)" % (time.time() - t0))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "phase0_results.txt")
    with open(path, "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    print("\n[log written to %s]" % path)


if __name__ == "__main__":
    main()
