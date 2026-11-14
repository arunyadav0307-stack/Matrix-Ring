# Phase 2 — Stage 2C: Galois duality, annihilators and reciprocal generators

**Status of this document.** Stage 2C executes `PHASE2_PROPOSAL_v2.md` §6.1 (**L-6.1**),
§6.2–§6.5 (**P-2.7**, the dual/annihilator formula), §6.6 (**P-2.8**, the explicit
generator) and the consistency checks of §6.5 (C1–C4) together with the cardinality and
double-dual identities of `RING_AND_GALOIS_FOUNDATIONS.md` §6.5–§6.7. Hull dimensions
(Phase 3), hull enumeration (Phase 4), Gray maps (Phase 5) and quantum constructions
(Phase 6) are **out of scope** and are not attempted. Nothing here claims that the
existence of a Galois dual produces a quantum code.

Companion verification: `04_COMPUTATION/phase2_stage2c_galois_duality.py`, log
`04_COMPUTATION/phase2_stage2c_galois_log.txt` (**596 / 596 checks PASS**: 101 `[EXH]`,
495 `[SMP]`, seed `20261107`, two consecutive runs byte-identical, log SHA-256
`00355e7f205de16cbe0a567881a978f326007e564a606663135a71f5103a30ed`, 777 lines).

**Status labels.** `PROVED IN PHASE 1` / `PHASE 2 STAGE 1` / `STAGE 2A` / `STAGE 2B` /
`STAGE 2C`, `IMPORTED RESULT`, `PROPOSED / UNPROVED`, `CONJECTURE`,
`COMPUTATIONALLY VERIFIED ONLY`, `OPEN`. A computation never promotes a statement: every
`PROVED` row below rests on the argument written here.

---

## 0. Scope, conventions, and what is carried in

### 0.1 Standing conventions (unchanged)

* `q = p^r`, `A_t = F_q[u]/⟨u^t⟩`, `R = M_2(A_t)`, `X` **central**,
  `R_n = R[X]/⟨X^n−1⟩`, `B = A_t[X]/⟨X^n−1⟩`, `R_n ≅ M_2(B)` (Stage 2A Lemma 1.3).
* **Right-module convention:** a cyclic code is a **right** ideal of `R_n`.
* **Morita column convention:** `P = B²` as columns; `im M` = the `B`-span of the two
  **columns** of `M`; `I_W = {M : im M ⊆ W}`.
* `ι : R^n → R_n`, `x ↦ Σ_e x_eX^e` (RGF Lemma 3.2) — the identification fixed in §3.1.
* `σ_s(a) = a^{p^s}` on `F_q`, extended to `A_t`, `R`, `R_n` by fixing `u` and `X`;
  `θ_s = σ_s ∘ (·)^T` on `R`, extended **coefficient-wise** to `R^n` and `R_n`.
* `B_s(x,y) = Σ_{e=0}^{n−1} θ_s(x_e)y_e ∈ R`, `b_s = Λ ∘ B_s`, `Λ = λ ∘ tr`,
  `λ` = the coefficient of `u^{t−1}`; `C^{⊥_s} = {y : B_s(x,y) = 0 ∀ x ∈ C}`.
* `rev(x)_e := x_{−e mod n}` on `R^n`; `rev(Σ u_eX^e) := Σ u_{−e}X^e` on `R_n`.

### 0.2 Results imported into Stage 2C

| Ref | Statement | Where | Status |
|---|---|---|---|
| **T-002** | `θ_s = σ_s ∘ (·)^T` is an **anti**-automorphism of `R = M_2(A_t)`; `σ_s` is an automorphism of `A_t` and of `R` | RGF Lemma 4.2, 4.3 | `PROVED IN PHASE 1` |
| **T-037** | `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)`; sesquilinearity of `b_s` | RGF Lemma 6.2, 6.3 | `PROVED IN PHASE 1` |
| **T-007 / Thm 6.6** | the **right radical** of `b_s` is `{0}`; `|C|·|C^{⊥_s}| = |R|^n` and `dim C + dim C^{⊥_s} = 4tn` for every right `R_n`-submodule | RGF Thm 6.6 | `PROVED IN PHASE 1` |
| **T-016 / Thm 6.8** | `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` | RGF Thm 6.8 | `PROVED IN PHASE 1` |
| **T-017 / Cor 6.9** | `C ↦ C^{⊥_s}` is reflexive ⟺ `r ∣ 2s` | RGF Cor 6.9 | `PROVED IN PHASE 1` |
| **T-010 / Lemma 6.7** | `B_s` and `b_s` define the **same** orthogonal | RGF Lemma 6.7 | `PROVED IN PHASE 1` |
| **T-070** | Morita bijection `W ↦ I_W` from `B`-submodules of `B²` onto right ideals of `M_2(B)`, inverse `I ↦ W(I) = Σ_{M∈I} im M`; `|I_W| = |W|²` | Stage 2A Thm 2.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-077 (L-2.3a)** | `xS = I_{im x}` for every `x ∈ M_2(B)` | Stage 2A Lemma 3.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-080 (L-2.3c)** | `im[w_1∣w_2] = Bw_1 + Bw_2` | Stage 2A Lemma 3.6 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-083** | `I_W` is principal ⟺ `μ_B(W) ≤ 2` | Stage 2A Thm 4.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-094–T-097** | squarefree part, Hensel, `F_j = f_j`, CRT decomposition `B ≅ ∏ B_j` | Stage 2B §1 | `PROVED IN PHASE 2 STAGE 2B` |
| **T-102 (L-2.6.4)** | Smith normal form over a finite chain ring; every submodule of `S²` is `≤ 2`-generated | Stage 2B Thm 3.3 | `PROVED IN PHASE 2 STAGE 2B` |
| **T-103 (L-2.6.3)** | `B_j` is a chain ring ⟺ `t = 1` or `p ∤ n` | Stage 2B Thm 3.6 | `PROVED IN PHASE 2 STAGE 2B` |
| **T-104** | `μ_B(W) = max_j μ_{B_j}(W_j)`; Nakayama `μ = dim_K(W/mW)` over a local ring | Stage 2B Lemma 4.2 | `PROVED IN PHASE 2 STAGE 2B` |
| **E-014** | Nakayama's lemma | Atiyah–MacDonald Prop. 2.6 | `IMPORTED RESULT` |

**Not used, and deliberately so.** The register rows **L-6.5** (`|im x| = |im x^T|`) and
**L-6.6** (`B` is Frobenius) were `PROPOSED / UNPROVED`, with L-6.6 an
`IMPORTED RESULT` conditional on verifying an unconfirmed reference. Stage 2C **proves
L-6.5** (Corollary 3.9) *without* L-6.6, from P-2.7 and the Phase-1 size formula alone.
No Frobenius property of `B` is used anywhere in this document.

### 0.3 Out of scope (unchanged)

Hull dimensions and hull enumeration, Gray maps, CSS/EA constructions, and any quantum
parameter. §5 records what the dual theory *will* feed into that work and nothing more.

---

## 1. Task A — L-6.1: `θ_s` is an anti-automorphism of `R_n`

Task A asks for the exact extension of `θ_s` from `R` to `R_n` and for a proof that is
**not** a quotation of the Phase-1 statement for `R`. The three rings are treated
separately and the passage between them is proved.

### 1.1 The three rings

| Ring | Elements | Product |
|---|---|---|
| `R = M_2(A_t)` | matrices | matrix product (`θ_s` known anti on this, T-002) |
| `R[X]` | polynomials `Σ_e u_eX^e`, `u_e ∈ R`, `X` central | convolution `(uv)_e = Σ_{a+b=e}u_av_b` |
| `R_n = R[X]/⟨X^n−1⟩` | classes mod `X^n−1`; normal form `Σ_{e<n}u_eX^e` | convolution with indices mod `n` |

### 1.2 Definition of `θ_s` on each

**Definition 1.1.** On `R`: `θ_s(A) = σ_s(A^T)` (Phase 1, T-002). On `R[X]` and on `R_n`:

```
θ_s( Σ_e u_e X^e )  :=  Σ_e θ_s(u_e) X^e .
```

`θ_s` is applied to the **coefficients** and **fixes `X`** (and hence fixes `u`, since
`θ_s(uI) = σ_s(u)I = uI`). On `R^n` the same formula reads `θ_s(x)_e = θ_s(x_e)`.

### 1.3 Additivity, semilinearity, bijectivity, inverse

**Lemma 1.2.** `θ_s : R[X] → R[X]` and `θ_s : R_n → R_n` are additive, `F_p`-linear,
`σ_s`-semilinear over `F_q`, and bijective, with `θ_s^{-1} = σ_{−2s} ∘ θ_s`.

