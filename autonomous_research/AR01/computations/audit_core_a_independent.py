#!/usr/bin/env python3
"""Algorithmically separate audit; NOT a human independent peer review.

Imports only standard-library modules and reads the main run as DATA. It does
not import core_a or project arithmetic. Two alternative routes are used:
(1) all 417,199 binary ambient RREF subspaces, B-action filtering and brute
    set orthogonals (not all generating matrices);
(2) original global R^2 matrix-valued pairing and right-multiplication spans,
    using hardcoded primitive-element field tables and iterative hyperplane
    restriction (not the primary field/matrix/kernel implementation).
"""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import hashlib
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def b2_product(a, b):
    a0, au, aw, az = ((a >> i) & 1 for i in range(4))
    b0, bu, bw, bz = ((b >> i) & 1 for i in range(4))
    return ((a0 & b0) | (((a0 & bu) ^ (au & b0)) << 1)
            | (((a0 & bw) ^ (aw & b0)) << 2)
            | (((a0 & bz) ^ (au & bw) ^ (aw & bu) ^ (az & b0)) << 3))


B2 = [[b2_product(a, b) for b in range(16)] for a in range(16)]


def binary_action(v, scalar):
    return B2[scalar][v & 15] | (B2[scalar][v >> 4] << 4)


def binary_span(values):
    space = {0}
    for v in values:
        if v not in space:
            space |= {x ^ v for x in space}
    return space


def binary_member(rows, v):
    for row in rows:
        p = row & -row
        if v & p:
            v ^= row
    return v == 0


def binary_rref_candidates():
    for dimension in range(9):
        for pivots in combinations(range(8), dimension):
            positions = [(i, c) for i, p in enumerate(pivots)
                         for c in range(p + 1, 8) if c not in pivots]
            for bits in range(1 << len(positions)):
                rows = [1 << p for p in pivots]
                for index, (i, c) in enumerate(positions):
                    if (bits >> index) & 1:
                        rows[i] |= 1 << c
                yield tuple(rows)


def binary_mu(space):
    radical = binary_span([binary_action(x, c) for x in space for c in (2, 4)])
    assert len(space) & (len(space) - 1) == 0
    assert len(radical) & (len(radical) - 1) == 0
    return len(space).bit_length() - len(radical).bit_length()


def binary_exhaustion(main_data):
    count = stable = 0
    principal_keys = set()
    distribution = Counter()
    maximum_principal_hull = 0
    all_rows = []
    for rows in binary_rref_candidates():
        count += 1
        if not all(binary_member(rows, binary_action(v, c)) for v in rows for c in (2, 4)):
            continue
        stable += 1
        w = binary_span(rows)
        d = {z for z in range(256)
             if all((B2[v & 15][z & 15] ^ B2[v >> 4][z >> 4]) == 0 for v in rows)}
        h = w & d
        assert len(w) * len(d) == 256
        assert len(h) & (len(h) - 1) == 0
        input_mu, hull_mu = binary_mu(w), binary_mu(h)
        distribution[(input_mu, hull_mu)] += 1
        if input_mu <= 2:
            principal_keys.add(rows)
            maximum_principal_hull = max(maximum_principal_hull, hull_mu)
            assert hull_mu <= 2
        all_rows.append({"basis_bits_low_pivots": rows, "input_dimension": len(rows),
                         "input_mu": input_mu, "hull_dimension": len(h).bit_length() - 1,
                         "hull_mu": hull_mu})
    assert count == 417199
    main_keys = {tuple(sum(x << i for i, x in enumerate(row)) for row in record["basis"])
                 for record in main_data["auxiliary_q2"]}
    assert principal_keys == main_keys
    assert maximum_principal_hull == 2
    return {"ambient_subspaces_exhausted": count, "all_B_submodules_found": stable,
            "principal_input_modules": len(principal_keys),
            "all_primary_principal_input_canonical_spaces_match": True,
            "maximum_principal_input_hull_mu": maximum_principal_hull,
            "outside_core_m_ge_2": True,
            "input_mu_hull_mu_counts": [{"mu_pair": list(k), "modules": v}
                                        for k, v in sorted(distribution.items())]}, all_rows


