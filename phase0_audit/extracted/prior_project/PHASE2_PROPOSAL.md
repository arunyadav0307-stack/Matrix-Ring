# PHASE 2 — PROPOSAL (structure of cyclic codes over `R_n = M_2(A_t)[X]/⟨X^n−1⟩`)

**Status: PROPOSAL ONLY. Not started. Nothing in this file is a proved result.**

* Every item tagged **[PROPOSED]** is a statement to be *proved or refuted* during Phase 2.
  None of them may be cited as a theorem until a proof exists in this repository and the
  theorem register records it as `proved`.
* Items tagged **[PHASE 1]** are already proved in
  `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` and are used as standing conventions.
* Items tagged **[IMPORTED]** are standard facts cited from the literature; each is
  identified so that its hypotheses can be checked.
* Constraints accepted with this proposal: Phase-1 results are frozen (any correction
  follows the T-042 procedure); the manuscript is not started; Phase-2 execution begins only
  on explicit approval of this proposal.

Standing conventions inherited from Phase 1 (**[PHASE 1]**): `q = p^r` with `r ≥ 2`,
`A_t = F_q[u]/⟨u^t⟩`, `R = M_2(A_t)`, `B = A_t[X]/⟨X^n−1⟩` (commutative),
`R_n = R[X]/⟨X^n−1⟩ ≅ M_2(B)`, `σ_s ∈ Aut(A_t)` the coefficient Frobenius fixing `u`,
`θ_s = σ_s ∘ (·)^T` (anti-automorphism), the pairing `B_s(x,y) = Σ_{e<n} θ_s(x_e)y_e ∈ R`
with `b_s = Λ ∘ B_s`, `Λ = λ ∘ tr`, and the **right**-module convention
`(x·a)_e = x_e a`. Notation: elements of `R_n` are written `u = Σ_e u_e X^e` with
`u_e ∈ R`; the indeterminate is `X`, so a *generator* of a code will be written `g`, never
`X`.

---

## 1. Definition of the objects (precise)

### P-2.D1 — Cyclic code (definition, restated for Phase 2)

The ambient space is `R^n` with the right `R`-module structure `(x·a)_e = x_e a`. A
**cyclic code of length `n` over `R`** is a right ideal of `R_n`; equivalently an
`F_q`-subspace `C ⊆ R^n` such that

1. `x ∈ C, a ∈ R ⇒ x·a ∈ C` (right `R`-submodule), and
2. `x ∈ C ⇒ T x ∈ C`, where `T` is the cyclic shift.

Equivalently: a right `R_n`-submodule of `R_n` under `R^n ≅ R_n`, `x ↦ Σ_e x_e X^e`.
**[PHASE 1]** Definition 5.1 + Lemma 5.3.

Three further equivalent descriptions, all to be made explicit in Phase 2:

* **Morita form.** Under `R_n ≅ M_2(B)`: `C = {M ∈ M_2(B) : every column of M lies in W}`
  for a unique `B`-submodule `W ⊆ B²` (Convention 5.8 **[PHASE 1]**).
* **Hom form.** `C = Hom_B(B², W)` — the maps `B² → B²` with image in `W`.
* **Generator form** (when it exists): `C = g·R_n` for a single `g ∈ R_n` (§5 below).

### P-2.D2 — The cyclic shift

`T : R^n → R^n`, `(Tx)_e := x_{e−1 mod n}`.

---

## 2. The shift action and its compatibility with the module structure

**Proposed Lemma P-2.1 (shift properties).** **[PROPOSED]** For all `n ≥ 1`, `t ≥ 1`:

1. `T` is right `R`-linear: `T(x·a) = (Tx)·a`;
2. `T` is left `R`-linear: `T(a·x) = a·(Tx)`;
3. `T` commutes with `σ_k` and with `θ_s` (both act coordinate-wise on `R^n`):
   `T σ_k = σ_k T`, `T θ_s = θ_s T`;
4. `T^n = id`, and `T` is an `F_q`-linear bijection and a Hamming isometry;
5. `T` is right multiplication by the central element `X` in `R_n`, and also left
   multiplication by `X`;
6. for the pairing: `B_s(x, Ty) = B_s(T^{-1}x, y)` (already **[PHASE 1]**, Lemma 5.6a(5)).

