# Phase 10 — Submission package checklist (FFA)

**Journal:** *Finite Fields and Their Applications*
**Date:** 2026-11-10
**Purpose:** inventory what the manuscript package already contains, and list
exactly what must be supplied by the researcher before a submission could be
made. **Nothing has been created, renamed or removed in Phase 10.**

**Rule applied throughout:** author, funding, institutional and declaration
information is **never invented**. Where it is missing it is listed as
*researcher input required*, with the source of the requirement.

---

## 1. What the package already contains — PRESENT

| item | location | detail | verdict |
|---|---|---|---|
| **Main LaTeX source** | `PAPER/main.tex` (sha256 `ee47ce7e…50737c`) | `\documentclass[11pt,a4paper]{article}`; 12 `\input` section files in `PAPER/sections/` | **PRESENT** — editable `.tex`, which is what FFA requires ("A PDF is not an acceptable source file") |
| **Section files** | `PAPER/sections/` | 10 numbered sections + `appendix_tables.tex` + `appendix_reproducibility.tex` | **PRESENT** |
| **Bibliography** | `PAPER/references.bib` (sha256 `73388338…d22feb`) | 13 entries, all cited; verified against publisher/arXiv/AIMS records | **PRESENT** |
| **Generated bibliography** | `PAPER/main.bbl` | BibTeX output | **PRESENT** |
| **Compiled PDF** | `PAPER/build_modern/main.pdf` — 563 659 B, sha256 `69265efb…e522fd`, 39 pp | the Phase 8B build on TeX Live 2024 with genuine BibTeX 0.99d | **PRESENT** (as an artefact; not acceptable as the *source*) |
| **Second PDF** | `PAPER/main.pdf` — 648 899 B, sha256 `b2ba1fee…641a03` | the Phase 8A build | **PRESENT** (superseded by the 8B build) |
| **Supplementary data and code** | `PAPER/supplementary/` — 85 files under `MANIFEST.sha256` | `README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, `MANIFEST.sha256`, `scripts/` (24 Python), `logs/` (24), `parameter_tables/` (8 CSV), `generator_matrices/` (28 JSON + `INDEX.json`) | **PRESENT — substantial** |
| **Generator matrices and certificates** | `supplementary/generator_matrices/` (28 JSON + `INDEX.json`); `supplementary/parameter_tables/certified_codes.csv` | one JSON per certified code, filename encoding `[[n,k,d;c]]_q` and `(q,t,n)`; the CSV carries `M1,M2,M3_lower_bound,all_methods_agree,F_p_abelian,EA_Singleton_defect,log_line` | **PRESENT** |
| **Reproducibility instructions** | Appendix B of the manuscript + `supplementary/README.md` + `ENVIRONMENT.md` + `CERTIFICATION_PROCEDURE.md` | exact interpreter, platform, seed (`SEED = 20261210`), and the command sequence (`cd PAPER/supplementary/scripts`) | **PRESENT** |
| **Computation scripts** | `supplementary/scripts/` — 24, incl. `matrix_ring_lib.py` | self-contained library implementing `F_q`, `A_t`, `R = M_2(A_t)`, `R_n` | **PRESENT** |
| **Computation logs** | `supplementary/logs/` — 24 | every CSV row carries the log line number it was parsed from | **PRESENT** |
| **Parameter tables** | `supplementary/parameter_tables/` — 8 CSV | certified codes, Grassl comparisons for `q=4` and `q=9`, entanglement budget, family census, family scan, non-principal witnesses, Pareto frontier | **PRESENT** |
| **Verification records** | `PAPER/build_modern/verification/` | `validate_latex.txt` (13/13), `check_log.txt`, `verify_examples.txt` (56/56), `inspect_pdf.txt`, `clean_rebuild.txt`, `provenance.txt` | **PRESENT** |
| **Audit and provenance documents** | `PAPER/` | `FINAL_VALIDATION_REPORT.md`, `MANUSCRIPT_SELF_AUDIT.md`, `CLAIM_TRACEABILITY_MATRIX.md`, `OPEN_ISSUES_AND_LIMITATIONS.md`, `LITERATURE_VERIFICATION.md`, `NOVELTY_COMPARISON.md`, `PARAMETER_COMPARISON.md`, `CONTRIBUTION_MAP.md`, `CHANGELOG.md` | **PRESENT** |
| **Archived packages** | `PAPER/*.zip` (3) + sidecars | Phase 8, 8A, 8B — all three verify OK | **PRESENT** |

## 2. Declarations — **ABSENT (all of them)**

| declaration | required by | status |
|---|---|---|
| Competing interests | Guide §Declaration of competing interests — "The declarations tool should always be completed" | **ABSENT** |
| Funding | Guide §Funding sources | **ABSENT** |
| Generative AI use | Guide §Declaration of generative AI use — "Authors **must declare**" | **ABSENT and applicable** |
| CRediT author contributions | Guide §Author contributions: CRediT (encouraged) | **ABSENT** |
| Data availability / research-data link or statement | Guide §Research data — **Option C, mandatory** | **ABSENT** |
| Acknowledgements | Guide §Acknowledgements (as applicable) | **ABSENT** |

**None of these has been drafted in Phase 10.** Each requires researcher
content, and two of them (funding, competing interests) require facts that
cannot be inferred from the repository.

## 3. Author metadata — **PLACEHOLDERS PRESENT, UNRESOLVED**

`\AUTHORPLACEHOLDER` occurs in `main.tex` at:

| line | use |
|---|---|
| 43 | `\newcommand{\AUTHORPLACEHOLDER}{…}` (the definition) |
| 53 | `pdfauthor={\AUTHORPLACEHOLDER}` in `\hypersetup` |
| 103 | `\author{\AUTHORPLACEHOLDER}` |

The header comment (l.8–10) records: "no author names, affiliations, funding,
acknowledgements or declarations have been supplied. The three
`\AUTHORPLACEHOLDER` marks below are the ONLY placeholders in this manuscript
and are deliberately visible."

The placeholder is **intentional and correct** — it is far better than invented
metadata. It must be resolved before submission:

| needed | requirement | supplied? |
|---|---|---|
| Author given + family names | Guide §Title page | **NO — researcher** |
| Author order | must match the submission system | **NO — researcher** |
| Affiliations, where the work was carried out | full name + postal address + **country** | **NO — researcher** |
| Corresponding author (exactly one) | clearly indicated; email will be published | **NO — researcher** |
| Present/permanent address footnotes | if applicable | **NO — researcher** |

## 4. Statements requiring researcher input at submission time

| # | statement | where it is entered | blocking? |
|---|---|---|---|
| 1 | Competing interests ("I have nothing to declare" if applicable) | https://declarations.elsevier.com/ → upload the generated document at the "attach/upload files" step | **YES** |
| 2 | Funding — grant numbers, or the exact sentence "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." | manuscript / submission system | **YES** |
| 3 | Generative AI declaration — new section **before the reference list**, naming the tool and the reason | manuscript | **YES** (manuscript modification — needs separate approval) |
| 4 | Research data — repository link, **or** a statement of why deposit is not possible (it will be published) | submission process | **YES** |
| 5 | Submission declaration: not previously published (preprint excepted); not under consideration elsewhere; approved by all authors | Editorial Manager affirmation | **YES** |
| 6 | Publication model: gold OA (USD 3 240 excl. taxes) or subscription (no fee) | after acceptance; no effect on review | decision needed eventually |
| 7 | CRediT contributions | encouraged | optional |
| 8 | Acknowledgements | separate section before the reference list | optional |
| 9 | Preprint decision | permitted, does not count as prior publication | optional |

## 5. Package gaps that are *not* blocking but should be closed

| # | gap | why it matters | action |
|---|---|---|---|
| 1 | **No repository deposit for the supplementary package** | FFA Option C **requires** either a deposit + link or a published statement of why not. The material (85 files) already exists and is self-contained, so a deposit is straightforward. | **RECOMMENDED:** deposit `PAPER/supplementary/` in a data repository (e.g. Zenodo) and cite the DOI. Resolves #26 of the compliance matrix *and* FFA's data-citation encouragement. |
| 2 | **Supplementary files are not individually cited** | FFA: "Cite all supplementary files in the manuscript text." The package is referenced as a whole in §8, §9 and Appendix B, but not file by file. | **RECOMMENDED:** add a per-file manifest to Appendix B. Content-neutral. |
| 3 | **No captions for supplementary files** | FFA: "Include a concise caption for each supplementary file." | **RECOMMENDED:** supply a caption list at submission. |
| 4 | **No highlights file** | Encouraged: 3–5 bullets, ≤85 characters each, separate file with "highlights" in the name. | **RECOMMENDED:** prepare at submission. |
| 5 | **Abstract at or over 250 words** | Verified hard limit. Measured 230–257 depending on counting convention. | **RECOMMENDED:** trim with margin. Manuscript modification — needs approval. |
| 6 | **Appendix tables not numbered A.1 / B.1** | FFA: "give separate numbering to tables and figures using formats such as Table A.1; Fig. A.1". | **RECOMMENDED:** if the Elsevier template is adopted, renumber. Cosmetic. |
| 7 | **DOIs not rendered** | FFA: "Where available include DOIs." 9 of 13 present in `references.bib`, 0 rendered; 3 entries have no DOI field. | **RECOMMENDED:** supply at proof stage, which is exactly when FFA says it will ask. No change needed now; D-1 stands. |
| 8 | **Stale provenance text** | `OPEN_ISSUES_AND_LIMITATIONS.md` §4 and `MANUSCRIPT_SELF_AUDIT.md` §5 still describe the modern-TeX-Live recompilation as "the one outstanding item". That item was **closed by Phase 8B** (2026-11-10). | **RECOMMENDED:** note the staleness; do not let a future cover letter or cover statement quote it. (Not a manuscript defect.) |
| 9 | **Language consistency** | FFA: American or British English, not a mixture. | **RECOMMENDED:** one systematic pass before submission. |

## 6. Files to upload, when a submission is made

Derived from FFA's file-format rule (editable `.tex`; PDF not acceptable as
source) and the supplementary-material rule (submit everything with the
manuscript; nothing can be added except at revision):

| file | purpose | ready? |
|---|---|---|
| `main.tex` | manuscript source | **YES** |
| `sections/*.tex` (12) | included sources | **YES** |
| `references.bib` | bibliography | **YES** |
| `main.bbl` | generated bibliography (helps Editorial Manager) | **YES** |
| `main.pdf` (8B build) | for reference / reviewer convenience — **not** as source | **YES** |
| `supplementary/` (85 files) | data, code, generator matrices, logs, certificates | **YES** (upload all — cannot be added later) |
| per-file supplementary captions | required by FFA | **NO — to be prepared** |
| highlights file | encouraged | **NO — to be prepared** |
| competing-interests document | from declarations.elsevier.com | **NO — researcher** |
| (optionally) the repository DOI | Option C | **NO — researcher** |

## 7. Not present, and not required

| item | note |
|---|---|
| Figures | The manuscript has none. FFA requires no figures. |
| Cover letter | **Deliberately not written.** Phase 10 is an assessment. |
| Cover image / graphical abstract | Not required by FFA's guide. |
| Permission documents for third-party material | Not needed: the manuscript reproduces no third-party figures or text. |
| Ethics approval | Not applicable: pure mathematics, no human or animal subjects. |
| Clinical trial registration | Not applicable. |

## 8. Bottom line

* **The scholarly package is complete and unusually well documented.** Source,
  bibliography, PDF, supplementary data and code, generator matrices,
  certificates, reproducibility instructions and verification records all
  exist, hash-verified.
* **Every missing item is a submission-time artefact, not a scholarly defect.**
  Author metadata, five declarations, the research-data route, and three
  optional-but-recommended files.
* **Nothing missing requires touching the mathematics**, with one exception:
  the generative-AI declaration must be added as a new section before the
  reference list, and that is a manuscript modification requiring separate
  explicit approval.
