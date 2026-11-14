#!/usr/bin/env python3
"""Exact named certificates for the explicitly fully split length-2N family.

Core A arithmetic supplies the reference component duals. The next, separate
checker reconstructs the original global cyclic right ideal and matrix-valued
pairing from the exported polynomial generator, with alternative field tables.
Not an exhaustive code census at n>2; not a novelty or quantum certificate.
"""
from pathlib import Path
import hashlib
import json
import sys
import traceback

from core_a import Field, module_span, mu, dual, intersection

HERE = Path(__file__).resolve().parent
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
U = (0, 1, 0, 0)
W = (0, 0, 1, 0)
Z = (0, 0, 0, 1)
IDENTITY = (ONE, ZERO, ZERO, ONE)
U_IDENTITY = (U, ZERO, ZERO, U)
Z_IDENTITY = (Z, ZERO, ZERO, Z)
P_MATRIX = (ONE, ZERO, ONE, Z)
Q_MATRIX = (U, (0, 0, 1, 1), U, W)
ZERO_MATRIX = (ZERO,) * 4


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inverse_crt(matrices, roots, N, field):
    n = 2 * N
    answer = [[0] * 8 for _ in range(n)]
    for root in roots:
        matrix = matrices[root]
        for j in range(N):
            factor = field.power(field.inverse[root], 2 * j)
            for entry, (c0, cu, cw, cz) in enumerate(matrix):
                answer[2 * j][2 * entry] ^= field.mul[factor][c0 ^ cw]
                answer[2 * j][2 * entry + 1] ^= field.mul[factor][cu ^ cz]
                answer[(2 * j + N) % n][2 * entry] ^= field.mul[factor][cw]
                answer[(2 * j + N) % n][2 * entry + 1] ^= field.mul[factor][cz]
    return tuple(a for coefficient in answer for a in coefficient)


def component_data(matrices, roots, N, s, field, delta_override=None):
    spaces = {r: module_span([matrices[r][0] + matrices[r][2], matrices[r][1] + matrices[r][3]], field) for r in roots}
    delta = {r: field.frobenius(field.inverse[r], -s) for r in roots} if delta_override is None else delta_override
    assert set(delta.values()) == set(roots)
    data = []
    for r in roots:
        d = dual(spaces[delta[r]], s, field)
        h = intersection(spaces[r], d, field)
        data.append({"root": r, "source_root_for_dual": delta[r], "input_matrix": matrices[r],
                     "input_basis": spaces[r], "dual_basis": d, "hull_basis": h,
                     "input_mu": mu(spaces[r], field), "hull_mu": mu(h, field)})
    return data


