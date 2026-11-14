# PHASE 0 — DECISION REPORT

**Project:** Quantum Error-Correcting Codes from (k)-Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings
**Date:** 2026-11-12 · **Branch:** `arena/7d88376d-matrix-ring` · All deliverables under `phase0_audit/` · Original repository untouched (git-verified).

---

## 1. Repository and source-material status

Complete prior campaign recovered: 23 phases of artefacts, 15 theorem documents, a 37-entry verified bibliography, an ≈187 KB updated theorem register, a full LaTeX manuscript with four successive **FFA submission packages**, three researcher-review versions, and a published, integrity-verified data package (`research-data/`, 86 files, **87/87 manifest OK** on re-check). The data package's own feasibility suite **reproduced byte-identically** under my re-execution (3 cosmetic diff lines; evidence in `phase0_audit/evidence/`). Submission state: prepared for *Finite Fields and Their Applications*; last recorded item = Option-C data-compliance ("conditionally acceptable — editorial confirmation pending", 2026-11-10). **No in-repo evidence of actual submission or an editorial decision — author confirmation required.**

## 2. Literature findings

Seven source PDFs physically identified; three records externally verified on 2026-11-12 (QIP 25:207 "Quantum codes construction from cyclic codes over matrix rings" — Joshi, Patel, Prakash; Liu–Pan 2020 DCC 88:241–255; Kushwaha–Prakash arXiv:2512.12335/2601.06609). Everything else inherits the prior campaign's `DIRECT`-tagged bibliography. The two decisive facts: **(a)** the external world now contains quantum codes from matrix-ring cyclic codes (A8, Euclidean/Hermitian, M₃); **(b)** the exact (k)-Galois-hull-over-matrix-ring intersection exists **in this repository** as a submission-prepared manuscript. Full table: `PHASE0_LITERATURE_REVIEW.md` §3.

## 3. Mathematical feasibility

**Established — demonstrated, not conjectured.** The ring/module layer (RQ1), the non-degenerate (k)-Galois pairing with the transpose-twist θ_k (RQ2), dual/hull theory (RQ3), proved Gray compatibility for the constructed map (RQ4), and CSS/EA quantum output with certification (RQ5) all exist with proofs and 550+ passing computational checks that re-ran cleanly. Binding constraints: m ≥ 2 for nontrivial Galois action; gcd(n,p) = 1 for the clean (squarefree/CRT) structure theory; the **reflexivity fork m | 2k**; right-ideal convention; λ-weighted scalar form (P2) as the Gray-coherent face of the R-valued form (P1).

## 4. Valid and invalid candidate approaches

**Valid (proved):** P1 pairing B_k(x,y) = Σ θ_k(xᵢ)yᵢ + P2 scalar companion b_k = λ∘Tr∘B_k; right-ideal cyclic codes via Morita; central factorization with squarefree hypothesis; φ_n Gray with transported pairing; SO/DC/EA quantum routes with 2-of-3-method certification.
**Invalid (documented):** plain dot products (fail the size law on one-sided modules — 31/35 counterexamples); automorphism-only twists without the transpose; two-sided-ideal restriction (no novelty); m = 1 "Galois"; reflexivity assumed without m | 2k; "first quantum from matrix rings" and "first hulls over noncommutative rings" positioning claims.

## 5. Unresolved mathematical obstacles (carried forward from the prior register, confirmed by this audit)

O-1 General principality/generator theorem at t ≥ 2 or p | n (T-021 conditional only) · O-2 general hull-dimension formulas (distributions computed, formula open) · O-3 15 census families beyond brute force · O-4 external benchmarking gaps (q = 8 untabulated; no EA table exists) · O-5 r ≥ 3 hull numerics nonexistent · O-6 skew×Galois compatibility theory nonexistent.

## 6. Recommended framework (justified)

