# Phase 11 / Task D — Manuscript positioning

Purpose: to frame the paper honestly for FFA. Every statement below is checked
against the manuscript. **Nothing is inflated.**

## D1. Quantum parameters — the honest framing

The temptation is to lead with the largest number in the paper. That number is
`d = 10`, from an entanglement-assisted code, and leading with it would be
misleading.

### What the manuscript actually obtains

| family | best codes | relation to the literature |
|---|---|---|
| Stabilizer | `[[24,8,4]]_9`, `[[20,4,4]]_4` | **All** stabilizer codes with `d ≥ 3` are **1–2 below** the best known distances in Grassl's tables. At `d = 2` the codes are at best **equal** to the best known, never better. |
| Entanglement-assisted | `[[20,2,10;18]]_4`, `[[24,2,10;18]]_9` | **Cannot be benchmarked at all** — no EA table exists (codetables.de has no EA table; the URL 404s). |
| Codes over `F_8` | several | **Unbenchmarked** — Grassl's tables have no `q = 8` entries. |

### The three errors to avoid

1. **"Improved quantum parameters."** False. No code in this paper beats the
   best known distance.
2. **"Record parameters."** False, and the manuscript says so explicitly in
   §10 ("No record parameter is claimed").
3. **"The EA codes achieve `d = 10`, the largest distances in the paper."**
   True but unusable as a selling point, because `d = 10` is unbenchmarkable
   and, for an EA code with `c = 18` ebits, is not comparable to a stabilizer
   distance at all.

### The framing that is both true and strong

The paper's value is **provenance and exactness, not records**:

> Every parameter reported here is *derived* from an explicitly stated
> algebraic construction and *certified* by three independent methods, with
> the hypotheses visible. The codes are not records; they are codes whose
> origin is a new algebraic mechanism, whose parameters are proved rather than
> asserted, and whose limits are bounded by two new results (the coset-distance
> theorem and the coset Singleton bound `K + d ≤ N + 1`).

This framing survives referee scrutiny because it is checkable. The
record-parameter framing does not, because one lookup in codetables.de
refutes it.

**Status: VERIFIED — consistent with §9, §10 and the Phase 10 scope
assessment.**

## D2. The Morita objection — prepared response

### The objection

> `R_n = R[X]/⟨X^n − 1⟩` with `R = M_2(A_t)` is Morita-equivalent to
> `B = A_t[X]/⟨X^n − 1⟩`, which is **commutative**. Right ideals of `R_n`
> correspond to `B`-submodules of `B²`, and the hull is the ideal
> corresponding to the intersection of the two associated submodules. So what
> does the matrix-ring formulation contribute? Isn't this commutative algebra
> wearing a noncommutative costume?

This is a **real and fair objection** and should be expected in review.

### The response (three parts)

**1. Morita equivalence is an equivalence of module categories, not of rings
with involution — and it does not carry the duality.**

The duality used throughout is defined by the anti-automorphism
`θ_s = σ_s ∘ (·)^T` of `R`. The transpose is what makes the dual of a *right*
ideal a right ideal with the correct size (failure lemma, duality theorem).
Over a commutative coefficient ring the twist degenerates to `σ_s` and there
is nothing to prove. The Galois pairing, the distinction between the general
Galois and the reflexive regime, and the self-orthogonality of hulls **without
reflexivity** are all statements about `R` and `θ_s`, made *before* any Morita
translation. Morita equivalence does not transport an involution.

**2. What Morita *does* give is exactly what it is used for.**

It converts the structure theory of hulls into a computation with submodules
of `B²`. That is precisely how the principality criterion and the
`t ≥ 2` ∧ `p | n` confinement are proved, and how the witnesses are
constructed. **The paper does not claim novelty from the noncommutativity of
`M_2(A_t)` alone.** The novelty claimed is in the duality that the
noncommutative alphabet *forces*, and in the hull phenomena that the
confinement criterion isolates.

**3. After the translation the residual problem is a finite-field problem —
which is why FFA is the right venue.**

