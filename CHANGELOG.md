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

---

## Phase 1 — final verification, supplementary conventions and audit package
*(2026-11-04, branch `arena/59de606f-matrix-ring`)*

### Added
* **`03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` §5.6** — "Left and right actions: complete
  conventions" (Task-C clarification). Documents, with side and coordinate formula, the four
  actions on `R = M_2(A_t)` (A1 right/columns, A2 left/rows, A3 `σ_k`, A4 `θ_s`), the
  actions on `R_n` and on code coordinates (B1 right `R`-action, B2 left `R`-action,
  B3 `X` = shift `T`, B4 `σ_k`, B5 `θ_s`), Morita in **both** handednesses, and:
  * **Lemma 5.6a** — the five pairing/action identities, e.g.
    `B_s(a·x, y) = B_s(x, θ_s(a)·y)` and `B_s(x, a·y) = B_s(θ_s^{-1}(a)·x, y)`;
  * **Lemma 5.6b** — for an **arbitrary** subset both orthogonals are right `R`-submodules
    (this strengthens Lemma 5.5, whose hypothesis is unnecessary); if the subset is a left
    `R`-submodule, both orthogonals are left submodules too (hence subbimodules);
  * **Remark 5.6c** — at `n = 1` the orthogonal of a left ideal is two-sided, i.e. one of
    the `t+1` ideals `u^iR`.
* **`04_COMPUTATION/module_actions_checks.py`** + `module_actions_log.txt` — 276 new
  checks (**276/276 PASS**, deterministic: two consecutive runs are byte-identical),
  covering §5.6 and including a brute-force cross-check of the orthogonal encoding.
* **`03_THEOREMS/UPDATED_THEOREM_REGISTER.md`** — rows **T-030 … T-043** for the Phase-1
  results (structure of `A_t` and `M_2(A_t)`, Morita both handednesses, `R_n ≅ M_2(B)`,
  `σ_s`/`θ_s` orders, Lemma 5.6a/b, the pairing package, the regime-dependent theorems,
  the cyclic-code counts, the withdrawn claim, and the Phase-1 scope).
* **`PHASE1_FINAL_AUDIT_PACKAGE.zip`** (24 entries) + `06_AUDIT/PHASE1_FINAL_AUDIT_MANIFEST.md`
  — hand-off bundle with a SHA-256 manifest; CRC test OK, 23/23 content hashes verified
  from inside the archive.

### Corrected
* **Remark 5.6 (last clause) is withdrawn** (register row **T-042**): it asserted that the
  left-handed closure "fails in general"; by Lemma 5.6b(2) the orthogonal of a left module
  *is* a left module. The premise of the remark (that `B_s(a·x,y)` is not a left multiple
  of `B_s(x,y)`) is correct, and a witness is printed in the computation log. Nothing in
  §§6–8 depends on the withdrawn clause.

### New computational facts (exhaustive over the `B`-submodule lattice)
* Cyclic-code counts `7 / 33 / 343 / 12 / 144 / 11 / 93 / 33` for
  `(q,t,n) = (4,1,1), (4,1,2), (4,1,3), (9,1,1), (9,1,2), (8,1,1), (8,1,2), (4,2,1)`.
  `343 = (q+3)^3` and `144 = (q+3)^2` confirm T-018 where `X^n−1` is squarefree;
  **`93 ≠ 121` at `q=8, n=2`** is a second confirmation (after `33 ≠ 49`) that the
  squarefree hypothesis is essential.
* Lemma 5.6b(2) holds for **every** left ideal enumerated (`0` failures out of
  `7, 33, 343, 12, 144, 11, 93, 33`) and the test is non-vacuous.
* Both logs regenerated and verified reproducible byte-for-byte;
  `ring_structure_log.txt` is byte-identical to the copy at commit `2e627b8`.

### Known open items carried forward (unchanged)
T-006 (entry-wise failure uncharacterised), T-021 (principality for `t ≥ 2` or `p ∣ n`),
T-027 (general `τ ∈ Aut(A_t)` undeveloped), hull-dimension formulas (Phase 4), Gray map
(Phase 5), quantum construction (Phase 6, regime R3 needs the hypothesis of Theorem 7.4).

---

## 2026-11-06 — Phase 5: Quantum Error-Correcting Code Construction (Tasks A–H)

