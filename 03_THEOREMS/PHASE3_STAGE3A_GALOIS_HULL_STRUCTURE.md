# Phase 3 — Stage 3A: Galois hull structure and dimension theory

**Status of this document.** Stage 3A executes Phase 3 §2–§8 of the approved plan:
the **definition and structure of the Galois hull** (Task A), the **hull formula**
(Task B), **hull dimension theory** by four independent routes (Task C), the **general
versus reflexive Galois regimes** (Task D), the **LCD / self-orthogonal / self-dual
characterisations** (Task E), **computation** (Task F) and a **literature comparison**
(Task G).

Hull **enumeration** (Phase 4), Gray maps (Phase 5) and quantum CSS/EAQECC
constructions and parameter claims (Phase 6) are **out of scope** and are not
attempted. In particular, nothing here claims that a Galois hull produces a quantum
code: the only outward-looking statement recorded is the (unused) identity
`Hull_s(C) = C ∩ rev(ann_r(θ_s(C)))`, logged in §5.4 for later use.

Companion verification: `04_COMPUTATION/phase3_stage3a_hull_structure.py`, log
`04_COMPUTATION/phase3_stage3a_hull_log.txt` — **583 checks, 583 PASS, 0 FAIL**
(117 `[EXH]`, 467 `[SMP]`; seed `20261108`, Python 3.11.2; two consecutive runs
byte-identical; log SHA-256
`478d62ff31f6d95d36731e4a25b8026f7d40bbf030ba39c6113b2427bd9acfe2`, 792 lines,
≈ 45 s per run).

**Status labels.** `PROVED IN PHASE 1`, `PROVED IN PHASE 2` (with the stage named),
`PROVED IN PHASE 3 STAGE 3A`, `IMPORTED RESULT`, `PROPOSED / UNPROVED`, `CONJECTURE`,
`COMPUTATIONALLY VERIFIED ONLY`, `OPEN`. A computation never promotes a statement:
every `PROVED` row rests on the argument written here.

---

## 0. Scope, conventions, and what is carried in

### 0.1 Standing conventions (unchanged)

* `q = p^r`, `A_t = F_q[u]/⟨u^t⟩`, `R = M_2(A_t)`, `X` **central**,
  `R_n = R[X]/⟨X^n−1⟩`, `B = A_t[X]/⟨X^n−1⟩`, `R_n ≅ M_2(B)` (Stage 2A Lemma 1.3).
* **Right-module convention:** a cyclic code is a **right** ideal of `R_n`.
* **Morita column convention:** `P = B²` as columns; `im M` = the `B`-span of the two
  **columns** of `M`; `I_W = {M : im M ⊆ W}`; `W(I) = Σ_{M∈I} im M`.
* `ι : R^n → R_n`, `x ↦ Σ_e x_eX^e`; `σ_s(a) = a^{p^s}` extended by fixing `u` and `X`;
  `θ_s = σ_s ∘ (·)^T`; `rev(x)_e = x_{−e mod n}`.
* `B_s(x,y) = Σ_e θ_s(x_e)y_e ∈ R`, `b_s = Λ ∘ B_s`; `C^{⊥_s} = {y : B_s(C,y) = 0}`.
* `ann_r(I) = {a : xa = 0 ∀x ∈ I}`, `ann_l(I) = {a : ax = 0 ∀x ∈ I}` (Stage 2C §2.1).

### 0.2 Results imported into Stage 3A

| Ref | Statement | Where | Status |
|---|---|---|---|
| **T-007** | `b_s` has trivial **right** radical; `|C|·|C^{⊥_s}| = |R|^n`; `dim_{F_q} C + dim_{F_q} C^{⊥_s} = 4tn` | RGF Thm 6.6 | `PROVED IN PHASE 1` |
| **T-016** | `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` | RGF Thm 6.8 | `PROVED IN PHASE 1` |
| **T-017** | `C ↦ C^{⊥_s}` is reflexive ⟺ `r ∣ 2s` | RGF Cor 6.9 | `PROVED IN PHASE 1` |
| **T-010** | `B_s` and `b_s` define the same orthogonal | RGF Lemma 6.7 | `PROVED IN PHASE 1` |
| **Lemma 6.10** | `Hull_s(C)` is a right `R_n`-submodule; `Hull_s(σ_kC) = σ_kHull_s(C)` | RGF Lemma 6.10 | `PROVED IN PHASE 1` |
| **Lemma 6.11** | `B_s(σ_kx,σ_ky) = σ_k B_s(x,y)`; `σ_k(C^{⊥_s}) = (σ_kC)^{⊥_s}` | RGF Lemma 6.11 | `PROVED IN PHASE 1` |
| **Cor 6.12** | `σ_{2s}(C)` has the same size, weight enumerator, minimum distance and **hull dimension** as `C` | RGF Cor 6.12 | `PROVED IN PHASE 1` |
| **Thm 7.2** | `b_s(y,x) = σ_s(b_s(x,y))` (σ_s-Hermitian) ⟺ `r ∣ 2s` | RGF Thm 7.2 | `PROVED IN PHASE 1` |
| **T-070** | Morita bijection `W ↦ I_W`; `|I_W| = |W|²`; `I_W ⊆ I_{W'} ⟺ W ⊆ W'` | Stage 2A Thm 2.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-077** | `xR_n = I_{im x}` | Stage 2A Lemma 2.3a | `PROVED IN PHASE 2 STAGE 2A` |
| **T-081** | `μ_{R_n}(I_W) = ⌈μ_B(W)/2⌉` | Stage 2A Thm 3.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-083** | `I_W` is principal ⟺ `μ_B(W) ≤ 2` | Stage 2A Thm 4.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-115 (L-6.1)** | `θ_s` is an anti-automorphism of `R_n` | Stage 2C Thm 1.3 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-125 (P-2.7)** | `C^{⊥_s} = rev(ann_r(θ_s(g)))`; Morita form `ann_r(v) = I_{ker v}` | Stage 2C Thm 3.5 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-126 (P-2.7 gen.)** | `C^{⊥_s} = rev(⋂ᵢ ann_r(θ_s(gᵢ)))` for any right ideal | Stage 2C Thm 3.8 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-128 (L-6.5)** | `|im x| = |im x^T|`; `|xR_n| = |R_nx|` | Stage 2C Cor 3.9 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-131 (P-2.8)** | SNF generator `h` of the dual in the chain-ring regime | Stage 2C Thm 4.2 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-132** | wild counterexample: the dual of a principal code need not be principal | Stage 2C Thm 4.3 | `PROVED IN PHASE 2 STAGE 2C` |
| **T-102/T-103** | SNF over a chain ring; `B_j` is a chain ring ⟺ `t = 1` or `p ∤ n` | Stage 2B Thm 3.3/3.6 | `PROVED IN PHASE 2 STAGE 2B` |
| **T-110** | `σ_k` permutes the CRT components by `ζ ↦ ζ^{p^k}` | Stage 2B Cor 6.2 | `PROVED IN PHASE 2 STAGE 2B` |

**Not used.** No Frobenius property of `B` (the unconfirmed import **L-6.6**) is used
anywhere; Stage 2C already removed that dependency, and Stage 3A inherits the removal.

### 0.3 The four computational routes

Every hull is computed by **four** routes that could disagree, and every dimension by
three:

| Route | Description | Ingredients |
|---|---|---|
| **D** (definition) | `C^{⊥_s}` by `F_q`-linear algebra on `b_s`; hull = intersection of two subspaces | the pairing only |
| **A** (annihilator) | `C^{⊥_s} = rev(ann_r(θ_s(C)))`, annihilators as kernels of the multiplication maps | `θ_s`, `rev`, `ann_r` |
| **M** (Morita) | `Hull = I_{W∩W'}`, `W = Σ im gᵢ`, `W' = ⋂ ker θ_s(rev gᵢ)` | `im`/`ker` on `B²`, columns |
| **N** (numerical) | `dim Hull = 4tn − dim(C+C^{⊥_s}) = dim C − rank ψ_C = 2 dim_{F_q}(W∩W')` | dimensions only |

---

## 1. Task A — the Galois hull: definition, ambient, closure, invariance

### 1.1 Definition and the ambient module

**Definition 1.1.** For a right `R_n`-submodule `C ⊆ R^n` (a cyclic code) and
`0 ≤ s ≤ r−1`:

```
Hull_s(C) := C ∩ C^{⊥_s},      C^{⊥_s} = {y ∈ R^n : B_s(x,y) = 0 for all x ∈ C}.
```

**The ambient module.** The intersection is taken in `R^n` — the same ambient space as
`C`, so no identification is involved. Under `ι : R^n → R_n` (which is an `F_q`-linear
bijection and a ring isomorphism for the convolution product) the hull is carried to

