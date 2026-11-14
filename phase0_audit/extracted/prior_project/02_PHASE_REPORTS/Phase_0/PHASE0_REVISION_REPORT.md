# Phase 0 — Revision and mathematical validation
## Master report for the three assigned tasks

**Date:** 2026-11-04 · **Branch:** `arena/59de606f-matrix-ring` · **Phase control: Phase 0
only** — no Phase 1–8 theorem is proved here and no manuscript is drafted.

**Working title (unchanged):** *Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings*.

---

## 0. Executive summary

| Task | Requirement | Outcome |
|---|---|---|
| **1** | Nontrivial Galois automorphism + a valid non-degenerate pairing, for $q=4,8,9$ (not $q=2$), with code and exact outputs | **DONE.** $\sigma_s$ ($s\not\equiv0\bmod r$) and $\theta_s=\sigma_s\circ{}^{\mathsf T}$ built; pairing $\langle x,y\rangle_s=\sum\theta_s(x_i)y_i$ verified on **all** cyclic codes in four exhaustive parameter sets ($q=4,8,9$; six runs counting both $s$ at $q=8$) + one 1200-code sample + one $t=2$ set. Every required property holds 100 % **except reflexivity, which holds iff $r\mid2s$** (343/343 at $q=4$; 144/144 and 1200/1200 at $q=9$; **35/737 at $q=8$**). The plain product pairing fails the size formula in every parameter set. |
| **2** | Complete proofs of additivity, $\theta_s(AB)=\theta_s(B)\theta_s(A)$, non-degeneracy, left/right module compatibility, the size/dimension formula, the double-dual, and cyclicity of the dual | **DONE** in `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` (§0–§6, plus the new reflexivity criterion Thm 3.9). Every statement is tagged `[PROVED-HERE]` / `[STANDARD]` / `[CONDITIONAL]` / `[COMPUTATIONAL]`. |
| **3** | Compare and reconcile with Alahmadi–Sboui–Solé–Yemen (A1), re-checking their Lemmas 2/4 and Theorems 1/2 with code | **DONE.** Their ring rebuilt from their own $i,\omega,u$; exhaustive censuses (5 codes at $n=1$, **35** at $n=3$); three readings of Thm 1 tested; Lemma 4 and Thm 2 tested. A clean discrepancy is documented (their parametrization covers at most 15 of the 35 codes) **with no claim that A1 is wrong** — one likely cause is identified (factorization over the non-central $\mathbb F_4$ instead of the centre $\mathbb F_2$). |

**Net verdict: MODIFY — conditional GO, with the parameter restriction sharpened to
$q=p^{2e}$, $s=r/2$.** See `UPDATED_PHASE0_FINAL_RECOMMENDATION.md`.

---

## 1. Notation and conventions (fixed once, used everywhere)

* $p$ prime, $q=p^{r}$, $A_t=\mathbb F_q[u]/\langle u^{t}\rangle$ ($t$ = nilpotency
  exponent), $R=M_m(A_t)$, $R_n=R[X]/\langle X^{n}-1\rangle$ with **$X$ central**.
* **Code** = right ideal of $R_n$ = shift-closed right $R$-submodule of $R^{n}$. Two-sided
  codes are excluded (they are Morita-equivalent to commutative codes and kill novelty).
* $\sigma_s(a)=a^{p^{s}}$ applied **entrywise** to the $\mathbb F_q$-coefficients ($u$ is
  fixed); $s$ is the Galois parameter; $k$ is never overloaded.
* $\theta_s=\sigma_s\circ{}^{\mathsf T}$; $\lambda(\sum a_iu^{i})=a_{t-1}$;
  $\Lambda=\lambda\circ\operatorname{tr}$.
* $\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i$; $C^{\perp_s}=\{y:\langle x,y\rangle_s=0\
  \forall x\in C\}$; $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$.

---

## 2. Task 1 — the experiments

Full record: `02_PHASE_REPORTS/Phase_0/NONTRIVIAL_GALOIS_EXPERIMENTS.md`.
Code: `04_COMPUTATION/galois_duality_experiments.py`, `galois_t2_check.py`.
Logs: `04_COMPUTATION/galois_experiments_log.txt`, `galois_t2_log.txt`.

