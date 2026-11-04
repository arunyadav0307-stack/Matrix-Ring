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
