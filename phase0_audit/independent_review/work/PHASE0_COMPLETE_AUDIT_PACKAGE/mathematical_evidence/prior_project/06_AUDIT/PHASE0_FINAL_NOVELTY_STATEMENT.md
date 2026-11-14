# Phase 0 — Final Novelty Statement (for researcher approval)

**Status:** draft, prepared by the audit. **Not a decision.** Every item below is
classified, with its evidence, into one of four boxes:

* **[PUB]** already published — we may use it, not claim it;
* **[NEW]** our proposed new result — with a written proof;
* **[CMP]** established computationally only — reproducible, but **not** a theorem;
* **[TOP]** still requires a theoretical proof (open).

The classification is the audit's; the final wording is the researcher's.

---

## 1. The four boxes

### A. [PUB] Already published — cite, do not claim

| # | Result | Source |
|---|---|---|
| P1 | Duality for codes over a finite ring obtained by assuming an **anti-isomorphism** of the ring and a well-behaved duality on the module alphabet | J. A. Wood, *Int. J. Inf. Coding Theory* **1**(4) (2010) 429–444, doi:10.1504/IJICOT.2010.032867 — "an elaboration on ideas of Nebe, Rains and Sloane" |
| P2 | Over a finite Frobenius ring, duals w.r.t. non-degenerate **sesquilinear** forms (relative to an anti-automorphism) and bilinear forms: module structure of the dual, **double-dual property**, cardinality complementarity, **MacWilliams identities** | Szabo & Wood, *J. Algebra Comb. Discrete Struct. Appl.* **4**(2) (2017) 105–113, doi:10.13069/jacodesmath.284934 (MR3601342, Zbl 1423.94156) |
| P3 | Form rings / types for self-dual codes over finite rings, including non-commutative alphabets such as `F_q + F_q u` with `u² = 0`; Clifford–Weil genus-`m` weight enumerators | Nebe, Rains & Sloane, *Self-Dual Codes and Invariant Theory*, Alg. Comput. Math. **17**, Springer 2006 |
| P4 | Left/right orthogonals over non-commutative Frobenius rings: a code equals its left orthogonal iff it equals its right orthogonal; constructions from self-dual codes over the centre | Dougherty & Leroy, *AAECC* **27** (2016) 185–203, doi:10.1007/s00200-015-0277-0 |
| P5 | **Cyclic self-dual codes over `M_2(F_2)`** (and `M_2(F_2[i])`), by analogy with `Z_4`; factorisations of `X⁷+1` over `M_2(F_2)` | P. Solé, 11th Mediterranean Microwave Symposium (MMS) 2011, doi:10.1109/MMS.2011.6068573 |
| P6 | Hulls (Euclidean/symplectic, left/right/two-sided) over a non-commutative **non-unital** ring; build-up, hull variation, classification up to length 8 | Kushwaha & Prakash, arXiv:2512.12335 (2025); arXiv:2601.06609 (2026) |
| P7 | Galois (ℓ-Galois) hulls of constacyclic codes → QEC/QMDS/EAQEC over **commutative** rings | Zhang, Kong & Zheng, *Entropy* **28**(4) 407 (2026); Li & Liu, *Quantum Inf. Process.* **24**:49 (2025); Debnath & Prakash, ICTIS 2025 |
| P8 | σ-inner products / σ-duals for classical and quantum codes over **fields** | e.g. arXiv:2606.13467 (2026) and refs. [3],[4] therein; Fan–Zhang 2017 |
| P9 | Frobenius rings as the exact alphabets for a perfect duality / MacWilliams extension theorem | Wood, *Amer. J. Math.* **121** (1999) 555–575 (already our E-001) |

### B. [NEW] Proposed new results (proofs written in this repository)

