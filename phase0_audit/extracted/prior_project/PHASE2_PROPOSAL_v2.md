# PHASE 2 — PROPOSAL v2 (structure of cyclic codes over `R_n = M_2(A_t)[X]/⟨X^n−1⟩`)

**Status: PROPOSAL ONLY. Phase 2 is NOT STARTED. Nothing in this file is a proved result.**

This revision addresses the six mandatory clarification points raised on v1. Every
statement below carries, in a uniform block: **Hypotheses · Statement · Status · Proof
strategy and required lemmas · Counterexamples / unresolved cases · Falsification test.**

Status labels used throughout:

| Label | Meaning |
|---|---|
| **DEFINITION** | a convention; neither true nor false |
| **PHASE 1** | already proved in `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` |
| **IMPORTED** | standard fact, cited; hypotheses to be checked before use |
| **PROPOSED** | to be proved *or refuted* in Phase 2; may not be cited until proved |
| **CONJECTURE** | numerically motivated, explicitly unproved, falsifiable |
| **WITHDRAWN** | a v1 statement that is retracted here, with reasons |

Approved decisions **B1**, **B2**, **B3** and all Phase-1 conventions are retained; Phase-1
files and commits are unchanged.

---

## 0. Changes from v1 (change log)

| # | v1 item | Change in v2 | Reason |
|---|---|---|---|
| 1 | P-2.1 stated as six brief properties | Split into P-2.1a–f with **complete coordinate-level proofs**, plus a commutation table separating `R`-linearity from `θ_s`-compatibility | mandatory point 1 |
| 2 | `μ(I_W) = ⌈μ_B(W)/2⌉` inferred from projectivity | `μ` defined precisely; the identity is derived from **two** lemmas (a set-equality lemma using projectivity, plus a separate minimality/counting lemma); explicit **counterexample-search protocol** added | mandatory point 2 |
| 3 | P-2.5/P-2.6 mixed an individual criterion with a global claim | Split into **P-2.5 (individual)** and **P-2.6 (global)**, each with a **proof-obligation list** (L-2.6.1 … L-2.6.7) and a **boundary-case table** (`n = 1`; `t = 1` with `p ∤ n`; `t = 1` with `p ∣ n`; `t ≥ 2` with `p ∤ n`; `t ≥ 2` with `p ∣ n`) | mandatory point 3 |
| 4 | P-2.7/P-2.8 asserted with a sketch | Full step-by-step derivation; `ann_r`, `ann_l`, `rev`, `θ_s` on `R_n` defined explicitly; multiplication order and `θ_s` placement fixed; **`rev` shown to be a ring automorphism**; a **worked hand example** (`n = 3`, `q = 4`, `t = 1`, `s = 0`, `g = E_11 + E_12 X`) verified; the equivalent "reciprocal-generator" form stated; P-2.8 upgraded to an explicit SNF formula | mandatory point 4 |
| 5 | C-2.1 with numeric predictions | All values explicitly **CONJECTURAL** (only `N(1,Q)` and `N(2,Q)` are known from Phase 1), with **three independent counting methods**, an **independent-verification strategy**, **falsification criteria**, and an explicit statement that numerical agreement is not a proof | mandatory point 5 |
| 6 | CRT/Hensel asserted | Precise factorisation hypotheses; the lift applied to the **squarefree part only** (`X^n − 1 = (X^{n'} − 1)^{p^v}`) so repeated factors are never lifted directly; **squarefree / repeated-root / wild** cases tabulated, with the explicit warning that the chain-ring description is unavailable in the wild case | mandatory point 6 |
| 7 | — | New §1 fixes all notation and tabulates **which maps commute, under which convention, and with which linearity type** | mandatory point 1 |
| 8 | Uniform bound `μ_B(W) ≤ 4` floated in P-2.5 | **WITHDRAWN** as a claim; retained as open problem O-2.2 with a falsification test | rigor |
| 9 | O-2.5 asked whether `ker θ_s(g)` is always a summand | Answer **no**, and this is already clear: at `S = F_4[u]/⟨u²⟩`, `v = uI_2` gives `ker v = uS ⊕ uS`, not a summand; O-2.5 restated accordingly | rigor |

---

## 1. Notation, conventions and the commutation table

### 1.1 Standing objects (all **PHASE 1** unless marked)

* `q = p^r` with `r ≥ 2`; `F_q`; `A_t = F_q[u]/⟨u^t⟩` (finite chain ring, maximal ideal
  `(u)`, nilpotency `t`, residue field `F_q`, `|A_t| = q^t`);
* `R = M_2(A_t)`; `B = A_t[X]/⟨X^n − 1⟩` (**commutative**, free of rank `n` over `A_t`);
* `R_n = R[X]/⟨X^n − 1⟩ ≅ M_2(B)` (Lemma 3.1);
* identification `ι : R^n → R_n`, `ι(x) = Σ_{e=0}^{n−1} x_e X^e`, where `x_e ∈ R`;
  indices `e` are read **mod `n`** throughout;
* `σ_s ∈ Aut(A_t)`: `σ_s(Σ a_i u^i) = Σ a_i^{p^s} u^i` (fixes `u`); extended entry-wise to
  `R`, `B`, and coordinate-wise to `R^n`, `R_n` (it fixes `X`);
* `θ_s = σ_s ∘ (·)^T`: anti-automorphism of `R`, extended coordinate-wise to `R^n` and
  `R_n` (fixes `X`); `θ_s² = σ_{2s}`; `ord(θ_s) = 2r/gcd(r, 2s)`;
* `Λ = λ ∘ tr` with `λ` the coefficient of `u^{t−1}`; `B_s(x,y) = Σ_e θ_s(x_e) y_e ∈ R`;
  `b_s = Λ ∘ B_s`;
* **Right-module convention** (Definition 5.1): a *cyclic code* is a right ideal of `R_n`,
  equivalently an `F_q`-subspace `C ⊆ R^n` closed under the right `R`-action and `T`.

### 1.2 The maps (definitions)

| Map | Definition | Convention | Linearity type |
|---|---|---|---|
| `ρ_a` (right action) | `(x·a)_e := x_e a` | `a ∈ R` acts on the **right** of each coordinate | `F_q`-linear |
| `λ_a` (left action) | `(a·x)_e := a x_e` | `a ∈ R` acts on the **left** of each coordinate | `F_q`-linear |
| `T` (cyclic shift) | `(Tx)_e := x_{e−1 mod n}` | Phase-1 convention (Cor. 6.4 proof) | `F_q`-linear |
| `T^{-1}` | `(T^{-1}x)_e := x_{e+1 mod n}` | — | `F_q`-linear |
| `σ_k` | `(σ_k x)_e := σ_k(x_e)` | entry-wise `p^k`-power, coordinate-wise | `σ_k`-semilinear over `F_q`; `F_p`-linear |
| `θ_s` | `(θ_s x)_e := θ_s(x_e)` | coordinate-wise | `σ_s`-semilinear over `F_q`; `F_p`-linear |
| `rev` | `rev(x)_e := x_{−e mod n}` | on `R^n`; on `R_n`, `rev(Σ u_eX^e) := Σ u_{−e}X^e` | `F_q`-linear |
| `μ_B(W)` | `min{k : W is generated by k elements as a B-module}`, `μ_B(0)=0` | minimal number of generators | — |
| `μ_S(I)` | `min{k : I = Σ_{i≤k} x_i S}` for a right ideal `I` of `S`, `μ_S(0)=0` | minimal number of **right-ideal** generators | — |
| `ann_r(v)` | `{w ∈ S : v w = 0}` | **right** annihilator (`v` multiplies from the left) | — |
| `ann_l(v)` | `{w ∈ S : w v = 0}` | **left** annihilator (`v` multiplies from the right) | — |

Convention: "principal" means generated by at most one element, so the zero ideal is
principal and `μ = 0`.

### 1.3 Commutation table (**PROPOSED**, with proofs in §2)