```
ι(Hull_s(C)) = ι(C) ∩ ι(C^{⊥_s}) ⊆ R_n ,
```

because `ι` is a bijection and hence preserves intersections. Both `ι(C)` and
`ι(C^{⊥_s})` are **right ideals** of `R_n` (Stage 1 and Phase 1 Cor 6.4), so the hull
may equivalently be regarded inside `R_n`; we pass between the two pictures with `ι`
and `ι^{-1}` and always say which is meant. Computationally all four routes work in
`R_n`-coordinates; the shift operator is only visible in `R^n`-coordinates.

### 1.2 The correct scalar field (Task C0, proved here)

**Lemma 1.2.** `C^{⊥_s}` and `Hull_s(C)` are `F_q`-subspaces of `R^n`.

*Proof.* `C` is a right `R_n`-submodule, hence closed under right multiplication by
`c·1` for every `c ∈ F_q`, hence an `F_q`-subspace. For the dual: `b_s` is `F_q`-linear
in the **second** slot, because `F_q` is **central** in `R`:

```
B_s(x, yc) = Σ_e θ_s(x_e)(y_e c) = Σ_e (θ_s(x_e)y_e) c = B_s(x,y)·c ,
```

(no twist appears: `c` commutes with everything, and `θ_s(c) = c` is *not* needed since
`c` never passes through `θ_s` here). Hence `y ∈ C^{⊥_s} ⟹ yc ∈ C^{⊥_s}`, so
`C^{⊥_s}` is an `F_q`-subspace, and so is the intersection. Note the contrast with the
**first** slot, where `B_s(xc,y) = σ_s(c)B_s(x,y)` — the form is `σ_s`-semilinear in `x`
and `F_q`-linear in `y`. ∎

Consequently `dim_{F_q}` is defined for `C`, `C^{⊥_s}` and `Hull_s(C)`, and
`dim_{F_p} = r · dim_{F_q}` for each of them (verified directly by an `F_p`-rank
computation, §6). **Every dimension in this document is an `F_q`-dimension unless
`F_p` is named.**

### 1.3 Closure: the hull is a right `R_n`-submodule, a cyclic code, and *not* a left one

**Proposition 1.3 (right-module structure).** `Hull_s(C)` is a right `R_n`-submodule of
`R_n` (under `ι`), i.e. a **cyclic code**; equivalently it is shift-invariant.

*Proof.* `ι(C)` is a right ideal (Stage 1) and `ι(C^{⊥_s})` is a right ideal
(Phase 1 Cor 6.4); the intersection of two right ideals is a right ideal. Shift
invariance in `R^n`-coordinates is `T(Hull) = Hull`, which is the same statement
transported by `ι` (Stage 1 identifies `T` with multiplication by `X`). This is
Phase-1 Lemma 6.10; the argument is repeated so that the statement is not merely
quoted. ∎

**Proposition 1.4 (the hull is not, in general, a left ideal).** There exist `C` and `s`
with `Hull_s(C)` a right ideal that is **not** closed under left multiplication; hence
the hull is not in general a two-sided ideal, and — since `θ_s` carries right ideals to
left ideals — the hull is *not* `θ_s`-stable as a set (§1.5 gives what `θ_s` does do).

*Explicit witness* (exhaustively verified at `(q,t,n) = (4,1,1)`, `s = 0`). Take
`g = [[0,1],[0,1]] ∈ M_2(F_4)`. Then `C = gR_n` has `dim_{F_q} C = 2`, `C` is
self-orthogonal, and

```
Hull_0(C) = C = { [[a,b],[a,b]] : a,b ∈ F_4 }   (matrices with equal rows),
```

a right ideal of size `4² = 16`. With `M = [[1,0],[1,0]] ∈ Hull` and `a = E_11`:

```
M·a = [[1,0],[1,0]] ∈ Hull      but      a·M = [[1,0],[0,0]] ∉ Hull .
```

So the hull is a right ideal and not a left ideal. Over the sampled cases (`s = 0`, `s = 1` — and `s = 2` at `(8,1,2)` — in that order):
`(4,1,1)` 3/3 and 6/6 nonzero hulls, `(4,1,2)` 5/5 and 10/10, `(4,2,1)` 10/10 and
15/15, `(4,2,2)` 8/8 and 11/11, `(4,1,3)` 20/20 and 20/20, `(9,1,2)` 3/3 and 4/4,
`(8,1,2)` 4/4, 1/1 and 3/3, `(4,2,3)` 27/27 and 26/27. Hence **every nonzero hull in
the whole study except one is not a left ideal** — 178 of 179.

### 1.4 Behaviour under `σ_k` (proved in Phase 1, verified here)

**Proposition 1.5.** For every `k`: `Hull_s(σ_kC) = σ_kHull_s(C)`. Consequently the
hull dimension, the size and the weight enumerator of the hull are `σ_k`-invariant.

*Proof.* Phase 1 Lemma 6.11 gives `σ_k(C^{⊥_s}) = (σ_kC)^{⊥_s}`; `σ_k` is a bijection
of `R^n`, so it preserves intersections: `σ_k(C ∩ C^{⊥_s}) = σ_kC ∩ (σ_kC)^{⊥_s}`.
Verified on 12 codes × `r` values of `k` per case. ∎

### 1.5 Behaviour under `θ_s` and `rev` (new in Stage 3A)

**Lemma 1.6 (annihilator side swap).** For every subset `I ⊆ R_n`,
`θ_s(ann_r(I)) = ann_l(θ_s(I))`.

*Proof.* `w ∈ ann_r(I)` ⟺ `xw = 0` for all `x ∈ I` ⟺ `θ_s(w)θ_s(x) = 0` for all `x ∈ I`
(θ_s is an anti-automorphism, Stage 2C Thm 1.3, and `θ_s(0) = 0`) ⟺
`θ_s(w) ∈ ann_l(θ_s(I))`. Since `θ_s` is a bijection on `R_n`, the image of `ann_r(I)`
is exactly `ann_l(θ_s(I))`. ∎

**Theorem 1.7 (θ_s of the hull).** For every right `R_n`-submodule `C`:

```
θ_s( Hull_s(C) )  =  θ_s(C) ∩ rev( ann_l( σ_{2s}(C) ) ) ,
```

which is a **left** ideal of `R_n`. In the principal case `C = gR_n`:

```
θ_s( Hull_s(C) )  =  R_n θ_s(g)  ∩  rev( ann_l( σ_{2s}(g) ) ) .
```

*Proof.* `θ_s` is a bijection, so `θ_s(A ∩ B) = θ_s(A) ∩ θ_s(B)`. By Stage 2C Thm 3.8,
`C^{⊥_s} = rev(ann_r(θ_s(C)))`, hence (using `rev θ_s = θ_s rev`, Stage 2C Prop 3.6(3))

```
θ_s(C^{⊥_s}) = θ_s(rev(ann_r(θ_s(C)))) = rev(θ_s(ann_r(θ_s(C))))
             = rev(ann_l(θ_s(θ_s(C))))  = rev(ann_l(σ_{2s}(C))) ,
```

the third equality by Lemma 1.6 and the fourth by `θ_s² = σ_{2s}` (Stage 2C Lemma 1.6).
`θ_s(C)` is a **left** ideal (`θ_s` is anti) and `rev(ann_l(σ_{2s}C))` is a left ideal
(`rev` is an automorphism and `ann_l` of anything is a left ideal), so the intersection
is a left ideal. For the principal form: `θ_s(gR_n) = R_nθ_s(g)` (because
`θ_s(gm) = θ_s(m)θ_s(g)` and `θ_s(R_n) = R_n`), and `ann_l(σ_{2s}(C)) =
ann_l(σ_{2s}(g))` because `σ_{2s}(C) = σ_{2s}(g)R_n` is a **right** ideal, and taking
`m = 1` shows `ann_l(gR_n) = ann_l(g)`. ∎

**Theorem 1.8 (rev of the hull).** `rev(Hull_s(C)) = rev(C) ∩ ann_r(θ_s(C))`.

*Proof.* `rev` is an automorphism (Stage 2C Prop 3.6(2)), so it preserves
intersections, and `rev(C^{⊥_s}) = rev(rev(ann_r(θ_s(C)))) = ann_r(θ_s(C))` by
`rev² = id`. ∎

Both statements are verified on 12 codes per (case, `s`), each side computed
independently.

### 1.6 The distinctions required by Task A(5)

