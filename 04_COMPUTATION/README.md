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

---

## Phase 2 — Stage 2A (added 2026-11-05)

Companion to `03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md` (Morita correspondence,
generator numbers, individual principality). Delivered in the Stage-2A commit; register
rows **T-069 … T-093**.

| File | Role |
|---|---|
| `phase2_stage2a_morita_checks.py` | Stage-2A verification: the Morita correspondence `W ↦ I_W = {M : im M ⊆ W}` (both directions, lattice operations, cardinality, left/two-sided ideals, and the dictionary with the Stage-1 cyclic-code representation); the generator-number identity `μ_S(I_W) = ⌈μ_B(W)/2⌉` via L-2.3a, L-2.3b, L-2.3c; the individual principality criterion `I_W` principal ⟺ `μ_B(W) ≤ 2`; and the projectivity counterexample for a non-projective module. Imports only `Field`, `Local`, `MatRing`, `rref` and the reporting helpers from `ring_structure_checks.py` (read-only); `B = A_t[X]/⟨X^n−1⟩`, `P = B^2` and `S = M_2(B)` are built here. Writes its log to the current directory. |
| `phase2_stage2a_morita_log.txt` | Recorded output: **429 checks, 429 PASS, 0 FAIL** (391 `[EXH]`, 38 `[SMP]`). |

### How to reproduce

```bash
cd 04_COMPUTATION
python3 phase2_stage2a_morita_checks.py        # -> phase2_stage2a_morita_log.txt
```

Run from its own directory: it imports `ring_structure_checks` (which must sit beside it)
and writes `phase2_stage2a_morita_log.txt` to the current working directory. Environment
as above (Python 3.11.2, standard library only). Sampling seed **20261105**; every check
is labelled `[EXH]` (exhaustive) or `[SMP]` (sampled). Runtime ≈ **285 s**.

**Reproducibility verified:** two consecutive runs produced **byte-identical** logs,
SHA-256 `3ef38b17b00ad765bdf1c77779a1481a4ae40951f28521ecb53967b90323abe5` (699 lines).
The log carries no timestamp and no elapsed time, so the comparison is exact.

### Independence safeguards

* `xS` is computed as `span_{F_q}{xN : N ∈ S}` by direct multiplication, **never** from
  `im x`, so that L-2.3a is tested rather than assumed.
* `μ_B` and `μ_S` are each computed by **three independent methods** — lattice BFS over
  sums of cyclics/principals; brute-force scan over `k`-tuples (resp. over all `x ∈ I`);
  and Nakayama on the semisimple quotient — and the three are cross-checked against each
  other before any comparison with `⌈μ_B(W)/2⌉`.

### Parameter coverage

| `(q,t,n)` | `B` | `|B|` | coverage |
|---|---|---|---|
| `(2,1,1)` | `F_2` | 2 | exhaustive over both lattices |
| `(2,1,2)` | `F_2[ε]/⟨ε²⟩` | 4 | exhaustive (repeated root, `t=1`) |
| `(2,2,1)` | `F_2[u]/⟨u²⟩` | 4 | exhaustive — **CT-1a model ring 1** |
| `(4,1,1)` | `F_4` | 4 | exhaustive (Phase-1 anchor: 7) |
| `(9,1,1)` | `F_9` | 9 | exhaustive (Phase-1 anchor: 12) |
| `(2,1,3)` | `F_2 × F_4` | 8 | exhaustive (Phase-1 anchor: 35) |
| `(2,3,1)` | `F_2[u]/⟨u³⟩` | 8 | exhaustive — **CT-1a model ring 2** |
| `(8,1,1)` | `F_8` | 8 | exhaustive (Phase-1 anchor: 11) |
| `(4,1,2)` | `F_4[ε]/⟨ε²⟩` | 16 | exhaustive (Phase-1 anchor: 33) |
| `(4,2,1)` | `F_4[u]/⟨u²⟩` | 16 | exhaustive (Phase-1 anchor: 33) |
| `(2,2,2)` | `F_2[u,ε]/⟨u²,ε²⟩` | 16 | exhaustive — **CT-1a model ring 3, wild**: `μ_B` up to `4`, 22 non-principal right ideals |
| `(4,1,3)` | `F_4³` | 64 | submodule lattice exhaustive (343, Phase-1 anchor); ideals targeted |
| `(4,2,2)` | `F_4[u,ε]/⟨u²,ε²⟩` | 256 | **targeted** (`|S| = 2³²`): six submodules, incl. `W = m ⊕ m` with `μ_B = 4` |

