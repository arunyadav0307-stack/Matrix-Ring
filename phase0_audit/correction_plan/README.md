# Phase0 hold-resolution and correction-plan package

**Recorded planning execution:** 2026-11-13 UTC (workspace clock).  
**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**

## Read first

- [Author decisions and approval boundaries](AUTHOR_APPROVAL_CHECKLIST.md)
- [Exact manuscript authority, version inventory and submission-status qualification](AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md)
- [All43 actions, each with eleven explicit fields](MASTER_CORRECTION_REGISTER.md)
- [Group A — mathematical proof obligations](MATHEMATICAL_PROOF_REPAIR_PLAN.md)
- [Group B — proposed bounded B00–B08 verification gates](COMPUTATIONAL_REPAIR_PLAN.md)
- [Group D — literature, benchmarks and novelty](LITERATURE_NOVELTY_REPAIR_PLAN.md)
- [Groups A–D — dependencies and safest sequence, including Group C notation/structure](CORRECTION_DEPENDENCY_MAP.md)

**Count convention:** 43 registered actions comprise **8 CRITICAL blocking families,29 MAJOR actions,6 MINOR actions**. The eight are the inherited BLOCKING findings, not43 independent false theorems. Major prerequisites and active scope corrections still need closure decisions. Audit self-disclosures A01–A04 are not additional blockers.

**Baseline finding:** Phase23 explicitly designates **MS03 / PAPER/FFA_FINAL_SUBMISSION_V2/** as the authoritative **staging** copy of the existing campaign. Its source-set SHA-256 is `b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24`. Current author confirmation of that baseline, actual submission status and any submitted/private later version remains required. This is not an unconditional identification of an actually submitted manuscript.

## Contents and evidence scope

`PHASE0_CORRECTION_PLAN.zip` is a planning package, **not a corrected manuscript or new research release**. It contains the seven requested documents above and supporting material:

- `evidence/manuscript_versions.csv`, `manuscript_files.csv`, comparisons/diffs and source manifest: 19 recovered complete roots, nine distinct core payloads, four audit mirrors, observed filenames/mtimes/hashes and unavailable-artifact qualifications.
- `evidence/correction_actions.json`, `master_correction_register.csv`, `correction_dependency_map.json`: all43 actions, source locators, proof/test/parameter obligations and checked dependency DAG.
- `evidence/audit_reports/`: **verbatim** copies of the seven independent-review reports, their relative-link evidence closure and additional existing evidence read for this plan. Scientific scripts found inside copied evidence are historical artifacts, **not executed by this task**.
- `evidence/documentary_sources/`: eight verbatim historical authority/data/submission-preparation records. Their original statements, dates, pending markers and references remain historical, not newly endorsed policy/status claims.
- `evidence/copied_evidence_provenance.json`:42 source/copy/size/SHA records; `audit_report_inputs.json`:seven primary report inputs.
- `evidence/source_reading_observations.md`:10 quoted source locators refining existing issue scopes; no new proofs or experiments.
- `evidence/pre_plan_snapshot.json`, final preservation comparison and validation: recorded protection of1,959 pre-existing files,106,136,867 bytes.
- `scripts/`: repository-specific read-only inventory/evidence-copy/planning renderers, delivery sealer and **portable read-only archive verifier**. Do not rerun exclusive-output builders in this delivered directory.
- `SHA256SUMS.txt`: every internal payload file except the manifest itself.

The complete manuscript bodies, research-data tree and original audit ZIPs are **not redundantly repackaged here**. They remain unchanged in the checkout and previously delivered independent-review package. Inventory paths are checkout-relative source identities, not promises that every original historical file is nested in this plan ZIP. Missing manuscript binaries remain missing; inherited ZIP/PDF digests are not verified recovered payloads. Copied historical documents may refer to their original source layout. The new planning documents and copied independent-review report links have checked local closure; this is not a claim of universal historical-reference recovery.

## Safe portable verification — no research execution

After extracting this package, run only the standard-library archive verifier:

```sh
python3 -B PHASE0_CORRECTION_PLAN/scripts/verify_correction_plan_archive.py /path/to/PHASE0_CORRECTION_PLAN.zip
```

It checks CRC, safe unique paths, exact manifest coverage/hashes, all seven required documents/status markers, the43-action/11-field register and severity counts, dependency acyclicity, copied-evidence hash identities, source-manifest fingerprint and new-document/report links. It checks the external `.zip.sha256` sidecar when present. It does **not** run scientific scripts, compile TeX, access the network, prove mathematics, certify novelty or confirm actual submission status.

The portable verifier validates the archived preservation **records**, not external source files absent from the ZIP. The repository-specific sealer performs the actual pre/post original-file comparison and verifies source-copy identities against the live frozen checkout. Those results are recorded in the archived evidence.

A separate `PHASE0_CORRECTION_PLAN_VERIFICATION.txt` and `PHASE0_CORRECTION_PLAN.zip.sha256` accompany the ZIP; they are not nested inside it, avoiding a circular self-hash. On systems with `sha256sum`:

```sh
sha256sum -c PHASE0_CORRECTION_PLAN.zip.sha256
```

## Boundaries and dates

All new outputs are within `phase0_audit/correction_plan/`. No manuscript, original report/data/archive or completed independent-review artifact is changed. No scientific rerun, replacement proof/theorem, new benchmark dataset, TeX build, Phase1/P1/P2/P3, editorial contact, release, submission, commit or push occurs in this task.

Original dates are preserved. New planning records use the workspace execution date2026-11-13 UTC. The older independent-review snapshot's erroneous Nov12 date field remains disclosed, not corrected in place. Filesystem recovery mtimes are not authoring/submission dates.

The seven documents specify obligations and decisions **only**. Wait for explicit author implementation approval and any required mathematical-audit gate; do not interpret an integrity PASS as mathematical GO.

**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**