| Notion | Inner product / form | Our notation | Status |
|---|---|---|---|
| **Galois hull** | `B_s(x,y) = Σ θ_s(x_e)y_e`, `s ≢ 0` and `2s ≢ 0` | `Hull_s(C)` | the object of this stage |
| **Transpose-Euclidean hull** | `B_0(x,y) = Σ x_e^T y_e` | `Hull_0(C)` | `s = 0` **in our family** |
| **Euclidean hull (classical)** | `Σ_e x_e y_e` (no transpose) | — | **not** of the form `B_s`; see below |
| **Hermitian hull** | `Σ_e \bar x_e^T y_e`, `\bar a = a^{√q}` | `Hull_{r/2}(C)` (`r` even) | `s = r/2`, and `r ∣ 2s` |
| **LCD** | `Hull_s(C) = {0}` | | `s`-dependent |
| **self-orthogonal** | `C ⊆ C^{⊥_s}` | | `s`-dependent |
| **self-dual** | `C = C^{⊥_s}` | | `s`-dependent |

**The classical Euclidean form is not in our family.** `θ_s = σ_s ∘ (·)^T` always
contains the transpose, so no value of `s` turns `B_s` into `Σ_e x_e y_e`. Explicitly,
with `x = E_12` and `y = E_21`:

```
B_0(x,y) = Σ x_e^T y_e = E_12^T E_21 = E_21E_21 = 0 ,
Σ_e x_e y_e  = E_12 E_21 = E_11 ≠ 0 .
```

So the Euclidean hull of the literature (defined by `Σ x_e y_e = 0`) is a **different**
notion from `Hull_0`, and the two duals are verified to differ (neg-6). The `s = 0`
member of our family is the **transpose**-Euclidean form; over a commutative alphabet
the transpose is invisible, which is why the distinction does not arise classically and
**does** arise here.

**Hermitian.** For `r` even and `s = r/2`, `θ_s(A) = σ_{r/2}(A^T)` is the
conjugate-transpose, so `Hull_{r/2}` is the Hermitian hull; note `r ∣ 2s` in that case,
so it lies in the **reflexive** regime. More generally, by Phase 1 Thm 7.2, `b_s` is
`σ_s`-Hermitian (`b_s(y,x) = σ_s(b_s(x,y))`) **iff** `r ∣ 2s`; we verify both
directions (Hermitian when `r ∣ 2s`; violations exhibited when `r ∤ 2s` — 51 of 60 random
ambient word pairs at `(8,1,2)`, `s = 1`, and 50 of 60 at `s = 2`).

**Warning.** `LCD`, `self-orthogonal` and `self-dual` are properties of the **pair**
`(C,s)`, not of `C` alone: the census of §6 shows the same code being LCD for one `s`
and not for another, and `dim Hull_s(C)` varying with `s`.

---

## 2. Task B — the hull formula

### 2.1 Principal codes

**Theorem 2.1.** Let `C = gR_n` and `0 ≤ s ≤ r−1`. Under `ι`:

```
Hull_s(C) = gR_n ∩ rev( ann_r( θ_s(g) ) )                                (B1)
          = gR_n ∩ ann_r( θ_s( rev g ) )                                 (B2)
          = I_{ W },   W := im g ∩ ker θ_s(rev g) ⊆ B²                   (B3)
```

and `|Hull_s(C)| = |W|²`, `dim_{F_q} Hull_s(C) = 2 dim_{F_q} W`.

*Proof.* (B1) is the definition of the hull combined with Stage 2C Thm 3.5
(`C^{⊥_s} = rev(ann_r(θ_s(g)))`); both inclusions are immediate: `y ∈ Hull` ⟺ `y ∈ C`
and `y ∈ C^{⊥_s}` ⟺ `y ∈ C` and `y ∈ rev(ann_r(θ_s(g)))`. (B2) is Stage 2C form 2.
For (B3): `C = gR_n = I_{im g}` (Stage 2A L-2.3a) and `C^{⊥_s} = ann_r(v) = I_{ker v}`
with `v = θ_s(rev g)` (Stage 2C Thm 3.5 + `ann_r(v) = {M : im M ⊆ ker v} = I_{ker v}`).
Therefore

```
Hull = I_{im g} ∩ I_{ker v} = {M : im M ⊆ im g and im M ⊆ ker v} = I_{im g ∩ ker v} ,
```

and the size/dimension statements follow from `|I_W| = |W|²` (Stage 2A T-070). ∎

Three remarks that the task asks for explicitly:

1. **Role of the reversal.** `rev` converts the condition `θ_s(g)·rev(y) = 0` (a
   statement about the *reversed* word) into a statement about `y`; equivalently it
   moves from `ann_r(θ_s(g))` to `ann_r(θ_s(rev g))`. It is an **automorphism**, not an
   anti-automorphism (Stage 2C Prop 3.6), which is precisely why `rev` may be moved
   inside `θ_s` and why (B1) and (B2) agree. It is the identity iff `n ≤ 2`, so it is
   load-bearing only for `n ≥ 3` — confirmed: omitting `rev` changes the hull for 20–23
   of 40 codes at `(4,1,3)` and `(4,2,3)`, and for **0** codes at every `n ≤ 2` case
   (where it is provably vacuous; the log says so instead of emitting a tautological
   pass).
2. **Which annihilator.** The **right** annihilator `ann_r`, of the **element**
   `θ_s(g)` (equivalently `θ_s(rev g)`). It is not `ann_l`, and it is not the
   annihilator of the *ideal* `C` (Stage 2C Lemma 2.3: `ann_r(gR_n) ⊊ ann_r(g)` in
   general). Substituting `ann_l` changes the hull for 1–29 of 40 codes per case.
3. **Role of the anti-automorphism.** `θ_s` converts the right ideal `C` into a **left**
   ideal `θ_s(C)`, and a left ideal's right annihilator *is* the intersection of the
   annihilators of its generators (Stage 2C Lemma 2.2) — this is the structural reason a
   single generator suffices. Dropping `θ_s` changes the hull for 1–27 of 40 codes.

### 2.2 Non-principal codes

**Theorem 2.2.** Let `C = Σ_{i=1}^m g_iR_n` be **any** right ideal (not necessarily
principal). Then

```
Hull_s(C) = C ∩ rev( ⋂_{i=1}^m ann_r( θ_s(g_i) ) )                       (B1')
          = I_{ W },   W := ( Σ_i im g_i ) ∩ ( ⋂_i ker θ_s(rev g_i) )     (B3')
```

with `|Hull| = |W|²` and `dim_{F_q} Hull = 2 dim_{F_q} W`.

*Proof.* Stage 2C Thm 3.8 gives `C^{⊥_s} = rev(⋂ᵢ ann_r(θ_s(gᵢ)))`; intersecting with
`C` gives (B1'). For (B3'): `W(C) = Σ_i im g_i` (Stage 2A) and
`W(C^{⊥_s}) = ⋂ᵢ ker θ_s(rev gᵢ)` (Stage 2C §3.8, using
`rev(ker θ_s(g)) = ker θ_s(rev g)` and `rev` distributing over intersections), so
`Hull = I_{W(C)} ∩ I_{W(C^{⊥_s})} = I_{W(C) ∩ W(C^{⊥_s})}` as in Theorem 2.1. ∎

**Justification that the principal formula may not be used in the non-principal case.**
The `m`-generator formula is *not* a formal consequence of the `1`-generator one, and
using `ann_r(θ_s(g_1))` alone is **wrong**: the tests exhibit genuinely non-principal
`2`-generator codes (those with `g_1R_n ⊊ C` and `g_2R_n ⊊ C`) and verify that the
one-generator formula gives a different answer for **all** of them — at 13 of the 17
`(case, s)` pairs, with counts 1/1, 1/1, 2/2, 2/2, 1/1, 1/1, 1/1, 4/4, 8/8, 2/2, 1/1,
8/8 and 8/8 of the genuinely non-principal codes. At the remaining 4 pairs the
omission test is **not exhibited**, because no genuinely non-principal `2`-generator
code appeared in that sample; the log says so rather than passing vacuously. All three
routes (D, A, M) agree on the `m`-generator hull (`15` two-generator codes per pair).

---

## 3. Task C — hull dimension theory

### 3.0 What is and is not available

There is **no** universal closed formula of the classical type (a `gcd` of generator
polynomials) and there cannot be one here, for two structural reasons:

1. **The hull need not be principal** in the wild regime (`p ∣ n`, `t ≥ 2`): by
   Stage 2A Thm 4.1 it is principal iff `μ_B(W) ≤ 2`, and Stage 2C exhibited a dual
   with `μ_B = 4`. A "generator polynomial of the hull" therefore need not exist.
2. **The CRT components are permuted** by the Galois action whenever `τ ≠ id`
   (§3.3), so the hull is *not* determined by the componentwise hulls.