### What the 429/429 result does and does not mean

* It is **supporting evidence, not proof.** The identity, the correspondence and the
  principality criterion are proved in `PHASE2_STAGE2A_MORITA_GENERATORS.md` §2–§4; the
  register rows T-069 … T-093 record, per statement, whether it is
  `PROVED IN PHASE 2 STAGE 2A`, `COMPUTATIONALLY VERIFIED ONLY`, or `OPEN`.
* `COMPUTATIONALLY VERIFIED ONLY` rows (T-087 … T-092) are claims about the listed
  parameter sets only.
* **Not attempted** (T-093): P-2.4 (CRT/Hensel), **P-2.6 (global principality — untouched,
  still `PROPOSED / UNPROVED`)**, the wild-case classification, P-2.7/P-2.8 (hence
  **L-6.1**), hulls, Gray maps, quantum constructions, C-2.1. **T-021 is not discharged.**
  `O-2.2` (`μ_B(W) ≤ 4` uniformly) remains open; the largest value observed is `4`.


---

## Phase 2 — Stage 2B: CRT/Hensel decomposition and the global principality criterion

**Deliverable:** `03_THEOREMS/PHASE2_STAGE2B_CRT_PRINCIPALITY.md`
**Script:** `phase2_stage2b_crt_principality.py` (2006 lines)
**Log:** `phase2_stage2b_crt_log.txt` — **460 checks, 460 PASS, 0 FAIL** (434 `[EXH]`,
26 `[SMP]`), seed `20261106`, 709 lines, SHA-256
`8db6fb5fd82bce710b792b74019e1e43b68b9232660215d55a559675b7ce0460`.

**Result.** P-2.4 (CRT/Hensel) and **P-2.6** are proved:

```
Every right ideal of R_n is principal   ⟺   p ∤ n   or   t = 1 .
```

* `⇐` R_n ≅ M_2(B) → Morita (Stage 2A) → CRT splits `W` → each component is a chain ring
  (`t = 1` or `p ∤ n`) → Smith normal form gives `μ ≤ 2` → `μ_B = max_j μ_{B_j}` →
  Stage-2A criterion.
* `⇒` In the wild case (`t ≥ 2`, `p ∣ n`) the component `B_j = A_t[X]/⟨f_j^{p^v}⟩` has
  `dim_{K_j}(m_j/m_j^2) = 2`, so `μ_B(m_j ⊕ m_j) = 4` and `I_W = M_2(m_j)` is **not**
  principal; `dim_{F_q}(I_W/I_W J(S)) = 8 > 4`, the bound for a cyclic module.

**What the script implements from scratch** (only `Field`, `Local`, `rref`,
`nullspace_basis` are imported from the Phase-1 library): polynomial arithmetic and
factorisation over `F_q` (cross-checked against `q`-cyclotomic cosets), Hensel lifting
(proved in the document, Lemma 1.2), the CRT map and its Bézout idempotents, the local
invariants of `B_j`, `M_2` over a quotient ring, submodule enumeration, four independent
`μ` computations, and principality certificates.

### Cases

| `(q,t,n)` | regime | `v`, `n'`, `e` | `J`, `{d_j}` | `#submodules of B^2` | all principal? |
|---|---|---|---|---|---|
| `(4,2,1)` | squarefree, `t ≥ 2` | 0, 1, 1 | 1, [1] | 33 | yes |
| `(4,1,2)` | repeated root, `t = 1` | 1, 1, 2 | 1, [1] | 33 | yes |
| `(2,1,3)` | squarefree, `t = 1` | 0, 3, 1 | 2, [1,2] | 35 = 5·7 | yes |
| `(9,1,2)` | squarefree, `t = 1` | 0, 2, 1 | 2, [1,1] | 144 = 12² | yes |
| `(8,1,2)` | repeated root, `t = 1` | 1, 1, 2 | 1, [1] | 93 | yes |
| `(4,2,3)` | squarefree, `t ≥ 2` | 0, 3, 1 | 3, [1,1,1] | 35 937 = 33³ | yes |
| `(2,2,2)` | **wild** | 1, 1, 2 | 1, [1] | targeted | **no** |
| `(4,2,2)` | **wild** | 1, 1, 2 | 1, [1] | targeted | **no** |
| `(9,2,3)` | **wild** | 1, 1, 3 | 1, [1] | targeted | **no** |

