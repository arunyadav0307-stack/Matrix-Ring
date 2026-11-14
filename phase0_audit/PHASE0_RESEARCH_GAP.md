# PHASE 0 — RESEARCH GAP ANALYSIS

**Date:** 2026-11-12 · This report answers RQ6: *the precise mathematical novelty compared with existing matrix-ring quantum-code constructions and Galois-hull quantum-code constructions.*

---

## 1. The headline: the proposed intersection is already occupied — by this repository

| Blueprint pillar (new) | Prior in-repo coverage | Status of the pillar |
|---|---|---|
| 1. Matrix ring structure & module theory | `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`, Stages 1–2B (Morita, CRT/Hensel, principality with hypotheses) | **Covered** (proved; conditional corners documented: T-021, squarefree hypothesis, non-principality T-173) |
| 2. (k)-Galois automorphisms & inner products | `PAIRING_COMPLETE_PROOFS.md` + audit re-derivation (N1–N11, all k; reflexivity criterion m∣2k in new notation) | **Covered** (proved) |
| 3. Galois duality & hulls | Stage 2C (dual formula), 3A/3B (hull structure/enumeration; cyclic hulls; non-principal hulls) | **Covered** (proved + enumerated; general dimension formula open) |
| 4. Gray map & compatibility | Phase 4 document: φ_n, transported-pairing compatibility **proved**, 463/463 checks | **Covered** (proved for that map) |
| 5. CSS quantum construction | Phase 5–7: SO/DC/EA routes, 28 certified codes, comparisons, honest limitations | **Covered** (computed/certified; benchmarking limits stated) |

The new blueprint's "(k)-Galois" is the prior project's "s/ℓ-Galois": same automorphism a ↦ a^{p^k}, same ring family, same objective, same endpoint (CSS + EAQECC). **Title difference: the single token "(k)-".** Re-executing the blueprint would re-prove proved theorems and re-compute computed tables — and any resulting "new paper" would substantially duplicate the author's own manuscript already prepared for *Finite Fields and Their Applications*.

## 2. External occupation of neighboring territory (see Literature Review for verification tags)

| Territory | Occupied by | Year |
|---|---|---|
| Cyclic codes over M₂, M₃, M₄ of F_p[u]/⟨uᵗ⟩-type rings (classical) | A1–A5 (2013–2019), A9/A10 (2021/2022), A7/A11 (2026 — same school) | 2013–2026 |
| **Quantum codes from cyclic codes over matrix rings** (Euclidean/Hermitian duality, M₃(F_p[u]/⟨uᵏ⟩), CSS + Gray, F₂₇ quantum families) | **A8 — Joshi, Patel, Prakash, QIP 25:207** | **2026** |
| ℓ-Galois hulls → QECC/EAQECC/QMDS over **commutative** rings (incl. Gray-compatible maps) | C5 (Entropy 2026 per prior audit), C6 (2024/25), C2/C2′/C3/C4 (fields, 2018–2021) | 2018–2026 |
| Hulls over a **noncommutative** alphabet (non-unital ring E; Euclidean/symplectic) | C7 Kushwaha–Prakash | 2025/26 |
| Skew-cyclic codes over M₂(F₂) (no hulls/quantum/Galois) | A6 Si–Niu 2023; Du–Niu 2025 | 2023/25 |
| Anti-automorphism/sesquilinear duality framework over Frobenius rings | B1–B5 (Wood; Szabo–Wood; NRS; Dougherty–Leroy) | 1999–2017 |

**Consequence:** any novelty claim must simultaneously differentiate from (i) the in-repo manuscript, (ii) A8, (iii) C5/C6, (iv) C7. A "first quantum codes from matrix rings" claim is dead (A8, externally verified 2026-06-09). A "first hulls over noncommutative rings" claim is dead (C7). The defensible sliver — *Galois* hulls of *cyclic* codes over *matrix rings* with *quantum* output — is precisely the in-repo manuscript.

## 3. Genuinely unexplored directions (candidate gaps)

### G1 — The non-reflexive (k)-Galois regime and its quantum use  · novelty risk: **MEDIUM-HIGH**
The proved in-repo law (C^{⊥_k})^{⊥_k} = σ_{2k}(C) with parameter invariance (N7) was *set aside*, not exploited. Open content: hull-pair theory (C, C^{⊥_k}) across two different dualities; EAQECC/LCD constructions at m odd (e.g. q = 8, where the prior system proved no reflexive duality exists); symmetrized forms (k, m−k) couples. Theorems substantially exist; the *application layer* does not. Risk: derivative of the in-repo manuscript unless the quantum constructions are genuinely different (m-odd families).

