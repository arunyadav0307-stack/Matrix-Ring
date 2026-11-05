# Computation: updated scripts, logs and reproducibility notes
## (Part 5 of the Phase-0 revision deliverables)

Everything below is **runnable source code plus its exact output**. No computational
result in this project is asserted without a script that produced it and a log that
records it.

**Environment.** Python **3.11.2**, standard library only (`itertools`, `random`).
Exact integer/tuple arithmetic throughout — no floats, no external packages.
All runs dated **2026-11-04**; timestamps are inside each log.

---

## 1. File inventory

| File | Lines | Purpose | Run time |
|---|---|---|---|
| `matrix_ring_lib.py` | 716 | exact-arithmetic library: `FiniteField`, `LocalRing` ($A_t=\mathbb F_q[u]/\langle u^t\rangle$), `MatrixRing`, `Ambient` ($R^n$), pairings, duals, hulls, linear algebra over $\mathbb F_q$ | (library) |
| `phase0_feasibility.py` | 605 | original Phase-0 driver, experiments **E1–E5** | 18.8 s |
| `galois_duality_experiments.py` | ~700 | **Task 1**: nontrivial Galois automorphisms + pairing, 6 parameter sets | ≈ 4 s |
| `galois_t2_check.py` | 262 | **Task 1 extension**: the same checks at $t=2$ (non-field local alphabet) | ≈ 1 s |
| `alahmadi_reconciliation.py` | ~520 | **Task 3**: direct code verification of Alahmadi–Sboui–Solé–Yemen (A1) | ≈ 11 s |
| `phase0_results.txt`, `phase0_stdout.txt` | 246 | log of E1–E5 (run 2026-11-04 03:52:42) | — |
| `galois_experiments_log.txt` | ~246 | log of `galois_duality_experiments.py full` | — |
| `galois_t2_log.txt` | ~35 | log of `galois_t2_check.py` | — |
| `alahmadi_reconciliation_log.txt` | 487+ | log of the reconciliation script | — |
| `README.md` | — | reproducibility notes for the original runs | — |
| `phase2_stage2a_morita_checks.py` | 1566 | **Phase 2, Stage 2A**: the Morita correspondence (both directions, lattice operations, left/two-sided ideals, Stage-1 dictionary), the identity `μ_S(I_W) = ⌈μ_B(W)/2⌉` via L-2.3a/b/c, the individual principality criterion, and the projectivity counterexample (see §9) | ≈ 285 s |
| `phase2_stage2a_morita_log.txt` | 699 | log of the Stage-2A script: **429 / 429 checks PASS** (391 `[EXH]`, 38 `[SMP]`) | — |
| `phase2_stage1_shift_checks.py` | 1001 | **Phase 2, Stage 1**: definitions and shift structure — $\iota$, cyclic convolution, centrality of $X$, $T^n=1$, $T$ as left/right multiplication by $X$, $F_q$- vs $R$-linearity, right ideals $\leftrightarrow$ $T$-invariant right $R$-submodules, $\sigma_k$/$\theta_s$ compatibility (see §8) | ≈ 100 s |
| `phase2_stage1_shift_log.txt` | 734 | log of the Stage-1 script: **553 / 553 checks PASS** (91 `[EXH]`, 462 `[SMP]`), 8 parameter sets | — |

## 2. How to reproduce

```bash
cd 04_COMPUTATION
python3 -u galois_duality_experiments.py full     # -> galois_experiments_log.txt
python3 -u galois_t2_check.py                     # -> galois_t2_log.txt
python3 -u alahmadi_reconciliation.py             # -> alahmadi_reconciliation_log.txt
python3 -u phase0_feasibility.py                  # -> phase0_results.txt (original E1-E5)
python3 -u phase2_stage2a_morita_checks.py        # -> phase2_stage2a_morita_log.txt (Stage 2A)
python3 -u phase2_stage1_shift_checks.py          # -> phase2_stage1_shift_log.txt (Phase 2, Stage 1)
```

All four exit with status **0** and rewrite their own log files. `python3 -u` (unbuffered)
is required to see progress; the scripts themselves are deterministic **except** for the
parts explicitly labelled `[SMP]`, which use fixed seeds (see below).

