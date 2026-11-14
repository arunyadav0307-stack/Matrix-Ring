# Nontrivial Galois Automorphism and a Valid Non-Degenerate Pairing
## Complete experimental record — Task 1 of the Phase-0 revision

**Status:** COMPLETE — code runs, logs attached, every number below is copied from a
log produced by the committed script.
**Date of the recorded run:** 2026-11-04 (see timestamps inside each log).
**Environment:** Python 3.11.2, standard library only, exact arithmetic (`int`/tuple),
no randomness except where explicitly labelled.
**Reading rule:** `[EXH]` = exhaustive over the whole stated class, `[BND]` = exhaustive
over a bounded class, `[SMP]` = sampled, `[PRF]` = proved (see
`03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`), `[EST]` = established in the literature.

---

### 0. Artifacts

| File | Contents |
|---|---|
| `04_COMPUTATION/matrix_ring_lib.py` | exact-arithmetic library: finite fields, `F_q[u]/<u^t>`, `M_m(A)`, `R^n`, pairings, duals, hulls |
| `04_COMPUTATION/galois_duality_experiments.py` | **Task-1 driver** (`full` = all six parameter sets) |
| `04_COMPUTATION/galois_experiments_log.txt` | its log |
| `04_COMPUTATION/galois_t2_check.py` | **t = 2 extension** (non-field local alphabet) |
| `04_COMPUTATION/galois_t2_log.txt` | its log |

Reproduce with

```bash
cd 04_COMPUTATION
python3 -u galois_duality_experiments.py full     # -> galois_experiments_log.txt
python3 -u galois_t2_check.py                     # -> galois_t2_log.txt
```

---

### 1. The objects, stated exactly

Throughout, `p` prime, `q = p^r`, `A = F_q[u]/<u^t>` (so `A = F_q` when `t = 1`),
`R = M_m(A)`, and `R_n = R[X]/<X^n - 1>` with `X` **central**.

* **Code** = right ideal of `R_n`, i.e. an `R`-submodule of `R^n` closed under the
  cyclic shift (equivalently: an `R_n`-submodule of the right module `R_n`). **Not**
  two-sided.
* `sigma_s(a) = a^(p^s)` applied **entrywise** to the `F_q`-coefficients of an element of
  `A` (so `u` is fixed). `sigma_s` is a ring automorphism of `A` and of `R`
  `[PRF: Lemma 1.1, 1.2]`; it is the identity **iff** `r | s` `[PRF: Lemma 1.2]`.
* `theta_s = sigma_s o transpose` — an **anti**-automorphism of `R`
  `[PRF: Thm 1.3]`; `theta_s^2 = sigma_{2s}` `[PRF: Thm 1.4]`, so `theta_s` is an
  involution **iff** `r | 2s`.
* `lambda(a_0 + a_1 u + ... ) = a_{t-1}`, `Lambda = lambda o tr`.
* Pairings on `R^n`:

  | name | formula | status |
  |---|---|---|
  | **Galois (twisted) pairing** | `<x,y>_s = sum_i theta_s(x_i) y_i` | the proposal |
  | plain product | `sum_i x_i y_i` | classical commutative choice — **fails here** |
* `C^(perp_s) = { y : <x,y>_s = 0 for all x in C }`; `Hull_s(C) = C ∩ C^(perp_s)`.

---

### 2. What was tested, and how strongly

For every code `C` in every parameter set the script checks, on the nose:

1. `C` is a right `R`-submodule of `R^n`; `C` is closed under the cyclic shift;
2. `C^(perp_s)` is a right `R`-submodule and is closed under the shift;
3. `|C| · |C^(perp_s)| = |R|^n` (equivalently `dim_Fq C + dim_Fq C^(perp_s) = n·m²·t`);
4. `Hull_s(C)` is a right `R`-submodule and is closed under the shift;
5. `(C^(perp_s))^(perp_s) = sigma_{2s}(C)` — the **general** double-dual formula;
6. `(C^(perp_s))^(perp_s) = C` — **reflexivity** of the duality (the property that
   makes `C ↦ C^(perp_s)` a Galois *duality* in the classical sense).

