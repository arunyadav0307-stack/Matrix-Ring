# 04 — Proposed mathematical framework and assumption contract

**BLUEPRINT ONLY: definitions and inherited facts, not new proofs.**

[Problem](03_SELECTED_RESEARCH_PROBLEM.md) · [Theorem roadmap](05_THEOREM_ROADMAP.md) · [Quantum boundary](07_QUANTUM_CONSTRUCTION_STRATEGY.md)

## 1. Notation, fixed before research

The old sources use r for the field degree in places. This proposal uses **m for field degree and r for matrix size**; translators must not identify the two.

| Symbol | Meaning / assumption |
|---|---|
| p, q=p^m | p prime; m≥1 in background, m≥2 for a nontrivial coefficient-Frobenius programme |
| A=A_t=F_q[u]/(u^t) | Commutative finite chain ring, t≥1; coefficient automorphisms below fix u |
| R=M_r(A) | Matrix ring; **r=2 in the recommended primary programme** |
| X | **Central** indeterminate; no Ore/skew relation in P2-S |
| B=A[X]/(X^n−1), S=R[X]/(X^n−1) | B commutative; S≅M_r(B); cyclic codes are **right ideals** of S |
| σ_s | a↦a^(p^s) on F_q, extended coefficientwise fixing u,X; s modulo m |
| θ_s=σ_s∘transpose | Anti-automorphism; not assumed involutive |
| rev | X↦X^(−1) on B/S; coefficient reversal modulo n; automorphism, not anti-automorphism |
| Λ | Matrix trace followed by coefficient of u^(t−1), valued in F_q |
| B_s(x,y)=Σ_i θ_s(x_i)y_i | R-valued form, first slot twisted; y lies in the right orthogonal |
| b_s=Λ∘B_s | F_q-valued scalar form; σ_s-semilinear in first slot, linear in second |
| C^(⊥s) | {y:B_s(x,y)=0 for every x∈C}; not an unqualified ordinary Euclidean dual |
| Hull_s(C) | C∩C^(⊥s), always an intersection/submodule of C |
| μ_T(M) | Minimal number of T-module generators; μ(0)=0; not vector-space dimension |
| dim_q | F_q-dimension unless the field is explicitly changed |

Recommended Core A: p=2, q=2^m, m≥2, t=2, n=2, r=2, all s. These are **proposed scope choices**, not approved assumptions for research execution. Wider t/e/r and a skew variable require separate gates.

## 2. Inherited results — inputs, not proposed contributions

The [master mathematical blueprint](evidence/context/phase0_audit/MASTER_CONSOLIDATED_AUDIT/MATHEMATICAL_CORRECTION_BLUEPRINT.md) and [independent pairing audit](evidence/context/phase0_audit/independent_review/PAIRING_AND_DUALITY_CRITICAL_AUDIT.md) control applicability. The old printed manuscript is not a blanket proof authority.

| ID | Background statement retained under its exact hypotheses | Status and limitation |
|---|---|---|
| E01 | A and R are finite Frobenius alphabets; the top-coefficient trace functional supplies the relevant nondegeneracy/ideal-catching structure | Established/imported background; do not infer same-sided perfect duality for an arbitrary form from nondegeneracy alone |
| E02 | For right R-modules and the specified first-slot θ_s pairing, ring-valued and scalar orthogonals agree; duals have the size/dimension complement | Audited conditional mathematics; the manuscript's defective Hom/surjectivity proof is not imported |
| E03 | Identical-twist double dual is **+σ_(2s)(C)**; universal reflexivity requires m divides2s (nontrivial matrix setting) | Inherited; codewise σ_(2s)-invariance is a different hypothesis; slot changes require translation |
| E04 | Under the column Morita dictionary, W≤B^r corresponds to I_W={M:im_B(M)⊆W}; dim_q(I_W)=r dim_q(W) | Standard/inherited; columns for right ideals, not rows |
| E05 | μ_S(I_W)=ceil(μ_B(W)/r); in particular I_W principal iff μ_B(W)≤r | Inherited packing threshold, **not** a new all-r theorem of this project |
| E06 | For C=Σ_i g_iS, W(C)=Σ_i im_B(g_i) and W(C^(⊥s))=∩_i ker_B(θ_s(rev g_i)) | Inherited, with right annihilator/reversal and sides fixed; no one-generator shortcut for a genuinely nonprincipal input |
| E07 | W(Hull_s(C))=W(C)∩W(C^(⊥s)) | Inherited hull reduction; for principal C=gS use im(g)∩ker(θ_s(rev g)) |
| E08 | CRT decomposes B into local repeated-root factors; μ_B(W)=max_j μ_(B_j)(W_j) | Standard/inherited; product of chain rings is not itself necessarily a local chain ring |
| E09 | At r=2, if t=1 or p∤n, all component submodules need at most2 generators, so every cyclic right ideal, including every hull, is principal | Inherited generation result, **not freeness** of every submodule |
| E10 | Coefficient expansion φ:C⊆R^n→F_q^N, N=tr²n, transports b_s to σ_s(x)J y^T with J=I_(r²n)⊗H_t in the fixed ordering | Inherited exact form/coordinate claim; not ordinary Euclidean/Hamming/CSS transfer |

