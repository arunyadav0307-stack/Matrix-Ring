# Phase 1 — Ring Specification and Algebraic Foundations

**Blueprint:** §5, Phase 1 — *Select ring and establish algebraic foundations*.
**Required deliverables (blueprint):** ring specification; notation sheet; lemmas on
automorphism; module conventions; **validated pairing or proof that the candidate fails**.
**Exit gate (blueprint):** *do not proceed if the Galois automorphism is trivial or the
pairing cannot be made valid for the intended construction.*

**Researcher decisions in force (Phase 0, approved):** B1 (Alahmadi et al. cited for the
framework only; the disputed theorem is neither restated nor challenged; the discrepancy
is preserved as a documented literature limitation); B2 (narrowed four-part novelty
statement; anti-automorphism duality over non-commutative rings is **not** claimed as new;
published / new / computational / open kept distinct); B3 (hybrid Galois regime:
general-*s* duality developed; reflexive regime primary for quantum constructions;
non-reflexive regime investigated separately; non-reflexive results retained only under
explicitly proved conditions; **no** assumption that every non-reflexive code satisfies
quantum-construction requirements).

This file proves every structural property it states. Nothing here is imported without a
proof or a citation. Computational corroboration is in
`04_COMPUTATION/ring_structure_checks.py` and its log.

---

## 0. Standing hypotheses, notation, and the four Galois regimes

### 0.1 Standing hypotheses (Phase 1)

| Symbol | Meaning | Standing hypothesis |
|---|---|---|
| `p` | prime | — |
| `q = p^r` | field size | **`r ≥ 2`** (at `r = 1` the Galois action is trivial: `σ_s = id` for all `s`) |
| `F_q` | finite field, `F_q^× = ⟨ω⟩` | — |
| `A_t` | `F_q[u]/⟨u^t⟩` | `t ≥ 1` |
| `R` | `M_2(A_t)` | `m = 2` (so `m ≥ 2`, which T-017 needs) |
| `n` | code length | `n ≥ 1`; `X^n − 1` squarefree (`gcd(n,p)=1`) **only** where stated |
| `X` | the cyclic indeterminate | central in `R[X]` |
| `s` | Galois parameter | taken mod `r` |

The four regimes are **not** equivalent and are never silently identified:

| Regime | Condition | `σ_s` | `θ_s` | Reflexive? | Non-trivial Galois? |
|---|---|---|---|---|---|
| **R0 Euclidean (trivial Galois)** | `s ≡ 0 (mod r)` | `id` | transpose (involution) | yes | **no** |
| **R1 genuine non-trivial reflexive** | `r` even, `s ≡ r/2 (mod r)` | order **2** | involution, `≠` transpose | yes | **yes** |
| **R2 reflexive (general)** | `2s ≡ 0 (mod r)` | order ≤ 2 | involution | yes | iff `s ≢ 0` |
| **R3 general non-trivial** | `s ≢ 0` and `2s ≢ 0 (mod r)` | order `≥ 3` | **not** an involution | **no** | yes |

`R0` and `R1` are the two members of `R2` when `r` is even (`s ≡ 0`, `s ≡ r/2`); for `r`
odd, `R2 = R0` only — **for odd `r`, a non-trivial Galois action and reflexivity are
mutually exclusive** (§4.6). `R1` is the primary quantum-construction setting (B3.2); `R3`
is investigated separately (B3.3–B3.5).

### 0.2 Notation sheet

```
q = p^r,  F_q,  F_q^x = <omega>,                 Tr = Tr_{F_q/F_p} : a -> sum_i a^{p^i}
A_t = F_q[u]/<u^t>   (u central;  normal form  sum_{i=0}^{t-1} a_i u^i)
lambda : A_t -> F_q,   lambda(sum a_i u^i) = a_{t-1}              (coefficient of u^{t-1})
v(a) = min{i : a_i != 0}   (u-adic valuation; v(0) = infinity)
R  = M_2(A_t);   E_ij matrix units;   I = I_2;   X^T transpose;   tr = matrix trace
Lambda = lambda o tr : R -> F_q
sigma_s : entrywise Frobenius, sigma_s(a) = a^{p^s} on F_q, sigma_s(u) = u
theta_s = sigma_s o ( . )^T        (anti-automorphism)
B  = A_t[X]/<X^n-1>;   R_n = R[X]/<X^n-1>  =  M_2(B)
ambient  R^n  <->  R_n,   x = (x_0,...,x_{n-1})  <->  sum_e x_e X^e
T = cyclic shift,  (Tx)_e = x_{e-1 mod n}   (= multiplication by X)
B_s(x,y) = sum_e theta_s(x_e) y_e  in R        (theta in the FIRST slot)
b_s(x,y) = Lambda(B_s(x,y))        in F_q
C^{perp_s} = { y in R^n : B_s(x,y) = 0 for all x in C }     (RIGHT orthogonal)
Hull_s(C)  = C n C^{perp_s}
cyclic code of length n  =  RIGHT ideal of R_n
N = dim_{F_q} R^n = 4tn
```

---

## 1. The coefficient ring `A_t`

### 1.1 Definition, normal form, cardinality

**Lemma 1.1.** Every element of `A_t` has a unique expression `Σ_{i=0}^{t−1} a_i u^i` with
`a_i ∈ F_q`; the natural map `F_q → A_t` is injective; `|A_t| = q^t`.

*Proof.* `u^t` is monic, so Euclidean division in `F_q[u]` gives a unique remainder of
degree `< t` in each class; two distinct remainders of degree `< t` differ by a nonzero
polynomial of degree `< t`, which cannot lie in `(u^t)`. Injectivity of `F_q → A_t`
follows (a nonzero constant has degree 0 `< t`). Cardinality: `q` choices for each of the
`t` coefficients. ∎

Consequences: `A_t` is commutative (`u` is an indeterminate, so it commutes with `F_q`,
and `F_q` is commutative), and `u^{t−1} ≠ 0`, `u^t = 0`.

### 1.2 Units, maximal ideal, residue field

**Lemma 1.2.** (i) `a = Σ a_i u^i` is a unit in `A_t` ⟺ `a_0 ≠ 0`.
(ii) The non-units form the ideal `(u)`; `A_t` is **local** with maximal ideal `(u)` and
residue field `A_t/(u) ≅ F_q`. (iii) `|A_t^×| = (q−1)q^{t−1}`, `|(u)| = q^{t−1}`,
`|(u)^i| = q^{t−i}`.

*Proof.* (i) If `a_0 ≠ 0`, write `a = a_0(1 + b)` with `b ∈ (u)`; then `b^t = 0`, so
`(1+b)^{−1} = Σ_{j=0}^{t−1} (−b)^j`. Conversely if `a ∈ (u)` and `a` were a unit then
`(a) = A_t`, i.e. `1 ∈ (u)`; applying the homomorphism `A_t → F_q`, `u ↦ 0`, gives `1 = 0`,
a contradiction.
(ii) By (i) the set of non-units is exactly `(u)`, an ideal; a commutative ring whose
non-units form an ideal is local with that ideal maximal. The quotient map
`Σ a_i u^i ↦ a_0` identifies `A_t/(u)` with `F_q`.
(iii) Count coefficient vectors: `a_0 ∈ F_q^×` (`q−1` choices) and `a_1,…,a_{t−1}`
arbitrary (`q^{t−1}`); `(u)^i = {Σ_{j≥i} a_j u^j}` has `q^{t−i}` elements. ∎

### 1.3 Ideals: `A_t` is a finite chain ring

**Lemma 1.3.** The ideals of `A_t` are exactly `(u^0) = A_t, (u), (u²), …, (u^{t−1}),
(u^t) = 0`. They are totally ordered by inclusion; in particular `A_t` is a principal
ideal ring and a **chain ring** of length `t`.

*Proof.* Let `I ≠ 0` be an ideal and put `i = min{v(a) : 0 ≠ a ∈ I}`. Choose `a ∈ I` with
`v(a) = i`; then `a = u^i(a_i + uc)` with `a_i ≠ 0`, and `a_i + uc` is a unit by Lemma
1.2(i), so `u^i = a(a_i+uc)^{−1} ∈ I`, whence `(u^i) ⊆ I`. Conversely every `b ∈ I` has
`v(b) ≥ i`, i.e. `b ∈ (u^i)`. Hence `I = (u^i)`. The chain is strictly decreasing because
`u^i ∉ (u^{i+1})` (valuation). ∎

### 1.4 Nilpotency, radical, socle

**Lemma 1.4.** (i) `(u)` is nilpotent with `(u)^t = 0`, `(u)^{t−1} ≠ 0`; the nilpotency
index of `A_t` is `t`. (ii) `Jac(A_t) = (u)`. (iii) `soc(A_t) := ann((u)) = (u^{t−1})`,
which is `1`-dimensional over `F_q`.

*Proof.* (i) Immediate from `u^t = 0`, `u^{t−1} ≠ 0`.
(ii) By Lemma 1.2(ii), `(u)` is the unique maximal ideal, hence equals the Jacobson
radical.
(iii) `b ∈ ann((u)) ⟺ ub = 0 ⟺ v(b) ≥ t−1 ⟺ b ∈ (u^{t−1})`; and
`(u^{t−1}) = {a u^{t−1} : a ∈ F_q} ≅ F_q`. ∎

### 1.5 The Frobenius form `λ`

