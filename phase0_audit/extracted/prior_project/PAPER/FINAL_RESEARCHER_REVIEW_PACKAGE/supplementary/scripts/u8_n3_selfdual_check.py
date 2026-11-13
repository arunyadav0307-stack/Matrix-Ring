"""
U8 PROBE.  Cyclic codes of length n = 3 over A = M_2(F_2).

TWO competing conventions for "a cyclic A-code of length n":

  (I)  RIGHT-IDEAL convention.  R_n = A[X]/(X^n-1); a cyclic code is a RIGHT
       ideal of R_n.  This is the convention stated in Alahmadi-Sboui-Sole-
       Yemen (2013), Sec. 2 ("the ring whose RIGHT SIDED IDEALS represent
       cyclic codes of length n"), and it is the convention used throughout
       Phase 0.
       Number at n = 3:  35.
       Structural check (CRT + Morita):  X^3 - 1 = X^3 + 1 = (X+1)(X^2+X+1)
       over F_2 (squarefree), so  R_3 = M_2(F_2) x M_2(F_4)  and
           #right ideals = #right ideals of M_2(F_2)  x  #right ideals of
                           M_2(F_4)                     =  5 x 7 = 35,
       with F_2-dimensions 2*v_1 + 4*v_2, v_1 in {0,1,2} (multiplicities
       1,3,1), v_2 in {0,1,2} (multiplicities 1,5,1).  The predicted
       dimension distribution is therefore
           dim  0  2  4  6   8  10  12
           #     1  3  6 15   6   3   1
       and the script checks that the enumeration reproduces it.

  (II) QUATERNARY convention.  Cyclic A-codes of length n are in bijection
       with cyclic codes of length n over F_4 (embedded in A as
       F_4 = <I, omega>), "quaternary codes of length n with respective
       generator polynomials" (Alahmadi et al.).  Number at n = 3:
       8 = 2^3 = # monic divisors of X^3 - 1 over F_4, since
       X^3 - 1 = (X+1)(X+omega)(X+omega^2) over F_4.
       The corresponding right ideals of R_3 are generated (as right ideals)
       by the image of the generator under phi : F_4 -> A.

For BOTH families the script computes exhaustively, for the two natural
non-degenerate F_2-bilinear forms on A^n

    beta_1(x,y) = sum_j tr(x_j y_j)       (the s = 0 Galois form; at q = 2
                                           sigma_0 = id, so this IS the
                                           Galois form of Phase 0)
    beta_2(x,y) = sum_j tr(x_j^T y_j)     (Euclidean / Frobenius form; this
                                           is the form called "Euclidean"
                                           in Alahmadi et al., Lemma 4)

  * |C| * |C^perp| = |A|^n = 2^12                       (both forms)
  * the hull  Hull(C) = C n C^perp  and its dimension
  * the number of self-orthogonal codes (C <= C^perp)
  * the number of self-dual codes (C = C^perp)
  * an explicit list of the self-orthogonal / self-dual codes.

Dimension bookkeeping for family (II): a quaternary cyclic code with
generator of degree d has |C| = |A|^(n-d) = 16^(n-d), i.e. F_2-dimension
4(n-d); at n = 3 this is 12, 8, 4, 0 for d = 0, 1, 2, 3 -- never 6
(= half of 4n = 12).  Hence family (II) contains NO self-dual code at
n = 3, and every self-orthogonal code in it has d >= 2.

Run:  python3 -u u8_n3_selfdual_check.py
"""

import importlib.util
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "alahmadi_reconciliation", os.path.join(HERE, "alahmadi_reconciliation.py"))
ar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ar)