| Relation | Status | Meaning |
|---|---|---|
| `T ρ_a = ρ_a T` | P-2.1a | `T` is **right `R`-linear** (scalar untouched) |
| `T λ_a = λ_a T` | P-2.1b | `T` is **left `R`-linear** (scalar untouched) |
| `T σ_k = σ_k T`, `T θ_s = θ_s T` | P-2.1c | genuine commutation of `F_p`-linear maps |
| `ρ_a λ_b = λ_b ρ_a` | trivial | the two actions commute (associativity) |
| `σ_k ρ_a = ρ_{σ_k(a)} σ_k`; `σ_k λ_a = λ_{σ_k(a)} σ_k` | P-2.1d | `σ_k` is a ring automorphism: it preserves the side |
| `θ_s ρ_a = λ_{θ_s(a)} θ_s` | P-2.1e | **`θ_s` swaps the side**: a right multiplier becomes a **left** multiplier by `θ_s(a)` |
| `θ_s λ_a = ρ_{θ_s(a)} θ_s` | P-2.1e | dual form |
| `rev ρ_a = ρ_a rev`, `rev σ_k = σ_k rev`, `rev θ_s = θ_s rev` | P-2.1f | `rev` permutes coordinates; all these act coordinate-wise |
| `rev T = T^{-1} rev` | P-2.1f | `rev` inverts the shift |
| `θ_s² = σ_{2s}`, `θ_s σ_k = σ_k θ_s` | **PHASE 1** (L4.4) | — |

**The distinction the reviewer asked for.** `T` being `R`-linear (P-2.1a/b) says the scalar
`a` is *untouched* when `T` is moved past the action. Compatibility with `θ_s` is a
*different* statement and comes in two forms, which must not be confused:

* (commutation) `T θ_s = θ_s T` — a plain commutation of maps on the set `R^n`;
* (intertwining) `θ_s ρ_a = λ_{θ_s(a)} θ_s` — `θ_s` **does** move a scalar, and it moves it
  from the right action to the **left** action. This is the property that makes the
  `θ_s`-pairing work (Lemma 5.6a(1)) and it is *not* a statement about `T`.

---

## 2. P-2.1 — the shift: coordinate-level proofs (mandatory point 1)

**Hypotheses.** `n ≥ 1`, `t ≥ 1`, arbitrary `q = p^r`; `R^n` with `ρ`, `λ` as in §1.2;
`R_n` with the indeterminate `X`.

### P-2.1a — `T` is right `R`-linear

**Statement.** For all `x ∈ R^n`, `a ∈ R`: `T(x·a) = (Tx)·a`.

**Status.** **PROPOSED** (proof below is complete; to be transcribed into the Phase-2
document verbatim).

*Proof (coordinate level).* For each `e ∈ Z/nZ`,
`[T(x·a)]_e = (x·a)_{e−1} = x_{e−1} a = (Tx)_e a = [(Tx)·a]_e`. ∎

Note: the proof uses **only** that the right action is coordinate-wise. No centrality of
`X` is involved at this level.

### P-2.1b — `T` is left `R`-linear

**Statement.** For all `x ∈ R^n`, `a ∈ R`: `T(a·x) = a·(Tx)`.

**Status.** **PROPOSED** (proof complete).

*Proof.* `[T(a·x)]_e = (a·x)_{e−1} = a x_{e−1} = a (Tx)_e = [a·(Tx)]_e`. ∎

**Consequence (definition-independent cyclicity).** Because `T` is `R`-linear on *both*
sides, the condition "`C` is closed under `T`" is a property of the `F_q`-subspace `C`
alone and does not depend on the right/left convention. The convention dependence of the
theory enters only through the pairing (Convention 5.2) and through Lemma 5.6a.

### P-2.1c — `T` commutes with `σ_k` and `θ_s`

**Statement.** `T σ_k = σ_k T` and `T θ_s = θ_s T`.

**Status.** **PROPOSED** (proof complete).

*Proof.* `[σ_k(Tx)]_e = σ_k((Tx)_e) = σ_k(x_{e−1}) = (σ_k x)_{e−1} = [T(σ_k x)]_e`.
Identically with `θ_s` in place of `σ_k`, since both act coordinate-wise and `T` permutes
coordinates. ∎

**Linearity caveat.** `T` is `F_q`-linear; `σ_k` and `θ_s` are `F_q`-**semilinear** and
`F_p`-linear. The relations above are commutations of `F_p`-linear maps; they say nothing
about `F_q`-scalar behaviour, and must not be read as "`θ_s` is `R`-linear". The correct
`F_q`-scalar statements are `σ_k(c x) = σ_k(c) σ_k(x)` and `θ_s(cx) = σ_s(c) θ_s(x)` for
`c ∈ F_q` (acting as `cI ∈ Z(R)`).

### P-2.1d/e — `σ_k` preserves the side, `θ_s` swaps it

**Statement.**
(d) `σ_k(x·a) = σ_k(x)·σ_k(a)` and `σ_k(a·x) = σ_k(a)·σ_k(x)`;
(e) `θ_s(x·a) = θ_s(a)·θ_s(x)` and `θ_s(a·x) = θ_s(x)·θ_s(a)`.

**Status.** **PROPOSED** (proofs complete).

*Proof.* (d) `[σ_k(x·a)]_e = σ_k(x_e a) = σ_k(x_e)σ_k(a)` (`σ_k` is a ring automorphism of
`R`), which is `[σ_k(x)·σ_k(a)]_e`. (e) `[θ_s(x·a)]_e = θ_s(x_e a) = θ_s(a)θ_s(x_e)`
(`θ_s` is an **anti**-automorphism of `R`), i.e. the **left** action of `θ_s(a)` on
`θ_s(x)`. The second form is identical with the roles of the factors exchanged. ∎

*Consistency check.* Applying (e) twice returns to the same side:
`θ_s(θ_s(x·a)) = θ_s(θ_s(a)·θ_s(x)) = θ_s(θ_s(x))·θ_s(θ_s(a)) = σ_{2s}(x)·σ_{2s}(a)`,
which agrees with `θ_s² = σ_{2s}` and the fact that an automorphism preserves the action.
This is a non-trivial cross-check of (e) against **PHASE 1** Lemma 4.4.

### P-2.1f — `rev`: definition and properties

**Statement.**
(i) `rev : R^n → R^n` is `F_q`-linear, `rev² = id`, and `rev T = T^{-1} rev`;
(ii) `rev ρ_a = ρ_a rev`, `rev σ_k = σ_k rev`, `rev θ_s = θ_s rev`;
(iii) transported to `R_n` by `ι`, `rev` is a **ring automorphism**:
`rev(uv) = rev(u)rev(v)`, `rev(X) = X^{-1} = X^{n−1}`, `rev|_R = id`;
(iv) `rev(ann_r(v)) = ann_r(rev(v))`.

**Status.** **PROPOSED** (proofs below are complete).

*Proof.* (i) `[rev(Tx)]_e = (Tx)_{−e} = x_{−e−1}` and `[T^{-1}(rev x)]_e = (rev x)_{e+1} =
x_{−e−1}`. (ii) all three maps act coordinate-wise while `rev` permutes coordinates.
(iii) With `u = Σ u_aX^a`, `v = Σ v_bX^b` and `X` central,
`(uv)_e = Σ_{a+b=e} u_a v_b`, so `rev(uv)_e = (uv)_{−e} = Σ_{a+b=−e} u_av_b`, while
`(rev u · rev v)_e = Σ_{a+b=e} u_{−a}v_{−b} = Σ_{a'+b'=−e} u_{a'}v_{b'}` after the
bijection `a ↦ −a`, `b ↦ −b`; the two agree. Hence `rev` is an automorphism (it is the
substitution `X ↦ X^{n−1}`, and `(X^{n−1})^n = 1`). (iv) `v w = 0 ⟺ rev(v)rev(w) = 0`. ∎

**Warning (this is where v1 was imprecise).** `rev` is an **automorphism**, not an
anti-automorphism; consequently the image under `rev` of a right ideal is again a right
ideal. It is **not** `B`-linear (it sends `X ↦ X^{-1}`), so `rev` of a `B`-submodule of
`B²` need not be a `B`-submodule — see the consistency check in §6.

### P-2.1g — `T` as multiplication by `X` (uses centrality)

**Statement.** Under `ι`, `T` equals right multiplication by `X` **and** left
multiplication by `X`; `T^n = id`; `T` is a Hamming isometry.

