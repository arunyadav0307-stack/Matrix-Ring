#!/usr/bin/env python3
"""Build a curated, immutable Phase 0 review ZIP; file operations only, no mathematics executes.

Must be launched from the Matrix-Ring repository root. All outputs are NEW files.
The saved preexisting_snapshot.json is the before-packaging baseline.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
import csv
import datetime as dt
import difflib
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import quote
import zipfile

ROOT = Path.cwd().resolve()
WORK = Path(__file__).resolve().parent
AUDIT = ROOT / "phase0_audit"
PRIOR = AUDIT / "extracted/prior_project"
NAME = "PHASE0_COMPLETE_AUDIT_PACKAGE"
OUT = AUDIT / NAME
ARCHIVE = AUDIT / (NAME + ".zip")
SIDECAR = AUDIT / (NAME + ".zip.sha256")
DELIVERY = AUDIT / (NAME + "_VERIFICATION.txt")
BASELINE = json.loads((WORK / "preexisting_snapshot.json").read_text())
REPORT_NAMES = (
    "PHASE0_REPOSITORY_AUDIT.md", "PHASE0_LITERATURE_REVIEW.md",
    "PHASE0_RING_FEASIBILITY.md", "PHASE0_PAIRING_OPTIONS.md",
    "PHASE0_RESEARCH_GAP.md", "PHASE0_DECISION_REPORT.md",
)
for target in (OUT, ARCHIVE, SIDECAR, DELIVERY):
    if target.exists():
        raise SystemExit("Refusing to overwrite existing output: " + str(target))
if BASELINE["branch"] != "arena/7d88376d-matrix-ring":
    raise SystemExit("Unexpected branch; no operations performed.")
if subprocess.check_output(["git", "branch", "--show-current"], text=True).strip() != BASELINE["branch"]:
    raise SystemExit("Current branch changed; refusing to proceed.")

payload = {}
roles = {}
source_map = {}
provenance = []
by_digest = {}
new_docs = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def txt(path, content, role="Packaging documentation"):
    if path in payload:
        raise RuntimeError("Duplicate new package destination: " + path)
    payload[path] = content.encode("utf-8") if isinstance(content, str) else content
    roles[path] = role
    return path


def csv_bytes(rows, fields):
    f = io.StringIO(newline="")
    writer = csv.DictWriter(f, fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return f.getvalue().encode("utf-8")


def source(path, destination, role, force=False):
    path = path.resolve()
    if not path.is_file() or path.is_symlink():
        raise RuntimeError("Required source file unavailable: " + str(path))
    rel = path.relative_to(ROOT).as_posix()
    data = path.read_bytes()
    digest = sha(data)
    actual = destination if force or digest not in by_digest else by_digest[digest]
    if actual == destination:
        txt(destination, data, role)
        by_digest.setdefault(digest, destination)
    source_map[rel] = actual
    provenance.append({"source_path": rel, "package_path": actual, "bytes": len(data),
                       "sha256": digest, "handling": "COPY" if actual == destination else "DEDUPLICATED_ALIAS",
                       "role": role})
    return actual


def check_originals():
    errors = []
    count = 0
    for row in BASELINE["files"]:
        p = ROOT / row["path"]
        if row["kind"] == "symlink":
            if not p.is_symlink() or p.readlink().as_posix() != row["target"]:
                errors.append(row["path"])
        elif not p.is_file() or p.is_symlink() or sha(p.read_bytes()) != row["sha256"]:
            errors.append(row["path"])
        count += 1
    diff = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], text=True)
    staged = subprocess.check_output(["git", "diff", "--cached", "--name-only"], text=True)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    if errors or diff or staged or head != BASELINE["head"]:
        raise RuntimeError("Originals changed: " + json.dumps({"paths": errors, "diff": diff, "staged": staged, "head": head}))
    return {"status": "PASS", "preexisting_entries_checked": count, "changed_or_missing_entries": errors,
            "head": head, "branch": BASELINE["branch"], "tracked_diff": diff, "staged_diff": staged}


check_originals()

# The six mandatory reports are never edited or reformatted.
for name in REPORT_NAMES:
    source(AUDIT / name, "reports/" + name, "Mandatory completed Phase 0 report, verbatim", force=True)

# Keep the published reproducibility unit intact so its active manifest remains directly usable.
research_files = sorted(p for p in (ROOT / "research-data").rglob("*") if p.is_file())
for p in research_files:
    source(p, "computational_evidence/" + p.relative_to(ROOT).as_posix(),
           "Previously supplied reproducibility data; historical evidence, not newly executed", force=True)
for p in sorted((AUDIT / "evidence").glob("*")):
    if p.is_file():
        source(p, "computational_evidence/current_phase0/" + p.name,
               "Existing current Phase 0 re-execution evidence, verbatim")

# Mathematical source dependency closure relevant to the completed Phase 0 conclusions.
for directory in ("00_BLUEPRINT", "02_PHASE_REPORTS/Phase_0", "03_THEOREMS"):
    for p in sorted((PRIOR / directory).rglob("*")):
        if p.is_file() and p.suffix in {".md", ".txt"}:
            source(p, "mathematical_evidence/prior_project/" + p.relative_to(PRIOR).as_posix(),
                   "Historical mathematical derivation/proof or Phase 0 context; source status labels retained")
for p in sorted((PRIOR / "06_AUDIT").glob("*.md")):
    if p.name not in {"Phase0_audit_request.md", "Phase0_revision_audit_request.md"}:
        source(p, "mathematical_evidence/prior_project/" + p.relative_to(PRIOR).as_posix(),
               "Historical proof/computational audit or decision record, not a fresh certification")
for name in ("PHASE1_COMPLETION_AND_APPROVAL_GATE.md", "PHASE2_PROPOSAL.md", "PHASE2_PROPOSAL_v2.md", "PROJECT_DECISION_LOG.md"):
    source(PRIOR / name, "mathematical_evidence/prior_project/" + name,
           "Historical definition/dependency/decision record referenced by proof sources")

# The prior computation tree is byte-identical to the curated data in most cases.
# Add only its distinct documentation; record all duplicate scripts/logs as aliases.
for p in sorted((PRIOR / "04_COMPUTATION").glob("*")):
    if p.is_file():
        source(p, "computational_evidence/prior_project/04_COMPUTATION/" + p.name,
               "Historical script/log/documentation supporting report claims")
for rel in (
    "PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv",
    "PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_CERTIFICATION_METHOD_AUDIT.md",
    "PHASE17_RESEARCHER_DECISION/PHASE17_CERTIFICATION_LOGIC.md",
    "PHASE17_RESEARCHER_DECISION/PHASE17_REFEREE_METHOD_NOTE.md",
):
    source(PRIOR / rel, "computational_evidence/prior_project/" + rel,
           "Historical distance-method applicability and certification interpretation")

for p in sorted((PRIOR / "01_LITERATURE").glob("*")):
    if p.is_file():
        source(p, "literature_evidence/prior_project/01_LITERATURE/" + p.name,
               "Inherited bibliography/comparison with its original verification qualifications")
for name in ("LITERATURE_VERIFICATION.md", "NOVELTY_COMPARISON.md"):
    source(PRIOR / "PAPER" / name, "literature_evidence/prior_project/PAPER/" + name,
           "Historical literature verification/positioning record; not independently re-verified now")

# Third-party papers occur once, as the exact supplied PDFs; do not repack the source ZIP.
pdfs = sorted((AUDIT / "extracted/literature/Matrix Ring 1").glob("*.pdf"))
if len(pdfs) != 7:
    raise RuntimeError("Expected seven supplied literature PDFs")
with zipfile.ZipFile(ROOT / "Matrix Ring 1.zip") as supplied:
    for p in pdfs:
        if p.read_bytes() != supplied.read("Matrix Ring 1/" + p.name):
            raise RuntimeError("Supplied PDF extraction mismatch: " + p.name)
        target = source(p, "literature_evidence/supplied_pdfs/" + p.name,
                        "User-supplied third-party PDF, private review only; no redistribution licence granted")
        loose = ROOT / p.name
        if loose.is_file() and sha(loose.read_bytes()) == sha(p.read_bytes()):
            source(loose, "literature_evidence/loose_duplicates/" + p.name,
                   "Loose PDF duplicate; one archive copy retained")

# One canonical manuscript source and only the byte-distinct latest-staging deltas.
# No build, submission, or manuscript edit occurs.
source(ROOT / "README.md", "repository_integrity/source_identity/root_README.md", "Original repository identity stub")
source(PRIOR / "README.md", "repository_integrity/prior_work/README.md", "Prior project identity and status record")
for p in [PRIOR / "PAPER/main.tex", PRIOR / "PAPER/references.bib", *sorted((PRIOR / "PAPER/sections").glob("*.tex"))]:
    source(p, "repository_integrity/prior_work/" + p.relative_to(PRIOR).as_posix(),
           "Existing canonical manuscript source, unmodified; historical identity/evidence")
for p in [PRIOR / "PAPER/FFA_FINAL_SUBMISSION_V2/main.tex", PRIOR / "PAPER/FFA_FINAL_SUBMISSION_V2/references.bib",
          *sorted((PRIOR / "PAPER/FFA_FINAL_SUBMISSION_V2/sections").glob("*.tex"))]:
    source(p, "repository_integrity/prior_work/" + p.relative_to(PRIOR).as_posix(),
           "Latest prior staging source; unchanged shared files are deduplicated to canonical sources")
for name in ("README.md", "CONTRIBUTION_MAP.md", "CLAIM_TRACEABILITY_MATRIX.md", "OPEN_ISSUES_AND_LIMITATIONS.md", "FINAL_VALIDATION_REPORT.md"):
    source(PRIOR / "PAPER" / name, "repository_integrity/prior_work/PAPER/" + name,
           "Historical manuscript identification/claim traceability/limitations record")
for p in sorted((PRIOR / "PHASE23_FFA_FINALIZATION").glob("*.md")):
    source(p, "repository_integrity/prior_work/" + p.relative_to(PRIOR).as_posix(),
           "Prior submission-preparation/data-availability status, not evidence of submission")
source(AUDIT / "extracted/patch_binary_files.txt", "repository_integrity/patch_binary_files.txt",
       "Existing list of unrecovered patch binary-only paths")
source(WORK / "preexisting_snapshot.json", "repository_integrity/preexisting_snapshot.json",
       "Before-packaging file/SHA-256 snapshot of every pre-existing worktree file excluding .git")
source(WORK / "verify_package.py", "repository_integrity/package_tools/verify_package.py",
       "Read-only standalone checksum/structure verifier, packaging only")
source(Path(__file__), "repository_integrity/package_tools/build_package.py",
       "Assembly/provenance script for this package, packaging only")

# Every tracked file is also compared to its HEAD blob, without writing Git objects.
tracked_rows = []
for entry in subprocess.check_output(["git", "ls-tree", "-rz", "HEAD"]).split(b"\0"):
    if not entry:
        continue
    metadata, rawpath = entry.split(b"\t", 1)
    mode, kind, object_id = metadata.decode().split()
    rel = rawpath.decode()
    data = (ROOT / rel).read_bytes()
    computed = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if computed != object_id:
        raise RuntimeError("Tracked file differs from HEAD blob: " + rel)
    tracked_rows.append({"path": rel, "mode": mode, "HEAD_git_blob_sha1": object_id,
                         "working_tree_sha256": sha(data), "bytes": len(data), "status": "MATCH_HEAD"})
txt("repository_integrity/tracked_files_vs_HEAD.csv", csv_bytes(tracked_rows, list(tracked_rows[0])),
    "All tracked originals compared byte-for-byte via Git blob hashes")
txt("repository_integrity/git_status_before.txt", BASELINE["git_status_before"], "Pre-packaging Git status")
txt("repository_integrity/original_files_inventory.csv", csv_bytes([
    {"path": r["path"], "bytes": r.get("bytes", ""), "sha256": r.get("sha256", ""), "kind": r["kind"]}
    for r in BASELINE["files"]], ["path", "bytes", "sha256", "kind"]), "Inventory of all pre-existing original/audit files")

# Inventories of omitted containers preserve evidence without redundant ZIP/patch copies.
zip_rows = []
for n in ("Matrix Ring.zip", "Matrix Ring 1.zip"):
    with zipfile.ZipFile(ROOT / n) as z:
        for i in z.infolist():
            zip_rows.append({"source_archive": n, "entry": i.filename, "directory": i.is_dir(),
                             "bytes": i.file_size, "CRC32": format(i.CRC, "08x"),
                             "sha256": "" if i.is_dir() else sha(z.read(i.filename))})
txt("repository_integrity/original_zip_inventories.csv", csv_bytes(zip_rows, list(zip_rows[0])),
    "Contents and checksums of the source ZIPs (empty stub included as inventory only)")

# Validate the selected recovered sources against the original patch's added lines.
patch = ROOT / "01a1a47c-f51d-7d7c-810c-207359de606f.patch"
patch_bytes = patch.read_bytes()
patch_rows = []
selected_patch_checks = []
selected = {p["source_path"].removeprefix("phase0_audit/extracted/prior_project/")
            for p in provenance if p["source_path"].startswith("phase0_audit/extracted/prior_project/")}
for section in re.split(rb"(?m)^diff --git ", patch_bytes)[1:]:
    lines = section.splitlines(keepends=True)
    head = lines[0].decode("utf-8", errors="replace").rstrip()
    match = re.search(r" b/(.*)$", head)
    if not match:
        raise RuntimeError("Unsupported patch header: " + head)
    rel = match.group(1)
    binary = any(line.startswith((b"Binary files ", b"GIT binary patch")) for line in lines[1:8])
    recovered = PRIOR / rel
    patch_rows.append({"prior_path": rel, "diff_kind": "BINARY_ONLY" if binary else "TEXT_DIFF",
                       "recovered_in_workspace": recovered.is_file(), "selected_for_review": rel in selected})
    if rel in selected and not binary:
        result = []
        in_hunk = False
        for line in lines[1:]:
            if line.startswith(b"@@"):
                in_hunk = True
                continue
            if not in_hunk:
                continue
            if line.startswith((b"+", b" ")):
                result.append(line[1:])
            elif line.startswith(b"\\ No newline") and result:
                result[-1] = result[-1].rstrip(b"\r\n")
        raw = b"".join(result)
        data = recovered.read_bytes()
        status = "EXACT_BYTES" if raw == data else "NEWLINE_NORMALIZED" if raw.replace(b"\r\n", b"\n") == data else "MISMATCH"
        selected_patch_checks.append({"prior_path": rel, "raw_added_lines_sha256": sha(raw),
                                      "recovered_source_sha256": sha(data), "status": status})
        if status == "MISMATCH":
            raise RuntimeError("Recovered selected source differs from patch: " + rel)
txt("repository_integrity/patch_diff_inventory.csv", csv_bytes(patch_rows, list(patch_rows[0])),
    "All patch file-diff paths; no unrelated file payloads included")
txt("repository_integrity/selected_patch_reconstruction_checks.csv",
    csv_bytes(selected_patch_checks, list(selected_patch_checks[0])), "Patch-to-selected-text provenance checks")

# Both inherited manifests are checked; the older one uses a previous flat layout.
manifest_rows = []
for manifest_name in ("PUBLICATION_MANIFEST.sha256", "documentation/MANIFEST.sha256"):
    for line in (ROOT / "research-data" / manifest_name).read_text().splitlines():
        digest, rel = line.split("  ", 1)
        actual = "research-data/" + rel
        if manifest_name.startswith("documentation/"):
            actual = {"README.md": "research-data/documentation/SUPPLEMENTARY_PACKAGE_README.md",
                      "CERTIFICATION_PROCEDURE.md": "research-data/verification_procedures/CERTIFICATION_PROCEDURE.md",
                      "ENVIRONMENT.md": "research-data/verification_procedures/ENVIRONMENT.md"}.get(rel, actual)
            if rel.startswith("parameter_tables/"):
                name = Path(rel).name
                actual = "research-data/" + ("distance_certificates/" if name == "certified_codes.csv" else "quantum_code_records/") + name
        status = "PASS" if (ROOT / actual).is_file() and sha((ROOT / actual).read_bytes()) == digest else "FAIL"
        if status != "PASS":
            raise RuntimeError("Inherited manifest failure: " + rel)
        manifest_rows.append({"source_manifest": manifest_name, "original_manifest_path": rel,
                              "resolved_source_path": actual, "package_path": source_map[actual],
                              "expected_sha256": digest, "status": status,
                              "layout": "CURRENT_DIRECT" if manifest_name == "PUBLICATION_MANIFEST.sha256" else "HISTORICAL_LAYOUT_RESOLVED"})
txt("repository_integrity/inherited_manifest_verification.csv", csv_bytes(manifest_rows, list(manifest_rows[0])),
    "87 active and 85 older-layout manifest entries resolved and hash-checked")

# Packaging-time analysis of artifacts only: no execution of research scripts.
original_stdout = (ROOT / "research-data/logs/phase0_stdout.txt").read_text().splitlines()
rerun_stdout = (AUDIT / "evidence/phase0_feasibility_rerun_2026-11-12.txt").read_text().splitlines()
changes = []
for i, (a, b) in enumerate(zip(original_stdout, rerun_stdout), 1):
    if a != b:
        changes.append({"line": i, "recorded": a, "rerun": b})
if len(original_stdout) != len(rerun_stdout) or len(changes) != 3:
    raise RuntimeError("Unexpected existing rerun comparison; inspect sources")
txt("computational_evidence/current_phase0/RERUN_COMPARISON.json",
    json.dumps({"comparison_performed_during_packaging": True, "research_script_rerun_during_packaging": False,
                "recorded_log_lines": len(original_stdout), "rerun_log_lines": len(rerun_stdout),
                "differing_lines": changes, "all_other_lines_equal": True,
                "scope": "Same-script reproducibility evidence, not independent mathematical validation."}, indent=2) + "\n")
script_rows = []
local_names = {p.stem for p in (ROOT / "research-data/scripts").glob("*.py")}
for p in sorted((ROOT / "research-data/scripts").glob("*.py")):
    tree = ast.parse(p.read_text(), filename=str(p))
    deps = set()
    for node in ast.walk(tree):
        names = ([node.module] if isinstance(node, ast.ImportFrom) and node.module else
                 [n.name for n in node.names] if isinstance(node, ast.Import) else [])
        deps.update(n.split(".")[0] for n in names if n.split(".")[0] in local_names)
    script_rows.append({"script": p.name, "syntax_parsed": "PASS", "executed_in_packaging": False,
                        "local_imports_json": json.dumps(sorted(deps)), "dependencies_packaged": True})
txt("computational_evidence/SCRIPT_DEPENDENCIES.csv", csv_bytes(script_rows, list(script_rows[0])),
    "Static script syntax/import dependency check; no mathematical computations run")

pdf_metadata = {
    "2602.18255v1 (1).pdf": ("Construction of cyclic codes over a class of matrix rings", "Soham Ravikant Joshi; Shikha Patel; Om Prakash", "2026", "arXiv:2602.18255v1", "10.48550/arXiv.2602.18255", "Preprint supplied; later publication not checked"),
    "s11128-026-05230-0 (3).pdf": ("Quantum codes construction from cyclic codes over matrix rings", "Soham Ravikant Joshi; Shikha Patel; Om Prakash", "2026", "Quantum Information Processing 25, article 207; Springer Nature", "10.1007/s11128-026-05230-0", "Version of record supplied; publisher-search metadata available from prior session"),
    "s12095-022-00572-9 (3).pdf": ("Cyclic codes over M4(F2 + uF2)", "Shikha Patel; Om Prakash; Habibul Islam", "2022 (copyright/front matter)", "Cryptography and Communications; Springer", "10.1007/s12095-022-00572-9", "Supplied journal PDF; final volume/pages not independently checked"),
    "s12190-018-01235-w (1).pdf": ("Cyclic codes over M4(F2)", "Joydeb Pal; Sanjit Bhowmick; Satya Bagchi", "2019", "Journal of Applied Mathematics and Computing 60, 749-756; Springer", "10.1007/s12190-018-01235-w", "Supplied journal PDF"),
    "s13226-021-00014-x (2).pdf": ("On the structure of cyclic codes over M2(Fp + uFp)", "Habibul Islam; Om Prakash; Dipak Kumar Bhunia", "2021", "INSA/Springer journal PDF; complete citation needs external confirmation", "10.1007/s13226-021-00014-x", "Supplied corrected journal PDF; journal title/volume/pages not newly verified"),
    "algebraic-structure-of-cyclic-codes-over-m3fp.pdf": ("Algebraic structure of cyclic codes over M3(Fp)", "Habibul Islam; Om Prakash; Dipak Kumar Bhunia", "Not confirmed", "Not confirmed", "", "Title/authors from supplied PDF; DOI/venue/year unconfirmed"),
    "Construction_of_Codes_Over_mathbbF_p3_from_Cyclic_Codes_Over_mathscrM_3leftmathbbF_pu_mathbbF_pu2_mathbbF_pright.pdf": ("Construction of Codes Over Fp3 From Cyclic Codes Over M3(Fp + uFp + u2Fp)", "Shikha Patel; Soham Ravikant Joshi; Om Prakash", "Not confirmed", "Not confirmed (conference-style supplied PDF)", "", "Title/authors from supplied PDF; DOI/venue/year unconfirmed"),
}
pdf_rows = []
excerpts = ["# Supplied PDF front-matter excerpts\n\nMechanical excerpts from the text extraction already produced during Phase 0. The supplied PDF is authoritative for symbols and layout. These excerpts are not fresh DOI resolutions and are not full-text substitutes.\n"]
for p in pdfs:
    title, authors, year, venue, doi, status = pdf_metadata[p.name]
    target = source_map[p.relative_to(ROOT).as_posix()]
    pdf_rows.append({"supplied_filename": p.name, "title_plain_text": title, "authors": authors,
                     "year_as_available": year, "venue_publisher_as_available": venue,
                     "DOI": doi, "DOI_URL": "https://doi.org/" + doi if doi else "",
                     "evidence_status": status, "package_path": target, "sha256": sha(p.read_bytes())})
    text_name = p.stem.replace(" ", "_").replace("(", "").replace(")", "").replace(",", "") + ".txt"
    extracted = AUDIT / "pdfs_text" / text_name
    if not extracted.is_file():
        raise RuntimeError("Missing completed PDF extraction: " + text_name)
    sample = "\n".join(extracted.read_text().splitlines()[:45])
    excerpts.append("\n## " + p.name + "\n\nPDF: `" + target + "`\n\nExisting extraction SHA-256: `" + sha(extracted.read_bytes()) + "`\n\n```text\n" + sample + "\n```\n")
txt("literature_evidence/SUPPLIED_PDF_METADATA.csv", csv_bytes(pdf_rows, list(pdf_rows[0])))
txt("literature_evidence/PDF_FRONT_MATTER_EXCERPTS.md", "".join(excerpts))

# This is explicitly a retrospective transcript summary, not a fabricated raw web capture.
txt("literature_evidence/SEARCH_EVIDENCE_TRANSCRIPTION.md", """# Search evidence retained from the completed Phase 0 conversation