What *is* available, in all regimes, is the **structural formula** (B3)/(B3'), which
reduces the hull to an intersection of two `B`-submodules of `B²` — a finite,
computable object — together with the parity and principality statements below.

### 3.1 C1 — kernel and intersection approach

**Theorem 3.1.** Let `ψ_C : C → Hom_{F_q}(C, F_q)`, `ψ_C(y)(x) = b_s(x,y)`. Then

```
Hull_s(C) = ker ψ_C  and  dim_{F_q} Hull_s(C) = dim_{F_q} C − rank(ψ_C) ,
```

and `rank(ψ_C)` is the rank of the restricted pairing matrix `M_{ij} = b_s(x_i,x_j)`
for any `F_q`-basis `(x_i)` of `C`.

*Proof.* `ψ_C` is `F_q`-linear because `b_s` is `F_q`-linear in the second slot
(Lemma 1.2). Its kernel is `{y ∈ C : b_s(x,y) = 0 ∀x∈C} = C ∩ C^{⊥_s}`. For the matrix
statement: `b_s` is `σ_s`-semilinear in the first slot, so the functional determined by
`x = Σ c_ix_i` is `Σ σ_s(c_i)ψ_C(x_i)`; since `σ_s` is a bijection, the `F_q`-span of
`{ψ_C(x) : x ∈ C}` equals the span of `{ψ_C(x_i)}`, whose dimension is
`rank(b_s(x_i,x_j))`. ∎

**Theorem 3.2 (sum formula).** `dim Hull_s(C) = 4tn − dim_{F_q}(C + C^{⊥_s})`.

*Proof.* Standard: `dim(A∩B) = dim A + dim B − dim(A+B)`, and
`dim C + dim C^{⊥_s} = 4tn` (Phase 1 Thm 6.6). ∎

### 3.2 C2 — Morita approach

**Theorem 3.3 (Morita hull formula).** For every right ideal `C` and every `s`:

```
Hull_s(C) = I_{W∩W'},   W = W(C),  W' = W(C^{⊥_s}),
dim_{F_q} Hull_s(C) = 2 dim_{F_q}(W ∩ W'),   |Hull_s(C)| = |W ∩ W'|² .
```

For a principal `C = gR_n`: `W = im g`, `W' = ker θ_s(rev g)`.

*Proof.* Theorem 2.2. ∎

**Corollary 3.4 (parity and principality).**

1. `dim_{F_q} Hull_s(C)` is **even**, for every `C`, `s` and regime.
2. `Hull_s(C)` is principal ⟺ `μ_B(W ∩ W') ≤ 2`; in particular in the chain-ring
   regime (`p ∤ n` or `t = 1`) `μ_B(W') ≤ 2` always (Stage 2B Thm 3.3) but
   `μ_B(W ∩ W')` must still be computed — it is `≤ 2` in every case observed.

*Verification.* 1. holds on every one of the sampled codes (0 odd dimensions, at all
17 `(case, s)` pairs). 2. is verified by an **exhaustive generator search** inside the
hull (not by `μ`): for each code with `q^{dim hull} ≤ 3000`, every element `x` of the
hull is tested for `xR_n = Hull`. The outcome agrees with `μ_B ≤ 2` on all codes
tested: 15 of the 17 `(case, s)` pairs are enumerated (40 codes each, 38 at
`(4,2,3)`), all principal; the two wild pairs are too large to enumerate and are
skipped with a note. The observed `μ_B(W_hull)` distribution is `{0: ·, 1: ·}` at every
enumerated pair — the hull is either `0` or `B`-free of rank `1` — with a single
exception at `(4,2,3)`, `s = 1`, where one code has `μ_B = 2` (still principal).

### 3.3 C3 — CRT component approach and the Galois permutation

**Setup.** Assume the split regime: `X^n − 1` splits over `F_q` into `n` distinct linear
factors (so `p ∤ n` and `F_q` contains the `n`-th roots of unity `ζ_1,…,ζ_n`), whence
`B ≅ ∏_j A_t` by evaluation at the roots (Stage 2B). Write `M_j` for the `j`-th
component of `M ∈ M_2(B)`; the component ring is `A_t`, i.e. the `n = 1` instance of our
own machinery.

**Theorem 3.5 (the permutation `τ`).** Let `π` and `ρ` be the permutations of the
components induced by `σ_s` and `rev`:

```
π: ζ ↦ ζ^{p^s}   (Stage 2B Cor 6.2),      ρ: ζ ↦ ζ^{−1}   (rev is X ↦ X^{−1}).
```

Then for every right ideal `C` and every component `j`,

```
(C^{⊥_s})_j = ( C_{τ(j)} )^{⊥_s},      τ := π^{−1} ∘ ρ ,
```

characterised by `ζ_{τ(j)}^{p^s} = ζ_j^{−1}`; consequently

```
Hull_s(C)_j = C_j ∩ (C_{τ(j)})^{⊥_s}  and  dim Hull_s(C) = Σ_j dim( C_j ∩ (C_{τ(j)})^{⊥_s} ).
```

Moreover, **in the split regime `τ = id` iff `n ∣ p^s + 1`**, and then (and only then)
the hull decomposes componentwise: `Hull_s(C)_j = Hull_s(C_j)`.

*Proof.* Multiplication is componentwise, so for every `v`, `ann_r(v)_j = ann_r(v_j)`
(stage-2C argument: `(vw)_j = v_jw_j`). By Stage 2C Thm 3.8 and `rev θ_s = θ_s rev`,

```
(C^{⊥_s})_j = [rev(ann_r(θ_s(g)))]_j = (ann_r(θ_s(g)))_{ρ(j)} = ann_r( (θ_s(g))_{ρ(j)} ),
```

and `(θ_s(g))_k = σ_s((g^T)_{π^{−1}(k)})`, so with `k = ρ(j)`:
`(C^{⊥_s})_j = ann_r(σ_s((g_{π^{−1}ρ(j)})^T)) = (C_{τ(j)})^{⊥_s}` — the last equality
because in the component (`n = 1`) `rev` is the identity and the componentwise dual of
`g_kR` is `ann_r(θ_s(g_k))`. Intersecting with `C_j` gives the hull formula, and the
dimension formula follows because `dim_{F_q} M_2(B) = Σ_j dim_{F_q} M_2(A_t)`.
For the criterion: `τ = id` ⟺ `ζ^{p^s} = ζ^{−1}` for every `n`-th root of unity ⟺
`ζ^{p^s+1} = 1` for all such `ζ` ⟺ `n ∣ p^s+1` (the `n`-th roots form a cyclic group of
order `n`). ∎

**This is where the Galois action genuinely permutes components** (Task C3's explicit
question), and it has a visible consequence:

| `(q,t,n)` | `s` | `p^s+1` mod `n` | `τ` | behaviour |
|---|---|---|---|---|
| `(4,1,3)` | 0 | `2 mod 3 ≠ 0` | `[0,2,1]` | **τ ≠ id** — the naive componentwise formula `Σ_j dim Hull_s(C_j)` **fails** for 9 of 20 codes |
| `(4,1,3)` | 1 | `3 mod 3 = 0` | `[0,1,2]` | τ = id — decomposes |
| `(4,2,3)` | 0 | `2 mod 3 ≠ 0` | `[0,2,1]` | **τ ≠ id** — fails for 1 of 20 codes |
| `(4,2,3)` | 1 | `3 mod 3 = 0` | `[0,1,2]` | τ = id — decomposes |
| `(9,1,2)` | 0,1 | `2,4 ≡ 0 mod 2` | `[0,1]` | τ = id — decomposes |
| `(4,1,1)`, `(4,2,1)` | 0,1 | `n = 1` | `[0]` | τ = id — decomposes |

**Explicit counterexample to the naive formula** (`(4,1,3)`, `s = 0`). For

```
g = ( 2+X        3+2X² ;  1+2X+2X²   1+X+X² )        (entries in F_4[X]/⟨X³−1⟩),
```

one has `dim_{F_q} Hull_0(C) = 2` while `Σ_j dim_{F_q} Hull_0(C_j) = 0` (each component
is LCD). The hull is **invisible** componentwise: it lives in the interaction between
components `1` and `2` that `τ` swaps.

**Chain regime.** When `B` is a chain ring (`t = 1`, or `p ∤ n` with a single
component) the CRT decomposition is **trivial** and the component analysis carries no
information; we say so rather than testing a tautology. The chain-ring route is the
Smith normal form (§3.5).

**Wild regime.** No component decomposition exists at all — this is recorded as a
genuine limitation, not as an untested case.

### 3.4 C4 — generator/matrix approach (principal case)

**Theorem 3.6.** For `C = gR_n`, with `v := θ_s(rev g) ∈ M_2(B)`:

```
Hull_s(C) = { M ∈ M_2(B) : im M ⊆ im g ∩ ker v } = I_{im g ∩ ker v} ,
dim_{F_q} Hull = 2 dim_{F_q}(im g ∩ ker v),
```

computable from the two matrices `g` and `v` by two kernel/image computations and one
intersection over `F_q`. Principality criterion: `μ_B(im g ∩ ker v) ≤ 2`.

*Proof.* Theorem 2.1 (B3). Note `im g` is generated by the two **columns** of `g`, so
no generator matrix in any other sense is used, and none is assumed to exist. ∎

### 3.5 C5 — Smith normal form (chain-ring regimes only)

**Theorem 3.7.** Assume `p ∤ n` or `t = 1` (chain-ring regime, Stage 2B Thm 3.6). Let
`h` be the Stage-2C P-2.8 generator of `C^{⊥_s}` (`h_j = V_j^{-1}diag(ω^{ℓ−a},ω^{ℓ−b})`,
assembled by CRT). Then

```
Hull_s(C) = gR_n ∩ hR_n .
```

*Proof.* `C = gR_n` and `C^{⊥_s} = hR_n` (Stage 2C Thm 4.2); intersect. ∎

Verified on 15 codes per (case, `s`) in every chain-ring case. **Not extended to the
wild regime**, where no Smith normal form exists; there the Morita route (Theorem 3.3)
and, when `μ_B ≤ 2`, the Nakayama generator are used instead.

### 3.6 The wild regime: what is lost

At `(q,t,n) = (4,2,2)` (`B = F_4[u,ε]/⟨u²,ε²⟩`, local, not a chain ring):

* no CRT decomposition, no SNF — stated, not silently skipped;
* `μ_B(W')` can be `4` (Stage 2C's `g = diag(uε,uε)`, where `ker v = m ⊕ m`), so the
  **dual** of a principal code can be non-principal;
* for the **hull** specifically, over `120` sampled wild codes the largest
  `μ_B(W ∩ W')` found was `2`, so no non-principal hull was exhibited. We do **not**
  claim the hull is always principal in the wild regime: `W ∩ W'` is a submodule of the
  `2`-generated module `im g`, and over a non-chain local ring a submodule can require
  more generators than its ambient module (as `m ⊕ m ⊆ B²` shows). Whether
  `μ_B(W_hull) ≤ 2` always is recorded as **O-3.1 (OPEN)**.

---

## 4. Task D — general Galois regime versus reflexive regime (hybrid regime B3)

Throughout, `D := C^{⊥_s}` and `d := 4tn`.

### 4.1 Valid for every `s` (no reflexivity)

**Theorem 4.1.** For every right `R_n`-submodule `C`, every `s`, and with
`D := C^{⊥_s}`:

1. `Hull_s(D) = D ∩ σ_{2s}(C) = (C + D)^{⊥_s}`;
2. `Hull_s(σ_{2s}C) = σ_{2s}Hull_s(C)`, hence
   `dim Hull_s(σ_{2s}C) = dim Hull_s(C)` (Phase-1 Cor 6.12, re-derived);
3. `dim Hull_s(C) = 4tn − dim(C + D)` and `dim Hull_s(D) = 4tn − dim(D + σ_{2s}C)`.

*Proof.* (1) `Hull(D) = D ∩ D^{⊥_s}` and `D^{⊥_s} = σ_{2s}(C)` (Phase 1 Thm 6.8); and
`(C+D)^{⊥_s} = C^{⊥_s} ∩ D^{⊥_s} = D ∩ σ_{2s}(C)`.

(2) `σ_{2s}(C ∩ D) = σ_{2s}C ∩ σ_{2s}D = σ_{2s}C ∩ (σ_{2s}C)^{⊥_s} = Hull(σ_{2s}C)`,
using `σ_k(C^{⊥_s}) = (σ_kC)^{⊥_s}` (Phase 1 Lemma 6.11).

(3) `dim(A∩B) = dim A + dim B − dim(A+B)` with `dim C + dim D = 4tn`. ∎

**Two cautions.** First, `Hull_s(σ_{2s}C)` and `Hull_s(C^{⊥_s})` are **different**
objects: the first is `σ_{2s}(C) ∩ (σ_{2s}C)^{⊥_s}`, the second is `D ∩ σ_{2s}(C)`.
The dimension invariance of Cor 6.12 concerns the **first**. Secondly, and this is a
correction to an earlier draft of this section, the equality

> `dim Hull_s(C^{⊥_s}) = dim Hull_s(C)`

is **not** a formal consequence of (1)–(3): by (3) it is *equivalent* to
`dim(D + σ_{2s}C) = dim(D + C)`, and an earlier attempted proof of that identity
conflated `D = C^{⊥_s}` with `σ_{2s}(D) = (σ_{2s}C)^{⊥_s}`. It is therefore recorded
as a conjecture (§4.2), not as a theorem.

### 4.2 Conjectures in the non-reflexive regime

> **Conjecture H-3A.2.** For every `C` and `s`,
> `dim_{F_q} Hull_s(C^{⊥_s}) = dim_{F_q} Hull_s(C)`; equivalently (by Theorem 4.1(3))
> `dim(C^{⊥_s} + σ_{2s}C) = dim(C^{⊥_s} + C)`.

Status: **CONJECTURE**. Verified at all 17 `(case, s)` pairs on the 40-code samples
(680 codes) and, in the non-reflexive regime, on the 64 nonzero hulls of the dedicated
probes plus 4 more from the `(8,1,2)` samples: **0 violations**. No proof is offered.
Note that H-3A.1 (§4.3 below) implies only the
inequality `dim Hull_s(C^{⊥_s}) ≥ dim Hull_s(C)`, since `Hull(C) ⊆ σ_{2s}C` gives
`Hull(C) ⊆ D ∩ σ_{2s}C = Hull(D)`.

### 4.3 Requires the reflexive regime `r ∣ 2s`

**Theorem 4.3.** If `r ∣ 2s` then `σ_{2s} = id` and `Hull_s(C^{⊥_s}) = Hull_s(C)` as
subspaces (not merely with equal dimension).

*Proof.* `Hull(D) = D ∩ σ_{2s}(C) = D ∩ C = Hull(C)`. ∎

**The converse direction is where the subtlety lies.** When `r ∤ 2s`,
`Hull(D) = D ∩ σ_{2s}(C)` need not equal `D ∩ C`; equality holds iff
`Hull_s(C) ⊆ σ_{2s}(C)` (if `Hull(C) ⊆ σ_{2s}(C)` then, `Hull(C)` also lying in `D`,
we get `Hull(C) ⊆ D ∩ σ_{2s}C = Hull(D)`; conversely `Hull(D) = Hull(C)` forces
`Hull(C) ⊆ σ_{2s}C`). We could neither prove nor refute this:

> **Conjecture H-3A.1.** For every right `R_n`-submodule `C` and every `s`,
> `Hull_s(C) ⊆ σ_{2s}(C)`; equivalently `Hull_s(C^{⊥_s}) = Hull_s(C)` as subspaces.
>
> Status: **CONJECTURE**. Trivial when `r ∣ 2s`. In the non-reflexive regime it was
> tested on `68` nonzero hulls: `64` arising from `600` dedicated probes at `(8,1,2)`
> (`r = 3`, `s = 1, 2`) plus `~2400` further codes in exploratory sweeps at
> `(8,1,2)`, `(8,1,3)`, `(8,2,1)`, `(8,2,3)`, of which about `10%` were **not**
> `σ_{2s}`-stable (so the inclusion is not vacuous for them): **0 violations were
> found**. Note that it would imply that every self-orthogonal code is
> `σ_{2s}`-stable; on that consequence the data is **uninformative**, since no
> self-orthogonal code was found in the non-reflexive sample (all 10 self-orthogonal
> codes found lie in the reflexive regime, where `σ_{2s} = id` and the conclusion is
> vacuous).

### 4.4 Requires `σ_{2s}(C) = C` for the individual code

**Proposition 4.4.** If `C` is `σ_{2s}`-stable then `Hull_s(C^{⊥_s}) = Hull_s(C)`.
Self-duality implies `σ_{2s}`-stability (§5.3), but `σ_{2s}`-stability alone does not
imply self-duality.

*Proof.* `σ_{2s}(C) = C` ⟹ `Hull(D) = D ∩ σ_{2s}C = D ∩ C = Hull(C)`. ∎

The three regimes (`s`-general, `r ∣ 2s`, codewise `σ_{2s}`-stable) are therefore **not** the same condition, and the tests report them
separately: `dim` equality (all `s`), set equality (reflexive, or `σ_{2s}`-stable, or
conjecturally always), and `σ_{2s}`-stability of the code itself (a separate, stronger,
codewise hypothesis).

### 4.5 Warning B3.5 (retained verbatim in effect)

A quantum construction must satisfy **its own** containment and field-linearity
hypotheses. Nothing in §4 licenses such a claim: even the reflexive regime gives
`C^{⊥_s⊥_s} = C` and a `σ_s`-Hermitian form, but no CSS/EA containment, no Gray map
and no `F_p`-linearity statement has been established here.

---

## 5. Task E — LCD, self-orthogonal and self-dual

### 5.1 LCD

**Theorem 5.1.** The following are equivalent, for every `C` and `s`:

1. `Hull_s(C) = {0}` (LCD);
2. `C ⊕ C^{⊥_s} = R^n`, i.e. `dim(C + C^{⊥_s}) = 4tn`;
3. `W(C) ∩ W(C^{⊥_s}) = {0}` (Morita);
4. in the principal case: `im g ∩ ker θ_s(rev g) = {0}`.

*Proof.* (1)⟺(2): `dim(C∩D) = dim C + dim D − dim(C+D) = 4tn − dim(C+D)`, so the
intersection is `0` iff `dim(C+D) = 4tn`. (1)⟺(3): `Hull = I_{W∩W'}` and `I_W = {0}`
iff `W = {0}` (Morita injectivity). (3)⟺(4) is Theorem 3.3. ∎

Note that `dim C + dim C^{⊥_s} = 4tn` holds **always**, so LCD is *not* automatic — it
is the statement that the two are **complementary**, which fails exactly when the hull
is nonzero. Verified on every sampled code (the three predicates agreed on 100% of
them).

### 5.2 Self-orthogonal

**Theorem 5.2.** `C ⊆ C^{⊥_s}` ⟺ `W(C) ⊆ W(C^{⊥_s})` ⟺, in the principal case,

```
θ_s(rev g) · g = 0   in M_2(B)      (equivalently  im g ⊆ ker θ_s(rev g) ).
```

*Proof.* `C ⊆ D` ⟺ `I_{W(C)} ⊆ I_{W(D)}` ⟺ `W(C) ⊆ W(D)` (Morita is an inclusion-
preserving bijection). For the principal case `W(C) = im g`, `W(D) = ker v` with
`v = θ_s(rev g)`, and `im g ⊆ ker v` ⟺ `v·(im g) = 0` ⟺ `v g = 0`. ∎

Verified: the product criterion and the containment criterion agreed on **every**
sampled code and `s` (0 disagreements).

### 5.3 Self-dual

**Theorem 5.3.** `C = C^{⊥_s}` ⟺ `C ⊆ C^{⊥_s}` and `2 dim_{F_q} C = 4tn` ⟺
(principal case) `im g = ker θ_s(rev g)`. In that case:

1. `dim_{F_q} C = 2tn`, `|C| = q^{2tn} = |R|^{n/2}`;
2. `C` is `σ_{2s}`-stable: `σ_{2s}(C) = C`; hence a self-dual code for `s` with
   `r ∤ 2s` must be `σ_{2s}`-stable (a real constraint).

*Proof.* `C = D` implies `dim C = dim D = 4tn − dim C`, i.e. `2 dim C = 4tn`;
conversely `C ⊆ D` with equal dimension gives equality. `im g = ker v` is Theorem 5.2
plus `|im g| = |ker v|`, which by Stage 2C Cor 3.9 (L-6.5) is equivalent to the
dimension statement. For (2): if `C = D` then `C = D^{⊥_s} = σ_{2s}(C)`. ∎

**Existence (verified, not assumed).** Self-dual codes were found and verified:
`(4,1,1)`, `s = 0`: 3 of 40 sampled codes; `s = 1`: 6 of 40; `(4,1,2)`, `s = 1`: 1 of
40. In all of them the necessary `σ_{2s}`-stability was verified (0 violations) — but
note that all three are **reflexive** cases (`r ∣ 2s`), where `σ_{2s} = id` and the
stability conclusion is vacuous; a non-reflexive instance would need a self-dual code
at `(8,1,2)`, and none was found. No
self-dual code was found in the remaining cases, and **none is claimed** to exist
there: the census is reported as found, and where the count is zero the corresponding
criterion check is skipped with an explicit note rather than passed vacuously.

---

## 6. Task F — computation

### 6.1 The script and its independence

`04_COMPUTATION/phase3_stage3a_hull_structure.py` imports the Stage-2C module
`phase2_stage2c_galois_duality.py` (rings, `ι`, `σ_k`, `θ_s`, `rev`, the pairing,
annihilators, `im`/`ker`/`I_W`, CRT components, SNF) and `ring_structure_checks.py`
(`Field`, `rref`, `nullspace_basis`, reporting). **Neither file is modified.** The hull
machinery is new: the `F_q`-subspace intersection (by the orthogonality trick, validated
against brute-force enumeration on 30 random pairs of subspaces), the four hull routes,
the `F_p`-rank routine, the CRT permutation `τ`, the principality-by-exhaustive-search
routine and all the tests.

Independence is structural: route **D** uses only the pairing; route **A** only
`θ_s`/`rev`/annihilators-as-kernels; route **M** only `im`/`ker` on `B²` and the column
convention; route **N** only dimensions. Route M never touches the pairing, and route D
never touches `im`/`ker`, so agreement is meaningful.

### 6.2 Cases

| `(q,t,n)` | `r` | regime | `|R_n|` | codes per `s` | boundary |
|---|---|---|---|---|---|
| `(4,1,1)` | 2 | split, `n = 1` | 256 | 40 | `n = 1` (O-2.7 anchor) |
| `(4,1,2)` | 2 | chain | 65 536 | 40 | `t = 1`, `p ∣ n` |
| `(4,2,1)` | 2 | chain | 65 536 | 40 | `t ≥ 2`, `p ∤ n` |
| `(4,2,2)` | 2 | **wild** | 4.3·10⁹ | 40 (+120 wild probes) | `p ∣ n`, `t ≥ 2` |
| `(4,1,3)` | 2 | split | 1.7·10⁷ | 40 | `n = 3`, `τ ≠ id` at `s = 0` |
| `(9,1,2)` | 2 | split | 4.3·10⁷ | 40 | `q = 9` |
| `(8,1,2)` | 3 | chain | 1.7·10⁷ | 40 (+600 probes) | `q = 8`, **non-reflexive** `s = 1,2` |
| `(4,2,3)` | 2 | split | 2.8·10¹⁴ | 40 | `n = 3`, `t ≥ 2`, `τ ≠ id` at `s = 0` |

Every `s ∈ {0,…,r−1}` is tested, so both `r ∣ 2s` and `r ∤ 2s` occur.

### 6.3 Results

| Area | Result |
|---|---|
| **Routes** | `hull_D = hull_A = hull_M` for every sampled code at every case and `s`; the duals `D_def = D_ann` agree; the two forms of `W(C^{⊥_s})` agree |
| **Both inclusions** | verified elementwise by set enumeration where the hull is small enough: 6 codes at 13 of the 17 pairs; the 4 remaining pairs are too large to enumerate and are skipped with a note |
| **Structure (A)** | hull is an `F_q`-subspace, a right `R_n`-submodule, shift-invariant; **not** a left ideal for every nonzero hull found (see §1.3 for counts); `Hull(σ_kC) = σ_kHull(C)`; `θ_s(Hull) = θ_s(C) ∩ rev(ann_l(σ_{2s}C))`; `rev(Hull) = rev(C) ∩ ann_r(θ_s(C))` |
| **Dimensions (C)** | `dim = 4tn − dim(C+C^{⊥_s}) = dim C − rank ψ_C = 2 dim(W∩W')` on all 40 codes at every one of the 17 pairs (0 violations); `dim_{F_p} = r·dim_{F_q}` verified by direct `F_p`-rank on 8 codes at 15 pairs; `|I_W| = |W|² = |Hull|` verified by enumeration on 6 codes at 13 pairs; hull dimension even at all 17 pairs |
| **Principality (C4)** | `Hull` principal ⟺ `μ_B(W∩W') ≤ 2`, verified by exhaustive generator search at 15 of the 17 pairs (40 codes each, 38 at `(4,2,3)`); `μ_B(W_hull)` distribution reported per pair; no non-principal hull found |
| **SNF (C5)** | `Hull = gR_n ∩ hR_n` with `h` the P-2.8 generator: 15/15 codes at each of the 15 non-wild pairs; the wild pairs are skipped (`B` is not a chain ring) |
| **CRT (C3)** | `(C^{⊥_s})_j = (C_{τ(j)})^{⊥_s}` and `Hull_j = C_j ∩ (C_{τ(j)})^{⊥_s}` hold for **all** 20 codes × components at every split case; the naive `Σ_j dim Hull(C_j)` fails exactly when `τ ≠ id` (9/20 at `(4,1,3)`, 1/20 at `(4,2,3)`, both at `s = 0`) |
| **Regimes (D)** | `Hull(D) = (C+D)^{⊥_s}` and `Hull(σ_{2s}C) = σ_{2s}Hull(C)` verified on all 40 codes at every pair; `dim Hull(D) = dim Hull(C)` at 17/17 pairs; `Hull(σ_{2s}C) = σ_{2s}Hull(C)` everywhere; `Hull(D) = Hull(C)` as subspaces at the 15 reflexive pairs; conjectures H-3A.1/H-3A.2: 0 violations in 68 nonzero hulls from 600 dedicated non-reflexive probes (plus 680 sample codes) |
| **LCD/SO/SD (E)** | the LCD equivalences agree on 100% of codes; the SO product criterion agrees on 100%; SD ⟹ `σ_{2s}`-stable with 0 violations; census below |
| **s-dependence** | `dim Hull_s(C)` varies with `s` for some code at 5 of the 8 cases — `(4,1,1)` 2/12, `(4,2,2)` 1/12, `(4,1,3)` 1/12, `(9,1,2)` 3/12, `(4,2,3)` 4/12 fixed codes; no variation among 12 fixed codes at `(4,1,2)`, `(4,2,1)`, `(8,1,2)` (reported, not passed) |

**Census (LCD / self-orthogonal / self-dual out of 40 sampled codes).**

| case | `s = 0` | `s = 1` | `s = 2` |
|---|---|---|---|
| `(4,1,1)` | 37 / 3 / **3** | 34 / 6 / **6** | — |
| `(4,1,2)` | 35 / 0 / 0 | 30 / 1 / **1** | — |
| `(4,2,1)` | 30 / 0 / 0 | 25 / 0 / 0 | — |
| `(4,2,2)` | 32 / 0 / 0 | 29 / 0 / 0 | — |
| `(4,1,3)` | 20 / 0 / 0 | 20 / 0 / 0 | — |
| `(9,1,2)` | 37 / 0 / 0 | 36 / 0 / 0 | — |
| `(8,1,2)` | 36 / 0 / 0 | 39 / 0 / 0 | 37 / 0 / 0 |
| `(4,2,3)` | 13 / 0 / 0 | 13 / 0 / 0 | — |

### 6.4 Negative controls (a wrong convention must FAIL)

| # | Wrong statement | Outcome |
|---|---|---|
| neg-1 | omit `rev` from the hull formula | detected by 20–23 of 40 codes at `n = 3`; **vacuous for `n ≤ 2`** (provably: `rev = id`), and the log says so instead of passing |
| neg-2 | `ann_l` instead of `ann_r` | detected by 1–29 of 40 codes per case (17/17 pairs) |
| neg-3 | `I_W` built from **rows** instead of columns | detected by 1–27 of 40 codes per case (17/17 pairs) |
| neg-4 | the hull is always two-sided | refuted: every nonzero hull found is **not** a left ideal |
| neg-5 | `Hull_s(σ_kC) = Hull_s(C)` (instead of `σ_kHull_s(C)`) | detected by 1–8 of 12 codes at 13 of the 17 pairs; not exhibited at `(4,1,1)` (`s = 0,1`) and `(8,1,2)` (`s = 1,2`), where every sampled hull happened to be `σ_k`-invariant — reported, not passed |
| neg-6 | the Euclidean form `Σ x_e y_e` gives the same dual | detected by 1–29 of 40 codes per case (17/17 pairs); the witness `x = E_12`, `y = E_21` is verified at all 17 pairs |
| neg-7 | `dim Hull_s(C)` is independent of `s` | refuted at 5 of the 8 cases (see §6.3) |
| — | naive componentwise hull when `τ ≠ id` | refuted at `(4,1,3)` and `(4,2,3)`, `s = 0`: 9/20 and 1/20 codes (§3.3) |

**Three real bugs were caught by this discipline during development**, recorded because
they are exactly the failure modes the controls exist to detect: (i) the
restricted-pairing matrix was built by dotting word-coordinate rows against
`R_n`-coordinate vectors — every other check passed, and only the rank formula exposed
it; (ii) `right_ideal_basis` returns lists while the route keys are tuples, so a
principality test compared list to tuple and reported "not principal" for everything
(the same trap in a second and third place later); (iii) the Euclidean-vs-transpose
witness search only looked at diagonal matrix units, where `x^Ty = xy`, and so found no
witness.

### 6.5 Reproducibility

**583 checks, 583 PASS, 0 FAIL** — 117 `[EXH]`, 467 `[SMP]`, seed `20261108`,
Python 3.11.2. Two consecutive runs (≈ 45 s each) produced **byte-identical** logs:
SHA-256 `478d62ff31f6d95d36731e4a25b8026f7d40bbf030ba39c6113b2427bd9acfe2` (792
lines). The log carries no timestamp and no elapsed time. **Regression:** the
Stage-2A, Stage-2B and Stage-2C scripts were not modified in Stage 3A.

---

## 7. Task G — literature comparison and novelty

### 7.1 What exists (verified references)

| Topic | Reference | Status |
|---|---|---|
| ℓ-Galois inner product / dual introduced | Fan, Y., Zhang, L. (2017), cited as the origin of the ℓ-Galois dual in Liu–Pan (2020) | `IMPORTED RESULT` (verified as cited) |
| Galois hulls over **finite fields**: dimension invariance under permutation equivalence, computation from a generator matrix, Galois LCD | Liu, H., Pan, X., *Galois hulls of linear codes over finite fields*, Des. Codes Cryptogr. **88**(2), 241–255 (2020) | `IMPORTED RESULT` (publisher page verified) |
| Galois LCD codes over finite fields; constacyclic characterisation | Liu, X., Fan, Y., Liu, H., *Galois LCD codes over finite fields*, Finite Fields Appl. **49**, 227–242 (2018) | `IMPORTED RESULT` |
| Galois hulls and EAQECC over finite fields | Cao, M., *MDS codes with Galois hulls of arbitrary dimensions and the related entanglement-assisted quantum error correction*, IEEE Trans. Inform. Theory **67**(12), 7964–7984 (2021) | `IMPORTED RESULT` (out of scope for use) |
| Hulls of cyclic codes over `Z_4`: types, average 2-dimension | Jitman, S., Sangwisut, E., Udomkavanich, P., *Hulls of cyclic codes over `Z_4`*, arXiv:1806.07590 | `IMPORTED RESULT` (arXiv record verified) |
| **Galois** hulls of cyclic serial codes over a **finite chain ring** (commutative) | Talbi, S., Batoul, A., Fotue Tabue, A., Martínez-Moro, E., *Galois hulls of cyclic serial codes over a finite chain ring*, arXiv:2102.06995 | `IMPORTED RESULT` (arXiv record verified) |
| Hull dimension → entanglement cost | Brun, Devetak, Hsieh (2006); Wilde–Brun; Guenda, K., Jitman, S., Gulliver, T.A., *Constructions of good entanglement-assisted quantum error correcting codes*, Des. Codes Cryptogr. **86**, 121–136 (2018) | `IMPORTED RESULT` (out of scope for use) |
| Cyclic codes over **matrix rings** (structure, self-dual codes, isometries) | Alahmadi, Oggier *et al.*, *Cyclic codes over `M_2(F_2)`* (2013); Islam, H., Prakash, O., Bhunia, D.K., *On the structure of cyclic codes over `M_2(F_p+uF_p)`* (2021); Falcunit–Sison (cyclic codes over `M_2(F_p)`); skew cyclic codes over `M_2(F_2)`, AIMS Math. **8**(10), 24434–24445 (2023) | `IMPORTED RESULT` |
| Cyclic codes in **noncommutative** skew polynomial rings | Boucher, Geiselmann, Ulmer (2007, 2008, 2011) | `IMPORTED RESULT` |

### 7.2 What we did not find

In this search we found **no** reference treating **Galois hulls of cyclic codes over a
matrix ring over a finite chain ring** — i.e. over `M_2(A_t)` with
`A_t = F_q[u]/⟨u^t⟩`, `t` arbitrary. The existing strands are (i) Galois hulls over
*fields* and over *commutative* chain rings, and (ii) cyclic codes over matrix rings
studied for their *Euclidean/self-dual* structure. The search was a targeted web
search, not a systematic bibliographic sweep, so the absence statement is
"**no reference was found in this search**", not "none exists".

### 7.3 The precise, narrow claim

We do **not** claim that Galois hulls, anti-automorphism duality, cyclic codes over
matrix rings, or hull-to-quantum constructions are new: §7.1 shows each of them is
established. The candidate contribution is the **combination**, and specifically the
following items, each proved here and each absent from the references found:

1. **Morita reduction of the hull**: `Hull_s(C) = I_{W∩W'}` with `W = W(C)`,
   `W' = W(C^{⊥_s})`, hence `dim Hull = 2 dim(W∩W')`, the **parity** of the hull
   dimension, and the principality criterion `μ_B(W∩W') ≤ 2` (which is a genuinely
   noncommutative statement: it has no analogue over a field, where every ideal is
   principal).
2. **Annihilator/reversal description**: `Hull = C ∩ rev(ann_r(θ_s(C)))` for
   **non-principal** right ideals, with the side discipline (`ann_r` vs `ann_l`,
   `θ_s(ann_r I) = ann_l(θ_s I)`) and the `θ_s`/`rev` behaviour of the hull itself
   (Theorems 1.7, 1.8).
3. **CRT permutation**: the hull does not decompose componentwise when `τ ≠ id`, with
   the exact criterion `n ∣ p^s + 1` for decomposition, and an explicit counterexample
   (`dim Hull = 2` versus `Σ_j dim Hull(C_j) = 0`).
4. **Non-reflexive regime**: the separation of `dim`-equality (all `s`) from
   set-equality (needs `r ∣ 2s`, or `σ_{2s}`-stability, or Conjecture H-3A.1).
5. **Wild-regime obstruction**: the failure of principality (Stage 2C's `M_2(m)`) and
   the resulting absence of a universal closed generator-polynomial formula for the
   hull.

Everything downstream — hull enumeration, Gray maps, quantum parameters — is out of
scope for this stage and is not claimed.

---

## 8. Traceability: result → obligations → tests → hypotheses → residual risk

| Result | Task | Proof | Tests (log) | Hypotheses | Residual risk |
|---|---|---|---|---|---|
| Lemma 1.2 (F_q-linearity) | A1, C0 | §1.2 | scalar multiples of dual basis vectors, per case | `F_q` central in `R` | none |
| Prop 1.3 (right module / cyclic) | A2, A3(cyclic) | §1.3 | closure under all ring generators; shift-invariance | Phase 1 Cor 6.4 + Stage 1 | none |
| Prop 1.4 (not a left ideal) | A2 | §1.3 | explicit witness + counts per case | — | none (witness exhibited) |
| Prop 1.5 (`σ_k`-equivariance) | A4 | §1.4 | 12 codes × `r` values of `k` | Phase 1 Lemma 6.11 | none |
| Lemma 1.6 + Thm 1.7 (`θ_s` of hull) | A4 | §1.5 | 12 codes, both sides independent | L-6.1, P-2.7 | none |
| Thm 1.8 (`rev` of hull) | A4 | §1.5 | 12 codes | P-2.1f | none |
| §1.6 distinctions | A5 | §1.6 | Euclidean witness; Hermiticity both directions; census | Thm 7.2 | the classical Euclidean hull is a different theory, not covered |
| Thm 2.1 (principal hull) | B | §2.1 | 3 routes + elementwise inclusions | P-2.7, Morita | none |
| Thm 2.2 (non-principal hull) | B | §2.2 | 3 routes + 1-generator failure | P-2.7 (general) | none |
| Thm 3.1 (rank formula) | C1 | §3.1 | every code | semilinearity handled | none |
| Thm 3.2 (sum formula) | C1 | §3.1 | every code | Phase 1 size formula | none |
| Thm 3.3 + Cor 3.4 (Morita, parity, principality) | C2, C4 | §3.2 | routes agree at 17/17 pairs; parity; exhaustive generator search at 15/17 | Morita (Stage 2A) | principality search limited to `q^{dim} ≤ 3000`; wild pair not enumerated |
| Thm 3.5 (CRT, `τ`, `n ∣ p^s+1`) | C3 | §3.3 | component formulas on 20 codes × components; naive formula fails when `τ ≠ id` | **split regime** | chain regime: decomposition trivial (not tested); wild: no decomposition (stated) |
| Thm 3.6 (matrix formula) | C4 | §3.4 | via Thm 3.3 | principal `C` | none |
| Thm 3.7 (SNF: `Hull = gR_n ∩ hR_n`) | C5 | §3.5 | 15 codes per chain-ring case | `p ∤ n` or `t = 1` | **not extended to wild** |
| §3.6 wild losses | C | §3.6 | 120 wild probes | wild regime | O-3.1 open |
| Thm 4.1 (`Hull(D) = (C+D)^{⊥_s}`, `σ_{2s}`-equivariance, sum formulas) | D | §4.1 | every code, every `s` | Phase 1 | the **dimension** equality is NOT proved here (see H-3A.2) |
| Thm 4.3 (reflexive ⟹ set equality) | D | §4.3 | reflexive cases | `r ∣ 2s` | none |
| **Conjecture H-3A.1** (`Hull(C) ⊆ σ_{2s}C`) | D | — | 64 nonzero hulls / 600 probes, 0 violations | `r ∤ 2s` | **unproved** |
| **Conjecture H-3A.2** (`dim Hull(C^{⊥_s}) = dim Hull(C)`) | D | — | ≈ 1300 codes, 0 violations | all `s` | **unproved** |
| Prop 4.4 (`σ_{2s}`-stable ⟹ set equality) | D | §4.4 | — | codewise | none |
| Thm 5.1 (LCD) | E | §5.1 | every code | — | none |
| Thm 5.2 (SO) | E | §5.2 | every code | principal for the product form | none |
| Thm 5.3 (SD) | E | §5.3 | 3 + 6 + 1 self-dual codes verified | — | all three are reflexive cases, so the `σ_{2s}`-stability check is vacuous there; existence not claimed where none found |
| §6.4 negative controls | F | — | 7 controls, all exhibited where meaningful | — | 2 controls not exhibited at some cases (reported) |
| §7 literature | G | — | — | — | absence claim limited to this search |

---

## 9. Report

### 9.1 Proved in Stage 3A

Lemma 1.2, Propositions 1.3–1.5, Lemma 1.6, Theorems 1.7, 1.8, 2.1, 2.2, 3.1, 3.2,
3.3, Corollary 3.4, Theorems 3.5, 3.6, 3.7, 4.1, 4.3, 5.1, 5.2, 5.3, Proposition 4.4,
and the distinction analysis of §1.6. Register rows **T-137 … T-166**.

### 9.2 Conjectures and open problems

* **H-3A.1 (CONJECTURE).** `Hull_s(C) ⊆ σ_{2s}(C)` for every `C`, `s` (equivalently
  `Hull_s(C^{⊥_s}) = Hull_s(C)` as subspaces). Trivial for `r ∣ 2s`; in the
  non-reflexive regime verified on 64 nonzero hulls from 600 dedicated probes (and
  ~2400 exploratory codes) with 0 violations, unproved.
* **H-3A.2 (CONJECTURE).** `dim Hull_s(C^{⊥_s}) = dim Hull_s(C)` for every `C`, `s`;
  verified on ≈ 1300 codes with 0 violations, unproved. (An earlier draft claimed a
  proof; the gap — conflating `C^{⊥_s}` with `(σ_{2s}C)^{⊥_s}` — is recorded in §4.1
  rather than papered over.)
* **O-3.1 (OPEN).** Is `μ_B(W_hull) ≤ 2` always, i.e. is the hull of a principal code
  always principal (even in the wild regime)? No counterexample in 120 wild probes;
  the obstruction is real for duals (Stage 2C).
* **O-3.2 (OPEN).** A closed generator-polynomial formula for the hull (the classical
  `gcd` form) — shown **not** to exist in general (§3.0); the strongest universal
  statement is the structural formula of Theorem 3.3.
* Carried forward unchanged: O-2.2, O-2.4 (partially resolved), O-2.5, O-2.6, O-2.9,
  L-6.6 (unverified import, now unused), T-006, T-027, T-011–T-014, warning B3.5, the
  Phase-1 coverage gaps, the `n ≥ 2` left-submodule gap, C-2.1d/e/f/g.

### 9.3 Exact hypotheses (summary)

* §1: no restriction beyond `q = p^r`, `t ≥ 1`, `n ≥ 1`, `X` central.
* §2: no restriction (principal and non-principal, all `s`, wild included).
* Thm 3.5 (CRT): **split** regime (`p ∤ n`, all `n`-th roots in `F_q`); decomposition
  iff `n ∣ p^s+1`.
* Thm 3.7 (SNF): `p ∤ n` or `t = 1`.
* Thm 4.3: `r ∣ 2s`. Prop 4.4: `σ_{2s}(C) = C`.
* Thm 5.2 (product form) and Thm 5.3 (image form): `C` principal.
* Principality search (Cor 3.4 verification): `q^{dim hull} ≤ 3000`.

### 9.4 Scope boundary (unchanged)

No hull enumeration, no Gray map, no CSS/EAQECC construction, no quantum parameter
claim, no manuscript preparation. The single outward-looking identity
`Hull_s(C) = C ∩ rev(ann_r(θ_s(C)))` is recorded for later use and **is not** a quantum
claim: the existence of a Galois hull does not by itself produce a quantum code, and
warning B3.5 is retained in full.
