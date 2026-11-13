# PHASE 0 — PAIRING OPTIONS
## Candidate (k)-Galois pairings on modules over R = M_r(A), A = F_{p^m}[u]/⟨u^t⟩

**Conventions.** Codes are **right** R-submodules of R^n (the standing convention; the left-sided mirror theory is obtained by replacing R with R^op and is stated alongside when relevant). σ_k : a ↦ a^{p^k} coefficientwise on A (fixing u), entrywise on R; transpose (·)ᵀ; θ_k := σ_k ∘ (·)ᵀ (anti-automorphism, θ_k² = σ_{2k}); Tr = matrix trace (A-valued); λ(a) = coefficient of u^{t-1}. Evidence tags: **[PROVED]** a proof exists (in-repo register T-…/N1–N12, independently re-verified 2026-11-04 by the prior audit's from-scratch re-derivation, and re-confirmed computationally by this audit's re-run) · **[COMPUTED]** exhaustive/seeded checks only · **[CANDIDATE]** my analysis in this audit, proof deferred · **[REJECTED]** with documented counterexample.

---

## P0 — Plain R-valued dot product  ⟨x,y⟩₀ = Σᵢ xᵢ yᵢ  — [REJECTED]

Additivity and right R-linearity in y hold, so C^{⊥₀} is a right submodule — but the form is **degenerate as a module pairing over the noncommutative R**: the annihilator/size law fails systematically.
**Counterexample evidence:** at R = M₂(F₂), n = 3, **31 of 35 cyclic codes satisfy |C|·|C^{⊥₀}| ≠ |R|ⁿ** (in-repo Phase-0 experiment E4; re-executed in this audit's re-run, matching the recorded log; proved failure mechanism = register T-006). Left/right mirror versions fail identically. This is exactly the pitfall the blueprint's Rule ("never assume extension of the field-level product") guards against.

## P1 — R-valued θ_k-form  B_k(x,y) = Σᵢ θ_k(xᵢ)·yᵢ  — **[PROVED] — primary candidate**

- **Domain/codomain:** R^n × R^n → R.
- **Linearity:** additive in both; **right R-linear in the 2nd variable:** B_k(x, yb) = B_k(x,y)·b; **θ_k-semilinear in the 1st:** B_k(ax, y) = θ_k(a)·B_k(x,y) (uses anti-multiplicativity of θ_k; this is *why the transpose is unavoidable*: an automorphism-twist alone cannot absorb left multiplication on a noncommutative ring).
- **Non-degeneracy:** for x ≠ 0 pick coordinate i and entry (a,b) with (xᵢ)_{ab} ≠ 0; choosing y = E_{ba} at coordinate i yields B_k(x,y) ⊇ σ_k-conjugate of (xᵢ)_{ab} ≠ 0 (full proof: register T-007/§3; the E_{ba}-probe is non-degeneracy of (X,Y) ↦ XY composed with an anti-automorphism). Hence the finite-size duality law **|C|·|C^{⊥_k}| = |R|ⁿ** for right submodules C.
- **Dual structure:** C^{⊥_k} is a right R-submodule; **cyclic if C is cyclic** via the shift identity B_k(x, Ty) = B_k(T^{-1}x, y) [N8]; the generator-level formula is C^{⊥_k} = rev(ann_r(θ_k C)) [Stage 2C Thm 3.8, uses reversal rev(X) = X^{-1}].
- **Double dual:** (C^{⊥_k})^{⊥_k} = σ_{2k}(C) for **every** k [N4, 6961/6961]; **reflexive ⟺ m | 2k**; symmetry identity θ_k(B_k(x,y)) = B_k(y, σ_{2k}x) [N2].
- **Hull:** Hull_k(C) := C ∩ C^{⊥_k} is again a cyclic right ideal, σ-equivariant [N12]; structure at generator level Hull_k(C) = I_{W∩W′} [Stage 3A], non-principal hulls exist (t ≥ 2, p | n) [T-173].
- **Left-sided mirror:** B′_k(x,y) = Σᵢ xᵢ·θ_k(yᵢ) on left R^n gives the left theory (right-linear ⇄ left-linear swapped). No mixing of sides is permitted anywhere.

## P2 — F_{p^m}-valued form  b_k := λ ∘ Tr ∘ B_k  — **[PROVED] — Gray-coherent companion**

- b_k(x,y) = λ( Σᵢ Tr( θ_k(xᵢ) yᵢ ) ) ∈ F_{p^m} (then Tr_{F_{p^m}/F_p} gives F_p-valued).
- **Theorem [N9]:** the F_{p^m}-valued orthogonal equals the R-valued orthogonal (mutual inclusion + equal size). So duality computations may use the scalar-valued form without loss.
- **Why it matters (Gray):** under the entrywise+u-adic expansion φ_n : R^n → F_{p^m}^{tr²n}, the transported form ⌈φ(x), φ(y)⌉ is an explicit F_{p^m}-valued Galois-type pairing for which **φ_n(C^{⊥_k}) = (φ_n C)^{⊥_k̂}-type compatibility is PROVED for this specific map** [T-176…189; 463/463 checks PASS]. This is the exact place where "never assume Gray compatibility" (Rule) was honored by proof — the reversal/permutation bookkeeping lives inside λ (coefficient of u^{t-1}) and is **not** a cosmetic detail.

## P3 — A-valued trace-transpose form  ⟨x,y⟩_k := Σᵢ Tr( xᵢ σ_k(yᵢ)ᵀ )  — **[CANDIDATE]** (independent alternative recorded in this audit)

- A-valued, A-bilinear up to the σ_k-twist, **non-degenerate** (proof sketch: fix x ≠ 0, (xᵢ)_{ab} ≠ 0; take yᵢ with σ_k(yᵢ)ᵀ = E_{ba}; then Tr(xᵢE_{ba}) = (xᵢ)_{ab} ≠ 0).
- Stability of duals under the R-action follows from trace cyclicity (Tr(PQ) = Tr(QP)): ⟨x, by⟩_k = ⟨σ_k(b)ᵀx, y⟩_k-type computations close the annihilator on the correct side.
- **Relation to P1/P2:** P3 differs from P2 by dropping λ and by where the transpose/automorphism sit; after applying λ∘(·), the two coincide up to σ-relative bookkeeping, so P3 is *not* a genuinely new theory — its duality is equivalent to P1's under θ ↔ σ-transpose exchange. **Recorded for completeness; NOT recommended** as the primary form (P2's equal-orthogonal theorem already exists for P1, and P3's value-range A adds no information over R after applying λ). Kept in the register so that a future phase does not rediscover it as "new".

## P4 — Character-theoretic (Frobenius/wood) framing — **framework [PUB], not to be claimed**

- R is Frobenius; with generating character χ = Tr_{F_{p^m}/F_p} ∘ λ ∘ Tr, annihilator duality w.r.t. non-degenerate sesquilinear forms relative to anti-automorphisms is **published framework** (Wood 1999; Wood 2010; Szabo–Wood 2017; Nebe–Rains–Sloane 2006; Dougherty–Leroy 2016). B_k is an instance. Consequently: **the pairing mechanism is not novel; the cyclic-structural + hull + quantum specialization is where novelty must live.** This is the prior audit's F-02 correction, re-confirmed here.

## Options ledger (status table)

| Option | Values | Module-side validity | Non-degenerate | Dual module-closed | Reflexivity | Gray coherence | Status |
|---|---|---|---|---|---|---|---|
| P0 plain dot | R | ✗ law fails | — | (closed) | — | — | **[REJECTED]** (T-006; E4 31/35) |
| P1 B_k = Σθ_k(xᵢ)yᵢ | R | ✓ | ✓ | ✓ (same side) | ⟺ m∣2k | via P2 | **[PROVED]** primary |
| P2 b_k = λTrB_k | F_{p^m} | ✓ | ✓ | ✓ | ⟺ m∣2k | ✓ (φ_n, proved) | **[PROVED]** companion |
| P3 ΣTr(xᵢσ_k(yᵢ)ᵀ) | A | ✓ (candidate) | ✓ (sketch) | ✓ (sketch) | ⟺ m∣2k (expected) | via P2-equivalence | **[CANDIDATE]** — equivalence to P1/P2 to be formally reconciled if ever used |
| P4 character/MacWilliams | F_p | ✓ | ✓ | ✓ | depends | — | **[PUB framework]** |

## Failed approaches register (Rule 12)

1. **Plain dot product** (P0) — fails the size law on one-sided modules (31/35 at q = 2, n = 3). *Mechanism:* annihilator of a right ideal under x ↦ Σxᵢyᵢ conflates left and right actions; noncommutativity breaks perfectness.
2. **"Automorphism-only" twist** Σ xᵢ σ_k(yᵢ) (no transpose): right-linearity in y would need σ_k(by) = bσ_k(y) — false for b matrix-valued (σ_k acts entrywise and cannot cross the left factor). Documented hypothesis, rejected by the same noncommutativity obstruction; the transpose is forced (θ_k anti, not auto).
3. **Two-sided-ideal-only codes:** duality works trivially but reduces to commutative quotient structure — excluded for novelty reasons (prior O6), reconfirmed.
4. **k-Galois with m = 1 (q = p):** σ_k = id — a "Galois" claim here would be fraudulent; excluded [N11].
5. **Reflexivity by default:** assuming ⟨x,y⟩_k = 0 ⟺ ⟨y,x⟩_k = 0 without m | 2k is false (counterexample family W = A(e₁ + a e₂); 702/737 computationally at q = 8) — never assert without the check [N5].

**Recommendation (carried to the Decision Report):** adopt P1 as the defining pairing with P2 as its scalar-valued/Gray-coherent companion; treat the reflexivity restriction m | 2k (i.e., m even, k = m/2) as the **default design lane**, with the non-reflexive regime explicitly flagged wherever used.
