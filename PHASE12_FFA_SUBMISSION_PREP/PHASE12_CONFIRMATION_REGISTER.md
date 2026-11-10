# Phase 12 / Task A — Researcher confirmation register

The single authoritative register of what the researcher has and has not
confirmed. **Nothing in this register was inferred.**

Manuscript: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings*
Target: **Finite Fields and Their Applications**
Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring` · Base commit: `a731ac7`

## Status vocabulary

| status | meaning |
|---|---|
| **CONFIRMED** | the researcher explicitly supplied or selected this value |
| **PENDING** | required, not yet supplied; nothing substituted |
| **VERIFIED** | independently checked by the agent, no researcher input needed |

---

## A1. Author names — **PENDING**

| field | value | status |
|---|---|---|
| Number of authors | **1** (single author) | CONFIRMED (count only) |
| Given name(s) | — | **PENDING** |
| Family name | — | **PENDING** |
| Name as it must appear | — | **PENDING** |

**Confirmed:** the researcher selected *single author*.
**Not supplied:** the name itself. The option was selected without the
accompanying text.

**Constraints honoured:** no name was inferred from the GitHub account
`arunyadav0307-stack`, from prior conversation, or from any institutional
reference. Author count was not defaulted to one — it was *selected*.

**Effect:** the title page cannot be completed. This is **BLOCKING**.

## A2. Author order — **PENDING (partially resolved)**

| field | value | status |
|---|---|---|
| Number of authors | 1 | CONFIRMED |
| Sequence | n/a for a single author | VERIFIED |

With one author there is no ordering decision, so **A2 is not independently
blocking** — but it cannot be finalised until A1 supplies the name. The
manuscript text uses "we" throughout, which is unremarkable for a
single-author mathematics paper; no change was made on that basis.

**Note:** FFA requires the manuscript's author order to match the order
entered in the submission system. With one author this is trivially
satisfiable, but must still be checked at submission.

## A3. Institutional affiliations — **PENDING**

The researcher selected *"I'll provide full details"* but **supplied no text**.

| field | author 1 | status |
|---|---|---|
| Institution | — | **PENDING** |
| Department or school | — | **PENDING** |
| University or organisation | — | **PENDING** |
| Street and postal address | — | **PENDING** |
| City | — | **PENDING** |
| State | — | **PENDING** |
| Country | — | **PENDING** |

**What FFA requires (verified 2026-11-10, official guide):**

> "Affiliations, referring to where the work was carried out, below the author
> names. Indicate affiliations using a **lowercase superscript letter**
> immediately after the author's name and in front of the corresponding
> address. Ensure that you provide the **full name and postal address of each
> affiliation, including the country name**."

The guide also states: "Authors should use either the **full, standard title**
of their institution or the standard abbreviation of the institutional name so
that the institutional name can be **independently verified for research
integrity purposes**."

**Constraints honoured:** no affiliation was inferred from institutions named
in the cited literature (Kent State, University of Delhi, IIT ISM Dhanbad,
Lovely Professional University all appear in the bibliography) or from
anything in earlier conversation.

**Effect:** the title page cannot be completed. **BLOCKING.**

## A4. Corresponding author — **PENDING**

The researcher selected *"I'll provide the email"* but **supplied no text**.

| field | value | status |
|---|---|---|
| Name | follows from A1 | **PENDING** |
| Publishable email address | — | **PENDING** |
| Institution | follows from A3 | **PENDING** |
| Country | follows from A3 | **PENDING** |

**What FFA requires:**

> "Corresponding author. Clearly indicate who will handle correspondence for
> your article: during the peer review and publication process, and also after
> publication. This responsibility includes answering any future queries about
> your results, data, or methodology. The **email address of the corresponding
> author must be included on the title page and will be published in the
> article**."

**Constraints honoured:** no email was invented, guessed, or substituted. A
personal or no-reply address was not assumed.

**Effect:** the title page cannot be completed. **BLOCKING.**

## A5. Research-data repository — **VERIFIED (repository) / PENDING (deposit)**

### What was verified

| check | result |
|---|---|
| Repository | `arunyadav0307-stack/Matrix-Ring` |
| Visibility | **public** |
| Licence | **NONE** — the repository declares no licence |
| Releases | **0** |
| Tags | **0** |
| Default branch | `main`, at `ea43e959` (2026-11-04) |
| Working branch | `arena/59de606f-matrix-ring`, at `a731ac7` (2026-11-10) |
| Branch relation | session branch is **35 commits ahead** of `main`, 0 behind |
| `PAPER/supplementary/` on `main` | **ABSENT (404)** |
| `PAPER/supplementary/` on session branch | **present, 8 top-level entries** |

### Does the repository as it stands satisfy FFA Option C?

**No — not yet.** FFA requires:

> "Deposit your research data in a relevant data repository. Provide a link to
> the dataset during the submission process."

| requirement | status | why |
|---|---|---|
| Data exists and is reproducible | **VERIFIED** | 86 files, 85 hash lines, 28 JSON + 1 index, 8 CSV, 22 scripts, 23 logs, 4 docs |
| Publicly accessible | **PARTIAL** | the branch is public, but a **branch is mutable** and can be deleted or force-pushed; it is not a citable object |
| Persistent identifier | **NOT SATISFIED** | no DOI exists; no release and no tag exists |
| Citable/stable snapshot | **NOT SATISFIED** | `main` does not even contain the data, so a reader following the default branch would not find it |
| Licence | **NOT SATISFIED** | repository declares none; a data deposit needs an explicit licence |

### Conclusion and recommendation

A GitHub repository branch is **not** a data repository in the sense FFA
Option C requires, because it carries no persistent identifier and is
mutable. **A DOI-based archive is recommended.**

Two prepared routes — **neither executed**, because both are public,
permanent and mint a DOI:

| route | mechanism | consequence |
|---|---|---|
| **R1** — GitHub release → Zenodo | Tag a release on the session branch; the GitHub–Zenodo integration archives it and Zenodo mints a DOI | Public, permanent, DOI minted; archives the whole repository unless scoped |
| **R2** — direct Zenodo upload | Build a clean `PAPER/supplementary/` bundle and upload it directly to Zenodo with chosen metadata | Public, permanent, DOI minted; **full control over scope** — recommended |

**Recommendation: R2**, because the repository contains audit and working
documents (Phases 0–12) that are not intended for publication, whereas
`PAPER/supplementary/` is exactly the research data.

**Also required before deposit:** the researcher must **choose a licence**
(CC BY 4.0 / CC0 / other). The repository currently has none. This is a legal
decision and was not defaulted.

**Not done:** no release, no tag, no deposit, no DOI, no licence — each
requires explicit authorization. See `PHASE12_RESEARCH_DATA_DEPOSIT_PLAN.md`.

### Two repository issues the researcher should know about

1. **`main` does not contain the supplementary data.** Anyone opening the
   repository lands on `main` and will not find `PAPER/supplementary/`. If the
   repository URL is to be cited at all, the session branch must be merged to
   `main` first — a decision for the researcher, since it changes the
   repository's default presentation.
2. **No licence.** Without one, the repository is "all rights reserved" by
   default, which is incompatible with the intent of a data deposit.

## A6. Competing interests — **CONFIRMED**

**Researcher response: "Nothing to declare."**

Elsevier's official guidance (verified 2026-11-10):

> "All authors must disclose any financial and personal relationships with
> other people or organizations that could inappropriately influence or bias
> their work. Examples of potential competing interests include: Employment,
> Consultancies, Stock ownership, Honoraria, Paid expert testimony, Patent
> applications or registrations, Grants or any other funding, Affiliation with
> the journal as an editor or advisory board member."
>
> "Authors with no competing interests to declare should select the option
> *'I have nothing to declare.'*"
>
> "The resulting Word document containing your declaration should be uploaded
> at the 'attach/upload files' step in the submission process. Save the
> document in .doc/.docx format. Author signatures are not required."

**Confirmed declaration text (Elsevier's standard):**

> The authors declare that they have no known competing financial interests or
> personal relationships that could have appeared to influence the work
> reported in this paper.

**Outstanding action (procedural, not a wording issue):** the
`declarations.elsevier.com` tool must still be completed and the generated
`.doc`/`.docx` **uploaded** at the submission step. The agent cannot do this.
Recorded in `PHASE12_RESEARCHER_ACTION_ITEMS.md`.

**Note:** this was *confirmed*, not assumed. The register does not treat
"nothing to declare" as a default.

## A7. Funding — **CONFIRMED**

**Researcher response: "No specific grant."**

Elsevier's official wording (verified 2026-11-10):

> "If no funding has been provided for the research, please include the
> following sentence:
> *This research did not receive any specific grant from funding agencies in
> the public, commercial, or not-for-profit sectors.*"

**Confirmed declaration text:**

> Funding: This research did not receive any specific grant from funding
> agencies in the public, commercial, or not-for-profit sectors.

**Not used** (the funded alternative, preserved here for completeness):

> Funding: This work was supported by [FULL OFFICIAL NAME OF FUNDER],
> [COUNTRY] [grant number [NUMBER]].

**Constraints honoured:** no agency, grant number or award was invented, and
"unfunded" was not inferred from the absence of a grant record in the
repository — it was **explicitly confirmed** by the researcher.

## A8. Generative-AI declaration — **PENDING**

**Researcher response: "Leave PENDING."**

### Official Elsevier requirement (verified 2026-11-10)

Section title:

> **Declaration of generative AI and AI-assisted technologies in the
> manuscript preparation process**

Statement template:

> "During the preparation of this work the author(s) used [NAME OF
> TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s)
> reviewed and edited the content as needed and take(s) full responsibility
> for the content of the published article."

Placement: "a statement at the end of the manuscript when the paper is first
submitted… placed in a **new section before the reference list**."

Exemption: "The declaration does not apply to the use of basic tools, such as
tools used to check grammar, spelling, and references."

### Why a declaration is required here

**AI assistance was extensive and is not covered by the exemption.** The
eight workflow areas named in Task A8, assessed honestly:

| # | area | AI involvement | covered by exemption? |
|---|---|---|---|
| 1 | Literature discovery | Venue attributions and prior-art identification were found by AI web search; four were later found wrong and corrected | **No** |
| 2 | Manuscript drafting and editing | Large portions of the LaTeX source drafted and revised by an AI agent | **No** |
| 3 | Mathematical exploration and proof exposition | Proof structure and exposition developed with AI assistance | **No** |
| 4 | Code development | All 22 supplementary scripts written with AI assistance | **No** |
| 5 | Computational verification assistance | Verification and audit tooling built and run by an AI agent | **No** |
| 6 | Abstract revision and language refinement | The Phase 11 abstract revision was drafted by an AI agent | **No** |
| 7 | Arena AI and ChatGPT usage | Arena AI agent: **yes, extensively**. ChatGPT: **unknown to the agent** — for the researcher to state | **No** |
| 8 | Human evaluation and responsibility | The researcher directed the work and approved each phase; final responsibility is human | n/a |

### What the agent will not assert

* **No tool name, model name, version, or provider is stated.** The researcher
  chose to leave this pending, and the agent will not guess.
* **No usage dates.**
* **No claim that AI independently proved or verified mathematics.** The
  mathematical results are the researcher's; AI assisted with exposition,
  structure, code and checking. All computed parameters come from
  deterministic scripts reproducible from `PAPER/supplementary/`.
* **No claim that AI tools were not used.** They demonstrably were.

### Proposed wording — PENDING RESEARCHER APPROVAL

> During the preparation of this work the author used [NAME OF TOOL/SERVICE]
> to [REASON]. After using this tool/service, the author reviewed and edited
> the content as needed and takes full responsibility for the content of the
> published article.

Note the singular: with one author confirmed (A1/A2), the template should read
"the author" / "takes", not "the author(s)" / "take(s)".

**What is needed:** the tool name(s), the reason, and confirmation of the
final sentence.

---

## Register summary

| category | status | blocking? |
|---|---|---|
| A1 Author names | **PENDING** (count = 1 confirmed) | **YES** |
| A2 Author order | **PENDING** (not independently blocking) | resolved by A1 |
| A3 Affiliations | **PENDING** | **YES** |
| A4 Corresponding author | **PENDING** | **YES** |
| A5 Research data | **VERIFIED** (repo) / **PENDING** (deposit) | **YES** |
| A6 Competing interests | **CONFIRMED** | no — upload action remains |
| A7 Funding | **CONFIRMED** | no |
| A8 Generative AI | **PENDING** | **YES** |

**2 of 8 confirmed. 6 pending, of which 5 are blocking.**

---

## Correction record — Phase 12, append-only

**Correction C1 — supplementary file counts.**

Earlier phase documents (Phase 10 `PHASE10_MANUSCRIPT_COMPLIANCE_MATRIX.md`,
`PHASE10_SCOPE_AND_NOVELTY_ASSESSMENT.md`; Phase 11
`PHASE11_FINAL_COMPLIANCE_MATRIX.md`) state that `PAPER/supplementary/`
contains **24 scripts and 24 logs**. **That is wrong.**

Verified by direct enumeration on 2026-11-10:

| directory | actual count | previously stated |
|---|---:|---:|
| `scripts/` | **22** | 24 |
| `logs/` | **23** | 24 |
| `generator_matrices/` | **29** (28 + `INDEX.json`) | 28 |
| `parameter_tables/` | **8** | 8 ✅ |
| root documents | **4** | 4 ✅ |
| **total** | **86** | 86 ✅ |
| `MANIFEST.sha256` lines | **85** (86 minus the manifest itself) | 85 ✅ |

The **total was right but the breakdown was wrong**, which is why the error
survived three phases: the totals matched, so nothing looked inconsistent.

The affected earlier documents are **not rewritten** (append-only). This
correction is the authoritative statement. All Phase 12 documents and the
submission package carry the corrected breakdown.

**Consequence:** the proposed Zenodo deposit contains **86 files**, not 89 as
an early draft of the deposit plan stated.
