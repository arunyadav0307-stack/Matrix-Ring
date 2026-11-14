#!/usr/bin/env python3
"""Finite verification; this script does not replace the uniform proof.

Usage: PYTHONDONTWRITEBYTECODE=1 python3 -B verify_core_a.py main_v1
Only new output labels are accepted. All 65,536 q=2 matrices are exhaustive
AUXILIARY cases; q=4,8,16 runs are named controls plus seeded stratified samples.
"""
from pathlib import Path
from collections import Counter
from itertools import product
import csv
import hashlib
import json
import random
import sys
import traceback

from core_a import (Field, add, rref, nullspace, contains, ring_mul, module_span,
                    radical, mu, beta, dual, intersection, sigma_space,
                    act_u, act_w, scale_ring, all_rref_subspaces,
                    all_binary_principal_inputs)

HERE = Path(__file__).resolve().parent
ZERO = (0,) * 8
E1 = (1, 0, 0, 0, 0, 0, 0, 0)
E2 = (0, 0, 0, 0, 1, 0, 0, 0)
U1 = act_u(E1)
U2 = act_u(E2)
W1 = act_w(E1)
W2 = act_w(E2)
Z1 = act_u(W1)
J4 = ((0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0))
SEED = 20261112


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arithmetic_checks(field):
    count = 0
    for a in range(field.q):
        assert field.power(a, field.q) == a
        for b in range(field.q):
            assert field.mul[a][b] == field.mul[b][a]
            for c in range(field.q):
                assert field.mul[field.mul[a][b]][c] == field.mul[a][field.mul[b][c]]
                assert field.mul[a][b ^ c] == (field.mul[a][b] ^ field.mul[a][c])
                count += 2
    for a in range(1, field.q):
        assert field.mul[a][field.inverse[a]] == 1
    for s in range(field.m):
        for a in range(field.q):
            for b in range(field.q):
                assert field.frobenius(field.mul[a][b], s) == field.mul[field.frobenius(a, s)][field.frobenius(b, s)]
                assert field.frobenius(a ^ b, s) == (field.frobenius(a, s) ^ field.frobenius(b, s))
    monomials = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    for a, b, c in product(monomials, repeat=3):
        assert ring_mul(ring_mul(a, b, field), c, field) == ring_mul(a, ring_mul(b, c, field), field)
    assert ring_mul(monomials[1], monomials[1], field) == (0, 0, 0, 0)
    assert ring_mul(monomials[2], monomials[2], field) == (0, 0, 0, 0)
    assert len(rref(J4, field, 4)) == 4
    return {"field_order": field.q, "binary_modulus": bin(field.modulus),
            "associativity_distributivity_triples_checked": count // 2,
            "all_nonzero_inverses_checked": field.q - 1,
            "frobenius_all_pairs_all_twists": True,
            "basis_ring_associativity_and_scalar_gram_rank": "PASS"}


def check_space(space, twist, field, principal_expected=True):
    assert len(space) <= 8
    for v in space:
        assert contains(space, act_u(v), field) and contains(space, act_w(v), field)
    d = dual(space, twist, field)
    h = intersection(space, d, field)
    assert len(d) == 8 - len(space)
    for v in h:
        assert contains(space, v, field) and contains(d, v, field)
    assert dual(d, twist, field) == sigma_space(space, 2 * twist, field)
    # Independent scalar condition within this implementation: actual ell=c_u+c_uw.
    constraints = []
    for v in space:
        row = []
        for i in range(8):
            value = beta(v, tuple(int(i == j) for j in range(8)), twist, field)
            row.append(value[1] ^ value[3])
        constraints.append(row)
    assert nullspace(constraints, field, 8) == d
    input_mu, hull_mu = mu(space, field), mu(h, field)
    if principal_expected:
        assert input_mu <= 2
        assert hull_mu <= 2
    return {"field_order": field.q, "twist": twist,
            "input_dim_k": len(space), "input_mu": input_mu,
            "dual_dim_k": len(d), "hull_dim_k": len(h),
            "hull_radical_dim_k": len(radical(h, field)), "hull_mu": hull_mu,
            "global_code_dim_k": 2 * len(space), "global_hull_dim_k": 2 * len(h)}


