#!/usr/bin/env python3
"""A13 separate field-table geometry and original-global sample audit.

No primary field/module/descriptor/hull implementation is imported. The only
shared new code is the PURE INTEGER prediction function; raw geometry counts
are separately enumerated before comparison. Alternative global arithmetic
comes from the old, unchanged audit implementation. Larger q32/q64 checks
are POINT/SELF-DUAL-PLANE checks only, NOT B^2 module censuses.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import sys
import traceback

from audit_core_a_independent import AuditArithmetic, plus, units, global_test
from core_a_distribution import distribution

HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def compact(d):
    return json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n"


class GeometryArithmetic(AuditArithmetic):
    def __init__(self, q):
        if q in (4, 8, 16):
            super().__init__(q)
            return
        self.q, self.m, self.mask = q, q.bit_length() - 1, q - 1
        polynomial = {32: 0b100101, 64: 0b1000011}[q]
        cycle, a = [], 1
        for _ in range(q - 1):
            cycle.append(a)
            a <<= 1
            if a & q:
                a ^= polynomial
        assert a == 1 and set(cycle) == set(range(1, q))
        logs = {v: i for i, v in enumerate(cycle)}
        self.table = tuple(tuple(0 if not x or not y else cycle[(logs[x] + logs[y]) % (q - 1)]
                                 for y in range(q)) for x in range(q))
        self.inverse = [0] + [next(y for y in range(1, q) if self.table[x][y] == 1) for x in range(1, q)]
        # Full finite distributivity validation: not merely the cycle's size.
        for x, y, z in product(range(q), repeat=3):
            assert self.table[x][y ^ z] == (self.table[x][y] ^ self.table[x][z])
        assert all(self.table[x][y] == self.table[y][x] for x in range(q) for y in range(q))


def grassmann(ar, dimension, alphabet=None):
    """Independently enumerated canonical field subspaces of width four."""
    if alphabet is None:
        alphabet = range(ar.q)
    for pivots in combinations(range(4), dimension):
        positions = [(row, col) for row, pivot in enumerate(pivots)
                     for col in range(pivot + 1, 4) if col not in pivots]
        for values in product(alphabet, repeat=len(positions)):
            rows = [[0] * 4 for _ in pivots]
            for row, pivot in enumerate(pivots):
                rows[row][pivot] = 1
            for (row, col), value in zip(positions, values):
                rows[row][col] = value
            yield tuple(tuple(v) for v in rows)


def omega(ar, v, y, s):
    return (ar.table[ar.sf(v[0], s)][y[2]] ^ ar.table[ar.sf(v[1], s)][y[3]]
            ^ ar.table[ar.sf(v[2], s)][y[0]] ^ ar.table[ar.sf(v[3], s)][y[1]])


def determinant(ar, v):
    return ar.table[v[0]][v[3]] ^ ar.table[v[1]][v[2]]


def constraints(ar, space, s):
    return [tuple(ar.sf(a, s) for a in v[2:] + v[:2]) for v in space]


def plane_data(ar, plane):
    zeroes = int(determinant(ar, plane[1]) == 0)
    for a in range(ar.q):
        zeroes += determinant(ar, plus(plane[0], ar.vscale(a, plane[1]))) == 0
    role = {0: "external", 1: "tangent", 2: "secant", ar.q + 1: "contained"}[zeroes]
    return role, zeroes, ar.q + 1 - zeroes


def record_plane(ar, plane, s, row, digest):
    assert ar.canon(tuple(ar.sf(a, 2 * s) for a in v) for v in plane) == ar.canon(plane)
    role, zeroes, rank_two = plane_data(ar, plane)
    row["observed_plane_types"][role] += 1
    row["observed_B_incidences"] += rank_two
    digest.update(compact({"q": ar.q, "s": s, "plane": plane, "quadric_points": zeroes}).encode())
    if role not in row["one_plane_witness_each_observed_type"]:
        row["one_plane_witness_each_observed_type"][role] = plane


def geometry_full(ar):
    """All subspaces T<=k^4, each twist, not an eight-dimensional module census."""
    rows = [{"q": ar.q, "s": s, "full_all_T_enumeration": True,
             "observed_isotropic_points": 0, "observed_U_rank_two_points": 0,
             "observed_B_incidences": 0, "observed_plane_types": Counter(),
             "observed_K_V_hull_mu_one": 0, "one_plane_witness_each_observed_type": {}}
            for s in range(ar.m)]
    dimensions = Counter()
    digest = hashlib.sha256()
    for dimension in range(5):
        for space in grassmann(ar, dimension):
            dimensions[dimension] += 1
            for s, row in enumerate(rows):
                radical = ar.restrict(space, constraints(ar, space, s))
                projections = ar.canon([v[:2] for v in radical] + [v[2:] for v in radical])
                hull_mu = 2 + len(radical) - len(projections)
                assert hull_mu in (1, 2, 3)
                row["observed_K_V_hull_mu_one"] += hull_mu == 1
                if dimension == 1 and len(radical) == 1:
                    row["observed_isotropic_points"] += 1
                    row["observed_U_rank_two_points"] += determinant(ar, space[0]) != 0
                if dimension == 2 and len(radical) == 2:
                    record_plane(ar, space, s, row, digest)
    q = ar.q
    assert dimensions == {0: 1, 1: q**3 + q**2 + q + 1,
                           2: (q**2 + 1) * (q**2 + q + 1), 3: q**3 + q**2 + q + 1, 4: 1}
    for row in rows:
        row["enumerated_T_by_dimension"] = dict(dimensions)
        row["selfdual_plane_stream_sha256_for_whole_field_all_twists"] = digest.hexdigest()
    return rows


def geometry_descended(ar, twists):
    """Higher fields: all projective points and all descended self-dual planes."""
    rows = []
    for s in twists:
        row = {"q": ar.q, "s": s, "full_all_T_enumeration": False,
               "observed_isotropic_points": 0, "observed_U_rank_two_points": 0,
               "observed_B_incidences": 0, "observed_plane_types": Counter(),
               "one_plane_witness_each_observed_type": {}}
        points = 0
        for (v,) in grassmann(ar, 1):
            points += 1
            if omega(ar, v, v, s) == 0:
                row["observed_isotropic_points"] += 1
                row["observed_U_rank_two_points"] += determinant(ar, v) != 0
        assert points == ar.q**3 + ar.q**2 + ar.q + 1
        row["all_projective_points_enumerated"] = points
        fixed = [a for a in range(ar.q) if ar.sf(a, 2 * s) == a]
        assert len(fixed) == 1 << math.gcd(2 * s, ar.m)
        candidates = 0
        digest = hashlib.sha256()
        for plane in grassmann(ar, 2, fixed):
            candidates += 1
            if all(omega(ar, v, y, s) == 0 for v in plane for y in plane):
                record_plane(ar, plane, s, row, digest)
        row["fixed_field_sigma_squared_size"] = len(fixed)
        row["all_descended_two_plane_candidates"] = candidates
        row["selfdual_plane_stream_sha256"] = digest.hexdigest()
        rows.append(row)
    return rows


def compare_geometry(row):
    prediction = distribution(row["q"].bit_length() - 1, row["s"])
    assert row["observed_isotropic_points"] == prediction["layer_isotropic_projective_points"]
    assert row["observed_U_rank_two_points"] == prediction["isotropic_projection_rank_two_points_U"]
    assert dict(row["observed_plane_types"]) == {k: v for k, v in prediction["selfdual_two_plane_quadric_intersection_types"].items() if v}
    assert row["observed_B_incidences"] == prediction["selfdual_two_plane_rank_two_point_incidences_B"]
    assert (row["q"] + 3) * row["observed_U_rank_two_points"] - row["observed_B_incidences"] == prediction["mu_one_K_equals_V_inputs"]
    if row["full_all_T_enumeration"]:
        assert row["observed_K_V_hull_mu_one"] == prediction["mu_one_K_equals_V_inputs"]
    row["all_stated_formula_comparisons"] = "PASS"


def independent_local_dual(ar, space, s):
    equations = []
    for v in space:
        sv = tuple(ar.sf(a, s) for a in v)
        columns = [plus(ar.bmul(sv[:4], y[:4]), ar.bmul(sv[4:], y[4:])) for y in units(8)]
        equations.extend(tuple(v[i] for v in columns) for i in range(4))
    return ar.restrict(units(8), equations)


def main(primary_label, audit_label):
    assert primary_label and audit_label and all(c.isalnum() or c in "_-" for c in primary_label + audit_label)
    source = HERE / "results" / primary_label
    directory = HERE / "results" / audit_label
    assert not directory.exists(), "Refusing to overwrite evidence"
    directory.mkdir(parents=True)
    source_bytes = Path(__file__).read_bytes()
    try:
        primary = json.loads((source / "summary.json").read_text())
        assert primary["status"] == "PASS" and primary["new_q16_generic_and_structural_full_space_cases"] == 666084
        geometry = []
        for q in (4, 8, 16):
            rows = geometry_full(GeometryArithmetic(q))
            for row in rows:
                compare_geometry(row)
                print("PASS full layer geometry", q, "twist", row["s"], flush=True)
            geometry.extend(rows)
        for q, twists in ((32, (1, 2, 3, 4)), (64, (1, 2, 4, 5))):
            rows = geometry_descended(GeometryArithmetic(q), twists)
            for row in rows:
                compare_geometry(row)
                print("PASS points/descended planes ONLY", q, "twist", row["s"], flush=True)
            geometry.extend(rows)
        path = source / "q16_global_audit_cases.jsonl"
        assert sha(path) == primary["selected_global_cases_sha256"]
        ar = AuditArithmetic(16)
        global_records = []
        for line in path.read_text().splitlines():
            record = json.loads(line)
            assert record["field_order"] == 16
            result = global_test(ar, record)
            assert result["local_hull_basis"] == ar.canon(record["hull_basis"])
            assert independent_local_dual(ar, ar.canon(record["generators"]), record["twist"]) == ar.canon(record["dual_basis"])
            global_records.append(result)
        assert len(global_records) == primary["q16_selected_original_global_audit_cases"]
        (directory / "geometry_cases.json").write_text(json.dumps(geometry, indent=2) + "\n")
        (directory / "q16_global_cases.jsonl").write_text("".join(compact(r) for r in global_records))
        summary = {"status": "PASS", "primary_summary_sha256": sha(source / "summary.json"),
                   "source_hashes": {p.name: sha(p) for p in (HERE / "audit_core_a_independent.py", HERE / "core_a_distribution.py", Path(__file__).resolve())},
                   "primary_field_module_descriptor_hull_code_imported": False,
                   "shared_code_limited_to_integer_prediction_function": True,
                   "full_all_T_geometry_fields_and_all_twists": {"4": [0, 1], "8": [0, 1, 2], "16": [0, 1, 2, 3]},
                   "higher_point_and_descended_plane_checks_only": {"32": [1, 2, 3, 4], "64": [1, 2, 4, 5]},
                   "all_isotropic_point_U_plane_type_B_incidence_comparisons": "PASS",
                   "q32_q64_full_finite_distributivity_checks": 32**3 + 64**3,
                   "original_global_q16_cases": len(global_records),
                   "q16_global_cases_are_named_deterministic_subset_not_census": True,
                   "full_local_and_global_dual_and_hull_spaces_checked_in_selected_cases": True,
                   "geometry_cases_sha256": sha(directory / "geometry_cases.json"),
                   "q16_global_cases_sha256": sha(directory / "q16_global_cases.jsonl"),
                   "human_independent_review_completed": False, "external_originality_certified": False,
                   "joint_same_input_all_twist_distribution_certified": False}
        text = json.dumps(summary, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="", flush=True)
    except Exception:
        (directory / "FAILURE_SOURCE.py").write_bytes(source_bytes)
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Do not use -O; assertions must remain enabled")
    if len(sys.argv) != 3:
        raise SystemExit("Supply a primary label and a fresh audit label")
    main(sys.argv[1], sys.argv[2])
