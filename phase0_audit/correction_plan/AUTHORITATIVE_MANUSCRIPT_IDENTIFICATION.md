# Authoritative manuscript identification

**Recorded planning execution:** 2026-11-13 UTC (workspace clock).  
**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**

## 1. Exact finding: authoritative **staging** source is documented

The historical Phase23 data-availability record explicitly says:

> Applied to: `PAPER/FFA_FINAL_SUBMISSION_V2/` (the new authoritative staging copy) only. The canonical manuscript, the V2 and V3 reviewer packages and the Phase 19 FFA copy are untouched.

See the [verbatim Phase23 designation](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md), opening and §§B5–B8. This is stronger evidence than folder names or filesystem mtimes. It identifies a staging authority, **not** an actually submitted or accepted version.

**Documented correction-planning baseline: MS03**

- Title: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings*.
- Complete recovered source root: `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/`.
- Entry file: `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex`.
- Entry file size: **13,996 bytes**.
- Observed entry-file mtime UTC: **2026-11-13T06:47:04.036386+00:00**.
- Entry-file SHA-256: `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0`.
- **14-file core-source-set SHA-256:** `b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24`.
- Core set: `main.tex`, **12** `sections/*.tex` files and `references.bib`. All literal section inputs exist in this full recovered root.

The core-set digest is SHA-256 of UTF-8 lines `file_sha256 + two spaces + relative_filename + newline`, sorted by relative filename. It is not the SHA of a hypothetical ZIP or compiled PDF. The exact [MS03 source manifest](evidence/MS03_source_manifest.sha256) and [all-file inventory](evidence/manuscript_files.csv) identify each source's bytes and observed mtime. Generated `.bbl` snapshots are inventoried separately and are not part of that 14-file digest.

**Author gate:** confirm that MS03 is still the intended baseline and identify any later/private/submitted revision before implementation. Until then no working manuscript copy is created and no source selection is silently adopted for correction.

## 2. Inventory scope and timestamp interpretation

Read-only local inventory found **19 recovered campaign source roots**, containing **9 distinct 14-file core payloads**, plus **4 curated audit mirrors**. These are snapshots/build copies of **one prior campaign**, not 19 different papers. Every available source filename, size, observed mtime and SHA-256 appears in [manuscript_files.csv](evidence/manuscript_files.csv); root identities are in [manuscript_versions.csv](evidence/manuscript_versions.csv).

The mtimes below are **recovery/extraction filesystem observations**, not verified creation dates, author approval dates or submission timestamps. The primary recovered files cluster around 2026-11-13T06:47:04Z; sorting those timestamps would give a misleading chronology. Original documents contain historical Nov9/Nov10 labels and decisions; these remain attributed historical records. No missing timestamp or hash is invented.

`PRIOR/` in the following table means exactly `phase0_audit/extracted/prior_project/`. Each entry file is `PRIOR/<root>/main.tex`.

