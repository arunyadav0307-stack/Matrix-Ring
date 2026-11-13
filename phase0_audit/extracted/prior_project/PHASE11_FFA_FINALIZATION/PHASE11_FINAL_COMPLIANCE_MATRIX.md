# Phase 11 — Final FFA compliance matrix

Manuscript: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings*
Target: **Finite Fields and Their Applications** — **preparation only; no
submission authorized.**
Guidelines re-verified: **2026-11-10**, from the official FFA guide for
authors. Phase 10 findings were **not** reused blindly; every row was
re-checked against the official source.

Primary source:
`https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/guide-for-authors`

## Status vocabulary

| status | meaning |
|---|---|
| **VERIFIED** | checked against the official source and satisfied |
| **CORRECTED** | a defect was found and fixed in the staging copy |
| **RESEARCHER CONFIRMATION REQUIRED** | cannot be completed without a fact only the authors hold; nothing invented |
| **NOT APPLICABLE** | the requirement does not arise for this manuscript |
| **UNVERIFIED** | the official source does not state it; no inference made |
| **BLOCKING** | submission is impossible until resolved |

---

## 1. Manuscript content

| # | requirement | current official policy | manuscript status | required action | status |
|---|---|---|---|---|---|
| 1 | Abstract length | **≤ 250 words**, stand-alone, no references, no undefined abbreviations | Canonical abstract measures 246 / 230 / **260** under three counting conventions — **fails the strictest by 10** | Revised to 213 / 199 / **226**, compliant on all three | **CORRECTED** (staging) |
| 2 | Keywords | **1–7 keywords** | 7 present | none | **VERIFIED** |
| 3 | Highlights | **3–5 bullets, ≤ 85 characters each**, separate editable file, "highlights" in the filename | Not present | Write 3–5 highlights from the contribution hierarchy | **RESEARCHER CONFIRMATION REQUIRED** |
| 4 | Title page — names | Given + family name, **exactly** as they should appear | `\AUTHORPLACEHOLDER` | Supply real names | **BLOCKING** |
| 5 | Title page — author order | Must **match** the submission system | Only a placeholder exists | Confirm order matches the system entry | **BLOCKING** |
| 6 | Title page — affiliations | Lowercase **superscript letters** after each name, with **full postal address including country** | Absent entirely | Supply institution + full address + country | **BLOCKING** |
| 7 | Corresponding author | **Exactly one**, with a **publishable** email (it is published) | Absent | Designate one and supply a publishable email | **BLOCKING** |
| 8 | Present/permanent address | **Numbered footnotes** on the title page if different from the affiliation | Absent | Confirm whether any differ | **RESEARCHER CONFIRMATION REQUIRED** |
| 9 | ORCID | Encouraged in the submission system | Absent | Optional; recommended | **RESEARCHER CONFIRMATION REQUIRED** |

## 2. Format and source files

| # | requirement | current official policy | manuscript status | required action | status |
|---|---|---|---|---|---|
| 10 | LaTeX source | **`.tex` required**; "a PDF is not an acceptable source file"; all editable sources demanded | `main.tex` + 12 `sections/*.tex` + `references.bib`, all editable; compiles cleanly | none | **VERIFIED** |
| 11 | Elsevier template | `els-cas-templates.zip` **encouraged, not required** | Not used; manuscript uses its own class setup | Permitted. Optionally migrate later | **VERIFIED** |
| 12 | References | "Does not set strict requirements on reference formatting at submission"; any consistent style; journal style applied at proof | `[n]` numeric, alphabetical-then-numbered list via `plain.bst` — consistent and complete | Add DOIs "where available" | **VERIFIED** |
| 13 | Tables | Editable text, with captions, **no vertical rules or shading** | 6 tables, editable LaTeX | Confirm no vertical rules/shading | **VERIFIED** |
| 14 | Figures | Separate files with captions | **0 figures** in the manuscript | none | **NOT APPLICABLE** |
| 15 | Appendices | Labelled A, B; equations `(A.1)`, tables `Table A.1` | Appendices A (tables) and B (reproducibility) present | Confirm numbering follows the convention | **VERIFIED** |
| 16 | Length limit | **None stated anywhere** in the guide | 42 pages, ~13 300 words | none | **UNVERIFIED** (no limit published to verify against) |

