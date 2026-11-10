# Task A — FFA / Elsevier formatting requirements, re-verified

**Primary source (all items below):**
<https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/guide-for-authors>
**Access date: 2026-11-10** (re-fetched this phase; sandbox UTC).

Supporting sources consulted this phase:

| source | URL | accessed |
|---|---|---|
| Journal home | <https://www.sciencedirect.com/journal/finite-fields-and-their-applications> | 2026-11-10 |
| Submission portal | <https://submit.elsevier.com/FFA> | 2026-11-10 |
| LaTeX support / template | <https://www.elsevier.com/latex> | 2026-11-10 |
| Research-data guidelines (Option C) | <https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines> | 2026-11-10 |

**Finding: the official guidelines are UNCHANGED** from the Phase 10 audit
(same access-dated source). Every requirement quoted below was re-read from the
live page in this phase and matches the Phase 10 record verbatim. The Phase 10
*compliance score* was **not** relied upon; requirements were re-verified
independently against the live text and then against the manuscript.

---

## Requirement-by-requirement

| # | requirement | official wording (abridged) | manuscript status |
|---|---|---|---|
| 1 | **Article type** | No formal article-type list is published for FFA; observed types in 2026 volumes are *Research article* and *Editorial*. | **Compliant** — full research article. |
| 2 | **Title page** | "Article title… **Author names**… **Affiliations**… using a **lowercase superscript letter** immediately after the author's name… full name and postal address… **including the country name**… **Corresponding author**… email address **must be included on the title page**." | **Compliant** — title; single author with `\textsuperscript{a}`; institution, organisation, street, city, state, postal code **122103**, country **India**; corresponding-author email present. |
| 3 | **Abstract** | "concise and factual abstract that **does not exceed 250 words**… stand alone… **Avoid references**… avoid non-standard or uncommon abbreviations." | **Compliant** — 231 / 217 / **244** under C1/C2/C3 (strictest), margin 6. Zero `\cite` in the abstract. |
| 4 | **Keywords** | "**1 to 7 keywords**… written in English… avoid keywords consisting of multiple words (using 'and' or 'of')." | **Compliant** — exactly **7**; none uses "and"/"of". |
| 5 | **Highlights** | "**encouraged**… **3 to 5 bullet points**, each a **maximum of 85 characters, including spaces**… separate editable file… with the word 'highlights' in the file name." | **Encouraged, not required.** Prepared as `HIGHLIGHTS.md` (separate file, 5 bullets). **Author confirmation required before upload.** |
| 6 | **MSC** | Not required by the FFA guide. | Present in the manuscript; harmless. |
| 7 | **LaTeX / file format** | "**.tex for LaTeX files**. **A PDF is not an acceptable source file.**"… "We **encourage** you use our LaTeX template… provide **all relevant editable source files**." | **Compliant** — full `.tex` sources shipped. The Elsevier CAS template is *encouraged, not mandated*; migration was **considered and declined** (see §Decisions). |
| 8 | **Math formulae** | "editable text, not images… **Present variables in italics**… **Denote powers of e by exp**… number them **consecutively**." | **Compliant after one change** — `e^{2\pi i x/p}` → `\exp(2\pi i x/p)`. Variables are italic (LaTeX math mode); equations numbered consecutively (12). |
| 9 | **Tables** | "editable text, not images… **Cite all tables**… **Number tables consecutively**… provide captions… notes below the table body… **Avoid vertical rules and shading within table cells**." | **Compliant** — 6 tables, all cited, all captioned; **0** vertical rules, **0** shading macros, no `colortbl`. |
| 10 | **Figures** | Number consecutively, cite in text, separate files. | **Not applicable** — the manuscript contains **0** figures. |
| 11 | **Equation numbering** | "numbering them consecutively in the order they are referred to". | **Compliant** — 12 numbered equations; **0** in appendices. |
| 12 | **Appendix numbering** | "Identify individual appendices… **A, B, etc.**… give separate numbering to tables and figures using formats such as **Table A.1**; Fig. A.1". | **Compliant** — Appendices A and B; **Table A.1** and **Table A.2**; no appendix equations or figures requiring `Eq. (A.1)`. |
| 13 | **References** | "This journal **does not set strict requirements on reference formatting at submission**… any style **as long as the style is consistent**… **Our journal reference style will be applied… at proof stage.**" Indicate by "a number within square brackets"; "list… arranged **alphabetically and then numbered**." "**Where available include Digital Object Identifiers (DOIs)**." | **Compliant** — `plain.bst` gives bracketed numerals sorted alphabetically, matching the stated style. **DOI caveat recorded below.** |
| 14 | **Supplementary material** | "**Cite all supplementary files in the manuscript text**… submit at the same time… include a **concise caption for each supplementary file**… appear online exactly as received." | **Partially compliant** — the package is cited repeatedly in the text (9 mentions, 10 `\filepath` references). **A per-file caption list is not yet provided**; flagged as pending. |
| 15 | **Research data** | "For this journal, **Option C** … you are **required** to: **Deposit your research data in a relevant data repository**; **Provide a link to the dataset during the submission process**; if sharing isn't possible, **make a statement explaining why**." | **NOT RESOLVED.** The researcher's standing decision is the existing public GitHub repository only, and the supplementary data are absent from the default branch. See §Open items. |
| 16 | **Declarations** | Competing interests, funding, generative AI, data availability, CRediT (encouraged), acknowledgements in a separate section before the reference list. | Funding, competing interests, generative-AI and data-availability sections **present**; the generative-AI text is **pending researcher confirmation** (deferred). |

### DOI caveat (recorded honestly)

The guideline's "References within text" section states *"Where available include
Digital Object Identifiers (DOIs)"*. Nine of the thirteen entries in
`references.bib` carry a `doi=`, but `plain.bst` has no `doi` field, so none
render in the PDF. The same guide also states that reference formatting is
applied by the journal at proof stage. Both facts are recorded: **the current
style is acceptable for initial submission, and the DOIs are present in the
source**, so nothing is lost — but if the researcher wants DOIs visible before
proof stage, a DOI-capable style (e.g. `plainurl`) should be adopted as a
deliberate separate change. Not changed in this phase.

## Decisions taken

* **Elsevier CAS LaTeX template — declined.** It is *encouraged*, not required.
  Migrating would require reworking the preamble, theorem environments, author
  block and bibliography macros in a manuscript that currently builds with zero
  errors, for no compliance gain. Recorded as a conscious choice, not an
  oversight.
* **Bibliography style — retained** as `plain`; explicitly permitted.
* **CRediT statement — not added.** Encouraged for corresponding authors; with a
  single author the safeguard against inventing contribution roles applies. Left
  for the researcher.

## Open items this phase cannot close

1. Research-data deposit / link (Option C) — **required**, unresolved.
2. Per-file captions for the supplementary package — **recommended**, not yet written.
3. Generative-AI declaration text — **deferred**, pending researcher.
4. Highlights file — prepared, pending author confirmation.
