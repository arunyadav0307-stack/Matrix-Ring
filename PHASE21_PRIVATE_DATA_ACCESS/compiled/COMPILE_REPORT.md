# Phase 22 — Compilation report

## MANDATORY STATUS — READ FIRST

> # ⚠️ EDITORIAL CONFIRMATION REQUIRED
>
> **PRIVATE DATA ACCESS IS NOT YET ESTABLISHED AS ACCEPTABLE UNDER FFA
> OPTION C.**
>
> This PDF is a **clean technical compile** of the Phase 21 staging manuscript
> and nothing more. It is **not** a submission-ready manuscript. The journal
> has **not** accepted the private-data arrangement, no exception has been
> granted, and no clarification email has been sent. The manuscript may not be
> submitted while the FFA research-data requirement is unresolved.

---

## 1. What was compiled, and why

The researcher requested a compiled PDF of the Phase 21 staging manuscript —
the version in which the withdrawn public GitHub data link is replaced by the
proposed private-access statement.

| | |
|---|---|
| source directory | `PHASE21_PRIVATE_DATA_ACCESS/staging/` (**only**) |
| output directory | `PHASE21_PRIVATE_DATA_ACCESS/compiled/` |
| canonical manuscript (`PAPER/main.tex`) | **not used** |
| Phase 19 formatted copy (`PAPER/FFA_FORMATTED_SUBMISSION/`) | **not used** |

The staging sources were **not modified**. The build toolchain copies the
sources into the build directory and compiles there, so
`staging/main.tex`, `staging/references.bib` and the 13 files in
`staging/sections/` are untouched — verified by hash before and after
(25 files, **0 changed**).

---

## 2. Compilation result: SUCCESS

| | |
|---|---|
| **PDF** | `compiled/main.pdf` |
| **pages** | **42** |
| **page size** | 595.3 × 841.9 pt (A4) |
| **file size** | **580,540 bytes** |
| **SHA-256** | `7fd0896a2e715afd050f1fb1c84f00423d6b3bf64a51f93a007b4bbd37626ae3` |

### Reproducibility

This PDF is **byte-identical** to the PDF produced by the Phase 21 build
(`staging/build/main.pdf`), confirmed by `cmp`. Two independent four-pass
builds from the same sources, with `SOURCE_DATE_EPOCH` pinned, produced the
same 580,540 bytes and the same hash.

---

## 3. Toolchain

| | |
|---|---|
| TeX Live | **2024** (`/home/user/texlive2024`) |
| pdfTeX | **3.141592653-2.6-1.40.26 (TeX Live 2024)**, preloaded format `pdflatex 2024.5.1` |
| BibTeX | **genuine `BibTeX 0.99d` (TeX Live 2024)** |
| LaTeX | LaTeX2e <2023-11-01> patch level 1 |
| bibliography style | `plain.bst` |
| build driver | `staging/compile/build_modern.sh` |
| reproducibility pin | `SOURCE_DATE_EPOCH=1794268800` (2026-11-10T00:00:00Z) |

### Four-pass cycle, as instructed

```
pass 1:  pdflatex main.tex     -> 0 errors
pass 2:  bibtex main           -> BibTeX 0.99d, plain.bst, 13 entries, 78-line .bbl
pass 3:  pdflatex main.tex
pass 4:  pdflatex main.tex
```

**No pre-generated bibliography was substituted.** Evidence that the
bibliography is genuine BibTeX output is in `compiled/main.blg`:

```
This is BibTeX, Version 0.99d (TeX Live 2024)
The top-level auxiliary file: main.aux
The style file: plain.bst
Database file #1: references.bib
You've used 13 entries, ...
```

No pybtex or any other bibliography tool was used at any point.

---

## 4. Errors and warnings

| check | count |
|---|---|
| LaTeX errors (`^! `) | **0** |
| undefined citations | **0** |
| undefined references | **0** |
| missing characters / glyphs | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| hyperref warnings | **0** |
| font warnings | **0** |
| `missfont.log` | not produced |

**No LaTeX error occurred, so no source modification was required.** The
minimum-technical-correction clause was therefore not invoked.

---

## 5. Content validation

### 5.1 Policy-critical checks

| check | result |
|---|---|
| old public GitHub data link absent (`github.com`) | ✅ **0 occurrences** in the rendered PDF |
| old commit hash `e41c571` absent | ✅ **0 occurrences** |
| any URL of any kind in the manuscript body | ✅ **0 occurrences** |
| proposed private-access statement present ("are not publicly available") | ✅ **PRESENT** |
| proposed private-access statement present ("on reasonable request") | ✅ **PRESENT** |
| status marker "PENDING EDITORIAL CONFIRMATION" | ✅ **PRESENT** |
| status marker "NOT COMPLIANT AS A FINAL STATEMENT" | ✅ **PRESENT** |
| Option C named in the section | ✅ **PRESENT** |
| inventory figures (86 files / 22 / 23 / 29 / 8) | ✅ **PRESENT** |

Two occurrences were examined and cleared rather than ignored:

* **`Zenodo`** appears **once**, on page 38, inside the staging-status
  sentence — "…has **not** authorised a public deposit, a public repository
  link, a Zenodo deposit, a DOI, a GitHub release or a public tag." This is a
  **negation**, not a link.
* **`http://`** appears **once**, on page 42, as part of reference [5]
  (Grassl, *Bounds on the minimum distance of linear codes and quantum codes*,
  `http://www.codetables.de`) — an ordinary bibliography entry, not a data
  link.