def named_cases(field):
    cases = [("zero", [ZERO, ZERO], 0),
             ("whole_ambient", [E1, E2], 0),
             ("one_u_column", [U1, ZERO], 1),
             ("u_identity", [U1, U2], 2),
             ("radical_mixed_columns", [add(U1, W2), add(W1, U2)], None)]
    if field.q >= 4:
        # alpha=2 is nonfixed by at least s=1 for every encoded field here.
        v = (1, 0, 0, 0, 1, 0, 0, 2)
        cases.append(("primitive_socle_norm_growth", [v, ZERO], None))
        cases.append(("nonreflexive_slope", [(1, 0, 0, 0, 2, 0, 0, 0), ZERO], None))
    results = []
    for name, generators, expected in cases:
        space = module_span(generators, field)
        for s in range(field.m):
            item = check_space(space, s, field)
            item.update(case=name, generators=[list(v) for v in generators])
            if expected is not None:
                assert item["hull_mu"] == expected
            if name == "primitive_socle_norm_growth":
                if field.frobenius(2, s) == 2:
                    assert item["hull_mu"] == 1 and item["hull_dim_k"] == 4
                else:
                    assert item["hull_mu"] == 2 and item["hull_dim_k"] == 3
            results.append(item)
    control = module_span([add(U1, U2), add(W1, W2), Z1], field)
    assert mu(control, field) == 3 and len(control) == 4 and len(radical(control, field)) == 1
    old_source = module_span([add(W1, W2), add(add(U1, U2), act_u(W2)),
                             add(add(U1, U2), add(act_u(W1), act_u(W2)))], field)
    assert old_source == control
    for s in range(field.m):
        assert dual(control, s, field) == control
        item = check_space(control, s, field, principal_expected=False)
        item.update(case="known_nonprincipal_input_control", input_outside_principal_class=True,
                    generators=[list(v) for v in (add(U1, U2), add(W1, W2), Z1)])
        results.append(item)
    return results


def exhaustive_auxiliary():
    field = Field(1)
    modules = all_binary_principal_inputs()
    rows = []
    for bits, (multiplicity, first, second) in sorted(modules.items()):
        space = rref([tuple((v >> i) & 1 for i in range(8)) for v in bits], field, 8)
        item = check_space(space, 0, field)
        item.update(matrix_preimages=multiplicity, representative_columns=[first, second],
                    basis=[list(v) for v in space])
        rows.append(item)
    assert sum(r["matrix_preimages"] for r in rows) == 65536
    return rows


def ideal_checks(field):
    total = stable = maximum = 0
    mu_counts = Counter()
    for space in all_rref_subspaces(field, 4):
        total += 1
        images = []
        for a in space:
            images.extend(((0, a[0], 0, a[2]), (0, 0, a[0], a[1])))
        if all(contains(space, v, field, 4) for v in images):
            stable += 1
            generators = len(space) - len(rref(images, field, 4))
            maximum = max(maximum, generators)
            mu_counts[generators] += 1
    assert stable == field.q + 5 and maximum == 2
    return {"field_order": field.q, "all_field_subspaces_of_B_examined": total,
            "ideals_found": stable, "maximum_ideal_mu": maximum,
            "mu_counts": dict(sorted(mu_counts.items()))}


def sampled_cases(field, rng):
    results = []
    categories = ("general", "radical", "one_generator", "primitive_plus_radical", "socle")
    for category in categories:
        for index in range(48):
            if category == "general":
                generators = [tuple(rng.randrange(field.q) for _ in range(8)) for _ in range(2)]
            elif category == "radical":
                generators = [tuple(0 if i in (0, 4) else rng.randrange(field.q) for i in range(8)) for _ in range(2)]
            elif category == "one_generator":
                generators = [tuple(rng.randrange(field.q) for _ in range(8)), ZERO]
            elif category == "primitive_plus_radical":
                v = [rng.randrange(field.q) for _ in range(8)]
                v[0] = 1
                generators = [tuple(v), tuple(0 if i in (0, 4) else rng.randrange(field.q) for i in range(8))]
            else:
                generators = [tuple(rng.randrange(field.q) if i in (3, 7) else 0 for i in range(8)) for _ in range(2)]
            space = module_span(generators, field)
            changed = add(scale_ring((1, 1, 0, 0), generators[0], field), act_w(generators[1]))
            assert module_span([changed, generators[1]], field) == space
            for s in range(field.m):
                item = check_space(space, s, field)
                item.update(category=category, sample_index=index, generators=[list(v) for v in generators])
                results.append(item)
    return results