| # | Result | Where | Status |
|---|---|---|---|
| N1 | `θ_s = σ_s ∘ transpose` is an anti-automorphism of `M_m(A_t)` with `θ_s² = σ_{2s}`; involution ⟺ `r ∣ 2s` | `PAIRING_COMPLETE_PROOFS.md` §1 | proved + verified `[EXH]` |
| N2 | **Key identity** `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)`; hence `B_s` is symmetric ⟺ `σ_{2s} = id` | audit `PHASE0_PROOF_VERIFICATION.md` §3 | proved (**new in the audit**) |
| N3 | Pairing `B_s(x,y) = Σ θ_s(x_e) y_e`: non-degenerate, right-`R`-linear in `y`, `θ_s`-semilinear in `x`; `C^{⊥_s}` is a right `R`-module; `|C|·|C^{⊥_s}| = |R|^n` | proofs §3 | **proved** (size formula is a proof, not an observation) |
| N4 | **Double dual** `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` — the twisted form, valid for *every* `s` | proofs §3; audit §5 | proved + verified 6 961/6 961 and 100 % independently |
| N5 | **Reflexivity criterion** `r ∣ 2s`, with the counterexample `W = A_t(e_1 + a e_2)` and the essential hypothesis `m ≥ 2` | proofs §3 | proved + verified (35/737 at `q = 8`) |
| N6 | **σ_{2s}-isometry**: `B_s(σ_k x, σ_k y) = σ_k B_s(x,y)`; weight, dual and hull are `σ_k`-equivariant | audit §8 | proved + verified (E1–E5, 100 %) |
| N7 | **Parameter invariance** in the non-reflexive regime: `C^{⊥⊥}` has the same size, weight enumerator, minimum distance and hull dimension as `C` | audit §8 | proved (from N4 + N6) |
| N8 | Cyclicity of the θ_s-dual, by the direct shift identity `B_s(x, Ty) = B_s(T^{−1}x, y)` | audit §7 | proved |
| N9 | Equality of the `R`-valued and `F_q`-valued orthogonals (inclusion + equal dimension) | audit §9 | proved + verified 6 961/6 961 |
| N10 | Generalisation to an arbitrary `τ ∈ Aut(A_t)`: `θ_τ² = τ²`, `(C^⊥)^⊥ = τ²(C)`, reflexive ⟺ `τ² = id` | audit §1, §5 | proved |
| N11 | **Parameter trichotomy**: `r = 1` ⇒ no Galois action; `r` odd ⇒ non-trivial Galois action and reflexivity are mutually exclusive; `r` even ⇒ `s = r/2` is the unique non-trivial reflexive choice | `PHASE0_U8_U9_DECISIONS.md` §4 | proved |
| N12 | **Galois (σ_s-) hulls of cyclic codes over matrix rings**: `Hull_s(C) = C ∩ C^{⊥_s}` is a cyclic code, `Hull_s(σ_k C) = σ_k Hull_s(C)` | proofs §3 + audit | proved |

### C. [CMP] Established computationally — **not** theorems

| # | Result | Range | Label |
|---|---|---|---|
| C1 | Cyclic-code census: `q=4,n=3 → 343`; `q=9,n=2 → 144`; `q=9,n=4 → 1200 sampled`; `q=8,n=3 → 737`; `q=2,n=1 → 5`; `q=2,n=3 → 35`; `q=4,n=2 → 33` | `m = 2`, `t = 1` | `[EXH]` except `q=9,n=4` `[SMP]` |
| C2 | CRT+Morita prediction of the **dimension distribution** at `q=2,n=3` (and its exact match) | one case | `[EXH]` |
| C3 | Right ideals of `M_2(F_q)`: `5, 7, 11, 12 = q+3` for `q = 2,4,8,9` | `m=2,t=1` | `[EXH]` |
| C4 | `t = 2` census: **33** right ideals of `M_2(F_4[u]/⟨u²⟩)`, dims `[(0,1),(2,5),(4,21),(6,5),(8,1)]`, all checks 33/33 | one case | `[EXH]` (+ structural formula `q²+3q+5`) |
| C5 | Squarefree-hypothesis counterexample: `q=4,n=2` has 33 codes, the squarefree formula predicts 49 | one case | `[EXH]` |
| C6 | Hull-dimension distributions (`q=4,n=3`: `0:64,2:144,4:108,6:27`; `q=9,n=2`: LCD 64, self-orthogonal 25, self-dual 16; `q=8,n=3,s=1,2`: LCD 640, self-orthogonal 8, self-dual 3; `q=27,n=1`: LCD 30, self-dual 0) | `m=2,t=1` | `[EXH]` |
| C7 | Reflexive-code counts: 343/343, 144/144, 5000/5000 `[SMP]` versus **35/737** (`q=8`) and **6/30** (`q=27`) | `m=2,t=1` | `[EXH]` (+ Galois-descent derivation) |
| C8 | `dim Hull(C^⊥) = dim Hull(C)` for **1 254/1 254** codes, both regimes | 4 parameter sets | `[EXH]` |
| C9 | `{σ_s-Hermitian Gram} = {σ_{2s}-invariant}` as **sets**, in all four parameter sets | 4 parameter sets | `[EXH]` |
| C10 | `M_2(F_2)`, `n = 3`: 3 self-dual codes exhibited; quaternary family: 8 codes, none self-orthogonal; A1's form `Σ x_j y_j` degenerate | one case | `[EXH]` |
| C11 | Plain-product control: size formula fails 8/343, 4/737, 4/144, 2/1200, 3/33 | `m=2,t=1,2` | `[EXH]` |

