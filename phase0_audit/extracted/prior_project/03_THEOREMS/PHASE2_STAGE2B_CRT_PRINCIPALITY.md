# Phase 2 — Stage 2B: CRT/Hensel decomposition and the global principality criterion

**Status of this document.** Stage 2B executes `PHASE2_PROPOSAL_v2.md` §4 (**P-2.4**,
CRT/Hensel with precise hypotheses) and §5.2 (**P-2.6**, the global principality
criterion), together with the parts of §3 needed to state them (L-2.4.1–L-2.4.6) and
the Galois-compatibility question of Task D. Everything outside those sections —
P-2.7/P-2.8 (duals and annihilators), the Galois hull, Gray maps, quantum
constructions, and C-2.1 (enumeration closed forms) — is **out of scope** and is not
attempted here.

Companion verification: `04_COMPUTATION/phase2_stage2b_crt_principality.py`, log
`04_COMPUTATION/phase2_stage2b_crt_log.txt` (**460 / 460 checks PASS**: 434 `[EXH]`,
26 `[SMP]`, seed `20261106`, two consecutive runs byte-identical, log SHA-256
`8db6fb5fd82bce710b792b74019e1e43b68b9232660215d55a559675b7ce0460`, 709 lines).

**Status labels used below.** `PROVED IN PHASE 1`, `PROVED IN PHASE 2 STAGE 1`,
`PROVED IN PHASE 2 STAGE 2A`, `PROVED IN PHASE 2 STAGE 2B`, `IMPORTED RESULT` (with the
source named), `PROPOSED / UNPROVED`, `CONJECTURE`, `COMPUTATIONALLY VERIFIED ONLY`,
`OPEN`. A computation never promotes a statement: every `PROVED` row below rests on the
argument written here.

---

## 0. Scope, conventions, and what is carried in

### 0.1 Standing conventions (unchanged from Phase 1, Stage 1 and Stage 2A)

* `q = p^r`, `A_t = F_q[u]/⟨u^t⟩`, `R = M_2(A_t)`, `X` a **central** variable,
  `R_n = R[X]/⟨X^n−1⟩`, `B = A_t[X]/⟨X^n−1⟩`.
* **Right-module convention:** right ideals of `R_n`; `B`-modules are **right** modules.
* **Morita column convention (Stage 2A §1):** `P = B^2` is the space of **columns**,
  `S = M_2(B) = End_B(P_B)` acts by `v ↦ Mv` (the usual matrix product), and
  `im M` is the `B`-span of the two **columns** of `M`.
* `ι : R^n → R_n` (Stage 1) and `R_n ≅ M_2(B)` (Stage 2A Lemma 1.3).
* `σ_k` is the coefficient Frobenius `σ_k(X)_{ij} = (X_{ij})^{p^k}`, extended to `R_n`
  coefficient-wise; it **fixes `u` and `X`** and is an automorphism (Phase 1, RGF Lemma
  4.2/A3; Stage 1 §6). `θ_s = σ_s ∘ (·)^T` (an **anti**-automorphism).

### 0.2 Results imported into Stage 2B

| Ref | Statement | Where proved | Status |
|---|---|---|---|
| **T-070** (Stage 2A) | `W ↦ I_W = {M : im M ⊆ W}` is a bijection from `B`-submodules of `B^2` onto right ideals of `S = M_2(B)`; inverse `I ↦ W(I) = Σ_{M∈I} im M`; lattice properties; `dim I_W = 2 dim W`, `|I_W| = |W|^2` | Stage 2A Thm 2.1 | `PROVED IN PHASE 2 STAGE 2A` (the dimension/cardinality part is `PROVED IN PHASE 1`, RGF Prop. 2.6) |
| **T-083** (Stage 2A) | `I_W` is principal `⟺ μ_B(W) ≤ 2` (`μ(0) = 0`, so `W = 0 ⇒ I_W = 0` is principal) | Stage 2A Thm 4.1 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-080** (Stage 2A) | `im[w_1∣w_2] = Bw_1 + Bw_2` | Stage 2A Lemma 3.6 | `PROVED IN PHASE 2 STAGE 2A` |
| **T-075** (Stage 2A) | `R_n ≅ M_2(B)` | Stage 2A Lemma 1.3 | `PROVED IN PHASE 2 STAGE 2A` |
| **E-011** | Chinese remainder theorem for pairwise comaximal ideals | Atiyah–MacDonald, Ch. 1 | `IMPORTED RESULT` |
| **E-012** | Hensel's lemma for lifting a factorisation into pairwise coprime monic factors over a complete local ring | Atiyah–MacDonald Ch. 10 / Eisenbud §7 | `IMPORTED RESULT` — **the reference is flagged "to be confirmed" in the register, so Stage 2B proves the instance it needs (Lemma 1.2) from scratch and does not rely on this import** |
| **E-014** | Nakayama: over a local ring `(B,m,k)`, elements generate `M` iff their images generate `M/mM`; hence `μ_B(M) = dim_k(M/mM)` | Atiyah–MacDonald Prop. 2.6, 2.8 | `IMPORTED RESULT` |
| **E-015** | Matrices over a chain ring admit a Smith normal form | McDonald, *Finite Rings with Identity* (1974) | `IMPORTED RESULT` — **explicitly "not a substitute for the proof L-2.6.4"; accordingly L-2.6.4 is proved here (§4.1) from first principles** |
| **C-2.1a/b** | `N(1,Q) = Q+3`, `N(2,Q) = Q^2+3Q+5` (submodules of `S^2` for a chain ring `S` with residue field of size `Q` and nilpotency `1`, `2`) | RGF §2 Cor. 2.7 (T-032) | `PROVED IN PHASE 1` |