**Enumeration.** Brute force over `R^n` is impossible: `|R^n| = (q^{m²t})^n`, e.g.
`16³ = 4096` at the smallest interesting case but `2.8·10^14` at `q = 9, m = 2, n = 4`.
Every code was therefore produced **algebraically** through the chain

```
right ideals of R_n  <--CRT-->  products of right ideals of R[X]/<f_j>
                     <--Morita->  submodules of  B^m ,  B = product of fields
```

and the submodules of `B^m` are enumerated by closing the set of cyclic submodules under
sums (this is complete because every submodule is a sum of cyclic ones). `[EXH]`

**Independent cross-check.** For the two smallest cases (`q = 2, m = 2, n = 1, 3`) the
same code list was also produced by a completely different method — closure of the whole
subspace lattice under the shift and under right multiplication — and the two lists
agree exactly (`agreement = True`, `5 = 5` and `35 = 35`). `[EXH]` This validates the
Morita/CRT enumerator.

**Completeness labels.** `q = 4 (n=3)`, `q = 8 (n=3, s = 1,2)`, `q = 9 (n=2)` and the
`t = 2` run are **[EXH]** — every code in the class. `q = 9, m = 2, n = 4` has
`20736` codes; **1200 of them were sampled** (seed `13572468`) — **[SMP]**, not
exhaustive. The `q = 2` runs are enumeration validation only; see §3.5.

---

### 3. Results

#### 3.1 Parameter sets

| # | q | r | m | t | n | s | #codes | completeness |
|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 2 | 2 | 1 | 3 | 1 | 343 = 7³ | **[EXH]** |
| 2 | 8 | 3 | 2 | 1 | 3 | 1, 2 | 737 = 11·67 | **[EXH]** (both s) |
| 3 | 9 | 2 | 2 | 1 | 2 | 1 | 144 = 12² | **[EXH]** |
| 4 | 9 | 2 | 2 | 1 | 4 | 1 | 20736 total, **1200 tested** | **[SMP]** (seed 13572468) |
| 5 | 4 | 2 | 2 | **2** | 1 | 1 | 32 | **[EXH]** (`galois_t2_check.py`) |
| 6 | 2 | 1 | 2 | 1 | 1 / 3 | 0 | 5 / 35 | **[EXH]** — enumeration validation only |

#### 3.2 `sigma_s` (log, part A)

| q | s | additive | multiplicative | nontrivial | witness | order |
|---|---|---|---|---|---|---|
| 4 | 1 | True | True | **True** | `a = 2 → 3` | 2 = r/gcd(r,s) |
| 8 | 1 | True | True | **True** | `a = 2 → 4` | 3 = r/gcd(r,s) |
| 8 | 2 | True | True | **True** | `a = 2 → 7` | 3 = r/gcd(r,s) |
| 9 | 1 | True | True | **True** | `a = 3 → 7` | 2 = r/gcd(r,s) |
| 2 | 0 | True | True | **False** (no element moves) | — | 1 |

#### 3.3 `theta_s` (log, part B) — the "no unproved involution" discipline

| q | s | additive | anti-multiplicative | `theta_s² = sigma_{2s}` | involution? (`r | 2s`) |
|---|---|---|---|---|---|
| 4 | 1 | True | True | True | **True** (`2s mod r = 0`) |
| 8 | 1 | True | True | True | **False** (`2s mod r = 2`) |
| 8 | 2 | True | True | True | **False** (`2s mod r = 1`) |
| 9 | 1 | True | True | True | **True** (`2s mod r = 0`) |
| 4 (t = 2) | 1 | True | True | True | **True** — verified on all 65536 matrices |

`theta_s` is **never** called an involution without the check `r | 2s`. At `q = 8`
(`r = 3`) it is *not* one, for either `s = 1` or `s = 2` — a case a careless
"Frobenius is an involution" claim would have missed.

#### 3.4 `Lambda` (log, part C)

`Lambda(X) = lambda(tr(X))`, `lambda` = coefficient of `u^{t-1}`:

* `R`-valued Gram matrix of `(X,Y) ↦ Lambda(XY)` has **full rank**
  (`4/4` at `q = 4, 8, 9`, and `8/8` at `t = 2` where `dim_Fq R = 8`) ⇒ `Lambda` is
  non-degenerate;
