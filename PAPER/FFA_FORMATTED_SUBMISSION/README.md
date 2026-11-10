# FFA-formatted submission copy — Phase 19

*Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*
Target journal: **Finite Fields and Their Applications** (Elsevier)

Derived from `PAPER/FINAL_RESEARCHER_REVIEW_V3/` (Phase 18, approved abstract
Option B). **V3 is preserved unchanged.**

## What is different from V3

**Exactly one change to the manuscript source**, plus the submission documents:

| change | file | requirement |
|---|---|---|
| `e^{2\pi i x/p}` → `\exp(2\pi i x/p)` | `sections/07_quantum.tex` | FFA "Math formulae": *"Denote powers of $e$ by exp."* |

No mathematical content changed. Everything else is byte-identical to V3
(`diff -rq` reports one differing file). Full record:
`FORMATTING_CHANGE_RECORD.md`.

## Contents

| item | path |
|---|---|
| 1 | `main.tex` |
| 2 | `sections/` — 13 section/appendix files |
| 3 | `references.bib` |
| 4 | `main.pdf` — compiled PDF (42 pp) |
| 5 | `COVER_LETTER_DRAFT.md` — **draft, not sent** |
| 6 | `FINAL_SUBMISSION_CHECKLIST.md` |
| 7 | `FFA_GUIDELINE_VERIFICATION.md` — requirement-by-requirement, with URLs and access date |
| 8 | `FORMATTING_CHANGE_RECORD.md` — before/after |
| 9 | `main.log` — build log |
| 10 | `SHA256_MANIFEST.txt` |
| 11 | this README |
| extra | `HIGHLIGHTS.md` (encouraged by FFA; separate file; pending confirmation), `main.bbl`, `build_modern/` (full build directory), `compile/` (toolchain) |

## Reproduce

```sh
# 1. verify this package
sha256sum -c SHA256_MANIFEST.txt

# 2. TeX Live 2024 (skip if /home/user/texlive2024 exists)
sh PAPER/compile/bootstrap_texlive.sh

# 3. four-pass build with genuine BibTeX
cd PAPER/FFA_FORMATTED_SUBMISSION
TL=/home/user/texlive2024 SOURCE_DATE_EPOCH=1794268800 \
  sh compile/build_modern.sh "$(pwd)/build_repro" main
```

Expected: 0 errors, 0 undefined citations, 0 undefined references, 0 overfull
boxes, 0 missing glyphs, 42 pages, PDF SHA-256
`a87491e2ac5071a896b4fd29d25054dc3de9a51275bd2d9dda32975a7f1bff68`.

```sh
# 4. validators (from the repository root)
python3 PAPER/tools/validate_latex_v2.py --root PAPER/FFA_FORMATTED_SUBMISSION
python3 PAPER/tools/verify_examples.py
```

Expected: `checks: 13 ; PASS 13 ; FAIL 0` and `CHECKS: 56  mismatches: 0`.

## Build recorded

| | |
|---|---|
| TeX Live | 2024 |
| BibTeX | genuine `BibTeX 0.99d`, `plain.bst`, 78-line `.bbl` |
| errors / undefined refs / undefined cites | 0 / 0 / 0 |
| Overfull / Underfull `\hbox` | 0 / 0 |
| missing glyphs | 0 |
| pages | 42 |
| bytes | 580 175 |
| SHA-256 | `a87491e2ac5071a896b4fd29d25054dc3de9a51275bd2d9dda32975a7f1bff68` |

## Important

* **Visual inspection was NOT performed** — Arena has no vision capability and
  did not view the rendered PDF. All results above are programmatic (build-log
  parsing, PDF text extraction, hash comparison). **The researcher must review
  the PDF.**
* **This is not a submission.** Nothing has been uploaded to Elsevier; no
  Editorial Manager account has been created; the cover letter has not been sent.
* Mandatory items remain unresolved — see `FINAL_SUBMISSION_CHECKLIST.md` §E.