**Lemma 1.5.** `λ(ab)` is a non-degenerate, symmetric, associative bilinear form on the
`F_q`-space `A_t`, and `λ` is **ideal-catching**: every nonzero ideal of `A_t` contains an
element `c` with `λ(c) ≠ 0`.

*Proof.* Symmetry is clear (`A_t` commutative). Associativity:
`λ((ab)c) = λ(a(bc))`. Non-degeneracy: let `0 ≠ a`, `i = v(a)`, and take
`b = u^{t−1−i}`; then `ab = a_i u^{t−1}` (all higher terms carry `u^{≥t} = 0`), so
`λ(ab) = a_i ≠ 0`. Ideal-catching: by Lemma 1.3 every nonzero ideal contains `(u^{t−1})`,
and `λ(u^{t−1}) = 1`. ∎

### 1.6 Automorphisms of `A_t` (complete description)

**Lemma 1.6.** Every `F_p`-algebra endomorphism `τ` of `A_t` is determined by
`τ|_{F_q} = Frob^{s}` (`s` mod `r`) and `τ(u) = c ∈ (u)`. It is an automorphism ⟺
`(c) = (u)`, i.e. `c = c_1u + c_2u² + …` with `c_1 ≠ 0`. Consequently

$$|\operatorname{Aut}(A_t)| = r\,(q-1)\,q^{\,t-2}\ \ (t\ge 2),\qquad |\operatorname{Aut}(A_1)| = r .$$

*Proof.* `A_t` is generated as an `F_p`-algebra by `F_q` and `u`, so `τ` is determined by
`τ|_{F_q}` and `c := τ(u)`. Since `u^t = 0` we need `c^t = 0`, i.e. `c ∈ (u)`. The
restriction `τ|_{F_q} : F_q → A_t` is an `F_p`-algebra embedding; the composite
`F_q → A_t → A_t/(u) = F_q` is an `F_p`-automorphism of `F_q`, i.e. `Frob^{s}`. Because
`F_q/F_p` is finite separable and hence étale and `(u)` is nilpotent, the infinitesimal
lifting property makes the lift of a given residue map **unique**
(`Hom_{F_p}(F_q, A_t) → Hom_{F_p}(F_q, F_q)` is a bijection), so `τ|_{F_q} = Frob^{s}`
acting coefficient-wise. Surjectivity of `τ` ⟺ its image contains a generator of the
maximal ideal ⟺ `(c) = (u)` ⟺ `c_1 ≠ 0` (Lemma 1.3). Finally, the number of `c` with
`(c) = (u)` is `|(u)| − |(u²)| = q^{t−1} − q^{t−2} = (q−1)q^{t−2}`. ∎

**Convention 1.7 (coefficient-Frobenius subgroup).** We use **only** the subgroup
`{σ_s : s ∈ Z/r}` of `Aut(A_t)` obtained by taking `c = u` in Lemma 1.6, i.e. `σ_s` fixes
`u`. This is an unstated restriction in the Phase-0 write-up and is now explicit. The
general theory for an arbitrary `τ ∈ Aut(A_t)` is recorded as T-027 (`θ_τ² = τ²`,
`(C^⊥)^⊥ = τ²(C)`, reflexive ⟺ `τ² = id`); the criterion `r ∣ 2s` is the specialisation
`τ = σ_s`.

---

## 2. The ring `R = M_2(A_t)`

### 2.1 Elements, matrix units, cardinality, identity

`R` is the ring of `2×2` matrices over `A_t` with the usual operations; `I = E_11 + E_22`
is the identity; the matrix units satisfy

$$E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \sum_i E_{ii}=I,\qquad E_{ij}^T = E_{ji}.$$

Every `X ∈ R` is `Σ_{i,j} x_{ij}E_{ij}` uniquely, so **Lemma 2.1:** `|R| = |A_t|^4 = q^{4t}`.
`R` is non-commutative: `E_12E_21 = E_11 ≠ E_22 = E_21E_12`.

### 2.2 Centre

**Lemma 2.2.** `Z(R) = {aI : a ∈ A_t} ≅ A_t`; hence `|Z(R)| = q^t`.

*Proof.* Let `X = (x_{ij})` be central. Comparing `XE_11` and `E_11X`:
`XE_11 = x_{11}E_11 + x_{21}E_21`, `E_11X = x_{11}E_11 + x_{12}E_12`, so `x_{21} = 0` and
`x_{12} = 0`, i.e. `X` is diagonal. Then `XE_12 = x_{11}E_12` and `E_12X = x_{22}E_12`
give `x_{11} = x_{22} =: a`, so `X = aI`. Conversely `A_t` is commutative, so `aI` is
central. The map `a ↦ aI` is injective, hence `Z(R) ≅ A_t`. ∎

### 2.3 Units

**Lemma 2.3.** For `X ∈ R`: `X ∈ R^×` ⟺ `det X ∈ A_t^×` ⟺ `det(X mod u) ≠ 0` ⟺
`X mod u ∈ GL_2(F_q)`. Moreover

$$|R^{\times}| = |GL_2(A_t)| = q^{4(t-1)}\,(q^2-1)(q^2-q).$$

*Proof.* If `det X` is a unit, `X · adj(X) = det(X) I` gives the inverse
`X^{−1} = (det X)^{−1} adj(X)`. If `X` is a unit, `1 = det(X X^{−1}) = det X · det X^{−1}`
forces `det X ∈ A_t^×`. The middle equivalence is Lemma 1.2(i) applied to `det X`, i.e.
its constant coefficient is nonzero, which is exactly `det(X mod u) ≠ 0`. For the count:
reduction `π : GL_2(A_t) → GL_2(F_q)` is surjective (lift a matrix over `F_q` entrywise)
with kernel `I + M_2((u))`, of size `|(u)|^4 = q^{4(t−1)}`; and
`|GL_2(F_q)| = (q²−1)(q²−q)` (choose the first column nonzero, then the second outside its
span). ∎

The non-units are the matrices whose reduction mod `u` is singular; `|R \ R^×| =
q^{4t} − q^{4t−4}(q²−1)(q²−q)`.

### 2.4 Jacobson radical and nilpotency

**Lemma 2.4.** `Jac(R) = M_2((u)) = uR`; `R/Jac(R) ≅ M_2(F_q)`; `Jac(R)^t = 0` and
`Jac(R)^{t−1} ≠ 0`, so the nilpotency index of `Jac(R)` is `t`.

*Proof.* `uR = M_2((u))` is a two-sided ideal with `(uR)^t = M_2((u)^t) = 0`, so it is
nilpotent. A nilpotent ideal lies in the Jacobson radical: if `x ∈ uR` and `y ∈ R`, then
`xy ∈ uR` is nilpotent, so `1 − xy` is a unit, which is the standard criterion for
`x ∈ Jac(R)`. Hence `uR ⊆ Jac(R)`, and since `uR ⊆ Jac(R)`,
`Jac(R)/uR = Jac(R/uR) = Jac(M_2(F_q)) = 0`, the last equality because `M_2(F_q)` is
simple Artinian, hence semisimple. Therefore `Jac(R) = uR`. Finally
`Jac(R)^i = M_2((u)^i)`, which is `0` exactly for `i ≥ t`. ∎

### 2.5 Two-sided ideals

**Lemma 2.5.** The two-sided ideals of `R` are exactly `M_2(J)` with `J` an ideal of
`A_t`; hence, by Lemma 1.3, they are `u^i R` for `i = 0,…,t` — exactly `t+1` of them.

*Proof.* Let `I` be a two-sided ideal of `M_2(A_t)`. Put
`J = {a ∈ A_t : aE_11 ∈ I}`, an ideal of `A_t`. If `X = (x_{ij}) ∈ I`, then
`E_{a1} X E_{1b} = x_{11}E_{ab} ∈ I` for all `a,b`, so `x_{11}E_{11} ∈ I`, i.e.
`x_{11} ∈ J`; applying the same with `E_{ai}XE_{jb}` shows every entry lies in `J`, so
`X ∈ M_2(J)` and `I ⊆ M_2(J)`. Conversely if `a ∈ J` then `aE_{11} ∈ I` and
`E_{i1}(aE_{11})E_{1j} = aE_{ij} ∈ I`, so `M_2(J) ⊆ I`. ∎

**Remark (why this matters).** Two-sided ideals are far too few to be the cyclic codes:
at `q = 2, n = 3` there are `4` two-sided ideals of `R_3` (ideals of `B = F_2 × F_4`) but
`35` right ideals. Our convention is right ideals (§5.1).

### 2.6 Right ideals and the Morita correspondence (with proof)

**Proposition 2.6.** For any ring `S` and `m ≥ 1`, the map

$$W \longmapsto I_W := \{M \in M_m(S) : \text{every column of } M \text{ lies in } W\}$$

is a bijection between right `S`-submodules `W ⊆ S^m` (column vectors) and right ideals of
`M_m(S)`; the inverse sends a right ideal `I` to the set `W_I` of all columns of elements
of `I`. If `S` is an `F_q`-algebra, then `dim_{F_q} I_W = m · dim_{F_q} W`.

