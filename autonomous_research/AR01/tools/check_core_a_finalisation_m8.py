#!/usr/bin/env python3
"""M8 document/preservation/result integrity, NOT mathematical proof checking.

Supply a fresh receipt label. Read-only except for that new evidence JSON.
Assertions must be enabled. No installs, repository changes or network calls.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "autonomous_research/AR01"
FINAL = RUN / "finalisation/M8"
COMPUTATIONS = RUN / "computations"
RESULTS = COMPUTATIONS / "results"
BASE = "c4f170dffbb6c6a99b7ae2339851ea3d29039022"
BRANCH = "arena/7d88376d-matrix-ring"
SIX = ["CORE_A_CLOSED_FORMULA_THEOREM.md", "CORE_A_CLOSED_FORMULA_FULL_PROOF.md",
       "CORE_A_INDEPENDENT_PROOF_AUDIT.md", "CORE_A_EXCEPTIONAL_CASES_REGISTER.md",
       "CORE_A_THEORY_COMPUTATION_COMPARISON.md", "CORE_A_PROOF_STATUS_REPORT.md"]
LOGS = ["GIT_PROGRESS_LOG.md", "RESEARCH_PROGRESS_LOG.md",
        "PHASE_COMPLETION_REGISTER.md", "FINAL_CHANGELOG.md"]
APPEND_ONLY = {"autonomous_research/AR01/README.md",
               "autonomous_research/AR01/computations/README.md", *LOGS}
PAIRS = [("foundations", "main_v1"), ("foundations_audit", "audit_v1"),
         ("structure", "structure_v1"), ("structure_global", "structure_global_v1"),
         ("distribution", "distribution_v1"), ("distribution_audit", "distribution_audit_v1"),
         ("proof", "closed_formula_proof_v1"), ("scalar_qc", "scalar_qc_v1"),
         ("split_boundary", "split_resumed_v1"),
         ("split_global_boundary", "split_global_resumed_v1")]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(path.read_bytes())


def load(path):
    return json.loads(path.read_text())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def require_prefix(current, previous):
    assert current.startswith(previous), "Old content was changed, not appended"


def verify_records(records):
    for row in records:
        path = ROOT / row["path"]
        assert path.is_file(), path
        assert path.stat().st_size == row["bytes"], path
        assert digest(path) == row["sha256"], path


def check_gate(gate, ledger):
    assert gate["statement_sha256"] == ledger["statement_sha256"]
    assert gate["proof_sha256"] == ledger["proof_sha256"]
    assert gate["independent_complete_proof_scrutiny"] == "NOT_ESTABLISHED"
    for key in ("candidate_formula_and_hypotheses_changed",
                "independent_human_review_completed", "complete_formal_proof_certificate",
                "unqualified_proved_status_authorized", "novelty_cleared",
                "sufficient_paper_depth_established", "submission_ready",
                "requested_independent_proof_terminal_condition_reached"):
        assert gate[key] is False, key
    assert gate["same_agent_line_scrutiny_completed"] is True
    assert gate["identified_unresolved_internal_mathematical_implications"] == []
    assert [(b["id"], b["status"]) for b in gate["proof_verification_blockers"]] == [("RB01", "OPEN")]
    assert [(b["id"], b["status"]) for b in gate["primary_source_blockers"]] == [
        (f"NL{i:02}", "OPEN") for i in range(1, 5)]
    assert gate["fresh_executed_runs"] == 11
    assert gate["fresh_q16_full_generic_structural_cases"] == 666084


def check_units(proof_bytes, ledger):
    assert sha(proof_bytes) == ledger["proof_sha256"]
    lines = proof_bytes.decode().splitlines()
    starts = [(i + 1, m.group(1)) for i, line in enumerate(lines)
              if (m := re.match(r"### (P\d\d)\.", line))]
    assert [u for _, u in starts] == [f"P{i:02}" for i in range(1, 31)]
    assert len(ledger["units"]) == 30 and len(lines) == ledger["proof_lines"]
    expected = []
    for i, ((start, unit), row) in enumerate(zip(starts, ledger["units"])):
        end = starts[i + 1][0] - 1 if i + 1 < len(starts) else len(lines)
        assert row["unit"] == unit and row["lines"] == [start, end]
        assert sha(("\n".join(lines[start - 1:end]) + "\n").encode()) == row["block_sha256"]
        assert all(dep in [u for _, u in starts[:i]] for dep in row["prior_unit_dependencies"])
        assert row["genuinely_independent_scrutiny"] == "NOT_ESTABLISHED"
        expected.append((unit, start, end))
    assert ledger["unqualified_proved_status_authorized"] is False
    return expected


def check_audit_ranges(text, expected):
    recorded = [("P" + u, int(a), int(b))
                for u, a, b in re.findall(r"\|P(\d\d),(\d+)–(\d+)\|", text)]
    assert recorded == expected


# Exact integer-coefficient polynomials in q,Q,d,U,F; this verifies assembly
# only. It does not prove the enumeration or check each logical proof step.
ZERO_KEY = (0,) * 5


def constant(n):
    return {ZERO_KEY: n} if n else {}


def plus(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, 0) + value
    return {k: v for k, v in out.items() if v}


def negative(poly):
    return {k: -v for k, v in poly.items()}


def times(*polys):
    out = constant(1)
    for poly in polys:
        nxt = {}
        for k, a in out.items():
            for l, b in poly.items():
                p = tuple(x + y for x, y in zip(k, l))
                nxt[p] = nxt.get(p, 0) + a * b
        out = {k: v for k, v in nxt.items() if v}
    return out


def assembly_identity():
    one, two, three = constant(1), constant(2), constant(3)
    q, Q, d, U, F = [{tuple(int(i == j) for i in range(5)): 1} for j in range(5)]
    q2, q3, q4, Q2 = times(q, q), times(q, q, q), times(q, q, q, q), times(Q, Q)
    a = times(plus(q, one), plus(times(two, q2), q, one))
    G = plus(q4, times(three, q3), times(constant(4), q2), times(three, q), constant(5))
    L = plus(times(two, q4), times(constant(8), q3), times(constant(10), q2),
             times(constant(7), q), constant(9))
    n0 = plus(times(plus(q, one, negative(d)), q3), two)
    n1 = plus(times(two, a),
              times(d, plus(q3, negative(times(two, q2)), negative(times(Q2, plus(q, negative(Q)))))),
              times(plus(q, three), U), negative(F))
    n2 = plus(G, times(d, plus(times(two, q2), times(Q2, plus(q, negative(Q))), negative(one))),
              negative(times(plus(q, three), U)), F)
    difference = plus(n0, n1, n2, d, negative(L))
    assert not difference
    assert plus(difference, one), "An intentionally wrong constant must not pass"


def main(label):
    assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", label)
    destination = RUN / "evidence" / (label + ".json")
    assert not destination.exists(), "Refusing to overwrite an integrity receipt"
    assert git("branch", "--show-current").decode().strip() == BRANCH
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT, check=True)

    # Every original, all frozen M5 inputs and all frozen M8 inputs remain
    # exact. The permitted current READMEs/logs may only gain a suffix.
    initial = load(RUN / "evidence/INITIAL_PRESERVATION.json")
    verify_records(initial["files"])
    m5 = load(RUN / "evidence/M5_FINALISATION_INPUT_MANIFEST.json")
    verify_records(m5["existing_uncommitted_input_files"])
    baseline = load(RUN / "evidence/M8_FINALISATION_BASELINE.json")
    assert len(baseline["files"]) == 166
    assert sum(r["bytes"] for r in baseline["files"]) == 13021961
    appended = []
    for row in baseline["files"]:
        previous = git("show", BASE + ":" + row["path"])
        assert len(previous) == row["bytes"] and sha(previous) == row["sha256"]
        current = (ROOT / row["path"]).read_bytes()
        if row["path"] in APPEND_ONLY:
            require_prefix(current, previous)
            if current != previous:
                appended.append(row["path"])
        else:
            assert current == previous, row["path"]
    for name in LOGS:
        require_prefix((ROOT / name).read_bytes(), git("show", BASE + ":" + name))

    inventory = load(RUN / "evidence/M8_INPUT_INVENTORY_V1.json")
    assert inventory["baseline_manifest_sha256"] == digest(RUN / "evidence/M8_FINALISATION_BASELINE.json")
    assert [{k: r[k] for k in ("path", "bytes", "sha256")} for r in inventory["frozen_AR01_files"]] == baseline["files"]
    legacy = inventory["legacy_content_groups"]
    assert len(legacy) == 12 and sum(len(g["paths"]) for g in legacy) == 93
    for group in legacy:
        for name in group["paths"]:
            assert digest(ROOT / name) == group["sha256"], name
    pdfs = load(RUN / "evidence/M8_LOCAL_PDF_SCOPE_V1.json")
    assert pdfs["deduplicated_pdf_count"] == len(pdfs["sources"]) == 10
    assert sum("pages" in row for row in pdfs["sources"]) == 9
    assert sum(bool(row.get("first_page_header")) for row in pdfs["sources"]) == 8
    assert sum("extraction_error" in row for row in pdfs["sources"]) == 1
    for row in pdfs["sources"]:
        assert digest(ROOT / row["representative"]) == row["sha256"]
        for name in row.get("all_copy_paths", []):
            assert digest(ROOT / name) == row["sha256"], name
    reading = load(RUN / "evidence/M8_SOURCE_READING_SCOPE_V1.json")
    assert reading["full_S01_S09_or_primary_geometry_article_acquired"] is False
    acquisitions = load(RUN / "evidence/M8_SOURCE_ACQUISITION_V1.json")
    assert len(acquisitions["sources"]) == 2 and len(reading["sources"]) == 3
    for acquired, read in zip(acquisitions["sources"], reading["sources"]):
        assert all(acquired[key] == read[key] for key in ("repository", "path", "blob_sha", "sha256"))
        assert read["full_technical_paper_read"] is False
        assert read["primary_or_final_version_authenticated"] is False
    supplied = reading["sources"][-1]
    assert supplied["id"] == "S10" and digest(ROOT / supplied["path"]) == supplied["pdf_sha256"]
    assert digest(ROOT / supplied["technical_extraction_path"]) == supplied["technical_extraction_sha256"]

    for name in SIX:
        assert (FINAL / name).is_file()
    ledger = load(FINAL / "CORE_A_PROOF_OBLIGATIONS.json")
    gate = load(FINAL / "CORE_A_GATE_STATUS.json")
    statement = (FINAL / SIX[0]).read_text()
    assert digest(FINAL / SIX[0]) == ledger["statement_sha256"]
    previous = (RUN / "phase3" / SIX[0]).read_text()
    assert statement.split("## T1.", 1)[1].split("\n## M8 provenance", 1)[0].rstrip() == previous.split("## T1.", 1)[1].rstrip()
    proof_bytes = (FINAL / SIX[1]).read_bytes()
    expected = check_units(proof_bytes, ledger)
    audit = (FINAL / SIX[2]).read_text()
    check_audit_ranges(audit, expected)
    assert ledger["statement_sha256"] in audit and ledger["proof_sha256"] in audit
    check_gate(gate, ledger)
    exception_ids = re.findall(r"\|EX(\d\d)\|", (FINAL / SIX[3]).read_text())
    assert exception_ids == [f"{i:02}" for i in range(1, 39)]
    links = 0
    for path in sorted(FINAL.glob("*.md")):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target.split("#", 1)[0]).is_file(), (path, target)
                links += 1
    assembly_identity()

    # Genuine finite reruns, with exact fresh/predecessor identities. This
    # receipt verifies files, not how many minutes ago an execution occurred.
    comparison = load(RUN / "evidence/M8_REGRESSION_COMPARISON_V1.json")
    assert len(comparison["fresh_reruns"]) == 10
    summaries = []
    compared_files = 0
    for (short, old), record in zip(PAIRS, comparison["fresh_reruns"]):
        fresh = "finalisation_m8_" + short + "_v1"
        assert record["fresh_label"] == fresh and record["preserved_predecessor"] == old
        names = sorted(p.name for p in (RESULTS / fresh).iterdir() if p.is_file())
        assert names == sorted(p.name for p in (RESULTS / old).iterdir() if p.is_file())
        assert names == [r["file"] for r in record["files"]]
        for row in record["files"]:
            left, right = RESULTS / fresh / row["file"], RESULTS / old / row["file"]
            assert left.read_bytes() == right.read_bytes()
            assert digest(left) == row["fresh_sha256"] == row["preserved_predecessor_sha256"]
            assert row["byte_identical"] is True
            compared_files += 1
        summaries.append((fresh, load(RESULTS / fresh / "summary.json")))
    assert compared_files == 39
    new = comparison["additional_new_standalone_run"]
    assert new["label"] == "finalisation_m8_directed_flags_v1" and new["not_a_rerun"] is True
    assert len(new["files"]) == 4
    for name, h in new["files"].items():
        assert digest(RESULTS / new["label"] / name) == h
    directed = load(RESULTS / new["label"] / "summary.json")
    summaries.append((new["label"], directed))
    assert directed["directed_two_plane_flags_checked"] == 101316
    assert directed["hermitian_graph_matrices_checked"] == 304
    assert directed["nonreflexive_wrong_direction_witnesses"] == 4
    assert directed["repository_code_imports"] == []
    assert digest(COMPUTATIONS / "audit_core_a_directed_flags.py") == directed["source_sha256"]
    absent_historical_review_flags = []
    for fresh, summary in summaries:
        assert summary["status"] == "PASS"
        if "human_independent_review_completed" in summary:
            assert summary["human_independent_review_completed"] is False
        else:
            absent_historical_review_flags.append(fresh)
        for key in ("source_hashes", "arithmetic_files_sha256", "implementation_source_sha256"):
            for name, h in summary.get(key, {}).items():
                assert digest(COMPUTATIONS / name) == h, (fresh, key, name)
        if "audit_script_sha256" in summary:
            assert digest(COMPUTATIONS / "audit_core_a_independent.py") == summary["audit_script_sha256"]
        for name, h in summary.get("input_hashes", {}).items():
            assert digest(COMPUTATIONS / name) == h, (fresh, name)
    for name, h in directed["output_hashes"].items():
        assert digest(RESULTS / new["label"] / name) == h
    imports = {}
    for p in sorted(COMPUTATIONS.glob("*.py")):
        tree = ast.parse(p.read_text())
        imports[p.name] = sorted({n.module for n in ast.walk(tree)
                                  if isinstance(n, ast.ImportFrom) and n.module
                                  and (COMPUTATIONS / (n.module + ".py")).is_file()})
    assert imports == inventory["local_computation_import_dependencies"]

    # In-memory deliberate corruptions only; never mutate scientific files.
    negatives = []
    def must_reject(name, callback):
        try:
            callback()
        except AssertionError:
            negatives.append(name)
        else:
            raise AssertionError("Validator accepted deliberate corruption: " + name)
    wrong = deepcopy(gate)
    wrong["unqualified_proved_status_authorized"] = True
    must_reject("unearned proved-status promotion", lambda: check_gate(wrong, ledger))
    must_reject("modified proof bytes", lambda: check_units(proof_bytes + b" ", ledger))
    must_reject("wrong audit line range", lambda: check_audit_ranges(
        audit.replace(f"|P01,{expected[0][1]}–{expected[0][2]}|", "|P01,1–2|", 1), expected))
    must_reject("replacement instead of append", lambda: require_prefix(b"changed", b"original"))
    ast.parse(Path(__file__).read_text())

    result = {
        "status": "PASS", "session_calendar_utc": "2026-11-12",
        "raw_environment_observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "timestamp_kind": "Raw sandbox observation is not the session calendar or publication date",
        "branch": BRANCH, "base_commit": BASE,
        "head_at_check": git("rev-parse", "HEAD").decode().strip(),
        "intake_originals_verified": len(initial["files"]),
        "intake_original_bytes_verified": sum(r["bytes"] for r in initial["files"]),
        "frozen_M5_input_files_verified": len(m5["existing_uncommitted_input_files"]),
        "M8_baseline_files_verified": len(baseline["files"]),
        "M8_baseline_permitted_append_only_paths": appended,
        "root_progress_logs_original_prefixes_verified": LOGS,
        "legacy_content_groups_and_paths_verified": [len(legacy), 93],
        "PDF_unique_hashes_metadata_headers_and_failures": [10, 9, 8, 1],
        "new_source_acquisition_and_reading_scope_crosslinks_verified": True,
        "all_six_required_successors_exist": True,
        "documents": {str(p.relative_to(ROOT)): {"sha256": digest(p), "lines": len(p.read_text().splitlines())}
                      for p in sorted(FINAL.iterdir()) if p.is_file()},
        "proof_units_and_audit_line_ranges": expected,
        "proof_block_hashes_and_prior_unit_dependencies_match": True,
        "candidate_statement_T1_T5_byte_unchanged": True,
        "local_document_links_checked": links,
        "exact_five_variable_N2_assembly_identity": True,
        "unchanged_rerun_result_files_verified": compared_files,
        "new_standalone_result_files_verified": 4,
        "run_source_input_and_output_hashes_verified": True,
        "historical_summaries_omitting_human_review_flag": absent_historical_review_flags,
        "absent_flags_not_treated_as_independent_review_evidence": True,
        "computational_import_dependency_graph_unchanged": True,
        "in_memory_negative_controls_rejected": negatives,
        "checker_sha256": digest(Path(__file__)),
        "unqualified_proved_status_authorized": False,
        "independent_complete_proof_acceptance_established": False,
        "external_originality_certified": False,
        "scope": "Document/range/hash/link, baseline/prefix/result/source integrity, exact assembly only. NOT a logical proof checker, independent review, execution attestation or novelty certificate."
    }
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must be enabled; do not use -O")
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh M8 integrity receipt label")
    main(sys.argv[1])