### D. [TOP] Still requiring a theoretical proof

| # | Item | Why it matters | Risk if left open |
|---|---|---|---|
| O1 | **T-012**: a Gray/Bachoc-type map `Φ` with a precise duality relation | the entire Phase 6 depends on it | highest (R3) |
| O2 | **T-013/T-014**: CSS/EA constructions and parameter formulas over a non-commutative alphabet | the "quantum" half of the title | high |
| O3 | **T-011**: hull-dimension formulas for meaningful families (we have distributions, no formula) | the difference between a census and a theorem | medium |
| O4 | **T-021**: principality at `t ≥ 2` or `p ∣ n` | no later phase may assume it | medium |
| O5 | Converse of C9 (Hermitian Gram ⇐ reflexive): verified, not proved | a remark, not load-bearing | low |
| O6 | `dim Hull(C^⊥) = dim Hull(C)` (C8): verified 1 254/1 254, proof not yet written | makes LCD behave identically in both regimes | low |
| O7 | MacWilliams identities for the θ_s-dual: need to check whether Szabo–Wood's hypotheses cover a **non-involutive** anti-automorphism | must not be claimed before checked | medium |
| O8 | Generalisation to `m ≥ 3` and `t ≥ 3`: no experiments yet | scope of the claims | low |

---

## 2. The six additional references versus our contributions

| Ref | What it already does | What we add on top | Verdict |
|---|---|---|---|
| **Wood 2010** (P1) | anti-isomorphism ⇒ duality + self-dual codes over non-commutative rings, general theory, various examples | the **explicit family** `θ_s = σ_s ∘ transpose` on `M_m(F_q[u]/⟨u^t⟩)`, the twist `σ_{2s}`, the criterion `r ∣ 2s`, and cyclic codes/matrix rings — none of which is in the abstract | **Overlap at the level of the idea; no overlap at the level of our statements.** Must be credited as the source of the idea. |
| **Szabo–Wood 2017** (P2) | general properties (module, double-dual, cardinality, MacWilliams) for non-degenerate forms over a Frobenius ring | the *twisted* double-dual `σ_{2s}(C)` (their statements appear to be in a hermitian/involutive setting — **to be checked, O7**), and all the explicit enumeration | **Our duality properties are a special case of their framework.** Credit; claim only the twist and the explicit identification. |
| **NRS 2006** (P3) | form rings/types, non-commutative examples, genus-`m` enumerators | our `θ_s`-forms as an explicit *type* on `M_m(A_t)`; the cyclic-code censuses | Complementary. Cite as the theoretical home. |
| **Dougherty–Leroy 2016** (P4) | left/right orthogonals over non-commutative Frobenius rings | we work with **right** modules and a *Galois-twisted* form; their left/right equivalence is the commutative of our right-module choice | Directly relevant to the (U8) convention question. Cite. |
| **Solé, MMS 2011** (P5) | **cyclic self-dual codes over `M_2(F_2)`** — the same alphabet, the same structure (cyclic + duality) | Galois twist (`s > 0`), hulls rather than self-duality, the `r ∣ 2s` phenomenon, the censuses, quantum | **The closest predecessor on our alphabet.** Cite prominently and differentiate: no Galois action (`F_2`, `F_2[i]`), no hulls, no quantum. |
| **Kushwaha–Prakash 2025/26** (P6) | hulls (left/right/two-sided) over a non-commutative, **non-unital** ring | our ring is unital, is a matrix ring over a local ring, and carries a **Galois** action and a **cyclic** structure they do not have | Adjacent, disjoint. Cite as evidence of timeliness. |

