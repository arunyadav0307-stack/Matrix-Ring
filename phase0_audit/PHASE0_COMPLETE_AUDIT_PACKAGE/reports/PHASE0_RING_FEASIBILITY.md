# PHASE 0 — RING & MODULE FEASIBILITY
## Candidate framework: A = F_{p^m}[u]/⟨u^t⟩ (t ≥ 2), R = M_r(A) (r ≥ 2)

**Notation reconciliation (mandatory, recorded once):** this blueprint writes q = p^m, R = M_r(A), Galois parameter k (σ_k : a ↦ a^{p^k}, 0 ≤ k < m). The prior in-repo project writes q = p^{r_old}, R = M_{m_old}(A_t), Galois parameter s. **Mapping: m ↔ r_old, r ↔ m_old, k ↔ s.** All imported results below are restated in *this blueprint's* notation and tagged **[REPO-proved]**, **[REPO-computed]**, or **[OPEN]**, with my independent algebraic analysis interleaved.

---

## 1. Base ring A = F_{p^m}[u]/⟨u^t⟩

Independent derivation (standard chain-ring theory, consistent with the prior register):
- A is a **commutative, local, principal ideal ring (a finite chain ring)**: |A| = p^{mt}; unique maximal ideal ⟨u⟩; ideals exactly ⟨u^i⟩, 0 ≤ i ≤ t; residue field A/⟨u⟩ ≅ F_{p^m}; socle ⟨u^{t-1}⟩ ≅ F_{p^m}.
- A is **Frobenius** (chain rings are Frobenius): the functional λ(a) := coefficient of u^{t-1} generates the character module; composing with the matrix trace and the field trace gives the standard generating character of R below.
- Automorphisms: the coefficientwise lift of σ_k (fixing u) is an R_t-algebra automorphism of A of order m/gcd(k,m); **σ_k = id_A if m = 1** — a genuine (k)-Galois theory with k > 0 requires **m ≥ 2**. This matches [REPO-proved T-003] and the E1 experiments re-run in this audit (`phase0_audit/evidence/`).

## 2. Matrix ring R = M_r(A)

- |R| = p^{mtr²}; **noncommutative for r ≥ 2**; center Z(R) = A·I_r.
- R ≅ M_r(F_{p^m}) ⊗_{F_{p^m}} A; Jacobson radical J(R) = M_r(⟨u⟩), R/J(R) ≅ M_r(F_{p^m}) (simple Artinian).
- **Ideals:** two-sided ideals are exactly M_r(⟨u^i⟩) = u^i R (t+1 of them: R is *not* a one-sided chain ring). Right ideals correspond, via Morita equivalence A ∼ R, to A-submodules W ≤ A^r: I_W = {matrices with all columns in W}. Finitely many ⟺ A finite — here yes; **most one-sided ideals are non-principal** (generator-number μ(W) can attain r) — [REPO-computed C3: right ideals of M₂(F_q) number q+3 for q ∈ {2,4,8,9}; nonprincipal hull witnesses exist at t = 2, `quantum_code_records/nonprincipal_witnesses.csv`].
- R is **Frobenius** [B1 Wood 1999; REPO register imported facts]: (X,Y) ↦ Tr(XY) is a non-degenerate A-bilinear symmetric form on the free A-module R (Tr(X E_{ba}) = X_{ab} shows the dual basis exists). Hence a perfect duality theory is available — *but only through forms compatible with the one-sided module structure* (see Pairing Options).

## 3. Cyclic-code module representation (RQ1)

- Fix the polynomial variable **central**: R_n := R[X]/⟨X^n−1⟩ ≅ M_r(B) with B := A[X]/⟨X^n−1⟩ commutative [REPO Stage 1; X central convention with shift identity T-explicit].
- **Convention (must be fixed and respected):** the prior project — and Alahmadi et al. (A1) — take **cyclic codes = right ideals of R_n**, equivalent to right R-submodules of R^n closed under the cyclic shift; the mirror theory with left ideals is obtained via the opposite ring. *This audit adopts the right-ideal convention as the standing one; every statement below carries its side.*
- Morita: cyclic codes ↔ B-submodules W ≤ B^r; **two-sided ideals correspond to W = I^r for B-ideals I** and "two-sided cyclic codes" reduce to codes over the commutative quotient — structurally simpler and largely covered by commutative literature; the noncommutative substance is in the one-sided theory [REPO O6 exclusion decision, audited as sound].
- **Semisimplicity constraint:** gcd(n,p) = 1 ⟹ Xⁿ−1 squarefree ⟹ CRT/Hensel component decomposition over the **center** F_{p^m}[X] governs structure and enumeration [REPO-proved T-018 *with the squarefree hypothesis* — counterexample recorded: q = 4, n = 2 has 33 ≠ 49 codes, i.e. the formula fails without it]; p | n gives ramified/wild regimes where principality fails in general [REPO T-173: hulls/codes need not be principal, phenomenon confined to t ≥ 2 and p | n].

## 4. Automorphism candidates and reflexivity (the decisive structural constraint)