**Headline numbers** (`[EXH]` unless marked):

| parameters | #codes | dual right module | size formula | hull closed | double dual $=\sigma_{2s}(C)$ | **reflexive** | plain size formula |
|---|---|---|---|---|---|---|---|
| $q=4,m=2,n=3,s=1$ | 343 | 343/343 | 343/343 | 343/343 | 343/343 | **343/343** | 8/343 |
| $q=8,m=2,n=3,s=1$ | 737 | 737/737 | 737/737 | 737/737 | 737/737 | **35/737** | 4/737 |
| $q=8,m=2,n=3,s=2$ | 737 | 737/737 | 737/737 | 737/737 | 737/737 | **35/737** | 4/737 |
| $q=9,m=2,n=2,s=1$ | 144 | 144/144 | 144/144 | 144/144 | 144/144 | **144/144** | 4/144 |
| $q=9,m=2,n=4,s=1$ | 1200 `[SMP]` | 1200/1200 | 1200/1200 | 1200/1200 | 1200/1200 | **1200/1200** | 2/1200 |
| $q=4,t=2,m=2,n=1,s=1$ | 32 | 32/32 | 32/32 | 32/32 | 32/32 | **32/32** | 2/32 |
| $q=2$ (enumerator validation only) | 5 / 35 | — | — | — | — | — | — |

$\sigma_s$ is nontrivial with explicit witnesses ($2\mapsto3$ at $q=4$; $2\mapsto4,7$ at
$q=8$; $3\mapsto7$ at $q=9$) and is the identity at $q=2$ (excluded from all Galois
claims). $\theta_s^2=\sigma_{2s}$ always; $\theta_s$ is an involution **only** at $q=4$
and $q=9$ here, **never** at $q=8$ — reported as such, not assumed.

---

## 3. Task 2 — the proofs

File: `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` (§0 conventions, §1 the maps, §2 pairing
properties, §3 the six required properties, §4 $R$-valued $=$ $\Lambda$-valued, §5 what
fails for the plain product, §6 summary table, plus the new §3.9 reflexivity criterion).

**Proved here:** $\sigma_s\in\operatorname{Aut}$ with $\sigma_s=\mathrm{id}\iff r\mid s$;
$\theta_s$ anti-automorphism; $\theta_s^2=\sigma_{2s}$; $\Lambda$ symmetric, associative,
non-degenerate, ideal-catching; additivity; right-$R$-linearity in $y$;
$\theta$-semilinearity in $x$; non-degeneracy and the bijection onto
$\operatorname{Hom}_R(R^n_R,R_R)$; the dual of **any** subset is a right module; the dual
of a cyclic code is cyclic; $|C||C^{\perp_s}|=|R|^n$; $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$;
reflexivity $\iff r\mid2s$; the hull is a right module, cyclic if $C$ is; the $R$-valued
and $\mathbb F_q$-valued duals coincide.

**Conditional:** principality of every right ideal (proved when $t=1$ **and**
$X^n-1$ is squarefree; open for $t\ge2$ or $p\mid n$).

**Still open (and must stay open in Phase 0):** hull-dimension formulas, the Gray map, and
everything quantum.

---

## 4. Task 3 — reconciliation with A1

Full record: `02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md`.
Code: `04_COMPUTATION/alahmadi_reconciliation.py`; log:
`04_COMPUTATION/alahmadi_reconciliation_log.txt` (exit 0, ≈ 11 s).

* Their ring is reproduced exactly from their generators ($i^2=I$, $\omega^2+\omega+I=0$,
  $i\omega=\omega^2i$, $u^2=0$, $\omega u\ne u\omega$).
* **Census (exhaustive, two independent methods):** 5 cyclic codes at $n=1$, **35** at
  $n=3$. Closed form: factor $X^n-1$ over the **centre** $\mathbb F_2$ →
  $R_3\cong M_2(\mathbb F_2)\times M_2(\mathbb F_4)$ → $5\times7=35$.
* **Lemma 2** at $n=1$ ($A[X]/(X-1)\cong A$): the list $(0),(u),(1)$ is **incomplete** —
  there are 5 right ideals, the extras being the column-space ideals
  $\langle(0,1)\rangle,\langle(1,0)\rangle$ ($uA$ has column space $\langle(1,1)\rangle$).