* `Lambda(XY) = Lambda(YX)` and `Lambda(X E_{j0,i0}) = X_{i0,j0} ≠ 0` (ideal-catching)
  verified constructively.

#### 3.5 Per-code results (log, part E)

| parameter set | right module | shift-closed | dual right module | dual shift-closed | size formula | hull right module | hull shift-closed | double-dual formula | **reflexivity** | plain size formula |
|---|---|---|---|---|---|---|---|---|---|---|
| q=4, n=3, s=1 (343) | 343 | 343 | 343 | 343 | 343 | 343 | 343 | 343 | **343/343** | 8/343 |
| q=8, n=3, s=1 (737) | 737 | 737 | 737 | 737 | 737 | 737 | 737 | 737 | **35/737** | 4/737 |
| q=8, n=3, s=2 (737) | 737 | 737 | 737 | 737 | 737 | 737 | 737 | 737 | **35/737** | 4/737 |
| q=9, n=2, s=1 (144) | 144 | 144 | 144 | 144 | 144 | 144 | 144 | 144 | **144/144** | 4/144 |
| q=9, n=4, s=1 (1200 sampled) | 1200 | 1200 | 1200 | 1200 | 1200 | 1200 | 1200 | 1200 | **1200/1200** | 2/1200 |
| q=4, t=2, n=1, s=1 (32) | 32 | — (n=1) | 32 | — | 32 | 32 | — | 32 | **32/32** | 2/32 |
| q=2, n=1, s=0 (5) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5/5 | 2/5 |
| q=2, n=3, s=0 (35) | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35/35 | 4/35 |

**Reading of the last two rows.** At `q = 2` (`r = 1`) `sigma_0` is the identity, so
these runs say **nothing** about Galois duality; they are included only because the
lattice-closure cross-check is affordable there and confirms the enumerator
(`agreement = True`). Per standing instruction, they are **not** used as evidence of
nontrivial Galois duality anywhere in this project.

#### 3.6 The decisive finding: reflexivity holds exactly when `r | 2s`

`q = 4` (`r = 2`, `s = 1`): `2s = 2 ≡ 0 (mod 2)` → reflexivity **343/343**.
`q = 9` (`r = 2`, `s = 1`): → **144/144** and **1200/1200** (sampled).
`q = 8` (`r = 3`, `s = 1` or `2`): `2s ≡ 2` or `1 (mod 3)` → reflexivity **35/737**.

This is not a numerical accident; it is exactly the prediction
`(C^(perp_s))^(perp_s) = sigma_{2s}(C)` `[PRF: Thm 3.8]`, which itself holds in
**100 %** of the cases in every row of §3.5. When `sigma_{2s} ≠ id`, most codes fail
`C = (C^(perp_s))^(perp_s)`. Explicit witness at `q = 8, m = 2, n = 3, s = 1`, code #3:

```
C                    = [(1,0,0,0,1,0,2,0,0,0,2,0), (0,1,0,0,0,1,0,2,0,0,0,2),
                        (0,0,1,0,6,0,0,0,6,0,1,0), (0,0,0,1,0,6,0,0,0,6,0,1)]
(C^(perp_s))^(perp_s)= [(1,0,0,0,1,0,7,0,0,0,7,0), (0,1,0,0,0,1,0,7,0,0,0,7),
                        (0,0,1,0,5,0,0,0,5,0,1,0), (0,0,0,1,0,5,0,0,0,5,0,1)]
```

(entries are `F_8`-elements; `2 ↦ 7` and `6 ↦ 5` are `sigma_2 = sigma_{2s}`).

**Design consequence.** To get a *reflexive* Galois duality in this family one must take
`r` even and `s = r/2` (e.g. `q = p^{2e}`, `s = e`), i.e. `theta_s` of order 2. No
nontrivial reflexive choice exists at `q = 8` (`r = 3`): both `s = 1` and `s = 2` fail.
This is now a *design constraint of the project*, recorded in §8 of the revision report.

#### 3.7 The plain product pairing fails

The classical commutative choice `<x,y> = Σ x_i y_i` produces a dual that is both a left
and a right module (`343/343`, `737/737`, ...) but destroys the size formula:

