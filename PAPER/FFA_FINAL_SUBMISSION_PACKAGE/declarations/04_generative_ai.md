# Declaration of generative AI and AI-assisted technologies

**STATUS: PENDING — UNRESOLVED DISCREPANCY. See
`PHASE13_AI_DECLARATION_RECONCILIATION.md`.**

**Update 2026-11-10 (Phase 13):** the researcher states that AI tools were used
**only for language enhancement**. The project records document substantially
broader AI assistance: manuscript drafting, LaTeX development, proof
exposition, the 22 computational scripts, verification tooling, literature
discovery (which produced four wrong venue attributions later corrected), and
abstract revision.

These two accounts are **not consistent**. The declaration has therefore
**not** been finalised in either direction:

* it has **not** been filled with a language-only statement, because the
  project record contradicts it;
* it has **not** been filled with the broader statement, because the
  researcher has not confirmed it.

Inserting either as final would be inserting an unconfirmed statement.

---

## Historical record (Phase 12 status — superseded)

A declaration is **required**. The Elsevier exemption for "basic tools, such as
tools used to check grammar, spelling, and references" does **not** cover the
assistance this manuscript received.

## Official Elsevier requirement (verified 2026-11-10)

Section title (exact):

> **Declaration of generative AI and AI-assisted technologies in the
> manuscript preparation process**

Statement template (exact):

> "During the preparation of this work the author(s) used [NAME OF
> TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s)
> reviewed and edited the content as needed and take(s) full responsibility
> for the content of the published article."

Placement: "a statement at the end of the manuscript when the paper is first
submitted… placed in a **new section before the reference list**."

## Factual record of AI assistance

| # | area | AI involvement |
|---|---|---|
| 1 | Literature discovery | Venue attributions and prior-art identification performed by AI web search. **Four attributions were wrong** and were corrected in Phase 11 (Fan–Zhang, Liu–Pan, Cao, Dinh et al.). |
| 2 | Manuscript drafting and editing | Large portions of the LaTeX source drafted and revised by an AI agent. |
| 3 | Mathematical exploration and proof exposition | Proof structure and exposition developed with AI assistance. |
| 4 | Code development | All 22 supplementary scripts written with AI assistance. |
| 5 | Computational verification assistance | Verification and audit tooling built and run by an AI agent. |
| 6 | Abstract revision and language refinement | The Phase 11 abstract revision (246/230/260 → 213/199/226 words) was drafted by an AI agent. |
| 7 | Arena AI and ChatGPT usage | **Arena AI agent: yes, extensively.** ChatGPT: **not known to the agent** — for the researcher to state. |
| 8 | Human evaluation and responsibility | The researcher directed the work and approved each phase. Final responsibility for the content is human. |

## What the agent will NOT assert

* **No tool name, model name, version or provider.** The researcher chose to
  leave this pending; the agent will not guess.
* **No usage dates.**
* **No claim that AI independently proved or verified mathematics.** The
  mathematical results are the researcher's. AI assisted with exposition,
  structure, code and checking. Every computed parameter comes from
  deterministic scripts reproducible from `supplementary/`.
* **No claim that AI tools were not used.** They demonstrably were.

## Proposed wording — PENDING APPROVAL

With one author confirmed, the template should be singular:

> During the preparation of this work the author used [NAME OF TOOL/SERVICE] to
> [REASON]. After using this tool/service, the author reviewed and edited the
> content as needed and takes full responsibility for the content of the
> published article.

## What is needed from the researcher

1. The **tool name(s)** to disclose.
2. The **reason** — the agent suggests "assist with drafting and revising the
   manuscript, developing proof exposition, writing the computational scripts,
   and performing verification and audit tasks".
3. Confirmation of the final sentence.

## Additional policy point

Elsevier's policy permits generative AI to create explanatory images and data
visualisations, but **not** to alter or fabricate primary data. The manuscript
contains **0 figures**, so the per-caption disclosure requirement does not
arise. No generative AI was used to alter or fabricate primary data.
