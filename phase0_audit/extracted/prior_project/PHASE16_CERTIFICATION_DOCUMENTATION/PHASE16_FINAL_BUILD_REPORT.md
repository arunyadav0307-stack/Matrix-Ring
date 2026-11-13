# Phase 16 / Task F — Final rebuild and reproducibility

Working copy: `PAPER/PHASE16_WORKCOPY/` (created from `PAPER/PHASE15_WORKCOPY/`).
Canonical `PAPER/` sources untouched.

## F.1 LaTeX validator

| validator | result |
|---|---|
| `tools/validate_latex.py` (original, preserved) | 13 checks, 11 PASS / 2 FAIL — identical to Phase 15 |
| `tools/validate_latex_v2.py` (corrected, Phase 16) | 13 checks, **13 PASS / 0 FAIL** |
| `validate_latex_v2.py --selftest` | **12 cases, 0 failures** |

V4: 264 refs / 116 labels, all resolve. V5: 116 labels, 0 duplicates.

## F.2 Example verification

`tools/verify_examples.py` (full run, not `--fast`), executed against the
**corrected** sources in a sandbox whose `sections/` is the Phase 16 copy and
whose `supplementary/` is the committed canonical package:

```
CHECKS: 56     mismatches: 0
```

## F.3 Four-pass build with genuine BibTeX

```
TL=/home/user/texlive2024 SOURCE_DATE_EPOCH=1794268800 sh compile/build_modern.sh
pdflatex -> bibtex -> pdflatex -> pdflatex
```

| | |
|---|---|
| TeX Live | 2024 (`/home/user/texlive2024`) |
| BibTeX | genuine `BibTeX 0.99d`, style `plain.bst`, 78-line `.bbl` |
| errors (`^! `) | **0** |
| undefined citations | **0** |
| undefined references | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| missing characters (glyphs) | **0** |
| hyperref warnings | **0** |
| font warnings | **0** |
| pages | **42** |
| page size | A4, 595.3 × 841.9 pt |
| bytes | 580 555 |
| **SHA-256** | `9c23bd8cdb539f0ed53ef2ae949bd6db1326dfdccf7ebc70c2b395b965bb838a` |

## F.4 PDF verification

42 pages, A4, 42/42 page images render. No empty or near-empty pages.

## F.5 Theorem and equation references

0 undefined references and 0 undefined citations in the build log; **0**
occurrences of the unresolved-reference marker `??` anywhere in the extracted
PDF text; 116 labels, 0 duplicates.

## F.6 Appendix table numbers

| string | pages |
|---|---|
| Table 1 | 18, 40 |
| Table 2 | 32, 32, 33, 36, 41 |
| Table 3 | 33, 33, 33, 36, 41 |
| Table 4 | 35, 41 |
| **Table A.1** | 32, 38, 39, 40 |
| **Table A.2** | 39, 40, 41, 41 |

Main-text Tables 1–4 preserved; appendix tables carry the `A.` prefixes; all
cross-references updated automatically (they use `\ref`).

## F.7 Example 13

Rendered on p. 33 as **Example 8.12 (certifying $[[20,2,10;18]]_4$)**, reading:

> "The support search (M2) is run only when M1 cannot finish, so it was not run
> here and contributes nothing; the ambient quantum search (M3) independently
> certifies $d\ge3$ as a lower bound, consistent with this value."

This matches this code's record exactly (M1 exact = 10, M2 `n/a`, M3 `>2`).

## F.8 Quantum parameters unchanged

All 34 `[[...]]` parameter tuples in Appendix A are **identical** to Phase 15
(extracted and compared programmatically). The diff against Phase 15 touches 17
lines, **none of which is a data line** — all are prose in the column-notes
paragraph.

## F.9 Manifests recomputed and verified

| package | entries | result |
|---|---|---|
| `PAPER/supplementary/MANIFEST.sha256` (historical) | 85 | **85/85 OK** — untouched |
| `PAPER/SUPPLEMENTARY_V2/MANIFEST.sha256` (corrected) | 86 | **86/86 OK** — 0 mismatches |
| `PAPER/FINAL_RESEARCHER_REVIEW_V2/SHA256_MANIFEST.txt` | 78 | re-verified **78/78 OK** |

## F.10 Corrected supplementary archive verified

86 content files; exactly one differs from the historical package
(`CERTIFICATION_PROCEDURE.md`); the other 85 are byte-identical by per-file
SHA-256 comparison; no `__pycache__` or `.pyc` present; `diff -r` reports a
single differing file.

## Note on visual inspection

**Arena has no vision capability and did not view any rendered page.** All
statements above come from programmatic verification: build-log parsing, PDF text
extraction, hash comparison and file-structure checks. No claim in this report
rests on visual inspection.
