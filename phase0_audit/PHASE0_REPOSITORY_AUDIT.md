# PHASE 0 — REPOSITORY AUDIT

**Project:** Quantum Error-Correcting Codes from (k)-Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings
**Date:** 2026-11-12 · **Branch:** `arena/7d88376d-matrix-ring` (base commit `12db091`, sole commit `12db091 "Add files via upload"`)
**Mode:** strictly read-only inspection of all pre-existing materials; every audit output is confined to `phase0_audit/`.
**Status of originals:** verified unchanged — `git status --short` shows only `?? phase0_audit/`; the `research-data/` SHA-256 manifest re-verified with **0 non-OK lines (87/87 OK)** after the audit.

---

## 1. Method and integrity evidence

1. Full inventory of the repository root, both ZIP archives, the `.patch` file, and `research-data/`.
2. `Matrix Ring 1.zip` extracted read-only into `phase0_audit/extracted/literature/` (7 PDFs, 6.1 MB uncompressed).
3. The 21 MB patch `01a1a47c-f51d-7d7c-810c-207359de606f.patch` (435 957 diff lines, 1315 `diff --git` entries) parsed read-only; **1150 text files reconstructed** into `phase0_audit/extracted/prior_project/`; 165 binary-only paths listed in `phase0_audit/extracted/patch_binary_files.txt` (binaries are NOT reconstructible from the patch and were not needed).
4. All 7 literature PDFs converted to text (`phase0_audit/pdfs_text/`, `pypdf` in an isolated venv) and identified from their own front matter.
5. **Integrity re-verification:** `sha256sum -c research-data/PUBLICATION_MANIFEST.sha256` → all **87 entries OK**.
6. **Independent re-execution:** the data package's own `research-data/scripts/phase0_feasibility.py` was run on this machine (Python 3.11.2, exit 0, 15.9 s). Output is byte-identical to the recorded log except 3 cosmetic lines (run date, elapsed time, log path). Evidence: `phase0_audit/evidence/phase0_feasibility_rerun_2026-11-12.txt`, `phase0_audit/evidence/phase0_rerun_diff_vs_recorded_log.txt`.
7. Cleanup: the rerun wrote a log copy and a `__pycache__` inside `research-data/scripts/`; both were **deleted**, restoring the package to its exact prior state (see status line above).

## 2. Root inventory

| Item | Size | Role |
|---|---:|---|
| `README.md` | 24 B | stub ("# Matrix-Ring / Research") |
| `Matrix Ring 1.zip` | 3.83 MB | literature bundle: **7 PDFs** (see §4) |
| `Matrix Ring.zip` | 178 B | **empty archive** (single 0-byte directory entry `Matrix Ring/`); non-informative — recorded as an artefact anomaly |
| `2602.18255v1 (1).pdf` | 437 552 B | arXiv preprint; byte-duplicate of the copy inside the zip |
| `s11128-026-05230-0 (3).pdf` | 446 086 B | Springer QIP article; byte-duplicate of the zip copy |
| `01a1a47c-...patch` | 21.3 MB | **complete snapshot of a prior research environment** (see §3) |
| `research-data/` | 2.1 MB | **published reproducibility package: 86 files** (see §5) |

Git history: a single squashed upload commit; the prior campaign's internal commit references (e.g. `3752a6c…`, `e41c571…`, `1327b26`) are **not present** in the local history — the patch file is the only carrier of the prior environment.

## 3. THE DECISIVE FINDING: a complete prior research campaign exists in this repository

The patch and `research-data/` together document a **finished, audited, manuscript-complete prior project** whose working title is:

> **"Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings"**
> — Arun Kumar Yadav, K.R. Mangalam University; manuscript prepared for *Finite Fields and Their Applications* (Elsevier).

This is the present blueprint's topic **verbatim except for the "(k)-" prefix**, which is a *notation change only*: the prior project uses a general Galois parameter `s` (equivalently ℓ), with its old blueprint explicitly mandating *"use t for the nilpotency exponent and s (or ℓ) for the Galois automorphism parameter. Do not use k for both."*

The prior campaign's phase map (all reconstructed from the patch):

