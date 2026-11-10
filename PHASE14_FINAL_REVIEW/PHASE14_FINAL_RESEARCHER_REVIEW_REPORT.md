# PHASE 14 — FINAL RESEARCHER REVIEW REPORT

Date: 2026-11-10
**Branch:** `arena/59de606f-matrix-ring`
**Base commit:** `19a76e1` (Phase 13)
**Working copy:** `PAPER/PHASE14_WORKCOPY/` (isolated; canonical manuscript untouched)

---

## 1. Identification and counts

| metric | value |
|---|---|
| Branch | `arena/59de606f-matrix-ring` |
| Commit | `19a76e1eb31700bc87fed29975477f123f26817e` |
| Manuscript pages | **42** |
| Manuscript words (sections, approx.) | **18,722** |
| Theorem-like statements | **83** |
| — theorems | 21 |
| — lemmas | 11 |
| — propositions | 9 |
| — remarks | 19 |
| — examples | 13 |
| — definitions | 8 |
| — corollaries | 2 |
| Worked examples | **13** |
| Verified references | **13** (13 cited, 13 in `.bib`, 0 orphans, 0 missing) |
| Labels | 116, **0 duplicates** |
| Certified quantum codes | **28** |
| — exact-distance constructions | **28** (each has M1 or M2 exact) |
| — lower-bound-only constructions | **0** (all 28 have an exact method) |
| — M3 lower-bound-only rows | 17 of 28 (M3 is a cross-check, not the primary certificate) |
| Route breakdown | SO 2, DC 1, EA 25 |
| Supplementary files | **86** |
| Manifest entries | **85**, all verified |
| PDF SHA-256 | `a021cf4b456377725f5db099368fe2ce6aa3a999339f3f93a9ea09b52c9db64c` |
| PDF size | 578,268 bytes |

---

## 2. Task results

### Task A — Author and title page — **VERIFIED**

| check | result |
|---|---|
| Author name spelling | ✅ `Arun Kumar Yadav` |
| Institutional name | ✅ School of Basic and Applied Sciences, K.R. Mangalam University |
| Full postal address + country | ✅ Sohna Road, Gurugram, Haryana, 122103, India |
| Corresponding-author identification | ✅ rendered as "Corresponding author. E-mail: …" |
| Email rendering | ✅ `arunyadav0307@gmail.com` |
| Single-author formatting | ✅ one author; affiliation marked with superscript `a` |
| Unconfirmed author metadata | ✅ **none in the body text**; one defect found and fixed (below) |
| Title and section ordering | ✅ title unchanged; section order intact |
| ORCID | ✅ **not invented** — none supplied |

**Defect found and CORRECTED (PDF metadata only):** the PDF's embedded
`/Author` field read `[AUTHOR METADATA TO BE SUPPLIED]`, because
`\hypersetup{pdfauthor={\AUTHORPLACEHOLDER}}` still pointed at the placeholder
macro. Fixed by moving the confirmed author macros into the preamble and
pointing `pdfauthor` at `\AUTHORONE`. The PDF now reports **Arun Kumar Yadav**.

### Task B — Abstract and presentation — **VERIFIED**

| convention | count | limit |
|---|---:|---:|
| C1 | **213** | 250 |
| C2 | **199** | 250 |
| C3 (strictest) | **226** | 250 |

All three match the reported values exactly. **Compliant**, margin 24 on the
strictest. Title, keywords (7), introduction, contributions, research-gap
statement, conclusion and references all inspected. **No new novelty claim and
no record-parameter claim was introduced**; the manuscript states "No record
parameters are claimed."

### Task C — Mathematical consistency audit — **1 ISSUE FOUND (CP-1)**

All core formulas verified present and internally consistent:
`R = M_2(A_t)`, `A_t = F_q[u]/⟨u^t⟩`, `θ_s = σ_s ∘ (·)^T`, `N = 4tn`, Hankel
Gram `I_{4n} ⊗ H_t`, `c = k − h_E`, `K = N − k − h_E`, coset Singleton
`K + d ≤ N + 1`, EA Singleton `N − K + c ≥ 2(d−1)`, right-ideal convention,
Gray image in `F_q^N`, `F_p`-basis commutation testing.

O-3.1 interpretation is correct and matches the record: **O-3.1a refuted**
(Theorem `thm:nonprincipal`), **O-3.1b open** (Remark `rem:o31b`).