# ---------------------------------------------------------------------------
# linear algebra over F_2; vectors are tuples of 0/1 of length N (the
# representation used by alahmadi_reconciliation: to_flat / from_flat)
# ---------------------------------------------------------------------------
def nullspace2(rows, N):
    """basis of {y : rows . y = 0} (rows: lists of 0/1 of length N)"""
    M = [list(r) for r in rows]
    piv_of_col = {}
    r = 0
    for c in range(N):
        pr = next((i for i in range(r, len(M)) if M[i][c]), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                M[i] = [a ^ b for a, b in zip(M[i], M[r])]
        piv_of_col[c] = r
        r += 1
    free = [c for c in range(N) if c not in piv_of_col]
    out = []
    for f in free:
        y = [0] * N
        y[f] = 1
        for c, ri in piv_of_col.items():
            y[c] = sum(M[ri][j] * y[j] for j in range(N)) & 1
        out.append(tuple(y))
    return out


def in_span2(basis, v):
    w = list(v)
    for b in basis:
        p = next((i for i in range(len(w)) if b[i]), None)
        if p is not None and w[p]:
            w = [x ^ y for x, y in zip(w, b)]
    return not any(w)


# ---------------------------------------------------------------------------
# the two forms.  Within a 4-bit block the bits are (a,b,c,d) for
# M = [[a,b],[c,d]]  (convention: M -> a*8+b*4+c*2+d, bits() MSB first).
#   tr(XY)    = a e + b g + c f + d h   -> offsets (0,0) (1,2) (2,1) (3,3)
#   tr(X^T Y) = a e + b f + c g + d h   -> offsets (0,0) (1,1) (2,2) (3,3)
# ---------------------------------------------------------------------------
FORM_PAIRS = {"tr(xy) (Galois, s=0)": [(0, 0), (1, 2), (2, 1), (3, 3)],
              "tr(x^T y) (Euclidean)": [(0, 0), (1, 1), (2, 2), (3, 3)]}


def form_matrix(form, n):
    """row i represents the functional y -> beta(e_i, y)."""
    N = 4 * n
    rows = []
    for i in range(N):
        j, o = divmod(i, 4)
        row = [0] * N
        for (p, q) in FORM_PAIRS[form]:
            if o == p:
                row[4 * j + q] ^= 1
        rows.append(row)
    return rows


_FORM_CACHE = {}


def form_matrix_c(form, n):
    if (form, n) not in _FORM_CACHE:
        _FORM_CACHE[(form, n)] = form_matrix(form, n)
    return _FORM_CACHE[(form, n)]


def beta_row(x, form, n):
    """the functional y -> beta(x, y), as a 0/1 row of length N."""
    N = 4 * n
    F = form_matrix_c(form, n)
    r = [0] * N
    for i in range(N):
        if x[i]:
            r = [a ^ b for a, b in zip(r, F[i])]
    return r


def dual_of(basis, form, n):
    """C^perp = {y : beta(x, y) = 0 for all x in C}"""
    N = 4 * n
    rows = [beta_row(x, form, n) for x in basis]
    if not rows:
        rows = [[0] * N]
    return nullspace2(rows, N)


def hull_of(basis, form, n):
    """Hull(C) = C n C^perp = {x in C : beta(c,x) = 0 for all c in C}.

    Writing x = sum_i a_i c_i, the condition is sum_i a_i beta(c_j, c_i) = 0
    for all j, i.e. a lies in the nullspace of the Gram matrix
    G[j][i] = beta(c_j, c_i).  (Taking the span of those basis vectors of C
    that happen to lie in C^perp is NOT the same thing.)"""
    N = 4 * n
    if not basis:
        return []
    rows = [beta_row(x, form, n) for x in basis]
    G = [[sum(r[i] * c[i] for i in range(N)) & 1 for c in basis] for r in rows]
    sols = nullspace2(G, len(basis))
    out = []
    for a in sols:
        v = [0] * N
        for coeff, c in zip(a, basis):
            if coeff:
                v = [x ^ y for x, y in zip(v, c)]
        if any(v):
            out.append(tuple(v))
    return out


def key(basis):
    return tuple(sorted(basis))


# ---------------------------------------------------------------------------
def show_word(v, n):
    """flat 0/1 vector of length 4n -> readable word of length n over A"""
    out = []
    for j in range(n):
        blk = v[4 * j] * 8 + v[4 * j + 1] * 4 + v[4 * j + 2] * 2 + v[4 * j + 3]
        # blk = a*8+b*4+c*2+d  ->  [[a,b],[c,d]]
        a, b, c, d = (blk >> 3) & 1, (blk >> 2) & 1, (blk >> 1) & 1, blk & 1
        out.append("[[%d,%d],[%d,%d]]" % (a, b, c, d))
    return "(" + " ".join(out) + ")"


def analyse(codes, n, label, names=None):
    N = 4 * n
    print()
    print("=" * 78)
    print("%s   --   %d codes" % (label, len(codes)))
    print("=" * 78)
    dims = {}
    for C in codes:
        dims[len(C)] = dims.get(len(C), 0) + 1
    print("F_2-dimension distribution : %s" % sorted(dims.items()))
    print("   (|C| * |C^perp| = |A|^n = 2^%d holds for both forms: "
          "verified per code below)" % N)
    ok_size = 0
    for form in FORM_PAIRS:
        hulld = {}
        nsd = 0
        nso = 0
        sd_codes = []
        so_codes = []
        for C in codes:
            D = dual_of(C, form, n)
            if len(C) + len(D) == N:
                ok_size += 1
            H = hull_of(C, form, n)
            hulld[len(H)] = hulld.get(len(H), 0) + 1
            if key(C) == key(D):
                nsd += 1
                sd_codes.append(C)
            if all(in_span2(D, x) for x in C):
                nso += 1
                so_codes.append(C)
        print()
        print("form beta = %s" % form)
        print("   |C| + |C^perp| = 4n  for  %d / %d codes" % (ok_size, len(codes)))
        print("   hull dim distribution : %s" % sorted(hulld.items()))
        print("   #self-orthogonal      : %d" % nso)
        print("   #SELF-DUAL            : %d" % nsd)
        for C in sd_codes:
            print("   SELF-DUAL code, dim %d:" % len(C))
            for w in C:
                print("        %s" % show_word(w, n))
        print("   self-orthogonal codes by dimension:")
        for C in sorted(so_codes, key=len):
            print("      dim %2d : %s" % (len(C), "  ".join(show_word(w, n)
                                                            for w in C)))
    if names:
        print()
        print("   generator polynomials (family II correspondence):")
        for nm, C in names:
            print("      %-22s dim %2d" % (nm, len(C)))


def main():
    n = 3
    N = 4 * n
    print("U8 PROBE: cyclic codes of length n = %d over A = M_2(F_2)" % n)
    print("run: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))

    # ---------------- family (I): right ideals of R_3 ----------------------
    ideals, nvecs = ar.enumerate_right_ideals(n)
    print()
    print("family (I)  RIGHT IDEALS of R_%d = A[X]/(X^%d - 1):" % (n, n))
    print("   ambient vectors scanned  : %d" % nvecs)
    print("   distinct right ideals    : %d" % len(ideals))
    predict = {0: 1, 2: 3, 4: 6, 6: 15, 8: 6, 10: 3, 12: 1}
    got = {}
    for C in ideals:
        got[len(C)] = got.get(len(C), 0) + 1
    print("   CRT/Morita prediction    : %s" % sorted(predict.items()))
    print("   enumeration              : %s" % sorted(got.items()))
    print("   MATCH                    : %s" % (got == predict))
    analyse(ideals, n, "FAMILY (I): RIGHT IDEALS (count %d)" % len(ideals))

    # ---------------- family (II): quaternary codes ------------------------
    F4, phi, gen = ar.build_phi()
    X3p1 = [1, 0, 0, 1]                    # X^3 - 1 = X^3 + 1 over F_2 c F_4
    divisors = set()
    for d in range(0, n + 1):              # monic, degree exactly d
        for coeffs in __import__("itertools").product(range(F4.q), repeat=d):
            g = list(coeffs) + [1]
            q, r = ar.pdivmod(F4, X3p1, g)
            if not any(r):
                divisors.add(tuple(ar.ptrim(g)))
    divisors = sorted(divisors, key=lambda g: (len(g), g))
    print()
    print("family (II) QUATERNARY: monic divisors of X^%d - 1 over F_4 : %d"
          % (n, len(divisors)))
    for g in divisors:
        print("      %s" % str(list(g)))

    qcodes = []
    names = []
    for g in divisors:
        word = tuple([phi[c] for c in g] + [ar.ZERO] * (n - len(g)))
        ops = [lambda v: ar.rn_shift(v, n)]
        for a in range(16):
            ops.append((lambda a: (lambda v: ar.rn_rmul(v, a, n)))(a))
        cur = ar.span2([ar.to_flat(word)], N)
        changed = True
        while changed:
            changed = False
            new = list(cur)
            for w in cur:
                for op in ops:
                    new.append(op(w))
            nv = ar.span2(new, N)
            if len(nv) != len(cur):
                cur = nv
                changed = True
        qcodes.append(cur)
        names.append((str(list(g)), cur))
    seen = {}
    for nm, C in zip([str(list(g)) for g in divisors], qcodes):
        seen[ar.key(C)] = (nm, C)
    print("   distinct right ideals of A^%d obtained : %d" % (n, len(seen)))
    analyse([C for (nm, C) in seen.values()], n,
            "FAMILY (II): QUATERNARY CODES (count %d)" % len(seen),
            names=[(nm, C) for (nm, C) in seen.values()])


if __name__ == "__main__":
    main()
