#!/usr/bin/env python3
"""Variable-length audit from the ORIGINAL global matrix-valued form.

Imports the alternative field-table/canonical-basis implementation only, not
core_a or verify_split_coupling. The primary run is read as data. Codes are
rebuilt by cyclic polynomial MATRIX products; duals and hulls by all eight
field coordinates of sum theta_s(x_i) y_i. Complete spaces, not only their
dimensions, are compared through a separately evaluated CRT map.

Same agent, separate arithmetic/representation/linear-algebra implementation;
NOT independent human review, external originality or an all-code census.
"""
from pathlib import Path
import hashlib
import json
import sys
import traceback

from audit_core_a_independent import AuditArithmetic, plus, units, local_action

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def basis_hash(basis):
    return hashlib.sha256(json.dumps(basis, separators=(",", ":")).encode()).hexdigest()


def power(ar, a, exponent):
    assert exponent >= 0
    result = 1
    for _ in range(exponent):
        result = ar.table[result][a]
    return result


def pack(ar, vector):
    assert len(vector) % 2 == 0
    assert all(0 <= a < ar.q for a in vector)
    return tuple(vector[i] | (vector[i + 1] << ar.m) for i in range(0, len(vector), 2))


def polynomial_product(ar, left, right):
    assert len(left) == len(right) and len(left) % 4 == 0
    n = len(left) // 4
    answer = [0] * (4 * n)
    nonzero_left = [(i, left[4 * i:4 * i + 4]) for i in range(n) if any(left[4 * i:4 * i + 4])]
    nonzero_right = [(i, right[4 * i:4 * i + 4]) for i in range(n) if any(right[4 * i:4 * i + 4])]
    for i, a in nonzero_left:
        for j, b in nonzero_right:
            value = ar.rmult(a, b)
            offset = 4 * ((i + j) % n)
            for entry in range(4):
                answer[offset + entry] ^= value[entry]
    return tuple(answer)


def original_pair(ar, left, right, s):
    assert len(left) == len(right) and len(left) % 4 == 0
    value = (0,) * 4
    for i in range(0, len(left), 4):
        x, y = left[i:i + 4], right[i:i + 4]
        if any(x) and any(y):
            value = plus(value, ar.rmult(ar.theta(x, s), y))
    return value


def adjoint(ar, word, s):
    n = len(word) // 4
    answer = [0] * len(word)
    for i in range(n):
        answer[4 * ((-i) % n):4 * ((-i) % n) + 4] = ar.theta(word[4 * i:4 * i + 4], s)
    return tuple(answer)


