# Phase 0 — Parameter Selection Recommendation (B3)

**Status:** recommendation only. The researcher decides. Nothing here modifies an
approved mathematical result; the new observations below (§3.4, §3.5) are labelled
"computational, proof to be supplied" and are **not** entered into the theorem register
until they are proved and the researcher agrees.

---

## 1. The two regimes

Recall `q = p^r`, `σ_s = Frob^s` (coefficient-wise), `θ_s = σ_s ∘ transpose`, and

$$B_s(x,y)=\sum_e \theta_s(x_e)\,y_e,\qquad C^{\perp_s}=\{y : B_s(C,y)=0\}.$$

| | **Regime 1 — general non-trivial Galois** | **Regime 2 — reflexive (`r ∣ 2s`)** |
|---|---|---|
| defining condition | `r ∤ s` (σ_s non-trivial), no restriction on `2s` | `r ∣ 2s` |
| θ_s | anti-automorphism, `θ_s² = σ_{2s} ≠ id` | **involution** |
| non-trivial choices exist for | every `r ≥ 2` | only `r` even: `s = r/2` (`σ_s` of order 2); `s ≡ 0` is the trivial/Euclidean member |
| examples | `q = 8` (`r=3`), `s=1,2`; `q = 27` (`r=3`), `s=1,2`; `q=16` (`r=4`), `s=1,3` | `q = 4, s=1`; `q = 9, s=1`; `q = 16, s=2`; `q = 25, s=1`; and `s ≡ 0` for every `q` |

**Structural fact (proved, N11 in the novelty file).** For `r` odd,
`r ∣ 2s ⟺ r ∣ s ⟺ σ_s = id`: **non-triviality of the Galois action and reflexivity are
mutually exclusive.** For `r` even, `s = r/2` is the unique non-trivial reflexive choice
(up to `s ≡ r/2 mod r`). For `r = 1` (`q = p`) there is no Galois action at all.

---

## 2. What is true in both regimes (no hypothesis needed)

These are proved and were verified on **2 011 (code, s) instances** over four parameter
sets in `04_COMPUTATION/decision_support_checks.py` (with the assertion
`(C^⊥)^⊥ = σ_{2s}(C)` firing on every single one):

* `C^{⊥_s}` is a right `R`-module; `C` cyclic ⇒ `C^{⊥_s}` cyclic;
* `|C|·|C^{⊥_s}| = |R|^n` (proved from non-degeneracy);
* `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`;
* `Hull_s(C) = C ∩ C^{⊥_s}` is a cyclic code;
* `σ_k` is a semilinear isometry: `B_s(σ_k x, σ_k y) = σ_k B_s(x,y)`, Hamming weight
  preserved, `σ_k(C^{⊥}) = (σ_k C)^{⊥}`, `Hull(σ_k C) = σ_k Hull(C)`;
* the key identity `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)`;
* `dim Hull(C^⊥) = dim Hull(C)` — **verified 1 254/1 254, both regimes** (§3.5).

What differs is exactly one thing: **whether `σ_{2s}` is the identity.**

---

## 3. The six areas, one by one

### 3.1 Galois hull characterization

| | Reflexive | General |
|---|---|---|
| `Hull_s(C) = C ∩ C^{⊥_s}` | a cyclic code, and the relation "`x ∈ C^{⊥_s}" is `σ_s`-Hermitian: `b_s(y,x) = σ_s(b_s(x,y))` | a cyclic code, but the relation is only *twisted*: `b_s(y,x) = σ_s(b_s(σ_{−2s}x, y))` |
| consequence | `Hull_s(C)` can be computed from a Gram matrix of `C` in the usual way; `C ⊆ C^{⊥_s}` can be tested on `i ≤ j` | **all ordered pairs must be tested**; the `G θ_s(G)^T = 0` shortcut is invalid |
| data | `b_s` Hermitian: 300/300 at `q=4`, 300/300 at `q=9` | 30/300 and 38/300 at `q=8`; 13/300 at `q=27` |

**Verdict.** Hulls exist and are well behaved in both regimes; only the *computational
handling* and the *symmetry* differ. Self-orthogonality tests are the practical casualty
in the general regime.

### 3.2 Duality and double-dual properties

| | Reflexive | General |
|---|---|---|
| `C ↦ C^{⊥_s}` | an involution of the code lattice (a Galois connection with itself) | a bijection with inverse `C ↦ σ_{−2s}(C^{⊥_s})` — still a bijection, but not an involution |
| `(C^{⊥})^{⊥}` | `C` | `σ_{2s}(C)` — **35/737 codes at `q=8` have `σ_{2s}(C) ≠ C`** |
| consequences | `C^{⊥⊥} = C` can be used freely | every proof step of the form "and the dual of the dual is the code" needs `σ_{2s}(C) = C` or must be redone |

