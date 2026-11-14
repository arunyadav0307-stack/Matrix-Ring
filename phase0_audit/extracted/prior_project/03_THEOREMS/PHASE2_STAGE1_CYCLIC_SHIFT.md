# PHASE 2 — STAGE 1: cyclic-code definitions and the shift structure

**Status: STAGE 1 COMPLETE (2026-11-04); STAGE 2 NOT STARTED.**
Companion verification: `04_COMPUTATION/phase2_stage1_shift_checks.py`, log
`04_COMPUTATION/phase2_stage1_shift_log.txt` (**553 / 553 checks PASS**, two consecutive
runs byte-identical).

---

## 0. Scope, labels, and what is carried over unchanged

### 0.1 Authorisation and scope

This document executes **Phase 2, Stage 1** under the authoritative planning document
`PHASE2_PROPOSAL_v2.md` (commit `1327b26`). Its scope is exactly the six items of the
Stage-1 brief:

* **A** exact definitions: `R_n`, its coefficient representation, multiplication, the right
  `R`-module structure on `R^n`, the cyclic shift, and the equivalence between right ideals
  of `R_n` and `T`-invariant right `R`-submodules of `R^n` (§2–§4);
* **B** left/right action conventions, with coordinate formulas and linearity statements,
  distinguishing right-`R`-linearity from `F_q`-linearity (§3);
* **C** centrality of `X`, the operator identity `XT = TX`, and what fails without
  centrality (§5);
* **D** compatibility of `σ_k` and `θ_s` with `T`, with the two actions, and with `F_q`
  scalars, including the side-swapping rule `θ_s ρ_a = λ_{θ_s(a)} θ_s` (§6);
* **E** hypotheses, coordinate proofs, Phase-1/Phase-2 attribution, boundary cases (incl.
  `n = 1`), computational tests and negative tests (everywhere; §8).

### 0.2 Explicitly NOT in Stage 1