## 3. Determinism and randomness

| script | deterministic parts | randomised parts (seeded) |
|---|---|---|
| `phase0_feasibility.py` | E2–E5 exhaustive | E1: 400 random trials, seed **12345** |
| `galois_duality_experiments.py` | all enumerations, all per-code checks | `q=9,n=4` sampling: 1200 of 20736 codes, seed **13572468**; $\theta$-anti-multiplicativity sanity: 300 random matrices |
| `galois_t2_check.py` | all 32 codes, all 65536 elements | 5000 random matrix pairs, seed **20261104** |
| `alahmadi_reconciliation.py` | everything (exhaustive scans of 16 and 4096 ambient vectors, all 27 triples) | none |
| `phase2_stage2a_morita_checks.py` | the whole submodule lattice of `B^2` and the whole right-ideal lattice of `S = M_2(B)` at the eleven parameter sets with `|B| ≤ 16` (every object, every statement); the submodule lattice at `(4,1,3)`; all `x ∈ S` for L-2.3a with `k = 1`; all `x ∈ I` for `μ_S = 1`; all pairs where the product is within budget; all 32 endomorphisms in the projectivity counterexample | L-2.3a with `k = 2` and L-2.3c at the largest rings; the Stage-1 dictionary where `|R^n|·#ideals` exceeds the budget (6 ideals); the `(x,a)` right-`R`-submodule pairs above budget; six targeted submodules at `(4,2,2)`; seed **20261105** |
| `phase2_stage1_shift_checks.py` | all checks at $(q,t,n)=(4,1,1)$ and $(9,1,1)$ (incl. all $65\,536$ $(x,a)$ pairs at $(4,1,1)$); all $B$-pairs at $(4,1,2)$; all $65\,536$ vectors for $T=$ right multiplication by $X$ at $(4,1,2)$ and $(4,2,1)$; the whole subspace census at $(4,1,1)$ | everything else: 20 000 sampled $(x,a)$ pairs per parameter set, 500 sampled vectors, seed **20261104** |

## 4. What each script verifies (at a glance)

**`galois_duality_experiments.py`** — for each parameter set:
(A) $\sigma_s$ additive / multiplicative / nontrivial / order;
(B) $\theta_s$ additive / anti-multiplicative / $\theta_s^2=\sigma_{2s}$ / involution?;
(C) $\Lambda$ non-degenerate (Gram rank), symmetric, ideal-catching;
(D) enumeration of all cyclic codes by Morita+CRT, with an independent lattice-closure
cross-check when affordable;
(E) per-code: right module, shift-invariance, dual right module, dual shift-invariance,
$|C||C^{\perp_s}|=|R|^n$, hull right module, hull shift-invariance, double dual
$=\sigma_{2s}(C)$, reflexivity, and the same three checks for the plain product pairing.

**`galois_t2_check.py`** — the same at $t=2$ ($A=\mathbb F_4[u]/\langle u^2\rangle$,
$R=M_2(A)$, $n=1$, $s=1$): 32 right ideals, all properties, plus $\theta_1^2=\mathrm{id}$
on all 65536 elements and the $\Lambda$ Gram rank $8/8$.

**`alahmadi_reconciliation.py`** — (1) rebuilds $A=M_2(\mathbb F_2)$ from the paper's own
$i,\omega,u$ and verifies $i^2=I$, $\omega^2+\omega+I=0$, $i\omega=\omega^2i$, $u^2=0$,
$\omega u\ne u\omega$, and the $a+ub$ multiplication rule on all 256 quadruples;
(2) exhaustive censuses at $n=1$ and $n=3$; (3) Lemma 2 at $n=1$; (4) Theorem 1 under
three readings, with residue/torsion generators and dimension formulas, plus a
Frobenius-invariance test; (5) Euclidean duality, Lemma 4, Theorem 2.

## 5. Known limitations (stated so that nobody over-reads a log)

1. `q=9, m=2, n=4` is **sampled** (1200 / 20736, `[SMP]`).
2. `t=2` is covered only at $n=1$ (ambient $|R^n| = 65536$; the Morita enumeration stays
   cheap but the number of codes grows fast).
