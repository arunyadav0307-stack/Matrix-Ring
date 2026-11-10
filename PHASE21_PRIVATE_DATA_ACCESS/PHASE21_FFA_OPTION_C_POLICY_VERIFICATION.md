# Task A — FFA research-data Option C: policy verification

**Access date for every source below: 2026-11-10.** All sources are official
Elsevier / *Finite Fields and Their Applications* pages. No secondary source,
no blog, no institutional summary, and no prior phase's conclusion was relied
upon: the wording was re-read from the live pages on the access date.

---

## 1. Sources consulted

| # | source | URL |
|---|---|---|
| S1 | FFA Guide for Authors — "Research data" and "Research data deposit, citation and linking" | <https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/guide-for-authors> |
| S2 | Elsevier Research data guidelines (defines Options A–E) | <https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines> |
| S3 | Elsevier Research data policy (principles) | <https://www.elsevier.com/about/policies-and-standards/research-data> |
| S4 | Elsevier Research data FAQs | <https://www.elsevier.com/about/policies-and-standards/research-data/faq> |
| S5 | Elsevier Data statement page | <https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement> |
| S6 | Elsevier Sharing research data page | <https://www.elsevier.com/researcher/author/tools-and-resources/research-data> |

---

## 2. Exact policy wording

### 2.1 The journal-level requirement (S1) — verbatim

> **Research data**
>
> "Research data are the results of observations or experiments that validate
> research findings. They may include software, code, models, algorithms,
> protocols, methods, and other relevant materials."

> **Research data deposit, citation and linking**
>
> "For this journal, **Option C** instructions from our research data guidelines
> apply. This means that you are **required** to:
> * Deposit your research data in a relevant data repository.
> * Provide a link to the dataset during the submission process.
> * If sharing your research data isn't possible, make a statement explaining
>   why during the submission process. The statement will appear in your
>   published article."

### 2.2 What Option C means at Elsevier level (S2) — verbatim

> "### Option C: Research data deposit, citation and linking (or a Research
> Data Availability Statement)
>
> You are **required** to:
> * Deposit your research data in a relevant data repository
> * Provide a link to the dataset during the submission process
> * If sharing your research data isn't possible, please make a statement
>   explaining why during the submission process. The statement will appear in
>   your published article"

(The surrounding options confirm the tiering: Option A and Option B say
"**encouraged**"; Option C, D and E say "**required**". FFA sits on Option C.)

### 2.3 The general policy (S3) — verbatim principles in tension

> "Research data should be made available free of charge to all researchers
> **wherever possible** and with minimal reuse restrictions"

> "Researchers should remain in control of how and when their research data is
> accessed and used, and should be recognized and valued for the investments
> they make in creating their research data and making it available"

These two principles pull in opposite directions and are quoted in full because
both are relevant to an "on request" arrangement.

### 2.4 The FAQ that might be mistaken for a loophole (S4) — verbatim

> "**Is it compulsory to share my research data?**
> No. Our policy is clear in that we encourage and support authors to share
> their research data rather than mandating them to do so, and provide tools
> and services to enable them to do this effectively. **Where there is
> community support for (often discipline-specific) mandates regarding data
> deposit, submission and sharing, some of our journals may reflect this with
> their own mandatory data sharing policies. Please check your journal's guide
> for authors for specific information.**"

**This does not help this manuscript.** FFA is exactly one of the journals that
has adopted its own mandatory policy — Option C, per S1 and S2. The general
"not compulsory" answer is overridden at journal level.

### 2.5 The data-statement mechanism (S5) — verbatim

> "With a data statement, an author can provide information about the data
> presented in an article and **provide a reason if data is not available to
> access**."

and (S6):

> "We understand that there are times when the data is simply not available to
> post or there are good reasons why it shouldn't be shared. A number of
> Elsevier journals encourage authors to submit a data statement alongside
> their manuscript. This statement allows you to clearly explain the data
> you've used in the article and **the reasons why it might not be available**."

---

## 3. The six questions, answered against the official text

### Q1. Does FFA explicitly require repository deposit and linking?

**Yes.** S1 and S2 both use the word "**required**", not "encouraged". Two
obligations are stated positively: deposit in a relevant data repository, and
provide a link during the submission process.

### Q2. Is a Data Availability Statement an alternative **only** when public sharing is not possible?

**Yes — that is the literal condition.** The third bullet is conditioned on
"**If sharing your research data isn't possible**". S5 and S6 reinforce this:
the statement exists to "provide a reason if data is not available to access".
The statement is therefore a **fallback for impossibility**, not a free choice
between deposit and non-deposit.

### Q3. Is private access upon reasonable request accepted?

**Not addressed anywhere in the official text.** The phrases "on request",
"upon reasonable request", "available from the author", "private access" and
any equivalent appear in **none** of S1–S6. The Option C text offers exactly
two branches:

