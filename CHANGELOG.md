# CHANGELOG (blueprint §9)

Every material change in scope, notation, assumptions or results.

## 2026-11-04 — Phase 0 executed (initial project setup)

### Added: project structure
```
Matrix-Ring/
├── 00_BLUEPRINT/
│   ├── Research_Blueprint.pdf                 (supplied controlling document)
│   └── Research_Blueprint_extracted_text.txt  (extract, for searchability)
├── 01_LITERATURE/
│   ├── annotated_bibliography.md   (17 verified + 4 unverified entries)
│   ├── references.bib              (BibTeX, per-entry VERIFY notes)
│   └── comparison_matrix.md        (13 rows x 9 columns + reading)
├── 02_PHASE_REPORTS/Phase_0/
│   └── Phase_0_Report.md           (main Phase-0 deliverable)
├── 03_THEOREMS/
│   └── theorem_register.md         (T-001..T-014 + imported facts E-001..E-004)
├── 04_COMPUTATION/
│   ├── matrix_ring_lib.py          (exact arithmetic library)
│   ├── phase0_feasibility.py       (experiments E1–E5)
│   ├── phase0_results.txt          (recorded log, 2026-11-04 03:52:42)
│   ├── phase0_stdout.txt           (identical copy)
│   └── README.md                   (reproducibility + completeness limits)
├── 05_MANUSCRIPT/                  (empty until Phase 8)
├── 06_AUDIT/
│   └── Phase0_audit_request.md     (copy-paste audit prompt for ChatGPT)
├── PROJECT_DECISION_LOG.md
└── CHANGELOG.md
```

### Scope / notation
* Notation fixed as required by the blueprint: $t$ = nilpotency exponent of
  $A_t=\mathbb F_q[u]/\langle u^t\rangle$; $s$ (or $\ell$) = Galois parameter;
  $k$ never used for both.
* Ring family retained as $R=M_m(A_t)$ with $m\in\{2,3,4\}$ **as alternatives
  to compare** (blueprint §2), not as an assumption.

### Assumptions changed / flagged (pending approval — see decision log D-006/7)
* **Change proposed (not yet ratified):** the Galois pairing must be built from
  the **anti-automorphism** $\theta_s=\sigma_s\circ{}^{\mathsf T}$, i.e.
  $\langle x,y\rangle_s=\sum_i\theta_s(x_i)\,y_i$, instead of the naive
  transport $\sum_i x_i\sigma_s(y_i)$ of the Fan–Zhang definition.
  *Evidence:* E3 (exhaustive, $n=1$, 3 rings) and E4 (exhaustive,
  $m=2,q=2,t=1,n=3$): the naive form is not a perfect duality for right ideals.
* **Restriction proposed:** claims involving a “Galois” parameter require
  $q=p^r$ with $r\ge2$; for $q=p$ every $\sigma_s$ is the identity (E1).
* **Convention proposed:** cyclic code = **right ideal** (matching
  Alahmadi–Sboui–Solé–Yemen 2013, Luo–Parampalli, Dinh et al., Joshi–Patel–
  Prakash), with two-sided codes explicitly excluded because they are
  Morita-equivalent to the commutative theory.

### Results (all marked conjectural / computational-only in the register)
* T-001, T-002, T-003, T-006, T-007, T-008, T-009, T-010: proposed with proof
  sketches + computational verification in a stated range.
* No theorem is claimed as proved.

### Known open items carried forward
* U1 papers absent from the repository; U2 Alahmadi-2013 re-derivation;
  U3 Nebe–Rains–Sloane anti-isomorphism reference; U4 MathSciNet novelty
  searches; U5 $R$-valued vs $\mathbb F_q$-valued definition of $C^{\perp_s}$;
  U6 positioning vs. skew-cyclic route (Si–Niu 2023); U7 scope of $t$.

---

## 2026-11-04 — Phase 0 REVISED (mathematical validation, Tasks 1-3)