3. The independent lattice-closure cross-check is skipped when $|R_n|>20000$, so it runs
   only for the two $q=2$ cases (where it agrees: 5 and 35).
4. $\theta$-anti-multiplicativity is checked on random samples at $t=2$ ($|M_2(A)|=65536$
   makes an all-pairs check $4\cdot10^9$ operations); $\theta^2$ **is** checked on all
   elements.
5. `LocalRing.elements()` and `MatrixRing.elements()` return `itertools.product`
   **generators** — they are consumed by the first loop over them. (This cost us one
   `StopIteration` during development; all current call sites wrap them in `list(...)`.)
6. Dual bases must be **reduced** (`rref`) before being compared. Comparing a raw
   `nullspace` basis against a reduced one produced a spurious "13/32 reflexivity
   failures" at $t=2$; after reducing, the same run gives 32/32. The same class of bug was
   found and fixed earlier in `galois_duality_experiments.py` (spurious 15/343
   double-dual failures at $q=4$). **Any new script must reduce both sides before
   comparing subspaces.**

## 6. Development log of the correction work (audit trail)

| date | issue | fix |
|---|---|---|
| 2026-11-04 | `FiniteField(2,2)`: "no primitive polynomial found" | off-by-one in `_is_primitive`; `r==1` special-cased |
| 2026-11-04 | `test_frobenius_functional` hung ($|R|^2$ loop at $|R|=65536$) | replaced by a Gram-rank test |
| 2026-11-04 | E5 aliasing bug `(f,g,h)[which] = tgt` | explicit `parts` list |
| 2026-11-04 | non-canonical dual basis → spurious double-dual failures (15/343) | `dual_of` returns a reduced (rref) basis |
| 2026-11-04 | $d=1$ $X$-multiplication bug in the $K$-subspace → $\mathbb F_q$-basis expansion | fixed |
| 2026-11-04 | zero code missing from the lattice-closure enumeration (4 vs 5, 34 vs 35) | seed `seen = {key([]): []}` |
| 2026-11-04 | `TypeError: unhashable type: 'list'` in the Lemma-4 lookup (`alahmadi_reconciliation.py`) | keys built with `key3(f,g,h)` of tuples |
| 2026-11-04 | mis-indented `sig`/`store.append` block silently emptied two result tables (`#triples: 0`) | re-indented into the loop body; `#triples` sanity-checked after every run |
| 2026-11-04 | $\sigma_s$ "nontrivial" flag computed from the order formula, printing `nontrivial=True (witness a=None)` at $q=2$ | flag now witness-based: `nontrivial = (wit is not None)` → prints `False` at $q=2$ |
| 2026-11-04 | `A.frobenius(X, 2*s)` with $2s=r$ → `IndexError` | index reduced mod $r$ |
| 2026-11-04 | $t=2$: spurious 13/32 reflexivity failures | reduce both sides before comparing (see §5.6) |
| 2026-11-04 | over-claiming log line "Lemma 2 is FALSE as stated" | replaced by an explicit reading-convention caveat (standing rule: no claim that A1 is wrong) |
| 2026-11-04 | mis-stated column spaces in the Lemma-2 comment (`⟨(1,1)⟩` vs `⟨(1,0)⟩`) | corrected: $uA=\{[[a,b],[a,b]]\}$ has column space $\langle(1,1)\rangle$; the two *missing* ideals have column spaces $\langle(0,1)\rangle,\langle(1,0)\rangle$ |

## 7. Non-claims

* No quantum code, Gray map, minimum distance, or hull-dimension formula is computed
  anywhere in `04_COMPUTATION`.
* The $q=2$ runs are **not** evidence about Galois duality ($\sigma_0=\mathrm{id}$); they
  validate the enumerator only.
* `computational only` results are evidence, not theorems. The theorems live in
  `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` and are proved there for all parameters.

---

## 8. Phase 2 — Stage 1 (added 2026-11-04)

Companion document: `03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md`.
Delivered in commit **`bfb16d7`**; register rows **T-044 … T-068**.
Scope: definitions, the cyclic shift, left/right action conventions, centrality of $X$,
and $\sigma_k$/$\theta_s$ compatibility. **Out of scope (not attempted):** P-2.3
(generator numbers), P-2.4 (CRT/Hensel), P-2.5/P-2.6 (principality), P-2.7/P-2.8 (duals
and annihilators, hence **L-6.1**), P-2.1f (`rev`), C-2.1 (enumeration), manuscript.
CT-0 … CT-6 were **not** run as a suite.

