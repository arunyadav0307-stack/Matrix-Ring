# Final researcher review — Version 3 (Phase 18: approved abstract Option B)

*Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*
Target journal: **Finite Fields and Their Applications** (Elsevier)

## What changed in Version 3

**One sentence.** The researcher approved **Phase 17 abstract wording Option B
(B2 variant)**; it has been applied to the abstract and nowhere else.

| | |
|---|---|
| before | "…certifies $28$ codes, each by two applicable independent methods, one exact and one a cross-check…" |
| after | "…certifies $28$ codes, each by two independent methods: one exact, and one quantum search **exact for $11$ codes and a lower bound for $17$**…" |

Word counts: **C1 231 · C2 217 · C3 244** (strictest), limit 250, **margin 6**.
These reproduce the approved Phase 17 baseline exactly; the +9 delta against
Option A is attributable solely to the replacement sentence.

No theorem, proof, equation, example, distance value, quantum parameter,
generator matrix, construction route, certification record, author metadata,
funding statement or competing-interest declaration was altered.

Versions 2 and 2.1 are **preserved unchanged** at
`PAPER/FINAL_RESEARCHER_REVIEW_V2/`.

---

## Contents (11 items)

| # | item | path |
|---|---|---|
| 1 | Revised LaTeX source | `source/main.tex`, `source/sections/*.tex` (13 files) |
| 2 | Updated abstract | in `source/main.tex` |
| 3 | Bibliography | `source/references.bib`, `build/main.bbl` |
| 4 | Sections and appendices | `source/sections/` (12 sections + 2 appendix files) |
| 5 | Compiled PDF (42 pp) | `build/manuscript.pdf` |
| 6 | Updated validation report | `validation/` |
| 7 | Abstract word-count report | `reports/ABSTRACT_WORD_COUNT_REPORT.md` |
| 8 | Certification consistency report | `reports/CERTIFICATION_CONSISTENCY_REPORT.md` |
| 9 | Supplementary package reference | `SUPPLEMENTARY.md` |
| 10 | SHA-256 manifest | `SHA256_MANIFEST.txt` |
| 11 | README with reproducibility | this file |

Plus `reports/PHASE17_ABSTRACT_WORDING_OPTIONS.md` (the approved options, for
traceability) and `build/main.log`.

---

## Reproducibility

### 1. Verify this package

```sh
cd PAPER/FINAL_RESEARCHER_REVIEW_V3
sha256sum -c SHA256_MANIFEST.txt
```

Every line must report `OK`.

### 2. TeX Live (skip if `/home/user/texlive2024` exists)

```sh
cd ../../..          # repository root
sh PAPER/compile/bootstrap_texlive.sh
```

### 3. Build (4 passes, genuine BibTeX)

```sh
cd PAPER/FINAL_RESEARCHER_REVIEW_V3/source
TL=/home/user/texlive2024 SOURCE_DATE_EPOCH=1794268800 \
  sh ../../compile/build_modern.sh "$(pwd)/../build_repro" main
```

`SOURCE_DATE_EPOCH=1794268800` is pinned for byte-reproducibility; with it the
PDF SHA-256 must equal the value in §Build below.

Expected: 0 errors, 0 undefined citations, 0 undefined references, 0 overfull
boxes, 0 missing glyphs, 42 pages.

### 4. Validators

```sh
cd ../../..
python3 PAPER/tools/validate_latex_v2.py --root PAPER/FINAL_RESEARCHER_REVIEW_V3/source
python3 PAPER/tools/verify_examples.py
```

Expected: `checks: 13 ; PASS 13 ; FAIL 0` and `CHECKS: 56  mismatches: 0`.

> `tools/validate_latex.py` (the original) is preserved and still reports its
> historic 11 PASS / 2 FAIL on two known heuristic false positives; prefer
> `validate_latex_v2.py`, which resolves them.

### 5. Supplementary data

```sh
cd PAPER/supplementary     && sha256sum -c MANIFEST.sha256   # 85 entries
cd PAPER/SUPPLEMENTARY_V2  && sha256sum -c MANIFEST.sha256   # 86 entries
```

---

## Build recorded for this package

| | |
|---|---|
| TeX Live | 2024 |
| BibTeX | genuine `BibTeX 0.99d`, style `plain.bst`, 78-line `.bbl` |
| errors / undefined refs / undefined cites | 0 / 0 / 0 |
| Overfull / Underfull `\hbox` | 0 / 0 |
| missing glyphs | 0 |
| duplicate labels | 0 (116 labels) |
| pages | **42** |
| page size | A4, 595.3 × 841.9 pt |
| bytes | 580 584 |
| **SHA-256** | `c87381bc29a2955c2f5822cbbbae0e80a4226e3e44ed50e3d89d595a0d16ec0c` |

Appendix tables verified as **Table A.1** / **Table A.2**, Tables 1–4 preserved.
Example 13 (`ex:certify`, rendered Example 8.12) verified on p. 33. All 13
worked examples present. Author metadata verified: **Arun Kumar Yadav**, K.R.
Mangalam University, Gurugram, Haryana, 122103, India;
arunyadav0307@gmail.com. Funding and competing-interest declarations unchanged.

## Caveat on visual inspection

**Arena has no vision capability and did not view any rendered page.** All
statements above come from build-log parsing, PDF text extraction and hash
comparison. Page images from the immediately preceding build are in
`PAPER/FINAL_RESEARCHER_REVIEW_V2/visual_review/` (42 pages at 150 dpi, 8 key
pages at 300 dpi, plus a contact sheet); they reflect the Phase 16 build and, on
pages 31, 38 and 39, predate the Phase 16 text additions. The researcher must
perform the visual review.
