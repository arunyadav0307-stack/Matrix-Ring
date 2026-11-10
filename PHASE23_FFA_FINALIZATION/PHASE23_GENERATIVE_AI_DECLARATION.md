# Task C — Generative-AI declaration reconciliation

**STATUS: RESEARCHER CONFIRMATION REQUIRED — NOT FINALISED, NOT INSERTED.**

This document has **not** been inserted into the manuscript, and nothing in it
has been submitted anywhere. It is the adjudication record for a discrepancy
that must be resolved by the researcher, not by the agent.

---

## C1. The discrepancy, stated plainly

| source | account of AI involvement |
|---|---|
| **Researcher** | "AI tools were used **only for language enhancement**." |
| **Project record** (commits, logs, decision log, prior phase reports) | AI assistance spanned manuscript drafting, LaTeX development, proof exposition, computational script generation, verification-tool construction, abstract revision, literature discovery **and** language enhancement. |

These two accounts **cannot both be complete**. Under Elsevier's policy the
"language enhancement only" account sits close to the exemption for basic
grammar, spelling and reference checking — i.e. **little or no disclosure
required**. The broader account describes substantive generative-AI assistance —
i.e. **disclosure required**.

The consequence of getting this wrong is asymmetric:

* If the narrow account is used and the broad one is accurate, the submission
  carries an **inaccurate declaration**.
* If the broad account is used and the narrow one is accurate, the submission
  **over-discloses** — undesirable, but not a misrepresentation.

**Therefore the declaration stays PENDING until the researcher adjudicates.
This phase does not resolve it and does not paper over it.**

---

## C2. Activity matrix — the eight activity types, separated

Each row states what the record actually shows, whether it falls inside the
"language enhancement only" account, and whether it is disclosable under the
Elsevier policy quoted in C3.

