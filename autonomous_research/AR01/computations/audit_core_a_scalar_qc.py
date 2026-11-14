#!/usr/bin/env python3
"""Check the exact A-valued index-2 QC reduction; not a Gray/field isometry.

Fresh scalar coordinate implementation; reuses only the alternative audit's
field tables, row restriction and original-global checker. No primary B-module
or descriptor/hull code is imported. All q4 and selected q16 records are data.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys
import traceback

from audit_core_a_independent import AuditArithmetic, global_test, plus, units

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rho(v):
    # Four A entries, time-block order, each expanded as constant,u coefficients.
    # c0+cu*u+cw*w+cz*u*w = (c0+cw)+(cu+cz)*u + X*(cw+cz*u).
    return (v[0] ^ v[2], v[1] ^ v[3], v[4] ^ v[6], v[5] ^ v[7],
            v[2], v[3], v[6], v[7])


def un_rho(v):
    return (v[0] ^ v[4], v[1] ^ v[5], v[4], v[5],
            v[2] ^ v[6], v[3] ^ v[7], v[6], v[7])


def nilpotent(v):
    return tuple(c for i in range(0, 8, 2) for c in (0, v[i]))


def shift(v):
    return v[4:] + v[:4]


def scalar_pair(ar, x, y, s):
    constant, nil = 0, 0
    for j in range(0, 8, 2):
        a, b = ar.sf(x[j], s), ar.sf(x[j + 1], s)
        constant ^= ar.table[a][y[j]]
        nil ^= ar.table[a][y[j + 1]] ^ ar.table[b][y[j]]
    return constant, nil


def scalar_qc_space(ar, generators):
    rows = []
    for v in generators:
        x = rho(v)
        rows.extend((x, nilpotent(x), shift(x), nilpotent(shift(x))))
    return ar.canon(rows)


def scalar_qc_dual_hull(ar, space, s):
    equations = []
    for x in space:
        values = [scalar_pair(ar, x, y, s) for y in units(8)]
        equations.extend(tuple(value[i] for value in values) for i in range(2))
    return ar.restrict(units(8), equations), ar.restrict(space, equations)


def scalar_transport_checks(ar):
    count = 0
    for x in units(8):
        assert un_rho(rho(x)) == x
        assert rho(un_rho(x)) == x
        for scalar in (1, 2):
            v = ar.vscale(scalar, x)
            for y in units(8):
                for s in range(ar.m):
                    sigma = tuple(ar.sf(a, s) for a in v)
                    beta = plus(ar.bmul(sigma[:4], y[:4]), ar.bmul(sigma[4:], y[4:]))
                    # Constant and X coefficients in A of the full B-valued product.
                    b_constant = (beta[0] ^ beta[2], beta[1] ^ beta[3])
                    b_x = (beta[2], beta[3])
                    assert scalar_pair(ar, rho(v), rho(y), s) == b_constant
                    assert scalar_pair(ar, shift(rho(v)), rho(y), s) == b_x
                    count += 1
    return count


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    destination = HERE / "results" / label
    assert not destination.exists(), "Refusing to overwrite evidence"
    destination.mkdir(parents=True)
    source = Path(__file__).read_bytes()
    try:
        arithmetic = {q: AuditArithmetic(q) for q in (4, 8, 16)}
        transport = sum(scalar_transport_checks(ar) for ar in arithmetic.values())
        inputs = [HERE / "results/structure_v1/cases_q4.jsonl",
                  HERE / "results/distribution_v1/q16_global_audit_cases.jsonl"]
        histograms = {0: Counter(), 1: Counter()}
        scope, complete_dual_records, stream = Counter(), 0, hashlib.sha256()
        for p in inputs:
            for line in p.read_text().splitlines():
                record = json.loads(line)
                q, s = record["field_order"], record["twist"]
                ar = arithmetic[q]
                Q = scalar_qc_space(ar, record["generators"])
                D, H = scalar_qc_dual_hull(ar, Q, s)
                assert len(D) == 8 - len(Q)
                assert 2 * len(Q) == record["global_code_dim_k"]
                assert 2 * len(H) == record["global_hull_dim_k"]
                for space in (Q, D, H):
                    assert ar.canon([*space, *(nilpotent(v) for v in space), *(shift(v) for v in space)]) == space
                h_local = ar.canon(un_rho(v) for v in H)
                assert h_local == ar.canon(record["hull_basis"])
                if "dual_basis" in record:
                    assert ar.canon(un_rho(v) for v in D) == ar.canon(record["dual_basis"])
                    complete_dual_records += 1
                radical = ar.canon([*(nilpotent(v) for v in H), *(plus(v, shift(v)) for v in H)])
                mu = len(H) - len(radical)
                assert mu == record["hull_mu"]
                actual_global = global_test(ar, record)
                assert actual_global["local_hull_basis"] == h_local
                scope[q] += 1
                if q == 4:
                    histograms[s][mu] += 1
                out = {"q": q, "s": s, "sample_index": record.get("sample_index"),
                       "qc_input_dimension_k": len(Q), "qc_dual_dimension_k": len(D),
                       "qc_hull_basis": H, "qc_minimum_module_generators": mu,
                       "original_global_hull_basis": actual_global["global_hull_basis"]}
                stream.update((json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n").encode())
        assert scope == {4: 2442, 16: 176}
        assert histograms[0] == {0: 258, 1: 522, 2: 440, 3: 1}
        assert histograms[1] == {0: 130, 1: 538, 2: 550, 3: 3}
        result = {"status": "PASS", "scope": "Exact scalar A-valued QC reduction at central length2 only; not a Gray/field/quantum isometry or novelty test",
                  "scalar_pair_constant_and_shift_basis_checks": transport,
                  "complete_all_q4_scalar_QC_and_original_global_cases": scope[4],
                  "selected_q16_scalar_QC_and_original_global_cases": scope[16],
                  "recorded_primary_complete_dual_spaces_compared": complete_dual_records,
                  "all_scalar_QC_hull_and_original_global_spaces_equal": True,
                  "u_and_QC_shift_closure_of_inputs_duals_and_hulls": True,
                  "all_minimum_QC_module_generator_counts_match": True,
                  "q4_hull_generator_histograms": {s: dict(sorted(c.items())) for s, c in histograms.items()},
                  "full_basis_stream_sha256_hash_only": stream.hexdigest(),
                  "input_hashes": {str(p.relative_to(HERE)): sha(p) for p in inputs},
                  "source_hashes": {p.name: sha(p) for p in (HERE / "audit_core_a_independent.py", Path(__file__).resolve())},
                  "no_primary_field_module_descriptor_hull_code_imports": True,
                  "human_independent_review_completed": False, "external_originality_certified": False}
        text = json.dumps(result, indent=2) + "\n"
        (destination / "summary.json").write_text(text)
        (destination / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        (destination / "FAILURE_SOURCE.py").write_bytes(source)
        (destination / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must stay enabled")
    if len(sys.argv) != 2:
        raise SystemExit("Supply one fresh result label")
    main(sys.argv[1])