**Status.** **PROPOSED** (proof complete, assuming `X` central in `R_n`).

*Proof.* `ι(x)·X = Σ_e x_e X^{e+1} = Σ_e x_{e−1}X^e = ι(Tx)` (re-index, using `X^n = 1`);
`X·ι(x) = Σ_e X x_e X^e = Σ_e x_eX^{e+1}` because `X` is central in `R_n` (it commutes
with `R` by construction of `R[X]`, and with everything in `B` since `B` is commutative).
`T^n = id` and the isometry statement are immediate. ∎

**Required lemma L-2.1.1 (centrality).** `X·I_2` is central in `M_2(B)`, equivalently `X`
commutes with every element of `R` inside `R_n`. *Proof strategy:* `R_n = R ⊗_{F_q}
F_q[X]/⟨X^n−1⟩` with the second factor central by construction.

**Known counterexamples / unresolved.** None: P-2.1a–g hold for every `(q,t,n)`. The only
delicate point is the *direction* convention for `T` (`x_{e−1}` vs `x_{e+1}`); the
convention is fixed by **PHASE 1** (Cor. 6.4 uses `B_s(x,Ty) = B_s(T^{-1}x,y)`) and by the
committed script `module_actions_checks.py` (part B). A sign/direction error would show up
immediately in CT-0.

**Falsification test CT-0 (tiny, exhaustive).** For `(q,t,n) ∈ {(4,1,1), (4,1,2), (4,1,3),
(4,2,2)}`, verify by exhaustion over all `x ∈ R^n` (feasible: `|R^n| = q^{4tn}` is `4^4`,
`4^8`, `4^{12}` — the last two only by sampling) and all `a ∈ R` (exhaustive when
`q^{4t} ≤ 70000`, else a seeded sample of 60): P-2.1a–g as *identities of vectors*.
Additionally verify `rev(uv) = rev(u)rev(v)` on `200` random pairs, and
`θ_s(uv) = θ_s(v)θ_s(u)` on `R_n` (this last one is not in Phase 1 for `n ≥ 2` and must be
checked: `θ_s` on `R_n` is an anti-automorphism only if the convolution index swap is
legitimate — see the proof in §6.1).

---

## 3. P-2.3 — generator numbers: precise definitions and the identity (mandatory point 2)

**Hypotheses.** `B` is a commutative finite ring (here `B = A_t[X]/⟨X^n−1⟩`);
`S := M_2(B) = End_B(B²)` acting on **column** vectors (Convention 5.8: columns);
`P := B²`; for a `B`-submodule `W ⊆ P`, `I_W := {M ∈ S : im M ⊆ W}`.

### Definitions (**DEFINITION**)

* `μ_B(W) := min{k ≥ 0 : ∃ w_1,…,w_k ∈ W with W = Σ_i B w_i}`; `μ_B(0) := 0`.
* `μ_S(I) := min{k ≥ 0 : ∃ x_1,…,x_k ∈ I with I = Σ_i x_i S}` for a right ideal `I ⊆ S`;
  `μ_S(0) := 0`. "Principal" `⟺ μ_S(I) ≤ 1`.

### P-2.3(1) — the Morita bijection

**Statement.** `W ↦ I_W` is a bijection from `B`-submodules of `B²` onto right ideals of
`S`, with inverse `I ↦ W(I) := Σ_{M∈I} im M`; and `I_W = Hom_B(P, W) ≅ W ⊕ W` as
`B`-modules, so `dim_{F_q} I_W = 2 dim_{F_q} W` and `|I_W| = |W|²`.

**Status.** `dim I_W = 2 dim W` is **PHASE 1** (Prop. 2.6, and verified computationally at
`t = 1, 2`); the bijection and the Hom description are **IMPORTED** (standard Morita;
`E-005` for fields) — to be written out in Phase 2 with the column convention fixed.

**Required lemma L-2.3.1.** `I_W` is a right ideal, and `W(I_W) = W`.
*Strategy:* `im(MN) ⊆ im M ⊆ W` gives right-ideal closure; `W(I_W) ⊇ W` because for
`w ∈ W` the matrix with first column `w` and second column `0` lies in `I_W`.

### P-2.3(2) — the identity `μ_S(I_W) = ⌈μ_B(W)/2⌉`

**Statement.** For every `B`-submodule `W ⊆ B²`: `μ_S(I_W) = ⌈μ_B(W)/2⌉`.

**Status.** **PROPOSED.** The reviewer is right that this does **not** follow from
projectivity alone; it follows from projectivity **plus** a separate minimality argument.
Both ingredients are stated separately so that each can fail independently.

**Lemma L-2.3a (set equality; uses projectivity).** For `x_1,…,x_k ∈ S`, writing
`W' := Σ_i im(x_i)`, one has `Σ_i x_i S = I_{W'}`.

*Proof.* "`⊆`": `im(x_i M_i) ⊆ im(x_i) ⊆ W'`, and `I_{W'}` is closed under addition.
"`⊇`": let `g ∈ I_{W'}`, i.e. `g : P → P` is `B`-linear with `im g ⊆ W'`. The map
`Φ : P^k → W'`, `(v_1,…,v_k) ↦ Σ_i x_i v_i`, is surjective by definition of `W'`. Since
`P = B²` is **free, hence projective**, `g` lifts along `Φ`: there is a `B`-linear
`G : P → P^k` with `Φ ∘ G = g`. Writing `G = (M_1,…,M_k)` with `M_i ∈ End_B(P) = S`, we get
`g = Σ_i x_i M_i ∈ Σ_i x_i S`. ∎

*Note.* Projectivity is used **only** here, and only to convert "image containment" into
"factorisation". Nothing about minimality is claimed.

**Lemma L-2.3b (counting).** `min{k : W = Σ_{i=1}^k U_i with each U_i generated by ≤ 2
elements} = ⌈μ_B(W)/2⌉`.

*Proof.* Let `m := μ_B(W)`. If `W = Σ_{i≤k} U_i` with `U_i` generated by `≤ 2` elements,
then `W` is generated by `≤ 2k` elements, so `2k ≥ m`, i.e. `k ≥ ⌈m/2⌉`. Conversely put
`k := ⌈m/2⌉`, so `2k ≥ m`; let `w_1,…,w_m` generate `W` and pad with zeros to a list of
`2k` elements; grouping them into `k` consecutive pairs and letting `U_i` be the submodule
generated by the `i`-th pair gives `W = Σ_{i≤k} U_i` with each `U_i` generated by `≤ 2`
elements. ∎

**Lemma L-2.3c (realisability).** For any two elements `w_1, w_2 ∈ P` there is `x ∈ S`
with `im x = B w_1 + B w_2` (take `x` with columns `w_1, w_2`). Hence "sum of `k`
submodules generated by `≤ 2` elements" `=` "sum of `k` images `im(x_i)`".

*Proof of P-2.3(2).* By L-2.3a, `I_W = Σ_{i≤k} x_i S` for some `x_i` **iff**
`W = Σ_i im(x_i)` (injectivity of the Morita bijection, L-2.3.1). Therefore
`μ_S(I_W) = min{k : W = Σ_{i≤k} im(x_i)} = min{k : W = Σ_{i≤k} U_i, μ_B(U_i) ≤ 2}`
(L-2.3c) `= ⌈μ_B(W)/2⌉` (L-2.3b). ∎

**Boundary cases.** `W = 0`: both sides `0`. `W = B²`: `μ_B = 2`, `⌈2/2⌉ = 1`,
`I_W = S` generated by the identity. `W` cyclic (`μ_B = 1`): `⌈1/2⌉ = 1` — a cyclic
submodule still needs one matrix (with a possibly zero second column), consistent.

**Known counterexamples / unresolved.** None known. The identity is *not* claimed for
`m × m` matrices with `m ≠ 2` (there it would read `μ = ⌈μ_B(W)/m⌉`), and it is **not**
claimed for `B` non-commutative (irrelevant here: `B` is commutative). If L-2.3a failed
for some ring, the identity could fail; L-2.3a uses only freeness of `B²`, so it is safe.

**Falsification test CT-1a (counterexample search, exhaustive).** For the rings