Framework = the proved in-repo one (it coincides with the blueprint's mathematical skeleton): A = F_{p^m}[u]/⟨u^t⟩, R = M_r(A), codes = **right ideals** of R[X]/⟨Xⁿ−1⟩, pairing **P1+P2**, σ_k coefficientwise fixing u, θ_k = σ_k∘transpose, φ_n expansion Gray map. Default lane: **m even, k = m/2** (reflexive); m-odd work must be explicitly framed in the non-reflexive duality (double dual σ_{2k}(C)). Notation must be unified: blueprint (r = matrix size, k = Galois) vs prior (m_old, s) — proposed binding choice: **blueprint letters, with a one-time translation table in any new document** (used throughout this audit).

## 7. Three candidate research problems (with required attributes)

### Problem P1 — Non-reflexive (k)-Galois hull theory and odd-m quantum codes
- **Problem:** develop the quantum-facing theory of Hull_k/C^{⊥_k} where m ∤ 2k (double dual σ_{2k}(C)), especially m odd; construct EAQECC families at q = p^{2e+1} (first case q = 8).
- **Required definitions/assumptions:** P1/P2 pairings; σ_{2k}-twisted double duality; hull dimension ℓ = dim(C ∩ C^{⊥_k}) feeding Brun–Devetak–Hsieh.
- **Expected theorem-level contribution:** hull-pair parameter formulas in the non-reflexive regime; first q = 8 EAQECC families from this framework. **Substantial parts already proved in-repo (N4, N7, N9, N12) — the new content is the application layer and new constructions.**
- **Difficulty:** medium. **Computational feasibility:** high (existing engine; q = 8, n ≤ 4 reachable; the census already covers much of it).
- **Literature relation:** extends Liu–Yu–Hu 2019-style (k)-Galois EAQECCs (fields) to matrix rings; stays consistent with N11 trichotomy.
- **Quantum application:** EAQECC, exact c-formulas. **Novelty risk: MEDIUM-HIGH** (derivative-of-own-work unless framed as the m-odd application paper; must cite the in-repo manuscript).

### Problem P2 — (k)-Galois hulls at matrix size r = 3 over A, t ≥ 2
- **Problem:** the full stack (duality → hulls → Gray → quantum) at R = M₃(A), where Morita generator numbers reach 3 and non-principal hull structure is richer; includes enumeration formulas (Gaussian-binomial sums) and the index-3 quasi-cyclic interpretation.
- **Definitions/assumptions:** uniform-in-r proofs transfer (in-repo), but hull structure theorems must be re-presented with μ_B ≤ 3 phenomena; C*-conventions vs A8's M₃(F_p[u]/⟨uᵏ⟩) submodule presentation must be reconciled explicitly.
- **Expected theorems:** r = 3 hull-structure theorem (incl. non-principal hulls, cf. T-173 mechanism amplified), μ-classified enumeration, quantum/EA families over F_{p²}-type fields with certified distances.
- **Difficulty:** medium-high (theory light, computation heavy: |R| = p^{18}·… at m = 2, t = 2). **Computational feasibility:** moderate — Morita+CRT required everywhere; brute force impossible beyond toy sizes.
- **Literature relation:** A9b/A11 (classical M₃), **A8 (Euclidean/Hermitian quantum M₃ — no Galois, no hulls)**; differentiation = the Galois-hull layer + hull-driven c-parameter + non-principality phenomena.
- **Quantum application:** CSS + EAQECC over F_{p²}-family fields.
- **Novelty risk: MEDIUM** — hinges on Rule-compliance: acceptable only with the structural (μ_B/QC-index-3) content, not as a "bigger matrix" parameter paper.

### Problem P3 — Skew-cyclic codes over R = M_r(A) twisted by σ, with (k)-Galois hulls and quantum output
- **Problem:** codes = right ideals of the Ore quotient R[X;σ]/⟨Xⁿ−1⟩ (σ ∈ Aut(R) entrywise Frobenius-type), duality via θ_k with a proved σ↔θ_k compatibility condition (when are duals of skew-cyclic codes skew-cyclic, and what is the hull theory?), Gray transfer, CSS/EA constructions.
- **Definitions/assumptions:** σ must be a *ring* automorphism centralizing the skew variable conditions; compatibility theorem to be discovered/proved (this is the core new mathematics).
- **Expected theorems:** σ–θ_k duality compatibility criterion; skew-cyclic hull structure theorem; parameter families; the skew analogue of T-176-type transport.
- **Difficulty:** HIGH. **Computational feasibility:** moderate at toy sizes with a re-engineered skew arithmetic (existing engine is a template, not a library).
- **Literature relation:** A6 (skew over M₂(F₂), no hulls/quantum/Galois), the skew-commutative hull literature style (C5/C6 without matrix rings, C7 without Galois) — **no located source occupies the intersection**.
- **Quantum application:** CSS + EAQECC with two independent twist parameters (skew σ, Galois k) — a genuinely richer design space.
- **Novelty risk: LOW** among the candidates; the price is difficulty and the need for a clean compatibility theorem before any quantum claim.

## 8. Recommended primary direction

**Sequenced recommendation (evidence-supported):**
1. **Immediate (non-research): Option G5 — finish and submit the existing manuscript.** Close the Option-C item, add A8 (and a differentiating sentence), re-run the 37-entry verification sweep. This converts *completed* work into the Q1 submission the blueprint ultimately wants.
2. **If the intent is a NEW research program: P3 (skew × Galois-hull × matrix ring × quantum)** as primary, **P2 (r = 3 hull program)** as the lower-risk fallback, **P1** only as a component of either, not standalone. Rationale: P3 is the only direction with an unoccupied external intersection *and* unoccupied in-repo content; P2 is defensible solely with its structural (μ_B, index-3 QC, enumeration) theorems; P4-style parameter pushes are excluded by the quality rules.

## 9. Q1 novelty assessment (with limitations)

- The **existing** manuscript's positioning ("the two have not met") survives A8 *only with a differentiating sentence* (A8: Euclidean/Hermitian duals over M₃, no Galois twist, no hulls, F₂₇; in-repo: θ_k-Galois hulls over M₂(A_t), CSS+EA, F₄/F₈/F₉). Without it: desk-reject risk on novelty.
- A **P2** paper is Q1-viable (FFA / Adv. Math. Commun. / Des. Codes Cryptogr. class) only with its structural theorems foregrounded; a **P3** paper — if the compatibility theorem lands — is the strongest Q1 candidate of the three. Journal quartiles must be re-checked at submission time (this sandbox cannot verify current Scimago/CiteScore quartiles; recorded limitation). Quantum-only venues (QIP) are partially de-risked for P2/P3 because A8 already occupies "QIP × matrix-ring cyclic × CSS" under the Euclidean banner.

## 10. GO / CONDITIONAL GO / NO-GO

> ## ⚠ CONDITIONAL GO — the condition being RESCOPING. Unmodified re-execution of the blueprint is NO-GO (it duplicates the author's own completed, submission-prepared manuscript).

**Conditions:**
- **C1.** The in-repo manuscript and artefacts are the baseline; any derivative paper cites it and differentiates explicitly (incl. against A8/QIP-2026, currently uncited).
- **C2.** Author confirms the true submission status of the FFA manuscript (submitted? accepted? in revision?) before *any* publicly visible new work on the same framework.
- **C3.** Notation unified per §6; left/right convention fixed as right ideals (consistent with the register).
- **C4.** Pairing fixed as P1+P2; any new variant must first prove non-degeneracy and module-closure (P3's equivalence reconciliation if ever used).
- **C5.** New-paper direction chosen by the author among P1/P2/P3 (recommended: P3 primary, P2 fallback); parameter-only papers excluded.
- **C6.** Toolchain remains the integrity-verified pure-Python engine (no Magma available; the package's first-principles design is a strength for review).

## 11. Confirmation

**PHASE 1 HAS NOT STARTED.** No new theory was implemented; the only computation run was the re-execution of the data package's own Phase-0 feasibility script for integrity evidence (artifacts preserved in `phase0_audit/evidence/`, its by-products cleaned out of `research-data/`). Phase 1 — or any rescoping decision — proceeds only on explicit author approval.

**Companion deliverables:** `PHASE0_REPOSITORY_AUDIT.md` · `PHASE0_LITERATURE_REVIEW.md` · `PHASE0_RING_FEASIBILITY.md` · `PHASE0_PAIRING_OPTIONS.md` · `PHASE0_RESEARCH_GAP.md` · this report. Supporting extractions/evidence: `phase0_audit/extracted/`, `phase0_audit/pdfs_text/`, `phase0_audit/evidence/`.