### 8.1 Files

| File | Role |
|---|---|
| `phase2_stage1_shift_checks.py` | 1001 lines. Builds $B=A_t[X]/\langle X^n-1\rangle$ and $M_2(B)$ from scratch, importing only `Field`, `Local`, `MatRing` and the $\mathbb F_q$-linear algebra (`rref`, `enumerate_subspaces`) from `ring_structure_checks.py`. Parts: **0** representation ($\iota$, convolution, $X^n=1$, centrality, $\iota$ bimodule-linearity, operator identities); **1** the shift ($T^n=1$, $T=$ right and left multiplication by $X$, Hamming isometry, $F_q$-linearity, right/left $R$-linearity, right/left $R_n$-linearity, non-central negative controls); **2** the equivalence (both directions, both round trips, three negative controls, exhaustive subspace census at $(4,1,1)$); **3** $\sigma_k$/$\theta_s$ (commutation with $T$, side preservation, side swapping, semilinearity, non-commutation and non-$F_q$-linearity controls, Phase-1 ring-level inputs on $R$); **4** the boundary case $n=1$. |
| `phase2_stage1_shift_log.txt` | 734 lines, recorded output of the run of 2026-11-04. |

### 8.2 Result

**553 checks, 553 PASS, 0 FAIL** — 91 `[EXH]`, 462 `[SMP]`.

### 8.3 Parameter coverage

| $(q,t,n)$ | $\dim_{\mathbb F_q}R^n$ | coverage |
|---|---|---|
| $(4,1,1)$ | 4 | fully exhaustive (all vectors, all $a\in R$, all $Z\in R_n$, all 65 536 $(x,a)$ pairs) + census over all 529 $\mathbb F_q$-subspaces |
| $(4,1,2)$ | 8 | all $B$-pairs; all 65 536 vectors for $T=$ right multiplication by $X$; pairs sampled |
| $(4,1,3)$ | 12 | sampled |
| $(9,1,1)$ | 4 | fully exhaustive |
| $(9,1,2)$ | 8 | sampled |
| $(4,2,1)$ | 8 | all 65 536 vectors for $T=$ right multiplication by $X$; rest sampled ($t=2$) |
| $(4,2,2)$ | 16 | sampled — **wild case** ($p\mid n$, $t\ge2$); no structural claim is made there |
| $(8,1,2)$ | 8 | sampled ($r=3$) |

All $k,s\bmod r$ at every parameter set.

### 8.4 Reproducibility

```bash
cd 04_COMPUTATION
python3 phase2_stage1_shift_checks.py        # -> phase2_stage1_shift_log.txt
```

Run from its own directory (it imports `ring_structure_checks`, which must sit beside it,
and writes its log to the current directory). Python 3.11.2, standard library only.
Sampling seed **20261104**; runtime ≈ 100 s. **Two consecutive runs produced
byte-identical logs**, SHA-256
`98383c76c957b2f4b613d97b8889c4bb39eebecf2c616edf48bc1fb1d9c5c3ef`.
Environment (Python version, dates) as in §"Environment" above.

### 8.5 Proved results versus computationally verified observations

The distinction is recorded per statement in the register (rows T-044 … T-068) and is
binding for every later stage:

* **Proved** (in `PHASE2_STAGE1_CYCLIC_SHIFT.md`, independently of any script): the
  convolution formula; $\iota$ as an $(R,R)$-bimodule isomorphism; $T^n=1$ and the
  elementary properties of $T$; **right and left $R$-linearity of $T$**; $T$ as right and
  left multiplication by $X$; $T$ left $R_n$-linear for free and right $R_n$-linear iff
  $X$ is central; **Theorem 4.1** (right ideals of $R_n$ ↔ $T$-invariant right
  $R$-submodules of $R^n$, both directions, all boundary cases); the operator statement
  $XT=TX$ and the equivalence "$L_X=R_X$ iff $X$ central"; the five failure modes without
  centrality; $T\sigma_k=\sigma_kT$ and $T\theta_s=\theta_sT$; $\sigma_k$ preserving the
  sides; **$\theta_s\rho_a=\lambda_{\theta_s(a)}\theta_s$** with an explicit witness that
  it is **not** a commutation; semilinearity of $\sigma_k,\theta_s$ and $F_q$-linearity
  of $T$; and two of the three negative controls (§4.3(a) and §4.3(c) of the document).
