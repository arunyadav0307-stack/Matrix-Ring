# FFA submission staging copy

**This is a staging copy. It is not the canonical manuscript.**

## Status

Isolated copy of `PAPER/` made on 2026-11-10, into which all Phase 11
manuscript changes were written. The canonical `PAPER/main.tex`,
`PAPER/references.bib`, `PAPER/main.bbl`, `PAPER/main.pdf` and every
`PAPER/sections/*.tex` file remain **byte-identical** to their pre-Phase-11
state.

**Promotion of any of this to the canonical manuscript requires explicit
researcher approval.**

## What differs from the canonical manuscript

| change | task | location |
|---|---|---|
| Revised abstract (246/230/**260** → **213/199/226**, limit 250) | B | `main.tex`, abstract environment |
| Author-metadata placeholder macros + centred affiliation block | C1 | `main.tex`, before `\title` and after `\maketitle` |
| Six declaration sections before the reference list | C2–C5 | `main.tex`, before `\appendix` |
| "The role of the matrix-ring formulation, and what Morita equivalence does and does not settle" | D2 | `sections/01_introduction.tex` |
| "Contributions, in order of emphasis" | D3 | same file |
| "On the parameters obtained" | D1 | same file |

## Placeholders — every one is unresolved

All bracketed `[...]` fields and every section marked *"Researcher
confirmation required"* is **unresolved**. Nothing has been invented. Search
for them with:

```sh
grep -rn '\[GIVEN NAME\]\|\[COUNTRY\]\|\[CORRESPONDING\|Researcher confirmation' main.tex
```

## Building

```sh
sh compile/bootstrap_texlive.sh     # rebuilds /home/user/texlive2024 if absent
cd FFA_SUBMISSION_STAGING
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

Current build: **0 errors, 0 warnings, 42 pages**, PDF SHA-256
`519513ba620660a5f673a52b562fe03caaa511b877a7330d1c8307c0ec07583c`
(`SOURCE_DATE_EPOCH=1794268800`). See
`PHASE11_FFA_FINALIZATION/PHASE11_LATEX_BUILD_REPORT.md`.

## Contents

| path | note |
|---|---|
| `main.tex`, `references.bib`, `main.bbl`, `sections/`, `supplementary/`, `compile/` | copied from `PAPER/` |
| `README_source.md` | the `PAPER/README.md` from the time of copying |
| `build_modern/` | build output, regenerated on each compile |