* **Theorem 1**, three readings: R1 (consistent with "torsion generator $=f$") → 9 of 27
  triples are right ideals; R2 (literal) → 4; R3 (right ideal generated) → 27 triples but
  only 15 distinct codes. Even R3 covers only 15 of the 35 codes.
* **The diagnostic:** for R1, $C$ is a cyclic code **iff** $f,g,h\in\mathbb F_2[X]=Z(A)[X]$
  — 9 vs 0 vs 0 vs 18 at $n=3$ and 3 vs 0 vs 0 vs 0 at $n=1$, no exceptions in either
  direction. Working triples $=3^{\#\mathbb F_2\text{-factors}}=3^2=9$, not $3^3=27$.
* **Duality:** their form $\sum x_jy_j$ is degenerate on $R_3$ ($\dim C+\dim C^\perp$
  takes the values $6,8,10,12$; 0 self-dual codes), while $\sum x_j^{\mathsf T}y_j$
  satisfies $\dim C+\dim C^\perp=12$ for all 35 codes and admits 3 self-dual codes
  ($|C|=64$). Lemma 4 matches 3/27 (their form) and 5/27 (transpose); 3/9 and 5/9 on the
  9 central triples. Their Thm-2 criterion $h=h^*, g=f^*$ holds for 3 triples, of which
  exactly one gives a self-dual code — under the **transpose** form.
* **No claim that A1 is wrong.** Three reconciling conventions are listed, and three
  checks that would settle it (§7 of the reconciliation document).

---

## 5. Deliverables produced by this revision

| # | File | Task |
|---|---|---|
| 1 | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` | 2 |
| 2 | `04_COMPUTATION/galois_duality_experiments.py` + `galois_experiments_log.txt` | 1 |
| 3 | `04_COMPUTATION/galois_t2_check.py` + `galois_t2_log.txt` | 1 (extension) |
| 4 | `04_COMPUTATION/alahmadi_reconciliation.py` + `alahmadi_reconciliation_log.txt` | 3 |
| 5 | `02_PHASE_REPORTS/Phase_0/NONTRIVIAL_GALOIS_EXPERIMENTS.md` | 1 |
| 6 | `02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md` | 3 |
| 7 | `02_PHASE_REPORTS/Phase_0/PHASE0_REVISION_REPORT.md` (this file) | all |
| 8 | `02_PHASE_REPORTS/Phase_0/UPDATED_PHASE0_FINAL_RECOMMENDATION.md` | all |
| 9 | `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` (supersedes, does not delete, `theorem_register.md`) | 2 |
| 10 | `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` | 1, 3 |
| 11 | updates to `PROJECT_DECISION_LOG.md`, `CHANGELOG.md`, root `README.md`, `06_AUDIT/Phase0_audit_request.md` | all |

---

## 6. What is still unresolved (short list; full list in the recommendation §8)

* **U8** — the A1 convention question (centre vs $\mathbb F_4$; right/left/two-sided
  generation). *Adjudication requested.*
* **U9** — is reflexivity actually required for the intended quantum construction? If
  not, the $q=p^{2e}, s=r/2$ restriction can be relaxed. *Adjudication requested.*
* **U10** — $t=2$ computations only at $n=1$.
* **U5–U7** — principality for $t\ge2$, the Gray map, hull-dimension formulas (all Phase
  1+ work, deliberately untouched).
* **U1–U4** — literature bookkeeping (no papers in the repo; two DOIs to confirm; one
  item on the do-not-cite list).

---

## 7. Standing rules honoured in this revision

* No invented citations, theorems, proofs, computations or files.
* No fabricated computational results: every number has a script and a log.
* $q=2$ is never used as Galois evidence.
* $\theta_s$ is never called an involution without the $r\mid2s$ check.
* No claim that A1 is incorrect.
* Previous versions of files were updated, not deleted (`theorem_register.md` is kept).
* Conditional and established results are labelled separately everywhere.
* $t$ = nilpotency, $s$ = Galois parameter; $k$ is never overloaded.
* Phase control: Phase 0 only.