**Evidence type:** retrospective transcription/summary of visible tool results from the earlier Phase 0 turn on 2026-11-12. No raw HTML, screenshot, Crossref response, or original tool-result export was saved in the workspace. No new network requests were made for this packaging task. Treat this as weaker evidence than a publisher-page capture.

## 1. Joshi–Patel–Prakash (publisher search result)
- Earlier query: `\"10.1007/s11128-026-05230-0\" OR \"Quantum codes construction from cyclic codes over matrix rings\" Joshi Patel Prakash`.
- Earlier result 1: https://link.springer.com/article/10.1007/s11128-026-05230-0
- Displayed title: *Quantum codes construction from cyclic codes over matrix rings*.
- Displayed authors: Soham Ravikant Joshi; Shikha Patel; Om Prakash.
- Displayed citation: *Quantum Information Processing* **25**, article **207** (2026).
- Displayed dates: received 31 December 2025; accepted 22 May 2026; version of record / published 9 June 2026.
- Displayed DOI: `10.1007/s11128-026-05230-0`.
- Stronger local evidence: the supplied PDF is included unchanged in `supplied_pdfs/` and its front matter agrees on these metadata fields. Packaging does not adjudicate the paper's mathematical validity or scope.

## 2. Liu–Pan (publisher PDF search result)
- Earlier query: `Liu Pan \"Galois hulls\" linear codes 2020 entanglement-assisted quantum`.
- Earlier result 1: https://link.springer.com/content/pdf/10.1007/s10623-019-00681-2.pdf
- Displayed title: *Galois hulls of linear codes over finite fields*.
- Displayed authors: Hongwei Liu; Xu Pan.
- Displayed citation: *Designs, Codes and Cryptography* **88**, 241–255 (2020).
- Displayed dates: published online 27 September 2019; issue February 2020.
- Displayed DOI: `10.1007/s10623-019-00681-2`.
- Its displayed reference list also cited Liu, X.; Yu, L.; Hu, P., *New entanglement-assisted quantum codes from (k)-Galois dual codes*, *Finite Fields and Their Applications* **55**, 21–32 (2019). That was secondary metadata, not a separate DOI verification.