(Related but not among the six: Oggier–Solé–Belfiore on matrix-ring alphabets for
space-time coding — the alphabet precedent; Zhang–Kong–Zheng 2026 — the closest
"Galois hull → quantum" template, commutative.)

---

## 3. Draft novelty paragraph (DRAFT — for the researcher to edit and approve)

> *Duality for codes over a non-commutative alphabet goes back to Wood's programme of
> endowing a finite ring with an anti-isomorphism and studying the resulting
> character-theoretic duality (Wood 2010; Nebe–Rains–Sloane 2006), and the general
> properties of duals with respect to non-degenerate sesquilinear forms over finite
> Frobenius rings — module structure, double dual, cardinality complementarity,
> MacWilliams identities — are worked out in Szabo and Wood (2017). Self-dual cyclic
> codes over the particular alphabet `M_2(F_2)` were studied by Solé (2011).*
>
> *In this paper we specialise that machinery to the matrix rings
> `R = M_m(F_q[u]/⟨u^t⟩)` and to the explicit one-parameter family of anti-automorphisms
> `θ_s = σ_s ∘ transpose`, where `σ_s` is the coefficient-wise Frobenius. We show that the
> associated pairing `B_s(x,y) = Σ_e θ_s(x_e) y_e` is non-degenerate, that the dual of a
> cyclic code is cyclic, and that the double dual is `σ_{2s}(C)` rather than `C`
> (Theorem …). Consequently the duality is reflexive exactly when `r ∣ 2s` (Theorem …),
> which for odd `r` forces the Galois action to be trivial; the unique non-trivial
> reflexive choice is `r` even with `s = r/2`. We prove that `σ_{2s}` is a semilinear
> isometry, so that even in the non-reflexive regime the size, weight enumerator, minimum
> distance and hull dimension of `C^{⊥⊥}` coincide with those of `C`. We then study the
> Galois hulls `Hull_s(C) = C ∩ C^{⊥_s}` of cyclic codes over `R`, give exhaustive
> censuses of these codes and their hull dimensions for …, and show that the
> squarefree hypothesis in the enumeration formula is essential (a counterexample at
> `q = 4, n = 2`). Finally we construct … (Phase 5–6, conditional on T-012).*

**Claims we must NOT make:**

1. "We introduce duality via an anti-automorphism." (Wood 2010.)
2. "We prove the double-dual property / size formula / MacWilliams identities for forms
   over Frobenius rings." (Szabo–Wood 2017.)
3. "We are the first to study cyclic codes with a duality over `M_2(F_2)`." (Solé 2011.)
4. "We are the first to study hulls over non-commutative rings." (Kushwaha–Prakash.)
5. Any Q1 claim: at Phase 0 the deliverable is an algebra-of-codes paper (Q2) unless and
   until T-012/T-013 produce a Gray map and a new quantum family.

---

## 4. What the researcher is asked to approve

1. The four-way classification of §1 (in particular: **C1–C11 stay labelled
   `[EXH]`/`[SMP]` and are never promoted to theorems**).
2. The draft paragraph of §3 (or an edited version).
3. The six new bibliography entries (P1–P6), plus Oggier–Solé–Belfiore and
   Zhang–Kong–Zheng where relevant.
4. The explicit exclusion of claims 1–5 above.

**Not approved by the audit, and not to be asserted:** anything in box D, and anything
marked "to be checked" (O7 in particular).