**Proof obligation L-2.6.1** of the proposal ("every right ideal of `R_n` is `I_W` for a
unique `W`") is **already discharged in Stage 2A** as T-070 + T-075; it is not re-proved
here.

---

## 1. Task A — the CRT/Hensel decomposition (P-2.4)

Throughout, `n = p^v n'` with `gcd(n',p) = 1`, `v = v_p(n)`, `e := p^v`.

### 1.1 The squarefree part

**Lemma 1.1 (the squarefree part).** In `F_q[X]`: `X^n − 1 = (X^{n'} − 1)^{p^v}`, and
`X^{n'} − 1` is **squarefree**. Writing `X^{n'} − 1 = ∏_{j=1}^{J} f_j` with `f_j` distinct
monic irreducibles, `d_j := deg f_j`, the `d_j` are the sizes of the `q`-cyclotomic cosets
mod `n'`; in particular `J` and the multiset `{d_j}` depend only on `(q,n')`, **not** on `t`.

*Proof.* `X^n − 1 = (X^{n'})^{p^v} − 1 = (X^{n'} − 1)^{p^v}` in characteristic `p` (the
`p^v`-power is additive). The derivative of `X^{n'}−1` is `n' X^{n'−1}`, and `n' ≠ 0` in
`F_q` because `p ∤ n'`; `n'X^{n'−1}` is a non-zero monomial, coprime to `X^{n'}−1` (which
has non-zero constant term `−1`), so `X^{n'}−1` is squarefree. For the last claim: the
roots of `X^{n'}−1` in an algebraic closure are the `n'`-th roots of unity; the
`F_q`-irreducible factors are `∏_{i ∈ C}(X − ζ^i)` for `C` running over the orbits of
`i ↦ qi` on `Z/n'`, i.e. the `q`-cyclotomic cosets. ∎

### 1.2 Hensel lifting

**Lemma 1.2 (Hensel, proved from scratch).** Let `A` be a commutative ring with a
nilpotent ideal `(u)`, `u^t = 0`, and let `g ∈ A[X]` be monic. Suppose
`ḡ = ∏_{j=1}^{J} f̄_j` in `(A/(u))[X]` with the `f̄_j` monic and **pairwise coprime**.
Then there are **unique** monic `F_j ∈ A[X]` with `F_j ≡ f̄_j mod u` and `g = ∏_j F_j`
exactly.

*Proof.* Existence by induction on the `u`-adic level. Put `F_j^{(1)} := f̄_j` (viewed in
`A[X]` via the constant-term section of `A → A/(u)` — in our application `A = A_t` and
`A/(u) = F_q ⊆ A_t`, so the section is the inclusion of `F_q`). Assume
`F_j^{(k)}` monic with `F_j^{(k)} ≡ f̄_j mod u` and `g − ∏_j F_j^{(k)} ∈ u^k A[X]`
(true for `k = 1`). Write the coefficient of `u^k` of `g − ∏_j F_j^{(k)}` as `c ∈ F_q[X]`.
Seek `F_j^{(k+1)} = F_j^{(k)} + u^k h_j` with `h_j ∈ F_q[X]`, `deg h_j < d_j` (this keeps
`F_j^{(k+1)}` monic of degree `d_j`). Since `2k ≥ k+1`,

```
∏_j (F_j^{(k)} + u^k h_j) ≡ ∏_j F_j^{(k)} + u^k Σ_j h_j Ĝ_j   (mod u^{k+1}),
```

where `Ĝ_j := ∏_{i≠j} f̄_i` (only the reduction modulo `u` of `∏_{i≠j}F_i^{(k)}` matters,
and it is `Ĝ_j`). Hence the requirement is **`Σ_j h_j Ĝ_j = c`** in `F_q[X]`.

Consider the `F_q`-linear map `Φ : ⊕_j (F_q[X])_{<d_j} → (F_q[X])_{<D}`, `D = Σ d_j`,
`(h_j) ↦ Σ_j h_j Ĝ_j`. It is injective: reduce `Σ h_j Ĝ_j = 0` modulo `f̄_i`; every term
with `j ≠ i` contains the factor `f̄_i` and vanishes, leaving `h_i Ĝ_i ≡ 0 mod f̄_i`, and
`Ĝ_i` is invertible mod `f̄_i` (the `f̄_j` are pairwise coprime), so `f̄_i ∣ h_i`, whence
`h_i = 0` as `deg h_i < d_i`. Domain and codomain both have dimension `D`, so `Φ` is
**bijective** and a unique solution `(h_j)` exists. This completes the induction; after
`t−1` steps `g − ∏F_j ∈ u^t A[X] = 0`.

Uniqueness: at each level the correction `(h_j)` is unique by the injectivity of `Φ`, so
the lift is unique. ∎

**Remark 1.3 (the lifting is constructive and was implemented).** `Φ` is a `D × D`
`F_q`-matrix; `solve_K` in the companion script assembles it and Gaussian-eliminates.
A **non-vacuity test** (log: "non-vacuity — a genuinely non-trivial Hensel lift") runs the
routine on `g = X^2 + X + u ∈ F_2[u]/⟨u^2⟩[X]`, whose reduction `X(X+1)` is a coprime
factorisation: the routine returns `F_1 = X + u`, `F_2 = X + 1 + u`, and indeed
`(X+u)(X+1+u) = X^2 + X + u` there. So the lifting step is not a no-op by construction.

### 1.3 The Hensel lifts are the base-field factors themselves

**Theorem 1.4 (P-2.4(1), with an explicit identification).** In the situation of
Lemma 1.1 there are unique monic pairwise coprime `F_j ∈ A_t[X]` with `F_j ≡ f_j mod u`
and `X^{n'} − 1 = ∏_j F_j` in `A_t[X]`, and **they are `F_j = f_j`**.

*Proof.* Existence and uniqueness are Lemma 1.2 applied to `A = A_t`, `g = X^{n'}−1`
(monic, with reduction `∏ f_j`). Since `X^{n'}−1 ∈ F_q[X]` and `∏_j f_j = X^{n'}−1`
already holds **in** `F_q[X] ⊆ A_t[X]`, the family `(f_j)` is itself a family of monic
pairwise coprime lifts with the required reductions and product. By uniqueness,
`F_j = f_j`. ∎

**Consequence 1.5 (the components are explicit).** `B_j = A_t[X]/⟨f_j^{p^v}⟩` with
`f_j ∈ F_q[X]`, and the CRT map is **reduction modulo `f_j^{p^v}`** — no lifted
polynomials have to be found. This is a genuine structural statement (Hensel applies and
its unique solution is the original factor), not a vacuous one: it is precisely why the
decomposition is computable, and why the maximal ideal is `(u, f_j)` with `f_j` a
**base-field** polynomial (used in Lemma 1.8 and Theorem 2.3).

**Remark 1.6 (the two Hensel routes agree here, but they are logically distinct).** The
proposal warns (mandatory point 6) that the repeated factor `f_j^{p^v}` must never be
lifted directly. Lifting the factorisation `X^n−1 = ∏_j f_j^{p^v}` (whose factors are
pairwise coprime mod `u`) is legitimate and, by the same uniqueness argument, returns
`G_j = f_j^{p^v}`. The log verifies both routes and their agreement
("[EXH] … lifting the repeated factorisation gives `f_j^{p^v}` too"). The **squarefree-only
route is the one that yields the structural description** `m_j = (u, F_j)` and hence the
three-case table; the direct route produces the moduli but not the description of `m_j`.

### 1.4 CRT

**Theorem 1.7 (P-2.4(2); = L-2.4.2).** The ideals `⟨f_j^{p^v}⟩ ⊆ A_t[X]` are pairwise
comaximal, and

```
B = A_t[X]/⟨X^n−1⟩  ≅  ∏_{j=1}^{J} B_j ,    B_j := A_t[X]/⟨f_j^{p^v}⟩,
b  ↦  (b mod f_j^{p^v})_j .
```

*Proof.* Since `gcd(f_i, f_j) = 1` in `F_q[X]`, a Bézout identity `af_i + bf_j = 1` holds
**in `F_q[X]`** and hence in `A_t[X] ⊆` ... (the same identity, read in `A_t[X]`): so
`⟨f_i^{p^v}⟩ + ⟨f_j^{p^v}⟩ = A_t[X]`, i.e. the ideals are pairwise comaximal. Now apply
the Chinese remainder theorem for pairwise comaximal ideals (E-011) to
`⟨X^n−1⟩ = ⟨∏_j f_j^{p^v}⟩ = ∏_j ⟨f_j^{p^v}⟩`. The inverse map is
`(c_j) ↦ Σ_j e_j c̃_j` with `e_j` the Bézout idempotents
(`e_j ≡ 1 mod f_j^{p^v}`, `e_j ≡ 0 mod f_i^{p^v}`, `i ≠ j`), which the script computes by
the extended Euclidean algorithm **in `F_q[X]`** and verifies: `e_j^2 = e_j`,
`e_ie_j = 0`, `Σ e_j = 1`, and `e_j ↦ (0,…,1,…,0)` under the CRT map. ∎

### 1.5 The local components

**Lemma 1.8 (P-2.4(3); = L-2.4.3 + L-2.4.4).** `B_j = A_t[X]/⟨f_j^{p^v}⟩` is a **finite
local** ring with maximal ideal `m_j = (u, f_j)`, residue field
`K_j = B_j/m_j ≅ F_q[X]/⟨f_j⟩ = F_{q^{d_j}}`, `dim_{F_q} B_j = t·d_j·p^v` and
`|B_j| = q^{t d_j p^v}`. Moreover `m_j^{t+p^v−1} = 0`.

*Proof.* Let `ρ_j : B_j → F_q[X]/⟨f_j⟩` be "reduce the `A_t`-coefficients modulo `u`,
then reduce modulo `f_j`". This is a ring homomorphism: it is the composite of the
coefficient map `A_t → F_q` (a ring homomorphism) with reduction mod `f_j`, and it is
well defined on the quotient because `ρ_j(u) = 0` and `ρ_j(f_j) = 0` force
`ρ_j(f_j^{p^v}) = 0`. It is surjective (both steps are). Hence
`ker ρ_j = (u, f_j)/(f_j^{p^v}) =: m_j` is a maximal ideal and
`B_j/m_j ≅ F_q[X]/⟨f_j⟩`, which is a field because `f_j` is irreducible.

Any monomial `u^a f_j^b` with `a + b ≥ t + p^v − 1` has `a ≥ t` or `b ≥ p^v`, hence
vanishes; so `m_j^{t+p^v−1} = 0` and `m_j` is nilpotent. A nilpotent maximal ideal is the
nilradical, hence the **unique** maximal ideal: `B_j` is local, and its units are exactly
the complement of `m_j`.

Since `f_j^{p^v}` is monic of degree `d_j p^v`, reduction modulo it gives the normal form
`Σ_{a<t, b<d_j p^v} c_{ab} u^a X^b`, so `{u^aX^b}` is an `F_q`-basis and
`dim_{F_q} B_j = t d_j p^v`, `|B_j| = q^{t d_j p^v}`. ∎

**Consistency.** `Σ_j t d_j p^v = t p^v Σ_j d_j = t p^v n' = tn`, so
`∏_j |B_j| = q^{tn} = |B|` — verified on every parameter set.

### 1.6 Ideals and submodules under the decomposition (P-2.4(4), first half)

**Lemma 1.9 (module decomposition).** Let `e_1,…,e_J` be the CRT idempotents. For every
`B`-module `M` (in particular `M = B^2` or `M = B`), `M = ⊕_j e_j M`, and
`e_j M` is a `B_j`-module (`e_jB ≅ B_j` acts through the projection). Consequently

* ideals of `B` ↔ tuples `(J_1,…,J_J)` of ideals `J_j ⊆ B_j`;
* `B`-submodules `W ⊆ B^2` ↔ tuples `(W_1,…,W_J)` of `B_j`-submodules `W_j ⊆ B_j^2`,
  via `W_j = {w_j : w ∈ W}` (equivalently `W_j = e_jW` under `e_j B^2 ≅ B_j^2`);
* `dim_{F_q} W = Σ_j dim_{F_q} W_j`, `|W| = ∏_j |W_j|`.

*Proof.* The `e_j` are central (the ring is commutative), orthogonal and sum to `1`, so
`M = ⊕ e_j M` and each `e_jM` is a module over `e_jB ≅ B_j`. If `W ⊆ M` is a submodule
then `e_j W ⊆ W` (as `e_j ∈ B`), so `W = ⊕_j (W ∩ e_jM)` and `W ∩ e_jM = e_jW`. Both
directions of the correspondence are then immediate, and the dimension formula is
additivity of dimension over a direct sum. ∎

### 1.7 The three regimes (CASE-2.4) — proved

**Theorem 2.3 below** (`dim_{K_j}(m_j/m_j^2)`) and **Theorem 4.3** (chain ring `⟺ t = 1`
or `p ∤ n`) give the case table in the exact form the proposal demands:

| Case | Hypothesis | `B_j` | Chain ring? | Tools available |
|---|---|---|---|---|
| Squarefree | `p ∤ n` (`v = 0`) | `A_t[X]/⟨f_j⟩ ≅ K_j[u]/⟨u^t⟩` | **yes**, `m_j = (u)`, nilpotency `t` | Smith normal form (§4.1) |
| Repeated root, `t = 1` | `p ∣ n`, `t = 1` | `F_q[X]/⟨f_j^{p^v}⟩` | **yes**, `m_j = (f_j)`, nilpotency `p^v` | Smith normal form (§4.1) |
| **Wild** | `p ∣ n` **and** `t ≥ 2` | `A_t[X]/⟨f_j^{p^v}⟩`, `m_j = (u,f_j)` | **NO** | **none**: no SNF, no shape classification |

**Explicit warning (mandatory point 6, honoured).** In the wild case the components are
local **non-chain** rings. Nothing in §4 (SNF, shape classification, chain-ring
enumeration) is used there, and no `(Q^2+3Q+5)`-type count is claimed for a wild
component.

---

## 2. The invariant `dim_{K_j}(m_j/m_j^2)` (L-2.4.6) and the wild case

**Theorem 2.3 (L-2.4.6, proved; = L-2.6.6).** With `K_j = B_j/m_j`,

```
dim_{K_j}(m_j / m_j^2)  =  0   if t = 1 and p^v = 1      (B_j = K_j is a field)
                           1   if (t ≥ 2, p^v = 1) or (t = 1, p^v ≥ 2)
                           2   if t ≥ 2 and p^v ≥ 2       (the wild case).
```

Equivalently: `dim = 2 ⟺ (t ≥ 2 and p ∣ n)`; `dim ≤ 1 ⟺ (t = 1 or p ∤ n)`.

*Proof.* All computations are in `B_j = A_t[X]/⟨f_j^{p^v}⟩`; write `α` for the class of
`u` and `φ` for the class of `f_j`, so `m_j = (α, φ)`, `α^t = 0`, `φ^{p^v} = 0`.

*m_j as an `F_q`-space.* Since `f_j^{p^v}` is monic of degree `d_j p^v`, the monomials
`u^a X^b` (`a < t`, `b < d_j p^v`) are an `F_q`-basis of `B_j`. Reduction modulo `f_j`
identifies `K_j` with the `F_q`-span of `{X^b : b < d_j}` (the normal form of degree
`< d_j`), and `ρ_j(u^aX^b) = 0` unless `a = 0`. Hence
`m_j = ker ρ_j = ⟨u^aX^b : a ≥ 1⟩ ⊕ ⟨f_j X^b : 0 ≤ b < d_j(p^v−1)⟩` — more conveniently,
`m_j = (α) + (φ)` with `(α) = α B_j` and `(φ) = φ B_j`, and

```
dim_{F_q} B_j = t d_j p^v ,   dim_{F_q} (α) = (t−1) d_j p^v ,   dim_{F_q} (φ) = t d_j (p^v−1).
```

*The three cases.*
1. `t = 1`, `p^v = 1`: then `α = 0` (as `u^1 = 0` in `A_1 = F_q`) and `φ = 0`
   (`f_j^1 = 0` in the quotient), so `m_j = 0` and `dim = 0`; `B_j ≅ K_j`.
2. `t ≥ 2`, `p^v = 1`: `B_j = A_t[X]/⟨f_j⟩ ≅ (F_q[X]/⟨f_j⟩)[u]/⟨u^t⟩ = K_j[u]/⟨u^t⟩`
   (both sides are `F_q[u,X]/(u^t, f_j)`; here it is used that `f_j ∈ F_q[X]`,
   Consequence 1.5). Its maximal ideal is `(u)`, `m_j^2 = (u^2)`, and
   `m_j/m_j^2 ≅ K_j·ū` has `K_j`-dimension `1` (for `t = 2` too: `m_j^2 = 0` and
   `m_j ≅ K_j` as a `K_j`-space).
3. `t = 1`, `p^v ≥ 2`: `B_j = F_q[X]/⟨f_j^{p^v}⟩` is a chain ring with uniformizer `φ`;
   `m_j = (φ)`, `m_j^2 = (φ^2)`, and `(φ)/(φ^2) ≅ K_j·φ̄` has dimension `1`
   (`φ^{p^v−1} ≠ 0` because `deg f_j^{p^v−1} = d_j(p^v−1) < d_j p^v`).
4. `t ≥ 2`, `p^v ≥ 2`: here `dim_{F_q}(m_j/m_j^2) = 2 d_j`. Indeed

   ```
   dim m_j − dim m_j^2 = [t d_j p^v − d_j] − [t d_j p^v − d_j(1 + 1_{t≥2} + 1_{p^v≥2})]
   ```

   concretely: `m_j` is spanned over `F_q` by the monomials `u^aX^b` with `a ≥ 1` together
   with `f_j X^b`, `0 ≤ b < d_j(p^v−1)`, and a direct count from the normal form gives
   `dim_{F_q} m_j = t d_j p^v − d_j` and `dim_{F_q} m_j^2 = t d_j p^v − 3 d_j`, so
   `dim_{F_q}(m_j/m_j^2) = 2 d_j`. Since `m_j/m_j^2` is a `K_j`-vector space and
   `[K_j : F_q] = d_j`, `dim_{K_j}(m_j/m_j^2) = 2 d_j / d_j = 2`.

   (Equivalently and more conceptually: `m_j/m_j^2` is spanned over `K_j` by the classes
   of `u` and `f_j`, and they are `K_j`-linearly independent because
   `dim_{K_j}(m_j/m_j^2) = 2`, which is the count just given. The two classes are
   non-zero: `u ∉ m_j^2` and `f_j ∉ m_j^2`, by the same normal-form count.)

**Computational confirmation (falsification test CT-2).** For every parameter set in §5
the script computes `m_j` as `ker ρ_j` **and** as the ideal `(u, f_j)` (they agree),
computes `m_j^2` as an ideal product, and compares `dim_{K_j}(m_j/m_j^2)` with the
prediction: `0` at the field components of `(2,1,3)` and `(9,1,2)`; `1` at `(4,2,1)`,
`(4,1,2)`, `(8,1,2)`, and the three components of `(4,2,3)`; `2` at the wild rings
`(2,2,2)`, `(4,2,2)`, `(9,2,3)`. **No case deviates.** (Log, e.g.
"[EXH] (4,2,2), component 0: `dim_{K_j}(m_j/m_j^2)` = 2 … dim_Fq m = 3, dim_Fq m^2 = 1".)

**Corollary 2.4 (`m_j` is principal `⟺ dim ≤ 1`).** By Nakayama (E-014) applied to the
local ring `B_j` and the finite module `m_j`, `μ_{B_j}(m_j) = dim_{K_j}(m_j/m_j^2)`.
Hence `m_j` is principal iff `dim_{K_j}(m_j/m_j^2) ≤ 1`.

---

## 3. Chain rings, and the shape of submodules of the free module of rank 2

This section proves **L-2.6.4** in full. The register's E-015 records the Smith normal
form over a chain ring as prior art *and explicitly refuses to let it replace the proof*,
so the proof is given here.

**Definition 3.1.** A finite commutative ring `S` is a **chain ring** if its ideals are
totally ordered by inclusion.

**Lemma 3.2 (valuation).** Let `S` be a finite chain ring, `m = (π)` its maximal ideal
(principal by Corollary 2.4 once `dim ≤ 1`; here assumed), `e` the nilpotency index
(`π^e = 0`, `π^{e−1} ≠ 0`), `K = S/m`. Then every `x ∈ S` is `x = 0` or `x = π^a·(unit)`
for a unique `0 ≤ a < e`; put `v(0) := e`, `v(π^a u) := a`. For all `x, y ∈ S`:
`v(xy) ≥ v(x) + v(y)` (clipped at `e`), and **`x ∣ y ⟺ v(x) ≤ v(y)`**; in particular of
any two elements one divides the other.

*Proof.* For `x ≠ 0`, choose `a` maximal with `x ∈ m^a = (π^a)`: then `x = π^a y` with
`y ∉ m`, i.e. `y` a unit (`S` local). Uniqueness of `a` is clear from `π^e = 0` and
`π^{e-1} ≠ 0`. If `v(x) ≤ v(y)`, write `x = π^a u`, `y = π^b w`, `a ≤ b`, `u, w` units:
then `y = x·(π^{b−a} w u^{−1})`. The converse is immediate. ∎

**Theorem 3.3 (Smith normal form over a finite chain ring; L-2.6.4).** Let `S` be a finite
chain ring and `W ⊆ S^2` an `S`-submodule. Then `W ≅ π^aS ⊕ π^bS` for some
`0 ≤ a ≤ b ≤ e` (with `π^e S := 0`); in particular **`W` is generated by at most two
elements**, i.e. `μ_S(W) ≤ 2`.

*Proof.* `S` is finite, hence noetherian, so `W` is finitely generated; say
`W = im(A : S^k → S^2)` for some `A ∈ M_{2×k}(S)` (its columns generate `W`).

*Elimination.* If `A = 0`, take `a = b = e`. Otherwise choose an entry of **minimal
valuation**, say `A_{i_0 j_0}`, and move it to position `(1,1)` by row and column
permutations (these are multiplication by invertible permutation matrices). Write
`x := A_{11}`.

*Clearing the first row.* For every `j`, `v(A_{1j}) ≥ v(x)`, so by Lemma 3.2
`A_{1j} = x c_j` for some `c_j`. Subtracting `c_j`·(column 1) from column `j` (right
multiplication by an invertible unipotent matrix) makes the first row `(x, 0, …, 0)`.
Note `c_1 = 1`, so column 1 is untouched.

*Clearing the first column.* For `i ≥ 2`, `v(A_{i1}) ≥ v(x)` (minimality was among **all**
entries of the original `A`), so `A_{i1} = x d_i`; subtracting `d_i`·(row 1) from row `i`
(left multiplication by an invertible unipotent matrix) makes the first column
`(x, 0)^T` and leaves the first row unchanged.

*Divisibility of the rest.* Every remaining entry is of the form `A_{ij} − d_iA_{1j}`
with `v(A_{ij}) ≥ v(x)` and `v(d_iA_{1j}) ≥ v(d_i) + v(x) ≥ v(x)` after the row clearing
(the first-row entries used are the **updated** ones, `0` for `j ≥ 2`), so every entry of
the remaining `(1 × (k−1))` block `B` has valuation `≥ v(x) = a`, i.e. is divisible by
`x`.

*Induction.* Apply the same procedure to `B` (operations on rows `{2}` and columns
`{2,…,k}` only, embedded as block-diagonal invertibles, so they do not disturb the first
row or column). `B` is `1 × (k−1)`, so one pass diagonalises it to `(y, 0, …, 0)` with
`v(y) ≥ a`. Writing `x = π^a u`, `y = π^b w` with `a ≤ b ≤ e` and multiplying by units
(absorbed into the invertible matrices) gives `U A V = diag(π^a, π^b)` (padded with zero
columns; `b = e` means the second diagonal entry is `0`).

*Conclusion.* Column operations do not change the image, and `U` carries it to
`U·im(D)`: so `W ≅ im(D) = π^aS ⊕ π^bS ⊆ S^2` as `S`-modules. The two elements
`U^{−1}(π^a, 0)^T` and `U^{−1}(0, π^b)^T` generate `W`, whence `μ_S(W) ≤ 2`. ∎

**Remark 3.4 (conventions).** `S^2` is a **right** `S`-module of columns; `A` acts by
`v ↦ Av`; row operations are left multiplication, column operations right multiplication.
`S` is commutative here (it is a `B_j`), so no side issue arises; for a non-commutative
ring the argument would need the right-sided form, which is why it is **not** applied in
the wild case (where in any case `B_j` is not a chain ring and the lemma is false).

**Remark 3.5 (what is *not* claimed).** Theorem 3.3 gives `μ ≤ 2` and the existence of a
Smith form. It does **not** count the submodules of a given shape: that is C-2.1d/e,
which is a `CONJECTURE` and is **out of scope**. Only C-2.1a/b (`PROVED IN PHASE 1`) are
used, and only as a cross-check on a count (§5, `(8,1,2)`).

**Theorem 3.6 (L-2.6.3: chain ⟺ `t = 1` or `p ∤ n`).** `B_j` is a chain ring
`⟺ t = 1` or `p ∤ n`.

*Proof.* `(⇐)` If `p ∤ n` then `e = 1` and `B_j ≅ K_j[u]/⟨u^t⟩` (Theorem 2.3, case 2);
its ideals are `(u^a)`, `0 ≤ a ≤ t`, totally ordered. If `t = 1` then
`B_j = F_q[X]/⟨f_j^{p^v}⟩`, a chain ring with uniformizer `f_j` (case 3).

`(⇒)` Suppose `t ≥ 2` and `p ∣ n`. By Theorem 2.3, `dim_{K_j}(m_j/m_j^2) = 2`, so by
Corollary 2.4 `m_j` is **not** principal. A finite local ring whose maximal ideal is not
principal is not a chain ring: if the ideals were totally ordered, then taking `x ∈ m_j`
of minimal `a` with `x ∉ m_j^2`… more directly, in a chain ring `S` with maximal ideal
`m`, Lemma 3.2's first part applies with any generator `π` of `m`, so `m` must be
principal. Precisely: if `S` is a chain ring, pick `x ∈ m \ m^2` (possible since `m ≠ m^2`
when `m ≠ 0`); then for each `y ∈ m`, either `x ∈ (y)` or `y ∈ (x)`; the first would give
`y ∣ x` and, as `y ∈ m`, force `x ∈ m^2` (for `y ∈ m \ m^2` we get `x = yz` with `z` a
unit by Lemma 3.2, so `(x) = (y)`; and for `y ∈ m^2` we get `x ∈ m^2`, excluded). Hence
`y ∈ (x)` for all `y ∈ m`, i.e. `m = (x)` is principal — contradiction. ∎

---

## 4. Task B — the global principality criterion (P-2.6)

Recall the statement under investigation (`PHASE2_PROPOSAL_v2.md` §5.2):

```
Every right ideal of R_n is principal   ⟺   p ∤ n   or   t = 1 .
```

### 4.1 The two directions

**Theorem 4.1 (P-2.6, `⇐`).** If `p ∤ n` or `t = 1`, then **every** right ideal of `R_n`
is principal.

*Proof.*
1. `R_n ≅ M_2(B)` (Stage 2A Lemma 1.3, T-075), so it suffices to treat the right ideals
   of `S = M_2(B)`.
2. Let `I` be a right ideal. By the Morita correspondence (Stage 2A Thm 2.1, T-070),
   `I = I_W` for the unique `W = W(I) ⊆ B^2`.
3. By the CRT (Theorem 1.7) and Lemma 1.9, `W ↔ (W_1,…,W_J)` with `W_j ⊆ B_j^2`.
4. By Theorem 3.6, each `B_j` is a chain ring (this is where `p ∤ n` or `t = 1` is used:
   it is exactly the hypothesis of Theorem 3.6).
5. By Theorem 3.3, `μ_{B_j}(W_j) ≤ 2` for every `j`.
6. By Lemma 4.2 below (L-2.4.5/L-2.6.5), `μ_B(W) = max_j μ_{B_j}(W_j) ≤ 2`.
7. By the individual criterion (Stage 2A Thm 4.1, T-083), `I_W` is principal. ∎

**Lemma 4.2 (L-2.4.5 / L-2.6.5, proved).** With the notation of Lemma 1.9,
`μ_B(W) = max_j μ_{B_j}(W_j)`; and if `B_j` is local, `μ_{B_j}(W_j) = dim_{K_j}(W_j/m_jW_j)`
(Nakayama, E-014).

*Proof.* `(≥)` If `w^{(1)},…,w^{(k)}` generate `W` over `B`, then their `j`-th
components generate `W_j` over `B_j` (the projection `B → B_j` is surjective and
`e_j w^{(i)}` are the components), so `μ_{B_j}(W_j) ≤ μ_B(W)` for each `j`.

`(≤)` Let `μ := max_j μ_{B_j}(W_j)` and, for each `j`, let `g^{(j)}_1,…,g^{(j)}_μ` generate
`W_j` (pad with zeros if `μ_{B_j}(W_j) < μ`). For `s = 1,…,μ` let `w^{(s)} ∈ W` be the
element whose `j`-th component is `g^{(j)}_s` for every `j` (it exists and lies in `W` by
Lemma 1.9). Then `w^{(1)},…,w^{(μ)}` generate `W`: indeed the `B`-submodule they generate
has `j`-th component containing all the `g^{(j)}_s`, hence equal to `W_j`, for every `j`,
so it equals `W`. Hence `μ_B(W) ≤ μ`.

The Nakayama formula is E-014 applied to the finite module `W_j` over the local ring
`B_j`. ∎

**Theorem 4.3 (P-2.6, `⇒`).** If `p ∣ n` and `t ≥ 2`, then **not** every right ideal of
`R_n` is principal: explicitly, for any index `j_0`, the right ideal `I_W` with

```
W = m_{j_0} ⊕ m_{j_0}   (in the j_0-th component; 0 in the others)
```

satisfies `μ_B(W) = 4 > 2` and `I_W = M_2(m_{j_0})` is **not principal** (and
`μ_{M_2(B)}(I_W) = 2`).

*Proof.* (`J ≥ 1` always, since `X^{n'}−1` has degree `n' ≥ 1`.)
1. By Theorem 2.3 (wild case), `dim_{K_{j_0}}(m_{j_0}/m_{j_0}^2) = 2`.
2. `m_{j_0}W = m_{j_0}^2 ⊕ m_{j_0}^2`, so
   `W/m_{j_0}W = (m/m^2) ⊕ (m/m^2)` and
   `dim_{K}(W/mW) = 2·dim_K(m/m^2) = 4`; by Nakayama (E-014), `μ_{B_{j_0}}(W) = 4`.
   By Lemma 4.2, `μ_B(W) = max(4, 0, …, 0) = 4`.
3. By the individual criterion (T-083), `I_W` is principal iff `μ_B(W) ≤ 2`; since
   `μ_B(W) = 4`, `I_W` is **not** principal.
4. `I_W = {M : both columns lie in W} = M_2(m_{j_0})` (a matrix has both columns in
   `m ⊕ m` iff all four entries lie in `m`), and by the generator-number identity of
   Stage 2A (Thm 3.1, T-081) `μ_{M_2(B)}(I_W) = ⌈μ_B(W)/2⌉ = 2`. ∎

**Corollary 4.4 (P-2.6, the global criterion — PROVED).**

```
Every right ideal of R_n is principal   ⟺   p ∤ n   or   t = 1 .
```

*Proof.* Theorems 4.1 and 4.3, and the fact that `(p ∣ n and t ≥ 2)` is the negation of
`(p ∤ n or t = 1)`. ∎

**Corollary 4.5 (what the criterion says in each regime).**

| Regime | `B_j` | All right ideals principal? |
|---|---|---|
| `p ∤ n`, `t = 1` | `K_j` (a field) | **yes** |
| `p ∤ n`, `t ≥ 2` | `K_j[u]/⟨u^t⟩` (chain) | **yes** |
| `p ∣ n`, `t = 1` | `F_q[X]/⟨f_j^{p^v}⟩` (chain) | **yes** |
| `p ∣ n`, `t ≥ 2` | `A_t[X]/⟨f_j^{p^v}⟩` (local, **not** chain) | **no** — `M_2(m_j)` is a counterexample |

**No counterexample to the statement was found; the statement is true as proposed.**
The `(4,2,2)` box of §5.2 ("predicted counterexample") is confirmed, and the `(9,2,3)`
case is confirmed as well (§5.3). Registers: **O-2.1 is discharged**; **T-021 is
superseded** (it asserted principality only under `t = 1` **and** `p ∤ n`; the correct
hypothesis is the disjunction).

### 4.2 Where each hypothesis is used

| Step | Uses |
|---|---|
| `R_n ≅ M_2(B)` | centrality of `X` (Stage 1) |
| Morita bijection onto right ideals | **nothing** beyond `B` unital (Stage 2A) |
| CRT decomposition | Hensel (Lemma 1.2) + comaximality + E-011 |
| `B_j` local, `m_j = (u,f_j)` | `f_j` irreducible over `F_q`, `u^t = 0` |
| `μ_{B_j}(W_j) ≤ 2` in the chain case | **chain ring**, hence SNF (Theorem 3.3) |
| `μ_B = max_j μ_{B_j}` | CRT idempotents |
| `I_W` principal `⟺ μ_B ≤ 2` | Stage 2A (L-2.3a/b/c, P-2.5(b)) |
| `μ_B(m⊕m) = 4` in the wild case | Nakayama + `dim_K(m/m²) = 2` |

**Nothing above uses a uniform bound `μ_B(W) ≤ 4`** (that is the withdrawn v1 claim, now
**O-2.2**, still `OPEN`): Theorem 4.1 needs only `μ ≤ 2`, which is proved.

---

## 5. Task C — independent computational verification

### 5.1 The script

`04_COMPUTATION/phase2_stage2b_crt_principality.py` (2006 lines; imports only `Field`, `Local`, `rref`, `nullspace_basis` from the Phase-1 library).
Everything else — polynomial arithmetic, factorisation, cyclotomic cosets, Hensel
lifting, the quotient rings `A_t[X]/⟨h⟩`, the CRT map and its Bézout idempotents, the
local invariants, `M_2` over a quotient ring, the ideal and submodule routines, `μ`, and
the principality certificates — **is written from scratch here**, independently of the
Stage-2A script (which used a different representation of `B` and a different `μ`
machinery). In particular:

* **factorisation** is by trial division over `F_q` with an irreducibility test, and is
  **cross-checked against the `q`-cyclotomic cosets** (an entirely different route:
  `#factors = #cosets`, `{d_j} = {coset sizes}`, `Σ d_j = n'`);
* **Hensel** is by the linear-algebra lifting of Lemma 1.2, with a non-vacuity test;
* **`μ`** is computed by (1) a lattice BFS over sums of cyclic submodules, (2) a
  brute-force scan over `k`-tuples, (3) Nakayama on the components, and (4) — for the
  principality question — an exhaustive scan for a single generator;
* **principality** is certified by exhibiting `x = [w_1∣w_2]` and checking
  `|x·M_2(B)| = |I_W| = |W|^2` (an equality of sizes together with `x ∈ I_W` **proves**
  `xS = I_W`); non-principality is certified by an exhaustive `x`-scan over `I_W` when
  feasible, and by the dimension bound below.

**The right ideal `xS` is always computed as `span_{F_q}{xN : N ∈ basis of M_2(B)}`**
(direct multiplication), never from `im x`, so that L-2.3a is tested, not assumed.

### 5.2 Negative controls (a wrong convention must FAIL)

| # | Control | Result |
|---|---|---|
| neg-1 | use the reduced modulus `⟨f_j⟩` instead of `⟨f_j^{p^v}⟩` when `p ∣ n` | `X^{n'}−1 ≠ 0` in `B` but maps to `0`: the reduced map is **not** injective (`PASS`) |
| neg-2 | read `W` as a condition on the **rows**: `{M : rows of M ⊆ W}` | **not** a right ideal — a counterexample is found by exhaustive search over `M_2(F_2)` (`PASS`) |
| neg-3 | `{M : im M ⊇ W}` (superset instead of subset) | **not** a right ideal; `0` is not even in the set (`PASS`) |
| neg-4 | the naive claim "`σ_1` fixes every CRT component" | **false**: at `(4,2,3)` the permutation is `(0,2,1)` (`PASS`) |
| neg-5 | non-vacuity of "all principal" in a chain-ring case | at `(4,2,1)`: 33 submodules, `max μ = 2`, so the claim is not vacuous (`PASS`) |

**A convention bug was caught by this discipline during development:** an early version
built `I_W` by placing the basis vectors of `W` in the **rows** of the matrix. All
dimension and cardinality checks still passed (the row version has the same `F_q`
dimension `2 dim W`), and only the membership test `x ∈ I_W` exposed it. This is
recorded because it is exactly the failure mode the proposal's mandatory point 6 warns
about.

### 5.3 Parameter cases

`v = v_p(n)`, `e = p^v`, `J` = number of irreducible factors of `X^{n'}−1`, `d_j` their
degrees.

| `(q,t,n)` | regime | `v`, `n'`, `e` | `J`, `d_j` | `#submodules of B^2` | all principal? | label |
|---|---|---|---|---|---|---|
| `(4,2,1)` | squarefree, `t ≥ 2` | 0, 1, 1 | 1, [1] | **33** | yes | `[EXH]` |
| `(4,1,2)` | repeated root, `t = 1` | 1, 1, 2 | 1, [1] | **33** | yes | `[EXH]` |
| `(2,1,3)` | squarefree, `t = 1` | 0, 3, 1 | 2, [1,2] | **35** = 5·7 | yes | `[EXH]` |
| `(9,1,2)` | squarefree, `t = 1` | 0, 2, 1 | 2, [1,1] | **144** = 12² | yes | `[EXH]` |
| `(8,1,2)` | repeated root, `t = 1` | 1, 1, 2 | 1, [1] | **93** | yes | `[EXH]` |
| `(4,2,3)` | squarefree, `t ≥ 2` | 0, 3, 1 | 3, [1,1,1] | **35 937** = 33³ | yes | `[EXH]` (built) + `[SMP]` certificates |
| `(2,2,2)` | **wild** | 1, 1, 2 | 1, [1] | targeted | **no** | `[EXH]` certificates |
| `(4,2,2)` | **wild** | 1, 1, 2 | 1, [1] | targeted | **no** | `[EXH]` certificates |
| `(9,2,3)` | **wild** | 1, 1, 3 | 1, [1] | targeted | **no** | `[EXH]` certificates |

Notes.

* The counts 33, 33, 35, 144 reproduce the Phase-1/Stage-2A values. **93** at `(8,1,2)`
  is `N(2,8) = 64 + 24 + 5` from C-2.1b (`PROVED IN PHASE 1`) — a new confirmation of a
  proved formula at `Q = 8`. **144 = 12²** and **35 = 5·7** are the product formula of
  Lemma 1.9 (P-2.4(4)) verified exhaustively over both lattices.
* **35 937 = 33³** at `(4,2,3)` is the register's `C-2.1g` prediction, which had the
  status `COMPUTATIONAL TEST PENDING`; it is now confirmed. The lattice of `B^2` at
  `(4,2,3)` (`|B^2| = 16.7·10^6`) cannot be enumerated by scanning elements, so the
  35 937 submodules were **built** from the three component lattices via the CRT, checked
  pairwise distinct, and cross-checked: 200 sampled closure checks, 399 sampled
  `μ`/principality certificates, and 180 random submodules of `B^2` all lying in the
  built list. The count is therefore `[EXH]` (all 33³ combinations were formed); the
  completeness beyond the built list is the theorem (Lemma 1.9), supported by the random
  sampling.
* `μ_B` distributions: `(4,2,1)` `[(0,1),(1,25),(2,7)]`; `(4,1,2)` the same;
  `(2,1,3)` `[(0,1),(1,23),(2,11)]`; `(9,1,2)` `[(0,1),(1,120),(2,23)]`;
  `(8,1,2)` `[(0,1),(1,81),(2,11)]`. In each case `μ_B ≤ 2`, as Theorem 4.1 predicts.
  (`(9,1,2)`: `144 − 11² = 23` submodules need two generators — the tuples
  `(W_1,W_2)` with `max(dim W_1, dim W_2) = 2`, an independent consistency check.)

### 5.4 The wild certificates

At each of `(2,2,2)`, `(4,2,2)`, `(9,2,3)` the script certifies, for `W = m_j ⊕ m_j`:

| `(q,t,n)` | `|m_j|` | `|W|` | `dim_{K_j}(W/m_jW)` | `dim_{F_q}(I_W/I_W J(S))` | principal? | `μ_S` |
|---|---|---|---|---|---|---|
| `(2,2,2)` | 8 | 64 | **4** (so `μ_B ≥ 4`) | **8** `> 4 d_j = 4` | **no** | 2 |
| `(4,2,2)` | 64 | 4096 | **4** | **8** `> 4` | **no** | 2 |
| `(9,2,3)` | 59 049 | 3 486 784 401 | **4** | **8** `> 4` | **no** | 2 |

*The `8 > 4` bound (the non-principality certificate).* `J(S) = M_2(J(B)) = M_2(m_j)`
(Stage 2A/E-003: two-sided ideals of `M_2(B)` are exactly `M_2(J)`; here `B` is local, so
`J(B) = m_j`). Hence `I_W J(S) = M_2(m_j)·M_2(m_j) = M_2(m_j^2)` and

```
dim_{F_q}(I_W / I_W J(S)) = 4 (dim_{F_q} m_j − dim_{F_q} m_j^2) = 4 d_j · dim_{K_j}(m_j/m_j^2) = 8 d_j.
```

For a **principal** right ideal `xS` the quotient `xS/xSJ(S)` is a cyclic right module
over the semisimple ring `S/J(S) = M_2(K_j)`; the cyclic right `M_2(K)`-modules are the
quotients of `M_2(K)` by its right ideals, which (Morita over the field `K`) have
`K`-dimension `4 − 2 dim_K(V) ≤ 4`, i.e. `F_q`-dimension `≤ 4 d_j`. Since
`8 d_j > 4 d_j`, `I_W` is not principal. (`d_j = 1` in all three rings, so the bound
reads `8 > 4`.)

At `(2,2,2)` this is backed by the **exhaustive** scan of all `4096` elements of
`I_W = M_2(m)` — none generates it — and in all three cases by two exhibited generators
that do generate it (`μ_S = 2`), matching `⌈μ_B/2⌉ = 2` (Stage 2A T-081).

### 5.5 Result and reproducibility

**460 checks, 460 PASS, 0 FAIL** — 434 `[EXH]`, 26 `[SMP]`, seed `20261106`.

Two consecutive runs (Python 3.11.2, ≈ 82 s each) produced **byte-identical** logs:
SHA-256 `8db6fb5fd82bce710b792b74019e1e43b68b9232660215d55a559675b7ce0460` (709 lines).
The log carries no timestamp and no elapsed time, so the comparison is exact.

**Regression.** The Stage-2A script was re-run unchanged in a scratch directory on the
same Phase-1 library and again produced its recorded log byte-for-byte
(`3ef38b17…23abe5`, 429/429 PASS), so the Stage-2A results are unaffected by Stage 2B.

---

## 6. Task D — Galois compatibility (`σ_k` on the CRT components)

Recall `σ_k(c u^a X^b) = c^{p^k} u^a X^b`: the Frobenius `p^k` on `F_q`-coefficients,
fixing `u` and `X`. It is a ring automorphism of `B` and of `R_n` (Phase 1, RGF Lemma
4.2; Stage 1 §6).

**Theorem 6.1 (`σ_k` permutes the components).** `σ_k(f_j) = f_{j'}` where `j'` indexes
the factor attached to the coset `p^k·C_j`; i.e. the induced permutation of the factors
(and hence of the components) is `C ↦ p^k C` on the `q`-cyclotomic cosets modulo `n'`.
Consequently `σ_k(e_j) = e_{j'}`, `σ_k(⟨f_j^{p^v}⟩) = ⟨f_{j'}^{p^v}⟩`,
`σ_k(m_j) = m_{j'}` (as preimages in `B`), and on residue fields `σ_k : K_j → K_{j'}` is
the Frobenius `x ↦ x^{p^k}`.

*Proof.* The roots of `f_j` are `{ζ^i : i ∈ C_j}`; `σ_k` raises coefficients to the
`p^k` power, so `σ_k(f_j)` is monic with root set `{ζ^{i p^k} : i ∈ C_j} =
{ζ^{i'} : i' ∈ p^k C_j}` (multiplication by `p^k` is a bijection of `Z/n'` because
`gcd(p,n') = 1`). Since `p^k C_j` is again a `q`-cyclotomic coset (`q·p^k C = p^k(qC) =
p^k C`), `σ_k(f_j)` is the irreducible factor `f_{j'}`. It is irreducible of the same
degree, so `d_{j'} = d_j`.

The rest follows by applying `σ_k` to the Bézout data: `σ_k(e_j)` is the idempotent
attached to `σ_k(f_j^{p^v}) = f_{j'}^{p^v}`, hence `σ_k(e_j) = e_{j'}`. Equivariance of
the CRT map is then immediate: `split(σ_k b)_{j'} = σ_k(split(b)_j)`. For the maximal
ideals, `m_j` is generated over `B_j` by `u` and `f_j`; `σ_k` fixes `u` and sends `f_j`
to `f_{j'}`, so it carries the preimage of `m_j` onto the preimage of `m_{j'}`. On
`B_j/m_j ≅ F_q[X]/⟨f_j⟩` the induced map is coefficient-wise Frobenius `p^k`. ∎

**Corollary 6.2 (stability).** The component `j` is `σ_k`-**stable** iff `p^k C_j = C_j`,
equivalently `σ_k(f_j) = f_j`, equivalently `f_j ∈ F_{p^{gcd(r,k)}}[X]`. In particular:
`σ_0 = id` fixes everything; `σ_k` depends only on `k mod r` (as `σ_r = id` on `F_q`);
and the component attached to `C = {0}` (the factor `X − 1`) is fixed by every `σ_k`.

**Corollary 6.3 (`μ` and principality are Galois-invariant).** For every `k` and every
`B`-submodule `W ⊆ B^2`, `σ_k(W)` is a `B`-submodule with `μ_B(σ_k W) = μ_B(W)`; hence
`I_W` is principal iff `I_{σ_k W}` is. In particular the property "every right ideal of
`R_n` is principal" is invariant under the Galois action — as it must be, since the
criterion of Corollary 4.4 (`p ∤ n` or `t = 1`) does not mention `s` or `k`.

*Proof.* `σ_k` is additive and `σ_k(cv) = σ_k(c)σ_k(v)`, so it carries `F_q`-subspaces to
`F_q`-subspaces; and `σ_k(W·b) = σ_k(W)σ_k(b)` with `σ_k(B) = B`, so it carries
submodules to submodules. A generating set is mapped to a generating set
(`σ_k` is an automorphism), whence `μ_B(σ_kW) = μ_B(W)`. Principality depends on `W`
only through `μ_B(W)` (Stage 2A T-083). ∎

**Computational verification (Task D).** For every parameter set and every `k` with
`0 ≤ k < r`, the script verifies: `σ_1` is a ring endomorphism of `B`; the computed
permutation of the factors **equals** the coset prediction `C ↦ p^kC`
(`[EXH]`); `σ_k(e_j) = e_{perm(j)}` (`[EXH]`); `split(σ_k b) = perm·split(b)` on 60
elements; `σ_k` maps the preimage of `m_j` onto that of `m_{perm(j)}` (`[EXH]`); and
`μ_B(σ_kW) = μ_B(W)` on the whole lattice of the small rings (`[EXH]`, e.g. 33
submodules × 2 automorphisms at `(4,2,1)`).

**Non-vacuity (neg-4).** The permutation is **not** always the identity: at `(4,2,3)`
(`q = 4`, `r = 2`, `n' = 3`) the cosets are `{0}, {1}, {2}` (since `4 ≡ 1 mod 3`) and
`σ_1` acts by `p = 2`, giving the permutation `(0,2,1)` — the two non-trivial components
are swapped while `X − 1` is fixed. So "the Galois action permutes the CRT components"
is a real phenomenon here, not a formality.

**Relation to the later Galois-dual and hull analysis (qualitative only; no dimensions
are computed, per the exclusions).** The hull analysis will pair a code with its
`θ_s`-dual. Three consequences of Theorem 6.1 will matter then, and are recorded here so
that they are not derived twice:

1. the CRT decomposition is **equivariant** for `σ_k` only up to the permutation
   `C ↦ p^kC`; a componentwise treatment of the dual must therefore track the orbits of
   that permutation, not individual components;
2. the components fixed by the relevant power of `σ` are exactly those with
   `p^kC = C`; on such a component `σ_k` is an automorphism of the local ring `B_j`, and
   it induces the Frobenius on the residue field `K_j` and fixes `u` and `f_j`;
3. since `μ` and principality are Galois-invariant (Corollary 6.3), the obstruction
   exhibited in Theorem 4.3 cannot be removed by passing to a Galois twist.

---

## 7. Traceability: theorems ↔ obligations ↔ tests ↔ residual risk

| Statement | Proposal obligation | Proof | Tests (log labels) | Residual risk |
|---|---|---|---|---|
| Lemma 1.1 (squarefree part, cosets) | P-2.4 notation | §1.1 | `[EXH]` `X^n−1 = (X^{n'}−1)^{p^v}`, squarefree, `∏f_j`, irreducibility, coprimality, `#cosets`, `{d_j}`, `Σd_j = n'` | none |
| Lemma 1.2 (Hensel) | **L-2.4.1** | §1.2 (self-contained) | `[EXH]` lifts are monic, reduce to `f_j`, product = `g`; uniqueness by exhaustive search over candidate tuples when feasible; non-vacuity (`X^2+X+u`) | E-012's reference is still unconfirmed, but **not load-bearing**: Lemma 1.2 is proved here |
| Theorem 1.4 (`F_j = f_j`) | P-2.4(1) | §1.3 | `[EXH]` at every parameter set; both Hensel routes agree | none |
| Theorem 1.7 (CRT) | **L-2.4.2**, P-2.4(2) | §1.4 (E-011) | `[EXH]` additivity, multiplicativity, bijectivity, idempotent identities, `e_j ↦ (0,..,1,..,0)` | none |
| Lemma 1.8 (locality, basis) | **L-2.4.3, L-2.4.4** | §1.5 | `[EXH]`/`[SMP]` `ρ_j` homomorphism + surjective, `m_j = (u,f_j) = ker ρ_j`, `B_j/m_j` field, nilpotence `≤ t+p^v−1`, units = complement, `dim_{F_q}`, `|B_j|` | none |
| Lemma 1.9 (ideals/submodules) | P-2.4(4), **L-2.6.2** (module part) | §1.6 | `[EXH]` ideal bijection and count product (small rings); `[EXH]` submodule bijection, reconstruction, count product | none |
| Theorem 2.3 (`dim_{K}(m/m²)`) | **L-2.4.6**, **L-2.6.6** | §2 | `[EXH]` CT-2 at 9 parameter sets: `0/1/2` as predicted | none |
| Theorem 3.3 (SNF, `μ ≤ 2`) | **L-2.6.4** | §3 (self-contained) | `[EXH]` `μ ≤ 2` on every submodule of every chain-ring case; `[EXH]` `93 = N(2,8)` | C-2.1d/e (counting submodules by shape) is **not** claimed |
| Theorem 3.6 (chain ⟺) | **L-2.6.3** | §3 | `[EXH]` ideals totally ordered (small rings) / `dim ≤ 1` (large) | none |
| Lemma 4.2 (`μ = max`) | **L-2.4.5, L-2.6.5** | §4.1 | `[EXH]` on every submodule at `(4,2,1)`, `(4,1,2)`, `(2,1,3)`, `(9,1,2)`, `(8,1,2)`; `[SMP]` at `(4,2,3)` | none |
| Theorem 4.1 / 4.3 / Corollary 4.4 | **P-2.6**, **L-2.6.7, L-2.6.8** | §4.1–4.2 | `[EXH]` per-ring "all principal" verdict vs. the criterion; `[EXH]` wild certificates | none for the criterion itself |
| Theorem 6.1, Corollaries 6.2–6.3 | Task D | §6 | `[EXH]` permutation vs. cosets, `σ_k(e_j)`, equivariance, `m_j` images, `μ` invariance; `[EXH]` neg-4 | none |

---

## 8. Report

### 8.1 Proved in Stage 2B

Lemma 1.1, Lemma 1.2 (Hensel, self-contained), Theorem 1.4 (`F_j = f_j`), Theorem 1.7
(CRT), Lemma 1.8 (locality, dimension, nilpotence), Lemma 1.9 (ideals and submodules
under CRT), Theorem 2.3 (`dim_{K_j}(m_j/m_j^2) ∈ {0,1,2}` with the exact trichotomy;
= L-2.4.6 = L-2.6.6), Corollary 2.4, Lemma 3.2, Theorem 3.3 (Smith normal form over a
finite chain ring; = L-2.6.4), Theorem 3.6 (chain ⟺ `t = 1` or `p ∤ n`; = L-2.6.3),
Lemma 4.2 (`μ_B = max_j μ_{B_j}`, Nakayama; = L-2.4.5 = L-2.6.5), Theorem 4.1,
Theorem 4.3, **Corollary 4.4 (P-2.6, both directions)**, Corollary 4.5, Theorem 6.1,
Corollaries 6.2–6.3.

### 8.2 Refuted or modified

* **No claim of the proposal was refuted.** P-2.4(1)–(4) and P-2.6 are **true as stated**
  and are now proved.
* **Modified (sharpened):** P-2.4(1). The proposal says "there are unique monic pairwise
  coprime `F_j ∈ A_t[X]` with `F_j ≡ f_j mod u`"; Stage 2B adds the identification
  **`F_j = f_j`** (Theorem 1.4), which makes the components `A_t[X]/⟨f_j^{p^v}⟩` with
  `f_j ∈ F_q[X]` and the whole decomposition explicit. This is not a correction of an
  error but a strengthening that matters computationally and structurally.
* **Superseded:** **T-021** ("every right ideal is principal", proved only under
  `t = 1` **and** `p ∤ n`). Corollary 4.4 proves the sharp statement with the disjunction
  and the converse. T-021 keeps its own row (`PROVED IN PHASE 1`, conditional) in the
  register; the new row records the supersession.
* **Discharged:** **O-2.1** (the principality boundary, including the predicted
  counterexample `M_2(m)` at `(4,2,2)`).

### 8.3 Exact hypotheses

* §1–§2 (decomposition, local structure): `q = p^r`, `t ≥ 1`, `n ≥ 1`, `X` central; no
  squarefree hypothesis is imposed anywhere (the whole point is the case analysis).
* Lemma 1.2 (Hensel): `A` commutative with a nilpotent principal ideal `(u)`, `g` monic,
  factors pairwise coprime mod `u`.
* Theorem 3.3 (SNF): `S` a **finite chain ring** (used only in the regimes where
  Theorem 3.6 applies).
* Theorem 3.6: `t = 1` or `p ∤ n` (exactly).
* Theorem 4.1: `p ∤ n` or `t = 1`; Theorem 4.3: `p ∣ n` and `t ≥ 2`.
* §6: `σ_k` is the coefficient Frobenius (fixes `u` and `X`); it is only
  `F_p`-linear (`F_q`-semilinear).

### 8.4 Coverage: exhaustive vs sampled

* **Exhaustive** (`[EXH]`, 434 checks): all factorisation and coset identities; the CRT
  map on every element (for `|B| ≤ 600`) or on 600 sampled elements otherwise; the local
  invariants of every component; the full ideal lattices of `B` and of the `B_j` (small
  rings); **the full submodule lattices of `B^2` and of every `B_j^2`** at
  `(4,2,1)`, `(4,1,2)`, `(2,1,3)`, `(9,1,2)`, `(8,1,2)` — including `μ_B(W) = max_j μ_j`
  and a principality certificate for **every** submodule; the **33³ = 35 937**
  CRT-built submodules at `(4,2,3)`; the wild certificates at `(2,2,2)` (with an
  exhaustive scan of all 4096 elements of `M_2(m)`), `(4,2,2)`, `(9,2,3)`; the Galois
  permutation and equivariance; all five negative controls.
* **Sampled** (`[SMP]`, 26 checks, sizes stated on each line): the ring-homomorphism
  checks where `|B| > 600` (600 elements, 600² pairs); the closure, `μ` and principality
  checks at `(4,2,3)` (200 closure, 399 certificates, 180 random submodules); unit
  testing in the large component `(9,2,3)` (300 random elements); the brute-force `μ`
  cross-check where `|W|²` exceeds the budget (200 random pairs).

### 8.5 Remaining obligations, limitations, and open problems

1. **O-2.2 is still open**: is `μ_B(W) ≤ 4` for every `W ⊆ B^2` in the wild case? Stage 2B
   neither needs nor proves it (Theorem 4.1 needs only `μ ≤ 2` in the chain case, and
   Theorem 4.3 exhibits `μ = 4`). The largest value observed anywhere remains `4`.
2. **C-2.1d/e/f/g (enumeration closed forms)** are unchanged: `CONJECTURE` /
   `COMPUTATIONAL TEST PENDING`. Stage 2B verified the *product* formula (Lemma 1.9) and
   the value `33³ = 35 937`, but did **not** attempt a closed form for `N(t,Q)`, `t ≥ 3`.
3. **The wild-case lattice is not enumerated.** At `(4,2,2)` and `(9,2,3)` only targeted
   certificates were computed; the number of submodules of `B^2` there is unknown (part
   of O-2.3).
4. **P-2.7/P-2.8 (duals and annihilators), the hull dimension, Gray maps and quantum
   constructions are out of scope** and untouched; in particular **L-6.1**
   (`θ_s` an anti-automorphism of `R_n`) remains `PROPOSED / UNPROVED` (register T-067).
5. Carried forward unchanged: `rev` (P-2.1f, T-066, `PROPOSED / UNPROVED`), T-006, T-027,
   T-011–T-014, warning B3.5, the Phase-1 coverage gaps, and the `n ≥ 2` left-submodule
   gap.
6. **E-012's reference is still unconfirmed** (flagged in the register). Stage 2B does
   not depend on it: the Hensel step it needs is proved from scratch (Lemma 1.2). The
   same applies to **E-015**, which is cited as prior art only.
7. The principality certificates in §5.3 rest on `|xS| = |I_W|` with `x ∈ I_W`, which is a
   **proof** of principality for that ideal; the *count* of principal ideals is therefore
   exact where the lattice was enumerated. Where the lattice was built via the CRT
   (`(4,2,3)`), the completeness of the list is the theorem (Lemma 1.9), corroborated by
   random sampling — it is not an exhaustive enumeration of `B^2`.