| ring `B` | `|B|` | `|B²|` | `|S| = |B|^4` |
|---|---|---|---|
| `F_2[u]/⟨u²⟩` | 4 | 16 | 256 |
| `F_2[u]/⟨u³⟩` | 8 | 64 | 4096 |
| `F_2[u,ε]/⟨u²,ε²⟩` (wild model) | 16 | 256 | 65536 |

do, for **every** submodule `W ⊆ B²` (enumerated by BFS closure under multiplication by
`u` and, in the wild model, by `ε`):

1. compute `μ_B(W)` by brute force: the least `k ≤ 4` such that some `k`-tuple of elements
   of `W` generates `W` (search all tuples for `k = 1, 2`; for `k ≥ 3` use
   `μ_B(W) = dim_{B/m}(W/mW)` after verifying Nakayama on the same run);
2. compute `μ_S(I_W)` by brute force: test `μ_S = 0` (`I_W = 0`), then `μ_S = 1` by
   scanning **all** `x ∈ S` and checking `xS = I_W` (feasible: `|S| ≤ 65536`), then
   `μ_S = 2` by exhibiting two generators built from a minimal generating set of `W` via
   L-2.3c;
3. compare with `⌈μ_B(W)/2⌉`.

**Falsification criterion.** A single mismatch refutes P-2.3(2) as stated; the report must
then state which of L-2.3a / L-2.3b / L-2.3c fails and why.

### P-2.3(3) — two-sided ideals

**Statement.** `I_W` is two-sided ⟺ `W = J·B² = J ⊕ J` for an ideal `J ⊴ B`.

**Status.** **IMPORTED** (`E-003`: two-sided ideals of `M_m(B)` are `M_m(J)`); to be
translated into the column convention in Phase 2.

---

## 4. P-2.4 — CRT/Hensel decomposition with precise hypotheses (mandatory point 6)

**Notation.** `n = p^v n'` with `gcd(n', p) = 1` (`v = v_p(n)`). Over `F_q`:
`X^n − 1 = (X^{n'})^{p^v} − 1 = (X^{n'} − 1)^{p^v}` (characteristic `p`), and
`X^{n'} − 1` is **squarefree** (its derivative `n' X^{n'−1}` is non-zero and coprime to it).
Write `X^{n'} − 1 = ∏_{j=1}^{J} f_j` with `f_j` distinct monic irreducibles over `F_q`,
`d_j := deg f_j`. The `d_j` are the sizes of the `q`-cyclotomic cosets mod `n'`, hence
depend only on `(q, n')`, **not** on `t`.

### P-2.4 — statement

**Status.** **PROPOSED** (the factorisation is standard; the *ring-theoretic* description
of the factors and the case analysis below are the content to be proved in Phase 2).

1. (Hensel) There are unique monic, pairwise coprime `F_j ∈ A_t[X]` with `F_j ≡ f_j mod u`
   and `X^{n'} − 1 = ∏_j F_j` exactly in `A_t[X]`.
2. (CRT) `B ≅ ∏_{j=1}^{J} B_j` with `B_j := A_t[X]/⟨F_j^{p^v}⟩`.
3. `B_j` is **local** with maximal ideal `m_j = (u, F_j)`, residue field
   `K_j = F_q[X]/⟨f_j⟩ ≅ F_{q^{d_j}}`, `dim_{F_q} B_j = t·d_j·p^v`, `|B_j| = q^{t d_j p^v}`.
4. Consequently `W ↔ (W_1,…,W_J)` with `W_j ⊆ B_j²` a `B_j`-submodule,
   `dim_{F_q} W = Σ_j dim_{F_q} W_j`, and `μ_B(W) = max_j μ_{B_j}(W_j)`.

**Proof strategy and required lemmas.**

* **L-2.4.1 (Hensel).** `A_t` is finite local with maximal ideal `(u)`, hence complete for
  the `(u)`-adic topology, and the `f_j` are pairwise coprime monic; Hensel's lemma for
  coprime factorisations lifts `∏ f_j` to `∏ F_j` dividing `X^{n'}−1` with `F_j ≡ f_j`
  mod `u`. **IMPORTANT:** the lift is applied to the **squarefree part only**; the repeated
  factor `f_j^{p^v}` is never lifted directly — it is obtained as `F_j^{p^v}`. (v1 was
  imprecise on this point.)
* **L-2.4.2 (CRT).** The `F_j^{p^v}` are pairwise coprime monic polynomials, so the ideals
  `⟨F_j^{p^v}⟩` are pairwise comaximal in `A_t[X]` and CRT applies.
* **L-2.4.3 (locality).** In `B_j`, `m_j = (u, F_j)` satisfies `B_j/m_j ≅ F_q[X]/⟨f_j⟩ =
  K_j` (a field), and `m_j` is nilpotent (`u^t = 0`, `F_j^{p^v} = 0`, so
  `m_j^{t + p^v − 1} = 0`); hence `m_j` is the nilradical and `B_j` is local.
* **L-2.4.4 (basis).** Reduction modulo the monic polynomial `F_j^{p^v}` of degree
  `d_j p^v` gives the normal form `Σ_{a<t, b<d_jp^v} c_{ab} u^aX^b`, whence
  `dim_{F_q} B_j = t·d_j·p^v`.
* **L-2.4.5 (generators across components).** For `W = ⊕_j W_j` over `B = ∏ B_j`:
  `μ_B(W) = max_j μ_{B_j}(W_j)` (a generating set generates each component; conversely pad
  componentwise generating sets with zeros and take the coordinatewise maximum).

### The three cases (this is the case distinction the reviewer required)

| Case | Hypothesis | `B_j` | Chain ring? | Structural tools available |
|---|---|---|---|---|
| **Squarefree** | `p ∤ n` (`v = 0`) | `A_t[X]/⟨F_j⟩ ≅ F_{q^{d_j}}[u]/⟨u^t⟩ =: A_t^{(d_j)}` | **yes** — `m_j = (u)`, nilpotency `t` | Smith normal form; submodules `≅ u^aS ⊕ u^bS` |
| **Repeated root, `t = 1`** | `p ∣ n`, `t = 1` | `F_q[X]/⟨f_j^{p^v}⟩` | **yes** — `m_j = (f_j)`, nilpotency `p^v` | same (chain ring) |
| **Wild** | `p ∣ n` **and** `t ≥ 2` | `A_t[X]/⟨F_j^{p^v}⟩`, `m_j = (u, F_j)` | **NO** — `m_j` needs two generators | **none of the above**: no SNF, no shape classification, no chain-ring enumeration |

**Required lemma L-2.4.6 (the wild case is genuinely non-chain).** If `t ≥ 2` and
`e := p^v ≥ 2`, then `dim_{K_j}(m_j/m_j²) = 2`; hence `m_j` is not principal and `B_j` is
not a chain ring. *Strategy:* `m_j` is spanned over `F_q` by the monomials
`u^aF_j^b` with `a + b ≥ 1` and `m_j²` by those with `a + b ≥ 2`, so `m_j/m_j²` is spanned
by the classes of `u` and `F_j`; these are `K_j`-linearly independent (each spans a
`K_j`-line of `F_q`-dimension `d_j`, and `dim_{F_q}(m_j/m_j²) = 2d_j`).

**Explicit warning (mandatory point 6).** In the wild case the decomposition is a product
of **local, non-chain** rings. Therefore: no Smith normal form, no classification of
submodules of `B_j²` by shapes, and **no** reduction of the cyclic-code enumeration to a
product of chain-ring counts. Any Phase-2 statement that silently uses SNF or a
`(q^{d}+3)`-type factor in the wild case is invalid.

**Known counterexamples / unresolved.** The Phase-1 datum `33 ≠ 49` at `q = 4, n = 2` is
the `t = 1` repeated-root case (there `B ≅ F_4[ε]/⟨ε²⟩` **is** a chain ring with residue
`F_4`, and `33 = N(2,4)`, consistent). The genuinely wild datum (`t ≥ 2`, `p ∣ n`) does
**not** exist yet: no count is known for `(q,t,n) = (4,2,2)`, and predicting it is
**O-2.2**, not a corollary of anything above.