*Proof.* Additivity is clear coefficient-wise. Semilinearity: for `c ∈ F_q`,
`θ_s(c·Σ u_eX^e) = Σ θ_s(cu_e)X^e = Σ σ_s(c)θ_s(u_e)X^e = σ_s(c)·θ_s(Σ u_eX^e)`, using
`θ_s(cA) = σ_s(c)θ_s(A)` on `R` (RGF Lemma 4.3). `σ_s` fixes `F_p`, so `θ_s` is
`F_p`-linear. Bijectivity: `σ_{−2s}θ_s` is a two-sided inverse because
`θ_s² = σ_{2s}` (Lemma 1.6 below) and `σ_kθ_s = θ_{s+k} = θ_sσ_k` (RGF §4.7):
`σ_{−2s}θ_sθ_s = σ_{−2s}σ_{2s} = id` and `θ_s(σ_{−2s}θ_s(X)) = σ_{−2s}(θ_s²(X)) = X`. ∎

### 1.4 Anti-multiplicativity — the three ingredients

**Theorem 1.3 (L-6.1).** For all `u, v ∈ R_n`, `θ_s(uv) = θ_s(v)θ_s(u)`; i.e. `θ_s` is an
**anti-automorphism** of `R_n`.

*Proof (direct, on the normal forms).* Write `u = Σ_a u_aX^a`, `v = Σ_b v_bX^b`. Because
`X` is **central**,

```
(uv)_e = Σ_{a+b=e} u_a v_b                                      (convolution)
```

— the coefficient `u_a ∈ R` commutes with `X^b`, so `u_aX^a·v_bX^b = u_av_b X^{a+b}`.
Applying Definition 1.1 and the fact that `θ_s` is an anti-automorphism of `R` (T-002):

```
θ_s((uv)_e) = Σ_{a+b=e} θ_s(u_av_b) = Σ_{a+b=e} θ_s(v_b) θ_s(u_a)      (*)
```

— note the **order**: inside each coefficient the `v`-factor comes first. This is the
matrix-order ingredient: `θ_s(u_av_b) = σ_s((u_av_b)^T) = σ_s(v_b^T u_a^T) =
σ_s(v_b^T)σ_s(u_a^T) = θ_s(v_b)θ_s(u_a)`; the reversal is the transpose.

On the other hand, with `θ_s(v)_a = θ_s(v_a)` and `θ_s(u)_b = θ_s(u_b)`,

```
(θ_s(v) θ_s(u))_e = Σ_{a+b=e} θ_s(v_a) θ_s(u_b) .                       (**)
```

The index set `{(a,b) : a+b=e}` is stable under the bijection `(a,b) ↦ (b,a)`, and under
that substitution `(*)` becomes `(**)`. Hence `θ_s((uv)_e) = (θ_s(v)θ_s(u))_e` for every
`e`, which is `θ_s(uv) = θ_s(v)θ_s(u)`. ∎

**Where each ingredient enters (the checklist of Task A).**

1. *Matrix multiplication order* — inside `θ_s(u_av_b) = θ_s(v_b)θ_s(u_a)` (T-002).
2. *Polynomial coefficient multiplication* — the convolution `(uv)_e = Σ u_av_b`, which
   needs `X` **central**.
3. *Centrality of `X`* — used in (2) and again in §1.5, where it makes `⟨X^n−1⟩` a
   two-sided ideal.
4. *The relation `X^n = 1`* — the reduction `X^{e} ↦ X^{e mod n}` in the quotient: the
   convolution is modulo `n` in `R_n` and over `N` in `R[X]`.
5. *Preservation of `⟨X^n−1⟩`* — §1.5.
6. *Well-definedness on the quotient* — §1.5.
7. *Additivity, bijectivity, inverse* — Lemma 1.2.
8. *`θ_s²` and the order* — Lemma 1.6.

**The same argument verbatim** proves:

**Corollary 1.4.** `θ_s` is an anti-automorphism of the polynomial ring `R[X]`. (The
proof never used the reduction mod `X^n−1`.)

### 1.5 Preservation of the ideal and well-definedness on the quotient

**Lemma 1.5.** (i) `θ_s(X^n − 1) = X^n − 1`. (ii) The ideal `⟨X^n−1⟩ ⊆ R[X]` is
**two-sided** and `θ_s` maps it onto itself. (iii) `θ_s` descends to a well-defined
anti-automorphism of `R_n`, and the descended map **is** the coefficient-wise map of
Definition 1.1.

*Proof.* (i) `θ_s` fixes `X` (Definition 1.1) and fixes `1`, and is additive.

(ii) `X^n − 1` is central in `R[X]`: `X` is central by standing convention and `1` is
central, so every left multiple `p·(X^n−1)` equals the right multiple `(X^n−1)·p`; hence
`⟨X^n−1⟩` is two-sided. Let `y = m·(X^n−1) ∈ ⟨X^n−1⟩` (every element of the ideal has
this form, and also the form `(X^n−1)·m'`). By Corollary 1.4 and (i),

```
θ_s(y) = θ_s(X^n−1) · θ_s(m) = (X^n−1)·θ_s(m) ∈ ⟨X^n−1⟩ .
```

So `θ_s(⟨X^n−1⟩) ⊆ ⟨X^n−1⟩`, and applying the same to `θ_s^{-1}` gives equality.

(iii) If `p ≡ q mod ⟨X^n−1⟩` then `p−q ∈ ⟨X^n−1⟩`, so `θ_s(p) − θ_s(q) = θ_s(p−q) ∈
⟨X^n−1⟩`, i.e. `θ_s(p) ≡ θ_s(q)`: the map on classes is well defined, and it is
anti-multiplicative, additive and bijective because `θ_s` on `R[X]` is. Finally, if
`Σ_{e<n}u_eX^e` is the normal form of a class, its image is `Σ_{e<n}θ_s(u_e)X^e`, which
is exactly Definition 1.1 — the descended map and the coefficient-wise map coincide. ∎

### 1.6 Square, inverse and order

**Lemma 1.6.** On `R_n` (and on `R[X]`): `θ_s² = σ_{2s}`; `θ_s^{2k} = σ_{2ks}` and
`θ_s^{2k−1} = θ_{(2k−1)s}`; `ord(θ_s) = 2r/gcd(r,2s)` — the same order as on `R`.

*Proof.* `θ_s²(Σ u_eX^e) = Σ θ_s²(u_e)X^e = Σ σ_{2s}(u_e)X^e = σ_{2s}(Σ u_eX^e)` by RGF
Lemma 4.4 (`θ_s² = σ_{2s}` on `R`) and because `σ_{2s}` also fixes `X`. The power formulas
follow by induction using `σ_kθ_{s'} = θ_{s'+k}`.

For the order: let `k ≥ 1`. If `θ_s^k = id` on `R_n`, then restricting to the constant
polynomials gives `θ_s^k = id` on `R`; conversely if `θ_s^k = id` on `R` then, coefficient
by coefficient, `θ_s^k = id` on `R_n`. Hence the orders on `R` and `R_n` coincide, and
RGF Lemma 4.4 gives `2r/gcd(r,2s)`. Note `θ_s` is **never** the identity (for `s ≡ 0`,
`θ_0` is the transpose, of order `2`). ∎

### 1.7 The three levels, distinguished

| Level | Statement | Proved by |
|---|---|---|
| `R = M_2(A_t)` | `θ_s` anti-automorphism; `θ_s² = σ_{2s}` | Phase 1 (T-002, RGF 4.3–4.4) — imported, not re-proved |
| `R[X]` | `θ_s` anti-automorphism, coefficient-wise, `X` fixed | Corollary 1.4 (proved here) |
| `R_n = R[X]/⟨X^n−1⟩` | `θ_s` anti-automorphism, well defined because `θ_s` fixes `X^n−1` and the ideal is two-sided | Theorem 1.3 + Lemma 1.5 (proved here) |

The passage `R → R[X]` needs the index swap; the passage `R[X] → R_n` needs the
**preservation of the ideal**, which is *not* automatic: it holds because `θ_s` fixes the
central element `X^n−1`. (For a general anti-automorphism `τ` of `R` extended
coefficient-wise, `τ` descends to `R[X]/⟨f⟩` iff `τ(f) ∈ ⟨f⟩`; here `τ = θ_s` and
`f = X^n−1` is fixed.)

### 1.8 What is not claimed

`θ_s` is `F_p`-linear and `σ_s`-semilinear; it is **not** `F_q`-linear unless `r ∣ s`. It
is an anti-automorphism of the **ring** `R_n`, not an anti-automorphism of the
`B`-algebra structure: it fixes `X` and sends a `B`-submodule to a `B`-submodule only up
to the semilinear twist (used in §3.8). Also, `θ_s` is not `B`-linear in the sense of
commuting with left multiplication by `B` — see Stage 1 §6.1 ("swaps the side").