### 5.2 Title page and metadata

| item | result |
|---|---|
| title | ✅ *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings* |
| author | ✅ Arun Kumar Yadav |
| affiliation | ✅ K.R. Mangalam University |
| corresponding email | ✅ arunyadav0307@gmail.com |
| postcode / country | ✅ 122103 / India |

### 5.3 Abstract, keywords and declarations — all unchanged

| item | result |
|---|---|
| abstract (Option B2) — "two independent methods" | ✅ present, unaltered |
| abstract — "exact for 11 codes and a lower bound for 17" | ✅ present, unaltered |
| keywords | ✅ 7, on the title page |
| funding declaration | ✅ "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." |
| competing-interest declaration | ✅ "The author declares no known competing financial interests or personal relationships…" |
| Acknowledgements section | ✅ present |
| CRediT placeholder | ✅ unchanged (still unconfirmed) |
| generative-AI declaration | ✅ **unchanged** — still the unconfirmed placeholder; not touched |
| honest-comparison statements ("at best equal", "No record parameter is claimed") | ✅ present |

### 5.4 Examples, tables, references, appendices

| item | result |
|---|---|
| worked examples rendered | ✅ **13** — 3.13, 3.14, 4.12, 4.13, 5.12, 5.13, 5.14, 5.15, 6.16, 6.17, 7.11, 7.12, 8.12 |
| Example 13 (= Example 8.12) | ✅ present, on **page 33**, Phase 15 correction intact |
| Appendix Table A.1 | ✅ present |
| Appendix Table A.2 | ✅ present |
| quantum parameter tuples | ✅ **125** tuples extracted; the sorted inventory is **identical** to the Phase 19 formatted PDF |
| the 28 certified codes | ✅ **28/28** located in the rendered text |
| references | ✅ 13 entries, all resolved, 0 undefined |
| appendices A and B | ✅ present |
| `??` (unresolved reference markers) | ✅ **0** |

### 5.5 Validators

| validator | result |
|---|---|
| `tools/validate_latex_v2.py --root PHASE21_PRIVATE_DATA_ACCESS/compiled` | **13 PASS / 0 FAIL** |
| `tools/verify_examples.py` (run against the staging sections) | **56 checks / 0 mismatches** |

`verify_examples.py` has no `--root` flag, so it was run from a scratch
directory containing a copy of `tools/`, a copy of the staging `sections/`, and
a symlink to `PAPER/supplementary` — the same arrangement used in earlier
phases.

### 5.6 Proof that nothing else changed

Removing the Data availability block from both this PDF and the Phase 19
formatted PDF leaves two documents of the **same length to the character**
(117,301 characters each) that differ only in **page numbers** — the table of
contents entries `B.2 Environment`, `B.3 Randomness` and `B.4 Where the numbers
come from` shift from page 39/40 to 40/41, and running footers shift with them.
That is pagination drift from inserting a slightly longer paragraph, not a
content change.

---

## 6. What was deliberately NOT done

Per the Phase 22 instructions, none of the following was done:

* the data-availability statement was **not** rewritten;
* no reason for restricted access was **invented**;
* no unconfirmed explanation was inserted;
* the old public GitHub link was **not** restored;
* the abstract, author information, funding declaration, competing-interest
  declaration, any theorem, proof, example or quantum parameter, and the
  generative-AI declaration were all left **exactly as they are**;
* **no licence was applied**.

### External actions — none taken

No editorial email sent · no manuscript uploaded · no data uploaded to GitHub
or Zenodo · no DOI created · no release or tag created · no branch merged · no
licence applied · no submission to Elsevier · no external publication action of
any kind.

---

## 7. Files in `compiled/`

| file | what it is |
|---|---|
| `main.pdf` | the compiled manuscript (42 pp, 580,540 B) |
| `main.log` | full pdflatex log of the final pass |
| `main.bbl` | the genuine BibTeX output (78 lines) |
| `main.blg` | the BibTeX log — proof that BibTeX 0.99d ran |
| `COMPILE_TRANSCRIPT.txt` | the complete console transcript of the four-pass build |
| `COMPILE_REPORT.md` | this report |
| `SHA256_MANIFEST.txt` | SHA-256 of every file here |
| `main.tex`, `references.bib`, `sections/` | the sources as copied in by the build script (compilation inputs, byte-identical to `staging/`) |
| `main.aux`, `main.out`, `main.toc` | LaTeX intermediates |

---

## 8. The remaining FFA Option C blocker — unchanged

Nothing in this phase changes the policy position established in Phase 21:

1. FFA Option C is **required**: deposit in a data repository **and** a link at
   submission, **or** a statement explaining **why** sharing isn't possible.
2. The official policy text does **not** mention access upon reasonable
   request. That ambiguity is real and unresolved.
3. The researcher has given **no reason** for non-deposition, and none was
   invented here.
4. On the strict reading this is a **submission blocker**.

**Status: EDITORIAL CONFIRMATION REQUIRED — PRIVATE DATA ACCESS NOT YET
ESTABLISHED AS ACCEPTABLE UNDER FFA OPTION C.**

Also still outstanding from Phase 21: the canonical manuscript's Data
availability section (page 37 of `PAPER/FFA_FORMATTED_SUBMISSION/main.pdf`)
still carries the withdrawn GitHub link and must be replaced before submission
on either route.

---

## 9. Stopping point

Phase 22 is complete. Compilation succeeded, validation is clean, and the
staging sources are unchanged. **Awaiting explicit researcher approval.** No
submission, no upload, no email, no deposit.
