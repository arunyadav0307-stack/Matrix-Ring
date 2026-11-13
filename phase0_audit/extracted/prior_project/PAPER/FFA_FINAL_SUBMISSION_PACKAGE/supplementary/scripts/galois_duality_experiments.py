#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 0 (REVISED) -- TASK 1:  NONTRIVIAL GALOIS EXPERIMENTS  (q = 4, 8, 9)

Exact arithmetic only (no floating point).  Python 3, standard library.
Uses FiniteField + linear algebra from matrix_ring_lib.py (same file that
produced the original Phase-0 log).

Setting
-------
p prime, q = p^r with r >= 2,  A = F_q (t = 1),  R = M_m(F_q),  n >= 1 with
gcd(n,p) = 1 (so that X^n - 1 is squarefree and B = F_q[X]/<X^n-1> is a
product of fields).  R_n := R[X]/<X^n-1>  ~=  M_m(B).

   sigma_s : entrywise Frobenius a -> a^(p^s)   (FIXES X)
   theta_s : sigma_s o transpose                (anti-automorphism)
   <x,y>_s := sum_i theta_s(x_i) y_i            (R-valued)
   Lambda  := trace on M_m(F_q)  ( = lambda o tr with lambda the coefficient of
              u^(t-1); for t = 1 that coefficient is the element itself)

What is checked, for every parameter set and every s:
  A. sigma_s is a ring automorphism of R; sigma_s is NONTRIVIAL; its order.
  B. theta_s is an anti-automorphism; theta_s^2 = sigma_{2s}; involution?
  C. Lambda is non-degenerate and ideal-catching (left and right).
  D. complete enumeration of the cyclic codes (right ideals of R_n), done
     twice: (i) Morita/CRT prediction, (ii) the lattice closure of all
     principal right ideals.  Both must agree.
  E. for EVERY cyclic code C:
       - C is a right R-submodule and T-invariant                     [sanity]
       - C^{perp_s} is a right R-submodule                            [Prop 5]
       - C^{perp_s} is T-invariant, i.e. the dual of a cyclic code is
         cyclic                                                       [Prop 8]
       - |C| |C^{perp_s}| = |R|^n                                     [Prop 6]
       - Hull_s(C) = C cap C^{perp_s} is a right R-submodule and
         T-invariant, hence cyclic                                    [Prop 9]
       - (C^{perp_s})^{perp_s} = sigma_{2s}(C)                        [Prop 7]
       - the PLAIN product dual sum_i x_i y_i is recorded too:
         is it a right module? a left module? does the size formula hold?
  F. summary table.