---

## 2. Task B — annihilator conventions

### 2.1 Definitions (four objects and two kernels)

For a **subset** `S ⊆ R_n`:

```
ann_r(S) := {a ∈ R_n : x a = 0 for every x ∈ S}      ("a sits on the right of x")
ann_l(S) := {a ∈ R_n : a x = 0 for every x ∈ S}      ("a sits on the left of x")
```

For a single element `v`: `ann_r(v) := ann_r({v}) = {w : vw = 0}` and
`ann_l(v) := {w : wv = 0}`. Both are additive subgroups (the ring is finite, so no
finiteness subtleties arise). The two kernels are:

```
ker( L_v ) = ker( w ↦ v w ) = ann_r(v) ,      ker( R_v ) = ker( w ↦ w v ) = ann_l(v) ,
```

where `L_v` (resp. `R_v`) is **left** (resp. **right**) multiplication by `v`. Note the
mnemonic trap: the *right* annihilator is the kernel of *left* multiplication.

### 2.2 The ideal-side laws

**Theorem 2.1 (side laws).** Let `I ⊆ R_n` be an additive subgroup.

1. `ann_r(I)` is **always a right ideal**.
2. If `I` is a **right** ideal, then `ann_r(I)` is also a **left** ideal — hence a
   two-sided ideal.
3. `ann_l(I)` is **always a left ideal**.
4. If `I` is a **left** ideal, then `ann_l(I)` is also a **right** ideal — hence
   two-sided.
5. `ann_r({v})` is a right ideal and `ann_l({v})` is a left ideal (the case `I = {v}` of
   (1) and (3)).

*Proof.* (1) Let `a ∈ ann_r(I)` and `r ∈ R_n`. For every `x ∈ I`, `x(ar) = (xa)r = 0`;
no property of `I` is used. (2) If moreover `I` is a right ideal, then `xr ∈ I` for every
`x ∈ I`, so `x(ra) = (xr)a = 0`, i.e. `ra ∈ ann_r(I)`. (3) `(ra)x = r(ax) = 0`. (4) If
`I` is a left ideal then `rx ∈ I`, so `(ar)x = a(rx) = 0`. (5) is immediate. ∎

**Warning.** The words "right" and "left" in `ann_r` / `ann_l` refer to the **side on
which `a` is placed relative to `x`**, not to the side of the resulting ideal. The table
in the log (`[SMP] … ann_r(v) is a RIGHT ideal`, `ann_r of a RIGHT ideal is two-sided`)
records both, and they are different statements.

### 2.3 Element, right ideal, left ideal — three genuinely different objects

**Lemma 2.2 (left ideals are determined by their generators).** Let `J = Σ_i R_n x_i` be
the **left** ideal generated by `x_1,…,x_k`. Then `ann_r(J) = ⋂_i ann_r(x_i)`. In
particular `ann_r(R_n g) = ann_r(g)`.

*Proof.* `⊆` is clear. For `⊇`: let `a ∈ ⋂_i ann_r(x_i)`; an element of `J` has the form
`Σ_i r_i x_i`, and `(Σ_i r_ix_i)a = Σ_i r_i(x_ia) = 0`. ∎

**Lemma 2.3 (right ideals are not).** Let `I = gR_n`. Then
`ann_r(I) = {a : g·R_n·a = 0} ⊆ ann_r(g)`, and the inclusion is **strict in general**.

*Proof.* `⊆`: take `m = 1` in `gma = 0`. Strictness: an explicit counterexample over
`F_4` (so `R_n = M_2(F_4)`, `n = 1`). Let `v = E_12`. Then `ann_r(v) = {w : vw = 0} =
{[[a,b],[0,0]]}` (top-row matrices), of size `4² = 16`, whereas `vR_n` is also the set of
top-row matrices and `ann_r(vR_n) = {a : xa = 0 ∀ x}` vanishes on `E_11` and `E_12`,
forcing `a = 0`. So `ann_r(vR_n) = {0} ⊊ ann_r(v)`. The reason is the plain
noncommutative identity `(gm)a = g(ma)`: `ga = 0` says nothing about `g(ma)`. ∎

**Computational confirmation.** `[EXH]`/`[SMP]`: `ann_r(R_n g) = ann_r(g)` for every
probe at every parameter set; `ann_r(gR_n) ⊊ ann_r(g)` for `19` of `25` probes at
`(4,1,1)`; `ann_r(v) ≠ ann_l(v)` for `19` of `25` probes.

### 2.4 Which annihilator belongs to a right ideal, and why

Let `C ⊆ R_n` be a **right** ideal (a cyclic code). Three candidates:

| Candidate | Side | Verdict |
|---|---|---|
| `ann_r(C)` | two-sided by Thm 2.1(1)+(2) | **wrong object**: too small, and it is a left ideal, whereas `C^{⊥_s}` is a right ideal |
| `ann_l(C)` | left ideal | **wrong side** entirely |
| `ann_r(θ_s(C))`, where `θ_s(C)` is a **left** ideal | **right ideal** by Thm 2.1(1) | **correct** — this is P-2.7 |

The decisive structural point: `θ_s` is an anti-automorphism, so it **converts the right
ideal `C` into a left ideal** `θ_s(C)`; and by Lemma 2.2 a left ideal's right annihilator
is determined by its generators. That is exactly why the single generator `g` of
`C = gR_n` suffices in P-2.7, whereas `ann_r(C)` would not be determined by `g`
(Lemma 2.3). The formula of §3.8 makes this precise and covers the non-principal case.

---

## 3. Task C — P-2.7: the Galois dual as a reversed annihilator

### 3.1 The identification `ι`, fixed

`ι : R^n → R_n`, `ι(x) = Σ_e x_eX^e` (RGF Lemma 3.2), is an `F_q`-linear bijection and a
ring isomorphism for the **convolution** product on `R^n`; under it, a cyclic code
(right `R`-submodule of `R^n` closed under the shift) is exactly a right ideal of `R_n`
(Stage 1). All computations below identify `C ⊆ R^n` with `ι(C) ⊆ R_n`, and
`ι(rev y) = rev(ι y)` (verified, `[SMP] 100 words` per case).

### 3.2 Coefficient expansion

Let `C = gR_n` with `g = Σ_a g_aX^a`, `g_a ∈ R`, and let `y ∈ R^n`, `m ∈ R_n`. Write
`x = gm ∈ C`. Since `X` is central, the coefficient of `X^e` in `gm` is

```
(gm)_e = Σ_{a+b=e} g_a m_b .                                            (3.1)
```

### 3.3 The convolution equations

**Step 1 (expand).** By (3.1), `x_e = Σ_{a+b=e}g_am_b`.

**Step 2 (apply `θ_s`).** By Theorem 1.3 and Definition 1.1, coefficient-wise,

```
θ_s(x_e) = Σ_{a+b=e} θ_s(g_a m_b) = Σ_{a+b=e} θ_s(m_b) θ_s(g_a) ,       (3.2)
```

the `m`-factor first (anti-multiplicativity, Theorem 1.3).

**Step 3 (form the pairing and re-index).** With `B_s(x,y) = Σ_e θ_s(x_e)y_e`,

```
B_s(gm, y) = Σ_e Σ_{a+b=e} θ_s(m_b) θ_s(g_a) y_e
           = Σ_b θ_s(m_b) ( Σ_a θ_s(g_a) y_{a+b} )
           = Σ_b θ_s(m_b) z_b = B_s(m, z) ,                              (3.3)
```

where `z ∈ R^n` is defined by

```
z_b := Σ_a θ_s(g_a) y_{a+b}     (indices mod n).                         (3.4)
```

The only reassociation used is `θ_s(m_b)θ_s(g_a)y_e = θ_s(m_b)(θ_s(g_a)y_e)`; the order
`θ_s(m_b)·θ_s(g_a)` is kept, and `z_b` is a **left** factor's coefficient times `y` — no
commutativity is used anywhere. Equation (3.4) is the system of `n` convolution equations
announced in Task C(3).

### 3.4 Non-degeneracy: the exact Phase-1 input

**Step 4.** `y ∈ C^{⊥_s}` ⟺ `B_s(gm,y) = 0` for all `m ∈ R_n` ⟺ `B_s(m,z) = 0` for all
`m` ⟺ `z = 0`, the last step because the **right** radical of `B_s` is trivial
(Phase 1, RGF Thm 6.6, T-007): for `z ≠ 0` there is `m` with `B_s(m,z) ≠ 0`.

*This is the one and only external input used in the proof of P-2.7* (besides L-6.1 and
the properties of `rev`). In particular no Frobenius property of `B` and no
`|gR_n| = |R_ng|` lemma is used. By RGF Lemma 6.7 the `R`-valued and the `F_q`-valued
forms define the same orthogonal, so the computation may be done with either.

