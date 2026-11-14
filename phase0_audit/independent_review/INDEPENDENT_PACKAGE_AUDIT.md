# Independent package audit

**Audit execution:** 2026-11-13 UTC (recorded workspace clock). **Input integrity: PASS. Reference closure: QUALIFIED, not universal. Scientific/submission readiness: HOLD.** No original report, manuscript, data file or source archive was changed.

## 1. Input identity and read-only scope

Input: `phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE.zip`.

```
SHA256 350e5b9e4796d6b7798c17ce8ef047ee032e50cc4e49df0ef6e8d28ea5538c4e
size   5,208,317 bytes
```

The archive was freshly reopened and safely extracted to `work/PHASE0_COMPLETE_AUDIT_PACKAGE/` in this review. It contains **211 regular files**, **11,137,023 uncompressed bytes**, no duplicate/unsafe member paths, and passes ZIP CRC. Its **210-entry internal SHA-256 manifest** covers every member except the manifest itself; all entries match. Every extracted file matches its archive bytes.

The six mandatory reports are readable UTF-8, exact copies of the preserved original reports, and independently hashed. See [readability/hash table](evidence/package_checks_v2/six_report_readability.csv). Exact results are in [independent package checks v2](evidence/package_checks_v2/independent_package_checks.json), produced by the new checker rather than inferred from the bundled verifier's old PASS output.

| Mandatory report | Bytes | Review consequence |
|---|---:|---|
| PHASE0_REPOSITORY_AUDIT.md | 12,539 | Recovery/inventory useful; count/readiness/verification wording needs qualification |
| PHASE0_LITERATURE_REVIEW.md | 11,534 | Broad overlap diagnosis survives; several metadata/benchmark/priority statements need correction |
| PHASE0_RING_FEASIBILITY.md | 9,415 | Core setting feasible; base-ring principality claim and stale obstacle are wrong |
| PHASE0_PAIRING_OPTIONS.md | 8,146 | Correct primary choice, but wrong action/probe and unreconciled mirror/candidate conventions |
| PHASE0_RESEARCH_GAP.md | 8,021 | Internal overlap established; P1/P2/P3 differentiation/novelty claims overstated |
| PHASE0_DECISION_REPORT.md | 12,136 | Earlier conditional-GO/immediate-submission advice superseded by this review's **HOLD** |

Independent readability extends to **all 204 non-PDF files**: strict UTF-8 decoding, JSON/CSV parsing as appropriate, and Python AST parsing. All **7 PDFs** parse with pypdf6.1.1 and contain extractable text; their page counts are30,5,13,30,14,8,9. Each is byte-identical to its **actual authentic member in `Matrix Ring 1.zip`**, not merely to an inherited digest. See [supporting-file checks](evidence/supporting_checks_v2/supporting_file_checks.json).

The original damaged extracted A5b PDF remains untouched; the input package correctly uses the intact original ZIP member. No valid compiled `PAPER/main.pdf` or original blueprint PDF was recovered from the patch's binary placeholders. The blueprint text extraction and manuscript TeX are available; they are not substitutes for a verified compiled PDF. No TeX compilation was performed in this audit.

## 2. Provenance and manifests

| Check | Fresh result | Important limit |
|---|---:|---|
| Original ZIP CRC / member identity | 211/211 PASS | Authenticity/integrity, not mathematical validity |
| Original package internal hashes | 210/210 PASS | Manifest excludes itself |
| Source-provenance records | **239/239** size/hash checks PASS | Multiple provenance rows can refer to one package payload |
| Active publication manifest | **87/87** PASS | Excludes the publication manifest itself |
| Inherited historical manifest mappings | **85/85** PASS | Historical paths are resolved by documented relocation, not assumed direct paths |
| Combined inherited-manifest verification rows | **172/172** PASS | 87+85; not172 distinct data files |
| Six reports versus originals | 6/6 byte-identical | Preserved defects are intentionally not overwritten |

### Exact resolution of 86 / 88 / 87

The current `research-data/` tree has **88 regular files**, **1,880,790 bytes**:

| Type | Files |
|---|---:|
| Python | 22 |
| Text logs | 23 |
| JSON (28 records+INDEX) | 29 |
| CSV | 8 |
| Markdown | 4 |
| SHA-256 manifests | 2 |
| **Total** | **88** |

There are two legitimate but different uses of **86**:

