# Phase 12 / Task G — Final LaTeX compilation report

**STATUS: VERIFIED — a genuine TeX Live 2024 compilation completed successfully
after the confirmed declarations were inserted.**

Date: 2026-11-10.

## 1. Toolchain

| component | version |
|---|---|
| pdfTeX (driving `pdflatex`) | **3.141592653-2.6-1.40.26 (TeX Live 2024)** |
| Preloaded format | `pdflatex 2024.5.1` |
| BibTeX | **0.99d (TeX Live 2024)** |
| kpathsea | 6.3.6/dev (binaries 6.4.0) |
| Bibliography style | `plain.bst` |

Real TeX Live 2024 components, assembled by
`PAPER/compile/bootstrap_texlive.sh`.

## 2. Cycle

```
cd PAPER/FFA_SUBMISSION_STAGING
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

which runs, with `SOURCE_DATE_EPOCH=1794268800` pinned for reproducibility:

```
pdflatex main.tex  →  bibtex main  →  pdflatex main.tex  →  pdflatex main.tex
```

**Genuine BibTeX.** The build directory is deleted and repopulated from
`main.tex`, `references.bib` and `sections/` on every run, so no pre-existing
`.bbl` can be used as a shortcut. BibTeX consumed all **13** entries from
`references.bib` via `plain.bst` and produced a **78-line** `main.bbl`.

## 3. Result — this build

| metric | value |
|---|---|
| Errors (`^!`) | **0** |
| Undefined citations | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| Missing characters | **0** |
| LaTeX/package warnings | **0** |
| Font warnings | **0** |
| Pages | **42** |
| PDF bytes | 576 194 |
| **PDF SHA-256** | `72bfa79dd0f08d11dc559febd923ce4351993f6dfd4989ae80233845946d20e0` |

### Independent validation

| tool | verdict |
|---|---|
| `PAPER/tools/check_log.py` | **VERDICT: clean** (0/0/0/0/0) |
| `PAPER/tools/validate_latex.py` | **13 checks, 13 PASS, 0 FAIL** |
| `PAPER/tools/inspect_pdf.py` (PyMuPDF) | **issues found: 0**; title, abstract, keywords, TOC, References and all 6 tables present; 13 bibliography entries rendered |

## 4. PDF history — all versions preserved

| phase | SHA-256 | pages | notes |
|---|---|---|---|
| Phase 8 (canonical) | `b2ba1fee72b6e70ae18f3f043c10ac3390673281e1d0ccd35da3f863d8641a03` | — | original, untouched |
| Phase 11 (first staging build) | `90379dbed85601128f5ea42fbd2742b6950fafe437d74254406be1920069e72e` | 42 | superseded |
| Phase 11 (after EA-code restoration) | `519513ba620660a5f673a52b562fe03caaa511b877a7330d1c8307c0ec07583c` | 42 | superseded |
| **Phase 12 (final)** | **`72bfa79dd0f08d11dc559febd923ce4351993f6dfd4989ae80233845946d20e0`** | **42** | current |

Logs and `.bbl`/`.blg` for the current build are archived in
`PAPER/FFA_FINAL_SUBMISSION_PACKAGE/build/`.

## 5. Title-page inspection

The title page renders as:

```
Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings

[GIVEN NAME] [FAMILY NAME]

[DEPARTMENT OR SCHOOL], [UNIVERSITY OR ORGANISATION],
[FULL POSTAL ADDRESS], [COUNTRY]
```

Placeholders are **visible and unresolved**, exactly as intended. They are
correctly positioned per FFA requirements: author names below the title,
affiliation below the author names. The corresponding-author email macro is
defined but not yet rendered, pending confirmation.

## 6. Declaration-section inspection (page 37)

Verified by text extraction from the compiled PDF:

* **Acknowledgements** — present, marked pending (optional).
* **Declaration of competing interests** — present, **confirmed text rendered**.
* **Funding** — present, **confirmed text rendered**.
* **Author contributions (CRediT)** — present, marked pending (encouraged).
* **Data availability** — present, marked pending (mandatory).
* **Declaration of generative AI…** — present, marked pending (mandatory).

All six appear **before the reference list**, as Elsevier requires.

## 7. Examples and appendices

All **13** worked examples compile and render. Appendix A (certification table
and comparison data) and Appendix B (reproducibility) are present. All 6
tables render. The bibliography renders 13 entries.

## 8. Reproducibility

```sh
cd PAPER && sh compile/bootstrap_texlive.sh
cd FFA_SUBMISSION_STAGING && TL=/home/user/texlive2024 sh compile/build_modern.sh
```

With `SOURCE_DATE_EPOCH=1794268800` the PDF should hash to
`72bfa79d…46d20e0`.

## 9. Status

**VERIFIED.** Clean build, genuine BibTeX, no unresolved compiler error, no
missing glyph, no overfull or underfull box. All required elements inspected
and present.
