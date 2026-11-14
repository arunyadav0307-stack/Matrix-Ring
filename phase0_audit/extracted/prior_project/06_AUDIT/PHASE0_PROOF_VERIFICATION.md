# Phase 0 — Independent Proof Verification

Every result below was re-derived from the definitions **before** consulting
`03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`; the file was read afterwards and the two
compared. Notation is fixed in §0. Verdicts used:

* **VERIFIED** — the statement is true and the existing proof (or the one below) is complete;
* **VERIFIED (better proof below)** — true, but the argument below is shorter/cleaner or
  removes a hidden assumption;
* **FALSE AS STATED / NEEDS HYPOTHESIS** — a correction is required;
* **UNRESOLVED** — cannot be settled here.

---

## 0. Setting

* `q = p^r`, `A_t = F_q[u]/⟨u^t⟩` (u central in `A_t`), `R = M_m(A_t)`,
  `R_n = R[X]/⟨X^n − 1⟩ ≅ M_m(B)`, `B = A_t[X]/⟨X^n − 1⟩` (commutative).
* `σ_s`: the **coefficient-wise** Frobenius, `σ_s(a) = a^{p^s}` on `F_q`, `σ_s(u) = u`,
  extended entrywise to `A_t`, `R`, `R_n`. (In `R_n`, `σ_s(X) = X`.)
* `θ_s = σ_s ∘ (·)^T` (entrywise Frobenius **then** transpose; the two commute).
* Pairing (the form actually used by `galois_duality_experiments.pair_theta`):

  $$B_s(x,y)\;=\;\sum_{e=0}^{n-1} \theta_s(x_e)\,y_e \;\in R ,$$

  and its trace-valued companion `b_s(x,y) = Λ(B_s(x,y))` with `Λ = λ ∘ tr`,
  `λ` = coefficient of `u^{t−1}`.
* `C^{⊥_s} = { y ∈ R^n : B_s(x,y) = 0 for all x ∈ C }` (a *right* orthogonal: θ sits in
  the first slot, and `B_s` is right-`R`-linear in `y`).
* "cyclic code of length n" = **right ideal** of `R_n`.

---

## 1. σ_s is a ring automorphism **VERIFIED**

`a ↦ a^{p^s}` is a field automorphism of `F_q` of order `r/gcd(r,s)` (so `σ_s = id ⟺ r | s`
and `σ_s` is nontrivial ⟺ `r ∤ s`); `u ↦ u` extends it to `A_t` (`σ_s(Σ a_i u^i) =
Σ a_i^{p^s} u^i`); entrywise extension to `M_m(A_t)` preserves addition and
multiplication componentwise. Bijective because `σ_s` is. Order on `M_m(A_t)` is again
`r/gcd(r,s)`.

**Hidden assumption (must be stated).** `Aut(A_t)` is much larger than `{σ_s}`: an
automorphism may send `u ↦ c_1u + c_2u² + …` with `c_1 ≠ 0`. *We use only the
coefficient-Frobenius subgroup.* Everything in §3–§6 below works verbatim for an
arbitrary `τ ∈ Aut(A_t)` with `θ_τ = τ ∘ (·)^T`; only the final criterion changes
(§5). This is not a defect, but it is an unstated restriction in the current write-up.

**Counterexample to the naive converse.** `σ_s = id` on `F_q` when `r | s`; at `q = 8`
(`r = 3`), `σ_1, σ_2` are both non-trivial of order 3 — verified on 4 000 sampled pairs.

---

## 2. θ_s is an anti-automorphism and θ_s² = σ_{2s} **VERIFIED (better proof below)**

$$\theta_s(XY)=\sigma_s\big((XY)^T\big)=\sigma_s(Y^TX^T)=\sigma_s(Y^T)\sigma_s(X^T)=\theta_s(Y)\theta_s(X),$$

additive and bijective ⇒ anti-automorphism. For the square:

$$\theta_s^2(X)=\theta_s\big(\sigma_s(X^T)\big)=\sigma_s\big(\sigma_s(X^T)^T\big)=\sigma_s\big(\sigma_s(X)\big)=\sigma_{2s}(X),$$