**New deliverable:** `03_THEOREMS/PHASE5_QUANTUM_CONSTRUCTIONS.md`
**New script/log:** `04_COMPUTATION/phase5_quantum_constructions.py` →
`phase5_quantum_log.txt` (88 checks, 88 PASS, 0 FAIL, seed `20261120`, ≈ 80 s,
two runs byte-identical, log SHA-256 `055a8af0…6cd1`).

The quantum framework (Weyl operators over `F_q`, commutation
`⟺ Tr_{F_q/F_p}(a·b' − a'·b) = 0`, `K = q^N/|C|`, the distance as a minimum
symplectic weight, Knill–Laflamme) is built from scratch and verified on a genuine
Hilbert space (`q = 4`, `N = 2`, `dim = 16`).

### Results (register rows T-190 … T-203)
* **T-190** the general-Galois / reflexive (`r | 2s`) / per-code
  `σ̂_{2s}`-invariant regimes are pairwise **non-equivalent** (witness
  `(8,1,2,1)`: 14 of 92 codes are `σ̂_2`-invariant and exactly those satisfy
  `D^{⊥⊥} = D`).
* **T-191/T-192** the transported form is Euclidean `⟺ t = 1 ∧ r | s`; **every
  Galois hull is self-orthogonal**, with no reflexivity and no principality
  hypothesis (226 hulls, `[EXH]`).
* **T-193 … T-197** three construction routes — R1 Galois-native twisted
  embedding (`[[N,N−k,d]]_q`, `d ≤ min wt(D^{⊥_E})`), R2 Euclidean/CSS
  (`[[N,N−2k,d]]_q` / `[[N,2k−N,d]]_q`), R3 entanglement-assisted
  (`[[N,N−k−h_E,d;k−h_E]]_q`) — compared; **R2 recommended** where available,
  R1 in the obstructed cases, R3 when entanglement may be spent.
* **T-198 … T-200** `N_phys = 4tn` **derived**; the form conversion
  `Ψ(u) = u(I_{4n} ⊗ T)`, `TᵀH_tT = I_t`, with eight verified properties, is
  non-monomial for `t ≥ 2`, `p` odd, and **does not exist** for `p = 2`,
  `t` even (alternating obstruction) — the Euclidean route is then impossible.
* **T-201/T-202** parameters proved; all 17 constructed codes satisfy the quantum
  Singleton and Hamming bounds.
* **T-203** commutation must be tested on an `F_p`-basis
  (`Tr_{F_4/F_2}(1) = 0`): the naive `F_q`-generator test would report `d = 1`
  for a code whose distance is `3`.

### Explicit codes
`[[8,4,2]]_4`, `[[12,8,2]]_4`, `[[16,4,3]]_4` (Knill–Laflamme with `t = 1`
verified over 58 081 error pairs), `[[8,4,2]]_8`, `[[8,4,2]]_9`,
`[[8,4,2]]_9` (via `Ψ` at `(9,2,1)`), `[[24,16,2]]_4`, `[[24,8,2]]_4`, and —
**prioritising non-principal hulls** — `[[16,10,2]]_4` and `[[16,8,2]]_4` from
hulls with `µ_B = 4` (the O-3.1 witness family of T-173).
Entanglement-assisted: `[[8,4,3;4]]_4`, `[[12,10,2;2]]_4`, `[[16,12,2;0]]_4`.

### Verification and safeguards
Seven negative controls (N1a, N1b, N2, N3, N4, N5, A4b) fail as they must.
Regression: Stage 2A 429/429, 2B 460/460, 2C 596/596, 3A 583/583, 3B 206/206,
Phase 4 463/463 — each reproducing its committed log byte-for-byte.  Protected-file
baseline (83 files, list SHA-256 `4e3814b1…9b66`): 78/78 files other than the five
append-only documents (`references.bib`, theorem register, computation README,
computation inventory, decision log) are byte-identical.

### Open problems newly recorded
O-5.1 (`d ≥ 3` for `t ≥ 2`?), O-5.2 (is `d_R1 = min wt(D^{⊥_E})`?), O-5.3 (EA
defect for the semilinear group `C_T`), O-5.4 (comparison with Grassl's tables —
not reachable offline; required before any manuscript text), O-5.5 (per-code `µ_B`
census), O-5.6 (R1 distance search capped at symplectic weight 2 for `N = 16`).

**Boundary honoured:** no manuscript text and no journal-submission material.