1. The current tree has **86 non-manifest files**, after excluding both `.sha256` files.
2. The historical supplementary layout has **85 mapped payload files + its own manifest =86**. Relative to that footprint, the current tree adds the top-level publication **`README.md`** and **`PUBLICATION_MANIFEST.sha256`**, producing88. The old README is separately preserved/mapped as `documentation/SUPPLEMENTARY_PACKAGE_README.md`; it is not the new publication README.

The active publication manifest has **87 entries** because it covers **all current files except itself**, including the inherited `documentation/MANIFEST.sha256`. Thus:

```
88 current files = 86 non-manifest files + 2 manifests
87 publication entries = 88 current files - publication manifest itself
86 historical footprint = 85 historical mapped payloads + historical manifest
```

A sentence saying “the current data package has86 files, with87/87 manifest entries” mixes counting bases and is misleading. Historical text with other script subtotals is preserved as historical wording; it does not override the explicit current inventory. Hash agreement cannot resolve a count without specifying the counted tree, date/layout and self-exclusion rule.

## 3. Internal references: comprehensive mechanical pass, qualified semantic closure

The independent checker rechecks **every row** in the input's declared reference-resolution table, its referring line/literal and each declared target. It also separately scans packaged Markdown links, all local Python imports, both TeX source variants, explicit T-ID citations/ranges in the six reports, and their supporting theorem text. The historical N1–N12 references are explicitly resolved in the mathematical report §2.1.

### Reference-resolution table

There are **1,010 reference occurrences** and **1,017 declared target edges**. Every declared target exists; all recorded referring literals are present at the indicated lines. **Zero literal-line exceptions.** But not every status denotes an available original reference:

| Status | Occurrences | Meaning for independent review |
|---|---:|---|
| PACKAGED | 619 | Selected source is present |
| PACKAGED_ALIAS | 226 | Present via documented relocation/reuse |
| PACKAGED_MULTIPLE | 41 | Multiple documented targets, not a unique literal path |
| OMITTED_HISTORICAL | 69 | Existing historical source omitted from curated package; no target payload here |
| UNAVAILABLE_HISTORICAL_CONTAINER | 15 | Original binary ZIP not recoverable; selected underlying material/limitations supplied |
| UNAVAILABLE_VALID_BINARY | 14 | Blueprint PDF/main.pdf not available as valid binaries |
| INVENTORY_ONLY | 11 | Inventory/hash of a container, not its duplicated content |
| UNRESOLVED_HISTORICAL | 11 | No supported original resolution |
| EXTERNAL_HISTORICAL_URL | 4 | Historical remote URLs, not independently fetched/validated as available |

The **41 occurrences in the six mandatory reports** comprise25PACKAGED+7ALIAS+2MULTIPLE+6INVENTORY_ONLY+1UNAVAILABLE_VALID_BINARY. Their mathematical/script evidence is present, but container inventories and a missing valid main.pdf must not be described as full original-file closure.

All exceptions, with exact referring file, line, literal and notes, are in [reference_exceptions_for_review.csv](evidence/reference_exceptions_for_review.csv); the complete independent pass is [here](evidence/package_checks_v2/independent_reference_resolution_check.csv).

Examples of genuinely unresolved historical literals: `00_MANIFEST.md`, `03_THEOREMS/CYCLIC_CODE_STRUCTURE.md`, `CYCLIC_CODE_STRUCTURE.md`, `binary.zip`, `release-texlive.txt`, `verification/clean_rebuild.txt`. The missing historical containers include Phase0/Phase1 and manuscript ZIPs; inventory records are not their byte contents. The patch identifies **165 binary-only paths**, not165 recovered binaries. No missing proof or archive has been fabricated.

### Additional cross-reference passes

| Item | Independent result | Scope |
|---|---|---|
| Markdown explicit links | **225/225 local destinations exist** | Does not establish correctness of linked claims |
| Research Python scripts | **22 parse; 34 local import edges resolve**; no nonstdlib/nonlocal imports detected | Static check; not all22 programs were rerun |
| T-ID/report pairs (including ranges) | **58/58 identifiers found** in packaged mathematics | Identifier presence is not a semantic proof-status check; stale T021 is an example |
| Canonical TeX | **13 inputs**,107labels,246references,32citation occurrences,13BibTeX entries; no duplicate labels/undefined refs/cites | Parsed source, not compiled output |
| Latest staged TeX | **13 inputs**,116labels,264references,32citation occurrences,13BibTeX entries; no duplicate labels/undefined refs/cites | **9 inputs require documented source-reuse mappings** after curation |