because transpose commutes with the entrywise Frobenius and `σ_s(X^T)^T = σ_s(X)`.
Hence **θ_s is an involution ⟺ σ_{2s} = id ⟺ r | 2s** (the last step because `σ_k = id
⟺ r | k`). Verified exhaustively on all 256 elements of `M_2(F_4[u]/⟨u²⟩)` (θ² = σ_{2s}
holds) and falsified at `q = 8` for `s = 1, 2` (σ_{2s} ≠ id).

---

## 3. Sesquilinearity and the key symmetry identity **VERIFIED (new, and load-bearing)**

Right-`R`-linearity in the second slot:
`B_s(x, y·a) = Σ θ_s(x_e)(y_e a) = (Σ θ_s(x_e) y_e) a = B_s(x,y)·a`.
In the first slot: `B_s(x·a, y) = Σ θ_s(x_e a) y_e = Σ θ_s(a)θ_s(x_e) y_e = θ_s(a)·B_s(x,y)`
— i.e. **θ_s-semilinear**, not linear.

**Key identity (new; it is what makes everything work):**

$$\boxed{\ \theta_s\big(B_s(x,y)\big)\;=\;B_s\big(y,\;\sigma_{2s}(x)\big)\ }$$

Proof: `θ_s(B_s(x,y)) = Σ θ_s(θ_s(x_e) y_e) = Σ θ_s(y_e) θ_s(θ_s(x_e)) = Σ θ_s(y_e) σ_{2s}(x_e) = B_s(y, σ_{2s}x)`. ∎

Consequences (all verified computationally, §2.3 of the audit report):

1. `B_s(x,y) = 0 ⟺ B_s(y, σ_{2s}x) = 0` (θ_s is bijective);
2. **the form is symmetric ⟺ σ_{2s} = id** — for `r ∤ 2s` it is *not* symmetric and not
   Hermitian either, only "σ_{2s}-twisted symmetric";
3. therefore **self-orthogonality cannot be tested on `B_s(x,x)` alone** (or on
   `B_s(g_i,g_j)` for `i ≤ j`) unless `r | 2s`. Any manuscript lemma of the form
   "`C ⊆ C^{⊥_s}` iff `G θ_s(G)^T = 0`" must carry the hypothesis `r | 2s`.
   *(Finding F-06.)*

---

## 4. Non-degeneracy, dual is a right module, size formula **VERIFIED**

**Non-degeneracy of `b_s`.** `(X,Y) ↦ Λ(XY)` is non-degenerate on `M_m(A_t)`: this is the
Frobenius property of `Λ` (T-001: Λ is symmetric, associative and *ideal-catching*, i.e.
non-zero on every non-zero left/right ideal). Given `y ≠ 0`, pick `e` with `y_e ≠ 0`;
ideal-catching gives `Z` with `Λ(Z y_e) ≠ 0`; put `x_e = θ_s^{-1}(Z)` and `x_j = 0`
elsewhere; then `b_s(x,y) = Λ(Z y_e) ≠ 0`. Since `dim V = N = m²tn`, right
non-degeneracy implies left non-degeneracy.
*Computational corroboration (independent implementation):* Gram rank of
`(X,Y) ↦ Λ(XY)` is **4/4** at `t = 1, m = 2` and **8/8** at `t = 2`; Gram rank of
`b_s` is full for every tested `(q, t, n, s)` (q = 4, 8, 9; t = 1 with n = 1, 2, 3 and
all s; t = 2 with n = 1, 2, 3).

**`C^{⊥_s}` is a right `R`-module.** If `y ∈ C^{⊥_s}` and `a ∈ R`, then
`B_s(x, y·a) = B_s(x,y)·a = 0`. ✓ (100 % on all runs.)

**Size formula.** `V → C^*`, `y ↦ (x ↦ b_s(x,y))` is `F_q`-linear with kernel `C^{⊥_s}`
and is **onto** (non-degeneracy + finite dimension: the image has dimension
`N − dim C^{⊥_s}` and the annihilator of `C` in `V` is exactly `C^{⊥_s}`, so
`dim C + dim C^{⊥_s} = N`). Hence
`|C|·|C^{⊥_s}| = q^N = |R|^n`. ✓ **PROVED** (this is the only place non-degeneracy is
used, and it is a genuine proof, not an experiment).

