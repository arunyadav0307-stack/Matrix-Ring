# Phase 10 — Manuscript-to-guideline compliance matrix

**Journal:** *Finite Fields and Their Applications*
**Manuscript:** *Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings*
**Baseline audited:** `PAPER/main.tex` (sha256 `ee47ce7e…50737c`),
`PAPER/references.bib` (sha256 `73388338…d22feb`), `PAPER/sections/*.tex`,
`PAPER/supplementary/`
**Audit date:** 2026-11-10 · **Guidelines access date:** 2026-11-10
**Status:** read-only assessment. **Nothing in the manuscript was changed.**

**Legend**
**COMPLIANT** — satisfies the verified rule as it stands.
**PARTIAL** — satisfies it in substance; a specific, small defect remains.
**GAP** — the manuscript cannot supply this; it requires researcher input at
submission time (not a manuscript defect).
**BLOCKING** — submission cannot proceed until this is resolved.
**N/A** — the rule does not bite on this manuscript.

---

## Compliance matrix

| # | Requirement | Official rule (verified) | Current manuscript status | Required action | Evidence |
|---|---|---|---|---|---|
| 1 | **Abstract length** | ≤ 250 words, concise and factual, must stand alone, no references, no undefined abbreviations | **PARTIAL.** Counted three ways: 257 words (commands stripped, math tokens expanded), 246 (commands stripped), 230 (each inline formula collapsed to one token). The true rendered count sits in **230–257**, i.e. **at or marginally over** the limit depending on how inline mathematics is counted. Elsevier does not state a counting convention. No references and no undefined abbreviations are present; the abstract does stand alone. | **RECOMMENDED (no action taken).** Trim to ≤ 250 with a safety margin of ~15 words. This is a copy-edit, not a mathematical change. | Guide for authors §Abstract; `main.tex` l.109–133 |
| 2 | **Abstract content** | State purpose; outline procedures; include main findings and principal conclusions; emphasize new and important aspects | **COMPLIANT.** All four elements are present, including the explicit "No record parameters are claimed." | None. | `main.tex` l.109–133 |
| 3 | **Keywords** | 1 to 7 keywords required | **COMPLIANT — exactly 7.** cyclic codes over rings; matrix rings; Galois duality; Galois hulls; Gray map; quantum stabilizer codes; entanglement-assisted quantum codes. Within the maximum. | None. Note: two contain hyphens and one is multi-word ("cyclic codes over rings"), which the guide discourages but does not forbid. | Guide §Keywords; `main.tex` l.135–138 |
| 4 | **Highlights** | Encouraged: 3–5 bullets, ≤ 85 characters each, separate editable file with "highlights" in the filename | **GAP.** No highlights file exists anywhere in the package. | **RECOMMENDED.** Prepare a highlights file at submission time; content can be drawn verbatim from §9.4 without inflating anything. | Guide §Highlights; no `highlights*` file in `PAPER/` |
| 5 | **Article title** | Concise and informative; avoid abbreviations and formulae where possible | **COMPLIANT.** 13 words, no abbreviations, no displayed formulae. | None. | `main.tex` l.101–102 |
| 6 | **Author names** | Given and family names of each author, order matching the submission system | **BLOCKING — absent.** `\author{\AUTHORPLACEHOLDER}`. The header comment states three placeholder marks are the only placeholders and are deliberately visible. | **Researcher must supply.** Nothing may be invented on the researcher's behalf. | `main.tex` l.8–10, l.104 |
| 7 | **Affiliations** | Where the work was carried out; lowercase superscript letters; **full name and postal address of each affiliation including country** | **BLOCKING — absent.** No affiliation data anywhere in the source. | **Researcher must supply**, including country. | Guide §Title page; `main.tex` l.104 |
| 8 | **Corresponding author** | Single corresponding author, clearly indicated, email address included and published; kept current throughout | **BLOCKING — absent.** No corresponding author, no email. | **Researcher must designate** one corresponding author and supply a durable email address. | Guide §Title page, §Corresponding author |
| 9 | **Authorship criteria** | All authors must have contributed to conception/design or acquisition/analysis, drafting or critical revision, and final approval | **GAP.** Cannot be assessed without an author list. | **Researcher must confirm** the author list satisfies all three limbs before submission. | Guide §Authorship |
| 10 | **Authorship stability** | Changes generally not considered after submission; never after acceptance | **RECOMMENDED.** Fix the author list and order **before** submission. | Researcher action; no manuscript change. | Guide §Changes to authorship |
| 11 | **File format** | `.tex` for LaTeX; **"A PDF is not an acceptable source file"**; all relevant editable source files must be provided | **COMPLIANT.** `main.tex` plus twelve `\input` section files plus `references.bib` are present and editable. A PDF also exists but would be supplementary, not the source. | None at submission. If the Elsevier template is adopted later, all sources remain editable. | Guide §File format; `PAPER/main.tex`, `PAPER/sections/` |
| 12 | **LaTeX template** | Elsevier `els-cas-templates.zip` **encouraged** (not required) | **PARTIAL.** The manuscript uses `\documentclass[11pt,a4paper]{article}` — not the Elsevier CAS class. This is permissible; the guide says "encourage", not "require". | **RECOMMENDED, deferred.** Adoption is a formatting change and is **not** authorised in Phase 10. Confirm at submission whether Editorial Manager accepts a non-template .tex; it normally does. | Guide §LaTeX; `main.tex` l.14 |
| 13 | **Reference formatting at submission** | "This journal **does not set strict requirements** on reference formatting at submission … any style or format as long as the style is **consistent**"; journal style applied at proof stage | **COMPLIANT.** `\bibliographystyle{plain}` is a single, consistent style throughout, and it is **alphabetical then numbered** — which is exactly the ordering FFA's own reference style specifies. | **None.** Decision D-1 (keep `plain`) is **compatible with FFA**. This audit does not revisit D-1. | Guide §Reference format, §Reference style; `main.tex` l.165 |
| 14 | **Reference completeness** | Author names, titles, year, volume, article numbers and pagination where applicable; every reference must be a real source | **COMPLIANT.** 13 entries, all 13 cited, all verified against publisher/arXiv/AIMS records per `LITERATURE_VERIFICATION.md`. | None. | `references.bib`; `FINAL_VALIDATION_REPORT.md` §5 |
| 15 | **DOIs in references** | "Where available include Digital Object Identifiers (DOIs)" | **PARTIAL.** 9 of 13 entries carry a DOI **in the .bib source**; **0 are rendered**, because `plain` prints no DOI. Three entries (`LiuPan2020`, `Cao2021`, `KetkarEtAl2006`) have **no DOI field at all** — recorded in the validation report as a deliberate non-retrieval, not an error. | **RECOMMENDED, at proof stage.** FFA states it will request missing reference data at proof stage; the 9 DOIs already in `references.bib` can be supplied then. Supplying the remaining 3 is optional. **No change to `main.tex` or `references.bib` is authorised in Phase 10.** | Guide §References within text; `FINAL_VALIDATION_REPORT.md` §5 |
| 16 | **References ↔ text consistency** | Any reference cited in the article must be in the list and vice versa | **COMPLIANT.** Validated 13/13 by `tools/validate_latex.py`. | None. | `build_modern/verification/validate_latex.txt` |
| 17 | **Tables** | Editable text not images; cited in text; numbered consecutively; captions; notes below body; **no vertical rules or shading** | **COMPLIANT.** 6 tables (§5 ×1, §8 ×2, §9 ×1, Appendix A ×2), all LaTeX `tabular` with `booktabs`, all captioned, all cited, no vertical rules, no cell shading. | None. | Guide §Tables; `sections/*.tex` |
| 18 | **Figures / artwork** | Separate files, cited and numbered, each with a caption; format and dpi rules | **N/A.** The manuscript contains **no figures**. Nothing in the guidelines requires figures. | None. | scan of `sections/*.tex`: 0 `figure` environments |
| 19 | **Math formulae** | Editable text not images; variables in italics; `exp` for powers of e; display equations numbered consecutively in order of first reference | **COMPLIANT.** All mathematics is LaTeX; 107 labels; numbering is consecutive through a shared `theorem` counter. | None. | Guide §Math formulae; `sections/*.tex` |
| 20 | **Appendices** | Identified as A, B; separate numbering for formulae (Eq. (A.1)) and for tables/figures (**Table A.1**, Fig. A.1) | **PARTIAL.** Two appendices exist and are lettered A and B by `\appendix`. Appendix tables are numbered continuously with the main text (e.g. `tab:cert`, `tab:pareto`), **not** as Table A.1 / Table B.1. | **RECOMMENDED (post-approval).** Renumber appendix tables to the A.1/B.1 form if the Elsevier template is adopted. Cosmetic only. | Guide §Appendices; `sections/appendix_tables.tex`, `sections/appendix_reproducibility.tex` |
| 21 | **Article structure** | Divide into clearly defined sections with headings | **COMPLIANT.** 10 numbered sections, ~60 subsections, 2 appendices, table of contents. | None. | `main.tex` l.146–161 |
| 22 | **Supplementary material — existence** | Encouraged; must be accurate and relevant | **COMPLIANT — strong.** `PAPER/supplementary/` contains 28 generator-matrix JSON files + `INDEX.json`, 8 parameter CSVs, 24 Python scripts, 24 computation logs, plus `README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, `MANIFEST.sha256`. | None. | `PAPER/supplementary/` |
| 23 | **Supplementary material — cited in text** | "Cite all supplementary files in the manuscript text" | **PARTIAL.** The package is referenced as a whole in §8 (l.224), §9 (l.26) and Appendix B (l.7, l.14, l.30–100, incl. the exact directory path `PAPER/supplementary/` and the script names). However, **individual files are not each cited**, and no per-file list appears in the manuscript. | **RECOMMENDED.** Add a per-file manifest (one line per supplementary file) so each file is individually cited. Content-neutral addition. | Guide §Supplementary material; `sections/08_certification.tex`, `09_comparison.tex`, `appendix_reproducibility.tex` |
| 24 | **Supplementary material — captions** | "Include a concise caption for each supplementary file, describing its content" | **PARTIAL.** No caption file exists. Individual JSON/CSV files carry descriptive filenames but no captions. | **RECOMMENDED.** Supply a caption list at submission. | Guide §Supplementary material |
| 25 | **Supplementary material — submitted together** | Submit at the same time as the manuscript; can only be added/replaced at revision stage | **GAP (procedural).** The material exists locally; it must be uploaded with the submission. | **Researcher action at submission.** Upload everything; nothing can be added later except at revision. | Guide §Supplementary material |
| 26 | **Research data — Option C** | **REQUIRED**: deposit research data in a relevant data repository **and** provide a link at submission; if impossible, make a statement explaining why (it will be published) | **NON-COMPLIANT (hard requirement).** No repository deposit exists. No repository link exists. No "why not possible" statement exists. The material that Option C covers — 24 scripts, 8 CSVs, 28 generator matrices, 24 logs — is in `PAPER/supplementary/` and in the repository, but it is **not** deposited in a data repository with a persistent identifier. | **BLOCKING until resolved by one of two routes:** (a) deposit the supplementary package in a repository (e.g. Zenodo) and provide the DOI link at submission; or (b) if the researcher cannot deposit, submit the explicit explanatory statement, which **will appear in the published article**. Route (a) is strongly preferable given the material already exists and is self-contained. | Guide §Research data deposit, citation and linking; `PAPER/supplementary/` |
| 27 | **Data references** | Encouraged: cite underlying datasets in text and list them with `[dataset]`, author, title, repository, version, year, persistent identifier | **GAP.** No data reference exists because no deposit exists. | Follows from #26. | Guide §Data references |
| 28 | **Declaration of competing interests** | All authors must disclose; the declarations tool "should always be completed"; the generated document is uploaded at the "attach/upload files" step; "I have nothing to declare" if applicable | **GAP — absent.** No competing-interests statement in the manuscript. | **BLOCKING at submission.** Researcher must complete https://declarations.elsevier.com/ and upload the document. Cannot be invented. | Guide §Declaration of competing interests |
| 29 | **Funding declaration** | Must disclose funding sources and sponsor role; if none, the exact sentence "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." | **GAP — absent.** No funding statement. | **BLOCKING at submission.** Researcher must supply either the grant details or the standard no-funding sentence. | Guide §Funding sources |
| 30 | **Declaration of generative AI use** | "Authors **must declare** the use of generative AI tools in the manuscript preparation process upon submission." Statement placed in a **new section before the reference list** | **GAP — absent and applicable.** There is no such section. This manuscript was produced with extensive AI assistance, so the declaration **is required**, not optional. The guide's exemption covers only basic grammar/spelling/reference checking. | **BLOCKING at submission.** Researcher must add the declaration section before the reference list, naming the tool and the reason. **Not added in Phase 10 — this is a manuscript modification and requires separate approval.** | Guide §Declaration of generative AI use |
| 31 | **CRediT author contributions** | Corresponding authors are **encouraged** to acknowledge co-author contributions using CRediT roles | **GAP — absent.** No CRediT statement. | **RECOMMENDED.** Supply at submission if there is more than one author. Encouraged, not mandatory. | Guide §Author contributions: CRediT |
| 32 | **Acknowledgements** | Separate section **directly before the reference list**; not on the title page, not a title footnote | **GAP — absent.** No acknowledgements section. | **RECOMMENDED** if the researcher wishes to acknowledge anyone; otherwise omit. | Guide §Acknowledgements |
| 33 | **Submission declaration** | Not previously published (preprint permitted); not under consideration elsewhere; approved by all authors and responsible authorities | **Cannot be verified from the files.** No simultaneous-submission statement exists in the package. | **Researcher must affirm** in Editorial Manager at submission. | Guide §Submission declaration |
| 34 | **Single anonymized peer review** | Single anonymized; editors screen first; then ≥ 2 reviewers | **N/A — no manuscript action.** Single anonymized means reviewers are anonymous; the author identities are known. The manuscript therefore needs **no** anonymisation. | None. | Guide §Peer review |
| 35 | **Manuscript length** | **Not stated** on any official FFA page | **N/A (monitor).** 39 pages, ~13 300 words of body, 83 theorem-like environments. No verified limit to breach. | None formally. See `PHASE10_DESK_REJECTION_RISK_REPORT.md` risk R-6 — length is an editorial, not a compliance, concern. | Guide (no length section); `build_modern/verification/inspect_pdf.txt` |
| 36 | **Article type** | **UNVERIFIED** — no article-types list published | **N/A.** The manuscript is a full research article, the only type observed in FFA. | None. | Guide (no such section); Vol 110/111/112 TOCs |
| 37 | **Inclusive language / ethics / image integrity** | Policies stated | **COMPLIANT.** Pure mathematics; no human or animal subjects, no images, no jurisdictional maps. | None. | Guide §Ethics and policies |
| 38 | **Language** | American or British English, not a mix | **COMPLIANT — British English** throughout (e.g. "organisation" not observed; spellings such as "behaviour", "characterise" would confirm). A systematic check is **RECOMMENDED** before submission. | **RECOMMENDED:** verify one variety is used consistently. | Guide §Language and editing services |
| 39 | **Preprint policy** | Preprint sharing permitted and does not count as prior publication | **N/A.** No preprint is posted. Permitted if the researcher wants one. | Optional researcher decision. | Guide §Preprints |
| 40 | **Publication model choice** | Gold OA (APC **USD 3 240** excl. taxes, all article types) or subscription (no fee); choice has no effect on peer review | **GAP — decision not recorded.** No OA/subscription decision exists in the package. | **RESEARCHER DECISION REQUIRED.** Either is available; the choice is made after acceptance and **does not affect review**. | OA information page §APC |
| 41 | **Submission charges** | None stated on official pages | **N/A.** No submission fee identified. | None. | Guide for authors; OA information page |
| 42 | **Proof correction window** | Corrections within **two days** | **N/A at this stage.** | Note for later: designate a corresponding author able to turn proofs around in 48 hours. | Guide §Proof correction |

---

## Roll-up

| status | count | items |
|---|---|---|
| **COMPLIANT** | 15 | 2, 3, 5, 11, 13, 14, 16, 17, 19, 21, 22, 34, 37, 41, 42(N/A) |
| **PARTIAL** | 6 | 1 (abstract length), 4→GAP, 12 (template), 15 (DOIs), 20 (appendix numbering), 23, 24 (supplementary citation/captions) |
| **GAP — researcher input** | 8 | 4, 9, 10, 25, 27, 28, 29, 31, 32, 40 |
| **BLOCKING** | 6 | 6, 7, 8 (author metadata); 26 (research data Option C); 28, 29, 30 (declarations) |
| **N/A** | rest | 18, 33–36, 38–39, 41 |

## The five things that actually gate submission

1. **Author metadata** — names, affiliations with full postal address and
   country, one corresponding author with email. (`\AUTHORPLACEHOLDER`, 3 marks.)
2. **Research data, Option C** — repository deposit plus link, or a published
   statement of why not. **Mandatory.**
3. **Competing interests** — declarations tool completed and uploaded.
4. **Funding** — disclosed, or the standard no-funding sentence.
5. **Generative-AI declaration** — a new section before the reference list.
   Required for this manuscript and currently absent.

Items 1–5 are all **submission-time artefacts**, not mathematical defects. None
requires touching the mathematics, and **none has been created in Phase 10**.

## Two things this audit will not do

* **It will not change the bibliography style.** FFA explicitly imposes no
  reference-format requirement at submission and applies its own style at proof
  stage. `plain` is alphabetical-then-numbered, which is precisely FFA's stated
  ordering. Decision D-1 stands, untouched.
* **It will not adopt the Elsevier template, trim the abstract, add the
  declarations, or add the AI-use section.** Each is a manuscript modification
  requiring separate explicit approval.