### 3.5 From `z` to a product: the exact role of `rev`

**Step 5.** Let `w := ι^{-1}(rev(ι(y)))`, i.e. `w_f = y_{−f}` (all indices mod `n`). Then

```
[ θ_s(g) · ι(w) ]_k = Σ_{a+f=k} θ_s(g_a) w_f = Σ_a θ_s(g_a) y_{a−k} = z_{−k} ,
```

so `ι(z) = rev( θ_s(g) · rev(ι(y)) )`, where `rev` on `R_n` is the ring automorphism
`Σ u_eX^e ↦ Σ u_{−e}X^e` (Proposition 3.6 below).

**Step 6.** Since `rev` is injective, `z = 0 ⟺ θ_s(g)·rev(ι(y)) = 0 ⟺
rev(ι(y)) ∈ ann_r(θ_s(g)) ⟺ ι(y) ∈ rev(ann_r(θ_s(g)))` (using `rev² = id`).

### 3.6 The formula

**Theorem 3.5 (P-2.7, proved).** Let `C = gR_n ⊆ R_n` be a principal right ideal and
`s` arbitrary. Under `ι`:

```
C^{⊥_s}  =  rev( ann_r( θ_s(g) ) )                                   (form 1)
         =  ann_r( θ_s( rev g ) )                                    (form 2)
         =  { y ∈ R^n : θ_s(g) · rev(ι(y)) = 0 in R_n } .            (form 3)
```

Moreover, in Morita terms,

```
ann_r(θ_s(g)) = I_{ker θ_s(g)} := {M ∈ M_2(B) : both columns of M lie in ker θ_s(g)},
```

so `dim_{F_q} C^{⊥_s} = 2 dim_{F_q} ker(θ_s(g))` and `|C^{⊥_s}| = |ker θ_s(g)|²`.

*Proof.* Steps 1–6 above give form 1 and form 3 (form 3 is the same statement before
applying `rev` to the set). Form 2 follows from form 1 by
`rev(ann_r(v)) = ann_r(rev v)` (P-2.1f(iv), proved as Proposition 3.6(iv) below) together
with `rev θ_s = θ_s rev` (Proposition 3.6(iii)):
`rev(ann_r(θ_s(g))) = ann_r(rev(θ_s(g))) = ann_r(θ_s(rev g))`.

For the Morita form: `ann_r(v) = {M : vM = 0} = {M : every column of M lies in ker v} =
I_{ker v}` by the definition of `I_W` and the column convention; the dimension and
cardinality statements are `|I_W| = |W|²` (Stage 2A T-070 / RGF Prop. 2.6). ∎

**Proposition 3.6 (`rev`, = P-2.1f, register T-066 — proved here).** Let
`rev(Σ u_eX^e) := Σ u_{−e}X^e` on `R_n` and `rev(y)_e := y_{−e}` on `R^n`. Then

1. `rev` is `F_q`-linear, `rev² = id`, and `rev T = T^{−1} rev` on `R^n`;
2. `rev` is a ring **automorphism** of `R_n`: `rev(uv) = rev(u)rev(v)`;
3. `rev(X) = X^{n−1} = X^{−1}`, `rev|_R = id`, and `rev σ_k = σ_k rev`,
   `rev θ_s = θ_s rev`;
4. `rev(ann_r(v)) = ann_r(rev v)`;
5. `ι(rev y) = rev(ι y)`.

*Proof.* (1) Permutation of coordinates; `rev² = id` because `−(−e) = e`; for `T`:
`(rev Tx)_e = (Tx)_{−e} = x_{−e−1} = (T^{−1} rev x)_e`.

(2) `rev` is the substitution `X ↦ X^{n−1}`: since `X` is central and
`(X^{n−1})^n = (X^n)^{n−1} = 1`, the assignment `X ↦ X^{n−1}` extends to a ring
endomorphism of `R[X]/⟨X^n−1⟩` (it sends the relation to a consequence of itself), it
acts on the coefficients as the identity, and it is exactly `rev` on normal forms.
Explicitly: `(uv)_e = Σ_{a+b=e}u_av_b` gives
`rev(uv)_e = Σ_{a+b=−e}u_av_b = Σ_{a'+b'=e}u_{−a'}v_{−b'} = (rev(u)rev(v))_e` via
`(a,b) ↦ (−a,−b)`. Note the order is **preserved**: `rev` is an automorphism, **not** an
anti-automorphism. Consequently `rev` maps right ideals to right ideals.

(3) `rev(X) = X^{−1 mod n} = X^{n−1}`; constants are fixed; `σ_k` and `θ_s` act on
coefficients while `rev` permutes the `X`-monomials, and `σ_k`, `θ_s` fix `X`, so they
commute with `rev`.

(4) Since `rev` is an automorphism, `vw = 0 ⟺ rev(v)rev(w) = 0`, so `w ∈ ann_r(v) ⟺
rev(w) ∈ ann_r(rev v)`, i.e. `rev(ann_r(v)) = ann_r(rev v)` (`rev² = id`).

(5) Direct from the definitions: `ι(rev y)_{ij} = Σ_e y_{−e}X^e = Σ_e y_eX^{−e}`. ∎

**Remark 3.7 (`rev` is trivial iff `n ≤ 2`).** On `R_n`, `rev = id` exactly when `−e ≡ e
(mod n)` for all `e`, i.e. `n ≤ 2`. So the reversal in P-2.7 is vacuous for `n = 1, 2`
and load-bearing for `n ≥ 3`. The log records this: at `(4,1,3)` and `(4,2,3)`, `92` and
`108` of `200` sampled `g` have `rev(ann_r(θ_s(g))) ≠ ann_r(θ_s(g))`, i.e. **the
reversal genuinely matters**; at `(4,1,1)`, `(4,1,2)`, `(4,2,1)`, `(9,1,2)`, `(8,1,2)`,
`(4,2,2)` (all `n ≤ 2`) every `g` is `rev`-stable, as it must be. This closes the gap the
proposal flagged in §6.4(6): its worked example was `rev`-stable and therefore did not
test the reversal.

### 3.7 Where `θ_s` acts

`θ_s` is applied **to the generator `g` only**, never to `y` (or to the dual vector). This
is visible in (3.2): `θ_s` hits the `g_a`, and `y` enters only through `z_b`. The negative
controls neg-5 (omit `θ_s`) and neg-7 (swap the two slots of the pairing) both fail, as
they must.

### 3.8 Non-principal right ideals — the general formula

**Theorem 3.8 (general P-2.7).** Let `C ⊆ R_n` be **any** right ideal (not necessarily
principal), generated as a right ideal by `g_1,…,g_k` (finite, since `R_n` is finite).
Then for every `s`,

```
C^{⊥_s} = rev( ann_r( θ_s(C) ) ) = rev( ⋂_{i=1}^k ann_r( θ_s(g_i) ) ) .
```

*Proof.* Repeat Steps 1–3 for each generator: `B_s(g_im, y) = B_s(m, z^{(i)})` with
`z^{(i)}_b = Σ_a θ_s((g_i)_a) y_{a+b}`. Hence `y ∈ C^{⊥_s}` ⟺ `z^{(i)} = 0` for all `i`
⟺ `θ_s(g_i)·rev(ι(y)) = 0` for all `i` ⟺ `rev(ι(y)) ∈ ⋂_i ann_r(θ_s(g_i))`. Finally
`θ_s(C) = Σ_i R_n θ_s(g_i)` is a **left** ideal (θ_s is anti), so Lemma 2.2 gives
`ann_r(θ_s(C)) = ⋂_i ann_r(θ_s(g_i))`. ∎

For `k = 1` this is Theorem 3.5. Note that `⋂_i ann_r(θ_s(g_i))` is **not**
`ann_r` of the right ideal generated by the `θ_s(g_i)` (Lemma 2.3) — the side flip is
essential.

**Morita form in general.** `ann_r(θ_s(C)) = I_W` with
`W = ⋂_i ker θ_s(g_i) ⊆ B²`, and `dim C^{⊥_s} = 2 dim_{F_q} W`,
`|C^{⊥_s}| = |W|²`.

### 3.9 Size consistency (C1), and a proof of L-6.5

**Corollary 3.9 (L-6.5, proved).** For every `x ∈ M_2(B)`: `|im x| = |im x^T|`, and
consequently `|xR_n| = |R_n x|`.

*Proof.* Let `v := θ_s(g)` and `w := θ_s(g)^T`… more precisely, apply Theorem 3.5 to
`C = gR_n` and use the two independent evaluations of the same quantity:

* `|C| = |gR_n| = |I_{im g}| = |im g|²` (Stage 2A L-2.3a + `|I_W| = |W|²`);
* `|C^{⊥_s}| = |ann_r(θ_s(g))| = |ker θ_s(g)|²` (Theorem 3.5, `rev` is a bijection).

