#!/usr/bin/env python3
"""Separate original-global-pairing audit of every saved q4 structural case.

Uses the unchanged alternative implementation from audit_core_a_independent;
imports NO primary/reference/structural arithmetic or descriptor algorithm.
Also independently builds every exceptional-line candidate at q4,q8,q16 and
checks full global spaces and same-input twist support. No external human
peer review or proof-assistant certification is implied.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import sys
import traceback

from audit_core_a_independent import AuditArithmetic, global_test

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def main(source_label, audit_label):
    assert source_label and audit_label and all(c.isalnum() or c in "_-" for c in source_label + audit_label)
    source = HERE / "results" / source_label
    directory = HERE / "results" / audit_label
    assert not directory.exists(), "Refusing to overwrite evidence"
    directory.mkdir(parents=True)
    try:
        primary_summary = json.loads((source / "summary.json").read_text())
        q4_path = source / "cases_q4.jsonl"
        assert primary_summary["status"] == "PASS"
        assert sha(q4_path) == primary_summary["q4_full_case_stream_sha256"]
        ar = AuditArithmetic(4)
        spaces_by_twist = [set(), set()]
        histograms = [Counter(), Counter()]
        basis_hash = hashlib.sha256()
        exceptional_certificates = []
        count = 0
        for line in q4_path.open():
            record = json.loads(line)
            assert record["field_order"] == 4 and record["twist"] in (0, 1)
            result = global_test(ar, record)
            assert result["local_hull_basis"] == ar.canon(record["hull_basis"])
            basis_hash.update(canonical_json(result).encode())
            s = record["twist"]
            key = ar.canon(record["generators"])
            assert key not in spaces_by_twist[s]
            spaces_by_twist[s].add(key)
            histograms[s][result["hull_mu"]] += 1
            if result["hull_mu"] > 2:
                assert key == result["local_hull_basis"] and record["input_mu"] == 3
                exceptional_certificates.append(result)
            count += 1
        assert count == 2442 and spaces_by_twist[0] == spaces_by_twist[1]
        assert len(spaces_by_twist[0]) == 1221
        assert histograms == [{0: 258, 1: 522, 2: 440, 3: 1}, {0: 130, 1: 538, 2: 550, 3: 3}]
        family_cases = []
        supports = []
        for q in (4, 8, 16):
            ar = AuditArithmetic(q)
            norm_counts = Counter()
            for a in range(1, q):
                generators = [(0, 1, 0, 0, 0, a, 0, 0), (0, 0, 1, 0, 0, 0, a, 0),
                              (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1)]
                observed_support = []
                for s in range(ar.m):
                    isotropic = ar.table[a][ar.sf(a, s)] == 1
                    record = {"generators": generators, "twist": s, "input_mu": 3,
                              "case": f"all_norm_line_candidates_q{q}_a{a}",
                              "global_code_dim_k": 8, "dual_dim_k": 4,
                              "global_hull_dim_k": 8 if isotropic else 4, "hull_mu": 3 if isotropic else 2}
                    result = global_test(ar, record)
                    assert len(result["local_hull_basis"]) == (4 if isotropic else 2)
                    if isotropic:
                        observed_support.append(s)
                        norm_counts[s] += 1
                    family_cases.append({"q": q, "a": a, "twist": s, "hull_mu": result["hull_mu"],
                                         "global_hull_dimension": result["global_hull_dimension"]})
                degree = next(h for h in range(1, ar.m + 1) if ar.sf(a, h) == a)
                if a == 1:
                    expected = list(range(ar.m))
                elif degree % 2 == 0 and ar.table[a][ar.sf(a, degree // 2)] == 1:
                    expected = [s for s in range(ar.m) if s % degree == degree // 2]
                else:
                    expected = []
                assert observed_support == expected
                supports.append({"q": q, "a": a, "minimal_field_degree": degree,
                                 "nonprincipal_twists_for_same_input": observed_support})
            for s in range(ar.m):
                assert norm_counts[s] == math.gcd((1 << s) + 1, q - 1)
        result = {"status": "PASS", "source_q4_cases_sha256": sha(q4_path),
                  "source_structural_summary_sha256": sha(source / "summary.json"),
                  "implementation_source_sha256": {p.name: sha(p) for p in (Path(__file__).resolve(), HERE / "audit_core_a_independent.py")},
                  "primary_reference_or_structural_code_imported": False,
                  "q4_all_embedded_modules_global_checked": 1221,
                  "q4_all_field_twist_cases_full_global_dual_and_hull_spaces": count,
                  "q4_primary_and_independent_hull_bases_equal": True,
                  "q4_hull_mu_histograms": [dict(sorted(h.items())) for h in histograms],
                  "q4_global_basis_stream_sha256": basis_hash.hexdigest(),
                  "all_norm_line_candidate_global_cases_q4_q8_q16": len(family_cases),
                  "norm_root_counts_and_same_input_support_formula_checked": True,
                  "q8_full_generic_census_not_repeated_globally_here": True,
                  "q16_checks_are_named_family_not_full_census": True,
                  "human_independent_review_completed": False, "external_originality_certified": False}
        (directory / "exceptional_q4_certificates.json").write_text(json.dumps(exceptional_certificates, indent=2) + "\n")
        (directory / "norm_line_family_cases.json").write_text(json.dumps(family_cases, indent=2) + "\n")
        (directory / "same_input_twist_supports.json").write_text(json.dumps(supports, indent=2) + "\n")
        text = json.dumps(result, indent=2) + "\n"
        (directory / "summary.json").write_text(text)
        (directory / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        (directory / "FAILURE.txt").write_text(traceback.format_exc())
        raise


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Supply structural output label and fresh audit label")
    main(sys.argv[1], sys.argv[2])