* **`COMPUTATIONALLY VERIFIED ONLY`** (no theorem claimed): the negative control
  §4.3(b) (T-056); the census at $(4,1,1)$ (T-064); the run record (T-065).
* **Not attempted, status preserved:** `rev` / P-2.1f (T-066, `PROPOSED / UNPROVED`);
  **L-6.1** (T-067, `PROPOSED / UNPROVED`); **T-021 principality** (unchanged,
  `proved (conditional)`, open for $t\ge2$ or $p\mid n$).
* **Open and carried forward per decision D3** (T-068): T-006, T-027 (the
  skew-polynomial comparison in §5.3(1) of the Stage-1 document is exactly this gap),
  T-011–T-014, warning B3.5, the Phase-1 enumeration coverage gaps ($q=9,n=3$; no
  enumeration at $q=4,t=2,n=2$ — the wild case is tested by Stage 1 but not counted), and
  the $n\ge2$ left-submodule gap. Pair tests are sampled outside $(4,1,1)$; the only
  exhaustive subspace census is at $n=1$.

**A passing script never promotes a statement.** Negative controls report mismatch counts
(e.g. non-central $Y=E_{11}$: $59\,760/65\,536$ mismatches at $(4,1,1)$ versus $0/65\,536$
for $Y=XI_2$; $\theta_s\rho_a\neq\rho_{\theta_s(a)}\theta_s$: $60\,480/65\,536$) so that a
test comparing the wrong two quantities cannot pass silently.

---

## 9. Phase 2 — Stage 2A (added 2026-11-05)

Companion document: `03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md`; register rows
**T-069 … T-093**. Scope: the Morita correspondence, the generator-number identity, and
the **individual** principality criterion. **Out of scope (not attempted):** P-2.4
(CRT/Hensel), **P-2.6 (global principality)**, the wild-case classification,
P-2.7/P-2.8, hulls, Gray maps, quantum constructions, C-2.1, manuscript. CT-0 … CT-6 were
**not** run as a suite.

### 9.1 Files

| File | Role |
|---|---|
| `phase2_stage2a_morita_checks.py` | 1566 lines. Builds `B = A_t[X]/⟨X^n−1⟩`, `P = B^2` and `S = M_2(B)` from scratch. Parts: ring sanity and the Jacobson radical; the submodule lattice and `μ_B` (three methods); the right-ideal lattice and `μ_S` (three methods); the Morita dictionary (bijection, lattice operations, cardinality, left/two-sided ideals); the identity and L-2.3a/b/c; the principality criterion; the Stage-1 dictionary (`R_n ≅ M_2(B)`, `W(I) = ρ(C·P_A)`); the wild case `(4,2,2)`; the projectivity counterexample. |
| `phase2_stage2a_morita_log.txt` | 699 lines, recorded output of 2026-11-05. |

### 9.2 Result

**429 checks, 429 PASS, 0 FAIL** — 391 `[EXH]`, 38 `[SMP]`.

### 9.3 Headline numbers