Numeric verification: `tools/verify_examples.py` → **56 checks, 0 mismatches**.

**Issue:** the "three independent methods" claim overstates per-code
certification. See **CP-1**. **Not applied** — reported for approval.

### Task D — Worked examples — **VERIFIED, 1 ISSUE (CP-2)**

All 13 examples located and enumerated with labels.

| # | file | label |
|---|---|---|
| 1 | 03_preliminaries | `ex:ring` |
| 2 | 03_preliminaries | `ex:crt` |
| 3 | 04_cyclic_galois | `ex:dual` |
| 4 | 04_cyclic_galois | `ex:nonreflexive` |
| 5 | 05_hulls | `ex:lcd` |
| 6 | 05_hulls | `ex:sd` |
| 7 | 05_hulls | `ex:witnessA` |
| 8 | 05_hulls | `ex:witnessB` |
| 9 | 06_gray | `ex:gray` |
| 10 | 06_gray | `ex:obstruction` |
| 11 | 07_quantum | `ex:fpbasis` |
| 12 | 07_quantum | `ex:routes` |
| **13** | **08_certification** | **`ex:certify`** |

**Example 13 (`ex:certify`) reconstructed from committed source data** —
`certified_codes.csv` row `[[20,2,10;18]]_4` and Phase-7 log line 454. Every
quantity recomputed independently and **agrees exactly**:
`c=18`, `K=2`, `d=10`, EA Singleton `36 ≥ 18` (defect 18), EA Hamming holds,
coset Singleton `12 ≤ 21`, `k` even, `K−c = −16 = N−2k` divisible by 4,
`c+K = 20 = N−2h_E`. The generator matrix for this exact code (not a
re-selected one with identical parameters) is `04_20_2_10-18_4_(4,1,5)_EA.json`.

**Issue:** `ex:certify` credits method M2, but M2 = `n/a` for that code. See
**CP-2**. Not applied.

*Note on the task's "Section 7, Example 13":* Section 7 contains Examples
**7.11** (`ex:fpbasis`) and **7.12** (`ex:routes`); the 13th example in document
order is `ex:certify` in Section 8 (rendered 8.12). Both readings were
verified — `ex:routes` numerically and `ex:certify` fully.

### Task E — Quantum parameter tables — **VERIFIED**

`tools/verify_examples.py` reconciled the 18 headline rows and all 28 rows of
`certified_codes.csv`: route bookkeeping `(K, c, h_E)` and EA Singleton defect
recomputed — **consistent on every row**. Phase 6 and Phase 7 corrections
(`c + K = N − 2h_E`, the corrected bookkeeping identity) are reflected
consistently; `ex:certify` explicitly notes the old formula `c+K = N−k` would
give `20 = 2`, which is false. **No improvement over known records is claimed.**

### Task F — References, equations, cross-references — **VERIFIED, 1 minor (CP-4)**

| check | result |
|---|---|
| Citations resolve | ✅ 13/13, 0 undefined |
| Every `.bib` entry cited | ✅ 13/13, no orphans |
| Author names / venues consistent | ✅ venue attributions verified in Phase 11 |
| DOIs correct where available | ⚠️ 9 in source, **0 rendered** — see CP-4 |
| Theorem/equation/table/example refs resolve | ✅ 0 undefined |
| Duplicate labels | ✅ **none** (116 labels) |
| Missing equations or references | ✅ none |
| Obsolete Phase 9 attributions | ✅ **none** in the manuscript |

`references.bib` **preserved unchanged** — no bibliographic error demonstrated.

### Task G — PDF build and inspection — **VERIFIED**

Four-pass build with genuine BibTeX:

| metric | result |
|---|---|
| Compilation errors | **0** |
| Undefined citations | **0** |
| Undefined cross-references | **0** |
| Missing glyphs | **0** |
| Duplicate labels | **0** |
| Overfull boxes | **0** |
| Underfull boxes | **0** |
| Pages | **42** |
| PDF SHA-256 | `a021cf4b…c9db64c` |

Programmatic layout inspection performed:
* **0 text blocks exceed the page margins** (A4, 595.3 × 841.9 pt).
* Fonts: exclusively Computer Modern (CMR/CMMI/CMTI/CMSY/CMBX) — **no
  substitution, no fallback fonts**.
* **No empty or near-empty pages.**
* Tables 1–6 all render; appendices A and B present.