## 3. Kushwaha–Prakash (arXiv PDF search result and secondary listing)
- Earlier query: `Kushwaha Prakash hulls codes non-commutative non-unital ring arXiv 2512.12335`.
- Earlier result 1: https://www.arxiv.org/pdf/2512.12335
- Displayed title/authors: *Hulls of Free Linear Codes over a Non-Unital Ring*; Anup Kushwaha and Om Prakash; arXiv:2512.12335 (2025).
- Earlier result 2 was an author listing: https://scholar.google.com/citations?hl=en&user=bAmP1egAAAAJ
- That secondary listing named *Symplectic Hulls over a Non-Unital Ring*, arXiv:2601.06609 (2026).
- **Qualification:** the visible evidence for 2601.06609 was a secondary listing, not a retrieved primary arXiv record. The six reports are preserved verbatim even where their verification language is stronger.

## 4. Inherited records
The original `prior_project/01_LITERATURE/references.bib`, annotated bibliography, comparison matrix, and `prior_project/PAPER/LITERATURE_VERIFICATION.md` are included unchanged. Their `DIRECT`, `SECONDARY`, `TO CONFIRM`, and other labels are historical source assertions. This package does not upgrade them or claim a new exhaustive literature/novelty search. Missing DOIs and venue fields remain missing rather than being guessed.
""")

# Focused navigational evidence indexes, not new mathematical derivations.
txt("mathematical_evidence/COUNTEREXAMPLES_AND_FAILURES_INDEX.md", """# Counterexamples and failed approaches: source index