Phase 1 (RGF Thm 6.6) gives `|C|·|C^{⊥_s}| = |R|^n = q^{4tn} = |B|^4`, so
`|im g|²·|ker θ_s(g)|² = |B|^4`. On the other hand `v := θ_s(g)` acts `B`-linearly on the
column module `B²`, so `|im v|·|ker v| = |B|²`, whence `|ker θ_s(g)|² = |B|^4/|im
θ_s(g)|²`. Substituting, `|im g|² = |im θ_s(g)|²`, so `|im g| = |im θ_s(g)|`. Finally
`θ_s(g) = σ_s(g^T)` and `σ_s` is a bijection of `B²` carrying `im(g^T)` onto
`im(σ_s(g^T))`, so `|im θ_s(g)| = |im g^T|`. Hence `|im g| = |im g^T|`.

For the last statement: `(xR_n)^T = R_n x^T` (transposition is an anti-automorphism of
`M_2(B)`), so `|R_n x^T| = |xR_n|`; applying `|im|`-equality with `x` replaced by `x^T`
gives `|R_n x| = |im x^T|² = |im x|² = |xR_n|`. ∎

**This is stronger than the register's L-6.5 row**, which was `PROPOSED / UNPROVED` and
whose proposed proof went through L-6.6 (`B` is Frobenius, an `IMPORTED RESULT` with an
unverified reference). The proof above uses only P-2.7 and Phase-1 Theorem 6.6.

**Consistency checks (C1–C4), all verified.**

| Check | Prediction | Result |
|---|---|---|
| C1 sizes | `|C|·|C^{⊥_s}| = |R|^n` | holds for **every** tested `g` (Phase 1 proves it in general; the tests confirm the annihilator formula is compatible) |
| C2 `n = 1` | `rev = id`, so `C^{⊥_s} = ann_r(θ_s(g))` | holds; at `(4,1,1)` all `256` elements × `2` values of `s` agree |
| C3 extremes | `g = 1 ⟹ C^{⊥_s} = 0`; `g = 0 ⟹ C^{⊥_s} = R^n` | included in the exhaustive `(4,1,1)` sweep |
| C4 module | `rev(ann_r(θ_s(g)))` is a right ideal | automatic since `rev` is an automorphism (Prop. 3.6(2)); confirmed — the computed dual is a right ideal in every case |

### 3.10 Limits of the statement

P-2.7 is an identity of **sets** (indeed of right ideals) and makes no claim about
minimum distances, weights, or hulls. It holds for every `g` and every `s`, in every
regime, wild included (verified at `(4,2,2)`). It does **not** say that `C^{⊥_s}` is
principal — that is §4.

---

## 4. Task D — P-2.8: reciprocal generators

Throughout, `v := θ_s(rev g)`, so that by Theorem 3.5 `C^{⊥_s} = ann_r(v) = I_{ker v}`.

### 4.1 The general (regime-free) recipe

**Theorem 4.1.** Let `C = gR_n`, `v = θ_s(rev g)`, `W = ker v ⊆ B²`. If
`μ_B(W) ≤ 2`, say `W = Bw_1 + Bw_2`, then

```
C^{⊥_s} = h·R_n ,        h := [ w_1 ∣ w_2 ]   (the matrix with COLUMNS w_1, w_2) ,
```

and `μ_{R_n}(C^{⊥_s}) = ⌈μ_B(W)/2⌉`. If `μ_B(W) ≥ 3` then `C^{⊥_s}` is **not**
principal.

*Proof.* `im h = Bw_1 + Bw_2 = W` (Stage 2A L-2.3c, T-080), so `hR_n = I_{im h} = I_W`
(Stage 2A L-2.3a, T-077) and `I_W = ann_r(v) = C^{⊥_s}` (Theorems 3.5, 3.6). The
generator-number identity is Stage 2A Thm 3.1 (T-081). If `μ_B(W) ≥ 3` then `I_W` is not
principal by the individual criterion (Stage 2A Thm 4.1, T-083). ∎

This is the honest noncommutative analogue of the classical "reciprocal polynomial"
statement: one does **not** divide `X^n−1` by `g`; one computes the kernel of
`θ_s(rev g)` and packs two of its generators into the columns of a matrix. Everything is
derived, nothing is imported from the commutative theory.

### 4.2 The chain-ring regime: the Smith-normal-form formula of the proposal

**Theorem 4.2 (P-2.8 as stated in §6.6, proved).** Assume `p ∤ n` or `t = 1`, so that by
Stage 2B Thm 3.6 every CRT component `B_j` of `B` is a **chain ring** (with uniformizer
`ω_j` and nilpotency length `ℓ_j`). Let `v_j = U_j diag(ω_j^{a_j}, ω_j^{b_j}) V_j` be a
Smith normal form of the `j`-th component of `v` (`0 ≤ a_j ≤ b_j ≤ ℓ_j`; Stage 2B
Thm 3.3). Then

```
C^{⊥_s} = h·R_n ,     h_j = V_j^{-1} · diag( ω_j^{ℓ_j − a_j} , ω_j^{ℓ_j − b_j} ) ,
```

assembled componentwise by the CRT. In particular, **in this regime the Galois dual of
every principal cyclic code is principal**.

*Proof.* By Stage 2B Thm 3.3 (SNF over a chain ring) and Thm 3.6 (chain ⟺ `t = 1` or
`p ∤ n`), each component `v_j` admits such a decomposition; and by Stage 2B Thm 3.3
`ker v_j` is generated by at most two elements, so `μ_B(ker v) = max_j μ_{B_j}(ker v_j)
≤ 2` (Stage 2B Lemma 4.2, T-104). Hence Theorem 4.1 applies and the dual is principal.

For the explicit `h_j`: `ker diag(ω^a, ω^b) = ann(ω^a) ⊕ ann(ω^b) = (ω^{ℓ−a}) ⊕
(ω^{ℓ−b})` in a chain ring (because `ω^c z = 0 ⟺ v(z) ≥ ℓ − c`). With
`v_j = U_j D_j V_j`, one has `ker v_j = V_j^{-1} ker D_j`: indeed `v_jw = 0 ⟺
U_jD_jV_jw = 0 ⟺ D_j(V_jw) = 0 ⟺ V_jw ∈ ker D_j`. Therefore

```
im( V_j^{-1} diag(ω^{ℓ−a}, ω^{ℓ−b}) ) = V_j^{-1} ( (ω^{ℓ−a}) ⊕ (ω^{ℓ−b}) )
                                       = V_j^{-1} ker D_j = ker v_j ,
```

so by Theorem 4.1 the component `h_j` generates the `j`-th component of the dual, and the
CRT assembles them. ∎

*Convention check.* With the convention `v_j = U_j D_j V_j` (the right factor is `V_j`),
the proposal's formula `h_j = V_j^{-1}diag(ω^{ℓ−a},ω^{ℓ−b})` is correct; with the
convention `U M V = D` used in the script the same matrix is `V·diag(ω^{ℓ−a},ω^{ℓ−b})`.
The script uses the latter and verifies `im h = ker v` directly, so no convention is
assumed.

*Classical limit.* For `t = 1` and `p ∤ n` the components are fields, `ω = 0`, `ℓ = 1`,
so `a_j,b_j ∈ {0,1}` and `h_j = V_j^{-1}diag(1−a_j, 1−b_j)` is the **complementary
projection** — the classical "check polynomial" statement, up to the `θ_s`-twist and the
reversal, exactly as the proposal predicted.

### 4.3 Hypotheses, normalisation, uniqueness

* **Hypotheses.** Theorem 4.1: `μ_B(ker θ_s(rev g)) ≤ 2` — no regime hypothesis.
  Theorem 4.2: `p ∤ n` or `t = 1` (which forces `μ ≤ 2`).
* **Which annihilator.** The **right** annihilator `ann_r`, of the **element**
  `θ_s(rev g)` (equivalently `rev` applied to `ann_r(θ_s(g))`) — not `ann_l`, not the
  annihilator of the ideal (§2.4).
* **Role of `θ_s`.** It converts the right ideal into a left ideal and twists the
  generator; it acts on `g` only.
* **Role of `rev`.** It converts the "annihilate on the right of the reversed generator"
  condition into the code condition; it is an automorphism, trivial iff `n ≤ 2`
  (Remark 3.7).
* **Normalisation.** In Theorem 4.2 the SNF is not unique (`U_j, V_j` are not), so `h` is
  not unique; the convention `0 ≤ a_j ≤ b_j ≤ ℓ_j` normalises the exponents only. In
  Theorem 4.1 one may always take `w_2 = 0` when `μ_B(W) ≤ 1`, and `h = 0` when `W = 0`.