| ID | Root relative to PRIOR | Observed main mtime UTC | main.tex SHA-256 | 14-file core SHA-256 |
|---|---|---|---|---|
| MS01 | PAPER | 2026-11-13T06:47:04.060386+00:00 | `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` | `57dd301e63a19f9c89fe0a26978c3ae9eb59294f6573440f6667fbcb276fdf60` |
| MS02 | PAPER/FFA_FINAL_SUBMISSION_PACKAGE/source | 2026-11-13T06:47:04.028385+00:00 | `7a89b18637222653c589c99bf70850e36384e89de9b12c3b6f80bb8bdf115be8` | `b7d3cb778f2f03c3ba9eeb96555be94df9e529b357dd18dcebaf90ec730c52cc` |
| MS03 | PAPER/FFA_FINAL_SUBMISSION_V2 | 2026-11-13T06:47:04.036386+00:00 | `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0` | `b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24` |
| MS04 | PAPER/FFA_FORMATTED_SUBMISSION | 2026-11-13T06:47:04.036386+00:00 | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` | `0be59487f8157147d8d08f9aa99d5ce0b3a023c0c971283d23047c6db78e8023` |
| MS05 | PAPER/FFA_FORMATTED_SUBMISSION/build_modern | 2026-11-13T06:47:04.036386+00:00 | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` | `0be59487f8157147d8d08f9aa99d5ce0b3a023c0c971283d23047c6db78e8023` |
| MS06 | PAPER/FFA_SUBMISSION_STAGING | 2026-11-13T06:47:04.036386+00:00 | `7a89b18637222653c589c99bf70850e36384e89de9b12c3b6f80bb8bdf115be8` | `b7d3cb778f2f03c3ba9eeb96555be94df9e529b357dd18dcebaf90ec730c52cc` |
| MS07 | PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/source | 2026-11-13T06:47:04.044386+00:00 | `614e230683a2fbb3d79cc1419067fa439ea6e14e75edaede10a7ac57a6943d49` | `e612409118715c7d08a6b16a4c06e653ed5b92dc5d5228e8abca17841873c9b2` |
| MS08 | PAPER/FINAL_RESEARCHER_REVIEW_V2/source | 2026-11-13T06:47:04.048386+00:00 | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` | `e05125b84d8ff0c92433d16ea38f52d4e4feec91714c9f3e5355626308a4f63f` |
| MS09 | PAPER/FINAL_RESEARCHER_REVIEW_V3/source | 2026-11-13T06:47:04.048386+00:00 | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` | `2ee3b16218b69b7e6cea0bb75e4e699914b6cc5a07c23dd76e60eda3e36f6cd9` |
| MS10 | PAPER/PHASE14_WORKCOPY | 2026-11-13T06:47:04.048386+00:00 | `614e230683a2fbb3d79cc1419067fa439ea6e14e75edaede10a7ac57a6943d49` | `e612409118715c7d08a6b16a4c06e653ed5b92dc5d5228e8abca17841873c9b2` |
| MS11 | PAPER/PHASE14_WORKCOPY/build_modern | 2026-11-13T06:47:04.048386+00:00 | `614e230683a2fbb3d79cc1419067fa439ea6e14e75edaede10a7ac57a6943d49` | `e612409118715c7d08a6b16a4c06e653ed5b92dc5d5228e8abca17841873c9b2` |
| MS12 | PAPER/PHASE15_WORKCOPY | 2026-11-13T06:47:04.052386+00:00 | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` | `697cbab33a470465cc632a6265941a02ac1575c5815d0f391092b38260801bb9` |
| MS13 | PAPER/PHASE15_WORKCOPY/build_modern | 2026-11-13T06:47:04.052386+00:00 | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` | `697cbab33a470465cc632a6265941a02ac1575c5815d0f391092b38260801bb9` |
| MS14 | PAPER/PHASE16_WORKCOPY | 2026-11-13T06:47:04.052386+00:00 | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` | `e05125b84d8ff0c92433d16ea38f52d4e4feec91714c9f3e5355626308a4f63f` |
| MS15 | PAPER/PHASE16_WORKCOPY/build_modern | 2026-11-13T06:47:04.052386+00:00 | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` | `e05125b84d8ff0c92433d16ea38f52d4e4feec91714c9f3e5355626308a4f63f` |
| MS16 | PAPER/PHASE18_WORKCOPY | 2026-11-13T06:47:04.056386+00:00 | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` | `2ee3b16218b69b7e6cea0bb75e4e699914b6cc5a07c23dd76e60eda3e36f6cd9` |
| MS17 | PAPER/PHASE18_WORKCOPY/build_modern | 2026-11-13T06:47:04.052386+00:00 | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` | `2ee3b16218b69b7e6cea0bb75e4e699914b6cc5a07c23dd76e60eda3e36f6cd9` |
| MS18 | PHASE21_PRIVATE_DATA_ACCESS/compiled | 2026-11-13T06:47:04.068386+00:00 | `c4edc36d420a9bd8cbaafd90daceda4cec9c642f06a5bdedc8233fa6c60062f5` | `11057c04d6a96c0629fcab3daecd990130d620ceb007bf0e66a35ee45b26b803` |
| MS19 | PHASE21_PRIVATE_DATA_ACCESS/staging | 2026-11-13T06:47:04.068386+00:00 | `c4edc36d420a9bd8cbaafd90daceda4cec9c642f06a5bdedc8233fa6c60062f5` | `11057c04d6a96c0629fcab3daecd990130d620ceb007bf0e66a35ee45b26b803` |