**Falsification test CT-2.** For `(q,t,n) ∈ {(4,2,2), (4,2,4), (9,2,3), (4,2,3), (4,3,2)}`,
compute `J`, the `d_j` and `e = p^v` by factoring `X^{n'}−1` over `F_q`; verify by
exhaustion that `|B| = q^{tn}` equals `∏_j |B_j|`, that each `B_j` has a unique maximal
ideal, that `dim_{K_j}(m_j/m_j²)` equals `1` in the squarefree and `t = 1` cases and `2`
in the wild case, and that `B_j` is a chain ring **exactly** when predicted.

---

## 5. Principality: individual criterion and global claim (mandatory point 3)

### 5.1 P-2.5 — individual criterion

**Hypotheses.** `B` commutative finite; `S = M_2(B)`; `W ⊆ B²` a `B`-submodule;
`I_W = {M : im M ⊆ W}`.

**Statement (individual).**
(a) `μ_S(I_W) = ⌈μ_B(W)/2⌉` ( = P-2.3(2) );
(b) `I_W` is **principal** `⟺ μ_B(W) ≤ 2`;
(c) `I_W` is generated by `2` elements whenever `μ_B(W) ≤ 4`.

**Status.** (a),(b) **PROPOSED** (proof: §3). (c) is a conditional corollary.

**Proof obligations.** L-2.3a, L-2.3b, L-2.3c, L-2.3.1 — all listed in §3.

**Boundary cases.**

| `W` | `μ_B(W)` | `I_W` | `μ_S` | Check |
|---|---|---|---|---|
| `0` | 0 | `0` | 0 | principal by convention |
| `B w` (cyclic) | 1 | matrices with columns in `Bw` | 1 | generator = `(w, 0)` |
| `B²` | 2 | `S` | 1 | generator = `I_2` |
| `u^aS ⊕ u^bS` (chain-ring factor) | ≤ 2 | — | 1 | principal |
| `m_j ⊕ m_j` (wild factor) | 4 (by L-2.4.6 + Nakayama) | `M_2(m_j)` | 2 | **not** principal |

**Withdrawn.** v1's uniform bound "`μ_B(W) ≤ 4` for all `W`" is **WITHDRAWN** as a claim
(it was never proved). It is retained as open problem **O-2.2**; it is verified in the
model wild ring `F_2[u,ε]/⟨u²,ε²⟩` (there `m² = 0`, so every submodule `W ⊆ B²` lies in
`mB² = m ⊕ m`, has `F_2`-dimension `≤ 4` and `μ_B(W) = dim_{F_2} W` by Nakayama).

**Falsification test.** CT-1a (§3) tests P-2.5(a)(b) exhaustively on three small rings.

### 5.2 P-2.6 — global claim (separate statement, separate obligations)

**Statement (global).** *Every* right ideal of `R_n` is principal `⟺ p ∤ n` or `t = 1`.

**Status.** **PROPOSED** (conjectured boundary; the `⇐` direction has a complete strategy,
the `⇒` direction rests on L-2.4.6 and on the Morita/`μ` machinery).

**Proof obligations.**

| # | Obligation | Status | Notes |
|---|---|---|---|
| **L-2.6.1** | every right ideal of `R_n` is `I_W` for a unique `W` (Morita bijection onto) | IMPORTED (to be written out) | necessary even to speak of "every right ideal" |
| **L-2.6.2** | CRT/Hensel decomposition of `B` with the case analysis | P-2.4 | §4 |
| **L-2.6.3** | `B_j` is a chain ring ⟺ `t = 1` or `p ∤ n` | PROPOSED | `⇐` by `m_j = (u)` resp. `(F_j)`; `⇒` by L-2.4.6 |
| **L-2.6.4** | over a finite chain ring `S`, every submodule of `S²` is `≅ u^aS ⊕ u^bS`, hence `2`-generated | PROPOSED | Smith normal form: in a chain ring, of any two elements one divides the other, so the classical elimination works; `im(U D V) = U·im(D) = U(u^aS ⊕ u^bS)` |
| **L-2.6.5** | `μ_B(W) = max_j μ_{B_j}(W_j)`; `μ_{B_j}(W_j) = dim_{K_j}(W_j/m_jW_j)` (Nakayama, `B_j` local) | PROPOSED | standard |
| **L-2.6.6** | `dim_{K_j}(m_j/m_j²) = 2` iff (`t ≥ 2` **and** `p ∣ n`), else `1` | PROPOSED | = L-2.4.6 |
| **L-2.6.7** | conclude: `p ∤ n` or `t = 1` ⟹ every `W_j` is `2`-generated ⟹ (L-2.4.5) `μ_B(W) ≤ 2` ⟹ (P-2.5) every `I_W` principal | PROPOSED | — |
| **L-2.6.8** | converse: `p ∣ n` and `t ≥ 2` ⟹ `W := m_j ⊕ m_j` (on one factor, `0` elsewhere) has `μ_B(W) = 4` ⟹ `I_W = M_2(m_j)` has `μ_S = 2` ⟹ not principal | PROPOSED | uses L-2.6.5, L-2.6.6 |

**Boundary cases (checked individually).**

| Case | Prediction | Reason | Status |
|---|---|---|---|
| `n = 1` (any `q,t`) | all principal | `B = A_t` (single factor, `d = 1`, `e = 1`); chain ring | to verify (Phase 1 counted `7/12/11/33` right ideals but did **not** test principality) |
| `t = 1`, `p ∤ n` | all principal | `B` a product of fields; `M_2` of a product of fields is semisimple | to verify |
| `t = 1`, `p ∣ n` | all principal | `B_j = F_q[X]/⟨f_j^{p^v}⟩` chain ring | **new**; Phase 1's `33` at `(4,1,2)` is consistent but untested for principality |
| `t ≥ 2`, `p ∤ n` | all principal | `B_j = A_t^{(d_j)}` chain ring | **new** |
| `t ≥ 2`, `p ∣ n` | **not** all principal | `I_{m_j⊕m_j} = M_2(m_j)`, `μ_S = 2` | **new**; explicit predicted counterexample |

**Known counterexamples / unresolved.**
* The predicted counterexample at `(q,t,n) = (4,2,2)`: `B = F_4[u,ε]/⟨u²,ε²⟩`
  (`ε = X + 1`), `m = (u,ε)`, `W = m ⊕ m`, `I_W = M_2(m)`. This is a **prediction**, not a
  verified counterexample; CT-1 must confirm that no single `x` satisfies `xS = M_2(m)`.
* Unresolved: in the wild case, is `μ_B(W) ≤ 4` for *every* `W` (so that every right ideal
  is `2`-generated)? **O-2.2**.
* Unresolved: for `t ≥ 2`, `p ∤ n`, does every right ideal admit a generator of the special
  form `U·diag(u^a,u^b)` (SNF form)? Expected yes; needed for P-2.8.

**Falsification test CT-1.** For `(q,t,n) ∈ {(4,1,1), (4,1,2), (4,1,3), (4,2,1), (4,2,3),
(9,2,1), (9,2,3), (4,2,2)}`: enumerate all `B`-submodules of `B²` by BFS closure under
multiplication by `X` and `u`; for each compute `μ_B(W)`; apply P-2.5 to predict
`μ_S(I_W)`; then **verify** the prediction directly by exhaustive search for a single
generator (`μ_S = 1`) over all `x ∈ S` when `|S| ≤ 10^6`, and by exhibiting two generators
from a minimal generating set of `W` when the prediction is `2`. Report the number of
non-principal right ideals.

| `(q,t,n)` | CT-1 prediction |
|---|---|
| `(4,1,1)`, `(4,1,2)`, `(4,1,3)` | `7`, `33`, `343` codes, **all** principal |
| `(4,2,1)`, `(4,2,3)`, `(9,2,1)` | `33`, `35 937`, `113` codes, **all** principal |
| `(9,2,3)`, `(4,2,2)` | **at least one** non-principal right ideal (viz. `M_2(m_j)`) |

---

## 6. P-2.7 / P-2.8 — dual and annihilator: full derivation (mandatory point 4)

### 6.0 Conventions fixed before the derivation (**DEFINITION**)

* `ann_r^{R_n}(v) := {w ∈ R_n : v·w = 0}` (`v` on the **left**);
  `ann_l^{R_n}(v) := {w ∈ R_n : w·v = 0}`.