def evaluate(ar, word, root):
    """Direct X -> root(1+w) expansion, no inverse-CRT import."""
    assert len(word) % 4 == 0
    entries = [[0] * 4 for _ in range(4)]
    factor = 1
    for i in range(len(word) // 4):
        for j in range(4):
            a = word[4 * i + j]
            a0, au = ar.table[factor][a & ar.mask], ar.table[factor][a >> ar.m]
            entries[j][0] ^= a0
            entries[j][1] ^= au
            if i % 2:
                entries[j][2] ^= a0
                entries[j][3] ^= au
        factor = ar.table[factor][root]
    return tuple(tuple(v) for v in entries)


def gamma(ar, vector, roots):
    word = pack(ar, vector)
    answer = []
    for root in roots:
        matrix = evaluate(ar, word, root)
        answer.extend(matrix[0] + matrix[2] + matrix[1] + matrix[3])
    return tuple(answer)


def expected_crt_space(ar, components, key):
    rows = []
    width = 16 * len(components)
    for i, component in enumerate(components):
        for v in component[key]:
            for col in (0, 1):
                row = [0] * width
                row[16 * i + 8 * col:16 * i + 8 * (col + 1)] = v
                rows.append(row)
    return ar.canon(rows)


def local_pair_equations(ar, source, s):
    equations = []
    for v in source:
        sv = tuple(ar.sf(a, s) for a in v)
        values = [plus(ar.bmul(sv[:4], z[:4]), ar.bmul(sv[4:], z[4:])) for z in units(8)]
        equations.extend(tuple(v[i] for v in values) for i in range(4))
    return equations


def module_mu(ar, space):
    radical = ar.canon(local_action(ar, b, v)
                        for b in ((0, 1, 0, 0), (0, 0, 1, 0)) for v in space)
    return len(space) - len(radical)


def scalar_identity_word(scalars):
    return tuple(x for a in scalars for x in (a, 0, 0, a))


def explicit_same_input_hull_generators(ar, n, s):
    assert ar.q == 4 and n == 6 and s in (0, 1)
    e = [0] * n
    root = 2 if s == 0 else 3
    for j in range(3):
        e[2 * j] = power(ar, ar.inverse[root], 2 * j)
    u = scalar_identity_word([1 << ar.m] + [0] * (n - 1))
    w = scalar_identity_word([1, 0, 0, 1, 0, 0])
    e = scalar_identity_word(e)
    if s == 0:
        return [polynomial_product(ar, e, u), polynomial_product(ar, e, w)]
    return [polynomial_product(ar, polynomial_product(ar, e, u), w)]


def audit_case(ar, record, cache):
    n, N, s = record["n"], record["N"], record["twist"]
    assert n == 2 * N and N % 2 == 1 and (ar.q - 1) % N == 0
    roots = record["roots"]
    assert roots == [r for r in range(1, ar.q) if power(ar, r, N) == 1]
    components = record["components"]
    assert [r["root"] for r in components] == roots
    width = 8 * n
    cache_key = (ar.q, n)
    if cache_key not in cache:
        field_units = units(width)
        right_units = [pack(ar, v) for v in field_units]
        # A FULL rank test, not just evaluation of this particular generator.
        assert ar.canon(gamma(ar, v, roots) for v in field_units) == ar.canon(field_units)
        cache[cache_key] = (field_units, right_units)
    field_units, right_units = cache[cache_key]
    generator = pack(ar, record["global_generator_field_coordinates"])
    global_c = ar.canon(ar.expand(polynomial_product(ar, generator, a)) for a in right_units)
    # Original form constraints are built before using any primary local dual.
    equations = []
    for x in global_c:
        values = [original_pair(ar, pack(ar, x), y, s) for y in right_units]
        for entry in range(4):
            for degree in (0, 1):
                equations.append(tuple((v[entry] >> (degree * ar.m)) & ar.mask for v in values))
    global_d = ar.restrict(field_units, equations)
    global_h = ar.restrict(global_c, equations)
    assert len(global_c) + len(global_d) == width
    assert len(global_c) == record["global_code_dim_k"]
    assert len(global_d) == record["global_dual_dim_k"]
    assert len(global_h) == record["global_hull_dim_k"]
    transformed = {}
    for name, space in (("input_basis", global_c), ("dual_basis", global_d), ("hull_basis", global_h)):
        transformed[name] = ar.canon(gamma(ar, x, roots) for x in space)
        assert transformed[name] == expected_crt_space(ar, components, name)
    dagger = adjoint(ar, generator, s)
    for root, component in zip(roots, components):
        actual = evaluate(ar, generator, root)
        assert actual == tuple(tuple(v) for v in component["input_matrix"])
        source_root = ar.sf(ar.inverse[root], -s)
        assert source_root == component["source_root_for_dual"]
        source = evaluate(ar, generator, source_root)
        expected_adjoint = tuple(tuple(ar.sf(x, s) for x in source[i]) for i in (0, 2, 1, 3))
        assert evaluate(ar, dagger, root) == expected_adjoint
    local_inputs, local_hulls, local_duals, component_results = {}, {}, {}, []
    for i, component in enumerate(components):
        root = component["root"]
        for key, destination in (("input_basis", local_inputs), ("dual_basis", local_duals), ("hull_basis", local_hulls)):
            destination[root] = ar.canon(v[16 * i + 8 * col:16 * i + 8 * (col + 1)]
                                         for v in transformed[key] for col in (0, 1))
        input_mu, hull_mu = module_mu(ar, local_inputs[root]), module_mu(ar, local_hulls[root])
        assert input_mu == component["input_mu"] <= 2
        assert hull_mu == component["hull_mu"]
        component_results.append({"root": root, "input_mu": input_mu, "hull_mu": hull_mu,
                                  "input_column_dimension": len(local_inputs[root]),
                                  "dual_column_dimension": len(local_duals[root]),
                                  "hull_column_dimension": len(local_hulls[root])})
    maximum_mu = max(module_mu(ar, h) for h in local_hulls.values())
    assert maximum_mu == record["maximum_component_hull_mu"]
    negative = {}
    if (ar.q, N, s) in ((4, 3, 0), (8, 7, 1)) and record["case"].startswith("moving_factor_mu4"):
        wrong = {r: (ar.sf(r, -s) if ar.q == 4 else ar.sf(ar.inverse[r], s)) for r in roots}
        wrong_h = {r: ar.restrict(local_inputs[r], local_pair_equations(ar, local_inputs[wrong[r]], s)) for r in roots}
        assert wrong_h != local_hulls
        wrong_mu = max(module_mu(ar, h) for h in wrong_h.values())
        assert wrong_mu != maximum_mu
        negative = {"wrong_rule": "no_reversal" if ar.q == 4 else "forward_instead_of_inverse_Frobenius",
                    "actual_global_hull_maximum_mu": maximum_mu, "wrong_predicted_maximum_mu": wrong_mu,
                    "complete_spaces_differ": True}
    result = {"case": record["case"], "q": ar.q, "n": n, "s": s,
              "original_global_code_dimension": len(global_c), "original_global_dual_dimension": len(global_d),
              "original_global_hull_dimension": len(global_h), "global_hull_maximum_component_mu": maximum_mu,
              "global_hull_matrix_ideal_minimum_generators": (maximum_mu + 1) // 2,
              "full_global_input_dual_hull_spaces_match_reference_under_CRT": True,
              "actual_adjoint_factor_rule_checked": True, "components": component_results,
              "global_code_canonical_basis_sha256": basis_hash(global_c),
              "global_dual_canonical_basis_sha256": basis_hash(global_d),
              "global_hull_canonical_basis_sha256": basis_hash(global_h), "negative_control": negative}
    if record["case"].startswith("same_input_q4_n6"):
        hull_generators = explicit_same_input_hull_generators(ar, n, s)
        generated = ar.canon(ar.expand(polynomial_product(ar, g, a)) for g in hull_generators for a in right_units)
        assert generated == global_h
        assert len(hull_generators) == record["global_hull_matrix_ideal_minimum_generators"]
        result["explicit_hull_generators_original_global_coordinates"] = [ar.expand(g) for g in hull_generators]
        result["original_global_input_generator"] = record["global_generator_field_coordinates"]
        result["global_hull_basis_field_coordinates"] = global_h
        result["explicit_hull_generators_right_ideal_equals_full_global_hull"] = True
    return result


def main(primary_label, audit_label):
    assert primary_label and audit_label
    assert all(c.isalnum() or c in "_-" for c in primary_label + audit_label)
    source = HERE / "results" / primary_label / "cases.jsonl"
    destination = HERE / "results" / audit_label
    assert not destination.exists(), "Refusing to overwrite prior audit evidence"
    destination.mkdir(parents=True)
    try:
        records = [json.loads(line) for line in source.read_text().splitlines()]
        arithmetic, cache, results = {}, {}, []
        for record in records:
            ar = arithmetic.setdefault(record["q"], AuditArithmetic(record["q"]))
            result = audit_case(ar, record, cache)
            results.append(result)
            print("PASS", result["case"], "hull dimension", result["original_global_hull_dimension"],
                  "maximum mu", result["global_hull_maximum_component_mu"], flush=True)
        same = [r for r in results if r["case"].startswith("same_input_q4_n6")]
        assert len(same) == 2
        assert same[0]["original_global_input_generator"] == same[1]["original_global_input_generator"]
        assert same[0]["global_code_canonical_basis_sha256"] == same[1]["global_code_canonical_basis_sha256"]
        assert [r["original_global_hull_dimension"] for r in same] == [12, 4]
        assert [r["global_hull_maximum_component_mu"] for r in same] == [4, 2]
        (destination / "global_cases.jsonl").write_text("".join(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n" for r in results))
        (destination / "same_input_q4_n6_certificates.json").write_text(json.dumps(same, indent=2) + "\n")
        summary = {"status": "PASS", "original_global_matrix_pairing_cases": len(results),
                   "primary_case_stream_sha256": sha(source),
                   "source_hashes": {p.name: sha(p) for p in (HERE / "audit_core_a_independent.py", Path(__file__).resolve())},
                   "no_primary_or_structural_arithmetic_imports": True,
                   "original_cyclic_matrix_product_used_to_generate_codes": True,
                   "all_eight_pairing_field_coordinates_enforced": True,
                   "complete_input_dual_hull_spaces_compared_not_only_dimensions": True,
                   "CRT_linear_map_full_rank_checked_each_field_length": sorted([list(k) for k in cache]),
                   "same_input_q4_n6_code_dimension": 20, "same_input_q4_n6_hull_dimensions_s0_s1": [12, 4],
                   "same_input_q4_n6_hull_matrix_generator_numbers_s0_s1": [2, 1],
                   "same_input_explicit_hull_matrix_generators_checked": True,
                   "negative_controls": [r["negative_control"] for r in results if r["negative_control"]],
                   "all_codes_at_lengths_n_greater_than_2_exhausted": False,
                   "global_case_stream_sha256": sha(destination / "global_cases.jsonl"),
                   "same_input_certificates_sha256": sha(destination / "same_input_q4_n6_certificates.json"),
                   "human_independent_review_completed": False, "external_originality_certified": False,
                   "quantum_or_distance_certificate": False}
        text = json.dumps(summary, indent=2) + "\n"
        (destination / "summary.json").write_text(text)
        (destination / "stdout.txt").write_text(text)
        print(text, end="", flush=True)
    except Exception:
        (destination / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must remain enabled; do not use python -O")
    if len(sys.argv) != 3:
        raise SystemExit("Supply a primary output label and a fresh audit output label")
    main(sys.argv[1], sys.argv[2])