**Verdict.** The double-dual *formula* holds in both; the *reflexive identity* only in
Regime 2. Nothing is lost for parameter-level statements (§2, isometry), but structural
proofs must be rewritten.

### 3.3 LCD codes

LCD means `C ∩ C^{⊥_s} = 0`; since `dim C + dim C^{⊥} = N`, this is equivalent to
`C ⊕ C^{⊥_s} = R^n` — a statement that uses only the size formula, **not** reflexivity.

* Reflexive: 64/343 LCD at `q=4,n=3`; 64/144 at `q=9,n=2`.
* General: 640/737 at `q=8,n=3` (both `s`); 30/30 at `q=27,n=1`.
* **"C LCD ⇒ C^{⊥} LCD" holds in both**: 64/64, 64/64, 640/640, 30/30 — i.e. **798/798**.
  This follows from `dim Hull(C^⊥) = dim Hull(C)` (§3.5), since
  `Hull(C^⊥) = C^⊥ ∩ (C^⊥)^{⊥} = C^⊥ ∩ σ_{2s}(C)`.

**Verdict.** **LCD is regime-independent.** Note the striking quantitative difference:
LCD codes are *abundant* in the non-reflexive regime (87 % at `q = 8`) and *rare* in the
reflexive one (19 % at `q = 4`). If an LCD-family paper is ever wanted, Regime 1 is the
richer hunting ground.

### 3.4 CSS construction

The classical CSS input is a pair `C_2 ⊆ C_1` (or a self-orthogonal `C ⊆ C^{⊥}`), and
the parameter derivation identifies the centralizer/normalizer of the stabilizer group
using the duals of `C_1` and `C_2`, **including `(C_i^{⊥})^{⊥} = C_i`**.

* Reflexive: the standard derivation applies verbatim, with `b_s` playing the role of the
  Hermitian form (exactly as in the Galois-hull literature over commutative rings —
  Zhang–Kong–Zheng 2026 use ℓ-Galois hulls with `σ^{2ℓ} = id`).
* General: two obstructions. **(i)** the derivation uses `C^{⊥⊥} = C`;
  **(ii)** the stabilizer machinery needs the underlying `F_p`-bilinear commutation form
  to be symmetric (or alternating). Here that form is `T(x,y) = Tr_{F_q/F_p}(b_s(x,y))`,
  and `r ∣ 2s` gives `b_s(y,x) = σ_s(b_s(x,y))`, whence — because the field trace is
  Frobenius-invariant — `T(y,x) = T(x,y)` ✓. In the general regime this fails:
  measured **138/300** and **158/300** at `q = 8` (≈ chance), **100/300** and **96/300**
  at `q = 27`.

**Per-code rescue (new, and verified).** The obstruction is *per-code*, not global.
Define `C` to be Galois-invariant if `σ_{2s}(C) = C`. Then:

* (proved) if the Gram matrix of `C` w.r.t. `b_s` is `σ_s`-Hermitian, then `σ_{2s}(C) = C`;
* (verified, converse) the two families **coincide as sets** in all four parameter sets:
  35 = 35 at `q = 8` (both `s`), 6 = 6 at `q = 27` (both `s`), and all codes in the two
  reflexive cases.
* These counts are predicted without any computation by **Galois descent**: at `q = 8`,
  `n = 3`, `B = F_8 × F_64`, and `σ_{2s} = Frob²` has fixed field `F_2` on `F_8` and
  `F_4` on `F_64`, giving `(1+3+1) × (1+5+1) = 5 × 7 = 35`; at `q = 27`, `n = 1`, the
  fixed field is `F_3` and the count is `1+4+1 = 6`. Both match exactly.

So in Regime 1 one may still do CSS — **on the 35 (resp. 6) Galois-invariant codes**,
where every obstruction disappears.

**Verdict.** Regime 2 for the general CSS theorem; Regime 1 admissible only on
Galois-invariant codes, with the restriction stated in the hypothesis.

### 3.5 EAQECC construction

The entanglement parameter is `c = dim C − dim Hull_s(C)`.

* Both regimes: `c` is well defined, and by the isometry lemma the pair
  `(|C|, dim Hull_s(C))` — hence `c` — is **identical** for `C` and for `C^{⊥⊥}`.
* Reflexive: the standard symplectic/commutation-matrix derivation applies (the
  commutation matrix is symmetric by §3.4).
* General: the *number* `c` is unchanged, but the derivation of
  `[[n, n − 2k + c, d; c]]` via the rank of the commutation matrix presupposes a
  symmetric (or alternating) `F_p`-form. With `T` not symmetric (138/300), the canonical
  symplectic decomposition used in the standard proof is not available; a direct counting
  derivation (stabilizer group order, coset counting) would still work but has not been
  written.