*Proof.* (i) `I_W` is a right ideal: `0 ∈ I_W`; it is closed under addition; and for
`M ∈ I_W`, `A ∈ M_m(S)`, the columns of `MA` are `S`-linear combinations of the columns
of `M`, hence lie in `W`.
(ii) `W_I` is a right `S`-submodule: sums and scalar multiples of occurring columns occur
as columns of the corresponding combinations (use `E_{ii}` to place a column in position
`i`).
(iii) `I_{W_I} = I`: `⊇` is clear. For `⊆`, let `M ∈ I_{W_I}` have columns `v_1,…,v_m`.
Each `v_i ∈ W_I`, so `v_i` is a column of some `X_i ∈ I`, say in position `j_i`. Then
`X_i E_{j_i i} ∈ I` is the matrix with `v_i` in column `i` and zeros elsewhere, and
`M = Σ_i X_iE_{j_i i} ∈ I`.
(iv) `W_{I_W} = W`: `⊆` clear; conversely if `w ∈ W` then the matrix with first column
`w` and all other columns zero lies in `I_W`, so `w ∈ W_{I_W}`.
(v) Dimension: `I_W` consists of the `m`-tuples of elements of `W`, one per column, so
`I_W ≅ W^m` as `F_q`-spaces. ∎

**Corollary 2.7.** (i) For `S = K` a field, right ideals of `M_2(K)` ↔ subspaces of `K²`,
so their number is `1 + (q_K+1) + 1 = q_K + 3` and their `K`-dimensions are
`0, 2, 2, …, 2, 4`. (This reproduces the audited counts `5, 7, 11, 12` for
`q = 2, 4, 8, 9`.)
(ii) For `S = A_t`, right ideals of `R` ↔ `A_t`-submodules of `A_t²`; in particular for
`t = 2` the count is `q² + 3q + 5` (verified: `33` at `q = 4`).

### 2.7 Module structures (fixed for Phase 1)

| Symbol | Structure | Dimension / size |
|---|---|---|
| `_R R` | `R` as a left module over itself | `dim_{F_q} = 4t` |
| `R_R` | `R` as a right module over itself | `dim_{F_q} = 4t` |
| `A_t²` | right `A_t`-module (Morita side) | `dim_{F_q} = 2t` |
| `R^n` | right `R`-module, `(x·a)_e = x_e a` | `dim_{F_q} = 4tn = N`; `|R^n| = q^{4tn}` |
| `R_n` | right `R_n`-module ≅ `R^n` | idem |
| `B²` | right `B`-module (Morita side for `R_n`) | — |

### 2.8 Cardinality summary

| Object | Cardinality |
|---|---|
| `A_t` | `q^t` |
| `A_t^×` | `(q−1)q^{t−1}` |
| `(u)^i ≤ A_t` | `q^{t−i}` |
| `R = M_2(A_t)` | `q^{4t}` |
| `R^× = GL_2(A_t)` | `q^{4(t−1)}(q²−1)(q²−q)` |
| `Jac(R) = uR` | `q^{4(t−1)}` |
| `R/Jac(R) ≅ M_2(F_q)` | `q^4` |
| `Z(R) ≅ A_t` | `q^t` |
| `R^n` | `q^{4tn}` |

---

## 3. The cyclic ambient `R_n`

**Lemma 3.1.** `R_n := R[X]/⟨X^n − 1⟩ ≅ M_2(B)` with `B := A_t[X]/⟨X^n−1⟩`; `X` is
central, `B` is commutative, and `R_n` is a free `A_t`-module of rank `4n`.

*Proof.* `X` is an indeterminate over `R`, hence central in `R[X]`, and
`R[X] ≅ M_2(A_t[X])` by applying `M_2(−)` entrywise; quotienting by the ideal generated by
the central element `X^n − 1` gives `M_2(A_t[X])/M_2((X^n−1)) ≅ M_2(A_t[X]/(X^n−1)) =
M_2(B)`. `B` is commutative (`A_t` commutative, `X` central), and `B` is a free
`A_t`-module of rank `n` (division by the monic polynomial `X^n − 1`), so `R_n` is free of
rank `4n` over `A_t`. ∎

**Lemma 3.2 (ambient identification).** The map `R^n → R_n`,
`(x_0,…,x_{n−1}) ↦ Σ_e x_e X^e`, is an isomorphism of right `R`-modules, and under it the
cyclic shift `T`, `(Tx)_e = x_{e−1 mod n}`, corresponds to multiplication by `X` on the
right. `T` is right-`R`-linear.

*Proof.* Bijectivity is Lemma 3.1 (remainders of degree `< n` are unique). For
`a ∈ R`, `(x·a)_e = x_ea` maps to `Σ_e x_eaX^e = (Σ_e x_eX^e)a` since `a` commutes with
`X`. Multiplication by `X` sends `Σ x_eX^e` to `Σ x_e X^{e+1}`, whose coefficient of
`X^e` is `x_{e−1}` (indices mod `n`, because `X^n = 1`), i.e. `T`. `T` is right-`R`-linear
because it is right multiplication by the central element `X`. ∎

---

## 4. Automorphisms and anti-automorphisms (Task B)

### 4.1 `σ_s` on `F_q`

**Lemma 4.1.** `σ_s(a) = a^{p^s}` is an `F_p`-automorphism of `F_q`, of order
`r/gcd(r,s)`; `σ_s = id ⟺ r ∣ s`; `σ_s` is non-trivial ⟺ `r ∤ s`.

*Proof.* The Frobenius `a ↦ a^p` generates `Gal(F_q/F_p) ≅ Z/r` (standard: `F_q/F_p` is
Galois of degree `r` with cyclic Galois group generated by the Frobenius), so
`σ_s = Frob^s` has order `r/gcd(r,s)` and is the identity exactly when `r ∣ s`. ∎

### 4.2 Extension to `A_t`, `R`, `R_n`

**Lemma 4.2.** `σ_s(Σ a_i u^i) := Σ a_i^{p^s} u^i` is a well-defined ring automorphism of
`A_t` fixing `u`; extended entrywise it is a ring automorphism of `R` and (with
`σ_s(X) = X`) of `R_n`. On `R` it satisfies `σ_s(aI) = σ_s(a) I` and
`σ_s(X^T) = σ_s(X)^T`; hence `σ_s` **commutes with the transpose**.

*Proof.* Well-defined: `σ_s` is a ring automorphism of `F_q[u]` (coefficient-wise) and
maps `(u^t)` onto itself, so it descends to the quotient. Entrywise extension preserves
matrix addition and multiplication componentwise. The two displayed identities are
immediate (the transpose permutes entries, and `σ_s` acts entrywise). ∎

### 4.3 `θ_s = σ_s ∘ transpose` is an anti-automorphism

**Lemma 4.3.** `θ_s` is additive, bijective, and `θ_s(XY) = θ_s(Y)θ_s(X)`; i.e. `θ_s` is
an **anti-automorphism** of `R` (and of `R_n`). It is `σ_s`-semilinear:
`θ_s(aX) = σ_s(a)θ_s(X)` for `a ∈ A_t` (in particular `θ_s(aI) = σ_s(a) I`), and it fixes
`F_p` elementwise.

*Proof.* Additivity and bijectivity are clear (both `σ_s` and the transpose are additive
bijections). Multiplicativity reversed:
`θ_s(XY) = σ_s((XY)^T) = σ_s(Y^TX^T) = σ_s(Y^T)σ_s(X^T) = θ_s(Y)θ_s(X)`. Semilinearity:
`θ_s(aX) = σ_s((aX)^T) = σ_s(a X^T) = σ_s(a) σ_s(X^T) = σ_s(a)θ_s(X)`. Over `F_p`,
`σ_s = id` and the transpose fixes scalars, so `θ_s(cX) = c θ_s(X)` for `c ∈ F_p`. ∎

### 4.4 Powers, square, order

**Lemma 4.4.** For all `k ≥ 1`: `θ_s^{2k} = σ_{2ks}` and `θ_s^{2k−1} = θ_{(2k−1)s}`; in
particular `θ_s² = σ_{2s}`. Moreover `θ_s` is **never** the identity, and

$$\operatorname{ord}(\theta_s) = \frac{2r}{\gcd(r,2s)} .$$

*Proof.* `θ_s²(X) = θ_s(σ_s(X^T)) = σ_s(σ_s(X^T)^T) = σ_s(σ_s(X)) = σ_{2s}(X)`, using
Lemma 4.2 (`σ_s` commutes with the transpose, so `σ_s(X^T)^T = σ_s(X)`). The general
power formula follows by induction using `σ_k ∘ θ_{s'} = θ_{s'+k}` (immediate from the
definitions). Since `θ_{s'}(E_12) = E_21 ≠ E_12 = σ_{s'}(E_12)`... more precisely
`θ_{s'} = id` would force `X^T = σ_{−s'}(X)` for all `X`, false at `X = E_12` (the
transpose of `E_12` is `E_21`, while `σ_{−s'}(E_12) = E_12`). Hence the order of `θ_s` is
even, and the least `2k` with `θ_s^{2k} = σ_{2ks} = id` is `2k = 2r/gcd(r,2s)` by Lemma
4.1. ∎

### 4.5 Involutivity

**Theorem 4.5.** `θ_s` is an involution ⟺ `σ_{2s} = id` ⟺ `r ∣ 2s` ⟺
`\dfrac{r}{\gcd(r,2)} \;\big|\; s`. Explicitly:

* `r` even: `s ≡ 0` or `s ≡ r/2 (mod r)` — exactly two solutions mod `r`;
* `r` odd: `s ≡ 0 (mod r)` — the trivial one only.