Every printed number is produced by the code in this file.  Nothing is
imported from a previous run.
"""
import sys
import time
import random
import itertools

from matrix_ring_lib import (FiniteField, rref, nullspace, row_space_basis,
                             in_span, intersect)

LINES = []


def say(s=""):
    print(s, flush=True)
    LINES.append(str(s))


# ---------------------------------------------------------------------------
# polynomials over F_q : coefficient lists, index = degree, trailing zeros
# stripped
# ---------------------------------------------------------------------------
def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(F, a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] = x
    for i, x in enumerate(b):
        out[i] = F.add[out[i]][x]
    return ptrim(out)


def pmul(F, a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] = F.add[out[i + j]][F.mul[x][y]]
    return ptrim(out)


def pdivmod(F, a, b):
    """b monic.  returns (q, r)"""
    a = list(a)
    db = len(b) - 1
    if db < 0:
        raise ValueError
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] = F.sub(a[i - db + j], F.mul[c][b[j]])
    return ptrim(q), ptrim(a[:db])


def pmod(F, a, b):
    return pdivmod(F, a, b)[1]


def monic_of_degree(F, d):
    for tail in itertools.product(range(F.q), repeat=d):
        yield list(tail) + [1]


def all_irreducibles(F, dmax):
    """all monic irreducible polynomials over F_q of degree <= dmax"""
    out = []
    for d in range(1, dmax + 1):
        for f in monic_of_degree(F, d):
            ok = True
            for g in out:
                if len(g) - 1 <= d // 2 and pmod(F, f, g) == []:
                    ok = False
                    break
            if ok:
                out.append(f)
    return out


def factor_poly(F, g):
    """factor monic g into monic irreducibles (with multiplicity)."""
    irred = all_irreducibles(F, len(g) - 1)
    cur = list(g)
    fac = []
    for f in irred:
        while len(cur) - 1 >= len(f) - 1 and cur != [] and cur != [1]:
            q, r = pdivmod(F, cur, f)
            if r == []:
                fac.append(f)
                cur = q
            else:
                break
    return fac, cur


# ---------------------------------------------------------------------------
# K = F_q[X]/<f>,  elements = tuples of length d = deg f
# ---------------------------------------------------------------------------
def kadd(F, a, b, d):
    return tuple(F.add[a[i]][b[i]] for i in range(d))


def kmul(F, f, a, b, d):
    r = pmod(F, pmul(F, list(a), list(b)), f)
    r = list(r) + [0] * (d - len(r))
    return tuple(r[:d])


def kscale(F, f, c, a, d):
    """c in K times a in K"""
    return kmul(F, f, c, a, d)


def subspaces_of_Km(F, K, d, m, f):
    """all K-subspaces of K^m, m = 2 assumed (enough for m = 2).
    Returns list of (label, list-of-K-basis-vectors).  Each basis vector is a
    tuple of m elements of K."""
    zero = tuple([tuple([0] * d)] * m)
    out = [(("0",), [])]
    one = tuple([1] + [0] * (d - 1))
    for a in K:
        out.append((("line", a), [(one, a)]))
    out.append((("line_inf",), [(tuple([0] * d), one)]))
    full = []
    for j in range(m):
        v = [tuple([0] * d)] * m
        v = list(v)
        v[j] = one
        full.append(tuple(v))
    out.append((("full",), full))
    return out


# ---------------------------------------------------------------------------
# reduction modulo a subspace (F_q-linear projection along V)
# ---------------------------------------------------------------------------
def reduce_vec(F, v, rbasis, piv):
    v = list(v)
    for row, c in zip(rbasis, piv):
        if v[c]:
            f = v[c]
            v = [F.sub(v[j], F.mul[f][row[j]]) for j in range(len(v))]
    return tuple(v)


# ---------------------------------------------------------------------------
# R = M_m(F_q) and R^n   (flat vectors of length N = n*m*m)
# index convention:  v[e*m*m + r*m + c]  = entry (r,c) of the matrix X_e
# ---------------------------------------------------------------------------
def mmul(F, A, B, m):
    out = [0] * (m * m)
    for r in range(m):
        for c in range(m):
            s = 0
            for k in range(m):
                s = F.add[s][F.mul[A[r * m + k]][B[k * m + c]]]
            out[r * m + c] = s
    return tuple(out)


def mtransp(A, m):
    return tuple(A[c * m + r] for r in range(m) for c in range(m))


def mtrace(F, A, m):
    s = 0
    for i in range(m):
        s = F.add[s][A[i * m + i]]
    return s


def rn_mul(F, x, y, m, n):
    """product in R[X]/<X^n-1>"""
    mm = m * m
    out = [0] * (n * mm)
    for e1 in range(n):
        X = x[e1 * mm:(e1 + 1) * mm]
        if not any(X):
            continue
        for e2 in range(n):
            Y = y[e2 * mm:(e2 + 1) * mm]
            if not any(Y):
                continue
            e = (e1 + e2) % n
            P = mmul(F, X, Y, m)
            for t in range(mm):
                out[e * mm + t] = F.add[out[e * mm + t]][P[t]]
    return tuple(out)


def rn_rmul(F, x, a, m, n):
    """x . a   (a in R, on the right)"""
    mm = m * m
    out = []
    for e in range(n):
        out.extend(mmul(F, x[e * mm:(e + 1) * mm], a, m))
    return tuple(out)


def rn_lmul(F, x, a, m, n):
    """a . x   (a in R, on the left)"""
    mm = m * m
    out = []
    for e in range(n):
        out.extend(mmul(F, a, x[e * mm:(e + 1) * mm], m))
    return tuple(out)


def rn_shift(x, m, n, k=1):
    mm = m * m
    out = [0] * (n * mm)
    for e in range(n):
        src = (e - k) % n
        out[e * mm:(e + 1) * mm] = x[src * mm:(src + 1) * mm]
    return tuple(out)


def rn_sigma(F, s, x):
    tab = F.frob[s % F.r]
    return tuple(tab[a] for a in x)


def rn_theta(F, s, x, m, n):
    mm = m * m
    out = []
    for e in range(n):
        Xe = x[e * mm:(e + 1) * mm]
        out.extend(rn_sigma(F, s, mtransp(Xe, m)))
    return tuple(out)


def pair_theta(F, s, x, y, m, n):
    """sum_e theta_s(x_e) y_e   (element of R, i.e. tuple of m^2 entries)"""
    mm = m * m
    tx = rn_theta(F, s, x, m, n)
    acc = [0] * mm
    for e in range(n):
        X = tx[e * mm:(e + 1) * mm]
        Y = y[e * mm:(e + 1) * mm]
        P = mmul(F, X, Y, m)
        for t in range(mm):
            acc[t] = F.add[acc[t]][P[t]]
    return tuple(acc)


def pair_plain(F, x, y, m, n):
    mm = m * m
    acc = [0] * mm
    for e in range(n):
        X = x[e * mm:(e + 1) * mm]
        Y = y[e * mm:(e + 1) * mm]
        P = mmul(F, X, Y, m)
        for t in range(mm):
            acc[t] = F.add[acc[t]][P[t]]
    return tuple(acc)


def unit_vec(N, j):
    v = [0] * N
    v[j] = 1
    return tuple(v)


def pair_rows(F, pair, x, m, n, s):
    """the (m^2 x N) matrix of the F_q-linear map  y -> pair(x,y)."""
    N = n * m * m
    mm = m * m
    rows = [[0] * N for _ in range(mm)]
    for j in range(N):
        img = pair(F, s, x, unit_vec(N, j), m, n) if pair is pair_theta \
            else pair(F, x, unit_vec(N, j), m, n)
        for k in range(mm):
            rows[k][j] = img[k]
    return [tuple(r) for r in rows]


def dual_of(F, basis, m, n, s, pair):
    N = n * m * m
    rows = []
    for x in basis:
        rows.extend(pair_rows(F, pair, x, m, n, s))
    ns = nullspace(F, rows, N)
    return span_of(F, ns, N)          # reduced -> canonical for comparisons


def span_of(F, vecs, N):
    if not vecs:
        return []
    return row_space_basis(F, vecs, N)


def subspace_key(basis):
    return tuple(sorted(basis))


# ---------------------------------------------------------------------------
# ENUMERATION OF THE CYCLIC CODES  (right ideals of R_n)
# method M1 (Morita/CRT):  right ideals of M_m(B)  <->  B-submodules of B^m
#                          (columns);  B = prod_i K_i  =>  tuples (V_i)
# method M2 (closure)   :  lattice generated by all principal right ideals
# ---------------------------------------------------------------------------
def enumerate_ideals_morita(F, m, n, verbose=True, limit=1200, seed=13572468):
    """returns (list_of_bases, info)  -- bases are F_q-bases of R^n.
    If the lattice is larger than `limit` ideals a RANDOM SAMPLE of `limit`
    ideals is returned and info['sampled'] is True (the total number of
    right ideals is still computed and reported)."""
    mm = m * m
    N = n * mm
    g = [F.neg(1)] + [0] * (n - 1) + [1]          # X^n - 1
    fac, rem = factor_poly(F, g)
    prod = [1]
    for f in fac:
        prod = pmul(F, prod, f)
    if prod != g:
        raise RuntimeError("factorisation failed: %r" % (rem,))
    if len(set(map(tuple, fac))) != len(fac):
        raise RuntimeError("X^n-1 is not squarefree -- Morita method skipped")
    comps = []
    for f in fac:
        d = len(f) - 1
        K = [tuple(([0] * d))]
        # enumerate the elements of K = F_q[X]/<f> as tuples
        elems = [tuple(c) for c in itertools.product(range(F.q), repeat=d)]
        comps.append({"f": f, "d": d, "K": elems})
        # sanity: it is a field  (every nonzero element invertible)
        if d > 1:
            for a in elems[1:]:
                inv = None
                for b in elems:
                    if kmul(F, f, a, b, d) == tuple([1] + [0] * (d - 1)):
                        inv = b
                        break
                if inv is None:
                    raise RuntimeError("component is not a field !")
    if verbose:
        say("    X^%d - 1 = %s  (fields of sizes %s)" %
            (n, " * ".join("deg%d" % (len(c['f']) - 1) for c in comps),
             ",".join(str(F.q ** (len(c['f']) - 1)) for c in comps)))
    # all tuples of subspaces
    choices = [subspaces_of_Km(F, c["K"], c["d"], m, c["f"]) for c in comps]
    total = 1
    for ch in choices:
        total *= len(ch)
    if verbose:
        say("    #B-submodules of B^%d = %d  (= #right ideals of R_n)"
            % (m, total))
    if total > limit:
        rnd = random.Random(seed)
        combos = [tuple(rnd.choice(ch) for ch in choices)
                  for _ in range(limit)]
        sampled = True
    else:
        combos = list(itertools.product(*choices))
        sampled = False
    ideals = []
    for combo in combos:
        # W = { w in B^m : red_i(w) in V_i for all i }
        rows = []
        for ci, (c, (lab, Vbasis)) in enumerate(zip(comps, combo)):
            d = c["d"]
            f = c["f"]
            # F_q-basis of V_i inside F_q^{m*d}:  { X^k . v }  (K = F_q[X]/<f>)
            xk = list(pmod(F, [0, 1], f)) + [0] * d
            xk = tuple(xk[:d])
            fqbasis = []
            for v in Vbasis:
                cur = list(v)
                for k in range(d):
                    cur2 = []
                    for comp in cur:
                        cur2.extend(comp)
                    fqbasis.append(tuple(cur2))
                    cur = [kmul(F, f, comp, xk, d) for comp in cur]
            rb, piv = rref(F, fqbasis, m * d) if fqbasis else ([], [])
            # images of the standard basis of F_q^{m n}
            cols = []
            for j in range(m):
                for e in range(n):
                    img = [0] * (m * d)
                    poly = [0] * (e + 1)
                    poly[e] = 1
                    r = pmod(F, poly, f)
                    for k in range(d):
                        img[j * d + k] = r[k] if k < len(r) else 0
                    cols.append(reduce_vec(F, tuple(img), rb, piv) if rb
                                else tuple(img))
            # transpose: rows of the composite map
            for k in range(m * d):
                rows.append(tuple(cols[j][k] for j in range(m * n)))
        W = nullspace(F, rows, m * n)
        # I_W = { M in M_m(B) : every column of M lies in W }
        basis = []
        for w in W:                       # w : m blocks of n coefficients
            for c0 in range(m):
                v = [0] * N
                for j in range(m):
                    for e in range(n):
                        v[e * mm + j * m + c0] = w[j * n + e]
                basis.append(tuple(v))
        ideals.append(span_of(F, basis, N))
    return ideals, {"total": total, "sampled": sampled, "comps": comps}


def enumerate_ideals_closure(F, m, n):
    """lattice closure of all principal right ideals (exhaustive but slow:
    |R|^n must be enumerable)."""
    mm = m * m
    N = n * mm
    Nall = (F.q ** mm) ** n
    if Nall > 20000:
        return None, "ambient too large (%d)" % Nall
    # all elements of R^n
    elems = []
    for digits in itertools.product(range(F.q), repeat=N):
        elems.append(tuple(digits))
    # operators: shift, right multiplication by matrix units
    units = []
    for rc in range(mm):
        a = [0] * mm
        a[rc] = 1
        units.append(tuple(a))
    ops = []

    def op_shift(v):
        return rn_shift(v, m, n)

    ops.append(op_shift)
    for a in units:
        ops.append((lambda a: (lambda v: rn_rmul(F, v, a, m, n)))(a))
    seen = {subspace_key([]): []}      # the zero code
    for v in elems:
        if not any(v):
            continue
        gens = [v]
        cur = span_of(F, gens, N)
        changed = True
        while changed:
            changed = False
            new = list(cur)
            for w in cur:
                for op in ops:
                    z = op(w)
                    if any(z):
                        new.append(z)
            nv = span_of(F, new, N)
            if len(nv) != len(cur):
                cur = nv
                changed = True
        seen[subspace_key(cur)] = cur
    ideals = list(seen.values())
    # close under sums
    changed = True
    while changed:
        changed = False
        cur = list(ideals)
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                s = span_of(F, list(cur[i]) + list(cur[j]), N)
                k = subspace_key(s)
                if k not in seen:
                    seen[k] = s
                    ideals.append(s)
                    changed = True
    return ideals, "ok"


# ---------------------------------------------------------------------------
# one parameter set
# ---------------------------------------------------------------------------
def run_case(p, r, m, n, slist, sample_cap=400, seed=987654321):
    q = p ** r
    F = FiniteField(p, r)
    mm = m * m
    N = n * mm
    say("")
    say("=" * 78)
    say("PARAMETER SET   p=%d r=%d q=%d  m=%d  t=1  n=%d   (N = dim_Fq R^n = %d)"
        % (p, r, q, m, n, N))
    say("=" * 78)
    t0 = time.time()
    rnd = random.Random(seed)

    def rnd_mat():
        return tuple(rnd.randrange(F.q) for _ in range(mm))

    def rnd_vec():
        return tuple(rnd.randrange(F.q) for _ in range(N))

    # ---------------- A. sigma_s ------------------------------------------
    say("-- A. sigma_s (entrywise Frobenius, u-trivial since t = 1) --")
    for s in slist:
        ok_add = ok_mul = True
        for _ in range(300):
            X, Y = rnd_mat(), rnd_mat()
            sx, sy = rn_sigma(F, s, X), rn_sigma(F, s, Y)
            if rn_sigma(F, s, tuple(F.add[X[i]][Y[i]] for i in range(mm))) != \
               tuple(F.add[sx[i]][sy[i]] for i in range(mm)):
                ok_add = False
            if rn_sigma(F, s, mmul(F, X, Y, m)) != mmul(F, sx, sy, m):
                ok_mul = False
        # nontriviality: exhibit an element that moves
        wit = None
        for a in range(F.q):
            X = tuple([a] + [0] * (mm - 1))
            if rn_sigma(F, s, X) != X:
                wit = (a, F.frob[s % F.r][a])
                break
        # order
        o = 1
        X = rnd_mat()
        cur = rn_sigma(F, s, X)
        while cur != X and o < 100:
            cur = rn_sigma(F, s, cur)
            o += 1
        # nontrivial = some element of F_q actually moves (witness-based;
        # at q=p with s=0 no element moves, so this is False)
        nontrivial = (wit is not None)
        say("   s=%d : additive=%s multiplicative=%s ; nontrivial=%s "
            "(witness a=%s -> a^(p^s)=%s) ; order(sigma_s)=%d  [r/gcd(r,s)=%d]"
            % (s, ok_add, ok_mul, nontrivial, wit[0] if wit else None,
               wit[1] if wit else None, o, r // _gcd(r, s % r)))

    # ---------------- B. theta_s ------------------------------------------
    say("-- B. theta_s = sigma_s o transpose --")
    for s in slist:
        ok_anti = ok_add = True
        for _ in range(300):
            X, Y = rnd_mat(), rnd_mat()
            if rn_theta(F, s, mmul(F, X, Y, m), m, 1) != \
               mmul(F, rn_theta(F, s, Y, m, 1), rn_theta(F, s, X, m, 1), m):
                ok_anti = False
            if rn_theta(F, s, tuple(F.add[X[i]][Y[i]] for i in range(mm)), m, 1) \
               != tuple(F.add[rn_theta(F, s, X, m, 1)[i]][rn_theta(F, s, Y, m, 1)[i]]
                        for i in range(mm)):
                ok_add = False
        # theta_s^2 = sigma_{2s}
        ok_sq = True
        for _ in range(200):
            X = rnd_mat()
            lhs = rn_theta(F, s, rn_theta(F, s, X, m, 1), m, 1)
            rhs = rn_sigma(F, 2 * s, X)
            if lhs != rhs:
                ok_sq = False
        involution = ((2 * s) % r == 0)
        say("   s=%d : additive=%s  anti-multiplicative=%s ; "
            "theta_s^2 = sigma_{2s} : %s ; theta_s INVOLUTION? %s "
            "(2s mod r = %d)" % (s, ok_add, ok_anti, ok_sq, involution,
                                 (2 * s) % r))

    # ---------------- C. Lambda -------------------------------------------
    say("-- C. Lambda = trace (t = 1) --")
    # Gram matrix of (X,Y) -> tr(XY) on M_m(F_q)
    basis = [unit_vec(mm, i) for i in range(mm)]
    G = []
    for A in basis:
        row = []
        for B in basis:
            row.append(mtrace(F, mmul(F, A, B, m), m))
        G.append(tuple(row))
    rk, _ = rref(F, G, mm)
    say("   Gram matrix of (X,Y) -> Lambda(XY) on M_%d(F_%d): rank = %d / %d"
        % (m, q, len(rk), mm))
    # ideal catching: for every nonzero X there is Y with Lambda(XY) != 0
    # (constructive: Y = E_{j0 i0} for a nonzero entry (i0,j0) of X)
    ok_catch = True
    for _ in range(200):
        X = rnd_mat()
        if not any(X):
            continue
        i0 = next(i for i in range(mm) if X[i])
        # X_{i0 j0} != 0 with i0 = row* m + col  ->  Y = E_{j0, row}
        row, col = divmod(i0, m)
        Y = [0] * mm
        Y[col * m + row] = 1
        Y = tuple(Y)
        if mtrace(F, mmul(F, X, Y, m), m) == 0:
            ok_catch = False
    say("   right-ideal-catching (trace(X.E_{j0,i0}) = X_{i0,j0} != 0): %s"
        % ok_catch)

    # ---------------- D. enumeration ---------------------------------------
    say("-- D. enumeration of the cyclic codes (right ideals of R_n) --")
    ideals, info = enumerate_ideals_morita(F, m, n)
    say("   Morita/CRT enumeration : %d right ideals (%d tested)"
        % (info["total"], len(ideals)))
    sizes = {}
    for b in ideals:
        sizes[len(b)] = sizes.get(len(b), 0) + 1
    say("   F_q-dimension distribution (dim : #codes): %s"
        % sorted(sizes.items()))
    sampled = info["sampled"]
    if sampled:
        say("   !! the lattice has %d right ideals > %d: a RANDOM SAMPLE of %d "
            "is tested (NOT exhaustive)" % (info["total"], sample_cap,
                                            len(ideals)))
    closure_note = None
    if (F.q ** mm) ** n <= 20000 and not sampled:
        id2, msg = enumerate_ideals_closure(F, m, n)
        if id2 is not None:
            k1 = set(subspace_key(b) for b in ideals)
            k2 = set(subspace_key(b) for b in id2)
            say("   independent lattice-closure enumeration : %d right ideals"
                % len(id2))
            say("   the two lists agree: %s" % (k1 == k2))
            closure_note = (len(id2), k1 == k2)
        else:
            say("   lattice closure skipped: %s" % msg)
    else:
        say("   lattice closure skipped (ambient %d > 20000)"
            % ((F.q ** mm) ** n))

    # ---------------- E. per-code checks ------------------------------------
    say("-- E. per-code checks (every code, every s) --")
    matrix_units = []
    for rc in range(mm):
        a = [0] * mm
        a[rc] = 1
        matrix_units.append(tuple(a))
    for s in slist:
        cnt = dict(codes=0, right=0, cyc=0, dualright=0, dualcyc=0, size=0,
                   hullright=0, hullcyc=0, dd=0, dd_eq=0, plain_right=0,
                   plain_left=0, plain_size=0)
        witness = None
        hull_dims = {}
        plain_dims = {}
        fails = []
        for idx, C in enumerate(ideals):
            cnt["codes"] += 1
            Nc = len(C)
            rb, piv = rref(F, C, N)

            def member(v):
                return in_span(F, rb, piv, v, N)
            # C is a right module + T-invariant
            if all(member(rn_rmul(F, x, a, m, n)) for x in C for a in matrix_units):
                cnt["right"] += 1
            if all(member(rn_shift(x, m, n)) for x in C):
                cnt["cyc"] += 1
            # theta-dual
            D = dual_of(F, C, m, n, s, pair_theta)
            rbd, pivd = rref(F, D, N) if D else ([], [])

            def member_d(v):
                if not rbd:
                    return not any(v)
                return in_span(F, rbd, pivd, v, N)
            if all(member_d(rn_rmul(F, y, a, m, n)) for y in D for a in matrix_units):
                cnt["dualright"] += 1
            if all(member_d(rn_shift(y, m, n)) for y in D):
                cnt["dualcyc"] += 1
            if len(C) + len(D) == N:
                cnt["size"] += 1
            else:
                fails.append(("size", idx, len(C), len(D)))
            # hull
            H = intersect(F, C, D, N) if (C and D) else []
            rbh, pivh = rref(F, H, N) if H else ([], [])

            def member_h(v):
                if not rbh:
                    return not any(v)
                return in_span(F, rbh, pivh, v, N)
            okhr = all(member_h(rn_rmul(F, z, a, m, n))
                       for z in H for a in matrix_units)
            okhc = all(member_h(rn_shift(z, m, n)) for z in H)
            cnt["hullright"] += 1 if okhr else 0
            cnt["hullcyc"] += 1 if okhc else 0
            hull_dims[len(H)] = hull_dims.get(len(H), 0) + 1
            # double dual  = sigma_{2s}(C) ?
            DD = dual_of(F, D, m, n, s, pair_theta) if D else list(
                unit_vec(N, j) for j in range(N))
            Cshift = span_of(F, [rn_sigma(F, 2 * s, x) for x in C], N)
            if subspace_key(DD) == subspace_key(Cshift):
                cnt["dd"] += 1
            else:
                fails.append(("doubledual", idx, len(DD), len(Cshift)))
            if subspace_key(DD) == subspace_key(span_of(F, C, N)):
                cnt["dd_eq"] += 1
            elif witness is None:
                witness = (idx, C, DD)
            # plain product dual
            P = dual_of(F, C, m, n, s, pair_plain)
            rbp, pivp = rref(F, P, N) if P else ([], [])

            def member_p(v):
                if not rbp:
                    return not any(v)
                return in_span(F, rbp, pivp, v, N)
            okpr = all(member_p(rn_rmul(F, y, a, m, n)) for y in P
                       for a in matrix_units)
            okpl = all(member_p(rn_lmul(F, y, a, m, n)) for y in P
                       for a in matrix_units)
            cnt["plain_right"] += 1 if okpr else 0
            cnt["plain_left"] += 1 if okpl else 0
            if len(C) + len(P) == N:
                cnt["plain_size"] += 1
            plain_dims[len(P)] = plain_dims.get(len(P), 0) + 1
        say("   s=%d : %d codes tested%s" % (s, cnt["codes"],
                                             " (SAMPLE)" if sampled else ""))
        say("      C right R-submodule .................. %d/%d"
            % (cnt["right"], cnt["codes"]))
        say("      C cyclic (T-invariant) ............... %d/%d"
            % (cnt["cyc"], cnt["codes"]))
        say("      C^{perp_s} right R-submodule ......... %d/%d"
            % (cnt["dualright"], cnt["codes"]))
        say("      C^{perp_s} cyclic .................... %d/%d"
            % (cnt["dualcyc"], cnt["codes"]))
        say("      |C|.|C^{perp_s}| = |R|^n ............. %d/%d"
            % (cnt["size"], cnt["codes"]))
        say("      Hull_s(C) right R-submodule .......... %d/%d"
            % (cnt["hullright"], cnt["codes"]))
        say("      Hull_s(C) cyclic ..................... %d/%d"
            % (cnt["hullcyc"], cnt["codes"]))
        say("      (C^{perp_s})^{perp_s} = sigma_{2s}(C)  %d/%d"
            % (cnt["dd"], cnt["codes"]))
        say("      (C^{perp_s})^{perp_s} = C  (reflexivity) %d/%d"
            % (cnt["dd_eq"], cnt["codes"]))
        if witness is not None:
            say("      witness for non-reflexivity: code #%d" % witness[0])
            say("         C               = %s" % (list(witness[1]),))
            say("         (C^{perp})^{perp} = %s" % (list(witness[2]),))
        say("      PLAIN dual: right module %d/%d ; left module %d/%d ; "
            "size formula %d/%d"
            % (cnt["plain_right"], cnt["codes"], cnt["plain_left"],
               cnt["codes"], cnt["plain_size"], cnt["codes"]))
        say("      hull F_q-dimension distribution: %s"
            % sorted(hull_dims.items()))
        say("      plain-dual F_q-dimension distribution: %s"
            % sorted(plain_dims.items()))
        if fails:
            say("      FAILURES: %s" % fails[:6])
        else:
            say("      no failure")
    say("   [elapsed %.1f s]" % (time.time() - t0))
    return {"q": q, "m": m, "n": n, "nideals": len(ideals), "sampled": sampled,
            "closure": closure_note}


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ---------------------------------------------------------------------------
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"
    say("NONTRIVIAL GALOIS EXPERIMENTS  --  Phase 0 revised, Task 1")
    say("run: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    say("python: %s" % sys.version.split()[0])
    say("")
    summary = []
    cases = []
    if mode == "quick":
        cases = [(2, 2, 2, 3, [1]), (3, 2, 2, 2, [1])]
    else:
        cases = [
            (2, 2, 2, 3, [1]),      # q = 4
            (2, 3, 2, 3, [1, 2]),   # q = 8
            (3, 2, 2, 2, [1]),      # q = 9, n = 2
            (3, 2, 2, 4, [1]),      # q = 9, n = 4  (sampled if too many)
        ]
    for (p, r, m, n, slist) in cases:
        summary.append(run_case(p, r, m, n, slist))
    say("")
    say("#" * 78)
    say("# VALIDATION OF THE ENUMERATION MACHINERY.")
    say("# r = 1 (q = 2): sigma_s IS THE IDENTITY HERE, so these two cases are")
    say("# NOT Galois evidence.  They are run only because the ambient set is")
    say("# small enough for a SECOND, INDEPENDENT enumeration (exhaustive")
    say("# lattice closure of all principal right ideals) to be affordable.")
    say("#" * 78)
    summary.append(run_case(2, 1, 2, 1, [0]))
    summary.append(run_case(2, 1, 2, 3, [0]))
    say("")
    say("=" * 78)
    say("SUMMARY")
    say("=" * 78)
    say("%-6s %-4s %-4s %-10s %-12s %s" %
        ("q", "m", "n", "#codes", "exhaustive", "independent closure check"))
    for row in summary:
        cc = row["closure"]
        say("%-6d %-4d %-4d %-10d %-12s %s" %
            (row["q"], row["m"], row["n"], row["nideals"],
             "no (sample)" if row["sampled"] else "yes",
             ("%d ideals, agree=%s" % cc) if cc else "not run"))
    with open("galois_experiments_log.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    say("")
    say("log written to galois_experiments_log.txt")


if __name__ == "__main__":
    main()