### Added: revised deliverables
```
02_PHASE_REPORTS/Phase_0/
├── PHASE0_REVISION_REPORT.md              (master report for Tasks 1-3)
├── NONTRIVIAL_GALOIS_EXPERIMENTS.md       (Task 1: full experimental record)
├── ALAHMADI_THEOREM_RECONCILIATION.md     (Task 3: direct code verification of A1)
└── UPDATED_PHASE0_FINAL_RECOMMENDATION.md (supersedes Phase_0_Report.md §8)
03_THEOREMS/
├── PAIRING_COMPLETE_PROOFS.md             (Task 2: complete proofs, §0-§6 + Thm 3.9)
└── UPDATED_THEOREM_REGISTER.md            (supersedes; theorem_register.md RETAINED)
04_COMPUTATION/
├── galois_duality_experiments.py + galois_experiments_log.txt   (Task 1)
├── galois_t2_check.py           + galois_t2_log.txt             (Task 1, t=2)
├── alahmadi_reconciliation.py   + alahmadi_reconciliation_log.txt (Task 3)
└── UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md
```

### Results now PROVED (was: conjectural)
* T-002 $\sigma_s,\theta_s$ are (anti-)automorphisms; T-003 $\sigma_s$ nontrivial iff
  $r\nmid s$; T-006 the plain product $\sum x_iy_i$ is perfect for **left** modules and
  broken for **right** ones; T-007 $\theta$-duality (right-module dual + size formula);
  T-008 cyclicity of the dual; T-009 hull is a right module / cyclic; T-010 the
  $\mathbb F_q$-valued form gives the same dual; T-015 $\theta_s^2=\sigma_{2s}$
  (involution iff $r\mid2s$); T-016 $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$;
  **T-017 reflexivity iff $r\mid2s$**; T-018 enumeration formula over the central
  factorization; T-001 ($\Lambda$ part).
* Conditional: T-021 principality (needs $t=1$ and $\gcd(n,p)=1$).
* Still open: T-011 hull dimensions, T-012 Gray map, T-013/T-014 quantum.

### Assumptions changed
* **Sharpened restriction:** a *reflexive* Galois duality requires $r\mid2s$; hence the
  recommended family is $q=p^{2e}$ with $s=r/2$. At $q=8$ ($r=3$) there is no nontrivial
  reflexive choice (35/737 codes reflexive).
* **New M5:** A1's Theorem 1 / Lemma 2 structure theory is not imported; enumeration uses
  the factorization of $X^n-1$ over the **centre** $\mathbb F_q$ (validated: 343, 737,
  144, 5, 35).
* **New M6:** principality statements carry "$t=1$ and $\gcd(n,p)=1$".
* $q=2$ data is enumerator validation only, never Galois evidence.

### Computational facts added (exhaustive unless marked)
* $q=4,m=2,n=3$: 343 codes, all properties 343/343, plain size formula 8/343.
* $q=8,m=2,n=3,s=1,2$: 737 codes, all properties 737/737, **reflexivity 35/737**.
* $q=9,m=2,n=2$: 144/144; $q=9,m=2,n=4$: 1200/1200 (`[SMP]`, 1200 of 20736, seed 13572468).
* $q=4,t=2,m=2,n=1$: 32 right ideals, 32/32, plain size formula 2/32.
* $A=M_2(\mathbb F_2)$: 5 cyclic codes at $n=1$, **35** at $n=3$ (two independent
  enumerations); $\sum x_jy_j$ degenerate, $\sum x_j^{\mathsf T}y_j$ perfect with 3
  self-dual codes.

### Known open items carried forward
* U1 papers absent; U2 A1 publisher DOI; U3 Luo-Parampalli pages; U4 do-not-cite item;
  U5 principality for $t\ge2$; U6 Gray map; U7 hull-dimension formulas;
  **U8 A1 convention question (adjudication requested)**;
  **U9 is reflexivity required? (adjudication requested)**; U10 $t=2$ only at $n=1$.
