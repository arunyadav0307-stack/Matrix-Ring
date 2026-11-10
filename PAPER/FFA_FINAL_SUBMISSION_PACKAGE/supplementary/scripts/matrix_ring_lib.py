"""
matrix_ring_lib.py
==================
Exact (no floating point) arithmetic for the rings appearing in the project
"Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings".

Structures implemented
----------------------
  F_q      : finite field of order q = p^r (elements = ints in [0,q): the
             base-p digits of the integer are the coefficients of the element
             written in the polynomial basis 1, x, x^2, ... of F_p[x]/(f),
             f a primitive polynomial found by exhaustive search).
  A_t      : F_q[u]/<u^t>       (commutative local Frobenius ring)
  M_m(A_t) : m x m matrices over A_t  (the noncommutative candidate alphabet)
  R^n      : ambient space of length-n codes over R = M_m(A_t), viewed as an
             F_q-vector space of dimension n * m^2 * t.

The library also provides:
  * entrywise field-Frobenius map sigma_s : a -> a^(p^s) on A_t and its
    entrywise extension to M_m(A_t) (to be *tested*, not assumed, for the
    automorphism property),
  * the u-scaling automorphism mu_c : u -> c u,
  * the transposition anti-automorphism and the composite theta = sigma o T,
  * the Frobenius functional Lambda = lambda o tr  (lambda = coefficient of
    u^(t-1)), which produces the F_q-valued *trace pairing*
        (X, Y) |-> Lambda(X Y),
  * several candidate pairings on R^n and F_q-linear algebra (span, rref,
    nullspace, intersection) used to compute dual codes and hulls exactly.

Everything is brute-force checkable on small parameters; nothing is assumed
without a test.  Written for the Phase-0 feasibility study.
"""

from itertools import product

# --------------------------------------------------------------------------
# Finite field F_q, q = p^r
# --------------------------------------------------------------------------


def _digits(a, p, length):
    d = []
    for _ in range(length):
        d.append(a % p)
        a //= p
    return d


def _from_digits(d, p):
    v = 0
    place = 1
    for c in d:
        v += c * place
        place *= p
    return v


def _poly_add(p, r, a, b):
    da = _digits(a, p, r)
    db = _digits(b, p, r)
    return _from_digits([(x + y) % p for x, y in zip(da, db)], p)


def _poly_mul(p, r, poly, a, b):
    """multiply in F_p[x]/(x^r - sum poly[i] x^i)."""
    da = _digits(a, p, r)
    db = _digits(b, p, r)
    conv = [0] * (2 * r - 1)
    for i, ai in enumerate(da):
        if ai:
            for j, bj in enumerate(db):
                if bj:
                    conv[i + j] = (conv[i + j] + ai * bj) % p
    for deg in range(2 * r - 2, r - 1, -1):
        c = conv[deg]
        if c:
            conv[deg] = 0
            for i in range(r):
                conv[deg - r + i] = (conv[deg - r + i] + c * poly[i]) % p
    return _from_digits(conv[:r], p)


class FiniteField(object):
    def __init__(self, p, r):
        assert r >= 1
        self.p = p
        self.r = r
        self.q = p ** r
        self.poly = (0,) if r == 1 else self._find_primitive_poly()
        q = self.q
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                self.add[a][b] = _poly_add(p, r, a, b)
                self.mul[a][b] = _poly_mul(p, r, self.poly, a, b)
        self.zero = 0
        self.one = 1
        # multiplicative order table of every element (0 -> None)
        self.order = [None] * q
        for a in range(1, q):
            x = a
            o = 1
            while x != 1:
                x = self.mul[x][a]
                o += 1
                if o > q:
                    raise RuntimeError("not a field")
            self.order[a] = o
        # Frobenius: a -> a^(p^s)
        self.frob = []
        for s in range(r):
            table = [0] * q
            for a in range(q):
                table[a] = self.pow(a, p ** s)
            self.frob.append(table)
        self.inv = [0] * q
        for a in range(1, q):
            self.inv[a] = self.pow(a, q - 2)

    # ---------------- primitive polynomial search ----------------
    def _is_primitive(self, poly):
        p, r, q = self.p, self.r, self.q
        x = p  # element "x"
        cur = x
        seen = set()
        for k in range(1, q - 1):
            if cur == 1 or cur == 0 or cur in seen:
                return False
            seen.add(cur)
            cur = _poly_mul(p, r, poly, cur, x)
        return cur == 1

    def _find_primitive_poly(self):
        p, r = self.p, self.r
        for coeffs in product(range(p), repeat=r):
            if self._is_primitive(coeffs):
                return coeffs
        raise RuntimeError("no primitive polynomial found")

    # ---------------- basic operations ----------------
    def pow(self, a, e):
        if e == 0:
            return 1
        result = 1
        base = a
        while e:
            if e & 1:
                result = self.mul[result][base]
            base = self.mul[base][base]
            e >>= 1
        return result

    def neg(self, a):
        # -a = (p-1)*a in characteristic p
        x = 0
        for _ in range(self.p - 1):
            x = self.add[x][a]
        return x

    def sub(self, a, b):
        return self.add[a][self.neg(b)]

    def div(self, a, b):
        return self.mul[a][self.inv[b]]

    def trace_to_prime_field(self, a):
        """absolute trace Tr_{F_q/F_p}(a) = sum_{i=0}^{r-1} a^(p^i) in F_p."""
        s = 0
        for i in range(self.r):
            s = self.add[s][self.frob[i][a]]
        # result lies in F_p: return as an int in [0,p)
        return _digits(s, self.p, self.r)[0]