`B = F_q[u,X]/⟨u^t, X^n − 1⟩` decomposes by the Chinese remainder theorem,
governed by the **factorisation of `X^n − 1` over `F_q`**. The condition
`p | n` is exactly the **repeated-root** case. This is where the finite-field
content of the paper lives, and it is the strongest answer to any scope
objection: the paper's engine is the structure of a polynomial ring over a
finite field, studied through the noncommutative alphabet it naturally
generates.

### Residual risk

The objection is **mitigated, not eliminated**. FFA is a finite-fields
journal; the alphabet is a finite noncommutative non-chain ring. Mitigation is
supported by FFA Vol 110, which carries chain-ring additive cyclic codes. A
screener could still mis-read the title. This is recorded as a desk-rejection
risk, not as a resolved issue.

**Status: PREPARED — text drafted and inserted into the staging copy as
§2.x "The role of the matrix-ring formulation, and what Morita equivalence
does and does not settle". It compiles cleanly.**

## D3. Contribution hierarchy

Ordered as the authors should present them. The ordering puts the algebra
first deliberately: FFA is an algebra journal, and the quantum payload is an
application.

| rank | contribution | manuscript location | why this rank |
|---|---|---|---|
| **1** | **Galois duality and hull theory over a noncommutative alphabet.** The Galois twist must be the anti-automorphism `θ_s`; duality and hull theory are developed for **arbitrary** right ideals with **no principality hypothesis**; hull self-orthogonality holds with **no reflexivity hypothesis**. | §4, §5 | This is the new mathematics. It is what makes everything else possible and it is where the noncommutativity is load-bearing. It is also the most naturally FFA-shaped contribution. |
| **2** | **Non-principal hull structure, and a counterexample.** Galois hulls need **not** be principal; `MU_B = 3` occurs; `MU_B ≥ 3` forces `t ≥ 2` **and** `p \| n`; no closed formula of gcd type exists. | §5 | A structural **negative** result with a sharp confinement theorem. FFA's "very strict refereeing standards" and its tolerance for nonexistence results make this the second-strongest asset. |
| **3** | **The duality-preserving expansion to `F_q^{4tn}`.** The transported form is identified exactly, with Hankel Gram matrix `I_{4n} ⊗ H_t`; duality and hulls are preserved, **non-principal ones included**. | §6 | Exactness is the point: this is not a Gray map that merely preserves distance, it is one that preserves the duality and the hulls. |
| **4** | **Quantum stabilizer and EA constructions.** Three routes (R1–R3) at `N = 4tn`, with the characteristic-two obstruction delimiting the Euclidean route. | §7 | The application. Real, but it depends on 1–3, and its parameters are not records (see D1). |
| **5** | **Exact distance certificates and two bounds.** The coset-distance theorem (distance = min weight of `D^{⊥_E}/Hull_E(D)`), the coset Singleton bound `K + d ≤ N + 1`, and the triple-method certification of 28 codes. | §8 | Methodological strength and the paper's reproducibility guarantee. |

### What is explicitly *not* claimed as a contribution

* **Improved parameters.** Not available (see D1).
* **Novelty from noncommutativity as such.** Disclaimed in D2.
* **Enumerator statistics and dimension-distribution data.** These are
  **supporting material**, reported where they support a construction and not
  presented as principal results. They should not be promoted into the
  contribution list.

**Status: PREPARED — inserted into the staging copy as §2.x "Contributions, in
order of emphasis" and "On the parameters obtained". Both compile cleanly.**

## D4. Where each piece was placed

| content | file | location |
|---|---|---|
| Morita response | `PAPER/FFA_SUBMISSION_STAGING/sections/01_introduction.tex` | new subsection before "Organisation" |
| Contribution hierarchy | same file | new subsection before "Organisation" |
| Honest parameter framing | same file | new subsection before "Organisation" |

All three were added to the **staging copy only**. The canonical
`PAPER/sections/01_introduction.tex` is unchanged (hash `2442af8c…`).
