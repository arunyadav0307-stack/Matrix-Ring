# Phase 0 — Computational Audit

All runs below were executed in this session on the working branch, from
`/home/user/Matrix-Ring/04_COMPUTATION/`. Timings are wall-clock.

---

## 1. Supplied scripts: reproducibility

| Script | Command | Exit | Time | Science identical to committed log? |
|---|---|---|---|---|
| `galois_duality_experiments.py` | `python3 -u galois_duality_experiments.py full` | 0 | ~30 s | **yes** — `diff` shows only `run:` timestamp and `[elapsed]` lines |
| `alahmadi_reconciliation.py` | `python3 -u alahmadi_reconciliation.py` | 0 | ~9 s | **yes** — same, only timestamp/elapsed |
| `galois_t2_check.py` | `python3 -u galois_t2_check.py` | 0 | <1 s | **no** — count changed 32 → 33 by design (§3) |

The supplied science is reproducible byte-for-byte apart from the t = 2 census, which
changed because a bug was fixed.

---

## 2. Independent implementation

`independent_audit_checks.py` (~600 lines, **no import of `matrix_ring_lib`**): own
`Field(p, r)` (descending search for an irreducible), own `rref` / `nullspace` /
`row-space basis` / `in_span` / `rank`, own `Local(F, t) = F_q[u]/⟨u^t⟩`, own
`MatRing(A, m)`, own `Ambient(R, n)`, own enumeration by brute-force subspace filtering
and by direct lattice closure. Sections A–E:

| Section | Content | Result |
|---|---|---|
| A | σ_s / θ_s laws, exhaustively where affordable | q = 4: all 256² pairs — σ_1 additive ✓ multiplicative ✓; θ_1 anti-multiplicative ✓; θ² = σ_{2s} on all 256 elements ✓; σ_{2s} = id ✓. q = 8 (4 000 sampled pairs): σ_1, σ_2, θ_1, θ_2 all ✓, θ² = σ_{2s} ✓, **σ_{2s} = id ✗**. q = 9: all ✓ |
| B | Non-degeneracy by own elimination | Gram rank of `(X,Y) ↦ Λ(XY)`: **4/4** (t=1, m=2), **8/8** (t=2). Gram rank of the θ_s-form: full for **every** tested `(q,t,n,s)` |
| C | Enumeration | right ideals of `M_2(F_q)`: q = 2,4,8,9 → **5, 7, 11, 12** = `q+3`, dims `[(0,1),(2,q+1),(4,1)]`. t = 2 (`A = F_q[u]/⟨u²⟩`, m = 2): **33**, dims `[(0,1),(2,5),(4,21),(6,5),(8,1)]`. Cyclic codes: `q=4,n=3 → 343`; `q=9,n=2 → 144`; `q=2,n=3 → 35` (direct scan of all 4 096 ambient vectors); **`q=4,n=2 → 33`** (squarefree formula would say 49) |
| D | Duality, hull, reflexivity on independently enumerated codes | see table below |
| E | 14 prediction/observation pairs | all OK after three corrections (see §4) |

Run: `python3 -u independent_audit_checks.py` → **EXIT=0, 12.0 s,
`ALL PREDICTIONS CONFIRMED: True`**; log `independent_audit_log.txt`.

### Section D — per-code checks

| Parameter set | #codes | right module | size formula | dual right | hull right | double-dual `=σ_{2s}(C)` | reflexive |
|---|---|---|---|---|---|---|---|
| q=4, n=1, s=1 | 7 | 7/7 | 7/7 | 7/7 | 7/7 | **7/7** | 7/7 |
| q=8, n=1, s=1 | 11 | 11/11 | 11/11 | 11/11 | 11/11 | **11/11** | **5/11** |
| q=8, n=1, s=2 | 11 | 11/11 | 11/11 | 11/11 | 11/11 | **11/11** | **5/11** |
| q=9, n=1, s=1 | 12 | 12/12 | 12/12 | 12/12 | 12/12 | **12/12** | 12/12 |
| q=4, t=2, s=1 | 33 | 33/33 | 33/33 | 33/33 | 33/33 | **33/33** | 33/33 |
| q=2, n=3, s=0 | 35 | 35/35 | 35/35 | 35/35 | 35/35 | **35/35** | 35/35 |

Plain-product control (no θ): the size formula succeeds only **2/7, 2/11, 2/12, 3/33,
4/35** — the θ_s twist is what makes the duality work, and the plain product is
demonstrably not a substitute.