def make_case(name, matrices, roots, N, s, field, expected_mu):
    data = component_data(matrices, roots, N, s, field)
    assert all(r["input_mu"] <= 2 for r in data)
    hull_mu = max(r["hull_mu"] for r in data)
    assert hull_mu == expected_mu
    return {"case": name, "q": field.q, "N": N, "n": 2 * N, "twist": s,
            "roots": roots, "components": data,
            "global_generator_field_coordinates": inverse_crt(matrices, roots, N, field),
            "global_code_dim_k": 2 * sum(len(r["input_basis"]) for r in data),
            "global_dual_dim_k": 2 * sum(len(r["dual_basis"]) for r in data),
            "global_hull_dim_k": 2 * sum(len(r["hull_basis"]) for r in data),
            "maximum_component_hull_mu": hull_mu,
            "global_hull_matrix_ideal_minimum_generators": (hull_mu + 1) // 2,
            "all_factors_self_coupled": N and ((1 << s) + 1) % N == 0}


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    directory = HERE / "results" / label
    assert not directory.exists(), "Refusing to overwrite evidence"
    directory.mkdir(parents=True)
    try:
        cases, permutations, negatives = [], [], {}
        for degree, odd_parts in ((2, (1, 3)), (3, (1, 7)), (4, (1, 3, 5, 15))):
            field = Field(degree)
            for N in odd_parts:
                roots = [a for a in range(1, field.q) if field.power(a, N) == 1]
                assert len(roots) == N and N % 2 == 1
                for s in range(field.m):
                    delta = {r: field.frobenius(field.inverse[r], -s) for r in roots}
                    all_fixed = all(r == delta[r] for r in roots)
                    assert all_fixed == (((1 << s) + 1) % N == 0)
                    permutations.append({"q": field.q, "N": N, "s": s, "delta_target_to_source": delta,
                                         "criterion_N_divides_2s_plus_1": all_fixed})
                    matrices = {r: ZERO_MATRIX for r in roots}
                    if all_fixed:
                        matrices = {r: U_IDENTITY for r in roots}
                        cases.append(make_case(f"self_coupled_control_q{field.q}_N{N}_s{s}", matrices, roots, N, s, field, 2))
                    else:
                        r = next(r for r in roots if delta[r] != r)
                        other = delta[r]
                        matrices[r], matrices[other] = IDENTITY, Z_IDENTITY
                        cases.append(make_case(f"moving_factor_mu4_q{field.q}_N{N}_s{s}", matrices, roots, N, s, field, 4))
                        wrong_forward = {a: field.frobenius(field.inverse[a], s) for a in roots}
                        wrong_no_reversal = {a: field.frobenius(a, -s) for a in roots}
                        if field.q == 8 and N == 7 and s == 1:
                            wrong = component_data(matrices, roots, N, s, field, wrong_forward)
                            assert max(x["hull_mu"] for x in wrong) != 4
                            negatives["inverse_not_forward_frobenius_permutation_detected_q8_N7_s1"] = True
                        if field.q == 4 and N == 3 and s == 0:
                            wrong = component_data(matrices, roots, N, s, field, wrong_no_reversal)
                            assert max(x["hull_mu"] for x in wrong) != 4
                            negatives["omitting_reversal_detected_q4_N3_s0"] = True
                        matrices = {a: ZERO_MATRIX for a in roots}
                        matrices[r], matrices[other] = P_MATRIX, Q_MATRIX
                        cases.append(make_case(f"moving_factor_mu3_q{field.q}_N{N}_s{s}", matrices, roots, N, s, field, 3))
        # One identical polynomial code, compared across twists rather than reselected.
        field = Field(2)
        roots = [1, 2, 3]
        matrices = {1: ZERO_MATRIX, 2: IDENTITY, 3: Z_IDENTITY}
        same = [make_case(f"same_input_q4_n6_s{s}", matrices, roots, 3, s, field, expected)
                for s, expected in ((0, 4), (1, 2))]
        assert same[0]["global_generator_field_coordinates"] == same[1]["global_generator_field_coordinates"]
        expected_coefficients = ((1, 1), (0, 2), (2, 3), (0, 1), (3, 2), (0, 3))
        expected_generator = tuple(a for scalar in expected_coefficients for a in scalar + (0, 0, 0, 0) + scalar)
        assert same[0]["global_generator_field_coordinates"] == expected_generator
        assert same[0]["global_code_dim_k"] == same[1]["global_code_dim_k"] == 20
        assert [x["global_hull_dim_k"] for x in same] == [12, 4]
        cases.extend(same)
        text = "".join(json.dumps(c, sort_keys=True, separators=(",", ":")) + "\n" for c in cases)
        (directory / "cases.jsonl").write_text(text)
        (directory / "factor_permutations.json").write_text(json.dumps(permutations, indent=2) + "\n")
        summary = {"status": "PASS", "named_field_length_twist_cases": len(cases),
                   "coverage": {"q4_N": [1, 3], "q8_N": [1, 7], "q16_N": [1, 3, 5, 15], "all_twists_for_each_listed_family": True},
                   "all_code_census_at_larger_lengths": False,
                   "actual_inverse_frobenius_reversal_factor_rule": "PASS",
                   "negative_controls": negatives,
                   "same_q4_n6_input_maximum_component_hull_mu_s0_s1": [4, 2],
                   "same_q4_n6_input_hull_matrix_generator_numbers_s0_s1": [2, 1],
                   "same_q4_n6_input_code_dimension": 20, "same_q4_n6_input_hull_dimensions_s0_s1": [12, 4],
                   "case_stream_sha256": sha(directory / "cases.jsonl"),
                   "source_hashes": {p.name: sha(p) for p in (HERE / "core_a.py", Path(__file__).resolve())},
                   "global_original_pairing_audit_required_separately": True,
                   "external_originality_certified": False, "human_independent_review_completed": False,
                   "quantum_or_distance_certificate": False}
        out = json.dumps(summary, indent=2) + "\n"
        (directory / "summary.json").write_text(out)
        (directory / "stdout.txt").write_text(out)
        print(out, end="")
    except Exception:
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh output label")
    main(sys.argv[1])