This is an index of existing artifacts, not a new proof or implementation. Consult the complete derivations and their stated left/right conventions; source-level labels are not independently certified by packaging.

| Issue reported in Phase 0 | Included source evidence |
|---|---|
| Plain product and one-sided-module size-law failure | `prior_project/03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`, section 5; `../computational_evidence/research-data/scripts/phase0_feasibility.py`; its recorded log and the existing current-Phase-0 rerun in `../computational_evidence/current_phase0/` (E4) |
| Non-reflexive Galois regime / double-dual orientation | Complete pairing proofs, sections 3.6–3.9; `prior_project/06_AUDIT/PHASE0_PROOF_VERIFICATION.md`; `galois_duality_experiments.py`, `independent_audit_checks.py`, and their historical logs in the research-data tree |
| Squarefree-factorization and generator/principality assumptions | `prior_project/02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md`; Stage 2A/2B/2C sources; reconciliation and CRT scripts/logs |
| Non-principal hull examples | Stage 3B hull-enumeration proof source and log; `../computational_evidence/research-data/quantum_code_records/nonprincipal_witnesses.csv` |
| Gray expansion is not automatically Euclidean-compatible or a ring-Hamming isometry | `prior_project/03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md`, sections 0.3, 2 and 3; `../computational_evidence/research-data/logs/phase4_gray_map_log.txt` |
| Candidate approaches rejected only for scope/novelty, versus mathematical failure | Mandatory `../reports/PHASE0_PAIRING_OPTIONS.md` and `PHASE0_RESEARCH_GAP.md`; inherited novelty audit. Do not conflate a scope rejection with an invalid mathematical construction. |