*Proof.* Immediate from Lemma 4.4 and Lemma 4.1; the divisibility
`r ∣ 2s ⟺ (r/gcd(r,2)) ∣ s` is elementary. ∎

### 4.6 The four regimes (consequences)

| `r` | reflexive `s` (mod `r`) | non-trivial reflexive? | `ord(θ_s)` at `s=1` | regime available |
|---|---|---|---|---|
| 2 (`q=4,9,25`) | `0, 1` | **yes**: `s=1` | 2 | R0 + **R1** |
| 4 (`q=16`) | `0, 2` | **yes**: `s=2` | 4 | R0 + **R1** |
| 3 (`q=8,27`) | `0` | **no** | 6 | R0 only (R3 otherwise) |
| odd `r` | `0` | **no** | `2r/gcd(r,2)` | R0 only |

**Corollary 4.6 (the odd-`r` obstruction).** For `r` odd, `r ∣ 2s ⟺ r ∣ s ⟺ σ_s = id`.
Hence for odd `r` **a non-trivial Galois action and reflexivity are mutually exclusive**:
`q = 8` and `q = 27` admit no non-trivial reflexive Galois parameter. For even `r`,
`s = r/2` is the unique non-trivial reflexive choice, and there `σ_s` has order `2` while
`θ_s` is an involution distinct from the transpose: this is the **genuine non-trivial
reflexive case (R1)**.

### 4.7 Interaction identities (used throughout)

$$\sigma_k\sigma_{s}=\sigma_{k+s},\qquad \sigma_k\theta_s=\theta_{s+k}=\theta_s\sigma_k,\qquad
\theta_s\big(B_s(x,y)\big)=B_s\big(y,\sigma_{2s}x\big)\ \ (\text{§6}).$$

The last identity is proved in §6.3 and is the engine of the double-dual theorem.

---

## 5. Module conventions (Task C)

### 5.1 The right-module convention (definition)

**Definition 5.1 (cyclic code).** The ambient space is `R^n` with the right `R`-module
structure `(x·a)_e = x_e a`. A **cyclic code of length `n` over `R`** is a right ideal of
`R_n`, equivalently (via Lemma 3.2) an `F_q`-subspace `C ⊆ R^n` such that

1. `C` is closed under right multiplication by `R` (`x ∈ C, a ∈ R ⇒ x·a ∈ C`), and
2. `C` is closed under the cyclic shift `T`.

Equivalently: `C` is a right `R_n`-submodule of `R_n`.

**Convention 5.2 (why right, not left).** The pairing of §6 is
`B_s(x,y) = Σ_e θ_s(x_e) y_e`, which is **right-`R`-linear in `y`** and `θ_s`-semilinear
in `x`. Consequently the orthogonal of a **right** module is again a **right** module
(Corollary 6.4). The choice is not cosmetic: with the *plain* product the side matters
decisively (§5.4).

**Lemma 5.3 (closure under the shift is closure under `X`).** Under the identification of
Lemma 3.2, condition 2 is equivalent to closure under right multiplication by `X`; hence
`C` is a right ideal of `R_n` iff it is an `R`-submodule closed under `T`.

*Proof.* `T` is right multiplication by `X` (Lemma 3.2), and `R_n` is generated as a ring
by `R` and `X`. ∎

### 5.2 The two orthogonals and their relation

**Definition 5.4.** For `C ⊆ R^n`:

$$C^{\perp_s} := \{y : B_s(x,y)=0 \ \forall x\in C\}\quad(\textbf{right} \text{ orthogonal}),$$
$${}^{\perp_s}\!C := \{y : B_s(y,x)=0 \ \forall x\in C\}\quad(\textbf{left} \text{ orthogonal}).$$

**Lemma 5.5 (side convention).** Let `C ⊆ R^n` be a **right** `R`-submodule. Then *both*
orthogonals are again right `R`-submodules:

$$C^{\perp_s}=\{y : B_s(x,y)=0\ \forall x\in C\},\qquad
{}^{\perp_s}\!C=\{y : B_s(y,x)=0\ \forall x\in C\}.$$

*Proof.* (i) For `a ∈ R`, `B_s(x, y·a) = Σ_e θ_s(x_e)(y_ea) = (Σ_e θ_s(x_e)y_e)a =
B_s(x,y)a`, so `B_s(x,y)=0 ⇒ B_s(x, y·a) = 0`.
(ii) Using that `θ_s` is an **anti**-automorphism, `θ_s(y_ea) = θ_s(a)θ_s(y_e)`, hence
`B_s(y·a, x) = Σ_e θ_s(y_ea)x_e = θ_s(a)\,Σ_e θ_s(y_e)x_e = θ_s(a)\,B_s(y,x)`, which
vanishes whenever `B_s(y,x) = 0`. ∎

**Remark 5.6 (why right, and no claim about left).** The mechanism in Lemma 5.5(ii) is
exactly that `θ_s` is an *anti*-automorphism: it converts the **right** action
`y ↦ y·a` in the first slot into the **left** multiplier `θ_s(a)`. For a **left** module
`C`, replacing `x` by `a·x` gives `B_s(a·x, y) = Σ_e θ_s(x_e)θ_s(a)y_e`, which is not a
left multiple of `B_s(x,y)`; the analogous closure therefore fails in general. We work
**exclusively with right modules** and make **no** claim about left modules. (The relation
between the two orthogonals of a right module is Lemma 5.7.)

> **Correction (Phase-1 final verification, §5.6.4).** The last clause above — "the
> analogous closure therefore fails in general" — is **wrong** and is withdrawn: the
> orthogonal of a left module *is* a left module, always (Lemma 5.6b(2)); the correct
> mechanism transfers the multiplier to the other slot (Lemma 5.6a(3)–(4)) instead of
> factoring it out. The premise (that `B_s(a·x,y)` is not a left multiple of `B_s(x,y)`)
> is correct. Nothing in §§6–8 uses this remark.

**Lemma 5.7 (left/right orthogonal identity).** For every `F_q`-subspace `C ⊆ R^n`,

$${}^{\perp_s}\!C \;=\; \big(\sigma_{-2s}C\big)^{\perp_s}.$$

*Proof.* `y ∈ ^{⊥_s}C ⟺ B_s(y,x) = 0 ∀x ∈ C`. By the key identity (§6.3),
`B_s(y,x) = θ_s(B_s(σ_{−2s}x, y))`... more directly: from
`θ_s(B_s(u,v)) = B_s(v, σ_{2s}u)` with `u = σ_{−2s}x`, `v = y`, we get
`θ_s(B_s(σ_{−2s}x, y)) = B_s(y, x)`. Since `θ_s` is a bijection, `B_s(y,x) = 0 ⟺
B_s(σ_{−2s}x, y) = 0`. Hence `y ∈ ^{⊥_s}C ⟺ B_s(x', y) = 0 ∀x' ∈ σ_{−2s}C ⟺
y ∈ (σ_{−2s}C)^{⊥_s}`. ∎

### 5.3 Morita coordinate convention

**Convention 5.8.** Under Proposition 2.6 and `R_n ≅ M_2(B)`, cyclic codes correspond to
**right `B`-submodules `W ⊆ B²` (columns)**: `C ↔ W`, `C = {M : every column of M ∈ W}`,
`dim_{F_q} C = 2·dim_{F_q} W`. When additionally `X^n−1 = ∏ f_j` is squarefree with
`deg f_j = d_j`, CRT gives `B ≅ ∏_j F_{q^{d_j}}` and hence

$$W = \bigoplus_j W_j,\quad W_j \subseteq \mathbb F_{q^{d_j}}^2,\qquad
\#\{\text{cyclic codes}\} = \prod_j \sum_{i=0}^{2}\begin{bmatrix}2\\ i\end{bmatrix}_{q^{d_j}}$
( $= \prod_j (q^{d_j}+3)$ ),

which is T-018; the **squarefree hypothesis is essential** (`q=4, n=2`: the formula would
give `49`, the truth is `33`).

### 5.4 The side-flip phenomenon (Phase-0 item O1, proved)

The point of `θ_s` is that the *plain* product pairing
`P(x,y) := Σ_e x_e y_e` does **not** give a perfect duality on right modules.

**Proposition 5.9 (side flip).** Let `n = 1`, `R = M_2(A_t)`, let `P(x,y) := xy` be the
**plain matrix product**, and for a subset `C ⊆ R` put

$$C^{\perp_P} := \{y \in R : xy = 0\ \text{for all } x \in C\}$$

(**the code is always in the first slot**). Take `C_r := E_11 R` (matrices with second row
zero — a **right** ideal) and `C_l := R E_11` (matrices with second column zero — a
**left** ideal). Then

* `C_r^{⊥_P} = {0}`, so `|C_r|·|C_r^{⊥_P}| = q^{2t} ≠ q^{4t} = |R|`: the plain product
  **fails** on right ideals;
* `C_l^{⊥_P} = {[[0,0],[r,s]] : r,s ∈ A_t}` has size `q^{2t} = |C_l|`, so
  `|C_l|·|C_l^{⊥_P}| = q^{4t} = |R|`: the plain product is **perfect** on this left ideal.

Hence the plain product is a perfect duality for left ideals and **fails** for right
ideals. (Verified computationally in `04_COMPUTATION/ring_structure_checks.py`,
`q = 4, 8, 9, 16, 25, 27`, `t = 1`, and `q = 4`, `t = 2`.)