See [TeX reference table](evidence/package_checks_v2/independent_latex_cross_references.csv), [Python imports](evidence/package_checks_v2/independent_python_imports.csv), and [T-ID table](evidence/package_checks_v2/six_report_theorem_id_resolution.csv). The staged delta tree alone is not an out-of-the-box complete build directory; assemble the documented shared sources first.

**Conclusion on “every internal reference”:** every declared reference/target and recognized syntax category above was mechanically checked, and the six reports' decisive mathematical references were semantically reviewed. This reveals, rather than eliminates, omitted/unavailable/unresolved items and inaccurate proof applicability. A claim of **universal reference closure or universal proof validity would be false**. The package is usable for qualified review, not a flawless archival reconstruction.

## 4. Reproduction and independent verification

The prior package builder did **not** rerun the full later research campaign. This independent review did more, while preserving that distinction:

- Three original-source runs completed exit0: feasibility32.460s; Gray217.269s; generator reconstruction616.785s.
- Gray log:463/463, byte-identical to the archived log. The generator run regenerated28records+INDEX byte-identically.
- A separately written finite-field implementation recertified all28 supplied field-code records and exact distances. There are17core+7follow-up+5scope assertions, including counterexamples; the final scope assertion explicitly imports disposable original-source helpers to reproduce a known representation error.
- No blanket claim that all120721 scanned codes, all5055 distance rows, all literature proofs, or all historical phases were independently verified follows.

The detailed run logs and scopes are in [ER](evidence/included_source_run_summary.json), [Gray evidence audit](GRAY_MAP_EVIDENCE_AUDIT.md), and [claim ledger](MATHEMATICAL_CLAIM_VERIFICATION.md). The bundled historical verifier was not rerun as a substitute for these independent checks.

## 5. Cross-report consistency and scientific failure modes

Physical integrity and path resolution pass, but scientific readiness does not. The independent review finds:

- wrong right-action formula and invalid matrix-unit nondegeneracy probe in the pairing summary;
- confusion of base-ring versus cyclic-quotient principality, and stale open-status claims;
- unreconciled left/inverse-twist candidate conventions;
- an invalid nonprincipal-hull construction in the manuscript and a separately reproduced Phase5 row-representation bug (a valid earlier explicit hull witness survives);
- bilinear/Hermitian/Euclidean scope errors despite a valid transported Gray theorem;
- foundational stabilizer/EA proof defects and incorrect all-route quotient/bookkeeping statements;
- incorrect field-encoding documentation and misinterpreted physical-alphabet/EA benchmark availability;
- bibliographic errors, unsupported priority/Q1 recommendations and significant overlap between the unchanged blueprint and the existing campaign.

Every correction is **separate** in [DISCREPANCY_AND_CORRECTION_REGISTER.md](DISCREPANCY_AND_CORRECTION_REGISTER.md). This report neither silently amends the six reports nor declares all28 valid code records invalid because other proofs fail.

## 6. Preservation, audit self-correction and delivery seal

The pre-review snapshot records **1,487 pre-existing regular files**, **71,459,327 bytes**, outside `.git`. Final sealing rehashes **every one**, checks for deletion/size change, unchanged HEAD/current branch, and additions outside the authorized review directory. The auditable result is [final_original_preservation.json](evidence/final_original_preservation.json). No commit or push was permitted or made.

Branch: `arena/7d88376d-matrix-ring`; baseline HEAD: `168ec3e0b860cbe086ccb7a92a1a1aac5f8a277b`.

**Date provenance:** originals keep their original dates. The new snapshot's `review_date` was initially copied as2026-11-12, whereas its actual `capture_clock_utc` is **2026-11-13T07:07:51.274681+00:00**. That mismatch is preserved, not overwritten. New audit execution dates use the recorded workspace-clock date; the inconsistent field is not evidence of an earlier run.

**Checker-development disclosures:** the first TeX citation parser retained a newline inside one key, creating a false missing-citation diagnostic; the executed v2 strips whitespace and reports **no undefined citations**. A first follow-up assertion contained an extraneous incorrect expression and was fixed before the successful v2 run. The initial PDF-check attempt could not find `pdftotext`; the successful v2 uses pypdf6.1.1. Preliminary artifacts are retained and not confused with the final results. These are audit-checker issues, not defects imputed to the research.

The delivered review ZIP contains the seven requested reports, evidence/scripts, the exact original ZIP and its fresh expanded review sources. It excludes disposable rerun trees/dependency installations and unrelated repository contents. Its SHA manifest and independent archive verifier support later checking. The **archive verification result** is separate from the **scientific HOLD** decision. No new research is authorized by either seal.