---

## 5. Double dual: `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` **VERIFIED (proof below; 100 % on data)**

*Inclusion.* Let `c ∈ C` and `y ∈ C^{⊥_s}`. By §3(1), `B_s(y, σ_{2s}c) = 0`
(because `B_s(c,y) = 0`). Hence `σ_{2s}(C) ⊆ (C^{⊥_s})^{⊥_s}`.
*Equality.* `dim σ_{2s}(C) = dim C` (σ is a bijection and `F_p`-linear), and by the size
formula applied twice `dim (C^{⊥_s})^{⊥_s} = N − dim C^{⊥_s} = dim C`. ∎

Equivalently and more generally: for **any** `τ ∈ Aut(A_t)`, with `θ_τ = τ∘(·)^T`,
`(C^{⊥})^{⊥} = τ²(C)`; our statement is the case `τ = σ_s`, `τ² = σ_{2s}`.
*Data:* 343/343, 737/737 (s = 1 and s = 2), 144/144, 5 000/5 000, and 100 % in the
independent implementation (7, 11, 11, 12, 33, 35 codes) — **including at `q = 8` where
`σ_{2s} ≠ id`**, i.e. the formula is exactly right and is *not* the reflexive statement.

---

## 6. Reflexivity criterion `r | 2s` **VERIFIED (hypothesis `m ≥ 2` is essential)**

By §5, `C ↦ C^{⊥_s}` is reflexive (i.e. `C^{⊥⊥} = C` for **all** right submodules `C`)
⟺ `σ_{2s}(C) = C` for all `C` ⟺ `σ_{2s} = id` on `A_t` ⟺ `r | 2s`
(the middle equivalence needs one submodule that detects `σ_{2s}`: under Morita, right
submodules of `A_t^m` ↔ submodules `W ⊆ A_t^m`; take `W = A_t(e_1 + a e_2)`, then
`σ_{2s}(W) = A_t(e_1 + σ_{2s}(a)e_2) ≠ W` whenever `σ_{2s}(a) ≠ a` — this is exactly the
counterexample recorded in the register, and it requires `m ≥ 2`).

**F-05 (must be added to T-017).** For `m = 1` the ring is `A_t`, whose ideals are
`(u^i)`; every one of them is σ-invariant, so `σ_{2s}(C) = C` for all `C` and the duality
is **always reflexive**. The hypothesis `m ≥ 2` is therefore not cosmetic.

*Data:* reflexive 343/343 (q = 4), 144/144 and 5 000/5 000 (q = 9), 33/33 (t = 2),
35/35 and 7/7, 12/12 — versus **35/737** at `q = 8` for both `s = 1` and `s = 2`, and
5/11 in the independent run. Note (F-11): at q = 8, 35 codes *are* reflexive; the
criterion is about *all* codes, and the looser reading "r ∤ 2s ⇒ no reflexive codes" is
false.

---

## 7. Cyclicity of the dual **VERIFIED (direct proof, no Morita needed)**

Let `T` be the cyclic shift, `(Tx)_e = x_{e−1}` (indices mod n). Then
`B_s(Tx, y) = Σ θ_s(x_{e−1}) y_e = Σ θ_s(x_e) y_{e+1} = B_s(x, T^{−1}y)` and likewise
`B_s(x, Ty) = B_s(T^{−1}x, y)`. Hence for `y ∈ C^{⊥_s}` and `x ∈ C`,
`B_s(x, Ty) = B_s(T^{−1}x, y) = 0` because `T^{−1}x ∈ C`. So `C^{⊥_s}` is
shift-invariant, and by §4 it is a right `R`-module; therefore it is a right ideal of
`R_n`, i.e. a cyclic code. ∎

