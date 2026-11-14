#!/usr/bin/env python3
"""Verify the embedded-layer/graph formulas against generic B-valued hulls.

Exhaustively construct ALL embedded inputs at auxiliary q2 and core q4,q8
using the proved descriptor (not arbitrary 8-dimensional RREF exhaustion).
Every resulting module is deduplicated and its generic dual/hull compared
with the structural reconstruction for every twist. q4 cases are saved in
compact JSONL for the separate original-global-pairing checker; q8 complete
case data are hashed in generation order rather than stored as a large set.

Usage: python3 -B verify_core_a_structure.py FRESH_LABEL
Standard library only; do not use -O (verification uses assertions).
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import sys
import traceback

from core_a import (Field, add, rref, nullspace, intersection, ring_mul,
                    module_span, mu, hull, dual, all_rref_subspaces)

HERE = Path(__file__).resolve().parent
B_UNITS = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
V_UNITS = ((1, 0), (0, 1))
Z = (0, 0, 0, 1)
J_BASIS = B_UNITS[1:]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True) + "\n"


def combo(coefficients, vectors, field, width):
    out = [0] * width
    for c, v in zip(coefficients, vectors):
        for i, a in enumerate(v):
            out[i] ^= field.mul[c][a]
    return tuple(out)


def socle(c):
    return (0, 0, 0, c[0], 0, 0, 0, c[1])


def radical_vector(a, b, c):
    return (0, a[0], b[0], c[0], 0, a[1], b[1], c[1])


def lines(field):
    return [basis[0] for basis in all_rref_subspaces(field, 2) if len(basis) == 1]


def scalar_ideals(field):
    yield "zero", ()
    yield "socle", (Z,)
    for a, b in lines(field):
        yield "line", rref([(0, a, b, 0), Z], field, 4)
    yield "radical", J_BASIS


def radical_descriptors(field):
    for k in all_rref_subspaces(field, 2):
        d = len(k)
        pivots = [next(i for i, a in enumerate(v) if a) for v in k]
        quotient_positions = [i for i in range(2) if i not in pivots]
        for t_coords in all_rref_subspaces(field, 2 * d):
            t_original = [combo(v[:d], k, field, 2) + combo(v[d:], k, field, 2)
                          for v in t_coords]
            for coefficients in product(range(field.q), repeat=len(t_original) * (2 - d)):
                graph = []
                for i, t in enumerate(t_original):
                    f = [0, 0]
                    for j, position in enumerate(quotient_positions):
                        f[position] = coefficients[i * (2 - d) + j]
                    graph.append(t + tuple(f))
                # Canonical T basis with the corresponding quotient representative of f.
                graph = rref(graph, field, 6)
                t = tuple(v[:4] for v in graph)
                f = tuple(v[4:] for v in graph)
                generators = [radical_vector(v[:2], v[2:], c) for v, c in zip(t, f)]
                generators.extend(socle(c) for c in k)
                space = rref(generators, field, 8)
                yield space, {"kind": "radical", "K": k, "T": t, "f": f}


def primitive_descriptors(field):
    for chart, residue in [(0, a) for a in range(field.q)] + [(1, 0)]:
        for kind, ideal in scalar_ideals(field):
            pivots = [next(i for i, a in enumerate(v) if a) for v in ideal]
            free = [i for i in (1, 2, 3) if i not in pivots]
            for coefficients in product(range(field.q), repeat=len(free)):
                t = [residue, 0, 0, 0]
                for i, c in zip(free, coefficients):
                    t[i] = c
                t = tuple(t)
                v = B_UNITS[0] + t if chart == 0 else t + B_UNITS[0]
                generators = [v]
                generators.extend(((0, 0, 0, 0) + j if chart == 0 else j + (0, 0, 0, 0))
                                  for j in ideal)
                space = module_span(generators, field)
                yield space, {"kind": "primitive", "chart": chart, "I_kind": kind, "I": ideal, "t": t}


def descriptors(field):
    yield from radical_descriptors(field)
    yield from primitive_descriptors(field)
    yield tuple(tuple(int(i == j) for i in range(8)) for j in range(8)), {"kind": "ambient"}


def projection_sum(t, field):
    return rref([v[:2] for v in t] + [v[2:] for v in t], field, 2)


def scalar_mu(basis, field):
    radical = rref([ring_mul(b, v, field) for b in B_UNITS[1:3] for v in basis], field, 4)
    return len(basis) - len(radical)


def structural_hull(space, descriptor, s, field):
    kind = descriptor["kind"]
    if kind == "ambient":
        return (), 2, 0
    if kind == "radical":
        k, t, f = descriptor["K"], descriptor["T"], descriptor["f"]
        equations = [tuple(field.frobenius(a, s) for a in v[2:] + v[:2]) for v in t]
        ts = intersection(t, nullspace(equations, field, 4), field, 4)
        pivots = [next(i for i, a in enumerate(v) if a) for v in t]
        hs = [radical_vector(v[:2], v[2:], combo([v[p] for p in pivots], f, field, 2)) for v in ts]
        hs.extend(socle(c) for c in k)
        result = rref(hs, field, 8)
        expected_input_mu = len(t) + len(k) - len(projection_sum(t, field))
        expected_hull_mu = len(ts) + len(k) - len(projection_sum(ts, field))
        return result, expected_input_mu, expected_hull_mu
    t, ideal = descriptor["t"], descriptor["I"]
    st = tuple(field.frobenius(a, s) for a in t)
    si = rref([tuple(field.frobenius(a, s) for a in v) for v in ideal], field, 4)
    n = add(B_UNITS[0], ring_mul(t, st, field))
    ideal_kind = descriptor["I_kind"]
    if ideal_kind == "zero":
        if n[0]:
            l, expected_hull_mu = (), 0
        elif not any(n):
            l, expected_hull_mu = B_UNITS, 1
        elif not (n[1] or n[2]):
            l, expected_hull_mu = J_BASIS, 2
        else:
            l, expected_hull_mu = rref([(0, n[1], n[2], 0), Z], field, 4), 1
    elif ideal_kind == "socle":
        l, expected_hull_mu = ((Z,), 1) if n[0] else (J_BASIS, 2)
    elif ideal_kind == "line":
        l = intersection(ideal, si, field, 4) if n[0] else si
        expected_hull_mu = 1
    else:
        assert ideal_kind == "radical"
        l, expected_hull_mu = (Z,), 1
    assert scalar_mu(l, field) == expected_hull_mu
    rows = [(ring_mul(st, b, field) + b if descriptor["chart"] == 0 else b + ring_mul(st, b, field)) for b in l]
    return rref(rows, field, 8), 1 + scalar_mu(ideal, field), expected_hull_mu


def exceptional_inputs(field, s):
    result = {}
    for a in range(1, field.q):
        if field.power(a, (1 << s) + 1) == 1:
            generators = [(0, 1, 0, 0, 0, a, 0, 0),
                          (0, 0, 1, 0, 0, 0, a, 0), socle((1, 0)), socle((0, 1))]
            result[module_span(generators, field)] = a
    return result


def verify_field(field, directory, q4_stream, binary_audit):
    seen = set()
    kind_counts, input_counts, histograms = Counter(), Counter(), [Counter() for _ in range(field.m)]
    exceptional = [exceptional_inputs(field, s) for s in range(field.m)]
    observed_exceptional = [set() for _ in range(field.m)]
    stream_hash = hashlib.sha256()
    for index, (space, descriptor) in enumerate(descriptors(field)):
        assert space not in seen, (field.q, descriptor)
        seen.add(space)
        assert module_span(space, field) == space
        kind_counts[descriptor["kind"]] += 1
        input_mu = mu(space, field)
        input_counts[input_mu] += 1
        for s in range(field.m):
            predicted, input_predicted, mu_predicted = structural_hull(space, descriptor, s, field)
            actual_dual = dual(space, s, field)
            actual = intersection(space, actual_dual, field)
            assert predicted == actual
            assert input_predicted == input_mu and mu(actual, field) == mu_predicted
            assert (mu_predicted > 2) == (space in exceptional[s])
            if mu_predicted > 2:
                assert actual == actual_dual == space and input_mu == mu_predicted == 3
                observed_exceptional[s].add(space)
            histograms[s][mu_predicted] += 1
            record = {"case": f"descriptor_q{field.q}_{descriptor['kind']}_{index}",
                      "field_order": field.q, "twist": s, "case_index": index,
                      "descriptor": descriptor, "generators": space,
                      "input_dim_k": len(space), "input_mu": input_mu,
                      "dual_dim_k": len(actual_dual), "hull_dim_k": len(actual), "hull_mu": mu_predicted,
                      "global_code_dim_k": 2 * len(space), "global_hull_dim_k": 2 * len(actual),
                      "hull_basis": actual}
            text = compact(record)
            stream_hash.update(text.encode())
            if field.q == 4:
                q4_stream.write(text)
    q = field.q
    total = 2 * q**4 + 8 * q**3 + 10 * q**2 + 7 * q + 9
    assert len(seen) == total
    assert kind_counts["radical"] == q**4 + 5 * q**3 + 7 * q**2 + 5 * q + 7
    assert input_counts == {0: 1, 1: q**4 + 3 * q**3 + 2 * q**2 + q + 1,
                            2: q**4 + 4 * q**3 + 7 * q**2 + 3 * q + 3,
                            3: q**3 + q**2 + 3 * q + 3, 4: 1}
    for s, histogram in enumerate(histograms):
        d = math.gcd((1 << s) + 1, q - 1)
        assert observed_exceptional[s] == set(exceptional[s])
        assert histogram[3] == d
        assert histogram[0] == (q + 1 - d) * q**3 + 2
        assert max(histogram) == 3
    if q == 2:
        expected = {tuple(tuple((v >> i) & 1 for i in range(8)) for v in rec["basis_bits_low_pivots"])
                    for rec in binary_audit}
        assert seen == expected
        (directory / "modules_q2.json").write_text(compact(sorted(seen)))
    if q == 4:
        # Historical values are comparison controls, not the source of this census.
        assert histograms == [{0: 258, 1: 522, 2: 440, 3: 1}, {0: 130, 1: 538, 2: 550, 3: 3}]
    return {"q": q, "auxiliary_outside_m_ge_2": q == 2,
            "all_embedded_modules": len(seen), "all_twists_tested": list(range(field.m)),
            "field_twist_cases": len(seen) * field.m, "kind_counts": dict(kind_counts),
            "input_mu_counts": dict(sorted(input_counts.items())),
            "hull_mu_counts_by_twist": [dict(sorted(h.items())) for h in histograms],
            "complete_stream_sha256_in_deterministic_generation_order": stream_hash.hexdigest(),
            "all_generic_and_structural_hull_bases_equal": True,
            "all_nonprincipal_inputs_and_LCD_counts_match_proved_formulas": True,
            "q2_all_spaces_match_separate_ambient_subspace_audit": q == 2}


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    directory = HERE / "results" / label
    assert not directory.exists(), "Refusing to overwrite prior evidence"
    directory.mkdir(parents=True)
    try:
        binary_path = HERE / "results/audit_v1/binary_all_modules.json"
        binary = json.loads(binary_path.read_text())
        fields = []
        with (directory / "cases_q4.jsonl").open("w") as stream:
            for m in (1, 2, 3):
                fields.append(verify_field(Field(m), directory, stream, binary))
        summary = {"status": "PASS", "proof_role": "Exhaustive finite checks of a separately written uniform theorem, not a proof substitute",
                   "field_results": fields, "q4_full_case_stream_sha256": digest(directory / "cases_q4.jsonl"),
                   "source_hashes": {p.name: digest(p) for p in (HERE / "core_a.py", Path(__file__).resolve())},
                   "separate_binary_audit_input_sha256": digest(binary_path),
                   "q16_exhaustion_not_run": True, "q8_all_case_stream_stored_as_hash_only": True,
                   "external_originality_certified": False, "human_independent_review_completed": False}
        text = json.dumps(summary, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh output label")
    main(sys.argv[1])
