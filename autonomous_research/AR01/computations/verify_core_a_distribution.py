#!/usr/bin/env python3
"""A13 formula checks and a NEW full q16 generic/structural census.

Old q2/q4/q8 census summaries are read as attributed comparison data, not
reported as newly rerun. All 166,521 q16 modules and all four twists are
actually checked here. Bulk records are deterministically hashed; a fixed
subset plus every exceptional case is saved for the separate global audit.
Sources/results of the old runs are not modified. No -O; use a fresh label.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys
import traceback

from core_a import Field, dual, intersection, mu, module_span
from verify_core_a_structure import descriptors, structural_hull, compact
from core_a_distribution import distribution

HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    directory = HERE / "results" / label
    assert not directory.exists(), "Refusing to overwrite prior evidence"
    directory.mkdir(parents=True)
    source_bytes = Path(__file__).read_bytes()
    try:
        old_path = HERE / "results/structure_v1/summary.json"
        old = json.loads(old_path.read_text())
        assert old["status"] == "PASS"
        predictions = []
        for row in old["field_results"]:
            m = row["q"].bit_length() - 1
            for s, histogram in enumerate(row["hull_mu_counts_by_twist"]):
                prediction = distribution(m, s)
                assert prediction["hull_mu_counts"] == {int(k): v for k, v in histogram.items()}
                predictions.append(prediction)
        field = Field(4)
        seen = set()
        histograms = [Counter() for _ in range(4)]
        kind_counts = Counter()
        kinds_mu_one = [Counter() for _ in range(4)]
        stream = hashlib.sha256()
        selected = []
        for index, (space, descriptor) in enumerate(descriptors(field)):
            assert space not in seen
            seen.add(space)
            assert module_span(space, field) == space
            kind_counts[descriptor["kind"]] += 1
            input_mu = mu(space, field)
            for s in range(4):
                structural, expected_input_mu, expected_hull_mu = structural_hull(space, descriptor, s, field)
                d = dual(space, s, field)
                h = intersection(space, d, field)
                assert structural == h
                assert expected_input_mu == input_mu
                actual_mu = mu(h, field)
                assert actual_mu == expected_hull_mu <= 3
                histograms[s][actual_mu] += 1
                if actual_mu == 1:
                    if descriptor["kind"] == "radical":
                        key = "K_line" if len(descriptor["K"]) == 1 else "K_V"
                        assert len(descriptor["K"]) in (1, 2)
                    else:
                        key = "primitive"
                        assert descriptor["kind"] == "primitive"
                    kinds_mu_one[s][key] += 1
                record = {"case": f"A13_q16_{descriptor['kind']}_{index}", "field_order": 16,
                          "twist": s, "case_index": index, "generators": space,
                          "input_dim_k": len(space), "input_mu": input_mu,
                          "dual_basis": d, "dual_dim_k": len(d), "hull_basis": h,
                          "hull_dim_k": len(h), "hull_mu": actual_mu,
                          "global_code_dim_k": 2 * len(space), "global_hull_dim_k": 2 * len(h)}
                stream.update(compact(record).encode())
                if index % 4096 == 0 or actual_mu > 2:
                    selected.append(record)
            if (index + 1) % 20000 == 0:
                print(f"q16: {index + 1} distinct embedded inputs checked, every twist", flush=True)
        assert len(seen) == distribution(4, 0)["all_embedded_input_modules"] == 166521
        q16 = []
        for s in range(4):
            prediction = distribution(4, s)
            assert dict(histograms[s]) == prediction["hull_mu_counts"]
            assert kinds_mu_one[s] == {"primitive": prediction["mu_one_primitive_inputs"],
                                       "K_line": prediction["mu_one_radical_K_line_inputs"],
                                       "K_V": prediction["mu_one_K_equals_V_inputs"]}
            predictions.append(prediction)
            q16.append({"s": s, "observed_hull_mu_counts": dict(sorted(histograms[s].items())),
                        "observed_mu_one_input_strata": dict(kinds_mu_one[s])})
        (directory / "formula_predictions.json").write_text(json.dumps(predictions, indent=2) + "\n")
        (directory / "q16_global_audit_cases.jsonl").write_text("".join(compact(r) for r in selected))
        summary = {"status": "PASS", "old_census_comparison_summary_sha256": sha(old_path),
                   "q2_q4_q8_censuses_read_as_old_evidence_not_new_execution": True,
                   "new_q16_all_embedded_modules": len(seen), "new_q16_all_twists": [0, 1, 2, 3],
                   "new_q16_generic_and_structural_full_space_cases": len(seen) * 4,
                   "all_q16_generic_and_structural_hull_bases_equal": True,
                   "q16_kind_counts": dict(kind_counts), "q16_observations": q16,
                   "q16_all_case_stream_sha256_not_bulk_stored": stream.hexdigest(),
                   "q16_selected_original_global_audit_cases": len(selected),
                   "selected_global_cases_sha256": sha(directory / "q16_global_audit_cases.jsonl"),
                   "source_hashes": {p.name: sha(p) for p in (HERE / "core_a.py", HERE / "verify_core_a_structure.py", HERE / "core_a_distribution.py", Path(__file__).resolve())},
                   "separate_global_and_incidence_audit_required": True,
                   "external_originality_certified": False, "human_independent_review_completed": False,
                   "full_joint_same_input_all_twist_distribution_claimed": False}
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
        raise SystemExit("Do not disable assertions with -O")
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh output label")
    main(sys.argv[1])