* **Uniqueness.** `h·u` generates the same ideal for every unit `u ∈ R_n^×`; conversely,
  `hR_n = h'R_n ⟺ im h = im h'` (because `I_W` determines `W` by Morita, and
  `W(hR_n) = im h` by L-2.3a), so two generators differ by a `B`-module automorphism of
  their common image. Whether they always differ by **right multiplication by a unit** was
  tested exhaustively: at `(4,1,1)` (all `256` elements of `R_n`, `7` ideals),
  `(4,1,2)` (all `65536`, `33` ideals) and `(4,2,1)` (all `65536`, `33` ideals), the set
  of generators of each principal right ideal is **exactly** the orbit
  `{h·u : u ∈ R_n^×}` (`[EXH]`, `0` failures). In general this is recorded as **O-2.9**,
  `OPEN`: no proof is offered here.
* **What changes in the wild regime.** No SNF, and the dual need not be principal — §4.4.

### 4.4 The wild regime: O-2.8 is answered negatively

**Theorem 4.3 (counterexample; `(q,t,n) = (4,2,2)`, `s = 0`).** Let
`B = F_4[u,ε]/⟨u²,ε²⟩` with `ε = X−1` (so `X²−1 = (X−1)²`, `t = 2`, `p = 2 ∣ n = 2`),
and put

```
g := v := diag(uε, uε) = [[uε, 0],[0, uε]] ,        C := g·R_n .
```

Then `C` is principal, `θ_s(rev g) = v` for `s = 0` (and the same construction with
`g = rev(θ_s^{-1}(v))` works for every `s`), and

```
C^{⊥_s} = ann_r(v) = I_{m ⊕ m} = M_2(m) ,     m = (u, ε) ,
```

with `μ_B(m ⊕ m) = 4 > 2`, so **`C^{⊥_s}` is not principal** (although it is
`2`-generated: `μ_{R_n} = 2`). Hence the register's **O-2.8 is answered NO**: in the wild
regime the Galois dual of a principal code need not be principal.

*Proof.* `uε ≠ 0` (it is the socle element: the unique monomial of maximal `u`- and
`ε`-degree) and `ann_B(uε) = {z : uεz = 0} = (u,ε) = m`, since the only monomial
surviving multiplication by `uε` is `z = 1`. Hence
`ker v = ann_B(uε) ⊕ ann_B(uε) = m ⊕ m`. By Stage 2B Thm 2.3/2.4 (wild case)
`dim_{F_4}(m/m²) = 2`, so `dim_{F_4}((m⊕m)/m(m⊕m)) = 4` and Nakayama gives
`μ_B(m⊕m) = 4`. By Theorem 3.5, `C^{⊥_s} = ann_r(v) = I_{m⊕m}` (a matrix has both
columns in `m⊕m` iff all entries lie in `m`, i.e. `I_{m⊕m} = M_2(m)`), and by
Stage 2A Thm 4.1 it is not principal, since `μ_B = 4 > 2`; by Stage 2A Thm 3.1,
`μ_{R_n} = ⌈4/2⌉ = 2`. ∎

**Computational certificate (`[EXH]`).** At `(4,2,2)`, for `s = 0` and `s = 1`:
`uε ≠ 0` and `uε·m = 0`; `ker v = m ⊕ m` with `|ker v| = 4096`, `|m| = 64`;
`μ_B(ker v) = 4`; `C^{⊥_s} = I_W` with `dim_{F_q} C^{⊥_s} = 12`, i.e.
`|C^{⊥_s}| = 4^{12} = 16 777 216`; **all `16 777 216` elements of `C^{⊥_s}` were scanned
and none generates it**; two explicit generators do (`μ_{R_n} = 2`); and
`|C|·|C^{⊥_s}| = 256 · 16 777 216 = 4^{12} = |R|^n`. The ideal `M_2(m)` is the same
wild obstruction that Stage 2B exhibited for P-2.6 — the two are now visibly the same
object.

**Remark 4.4 (O-2.5).** The proposal already noted that `ker v` need not be a direct
summand: for `v = uI_2` over `B = F_4[u]/⟨u²⟩`, `ker v = uB ⊕ uB` with quotient `F_4²`,
not free. Stage 2C confirms the conceptual point: principality of `ann_r(v)` depends on
`μ_B(ker v) ≤ 2` (Stage 2A Thm 4.1), **not** on `ker v` being a summand. O-2.5
(classification of the `v` for which `ker v` is a summand) remains `OPEN` and is not
needed.

---

## 5. Task E — cardinality and double-dual consistency

Both identities are **Phase-1 theorems** (RGF Thm 6.6 and Thm 6.8); Stage 2C verifies
that the annihilator formula of §3 is consistent with them, and separates what does and
does not need reflexivity.

### 5.1 The cardinality identity

**Theorem (Phase 1, RGF Thm 6.6).** For every right `R_n`-submodule `C` and every `s`:
`|C|·|C^{⊥_s}| = |R|^n` and `dim_{F_q} C + dim_{F_q} C^{⊥_s} = 4tn`.

**Reflexivity is NOT needed** — the proof uses only the triviality of the right radical,
which holds for every `s`. Stage 2C verifies the identity **for every tested code at every
parameter set, including the non-reflexive ones** at `(8,1,2)` with `s = 1, 2`
(`200` codes × `3` values of `s`), and reconciles it with the annihilator formula via
Corollary 3.9 (L-6.5).

### 5.2 The double dual

**Theorem (Phase 1, RGF Thm 6.8).** `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` for every right
`R_n`-submodule `C` and every `s`.

*Verified* at every parameter set on `60` codes per `s` (`[SMP]`), by computing the dual
twice from the definition and comparing with `σ_{2s}(C)`.

**Where reflexivity enters.** By RGF Cor 6.9, `C^{⊥_s⊥_s} = C` for **all** `C` ⟺
`r ∣ 2s` ⟺ `σ_{2s} = id`. So:

* the identity `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` holds for **all** `s` — reflexivity not
  needed;
* the **sharper** form `(C^{⊥_s})^{⊥_s} = C` needs `r ∣ 2s`, and for individual codes it
  may hold or fail when `r ∤ 2s`.

**Non-reflexive witness (`[SMP]`, `(8,1,2)`).** Here `q = 8`, `r = 3` (odd), so by RGF
Cor 4.6 no non-trivial `s` is reflexive. At `s = 1` and `s = 2`, `8` of `60` sampled codes
have `(C^{⊥_s})^{⊥_s} ≠ C`, while the identity `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` held for all
`60`. At `s = 0` all `60` are fixed, as they must be. So the failure of reflexivity is
explicitly exhibited, not assumed away.

**Consistency with P-2.7.** Applying Theorem 3.5 twice gives
`C^{⊥_s⊥_s} = rev(ann_r(θ_s(h)))` where `h` generates `C^{⊥_s}`; the log verifies this is
`σ_{2s}(C)`, i.e. the annihilator formula reproduces the Phase-1 double-dual theorem — a
nontrivial cross-check of the two independent derivations.

### 5.3 What is deliberately not derived

No hull `C ∩ C^{⊥_s}`, no `dim Hull`, and no statement about `σ_{2s}`-invariant codes
beyond what Phase 1 proves. Phase 3 will need the following, recorded here and **not**
used: `Hull_s(C) = C ∩ rev(ann_r(θ_s(C)))`, and `C` is `σ_{2s}`-stable iff
`C^{⊥_s⊥_s} = C`.

---

## 6. Task F — computational verification

### 6.1 The script and its independence

`04_COMPUTATION/phase2_stage2c_galois_duality.py` (1975 lines) imports from the Phase-1
library only `Field`, `Local`, `MatRing`, `rref`, `nullspace_basis` and the reporting
helpers. Everything else is written from scratch here: `B = A_t[X]/⟨X^n−1⟩` with its own
arithmetic; the identification `ι` and its inverse; `σ_k`, `θ_s`, `rev` on `R^n` and on
`R_n`; the **polynomial level** `R[X]` (needed for Task A(5)–(6)); the pairings `B_s` and
`b_s`; the dual by `F_q`-linear algebra directly from the definition; annihilators by
brute force over the standard basis; the Morita side (`im`, `ker`, `I_W`, `μ`); the CRT
components and the Smith normal form over chain rings.

Crucially, the dual `C^{⊥_s}` is always computed **from the definition** (`{y :
B_s(x,y) = 0 ∀ x ∈ C}` by linear algebra over `F_q`), and the annihilators are computed as
**kernels of the multiplication maps** — never from `im`, never from Morita — so that
P-2.7, the Morita form and P-2.8 could each have failed.

### 6.2 Cases