No proofs of E01–E10 are supplied here. Before use in a new paper, a future applicability audit must identify valid supporting arguments and retain their hypotheses. If that requires repairing MS03, that is a **separate old-paper correction task**, not silently authorized by a new research phase.

## 3. Proposed objects for the new question

For C=I_W, define

- **D_s(W):=W(C^(⊥s))**, using the actual global dual and the fixed Morita dictionary;
- **H_s(W):=W∩D_s(W)**;
- **generator-growth statistic Δ_s(W):=μ_B(H_s(W))−μ_B(W)**;
- **principality margin P_s(W):=μ_B(H_s(W))−r**;
- **principal-input spectrum**: the attainable profiles of H_s(W) among W≤B^r with μ_B(W)≤r.

These are **definitions/research bookkeeping**, not claimed new invariants or theorems. Their usefulness and external originality are unverified. Δ can be recorded without assuming its sign. A positive Δ does not alone mean a nonprincipal hull; that requires P_s(W)>0. A nonprincipal **dual** of a principal input, already known internally, is not the same as a nonprincipal **hull**.

A useful profile may retain: field length, μ, radical-layer dimensions, socle dimension/type, relations among minimal generators, off-diagonal extension parameters, and the restricted pairing/embedding data. This list is **not asserted complete**. Equal abstract module type or equal field dimension need not determine how a module meets its dual; any claimed sufficiency is a future theorem obligation.

## 4. Local factors and their forms

Write n=p^a n_0 with gcd(n_0,p)=1 and factor X^(n_0)−1 over F_q. CRT gives local factors B_j; a coordinate model has the form

T_j≅K_j[u,w]/(u^t,w^e),  K_j≅F_(q^(d_j)),  e=p^a.

The exact coefficient-field embedding/isomorphism must be recorded, not assumed canonical. In a non-chain factor (t,e≥2), the maximal ideal is m_j=(u,w). **Nakayama's background identity** is μ_(T_j)(M)=dim_(K_j)(M/m_jM). Computing this quotient on a fully computed hull is not the proposed new theorem.

Core A has a single factor T=F_q[u,w]/(u²,w²) in characteristic2. However, its **duality is induced from the original coefficient pairing and reversal**, not chosen afresh as a convenient dot product on T². Reversal may act nontrivially on nilpotent coordinates in larger multiplicity; a linearized sign replacement is not licensed. For multiple factors, σ_s and reversal can couple different components.

A future local-form contract must specify:

1. source/target factors for every σ_s/rev map;
2. semilinearity over the correct coefficient/residue fields;
3. the induced functional/pairing matrix in the chosen bases;
4. which generator columns and kernels live in each module;
5. how global H_s(W) is reconstructed.

The known split, squarefree permuted-intersection formula is prior work. Establishing or verifying a more general translator is infrastructure unless it has independently demonstrated new content. No local orthogonal or reciprocal-factor formula is proved here.

## 5. Equivalence and normal-form discipline

- A change of generators of **the same** W preserves the input module/code. Exact canonical F_q-basis keys can identify equal subspaces after the B-action closure is known.
- Arbitrary left GL_r(B) changes the **embedded** module and generally its pairing relation. It is not automatically an isometry or hull-preserving equivalence.
- If a normal form uses an ambient change of basis, the pairing/adjunction and all structure operators must be transported too; discard neither the form nor the embedding parameters.
- A B-module isomorphism, a ring-code isometry, a coefficient-Hamming isometry and a physical Clifford/symplectic equivalence are different assertions.
- type(M)=dim_K soc(M) and μ(M)=dim_K(M/mM) must not be equated outside justified chain-ring situations; NL11 makes this distinction essential.

Thus the proposed classification is of a **specified embedded principal-input class with its induced form**, not all wild modules up to abstract isomorphism.

## 6. Correct dimensions, coordinates and metrics

For r=2, a Morita vector has2tn F_q coordinates; a word of R^n has4tn. If dim_q W=d, then dim_q C=2d. A field basis of the **hull Morita module** is not a full field basis of the image code. Feeding full image rows into a Morita unpair routine recreates MC11.

Coefficient expansion has N=tr²n and quasi-cyclic index tr² in the stated ordering, not index r. Its metric is coefficient Hamming, not ring-symbol Hamming or normalized homogeneous weight. A nonmonomial coordinate congruence may change minimum distance and requires recertification. In characteristic2, the alternating **bilinear** obstruction at even t does not forbid every Hermitian congruence or every code-specific CSS inclusion.

## 7. Explicit exclusions

No unqualified freeness, arbitrary automorphisms moving u, automatic Euclidean/trace orthogonal substitution, unverified skew quotient, generic gcd impossibility claim, conjectural DD-reflexivity assumption, or μ-to-entanglement identification is allowed. P3 would need its own Ore quotient and sided compatibility contract before adopting any of this central-variable framework.

**No new theorem is proved or computational method implemented in this framework. All future work is approval-gated.**

**BLUEPRINT DEVELOPMENT ONLY — wait for explicit author approval before Phase1.**