### G2 — Matrix size r ≥ 3 with the Galois-hull stack (t ≥ 2)  · novelty risk: **MEDIUM**
Duality theorems are uniform in r (proved), but no computations or manuscript exist beyond r = 2. The M₃ classical (A9b, A11) and M₃-Euclidean-quantum (A8) slots are taken by the IIT-Patna school; the M₃ (or general r) **Galois-hull** slot is not. Required structural value-add (Rule: no "size-change novelty"): Morita data with generator number μ_B up to r (non-principal hulls at μ_B ≥ 3 already witnessed at r = 2, t = 2 — the phenomenon *grows* with r), links to quasi-cyclic codes of index r (Solé–Yemen viewpoint), and enumeration formulas via Gaussian binomials. Feasible with the existing pure-Python engine; memory wall at N = tr²n.

### G3 — Skew-cyclic (Ore-twisted) codes over M_r(A) with (k)-Galois hulls → quantum  · novelty risk: **LOW(-er), if executed with a real internal-consistency theorem**
No source located (in-repo 37-entry bibliography + this audit's checks + the A-cluster) combines: skew polynomial rings R[X; σ] over a noncommutative base, a *second* twist θ_k in the pairing, hull theory, Gray transfer, and quantum construction. The skew cluster over matrix rings (A6) has none of these; skew-Galois-hull treatments in the commutative world (style of C5/C6) have no matrix rings. Genuine theorem-level problem: compatibility condition between the skew automorphism σ and the duality anti-automorphism θ_k (σ must interact correctly with rev/annihilator for duals of skew-cyclic codes to be skew-cyclic) — a real algebraic content claim, not a parameter push. Difficulty: HIGH; computation: feasible at small (r, q, t, n) with the existing engine patterns (exact first-principles arithmetic), but skew multiplication raises cost.

### G4 — Deep-nilpotent / wide-parameter quantitative program (t ≥ 3, q = 16, r = 2, semisimple n growing)  · novelty risk: **HIGH**
Extends tables; theorems mostly in place; little journal-level novelty beyond new parameters, which the quality rules explicitly disallow as a novelty basis. Not recommended as a paper.

### G5 — Stewardship of the existing manuscript (not a new paper)  · **highest expected value per unit effort**
The in-repo manuscript is at submission-prep with one open compliance item (FFA Option C → "conditionally acceptable — editorial confirmation required", Phase 23) and a literature gap found by this audit (A8/QIP-2026 uncited; positioning sentence "quantum codes … over matrix rings … the two have not met" needs a nuance sentence differentiating A8's Euclidean/Hermitian M₃ route). This is the shortest path to an actual Q1 submission.

## 4. Gap-validity grading

| Gap | Mathematically meaningful new theorems needed? | Quantum application | Occupied externally? | Occupied in-repo? | Verdict |
|---|---|---|---|---|---|
| G1 | mostly proved; applications new | EAQECC at odd m | No sign | theory yes, applications no | viable as *extension note*, weak as standalone |
| G2 | yes (μ_B-structure, index-r QC links, enumeration) | CSS + EA | partially (A8 only Euclidean/Hermitian at r = 3) | no (r = 2 only) | **viable with structural novelty argument** |
| G3 | yes (σ–θ_k compatibility hull theory) | CSS + EA | no evidence | no | **strongest new-paper candidate** |
| G4 | few | parameter tables | style occupied | partially | not recommended |
| G5 | n/a | n/a | n/a | the manuscript itself | **immediate action** |

## 5. Explicit non-gaps (do not re-propose)

1. θ_k-pairing validity/non-degeneracy/size/double-dual/reflexivity — done.
2. Cyclicity of Galois duals; hull structure Hull_k(C) = I_{W∩W′}; cyclic hulls; σ-equivariance — done.
3. Gray compatibility via transported pairing for φ_n — done (463/463).
4. CSS/EA routes with certified small codes at q = 4, 8, 9 — done (28 codes).
5. "Quantum codes from cyclic codes over matrix rings" as a headline — externally taken by A8.