# --------------------------------------------------------------------------
# Linear algebra over F_q  (vectors are tuples of ints in [0,q))
# --------------------------------------------------------------------------

def rref(F, rows, ncols):
    rows = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        sel = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        inv = F.inv[rows[r][c]]
        rows[r] = [F.mul[inv][v] for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [F.sub(rows[i][j], F.mul[f][rows[r][j]])
                           for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    out = [tuple(x) for x in rows[:r]]
    return out, piv


def row_space_basis(F, vectors, ncols):
    m, _ = rref(F, vectors, ncols)
    return m


def in_span(F, basis, piv, v, ncols):
    """membership test using an already reduced basis"""
    v = list(v)
    for row, c in zip(basis, piv):
        if v[c] != 0:
            f = v[c]
            v = [F.sub(v[j], F.mul[f][row[j]]) for j in range(ncols)]
    return all(x == 0 for x in v)


def nullspace(F, rows, ncols):
    """{v in F^ncols : rows . v = 0}"""
    m, piv = rref(F, rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for row, pc in zip(m, piv):
            v[pc] = F.neg(row[fc])
        basis.append(tuple(v))
    return basis


def intersect(F, b1, b2, ncols):
    """intersection of two subspaces of F^ncols, each given by a list of basis
    vectors; returns a reduced basis of the intersection."""
    if not b1 or not b2:
        return []
    return _intersect_clean(F, b1, b2, ncols)


def _intersect_clean(F, b1, b2, ncols):
    n1, n2 = len(b1), len(b2)
    # unknowns: a_1..a_n1, c_1..c_n2 ; equations: sum a_i b1_i + sum c_j b2_j = 0
    A = []
    for k in range(ncols):
        row = [b1[i][k] for i in range(n1)] + [b2[j][k] for j in range(n2)]
        A.append(row)
    ns = nullspace(F, A, n1 + n2)
    out = []
    for v in ns:
        coeffs = v[:n1]
        vec = [0] * ncols
        for i in range(n1):
            if coeffs[i]:
                vec = [F.add[vec[k]][F.mul[coeffs[i]][b1[i][k]]]
                       for k in range(ncols)]
        out.append(tuple(vec))
    # reduce
    return row_space_basis(F, out, ncols)


# --------------------------------------------------------------------------
# A_t = F_q[u]/<u^t>
# --------------------------------------------------------------------------

class LocalRing(object):
    """A_t = F_q[u] / <u^t>.  Elements: tuples of t field elements."""

    def __init__(self, F, t):
        self.F = F
        self.t = t
        self.zero = tuple([F.zero] * t)
        self.one = (F.one,) + tuple([F.zero] * (t - 1))

    def add(self, a, b):
        F = self.F
        return tuple(F.add[a[i]][b[i]] for i in range(self.t))

    def neg(self, a):
        F = self.F
        return tuple(F.neg(x) for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        F = self.F
        t = self.t
        out = [F.zero] * t
        for i in range(t):
            if a[i] == F.zero:
                continue
            for j in range(t - i):
                if b[j] == F.zero:
                    continue
                out[i + j] = F.add[out[i + j]][F.mul[a[i]][b[j]]]
        return tuple(out)

    def scalar(self, c, a):
        F = self.F
        return tuple(F.mul[c][x] for x in a)

    def frobenius(self, a, s):
        """a = sum a_i u^i  ->  sum a_i^(p^s) u^i  (u fixed)."""
        F = self.F
        return tuple(F.frob[s][x] for x in a)

    def uscale(self, a, c):
        """u -> c u  (F_q-algebra automorphism when c != 0)."""
        F = self.F
        return tuple(F.mul[F.pow(c, i)][a[i]] for i in range(self.t))

    def coeff(self, a, k):
        return a[k]

    def elements(self):
        return product(range(self.F.q), repeat=self.t)


# --------------------------------------------------------------------------
# R = M_m(A_t)
# --------------------------------------------------------------------------

class MatrixRing(object):
    """Elements: tuple of m rows; each row a tuple of m elements of A_t."""

    def __init__(self, A, m):
        self.A = A
        self.m = m
        self.zero = tuple(tuple([A.zero] * m) for _ in range(m))
        one = []
        for i in range(m):
            row = [A.one if j == i else A.zero for j in range(m)]
            one.append(tuple(row))
        self.one = tuple(one)

    def add(self, X, Y):
        A = self.A
        return tuple(tuple(A.add(X[i][j], Y[i][j]) for j in range(self.m))
                     for i in range(self.m))

    def neg(self, X):
        A = self.A
        return tuple(tuple(A.neg(x) for x in row) for row in X)

    def sub(self, X, Y):
        return self.add(X, self.neg(Y))

    def mul(self, X, Y):
        A = self.A
        m = self.m
        out = []
        for i in range(m):
            row = []
            for j in range(m):
                s = A.zero
                for k in range(m):
                    if X[i][k] == A.zero or Y[k][j] == A.zero:
                        continue
                    s = A.add(s, A.mul(X[i][k], Y[k][j]))
                row.append(s)
            out.append(tuple(row))
        return tuple(out)

    def transpose(self, X):
        m = self.m
        return tuple(tuple(X[j][i] for j in range(m)) for i in range(m))

    def trace(self, X):
        A = self.A
        s = A.zero
        for i in range(self.m):
            s = A.add(s, X[i][i])
        return s

    def entrywise(self, f):
        """apply f : A_t -> A_t to every entry"""
        return lambda X: tuple(tuple(f(x) for x in row) for row in X)

    def elements(self):
        A = self.A
        m = self.m
        els = list(A.elements())
        for entries in product(els, repeat=m * m):
            yield tuple(tuple(entries[i * m:(i + 1) * m]) for i in range(m))

    def dim_over_F(self):
        return self.m * self.m * self.A.t

    def basis_elements(self):
        """F_q-basis: E_ij * u^l, ordered by (l, i, j)."""
        A = self.A
        F = A.F
        m = self.m
        out = []
        for l in range(A.t):
            coef = [F.zero] * A.t
            coef[l] = F.one
            coef = tuple(coef)
            for i in range(m):
                for j in range(m):
                    M = [[A.zero] * m for _ in range(m)]
                    M[i][j] = coef
                    out.append(tuple(tuple(row) for row in M))
        return out


# --------------------------------------------------------------------------
# Ambient space R^n  (codes live here)
# --------------------------------------------------------------------------

class Ambient(object):
    """R^n as an F_q-vector space, with coordinatewise ring operations."""

    def __init__(self, R, n):
        self.R = R
        self.n = n
        self.d = R.dim_over_F()
        self.dim = n * self.d
        self.F = R.A.F
        self.basis = self.basis_vectors()

    # ---- vectorisation: index = pos*d + l*m^2 + i*m + j
    def vec(self, x):
        A = self.R.A
        m = self.R.m
        out = []
        for X in x:
            for l in range(A.t):
                for i in range(m):
                    for j in range(m):
                        out.append(X[i][j][l])
        return tuple(out)

    def unvec(self, v):
        A = self.R.A
        m = self.R.m
        t = A.t
        d = self.d
        out = []
        for pos in range(self.n):
            M = [[None] * m for _ in range(m)]
            for l in range(t):
                for i in range(m):
                    for j in range(m):
                        idx = pos * d + l * m * m + i * m + j
                        coef = v[idx]
                        if l == 0:
                            M[i][j] = [0] * t
                        M[i][j][l] = coef
            out.append(tuple(tuple(tuple(row) for row in M)))
        return tuple(out)

    def basis_vectors(self):
        out = []
        for k in range(self.dim):
            v = [0] * self.dim
            v[k] = 1
            out.append(self.unvec(tuple(v)))
        return out

    # ---- code operations
    def add(self, x, y):
        R = self.R
        return tuple(R.add(x[i], y[i]) for i in range(self.n))

    def shift(self, x):
        return (x[-1],) + x[:-1]

    def right_mult(self, x, b):
        R = self.R
        return tuple(R.mul(x[i], b) for i in range(self.n))

    def left_mult(self, x, b):
        R = self.R
        return tuple(R.mul(b, x[i]) for i in range(self.n))

    # ---- pairings (all F_q-bilinear in the SECOND argument)
    def pair_dot(self, x, y):
        """sum_i x_i y_i   (R-valued, plain 'Euclidean')"""
        R = self.R
        s = R.zero
        for i in range(self.n):
            s = R.add(s, R.mul(x[i], y[i]))
        return s

    def pair_dot_T(self, x, y):
        """sum_i x_i^T y_i  (R-valued, transpose-twisted)"""
        R = self.R
        s = R.zero
        for i in range(self.n):
            s = R.add(s, R.mul(R.transpose(x[i]), y[i]))
        return s

    def pair_sigma_inv(self, x, y, s):
        """sum_i sigma_s^{-1}(x_i) y_i  (R-valued).
        The zero-set of  sum_i x_i sigma_s(y_i)  equals the zero-set of this
        form (apply sigma_s^{-1}), so the *dual codes coincide*, but this one
        is F_q-bilinear and can be handled by linear algebra."""
        R = self.R
        A = R.A
        inv_s = (A.F.r - s) % A.F.r
        acc = R.zero
        for i in range(self.n):
            acc = R.add(acc, R.mul(R.entrywise(lambda z: A.frobenius(z, inv_s))(x[i]), y[i]))
        return acc

    def pair_sigma(self, x, y, s):
        """sum_i x_i sigma_s(y_i)   (Fan-Zhang Galois form; sigma-semilinear
        in the second argument).  Provided for cross-checking only."""
        R = self.R
        A = R.A
        acc = R.zero
        for i in range(self.n):
            acc = R.add(acc, R.mul(x[i], R.entrywise(lambda z: A.frobenius(z, s))(y[i])))
        return acc

    def theta(self, X, s):
        """theta_s = sigma_s o transpose : an ANTI-automorphism of R
        (verified experimentally in E1)."""
        A = self.R.A
        R = self.R
        return R.transpose(R.entrywise(lambda z: A.frobenius(z, s))(X))

    def pair_theta(self, x, y, s):
        """sum_i theta_s(x_i) y_i   (R-valued, F_q-bilinear in y).
        This is the candidate that makes the dual of a RIGHT module again a
        RIGHT module (the transpose is what compensates for
        non-commutativity)."""
        R = self.R
        acc = R.zero
        for i in range(self.n):
            acc = R.add(acc, R.mul(self.theta(x[i], s), y[i]))
        return acc

    def pair_trace_theta(self, x, y, s):
        """F_q-valued version: Lambda(sum_i theta_s(x_i) y_i)."""
        return self.Lambda(self.pair_theta(x, y, s))

    def Lambda(self, X):
        """Frobenius functional on R:  Lambda(X) = lambda(tr(X)) where
        lambda picks the coefficient of u^(t-1) in A_t."""
        A = self.R.A
        return A.coeff(self.R.trace(X), A.t - 1)

    def pair_trace(self, x, y):
        """F_q-valued trace pairing  Lambda(sum_i x_i y_i)."""
        return self.Lambda(self.pair_dot(x, y))

    def pair_trace_sigma(self, x, y, s):
        """F_q-valued Galois trace pairing: Lambda(sum_i sigma^{-1}(x_i) y_i).
        Same zero-set as  Lambda(sum_i x_i sigma(y_i)) = 0."""
        return self.Lambda(self.pair_sigma_inv(x, y, s))

    # ---- duals and hulls
    def dual_matrix_rows(self, gens, pairing, s=0):
        """rows of the F_q-linear system whose nullspace is the dual code.
        pairing is one of 'dot', 'dotT', 'sigmainv', 'trace', 'tracesigma'."""
        rows = []
        dim = self.dim
        d = self.d
        for xv in gens:
            x = self.unvec(xv) if (isinstance(xv, tuple)
                                   and len(xv) == dim
                                   and all(isinstance(c, int) for c in xv)) else xv
            if pairing == 'trace':
                rows.append([self.pair_trace(x, e) for e in self.basis])
                continue
            if pairing == 'tracesigma':
                rows.append([self.pair_trace_sigma(x, e, s) for e in self.basis])
                continue
            if pairing == 'tracetheta':
                rows.append([self.pair_trace_theta(x, e, s) for e in self.basis])
                continue
            vals = []
            for e in self.basis:
                if pairing == 'dot':
                    val = self.pair_dot(x, e)
                elif pairing == 'dotT':
                    val = self.pair_dot_T(x, e)
                elif pairing == 'sigmainv':
                    val = self.pair_sigma_inv(x, e, s)
                elif pairing == 'theta':
                    val = self.pair_theta(x, e, s)
                else:
                    raise ValueError(pairing)
                vals.append(self.R_vec(val))
            # vals[j] is the coordinate vector (length d) of the value at e_j;
            # the R-valued equation splits into d scalar equations:
            for k in range(d):
                rows.append([vals[j][k] for j in range(dim)])
        return rows

    def R_vec(self, X):
        A = self.R.A
        m = self.R.m
        out = []
        for l in range(A.t):
            for i in range(m):
                for j in range(m):
                    out.append(X[i][j][l])
        return out

    def as_vectors(self, gens):
        out = []
        for g in gens:
            if isinstance(g, tuple) and len(g) == self.dim \
                    and all(isinstance(c, int) for c in g):
                out.append(g)
            else:
                out.append(self.vec(g))
        return out

    def dual(self, gens, pairing, s=0):
        rows = self.dual_matrix_rows(self.as_vectors(gens), pairing, s)
        return nullspace(self.F, rows, self.dim)

    def hull(self, gens, pairing, s=0):
        V = row_space_basis(self.F, self.as_vectors(gens), self.dim)
        D = self.dual(V, pairing, s)
        return _intersect_clean(self.F, V, D, self.dim)

    # ---- fast linear-algebra closures (precomputed operator images) ----
    def op_images(self, fn):
        """images of the standard basis under a linear map fn: R^n -> R^n"""
        return [self.vec(fn(e)) for e in self.basis]

    def shift_images(self):
        if not hasattr(self, '_shift_imgs'):
            self._shift_imgs = self.op_images(self.shift)
        return self._shift_imgs

    def right_images(self):
        if not hasattr(self, '_right_imgs'):
            self._right_imgs = [self.op_images(lambda v, b=b: self.right_mult(v, b))
                                for b in self.R.basis_elements()]
        return self._right_imgs

    def left_images(self):
        if not hasattr(self, '_left_imgs'):
            self._left_imgs = [self.op_images(lambda v, b=b: self.left_mult(v, b))
                               for b in self.R.basis_elements()]
        return self._left_imgs

    def apply_lin(self, imgs, v):
        F = self.F
        out = [F.zero] * self.dim
        for k, c in enumerate(v):
            if c:
                im = imgs[k]
                out = [F.add[out[j]][F.mul[c][im[j]]] for j in range(self.dim)]
        return tuple(out)

    def close_under(self, imgs_list, vectors):
        """smallest subspace containing `vectors` (given as F_q coordinate
        vectors) and stable under every operator in imgs_list."""
        cur = [self.vec(v) if not (isinstance(v, tuple) and len(v) == self.dim
                                   and all(isinstance(c, int) for c in v)) else v
               for v in vectors]
        cur = row_space_basis(self.F, cur, self.dim)
        while True:
            new = list(cur)
            for v in cur:
                for imgs in imgs_list:
                    new.append(self.apply_lin(imgs, v))
            b = row_space_basis(self.F, new, self.dim)
            if len(b) == len(cur):
                return b
            cur = b

    # ---- cyclicity closures
    def cyclic_closure_right(self, vectors):
        """smallest subspace containing `vectors` and closed under the cyclic
        shift and under coordinatewise RIGHT multiplication by R."""
        R = self.R
        gens = list(vectors)
        cur = gens
        while True:
            new = list(cur)
            for v in cur:
                new.append(self.shift(v))
                for b in R.basis_elements():
                    new.append(self.right_mult(v, b))
            b = row_space_basis(self.F, [self.vec(v) for v in new], self.dim)
            if len(b) == len(row_space_basis(self.F,
                                             [self.vec(v) for v in cur],
                                             self.dim)):
                # stable
                return [self.unvec(x) for x in b], b
            cur = [self.unvec(x) for x in b]

    def cyclic_closure_left(self, vectors):
        R = self.R
        cur = list(vectors)
        while True:
            new = list(cur)
            for v in cur:
                new.append(self.shift(v))
                for b in R.basis_elements():
                    new.append(self.left_mult(v, b))
            b = row_space_basis(self.F, [self.vec(v) for v in new], self.dim)
            old = row_space_basis(self.F, [self.vec(v) for v in cur], self.dim)
            if len(b) == len(old):
                return [self.unvec(x) for x in b], b
            cur = [self.unvec(x) for x in b]

    def all_vectors(self):
        """iterate over all |R|^n vectors (only for tiny ambient sizes)."""
        F = self.F
        for v in product(range(F.q), repeat=self.dim):
            yield self.unvec(tuple(v))