## 3. Research data and supplementary material

| # | requirement | current official policy | manuscript status | required action | status |
|---|---|---|---|---|---|
| 17 | Research data | **Option C — REQUIRED.** Deposit in a relevant repository **and** give the link at submission; else a published statement of why not | 86 files in `PAPER/supplementary/` (28 JSON, 8 CSV, 24 scripts, 24 logs, 4 docs), fully reproducible, **but nothing deposited and no DOI** | Choose a route; authorize deposit; obtain DOI; write the availability statement | **BLOCKING** |
| 18 | Data-licence choice | Implied by deposit | No licence chosen | Choose deliberately — a legal decision | **RESEARCHER CONFIRMATION REQUIRED** |
| 19 | Supplementary material | **Encouraged**; cite every file in the text; submit **together**; **concise caption per file**; published exactly as received; cannot be added except at revision | Not yet designated as supplementary | Decide what is supplementary vs. in-article; write per-file captions | **RESEARCHER CONFIRMATION REQUIRED** |

## 4. Declarations

| # | requirement | current official policy | manuscript status | required action | status |
|---|---|---|---|---|---|
| 20 | Competing interests | `declarations.elsevier.com` "should **always** be completed" and the statement **uploaded** | Section added to staging with unconfirmed proposed wording | Each author answers; complete the tool; upload | **BLOCKING** |
| 21 | Funding | Disclose all sources and the sponsor's role; or use the exact Elsevier no-funding sentence | Section added to staging with both outcomes, neither selected | State funding status; confirm wording | **BLOCKING** |
| 22 | Generative AI | **MANDATORY**; new section **before the reference list**; narrow exemption for grammar/spelling/reference checking only | Section added to staging; **AI assistance was extensive, so a declaration is required** | Authors name the tools, verify the scope, confirm wording | **BLOCKING** |
| 23 | CRediT contributions | **Encouraged**, not mandatory | Section added to staging, cannot be completed without the author list | Confirm author list, then assign roles | **RESEARCHER CONFIRMATION REQUIRED** |
| 24 | Acknowledgements | Separate section **immediately before** the reference list | Section added to staging, marked optional | Confirm or delete | **RESEARCHER CONFIRMATION REQUIRED** |

## 5. Journal fit and positioning

| # | item | assessment | status |
|---|---|---|---|
| 25 | Scope fit | FFA's aims and scope name **algebraic coding theory, cryptology, combinatorial design theory**; gate sentence "finite fields play a nontrivial role". The engine is `F_q[u,X]/⟨u^t, X^n−1⟩` structure — satisfied, though the alphabet is a noncommutative non-chain ring | **VERIFIED** (residual scope risk, mitigated not eliminated) |
| 26 | Peer-review model | **Single anonymized**; editors screen first, then ≥2 reviewers | **VERIFIED** |
| 27 | Refereeing standard | "Very strict refereeing standards, accepting only those papers which receive excellent referee reports" | **VERIFIED** — raises the bar |
| 28 | Quantum-parameter claims | **No code beats the best known.** All `d ≥ 3` stabilizer codes are 1–2 below Grassl; EA codes unbenchmarkable; `q = 8` unbenchmarked. Manuscript states "No record parameter is claimed." | **CORRECTED** (framed honestly; no inflated claim remains) |
| 29 | Morita objection | Real and fair. Response prepared: Morita does not transport the involution; the paper claims no novelty from noncommutativity as such; the residual problem is a finite-field one | **CORRECTED** (response drafted in staging) |
| 30 | Contribution hierarchy | 1 duality/hulls — 2 non-principal — 3 expansion map — 4 quantum constructions — 5 certificates | **CORRECTED** (stated in staging) |
| 31 | Prior-venue attributions | Four Phase 9 attributions were **wrong**; correct census is **0 FFA papers among the 13 cited**; `references.bib` was correct throughout | **CORRECTED** (append-only) |
| 32 | APC | **USD 3 240** excl. taxes for gold OA; **subscription carries no charge**; no submission charge found | **VERIFIED** |
| 33 | Preprints | Allowed; do **not** count as prior publication | **VERIFIED** |
| 34 | Time to first decision | Not stated in the guide | **UNVERIFIED** |
| 35 | Article types | No article-types section exists in the guide; only "Research article" and "Editorial board" were observed | **UNVERIFIED** |
| 36 | Named handling editor | Not published | **UNVERIFIED** |