*Proof.* Let `y = [[p,q],[r,s]]`. For `x ∈ C_r`, `x = [[a,b],[0,0]]` and
`xy = [[ap+br, aq+bs],[0,0]]`, which vanishes for **all** `a,b ∈ A_t` iff
`p = q = r = s = 0`, i.e. `y = 0`; and `|C_r| = q^{2t}` (two free entries `a,b`).
For `x ∈ C_l`, `x = [[a,0],[c,0]]` and `xy = [[ap, aq],[cp, cq]]`, which vanishes for all
`a,c ∈ A_t` iff `p = q = 0`, i.e. `y ∈ {[[0,0],[r,s]]}`, a set of size `q^{2t}`; and
`|C_l| = q^{2t}` (two free entries `a,c`). ∎

**Remark 5.9a (why the slot convention is part of the statement).** The outcome depends on
which slot the code sits in: for the **same** left ideal `C_l`, the set
`{y : yx = 0 ∀x ∈ C_l}` (code in the second slot) is `{0}`, i.e. it degenerates. This is
exactly the asymmetry recorded as Phase-0 item O1: without an anti-automorphism there is
no slot choice that works uniformly for right modules.

**Remark 5.9b (a pairing that must not be confused with `P`).** The *entry-wise*
("Frobenius") form `⟨x,y⟩ := Σ_{i,j} x_{ij}y_{ij} ∈ A_t` is a different pairing, and at
`n = 1` it is perfect on **both** `C_r` and `C_l` (both orthogonals have `F_q`-dimension
`2t`) — verified in the same script. Its failure is a phenomenon of `n ≥ 2`: it is the
form underlying the Phase-0 observation (T-006) that `dim C + dim C^{⊥}` is not constant
and that the dual of a right module need not be a right module. Nothing in this paper uses
the entry-wise form.

**Corollary 5.10.** In the `θ_s`-pairing this asymmetry disappears: for the same
`C_r = E_11R`, `|C_r^{⊥_s}| = |R|/|C_r| = q^{4t−2t} = q^{2t}` (size formula, §6.5).

### 5.5 Conventions explicitly **not** adopted

| Not adopted | What it is | Why not |
|---|---|---|
| Two-sided ideals of `R_n` | ↔ ideals of `B` | too few (`4` vs `35` at `q=2,n=3`); no hull theory |
| The quaternary (`F_4`-correspondence) family | A1's bijection with cyclic `F_4`-codes (`8` codes at `n=3`) | a different family; it contains **no** non-zero self-orthogonal and no self-dual code at `n = 3` |
| A1's "Euclidean" form `Σ_j x_j y_j` | matrix product, no transpose | degenerate on right modules: at `q=2,n=3`, `dim C + dim C^⊥` is not constant (`[(6,15),(8,10),(10,6),(12,4)]`) and there are `0` self-dual codes |
| Coefficients in a non-central subfield (e.g. `F_4 ⊂ M_2(F_2)`) | A1's parametrisation | our coefficient centre is `F_q = Z(A_t)`'s field of coefficients; mixing the two produced the earlier 27-vs-35 confusion (T-019) |

Per decision **B1**, Alahmadi–Sboui–Solé–Yemen (2013) is cited **for its framework**
(cyclic codes over `M_2(F_2)`, the `F_4`-correspondence, the residue/torsion description);
its disputed Theorem 1 is **neither restated nor challenged**, and the discrepancy is
preserved as a documented literature limitation (see
`06_AUDIT/PHASE0_RESEARCHER_DECISION_SHEET.md` §1).

### 5.6 Left and right actions: complete conventions (Task-C clarification)

This subsection makes every action used in the paper explicit — its **side**, its formula
on **coordinates**, and its behaviour under the pairing — for the three ambient objects
`R`, `R_n` and `R^n`. It is a documentation and bookkeeping section: no earlier proof is
changed, except that §5.6.4 records **one correction** to the final sentence of
Remark 5.6 (a genuine error, found during the Phase-1 final verification).

#### 5.6.1 The four actions on `R = M_2(A_t)`

| # | Action | Notation | Formula | Kind |
|---|---|---|---|---|
| A1 | right multiplication | `X ↦ Xa` | `col_j(Xa) = Σ_k a_{kj} col_k(X)` | right action |
| A2 | left multiplication | `X ↦ aX` | `row_i(aX) = Σ_k a_{ik} row_k(X)` | left action |
| A3 | coefficient Frobenius | `σ_k` | `σ_k(X)_{ij} = (X_{ij})^{p^k}` (entry-wise) | automorphism |
| A4 | transpose–Frobenius | `θ_s = σ_s ∘ (·)^T` | `θ_s(XY) = θ_s(Y)θ_s(X)` | anti-automorphism |

Facts used throughout: `(aX)b = a(Xb)` (associativity — `R` is an `(R,R)`-bimodule over
itself); the two actions agree on `F_p`-scalars because `F_p·I ⊆ Z(R)`; `σ_k` is a ring
automorphism fixing `u` (Convention 1.7) and `θ_s = σ_s ∘ (·)^T` is an anti-automorphism
(Lemma 4.3). Note the **side convention**: A1 mixes **columns**, A2 mixes **rows**.

**Proposition 2.6, both handednesses (completed).** With the column convention of
Proposition 2.6:

* **right** ideals of `R` ↔ `A_t`-submodules `W ⊆ A_t²` of the **column** space:
  `I_W = {X : every column of X lies in W}`, `dim_{F_q} I_W = 2 dim_{F_q} W`;
* **left** ideals of `R` ↔ `A_t`-submodules `U ⊆ A_t²` of the **row** space:
  `L_U = {X : every row of X lies in U}`, `dim_{F_q} L_U = 2 dim_{F_q} U`;
* `X ↦ X^T` is a bijection from the family of right ideals onto the family of left
  ideals, so the two families are **equinumerous** — `q+3` at `t = 1`, `q²+3q+5` at
  `t = 2` (`33` at `q = 4, t = 2`).

#### 5.6.2 The actions on `R_n` and on code coordinates

The ambient space of a code is `R^n` (Definition 5.1). Under `R_n ≅ M_2(B)`
(Lemma 3.1), `x ∈ R^n ↔ Σ_e x_e X^e ∈ M_2(B)`:

| # | Action | Formula on coordinates | Remark |
|---|---|---|---|
| B1 | right action of `a ∈ R` | `(x·a)_e = x_e a` | the right `R`-module structure of Definition 5.1 |
| B2 | left action of `a ∈ R` | `(a·x)_e = a x_e` | the left `R`-module structure (not used for codes) |
| B3 | multiplication by `X` (either side) | `(Tx)_e = x_{e−1 mod n}` | `X` is **central** in `B`, so left = right; `T^n = 1` |
| B4 | `σ_k` on `R^n` | `σ_k(x)_e = σ_k(x_e)` (entry-wise `p^k`-power) | ring automorphism of `R_n`, fixes `X` |
| B5 | `θ_s` on `R^n` | `θ_s(x)_e = θ_s(x_e)` | anti-automorphism of `R_n`, fixes `X` |

`T` commutes with **both** the left and the right `R`-action, since it only permutes
coordinates: `(T(x·a))_e = x_{e−1}a = ((Tx)·a)_e` and `(T(a·x))_e = ax_{e−1} =
(a·(Tx))_e`. Hence a cyclic code (a right ideal of `R_n`) is exactly an `F_q`-subspace of
`R^n` closed under B1 and B3 (Definition 5.1 and Lemma 5.3), and the **same** description
with B2 in place of B1 describes the left ideals of `R_n`. The asymmetry between the sides
comes from the pairing, not from `T` (Convention 5.2).

#### 5.6.3 The pairing versus the four actions

**Lemma 5.6a (pairing/action compatibility).** For all `x, y ∈ R^n` and `a ∈ R`:

1. `B_s(x·a, y) = θ_s(a)·B_s(x,y)`;
2. `B_s(x, y·a) = B_s(x,y)·a`;
3. `B_s(a·x, y) = B_s(x, θ_s(a)·y)`;
4. `B_s(x, a·y) = B_s(θ_s^{-1}(a)·x, y)`;
5. `B_s(x, Ty) = B_s(T^{-1}x, y)`.

Items 1 and 2 are Lemma 6.2, item 5 is the computation inside the proof of
Corollary 6.4; items 3 and 4 are the left-handed counterparts.

*Proof.* (3) Both sides equal `Σ_e θ_s(x_e)θ_s(a)y_e`: the left-hand side because
`θ_s(a x_e) = θ_s(x_e)θ_s(a)`, the right-hand side by associativity
`θ_s(x_e)(θ_s(a)y_e) = (θ_s(x_e)θ_s(a))y_e`. (4) Both sides equal `Σ_e θ_s(x_e) a y_e`:
the right-hand side because `θ_s(θ_s^{-1}(a) x_e) = θ_s(x_e)θ_s(θ_s^{-1}(a)) =
θ_s(x_e)a`. ∎

**Lemma 5.6b (which side an orthogonal has — sharp form).** Let `S ⊆ R^n` be an
**arbitrary** subset. Then

1. `S^{⊥_s}` and `^{⊥_s}S` are **right** `R`-submodules of `R^n`;
2. if moreover `S` is a **left** `R`-submodule, then `S^{⊥_s}` and `^{⊥_s}S` are **left**
   `R`-submodules as well, hence `R`-subbimodules.