---

## 3. Bug found in supplied code (F-03): `galois_t2_check.py` ⇒ 32 → 33

**Symptom.** The census of right ideals of `M_2(F_q[u]/⟨u²⟩)` (i.e. `A`-submodules of
`A²`, `A = F_4[u]/⟨u²⟩`) returned **32**, and the reported `F_q`-dimension distribution
started at dim 2 — the zero code was missing.

**Cause.** The enumerator built `seen` only from non-zero vectors (`if not any(flat(v)):
continue`) and never seeded `seen` with the zero subspace, so the zero submodule was
never in the lattice.

**Fix.** `seen = {tuple(): []}` (with an explanatory comment) in `galois_t2_check.py`.

**After the fix.** `#right ideals = 33`; `F_q`-dim distribution
`[(0,1), (2,5), (4,21), (6,5), (8,1)]`; and **33/33** on every per-code check
(right module, dual right module, size formula, hull right module, double-dual =
σ_{2s}(C), reflexivity). Previously reflexivity read 31/32 and the size formula 32/32.

**Independent confirmation that 33 is the right number** (structural, not computational):
right ideals ↔ `A`-submodules `W ⊆ A²`; counting them gives
`1 + (q+1) + (q²+q+1) + (q+1) + 1 = q² + 3q + 5`, i.e. **33** for `q = 4` (details in
`PHASE0_PROOF_VERIFICATION.md` §11). The same count reappears, from a completely
different direction, as the `q = 4, n = 2` repeated-root cyclic-code census (§2.C) —
two independent derivations of the same 33.

**Action.** Every document quoting "32 right ideals" or "32/32" for t = 2 must be
corrected (F-09). The register has been corrected in this audit.

---

## 4. Bugs in my own independent script (and their lessons)

1. `add` / `mul` / `inv` were used as subscriptable tables instead of methods
   (`A.add[x][y]` → `A.add(x,y)`).
2. `Ambient.hull` and `check_list` mixed two representations (`R`-elements vs
   `F_q`-coordinate vectors).
3. **My D2 reconstruction used the wrong vector-coordinate order**: `MatRing.vec` is
   `vv[(i*m + j)*t + l] = w[i*t + l]`, not `vv[l*4 + i*2 + j]`. The wrong order produced
   spurious "3/33" failures on the right-module and size-formula checks — i.e. a
   *false positive* defect report, which is exactly the failure mode an audit must
   guard against. Once fixed, everything passed.
4. The hull must be computed as the nullspace of the Gram matrix
   `G[j][i] = β(c_j, c_i)`, **not** as the span of those basis vectors of `C` that happen
   to lie in `C^⊥`. (The same trap was hit and fixed in `u8_n3_selfdual_check.py`.)

Lessons carried into the register: any future hull computation must use the
Gram/nullspace method, and any "counterexample" found by a new script must be reproduced
by a second method before it is believed.

---

## 5. New scripts written for this audit

| Script | Purpose | Runtime | Log |
|---|---|---|---|
| `independent_audit_checks.py` | from-scratch re-implementation + sections A–E | 12.0 s | `independent_audit_log.txt` |
| `audit_pairing_equivalence.py` | trace-valued vs matrix-valued dual; σ_{2s}-isometry (E1–E6); double-dual and reflexivity **on the supplied code paths**; 4 parameter sets | 86 s | `audit_pairing_equivalence_log.txt` |
| `u8_n3_selfdual_check.py` | `n = 3`, `A = M_2(F_2)`: both code conventions, both bilinear forms, hulls, self-orthogonal / self-dual censuses | 8 s | `u8_n3_selfdual_log.txt` |

### 5.1 `audit_pairing_equivalence.py` (used the **supplied** `pair_theta` and
**supplied** `enumerate_ideals_morita`)

| | q=4, n=3 (343) | q=8, n=3 (737) | q=9, n=2 (144) | q=9, n=4 (5 000) |
|---|---|---|---|---|
| trace dual = matrix dual | 343/343 | 737/737 (s=1), 737/737 (s=2) | 144/144 | 5000/5000 |
| size formula (both) | 343/343 | 737/737 | 144/144 | 5000/5000 |
| (E1) `B_s(σ_kx,σ_ky)=σ_kB_s(x,y)` | 300/300 | 300/300 | 300/300 | 300/300 |
| (E2) `B_s=0` preserved | 300/300 | 300/300 | 300/300 | 300/300 |
| (E3) weight preserved | 300/300 | 300/300 | 300/300 | 300/300 |
| (E4) `σ_k(C^⊥)=(σ_kC)^⊥` | 343/343 | 737/737 | 144/144 | 5000/5000 |
| (E5) `Hull(σ_kC)=σ_kHull(C)` | 343/343 | 737/737 | 144/144 | 5000/5000 |
| (E6) `(C^⊥)^⊥=σ_{2s}(C)` | **343/343** | **737/737** | **144/144** | **5000/5000** |
| reflexive | **343/343** | **35/737** | **144/144** | **5000/5000** |