| `(q,t,n)` | `r` | regime | `|B|` | `|R_n|` | generators tested |
|---|---|---|---|---|---|
| `(4,1,1)` | 2 | split, `n = 1` | 4 | 256 | **all 256** `[EXH]` |
| `(4,1,2)` | 2 | chain (`t = 1`, `p ∣ n`) | 16 | 65 536 | 200 random `[SMP]` |
| `(4,2,1)` | 2 | chain (`t ≥ 2`, `p ∤ n`) | 16 | 65 536 | 200 random `[SMP]` |
| `(4,2,2)` | 2 | **wild** | 256 | 4.3·10⁹ | 200 random `[SMP]` + the counterexample `[EXH]` |
| `(4,1,3)` | 2 | split, `n = 3` (`rev` non-trivial) | 64 | 1.7·10⁷ | 200 random `[SMP]` |
| `(9,1,2)` | 2 | split, reflexive `s = 1` | 81 | 4.3·10⁷ | 200 random `[SMP]` |
| `(8,1,2)` | 3 | chain, **non-reflexive** (`r` odd) | 64 | 1.7·10⁷ | 200 random `[SMP]` |
| `(4,2,3)` | 2 | split, `t ≥ 2`, `rev` non-trivial | 4096 | 2.8·10¹⁴ | 200 random `[SMP]` |

For each case, every `s ∈ {0,…,r−1}` is tested, so `θ_s` is exercised in the trivial and
non-trivial Galois regimes alike.

### 6.3 Results (all `[EXH]`/`[SMP]` counts are in the log)

| Test | Result |
|---|---|
| L-6.1: `θ_s(uv) = θ_s(v)θ_s(u)` on `R_n` | `65 536` pairs exhaustively at `(4,1,1)`; `150`–`200` pairs elsewhere; **0 failures** |
| `θ_s` additive, bijective, `θ_s² = σ_{2s}`, `θ_s^{-1} = σ_{−2s}θ_s`, `ord(θ_s) = 2r/gcd(r,2s)` (with minimality) | **0 failures** at all 8 parameter sets |
| `θ_s` anti on `R` and on `R[X]` (the two lower levels) | **0 failures** (200 pairs each, per case) |
| `θ_s(X^n−1) = X^n−1`; `θ_s` preserves `⟨X^n−1⟩`; well-definedness; descended = coefficient-wise | **0 failures** (100 multipliers / 100 congruent pairs / 100 polynomials per case) |
| `θ_s` fixes `X` and `u` | **0 failures** |
| P-2.1f: `rev² = id`, `rev` an **automorphism**, `rev(X) = X^{n−1}`, `rev|_R = id`, `rev` commutes with `σ_k` and `θ_s`, `rev T = T^{−1} rev`, `ι(rev y) = rev(ι y)`, `rev(ann_r v) = ann_r(rev v)` | **0 failures** |
| Annihilator side laws (Thm 2.1), left/right distinctness, kernels of `L_v`/`R_v` (brute force over all `w`), `ann_r(R_n g) = ann_r(g)`, `ann_r(gR_n) ⊊ ann_r(g)` | **0 failures**; e.g. `19` of `25` probes show strictness at `(4,1,1)` |
| **P-2.7 forms 1, 2, 3** and the Morita form | `256/256` `[EXH]` at `(4,1,1)`; `200/200` `[SMP]` at every other parameter set, for **every** `s`; **0 failures** |
| `|C|·|C^{⊥_s}| = |R|^n` | **0 failures** (every tested code, every `s`) |
| `rev`-sensitivity | `92` of `200` `g` at `(4,1,3)` and `108` of `200` at `(4,2,3)` are **not** `rev`-stable; all `g` are `rev`-stable at every `n ≤ 2` case (Remark 3.7) |
| `μ_B(ker θ_s(rev g))` | `≤ 2` for **every** tested `g` in the chain-ring regime (`(4,1,1)`: `{0:180, 1:75, 2:1}`; `(4,1,2)`: `{0:149, 1:49, 2:2}`; `(4,2,1)`: `{0:136, 1:62, 2:2}`; `(4,1,3)`: `{0:65, 1:135}`; `(9,1,2)`: `{0:155, 1:45}`; `(8,1,2)`: `{0:169, 1:31}`; `(4,2,3)`: `{0:68, 1:131, 2:1}`) |
| **P-2.8** (SNF generator `h`, `hR_n = C^{⊥_s}`) | `256/256` `[EXH]` at `(4,1,1)`; `200/200` at each other chain-ring parameter set; **0 failures** |
| P-2.8 in the wild case (Nakayama generator) | `200/200` sampled codes with `μ ≤ 2`; plus the `μ = 4` counterexample of §4.4 |
| **Wild counterexample** (`(4,2,2)`, `s = 0, 1`) | `ker v = m ⊕ m` (`|ker v| = 4096`, `|m| = 64`), `μ_B = 4`, `|C^{⊥_s}| = 16 777 216`, all `16 777 216` elements scanned and none generates it, `2`-generated, `|C||C^{⊥_s}| = |R|^n` |
| Generator uniqueness | `[EXH]` at `(4,1,1)` (7 ideals, all 256 elements), `(4,1,2)` and `(4,2,1)` (33 ideals, all 65 536 elements each): the generators of each principal right ideal form exactly one orbit under right multiplication by units |
| Double dual `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` | **0 failures** (60 codes per `s`) |
| Reflexivity | `r ∣ 2s`: all `60` codes fixed; `r ∤ 2s` (`(8,1,2)`, `s = 1, 2`): `8` of `60` codes have `C^{⊥_s⊥_s} ≠ C` |

### 6.4 Negative controls (a wrong convention must FAIL)

| # | Wrong statement | Outcome |
|---|---|---|
| neg-1 | `θ_s(uv) = θ_s(u)θ_s(v)` (wrong order) | **fails** — counterexample found at every parameter set |
| neg-2 | `rev` is an anti-automorphism | **fails** — counterexample found (`rev` is an automorphism) |
| neg-3 | use `ann_l` instead of `ann_r` in P-2.7 | **fails** (`10`–`23` of `40` codes detect it) |
| neg-4 | omit `rev` (`C^{⊥_s} = ann_r(θ_s(g))`) | **fails** at `n ≥ 3` (`19` of `40` codes at `(4,1,3)`); vacuous for `n ≤ 2`, and the log says so |
| neg-5 | omit `θ_s` (`C^{⊥_s} = rev(ann_r(g))`) | **fails** (`6`–`20` of `40` codes) |
| neg-6 | build `I_W` from **rows** instead of **columns** | **fails** (`9`–`23` of `40` codes) |
| neg-7 | the swapped pairing `B_s(y,x)` gives the same dual | **fails** (`7`–`23` of `40` codes) |

**A real bug was caught by this discipline during development**, and it is recorded
because it is the exact failure mode the controls exist to detect: the first version of
the kernel routine passed the images of the basis vectors as **rows** to the nullspace
routine, which computes the kernel of the **transpose**. Every dimension and cardinality
check still passed; only the containment half of the certificate exposed it. The same
trap (rows vs columns of `I_W`) is now itself a negative control (neg-6).

### 6.5 Reproducibility

**596 checks, 596 PASS, 0 FAIL** — 101 `[EXH]`, 495 `[SMP]`, seed `20261107`, Python
3.11.2. Two consecutive runs (≈ 78 s each) produced **byte-identical** logs: SHA-256
`00355e7f205de16cbe0a567881a978f326007e564a606663135a71f5103a30ed` (777 lines). The log carries no timestamp and no elapsed time, so the comparison is exact.

**Regression.** The Stage-2A and Stage-2B scripts were not modified in Stage 2C; the
Phase-1 library `ring_structure_checks.py` is byte-for-byte unchanged (§9 of the Stage-2B
report, re-checked here).

---

## 7. Traceability: theorem → obligations → tests → hypotheses → residual risk

