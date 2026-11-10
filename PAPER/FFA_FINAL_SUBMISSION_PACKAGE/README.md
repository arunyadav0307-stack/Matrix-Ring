# FFA final submission package

Manuscript: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings*
Target: **Finite Fields and Their Applications** (Elsevier)

**STATUS: CONDITIONALLY READY — SPECIFIC CONFIRMATIONS PENDING.**
This is a preparation package. **No submission has been made or authorized.**

Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring` · Commit: `a731ac7`

---

## What is still missing

Six blocking items require facts only the researcher holds, or authorization
for actions with external consequences. **Nothing has been invented to fill
them.**

| # | blocking item |
|---|---|
| 1 | Author **name** |
| 2 | Author **affiliation** (institution, dept, street, city, state, country) |
| 3 | Corresponding-author **email** (publishable) |
| 4 | **Data-availability statement** — GitHub-only route chosen; needs the `main`-branch gap fixed |
| 5 | **Generative-AI declaration** — needs the tool name(s) |
| 6 | **Research-data accessibility** — follows from item 4 |

See `PHASE12_RESEARCHER_ACTION_ITEMS.md` at the repository root under
`PHASE12_FFA_SUBMISSION_PREP/`.

---

## Contents

| # | required component | location |
|---|---|---|
| 1 | Final LaTeX source | `source/main.tex`, `source/references.bib`, `source/main.bbl` |
| 2 | All section and appendix files | `source/sections/` (12 files) |
| 3 | Final bibliography | `source/references.bib` + `source/main.bbl` (13 entries) |
| 4 | Compiled PDF | `build/manuscript.pdf` (42 pp) |
| 5 | Supplementary scripts | `supplementary/scripts/` (22) |
| 6 | Computational logs | `supplementary/logs/` (23) |
| 7 | Generator matrices | `supplementary/generator_matrices/` (29) |
| 8 | Reproduction instructions | `supplementary/README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md` |
| 9 | Data-availability statement | `declarations/01_data_availability.md` — **PENDING** (GitHub-only route chosen) |
| 10 | Competing-interest declaration | `declarations/02_competing_interests.md` — **CONFIRMED** |
| 11 | Funding declaration | `declarations/03_funding.md` — **CONFIRMED** |
| 12 | Generative-AI declaration | `declarations/04_generative_ai.md` — **PENDING — UNRESOLVED DISCREPANCY** |
| 13 | Final author metadata | `declarations/05_author_metadata.md` — **CONFIRMED** |
| 14 | Final compliance matrix | `PHASE12_FINAL_READINESS_AUDIT.md` (see below) |
| 15 | SHA-256 manifest | `SHA256_MANIFEST.txt` |
| 16 | This README | `README.md` |

Items 14's full detail, plus the confirmation register, change record, deposit
plan, manuscript check, build report, action items and decision report, live in
`PHASE12_FFA_SUBMISSION_PREP/` at the repository root.

---

## Declaration status at a glance

| declaration | status |
|---|---|
| Competing interests | ✅ **CONFIRMED** — "no known competing financial interests…" — already in the PDF |
| Funding | ✅ **CONFIRMED** — "did not receive any specific grant…" — already in the PDF |
| Data availability | ⏳ **PENDING** — no deposit exists |
| Generative AI | ⏳ **PENDING — DISCREPANCY** — researcher says language-only; records show broader use |
| Acknowledgements | ⏳ PENDING (optional) |
| CRediT contributions | ⏳ PENDING (encouraged) |

---

## Build

```sh
cd PAPER
sh compile/bootstrap_texlive.sh                 # if /home/user/texlive2024 is absent
cd FFA_SUBMISSION_STAGING
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

Real TeX Live 2024: pdfTeX 1.40.26, BibTeX 0.99d, four-pass cycle
(`pdflatex → bibtex → pdflatex → pdflatex`), `SOURCE_DATE_EPOCH=1794268800`.

| metric | value |
|---|---|
| Errors / warnings / overfull / underfull / missing glyphs | **0 / 0 / 0 / 0 / 0** |
| Pages | **42** |
| PDF SHA-256 | `72bfa79dd0f08d11dc559febd923ce4351993f6dfd4989ae80233845946d20e0` |

Logs: `build/main.log`, `build/main.bbl`, `build/main.blg`.

---

## Source of the files

All content derives from `PAPER/FFA_SUBMISSION_STAGING/`, which is itself an
isolated copy of the canonical `PAPER/`. **The canonical manuscript is
untouched** — `PAPER/main.tex` remains byte-identical to its pre-Phase-11
state (SHA-256 `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c`).

---

## What NOT to submit yet

* The PDF contains **visible placeholders** on the title page
  (`[GIVEN NAME] [FAMILY NAME]`, `[FULL POSTAL ADDRESS]`, `[COUNTRY]`).
* The data-availability and generative-AI sections are marked as requiring
  confirmation.
* Highlights (3–5 bullets, ≤ 85 chars, separate file with "highlights" in the
  name) are **not yet written** — FFA encourages them.
* Per-file supplementary captions are **not yet written** — FFA requires them.
