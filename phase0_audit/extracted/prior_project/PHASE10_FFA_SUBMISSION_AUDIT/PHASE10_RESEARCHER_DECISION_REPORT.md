# Phase 10 — Researcher decision report (concise)

**Journal:** *Finite Fields and Their Applications* (Elsevier)
**Date:** 2026-11-10 · **Guidelines accessed:** 2026-11-10
**Type:** read-only assessment. No manuscript file was modified. Nothing was
submitted. No cover letter was written.

---

## 1. Starting conditions — verified

| check | result |
|---|---|
| Branch | `arena/59de606f-matrix-ring` |
| HEAD | `1fea3aa` (the Phase 9 commit) — confirmed |
| Working tree | clean, except one untracked leftover: `PHASE9A_JOURNAL_AUDIT/` (the partial Phase 9A file the researcher asked to skip) |
| Phase 8B package | `6d39f643…86fec0`, 700 055 B — **OK** |
| Phase 8A package | `14ecac0e…42910`, 1 096 851 B — **OK** |
| Phase 8 package | `d1ba4c82…9a80d`, 543 086 B — **OK** |
| `PAPER/main.tex` | sha256 `ee47ce7e91444ef3b05901e54a7e4c40e16df19aeb81817368d277ac4501737c` |
| `PAPER/references.bib` | sha256 `73388338bb83adb695db32d2f69b3d2c8d7279647c546cf4da4b9dc5abd22feb` (unchanged; D-1 intact) |
| `main.tex:165` | still `\bibliographystyle{plain}` |
| PDF | not recompiled |

## 2. Readiness verdict

**The scholarly package is complete. The submission package is not.**

FFA's *scientific* requirements are met or exceedable: the scope gate
("finite fields play a nontrivial role") is passed by the Galois/Frobenius
content; the reference-style question is a non-issue because FFA imposes **no**
reference format at submission and applies its own at proof stage — so **decision
D-1 (keep `plain`) is compatible with FFA and needs no change**.

What is missing is **six submission-time artefacts**, five of which need facts
only the researcher has.

## 3. The five blockers

| # | blocker | official basis | who supplies it |
|---|---|---|---|
| 1 | **Author metadata** — names, affiliations (full postal address + country), one corresponding author with a publishable email | Guide §Title page | **Researcher** |
| 2 | **Research data, Option C** — deposit in a repository + link, **or** a statement of why not (which gets published). *Mandatory.* | Guide §Research data | **Researcher** (deposit is straightforward: 85 files already exist) |
| 3 | **Competing interests** — via https://declarations.elsevier.com/, uploaded at "attach/upload files" | Guide §Declaration of competing interests | **Researcher** |
| 4 | **Funding** — grant details, or the exact no-funding sentence | Guide §Funding sources | **Researcher** |
| 5 | **Generative-AI declaration** — new section **before the reference list**. Required for this manuscript; currently absent. | Guide §Declaration of generative AI use | **Researcher** — and it is a manuscript edit, so it needs separate approval |

## 4. Strongest three contributions for a future cover letter

1. **The Galois duality over `M_2(F_q[u]/⟨u^t⟩)` and the refutation of
   principality** — `θ_s = σ_s ∘ (·)^T` is an anti-automorphism and is what
   makes the dual of a right module a right module; hulls are developed with no
   principality hypothesis; the conjecture that hulls are principal is **false**,
   with `MU_B ≥ 3` forcing `t ≥ 2` **and** `p | n`.
2. **The exact transported form and the two bounds** — `u^{[s]}(I_{4n} ⊗ H_t)v^T`,
   a Hankel-Gram `σ̂_s`-Hermitian form preserving duality and hulls including
   the non-principal ones; plus the coset-distance theorem and the coset
   Singleton bound `K + d ≤ N + 1`, proved not to follow from the EA Singleton
   bound.
3. **The certification** — 28 codes by three independent methods, 5 055 codes
   with a computed distance, 88 non-dominated tuples, all shipped with a fixed
   seed and a manifest. FFA's scope names computation explicitly.

**Do not claim improved or record parameters.** Verified from §9.2: every
stabilizer code is at best equal to best known (only at `d = 2`), and every
`d ≥ 3` code is **1–2 below** best known. The EA codes (largest `d = 10`) are
unbenchmarkable — no EA table exists.

## 5. Top two editorial risks

| risk | why | remedy (content-based, no rewriting) |
|---|---|---|
| **R-3 — parameters below best known** (highest) | FFA's coding papers skew parameter-forward; the 2026 competitors all claim improved parameters | Reframe on algebraic origin; state the gap openly as §9.3 already does; lead with contributions 1–3 |
| **R-7 — "noncommutative" is deflatable by Morita** (high) | The paper itself states `R_n ≅ M_2(B_q)` with `B_q` commutative | Answer it up front: the anti-automorphism sets up the duality; Morita makes the structure theory tractable; the residue is repeated-root cyclic codes over `F_q[u,X]/⟨u^t, X^n−1⟩`, governed by the factorisation of `X^n − 1` over `F_q` — which is FFA's home ground |

## 6. Small fix worth doing first

The abstract is **at or over FFA's verified 250-word limit** — measured at 230,
246 and 257 words under three counting conventions. Trim with margin. It is a
copy-edit, not a mathematical change, and it is the only guideline breach that
is visible on the first screen.

## 7. Decisions the researcher now owns

1. Resolve the five blockers in §3 — in particular, **choose the research-data
   route**: deposit (recommended) or published statement of why not.
2. **Choose gold OA (USD 3 240, excl. taxes) or subscription (no fee).** The
   choice is made after acceptance and has no effect on review, but it should be
   decided before submission so the funding statement is coherent.
3. **Authorise or decline the abstract trim** (§6) — a manuscript modification.
4. **Authorise or decline the generative-AI declaration section** — a
   manuscript modification, and the only missing item that must go *into* the
   manuscript rather than into the submission system.
5. **Decide on a preprint.** FFA permits it and it does not count as prior
   publication; it can help in a crowded 2026 niche.
6. **Decide whether to delete `PHASE9A_JOURNAL_AUDIT/`** (the partial file you
   asked to skip). It is untracked and harmless; say the word and it goes.
7. Note: the Phase 9 evidence register contains **four wrong venue
   attributions** (Fan–Zhang 2017 and Liu–Pan 2020 are *Designs, Codes and
   Cryptography*, not FFA; Cao 2021 is *IEEE TIT*, not *Discrete Mathematics*;
   Dinh 2024 is *Advances in Mathematics of Communications*, not *J. Algebra
   Appl.*). The manuscript's own `references.bib` and validation report are
   **correct**; only the Phase 9 prose is wrong. Offer to correct it stands.

## 8. What Phase 10 did not do

* Did not modify `main.tex` or any section file.
* Did not change the bibliography style; D-1 stands.
* Did not rewrite the abstract, adopt the Elsevier template, or reformat
  anything.
* Did not write a cover letter.
* Did not consider any alternative journal.
* Did not upload or submit anything.
* Did not claim acceptance, or that the paper is submission-ready.

**Awaiting explicit approval before any of these.**