| `(q,t,n)` | `#submodules of B^2` = `#right ideals of S` | `#principal` | `μ_B` distribution | `μ_S` distribution |
|---|---|---|---|---|
| `(2,1,1)` | 5 | 5 | `0:1, 1:3, 2:1` | `0:1, 1:4` |
| `(2,1,2)` | 15 | 15 | `0:1, 1:9, 2:5` | `0:1, 1:14` |
| `(2,2,1)` | 15 | 15 | `0:1, 1:9, 2:5` | `0:1, 1:14` |
| `(4,1,1)` | 7 | 7 | `0:1, 1:5, 2:1` | `0:1, 1:6` |
| `(9,1,1)` | 12 | 12 | `0:1, 1:10, 2:1` | `0:1, 1:11` |
| `(2,1,3)` | 35 | 35 | `0:1, 1:23, 2:11` | `0:1, 1:34` |
| `(2,3,1)` | 37 | 37 | `0:1, 1:21, 2:15` | `0:1, 1:36` |
| `(8,1,1)` | 11 | 11 | `0:1, 1:9, 2:1` | `0:1, 1:10` |
| `(4,1,2)` | 33 | 33 | `0:1, 1:25, 2:7` | `0:1, 1:32` |
| `(4,2,1)` | 33 | 33 | `0:1, 1:25, 2:7` | `0:1, 1:32` |
| `(2,2,2)` (wild model) | **159** | **137** | `0:1, 1:51, 2:85, 3:21, 4:1` | `0:1, 1:136, 2:22` |
| `(4,1,3)` | 343 (ideals targeted) | — | `0:1, 1:215, 2:127` | `0:1, 1:342` |

The values 7, 12, 11, 33, 33, 343 and 35 reproduce the Phase-1 cyclic-code counts
(T-041, T-020); 159 at `(2,2,2)` is new. At `(2,2,2)`: `1+51+85 = 137` = the number of
principal right ideals = `#{W : μ_B(W) ≤ 2}`, and `21+1 = 22` = the number of right ideals
needing two generators; the unique `μ_B = 4` submodule is `m ⊕ m`, whose ideal `M_2(m)` is
**not principal** (certified by an exhaustive `x`-scan over all 4096 of its elements).

### 9.4 Reproducibility

```bash
cd 04_COMPUTATION
python3 phase2_stage2a_morita_checks.py        # -> phase2_stage2a_morita_log.txt
```

Python 3.11.2, standard library only; seed **20261105**; runtime ≈ 285 s. **Two
consecutive runs produced byte-identical logs**, SHA-256
`3ef38b17b00ad765bdf1c77779a1481a4ae40951f28521ecb53967b90323abe5` (699 lines).

### 9.5 Proved versus computationally verified

* **Proved** (in the companion document, independently of any script): the identification
  `R_n ≅ M_2(B)`; the Morita correspondence with all its lattice properties; the left-ideal
  and two-sided-ideal dictionaries; the agreement of the Stage-1 and Morita
  correspondences; **L-2.3a** (by column packing, with no hypothesis — the lifting proof
  that uses projectivity is recorded as a second route, and Proposition 3.3 shows the
  projectivity hypothesis is not removable for a general module `P`); **L-2.3b**;
  **L-2.3c**; the identity `μ_S(I_W) = ⌈μ_B(W)/2⌉`; the individual principality criterion;
  the wild counterexample at `(4,2,2)`; and the reduction of the global question.
* **`COMPUTATIONALLY VERIFIED ONLY`** (T-087 … T-092): the census tables, the agreement of
  the three `μ` methods, the `(2,2,2)` wild census, the `(4,2,2)` targeted certificates, the
  projectivity counterexample as computed, and the byte-identical reproducibility.
* **Not attempted** (T-093): P-2.4, **P-2.6** (untouched), L-2.6.1–L-2.6.8, **T-021**
  (unchanged), L-6.1, P-2.7/P-2.8, hulls, Gray maps, quantum, C-2.1; `O-2.2` remains open
  (largest `μ_B` observed: 4).

**A passing script never promotes a statement.** The right ideals `xS` are computed from
the definition (`span_{F_q}{xN}`), never from `im x`, so that L-2.3a could have failed;
it did not, anywhere.


---

## 10. Phase 2 — Stage 2B: `phase2_stage2b_crt_principality.py`

**Purpose.** Independent verification of P-2.4 (CRT/Hensel with exact hypotheses) and
P-2.6 (the global principality criterion), plus the Galois-compatibility question of
Task D. Companion document: `03_THEOREMS/PHASE2_STAGE2B_CRT_PRINCIPALITY.md`.

**Log.** `phase2_stage2b_crt_log.txt` — **460 checks, 460 PASS, 0 FAIL**, 434 `[EXH]` and
26 `[SMP]`, seed `20261106`, 709 lines, 60 383 bytes, SHA-256
`8db6fb5fd82bce710b792b74019e1e43b68b9232660215d55a559675b7ce0460`. Two consecutive runs
(Python 3.11.2, ≈ 82 s each) produced **byte-identical** logs; the log carries no
timestamp and no elapsed time, so the comparison is exact.