*Proof.* (1) Let `y ∈ S^{⊥_s}` and `a ∈ R`. By Lemma 5.6a(2),
`B_s(x, y·a) = B_s(x,y)a = 0` for every `x ∈ S`, so `y·a ∈ S^{⊥_s}`; no property of `S`
is used. For the left orthogonal, by Lemma 5.6a(1), `B_s(y·a, x) = θ_s(a)B_s(y,x) = 0`.
(2) Let `S` be a left submodule, `y ∈ S^{⊥_s}`, `a ∈ R`. By Lemma 5.6a(4),
`B_s(x, a·y) = B_s(θ_s^{-1}(a)·x, y) = 0` for every `x ∈ S`, because
`θ_s^{-1}(a)·x ∈ S`; hence `a·y ∈ S^{⊥_s}`. For the left orthogonal, by Lemma 5.6a(3),
`B_s(a·y, x) = B_s(y, θ_s(a)·x) = 0` because `θ_s(a)·x ∈ S`. ∎

Part 1 strengthens Lemma 5.5, whose right-module hypothesis is in fact unnecessary; part 2
is the left-handed statement that Remark 5.6 asserted to fail.

#### 5.6.4 Correction to Remark 5.6 (recorded openly)

Remark 5.6 ends: *"For a **left** module `C`, replacing `x` by `a·x` gives
`B_s(a·x,y) = Σ_e θ_s(x_e)θ_s(a)y_e`, which is not a left multiple of `B_s(x,y)`; the
analogous closure therefore fails in general."*

The **premise is correct** — `B_s(a·x,y)` is indeed not, in general, a left multiple of
`B_s(x,y)` (an explicit witness is printed in `module_actions_log.txt`, e.g. at
`q = 4, t = 1, n = 1, s = 0`: `B_s(a·x,y) = [[3,0],[2,1]]` while
`a·B_s(x,y) = [[2,3],[1,0]]`). The **conclusion is wrong**: the criterion being tested —
factoring the multiplier out of `B_s` — is not the one that governs closure of an
orthogonal. By Lemma 5.6a(3)–(4) the multiplier is not extracted but **transferred to the
other slot**, and by Lemma 5.6b(2) the orthogonal of a left module **is** a left module,
always. The last clause of Remark 5.6 is therefore **withdrawn**; it is superseded by
Lemma 5.6b.

Scope of the correction: nothing in §§6–8 depends on Remark 5.6. Every statement there
concerns right modules and rests on Lemma 6.2 / Corollary 6.4, which are untouched. The
convention itself is unchanged: we work with right modules (Definition 5.1,
Convention 5.2) because only for them is the *dual of a cyclic code again a cyclic code*
(Corollary 6.4) — a left module has no shift-stability to preserve.

**Remark 5.6c (at `n = 1` the left dual is even two-sided).** At `n = 1` and for a left
ideal `L ⊆ R`, `L^{⊥_s} = {y ∈ R : my = 0 ∀ m ∈ θ_s(L)}`; since `θ_s` is an
anti-automorphism, `θ_s(L)` is a **right** ideal, so this set is the right annihilator of
a right ideal, hence a **two-sided** ideal of `R` — one of the `t+1` ideals `u^iR` (§2).
(Verified for `q = 4, 9, 8` and `t = 1, 2`.) At `n ≥ 2` no such description is available:
`B_s(c,y) = Σ_e θ_s(c_e)y_e` is not a coefficient of the product in `M_2(B)`.

#### 5.6.5 Computational corroboration of §5.6

`04_COMPUTATION/module_actions_checks.py` (log `module_actions_log.txt`, **276 of 276
checks PASS**) re-derives the whole of §5.6 from the definitions, importing only the
`F_q`/`A_t`/`M_2(A_t)` arithmetic and the `F_q`-linear algebra of
`ring_structure_checks.py`, and building `B = A_t[X]/⟨X^n−1⟩` and `M_2(B)` afresh.

| Part | Content | Parameters |
|---|---|---|
| A | A1–A2 on `R`: column/row mixing, `(aX)b = a(Xb)`, Morita in **both** handednesses, `dim I_W = dim L_U = 2 dim W`, transpose bijection, `F_p` centrality | `q = 4, 9` (`t = 1`), `q = 4` (`t = 2`) |
| B | `X` central in `B`, `X^n = 1`, left = right multiplication by `X` = the shift `T`, B1/B2 coordinate-wise | `(q,t,n) = (4,1,1), (4,1,2), (4,1,3), (9,1,2), (4,2,2)` |
| C | Lemma 5.6a(1)–(5); the Remark 5.6 witness; Lemma 5.6b(1) for arbitrary subsets; Lemma 5.6b(2) for every enumerated left ideal and for randomly generated left submodules; non-vacuity; Remark 5.6c; `σ_k(C^{⊥_s}) = (σ_k C)^{⊥_s}` (Lemma 6.11); Corollary 6.4 and `dim C + dim C^{⊥_s} = 4tn` at `n ≥ 2` | `q = 4` (`t = 1`, `n = 1,2,3`), `q = 9` (`n = 1,2`), `q = 8` (`n = 1,2`), `q = 4, t = 2` (`n = 1,2`) |

Highlights:

* Part C also verifies the linear-algebra encoding of both orthogonals against a
  **brute-force** enumeration at `q = 4, t = 1, n = 1` (all `256` ambient vectors), so the
  semilinear solve of `^{⊥_s}C` (in the variables `σ_s(y_j)`) is not taken on trust.
* Non-vacuity of the left-module test: the cyclic code generated by `E_11` in coordinate 0
  is a right module and **not** a left module (`dim = 4` at `n = 1`, `6` at `n = 3`,
  `q = 4`).
* Cyclic-code counts obtained by the Morita/`B`-submodule enumeration — an independent
  cross-check of Convention 5.8 (T-018): `(q,t,n) = (4,1,1) → 7 = q+3`;
  `(4,1,3) → 343 = (q+3)³` (`X³−1` splits into three distinct linear factors over `F_4`,
  since `3 ∣ q−1`); `(9,1,1) → 12 = q+3`; `(9,1,2) → 144 = (q+3)²` (`X²−1 = (X∓1)`,
  squarefree in characteristic `3`); and, where the **squarefree hypothesis fails**,
  `(4,1,2) → 33` (formula would give `49`) and `(8,1,2) → 93` (formula would give `121`).
  The last two are new confirmations that the hypothesis of Convention 5.8 is essential.
* Enumeration is exhaustive over the `B`-submodule lattice and is skipped, with a note in
  the log, when `dim_{F_q} B² > 6` or `|B²| > 20 000` (i.e. for `q = 9, n = 3` and
  `q = 4, t = 2, n = 2`).

---

## 6. The validated pairing (blueprint Phase-1 deliverable 5)

### 6.1 Definition and the U5 decision

**Definition 6.1.** `B_s(x,y) := Σ_{e=0}^{n−1} θ_s(x_e) y_e ∈ R`, and
`b_s := Λ ∘ B_s : R^n × R^n → F_q` with `Λ = λ ∘ tr`.

**Decision U5 (recorded).** **Both** pairings are used, with `B_s` (the `R`-valued one) as
the *definition* of `C^{⊥_s}` — it is the one that is right-`R`-linear and therefore
produces right modules — and `b_s` (the `F_q`-valued one) as the *computational and
quantum-facing* form. Lemma 6.7 shows they define the **same** orthogonal, so nothing
depends on the choice; `b_s` is used whenever an `F_p`-bilinear form is needed (e.g. the
commutation form in Phase 6).

### 6.2 Sesquilinearity

**Lemma 6.2.** (i) `B_s(x, y·a) = B_s(x,y)·a` (right-`R`-linear in `y`);
(ii) `B_s(x·a, y) = θ_s(a)·B_s(x,y)` (`θ_s`-semilinear in `x`);
(iii) `b_s` is `σ_s`-**sesquilinear** over `F_q` (with `c ∈ F_q` acting as the scalar
matrix `cI ∈ Z(R)`): `b_s(cx, y) = σ_s(c)·b_s(x,y)` and `b_s(x, cy) = c·b_s(x,y)`.
Consequently `b_s` is `F_p`-**bilinear** (`σ_s` fixes `F_p` pointwise), and it is
`F_q`-bilinear exactly in the trivial-Galois case `σ_s = id`, i.e. `r ∣ s`.

*Proof.* (i) `Σ θ_s(x_e)(y_ea) = (Σ θ_s(x_e)y_e)a`. (ii) `Σ θ_s(x_ea)y_e =
Σ θ_s(a)θ_s(x_e)y_e = θ_s(a)Σ θ_s(x_e)y_e`. (iii) follows with `a = cI`, using
`θ_s(cI) = σ_s(c)I` and `Λ(θ_s(a)M) = σ_s(Λ(M))` for `a = cI`. ∎

### 6.3 The key identity

**Lemma 6.3.** `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)` for all `x,y`. Consequently
`B_s(x,y) = 0 ⟺ B_s(y, σ_{2s}x) = 0`.

*Proof.* `θ_s(B_s(x,y)) = Σ_e θ_s(θ_s(x_e)y_e) = Σ_e θ_s(y_e)θ_s(θ_s(x_e)) =
Σ_e θ_s(y_e)σ_{2s}(x_e) = B_s(y, σ_{2s}x)`, using Lemma 4.4. Since `θ_s` is a bijection,
the vanishing statement follows. ∎