| Cluster | Contents (reconstructed file counts) |
|---|---|
| `00_BLUEPRINT` | the prior research blueprint (Arena AI × ChatGPT gated workflow, researcher = final approver) + full extracted text |
| `01_LITERATURE` | verified annotated bibliography, comparison matrix, `references.bib` (**37 entries**, each with a `VERIFY` tag) |
| `02_PHASE_REPORTS/Phase_0` | Phase 0 report, revision report, Alahmadi-theorem reconciliation, nontrivial-Galois experiments, **updated final recommendation (MODIFY→GO)** |
| `03_THEOREMS` | **15 documents** incl. `PAIRING_COMPLETE_PROOFS.md`, Stage 1 (cyclic shift), 2A (Morita generators), 2B (CRT/Hensel principality), 2C (Galois duality), 3A (hull structure), 3B (hull enumeration), Phase 4 (Gray-map compatibility), Phase 5 (quantum constructions), Phase 6 (parameter enhancement), Phase 7 (extended search), and an **Updated Theorem Register (≈ 187 KB, registers T-…, N1–N12, C1–C4, O-…)** |
| `04_COMPUTATION` | **45 files** — all scripts + verbatim logs, seeds recorded |
| `06_AUDIT` | **13 audit documents** incl. independent audit report, proof verification, novelty statement (`[PUB]/[NEW]/[CMP]/[TOP]` classification), final GO/MODIFY/STOP |
| `PAPER/` | complete LaTeX manuscript `main.tex` + 12 sections + 2 appendices (`01_introduction … 10_conclusion`, reproducibility & tables appendices), compilation toolchain, **four successive FFA submission packages** (`FFA_SUBMISSION_STAGING`, `FFA_FORMATTED_SUBMISSION`, `FFA_FINAL_SUBMISSION_PACKAGE`, `FFA_FINAL_SUBMISSION_V2`), three researcher-review versions (V1–V3), workcopies through "Phase 18" |
| `PHASE9A/9 … PHASE23` | journal selection audit, FFA submission audit/finalization/prep, final integration, review, corrections, certification documentation, researcher decision, **private-data-access staging, GitHub data publication, FFA finalization (Option-C data-compliance: "conditionally acceptable — editorial confirmation required")** |

### 3.1 What the prior campaign established (quoted from its own audit, `06_AUDIT/PHASE0_FINAL_NOVELTY_STATEMENT.md`, box [NEW] — proofs in `03_THEOREMS/`)

N1 `θ_s = σ_s ∘ transpose` is an anti-automorphism of `M_{m_old}(A_t)`, `θ_s² = σ_{2s}`, involution ⟺ `r_old | 2s` · N2 key symmetry identity · N3 non-degenerate pairing, right-module dual, size formula `|C|·|C^{⊥_s}| = |R|^n` · N4 double dual `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` (verified 6961/6961) · N5 reflexivity criterion with counterexample family · N6 `σ`-isometry equivariance of weights/duals/hulls · N7 parameter invariance in the non-reflexive regime · N8 cyclicity of the Galois dual · N9 R-valued = F_q-valued orthogonals · N10 arbitrary τ ∈ Aut(A_t) generalization · N11 parameter trichotomy (`r_old = 1` trivial; `r_old` odd ⇒ Galois nontriviality and reflexivity mutually exclusive; `r_old` even ⇒ unique midpoint) · N12 Galois hulls of cyclic codes are cyclic, σ-equivariant.

Further register highlights: dual formula `C^{⊥_s} = rev(ann_r(θ_s C))` (Stage 2C Thm 3.8); Morita correspondence `C = I_W`, W a B-submodule of `B²`, B = A_t[X]/⟨X^n−1⟩ (Stage 2A); CRT/Hensel principality with squarefree/semisimple hypotheses (T-021 conditional; counterexample `q=4,n=2`: 33 ≠ 49 codes); **Gray map φ_n with a proved transported pairing** (T-176…T-189; 463/463 checks PASS, byte-reproducible); **hulls need not be principal** (T-173; phenomenon confined to `t ≥ 2` and `p | n`).

### 3.2 Computational evidence shipped (`research-data/`, integrity-verified)

- 22 pure-standard-library Python scripts (`matrix_ring_lib.py` implements F_q, A_t, R, R_n from first principles — deliberately no CAS), 23 verbatim logs, fixed seeds, deterministic replay procedure documented.
- **28 certified quantum codes** with generator matrices (`distance_certificates/certified_codes.csv`): stabilizer/self-orthogonal route (e.g. `[[24,8,4]]_9`, `[[20,4,4]]_4`), dual-containing CSS route, and entanglement-assisted route up to `[[20,2,10;18]]_4` and `[[24,2,10;18]]_9`. Distances certified by M1 (complete enumeration) or M2 (support search), cross-checked by M3 (independent ambient quantum search; exact for 11, proved lower bound for 17; **no code by all three** — stated with unusual honesty).
- 42-family census (15 families not enumerable — recorded as blocked), Pareto frontier, entanglement budget, non-principal-hull witnesses (μ_B ≥ 3 at t = 2), Grassl-table comparisons for q = 4 (8 rows: record-equal at d = 2; otherwise 1–2 below best known) and q = 9 (3 rows: 1–2 below); q = 8 not tabulated at codetables.de; **entanglement-assisted external table does not exist (HTTP 404) — EA codes unbenchmarked** (documented limitation).