The counts 33, 33, 35, 144 agree with Phase 1 / Stage 2A; 93 is `N(2,8) = 8² + 3·8 + 5`
(C-2.1b, proved in Phase 1); 35 937 = 33³ confirms the pending register value C-2.1g.
The 35 937 submodules are **built** componentwise via the CRT (`|B^2| = 1.7·10⁷` forbids
element scanning): the count is `[EXH]`, the closure/`μ`/principality certificates are
`[SMP]` (200 / 399 / 180 samples).

### Wild certificates (`W = m_j ⊕ m_j`, so `I_W = M_2(m_j)`)

| `(q,t,n)` | `|W|` | `dim_{K_j}(W/m_jW)` | `dim_{F_q}(I_W/I_WJ(S))` | principal? | `μ_S` |
|---|---|---|---|---|---|
| `(2,2,2)` | 64 | 4 | 8 > 4 | **no** (all 4096 elements of `I_W` scanned) | 2 |
| `(4,2,2)` | 4096 | 4 | 8 > 4 | **no** | 2 |
| `(9,2,3)` | 3 486 784 401 | 4 | 8 > 4 | **no** | 2 |

### Negative controls (a wrong convention must FAIL — all five do)

| Control | Wrong convention | Outcome |
|---|---|---|
| neg-1 | reduced modulus `⟨f_j⟩` instead of `⟨f_j^{p^v}⟩` | kills `X^{n'}-1 ≠ 0`, so the map is not injective |
| neg-2 | `{M : rows of M ⊆ W}` | not a right ideal (counterexample found exhaustively) |
| neg-3 | `{M : im M ⊇ W}` | not a right ideal; does not even contain `0` |
| neg-4 | "`σ_1` fixes every component" | false: at `(4,2,3)` the permutation is `(0,2,1)` |
| neg-5 | "all principal" is vacuous in chain-ring cases | false: 33 submodules, `max μ = 2` |

**Why they matter.** During development an early version packed basis vectors of `W` into
the **rows** of the matrix; every dimension and cardinality check still passed, and only
the containment half of the certificate exposed it. Size-only principality tests are not
sufficient — the certificates check `x ∈ I_W` **and** `|xS| = |I_W|`.

### What the 460/460 result does and does not mean

* It is **supporting evidence, not proof.** P-2.4 and P-2.6 are proved in
  `PHASE2_STAGE2B_CRT_PRINCIPALITY.md` §1–§4; register rows T-094 … T-114 record, per
  statement, whether it is `PROVED IN PHASE 2 STAGE 2B`, `COMPUTATIONALLY VERIFIED ONLY`
  (T-112, T-113) or `OPEN` (T-114).
* **Not attempted** (T-114): P-2.7/P-2.8, hull dimensions, Gray maps, quantum
  constructions, C-2.1d/e/f/g closed forms. `O-2.2` (`μ_B(W) ≤ 4` uniformly in the wild
  case) remains **open** — Stage 2B uses only `μ ≤ 2`, proved where it is used.
* **Regression.** `phase2_stage2a_morita_checks.py` was re-run unchanged on the same
  Phase-1 library and reproduced its log byte-for-byte (429/429, `3ef38b17…23abe5`).

---

## Phase 2 — Stage 2C: Galois duality, annihilators and reciprocal generators

**Deliverable:** `03_THEOREMS/PHASE2_STAGE2C_GALOIS_DUALITY.md`
**Script:** `phase2_stage2c_galois_duality.py` (1975 lines)
**Log:** `phase2_stage2c_galois_log.txt` — **596 checks, 596 PASS, 0 FAIL** (101 `[EXH]`,
495 `[SMP]`), seed `20261107`, Python 3.11.2, two consecutive runs byte-identical,
SHA-256 `00355e7f205de16cbe0a567881a978f326007e564a606663135a71f5103a30ed` (777 lines).
**Register rows:** T-115 … T-136 (insertion-only).