The summary in `../reports/PHASE0_PAIRING_OPTIONS.md` uses `ax` in one semilinearity formula, whereas the complete source proof Proposition 2.1(3) uses the right action `x a`. Both are preserved without modification so the independent reviewer can check the side convention. This package does not repair or certify the reports' shorthand, candidate equivalences, or theorems.
""")
txt("computational_evidence/README.md", """# Computational evidence and reproducibility status

- `current_phase0/`: the already-existing 2026-11-12 run of **the same** prior Phase 0 feasibility script and its recorded diff. `RERUN_COMPARISON.json` verifies the 3 differing metadata/timing/path lines; it does not claim a mathematically independent implementation.
- `research-data/`: the complete original reproducibility unit (88 regular files including its two manifests). It contains 22 scripts, 23 logs, 29 JSON files, 8 CSV tables, 4 Markdown files, and 2 `.sha256` files. No file in it is newly authored or executed by this packaging task.
- `prior_project/`: distinct historical documentation and certification-method notes. Duplicate historical scripts/logs are stored only once in `research-data/`; their aliases are in `../repository_integrity/source_provenance.csv`.
- `SCRIPT_DEPENDENCIES.csv`: static syntax and local-import checks only, no execution.

## Gray-map results
The historical `research-data/logs/phase4_gray_map_log.txt` ends with 463 checks / 463 PASS / 0 FAIL, distinguishes EXH from SMP, and records the transported Hankel/reversal Gram matrix. Its script and complete mathematical source are included. It was **not re-run** during this packaging task; preservation and checksum verification are not fresh computational or mathematical certification. The report's broad wording about hundreds of checks being rerun should be read alongside this narrower actual-run evidence.

## Safe reproduction by an independent reviewer
Some historical scripts write log files next to their own source, and some have expensive/exhaustive modes. Do not run them directly in the sealed package or the original repository. First copy `research-data/` to a separate disposable working directory, inspect each script's entry point and the included environment/certification procedures, then run the desired historical check there with `PYTHONDONTWRITEBYTECODE=1`. Full extended searches are not implied by package verification.

Directly checking the active source-data manifest is read-only:

```sh
cd research-data
sha256sum -c PUBLICATION_MANIFEST.sha256
```

`documentation/MANIFEST.sha256` describes an older flat layout. Its entries were checked through an explicit relocation map in `../repository_integrity/inherited_manifest_verification.csv`; do not interpret its old paths as newly missing research data.
""")
txt("repository_integrity/EVIDENCE_LIMITATIONS.md", """# Evidence limitations and reviewer cautions

This document qualifies the packaging evidence; it does not edit any completed report, implement a research problem, or perform a new mathematical/novelty audit.

1. **Six reports unchanged.** Every mandatory report is an exact byte copy, with its source digest in `source_provenance.csv`. Labels such as PROVED, NEW, VERIFIED, FEASIBLE, LOW novelty risk, or Q1-viable remain the source's assertions, not a new guarantee. This package is for independent review of those assertions.
2. **File-count discrepancy.** The reports and inherited README say 86 data files in places. The actual `research-data/` tree has **88 regular files**: 22 Python scripts, 23 text logs, 29 JSON files, 8 CSV files, 4 Markdown files, 2 SHA-256 manifests. Its active publication manifest covers **87** files, excluding itself. The package preserves both the source wording and the counted evidence.
3. **What was actually rerun.** Completed current Phase 0 contains one stored rerun of `phase0_feasibility.py`; the stored comparison differs at three metadata/timing/path lines. The Gray-map, hull, quantum, extended-search and historical independent-audit logs are inherited, not newly rerun in this packaging task. The six reports sometimes summarize the scope more broadly. No mathematical script executed during packaging.
4. **Side conventions / proof summaries need independent checking.** In particular, the summary pairing report prints `B_k(ax,y)` whereas the detailed source Proposition 2.1(3) prints the right action `B_s(x a,y)`. Preserve and review the full proof rather than treating the abbreviated summary as a complete proof. General principality, dual orientation and candidate-equivalence assertions also require their exact source hypotheses; no correction or new theorem is attempted here.
5. **Gray transfer has a specified target form.** The complete source explicitly distinguishes its transported Hankel/reversal form from the ordinary Euclidean form and warns about metrics. The 463-check log is finite EXH/SMP evidence, not a proof of arbitrary-map compatibility or CSS inclusion in arbitrary new parameters.
6. **DOI/web evidence is bounded.** Seven exact user-supplied PDFs are included. Original raw web responses were not saved; the prior search results are transparently transcribed in the literature evidence folder. Most bibliography verification labels are inherited. The symplectic-hull arXiv title was seen in a secondary listing. No fresh network sweep, peer-review-status check, or novelty certification occurred here. Some supplied items still lack confirmed venue/year/DOI.
7. **Binary prior artifacts.** The patch marks 165 paths binary-only; they are enumerated but not recoverable as full binary contents. The recovered `PAPER/main.pdf` is a text-decoded/lossy binary representation and is deliberately excluded. The source `.tex` files are included instead. No compiled manuscript PDF or original blueprint PDF is asserted to be available in valid form.
8. **Manuscript versions and submission.** One canonical source tree plus only byte-distinct latest-staging deltas is included; shared sources are recorded as aliases. These are pre-existing versions, not a newly revised manuscript or a newly compiled submission bundle. The last Phase 23 records concern preparation/compliance; actual submission/acceptance status is not established by the package.
9. **Historical references versus current package dependencies.** `reference_resolution.csv` distinguishes present package targets, existing-but-omitted historical files, container inventory records, and unavailable/planned/abbreviated references. Historical proofs discuss old branch paths, proposed filenames, prior packages and instructions; those are not new instructions or broken dependencies of the package verifier. Newly declared package targets are all checked for existence.
10. **Rights and confidentiality.** Supplied papers and the author's unpublished manuscript sources are included for the requested private independent review. No new licence, open-access status, or permission for public redistribution is asserted. Credentials, `.git`, caches, original large container duplicates, repeated manuscript copies and unrelated journal-administration trees are excluded.
11. **Approval gate unchanged.** P1, P2 and P3 research directions remain unimplemented; no Phase 1 work, commit, push, submission, or manuscript modification was performed. References to older phases in included source material describe historical work, not progression in the current session.
""")
txt("repository_integrity/prior_work/PAPER/FFA_FINAL_SUBMISSION_V2/SOURCE_REUSE.md", """# Latest prior staging version: source reuse