### 3.3 Submission status

The trail reaches **submission preparation for FFA**, with a data-availability compliance item still marked *"PROPOSED — FFA POLICY CONFIRMATION PENDING"* (Phase 23, dated 2026-11-10). **No artefact in this repository records actual submission, a manuscript number, or an editorial decision.** The author must confirm the true status; everything downstream of this audit depends on it (§7 of the Decision Report).

## 4. Literature bundle (`Matrix Ring 1.zip`) — identified items

| File (in zip) | Identified as | Venue/DOI (as printed) |
|---|---|---|
| `s11128-026-05230-0 (3).pdf` | Joshi–Patel–Prakash, **"Quantum codes construction from cyclic codes over matrix rings"** | *Quantum Inf. Process.* **25**:207 (2026), DOI 10.1007/s11128-026-05230-0 |
| `2602.18255v1 (1).pdf` | Joshi–Patel–Prakash, "Construction of cyclic codes over a class of matrix rings" (M₄(F₂[u]/⟨uᵏ⟩)) | arXiv:2602.18255v1 (Feb 2026) |
| `s12095-022-00572-9 (3).pdf` | Patel–Prakash–Islam, "Cyclic codes over M₄(F₂+uF₂)" | *Cryptogr. Commun.* (2022), DOI 10.1007/s12095-022-00572-9 |
| `s12190-018-01235-w (1).pdf` | Pal–Bhowmick–Bagchi, "Cyclic codes over M₄(F₂)" | *J. Appl. Math. Comput.* 60:749–756 (2019), DOI 10.1007/s12190-018-01235-w |
| `s13226-021-00014-x (2).pdf` | Islam–Prakash–Bhunia, "On the structure of cyclic codes over M₂(F_p+uF_p)" | INSA journal (2021), DOI 10.1007/s13226-021-00014-x |
| `algebraic-structure-of-cyclic-codes-over-m3fp.pdf` | Islam–Prakash–Bhunia, "Algebraic structure of cyclic codes over M₃(F_p)" | preprint-style, venue unconfirmed |
| `Construction_of_Codes_Over_…M_3(F_pu_F_pu2_F_p)….pdf` | Patel–Joshi–Prakash, "Construction of codes over F_{p³} from cyclic codes over M₃(F_p+uF_p+u²F_p)" | conference-style, venue unconfirmed |

Details and overlap analysis: `PHASE0_LITERATURE_REVIEW.md`.

## 5. Missing or inaccessible materials (explicit record)

1. **Magma, SageMath, GAP:** absent from this environment. The prior package is deliberately pure-Python (no CAS) — this remains the viable toolchain.
2. **Scholarly databases / publisher sites / codetables.de / arXiv fetch:** blocked from the sandbox (only github.com, registry.npmjs.org, pypi.org reachable). A platform web-search tool *was* usable and was used to verify three critical records (see Literature Review); full re-verification of all 37 prior bib entries online was not possible here.
3. **Google Drive connector:** connected but **turned OFF** for this conversation — any Drive-resident materials were unavailable. (Not needed for this phase; flagged for the author.)
4. The prior environment's binary artefacts inside the patch (compiled `main.pdf` etc.) are not reconstructible from the patch alone; the source tree is complete (1150 text files).
5. No licence file anywhere in the repository (the `research-data/README.md` explicitly reserves all rights).

## 6. Conclusion of the repository audit

The repository does **not** contain a blank canvas; it contains a **completed, independently audited, computation-certified research project reaching the FFA submission-preparation stage on exactly the blueprint's topic**. Phase 0's most consequential output is this fact. All "new-implementation" decisions must be made against this baseline to avoid duplicating the author's own finished work (self-overlap), and to avoid redundancy against the external 2026 literature that post-dates or complements it (QIP 25:207).

**Files created by this audit (all under `phase0_audit/`):** this report; the five companion reports; `extracted/literature/` (7 PDFs); `extracted/prior_project/` (1150 reconstructed files); `extracted/patch_binary_files.txt`; `pdfs_text/` (7 texts); `evidence/` (2 re-run evidence files). Nothing else in the repository was created, modified, renamed or deleted.