1. deposit + link; or
2. statement explaining why sharing **isn't possible**.

An "available from the author on request" statement fits neither branch
cleanly. It is not branch 1 (no repository, no link). It is not branch 2
either, because the author is *not* saying sharing isn't possible — the author
is saying the materials exist, are intact and will be handed over.

> **AMBIGUITY — explicitly identified.** The official policy is silent on
> author-request arrangements. Silence is not permission and it is not
> prohibition. This phase does **not** resolve it by inference; it is referred
> to the editorial office (Task E).

### Q4. Must the author explain why public sharing is not possible?

**Yes, if the second branch is used.** Both S1 and S2 say the statement must
"explai[n] why". S5 and S6 repeat that the statement explains "the reasons why
it might not be available".

**Consequence for this manuscript — stated plainly.** The researcher has
decided not to publish the data, but has supplied **no reason** for that
decision. A reason therefore **cannot be written truthfully** without the
researcher providing one. This phase does **not** invent one. In particular it
does **not** assert confidentiality, proprietary status, commercial
sensitivity, legal restriction, institutional restriction, privacy, security or
ethical constraint — none of these has been stated by the researcher and none
is supported by the material.

**A second, related problem.** Even the precondition for branch 2 is doubtful
here: the materials plainly *can* be shared. They are 86 files of ~2.4 MB, all
original work, pure Python standard library, no third-party package, and no
licence encumbrance of the author's own making (see the inventory). Only one
file carries external third-party content, and that content is itself a
publicly published table. The materials are fully depositable.

### Q5. Does private access for editors or reviewers differ from public access for readers?

**The policy makes no such distinction.** S1–S6 address only (a) deposit plus
link, which is public by nature, and (b) a statement which "**will appear in
your published article**" — i.e. it is also public. Nothing in the official
text establishes a reviewer-only or editor-only private channel as a means of
satisfying Option C.

Two related facts, and one thing that is **not** verified:

* FFA's supplementary-material route is **not** private. S1 states: "all
  supplementary material provided will appear online exactly as received".
  Supplying the package as supplementary material would therefore publish it.
* Peer review is a separate process from the research-data policy, and the
  policy text does not speak to it.
* **NOT VERIFIED:** whether the submission system offers a reviewer-only file
  channel. This was **not** checked against any official source and must not be
  relied upon. It is one of the questions put to the editorial office.

### Q6. Can an author-request arrangement satisfy the journal's mandatory policy?

**Not established by the official text.** On the strict reading of S1/S2 it
does **not**: Option C requires a repository deposit and a link, and the only
express alternative is unavailable here for the reason given in Q4 (the
materials are depositable, and no reason for non-deposition has been given).
On a lenient reading the policy's silence leaves room for the editor to accept
it.

> **Conclusion: this cannot be settled from the policy documents. It requires
> editorial confirmation.**

---

## 4. Implications for this manuscript

| # | implication |
|---|---|
| I-1 | The materials at issue **are** research data under the FFA definition: "software, code, models, algorithms, protocols, methods, and other relevant materials". The 22 scripts, 23 logs, 29 generator matrices and 8 parameter tables fall squarely inside that definition. An argument that this is "not research data" is not available. |
| I-2 | The researcher's chosen arrangement — no public deposit, no DOI, no Zenodo, no release, no tag, private provision on reasonable request — is **not** one of the two branches Option C offers. |
| I-3 | A truthful "why" does not currently exist. Any statement that supplied one would have to invent a restriction. It must not. |
| I-4 | The statement, once given, **is published with the article**. It is not a private accommodation; it is public text. |
| I-5 | Strict reading → **SUBMISSION BLOCKER**. Lenient reading → **EDITORIAL CONFIRMATION REQUIRED**. Both are recorded; neither is resolved here. |
| I-6 | The canonical manuscript currently carries a **superseded** data-availability statement containing a public GitHub link (rendered on p. 37 of the FFA PDF). The researcher has withdrawn authorisation for that link. That section must be replaced before submission **whatever** route is finally chosen. See `PHASE21_MANUSCRIPT_STAGING_NOTE.md`. |

---

## 5. Change compared with earlier phases

The Option C wording re-read on 2026-11-10 is **identical** to the wording
recorded in Phase 10, Phase 11, Phase 12 and Phase 13. **The policy is
unchanged.** What has changed is the researcher's decision: Phases 12–13
planned a *public* GitHub route (commit-pinned URL); Phase 21 replaces that
with *private access on request*. The GitHub route is now withdrawn and is no
longer available as the compliance answer.

No Phase 20 data-access report exists in this repository (verified by search);
the most recent dedicated reports are Phase 13
(`PHASE13_GITHUB_RESEARCH_DATA_ACCESS_PLAN.md`) and the Phase 19 checklist
item, both of which were read.