Only files whose contents differ from the canonical `../main.tex`, `../references.bib`, and `../sections/` sources are physically repeated here. Identical files are stored once. `../../../source_provenance.csv` maps every selected staging source to its physical package copy; `../../../manuscript_input_resolution.csv` resolves all section/bibliography inputs for both versions.

This is a review collection of existing source versions, not a ready-to-compile, newly assembled submission bundle. To compile a version separately, materialize the mapped source tree in a disposable directory and supply the usual LaTeX packages. No original source is edited and no compilation is performed by packaging.
""")

# Resolve LaTeX inputs through the source/alias map, including deduplicated staging sections.
input_rows = []
for main in (PRIOR / "PAPER/main.tex", PRIOR / "PAPER/FFA_FINAL_SUBMISSION_V2/main.tex"):
    for kind, name in re.findall(r"\\(input|bibliography)\{([^}]+)\}", main.read_text()):
        local = main.parent / (name + (".tex" if kind == "input" else ".bib"))
        rel = local.relative_to(ROOT).as_posix()
        if rel not in source_map or source_map[rel] not in payload:
            raise RuntimeError("Missing selected manuscript input: " + rel)
        input_rows.append({"main_source": main.relative_to(ROOT).as_posix(), "input": name,
                           "source_path": rel, "package_path": source_map[rel], "status": "PACKAGED"})
txt("repository_integrity/manuscript_input_resolution.csv", csv_bytes(input_rows, list(input_rows[0])),
    "Every canonical/latest-staging LaTeX input resolves to a real packaged source, with aliases")

# Source reference register: exact relative references and historical exceptions are not conflated.
file_ext = r"(?:md|py|txt|csv|json|bib|tex|pdf|sha256|zip|patch)"
token_re = re.compile(r"(?<![A-Za-z0-9_])(?:[A-Za-z0-9_.+-]+/)*[A-Za-z0-9_.+-]+\." + file_ext + r"(?![A-Za-z0-9_])")
known_by_basename = defaultdict(set)
for original, target in source_map.items():
    known_by_basename[Path(original).name].add(target)
baseline_paths = {r["path"] for r in BASELINE["files"]}


def resolve(token):
    token = token.strip().strip(";, ")
    exact = [token, "phase0_audit/" + token, "phase0_audit/extracted/prior_project/" + token,
             "research-data/" + token, "research-data/scripts/" + token, "research-data/logs/" + token]
    for rel in exact:
        if rel in source_map:
            return "PACKAGED", [source_map[rel]], "Exact source path or standard evidence-root relocation"
    if token in REPORT_NAMES:
        return "PACKAGED", ["reports/" + token], "Mandatory report"
    if token in {"Matrix Ring 1.zip", "Matrix Ring.zip", patch.name, "01a1a47c-...patch"}:
        return "INVENTORY_ONLY", ["repository_integrity/original_zip_inventories.csv" if token.endswith(".zip") else "repository_integrity/patch_diff_inventory.csv"], "Original container hashed/inventoried; payload not duplicated"
    if token in {"main.pdf", "PAPER/main.pdf", "00_BLUEPRINT/Research_Blueprint.pdf"}:
        return "UNAVAILABLE_VALID_BINARY", ["repository_integrity/patch_binary_files.txt", "repository_integrity/EVIDENCE_LIMITATIONS.md"], "Binary absent from patch or lossy text reconstruction; valid source text included instead"
    if "Construction_of_Codes_Over_" in token and ("…" in token or "..." in token):
        name = next(n for n in pdf_metadata if n.startswith("Construction_of_Codes_Over_"))
        return "PACKAGED_ALIAS", sorted(known_by_basename[name]), "Abbreviated supplied PDF filename expanded"
    name = Path(token).name
    targets = sorted(known_by_basename.get(name, set()))
    if targets:
        return ("PACKAGED_ALIAS" if len(targets) == 1 else "PACKAGED_MULTIPLE"), targets, "Historical basename/layout alias; multiple targets left explicit when ambiguous"
    for rel in exact:
        if rel in baseline_paths:
            return "OMITTED_HISTORICAL", [], "Source exists in before-packaging inventory but omitted as nonessential/redundant"
    if any(Path(r).name == name for r in baseline_paths):
        return "OMITTED_HISTORICAL", [], "Matching historical filename exists in inventory; not a package execution dependency"
    return "UNRESOLVED_HISTORICAL", [], "Unlocated/proposed/abbreviated historical reference; no missing file silently fabricated"


reference_rows = []
for row in list(provenance):
    rel, target = row["source_path"], row["package_path"]
    if row["handling"] != "COPY" or not rel.endswith(".md"):
        continue
    text = payload[target].decode("utf-8", errors="replace")
    for line_number, line in enumerate(text.splitlines(), 1):
        for code in re.findall(r"`([^`\n]+)`", line):
            if not re.search(r"\." + file_ext, code):
                continue
            # Preserve filenames containing spaces when they are recognized full literals.
            if code.strip() in source_map or code.strip() in REPORT_NAMES or code.strip() in {"Matrix Ring 1.zip", "Matrix Ring.zip", "2602.18255v1 (1).pdf", "s11128-026-05230-0 (3).pdf"} or "Construction_of_Codes_Over_…" in code:
                tokens = [code.strip()]
            else:
                tokens = [m.group() for m in token_re.finditer(code)]
            for token in dict.fromkeys(tokens):
                status, targets, note = resolve(token)
                if any(t not in payload for t in targets):
                    raise RuntimeError("Declared package reference target missing: " + token)
                reference_rows.append({"referring_package_file": target, "line": line_number,
                                       "literal_reference": token, "status": status,
                                       "package_targets_json": json.dumps(targets, ensure_ascii=False), "note": note})
txt("repository_integrity/reference_resolution.csv", csv_bytes(reference_rows, list(reference_rows[0])),
    "Explicit source-report/proof Markdown file references with resolvable aliases and honest historical exceptions")
reference_counts = Counter(r["status"] for r in reference_rows)

# Source provenance is complete for all included original copies and duplicate aliases.
txt("repository_integrity/source_provenance.csv", csv_bytes(provenance, list(provenance[0])),
    "Exact source/package hashes, sizes, roles and deduplication aliases")
txt("repository_integrity/duplicate_aliases.csv", csv_bytes([r for r in provenance if r["handling"] == "DEDUPLICATED_ALIAS"], list(provenance[0])),
    "Omitted exact duplicate contents mapped to their one retained copy")

# Original-file preservation is checked after all source reads and before archive construction.
original_check = check_originals()
original_check.update({"tracked_files_matching_HEAD": len(tracked_rows),
                       "research_data_regular_file_count": len(research_files),
                       "active_publication_manifest_entries_PASS": sum(r["source_manifest"] == "PUBLICATION_MANIFEST.sha256" for r in manifest_rows),
                       "historical_manifest_entries_resolved_PASS": sum(r["source_manifest"].startswith("documentation/") for r in manifest_rows),
                       "selected_patch_source_checks": dict(Counter(r["status"] for r in selected_patch_checks)),
                       "reference_resolution_counts": dict(reference_counts),
                       "new_research_script_runs_in_packaging": 0,
                       "created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                       "scope": "Preservation/file integrity, not mathematical correctness or novelty."})
txt("repository_integrity/PACKAGING_VERIFICATION.json", json.dumps(original_check, indent=2, ensure_ascii=False) + "\n",
    "Originals/manifest/dependency verification results; final ZIP test is recorded beside the delivered archive")

# Reviewer landing page. Only new metadata is authored; original scientific sources remain unchanged.
report_links = "\n".join("- [" + n + "](reports/" + n + ")" for n in REPORT_NAMES)
readme = """# Phase 0 complete audit package