### 6.4 The dual is a right module, and cyclicity

**Corollary 6.4.** If `C` is a right `R`-module, so is `C^{⊥_s}`; if `C` is a cyclic code,
so is `C^{⊥_s}`.

*Proof.* Lemma 6.2(i) gives the first part. For the second: `B_s(x, Ty) =
Σ_e θ_s(x_e)y_{e−1} = Σ_e θ_s(x_{e+1})y_e = B_s(T^{−1}x, y)`, so `y ∈ C^{⊥_s}` and
`T^{−1}x ∈ C` (as `C` is `T`-stable) give `B_s(x,Ty) = 0`, i.e. `Ty ∈ C^{⊥_s}`. ∎

### 6.5 Non-degeneracy and the size formula

**Lemma 6.5 (ideal-catching for `Λ`, both sides).** Let `0 ≠ X ∈ R`, let `x_{ij} ≠ 0` be an
entry of minimal valuation `k = v(x_{ij})`, and put `Y := u^{t−1−k}E_{ji}`. Then

$$\Lambda(YX) = \Lambda(XY) = c_k \neq 0 ,$$

where `c_k` is the leading (lowest-order nonzero) coefficient of `x_{ij}`. Consequently
every nonzero **left** ideal and every nonzero **right** ideal of `R` contains an element
`Z` with `Λ(Z) ≠ 0`.

*Proof.* Write `c := u^{t−1−k}` and `Y := cE_{ji}`, so that `Y_{ml'} = c\,[m=j][l'=i]`.
Right multiple: `(XY)_{ll'} = Σ_m X_{lm}Y_{ml'} = X_{lj}\,c\,[l'=i]`; its diagonal entries
(`l' = l`) survive only for `l = i`, giving `tr(XY) = X_{ij}c`.
Left multiple: `(YX)_{ll'} = Σ_m Y_{lm}X_{ml'} = c\,[l=j]\,X_{il'}`; its diagonal entries
survive only for `l = l' = j`, giving `tr(YX) = X_{ij}c` as well (as it must, since
`tr(YX) = tr(XY)`). Finally `X_{ij}c = (c_ku^k + \dots)u^{t−1−k} = c_ku^{t−1}`, because every
higher term carries `u^{≥t} = 0`; hence `Λ(XY) = Λ(YX) = λ(c_ku^{t−1}) = c_k ≠ 0`. Since
`XY` lies in the right ideal generated by `X` and `YX` in the left ideal generated by `X`,
both ideals contain an element on which `Λ` is nonzero. ∎

**Theorem 6.6 (non-degeneracy and size formula).** The form `b_s` is additive in both
slots, `F_p`-bilinear, right-`F_q`-linear and left-`σ_s`-semilinear, and its right radical
is `{0}`. Consequently, for every right `R_n`-submodule `C`,

$$\dim_{\mathbb F_q} C + \dim_{\mathbb F_q} C^{\perp_s} = N = 4tn,\qquad
|C|\cdot|C^{\perp_s}| = |R|^n .$$

*Proof.* Additivity and the two homogeneities are Lemma 6.2(iii); `F_p`-bilinearity
follows because `σ_s` fixes `F_p`. Right radical: let `0 ≠ y ∈ R^n` and pick `e` with
`y_e ≠ 0`. Choose an entry `(y_e)_{ij} ≠ 0` of minimal valuation `k`, put
`a := u^{t−1−k}E_{ji}` and `x_e := θ_s^{−1}(a) = σ_{−s}(a^{\mathsf T})`, `x_{e'} := 0`
for `e' ≠ e`. Then `θ_s(x_e) = a`, so

$$b_s(x,y) = \Lambda\big(\theta_s(x_e)y_e\big) = \Lambda(a\,y_e) \neq 0$$

by Lemma 6.5 (left-ideal case, applied to the left ideal `R y_e`). Hence the right radical
is trivial. For the dimension count, view `V = R^n` as an `F_p`-space; the map
`ψ : V → V^*`, `y ↦ (x ↦ b_s(x,y))`, is `F_p`-linear and injective, hence bijective, and
the restriction map `V^* → C^*` is surjective, so `φ : V → C^*`, `y ↦ b_s(·,y)|_C`, is
surjective with kernel `C^{⊥_s}`. Therefore `dim_{F_p} C^{⊥_s} = dim_{F_p} V − dim_{F_p} C`,
and dividing by `[F_q:F_p] = r` gives the `F_q`-statement; the cardinality statement
follows from `|C| = q^{\dim_{F_q} C}`. ∎

### 6.6 Equality of the two orthogonals (Phase-0 item U5, proved)

**Lemma 6.7.** For every right `R_n`-submodule `C`,
`{y : B_s(C,y) = 0} = {y : b_s(C,y) = 0}`; i.e. the `R`-valued and `F_q`-valued pairings
define the same dual.

*Proof.* `⊆` is clear (`B_s = 0 ⇒ Λ(B_s) = 0`). For `⊇`: the left-hand side has dimension
`N − dim C` by Theorem 6.6, and the right-hand side is the orthogonal of `C` with respect
to the form `b_s` of Theorem 6.6, hence has the same dimension
`N − dim C`. Containment plus equal (finite) dimension gives equality. ∎

### 6.7 Double dual, reflexivity, hulls

**Theorem 6.8.** For every right `R_n`-submodule `C`: `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`.

*Proof.* Inclusion: let `c ∈ C`, `y ∈ C^{⊥_s}`. Then `B_s(c,y) = 0`, so by Lemma 6.3,
`B_s(y, σ_{2s}c) = 0`; hence `σ_{2s}(C) ⊆ (C^{⊥_s})^{⊥_s}`. Equality: both sides have
dimension `dim C` (`σ_{2s}` is a bijection and `F_p`-linear; the double dual has dimension
`N − (N − dim C)`). ∎

**Corollary 6.9 (reflexivity).** `C ↦ C^{⊥_s}` is reflexive on right `R_n`-submodules
(i.e. `C^{⊥_s⊥_s} = C` for all `C`) ⟺ `r ∣ 2s`. For `m = 1` it is always reflexive (all
ideals of `A_t` are `σ`-invariant), so the hypothesis `m ≥ 2` is essential; here `m = 2`.

*Proof.* By Theorem 6.8, reflexivity for all `C` ⟺ `σ_{2s}(C) = C` for all `C` ⟺
`σ_{2s} = id` ⟺ `r ∣ 2s` (take `W = A_t(e_1 + ae_2) ⊆ A_t²` under Proposition 2.6:
`σ_{2s}(W) = A_t(e_1 + σ_{2s}(a)e_2) ≠ W` whenever `σ_{2s}(a) ≠ a`). ∎

**Lemma 6.10 (hull).** `Hull_s(C) = C ∩ C^{⊥_s}` is a right `R_n`-submodule, i.e. a cyclic
code; and `Hull_s(σ_kC) = σ_k Hull_s(C)` for all `k`.

*Proof.* Intersection of two right `R_n`-submodules. The equivariance follows from the
isometry of Lemma 6.11 below. ∎

**Lemma 6.11 (isometry).** For all `k`: `B_s(σ_kx, σ_ky) = σ_k(B_s(x,y))`; Hamming weight
is `σ_k`-invariant; `σ_k(C^{⊥_s}) = (σ_kC)^{⊥_s}`; `Hull_s(σ_kC) = σ_kHull_s(C)`.

*Proof.* `θ_s(σ_kX) = σ_s(σ_k(X^T)) = σ_{s+k}(X^T) = σ_k(θ_s(X))`, hence
`B_s(σ_kx,σ_ky) = Σ σ_k(θ_s(x_e))σ_k(y_e) = σ_k(B_s(x,y))`. Weight is preserved because
`σ_k` is a bijection fixing `0`. The remaining statements follow by applying this to the
definitions. ∎

**Corollary 6.12 (parameter invariance in regime R3).** Even when `r ∤ 2s`, the code
`C^{⊥_s⊥_s} = σ_{2s}(C)` has the same cardinality, the same weight enumerator, the same
minimum distance and the same hull dimension as `C`.

### 6.8 Exit gate (blueprint)

The Phase-1 exit gate has two clauses:

1. *"Do not proceed if the Galois automorphism is trivial."* — `σ_s` is non-trivial ⟺
   `r ∤ s`, and we assume `r ≥ 2` and work with `s ≢ 0` (regimes R1/R3); for regime R1
   (`r` even, `s = r/2`) the Galois automorphism is non-trivial **and** `θ_s` is an
   involution. **Gate satisfied.**
2. *"…or the pairing cannot be made valid for the intended construction."* — `B_s` is
   non-degenerate, right-`R`-linear, makes the dual of a cyclic code cyclic, and satisfies
   the size formula and the double-dual formula, for **all** `m ≥ 1`, `t ≥ 1`, `n ≥ 1` and
   all `s` (§6.2–6.7). The symmetry/Hermitian properties needed for CSS/EA hold exactly
   when `r ∣ 2s` (§7). **Gate satisfied**, with the regime restriction recorded, not
   assumed away.

---

## 7. Regime-dependent statements (decision B3)

