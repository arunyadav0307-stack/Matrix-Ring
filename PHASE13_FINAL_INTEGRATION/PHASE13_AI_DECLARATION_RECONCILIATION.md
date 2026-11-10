# Phase 13 / Task C — Generative-AI declaration reconciliation

**STATUS: UNRESOLVED. The AI declaration remains PENDING in the manuscript.**

This document exists because two accounts of AI involvement disagree, and the
disagreement is material. It is not resolved by choosing whichever account is
more convenient.

Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring` · Base commit: `e41c571`

---

## C0. Summary of the discrepancy

| source | account of AI involvement |
|---|---|
| **Researcher (Phase 13 instruction)** | "AI tools were used **only for language enhancement**." |
| **Phase 12 project report** | AI assistance spanned manuscript drafting, LaTeX development, mathematical proof exposition, computational script development, verification tooling, abstract revision, **and** language enhancement. |

These are **not consistent**. Under Elsevier's policy, "language enhancement"
sits close to the exemption for basic grammar, spelling and reference
checking — which would mean **little or no disclosure is required**. The
broader account describes substantive generative-AI assistance, which
**requires** disclosure.

If the narrower account were used and the broader one is accurate, the
submission would carry an inaccurate declaration. If the broader account were
used and the narrower one is accurate, the submission would over-disclose —
undesirable but not a misrepresentation.

**Therefore the declaration cannot be finalised until the researcher
adjudicates. Until then it stays PENDING.**

---

## C1. Reconstructed workflow — activity matrix

Evidence base: 37 commits, `PROJECT_DECISION_LOG.md`, `CHANGELOG.md`,
`06_AUDIT/Phase0_audit_request.md`, `02_PHASE_REPORTS/`, `03_THEOREMS/`,
Phase 9–12 deliverables.

| # | activity | who/what performed it | evidence | within the "language only" account? | researcher confirmation required |
|---|---|---|---|---|---|
| 1 | **Language and grammar improvement** | AI tool | throughout the drafting phases | **YES** | no — consistent with both accounts |
| 2 | **Manuscript drafting** (LaTeX prose, §1–§10, appendices) | **Arena AI agent** | 7 commits authored `Arena Agent <agent@arena.ai>`; 12 `sections/*.tex` files produced across Phases 8–8B | **NO** | **YES** |
| 3 | **LaTeX formatting and document generation** | AI tool + TeX Live | `PAPER/compile/bootstrap_texlive.sh`, `build_modern.sh`, `map_ts1_lm.py` all written by the agent; Phase 8/8A/8B build reports | **NO** | **YES** |
| 4 | **Mathematical brainstorming and proof exposition** | Researcher **and** AI tool | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`; decision-log entries D-006/D-010 record the pairing as *proposed by* the agent and later *upgraded to proved* | **NO** | **YES — most consequential** |
| 5 | **Computational script generation** (22 scripts) | **AI tool** | `PAPER/supplementary/scripts/`; written during Phases 0–7 by the agent | **NO** | **YES** |
| 6 | **Execution of the scripts** (deterministic) | **Computer environment** | `PAPER/supplementary/logs/` (23 logs) | n/a — not AI work | no |
| 7 | **Independent verification of results** | **Script-based, deterministic** + AI-built audit tooling | `tools/validate_latex.py`, `check_log.py`, `inspect_pdf.py`, `verify_examples.py`; triple certification of 28 codes by three independent methods | n/a — machine execution, though the *tooling* was AI-written | no (but see #3) |
| 8 | **Literature discovery and reference checking** | **AI tool** (web search) | 13-entry bibliography; **four venue attributions were wrong** and were corrected in Phase 11 (Fan–Zhang, Liu–Pan, Cao, Dinh et al.) | **NO** — goes beyond the reference-checking exemption, which the agent exercised substantively | **YES** |
| 9 | **Prompt preparation and project coordination** | **Researcher** | 30 of 37 commits authored by `arunyadav0307-stack`; blueprint supplied by the researcher; every phase gated on researcher approval | n/a — human work | no |

### The four-way distinction the task requires

| performed by | what |
|---|---|
| **The researcher** | Supplied the research blueprint and the mathematical programme; authored 30 of 37 commits; approved every phase at its gate; made all substantive decisions (D-001…D-015+); supplied author metadata and declarations |
| **An AI tool** | Drafted LaTeX, wrote the 22 scripts, wrote the build/audit tooling, performed literature discovery, revised the abstract, improved language |
| **The computer environment** | Executed the 22 scripts deterministically, producing 23 logs and the 28 certified code parameters; ran TeX Live to build the PDF |
| **Independently checked** | Every numerical result is reproducible from the scripts; the 28 codes were certified by **three independent methods**; the LaTeX build was validated by three separate tools |

**Important:** the mathematical *results* are the researcher's. Nothing here
claims an AI tool independently proved or verified mathematics. What AI did
was assist with exposition, structure, code and checking.

---

## C2. Tool identification — what can and cannot be verified

| tool | verifiable? | evidence | confidence |
|---|---|---|---|
| **Arena AI agent** | **YES** | 7 commits authored `Arena Agent <agent@arena.ai>`; named throughout Phases 9–12 deliverables | **High** |
| **ChatGPT** | **PARTIALLY** | The researcher's own blueprint (§8B) mandates ChatGPT as the independent auditor. `06_AUDIT/Phase0_audit_request.md` states: *"Researcher (Arun): copy everything below the line into ChatGPT, together…"* `PROJECT_DECISION_LOG.md` records D-006 and D-010 as *"Pending: researcher + ChatGPT audit"*. `PHASE1_COMPLETION_AND_APPROVAL_GATE.md` line 180 lists *"Independent reviewer (ChatGPT)"* | **The role is documented; whether the audits were actually carried out is NOT verifiable from the repository** |
| Model names / versions | **NO** | nowhere recorded | **None — will not be guessed** |
| Providers | **NO** | nowhere recorded | **None — will not be guessed** |
| Exact usage dates | **NO** | only commit dates, which record when work was committed, not when a tool was used | **None — will not be guessed** |

**What is NOT claimed:** no model version, no provider, no usage date, no
statement of product capabilities, and no AI authorship credit. Elsevier
explicitly forbids listing or citing an AI tool as an author.

---

## C3. Official Elsevier policy — verified 2026-11-10

From the FFA guide for authors:

> "Authors must declare the use of generative AI tools in the manuscript
> preparation process upon submission of the paper."
>
> "Authors preparing a manuscript for this journal may use AI tools to support
> them. However, these tools must never be used as a substitute for human
> critical thinking, expertise, and evaluation. AI tools may only be applied
> with human oversight and control."
>
> "…authors are responsible and accountable for the contents of their work.
> This includes accountability for: Carefully reviewing and verifying the
> accuracy, comprehensiveness, and impartiality of all AI generated output…
> Editing and adapting all material thoroughly to ensure the manuscript
> represents the author's authentic and original contribution…"

**The declaration requirement and its exemption:**

> "The use of AI tools in the manuscript preparation process must be declared
> by adding a statement at the end of the manuscript when the paper is first
> submitted. The statement will appear in the published work and should be
> placed in a **new section before the reference list**."
>
> "The declaration **does not apply** to the use of basic tools, such as tools
> used to check grammar, spelling, and references."
>
> "If you have nothing to disclose, you do not need to add a statement."

### Applying the policy to each activity

| activity | requires disclosure? | reasoning |
|---|---|---|
| 1 Language/grammar improvement | **Borderline** | Purely mechanical grammar and spelling is exempt. Substantive rewording of scientific content is not. |
| 2 Manuscript drafting | **YES** | Drafting is the archetypal disclosable use; it is not grammar checking. |
| 3 LaTeX formatting / document generation | **NO** (probably) | Typesetting automation is a technical tool, not generative-AI authorship. Disclose only if AI generated substantive content. |
| 4 Mathematical proof exposition | **YES** | Substantive scientific content. |
| 5 Computational script generation | **YES** | Code generation by AI is disclosable assistance in preparing the work. |
| 6 Script execution | **NO** | Performed by the computer, not an AI tool. |
| 7 Independent verification | **NO** for the verification itself; **YES** for the AI-written tooling, if disclosed at all | Machine-executed; the exemption is not relevant. |
| 8 Literature discovery | **YES**, beyond the narrow exemption | The exemption covers *checking* references, not AI-driven discovery that produced **four wrong venue attributions** requiring later correction. |
| 9 Prompt preparation / coordination | **NO** | Human work. |

**Conclusion: the policy, applied honestly to the documented record, requires
disclosure.** The "language enhancement only" account, if adopted, would place
activities 2, 4, 5 and 8 outside the declaration — and the project records
show all four occurred.

**The exemption is not being applied narrowly here; it is being applied as the
policy states.** Applying it to cover drafting, proof exposition, code
generation and literature discovery would be broader than the policy permits.

---

## C4. The discrepancies, stated precisely

| # | discrepancy | detail |
|---|---|---|
| **D1** | **Drafting vs. language only** | 12 section files and the whole LaTeX scaffold were drafted by an AI agent. "Language enhancement" does not describe drafting. |
| **D2** | **Code generation vs. language only** | 22 computational scripts were written by an AI agent. Not a language function. |
| **D3** | **Literature discovery vs. language only** | AI web search produced the bibliography and four wrong attributions. Not a language function. |
| **D4** | **Proof exposition vs. language only** | Decision-log entries D-006/D-010 show the central Galois pairing being proposed and then proved with AI involvement in the exposition. Not a language function. |
| **D5** | **What "language enhancement" may mean** | The researcher may mean that the *mathematical content* was theirs and AI only polished wording — which would be consistent with the four-way distinction in C1 but would still not make activities 2, 5 and 8 disappear. **This is the most likely reading and needs confirmation.** |

---

## C5. Proposed declaration — PENDING, NOT INSERTED

Prepared so the researcher has something concrete to accept, amend or reject.
**It has deliberately not been inserted into the manuscript.**

Section title (exact Elsevier wording):

> **Declaration of generative AI and AI-assisted technologies in the manuscript
> preparation process**

Proposed statement (single author):

> During the preparation of this work the author used [NAME OF TOOL(S)] to
> [REASON]. After using this tool/service, the author reviewed and edited the
> content as needed and takes full responsibility for the content of the
> published article.

Suggested completion, reflecting the documented record:

> During the preparation of this work the author used an AI assistant (Arena
> AI agent) to assist with drafting and revising the LaTeX manuscript,
> developing proof exposition, writing the computational scripts, performing
> literature discovery, and improving the language. All mathematical results
> are the author's own; every numerical result was produced by deterministic
> scripts and independently certified. After using this tool, the author
> reviewed and edited the content as needed and takes full responsibility for
> the content of the published article.

**This wording is a proposal only.** It must not be submitted until the
researcher confirms it is accurate.

### A narrower alternative, if the researcher's account prevails

If the researcher confirms that AI involvement was genuinely limited to
language polishing — and that drafting, scripting and literature discovery
were **not** AI-performed — then the exemption arguably applies and Elsevier
says "If you have nothing to disclose, you do not need to add a statement."
In that case the section would be **omitted**, not filled with a
language-only sentence.

**But this contradicts the commit record, and the researcher must say so
explicitly before it is adopted.**

---

## C6. Specific facts requiring the researcher's confirmation

1. **Was the LaTeX manuscript drafted by you or by an AI tool?** The commit
   record shows an AI agent authoring 7 commits and producing the section
   files.
2. **Were the 22 computational scripts written by you or by an AI tool?**
3. **Was the bibliography assembled by you or by AI web search?** (Four
   attributions were wrong and needed correction.)
4. **Was the mathematical proof exposition produced by you, or drafted with AI
   assistance?** The mathematical *results* are yours either way; the question
   is about the writing.
5. **Which tool(s) should be named?** Arena AI agent is verifiable. ChatGPT is
   documented as the blueprint's independent auditor, but **whether those
   audits were actually performed is not verifiable from the repository** —
   please confirm.
6. **Is the proposed statement in C5 accurate?** If not, please give the
   corrected wording.
7. **Do you want the declaration included at all?** If your position is that
   AI involvement was exempt, say so explicitly and the section will be
   removed rather than filled with a misleading sentence.

---

## C7. What has been done in the manuscript

**The AI declaration section remains in the manuscript marked
`[Researcher confirmation required --- mandatory where applicable.]`.**

It has **not** been filled with the "language enhancement only" account,
because doing so would insert a statement the project record contradicts.
It has **not** been filled with the broader account either, because the
researcher has not confirmed it.

Both would be inserting an unconfirmed statement as final, which the task
forbids.

## C8. Status

**PENDING — researcher adjudication required.** No AI declaration will be
inserted into the submission-ready manuscript until item C6 is resolved.