P-2.3 (generator numbers / `μ`), P-2.4 (CRT/Hensel), P-2.5/P-2.6 (principality),
P-2.7/P-2.8 (duals and annihilators — in particular **L-6.1**, "`θ_s` is an
anti-automorphism of `R_n`", is *not* proved here), hull dimensions, Gray maps, quantum
constructions, C-2.1 (enumeration conjecture), and any manuscript text. CT-0–CT-6 were
**not** run as a suite; only the focused Stage-1 tests of §8 were run.

### 0.3 Labels used in this document

| Label | Meaning |
|---|---|
| **PROVED IN PHASE 1** | a complete proof already exists in `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` (cited); the statement is imported, not re-proved here |
| **PROVED IN PHASE 2 STAGE 1** | proved here, with a complete coordinate-level proof; the Phase-1 inputs it uses are named |
| **COMPUTATIONALLY VERIFIED ONLY** | checked by exhaustive or sampled computation in a stated range; **not** claimed as a theorem |
| **PROPOSED / UNPROVED** | stated in the planning document, not attempted in Stage 1 |
| **OPEN** | no claim made |

A passing script never promotes a statement: every statement below carries a proof, and
the computation is supporting evidence only.

### 0.4 Carried over unchanged (decisions D1–D4, B1–B3)

* **D1** — the Phase-1 framework is the foundation: `A_t = F_q[u]/⟨u^t⟩`, `R = M_2(A_t)`,
  `R_n = R[X]/⟨X^n−1⟩ ≅ M_2(B)`, `B = A_t[X]/⟨X^n−1⟩`; the **right-module convention**
  (RGF Definition 5.1); the Morita **column** convention (RGF Convention 5.8); the pairing
  `B_s(x,y) = Σ_e θ_s(x_e) y_e` with `θ_s = σ_s ∘ (·)^T`; §5.6 in full.
  **No Phase-1 convention is altered or silently extended here.**
* **D2** — T-042 (the last clause of RGF Remark 5.6) stays **withdrawn** and is cited only
  as "withdrawn / corrected".
* **D3** — every unresolved Phase-1 issue (T-006, T-027, T-021, T-011, T-012, T-013/T-014,
  warning B3.5, the enumeration coverage gaps, the `n ≥ 2` left-submodule gap) is carried
  forward; see §9.3.
* **D4 / B1–B3** — Alahmadi–Sboui–Solé–Yemen (2013) cited for its framework only; the
  novelty claim stays narrowed; the hybrid Galois regime is retained.
* No Phase-1 file was modified while producing this document.

---

## 1. Standing hypotheses and notation

Inherited verbatim from RGF §0.1, with one remark on which hypotheses are actually used.

| Symbol | Meaning | Hypothesis |
|---|---|---|
| `p` | prime | — |
| `q = p^r` | field size | `r ≥ 2` (Phase-1 standing hypothesis, so that a Galois action exists); **nothing in Stage 1 needs `r ≥ 2`** — every statement below holds for all `r ≥ 1` |
| `F_q` | finite field | — |
| `A_t` | `F_q[u]/⟨u^t⟩` | `t ≥ 1` |
| `R` | `M_2(A_t)` | `m = 2` |
| `n` | code length | `n ≥ 1`; **no squarefree hypothesis** (`gcd(n,p) = 1` is not assumed anywhere in Stage 1) |
| `X` | the cyclic indeterminate | central in `R[X]`, hence in `R_n` |
| `s` | Galois parameter | mod `r`; arbitrary in Stage 1 |

Notation (RGF §0.2, unchanged):

```
iota : R^n -> R_n,    x = (x_0,...,x_{n-1})  |->  sum_{e=0}^{n-1} x_e X^e
T    : R^n -> R^n,    (Tx)_e = x_{e-1 mod n}          (the cyclic shift)
rho_a: R^n -> R^n,    (x.a)_e = x_e a                 (RIGHT action of a in R)
lam_a: R^n -> R^n,    (a.x)_e = a x_e                 (LEFT  action of a in R)
sigma_k, theta_s : applied coordinate-wise on R^n, entry-wise on R and R_n
c in F_q acts on R^n through cI in Z(R)   (so an F_q-subspace is the same thing as an
                                           F_p-subspace closed under the cI-actions)
```

**The shift convention.** `T(x_0, x_1, …, x_{n−1}) = (x_{n−1}, x_0, …, x_{n−2})`, i.e.
`(Tx)_e = x_{e−1 mod n}`. This is the Phase-1 convention (RGF §0.2 notation sheet and
Lemma 3.2) and matches the Stage-1 brief exactly. **Warning (T-042-adjacent bookkeeping):**
the opposite convention `(Tx)_e = x_{e+1}` would change the sign in every intertwining
formula involving `T` and `T^{-1}`; it is not used anywhere in this repository.

**Indices** are read modulo `n` throughout. `E_ij` are the matrix units of `R`.

---

## 2. The ring `R_n`: definition, coefficient representation, multiplication

### Definition 2.1 (the cyclic ambient) — **PROVED IN PHASE 1** (RGF Lemma 3.1)

`R_n := R[X]/⟨X^n − 1⟩`, where `X` is a central indeterminate over `R` and `⟨X^n−1⟩` is
the principal two-sided ideal generated by the central element `X^n − 1`.

### Lemma 2.2 (coefficient representation) — **PROVED IN PHASE 1** (RGF Lemma 3.1, Lemma 3.2)

*Hypotheses.* `t ≥ 1`, `n ≥ 1`.

*Statement.* Every element of `R_n` has a **unique** expression

  `Σ_{e=0}^{n−1} x_e X^e`, `x_e ∈ R`,

so `ι : R^n → R_n`, `ι(x) := Σ_e x_e X^e`, is a bijection; `dim_{F_q} R_n = 4tn` and
`|R_n| = q^{4tn}`.

*Proof (reproduced for completeness).* `X^n − 1` is **monic**, so Euclidean division by it
is valid over any coefficient ring: every class has a representative of degree `< n`, and
two such representatives differ by a multiple of `X^n − 1` of degree `< n`, hence by `0`.
The dimension count is `dim_{F_q} R = 4t` times `n`. ∎

*Computationally verified:* `iota_inv ∘ iota = id` and injectivity over the whole ambient
([EXH] at `(q,t,n) = (4,1,1)` and `(9,1,1)`; sampled elsewhere), plus surjectivity by
cardinality at `(4,1,1)`.

### Lemma 2.3 (multiplication is cyclic convolution) — **PROVED IN PHASE 2 STAGE 1**

*Hypotheses.* `t ≥ 1`, `n ≥ 1`; `X` central (Lemma 2.4 below).

*Statement.* For `x, y ∈ R^n`,

  `ι(x)·ι(y) = ι(z)` with `z_e = Σ_{a+b ≡ e (mod n)} x_a y_b`.

*Proof.* `ι(x)ι(y) = (Σ_a x_aX^a)(Σ_b y_bX^b) = Σ_{a,b} x_aX^a y_bX^b`. Since `X` is
central, `X^a y_b = y_b X^a`, so the term is `x_a y_b X^{a+b}`. In `R_n` we have
`X^n = 1`, so `X^{a+b} = X^{(a+b) mod n}`. Collecting the coefficient of each `X^e` gives
exactly `Σ_{a+b ≡ e} x_a y_b`. ∎

*Computationally verified:* [EXH] over all pairs in `B` at `(4,1,1)`, `(4,1,2)`,
`(4,2,1)`; sampled by a stride elsewhere.

*Remark.* This is the only place where the ring multiplication of `R_n` is used in Stage 1.
Note the **order**: `x_a y_b` (the coefficient of the *earlier* factor on the left). Over
the commutative ring `B` this is invisible entry-wise, but it is not invisible in `R`.

### Lemma 2.4 (centrality of `X`) — **PROVED IN PHASE 1** (RGF Lemma 3.1; register L-2.1.1)

*Hypotheses.* none beyond the definition.

*Statement.* (i) `X` commutes with every element of `R` inside `R_n`; equivalently the
element `X·I_2` is central in `M_2(B)`. (ii) `B = A_t[X]/⟨X^n−1⟩` is commutative and
`R_n ≅ M_2(B)`, the isomorphism sending `Σ_e x_eX^e` to the matrix over `B` whose
`(i,j)` entry is `Σ_e (x_e)_{ij} X^e`.

*Proof.* (i) In the polynomial ring `R[X]` the indeterminate commutes with `R` by
construction, and a quotient of a ring by a two-sided ideal inherits that. (ii)
`R[X] ≅ M_2(A_t[X])` entrywise; the ideal generated by the central element `X^n − 1`
corresponds to `M_2((X^n−1))`, so `R_n ≅ M_2(A_t[X]/(X^n−1)) = M_2(B)`. `B` is
commutative because `A_t` is and `X` is central. The matrix description of `ι` follows by
comparing coefficients. ∎

*Computationally verified:* `(X I) Z = Z (X I)` for all `Z` ([EXH] at `(4,1,1)`,
`(9,1,1)`; sampled elsewhere); `B` commutative ([EXH] at three parameter sets).

### Lemma 2.5 (`R_n` is generated by `R` and `X`; `ι` is `R`-bilinear) — **PROVED IN PHASE 2 STAGE 1**

*Hypotheses.* Lemma 2.4.

*Statement.*
1. The map `emb : R → R_n`, `a ↦ a` (constant polynomial), is an **injective ring
   homomorphism**; we identify `R` with its image. `R_n` is generated as a ring by
   `emb(R)` and `X`.
2. `ι` is additive and `F_q`-linear.
3. `ι` is **right `R`-linear**: `ι(x·a) = ι(x)·emb(a)` for all `x ∈ R^n`, `a ∈ R`.
4. `ι` is **left `R`-linear**: `ι(a·x) = emb(a)·ι(x)`.
5. `ι(Tx) = ι(x)·(X·I)` — **this one does not need centrality**.

*Proof.* (1) is immediate from the definitions (constant polynomials multiply as in `R`).
(2) is immediate. (3) `ι(x·a) = Σ_e (x_ea)X^e`, while
`ι(x)·emb(a) = (Σ_e x_eX^e)·a = Σ_e x_e X^e a = Σ_e x_e a X^e` — the last equality uses
that `X` commutes with `a` (**centrality**). (4) is the mirror computation. (5)
`ι(x)·X = Σ_e x_e X^{e+1} = Σ_e x_{e−1}X^e = ι(Tx)` by re-indexing modulo `n` (using
`X^n = 1`); no commutation of `X` with `R` is involved because `X` is multiplied from the
right onto a polynomial in `X` with coefficients on the left. ∎

*Computationally verified:* all four items, [EXH] over all `(x,a)` at `(4,1,1)`, sampled
elsewhere.

**This is the precise point at which centrality enters the equivalence of §4:** items (3)
and (4) fail without it (§5.3), while item (5) does not.

---

## 3. The right `R`-module `R^n`, the two actions, and the shift

### Definition 3.1 (the two actions) — **PROVED IN PHASE 1** (RGF Definition 5.1, §5.6.2 B1/B2)

For `x ∈ R^n`, `a ∈ R`:

  `(x·a)_e := x_e a` (right action `ρ_a`), `(a·x)_e := a x_e` (left action `λ_a`).

Elementary consequences (all immediate from associativity in `R`, all used below):

* `ρ_a ρ_b = ρ_{ba}` — i.e. `a ↦ ρ_a` is a **ring anti-homomorphism** `R → End_{F_q}(R^n)`
  in the convention `ρ_a ρ_b := ρ_a ∘ ρ_b`; equivalently `x·(ab) = (x·a)·b`, so `R^n` is a
  **right `R`-module**.
* `λ_a λ_b = λ_{ab}` — `R^n` is a **left `R`-module**.
* `λ_a ρ_b = ρ_b λ_a` — `R^n` is an `(R,R)`-**bimodule**.
* `F_q`-structure: for `c ∈ F_q` let `c·x := x·(cI) = (cI)·x` (the two agree because
  `cI ∈ Z(R)`). A right (or left) `R`-submodule is automatically an `F_q`-subspace, since
  it is an additive subgroup closed under the `cI`-actions.
* **Do not confuse the two notions of linearity.** `F_q`-linearity only involves the
  central scalars `cI`; right-`R`-linearity involves all of `R` and is strictly stronger.
  `T` below has both; `σ_k` and `θ_s` have **neither** (they are semilinear, §6).

### Definition 3.2 (the cyclic shift) — **PROVED IN PHASE 1** (RGF §0.2, Lemma 3.2)

  `T(x)_e := x_{e−1 mod n}`, i.e. `T(x_0,…,x_{n−1}) = (x_{n−1}, x_0, …, x_{n−2})`.

### Lemma 3.3 (elementary properties of `T`) — **PROVED IN PHASE 2 STAGE 1** (item (iii) is Phase 1)

*Hypotheses.* `n ≥ 1`.

*Statement.* (i) `T` is `F_q`-linear and bijective, with `T^{-1}` given by
`(T^{-1}x)_e = x_{e+1 mod n}`; (ii) `T` is a Hamming isometry:
`wt(Tx) = wt(x)`, where `wt(x) := #{e : x_e ≠ 0}`; (iii) `T^n = id`.

*Proof.* (i) `T` permutes the coordinates, so it is additive, commutes with the
coordinate-wise `F_q`-action (`(c·T x)_e = c x_{e−1} = (T(c·x))_e`), and is inverted by
the stated coordinate permutation. (ii) `wt` counts nonzero coordinates and `T` permutes
them. (iii) `T^k` is `x_e ↦ x_{e−k}`, so `T^n = id`. ∎

*Attribution.* (iii) is RGF Lemma 3.2 (`T` is right multiplication by `X`, and `X^n = 1`).
(i) and (ii) are not promoted to lemmas in Phase 1; they are proved here.

*Computationally verified:* [EXH] at `(4,1,1)`, `(9,1,1)`; sampled elsewhere.

### Lemma 3.4 (`T` is right `R`-linear) — **PROVED IN PHASE 2 STAGE 1** (the computation is displayed in RGF §5.6.2)

*Hypotheses.* none. *Statement.* `T(x·a) = (Tx)·a` for all `x ∈ R^n`, `a ∈ R`.

*Coordinate proof.* For every `e`,

  `[T(x·a)]_e = (x·a)_{e−1} = x_{e−1} a = (Tx)_e a = [(Tx)·a]_e`. ∎

*Remark (what the proof does **not** use).* Only that the right action is coordinate-wise.
No centrality, no identification with multiplication by `X`. Contrast the proof via
Lemma 2.5(5)+Lemma 2.4: `T = ρ_X` and `ρ_X ρ_a = ρ_{aX}`, `ρ_a ρ_X = ρ_{Xa}`, which agree
**only because `X` is central**. The coordinate statement is the more robust one; the
identification-based proof is the one that needs the hypothesis.

*Computationally verified:* [EXH] over **all** `65 536` pairs `(x,a)` at `(4,1,1)`;
`20 000` sampled pairs (seed `20261104`) at each of the other seven parameter sets.

### Lemma 3.5 (`T` is left `R`-linear) — **PROVED IN PHASE 2 STAGE 1**

*Hypotheses.* none. *Statement.* `T(a·x) = a·(Tx)`.

*Coordinate proof.* `[T(a·x)]_e = (a·x)_{e−1} = a x_{e−1} = a (Tx)_e = [a·(Tx)]_e`. ∎

*Attribution note.* The displayed computation `[T(a·x)]_e = a x_{e−1} = (a·(Tx))_e` appears
in RGF §5.6.2, but is not stated there as a lemma and does not appear in the Phase-1
register (T-033 records only right-linearity). The complete coordinate proof is given
here, so the statement is a **Phase-2 Stage-1** result.

*Consequence (convention-independence of "cyclic").* Since `T` is `R`-linear on **both**
sides, the property "closed under `T`" is a property of the underlying `F_q`-subspace
alone: it does not depend on the right/left convention. The convention dependence of the
theory enters only through the pairing (RGF Convention 5.2) and through Lemma 5.6a.

### Lemma 3.6 (`T` is multiplication by `X`, on either side) — **PROVED IN PHASE 1** (right) **+ PROVED IN PHASE 2 STAGE 1** (left)

*Hypotheses.* Lemma 2.4. *Statement.* Under `ι`, for every `x ∈ R^n`:

  `ι(Tx) = ι(x)·(X·I₂)` **(no centrality needed)**, and `ι(Tx) = (X·I₂)·ι(x)`
  **(needs centrality)**.

*Proof.* The first is Lemma 2.5(5) = RGF Lemma 3.2. For the second, write
`ι(x) = Σ_e x_eX^e` with `x_e ∈ R`; then `(X·I₂)·ι(x) = Σ_e X x_e X^e = Σ_e x_e X^{e+1}`
(the middle equality is exactly centrality of `X` with respect to `R`), which is
`ι(Tx)`. ∎

*Computationally verified:* both, [EXH] over all of `R^n` at `(4,1,1)`, `(4,1,2)`
(`65 536` vectors) and `(4,2,1)` (`65 536` vectors); sampled elsewhere.

### Lemma 3.7 (`T` as an `R_n`-module map) — **PROVED IN PHASE 2 STAGE 1**

*Hypotheses.* Lemma 2.4. *Statement.* Let `L_X, R_X : R_n → R_n` be left and right
multiplication by the central element `X·I₂` (so `L_X = R_X = T` under `ι`). Then

1. `T` is **left `R_n`-linear**: `T(uv) = u·T(v)` for all `u,v ∈ R_n` — this holds for
   **any** element in place of `X`, by associativity alone;
2. `T` is **right `R_n`-linear**: `T(uv) = T(u)·v` — this holds **iff `X` is central**.

*Proof.* (1) `T(uv) = (uv)X = u(vX) = u·T(v)`. (2) `T(uv) = (uv)X = u(vX)` while
`T(u)v = (uX)v = u(Xv)`; the two agree for all `u,v` iff `vX = Xv` for all `v` (take
`u = 1`), i.e. iff `X ∈ Z(R_n)`. ∎

*Computationally verified:* both identities ([SMP], 8 000 pairs per parameter set), plus
the negative control of §5.3(iii).

---

## 4. The equivalence: right ideals of `R_n` versus `T`-invariant right `R`-submodules

### Theorem 4.1 (the equivalence) — **PROVED IN PHASE 2 STAGE 1** (both directions; the statement is Phase 1, the complete proof is new)

*Hypotheses.* `q = p^r` (any `r ≥ 1`), `t ≥ 1`, `n ≥ 1`; `X` central (Lemma 2.4); the
right-module convention (RGF Definition 5.1). **No** squarefree hypothesis, **no**
hypothesis on `gcd(n,p)`, **no** principality hypothesis.

*Statement.* The map

  `C ⟼ ι(C)`

is a **bijection** from the set of `T`-invariant right `R`-submodules `C ⊆ R^n` onto the
set of right ideals of `R_n`, with inverse `J ⟼ ι^{-1}(J)`. Moreover it preserves
inclusions and `dim_{F_q}` (so it is a lattice isomorphism onto the lattice of right
ideals).

*Attribution.* The statement is RGF Definition 5.1 + Lemma 5.3 ("`C` is a right ideal of
`R_n` iff it is an `R`-submodule closed under `T`"). RGF proves the *closure* direction in
half a line via Lemma 3.2 and does not verify the converse in detail. The complete
two-direction proof, the boundary analysis and the counterexamples of §4.3 are
**Phase-2 Stage-1** work.

**Proof, direction (⇒) [right ideal ⟹ `T`-invariant right `R`-submodule].**
Let `J` be a right ideal of `R_n` and `C := ι^{-1}(J)`.

1. `C` is an `F_q`-subspace. `J` is an additive subgroup; for `c ∈ F_q` and `m ∈ J`,
   `m·(cI) = c m ∈ J`, so `J` is `F_q`-closed, and `ι` is `F_q`-linear (Lemma 2.5(2)).
2. `C` is a right `R`-submodule. For `x ∈ C`, `a ∈ R`: by Lemma 2.5(3),
   `ι(x·a) = ι(x)·emb(a) ∈ J` because `J` is a right ideal and `emb(a) ∈ R_n`. Hence
   `x·a ∈ C`.
3. `C` is `T`-invariant. By Lemma 2.5(5), `ι(Tx) = ι(x)·(X·I₂) ∈ J`. Hence `Tx ∈ C`. ∎

**Proof, direction (⇐) [`T`-invariant right `R`-submodule ⟹ right ideal].**
Let `C ⊆ R^n` be an `F_q`-subspace closed under `ρ_a` for every `a ∈ R` and under `T`; put
`J := ι(C)`.

1. `J` is an `F_q`-subspace (`ι` is `F_q`-linear).
2. `J` is closed under right multiplication by every element of `R_n`. By Lemma 2.2 every
   `w ∈ R_n` is a finite sum `w = Σ_e a_eX^e` with `a_e ∈ R`. For `u ∈ J`, write
   `x := ι^{-1}(u) ∈ C`. For each `e`: `x·a_e ∈ C` (right `R`-submodule), hence
   `ι(x·a_e) = u·emb(a_e) = u a_e ∈ J` (Lemma 2.5(3)); then
   `u a_e X^e = ι(T^e(x·a_e)) ∈ J`, because `C` is `T`-invariant and
   `ι(T^e y) = ι(y)·(X·I₂)^e` (Lemma 2.5(5) iterated). Summing over `e`,
   `u·w = Σ_e u a_eX^e ∈ J`.
3. Therefore `J` is a right ideal of `R_n`. ∎

**The two maps are inverse** because `ι` is a bijection (Lemma 2.2); inclusions and
`F_q`-dimensions are preserved because `ι` is an `F_q`-linear bijection. ∎

**Where centrality is used.** In step (⇒).2 and step (⇐).2, through Lemma 2.5(3):
`ι(x·a) = ι(x)·emb(a)` holds **iff `X` commutes with `R`**. Everything else
(`T^n = 1`, `ι(Tx) = ι(x)X`, additivity, the normal form) is free. See §5.3.

### 4.2 Boundary cases

| Case | What the theorem says | Status |
|---|---|---|
| `n = 1` | `X = 1` in `B`, so `R_1 = R` and `ι(x) = x_0` is the identity; `T = id`, so the `T`-invariance condition is **vacuous** and Theorem 4.1 degenerates to the tautology "right ideals of `R` = right `R`-submodules of `R`" | **PROVED IN PHASE 2 STAGE 1** (immediate); verified [EXH] at `(4,1,1)` and `(9,1,1)` |
| `C = 0` | corresponds to the zero ideal | immediate |
| `C = R^n` | corresponds to `R_n` | immediate |
| `p ∣ n` (`X^n−1` not squarefree) | the theorem is **unchanged**: no squarefree hypothesis is used anywhere above | **PROVED IN PHASE 2 STAGE 1**; verified at `(4,1,2)`, `(4,2,2)` |
| `n ≥ 2` | both conditions are genuinely needed — see §4.3 | **PROVED IN PHASE 2 STAGE 1** |

*Independent census (n = 1).* At `(q,t,n) = (4,1,1)` all `529` `F_q`-subspaces of `R^1`
were enumerated by brute force; exactly **7** are `T`-invariant right `R`-submodules, with
`F_q`-dimensions `[0,2,2,2,2,2,4]`, and every right `R`-submodule is `T`-invariant
(consistent with `T = id`). The count `7 = q+3` and the dimension distribution agree with
the Phase-1 Morita count (T-032/T-041), obtained here by a **different** route (brute
force over subspaces, no Morita). **[EXH]**

### 4.3 Both conditions are necessary (negative controls)

Let `n ≥ 2`.

**(a) A right `R`-submodule that is not `T`-invariant is not a right ideal.**
*Statement.* `C_0 := {x ∈ R^n : x_e = 0 for all e ≥ 1}` is a right `R`-submodule, is not
`T`-invariant, and `ι(C_0) = R ⊆ R_n` (the constant polynomials) is **not** a right ideal.

*Proof.* For `x ∈ C_0` and `a ∈ R`, `(x·a)_0 = x_0a` and `(x·a)_e = 0` for `e ≥ 1`, so
`C_0` is a right `R`-submodule. `T(C_0) = {x : x_e = 0 for e ≠ 1} ≠ C_0`. Finally
`1 ∈ ι(C_0)` but `1·X = X ∉ ι(C_0)`, since the coefficient of `X^1` in `X` is `1 ≠ 0`.
∎ **PROVED IN PHASE 2 STAGE 1**; verified computationally at every `n ≥ 2` parameter set.

**(b) A `T`-invariant `F_q`-subspace that is not a right `R`-submodule is not a right
ideal.** For a randomly drawn `v`, `D := span_{F_q}{T^e v : e}` is `T`-invariant by
construction; whether it is a right `R`-submodule depends on `v`.
**COMPUTATIONALLY VERIFIED ONLY**: for the tested `v` at each `n ≥ 2` parameter set, `D`
is neither a right `R`-module nor a right ideal. (No general statement is claimed.)

**(c) A `T`-invariant LEFT `R`-submodule need not be a right ideal (the wrong side).**
*Statement.* Let `v := (E_11, 0, …, 0)` and `E :=` the left `R`-submodule of `R^n`
generated by `{T^e v : 0 ≤ e < n}`. Then `E` is `T`-invariant, is a left `R`-submodule,
is **not** a right `R`-submodule, and `ι(E)` is not a right ideal.

*Proof.* `E` is `T`-invariant because `T` permutes the generators `{T^e v}` and is left
`R`-linear (Lemma 3.5). Explicitly `E = {y ∈ R^n : every coordinate y_e ∈ R E_11}`, and
`R E_11 = {matrices whose second column is zero}`. Take `y := v·E_12 = (E_12, 0, …, 0)`:
its coordinate `E_12` has second column `(1,0)^T ≠ 0`, so `E_12 ∉ R E_11` and `y ∉ E`.
Hence `E` is not closed under the right `R`-action. ∎ **PROVED IN PHASE 2 STAGE 1**;
verified computationally at every `n ≥ 2` parameter set.

*Remark.* Item (c) is the "wrong side" control demanded by the brief: it is the failure
that would be silently invisible if one tested only `T`-invariance plus *left* closure.
By RGF Lemma 5.6b(2) the orthogonal of a left submodule *is* a left submodule; that has
no bearing on whether a left submodule is a **right ideal**, and the two must not be
conflated (cf. the withdrawn claim T-042).

---

## 5. Centrality of `X`: what it gives, and what fails without it

### 5.1 The operator statement `XT = TX` — **PROVED IN PHASE 2 STAGE 1**

Fix the representation: on `R_n` let `L_X(u) := (X·I₂)·u` and `R_X(u) := u·(X·I₂)`; on
`R^n` let `T` be the shift. By Lemma 3.6, under `ι` we have `R_X = T`, and `L_X = T`
(**if `X` is central**).

**Lemma 5.1.** (i) `L_X ∘ R_X = R_X ∘ L_X` — by associativity alone:
`X(uX) = (Xu)X` for every `u ∈ R_n`. (ii) `L_X = R_X` **iff** `X` is central.
(iii) Consequently, when `X` is central, "multiplication by `X`" is a single operator
`X̂ := L_X = R_X = T`, and the identity `X T = T X` holds **as the trivial statement
`X̂ ∘ X̂ = X̂ ∘ X̂`**; both compositions equal `T² = ` multiplication by `X²`.

*Proof.* (i) is associativity. (ii) `L_X = R_X` means `Xu = uX` for all `u`, i.e.
`X ∈ Z(R_n)`; conversely if `X` is central they are equal. (iii) is (ii) plus
commutativity of an operator with itself. ∎

*Computationally verified:* both (i) and (ii), [SMP], 200 elements per parameter set.

**Lemma 3.7 restated in this language:** `T = R_X` is left `R_n`-linear for free
(associativity) and right `R_n`-linear exactly when `L_X = R_X`, i.e. exactly when `X` is
central.

### 5.2 Left and right multiplication by `X` give the same shift — **PROVED IN PHASE 1 + STAGE 1**

This is Lemma 3.6: `ι(Tx) = ι(x)·X = X·ι(x)`. The first equality is RGF Lemma 3.2
(no centrality); the second is Stage 1 (uses centrality, Lemma 2.4). So left and right
multiplication by `X` induce the **same** cyclic shift, and the equality of the two is
*equivalent* to the centrality of `X`.

### 5.3 What fails if `X` were not central — **PROVED IN PHASE 2 STAGE 1** (a precise comparison)

Suppose one tries to run the same construction with an indeterminate that does not commute
with `R`. Then:

1. **The quotient need not be a ring.** `⟨X^n − 1⟩` must be a *two-sided* ideal for the
   quotient to inherit a ring structure. With a central indeterminate this is automatic;
   without it one is in a skew polynomial ring `R[X;τ]`, `Xa = τ(a)X`, where
   `(X^n−1)·a = τ^n(a)X^n − a`, so the ideal is two-sided only under a compatibility
   condition such as `τ^n = id` (and even then the normal form changes: coefficients move
   to the other side of `X`). **Skew-polynomial theory is out of scope** (Phase-1 item
   T-027 records the general-`τ` question as open); this remark is only a comparison.
2. **`B` would not be commutative and `R_n` would not be `M_2(B)`** (Lemma 2.4(ii)), so
   the entire Morita/CRT apparatus of later stages — which is built on `M_2(B)` with `B`
   commutative — would be unavailable.
3. **`ι` would not be `R`-linear** (Lemma 2.5(3),(4)), hence
   **Theorem 4.1 would fail**: `T`-invariance plus right `R`-closure of `C` would no
   longer be equivalent to `ι(C)` being a right ideal.
4. **`T` would not be right `R_n`-linear** (Lemma 3.7(2)), though it would remain left
   `R_n`-linear (Lemma 3.7(1)). It would remain right/left **`R`-linear as a coordinate
   permutation** (Lemmas 3.4, 3.5), because those statements never mention `X`.
5. **Left multiplication by `X` would no longer be the shift** (Lemma 3.6): it would give
   `Σ_e X x_e X^e` with the scalar trapped on the wrong side.

*Negative control (computational).* Take the genuinely non-central element
`Y := E_11·I ∈ R_n` and let `R_Y(u) := uY`. Then `R_Y(x·a) ≠ R_Y(x)·a` for most pairs
(e.g. `3 984 / 4 000` at `(4,2,2)`, `59 760 / 65 536` at `(4,1,1)`), whereas for the
central `Y = X·I₂` the mismatch count is **0**. This shows that the
right-`R`-linearity test is not vacuous and that centrality is exactly the hypothesis that
makes it pass. **[SMP]/[EXH]**

---

## 6. Automorphism compatibility: `σ_k` and `θ_s`

Throughout, `σ_k(x)_e := σ_k(x_e)` and `θ_s(x)_e := θ_s(x_e)` (coordinate-wise on `R^n`);
both fix `X`. Inputs from Phase 1: `σ_k` is a ring **automorphism** of `R` and `R_n`
(RGF Lemma 4.2); `θ_s = σ_s ∘ (·)^T` is an **anti**-automorphism of `R` (RGF Lemma 4.3);
`θ_s² = σ_{2s}` and `σ_kθ_s = θ_sσ_k` (RGF Lemmas 4.4, 4.7).

### 6.1 Summary table (all entries proved in §6.2–§6.5)

| Property | `σ_k` | `θ_s` |
|---|---|---|
| commutes with `T` (plain commutation of `F_p`-linear maps on `R^n`) | **yes**: `Tσ_k = σ_kT` | **yes**: `Tθ_s = θ_sT` |
| right-action compatibility | **preserves the side**: `σ_kρ_a = ρ_{σ_k(a)}σ_k` | **swaps the side**: `θ_sρ_a = λ_{θ_s(a)}θ_s` |
| left-action compatibility | **preserves**: `σ_kλ_a = λ_{σ_k(a)}σ_k` | **swaps**: `θ_sλ_a = ρ_{θ_s(a)}θ_s` |
| `F_q`-linearity | **no** (`σ_k`-semilinear) | **no** (`σ_s`-semilinear) |
| `F_p`-linearity | yes | yes |
| ring-level nature | automorphism of `R` and `R_n` | anti-automorphism of `R` (Phase 1); on `R_n`: **L-6.1, not treated in Stage 1** |

### 6.2 Commutation with `T` — **PROVED IN PHASE 2 STAGE 1**

*Statement.* For all `x ∈ R^n`: `T(σ_k x) = σ_k(Tx)` and `T(θ_s x) = θ_s(Tx)`; i.e.
`Tσ_k = σ_kT` and `Tθ_s = θ_sT`.

*Coordinate proof.* `[σ_k(Tx)]_e = σ_k((Tx)_e) = σ_k(x_{e−1}) = (σ_k x)_{e−1} =
[T(σ_k x)]_e`. Identically for `θ_s`, since both maps act coordinate-wise while `T`
permutes coordinates. ∎

*Caveat (what this is not).* These are **commutations of maps on the set `R^n`**, and
`σ_k`, `θ_s` are only `F_p`-linear (`F_q`-semilinear). They say nothing about
`F_q`-scalar behaviour and nothing about the `R`-actions. They must also not be confused
with RGF Lemma 5.6a(5), `B_s(x,Ty) = B_s(T^{-1}x,y)`, which is a statement about the
pairing.

*Computationally verified:* [EXH] at `(4,1,1)`, `(9,1,1)`; [SMP] elsewhere; for all
`k, s` mod `r`.

### 6.3 `σ_k` preserves the side — **PROVED IN PHASE 2 STAGE 1**

*Statement (coordinate form).* `σ_k(x·a) = σ_k(x)·σ_k(a)` and
`σ_k(a·x) = σ_k(a)·σ_k(x)`; equivalently `σ_kρ_a = ρ_{σ_k(a)}σ_k` and
`σ_kλ_a = λ_{σ_k(a)}σ_k`.

*Coordinate proof.* `[σ_k(x·a)]_e = σ_k(x_ea) = σ_k(x_e)σ_k(a)` because `σ_k` is a ring
**automorphism** of `R` (RGF Lemma 4.2); this is `[σ_k(x)·σ_k(a)]_e`. The left version is
identical. ∎

*Consistency check (against Phase 1).* Applying twice and using `σ_k² = σ_{2k}` is
consistent; and `σ_k` being an automorphism means it can never swap the sides, which is
exactly why `θ_s` (an *anti*-automorphism) does.

*Computationally verified:* [EXH] over all `65 536` pairs at `(4,1,1)`; [SMP] elsewhere.

### 6.4 `θ_s` swaps the side — **PROVED IN PHASE 2 STAGE 1** (the input `θ_s` anti on `R` is Phase 1)

*Statement (coordinate form).* For all `x ∈ R^n`, `a ∈ R`:

  `θ_s(x·a) = θ_s(a)·θ_s(x)`, i.e. `θ_s ρ_a = λ_{θ_s(a)} θ_s`;
  `θ_s(a·x) = θ_s(x)·θ_s(a)`, i.e. `θ_s λ_a = ρ_{θ_s(a)} θ_s`.

*Coordinate proof.* `[θ_s(x·a)]_e = θ_s(x_ea) = θ_s(a)θ_s(x_e)` because `θ_s` is an
**anti**-automorphism of `R` (RGF Lemma 4.3); and `θ_s(a)θ_s(x_e) = [θ_s(a)·θ_s(x)]_e` is
the **left** action of `θ_s(a)` on `θ_s(x)`. The second identity is the same computation
with the factors exchanged: `θ_s(a x_e) = θ_s(x_e)θ_s(a)`. ∎

*Consistency check (against Phase 1).* Applying the first identity twice:
`θ_s(θ_s(x·a)) = θ_s(θ_s(a)·θ_s(x)) = θ_s(θ_s(x))·θ_s(θ_s(a)) = σ_{2s}(x)·σ_{2s}(a)`,
which agrees with `θ_s² = σ_{2s}` (RGF Lemma 4.4) and the fact that an automorphism
preserves the action. This is a non-trivial cross-check.

**This is NOT commutation — and here is the explicit witness.**
*Statement.* `θ_sρ_a ≠ ρ_{θ_s(a)}θ_s` in general.

*Proof by example (`n = 1`, any `q`, `s = 0`).* Take `x = E_11`, `a = E_12`. Then
`x·a = E_11E_12 = E_12`, so `θ_0(x·a) = E_12^T = E_21`. But
`θ_0(x)·θ_0(a) = E_11^T E_12^T = E_11E_21 = 0` (since `E_ijE_kl = δ_{jk}E_il`). Hence
`θ_0(x·a) = E_21 ≠ 0 = θ_0(x)·θ_0(a)`, while the correct identity holds:
`θ_0(a)·θ_0(x) = E_21E_11 = E_21 = θ_0(x·a)`. ∎

*Computationally verified:* the correct (swapped) identities hold on every tested pair,
while the "commuted" version fails on most pairs — e.g. `60 480 / 65 536` mismatches at
`(4,1,1)` (both `s = 0` and `s = 1`), `3 923 / 4 000` at `(4,1,2)`. The mismatch counts are
reported in the log, so the test cannot pass vacuously.

### 6.5 Semilinearity — **PROVED IN PHASE 2 STAGE 1**

*Statement.* For `c ∈ F_q` (acting as `cI ∈ Z(R)`) and `x ∈ R^n`:

  `σ_k(c·x) = σ_k(c)·σ_k(x)`, `θ_s(c·x) = σ_s(c)·θ_s(x)`, and `T(c·x) = c·T(x)`.

So `σ_k` is `σ_k`-semilinear and `θ_s` is `σ_s`-semilinear over `F_q`; both are
`F_p`-linear. `T` is plain `F_q`-linear.

*Proof.* `c·x_e = (cI)x_e`, so `σ_k(c·x_e) = σ_k(cI)σ_k(x_e) = σ_k(c)·σ_k(x_e)`, using
`σ_k(cI) = σ_k(c)I` (RGF Lemma 4.2) and that `σ_k` is multiplicative. For `θ_s`:
`θ_s(cI·x_e) = θ_s(x_e)θ_s(cI) = θ_s(x_e)·σ_s(c)I = σ_s(c)·θ_s(x_e)`, the middle
equality because `θ_s` is **anti**-multiplicative and `θ_s(cI) = σ_s(c)I` (RGF Lemma 4.3),
and the last because `σ_s(c) ∈ F_q` is central. For `T` this is Lemma 3.3(i). ∎

*Computationally verified:* [SMP]; plus negative controls showing that `σ_k` and `θ_s`
are **not** `F_q`-linear when the Frobenius is non-trivial (mismatch counts reported), and
positive control `T(c x) = c T(x)` for every `c ∈ F_q`.

### 6.6 Out of Stage 1's scope (recorded, not attempted)

**L-6.1** — "`θ_s` is an anti-automorphism of `R_n`" — is **not** proved here. Two
observations, recorded without claim: (i) RGF Lemma 4.3 states `θ_s` is an
anti-automorphism "of `R` (and of `R_n`)", and its proof (`θ_s(XY) = σ_s((XY)^T) =
σ_s(Y^TX^T) = …`) is a matrix computation that applies verbatim to `M_2(B)` once
`σ_s` is extended to `B` fixing `X`; (ii) under `R_n ≅ M_2(B)`, coordinate-wise `θ_s` on
`R_n` agrees with `σ_s ∘ (·)^T` on `M_2(B)`. **No claim is made**; the planning row L-6.1
keeps its status `PROPOSED / UNPROVED` and will be settled in the stage that treats
P-2.7/P-2.8.

---

## 7. Status table (every statement of Stage 1)

| # | Statement | Status | Where | Phase-1 input used |
|---|---|---|---|---|
| 2.1 | `R_n = R[X]/⟨X^n−1⟩` | **PROVED IN PHASE 1** | RGF Lemma 3.1 | — |
| 2.2 | coefficient representation, `ι` bijective, `dim = 4tn` | **PROVED IN PHASE 1** | RGF Lemma 3.1–3.2 | — |
| 2.3 | multiplication = cyclic convolution | **PROVED IN PHASE 2 STAGE 1** | §2 | Lemma 2.4 |
| 2.4 | `X` central; `R_n ≅ M_2(B)`, `B` commutative | **PROVED IN PHASE 1** (= L-2.1.1, T-033) | RGF Lemma 3.1 | — |
| 2.5 | `emb` injective ring hom; `ι` additive, right/left `R`-linear; `ι(Tx) = ι(x)X` | **PROVED IN PHASE 2 STAGE 1** | §2 | Lemma 2.4 |
| 3.1 | the two actions, bimodule laws, `F_q`-structure | **PROVED IN PHASE 1** | RGF Def. 5.1, §5.6.2 | — |
| 3.2 | the shift convention `(Tx)_e = x_{e−1}` | **PROVED IN PHASE 1** | RGF §0.2, Lemma 3.2 | — |
| 3.3 | `T` `F_q`-linear, bijective, `T^n = id`, Hamming isometry | **PROVED IN PHASE 2 STAGE 1** (iii: Phase 1) | §3 | — |
| 3.4 | `T` right `R`-linear (P-2.1a) | **PROVED IN PHASE 2 STAGE 1** | §3 | — |
| 3.5 | `T` left `R`-linear (P-2.1b) | **PROVED IN PHASE 2 STAGE 1** | §3 | — |
| 3.6 | `T` = right **and** left multiplication by `X` (P-2.1g) | **PROVED IN PHASE 1** (right) + **STAGE 1** (left) | §3 | Lemma 2.4 |
| 3.7 | `T` left `R_n`-linear (free) / right `R_n`-linear (iff central) | **PROVED IN PHASE 2 STAGE 1** | §3 | Lemma 2.4 |
| 4.1 | right ideals ↔ `T`-invariant right `R`-submodules (bijection) | **PROVED IN PHASE 2 STAGE 1** | §4 | 2.2, 2.4, 2.5 |
| 4.2 | boundary `n = 1`; no squarefree hypothesis needed | **PROVED IN PHASE 2 STAGE 1** | §4.2 | — |
| 4.3(a) | right `R`-submodule, not `T`-invariant ⇒ not a right ideal | **PROVED IN PHASE 2 STAGE 1** | §4.3 | — |
| 4.3(b) | `T`-invariant `F_q`-subspace need not be a right ideal | **COMPUTATIONALLY VERIFIED ONLY** | §4.3, §8 | — |
| 4.3(c) | `T`-invariant **left** `R`-submodule need not be a right ideal | **PROVED IN PHASE 2 STAGE 1** | §4.3 | Lemma 3.5 |
| 5.1 | `L_XR_X = R_XL_X` (free); `L_X = R_X` iff central; `XT = TX` | **PROVED IN PHASE 2 STAGE 1** | §5.1 | Lemma 2.4 |
| 5.2 | left and right multiplication by `X` give the same shift | **PROVED IN PHASE 1** + **STAGE 1** | §5.2 | Lemma 2.4 |
| 5.3 | what fails without centrality (five items) | **PROVED IN PHASE 2 STAGE 1** (comparison) | §5.3 | — |
| 6.2 | `Tσ_k = σ_kT`, `Tθ_s = θ_sT` (P-2.1c) | **PROVED IN PHASE 2 STAGE 1** | §6.2 | — |
| 6.3 | `σ_kρ_a = ρ_{σ_k(a)}σ_k`, `σ_kλ_a = λ_{σ_k(a)}σ_k` (P-2.1d) | **PROVED IN PHASE 2 STAGE 1** | §6.3 | RGF Lemma 4.2 |
| 6.4 | `θ_sρ_a = λ_{θ_s(a)}θ_s`, `θ_sλ_a = ρ_{θ_s(a)}θ_s` (P-2.1e); and `θ_sρ_a ≠ ρ_{θ_s(a)}θ_s` | **PROVED IN PHASE 2 STAGE 1** | §6.4 | RGF Lemma 4.3 |
| 6.5 | `σ_k(cx) = σ_k(c)σ_k(x)`, `θ_s(cx) = σ_s(c)θ_s(x)`, `T(cx) = cT(x)` | **PROVED IN PHASE 2 STAGE 1** | §6.5 | RGF Lemma 4.2 |
| — | L-6.1: `θ_s` anti-automorphism of `R_n` | **PROPOSED / UNPROVED** (out of Stage 1 scope) | planning row L-6.1 | — |
| — | P-2.1f (`rev`): ring automorphism of `R_n`, `rev T = T^{-1}rev`, `rev(ann_r v) = ann_r(rev v)` | **PROPOSED / UNPROVED** (Stage 1 did not treat `rev`; it is needed only for P-2.7) | `PHASE2_PROPOSAL_v2.md` §2 | — |
| — | P-2.3, P-2.4, P-2.5, P-2.6, P-2.7, P-2.8, C-2.1 | **PROPOSED / UNPROVED** (out of Stage 1 scope) | `PHASE2_PROPOSAL_v2.md` | — |

---

## 8. Computational verification (Stage-1 focused tests only)

### 8.1 The script and its log

* Script: `04_COMPUTATION/phase2_stage1_shift_checks.py`
* Log: `04_COMPUTATION/phase2_stage1_shift_log.txt`
* Run from its own directory: `cd 04_COMPUTATION && python3 phase2_stage1_shift_checks.py`
  (it imports `ring_structure_checks`, which must sit beside it, and writes the log to the
  current directory).
* Arithmetic (`Field`, `Local`, `MatRing`) and `F_q`-linear algebra (`rref`,
  `enumerate_subspaces`) are imported from `ring_structure_checks.py` (401/401 there);
  `B = A_t[X]/⟨X^n−1⟩`, `M_2(B)`, `ι`, `T` and every check are built here from scratch.
* Seed `20261104`; all sampling deterministic.

### 8.2 Result

**553 checks, 553 PASS, 0 FAIL** — of which **91 `[EXH]`** (exhaustive) and
**462 `[SMP]`** (sampled, with the sample size, the budget and the seed printed on every
line).

Reproducibility: two consecutive runs produced **byte-identical** logs
(SHA-256 `98383c76c957b2f4b613d97b8889c4bb39eebecf2c616edf48bc1fb1d9c5c3ef`,
`phase2_stage1_shift_log.txt`), wall time ≈ 100 s per run.

### 8.3 Parameter sets (all admissible: `r ≥ 2`, `t ≥ 1`, `n ≥ 1`)

| `(q,t,n)` | `dim_{F_q} R^n` | `|R^n|` | Coverage |
|---|---|---|---|
| `(4,1,1)` | 4 | 256 | **fully exhaustive** (all vectors, all `a ∈ R`, all `Z ∈ R_n`, all `65 536` pairs); plus the brute-force census over all `529` `F_q`-subspaces |
| `(4,1,2)` | 8 | 65 536 | all `B`-pairs exhaustive; all `65 536` vectors for `T = ` right multiplication by `X`; pairs sampled |
| `(4,1,3)` | 12 | 1.7 × 10⁷ | sampled |
| `(9,1,1)` | 4 | 6 561 | **fully exhaustive** (all vectors, all `a`, all `Z`) |
| `(9,1,2)` | 8 | 4.3 × 10⁷ | sampled |
| `(4,2,1)` | 8 | 65 536 | all `65 536` vectors for `T = ` right multiplication by `X`; rest sampled (`t = 2`) |
| `(4,2,2)` | 16 | 4.3 × 10⁹ | sampled (**wild case**: `p ∣ n` and `t ≥ 2`; Stage 1 makes no structural claim there and none is needed) |
| `(8,1,2)` | 8 | 1.7 × 10⁷ | sampled (`r = 3`, so `θ_s` is not an involution) |

All `k, s` mod `r` are tested at every parameter set.

### 8.4 What is checked (per parameter set)

* **Part 0** — `ι` is a bijection and agrees with the coefficient rearrangement;
  `B`-multiplication is the cyclic convolution; `B` commutative; `X^n = 1`; `(XI)^n = I`;
  **centrality of `X`**; `emb` is an injective ring homomorphism; `ι` is additive and
  right/left `R`-linear; `L_XR_X = R_XL_X`; `L_X = R_X`; the right ideal generated by `1`
  is all of `R_n`.
* **Part 1** — `T^n = id`; `T` bijective; `T = ` right and = left multiplication by `X`;
  Hamming isometry; `F_q`-linearity (additive and scalar); **right and left
  `R`-linearity**; right and left `R_n`-linearity; **negative control** with a non-central
  `Y = E_11` (mismatches expected) and the positive control `Y = XI` (0 mismatches).
* **Part 2** — the two directions of Theorem 4.1, both round trips, and the three negative
  controls of §4.3; plus the exhaustive subspace census at `(4,1,1)`.
* **Part 3** — `Tσ_k = σ_kT`, `Tθ_s = θ_sT`; `σ_k` preserves both sides; `θ_s` swaps both
  sides; the **negative controls** that `θ_s` is not a commutation and is not `F_q`-linear;
  semilinearity of `σ_k`, `θ_s` and `F_q`-linearity of `T`; and the Phase-1 ring-level
  inputs on `R` (`σ_k` automorphism, `θ_s` anti-automorphism, `θ_s² = σ_{2s}`,
  `σ_kθ_s = θ_sσ_k`).
* **Part 4** (at `n = 1`) — `T = id`; `X = 1`; `ι` is the coefficient embedding; the two
  actions are the two actions of `R` on itself.

**A passing script is evidence, not proof.** Every statement above is proved in §2–§6; the
script's role is to catch convention errors (wrong side, wrong shift direction, wrong
`θ_s` placement), which is why the negative controls are mandatory: without them, a test
that compares the wrong two quantities could still "pass".

---

## 9. Stage-1 report

### 9.1 Proved in Stage 1

1. The coefficient representation of `R_n` and the convolution formula (Lemma 2.3).
2. `ι` is an isomorphism of `(R,R)`-bimodules between `R^n` (coordinate-wise actions) and
   `R_n` (embedded `R` acting on both sides), and `ι(Tx) = ι(x)X` (Lemma 2.5).
3. `T` is `F_q`-linear, bijective, a Hamming isometry, `T^n = id` (Lemma 3.3).
4. `T` is right `R`-linear **and** left `R`-linear, by coordinate proofs that use no
   hypothesis at all (Lemmas 3.4, 3.5). Hence "closed under `T`" is convention-free.
5. `T` = right multiplication by `X` (Phase 1) = left multiplication by `X` (Stage 1, uses
   centrality) (Lemma 3.6).
6. `T` is left `R_n`-linear for free and right `R_n`-linear iff `X` is central (Lemma 3.7).
7. **Theorem 4.1**: the equivalence between right ideals of `R_n` and `T`-invariant right
   `R`-submodules of `R^n`, with both directions proved, all boundary cases (`n = 1`,
   `C = 0`, `C = R^n`, `p ∣ n`) and counterexamples showing both conditions are needed.
8. Centrality: `L_XR_X = R_XL_X` (associativity), `L_X = R_X` iff central, and therefore
   the operator identity `XT = TX` in the precise sense of §5.1; plus the five-item
   analysis of what fails without centrality (§5.3).
9. Automorphism compatibility: `Tσ_k = σ_kT`, `Tθ_s = θ_sT` (commutation);
   `σ_kρ_a = ρ_{σ_k(a)}σ_k`, `σ_kλ_a = λ_{σ_k(a)}σ_k` (side preserved);
   **`θ_sρ_a = λ_{θ_s(a)}θ_s`** and `θ_sλ_a = ρ_{θ_s(a)}θ_s` (**side swapped**, with an
   explicit witness that this is not commutation); semilinearity of `σ_k` and `θ_s` and
   `F_q`-linearity of `T`.

Together these discharge, in whole or in part, the planning rows **L-2.1.1, P-2.1a,
P-2.1b, P-2.1c, P-2.1d, P-2.1e, P-2.1g** and the commutation table **TBL-2.1** (see §7).

### 9.2 Computational evidence

553/553 checks pass, 91 exhaustive, 462 sampled, byte-reproducible (§8). Highlights:

* the equivalence of Theorem 4.1 tested on both objects and both round trips at eight
  parameter sets, including the wild case `(4,2,2)`;
* an **independent** confirmation at `(4,1,1)`: a brute-force enumeration of all `529`
  `F_q`-subspaces finds exactly `7 = q+3` `T`-invariant right `R`-submodules with
  dimensions `[0,2,2,2,2,2,4]`, matching the Phase-1 Morita count by a different route;
* exhaustive verification of `T = ` right multiplication by `X` over all `65 536` vectors
  at both `(4,1,2)` and `(4,2,1)`;
* negative controls with explicit mismatch counts: non-central `Y = E_11` breaks right
  `R`-linearity (e.g. `59 760/65 536` at `(4,1,1)`) while `Y = XI` does not (`0/65 536`);
  `θ_s` is not a commutation (`60 480/65 536` mismatches at `(4,1,1)`); `σ_1`, `θ_1` are
  not `F_q`-linear.

### 9.3 Limitations and unresolved questions

1. **Scope.** Nothing here touches generator numbers (P-2.3), CRT/Hensel (P-2.4),
   principality (P-2.5/P-2.6), duals (P-2.7/P-2.8) or enumeration (C-2.1). In particular
   the question "is every cyclic code principal?" is **not** addressed; T-021 remains
   `proved (conditional)` and open for `t ≥ 2` or `p ∣ n`.
2. **`rev` (P-2.1f) is not treated.** It is needed only for the dual/annihilator stage;
   the planning row keeps its status `PROPOSED / UNPROVED`.
3. **L-6.1 (`θ_s` anti-automorphism of `R_n`) is not proved here**; see the remark in
   §6.6, which records (without claiming) that RGF Lemma 4.3 may already cover it. To be
   settled in the P-2.7/P-2.8 stage, with CT-0's check `θ_s(uv) = θ_s(v)θ_s(u)` on `R_n`.
4. **Sampling.** Outside `(4,1,1)` and `(9,1,1)` the pair tests are sampled (20 000 pairs,
   fixed seed). Exhaustive confirmation of the pair identities is available only at
   `(4,1,1)` (all 65 536 pairs).
5. **The census at `n = 1` is the only exhaustive subspace enumeration**; at `n ≥ 2` the
   ambient `F_q`-dimension is `≥ 8`, so a brute-force census is infeasible and the
   equivalence was tested by generator/closure comparison instead.
6. **Carried forward per D3 (unchanged, unresolved):** T-006 (entry-wise form,
   uncharacterised), T-027 (general `τ ∈ Aut(A_t)`; the skew-polynomial comparison of
   §5.3(1) is exactly this gap), T-021 (principality), T-011/T-012/T-013/T-014 (hulls,
   Gray map, quantum), warning B3.5, the Phase-1 enumeration coverage gaps (`q = 9, n = 3`;
   `q = 4, t = 2, n = 2`) — **note that `(4,2,2)` is in the wild case and is now covered by
   Stage-1 tests but not by any enumeration**, and the `n ≥ 2` left-submodule gap.
7. **Nothing here is a duality statement.** Stage 1 concerns the shift and the actions
   only; T-042 stays withdrawn (D2) and is not used.

### 9.4 Stop condition

**Stage 1 is complete.** Stage 2 (and any later Phase-2 task, including P-2.3) has **not**
been started and awaits explicit approval.