**Theorem 7.1 (regime-independent — hold for every `s`).** For every right `R_n`-submodule
`C`: (i) `C^{⊥_s}` is a cyclic code; (ii) `|C|·|C^{⊥_s}| = |R|^n`;
(iii) `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`; (iv) `Hull_s(C)` is a cyclic code;
(v) `σ_k`-equivariance and all consequences of Lemma 6.11; (vi) Corollary 6.12;
(vii) `^{⊥_s}C = (σ_{−2s}C)^{⊥_s}`.

**Theorem 7.2 (require `r ∣ 2s`, i.e. regimes R0–R2).** (i) `θ_s` is an involution and
`C ↦ C^{⊥_s}` is reflexive. (ii) `b_s(y,x) = σ_s(b_s(x,y))` — the form is
`σ_s`-**Hermitian**. (iii) `Tr_{F_q/F_p} ∘ b_s` is a **symmetric** `F_p`-bilinear form
(the trace is Frobenius-invariant), so the commutation matrix of a code is symmetric and
the standard stabilizer/CSS/EA machinery applies. (iv) Self-orthogonality
`C ⊆ C^{⊥_s}` can be tested on `i ≤ j`.

*Proof.* (ii): Lemma 6.3 with `σ_{2s} = id` gives `θ_s(B_s(x,y)) = B_s(y,x)`; applying
`Λ` and using `Λ(θ_sM) = σ_s(Λ(M))` yields `σ_s(b_s(x,y)) = b_s(y,x)`. (iii):
`Tr(b_s(y,x)) = Tr(σ_s(b_s(x,y))) = Tr(b_s(x,y))`. (iv) follows from (ii). ∎

**Theorem 7.3 (regime R3 — non-reflexive).** If `r ∤ 2s` then, in general,
`C^{⊥_s⊥_s} ≠ C` (e.g. `35` of `737` cyclic codes at `q = 8, n = 3` are reflexive),
`b_s` is **not** `σ_s`-Hermitian (`30/300` and `38/300` of random pairs at `q=8`), and
`Tr∘b_s` is **not** symmetric (`138/300`, `158/300`). Retained results: all of Theorem
7.1. **Not** available without extra hypotheses: the Hermitian/symmetric structure of
Theorem 7.2, hence the standard CSS/EA derivations.

**Theorem 7.4 (per-code rescue in R3).** Let `r ∤ 2s` and let `C` be `σ_{2s}`-invariant
(`σ_{2s}(C) = C`). Then `C^{⊥_s⊥_s} = C`, and all the conclusions of Theorem 7.2 hold
**for that code**. The `σ_{2s}`-invariant cyclic codes are exactly the codes obtained by
Galois descent from the fixed field of `σ_{2s}` (at `q=8, n=3`: `5 × 7 = 35` of `737`;
at `q=27, n=1`: `6` of `30`).

*Proof.* `C^{⊥⊥} = σ_{2s}(C) = C` by Theorem 6.8. The remaining statements are the
per-code versions of Theorem 7.2 (the proofs restrict to `x,y ∈ C` and use
`σ_{−2s}(C) = C`). The counts are verified in `decision_support_log.txt`. ∎

**Warning (B3.5).** Nothing above licenses the assumption that an arbitrary
non-reflexive code satisfies the requirements of a quantum construction. In regime R3 the
quantum sections may use only codes satisfying the proved hypothesis of Theorem 7.4, or a
derivation that avoids `C^{⊥⊥} = C` and the symmetry of the commutation form.

---

## 8. What Phase 1 does **not** claim

* No hull-dimension **formula** (only the distributions from Phase 0) — Phase 4.
* No Gray map, no metric/distance statements — Phase 5.
* No quantum construction — Phase 6.
* No claim that anti-automorphism duality is new (B2; see Wood 2010, Szabo–Wood 2017,
  NRS 2006).
* No restatement or correction of Alahmadi et al.'s Theorem 1 (B1).
* `q = 2` (`r = 1`) is never used as Galois evidence — enumerator validation only.

---

## 9. Computational corroboration

`04_COMPUTATION/ring_structure_checks.py` (log: `ring_structure_log.txt`) rebuilds
`F_q`, `A_t` and `R = M_2(A_t)` from scratch and re-derives every structural quantity
above **from the definitions** — units by exhibiting an inverse, `Jac` by the criterion
`1 − xy ∈ R^×`, ideals by closing under the relevant operations, `|Aut(A_t)|` by
enumerating `F_p`-algebra endomorphisms and testing bijectivity — never from the formula
being checked. Coverage:

| Section | Parameter sets `(q, t)` |
|---|---|
| A.1 `A_t` | `(4,1), (4,2), (4,3), (9,1), (8,1), (16,1)` |
| A.2 `R = M_2(A_t)` | `(4,1), (9,1), (8,1), (4,2)` |
| A.3 Morita | `(4,1), (9,1), (8,1), (4,2)` |
| B `σ_s`, `θ_s` | `(4,1), (9,1), (8,1), (27,1), (16,1), (4,2)` |
| C modules / pairing | `(4,1), (9,1), (8,1), (27,1), (16,1), (4,2)` |

**Result: 401 of 401 checks PASS.** Each is labelled `[EXH]` (exhaustive over the finite
object: all elements of the ring, all subspaces of the relevant space, all `s` mod `r`) or
`[SMP]` (uniformly seeded sample, with the sample size stated in the log). Highlights:

* `|Aut(A_t)|` = `2, 6, 24, 2, 3, 4` for the six parameter sets, matching
  `r` (`t = 1`) and `r(q−1)q^{t−2}` (`t ≥ 2`) exactly; the coefficient-Frobenius
  subgroup `{σ_s}` (which fixes `u`) has order `r` in each case — Convention 1.7.
* `|GL_2(A_t)|` = `180` (`q=4,t=1`), `5 760` (`q=9`), `3 528` (`q=8`),
  `46 080` (`q=4,t=2`), i.e. `q^{4(t−1)}(q²−1)(q²−q)`; every unit has a two-sided inverse.
* `Z(R) = {aI}`, `|Z(R)| = q^t`; `Jac(R) = uR` verified by the unit criterion;
  `R/uR ≅ M_2(F_q)` simple (every nonzero element generates the whole two-sided ideal);
  exactly `t+1` two-sided ideals.
* Right ideals (Morita, columns convention of Proposition 2.6): `7, 12, 11` at `t = 1`
  for `q = 4, 9, 8` (`= q+3`) and `33` at `q = 4, t = 2` (`= q²+3q+5`), with
  `dim_{F_q} I_W = 2 dim_{F_q} W`, injectivity, closure under sums, and every principal
  right ideal occurring — i.e. the enumerated family **is** the full lattice.
* `ord(σ_s) = r/gcd(r,s)` and `ord(θ_s) = 2r/gcd(r,2s)`: measured `[1,2] / [2,2]` at
  `q = 4`, `[1,3,3] / [2,6,6]` at `q = 8` and `q = 27`, `[1,4,2,4] / [2,4,2,4]` at
  `q = 16`; `θ_s` is never the identity (`θ_s(E_12) = E_21`).
* Involutive `s`: `{0,1}` at `q = 4`, `{0,2}` at `q = 16`, `{0}` at `q = 8` and `q = 27`
  — **Corollary 4.6 confirmed**: odd `r` admits no non-trivial reflexive `s`.
* Pairing: `b_s` non-degenerate (`rank Gram = dim R = 4t`), `|C|·|C^{⊥_s}| = |R|`,
  `^{⊥_s}C = (σ_{−2s}C)^{⊥_s}`, the two orthogonals coincide, and
  `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` on **every** right ideal enumerated (`7` at `q=4,t=1`;
  `12` at `q=9`; `11` at `q=8`; `30` at `q=27`; `19` at `q=16`; `33` at `q=4,t=2`), in
  both the reflexive regime (involution) and the non-reflexive one, where at `s = 1` the
  number of codes that are **not** `σ_{2s}`-invariant is `6/11` (`q=8`), `24/30`
  (`q=27`) and `12/19` (`q=16`) — direct confirmation of Theorem 6.8 and of the
  non-reflexivity of regime R3.
* Side flip (Proposition 5.9): with the plain matrix product the orthogonal of
  `E_11 R` is `{0}` (degenerate), that of `R E_11` is perfect, and the same left ideal
  degenerates when the code is moved to the other slot (Remark 5.9a); the entry-wise form
  is perfect on both at `n = 1` (Remark 5.9b).

A second, independent script `04_COMPUTATION/module_actions_checks.py` (log
`module_actions_log.txt`, **276 of 276 checks PASS**) covers §5.6, the left/right module
conventions: the column/row mixing formulas, the Morita dictionary in **both**
handednesses, centrality of `X` and `T` = the shift, the five pairing/action identities of
Lemma 5.6a, Lemma 5.6b (both parts, with a brute-force cross-check of the orthogonal
encoding at `q = 4, t = 1, n = 1`), Remark 5.6c, and the cyclic-code counts
`7 / 33 / 343 / 12 / 144 / 11 / 93 / 33` for `(q,t,n) = (4,1,1), (4,1,2), (4,1,3),
(9,1,1), (9,1,2), (8,1,1), (8,1,2), (4,2,1)`; see §5.6.5. It also produced the two new
non-squarefree data points (`33` at `q=4,n=2` and `93` at `q=8,n=2`, against the
squarefree predictions `49` and `121`) and the correction to Remark 5.6 recorded in
§5.6.4.
