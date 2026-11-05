# 04 — Computation: reproducibility notes (blueprint rule 11)

## Software environment
* Python **3.11.2** (CPython), standard library only — no third-party packages,
  no floating point anywhere (all arithmetic is exact over $\mathbb F_p$).
* OS: Linux sandbox; run date of the recorded log: **2026-11-04 03:52:42**.
* Total runtime of the full Phase-0 script: **18.8 s**.

## Files
| File | Role |
|---|---|
| `matrix_ring_lib.py` | Library: $\mathbb F_q$ (tables + primitive polynomial found by search), $A_t=\mathbb F_q[u]/\langle u^t\rangle$, $R=M_m(A_t)$, $R^n$ as an $\mathbb F_q$-space, candidate pairings, $\mathbb F_q$-linear algebra (rref / span / nullspace / intersection), operator-image closures. |
| `phase0_feasibility.py` | Experiments E1–E5 (see below). |
| `phase0_results.txt` | Recorded output of the run of 2026-11-04 (also `phase0_stdout.txt`, identical content). |

## How to reproduce
```bash
cd 04_COMPUTATION
python3 phase0_feasibility.py          # writes phase0_results.txt
```
Deterministic: `test_automorphisms` seeds `random.seed(12345)`; every other
experiment is exhaustive.

## Experiments, inputs, and honest completeness limits

| ID | Question | Parameters | Method | Completeness |
|----|----------|-----------|--------|--------------|
| **E1** | Is the entrywise Frobenius $\sigma_s$ an automorphism of $M_m(A_t)$? Is $\mu_c:u\mapsto cu$? Is $\theta_s=\sigma_s\circ{}^{\mathsf T}$ an anti-automorphism? Are they nontrivial? | $(p,r,t,m)\in\{(2,1,1,2),(2,2,1,2),(2,1,2,2),(2,2,2,2),(2,1,1,3),(3,2,1,2)\}$ | **randomised**, 400 trials per map (sampled uniformly from $R\times R$) | **NOT exhaustive** (except on the smallest ring). Sufficient to *detect* failure, not to *prove* the property. Proofs are Phase-1 deliverables (register T-002, T-003). |
| **E2** | Is $\Lambda=\lambda\circ\mathrm{tr}$ non-degenerate / ideal-catching on both sides? | $(q,t,m)\in\{(2,1,2),(4,1,2),(2,2,2),(4,2,2),(2,1,3),(16,1,2)\}$ | **exhaustive** on a basis (Gram matrix on an $\mathbb F_q$-basis, rank test — valid because the form is bilinear) | Exhaustive for the listed parameters; general $m,t,q$ still needs the Phase-1 proof (T-001). |
| **E3** | Which pairings give $|C||C^\perp|=|R|$ for **left** vs **right** ideals, and on which side does the dual land? | $R=M_2(\mathbb F_2),M_2(\mathbb F_4),M_2(\mathbb F_2[u]/\langle u^2\rangle)$; $n=1$ | **exhaustive**: *all* one-sided ideals enumerated (BFS: principal ideals + closure under pairwise sums; completeness guaranteed because every ideal is the sum of the principal ideals it contains) | Exhaustive for these three rings at $n=1$. |
| **E4** | Same question for cyclic codes of length 3; hull dimensions; is the hull a module? | $R=M_2(\mathbb F_2)$, $n=3$ (ambient $\mathbb F_2^{12}$, $|R^3|=4096$) | **exhaustive**: all 4096 ambient vectors → principal codes → closure under pairwise sums; 35 right-cyclic, 35 left-cyclic, 4 two-sided codes found | Exhaustive for $(m,q,t,n)=(2,2,1,3)$ **only**. |
| **E5** | Does the parametrisation $C=(fh)+u(fg)$ of Alahmadi–Sboui–Solé–Yemen (2013) reproduce the complete list? | $R=M_2(\mathbb F_2)$, $n=3$; all $3^3=27$ assignments of the three $\mathbb F_4$-irreducible factors of $X^3-1$ to $(f,g,h)$; three readings of the notation (A: right ideals, $u$ left; B: right ideals, $u$ right; C: residue+torsion $\{r+ut\}$) | exhaustive over the 27 triples | **Warning:** this experiment depends on my *interpretation* of the source's notation. It is evidence, not a refutation. See `02_PHASE_REPORTS/Phase_0/Phase_0_Report.md` §7 GAP 2 and issue U2. |

## What is NOT claimed
* No result here is a theorem. Every table in `phase0_results.txt` is a
  **computational observation over the stated (finite) parameter range**.
* E1 is randomised; E2–E5 are exhaustive in the stated range only.
* No minimum distances, no quantum parameters and no comparison tables have been
  computed yet (those are Phase 7).

## Known limitations / planned extensions
1. The ambient enumeration scales as $|R|^n$; E4 at $n=3$, $m=2$, $q=2$, $t=1$
   is already at the edge ($2^{12}$). For $(q,t)=(4,2)$ a brute-force ambient
   enumeration is impossible; Phase 1 must use the Morita parametrisation
   (register T-005) instead.
2. E4/E5 currently only cover $n=3$ (odd, coprime to $q$ in the semisimple
   case). Repeated-root lengths ($p\mid n$) are **not** covered and are a
   separate, harder regime.
3. `matrix_ring_lib.py` has no unit-test suite yet; Phase 1 should add one
   (e.g. associativity/distributivity spot checks, round-trip vectorisation
   tests) before the library is used to support published tables.

---

## Phase 2 — Stage 1 (added 2026-11-04)