* `θ_s` on `R_n`: `θ_s(Σ u_eX^e) := Σ θ_s(u_e) X^e` — `θ_s` is applied **only to the
  generator `g`** in the formulas below, never to `y`; it fixes `X`.
* `rev` on `R_n`: `rev(Σ u_eX^e) := Σ u_{−e}X^e`; a ring **automorphism** (P-2.1f(iii)),
  `rev(X) = X^{n−1}`, `rev|_R = id`; on `R^n`: `rev(y)_e = y_{−e}`.
* Products in `R_n` are convolutions in the central variable `X`:
  `(uv)_e = Σ_{a+b=e} u_a v_b`.
* `C = g·R_n` is the right ideal generated by `g` (right multiplication).

### 6.1 Required lemma: `θ_s` is an anti-automorphism of `R_n`

**Status.** **PROPOSED** (new in v2 — Phase 1 proves this only for `R`, i.e. `n = 1`).

*Proof.* `θ_s((uv)_e) = θ_s(Σ_{a+b=e}u_av_b) = Σ_{a+b=e}θ_s(v_b)θ_s(u_a)` (additive +
anti on `R`), while `(θ_s(v)θ_s(u))_e = Σ_{a+b=e}θ_s(v_a)θ_s(u_b)`; these agree by the
bijection `(a,b) ↦ (b,a)` on the index set `{a+b=e}`. Bijectivity is clear
(`θ_s^{-1} = σ_{−2s}θ_s`, using `θ_s² = σ_{2s}` and `θ_sσ_k = σ_kθ_s`). ∎

**Falsification.** CT-0 must check `θ_s(uv) = θ_s(v)θ_s(u)` on random pairs in `R_n` for
`n = 2, 3` before anything below is used.

### 6.2 P-2.7 — statement

**Hypotheses.** `C = g·R_n` a principal cyclic code, `g = Σ_e g_eX^e ∈ R_n`; `s` arbitrary;
`B_s(x,y) = Σ_e θ_s(x_e)y_e`.

**Statement.**
$$C^{\perp_s} \;=\; \mathrm{rev}\big(\mathrm{ann}_r^{R_n}(\theta_s(g))\big)
\;=\; \mathrm{ann}_r^{R_n}\big(\theta_s(\mathrm{rev}\,g)\big)
\;=\; \{\,y \in R^n : \theta_s(g)\cdot \mathrm{rev}(y) = 0 \text{ in } R_n\,\}.$$
In Morita terms `ann_r(θ_s(g)) = I_{ker(θ_s(g))}` (matrices whose columns lie in the
kernel of `θ_s(g)` acting on `B²`), so
`dim_{F_q} C^{\perp_s} = 2 dim_{F_q} ker(θ_s(g))` and `|C^{\perp_s}| = |ker θ_s(g)|²`.

**Status.** **PROPOSED** (derivation complete below, modulo L-6.1 and the Phase-1
non-degeneracy).

### 6.3 Derivation, step by step

Let `y ∈ R^n` and `m ∈ R_n`. Write `z(y) ∈ R^n` for the vector with coordinates
`z_b := Σ_{a} θ_s(g_a)\, y_{a+b}` (indices mod `n`).

**Step 1 (expand the product).** `(gm)_e = Σ_{a+b=e} g_a m_b` (convolution; `X` central).

**Step 2 (apply `θ_s`).** `θ_s((gm)_e) = Σ_{a+b=e} θ_s(g_a m_b) = Σ_{a+b=e} θ_s(m_b)θ_s(g_a)`
— note the **order**: `θ_s` is anti, so the `m`-factor comes first.

**Step 3 (form the pairing and re-index).**
`B_s(gm, y) = Σ_e Σ_{a+b=e} θ_s(m_b)θ_s(g_a)y_e = Σ_b θ_s(m_b)\big(Σ_a θ_s(g_a) y_{a+b}\big)
= Σ_b θ_s(m_b) z_b = B_s(m, z)`.

**Step 4 (use non-degeneracy).** `y ∈ C^{⊥_s} ⟺ B_s(gm,y) = 0 ∀m ⟺ B_s(m,z) = 0 ∀m ⟺ z = 0`,
because the **right** radical of `B_s` is trivial (Theorem 6.6, **PHASE 1**).

**Step 5 (convert `z` into a product).** With `w := rev(y)`, i.e. `w_f = y_{−f}`:
`[θ_s(g)·w]_k = Σ_{a+f=k}θ_s(g)_a w_f = Σ_a θ_s(g_a)\, y_{a−k}`, whereas
`z_b = Σ_a θ_s(g_a) y_{a+b}`; hence `[θ_s(g)·rev(y)]_k = z_{−k}`, i.e.
`z = rev(θ_s(g)·rev(y))`.

**Step 6 (conclude).** `z = 0 ⟺ θ_s(g)·rev(y) = 0` (`rev` injective) `⟺ rev(y) ∈
ann_r(θ_s(g)) ⟺ y ∈ rev(ann_r(θ_s(g)))` (`rev² = id`). The second displayed form follows
from `rev(ann_r(v)) = ann_r(rev(v))` (P-2.1f(iv)) and `rev(θ_s(g)) = θ_s(rev g)`. ∎

**Multiplication order, in words.** The left factor is `θ_s(g)`, the right factor is
`rev(y)`; the condition is that their product vanish. `θ_s` is applied to `g` only.

### 6.4 Worked hand example (verification before retaining the statement)

Take `q = 4`, `t = 1`, `n = 3`, `s = 0`, and `g = E_11 + E_12 X`, i.e. as a matrix over
`B = F_4[X]/⟨X³−1⟩`, `g = [[1, X],[0,0]]`. (Here `X` is a **unit**, `X^{-1} = X²`.)

1. **The code.** For `M ∈ M_2(B)` with rows `r_1, r_2`, `gM` has rows `r_1 + X r_2` and `0`.
   Hence `C = gR_3 = {[[a,b],[0,0]] : a,b ∈ B}` and `|C| = |B|² = (4³)² = 4⁶`.
2. **`θ_0(g)`.** `θ_0 = (·)^T`, so `θ_0(g) = [[1,0],[X,0]]`.
3. **The annihilator.** `[[1,0],[X,0]]·[[w_11,w_12],[w_21,w_22]] = [[w_11,w_12],[Xw_11,Xw_12]]`,
   which vanishes iff `w_11 = w_12 = 0` (as `X` is a unit). So
   `ann_r(θ_0(g)) = {[[0,0],[c,d]] : c,d ∈ B}` — equivalently, matrices whose columns lie in
   `ker [[1,0],[X,0]] = {(0,z₂)}`.
4. **Reversal.** `X ↦ X²`, so `rev([[0,0],[c,d]]) = [[0,0],[rev c, rev d]]`, and `c ↦ rev c`
   is a bijection of `B`; hence `rev(ann_r(θ_0(g))) = ann_r(θ_0(g))` **as a set** in this
   example. Prediction: `C^{⊥_0} = {[[0,0],[c,d]] : c,d ∈ B}`, of size `|B|² = 4⁶`.
5. **Direct verification.** Let `y = [[0,0],[p,q]]` with `p,q ∈ B`, `p = Σ p_eX^e`,
   `q = Σ q_eX^e`; an element `c ∈ C` has coordinates `c_e = [[a_e,b_e],[0,0]]` with
   `a_e,b_e ∈ F_4` arbitrary. Then `c_e^T = [[a_e,0],[b_e,0]]` and
   `y_e = [[0,0],[p_e,q_e]]`, so `c_e^T y_e = 0` for every `e`, whence `B_0(c,y) = 0`.
   Conversely the size count `|C|·|C^{⊥_0}| = 4⁶·4⁶ = 4^{12} = |R|³` forces equality.
   ✔ The formula survives.
6. **Honest limitation of this example.** The annihilator here is `rev`-stable, so this
   example does **not** test the reversal. A `rev`-sensitive test is mandatory in CT-4:
   find `g` with `rev(ann_r(θ_s(g))) ≠ ann_r(θ_s(g))` and check which one equals
   `C^{⊥_s}`. (Both sets are right ideals, since `rev` is an automorphism; they need not be
   equal.)