**Purpose:** private independent review of completed Phase 0, not authorization or execution of Phase 1. Packaged 2026-11-12 from branch `arena/7d88376d-matrix-ring`, HEAD `12db091726835cc6f264fb0f679afc759610c89a`.

## Start here
1. Read [evidence limitations and reviewer cautions](repository_integrity/EVIDENCE_LIMITATIONS.md) before interpreting proof/verification/novelty labels.
2. Read the six unchanged reports:
{report_links}
3. Use [PACKAGE_MANIFEST.md](PACKAGE_MANIFEST.md) for every packaged file and its role. [source_provenance.csv](repository_integrity/source_provenance.csv) gives exact original paths, hashes and duplicate aliases. [reference_resolution.csv](repository_integrity/reference_resolution.csv) resolves historical names without pretending omitted or unavailable artifacts exist.

## Layout
- `reports/`: all six mandatory reports, byte-for-byte copies.
- `mathematical_evidence/`: complete selected historical derivations/proofs, claim registers, Phase 0 audits and [counterexample source index](mathematical_evidence/COUNTEREXAMPLES_AND_FAILURES_INDEX.md). Labels in these files are historical assertions, not a new certification.
- `computational_evidence/`: the full original 88-file reproducibility unit, existing current Phase 0 rerun evidence, historical Gray-map and quantum logs/scripts/matrices, and static dependency checks. See its [README](computational_evidence/README.md).
- `literature_evidence/`: the seven exact supplied PDFs (one copy each), original bibliography/comparison/verification documents, metadata/front-matter evidence, and a transparently labelled [transcription of earlier search results](literature_evidence/SEARCH_EVIDENCE_TRANSCRIPTION.md). No new online verification sweep is claimed.
- `repository_integrity/`: before-packaging snapshot, tracked-file/HEAD checks, source-container inventories, selected patch reconstruction checks, provenance, reference resolution, prior-manuscript identity/source evidence, limitations and package-only verification tools.

The historical proofs, scripts and manuscript sources were already present in the supplied prior-work patch. Their older phase numbers do not mean those phases have started in the current session. Full repeated submission packages, compiled/lossily recovered binaries, caches, `.git`, credentials, the original large ZIP/patch containers and unrelated administration were intentionally excluded. Duplicate mathematical scripts and unchanged manuscript sections are represented by aliases, not repeated payloads.

## Read-only verification
From inside this extracted top-level directory:

```sh
sha256sum -c SHA256SUMS.txt
python3 -B repository_integrity/package_tools/verify_package.py .
```

To test the ZIP without extracting it:

```sh
unzip -t PHASE0_COMPLETE_AUDIT_PACKAGE.zip
python3 -B PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/package_tools/verify_package.py PHASE0_COMPLETE_AUDIT_PACKAGE.zip
```

The last command assumes the verifier is available from a separately extracted copy. `SHA256SUMS.txt` hashes every payload file except itself (standard non-self-referential convention). The adjacent `PHASE0_COMPLETE_AUDIT_PACKAGE.zip.sha256` authenticates the delivered ZIP, including that internal manifest. Final ZIP integrity/size/count results are recorded in the adjacent `PHASE0_COMPLETE_AUDIT_PACKAGE_VERIFICATION.txt`; the archive cannot non-circularly contain its own final checksum.

## Review boundaries and missing evidence
The packaging check proves file presence, preservation, dependency resolution and byte integrity only. It does not prove mathematics, novelty, journal quality, actual publication/submission status or current external benchmark rankings. Unavailable valid historical binary PDFs and missing raw publisher-page captures are documented, not silently substituted. Research-data count wording and narrower actual-rerun scope are documented without changing the six reports. Inherited unresolved/planned references remain visible in the reference register.

