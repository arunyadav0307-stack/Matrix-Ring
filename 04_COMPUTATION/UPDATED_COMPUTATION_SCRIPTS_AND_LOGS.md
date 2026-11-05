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
| `phase2_stage1_shift_checks.py` | 1001 | **Phase 2, Stage 1**: definitions and shift structure — $\iota$, cyclic convolution, centrality of $X$, $T^n=1$, $T$ as left/right multiplication by $X$, $F_q$- vs $R$-linearity, right ideals $\leftrightarrow$ $T$-invariant right $R$-submodules, $\sigma_k$/$\theta_s$ compatibility (see §8) | ≈ 100 s |
| `phase2_stage1_shift_log.txt` | 734 | log of the Stage-1 script: **553 / 553 checks PASS** (91 `[EXH]`, 462 `[SMP]`), 8 parameter sets | — |

## 2. How to reproduce

```bash
cd 04_COMPUTATION
python3 -u galois_duality_experiments.py full     # -> galois_experiments_log.txt
python3 -u galois_t2_check.py                     # -> galois_t2_log.txt
python3 -u alahmadi_reconciliation.py             # -> alahmadi_reconciliation_log.txt
python3 -u phase0_feasibility.py                  # -> phase0_results.txt (original E1-E5)
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