> ⚠️ **Honest limitation:** the task requires visual inspection. **I have no
> vision capability — I cannot see rendered pages.** What was performed is
> text extraction plus geometric layout analysis (block bounding boxes, font
> inventory, margin-overflow detection). This verifies structure, geometry and
> content, but it is **not equivalent to a human looking at the pages**. A
> human visual pass is still **RESEARCHER REVIEW REQUIRED**.

**Minor finding:** appendix tables render as Table 5–6 rather than A.1–A.2
(FFA's guide specifies `Table A.1`). See **CP-3**, not applied.

### Task H — Supplementary package integrity — **VERIFIED**

| check | result |
|---|---|
| Scripts present | ✅ **22** |
| Logs present | ✅ **23** |
| Generator matrices present | ✅ **29** (28 + INDEX) |
| Parameter tables | ✅ **8** |
| Documentation | ✅ **4** |
| Distance-certification evidence | ✅ `certified_codes.csv`, `CERTIFICATION_PROCEDURE.md`, Part 6 of the Phase-7 log |
| Reproduction instructions | ✅ `README.md`, `ENVIRONMENT.md` |
| File counts accurate | ✅ **86** total |
| `MANIFEST.sha256` | ✅ **85/85 verified, 0 mismatches, 0 missing** |
| Obsolete/misleading files | ⚠️ one generated artefact found and removed (below) |
| Historical logs preserved | ✅ untouched |

**Cleanup:** a `scripts/__pycache__` directory (3 `.pyc` files) had been
created by my own verification run. It was untracked, already gitignored
(`PAPER/.gitignore:12`), and absent from the manifest. Removed, restoring the
package to its true 86-file content. **No source code or computational result
was altered.**

### Task I — Review package — **VERIFIED**

`PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` created: **113 files**, all hashes
verified, with a README giving exact reproduction instructions.

---

## 3. Outstanding issues

| id | issue | status |
|---|---|---|
| **CP-1** | "Three independent methods" overstates per-code certification (0 of 28 codes have all three) | **RESEARCHER REVIEW REQUIRED** |
| **CP-2** | `ex:certify` credits method M2, which is `n/a` for that code | **RESEARCHER REVIEW REQUIRED** |
| **CP-3** | Appendix tables numbered 5–6, not A.1–A.2 | **OPEN** (cosmetic) |
| **CP-4** | 9 DOIs in source, 0 rendered by `plain.bst` | **OPEN** (minor; FFA restyles at proof) |
| — | Generative-AI declaration: researcher's account contradicts the record | **BLOCKING** (from Phase 13) |
| — | Data availability: GitHub-only; data absent from `main` branch | **BLOCKING** (from Phase 13) |
| — | Human visual inspection of the PDF | **RESEARCHER REVIEW REQUIRED** (I cannot see images) |

---

## 4. Final recommendation

> ## The manuscript is READY FOR THE RESEARCHER'S FINAL READING.

The mathematics, the examples, the parameter tables, the references, the
cross-references and the supplementary package are **internally consistent and
reproducible**: 56/56 automated checks pass, 85/85 manifest entries verify, the
build is clean at 0 errors and 0 warnings, and every protected file is
byte-identical to its pre-Phase-14 state.

Four issues are recorded and **none has been applied**. Two (CP-1, CP-2)
concern how the certification is *described* and deserve the researcher's
attention before submission, particularly CP-1, which sits in the abstract.
Two (CP-3, CP-4) are cosmetic.

Two items remain **BLOCKING** but are external to the manuscript: the
generative-AI declaration and the data-availability statement — both carried
from Phase 13 and both requiring the researcher's decision.

One honest caveat: **I could not visually inspect the rendered PDF.** Layout
was verified geometrically, not visually.

---

## 5. Repository safeguards

| check | result |
|---|---|
| Canonical `PAPER/main.tex` | ✅ unchanged (`ee47ce7e…4501737c`) |
| `references.bib` | ✅ unchanged (`73388338…d22feb`) |
| `main.pdf` (Phase 8) | ✅ unchanged (`b2ba1fee…8641a03`) |
| `main.bbl` | ✅ unchanged (`23074d10…477b2d3`) |
| 12 section files | ✅ all unchanged |
| Phase 8 / 8A / 8B archives | ✅ all present and pass `unzip -t` |
| Historical computational logs | ✅ untouched |
| Changes made | **one**, in the isolated working copy: PDF `/Author` metadata |
| Commits | normal fast-forward only |