Tasks: (A) **L-6.1** — `θ_s = σ_s ∘ (·)^T` is an anti-automorphism of `R_n`, proved on the
normal forms (matrix order + convolution + index swap), with the three levels
`R` / `R[X]` / `R_n` kept separate and the descent proved via `θ_s(X^n−1) = X^n−1` and the
centrality of `X^n−1`; (B) annihilator conventions and their exact side laws;
(C) **P-2.7** — `C^{⊥_s} = rev(ann_r(θ_s(g)))`, derived from the convolution equations,
in three equivalent forms plus the Morita form `ann_r(θ_s(g)) = I_{ker θ_s(g)}`, and in a
general form for **non-principal** right ideals; (D) **P-2.8** — reciprocal generators, in
a regime-free form (`h = [w_1∣w_2]` from `ker θ_s(rev g)`) and in the Smith-normal-form
form of the proposal for the chain-ring regime; (E) cardinality and double-dual
consistency, including the non-reflexive regime; (F) the computation above.

Cases: `(q,t,n) = (4,1,1), (4,1,2), (4,2,1), (4,2,2), (4,1,3), (9,1,2), (8,1,2), (4,2,3)`,
every `s ∈ {0,…,r−1}`.

Run: `python3 -u phase2_stage2c_galois_duality.py` (~78 s), which rewrites
`phase2_stage2c_galois_log.txt`. The script imports from `ring_structure_checks.py` only
`Field`, `Local`, `MatRing`, `rref`, `nullspace_basis` and the reporting helpers; the ring
`B = A_t[X]/⟨X^n−1⟩`, the maps `σ_k`, `θ_s`, `rev`, `ι`, both pairings, all annihilators
(computed as kernels of the multiplication maps) and the Smith normal form are written
from scratch here. The dual is always computed **from the definition**, so every formula
could have failed.

### What the 596/596 result does and does not mean

* It is **supporting evidence, not proof.** L-6.1, P-2.7 and P-2.8 are proved in
  `PHASE2_STAGE2C_GALOIS_DUALITY.md` §1, §3 and §4; register rows T-115 … T-136 record,
  per statement, whether it is `PROVED IN PHASE 2 STAGE 2C`, `COMPUTATIONALLY VERIFIED
  ONLY` (T-129, T-133, T-134, T-135) or `OPEN` (T-136).
* **Settled here:** L-6.1 (T-115), `rev` (T-124, discharging T-066), P-2.7 in a general
  form (T-125, T-126), L-6.5 (T-128, proved without the unconfirmed import L-6.6),
  P-2.8 (T-130, T-131), the `n = 1` anchor O-2.7, and **O-2.8, answered NO** by the wild
  counterexample `g = diag(uε, uε)` at `(4,2,2)` (T-132): `C^{⊥_s} = M_2(m)` with
  `μ_B(ker) = 4`, all 16 777 216 of its elements scanned and none generating it.
* **Not attempted** (T-136): hull dimensions, hull enumeration, Gray maps, quantum
  constructions. Still open: **O-2.9** (is every generator of a principal right ideal of
  the form `h·u`? — exhaustively verified at three parameter sets, unproved in general),
  **O-2.2**, **O-2.4** (partially resolved), **O-2.5**, **O-2.6**.
* **Regression.** `phase2_stage2a_morita_checks.py` and
  `phase2_stage2b_crt_principality.py` were re-run unchanged on the same Phase-1 library
  and reproduced their recorded logs byte-for-byte (429/429 and 460/460).

## Phase 3 — Stage 3A: Galois hull structure and dimension
`phase3_stage3a_hull_structure.py` → `phase3_stage3a_hull_log.txt`

Studies `Hull_s(C) = C ∩ C^{⊥_s}` for cyclic codes over `M_2(A_t)`:
structure and closure properties (Task A), the hull formula in the principal and
non-principal cases (Task B), hull dimension by four independent routes (Task C), the
general / reflexive / codewise Galois regimes (Task D), and LCD / self-orthogonal /
self-dual characterisations (Task E).
Companion document: `03_THEOREMS/PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md`.

Cases: `(q,t,n) = (4,1,1), (4,1,2), (4,2,1), (4,2,2), (4,1,3), (9,1,2), (8,1,2),
(4,2,3)`, every `s ∈ {0,…,r−1}`; `(8,1,2)` additionally probes the **non-reflexive**
regime (`r = 3`, `s = 1, 2`) with 600 dedicated codes.