### Curated audit mirrors — not four extra author versions

The inventory mirror identifiers `CP01`/`CP02` below are **not** the correction-action identifiers of the same spelling in the master register; their namespace is the version inventory.

The full canonical mirrors CP01/IP01 reproduce MS01. CP02/IP02 contain only the curated MS03 delta (**5 core files**, not the full14); eight section inputs plus the bibliography are mapped to shared canonical sources by the original package's input-resolution table. Their entry-file hash matches MS03, but their partial directory digest does not identify a self-contained manuscript. **Use the complete MS03 recovered source set for any later approved build, not a delta directory alone.**

| ID | Exact root | Observed main mtime UTC | main.tex SHA-256 | Core files |
|---|---|---|---|---|
| CP01 | phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER | 2026-11-13T06:56:33.090963+00:00 | `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` | 14 |
| CP02 | phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER/FFA_FINAL_SUBMISSION_V2 | 2026-11-13T06:56:33.090963+00:00 | `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0` | 5 |
| IP01 | phase0_audit/independent_review/work/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER | 2026-11-13T07:07:51.360000+00:00 | `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` | 14 |
| IP02 | phase0_audit/independent_review/work/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER/FFA_FINAL_SUBMISSION_V2 | 2026-11-13T07:07:51.356000+00:00 | `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0` | 5 |

## 3. Which version corresponds to the completed prior research campaign?

**MS01**, `phase0_audit/extracted/prior_project/PAPER/`, is the preserved Phase8 canonical manuscript with the full completed-campaign theorem/computation sections. Its entry SHA-256 is `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` and its 14-file core digest is `57dd301e63a19f9c89fe0a26978c3ae9eb59294f6573440f6667fbcb276fdf60`. Its [README](evidence/documentary_sources/PAPER/README.md) is an earlier Phase8 record and is not an up-to-date submission-status attestation.

**MS03 is the later documented authoritative staging derivative of that same campaign**, incorporating author/abstract/certification/formatting/data-availability updates through Phase23. The included 28 supplied generator records, q4/q8/q9 routes and historical wider search are the campaign described by these sources; MS03 is not a new P1/P2/P3 manuscript. The existence of a completed campaign does not certify every theorem or mean it is submission-ready.

## 4. Conflicting arguments and why switching folders will not remove HOLD

The [per-version comparison table](evidence/version_comparisons.csv) and [MS03-versus-canonical diff](evidence/version_diffs/MS03_vs_canonical.diff) show exactly which files differ. Across all 19 recovered roots, the core files **§§2–6, §9, §10, Appendix Reproducibility and references.bib are byte-identical** to their canonical counterparts. Thus the nonprincipal-hull family, scalar/module/slot proof obligations, broad alternatingness/congruence consequences and benchmark mistakes are not cured by selecting a later directory.

Between MS01 and MS03:

- `main.tex`: author metadata, abstract and declaration/data-availability blocks differ; the MS03 abstract gives the11/17 quantum-search split instead of the historical three-method overclaim.
- `sections/01_introduction.tex`: updated contribution/certification description.
- `sections/07_quantum.tex`: exponential typesetting only; **the substantive stabilizer, EA and all-route parameter proof defects persist**.
- `sections/08_certification.tex`: historical “all three methods”/worked-example statements are corrected in MS03; route/quotient/bookkeeping defects persist.
- `sections/appendix_tables.tex`: later certification-method explanation/table presentation; it does not recertify all wild/headline claims.

MS04/MS05 are the Phase19 formatting copies; MS09/MS16/MS17 carry the later approved abstract; MS18/MS19 stage private-request data wording; MS03 stages the later public commit-pinned data wording. These sources contain **incompatible data-access declarations** if treated as simultaneously current. The Phase23 record supersedes the earlier statement only for MS03 and keeps its own wording **PROPOSED**. This plan does not select author declarations or conflate formatting/certification updates with repaired mathematics.

