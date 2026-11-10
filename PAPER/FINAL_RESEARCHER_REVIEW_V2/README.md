# Final researcher review — Version 2 (Phase 15 corrections)

*Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*
Target journal: **Finite Fields and Their Applications** (Elsevier)

Version 2 contains the three accuracy corrections of Phase 15. It **supersedes**
`PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` for reading purposes, but does **not**
replace it: that package is the Phase 14 archive and is preserved unchanged.

---

## Version 2.1 (Phase 16) — certification documentation alignment

Phase 16 corrected the **supplementary** certification documentation and removed
one residual inaccuracy in the manuscript. Nothing mathematical changed.

* **New authoritative supplementary package: `PAPER/SUPPLEMENTARY_V2/`.**
  `PAPER/supplementary/` is **preserved unchanged** as historical evidence; the
  corrected package differs from it in exactly one file
  (`CERTIFICATION_PROCEDURE.md`) out of 86. See `SUPPLEMENTARY.md`.
* **The M3 cross-check is not uniform — now stated explicitly.** M3 scans
  increasing symplectic weight and returns the first hit, so a returned value is
  *exact*: this happens for **11** of the 28 codes. For the other **17** it finds
  nothing below the search weight and yields a proved lower bound only.
  Appendix A previously said "M3 is … rather than an exact method", which those
  11 records contradict; both Appendix A and §8.5 now state the 11/17 split.
* **Validator false positives resolved.** `tools/validate_latex_v2.py` reports
  **13 PASS / 0 FAIL** with a 12-case self-test; the original
  `tools/validate_latex.py` is preserved unchanged. See
  `PHASE16_VALIDATOR_REVIEW.md`.
* Full per-code reconstruction:
  `corrected_appendix/PHASE16_28_CODE_APPLICABILITY_TABLE.csv` and
  `corrections/PHASE16_RESEARCHER_DECISION_REPORT.md`.

### Certification-method summary (all 28 codes, 0 discrepancies)

| | M1 completes | M1 does not complete | total |
|---|---|---|---|
| codes | **24** | **4** | **28** |
| exact-distance method | M1 | M2 | — |
| M2 | conditionally skipped | run (exact) | — |
| M3 | run | run | 28 |
| **methods executed** | **M1 + M3** | **M2 + M3** | **2 per code** |

**0 of 28 codes executed all three methods.** M3's cross-check is exact for 11
codes and a lower bound for 17.

---

## What changed in Version 2

---

## What changed in Version 2

| ID | Correction | Where to look |
|---|---|---|
| **CP-1** | The claim that all 28 certified codes are certified by *three* independent methods was **false**. 0 of 28 codes have all three; **28 of 28 have exactly two**. Each code's exact distance comes from exactly one exact method (M1 complete enumeration where it completes, otherwise M2 support search, which is run precisely when M1 cannot finish), plus the ambient quantum search M3 as a cross-check (a lower bound for 17 of 28). | abstract (p1), Introduction (pp. 3–6), §8.5 (p31), Appendix A (p38) |
| **CP-2** | Example 8.12 (`ex:certify`, p33) credited the support search (M2), which was never run for that code. Method attribution corrected only — generator matrix, parameters and all arithmetic untouched and independently recomputed. | p33 |
| **CP-3** | The two appendix tables rendered as `Table 5` / `Table 6`; per the FFA guide for authors they must be `Table A.1` / `Table A.2`. Main-text Tables 1–4 unchanged; table contents unchanged. | pp. 38–39 |
| **CP-4** | Nine DOIs are present in `references.bib` but `plain.bst` renders none. **Retained deliberately** — FFA applies reference formatting at proof stage. | `audit/OPEN_ISSUES_AND_LIMITATIONS.md` §5.1 |

No theorem, proof, generator matrix or numerical parameter was modified.

---

## Contents of this package (12 items)