(For the hull: `Hull_s(C) = C ∩ C^{⊥_s}` is an intersection of right ideals of `R_n`,
hence a right ideal, hence a cyclic code — *no* principality is needed for that
statement. T-021 "every cyclic code is principal" is a **separate** claim and remains
conditional on `t = 1` **and** `X^n − 1` squarefree.)

---

## 8. The σ_{2s}-isometry lemma **VERIFIED (new; settles U9)**

For every `k`, `σ_k` commutes with the transpose and `Λ(σ_k M) = σ_k(Λ(M))`, hence

* **(E1)** `B_s(σ_k x, σ_k y) = σ_k(B_s(x,y))`;
* **(E2)** `B_s(x,y) = 0 ⟺ B_s(σ_k x, σ_k y) = 0`;
* **(E3)** `wt(σ_k x) = wt(x)` (Hamming weight over the alphabet `R`);
* **(E4)** `σ_k(C^{⊥_s}) = (σ_k C)^{⊥_s}`;
* **(E5)** `Hull_s(σ_k C) = σ_k(Hull_s(C))`.

*Data (supplied pairing, supplied enumerator):* E1–E3 300/300 random pairs in each of the
four parameter sets; E4, E5 343/343, 737/737 (×2), 144/144, 5 000/5 000.

**Corollary (the answer to U9).** Even when `r ∤ 2s`, `C^{⊥_s⊥_s} = σ_{2s}(C)` is a code
with the **same cardinality, the same weight enumerator, the same minimum distance and
the same hull dimension** as `C`. So none of the numerical invariants used by hull-based
quantum constructions can see the failure of reflexivity. See
`PHASE0_U8_U9_DECISIONS.md` §5 for what reflexivity *is* needed for.

---

## 9. Equality of the `R`-valued and `F_q`-valued orthogonals (T-010) **VERIFIED**

`C^{⊥,R}_s := {y : B_s(C,y) = 0}` and `C^{⊥,F_q}_s := {y : b_s(C,y) = 0}`.
Trivially `C^{⊥,R} ⊆ C^{⊥,F_q}`; `b_s` is a non-degenerate `F_q`-bilinear form, so
`dim C^{⊥,F_q} = N − dim C` (§4); the supplied experiments show
`dim C^{⊥,R} = N − dim C` for every code tested. Containment + equal dimension ⇒
**equality**. *Data:* 6 961/6 961 (code, s) instances across `q = 4 (n=3)`,
`q = 8 (n=3, s=1,2)`, `q = 9 (n=2)`, `q = 9 (n=4, sampled)`.

*Orientation remark.* The supplied code applies θ_s to the **first** slot; the
independent implementation applies it to the second (`Σ Λ(x_e θ_s(y_e))`). Both give the
same dual (6 961/6 961 and 100 % respectively), as they must by the size-formula
argument. The register should say the convention is immaterial.

---

## 10. Enumeration formula (T-018) **NEEDS HYPOTHESIS (F-04)**

Claim as recorded: if `X^n − 1 = ∏ f_j` over `F_q` with `deg f_j = d_j`, then

$$\#\{\text{cyclic codes}\}\;=\;\prod_j\ \sum_{i=0}^{m}\begin{bmatrix}m\\ i\end{bmatrix}_{q^{d_j}} .$$

This uses **CRT** (`B ≅ ∏ F_{q^{d_j}}`) and therefore requires `X^n − 1` **squarefree**
(i.e. `gcd(n,p) = 1`). The register states T-021 (principality) with that hypothesis but
not T-018.

**Counterexample (independent enumeration, `q = 4, n = 2`, `m = 2`).** In characteristic 2,
`X² − 1 = (X+1)²` is not squarefree. The formula (two degree-1 factors) predicts
`(1 + 5 + 1)² = 49`. The true number of right ideals is **33**
(`B = F_4[ε]/⟨ε²⟩`, and `M_2(B)`-right-ideals ↔ `B`-submodules of `B²`; see §11).
So the hypothesis `gcd(n,p) = 1` is **essential**, not decorative. Validated instances
where it does hold: `343 = 7³` (`q=4,n=3`), `144 = 12²` (`q=9,n=2`), `5`, `35 = 5·7`.