| # | activity type | performed by | what the record shows | inside "language only"? | disclosable? |
|---|---|---|---|---|---|
| **1** | **Manuscript drafting** | **AI assistant (Arena AI agent)** | 7 commits authored `Arena Agent <agent@arena.ai>`; the 12 `sections/*.tex` files (10 sections + 2 appendices) were produced across the drafting phases. Total commit authorship: 41 commits `arunyadav0307-stack`, 7 `Arena Agent`, 2 `Arun Kumar Yadav`. | ❌ **NO** — drafting is not polishing | ✅ **YES** |
| **2** | **LaTeX generation / document build** | **AI assistant + TeX Live 2024** | The build toolchain itself — `PAPER/compile/bootstrap_texlive.sh`, `build_modern.sh`, `map_ts1_lm.py` — was *written by* the agent; TeX Live then executed it deterministically. | ❌ **NO** | ⚠️ **Borderline** — typesetting automation is arguably a technical tool; disclose if AI generated substantive content. Reported here, not decided. |
| **3** | **Mathematical proof exposition** | **Researcher, with AI assistance in exposition** | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`; decision-log entries D-006/D-010 record the central Galois pairing as *proposed* and later *upgraded to proved*. | ❌ **NO** | ✅ **YES — most consequential** |
| **4** | **Literature discovery** | **AI assistant (web search)** | The 13-entry bibliography was assembled with AI search; **four venue attributions were wrong** (Fan–Zhang, Liu–Pan, Cao, Dinh et al.) and were corrected in Phase 11. | ❌ **NO** | ✅ **YES** — the exemption covers *checking* references, not AI-driven discovery that introduced errors |
| **5** | **Computational script generation** | **AI assistant** | All 22 scripts under `research-data/scripts/` (published copies of the originals) were written by the agent. | ❌ **NO** | ✅ **YES** |
| **6** | **Verification tooling** | **AI assistant wrote the tools; the computer ran them** | `tools/validate_latex_v2.py`, `verify_examples.py`, `check_log.py`, `inspect_pdf.py` are agent-written. Their *execution* — 13/13 LaTeX checks, 56/56 example checks, 28 codes certified by three independent methods — is deterministic machine work. | ❌ **NO** (tooling); n/a (execution) | ⚠️ **Split** — the tooling is AI-authored; the verification it performs is not |
| **7** | **Abstract revision** | **AI assistant** | The abstract was revised during the drafting phases to fit the ≤250-word FFA limit; current version is 240 words after stripping LaTeX and math. | ❌ **NO** — revision of substantive content is not language polishing | ✅ **YES** |
| **8** | **Language enhancement** | **AI assistant** | Polishing of wording throughout the drafting phases. | ✅ **YES** | ❌ **Borderline/no** — pure grammar and spelling is exempt; substantive rewording of scientific content is not |

### Summary of the split

| classification | activity types |
|---|---|
| **Clearly outside the "language only" account** | 1 (drafting), 3 (proof exposition), 4 (literature discovery), 5 (script generation), 7 (abstract revision) |
| **Partly outside — AI-authored tooling, machine-executed** | 2 (LaTeX build), 6 (verification tooling) |
| **Inside the account** | 8 (language enhancement) |
| **Not AI work at all** | Script execution; PDF compilation; the researcher's blueprint, decisions and 43 human commits |

**Five of the eight activity types fall clearly outside the researcher's stated
account.** The record is not ambiguous on this point.

---

## C3. Elsevier policy — quoted, not paraphrased

Source: <https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals>
(accessed 2026-11-10).

> "Authors should disclose the use of AI tools for manuscript preparation in a
> separate AI declaration statement included in their manuscript upon
> submission. This statement will appear in the published article to ensure
> transparency. Authors should document their use of AI, including **the name of
> the AI tool used, the purpose of its use, and the extent of their oversight**."

> "**Please note:** Basic checks of grammar, spelling and punctuation do not
> need a declaration statement. However, **when an AI tool makes substantive
> changes to sentence structure or organization of a part of the text, this
> should be disclosed.**"

> "Where AI tools are used as part of the **research process** rather than
> manuscript preparation, this use should be **described in detail in the
> Methods section**."

> "Authors should not list AI tools as an author or co-author, nor cite AI tools
> as an author."

Recommended format:

> **Title of section:** Declaration of generative AI and AI-assisted
> technologies in the manuscript preparation process
>
> **Statement:** During the preparation of this work, the author(s) used
> [NAME OF TOOL / SERVICE] in order to [REASON]. After using this tool/service,
> the author(s) reviewed and edited the content as needed and take(s) full
> responsibility for the content of the published article.

**The exemption is narrow: "basic checks of grammar, spelling and punctuation"
plus reference *checking*.** It does not extend to drafting, proof exposition,
code generation, abstract revision, or literature *discovery*. Applying the
exemption to those five activities would be broader than the policy permits.

---

## C4. Tool identification — what is and is not verifiable

| item | verifiable? | evidence | confidence |
|---|---|---|---|
| **Arena AI agent** | ✅ **YES** | 7 commits authored `Arena Agent <agent@arena.ai>`; named throughout the phase deliverables | **High** |
| **ChatGPT** | ⚠️ **PARTIALLY** | The researcher's blueprint (§8B) mandates ChatGPT as independent auditor; `06_AUDIT/Phase0_audit_request.md` says "copy everything below the line into ChatGPT"; `PROJECT_DECISION_LOG.md` records D-006/D-010 as "Pending: researcher + ChatGPT audit"; a completion gate lists "Independent reviewer (ChatGPT)". **The role is documented; whether the audits were actually carried out is NOT verifiable from the repository.** | Role documented, execution unverified |
| **Model names** | ❌ **NO** | nowhere recorded | **None — will not be guessed** |
| **Model versions** | ❌ **NO** | nowhere recorded | **None — will not be guessed** |
| **Providers** | ❌ **NO** | nowhere recorded | **None — will not be guessed** |
| **Usage dates** | ❌ **NO** | only commit dates, which record when work was committed, not when a tool was used | **None — will not be guessed** |

**Nothing here claims a model name, version, provider, date, or statement of
product capabilities, and no AI tool is credited with authorship.** Elsevier
forbids listing or citing an AI tool as an author, and this phase does not do
so.

**Consequence for the declaration:** Elsevier asks for "the name of the AI tool
used". Only one tool — the Arena AI agent — can be named with confidence. If the
researcher used ChatGPT or any other tool, **the researcher must supply the
name**, since the record cannot.

---

## C5. What the manuscript currently says

The current declaration section in `PAPER/FFA_FINAL_SUBMISSION_V2/main.tex`
reads, in relevant part:

> "[*Researcher confirmation required — mandatory where applicable.*] Elsevier
> requires authors to declare the use of generative AI … AI assistance **was**
> used extensively in the preparation of this manuscript and therefore a
> declaration is required; the exemption for basic grammar, spelling and
> reference checking does not cover this use. The exact wording, the tools to be
> named and the scope of the disclosure … must be confirmed by the author before
> submission."

**This is a placeholder, not a declaration, and it cannot be submitted as it
stands.** It asserts that AI was used extensively — which contradicts the
researcher's "language enhancement only" account — while naming no tool. The
contradiction is deliberate and visible: it is exactly the discrepancy the
researcher must resolve.

---

## C6. Two candidate declarations — both PENDING

The researcher must choose one, or supply a third. **Neither has been inserted.**

### Option 1 — broad disclosure (consistent with the project record)

Section title (Elsevier's exact wording): **Declaration of generative AI and
AI-assisted technologies in the manuscript preparation process**

> During the preparation of this work the author used an AI assistant (Arena AI
> agent) in order to support the preparation of the LaTeX manuscript, the
> exposition of the proofs, the development of the computational scripts, the
> literature search, and the improvement of the language. All mathematical
> results are the author's own, and every numerical result was produced by
> deterministic scripts and independently certified by three methods. After
> using this tool/service, the author reviewed and edited the content as needed
> and takes full responsibility for the content of the published article.

**Requires the researcher to name any additional tool actually used**, since
only the Arena AI agent is verifiable from the record.

### Option 2 — narrow, if the researcher's account prevails

If the researcher confirms that AI involvement was genuinely limited to
language polishing — and that drafting, proof exposition, script generation,
abstract revision and literature discovery were **not** AI-performed — then
Elsevier's exemption applies and the policy says "If you have nothing to
disclose, you do not need to add a statement." In that case the section would
be **omitted entirely**, not filled with a language-only sentence.

**But this contradicts the commit record, and the researcher would have to say
so explicitly, in writing, before it is adopted.** The agent will not adopt it
unilaterally.

### The middle case — most likely, and still requiring confirmation

The researcher may mean that the *mathematical content* is entirely theirs and
that AI only helped express it. That reading is consistent with the four-way
split (researcher / AI / computer / independent check) — but it still does not
make drafting, script generation, abstract revision or literature discovery
disappear, because those are not language functions. **This is a genuine third
possibility and needs to be stated, not inferred.**

---

## C7. The question the researcher must answer

> Does the final declaration describe AI involvement as **(a)** language
> enhancement only — in which case, under Elsevier's policy, no statement is
> needed — or **(b)** the broader set of activities documented in the project
> record (drafting, proof exposition, script generation, abstract revision,
> literature discovery, language enhancement) — in which case a declaration
> naming **every tool you actually used** is required?

The agent cannot answer this. It is the author's attestation and the author's
responsibility.

---

## C8. What this phase did and did not do

| | |
|---|---|
| Produced the eight-way activity matrix | ✅ |
| Reconciled the discrepancy | ❌ **No — it remains unreconciled** |
| Finalised the declaration | ❌ **No** |
| Inserted any wording into the manuscript | ❌ **No** |
| Named a model, version, provider or date | ❌ **No — none is verifiable** |
| Credited an AI tool with authorship | ❌ **No — forbidden by policy** |
| Sent anything anywhere | ❌ **No** |