**Verdict.** Same as CSS: Regime 2 for the theorem; Regime 1 only on Galois-invariant
codes or with a bespoke counting proof.

### 3.6 Quantum parameter derivations (summary)

| Derivation style | Reflexive | General |
|---|---|---|
| via `C^{⊥⊥} = C` and Gram–Schmidt over the commutation form | available | **not available** (form not symmetric; `C^{⊥⊥} ≠ C`) |
| via direct counting (orders of stabilizer/centralizer, coset index) | available | available in principle — **must be written explicitly** |
| MacWilliams identities for the θ_s-dual | expected (Szabo–Wood), **hypotheses to be checked** (O7) | **unknown** — must not be claimed |

---

## 4. Recommendation

**Option (3): hybrid.**

1. **Primary regime for the quantum sections (§7): reflexive, `r ∣ 2s`.**
   Concretely: `q = p^{2e}` with `s = r/2` (the Galois–Hermitian case:
   `q = 4, s = 1`; `q = 9, s = 1`; `q = 16, s = 2`; `q = 25, s = 1`), plus the
   Euclidean baseline `s ≡ 0` for every `q` as a control. State `r ∣ 2s` in the
   hypotheses of every symmetry-dependent theorem, not in a remark.
2. **Retain all general-`s` results as companion theorems** (they are proved and cost
   nothing): the twisted double dual, the size formula, cyclicity, hull closure, the
   isometry lemma, and the parameter-invariance corollary. Present them as "for all `s`".
3. **Admit the non-reflexive regime only through the Galois-invariant sub-family**
   (`σ_{2s}(C) = C`), where the full reflexive toolkit applies per-code. Keep `q = 8` and
   `q = 27` in the paper as (a) the demonstration that reflexivity can fail (35/737, 6/30)
   and (b) the demonstration that the failure is completely explained by Galois descent.
4. **Standing hypothesis `r ≥ 2`** (at `r = 1` there is no Galois action). Say it in §1.

### Why this and not the alternatives

| | (1) general only | (2) reflexive only | **(3) hybrid** |
|---|---|---|---|
| CSS/EA derivations | must be reinvented; two obstructions | standard | standard (primary), plus a clean per-code extension |
| novelty of the `r ∣ 2s` phenomenon | the phenomenon is the *main* result, but no quantum payoff | the phenomenon appears only as a restriction | the phenomenon is both explained (descent) and exploited |
| risk | high (O2 grows) | low | low |
| amount of material | largest | smallest | largest that is safe |
| fits the existing data | yes | yes | yes |
| what is lost | — | the `q=8`/`q=27` story and the LCD-rich regime | nothing |

### Concrete consequences for the parameter tables

* headline families: `q = 4 (s=1)`, `q = 9 (s=1)`, `q = 16 (s=2)`, `q = 25 (s=1)`;
* control/baseline: the same `q` with `s = 0`;
* counterexamples: `q = 8 (s=1,2)`, `q = 27 (s=1,2)` — with the descent counts 35 and 6;
* `m = 2` throughout (`m ≥ 2` is required for the reflexivity criterion to bite);
* `t = 1` for the quantum families (the Gray map T-012 is open, and `t = 2` has only the
  single 33-code census);
* keep `q = 2` out of every Galois table (`r = 1`).

---

## 5. Open items created by this recommendation

| # | Item | Status |
|---|---|---|
| 1 | Converse "reflexive ⇒ `σ_s`-Hermitian Gram": verified 1 254/1 254, **not proved** | to prove or to state as computational |
| 2 | `dim Hull(C^⊥) = dim Hull(C)`: verified 1 254/1 254, **not proved** | to prove or to state as computational (it is what makes LCD regime-independent) |
| 3 | Galois-descent counts (35, 6): derived here heuristically; formalise as a lemma | to write |
| 4 | MacWilliams identities in the non-reflexive regime (O7) | blocked on the Szabo–Wood hypothesis check |
| 5 | A direct-counting EA parameter formula (if the researcher wants Regime 1 in full) | not written |

---

## 6. What the researcher is asked to decide

☐ **(1)** general non-trivial Galois regime as the primary setting;
☐ **(2)** reflexive regime `r ∣ 2s` as the primary setting;
☐ **(3)** hybrid: reflexive primary (`s ≡ 0` or `r` even with `s = r/2`), general-`s`
theorems retained as companions, non-reflexive regime limited to `σ_{2s}`-invariant
codes — **the audit's recommendation**;
☐ other: ____________________

and, if (3): whether the `q = 8` / `q = 27` material is presented as a section of its own
(recommended) or folded into a remark.
