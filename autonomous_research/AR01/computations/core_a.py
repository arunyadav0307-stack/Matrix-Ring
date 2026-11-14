"""Exact reference arithmetic for the unchanged Core A contract.

No project arithmetic or third-party package is imported. Local monomial order
is (1,u,w,uw), with an 8-coordinate column in B^2. This is infrastructure,
not a claim of a novel hull algorithm.
"""
from itertools import combinations, product


class Field:
    POLYNOMIALS = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

    def __init__(self, degree):
        self.m = degree
        self.q = 1 << degree
        self.modulus = self.POLYNOMIALS[degree]
        self.mul = [[self._multiply(a, b) for b in range(self.q)] for a in range(self.q)]
        self.inverse = [0] + [self.power(a, self.q - 2) for a in range(1, self.q)]

    def _multiply(self, a, b):
        answer = 0
        while b:
            if b & 1:
                answer ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return answer

    def power(self, a, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul[answer][a]
            a = self.mul[a][a]
            exponent >>= 1
        return answer

    def frobenius(self, a, twist):
        return self.power(a, 1 << (twist % self.m))


def rref(rows, field, width):
    rows = list(rows)
    assert all(len(r) == width and all(0 <= x < field.q for x in r) for r in rows)
    matrix = [list(r) for r in rows if any(r)]
    pivot_row = 0
    for col in range(width):
        chosen = next((i for i in range(pivot_row, len(matrix)) if matrix[i][col]), None)
        if chosen is None:
            continue
        matrix[pivot_row], matrix[chosen] = matrix[chosen], matrix[pivot_row]
        inv = field.inverse[matrix[pivot_row][col]]
        matrix[pivot_row] = [field.mul[inv][x] for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [x ^ field.mul[factor][y] for x, y in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(r) for r in matrix[:pivot_row])


def nullspace(rows, field, width):
    reduced = rref(rows, field, width)
    pivots = [next(i for i, x in enumerate(r) if x) for r in reduced]
    free = [i for i in range(width) if i not in pivots]
    answer = []
    for col in free:
        v = [0] * width
        v[col] = 1
        for row, pivot in zip(reduced, pivots):
            v[pivot] = row[col]  # minus equals plus in characteristic two
        answer.append(v)
    return rref(answer, field, width)


def intersection(left, right, field, width=8):
    # This is ordinary field linear algebra, not an assertion about the code's
    # sesquilinear dual: (L^o + R^o)^o = L intersect R.
    constraints = nullspace(left, field, width) + nullspace(right, field, width)
    return nullspace(constraints, field, width)


def contains(space, vector, field, width=8):
    return len(rref(tuple(space) + (tuple(vector),), field, width)) == len(space)


def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def ring_mul(a, b, field):
    assert len(a) == len(b) == 4
    answer = [0, 0, 0, 0]
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y and not (i & j):
                    answer[i | j] ^= field.mul[x][y]
    return tuple(answer)


def scale_ring(a, vector, field):
    assert len(vector) == 8
    return ring_mul(a, vector[:4], field) + ring_mul(a, vector[4:], field)


def act_u(v):
    assert len(v) == 8
    return (0, v[0], 0, v[2], 0, v[4], 0, v[6])


def act_w(v):
    assert len(v) == 8
    return (0, 0, v[0], v[1], 0, 0, v[4], v[5])


def module_span(generators, field):
    rows = []
    for v in generators:
        assert len(v) == 8
        rows.extend((v, act_u(v), act_w(v), act_u(act_w(v))))
    return rref(rows, field, 8)


def radical(space, field):
    return rref([act_u(v) for v in space] + [act_w(v) for v in space], field, 8)


def mu(space, field):
    return len(space) - len(radical(space, field))


def beta(v, z, twist, field):
    sigma_v = tuple(field.frobenius(x, twist) for x in v)
    return add(ring_mul(sigma_v[:4], z[:4], field),
               ring_mul(sigma_v[4:], z[4:], field))


def dual(space, twist, field):
    constraints = []
    for v in space:
        columns = []
        for i in range(8):
            unit = tuple(int(j == i) for j in range(8))
            columns.append(beta(v, unit, twist, field))
        constraints.extend(tuple(columns[col][coefficient] for col in range(8))
                           for coefficient in range(4))
    return nullspace(constraints, field, 8)


def hull(space, twist, field):
    return intersection(space, dual(space, twist, field), field)


def sigma_space(space, twist, field):
    return rref([tuple(field.frobenius(a, twist) for a in v) for v in space], field, 8)


def all_rref_subspaces(field, width):
    """Complete RREF enumeration; practical here only for very small widths."""
    for dimension in range(width + 1):
        for pivots in combinations(range(width), dimension):
            free_positions = [(i, col) for i, pivot in enumerate(pivots)
                              for col in range(pivot + 1, width) if col not in pivots]
            for values in product(range(field.q), repeat=len(free_positions)):
                rows = [[0] * width for _ in pivots]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for (i, col), value in zip(free_positions, values):
                    rows[i][col] = value
                yield tuple(tuple(r) for r in rows)


def binary_basis(values):
    """Canonical XOR basis, used only for exhaustive q=2 generator deduplication."""
    pivots = {}
    for value in values:
        for p in sorted(pivots, reverse=True):
            if (value >> p) & 1:
                value ^= pivots[p]
        if value:
            p = value.bit_length() - 1
            for j in list(pivots):
                if (pivots[j] >> p) & 1:
                    pivots[j] ^= value
            pivots[p] = value
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def binary_u(value):
    def one(a):
        return ((a & 1) << 1) | ((a & 4) << 1)
    return one(value & 15) | (one(value >> 4) << 4)


def binary_w(value):
    def one(a):
        return ((a & 1) << 2) | ((a & 2) << 2)
    return one(value & 15) | (one(value >> 4) << 4)


def all_binary_principal_inputs():
    """Enumerate all 16^4 matrices over the auxiliary q=2 ring, with multiplicity."""
    closures = [binary_basis((v, binary_u(v), binary_w(v), binary_u(binary_w(v))))
                for v in range(256)]
    result = {}
    for first in range(256):
        for second in range(256):
            key = binary_basis(closures[first] + closures[second])
            if key in result:
                result[key][0] += 1
            else:
                result[key] = [1, first, second]
    assert sum(r[0] for r in result.values()) == 65536
    return result