Run: `python3 -u phase3_stage3a_hull_structure.py` (~45 s), which rewrites
`phase3_stage3a_hull_log.txt`. The script imports the Stage-2C module
(`phase2_stage2c_galois_duality.py`) and `ring_structure_checks.py` **without
modifying** them; the hull machinery — the `F_q`-subspace intersection, the four routes,
the `F_p`-rank routine, the CRT permutation `τ`, the exhaustive principality search and
all tests — is written here.

### What the 583/583 result does and does not mean

* It is **supporting evidence, not proof.** The theorems are proved in
  `PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md`; register rows T-137 … T-168 record, per
  statement, whether it is `PROVED IN PHASE 3 STAGE 3A` (20 rows), `PROVED IN PHASE 1`
  (3), `IMPORTED RESULT` (1), `COMPUTATIONALLY VERIFIED ONLY` (6), `CONJECTURE` (2) or
  `OPEN` (1).
* **Settled here:** the Morita hull formula `Hull = I_{W∩W'}` with the parity and
  principality consequences; the non-principal annihilator/reversal formula; the CRT
  permutation `τ` and the exact criterion `n ∣ p^s+1` for componentwise decomposition
  (with a witness where the naive formula gives `0` but `dim Hull = 2`); the separation
  of the general, reflexive and codewise regimes; the LCD/SO/SD characterisations.
  **No universal closed (gcd-type) hull formula exists** — the document proves the
  obstruction and records what is available instead.
* **Conjectures, unproved:** `Hull_s(C) ⊆ σ_{2s}(C)` (H-3A.1) and
  `dim Hull_s(C^{⊥_s}) = dim Hull_s(C)` (H-3A.2). The second was **downgraded** from a
  claimed theorem when the proof gap was found.
* **Open:** O-3.1 (is the hull of a principal code always principal, even in the wild
  regime? 120 wild probes found none with `μ_B ≥ 3`) and O-3.2 (the closed-formula
  obstruction, now a proved impossibility plus an open refinement).
* **Not attempted** (T-168): hull enumeration, Gray maps, quantum constructions, and no
  quantum parameter claim is made anywhere.
* **Regression.** The Stage-2A, Stage-2B and Stage-2C scripts and their logs are
  unchanged and were re-run unchanged against the start-of-stage baseline.

## Phase 3 — Stage 3B: enumeration of Galois hull dimensions

`phase3_stage3b_hull_enumeration.py` → `phase3_stage3b_hull_log.txt`
(696 lines, **206 checks, 206 PASS, 0 FAIL**; 189 `[EXH]`, 19 `[SMP]`;
seed `20261109`; Python 3.11.2; two consecutive runs byte-identical;
SHA-256 `c8904a232faf25b550a9e7f84cc1ea7f41ed3921779ac2324bf6fa7887409814`).
Deliverable: `03_THEOREMS/PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md`.

* **Task A — the four counting problems, kept separate:** (1) distinct right ideals
  (= `B`-submodules of `B^2`), (2) distinct generator matrices (generating tuples;
  `Σ_W f_k(W) = |B^2|^k` verified exhaustively), (3) unit-equivalence classes =
  orbits of `R_n^× = GL_2(B)` acting by **left** multiplication (`W ↦ UW` under
  Morita — the scalar action `u·W`, `u ∈ B^×`, is trivial and the log says so),
  (4) Morita-equivalent submodules = isomorphism classes of the `B`-modules `W`.
  Results `(1)/(3)/(4)`: `7/3/3`, `33/6/6`, `33/6/6`, `1221/58/nc`, `343/27/27`,
  `144/9/9`, `93/6/6`, `35937/216/216`.
* **Task B — enumeration:** exhaustive BFS over the submodule lattice of `B^2` where
  `|B^2| ≤ 6561`; the CRT product `L(A_t^2)^{n}` in the split regime otherwise
  (`(4,2,3)`: `33^3 = 35937` codes). Counts agree wherever both are affordable.
* **Tasks C–E:** two independent hull routes (restricted Gram/pairing; Morita
  annihilator `W' = ⋂ᵢ ker θ_s(rev gᵢ)`) agree **in dimension and as subspaces** on
  every code of every family, every `s`; hull-dimension distributions and
  `N_LCD / N_SO / N_SD` for all eight parameter sets, with SO verified by containment
  and SD by equality, never from the hull dimension alone.
