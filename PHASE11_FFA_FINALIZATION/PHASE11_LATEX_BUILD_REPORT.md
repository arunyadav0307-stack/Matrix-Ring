# Phase 11 / Task G — LaTeX build report

**Status: VERIFIED — a genuine modern TeX Live compilation was performed and
succeeded.**

Date: 2026-11-10.

## 1. Toolchain

Assembled in this session from scratch (the sandbox resets between turns and
removes `/home/user/texlive2024`), by `PAPER/compile/bootstrap_texlive.sh`.
Every component is a real TeX Live 2024 artifact.

| component | version | source |
|---|---|---|
| pdfTeX (driving `pdflatex`) | **3.141592653-2.6-1.40.26 (TeX Live 2024)** | TeX Live 2024 binaries |
| Preloaded format | `pdflatex 2024.5.1` | built by the bootstrap |
| BibTeX | **0.99d (TeX Live 2024)** | built from TeX Live 2024 `bibtex.web` sources |
| kpathsea | 6.3.6/dev (6.4.0 for the `pdftex` binary) | built from TL 2024 sources |
| Bibliography style | `plain.bst` | TeX Live 2024 texmf tree |

This is **not** the recovered pdfTeX 1.40.11 tree used in earlier phases to
reproduce the historical build. This is a current engine.

## 2. Build command and cycle

```
cd PAPER/FFA_SUBMISSION_STAGING
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

which performs exactly the required cycle:

```
pdflatex main.tex   →   bibtex main   →   pdflatex main.tex   →   pdflatex main.tex
```

with `SOURCE_DATE_EPOCH=1794268800` pinned so the PDF is byte-reproducible and
its SHA-256 is checkable.

**BibTeX is genuine.** It was run against `references.bib` using `plain.bst`
and consumed all 13 entries, producing a 78-line `main.bbl`. No pre-existing
`.bbl` was used as a shortcut: the build directory is deleted and repopulated
from `main.tex`, `references.bib` and `sections/` on every run.

## 3. Result

| metric | value |
|---|---|
| Errors (`^!` in log) | **0** |
| Undefined citations | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| Missing characters | **0** |
| LaTeX/package warnings | **0** |
| Font warnings | **0** |
| PDF produced | **yes** |
| PDF bytes | 577 558 |
| **PDF SHA-256** | `519513ba620660a5f673a52b562fe03caaa511b877a7330d1c8307c0ec07583c` |
| Pages | **42** |

### Independent verifications

* `PAPER/tools/check_log.py` → **VERDICT: clean** (0 errors, 0 missing
  characters, 0 overfull, 0 underfull, 0 warnings).
* `PAPER/tools/validate_latex.py` → **13 checks, 13 PASS, 0 FAIL**.
* `PAPER/tools/inspect_pdf.py` (via PyMuPDF) → **issues found: 0**; confirms
  title, abstract, keywords, TOC, References, all 6 tables, and **13 rendered
  bibliography entries**.

The repository's own validation tooling therefore agrees with the manual log
inspection.

## 4. One real problem encountered and fixed

The first build attempt **failed hard**:

```
kpathsea: Running mktexpk ... tcrm0600
!pdfTeX error: pdflatex (file tcrm0600): Font tcrm0600 at 600 not found
==> Fatal error occurred, no output PDF file produced!
```

**Cause:** the new author-metadata block used `\thanks{…}` for the
affiliation. `\thanks` sets a footnote marker, and the marker glyph must come
from the TS1 (text companion) encoding at 6pt. The font map in use supplies
TS1 by remapping to Latin Modern, but the 6pt `tcrm0600` instance is not
provided, and `mktexpk` cannot generate it in this offline sandbox.

**Fix:** dropped `\thanks` and typeset the affiliation as a centred block
after `\maketitle`, driven by macros:

```latex
\author{\AUTHORONE}
\newcommand{\AFFILIATIONBLOCK}{%
  \begin{center}\small
  \AUTHORONEINST, \AUTHORONEORG, \AUTHORONEADDR, \AUTHORONECOUNTRY
  \end{center}}
```

followed by `\maketitle` then `\AFFILIATIONBLOCK`. Cosmetically equivalent,
structurally simpler, and it avoids the missing glyph entirely.

A second, cosmetic issue: the long uppercase placeholder
`[RESEARCHER CONFIRMATION REQUIRED]` produced an underfull `\hbox` because TeX
cannot hyphenate all-caps text. Lowercased and re-punctuated to
`[Researcher confirmation required — …]`, after which underfull boxes went to
**0**.

**Both fixes are in the staging copy only.** Neither touched a protected file.

## 5. What was compiled

The **staging copy**, `PAPER/FFA_SUBMISSION_STAGING/`, not the canonical
manuscript. It differs from the canonical `PAPER/main.tex` in:

| change | purpose |
|---|---|
| Revised abstract (Task B) | FFA's ≤ 250-word limit |
| Author-metadata placeholder block + centred affiliation block (Task C1) | FFA title-page requirements |
| Six declaration sections before the reference list (Tasks C2–C5) | FFA/Elsevier declaration requirements |
| Three new introduction subsections (Task D) | Morita response, contribution hierarchy, honest parameter framing |

The canonical manuscript was **not** recompiled in this phase and is
unchanged; its PDF remains the Phase 8 artifact.

## 6. Reproducibility

To reproduce:

```sh
cd PAPER
sh compile/bootstrap_texlive.sh            # ~45 s; rebuilds /home/user/texlive2024
cd FFA_SUBMISSION_STAGING
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

With `SOURCE_DATE_EPOCH=1794268800` the resulting `main.pdf` should hash to
`519513ba…c07583c`.

## 7. Status

**VERIFIED.** Modern TeX Live compilation completed: 0 errors, 0 warnings,
42 pages, genuine BibTeX, PDF produced and independently validated.