*Proof strategy.* (1)–(3) are index manipulations: `T` permutes coordinates while the
`R`-actions, `σ_k` and `θ_s` act coordinate-wise, so they commute. (4) `T^n = id` is
immediate; `T` preserves the set of nonzero coordinates, hence Hamming weight. (5) In
`R_n`, `(uX)_e = u_{e−1}` because `X` is central and `X^n = 1`; likewise `(Xu)_e = u_{e−1}`.
(6) is the Phase-1 computation. ∎ (to be written out in full in Phase 2)

**Why (1)–(2) matter.** Because `T` is `R`-linear on *both* sides, the cyclicity condition
is unambiguous: "closed under `T`" is a property of the underlying `F_q`-subspace and does
not depend on the choice of right vs. left module convention. The left/right asymmetry
enters only through the pairing (Convention 5.2) — a point to state explicitly in the
manuscript.

**Consequence to be proved (P-2.1').** **[PROPOSED]** The three descriptions "right ideal of
`R_n`", "right `R`-submodule of `R^n` closed under `T`", and "left `R`-submodule of `R^n`
closed under `T`" coincide *as families of subspaces* if and only if every right ideal of
`R_n` is two-sided — i.e. in general they do **not** coincide, and the second is the
definition. (Falsifiable: exhibit a left ideal of `R_n` that is not a right ideal, e.g.
`R_n·E_11` at any `n`.)

---

## 3. The role of centrality of `X`

**Proposed Lemma P-2.2 (what centrality buys).** **[PROPOSED]**

1. `X` is central in `B` (indeed `B` is commutative, being a quotient of `A_t[X]`), hence
   `X·I_2` is central in `M_2(B) = R_n`; therefore left and right multiplication by `X`
   coincide and both equal `T`. *No* skew/Öre structure arises from the indeterminate: the
   only non-commutative ingredient of the paper is the matrix ring and the anti-automorphism
   `θ_s`.
2. `R_n ≅ R ⊗_{F_q} F_q[X]/⟨X^n−1⟩`, so `R_n` is a free `R`-module of rank `n` with
   `R`-basis `1, X, …, X^{n−1}`; `dim_{F_q} R^n = 4tn`.
3. Because `B` is commutative, Morita applies in the strong form used in Convention 5.8:
   right ideals of `M_2(B)` ↔ `B`-submodules of `B²`, and the Chinese Remainder Theorem is
   available over the **centre** `F_q[X]`.
4. `X` central and `X^n = 1` make `T` invertible with `T^n = 1`, so no "skew-constant"
   correction terms appear in the dual (contrast: skew-cyclic codes, where the dual is
   controlled by the Nakayama/Öre twist).

*Proof strategy.* (1)–(2) are immediate from the definitions; (3) is standard Morita plus
CRT for the commutative ring `B`; (4) is Lemma P-2.1(4)–(5).

**Open check (P-2.2*).** **[PROPOSED]** Verify explicitly at `n = 2`, `q = 4`, `t = 2`
(non-squarefree, `p ∣ n`) that `R_n` is *not* a skew-polynomial ring in any natural sense
and that `X` remains central — i.e. that the "wild" phenomena of §5 are caused by the
arithmetic of `B`, not by any failure of centrality.

---

## 4. Matrix-ring cyclic codes and the Morita-module description

**Proposed Theorem P-2.3 (Morita dictionary, quantitative form).** **[PROPOSED]**
The assignment `W ↦ I_W := {M ∈ M_2(B) : every column of M ∈ W}` is a bijection from
`B`-submodules of `B²` onto right ideals of `M_2(B)`, with inverse
`I ↦ W(I) := Σ_{M ∈ I} im(M)`. Moreover:

1. `I_W ≅ Hom_B(B², W) ≅ W ⊕ W` as `B`-modules; hence `dim_{F_q} I_W = 2 dim_{F_q} W` and
   `|I_W| = |W|²`;
2. `I_W` is generated, as a right ideal of `M_2(B)`, by `k` elements **iff** `W` is
   generated, as a `B`-module, by at most `2k` elements; in particular
   `μ(I_W) = ⌈μ_B(W)/2⌉`, where `μ` denotes the minimal number of generators (as a right
   ideal, resp. as a `B`-module);
3. `I_W` is two-sided iff `W` is of the form `J·B² = J ⊕ J` for an ideal `J ⊴ B`.

*Proof strategy.* (1) is the Hom description: `I_W = {M : im M ⊆ W} = Hom_B(B², W)`, and
`Hom_B(B²,W) ≅ W²` because `B²` is free of rank 2. (2) Both directions use that `B²` is
**projective**: `Σ_i X_i M_2(B) = I_{Σ_i im(X_i)}` — "⊆" is clear, and "⊇" holds because any
`B`-linear map `B² → B²` with image inside `Σ_i im(X_i)` lifts through the surjection
`⊕_i X_i : (B²)^k ↠ Σ_i im(X_i)`. Since `im(X_i)` is generated by the two columns of `X_i`,
the claim follows, and `μ_B(W) ≤ 2k` is realised by packing generators into columns.
(3) Standard Morita ([IMPORTED], `E-003`: two-sided ideals of `M_m(B)` are `M_m(J)`).
(1) is partly **[PHASE 1]** (Proposition 2.6 gives `dim I_W = 2 dim W`); the new content is
(2) and (3).

**Proposed Theorem P-2.4 (CRT decomposition).** **[PROPOSED]** Write
`n = p^v n'` with `p ∤ n'` and let `X^{n'} − 1 = ∏_{j=1}^{J} f_j` be the factorisation into
monic irreducibles over `F_q`, `d_j = deg f_j`. Then `X^n − 1 = ∏_j f_j^{p^v}` and, by CRT
together with Hensel lifting to `A_t`,

$$B \;\cong\; \prod_{j=1}^{J} B_j,\qquad B_j := A_t[X]/\langle F_j^{p^v}\rangle ,$$

where `F_j` is the Hensel lift of `f_j`; `B_j` is local with maximal ideal
`m_j = (u, F_j)`, residue field `K_j := F_{q^{d_j}}`, `F_q`-basis
`{u^a X^b : 0 ≤ a < t, 0 ≤ b < d_j p^v}`, hence `dim_{F_q} B_j = t d_j p^v` and
`|B_j| = q^{t d_j p^v}`. Consequently

$$C \;\longleftrightarrow\; (W_1,\dots,W_J),\qquad W_j \subseteq B_j^2\ \text{a}\ B_j\text{-submodule},$$

with `dim_{F_q} C = 2 Σ_j dim_{F_q} W_j` and `μ_B(W) = max_j μ_{B_j}(W_j)`.

*Proof strategy.* `X^n − 1 = (X^{n'} − 1)^{p^v} = ∏_j f_j^{p^v}` in `F_q[X]`; lift the
pairwise coprime monic factors `f_j^{p^v}` to monic polynomials `F_j^{p^v}` in `A_t[X]`
(Hensel, valid because `A_t` is finite local, hence complete for the `(u)`-adic topology),
and apply CRT to the coprime ideals `⟨F_j^{p^v}⟩`. `B_j` is local: `A_t[X]/⟨F_j^{e}⟩` has
the unique maximal ideal `(u, F_j)` (the quotient by it is `F_q[X]/⟨f_j⟩ = K_j`), and every
element outside it is a unit. The `F_q`-basis is `{u^a X^b : 0 ≤ a < t, 0 ≤ b < d_j p^v}`,
since `F_j^{p^v}` is monic of degree `d_j p^v` and reduction modulo it gives a normal form
of degree `< d_j p^v` with coefficients in `A_t`; this gives `dim_{F_q} B_j = t d_j p^v`.
Finally submodules of `B²` decompose componentwise under `B = ∏ B_j`, and the minimal
number of generators is the maximum over the components.

**Two regimes.** **[PROPOSED, structural]**

* `p ∤ n` (`v = 0`): each `B_j ≅ A_t[X]/⟨F_j⟩ ≅ F_{q^{d_j}}[u]/⟨u^t⟩ =: A_t^{(d_j)}`, a
  **chain ring** (finite chain ring with residue field `F_{q^{d_j}}`, nilpotency `t`).
* `t = 1`: each `B_j ≅ F_q[X]/⟨f_j^{p^v}⟩`, again a **chain ring** (residue `F_{q^{d_j}}`,
  nilpotency `p^v`).
* `p ∣ n` **and** `t ≥ 2`: `B_j` is local but **not** a chain ring: `m_j/m_j²` has
  `F_{q^{d_j}}`-dimension `2`, so `μ(B_j) = 2` and submodules of `B_j²` may require up to
  `4` generators. This is the "wild" case.

---

## 5. Principality and generator descriptions — exact hypotheses

This is the Phase-2 resolution of **T-021** (currently `proved (conditional)`: `t = 1` and
`X^n − 1` squarefree).

**Proposed Theorem P-2.5 (principality criterion).** **[PROPOSED]** For every right ideal
`I = I_W` of `R_n ≅ M_2(B)`:

* `I` is principal ⟺ `W` is generated by at most `2` elements as a `B`-module;
* `μ(I) = ⌈μ_B(W)/2⌉`; in particular `I` is `2`-generated whenever `μ_B(W) ≤ 4`.

*Proof strategy.* Theorem P-2.3(2) with `k = 1`; the second clause is the same identity.
**The uniform bound `μ_B(W) ≤ 4` is NOT claimed here.** It is automatic in the chain-ring
cases (every submodule of `S²` is `≅ u^aS ⊕ u^bS`, hence `2`-generated, so `μ(I) = 1`), and
it is *verified* for the model wild ring `K[u,ε]/⟨u,ε⟩²` (there `m² = 0`, so every
`B`-submodule `W ⊆ B²` is a `K`-subspace of `mB² = m ⊕ m`, of `K`-dimension `≤ 4`, and
`μ_B(W) = dim_K W` by Nakayama). Whether `μ_B(W) ≤ 4` holds for **every** local factor
`A_t[X]/⟨F^{e}⟩` is open — **O-2.2**; the proof strategy is Nakayama plus an explicit
description of submodules of `B_j²`, to be obtained in Phase 2.

**Proposed Theorem P-2.6 (exact boundary for principality; resolves T-021).** **[PROPOSED]**

> Every right ideal of `R_n` is principal ⟺ `p ∤ n` **or** `t = 1`.
> Equivalently: a non-principal right ideal exists ⟺ `p ∣ n` and `t ≥ 2`.

*Proof strategy.*
(⇐) In both listed cases every `B_j` is a chain ring (P-2.4). Over a chain ring `S` every
submodule of `S²` is of the shape `u^aS ⊕ u^bS` (Smith normal form over the principal ideal
ring `S`), hence `2`-generated; by P-2.3(2) `I_W` is principal. Products preserve
principality (components glue by CRT).
(⇒) If `p ∣ n` and `t ≥ 2`, fix a factor `B_j` with maximal ideal `m_j = (u, F_j)` of
embedding dimension `2` and take `W = m_j ⊕ m_j ⊆ B_j²` (extended by `0` on the other
components). Then `μ_B(W) = dim_{F_{q^{d_j}}}(W/m_jW) = 2·dim(m_j/m_j²) = 4`, so `μ(I_W) = 2`
by P-2.3(2): `I_W` is **not** principal. Concretely `I_W = M_2(m_j)`, i.e. **the Jacobson
radical of the corresponding block of `R_n` is a non-principal right ideal.**

*Falsification test.* If the enumeration CT-1 below finds a principal generator for
`M_2(m)` at `(q,t,n) = (4,2,2)`, Theorem P-2.6 is refuted as stated and the correct
invariant must be recomputed.

**Proposed Theorem P-2.7 (dual of a principal code).** **[PROPOSED]** Let `C = g·R_n` be a
principal cyclic code, `g = Σ_e g_e X^e`, and let `rev(y) := Σ_e y_{−e mod n} X^e`. Then

$$C^{\perp_s} \;=\; \{\,y \in R^n : \theta_s(g)\cdot \mathrm{rev}(y) = 0 \text{ in } R_n\,\}
\;=\; \mathrm{rev}\big(\mathrm{ann}_r^{R_n}(\theta_s(g))\big),$$

where `θ_s(g) = Σ_e θ_s(g_e)X^e`. In Morita terms, `ann_r(θ_s(g))` corresponds to the
`B`-submodule `ker(θ_s(g)) ⊆ B²` (`θ_s(g)` acting on column vectors), so

$$\dim_{F_q} C^{\perp_s} = 2\dim_{F_q}\ker\big(\theta_s(g)\big),\qquad
|C^{\perp_s}| = |\ker \theta_s(g)|^2 .$$

*Proof strategy.* Compute, for `M ∈ R_n`,
`B_s(gM, y) = Σ_e θ_s((gM)_e) y_e = Σ_b θ_s(M_b) z_b = B_s(M, z)` with
`z_b := Σ_a θ_s(g_a) y_{a+b}`; this uses only `θ_s(M_b g_a) = θ_s(g_a)θ_s(M_b)` (anti) and
associativity. Hence `y ∈ C^{⊥_s} ⟺ B_s(M, z) = 0 ∀M ⟺ z = 0` (trivial right radical of
`B_s`, **[PHASE 1]** Theorem 6.6). Finally `z = 0 ⟺ θ_s(g)·rev(y) = 0` by the index
substitution `k = −b`. The Morita translation: `θ_s(g)·w = 0` in `M_2(B)` means every column
of `w` lies in `ker(θ_s(g))`, so the right annihilator is `I_{ker θ_s(g)}`.

**Consistency checks (must hold, or the statement is wrong).** **[PROPOSED]**
(i) `|ann_r(θ_s(g))|·|gR_n| = |R_n|` — the standard finite-Frobenius-ring identity
(`R_n` is Frobenius: **[IMPORTED]** Wood 1999 via `T-001`, plus `M_2(B)` Frobenius when `B`
is), which must agree with the Phase-1 size formula `|C|·|C^{⊥_s}| = |R|^n`.
(ii) For `t = 1`, `p ∤ n`, `θ_s(g)` is a matrix over a product of fields and
`dim ker θ_s(g) = dim B² − rank θ_s(g)` with `rank θ_s(g) = rank g` (transpose and
`σ_s` preserve rank), recovering `dim C + dim C^{⊥_s} = 4tn`.
(iii) In the wild case (`p ∣ n`, `t ≥ 2`) `ker θ_s(g)` need not be a direct summand of `B²`;
whether it always is, is **open (O-2.5)**.

**Proposed Corollary P-2.8 (generator of the dual).** **[PROPOSED]** If `p ∤ n` or `t = 1`
(so that every right ideal is principal, P-2.6) then `C^{⊥_s} = h·R_n` where `h` is any
generator of `rev(ann_r(θ_s(g)))`; an explicit `h` in terms of `g` (an analogue of the
classical "reciprocal polynomial" generator `h(x) = (x^n−1)/g*(x)`) is to be derived, first
in the semisimple case `t = 1`, `p ∤ n`, where `B` is a product of fields and the
description reduces to linear algebra over the fields `F_{q^{d_j}}`.

---

## 6. Open problems Phase 2 must address

| ID | Problem | Why it matters | Test |
|---|---|---|---|
| **O-2.1** | Prove or refute P-2.6 (principality ⟺ `p ∤ n` or `t = 1`); if refuted, find the right invariant | closes **T-021**, which blocks any "generator polynomial" theory | CT-1 |
| **O-2.2** | Count/ classify `B`-submodules of `B²` in the wild case (`p ∣ n`, `t ≥ 2`), where no Smith normal form is available; in particular decide whether `μ_B(W) ≤ 4` for every submodule (so that every right ideal of `R_n` is `2`-generated) | needed for any enumeration or census in the wild regime, and for the uniform bound in P-2.5 | CT-1, CT-5 |
| **O-2.3** | Extend the enumeration formula (Convention 5.8 / T-018) from `t = 1` to all `t`, via `N(t,Q) := #{S-submodules of S²}` for `S` a chain ring with residue field of size `Q` and nilpotency `t` | the only route to a code census at `t ≥ 2` | CT-2, CT-3 |
| **O-2.4** | Explicit generator `h` of the dual of a principal code (Corollary P-2.8), and the analogue of "parity-check polynomial" | needed before any syndrome/decoding or hull work | CT-4 |
| **O-2.5** | Is `ker θ_s(g) ⊆ B²` always a direct summand? (equivalently: is `C^{⊥_s}` always "nice"?) | governs whether a generator for the dual can always be chosen idempotently | CT-4, CT-5 |
| **O-2.6** | Interaction of `σ_s` with the CRT factors: `σ_s` acts coefficient-wise, hence preserves each `B_j` and induces the Frobenius on the residue field `F_{q^{d_j}}`; describe the induced action on `W_j` and its effect on reflexivity (`r ∣ 2s`) and on the per-code rescue (Theorem 7.4) | connects the Galois datum to the code decomposition; needed for regime statements | CT-6 |
| **O-2.7** | The `n = 1` boundary: at `n = 1`, `B = A_t` and the theory must degenerate to the ideal theory of `M_2(A_t)` (`q+3` / `q²+3q+5` right ideals, all principal) | sanity anchor for every formula | CT-3 (`n = 1`) |
| **Carried forward (not Phase-2 tasks)** | **T-006** (entry-wise form failure, uncharacterised), **T-027** (general `τ ∈ Aut(A_t)` undeveloped), hull-dimension formulas (Phase 4), Gray map (Phase 5), quantum construction (Phase 6, with warning B3.5) | recorded in `PHASE1_COMPLETION_AND_APPROVAL_GATE.md` §5 and re-stated here by decision **D3** | — |

---

## 7. Computational test cases

All are *predictions of the proposals above* — a mismatch refutes the corresponding
proposal, which is the point. Conventions: exhaustive enumerations are labelled `[EXH]`,
uniformly seeded samples `[SMP]`, with seeds recorded in the log; the scripts are to be
added under `04_COMPUTATION/` and must import the Phase-1 arithmetic
(`ring_structure_checks.py`) unchanged.

**CT-1 — principality boundary (`O-2.1`).**
Enumerate all `B`-submodules of `B²` by breadth-first closure under `B` (generators: `X` and
`u`) and compute `μ_B(W)` for each; count principal (`μ_B(W) ≤ 2`) versus non-principal
right ideals.

| `(q,t,n)` | `B` | Prediction (P-2.6) |
|---|---|---|
| `(4,1,1)` | `F_4` | all principal (`7` codes) |
| `(4,1,2)` | `F_4[ε]/⟨ε²⟩` chain | all principal (`33` codes) — `t = 1` |
| `(4,2,1)` | `A_2` chain | all principal (`33` codes) — `p ∤ n` |
| `(4,2,2)` | `F_4[u,ε]/⟨u²,ε²⟩`, `m = (u,ε)`, `|B| = 256`, `|B²| = 4^8` | **non-principal right ideals exist**; `W = m ⊕ m` (`dim_{F_4} W/mW = 4`) gives `I_W = M_2(m)` with `μ = 2` |
| `(9,2,3)` | `p = 3 ∣ n`, `t = 2` | **non-principal right ideals exist** |
| `(4,2,3)` | `p ∤ n` | all principal |

**CT-2 — submodule counts over a chain ring (`O-2.3`).** Let `N(t,Q)` be the number of
`S`-submodules of `S²` for `S = F_Q[u]/⟨u^t⟩`. Known: `N(1,Q) = Q+3`
(`1 + (Q+1) + 1`), `N(2,Q) = Q²+3Q+5` (**[PHASE 1]**, Corollary 2.7).

> **Conjecture C-2.1 (UNPROVED — to be proved or refuted).** For `0 ≤ a ≤ b ≤ t`, the number
> of submodules of shape `S/u^a ⊕ S/u^b` is `1` if `a = b` and `Q^{b−a−1}(Q+1)` if `a < b`;
> hence
> $$N(t,Q) = (t+1) + (Q+1)\sum_{d=1}^{t}(t+1-d)\,Q^{d-1},$$
> giving `N(3,Q) = Q³+3Q²+5Q+7`, i.e. `N(3,4) = 139`, `N(2,2) = 15`, `N(3,2) = 37`,
> `N(4,2) = 83`.

Test by exhaustive BFS: `(Q,t) = (2,2) [|S²| = 16]`, `(2,3) [64]`, `(2,4) [256]`,
`(4,2) [256]`, `(4,3) [4096]`, `(9,2) [6561]`. A single mismatch invalidates C-2.1 and the
shape counts must be recomputed.

**CT-3 — cyclic-code census at `t ≥ 2` (`O-2.3`, `O-2.7`).** Prediction from P-2.4 + C-2.1:
for `p ∤ n`, `#{cyclic codes} = ∏_j N(t, q^{d_j})`.

| `(q,t,n)` | factorisation of `X^{n'}−1` | prediction |
|---|---|---|
| `(4,2,1)` | `X−1`, `d = 1` | `N(2,4) = 33` (matches **[PHASE 1]**) |
| `(9,2,1)` | `X−1` | `N(2,9) = 113` (**new**) |
| `(4,2,3)` | `X³−1 = ∏_{ω³=1}(X−ω)`, three factors `d_j = 1` | `N(2,4)³ = 35 937` (**new**) |
| `(4,3,1)` | `X−1` | `N(3,4) = 139` (**new**) |

Because `35 937` exceeds comfortable exhaustive listing, the census at `(4,2,3)` is to be
verified **structurally** (product of independently enumerated submodule lattices), and a
`[SMP]` cross-check should confirm that independently generated cyclic codes (`T`-stable
right submodules obtained by closure of random seeds) all lie in the enumerated family.

**CT-4 — dual of a principal code (`O-2.4`, `O-2.5`).** For every principal cyclic code
`C = gR_n` at `(q,t,n) = (4,1,3)` (`343` codes), `(9,1,2)` (`144`), `(4,2,1)` (`33`),
`(4,1,2)` (`33`): verify `C^{⊥_s} = rev(ann_r(θ_s(g)))` against the orthogonal computed
from the Phase-1 linear-algebra routine; verify `|C^{⊥_s}| = |ker θ_s(g)|²`; and verify
`dim C + dim C^{⊥_s} = 4tn`. Also record, per code, whether `ker θ_s(g)` is a direct summand
of `B²` (O-2.5).

**CT-5 — the wild case (`O-2.2`).** At `(q,t,n) = (4,2,2)` and `(4,2,4)` (`p = 2 ∣ n`,
`t = 2`): enumerate all `B`-submodules of `B²`; report the distribution of `μ_B(W)`, the
number of principal right ideals, the total count (to be compared with the squarefree
prediction `N(2,4)^{?}`, which does **not** apply — cf. the Phase-1 datum `33 ≠ 49` at
`q = 4, n = 2`, `t = 1`), and whether the count factorises over the factors of `X^n − 1`.

**CT-6 — Galois action on the CRT components (`O-2.6`).** At `(q,t,n) = (4,1,3)` and
`(16,1,3)`: describe the permutation/Frobenius action induced by `σ_s` on the components
`W_j`, and count `σ_{2s}`-invariant codes (the Phase-1 per-code rescue, Theorem 7.4); check
the prediction that `σ_{2s}`-invariance is exactly "descended from the fixed field of
`σ_{2s}`".

**Regression requirement.** Every new script must first re-run and reproduce the Phase-1
logs (`401/401` and `276/276`, byte-identical) before producing new output, so that no
Phase-2 change silently alters a Phase-1 result.

---

## 8. Out of scope for Phase 2 (explicitly)

* Hull-dimension **formulas** and self-dual/self-orthogonal code constructions — Phase 4
  (Phase 2 may compute hull *data* only if it is needed to test a structural claim).
* Gray maps, Lee/Hamming isometry statements, weight enumerators — Phase 5.
* Quantum (CSS/EA) constructions — Phase 6, and only under warning B3.5.
* Any change to the Phase-1 conventions (right-module convention, Morita column convention,
  pairing, regimes) — frozen by decision **D1**.
* Manuscript writing — not started.

---

## 9. Deliverables and acceptance criteria for Phase 2

1. A Phase-2 document `03_THEOREMS/CYCLIC_CODE_STRUCTURE.md` containing proofs of P-2.1,
   P-2.2, P-2.3, P-2.4, P-2.5, P-2.6, P-2.7, P-2.8 — **or** their refutations, with the
   corrected statements. Nothing may be recorded in the register as `proved` without a
   complete proof in that file.
2. New scripts + logs under `04_COMPUTATION/` for CT-1 … CT-6, each labelled `[EXH]`/`[SMP]`,
   plus the mandatory Phase-1 regression run.
3. Register rows `T-044 …` for whatever is proved or refuted, including an updated row for
   **T-021** (principality) that states the exact hypothesis, and a row for C-2.1 recording
   whether it was proved or refuted.
4. An honest list of whatever remains open, carried forward under decision **D3**.

**Approval requested.** Phase 2 will begin only on explicit approval of this proposal
(including the parameter tables of §7 and the scope limits of §8).