## Rights
This package is supplied for the requested private review. Third-party papers and the author's manuscript retain their existing rights; no public-redistribution licence is granted. The manuscript has not been revised. No Phase 1 work, P1/P2/P3 implementation, commit, push, submission or new mathematical computation was performed. Await further author instructions.
""".format(report_links=report_links)
txt("README.md", readme, "Reviewer landing page, verification instructions, scope and rights")

# Manifest has an explicit self-exclusion convention and names every final member.
final_paths = sorted([*payload, "PACKAGE_MANIFEST.md", "SHA256SUMS.txt"])
counts = Counter(p.split("/")[0] if "/" in p else "(top-level)" for p in final_paths)
manifest = ["# Package manifest\n\n", "**Regular files inside the ZIP: " + str(len(final_paths)) + "** (including this manifest and `SHA256SUMS.txt`; directory entries are not counted).\n\n",
            "All source copies are unchanged. Provenance and alias hashes are in `repository_integrity/source_provenance.csv`. SHA-256 coverage is every file listed here except `SHA256SUMS.txt` itself. Its bytes are covered by the external archive checksum. Final compressed ZIP size is measured after sealing and is stated in the delivery verification sidecar.\n\n",
            "## Category counts\n\n| Category | Files |\n|---|---:|\n"]
for cat, count in sorted(counts.items()):
    manifest.append("| `" + cat + "` | " + str(count) + " |\n")
manifest.append("\n## Complete file list\n\n| File | Purpose |\n|---|---|\n")
for name in final_paths:
    role = roles.get(name, "Package file inventory" if name == "PACKAGE_MANIFEST.md" else "SHA-256 of every other packaged file")
    manifest.append("| [" + name + "](" + quote(name, safe="/._-") + ") | " + role.replace("|", "/") + " |\n")
txt("PACKAGE_MANIFEST.md", "".join(manifest), "Complete final archive file inventory")

# All declared new links must exist; only inherited references are allowed documented exceptions.
for name in ("README.md", "PACKAGE_MANIFEST.md"):
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", payload[name].decode()):
        from urllib.parse import unquote
        path = unquote(target)
        if path != "SHA256SUMS.txt" and path not in payload:
            raise RuntimeError("New documentation link missing: " + path)
checksums = "".join(sha(payload[name]) + "  " + name + "\n" for name in sorted(payload))
txt("SHA256SUMS.txt", checksums, "Non-self-referential checksum manifest")
if set(payload) != set(final_paths):
    raise RuntimeError("Final file-list accounting mismatch")
for row in provenance:
    if sha(payload[row["package_path"]]) != row["sha256"]:
        raise RuntimeError("Source copy mismatch at " + row["source_path"])
if len({sha(v) for v in payload.values()}) != len(payload):
    # A true byte-identical data manifest/file can be intentional; report rather than deleting it.
    duplicates = defaultdict(list)
    for n, b in payload.items(): duplicates[sha(b)].append(n)
    actual_dupes = [v for v in duplicates.values() if len(v) > 1]
    raise RuntimeError("Unexpected redundant payload files: " + json.dumps(actual_dupes))

# Exclusive writes only. No pre-existing path is ever replaced or removed.
OUT.mkdir()
for name, data in sorted(payload.items()):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        f.write(data)
verifier = OUT / "repository_integrity/package_tools/verify_package.py"
verified = subprocess.run([sys.executable, "-B", str(verifier), str(OUT)], capture_output=True, text=True)
if verified.returncode:
    raise RuntimeError("Package verifier failed: " + verified.stdout + verified.stderr)
checksum_run = subprocess.run(["sha256sum", "-c", "SHA256SUMS.txt"], cwd=OUT, capture_output=True, text=True)
if checksum_run.returncode:
    raise RuntimeError("External SHA-256 validation failed: " + checksum_run.stdout + checksum_run.stderr)
with zipfile.ZipFile(ARCHIVE, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name in sorted(payload):
        info = zipfile.ZipInfo(NAME + "/" + name, date_time=(2026, 11, 12, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, payload[name])
with zipfile.ZipFile(ARCHIVE) as z:
    if z.testzip() is not None:
        raise RuntimeError("ZIP CRC testing failed")
    if set(z.namelist()) != {NAME + "/" + p for p in payload}:
        raise RuntimeError("ZIP members differ from assembled payload")
    for name, data in payload.items():
        if z.read(NAME + "/" + name) != data:
            raise RuntimeError("ZIP content mismatch: " + name)
unzip_run = subprocess.run(["unzip", "-t", str(ARCHIVE)], capture_output=True, text=True)
if unzip_run.returncode:
    raise RuntimeError("unzip -t failed: " + unzip_run.stdout + unzip_run.stderr)
zip_verified = subprocess.run([sys.executable, "-B", str(verifier), str(ARCHIVE)], capture_output=True, text=True)
if zip_verified.returncode:
    raise RuntimeError("Standalone ZIP SHA-256 verifier failed: " + zip_verified.stdout + zip_verified.stderr)
final_originals = check_originals()
archive_sha = sha(ARCHIVE.read_bytes())
with SIDECAR.open("x", encoding="utf-8") as f:
    f.write(archive_sha + "  " + ARCHIVE.name + "\n")
summary = {"archive": ARCHIVE.relative_to(ROOT).as_posix(), "ZIP_regular_file_count": len(payload),
           "ZIP_bytes": ARCHIVE.stat().st_size, "ZIP_MiB": round(ARCHIVE.stat().st_size / 1048576, 6),
           "uncompressed_bytes": sum(len(v) for v in payload.values()), "zip_SHA256": archive_sha,
           "SHA256SUMS_entries": len(payload) - 1, "mandatory_reports": "6/6 present and byte-identical to originals",
           "original_file_preservation": final_originals, "tracked_files_match_HEAD": len(tracked_rows),
           "sha256sum_test": "PASS", "zip_testzip_CRC": "PASS", "unzip_test_exit_code": unzip_run.returncode,
           "standalone_ZIP_verifier": "PASS", "source_alias_rows": len(provenance),
           "deduplicated_source_copies": sum(r["handling"] == "DEDUPLICATED_ALIAS" for r in provenance),
           "reference_status_counts": dict(reference_counts), "research_scripts_executed_during_packaging": 0,
           "limitations": "See repository_integrity/EVIDENCE_LIMITATIONS.md; file integrity is not mathematical/novelty certification."}
with DELIVERY.open("x", encoding="utf-8") as f:
    f.write(json.dumps(summary, indent=2, ensure_ascii=False) + "\n\n--- standalone extracted-package verifier ---\n" + verified.stdout)
    f.write("\n--- standalone ZIP verifier ---\n" + zip_verified.stdout)
    f.write("\n--- sha256sum -c SHA256SUMS.txt ---\n" + checksum_run.stdout)
    f.write("\n--- unzip -t ---\n" + unzip_run.stdout + unzip_run.stderr)
print(json.dumps(summary, indent=2, ensure_ascii=False))