### 6.5 Consistency checks (each is a falsification opportunity)

* **(C1) Sizes.** `|C^{⊥_s}| = |ann_r(θ_s(g))|`; the Frobenius-ring identity
  `|ann_r(v)|·|vR_n| = |R_n|` (**IMPORTED**, requires `R_n` Frobenius) gives
  `|C^{⊥_s}| = |R_n|/|θ_s(g)R_n| = |R_n|/|R_n g|`. Agreement with the Phase-1 formula
  `|C^{⊥_s}| = |R|^n/|gR_n|` therefore requires `|gR_n| = |R_n g|`.
  **Required lemma L-6.5:** for `x ∈ M_m(B)` with `B` a finite Frobenius ring, the row
  module and the column module of `x` have equal cardinality. *Strategy:* with the standard
  dot product, `im(x)^⊥ = ker(x^T)`; the Frobenius identity `|M|·|M^⊥| = |B|^m` gives
  `|ker(x^T)| = |B|^m/|im x|`, and `|im x^T| = |B|^m/|ker(x^T)| = |im x|`; the row module is
  `im(x^T)`. **Required lemma L-6.6:** `B` is Frobenius (*strategy*: `B = A_t[X]/⟨h⟩` with
  `h` monic is a Frobenius `A_t`-algebra via the residue pairing, `A_t` is Frobenius over
  `F_q`, and Frobenius is transitive for free algebras; `M_2(B)` is Frobenius).
* **(C2) `n = 1`.** `rev = id`, so `C^{⊥_s} = ann_r^R(θ_s(g)) = {y : θ_s(g)y = 0}`.
  Direct check: `B_s(gm,y) = θ_s(gm)y = θ_s(m)θ_s(g)y`, and `θ_s(m)` ranges over all of `R`,
  so vanishing for all `m` is equivalent to `θ_s(g)y = 0`. ✔
* **(C3) Extreme `g`.** `g = 1`: `C = R_n`, formula gives `C^{⊥_s} = rev(ann_r(1)) = 0`. ✔
  `g = 0`: `C = 0`, formula gives `rev(ann_r(0)) = rev(R_n) = R^n`. ✔
* **(C4) Module structure.** `ann_r(v)` is a right ideal (`v w = 0 ⇒ v(wm) = 0`) and `rev`
  is an automorphism, so `rev(ann_r(v))` is a right ideal — consistent with Corollary 6.4
  (**PHASE 1**). If any computed `rev(ann_r(θ_s(g)))` failed to be a right ideal, P-2.7
  would be refuted.

**Falsification test CT-4.** For `(q,t,n,s)` ∈ `{(4,1,3,0), (4,1,3,1), (9,1,2,0), (4,1,2,1),
(4,2,1,0), (4,2,3,0)}` and for **every** principal cyclic code (i.e. every code when the
case is non-wild; a seeded sample of 200 codes at `(4,2,3)`):
(i) compute `C^{⊥_s}` from the Phase-1 linear-algebra routine;
(ii) compute `rev(ann_r(θ_s(g)))` by Morita as `I_{ker(θ_s(g))}` then reversing;
(iii) compare as sets, and compare `|C|·|C^{⊥_s}|` with `|R|^n`;
(iv) record whether `ann_r(θ_s(g))` is `rev`-stable, and report at least one `g` where it
is not (or report that none exists — itself a finding);
(v) check `|gR_n| = |R_n g|` (C1).

### 6.6 P-2.8 — explicit generator of the dual

**Hypotheses.** `C = gR_n`; `B` is a product of **chain rings** (`p ∤ n` or `t = 1`), so
that Smith normal form is available over each `B_j` (L-2.6.4); write
`v := θ_s(rev g)` (equivalently work with `θ_s(g)` and reverse at the end).

**Statement.** With `v = θ_s(rev g)` and (componentwise, over `B = ∏ B_j`)
`v_j = U_j · diag(ω^{a_j}, ω^{b_j}) · V_j` the Smith normal form of `v_j` over the chain
ring `B_j` (`ω_j` a generator of the maximal ideal, `0 ≤ a_j ≤ b_j ≤ ℓ_j` the nilpotency
length), one has

$$C^{\perp_s} \;=\; h\cdot R_n,\qquad
h_j \;=\; V_j^{-1}\,\mathrm{diag}\big(\omega_j^{\,\ell_j-a_j},\ \omega_j^{\,\ell_j-b_j}\big).$$

**Status.** **PROPOSED.** (v1 only asserted existence; the explicit form is new here.)

*Proof strategy.* By P-2.7, `C^{⊥_s} = ann_r(v)`. Now `ann_r(v) = {w : v w = 0} = {w : im w ⊆
ker v} = I_{ker v}`. With `v = U D V`, `ker v = V^{-1} ker D`, and over a chain ring
`ker diag(ω^a, ω^b) = ann(ω^a) ⊕ ann(ω^b) = ω^{ℓ−a}S ⊕ ω^{ℓ−b}S`. A generator of
`I_{ker v}` is any matrix whose two columns generate `ker v` (P-2.5 + L-2.3c), namely
`V^{-1}diag(ω^{ℓ−a}, ω^{ℓ−b})`. Finally assemble the components by CRT.

**Sanity check (classical limit).** For `t = 1` and `p ∤ n` the factors are fields,
`ω = 0`, `ℓ = 1`, so the exponents are `a_j, b_j ∈ {0,1}` and `ℓ − a ∈ {1,0}`: the
generator is the **complementary projection** — exactly the classical statement that the
dual code is generated by the "check polynomial" `h` with `g h = X^n − 1` (up to the
`θ_s`-twist and the reversal). This is the sense in which P-2.8 is the correct analogue.

**Counterexamples / unresolved.**
* In the **wild** case there is no SNF, so P-2.8 gives nothing; whether `C^{⊥_s}` is
  principal there is **O-2.8** (it *is* principal whenever `μ_B(ker θ_s(g)) ≤ 2`, by P-2.5,
  even without SNF — so the open question is whether `μ_B(ker v) ≤ 2` always holds).
* `ker(v)` need not be a direct summand of `B²`: at `S = F_4[u]/⟨u²⟩` and `v = uI_2`,
  `ker v = uS ⊕ uS` is not a summand (the quotient is `F_4²`, not free). So **O-2.5 as
  posed in v1 is answered negatively**; the principality of `ann_r(v)` survives because
  `μ_B(uS ⊕ uS) = 2 ≤ 2`.

**Falsification test.** Included in CT-4: for each principal `C`, verify that the `h`
produced by the SNF recipe satisfies `hR_n = C^{⊥_s}`.

---

## 7. C-2.1 — submodule counts over a chain ring (mandatory point 5)

**Notation.** `S := F_Q[u]/⟨u^t⟩` (finite chain ring, residue field `F_Q`, nilpotency `t`);
`N(t,Q) := # {S-submodules of S²}`.

**Status of the values.** **CONJECTURE** — explicitly unproved, and *numerical agreement is
not a proof*. Two cases are known and are **not** conjectures:

| Value | Status |
|---|---|
| `N(1,Q) = Q + 3` | **PHASE 1** — `t = 1`: `S = F_Q`, submodules = subspaces of `F_Q²` |
| `N(2,Q) = Q² + 3Q + 5` | **PHASE 1** (Corollary 2.7, verified at `Q = 4`: `33`) |
| `N(t,Q)` for `t ≥ 3` | **CONJECTURE** |

**Conjecture C-2.1 (shape counts).** Submodules of `S²` are (as `S`-modules) of the form
`u^aS ⊕ u^bS`, `0 ≤ a ≤ b ≤ t`; for `a < b` the number of submodules of that shape is
`Q^{\,b−a−1}(Q+1)`, and for `a = b` it is `1`. Consequently

$$N(t,Q) \;=\; (t+1) \;+\; (Q+1)\sum_{d=1}^{t}(t+1-d)\,Q^{\,d-1}.$$