Note the abort at `q = 8, n = 2`: the Morita enumerator raises
`X^n-1 is not squarefree`. In characteristic 2 this forces **odd n** for any future
Morita-based run (F-10).

### 5.2 `u8_n3_selfdual_check.py` (`n = 3`, `A = M_2(F_2)`)

**Family (I) — right ideals (`R_3 = A[X]/⟨X³−1⟩`).** 35 codes (4 096 ambient vectors
scanned). The CRT+Morita prediction `R_3 ≅ M_2(F_2) × M_2(F_4)` ⇒ `5 × 7 = 35` with
`F_2`-dimensions `2v_1 + 4v_2` predicts the distribution
`[(0,1),(2,3),(4,6),(6,15),(8,6),(10,3),(12,1)]`; the enumeration reproduces it
**exactly** (`MATCH: True`) — a structural, independent confirmation of the enumerator.

Form `β = Σ_j tr(x_j^T y_j)` (this **is** the Phase-0 Galois form at s = 0, since
`θ_0` = transpose): `dim C + dim C^⊥ = 12` for **35/35**; hull-dim distribution
`[(0,16),(2,4),(4,12),(6,3)]` — which **coincides exactly** with the `galois_experiments_log`
entry for `q=2, n=3`, and yields **3 self-dual codes** (dim 6), matching
`alahmadi_reconciliation_log.txt` §5 (`C = C^perp with the form sum x_j^T y_j : 3 codes`).
The three codes are listed explicitly as words of length 3 over `M_2(F_2)` in the log.

Form `β = Σ_j tr(x_j y_j)` (no transpose): size formula 35/35, but hull dims
`[(0,4),(1,6),(2,10),(3,15)]`, **0** self-dual codes.

**Family (II) — quaternary convention** (`F_4 = ⟨I, ω⟩ ⊂ A`, generators = monic divisors
of `X³−1` over `F_4`): **8** generators (`X³−1 = (X+1)(X+ω)(X+ω²)` over `F_4`), giving
codes of dimensions `0, 4, 4, 4, 8, 8, 8, 12`. **No non-zero self-orthogonal code and no
self-dual code** under either form: half-dimension is 6 and `dim = 4(3 − deg g) ∈
{0,4,8,12}`. (The zero code — `g = X³−1` — is trivially self-orthogonal; it was not
generated by the probe because of a truncation in the word construction, so the run lists
7 of the 8 explicitly plus the whole-space code twice.)

**Why this matters (F-07).** Alahmadi et al.'s "Euclidean" form is `Σ_j x_j y_j`
(**matrix product**, no transpose). `alahmadi_reconciliation_log.txt` §5 shows
`dim C + dim C^⊥` is **not** constant for it (`[(6,15),(8,10),(10,6),(12,4)]`) and it
admits **0** self-dual codes; their Lemma 4 matches only 3/9 (their form) versus 5/9
(transpose form) on the 9 "genuine" triples. Any manuscript comparison must state which
form is meant.

---

## 6. What is **not** yet verified computationally

1. `t ≥ 3` (`F_q[u]/⟨u³⟩`) — never run; the t = 2 structural derivation suggests the
   submodule lattices get richer, so the "same behaviour" claim at t = 2 should not be
   extrapolated.
2. `m ≥ 3` — all runs are `m = 2`. The reflexivity criterion needs `m ≥ 2` and the
   enumeration formula is `m`-dependent; `m = 3` would be a cheap, high-value check.
3. `n` even in characteristic `p` with `p | n` beyond the single `q = 4, n = 2`
   counterexample.
4. Principality at `t ≥ 2` (never tested; T-021 stays conditional).
5. Weight enumerators / minimum distances of the hulls (no code computes them yet; T-011
   remains open).
6. Anything at `q = 8` with `n` even (enumerator restriction, F-10).
7. The `q = 9, n = 4` census is **sampled** (5 000 codes), not exhaustive — it must
   always be labelled `[SMP]`.
