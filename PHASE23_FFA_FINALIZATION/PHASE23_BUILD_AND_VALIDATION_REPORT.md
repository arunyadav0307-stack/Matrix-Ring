# Task G + Task I — Submission-package change record, build and validation

**Package:** `PAPER/FFA_FINAL_SUBMISSION_V2/`
**Built:** 2026-11-10
**Branch:** `arena/59de606f-matrix-ring` · **HEAD before this work:** `8b7f2e6`

---

# Part 1 — Task G: change record (before / after)

## G1. Provenance of the new copy

`PAPER/FFA_FINAL_SUBMISSION_V2/` was created as a **copy** of the latest FFA
manuscript, `PAPER/FFA_FORMATTED_SUBMISSION/` (Phase 19). `main.tex`,
`references.bib`, all 12 `sections/*.tex` and the whole `compile/` toolchain
were copied; the only build artefacts (`build_modern/`, `main.pdf`, `main.bbl`,
`main.log`) and the Phase 19 documentation files were **not** copied, since the
package is meant to be rebuilt and re-documented here.

**The Phase 19 copy is retained untouched.** No historical manuscript version
was overwritten.

## G2. The single substantive change

| | |
|---|---|
| File changed | `main.tex` — **only** the `\section*{Data availability}` block |
| Section files changed | **none** — all 12 byte-identical to Phase 19 |
| `references.bib` changed | **no** — byte-identical |
| Theorems, proofs, generator matrices, quantum parameters, distance certificates, mathematical conclusions | **none touched** |

### Before (Phase 19 wording)

> [*Researcher confirmation required — mandatory.*] … The researcher has elected
> to use the project's existing public GitHub repository *instead of* a
> dedicated data repository such as Zenodo. The data are publicly readable at
> the commit-pinned address
> `…/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary`
> which resolves to 86 files … certified by a SHA-256 manifest.
>
> **This statement is not yet final.** Two material limitations must be
> resolved before it can be submitted: (i) the supplementary data are present
> only on the research branch and are **absent from the repository's default
> branch** …; and (ii) that branch is unprotected …

### After (Phase 23 wording)

> [*PROPOSED — FFA POLICY CONFIRMATION PENDING.*] *Finite Fields and Their
> Applications* applies Elsevier research-data **Option C**, under which authors
> are required to deposit their research data in a relevant data repository and
> to provide a link to the dataset during the submission process.
>
> The computational scripts, verification logs, generator matrices, quantum-code
> records, distance certificates, verification procedures and supporting
> documentation used in this study are publicly available in the
> *research-data* directory of the project's GitHub repository at
> `…/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data`
> which is pinned to an immutable commit and comprises 86 files … each verified
> by a SHA-256 manifest …
>
> *Status: PROPOSED — FFA POLICY CONFIRMATION PENDING.* … Whether a
> commit-pinned public repository satisfies Option C is not established by the
> official policy text … The repository carries no licence …

### Why each change was made

| change | reason |
|---|---|
| `e41c571…` → `3752a6c…` | the old commit was on the research branch and **did not contain** `research-data/`; `3752a6c` is the published commit on `main`, verified publicly reachable |
| `/PAPER/supplementary` → `/research-data` | the curated `research-data/` directory is what was actually published; `PAPER/supplementary` is not on `main` |
| "elected … instead of a dedicated data repository such as Zenodo" removed | that framing pre-empts the editorial question and sounds like a request for an exemption; the new wording simply states what was done |
| "are **absent from the repository's default branch**" removed | **no longer true** — the data are on `main`. Retaining it would have been a false statement. |
| "that branch is unprotected" removed | still true, but no longer the operative limitation; replaced by an accurate statement of what remains unresolved |
| licence gap added | previously unstated; it is material to whether the deposit satisfies Option C |
| file-category wording updated | "8 parameter tables" → "8 tables of quantum-code records and distance certificates", "4 documentation files" → "4 documentation and verification files", matching the published directory exactly |

**Both limitations that the old statement flagged have been resolved; the new
statement flags a different, still-open one (policy confirmation and licence).**

## G3. What was deliberately NOT changed

| item | status |
|---|---|
| **Option B2 abstract** | ✅ **preserved word-for-word** — byte-identical between Phase 19 and V2 |
| Author name, affiliation, address, country | ✅ preserved |
| Corresponding-author e-mail | ✅ preserved |
| Funding declaration | ✅ preserved |
| Competing-interests declaration | ✅ preserved |
| Acknowledgements | ✅ preserved |
| The 12 section files | ✅ byte-identical |
| `references.bib` | ✅ byte-identical |
| Any theorem, proof, matrix, parameter or certificate | ✅ untouched |
| The generative-AI declaration | ✅ **left as the Phase 19 placeholder** — deliberately not finalised |

## G4. Proof that only the data-availability block changed