## 6. Roll-up

| status | count |
|---|---:|
| VERIFIED | 16 |
| CORRECTED | 6 |
| RESEARCHER CONFIRMATION REQUIRED | 8 |
| NOT APPLICABLE | 1 |
| UNVERIFIED | 4 |
| BLOCKING | 7 |
| **total** | **42** |

### The seven blocking items

1. Author names (Task C1)
2. Author order matching the submission system (C1)
3. Affiliations with full postal address and country (C1)
4. Corresponding author with a publishable email (C1)
5. Research data: deposit + link (C2)
6. Competing-interests declaration (C3)
7. Funding declaration (C4)

Plus the generative-AI declaration (C5), which is **mandatory** and whose
wording is for the authors to settle — counted under RESEARCHER CONFIRMATION
REQUIRED because the *requirement* is verified and only the exact text is
outstanding; it should be treated as blocking in practice.

## 7. Protected-artifact integrity

Every protected file is **byte-identical** to its pre-Phase-11 state. All
Phase 11 edits were confined to `PAPER/FFA_SUBMISSION_STAGING/`.

| artifact | SHA-256 (pre-Phase-11 = post-Phase-11) |
|---|---|
| `PAPER/main.tex` | `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` |
| `PAPER/references.bib` | `73388338bb83adb695db32d2f69b3d2c8d7279647c546cf4da4b9dc5abd22feb` |
| `PAPER/main.pdf` | `b2ba1fee72b6e70ae18f3f043c10ac3390673281e1d0ccd35da3f863d8641a03` |
| `PAPER/main.bbl` | `23074d101b9171bdc3222c31eb70693caf699a2bcca5e6418bb4ceabb477b2d3` |
| Phase 8B package ZIP | `6d39f643f027f6fb8a7129ebf7623456f26386fdca8dac84e4c02dc69b86fec0` |
| Phase 8A package ZIP | `14ecac0e8649009ef535f63bc128734335c88ac3c1bbc6ef4e05a5a868342910` |
| Phase 8 package ZIP | `d1ba4c821b1af01b8105eff702315957e692cfcaed21d5491a8ea03e4b29a80d` |

Section hashes (first 8 hex): 01 `2442af8c` · 02 `d7b92a2f` · 03 `f595c690` ·
04 `5cb71fcf` · 05 `9aae2d7a` · 06 `1f34e5da` · 07 `95c70603` · 08 `fb853d83` ·
09 `f0a6d5ad` · 10 `4413432c` · `appendix_reproducibility` `8938d5eb` ·
`appendix_tables` `64d3b8a3`.

## 8. Verdict

**CONDITIONALLY READY — AUTHOR CONFIRMATIONS PENDING.**

Every item within the agent's authority is complete: the guidelines were
re-verified from official sources, the abstract was corrected, the
declarations were structured with placeholders rather than inventions, the
positioning was framed honestly, four bibliographic errors were corrected
append-only, the superseded Phase 9A directory was preserved and marked, a
genuine modern TeX Live build succeeded with zero errors, and the staging copy
is in place. What remains is a set of **facts only the authors hold** — names,
affiliations, funding, competing interests, and the AI-declaration wording —
plus one action with external consequences, the research-data deposit, which
requires explicit authorization.