Companion to `03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md`; delivered in commit `bfb16d7`.
Stage 1 covers **definitions and the shift structure only** — no generator numbers
(P-2.3), no CRT/Hensel (P-2.4), no principality (P-2.5/P-2.6), no duals or annihilators
(P-2.7/P-2.8), no enumeration conjecture (C-2.1), and no manuscript text. CT-0 … CT-6
were **not** run as a suite; only the focused Stage-1 tests below were run.

| File | Role |
|---|---|
| `phase2_stage1_shift_checks.py` | Stage-1 verification: the coefficient representation $\iota:R^n\to R_n$, multiplication as cyclic convolution, centrality of $X$, $\iota$ as an $(R,R)$-bimodule isomorphism, $T^n=1$, $T$ as right **and** left multiplication by $X$, $F_q$-linearity versus right/left $R$-linearity of $T$, the equivalence between right ideals of $R_n$ and $T$-invariant right $R$-submodules of $R^n$ (both directions + negative controls), and the $\sigma_k$ / $\theta_s$ identities (commutation with $T$, side preservation, **side swapping** $\theta_s\rho_a=\lambda_{\theta_s(a)}\theta_s$, semilinearity). Imports `Field`, `Local`, `MatRing` and the $\mathbb F_q$-linear algebra from `ring_structure_checks.py`; $B=A_t[X]/\langle X^n-1\rangle$, $M_2(B)$, $\iota$ and $T$ are built here from scratch. Writes its log to the current directory. |
| `phase2_stage1_shift_log.txt` | Recorded output of the run of 2026-11-04: **553 checks, 553 PASS, 0 FAIL** (91 `[EXH]`, 462 `[SMP]`). |

### How to reproduce

```bash
cd 04_COMPUTATION
python3 phase2_stage1_shift_checks.py        # -> phase2_stage1_shift_log.txt
```

Run it **from its own directory**: it imports `ring_structure_checks` (which must sit
beside it) and writes `phase2_stage1_shift_log.txt` to the current working directory.
Environment as above (Python 3.11.2, standard library only). Sampling seed **20261104**;
every check is labelled `[EXH]` (exhaustive) or `[SMP]` (sampled, with the sample size,
the budget and the seed printed on the line). Runtime ≈ **100 s**.

**Reproducibility verified:** two consecutive runs produced **byte-identical** logs,
SHA-256 `98383c76c957b2f4b613d97b8889c4bb39eebecf2c616edf48bc1fb1d9c5c3ef`
(`phase2_stage1_shift_log.txt`, 734 lines).

### Parameter coverage

| $(q,t,n)$ | $\dim_{\mathbb F_q}R^n$ | $|R^n|$ | coverage |
|---|---|---|---|
| $(4,1,1)$ | 4 | 256 | **fully exhaustive**: all vectors, all $a\in R$, all $Z\in R_n$, all 65 536 $(x,a)$ pairs, plus a brute-force census over all 529 $\mathbb F_q$-subspaces |
| $(4,1,2)$ | 8 | 65 536 | all $B$-pairs exhaustive; **all 65 536 vectors** for $T=$ right multiplication by $X$; pairs sampled |
| $(4,1,3)$ | 12 | $1.7\times10^{7}$ | sampled |
| $(9,1,1)$ | 4 | 6 561 | **fully exhaustive** (all vectors, all $a$, all $Z$) |
| $(9,1,2)$ | 8 | $4.3\times10^{7}$ | sampled |
| $(4,2,1)$ | 8 | 65 536 | **all 65 536 vectors** for $T=$ right multiplication by $X$; rest sampled ($t=2$) |
| $(4,2,2)$ | 16 | $4.3\times10^{9}$ | sampled — **wild case** ($p\mid n$ and $t\ge2$); Stage 1 makes no structural claim there |
| $(8,1,2)$ | 8 | $1.7\times10^{7}$ | sampled ($r=3$, so $\theta_s$ is not an involution) |

All $k,s \bmod r$ are tested at every parameter set.

### What the 553/553 result does and does not mean

* It is **supporting evidence, not proof**. Every Stage-1 statement is proved in
  `03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md` §2–§6; the register rows T-044 … T-068
  record, per statement, whether it is `PROVED IN PHASE 1`,
  `PROVED IN PHASE 2 STAGE 1`, `COMPUTATIONALLY VERIFIED ONLY`,
  `PROPOSED / UNPROVED` or `OPEN`. **No statement is recorded as proved because a script
  passed.**
* Three results are `COMPUTATIONALLY VERIFIED ONLY` and are claims about no parameter
  range beyond what was run: (i) the negative control "a $T$-invariant $\mathbb F_q$-subspace
  need not be a right $R$-submodule" (T-056); (ii) the census at $(4,1,1)$ — exactly
  $7=q+3$ $T$-invariant right $R$-submodules with $\mathbb F_q$-dimensions
  $[0,2,2,2,2,2,4]$, obtained by brute force over subspaces and **without** Morita
  (T-064); (iii) the run record itself (T-065).
* The negative controls carry explicit mismatch counts (e.g. non-central $Y=E_{11}$
  breaks right $R$-linearity in $59\,760/65\,536$ cases at $(4,1,1)$ while the central
  $Y=XI_2$ gives $0$; $\theta_s\rho_a\neq\rho_{\theta_s(a)}\theta_s$ in
  $60\,480/65\,536$ cases) so that no convention test can pass vacuously.
* Not attempted anywhere in Stage 1 (register T-066, T-067, T-068): `rev` (P-2.1f),
  **L-6.1** ($\theta_s$ as an anti-automorphism of $R_n$), and **T-021** (principality,
  still `proved (conditional)` and open for $t\ge2$ or $p\mid n$).