| # | Item | Path |
|---|---|---|
| 1 | Corrected LaTeX source | `source/main.tex`, `source/sections/*.tex` (12 files) |
| 2 | Bibliography | `source/references.bib`, `build/main.bbl` |
| 3 | Compiled PDF (42 pp) | `build/manuscript.pdf` (see `build/`) |
| 4 | Corrected appendix tables + CP-1 table | `corrected_appendix/` |
| 5 | Example-verification output | `verification/example_verification_output.txt` |
| 6 | Updated mathematical self-audit | `audit/MANUSCRIPT_SELF_AUDIT.md` |
| 7 | Final correction report | `corrections/PHASE15_FINAL_CORRECTIONS_REPORT.md` |
| 8 | Visual-review images | `visual_review/pages/`, `visual_review/key_pages/` |
| 9 | Contact sheet | `visual_review/contact_sheet.png` |
| 10 | Supplementary-package reference | `SUPPLEMENTARY.md` |
| 11 | SHA-256 manifest | `SHA256_MANIFEST.txt` |
| 12 | Reproduction instructions | this file, §Reproduction below |

Plus `audit/OPEN_ISSUES_AND_LIMITATIONS.md` and `audit/CLAIM_TRACEABILITY_MATRIX.md`
(claim **T-225** corrected in place).

---

## Reproduction

### 1. Verify the package

```sh
cd PAPER/FINAL_RESEARCHER_REVIEW_V2
sha256sum -c SHA256_MANIFEST.txt
```

Every line must report `OK`.

### 2. Obtain a TeX Live tree (skipped if `/home/user/texlive2024` exists)

```sh
cd ../../..          # repository root
sh PAPER/compile/bootstrap_texlive.sh
```

### 3. Build the manuscript (4 passes with genuine BibTeX)

```sh
cd PAPER/FINAL_RESEARCHER_REVIEW_V2/source
TL=/home/user/texlive2024 SOURCE_DATE_EPOCH=1794268800 \
  sh ../../compile/build_modern.sh "$(pwd)/../build_repro" main
```

`SOURCE_DATE_EPOCH=1794268800` is pinned so the build is byte-reproducible; with
it, the PDF SHA-256 must equal the value recorded in §Build below.

Expected: 0 errors, 0 undefined citations, 0 undefined references, 0 overfull
boxes, 0 missing glyphs, 42 pages.

### 4. Re-verify the worked examples and parameter tables

```sh
cd ../../..          # repository root
python3 PAPER/tools/verify_examples.py
```

Expected tail: `CHECKS: 56     mismatches: 0`

### 5. Static source validation

```sh
python3 PAPER/tools/validate_latex.py --root PAPER/FINAL_RESEARCHER_REVIEW_V2/source
```

Expected: `checks: 13 ; PASS 11 ; FAIL 2`. The two FAILs (V9, V11) are
**pre-existing heuristic false positives**, present identically before the Phase
15 edits — see §Validation in the correction report.

### 6. Regenerate the per-code method-applicability table

```sh
python3 - <<'PY'
import csv
rows=list(csv.DictReader(open('PAPER/supplementary/parameter_tables/certified_codes.csv')))
for r in rows:
    m1,m2,m3=r['M1'],r['M2'],r['M3_lower_bound']
    used=(['M1'] if m1 not in ('-','n/a') else [])+(['M2'] if m2 not in ('-','n/a') else [])+['M3']
    print(f"{r['code']:<18}{r['route']:<4}{'+'.join(used):<10}{len(used)}")
PY
```

Every row must print `2`.

### 7. Supplementary data

The supplementary package is **referenced, not duplicated** here — see
`SUPPLEMENTARY.md`. Verify it in place:

```sh
cd PAPER/supplementary && sha256sum -c MANIFEST.sha256
```

Expected: 85 entries, all `OK`.

---

## Build recorded for this package

| | |
|---|---|
| TeX Live | 2024 |
| BibTeX | `BibTeX 0.99d`, style `plain.bst`, 78-line `.bbl` |
| errors / undefined refs / undefined cites | 0 / 0 / 0 |
| Overfull / Underfull `\hbox` | 0 / 0 |
| missing glyphs | 0 |
| duplicate labels | 0 (116 labels) |
| pages | 42 |
| page size | A4, 595.3 × 841.9 pt |
| bytes | 580 555 |
| **SHA-256** | `9c23bd8cdb539f0ed53ef2ae949bd6db1326dfdccf7ebc70c2b395b965bb838a` |

---

## Important caveat on the visual review

The page images in `visual_review/` were produced **for the researcher to
inspect**. **Arena has no vision capability and did not look at them.** Nothing
in the accompanying reports rests on visual inspection; the layout was verified
only programmatically (page count, geometry, absence of margin overflow, font
set, absence of empty pages, and text content extracted from every page).