- **σ_k on R** (entrywise, fixing u): ring automorphism, order m/gcd(k,m) [REPO-proved N1/T-002; E1 re-run confirms].
- **θ_k := σ_k ∘ transpose**: anti-automorphism of R with **θ_k² = σ_{2k}**: an *involution* ⟺ m | 2k [REPO-proved N1].
- **Reflexivity of the induced duality** (x ⊥_k y ⟹ y ⊥_k x; equivalently (C^{⊥_k})^{⊥_k} = C without the σ_{2k}-twist) holds **⟺ m | 2k** [REPO-proved N5/N11 with computed counterexample: at q = 8 (m = 3) reflexivity fails for 702 of 737 length-3 cyclic codes]:
  - **m odd:** nontrivial Galois action (k ≠ 0) and reflexivity are **mutually exclusive**.
  - **m even:** the unique nontrivial reflexive choice is the **Hermitian-like midpoint k = m/2**.
  - The double dual always satisfies (C^{⊥_k})^{⊥_k} = σ_{2k}(C) [REPO-proved N4], so the non-reflexive regime is still a *tame* duality theory — this is a genuine design fork (see Decision Report, Problems P1 vs P2/P3).

## 5. Candidate parameter tuples (r, p, m, t)

| (r, p, m, t) | A | R | |R| | Galois k options | Reflexive? | Status vs prior computation |
|---|---|---|---|---|---|---|
| (2,2,2,1) | F₄ | M₂(F₄) | 2⁸ | k∈{0,1} | k=1 ✓ (midpoint) | **[REPO hub]** exhausted n ≤ 6 |
| (2,2,2,2) | F₄[u]/u² | M₂ | 2¹⁶ | k∈{0,1} | k=1 ✓ | duality verified t=2; census at n≤2 |
| (2,2,3,1) | F₈ | M₂ | 4096 | k∈{0,1,2} | **none nontrivial** (m=3) | size/closure OK, reflexivity fails (702/737) |
| (2,3,2,1) | F₉ | M₂ | 6561 | k∈{0,1} | k=1 ✓ | [REPO hub] exhausted n ≤ 6 |
| (2,2,4,1) | F₁₆ | M₂ | 2¹⁶ | k∈{0,…,3} | k=2 ✓ (only midpoint) | **unexplored computationally** |
| (3,2,2,1) | F₄ | M₃ | 4⁹ = 2¹⁸ | k∈{0,1} | k=1 ✓ | theory uniform-in-r [REPO-proved]; no computations; classical M₃ papers exist (A9b, A8, A11) |
| (3,2,2,2) | F₄[u]/u² | M₃ | 2³⁶ | k∈{0,1} | ✓ | unexplored; Morita/CRT machinery required (μ_B ≤ 3) |
| (2,2,2,3),(2,2,2,4) | t = 3,4 | M₂ | 2²⁴, 2³² | k∈{0,1} | ✓ | partial census (t≤4, n≤2); wild cases blocked |

Standing arithmetic: |R_n| = |R|ⁿ = p^{mtr²n}; Gray/expansion length to the field: N = t·r²·n over F_{p^m} (prior: Nlen = 4tn at r = 2 ✓).

## 6. Feasibility assessment per research question

| RQ | Status | Evidence |
|---|---|---|
| RQ1 module structure | **Feasible — established in-repo** | right-ideal convention, Morita correspondence, shift convention T [REPO-proved Stages 1–2A] |
| RQ2 non-degenerate (k)-Galois pairing | **Feasible — established in-repo** | B_k = Σ θ_k(x_i)y_i proved: non-degenerate, right-linear in y, θ_k-semilinear in x, size formula, dual is right ideal, σ_{2k} double dual [N1–N12]; naive products provably fail [T-006] — see Pairing Options |
| RQ3 Galois dual/hull characterization | **Feasible — established in-repo** | dual formula rev∘ann_r∘θ_k (Thm 3.8); hull = I_{W∩W′} cyclic; hulls can be non-principal for t ≥ 2, p | n [T-173]; dimension formulas for principal cases; general dimension formula **[OPEN]** (distributions computed) |
| RQ4 Gray compatibility | **Feasible — established in-repo for the specific φ_n** | entrywise+u-adic expansion φ_n with transported pairing; 463/463 checks; the compatibility is **proved for this map**, not assumed [T-176…189]; general compatibility theorem for arbitrary Gray maps **[OPEN]** |
| RQ5 CSS quantum codes | **Feasible — established in-repo** | routes SO/DC via stabilizer/CSS, EA via hull dimension c; 28 certified codes; quantum Singleton defects computed; benchmarking gaps: q = 8 untabulated; no EA table exists (404) |
| RQ6 precise novelty | **NOT feasible as posed** — the posed program exists in-repo (see Decision Report) |

## 7. What remains genuinely open (mathematically)

1. **t ≥ 2 structure theory in full generality** (classification/principality of one-sided cyclic codes without the t = 1 ∧ gcd(n,p) = 1 hypotheses; T-021 is conditional).
2. **General hull-dimension formulas** beyond computationally recorded distributions.
3. **The 15 blocked census families** (component BFS too large; n up to 6 at q ≤ 9, r = 2) — larger (n, q, r) need sharper theory, not more BFS.
4. **q = 8 benchmarking** (no external table) and **EA-code benchmarking** (no table exists) — reporting-limitation, not mathematics.
5. Uniform-in-(r, t) *stated* theorem package: the in-repo duality theorems are proved uniformly in r and t, but the manuscript's framing is r = 2; an r ≥ 3 presentation must redo the *classical-side* citations (A8–A11 occupy M₃/M₄ classically).

## 8. Verdict of this section

**Mathematically FEASIBLE** — indeed, stronger: feasibility is not merely argued but *demonstrated* by an integrity-verified, re-executed body of proofs and computations already in this repository. The binding constraints are: **m ≥ 2** (nontrivial Galois), **gcd(n,p) = 1** for the clean structure theory (ramified cases deliberately separated), the **reflexivity fork m | 2k**, and the **one-sided (right-ideal) convention**. The feasibility question that Phase 0 was commissioned to answer is therefore superseded by a *duplication* question — carried to the Research Gap and Decision reports.