* **Task F — closed form (T-169, proved):** in the split regime
  `H_{q,t,n,s}(Z) = ∏_{τ-orbits O} Tr(N^{|O|})`, `N[V,W] = Z^{dim(V ∩ δ_s(W))}`
  (bivariate version with `U^{2 dim V}`), verified exhaustively against brute force
  at `(4,1,3)`, `(9,1,2)` and `(4,2,3)` — including a case with `τ ≠ id`.
  **O-3.1 is REFUTED:** at `(4,2,2)` there are 1 (`s=0`) and 3 (`s=1`) codes whose hull
  has `μ_B = 3`; all four witnesses are self-dual codes, verified by two hull routes,
  by `μ_B(V) = dim_k(V/rad V)`, and by a randomised 2-generator search.
* **Task H — negative controls** (a wrong argument must fail): the split product count
  in the wild regime (`33 ≠ 1221`); `τ = id` when it is not; `dim C = 2tn ⇒ SD`
  (e.g. `155` vs `7` at `(4,1,3)`, `s=0`); additivity of hull dimensions over CRT
  components (`210` of `343` disagree); "every code is principal" (fails in the wild
  regime: `1125` of `1221`); the hull dimension determining the hull; and the trivial
  scalar unit action. Boundary: the zero code and the ambient code `R_n` both have
  hull `0` (so `𝔟_s` is non-degenerate on `R_n` in every case tested).
* **Not attempted** (T-175): Gray maps, CSS/EAQECC, quantum parameters, manuscript.
  No hull enumerator is read as a quantum-code parameter.
* **Regression.** Stage 2A (no failures), 2B `460/460`, 2C `596/596`, 3A `583/583`
  re-run unchanged, each reproducing its committed log byte-for-byte; the 77-file
  start-of-stage baseline is unchanged.

---

## Phase 4 — Gray map compatibility (Tasks A–H)

`phase4_gray_map_compatibility.py` → `phase4_gray_map_log.txt`
(1106 lines, **463 checks, 463 PASS, 0 FAIL** — 311 `[EXH]`, 152 `[SMP]` —,
seed 20261110, two runs byte-identical, SHA-256 `55656a9d…9a92`).
Deliverable: `03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md`.

* **Task A** — the candidate maps $\varphi_A:A_t\to\mathbb F_q^t$,
  $\varphi_R:R\to\mathbb F_q^{4t}$, $\varphi_n:R^n\to\mathbb F_q^{4tn}$
  (coefficient expansion: coordinate $((e\cdot4+k)t+a)$). Each is $\mathbb F_q$-linear,
  additive, injective and surjective; $\varphi_nT=\widehat T\varphi_n$ with $\widehat T$
  the rotation by $4t$; none is a ring homomorphism ($R$ is non-commutative); the
  transported left regular representation $a\mapsto M_L(a)$ is an injective
  $\mathbb F_q$-algebra homomorphism $R\hookrightarrow M_{4t}(\mathbb F_q)$. Variants:
  the coefficient reversal $P$, the Bachoc-type map (for $t=2$), and a general linear
  change of coordinates $T$.
* **Task B** — four weights ($w_{\mathrm H}$, $w_{\mathrm{ent}}$, $w_{\mathrm{coef}}$,
  $w_{\mathrm{rank}}$) with the sharp chain
  $w_{\mathrm H}\le\mathrm{wt}_{\mathrm H}\varphi_n\le4t\,w_{\mathrm H}$, plus the
  homogeneous weight built from the generating character in exact integer arithmetic:
  closed form $0\,/\,1+\frac1{q^2-1}\,/\,1-\frac1{(q-1)^2(q+1)}$ on $M_2(\mathbb F_q)$,
  verified exhaustively for $q=4,8,9$; **no Hamming isometry exists for it**.
* **Task C (central)** — the transported form is
  $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$, a
  $\widehat\sigma_s$-Hermitian form with a **Hankel** Gram matrix, and
  $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$ holds for every code of
  every instance, by two independent routes.
