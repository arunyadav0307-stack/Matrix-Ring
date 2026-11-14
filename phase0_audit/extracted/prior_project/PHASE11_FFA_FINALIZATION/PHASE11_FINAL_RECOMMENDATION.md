# Phase 11 — Final recommendation

Manuscript: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings*
Target: **Finite Fields and Their Applications**
Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring`

## Verdict

> ## CONDITIONALLY READY — AUTHOR CONFIRMATIONS PENDING

**Not** "ready for submission", and **not** "not ready". The distinction is
precise and it is the whole point of this phase:

* Everything within the agent's authority **is done**.
* Everything that remains is either a **fact only the authors hold** (names,
  affiliations, funding, competing interests, AI-declaration wording) or an
  **action with external consequences** requiring authorization (the
  research-data deposit, which is public, permanent, and mints a DOI).

No amount of further agent work can close those items. Inventing them would be
worse than leaving them open.

## What Phase 11 accomplished

| Task | outcome | status |
|---|---|---|
| **A** — Reverify all 13 FFA guideline points against official sources | Re-read from the official FFA guide on 2026-11-10. **No policy drift** since Phase 10. Six items remain genuinely UNVERIFIED because the guide does not state them (article types, page limit, time to first decision, named handling editor) — recorded as such, not inferred | **VERIFIED / UNVERIFIED (honest)** |
| **B** — Revise the abstract to ~210–220 words | Original failed at **260** on the strictest counting convention. Revised to **213 / 199 / 226**, compliant on all three, with every mathematical claim preserved and verified against the manuscript register | **CORRECTED** |
| **C** — Five submission declarations | All five structured with visible placeholders. **Nothing invented**: no name, affiliation, funder, or interest was inferred | **RESEARCHER CONFIRMATION REQUIRED** |
| **D** — Positioning | Honest parameter framing (no records, no inflated novelty); a prepared response to the Morita objection; a five-level contribution hierarchy | **CORRECTED** |
| **E** — Phase 9 bibliographic corrections | Four wrong venue attributions found and corrected **append-only**. `references.bib` was correct throughout — the errors were only in the Phase 9 documents | **CORRECTED** |
| **F** — Preserve `PHASE9A_JOURNAL_AUDIT/` | **Not deleted.** Retained with a README marking it superseded, listing its known error, and pointing to the authoritative documents | **VERIFIED** |
| **G** — Modern TeX Live compile | **Genuine** TeX Live 2024: pdfTeX 1.40.26, BibTeX 0.99d, four-pass cycle. **0 errors, 0 warnings, 42 pages**, PDF produced and independently validated by three tools | **VERIFIED** |
| **H** — Staging copy + compliance matrix | `PAPER/FFA_SUBMISSION_STAGING/` created and compiling; 42-row matrix with six status values | **VERIFIED** |

## The three findings that matter most

### 1. The abstract genuinely failed the limit — and the failure was invisible under two of three counting conventions

Measured 246 / 230, the abstract looks compliant. Measured under the strictest
convention, which splits sub/superscripts, it is **260** — ten over. This is
exactly the kind of defect that passes a casual check and is caught by a
submission portal. It is now fixed with a 24-word margin on the strictest
count.

### 2. The manuscript cites **zero** FFA papers, not two

Phase 9 claimed the manuscript's citation lineage already ran through FFA. That
claim was **false** and rested on four wrong attributions (Fan–Zhang and
Liu–Pan are *Designs, Codes and Cryptography*; Cao is *IEEE Trans. Inform.
Theory*; Dinh et al. is *Advances in Mathematics of Communications*).

Critically, **`references.bib` was correct all along** — the errors lived only
in the selection documents. But the false claim was a *supporting argument for
the FFA recommendation*, and it would have been repeated to an editor in a
cover letter. It is now withdrawn, append-only, with the original text
preserved.

**The FFA recommendation itself stands**, because three of its five arguments
are unaffected and were verified directly against official FFA pages: the
scope text names algebraic coding theory; FFA is publishing in this area in
2026 (Vols 109–112 verified); and FFA advertises "very strict refereeing
standards", which suits a paper whose strongest asset is a structural negative
result.

### 3. AI assistance must be declared, and the declaration cannot be written by the agent

AI assistance in preparing this manuscript was **extensive** — drafting, proof
exposition, computational scripts, verification, auditing, and the abstract
revision itself. Elsevier's exemption covers only grammar, spelling and
reference checking; it plainly does not cover this. A declaration is
**mandatory**.

The agent has deliberately **not** guessed tool names, model names, version
numbers or dates. Those are facts the authors must supply. Submitting a
vague or inaccurate declaration is a research-integrity matter, and
submitting none would be a misrepresentation.

## Honest assessment of risk

| risk | level | mitigation |
|---|---|---|
| Scope: noncommutative non-chain ring in a *finite fields* journal | **moderate — the highest desk-stage risk** | Mitigated, not eliminated. The Morita response shows the engine is `F_q[u,X]/⟨u^t, X^n−1⟩` structure and `p \| n` is the repeated-root case; FFA Vol 110 carries chain-ring codes. A screener could still mis-read the title |
| Refereeing standard | high | FFA accepts "only those papers which receive excellent referee reports". The mathematics must be airtight |
| Quantum parameters are not records | moderate | Handled by honest framing. Leading with `d = 10` would be refuted by one lookup |
| Morita objection | moderate | A real objection; prepared response in the staging copy |
| Data deposit incomplete | **blocking** | Requires authorization |

## What must happen next

1. Answer the **8 blocking items** in
   `PHASE11_RESEARCHER_ACTION_ITEMS.md` Group A.
2. Read and approve the three new introduction subsections — they make claims
   about emphasis and intent.
3. Authorize the research-data deposit, or decline and accept that the Option C
   fallback statement (a published explanation of why deposition is
   impossible) does not apply here, since the data are plainly depositable.
4. Approve promotion of the staging copy to the canonical manuscript. **Until
   then, the canonical manuscript is unchanged.**

## Stopping point

Phase 11 is complete. In line with the standing instruction, the agent has
**not**:

* submitted the manuscript, or created any journal account;
* written a cover letter;
* prepared a second-journal fallback;
* created a Zenodo deposit, GitHub release, DOI or licence;
* modified `PAPER/main.tex`, `PAPER/references.bib`, any `sections/*.tex`
  file, or any protected archive.

All protected artifacts are byte-identical to their pre-Phase-11 state; hashes
are recorded in `PHASE11_FINAL_COMPLIANCE_MATRIX.md` §7.

**Awaiting your approval before any of the above.**