| check | result |
|---|---|
| `diff -rq` of the two source trees, excluding build artefacts and docs | **1 differing file** (`main.tex`); all 12 section files and `references.bib` identical |
| `diff -u` of `main.tex` | a single hunk, confined to `@@ -237,33 +237,39 @@`, i.e. the Data availability section |
| PDF text outside the Data availability block, Phase 19 vs V2 | **identical length (117,385 chars)**; the only textual differences are (a) the DA block itself and (b) the page numbers in the table of contents and the running heads, which shift because the DA block is longer |
| 125 `[[…]]_q` quantum-code tuples, Phase 19 vs V2 | **sorted lists identical** |
| Abstract, LaTeX source, Phase 19 vs V2 | **byte-identical** |

---

# Part 2 — Task I: build and validation

## I1. Toolchain

| | |
|---|---|
| TeX Live | **2024** (installed via `PAPER/FFA_FINAL_SUBMISSION_V2/compile/bootstrap_texlive.sh`) |
| Engine | **pdfTeX 3.141592653-2.6-1.40.26** |
| Bibliography | **genuine BibTeX 0.99d** — a real `bibtex` pass, not a pre-existing `.bbl` |
| kpathsea | 6.3.6/dev |
| Build command | `TL=/home/user/texlive2024 SOURCE_DATE_EPOCH=1794268800 sh compile/build_modern.sh "$(pwd)/build" main` |
| Cycle | **pdflatex → bibtex → pdflatex → pdflatex** (four passes) |

## I2. Build results

| metric | result |
|---|---|
| LaTeX errors (`^! `) | **0** |
| Undefined citations | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| Missing characters | **0** |
| hyperref warnings | **0** |
| Font warnings | **0** |
| `.bbl` entries produced by BibTeX | **13** |
| Pages | **42** |
| Page size | A4, 595.3 × 841.9 pt |
| PDF bytes | **580,019** |
| **PDF SHA-256** | **`d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1`** |

## I3. Validators

| validator | command | result |
|---|---|---|
| LaTeX structural validator | `python3 PAPER/tools/validate_latex_v2.py --root PAPER/FFA_FINAL_SUBMISSION_V2` | **13 checks, 13 PASS, 0 FAIL** |
| Worked-example verifier | `python3 tools/verify_examples.py` (from a scratch tree with `tools/`, `sections/` and a symlink to `PAPER/supplementary`) | **56 checks, 0 mismatches** |

## I4. Requested checks

| # | check | result |
|---|---|---|
| 1 | **Page count** | **42** |
| 2 | **References: 13 entries present and formatted per `plain` style, no missing BibTeX entries** | ✅ **13/13** `\bibitem`s in the `.bbl`; 13 `[n]` markers in the rendered References section; `\bibliographystyle{plain}`; 0 undefined citations; 0 `??` |
| 3 | **Abstract word count ≤ 250** | ✅ **240 words** after stripping LaTeX commands and inline math (250 raw whitespace-separated tokens). Identical to Phase 19. |
| 4 | **Keyword count between 1 and 7** | ✅ **7**: cyclic codes over rings; matrix rings; Galois duality; Galois hulls; Gray map; quantum stabilizer codes; entanglement-assisted quantum codes |
| 5 | **Every cited reference appears in the bibliography** | ✅ 0 undefined citations; all 13 entries resolve |
| 6 | **Highlight count and length** | ✅ **5** highlights (FFA requires 3–5), lengths **75, 78, 75, 73, 75** characters — all ≤ 85. *(From `PAPER/FFA_FORMATTED_SUBMISSION/HIGHLIGHTS.md`; marked PENDING AUTHOR CONFIRMATION there.)* |
| 7 | **Sections and appendices present** | ✅ 10 numbered sections (§1–§10) + **Appendix A** (Certification table and comparison data) + **Appendix B** (Reproducibility). Appendix tables numbered **Table A.1**, **Table A.2** per Elsevier convention. |
| 8 | **Acknowledgements, funding and competing interests present** | ✅ all three on p. 37. Funding: "did not receive any specific grant…". Competing interests: "declares no known competing financial interests". |
| 9 | **Author details present** | ✅ name, institution, full address, country, corresponding-author e-mail — all on p. 1 |
| 10 | **13 worked examples with correct numbering** | ✅ **13** unique examples: 3.13, 3.14, 4.12, 4.13, 5.12, 5.13, 5.14, 5.15, 6.16, 6.17, 7.11, 7.12, 8.12. `verify_examples.py`: 56/56. |
| 11 | **28 certified codes present** | ✅ Table A.1 lists all 28; re-derived from the published `certified_codes.csv` |
| 12 | **No colour / no vertical rules** | ✅ `\vline` count **0**; all 7 tables use `booktabs` (`\toprule`/`\midrule`/`\bottomrule`); 0 vertical rules. *(Note: hyperlinks are coloured via `hyperref` `colorlinks=true` — permitted, and harmless for a review PDF.)* |
| 13 | **No unresolved placeholders** | ✅ `??` = **0**; `[?]` = **0**; "AUTHOR METADATA TO BE SUPPLIED" **absent** |
| 14 | **125 `[[…]]_q` tuples** | ✅ **125**, sorted list identical to Phase 19 |
| 15 | **Quantified results intact** | ✅ 21 theorems, 9 propositions, 11 lemmas, 2 corollaries; 125 tuples; 28 certified codes |
| 16 | **No placeholder author metadata** | ✅ none |