### 10.1 Independence from Stage 2A

Only `Field`, `Local`, `rref` and `nullspace_basis` are imported from
`ring_structure_checks.py`. Everything else is written again here, with different
representations: `B` is `A_t[X]/⟨h⟩` (coefficient lists) rather than the Stage-2A model;
factorisation is by trial division with an irreducibility test and is cross-checked
against the `q`-cyclotomic cosets; `μ` is computed by (i) a lattice BFS, (ii) brute-force
`k`-tuples, (iii) Nakayama on components, (iv) an exhaustive single-generator scan for
principality.

### 10.2 Sections of the log

| Section | Content | Tests |
|---|---|---|
| Hensel (per case) | lifts are monic, reduce to `f_j` mod `u`, product = `g`; non-vacuity `X²+X+u ↦ (X+u)(X+1+u)`; both routes (squarefree-only, repeated) agree | `[EXH]` |
| CRT (per case) | additivity, multiplicativity, bijectivity of `B → ∏ B_j`; Bézout idempotent identities; `e_j ↦ (0,…,1,…,0)` | `[EXH]` |
| local components | `ρ_j` a surjective homomorphism; `m_j = (u,f_j) = ker ρ_j`; `B_j/m_j` a field; nilpotency `t+p^v−1`; units = complement; `dim_{F_q}`, `|B_j|` | `[EXH]`/`[SMP]` |
| invariant | `dim_{K_j}(m_j/m_j²)` vs. the 0/1/2 trichotomy (falsification test CT-2) | `[EXH]` |
| ideals/submodules | ideal tuples; submodule tuples; reconstruction; `dim` additive, `|W|` multiplicative | `[EXH]` |
| Galois (Task D) | `σ_k` permutation vs. `C ↦ p^kC`; `σ_k(e_j) = e_{perm(j)}`; equivariance; `m_j` preimages | `[EXH]` |
| census | full submodule lattices (5 rings); `[EXH]` `μ` agreement; principality certificates | `[EXH]` |
| CRT-built lattice | 35 937 = 33³ at `(4,2,3)`, closure / `μ` / principality sampled | `[EXH]` + `[SMP]` |
| wild | `dim_K(m/m²) = 2`; `dim_{K}(W/mW) = 4`; `dim_{F_q}(I_W/I_WJ(S)) = 8 > 4`; exhaustive `x`-scan; two generators | `[EXH]` |
| negative controls | neg-1 … neg-5 | `[EXH]` 5/5 |

### 10.3 Proved versus computationally verified (Stage 2B)

* **Proved** (in the companion document, independently of the script): the squarefree-part
  lemma; **Hensel (L-2.4.1) from scratch**; `F_j = f_j`; the CRT decomposition (L-2.4.2);
  locality, dimension and nilpotence of `B_j` (L-2.4.3/L-2.4.4); the ideal and submodule
  correspondences; the trichotomy `dim_{K_j}(m_j/m_j²) ∈ {0,1,2}` (L-2.4.6 = L-2.6.6);
  **Smith normal form over a finite chain ring (L-2.6.4), proved in full**; chain ring
  `⟺ t = 1` or `p ∤ n` (L-2.6.3); `μ_B = max_j μ_{B_j}` (L-2.4.5 = L-2.6.5); **P-2.6 in
  both directions**; the Galois permutation and its corollaries (Task D).
* **`COMPUTATIONALLY VERIFIED ONLY`** (T-112, T-113): the census, the negative controls and
  the byte-identical reproducibility.
* **Not attempted** (T-114): P-2.7/P-2.8, hulls, Gray maps, quantum constructions,
  C-2.1d/e/f/g; `O-2.2` remains open.

**A passing script never promotes a statement.** Every principality certificate exhibits a
generator `x` and checks both `x ∈ I_W` and `|xS| = |I_W|`; every non-principality
certificate is backed by a dimension bound (and, at `(2,2,2)`, by an exhaustive scan of
all 4096 elements of `I_W`).

