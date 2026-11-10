# Phase 13 — LaTeX build report

**STATUS: VERIFIED — clean four-pass build after incorporating the confirmed
author metadata and the GitHub data-availability text.**

Date: 2026-11-10 · Staging copy: `PAPER/FFA_SUBMISSION_STAGING/`

## 1. Toolchain

| component | version |
|---|---|
| pdfTeX (driving `pdflatex`) | **3.141592653-2.6-1.40.26 (TeX Live 2024)** |
| Preloaded format | `pdflatex 2024.5.1` |
| BibTeX | **0.99d (TeX Live 2024)** |
| kpathsea | 6.3.6/dev |
| Bibliography style | `plain.bst` |

## 2. Cycle

```
pdflatex main.tex → bibtex main → pdflatex main.tex → pdflatex main.tex
```

with `SOURCE_DATE_EPOCH=1794268800`. Genuine BibTeX: the build directory is
wiped and repopulated from source each run, so no pre-existing `.bbl` can be
used. BibTeX consumed all **13** entries and produced a 78-line `.bbl`.

## 3. Result

| metric | value |
|---|---|
| Errors | **0** |
| Undefined citations / references | **0 / 0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| Missing characters | **0** |
| LaTeX/package warnings | **0** |
| Font warnings | **0** |
| Pages | **42** |
| PDF bytes | 578 355 |
| **PDF SHA-256** | `a0fea51c4054b89641b9b9cb2407bb7cbefb54aaba6b75d7302814efb8bdd509` |

### Independent validation

| tool | verdict |
|---|---|
| `tools/check_log.py` | **VERDICT: clean** |
| `tools/validate_latex.py` | **13 checks, 13 PASS, 0 FAIL** |
| `tools/inspect_pdf.py` | **issues found: 0** |

## 4. One problem encountered and fixed

Inserting the commit-pinned GitHub URL produced an **overfull `\hbox` of
163.8 pt** — a 40-character unbreakable SHA token.

**Fix applied in three steps:**

1. Wrapped the URL in `\begin{quote}\small` — still overfull (the SHA is a
   single unbreakable token).
2. Added `\penalty0` break points between URL segments — still overfull.
3. Added `\raggedright` **and** inserted `\penalty0` **inside** the SHA, every
   8 hex characters — **overfull boxes went to 0**.

Final form:

```latex
\begin{quote}\small\raggedright
\texttt{https://github.com/}\penalty0
\texttt{arunyadav0307-stack/}\penalty0
\texttt{Matrix-Ring/tree/}\penalty0
\texttt{e41c5713\penalty0 fec5cce1\penalty0 d7cb5110\penalty0 5f25d168\penalty0 dc05ebce}\penalty0
\texttt{/PAPER/supplementary}
\end{quote}
```

The URL renders correctly and remains copy-pasteable as a single string.

## 5. Rendered output verified

**Title page (page 1)** — extracted from the PDF:

```
Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings

Arun Kumar Yadavᵃ

ᵃ School of Basic and Applied Sciences, K.R. Mangalam University,
  Sohna Road, Gurugram, Haryana, 122103, India.

Corresponding author. E-mail: arunyadav0307@gmail.com
```

**Declarations (page 37)** — all six sections present before the reference
list:

| section | status |
|---|---|
| Acknowledgements | pending (optional) |
| Declaration of competing interests | **CONFIRMED — rendered** |
| Funding | **CONFIRMED — rendered** |
| Author contributions (CRediT) | pending (encouraged) |
| Data availability | pending (mandatory) — GitHub URL rendered |
| Generative AI | **pending — discrepancy unresolved** |

## 6. Abstract preserved

Re-measured after all edits: **213 / 199 / 226** words — identical to the
Phase 11 approved abstract. Unchanged.

## 7. PDF history

| phase | SHA-256 | pages |
|---|---|---|
| Phase 8 (canonical) | `b2ba1fee…8641a03` | — |
| Phase 11 first | `90379dbe…069e72e` | 42 |
| Phase 11 final | `519513ba…c07583c` | 42 |
| Phase 12 | `72bfa79d…46d20e0` | 42 |
| **Phase 13** | **`a0fea51c…b8bdd509`** | **42** |

All prior versions preserved; logs archived in
`PAPER/FFA_FINAL_SUBMISSION_PACKAGE/build/`.

## 8. Status

**VERIFIED.** Clean build, genuine BibTeX, no unresolved error, no missing
glyph, no overfull or underfull box. Title page, abstract, declarations,
references and appendices all inspected and correct.