---

## 11. The `t = 2` census: 33, not 32 **VERIFIED (F-03)**

Right ideals of `M_2(A)`, `A = F_q[u]/⟨u²⟩`, ↔ `A`-submodules `W ⊆ A²` (Morita), with
`dim_{F_q}` of the ideal `= m·dim_{F_q} W = 2 dim_{F_q} W`. Counting submodules of `A²`
directly (`|A| = q²`, `uA² ≅ F_q²`, `A^× = q² − q`):

| `dim_{F_q} W` | submodules | count |
|---|---|---|
| 0 | `{0}` | 1 |
| 1 | any line inside `uA² ≅ F_q²` | `q + 1` |
| 2 | free cyclic `A·w`, `w ∉ uA²`: `(q⁴ − q²)/(q² − q) = q(q+1)`; plus `uA²` | `q² + q + 1` |
| 3 | duals of the dim-1 ones | `q + 1` |
| 4 | `A²` | 1 |

Total `= q² + 3q + 5`; for `q = 4`: `16 + 12 + 5 = 33`, with ideal dimensions
`[(0,1), (2,5), (4,21), (6,5), (8,1)]` — exactly what the corrected script and the
independent enumeration produce. (`q = 2` predicts 15.)

The supplied `galois_t2_check.py` reported **32** because it skipped the zero vector and
never seeded `seen` with the zero subspace; patched (`seen = {tuple(): []}`), it now
reports 33 and 33/33 on every per-code check (right module, dual right module, size
formula, hull right module, double-dual = σ_{2s}(C), reflexivity). **All downstream
documents quoting 32 must be corrected.**

---

## 12. Cyclicity / principality (T-021) **UNCHANGED, still conditional**

Proved for `t = 1` with `X^n − 1` squarefree (`B` is a product of fields, `M_m(B)` is a
product of matrix rings over fields, every right ideal is generated by an idempotent).
Open — and now known to be delicate — for `t ≥ 2` or `p | n`: at `q = 4, n = 2` the
ring `B` is `F_4[ε]/⟨ε²⟩`, which is a chain ring, and the submodule lattice is strictly
richer than the "product of subspace lattices" picture. Nothing may use principality
there.

---

## 13. Summary table

| Result | Verdict |
|---|---|
| σ_s automorphism; order `r/gcd(r,s)`; `= id ⟺ r|s` | **VERIFIED** (+ hidden assumption: coefficient-Frobenius subgroup only) |
| θ_s anti-automorphism; θ_s² = σ_{2s}; involution ⟺ `r|2s` | **VERIFIED** |
| `B_s` right-`R`-linear in y, θ_s-semilinear in x | **VERIFIED** |
| Key identity `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)` | **VERIFIED (new)** |
| Non-degeneracy of `b_s` | **VERIFIED** (ideal-catching + Gram rank full) |
| `C^{⊥_s}` right module | **VERIFIED** |
| `|C|·|C^{⊥_s}| = |R|^n` | **VERIFIED (proved, not just observed)** |
| `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` | **VERIFIED** (inclusion + dimension) |
| Reflexive ⟺ `r | 2s` | **VERIFIED** (needs `m ≥ 2`; **F-05**) |
| `C` cyclic ⇒ `C^{⊥_s}` cyclic | **VERIFIED** (direct shift argument) |
| Hull is a right ideal / cyclic code | **VERIFIED** (trivial intersection argument) |
| σ_{2s} isometry (E1–E5) | **VERIFIED (new)** |
| `R`-valued dual = `F_q`-valued dual (T-010) | **VERIFIED** (inclusion + dimension; 6 961/6 961) |
| Enumeration formula (T-018) | **NEEDS HYPOTHESIS** `gcd(n,p)=1` (**F-04**) |
| t = 2 census | **VERIFIED = 33**, structural derivation `q²+3q+5` (**F-03**) |
| Principality (T-021) | **conditional**; open for `t ≥ 2` or `p|n` |
| A1 Theorem 1 as recorded | **UNRESOLVED / inconsistent** (**F-01**) |