def negative_controls():
    field = Field(2)
    j = module_span([U1, W1], field)
    socle_rows = [v for v in j if not any(act_u(v)) and not any(act_w(v))]
    # For this named ideal the canonical basis contains the whole one-dimensional socle.
    assert mu(j, field) == 2 and len(socle_rows) == 1
    uline = module_span([U1], field)
    assert mu(uline, field) == 1 and all(v[0] == v[4] == 0 for v in uline)
    wrong_dot_dual = nullspace(uline, field, 8)
    assert wrong_dot_dual != dual(uline, 0, field)
    shape_rejected = False
    try:
        rref([[1] + [0] * 15], field, 8)
    except AssertionError:
        shape_rejected = True
    assert shape_rejected
    f8 = Field(3)
    slope = module_span([(1, 0, 0, 0, 2, 0, 0, 0)], f8)
    dd = dual(dual(slope, 1, f8), 1, f8)
    assert dd == sigma_space(slope, 2, f8) and dd != slope
    return {"mu_not_socle_type": {"ideal_mu": 2, "ideal_socle_dimension": 1},
            "top_not_embedded_residue": {"u_line_mu": 1, "embedded_residue_dimension": 0},
            "ordinary_coordinate_dot_product_gives_different_dual": True,
            "sixteen_coordinate_row_rejected_by_eight_coordinate_api": shape_rejected,
            "q8_s1_double_dual_positive_twist_and_not_original": True,
            "positive_growth_not_nonprincipality": "Named primitive_socle_norm_growth has mu(W)=1, mu(H)=2",
            "all_hulls_principal_false_without_input_hypothesis": "Known control has input_mu=hull_mu=3"}


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    directory = HERE / "results" / label
    assert not directory.exists(), "Refusing to overwrite previous run"
    directory.mkdir(parents=True)
    try:
        arithmetic = [arithmetic_checks(Field(m)) for m in range(1, 5)]
        auxiliary = exhaustive_auxiliary()
        ideals = [ideal_checks(Field(m)) for m in (1, 2)]
        named, sampled = [], []
        rng = random.Random(SEED)
        for m in (2, 3, 4):
            field = Field(m)
            named.extend(named_cases(field))
            sampled.extend(sampled_cases(field, rng))
        controls = negative_controls()
        data = {"arithmetic": arithmetic, "ideals": ideals, "auxiliary_q2": auxiliary,
                "named_core_cases": named, "sampled_core_cases": sampled,
                "negative_controls": controls}
        (directory / "cases.json").write_text(json.dumps(data, indent=2) + "\n")
        csv_fields = ["field_order", "twist", "input_dim_k", "input_mu", "dual_dim_k",
                      "hull_dim_k", "hull_radical_dim_k", "hull_mu", "matrix_preimages",
                      "representative_columns", "basis"]
        with (directory / "auxiliary_q2.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=csv_fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(auxiliary)
        hist = Counter((r["field_order"], r["twist"], r["input_mu"], r["hull_mu"]) for r in sampled)
        summary = {"status": "PASS", "proof_role": "Finite evidence only; universal statement proved separately",
                   "seed": SEED, "python": sys.version,
                   "arithmetic_files_sha256": {p.name: sha(p) for p in (HERE / "core_a.py", Path(__file__).resolve())},
                   "auxiliary_q2": {"all_generator_matrices": 65536, "distinct_principal_input_modules": len(auxiliary),
                                    "all_twists": [0], "outside_core_m_ge_2": True,
                                    "maximum_hull_mu": max(r["hull_mu"] for r in auxiliary)},
                   "core_named_cases_including_out_of_class_controls": len(named),
                   "core_sampled_field_twist_cases": len(sampled),
                   "sampled_generating_matrices_per_q": 240, "sampling_not_exhaustive_for_q4_q8_q16": True,
                   "all_sampled_local_B_scalar_duality_size_and_positive_double_twist_checks": "PASS",
                   "maximum_sampled_hull_mu": max(r["hull_mu"] for r in sampled),
                   "sample_histogram_q_s_inputmu_hullmu": [{"q_s_inputmu_hullmu": list(k), "cases": v} for k, v in sorted(hist.items())],
                   "ideal_exhaustions": ideals, "negative_controls": controls,
                   "cases_sha256": sha(directory / "cases.json"),
                   "independent_human_review": False, "novelty_certified": False}
        text = json.dumps(summary, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        failure = traceback.format_exc()
        (directory / "FAILURE.txt").write_text(failure)
        raise


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh output label")
    main(sys.argv[1])