*Consistency:* `t = 1` gives `2 + (Q+1) = Q+3` ✔; `t = 2` gives `3 + (Q+1)(Q+2) =
Q²+3Q+5` ✔ (both **PHASE 1**).
*Arithmetic of the closed form (all hand-checkable).*
`N(3,Q) = 4 + (Q+1)(Q²+2Q+3) = Q³+3Q²+5Q+7`, hence `N(3,2) = 8+12+10+7 = 37` and
`N(3,4) = 64+48+20+7 = 139`, `N(3,9) = 729+243+45+7 = 1024`.
`N(4,Q) = 5 + (Q+1)(Q³+2Q²+3Q+4)`, hence `N(4,2) = 5 + 3·(8+8+6+4) = 83`.
`N(2,9) = 81+27+5 = 113`. Every one of these is a **prediction of the conjecture**, not a
computed value.

**Counting method (three independent routes; all three must be run).**

1. **BFS over the submodule lattice (enumeration).** Start from `{0}`; repeatedly add one
   vector of `S²` and close the `F_Q`-span under multiplication by `u`; canonical key =
   reduced row-echelon basis over `F_Q` of the `2t`-dimensional `F_Q`-space. (The committed
   Phase-1 routine `b_submodules` in `04_COMPUTATION/module_actions_checks.py` already does
   exactly this, closing under `X` and `u`; running it with *new* parameters is Phase-2
   work.) Cost: `|S²| = Q^{2t}` candidate vectors; feasible for `Q^{2t} ≤ 10^5`.
2. **Brute-force over all `F_Q`-subspaces (independent of route 1).** Enumerate all
   subspaces of the `2t`-dimensional `F_Q`-space and keep those closed under multiplication
   by `u`. Independent code path; feasible for `Q^{2t} ≤ 10^4` (e.g. `Q = 2, t ≤ 3`;
   `Q = 4, t = 2`).
3. **Closed form (route 3 = C-2.1).** The formula above, *derived* only if the shape
   classification is proved.

**Independent verification strategy.** Agreement of routes 1 and 2 on the overlap
(`(Q,t) = (2,2), (2,3), (4,2)`) validates the *enumeration*; agreement of route 1 with
route 3 on `t = 1, 2` is a **sanity check the formula already passes**; agreement on
`t ≥ 3` is **evidence, not proof**. Proof requires the shape classification: that every
submodule of `S²` over a chain ring has a Smith normal form `U diag(u^a,u^b) V` (so
`≅ u^aS ⊕ u^bS`), and that the number of submodules of a given shape is
`Q^{b−a−1}(Q+1)` — the latter requires counting the orbits/cosets parametrising the
embeddings (this is the genuinely open part).

**Falsification criteria.** (i) Any disagreement between routes 1 and 2 on their overlap
refutes the *enumeration* and everything must be re-run. (ii) Any disagreement between
route 1 and C-2.1 refutes the conjecture, and the shape counts must be recomputed (the
report must then say for which `(t,Q)` the failure first occurs). (iii) A proof of the
shape classification that yields a different closed form supersedes C-2.1.

**Explicit warning.** Agreement at ten parameter values does not make the formula a
theorem. In the Phase-2 document and in the register, `N(t,Q)` for `t ≥ 3` may be recorded
as `conjectural` until the shape classification is proved; the register row must say which
values were checked, not merely that they matched.

---

## 8. Open problems (updated from v1)

| ID | Problem | Status |
|---|---|---|
| **O-2.1** | Principality boundary (P-2.6), including the predicted counterexample `M_2(m)` at `(4,2,2)` | open; CT-1 |
| **O-2.2** | Wild case: classify submodules of `B_j²`; decide whether `μ_B(W) ≤ 4` always (so every right ideal is `2`-generated) | open; the v1 claim of the bound is **withdrawn**; CT-1, CT-5 |
| **O-2.3** | Enumeration at `t ≥ 2`: `N(t,Q)` (C-2.1) and the product formula over CRT factors | conjectural; CT-2, CT-3 |
| **O-2.4** | Explicit generator of the dual (P-2.8) and its failure mode in the wild case | open; CT-4 |
| **O-2.5** | (restated) For which `v` is `ker v` a direct summand of `B²`? — **not** always (`v = uI_2` over `F_4[u]/⟨u²⟩`) | partially answered; classification open |
| **O-2.6** | Galois action `σ_s` on the CRT components (it preserves each `B_j` and induces Frobenius on `K_j`); effect on `σ_{2s}`-invariance and on the per-code rescue (Theorem 7.4) | open; CT-6 |
| **O-2.7** | `n = 1` anchor: confirm that the whole theory degenerates to the ideal theory of `M_2(A_t)` (`7/12/11/33` right ideals, all principal) | open; CT-1 |
| **O-2.8** | In the wild case, is `μ_B(ker θ_s(g)) ≤ 2` for every `g` (equivalently: is the dual of every principal code principal)? | open; CT-4, CT-5 |
| **Carried forward (D3)** | T-006 (entry-wise form, uncharacterised), T-021 (resolved by P-2.6 only if proved), T-027 (general `τ ∈ Aut(A_t)`), hull formulas (Phase 4), Gray map (Phase 5), quantum (Phase 6, warning B3.5) | recorded, not resolved |

---

## 9. Computational test plan (all Phase-2 work; none of it has been run)

| Test | What it does | Refutes |
|---|---|---|
| **CT-0** | Exhaustive/sampled verification of P-2.1a–g, including `θ_s(uv)=θ_s(v)θ_s(u)` on `R_n` for `n = 2,3` and `rev(uv)=rev(u)rev(v)` | §2 |
| **CT-1a** | Exhaustive check of `μ_S(I_W) = ⌈μ_B(W)/2⌉` on `F_2[u]/⟨u²⟩`, `F_2[u]/⟨u³⟩`, `F_2[u,ε]/⟨u²,ε²⟩` | P-2.3(2), P-2.5 |
| **CT-1** | Principality census over the boundary-case table (`n=1`; `t=1` with/without `p∣n`; `t≥2` with/without `p∣n`), with the explicit `M_2(m)` test | P-2.6, O-2.1, O-2.2, O-2.7 |
| **CT-2** | CRT/Hensel data: `J`, `d_j`, `e = p^v`, `dim_{K_j}(m_j/m_j²)`, chain-ring predicate | P-2.4, L-2.4.6 |
| **CT-3** | Census of cyclic codes at `t ≥ 2` where `p ∤ n` (predicted `N(2,4)=33`, `N(2,9)=113`, `N(2,4)³ = 35 937`, `N(3,4)=139`) compared with C-2.1 | C-2.1, O-2.3 |
| **CT-4** | P-2.7/P-2.8 on every principal code at six parameter sets; `rev`-sensitivity search; `|gR_n| = |R_n g|` | P-2.7, P-2.8, L-6.5, O-2.8 |
| **CT-5** | Wild-case census at `(4,2,2)`, `(4,2,4)`, `(9,2,3)`: submodule counts, `μ_B` distribution, principality | O-2.2, O-2.8 |
| **CT-6** | Galois action on CRT components and `σ_{2s}`-invariant counts | O-2.6 |
| **Regression** | Re-run `ring_structure_checks.py` (401/401) and `module_actions_checks.py` (276/276); require byte-identical logs | guards Phase 1 |

---

## 10. Scope, deliverables, and the approval gate

**Out of scope (explicit).** Hull-dimension *formulas* and self-dual code constructions
(Phase 4); Gray maps and metric statements (Phase 5); quantum constructions (Phase 6, under
warning B3.5); any change to Phase-1 conventions (**D1**); the manuscript.

**Deliverables.** (1) `03_THEOREMS/CYCLIC_CODE_STRUCTURE.md` with complete proofs of
P-2.1–P-2.8 **or** their refutations and corrected statements; (2) scripts + logs for
CT-0 … CT-6 with `[EXH]`/`[SMP]` labels and seeds, plus the Phase-1 regression run;
(3) register rows `T-044 …` for what is proved or refuted — including an updated **T-021**
stating the exact principality hypothesis, a row for **C-2.1** recording precisely which
values were *checked* (not merely that they matched), and rows for every withdrawn
statement; (4) an honest carried-forward list (decision **D3**).

**Approval.** Phase 2 is **NOT STARTED** and will begin only on explicit approval of this
v2 proposal (scope §10, statement list §2–§7, test plan §9).
