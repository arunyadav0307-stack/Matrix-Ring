# Review navigation and safe verification

This is an **independent Phase-0 audit**, not a corrected research release. Start with [AUTHOR_DECISION_BRIEF.md](AUTHOR_DECISION_BRIEF.md). The seven requested reports have their exact requested filenames. Extra files here are supporting evidence, navigation and integrity tooling, not additional mandatory reports.

## Archive layout

- Seven review reports at the top level.
- `evidence/`: immutable-to-this-delivery run results, stdout, preliminary and authoritative-v2 checks, web retrieval **notes** (not raw captures), inventories, claim-support tables, baseline and final preservation evidence.
- `scripts/`: independently written audit checks, source-rerun wrapper, navigation-table builder, delivery sealer and portable archive verifier.
- `evidence/input/PHASE0_COMPLETE_AUDIT_PACKAGE.zip`: **exact original input**, SHA256 `350e5b9e4796d6b7798c17ce8ef047ee032e50cc4e49df0ef6e8d28ea5538c4e`.
- `work/PHASE0_COMPLETE_AUDIT_PACKAGE/`: its exact211-file expansion, allowing the review's source links/locators to resolve without the original checkout.
- `SHA256SUMS.txt`: all review payload files except the manifest itself.

The delivery excludes disposable `work/source_runs/`, `work/focused_source_check/`, `work/python-dependencies/`, Git metadata and unrelated repository originals. All required original research scripts/generator records and seven authentic literature PDFs are already in the included input/expansion. Recorded absolute commands identify the actual audit environment; they are provenance, not portable-path promises.

## Verify without executing research code

The archive verifier is read-only and uses only the Python standard library:

```sh
python3 -B PHASE0_INDEPENDENT_REVIEW/scripts/verify_review_archive.py /path/to/PHASE0_INDEPENDENT_REVIEW.zip
```

It checks ZIP CRC/safe unique paths, exact manifest coverage/hashes, the seven report names, the nested original ZIP's known identity/internal hashes, byte-identical expanded sources and links among the new top-level review documents. If the external `.zip.sha256` sidecar is available next to the ZIP, it checks that too. It **does not rerun research, fetch literature, or prove mathematics**.

On systems with `sha256sum`, the external sidecar can also be checked from the ZIP directory:

```sh
sha256sum -c PHASE0_INDEPENDENT_REVIEW.zip.sha256
```

The separate `PHASE0_INDEPENDENT_REVIEW_VERIFICATION.txt` records the executed portable verifier result. It and the ZIP's own external digest are not nested inside the ZIP, avoiding a circular hash claim. The authoritative internal seal is `SHA256SUMS.txt`.

## Reproduce scientific checks safely, only in a fresh disposable directory

**Do not rerun research scripts against the original `research-data/` or overwrite this sealed evidence.** Historical scripts can write adjacent logs. The independent scripts deliberately use exclusive output creation, so rerunning them in a delivered directory containing existing output files will fail rather than silently overwrite evidence.

To rerun, create a separate temporary audit layout with copies of `scripts/`, `work/PHASE0_COMPLETE_AUDIT_PACKAGE/`, and an empty `evidence/` directory. Preserve these relative paths. Use `python3 -B` with `PYTHONDONTWRITEBYTECODE=1`. This is guidance for verification, not new authorization to conduct a research phase.

| Script | Input / output behavior and scope |
|---|---|
| `independent_math_checks.py` | Existing supplied examples only; independent field/matrix/dual/distance arithmetic. Produces17core assertions and28record results. No project arithmetic imports |
| `critical_followup_checks.py` | Imports the independent audit arithmetic; produces7focused convention/proof/encoding checks |
| `remaining_scope_checks.py` | First4checks independent; fifth copies all historical scripts into a **new** disposable helper directory and reproduces the Phase5 μ bug. Does not modify input |
| `run_included_sources.py` | Makes new disposable copies, runs Phase0/Gray/generator extraction with time limits and `MATRIX_RING_COMP`; produces execution records and byte comparisons. This is original-source reproduction, not independent arithmetic |
| `independent_package_checks.py` | Needs exact input ZIP (fallback `evidence/input/`), expanded source and a nonexistent `evidence/package_checks_v2/` output directory. Report-versus-checkout comparison is only available if the corresponding originals are present |
| `supporting_file_checks.py` | Needs pypdf6.1.1 (installed locally for this audit); new `supporting_checks_v2/` output. PDF-versus-**actual source container** comparison requires original `Matrix Ring 1.zip` in the checkout. That unrelated container is not duplicated in the delivery; all seven checked PDF bytes and actual comparison results are preserved |
| `build_review_tables.py` | Requires previously generated evidence; writes new tables exclusively. No code search/network access |
| `seal_review_delivery.py` | **Repository-specific** final preservation/link/classification checks and ZIP builder. Requires the1,487-file original checkout/baseline, writes only within this review directory, and refuses existing sealed outputs |
| `verify_review_archive.py` | Portable, read-only, no research execution; safe default for recipients |

Computational costs depend on hardware. Recorded source reruns took32.460s,217.269s and616.785s concurrently; the supplied exact-distance checks also require finite enumeration/support search. No demand to reproduce all historical5055distance results or every searched code is implied.

## Authoritative versus preliminary evidence

Use `evidence/package_checks_v2/` and `evidence/supporting_checks_v2/` for final structural/readability results; the earlier outputs are preserved checker-development history. The first follow-up/stdout and corrected-v2 stdout are likewise distinguished. See the audit's A01–A04 entries in [DISCREPANCY_AND_CORRECTION_REGISTER.md](DISCREPANCY_AND_CORRECTION_REGISTER.md).

The baseline's copied `review_date` field is wrong; its actual `capture_clock_utc` is2026-11-13T07:07:51.274681+00:00. The original snapshot was intentionally not rewritten. New audit dates report the recorded workspace execution date. [Final preservation](evidence/final_original_preservation.json), [per-original comparison](evidence/final_original_file_comparison.csv) and [delivery validation](evidence/final_review_validation.json) supply the seal's evidence.

**Integrity PASS is not mathematical GO. The scientific decision remains HOLD, and explicit author approval is required before any correction implementation or new research.**