The [supplemental source-reading observations](evidence/source_reading_observations.md) refine existing audit action scopes (CP01/03/04/05/08/12/31/40). They flag exact printed proof/type/quantifier obligations, **not** newly supplied proofs or a claim that all manuscript arguments have now been re-audited.

## 5. Compiled PDFs and archival versions

- `phase0_audit/extracted/prior_project/PAPER/main.pdf` is the previously audited lossy patch-text recovery, **not a valid authoritative compiled manuscript**. Observed size617,752 bytes; observed SHA-256 `709fdd7bc52cd66187e39839ad9a5a9eb0c3818b73501270b57aa548ef11faf1`. Its `%PDF` prefix does not repair the binary corruption.
- The Phase23 record claims a42-page/580,019-byte staged PDF with SHA-256 `d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1`. Its actual bytes were **not** recovered/verified here. Treat this as a historical documentary digest, not the hash of an available submitted PDF.
- The patch inventories **11 manuscript-related binary-only paths**:7PDFs and4ZIPs. See [unavailable artifacts](evidence/unavailable_manuscript_artifacts.csv). Other PDFs mentioned in review-package manifests are also not established as recovered valid binaries merely by their names/digests in text.
- Four manuscript archive `.sha256` sidecars survive. Their exact filenames, observed timestamps, sidecar hashes and **unverified inherited target digests** are in [historical archive claims](evidence/historical_archive_digest_claims.csv). None of those four target ZIPs is present. Neither `Matrix Ring.zip` (an empty unrelated archive) nor the literature `Matrix Ring 1.zip` is a manuscript release.
- `PHASE0_COMPLETE_AUDIT_PACKAGE.zip` and `PHASE0_INDEPENDENT_REVIEW.zip` are audit containers with selected sources/evidence, not original author submission archives.

No PDF reconstruction, TeX build or manuscript ZIP reconstruction is authorized or performed in this planning task.

## 6. Submission status — **AUTHOR CONFIRMATION REQUIRED**

The local documentary search covered **209 recovered Markdown records**, plus the source/version inventories and submission-like filenames. See [search rows](evidence/submission_documentary_search.csv) and [scope summary](evidence/manuscript_inventory_summary.json). Findings:

1. The [earlier final-submission package README](evidence/documentary_sources/PAPER/FFA_FINAL_SUBMISSION_PACKAGE/README.md) explicitly calls itself preparation and says no submission was made/authorized.
2. [Phase21](evidence/documentary_sources/PHASE21_PRIVATE_DATA_ACCESS/PHASE21_FINAL_DECISION_REPORT.md), §6, says nothing was submitted and no Editorial Manager account existed **at that historical stage**.
3. The later [Phase23 data statement](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md), §B6, says “Submitted anything — No”; §B8 still awaits researcher/editorial confirmation.
4. [Phase23 Option-C record](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_FFA_OPTION_C_COMPLIANCE.md), Appendix E, marks its email **DRAFT — NOT SENT**. No editorial acceptance/exception follows from the manuscript phrase “referred for editorial confirmation.”
5. No verified journal receipt, manuscript/submission identifier, dated editorial decision or acceptance letter was located. No journal account, email service, current submission portal or private author records were accessed. Historical data publication on GitHub is not manuscript submission.

Therefore the documents support **historical non-submission/preparation**, not an unconditional claim about today's private author actions. Current submission status, any later version and exact submitted PDF/source identity remain **AUTHOR CONFIRMATION REQUIRED**. A missing local receipt does not prove no external submission occurred.

## 7. Consequence for this plan

Use **MS03** for exact line/label locators and planned successor work **subject to fresh author confirmation**. Preserve MS01 and every other snapshot as immutable history. Confirm existing authorship/declaration approvals rather than inventing new ones. Do not compile, change claims, send an editorial message, submit, create a release, commit or push without separate explicit authorization.

**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**
