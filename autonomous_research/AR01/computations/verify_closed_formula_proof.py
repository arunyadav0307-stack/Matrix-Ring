#!/usr/bin/env python3
"""Fresh proof-route regression: trace hyperplanes, graph charts, global form.

Uses the separate audit arithmetic, not the primary field/module/descriptor
implementation. Reads existing full q16 evidence as data; does NOT claim to
rerun that census. Shared integer formula is a prediction, not its oracle:
a second formula and exact sparse-polynomial identities are checked here.
No external human review or proof-assistant certification is implied.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import sys
import traceback

from audit_core_a_independent import AuditArithmetic, plus, units, global_test
from audit_core_a_distribution import GeometryArithmetic, grassmann
from core_a_distribution import distribution

HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def compact(d):
    return json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n"


class Poly:
    """Exact integer sparse polynomials in two formal variables q,Q."""
    def __init__(self, terms):
        self.terms = {k: v for k, v in terms.items() if v}

    @staticmethod
    def cast(value):
        return value if isinstance(value, Poly) else Poly({(0, 0): value})

    def __add__(self, other):
        out = dict(self.terms)
        for key, value in Poly.cast(other).terms.items():
            out[key] = out.get(key, 0) + value
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly.cast(other))

    def __rsub__(self, other):
        return Poly.cast(other) + (-self)

    def __mul__(self, other):
        out = {}
        for (i, j), a in self.terms.items():
            for (k, l), b in Poly.cast(other).terms.items():
                key = (i + k, j + l)
                out[key] = out.get(key, 0) + a * b
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert exponent >= 0
        out = Poly.cast(1)
        for _ in range(exponent):
            out = out * self
        return out

    def __eq__(self, other):
        return self.terms == Poly.cast(other).terms


def polynomial_identities():
    q, Q = Poly({(1, 0): 1}), Poly({(0, 1): 1})
    checks = []
    for parity in ("odd", "even"):
        e = Q if parity == "odd" else Q**2
        c = Q**2 if parity == "odd" else Q * (Q**2 - Q + 1)
        z = q**2 + (e + 1) * (q - 1) * q * Q + (q - e) * (q - 1) * q
        assert z == 1 + (q - 1) * (q**2 + q + 1 + q * c)
        p = (Q + 1) * (Q**2 + 1) if parity == "odd" else (Q + 1) * (Q**3 + 1)
        contained = Q + 2 if parity == "odd" else 2 * (Q + 1)
        base = (Q + 1)**3 if parity == "odd" else (Q + 1)**2 * (2 * Q**2 - Q + 1)
        f = (q + 1) * p - base - contained * (q - e)
        expected = q * (Q**3 + Q**2 - 1) - Q**2 if parity == "odd" else (Q**2 - 1) * (q * (Q**2 + Q + 1) - Q**2)
        assert f == expected
        checks.extend([parity + "_trace_vector_count", parity + "_base_incidence_F"])
    a = (q + 1) * (2 * q**2 + q + 1)
    G = q**4 + 3 * q**3 + 4 * q**2 + 3 * q + 5
    L = 2 * q**4 + 8 * q**3 + 10 * q**2 + 7 * q + 9
    assert 1 + a + G + (q + 1) * (q**3 + 2 * q**2 + q + 1) + 1 == L
    checks.append("complete_descriptor_total")
    return checks


def independent_integer_counts(m, s):
    q = 1 << m
    Q = 1 << math.gcd(m, s)
    r = m // math.gcd(m, s)
    e = Q if r % 2 else Q**2
    d = 1 if r % 2 else Q + 1
    vectors = q**2 + (e + 1) * (q - 1) * q * Q + (q - e) * (q - 1) * q
    points = (vectors - 1) // (q - 1)
    rank_one = d * (q + 1) + (q + 1 - d) * (Q + 1)
    U = points - rank_one
    planes = (Q + 1) * (Q**2 + 1) if r % 2 else (Q + 1) * (Q**3 + 1)
    contained = Q + 2 if r % 2 else 2 * (Q + 1)
    base_inc = (Q + 1)**3 if r % 2 else (Q + 1)**2 * (2 * Q**2 - Q + 1)
    F = (q + 1) * planes - base_inc - contained * (q - e)
    a = (q + 1) * (2 * q**2 + q + 1)
    G = 2 + 2 * (q**3 + q**2 + q + 1) + (q**2 + 1) * (q**2 + q + 1)
    total = 1 + a + G + (q + 1) * (q**3 + q**2 + (q + 1) * q + 1) + 1
    n0, n3 = (q + 1 - d) * q**3 + 2, d
    n1 = (a - d * q**2) + (a - d * q**2 + d * (q**3 - Q**2 * (q - Q))) + (q + 3) * U - F
    n2 = G + d * (2 * q**2 + Q**2 * (q - Q) - 1) - (q + 3) * U + F
    assert n0 + n1 + n2 + n3 == total
    return {0: n0, 1: n1, 2: n2, 3: n3}, U, F


def det(ar, v):
    return ar.table[v[0]][v[3]] ^ ar.table[v[1]][v[2]]


def omega(ar, v, y, s):
    return (ar.table[ar.sf(v[0], s)][y[2]] ^ ar.table[ar.sf(v[1], s)][y[3]]
            ^ ar.table[ar.sf(v[2], s)][y[0]] ^ ar.table[ar.sf(v[3], s)][y[1]])


def trace_and_charts(ar, s, previous):
    q = ar.q
    r = ar.m // math.gcd(ar.m, s)
    fixed = {a for a in range(q) if ar.sf(a, s) == a}
    E = [a for a in range(q) if ar.sf(a, 2 * s) == a]
    Q = len(fixed)
    sigma = [ar.sf(a, s) for a in range(q)]
    def trace(a):
        result = 0
        for j in range(r):
            result ^= ar.sf(a, j * s)
        return result
    image = {a ^ sigma[a] for a in range(q)}
    assert image == {a for a in range(q) if trace(a) == 0}
    assert {trace(a) for a in range(q)} == fixed
    for c in range(1, q):
        assert ({ar.table[c][a] for a in image} == image) == (c in fixed)
        assert (ar.table[c][sigma[c]] in fixed) == (c in E)
    kernel_counts = Counter()
    total_kernels = 0
    for a1, a2 in [(1, t) for t in range(q)] + [(0, 1)]:
        count = 0
        for b1 in range(q):
            for b2 in range(q):
                value = (ar.table[sigma[a1]][b1] ^ ar.table[sigma[a2]][b2]
                         ^ ar.table[sigma[b1]][a1] ^ ar.table[sigma[b2]][a2])
                count += value == 0
        expected = q * Q if a1 == 0 or a2 in E else q
        assert count == expected
        kernel_counts[count] += 1
        total_kernels += count
    vectors = q**2 + (q - 1) * total_kernels
    assert (vectors - 1) // (q - 1) == previous["observed_isotropic_points"]
    ranks, contained, base_rank_one, extended_rank_one = Counter(), 0, 0, 0
    for plane in grassmann(ar, 2, E):
        if not all(omega(ar, v, y, s) == 0 for v in plane for y in plane):
            continue
        rank = len(ar.canon([v[:2] for v in plane]))
        ranks[rank] += 1
        def roots(alphabet):
            return int(det(ar, plane[1]) == 0) + sum(det(ar, plus(plane[0], ar.vscale(t, plane[1]))) == 0 for t in alphabet)
        base, extended = roots(E), roots(range(q))
        is_contained = base == len(E) + 1
        contained += is_contained
        assert extended == (q + 1 if is_contained else base)
        if not r % 2:
            assert base > 0  # No external plane: tested separately from old type table.
        if rank == 2:
            v, y = plane
            assert v[:2] == (1, 0) and y[:2] == (0, 1)
            M = (v[2], y[2], v[3], y[3])
            assert M == tuple(ar.sf(M[i], s) for i in (0, 2, 1, 3))
        base_rank_one += base
        extended_rank_one += extended
    expected_ranks = {0: 1, 1: Q * (Q + 1), 2: Q**3} if r % 2 else {0: 1, 1: Q * (Q**2 + 1), 2: Q**4}
    assert dict(ranks) == expected_ranks
    assert contained == (Q + 2 if r % 2 else 2 * (Q + 1))
    assert base_rank_one == ((Q + 1)**3 if r % 2 else (Q + 1)**2 * (2 * Q**2 - Q + 1))
    F = (q + 1) * sum(ranks.values()) - extended_rank_one
    assert F == previous["observed_B_incidences"]
    return {"q": q, "s": s, "scope": "Trace kernels and descended plane graph charts ONLY, not a B^2 module census",
            "fixed_field_size": Q, "sigma_squared_fixed_field_size": len(E),
            "kernel_size_direction_counts": dict(kernel_counts), "isotropic_vectors": vectors,
            "selfdual_plane_projection_rank_counts": dict(ranks), "contained_planes": contained,
            "base_rank_one_incidences": base_rank_one, "extended_rank_one_incidences": extended_rank_one,
            "rank_two_incidences_F": F, "all_new_route_and_old_raw_geometry_counts_match": True}


def pairing_transport(ar):
    checks = 0
    for left in units(16):
        for scalar in (1, 2):
            x = ar.pack(ar.vscale(scalar, left))
            xc = ar.word_to_columns(x)
            for right in units(16):
                y = ar.pack(right)
                yc = ar.word_to_columns(y)
                for s in range(ar.m):
                    def beta(v, t):
                        sv = tuple(ar.sf(a, s) for a in v)
                        return plus(ar.bmul(sv[:4], t[:4]), ar.bmul(sv[4:], t[4:]))
                    local_columns = [beta(xc[0], yc[j]) + beta(xc[1], yc[j]) for j in (0, 1)]
                    product_word = ar.spoly(ar.theta(x[:4], s) + ar.theta(x[4:], s), y)
                    assert product_word == ar.local_to_word(local_columns)
                    assert product_word[:4] == ar.global_pair(x, y, s)
                    assert product_word[4:] == ar.global_pair(x[4:] + x[:4], y, s)
                    checks += 1
    return checks


def local_dual(ar, space, s):
    equations = []
    for v in space:
        sv = tuple(ar.sf(a, s) for a in v)
        values = [plus(ar.bmul(sv[:4], y[:4]), ar.bmul(sv[4:], y[4:])) for y in units(8)]
        equations.extend(tuple(v[i] for v in values) for i in range(4))
    return ar.restrict(units(8), equations)


def global_dual(ar, space, s):
    packed_units = [ar.pack(v) for v in units(16)]
    equations = []
    for v in space:
        values = [ar.global_pair(ar.pack(v), y, s) for y in packed_units]
        equations.extend(tuple((value[entry] >> (degree * ar.m)) & ar.mask for value in values)
                         for entry in range(4) for degree in (0, 1))
    return ar.restrict(units(16), equations)


def noninvolution_control():
    ar = AuditArithmetic(8)
    v, zero = (1, 0, 0, 0, 2, 0, 0, 0), (0,) * 8
    g = ar.local_to_word([v, zero])
    c = ar.canon(ar.expand(ar.spoly(g, ar.pack(e))) for e in units(16))
    dd = global_dual(ar, global_dual(ar, c, 1), 1)
    expected = ar.canon(tuple(ar.sf(a, 2) for a in row) for row in c)
    assert dd == expected and dd != c
    return {"q": 8, "s": 1, "input_free_line_slope": 2,
            "double_dual_slope_sigma_squared": ar.sf(2, 2),
            "original_global_double_dual_equals_positive_sigma_squared_not_input": True}


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    directory = HERE / "results" / label
    assert not directory.exists(), "Refusing to overwrite evidence"
    directory.mkdir(parents=True)
    own_source = Path(__file__).read_bytes()
    try:
        polynomial_checks = polynomial_identities()
        integer_cases = 0
        for m in range(1, 65):
            for s in range(m):
                observed, U, F = independent_integer_counts(m, s)
                expected = distribution(m, s)
                assert observed == expected["hull_mu_counts"]
                assert U == expected["isotropic_projection_rank_two_points_U"]
                assert F == expected["selfdual_two_plane_rank_two_point_incidences_B"]
                integer_cases += 1
        geometry_path = HERE / "results/distribution_audit_v1/geometry_cases.json"
        old_geometry = json.loads(geometry_path.read_text())
        arithmetic, geometry = {}, []
        for row in old_geometry:
            q, s = row["q"], row["s"]
            if q not in arithmetic:
                arithmetic[q] = GeometryArithmetic(q)
            geometry.append(trace_and_charts(arithmetic[q], s, row))
            print("PASS independent trace/graph route", q, s, flush=True)
        basis_checks = sum(pairing_transport(AuditArithmetic(q)) for q in (4, 8, 16))
        negative = noninvolution_control()
        results, hist_q4 = [], [Counter(), Counter()]
        paths = (HERE / "results/structure_v1/cases_q4.jsonl", HERE / "results/distribution_v1/q16_global_audit_cases.jsonl")
        for path in paths:
            for line in path.read_text().splitlines():
                record = json.loads(line)
                ar = arithmetic[record["field_order"]]
                result = global_test(ar, record)
                assert result["local_hull_basis"] == ar.canon(record["hull_basis"])
                if "dual_basis" in record:
                    assert local_dual(ar, ar.canon(record["generators"]), record["twist"]) == ar.canon(record["dual_basis"])
                if record["field_order"] == 4:
                    hist_q4[record["twist"]][result["hull_mu"]] += 1
                results.append(result)
        assert len(results) == 2442 + 176
        for s in (0, 1):
            assert dict(hist_q4[s]) == independent_integer_counts(2, s)[0]
        q16_path = HERE / "results/distribution_v1/summary.json"
        q16 = json.loads(q16_path.read_text())
        assert q16["status"] == "PASS" and q16["new_q16_generic_and_structural_full_space_cases"] == 666084
        for row in q16["q16_observations"]:
            assert {int(k): v for k, v in row["observed_hull_mu_counts"].items()} == independent_integer_counts(4, row["s"])[0]
        (directory / "trace_and_graph_cases.json").write_text(json.dumps(geometry, indent=2) + "\n")
        h = hashlib.sha256()
        for r in results:
            h.update(compact(r).encode())
        # Complete q4 output already exists at M3: do not duplicate a bulk stream.
        (directory / "noninvolution_control.json").write_text(json.dumps(negative, indent=2) + "\n")
        summary = {"status": "PASS", "exact_sparse_polynomial_identities": polynomial_checks,
                   "integer_formula_regressions_m1_to_64": integer_cases,
                   "integer_regressions_not_claimed_as_field_or_module_censuses": True,
                   "new_trace_graph_geometry_cases": len(geometry),
                   "higher_q32_q64_geometry_only_not_module_census": True,
                   "original_global_coefficient_and_shift_basis_checks": basis_checks,
                   "fresh_original_global_all_q4_cases": 2442, "fresh_original_global_selected_q16_cases": 176,
                   "full_global_dual_hull_and_reference_hull_spaces_checked": True,
                   "q16_full_module_census_compared_as_existing_evidence_not_rerun": 666084,
                   "original_global_basis_stream_sha256_hash_only": h.hexdigest(),
                   "q16_existing_summary_sha256": sha(q16_path), "existing_geometry_sha256": sha(geometry_path),
                   "new_trace_graph_records_sha256": sha(directory / "trace_and_graph_cases.json"),
                   "source_hashes": {p.name: sha(p) for p in (HERE / "audit_core_a_independent.py", HERE / "audit_core_a_distribution.py", HERE / "core_a_distribution.py", Path(__file__).resolve())},
                   "human_independent_review_completed": False, "proof_assistant_checked": False,
                   "external_originality_certified": False}
        text = json.dumps(summary, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="", flush=True)
    except Exception:
        (directory / "FAILURE_SOURCE.py").write_bytes(own_source)
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Do not disable assertions with -O")
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh result label")
    main(sys.argv[1])