class AuditArithmetic:
    def __init__(self, q):
        self.q = q
        self.m = q.bit_length() - 1
        self.mask = q - 1
        if q == 4:
            self.table = ((0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))
        else:
            # Explicit powers of alpha; not shift/reduce arithmetic from core_a.
            cycle = {8: (1, 2, 4, 3, 6, 7, 5),
                     16: (1, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9)}[q]
            assert set(cycle) == set(range(1, q))
            logs = {v: i for i, v in enumerate(cycle)}
            self.table = tuple(tuple(0 if not a or not b else cycle[(logs[a] + logs[b]) % (q - 1)]
                                     for b in range(q)) for a in range(q))
        self.inverse = [0] + [next(b for b in range(1, q) if self.table[a][b] == 1)
                              for a in range(1, q)]

    def sf(self, a, s):
        for _ in range(s % self.m):
            a = self.table[a][a]
        return a

    def amul(self, a, b):
        a0, a1 = a & self.mask, a >> self.m
        b0, b1 = b & self.mask, b >> self.m
        return self.table[a0][b0] | ((self.table[a0][b1] ^ self.table[a1][b0]) << self.m)

    def asigma(self, a, s):
        return self.sf(a & self.mask, s) | (self.sf(a >> self.m, s) << self.m)

    def bmul(self, a, b):
        a0, au, aw, az = a
        b0, bu, bw, bz = b
        t = self.table
        return (t[a0][b0], t[a0][bu] ^ t[au][b0], t[a0][bw] ^ t[aw][b0],
                t[a0][bz] ^ t[au][bw] ^ t[aw][bu] ^ t[az][b0])

    def rmult(self, a, b):
        return (self.amul(a[0], b[0]) ^ self.amul(a[1], b[2]),
                self.amul(a[0], b[1]) ^ self.amul(a[1], b[3]),
                self.amul(a[2], b[0]) ^ self.amul(a[3], b[2]),
                self.amul(a[2], b[1]) ^ self.amul(a[3], b[3]))

    def theta(self, a, s):
        return tuple(self.asigma(a[i], s) for i in (0, 2, 1, 3))

    def spoly(self, a, b):
        a0, a1, b0, b1 = a[:4], a[4:], b[:4], b[4:]
        return plus(self.rmult(a0, b0), self.rmult(a1, b1)) + plus(self.rmult(a0, b1), self.rmult(a1, b0))

    def global_pair(self, a, b, s):
        return plus(self.rmult(self.theta(a[:4], s), b[:4]),
                    self.rmult(self.theta(a[4:], s), b[4:]))

    def expand(self, global_word):
        return tuple(x for a in global_word for x in (a & self.mask, a >> self.m))

    def pack(self, field_word):
        return tuple(field_word[i] | (field_word[i + 1] << self.m) for i in range(0, 16, 2))

    def local_to_word(self, columns):
        assert len(columns) == 2
        entries = (columns[0][:4], columns[1][:4], columns[0][4:], columns[1][4:])
        constants, xcoeff = [], []
        for c0, cu, cw, cz in entries:
            constants.append((c0 ^ cw) | ((cu ^ cz) << self.m))
            xcoeff.append(cw | (cz << self.m))
        return tuple(constants + xcoeff)

    def word_to_columns(self, word):
        columns = []
        for col in (0, 1):
            vector = []
            for row in (0, 1):
                a = word[2 * row + col]
                b = word[4 + 2 * row + col]
                vector.extend(((a & self.mask) ^ (b & self.mask),
                               (a >> self.m) ^ (b >> self.m), b & self.mask, b >> self.m))
            columns.append(tuple(vector))
        return columns

    def vscale(self, a, v):
        return tuple(self.table[a][x] for x in v)

    def dot(self, a, b):
        answer = 0
        for x, y in zip(a, b):
            answer ^= self.table[x][y]
        return answer

    def canon(self, vectors):
        pivots = {}
        for v in vectors:
            row = tuple(v)
            for p in sorted(pivots, reverse=True):
                if row[p]:
                    row = plus(row, self.vscale(row[p], pivots[p]))
            if any(row):
                p = max(i for i, x in enumerate(row) if x)
                row = self.vscale(self.inverse[row[p]], row)
                for old in list(pivots):
                    if pivots[old][p]:
                        pivots[old] = plus(pivots[old], self.vscale(pivots[old][p], row))
                pivots[p] = row
        return tuple(pivots[p] for p in sorted(pivots, reverse=True))

    def restrict(self, vectors, equations):
        # Successive hyperplane intersections, not a primary RREF nullspace.
        vectors = list(vectors)
        for equation in equations:
            values = [self.dot(equation, v) for v in vectors]
            if not any(values):
                continue
            pivot = next(i for i, a in enumerate(values) if a)
            normalized = self.vscale(self.inverse[values[pivot]], vectors[pivot])
            vectors = [plus(v, self.vscale(values[i], normalized))
                       for i, v in enumerate(vectors) if i != pivot]
        return self.canon(vectors)