## I5. SHA-256 of the package

| file | SHA-256 |
|---|---|
| `build/main.pdf` | `d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1` |
| `main.tex` | `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0` |
| `references.bib` | `73388338bb83adb695db32d2f69b3d2c8d7279647c546cf4da4b9dc5abd22feb` |
| `sections/01_introduction.tex` | `3b7dd120c137c5bdf08d27c8452afa5048cb8f8eced5fe2c505184f3f548fa78` |
| `sections/02_literature.tex` | `d7b92a2ff1cedb6e325f5ce59fa72fb98d39ae7a8b8de02c03173c4b353de0c5` |
| `sections/03_preliminaries.tex` | `f595c690fa7b36179515d0db3ba6ab65de0b67cdd2e157efcd842c2ef973c9dd` |
| `sections/04_cyclic_galois.tex` | `5cb71fcf6f627a940ac835df3ee1db5bc8a5799a5843301f336cb681a5075779` |
| `sections/05_hulls.tex` | `9aae2d7aa4df85144ddf2da49070e31a66ce7a783a3ab69c8c676fc4ac8ab5c6` |
| `sections/06_gray.tex` | `1f34e5da2992a6826a0051fe07ef821c17b59afd2814fc99183a9cff9431b9a1` |
| `sections/07_quantum.tex` | `838d354d279e8a4b1fd60816b9f4ea0d8e1f9818b887557e45ba2d2afe9e9a55` |
| `sections/08_certification.tex` | `15d94372e3d795fad91fa1b738243ec5aaa400d1d264167c81331b4343d99ed8` |
| `sections/09_comparison.tex` | `f0a6d5adaa83c25a631d16ccba6c82a09d7a994b341ad077bf7bc161bc292be1` |
| `sections/10_conclusion.tex` | `4413432cbc1fce848e280790038eb5f7b4ef0ff38d7ab07e9f7c55cb67ed7011` |
| `sections/appendix_reproducibility.tex` | `8938d5eb359dbd8339dda29e2624eb1bdabd95b381c311d252259ac80cd3e67f` |
| `sections/appendix_tables.tex` | `ce67be41958a4d2acfb214a9708d0b63d42fedd72c5a7be3b81d6ef1f5367933` |

(The 10 `compile/` files are unchanged from `PAPER/FFA_FORMATTED_SUBMISSION/compile/`
and are listed in the Phase 19 manifest.)

## I6. Protected-hash verification — before and after

| | |
|---|---|
| Hashes recorded before this phase | **137** (`/tmp/p23_pre.txt`) |
| Verified after all Phase 23 work | **137 OK, 0 FAILED, 0 missing** |

Nothing protected was touched. The only modification to a tracked file in the
whole workspace is `PAPER/FFA_FORMATTED_SUBMISSION/SHA256_MANIFEST.txt`, which
was **regenerated** this phase because the gitignored `*.log` files were lost in
the workspace restore and had to be reproduced; the manifest now reports **55
entries, 55 OK** (it had read 49/55 while the logs were missing).

## I7. Reproducibility cross-check

As an independent confirmation that the toolchain is sound, the Phase 19
manuscript was rebuilt in this workspace after the restore. Its PDF came out at
**580,175 bytes, SHA-256
`a87491e2ac5071a896b4fd29d25054dc3de9a51275bd2d9dda32975a7f1bff68`** —
**byte-identical** to the Phase 19 record. The same toolchain therefore produced
the V2 PDF; the difference between the two PDFs is attributable solely to the
Data availability block.

---

# Part 3 — What this build does and does not establish

**Established by this build:** the package compiles cleanly, all 13 references
resolve, all 13 examples verify, all 28 certified codes are present, the
mathematical content is byte-identical to Phase 19 outside the Data
availability block, and nothing protected was altered.

**NOT established, and not claimable:**

* that the package is **ready to submit** — seven author attestations are
  outstanding;
* that the **generative-AI declaration** is settled — it is a placeholder;
* that the **data-availability wording** is final — it is marked PROPOSED;
* that the deposit **satisfies Option C** — editorial confirmation is pending;
* that the **comparison-section wording** about entanglement-assisted tables is
  correct — it is not, and a correction is proposed but **not applied**;
* that any licence applies to the deposit — none does.