| parameter set | plain size formula holds |
|---|---|
| q=4, n=3 | 8/343 |
| q=8, n=3 (s=1 and s=2) | 4/737 |
| q=9, n=2 | 4/144 |
| q=9, n=4 (sampled) | 2/1200 |
| q=4, t=2, n=1 | 2/32 |

*Why* it fails is shown by a tiny counterexample `[PRF: §5]`: in `R = M_2(F_2)` with
`n = 1`, `C = uR` (recall `A = F_4 ⊕ uF_4`, `u = 1 + i`), one gets
`|C|·|C^⊥| = 4 ≠ 16 = |R|`. The obstruction is structural: `y ↦ (x ↦ Σ x_i y_i)` is
`R`-linear from the *right* module `R^n` into `Hom_R(R^n, R)` in the wrong variance —
the plain product is perfect for **left** ideals and broken for **right** ideals
(verified `31/35` failures in the original E4 experiment).

#### 3.8 Hull data (for later phases)

`q = 4, m = 2, n = 3, s = 1`: hull `F_q`-dimension distribution over the 343 codes —
`dim 0: 64, dim 2: 144, dim 4: 108, dim 6: 27`.
`q = 8, m = 2, n = 3, s = 1`: `dim 0: 640, dim 2: 64, dim 4: 30, dim 6: 3`.
So LCD codes (`Hull = 0`) are plentiful, and self-orthogonal codes exist — the raw
material a hull-based quantum construction needs — but no quantum claim is made here.

---

### 4. What is proved, and what the experiments add

* Proved in `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`: `sigma_s ∈ Aut(R)` and
  `sigma_s = id ⟺ r | s`; `theta_s` anti-automorphism; `theta_s² = sigma_{2s}`
  (involution ⟺ `r | 2s`); `Lambda` symmetric, non-degenerate, ideal-catching;
  additivity, right-`R`-linearity in `y`, `theta_s`-semilinearity in `x`;
  non-degeneracy and the bijection onto `Hom_R(R^n_R, R_R)`; dual of any subset is a
  right module; dual of a cyclic code is cyclic; `|C|·|C^(perp_s)| = |R|^n` for right
  submodules; double dual `= sigma_{2s}(C)`; hull is a right module and cyclic;
  the `R`-valued and `Lambda`-valued duals coincide.
* The experiments do **not** replace those proofs; they (a) confirm them independently on
  seven runs (six in the main sweep, two of which are the `q = 2` validation cases, plus the `t = 2` run), (b) quantify the reflexivity
  threshold, which is a *design* question the proofs settle in the form
  "`sigma_{2s}` vs `id`" but whose practical impact ("how many codes break") only
  computation shows, and (c) exhibit explicit witnesses.

---

### 5. Limitations and explicit non-claims

1. `q = 2` (`r = 1`) gives the trivial Frobenius; nothing in this project rests on it.
2. `q = 9, m = 2, n = 4` is **sampled** (1200 of 20736), not exhaustive.
3. The `t = 2` run covers `n = 1` only (`|R^n| = 65536` was already at the edge of what
   the Morita enumeration allows cheaply). The proofs are uniform in `t`; extending the
   computation to `t = 2, n ≥ 2` is open work.
4. Cheap sanity runs at `t = 1, n = 1` would be vacuous for the shift; none is claimed.
5. `theta_s` anti-multiplicativity at `t = 2` was checked on 5000 uniformly random pairs
   (seed 20261104) plus all basis sums — **sampled**, because `|M_2(A)| = 65536` makes
   an all-pairs check `4·10^9` operations. `theta_1² = id` *was* checked on all 65536
   matrices. At `t = 1` the corresponding checks are on 300 random matrices (`[SMP]`).
6. No quantum code, no Gray map, no minimum distance, and no hull-dimension formula is
   claimed or tested here.
7. The independent "lattice closure" cross-check is skipped whenever
   `|R_n| = (q^{m²t})^n` exceeds 20000, so it only runs for the two `q = 2` cases
   (where it agrees). The `q = 4, 8, 9` code lists therefore rest on the Morita/CRT
   enumerator alone — validated, but not doubly validated, at those parameters.