def plus(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def units(n):
    return [tuple(int(i == j) for i in range(n)) for j in range(n)]


def local_action(arithmetic, scalar, v):
    return arithmetic.bmul(scalar, v[:4]) + arithmetic.bmul(scalar, v[4:])


def local_module(arithmetic, generators):
    monomials = units(4)
    return arithmetic.canon(local_action(arithmetic, b, g) for g in generators for b in monomials)


def lift(arithmetic, basis):
    zero = (0,) * 8
    return arithmetic.canon(arithmetic.expand(arithmetic.local_to_word(cols))
                            for v in basis for cols in ([v, zero], [zero, v]))


def global_test(arithmetic, record):
    generators = [tuple(g) for g in record["generators"]]
    zero = (0,) * 8
    input_matrices = [arithmetic.local_to_word([g, zero]) for g in generators]
    # Each input column generates its right ideal by original polynomial products.
    right_units = [arithmetic.pack(v) for v in units(16)]
    c = arithmetic.canon(arithmetic.expand(arithmetic.spoly(g, a))
                         for g in input_matrices for a in right_units)
    w = local_module(arithmetic, generators)
    assert c == lift(arithmetic, w)
    s = record["twist"]
    equations = []
    for x in c:
        columns = [arithmetic.global_pair(arithmetic.pack(x), y, s) for y in right_units]
        for entry in range(4):
            for degree in (0, 1):
                equations.append(tuple((v[entry] >> (degree * arithmetic.m)) & arithmetic.mask
                                       for v in columns))
    d_global = arithmetic.restrict(units(16), equations)
    h_global = arithmetic.restrict(c, equations)
    local_equations = []
    for v in w:
        columns = []
        sigma_v = tuple(arithmetic.sf(a, s) for a in v)
        for z in units(8):
            columns.append(plus(arithmetic.bmul(sigma_v[:4], z[:4]),
                                arithmetic.bmul(sigma_v[4:], z[4:])))
        local_equations.extend(tuple(v[i] for v in columns) for i in range(4))
    d_local = arithmetic.restrict(units(8), local_equations)
    h_local = arithmetic.restrict(w, local_equations)
    assert d_global == lift(arithmetic, d_local)
    assert h_global == lift(arithmetic, h_local)
    projected = arithmetic.canon(v for x in h_global
                                 for v in arithmetic.word_to_columns(arithmetic.pack(x)))
    assert projected == h_local
    jh = arithmetic.canon(local_action(arithmetic, b, v) for b in ((0, 1, 0, 0), (0, 0, 1, 0))
                          for v in projected)
    hull_mu = len(projected) - len(jh)
    assert len(c) == record["global_code_dim_k"]
    assert len(h_global) == record["global_hull_dim_k"]
    assert len(d_local) == record["dual_dim_k"]
    assert hull_mu == record["hull_mu"]
    return {"q": arithmetic.q, "twist": s,
            "name": record.get("case", record.get("category", "sample")),
            "sample_index": record.get("sample_index"),
            "global_code_dimension": len(c), "global_dual_dimension": len(d_global),
            "global_hull_dimension": len(h_global), "hull_mu": hull_mu,
            "global_local_bases_equal": True,
            "local_hull_basis": h_local, "global_hull_basis": h_global}


def functional_and_negative_checks(arithmetic):
    for x in units(16):
        for scalar in (1, 2):
            x = arithmetic.vscale(scalar, x)
            for y in units(16):
                xc = arithmetic.word_to_columns(arithmetic.pack(x))
                yc = arithmetic.word_to_columns(arithmetic.pack(y))
                for s in range(arithmetic.m):
                    value = arithmetic.global_pair(arithmetic.pack(x), arithmetic.pack(y), s)
                    global_scalar = (value[0] >> arithmetic.m) ^ (value[3] >> arithmetic.m)
                    local_scalar = 0
                    for v, z in zip(xc, yc):
                        sv = tuple(arithmetic.sf(a, s) for a in v)
                        b = plus(arithmetic.bmul(sv[:4], z[:4]), arithmetic.bmul(sv[4:], z[4:]))
                        local_scalar ^= b[1] ^ b[3]
                    assert global_scalar == local_scalar
    # Wrong left-action law, checked on actual matrices over A.
    a, x, y = (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 1)
    lhs = arithmetic.rmult(arithmetic.theta(arithmetic.rmult(a, x), 0), y)
    rhs = arithmetic.rmult(arithmetic.theta(a, 0), arithmetic.rmult(arithmetic.theta(x, 0), y))
    assert lhs != rhs
    u = 1 << arithmetic.m
    assert arithmetic.asigma(u, 1) == u and arithmetic.amul(u, u) == 0
    return {"q": arithmetic.q, "actual_scalar_functional_basis_checks_all_twists": "PASS",
            "wrong_left_action_counterexample_detected": True,
            "coefficient_frobenius_fixes_u_but_whole_ring_square_does_not": True}


def main(main_label, audit_label):
    assert all(c.isalnum() or c in "_-" for c in main_label + audit_label)
    source = HERE / "results" / main_label / "cases.json"
    directory = HERE / "results" / audit_label
    assert not directory.exists(), "Refusing to overwrite a prior audit"
    directory.mkdir(parents=True)
    try:
        data = json.loads(source.read_text())
        binary, binary_records = binary_exhaustion(data)
        selected = list(data["named_core_cases"])
        selected.extend(r for r in data["sampled_core_cases"] if r["field_order"] == 4 and r["sample_index"] < 4)
        arithmetic = {q: AuditArithmetic(q) for q in (4, 8, 16)}
        global_records = [global_test(arithmetic[r["field_order"]], r) for r in selected]
        functional = [functional_and_negative_checks(arithmetic[q]) for q in arithmetic]
        result = {"status": "PASS", "primary_source_data_sha256": digest(source),
                  "audit_script_sha256": digest(Path(__file__).resolve()),
                  "no_primary_or_original_project_arithmetic_imports": True,
                  "binary_auxiliary_exhaustion": binary,
                  "global_matrix_pairing_cases": len(global_records),
                  "global_case_scope": "All 72 named q=4,8,16 cases including out-of-class controls; first four samples/category at q=4 for both twists (40 cases)",
                  "full_global_local_hull_and_dual_spaces_compared_not_only_dimensions": True,
                  "functional_checks": functional,
                  "human_independent_review_completed": False,
                  "limitations": "Finite algorithmic/representation cross-check by same agent; neither external peer review, proof assistant certificate nor exhaustive core q=4,8,16 census"}
        (directory / "binary_all_modules.json").write_text(json.dumps(binary_records, indent=2) + "\n")
        (directory / "global_cases.json").write_text(json.dumps(global_records, indent=2) + "\n")
        text = json.dumps(result, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Supply primary output label and fresh audit label")
    main(sys.argv[1], sys.argv[2])