| Statement | Task obligations | Proof | Tests (log) | Hypotheses | Residual risk |
|---|---|---|---|---|---|
| Lemma 1.2 (additive, bijective, inverse) | A(7) | §1.3 | additivity, injectivity, `θ_s^{-1} = σ_{−2s}θ_s` per case | — | none |
| **Theorem 1.3 (L-6.1)** | A(all), C | §1.4 | `[EXH]` 65 536 pairs at `(4,1,1)`, sampled elsewhere, every `s` | `X` central | none |
| Corollary 1.4 (`R[X]`) | A(2) | §1.4 | 200 polynomial pairs per case | — | none |
| Lemma 1.5 (ideal, well-definedness) | A(3)(4)(5)(6) | §1.5 | `θ_s(X^n−1)=X^n−1`, 100 multipliers, 100 congruent pairs, 100 polynomials | `X^n−1` central | none |
| Lemma 1.6 (`θ_s²`, order) | A(8) | §1.6 | `θ_s² = σ_{2s}`; order with minimality, 60 probes | — | none |
| Theorem 2.1 (annihilator side laws) | B | §2.2 | right/left ideal-ness, two-sidedness, per case | — | none |
| Lemma 2.2 / 2.3 (left vs right ideals) | B | §2.3 | `ann_r(R_ng) = ann_r(g)`; strictness witness | noncommutativity | none |
| Kernels of `L_v`, `R_v` | B | §2.1 | brute force over all `w` at `(4,1,1)` | — | none |
| Proposition 3.6 (P-2.1f, `rev`) | C(6) | §3.6 | 8 checks per case | — | none |
| **Theorem 3.5 (P-2.7)** | C(all) | §3.2–3.6 | forms 1–3 + Morita, `[EXH]`/`[SMP]`, every `s` | L-6.1, P-2.1f, Phase-1 non-degeneracy | none for principal codes |
| **Theorem 3.8 (P-2.7, general)** | C(9) | §3.8 | structure verified; used implicitly for every right ideal | `C` finitely generated (automatic) | the non-principal case is covered by the theory and by the Morita form, but the log's per-code sweep only exhibits principal `C` |
| Corollary 3.9 (L-6.5) | C1 | §3.9 | `|C||C^{⊥_s}| = |R|^n` on every code | P-2.7 + Phase 1 | none (and L-6.6 / Frobenius is **not** needed) |
| Theorem 4.1 (general recipe) | D | §4.1 | P-2.8 checks; wild Nakayama generator | `μ_B(ker) ≤ 2` | none |
| Theorem 4.2 (P-2.8, SNF) | D | §4.2 | `hR_n = C^{⊥_s}`, `[EXH]`/`[SMP]` | `p ∤ n` or `t = 1` | none in that regime |
| Theorem 4.3 (wild counterexample) | D, O-2.8 | §4.4 | `[EXH]` certificate at `(4,2,2)`, `s = 0, 1` | wild regime | — |
| §5.1 cardinality | E | Phase 1 | every code, every `s` | none (all `s`) | none |
| §5.2 double dual | E | Phase 1 | 60 codes per `s`; non-reflexive witness at `(8,1,2)` | `= σ_{2s}(C)` all `s`; `= C` needs `r ∣ 2s` | none |
| neg-1 … neg-7 | F(10) | §6.4 | all fail as required | — | neg-4 vacuous for `n ≤ 2` (stated in the log) |

---

## 8. Report

### 8.1 Proved in Stage 2C

Lemma 1.2, **Theorem 1.3 (L-6.1)**, Corollary 1.4, Lemma 1.5, Lemma 1.6, **Theorem 2.1**
(annihilator side laws), Lemmas 2.2–2.3, **Proposition 3.6 (P-2.1f, `rev`)**,
**Theorem 3.5 (P-2.7)**, **Theorem 3.8 (P-2.7 for arbitrary right ideals)**,
**Corollary 3.9 (L-6.5)**, **Theorem 4.1** (regime-free reciprocal generator),
**Theorem 4.2 (P-2.8, SNF form)**, **Theorem 4.3** (wild counterexample), and the
consistency analysis of §5.

Register rows: **T-115 … T-136** (22 rows: 17 `PROVED IN PHASE 2 STAGE 2C`, 4 `COMPUTATIONALLY VERIFIED ONLY`, 1 `OPEN`).

### 8.2 Refuted or modified

* **No claim of the proposal was refuted.** L-6.1, P-2.7 and P-2.8 are **true as
  stated** and are now proved, including the explicit SNF form of P-2.8 with the
  convention `v_j = U_j D_j V_j ⟹ h_j = V_j^{-1}diag(ω^{ℓ−a},ω^{ℓ−b})`.
* **Modified (sharpened, not corrected):** the proposal derives P-2.7 for a principal
  code. Stage 2C proves the **general** form `C^{⊥_s} = rev(ann_r(θ_s(C)))` for every
  right ideal (Theorem 3.8), which reduces to the proposal's form via Lemma 2.2 — and
  which explains *why* a single generator suffices: `θ_s` turns the right ideal into a
  left ideal, and left ideals are annihilator-determined by their generators.
* **Resolved negatively: O-2.8.** In the wild regime the Galois dual of a principal code
  need not be principal (Theorem 4.3, `(4,2,2)`, `g = diag(uε,uε)`).
* **Resolved: L-6.5** (was `PROPOSED / UNPROVED`, was to be proved via the unconfirmed
  import L-6.6). Proved here from P-2.7 and Phase 1 alone; **L-6.6 (B Frobenius) is not
  needed** and remains an `IMPORTED RESULT` with an unverified reference, used nowhere.
* **Discharged: O-2.7** (the `n = 1` anchor): at `(4,1,1)` the theory degenerates to the
  ideal theory of `M_2(F_4)`; the `7` right ideals found exhaustively match the Phase-1
  anchor `7`.

### 8.3 Exact hypotheses

* §1 (L-6.1): `q = p^r`, `t ≥ 1`, `n ≥ 1`, `X` central. No squarefree, chain or
  semisimplicity hypothesis.
* §2 (annihilators): none (finite ring; `R_n` unital).
* Theorem 3.5 / 3.8 (P-2.7): none beyond L-6.1, P-2.1f, and Phase-1 non-degeneracy —
  valid in the wild regime, for every `s`, and for non-principal codes.
* Theorem 4.1: `μ_B(ker θ_s(rev g)) ≤ 2` (no regime hypothesis).
* Theorem 4.2: `p ∤ n` or `t = 1` (exactly the chain-ring regime of Stage 2B Thm 3.6).
* Theorem 4.3: `p ∣ n` and `t ≥ 2` (wild), with an explicit instance.
* §5: cardinality for all `s`; `C^{⊥_s⊥_s} = C` for all `C` iff `r ∣ 2s`.
* Generator uniqueness (orbit under `R_n^×`): `[EXH]` at three parameter sets; **O-2.9**,
  `OPEN` in general.

### 8.4 Coverage

* **Exhaustive** (`[EXH]`, 101 checks): all `256` elements of `R_n` at `(4,1,1)` (all
  `65 536` pairs for the anti-multiplicativity and `rev`-automorphism tests, brute-force
  annihilator kernels over all `w`, all `7` principal ideals for generator uniqueness);
  all `65 536` elements grouped by the ideal they generate at `(4,1,2)` and `(4,2,1)`
  (33 ideals each) for generator uniqueness; the complete wild certificate at `(4,2,2)`
  including the scan of all `16 777 216` elements of `C^{⊥_s}`; `θ_s(X^n−1) = X^n−1`;
  `rev(X) = X^{n−1}`; `θ_s` fixes `X` and `u`; neg-1 and neg-2.
* **Sampled** (`[SMP]`, 495 checks, sizes stated on every line): `150`–`200` distinct
  elements or `200` distinct generators per case elsewhere; `60` codes for the double
  dual; `40` codes per negative control; `100` multipliers / congruent pairs /
  polynomials for the polynomial-level tests.

### 8.5 Open problems and carried-forward limitations (T-136)

1. **O-2.9 (new):** is every generator of a principal right ideal of `R_n` of the form
   `h·u` with `u ∈ R_n^×`? Verified exhaustively at three parameter sets; no proof.
   (The weaker statement `hR_n = h'R_n ⟺ im h = im h'` **is** proved.)
2. **O-2.2** (`μ_B(W) ≤ 4` uniformly in the wild case) remains `OPEN`; Stage 2C observed
   `μ ≤ 2` on `200` random wild generators and `μ = 4` for the constructed `v`.
3. **O-2.5** (when is `ker v` a direct summand?) remains `OPEN`; principality does not
   require it (Remark 4.4).
4. **O-2.4** (P-2.8 in the wild case) is **partially resolved**: Theorem 4.1 gives a
   generator whenever `μ_B(ker) ≤ 2`, and Theorem 4.3 shows it can fail. A *criterion*
   for `μ_B(ker θ_s(rev g)) ≤ 2` in the wild regime is still open.
5. The `M_2(B)`-side enumeration of non-principal right ideals was not swept per-code in
   the log; Theorem 3.8 covers them structurally.
6. Carried forward unchanged: P-2.7/P-2.8 hull consequences (Phase 3), hull enumeration
   (Phase 4), Gray maps (Phase 5), quantum constructions (Phase 6), C-2.1d/e/f/g,
   L-6.6 (unverified import, now unused), T-066 is **discharged** by Proposition 3.6,
   T-021 is superseded by Stage 2B T-107, and the Phase-1 coverage gaps, the `n ≥ 2`
   left-submodule gap, T-006, T-011–T-014, warning B3.5.
7. **Not attempted by instruction:** hull dimensions, hull enumeration, Gray maps, CSS or
   EA parameter claims, and any quantum construction. Nothing in this document implies
   the existence of a quantum code.