* **Task D** — $\varphi_n(\operatorname{Hull}_s(C))=\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$,
  including the four $\mu_B=3$ (non-principal) witnesses of T-173; no principality
  hypothesis is used.
* **Task E** — the image is an $\mathbb F_q$-linear $[4tn,\dim C]_q$ code, **quasi-cyclic
  of index $4t$ and co-index $n$**, and **not** cyclic in general (measured counts, e.g.
  4 of 1220 at $(4,2,2)$ and 0 of 400 at $(4,2,3)$); minimum distances are bounded by the
  ring-Hamming distance, not equal to it.
* **Task F** — eight quantum-relevant sufficient conditions are recorded (F1–F8 of §6);
  no CSS/EAQECC is constructed and no quantum parameter is derived.
* **Task G** — two independent routes for every critical identity, `[EXH]`/`[SMP]` labels,
  and eight negative controls that must fail and do (§7).
* **Task H** — literature review and the novelty gap, with the search limitation stated
  explicitly (§8).

**Not attempted** (phase boundary): CSS construction, EAQECC construction, quantum
parameters, manuscript text.

---

## Phase 5 — quantum error-correcting code construction (Tasks A–H)

**Deliverable:** `03_THEOREMS/PHASE5_QUANTUM_CONSTRUCTIONS.md`
**Script:** `phase5_quantum_constructions.py` → `phase5_quantum_log.txt`
(88 checks, 88 PASS, 0 FAIL, seed 20261120, byte-reproducible).

The quantum framework (Weyl operators, the commutation criterion
$\operatorname{Tr}_{F_q/F_p}(a\cdot b'-a'\cdot b)=0$, $K=q^N/\lvert\mathcal C\rvert$,
the distance as a minimum symplectic weight, Knill–Laflamme) is **set up from
scratch** in §0 of the deliverable and verified on a genuine Hilbert space
($q=4$, $N=2$, $\dim\mathcal H=16$); nothing is imported for it.

* **Task A** — the induced form is T-177's $u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$;
  the general Galois, reflexive ($r\mid2s$) and per-code $\widehat\sigma_{2s}$-invariant
  regimes are separated with witnesses (T-190) and are **not** equivalent.
* **Task B** — every Galois hull is self-orthogonal, with **no** reflexivity and
  **no** principality hypothesis (T-192, proved one-sidedly); three routes are
  compared (R1 twisted/Galois-native, R2 Euclidean/CSS, R3 entanglement-assisted)
  and **R2 is recommended** where available, R1 in the obstructed cases, R3 when
  entanglement may be spent.
* **Task C** — $N_{\rm phys}=4tn$ is **derived** from $\dim_{F_q}R=4t$; the
  conversion $\Psi(u)=u(I_{4n}\otimes T)$ with $T^{\mathsf T}H_tT=I_t$ is given with
  eight verified properties; it is non-monomial for $t\ge2$, $p$ odd, and it does
  **not** exist for $p=2$, $t$ even (T-200) — the Euclidean route is then
  obstructed outright.
* **Task D** — explicit codes for the four required parameter sets $(4,1,2)$,
  $(4,2,1)$, $(4,2,2)$, $(4,2,3)$ plus $q=8,9$, **prioritising non-principal
  hulls**: $[[16,10,2]]_4$ and $[[16,8,2]]_4$ come from hulls with $\mu_B=4$
  (the O-3.1 witness family of T-173).
* **Task E** — parameters $[[N,K,d]]_q$ proved for all three routes (T-201);
  the best distance found is $d=3$ ($[[16,4,3]]_4$ and $[[8,4,3;4]]_4$).
* **Task F** — quantum Singleton and Hamming bounds verified for all codes
  (T-202); **no claim of record parameters** (Grassl's tables are not reachable
  offline — O-5.4).
* **Task G** — per-code verification, seven negative controls, and
  PROVED / COMPUTATIONALLY VERIFIED ONLY / CONJECTURE / OPEN labels throughout.
* **Task H** — literature recorded; `01_LITERATURE/references.bib` extended by
  nine entries (Greferath–Schmidt 1999, Greferath–O'Sullivan 2004,
  arXiv:1409.7228, Calderbank–Shor, Steane, Gottesman, Knill–Laflamme,
  Wilde–Brun, Rains), every one carrying a `VERIFY` note.

**Not attempted** (phase boundary): manuscript text, journal submission material.