### 10.4 Regression

`phase2_stage2a_morita_checks.py` was re-run unchanged in a scratch directory on the same
Phase-1 library and produced its recorded log byte-for-byte
(`3ef38b17b00ad765bdf1c77779a1481a4ae40951f28521ecb53967b90323abe5`, 429/429 PASS), so the
Stage-2A results are unaffected by Stage 2B.

---

## 11. Phase 2 — Stage 2C: `phase2_stage2c_galois_duality.py`

Stage 2C verifies **L-6.1** (`θ_s` is an anti-automorphism of `R_n`), the annihilator
conventions, **P-2.7** (`C^{⊥_s} = rev(ann_r(θ_s(g)))`), **P-2.8** (reciprocal
generators), and the cardinality / double-dual identities.
Companion document: `03_THEOREMS/PHASE2_STAGE2C_GALOIS_DUALITY.md`.

**Log.** `phase2_stage2c_galois_log.txt` — **596 checks, 596 PASS, 0 FAIL**, 101 `[EXH]`
and 495 `[SMP]`, seed `20261107`, two consecutive runs byte-identical, SHA-256
`00355e7f205de16cbe0a567881a978f326007e564a606663135a71f5103a30ed` (777 lines).

**Cases** (each for every `s ∈ {0,…,r−1}`): `(4,1,1)` exhaustive over all 256 elements of
`R_n`; `(4,1,2)`, `(4,2,1)`, `(9,1,2)`, `(8,1,2)`, `(4,1,3)`, `(4,2,3)` with 200 distinct
random generators each (`[SMP]`); `(4,2,2)` sampled plus a fully `[EXH]` wild
counterexample.

### 11.1 Independence of the tests

The dual `C^{⊥_s}` is computed **from the definition** by `F_q`-linear algebra
(`{y : B_s(x,y) = 0 ∀ x ∈ C}`); every annihilator is computed as the **kernel of the
multiplication map** `w ↦ vw` over the standard basis (brute force, never from `im`,
never via Morita); `im` and `ker` are separate routines, and the Morita form
`ann_r(v) = I_{ker v}` is therefore an independent statement. Two real bugs were caught
this way during development and are recorded in T-132 (the SNF exponent `ω^{ℓ−a}` at
`a = 0`) and in the negative controls (rows vs columns of `I_W`).

### 11.2 Proved versus computationally verified (Stage 2C)

* **Proved** (register rows T-115 … T-128, T-130, T-131, T-132): L-6.1 on `R[X]` and on
  `R_n`; the descent to the quotient; additivity/bijectivity/inverse; `θ_s² = σ_{2s}` and
  the order `2r/gcd(r,2s)`; the annihilator side laws; `ann_r(R_n g) = ann_r(g)` versus
  the strict inclusion for right ideals; P-2.1f (`rev`); P-2.7 in three equivalent forms
  and the Morita form, for principal **and** non-principal right ideals; L-6.5; P-2.8 in
  its regime-free and Smith-normal-form versions; the wild counterexample.
* **Computationally verified only** (T-129, T-133, T-134, T-135): the C1–C4 consistency
  checks, the cardinality and double-dual checks (the identities themselves are Phase-1
  theorems), the generator-orbit uniqueness statement, and the census/negative controls.
* **Not attempted** (T-136): hulls, Gray maps, quantum constructions.

### 11.3 Negative controls

All seven **must** fail, and all seven do: neg-1 wrong multiplication order in `θ_s`;
neg-2 `rev` treated as an anti-automorphism; neg-3 `ann_l` in place of `ann_r`; neg-4
`rev` omitted (genuinely vacuous for `n ≤ 2`, and the log says so instead of emitting a
tautological pass; it detects 19 of 40 codes at `(4,1,3)`); neg-5 `θ_s` omitted; neg-6
`I_W` built from rows instead of columns; neg-7 the swapped pairing.

### 11.4 Regression

`phase2_stage2a_morita_checks.py` and `phase2_stage2b_crt_principality.py` were re-run
unchanged on the same Phase-1 library and reproduced their recorded logs byte-for-byte
(429/429 and 460/460), so the Stage-2A and Stage-2B results are unaffected by Stage 2C.
