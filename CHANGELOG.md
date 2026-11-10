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
two runs byte-identical, log SHA-256 `dd4962cc…d03a0`, 491 lines).

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

---

## 2026-11-06 — Phase 6: Quantum Parameter Enhancement, Exact Distance Certification and Novel Code Construction (Tasks A–I)

**Scope.** Systematic search over the whole accessible range, **exact** distance
certification, re-derivation of the O-3.1 witnesses, the exact domain of the
characteristic-two obstruction, parameter verification, and the literature
comparison that O-5.4 had declared impossible offline. No manuscript text.

### Added
* `03_THEOREMS/PHASE6_QUANTUM_PARAMETER_ENHANCEMENT.md` — the Phase-6
  deliverable (§0 conventions and the corrected distance framework, §1 Task A,
  §2 Task B + Pareto frontier, §3 Task C certification, §4 Task D non-principal
  hulls, §5 Task E obstruction, §6 Task F negative controls, §7 Task G
  parameters, §8 Task H bounds + literature, §9 Task I search report, §10
  register rows, §11 resolution of O-5.1 … O-5.6, §12 open problems O-6.1 … O-6.6,
  §13 completion report).
* `04_COMPUTATION/phase6_quantum_parameter_enhancement.py` and its log
  `04_COMPUTATION/phase6_quantum_parameter_log.txt` (424 lines, **13 checks, 13
  PASS, 0 FAIL**, seed 20261130, two runs byte-identical, SHA-256 `985a41b2…43ee`).

### New register rows T-204 … T-215
* **T-204** parameter census: exhaustive iff $q^{2tn}\le200000$; 13 families,
  3942 codes, 2 of them seeded 300-code samples (`[SMP]`).
* **T-205** maximum certified distances: $d=3$ (stabilizer, $[[16,4,3]]_4$),
  $d\le2$ (R1), **$d=6$** (entanglement-assisted, $[[12,2,6;10]]_4$); every
  $d\ge4$ requires entanglement.
* **T-206** all 22 certified distances are exact by three independent methods
  (complete enumeration, independent support search, ambient quantum search).
* **T-207** $d=\min\mathrm{swt}(V^{\perp_\omega}\setminus V)$ for all three
  routes; $D^{\perp_E}\setminus D=D^{\perp_E}\setminus\mathrm{Hull}_E(D)$, so
  T-197's formula is the **same number** (clarified, not refuted).
* **T-208** the R1 cap is R1-only (`[EXH]`, 99 codes); R2/R3 escape it.
* **T-209** the four O-3.1 witnesses re-derived: exactly 1 at $s=0$ and 3 at
  $s=1$, $\mu_B=3$ by two implementations; $\mu_B$ census for 5 families.
* **T-210/T-211** the char-2 obstruction holds for **every** linear coordinate
  transformation ($t$ even) and **only** for $t$ even ($t$ odd: congruence
  constructed for $t=1,3,5$).
* **T-212** the J-frame CSS $A\times(JB)$ is a valid bypass but yields $d\le2$.
* **T-213/T-214** $K=N-\dim S-c$ recomputed for all 22 codes, abelian on an
  $F_p$-basis; EA Singleton and EA Hamming bounds hold.
* **T-215** **no record parameters**: 3 of 8 comparable stabilizer tuples meet
  Grassl's best known distance, 5 are 1–3 below; EA codes compared with the EA
  Singleton bound only.

### New codes (all entanglement-assisted, all exactly certified)
$[[12,2,6;10]]_4$, $[[16,4,5;8]]_4$, $[[24,4,5;12]]_4$ `[SMP]`, $[[12,2,5;6]]_4$,
$[[8,2,4;6]]_9$, $[[16,4,4;12]]_4$, $[[8,4,3;4]]_{4,8}$.

### Corrections (append-only, recorded in the register's annotations)
* **Phase 5 §6** ("no access to Grassl's code tables") — **corrected**: the
  tables are reachable at `http://www.codetables.de`; the comparison is done.
* **Phase 5 §4** — disambiguated: $\mu_B=4$ there is $\mu_B$ of the **codes**;
  the O-3.1/T-173 quantity is $\mu_B$ of the **hull** (census $\{0,1,2,3\}$).
* **T-200** — extended (every linear transformation) **and** delimited ($t$ even
  only).

### Open problems
O-5.1, O-5.2, O-5.4, O-5.5, O-5.6 **resolved**; O-5.3 **still open** (carried to
O-6.6). New: O-6.1 … O-6.6.

### Verification and safeguards
13 checks, 13 PASS, 0 FAIL; log byte-identical on two runs; the exact enumerator
cross-checked against brute force on 110 instances. Two defects found and fixed
in Phase 6's own verification are recorded in the completion report
(certification of a re-selected code; the entanglement-assisted distance tested
against $\mathrm{rad}\,V$ instead of $V$). Regressions of Phases 2A/2B/2C/3A/3B/4/5
re-run; protected Phase 0–5 files verified against the Phase-6 baseline.

**Boundary honoured:** no manuscript text and no journal-submission material.

---

## 2026-11-04 — Phase 7: Extended search for optimal quantum parameters, entanglement efficiency, and the structure of the attainable frontier (Tasks A–H)

**Scope.**  Phase 6 left four open problems that its own machinery could not
settle: the ring-component routine did not support `n = 5, 6` at `t = 1` nor
`n = 3` at `q = 8` (O-6.3), the `µ_B ≥ 3` hull phenomenon was seen in one
family only (O-6.4), the entanglement budget of the high-distance codes was
unmeasured (O-6.1), and the `t ≥ 2` barrier was unquantified (O-6.2).  Phase 7
replaces the component routine by a general CRT decomposition, re-runs the
whole search over the enlarged family list, and answers all four.  No
manuscript text.

### Added
* `03_THEOREMS/PHASE7_EXTENDED_SEARCH.md` — the **first** Phase-7 deliverable
  (v1).  **Preserved unchanged**; superseded on the same day by
  `PHASE7_LONGER_LENGTH_AND_PARAMETER_OPTIMIZATION.md` (see the entry below),
  which extends it to the full Task A–H specification.  Nothing in v1 is
  retracted.
* `04_COMPUTATION/phase7_extended_search.py` and its log
  `04_COMPUTATION/phase7_extended_search_log.txt` (639 lines, **17 checks, 17
  PASS, 0 FAIL**, seed 20261210, ≈1050 s, SHA-256 `634a63d3…c35eb`).  The v1
  log is preserved verbatim as
  `04_COMPUTATION/phase7_extended_search_log_v1.txt` (SHA-256
  `634a63d3…c35eb`); the canonical `…_log.txt` now holds the v2 run described
  below.

### New register rows T-216 … T-229
* **T-216/T-217** a general CRT decomposition
  `B = A_t[X]/(X^n−1) = ∏_j A_t[X]/(g_j^{e_j})`, implemented as an `F_q`-linear
  isomorphism, reproduces the Phase-3B exhaustive BFS **as a set** on all ten
  supported families; `(4,1,5)` (`N=20`, 2527 codes), `(4,1,6)` (`N=24`, 35937)
  and `(8,1,3)` (`N=12`, 737) become exhaustive, and ten families Phase 6 could
  only sample are now exhaustive.  **O-6.3 resolved.**  Census: 42 families, 23
  exhaustive, 4 counted-only, 15 blocked by the component BFS.
* **T-218** 25 families, 120721 codes with invariants, 5055 with a distance
  (4418 exact, 637 proved lower bounds); largest exact distance `d = 10`.
* **T-219 / E-7.1** the corrected bookkeeping: `k` even,
  `K − c = N − 2k ≡ 0 (mod 4)`, `c + K = N − 2h_E`, `c ≥ 2k − N`.
  **Erratum E-7.1**: Phase 6 §12 (O-6.1) states `c + K = N − k`; that is wrong
  (only 2 of Phase 6's own 25 Pareto rows satisfy it).  No Phase 6 *parameter*
  is affected.
* **T-220 / T-221** **O-6.1** answered: with `c ≤ 4` the frontier is `d = 4`
  (`[[24,10,4;2]]_9`, `K = 10`); `d = 5` costs `c ≥ 2` and leaves `K ≤ 6`;
  `d = 6` costs `c = 10`.  **O-6.2** answered: the stabilizer routes give
  `d ≤ 4` at `t = 1`, `d ≤ 2` at `t = 2`, and `d = 1` (no detection at all) for
  `t ≥ 3`; the entanglement-assisted route reaches `d = 6` at `t = 2` and
  `d = 4` at `t = 3`.
* **T-222 … T-224** a structure theorem for `µ_B` (chain ring `⟺` `t = 1` or
  `e_j = 1`; `µ_B(W) = max_j µ_{B_j}(W_j)`; `µ_B ≥ 3` **requires** `t ≥ 2` and
  `p | n`; and the bound `µ_B ≤ 2` is **false** over non-chain local rings).
  **O-6.4 answered: `µ_B(Hull_s) ≥ 3` reappears at `(9,2,3)` and `(4,2,4)`, not
  at `(8,2,2)`**, via the deterministic family `W = m^i e_1 ⊕ U`,
  `U ≤ ann_{B^2}(m)`.
* **T-225/T-226** 28 headline codes certified by three independent methods; the
  new search reproduces or improves every shared Phase-6 Pareto distance (3
  improved, 5 equal), and Phase 6's "no stabilizer `d ≥ 4`" is **re-scoped** to
  the families Phase 6 scanned (`N ≤ 16`).
* **T-227/T-228** 5055 codes, 0 EA-Singleton and 0 EA-Hamming violations;
  literature comparison limited to `GF(4)` (see the correction below), 5 of 12
  comparable stabilizer entries meet the best known distance, 7 are 1–2 below.
  **No record is claimed.**

### New codes (all certified; stabilizer ones marked)
`[[20,2,10;18]]_4`, `[[24,2,10;18]]_9`, `[[20,4,9;16]]_9`, `[[24,4,9;20]]_4`,
`[[16,2,8;14]]_9`, `[[16,2,7;10]]_9`, `[[12,2,6;10]]_4`, and — the first
stabilizer distance 4 in this framework — **`[[24,8,4]]_9` (SO)** and
**`[[20,4,4]]_4` (DC)**.

### Corrections (append-only, recorded in the register's annotations)
* **E-7.1** — Phase 6 §12 (O-6.1): `c + K = N − k` is wrong; correct is
  `c + K = N − 2 h_E`.
* **T-205** — re-scoped: "no stabilizer point has `d ≥ 4`" holds for the
  families Phase 6 scanned (`N ≤ 16`); `(4,1,5)`, `N = 20`, has `d = 4`.
* **T-215** — corrected in one respect: `codetables.de` does **not** tabulate
  `q = 8` ("currently not available for q=8"), so of the alphabets used here
  only `GF(4)` can be compared.  The conclusion (no record) is unchanged.

### Open problems
O-6.1, O-6.2, O-6.3, O-6.4 **resolved**; O-6.5 **still open** (and worse than
recorded: there is no table for `q = 8` or `q = 9` either); O-6.6 **still
open** (carried to O-7.6).  New: O-7.1 … O-7.6.

### Verification and safeguards
17 checks, 17 PASS, 0 FAIL; the run is seeded (`20261210`) and two runs of the
final script agree on every line except the per-family elapsed-time
annotations, which are wall-clock readings.  Three negative controls (N1–N3)
have teeth: a deliberately false factorisation of `X^5 − 1` is detected by the
multiplicativity test; the chain-ring test separates `F_4[u]/(u^2)` from the
wild `F_4[u,w]/(u^2,w^2)`; the product assembly is exactly the product of the
component lattices.  Protected-file baseline (89 files, list SHA-256
`60f654ba…4312a`): Phases 0–6 documents, scripts and logs verified unchanged.

**Boundary honoured:** no manuscript text and no journal-submission material.

---

## 2026-11-04 — Phase 7 (v2): longer lengths, parameter optimization, and the proved criterion behind O-6.1 (Tasks A–H, full specification)

**Scope.**  The Phase-7 brief was re-issued in an expanded form (Tasks A–H),
requiring a single deliverable named
`03_THEOREMS/PHASE7_LONGER_LENGTH_AND_PARAMETER_OPTIMIZATION.md`.  The v1
deliverable `03_THEOREMS/PHASE7_EXTENDED_SEARCH.md` and the v1 log are
**preserved unchanged** (see the entry above); v2 extends v1 rather than
replacing it.  No manuscript text.

### Added
* `03_THEOREMS/PHASE7_LONGER_LENGTH_AND_PARAMETER_OPTIMIZATION.md` (1342 lines)
  — the Phase-7 deliverable for Tasks A–H: §0 conventions, §1 Task B (general
  CRT decomposition, census, `n = 5`/`n = 6` specifically, complexity and
  memory), §2 Task C (systematic search, the four Phase-6 baselines compared,
  the non-dominated set), §3 Task A (the *proved* criterion for O-6.1, the
  entanglement budget, the coset Singleton bound), §4 Task D (O-6.4, and the
  reconciliation of Phase 5's `µ_B = 4` with the Phase-3B hull census), §5
  Task E (certification), §6 Task F (recheck of the Phase-6 obstructions and
  errata), §7 Task G (bounds and literature), §8 Task H (negative controls),
  §9 register rows T-216 … T-233, §10 resolution of O-6.1 … O-6.6, §11 open
  problems O-7.1 … O-7.6, §12 completion report and §12.1 recommended
  constructions.
* `04_COMPUTATION/phase7_extended_search_log_v1.txt` — the v1 log, preserved
  verbatim (639 lines, 17 checks, 17 PASS, SHA-256 `634a63d3…c35eb`).

### Changed
* `04_COMPUTATION/phase7_extended_search.py` gained four reporting/verification
  sections — (f) the dominance / non-dominated table, (g) the coset Singleton
  bound with the new check **H1**, (h) the comparison against the four
  Phase-6 baselines — plus a peak-resident-memory line in the completion
  report.  The **search itself is unchanged**: all v1 numbers (25 families,
  120721 codes with invariants, 5055 with a distance, every table of v1) are
  reproduced bit for bit.
* `04_COMPUTATION/phase7_extended_search_log.txt` now holds the v2 run: 727
  lines, **18 checks, 18 PASS, 0 FAIL**, seed 20261210, ≈517 s, peak resident
  memory 367.3 MB.

### New register rows T-230 … T-233
* **T-230 (PROVED)** for every route the distance is the minimum weight of the
  **quotient (coset) code** `D^{⊥_E}/Hull_E(D)`, of dimension `K = N − k − h_E`
  and length `N`; equivalently `d = min wt(D^{⊥_E} \ D)`.  Hence `d ≥ 4` iff
  every vector of weight `≤ 3` in `D^{⊥_E}` lies in `Hull_E(D)`.
* **T-231 (COMPUTATIONALLY VERIFIED ONLY)** the non-dominated parameter tuples
  of the whole search, where `(N,K,d,c)` dominates `(N',K',d',c')` iff
  `N ≤ N'`, `K ≥ K'`, `d ≥ d'`, `c ≤ c'` with at least one strict, inside one
  alphabet.  368 distinct tuples with a distance, 88 non-dominated, 280
  dominated.  This — not the single best distance — is the optimisation
  deliverable of Task C.
* **T-232 (PROVED + `[EXH]`)** **coset Singleton bound** `K + d ≤ N + 1`, from
  the injectivity of puncturing `N − d + 1` coordinates on the quotient of
  T-230.  It is neither the EA Singleton bound nor implied by it (for
  `[[20,2,10;18]]_4` it gives `K ≤ 11` where EA-Singleton allows `K ≤ 20`).
  Check **H1**: 0 violations on 5055 codes.
* **T-233 (PROVED)** **feasibility inequality**: `d ≥ 4` with `c ≤ c_0` and
  `K ≥ K_0` forces `2k ≤ N + c_0 − K_0` — the image dimension cannot exceed
  half the length by more than half the entanglement budget.

### The four Phase-6 baselines (Task C)
`[[16,4,3]]_4`, `[[12,2,6;10]]_4` and `[[16,4,5;8]]_4` are reproduced exactly
and are **non-dominated** in the new search.  `[[24,4,5;12]]_4` is **not
reproduced and is dominated**: Phase 6 obtained it at `(4,2,3)` from a 300-code
sample, and the new search enumerates that family exhaustively (35937 codes) and
finds `d = 6` there.  Phase 6's value was a sampled lower bound, not an
optimum — the baseline is improved by this phase, not refuted.

### Verification and safeguards
18 checks, 18 PASS, 0 FAIL.  Three consecutive runs of the final script
(519.9 s, 527.8 s, 516.6 s) agree on **every** line except the per-family
elapsed-time annotations `[..s]` and the peak-memory line, which are wall-clock
and resource readings; the committed log is the 516.6 s run, produced by the
committed script (SHA-256 `682e2a36…d932a0`, 2020 lines).  Protected-file baseline (89 files): Phases
0–6 documents, scripts and logs verified unchanged; the theorem register grows
by insertion only (T-216 … T-233); no Phase 0–6 file was modified; no record is
claimed; no distance is reported without an exhaustive or proved-lower-bound
computation; no sample is presented as exhaustive.

**Boundary honoured:** no manuscript text and no journal-submission material.

---

## Phase 15 — Final manuscript corrections, certification-claim accuracy and visual review package

**Branch** `arena/59de606f-matrix-ring` · **Scope** final correction phase only:
no new mathematical research, no journal submission, no Elsevier upload, no cover
letter, no repository release, no licence change.

**Corrections applied** (in `PAPER/FINAL_RESEARCHER_REVIEW_V2/`, from the working
copy `PAPER/PHASE15_WORKCOPY/`; canonical `PAPER/` untouched):

* **CP-1 — three-method claim corrected.** The manuscript claimed the 28 certified
  codes are certified by three independent methods. They are not.
  `phase7_extended_search.py::part6_certification` (lines 1672–1679) runs M2
  **only when M1 fails to complete**, so **0 of 28 codes have all three methods
  and 28 of 28 have exactly two**: one exact method (M1, or M2 where M1 cannot
  finish) plus the ambient quantum search M3 as a cross-check (a proved lower
  bound for 17 of 28). Corrected in six locations — abstract, two places in the
  Introduction, the certification methodology, the headline-table sentence and
  Appendix A. Per-code table:
  `PHASE15_FINAL_CORRECTIONS/CP1_method_applicability_table.csv`.
  The overclaim originates in the historical log itself (line 478, check
  `[EXH] E1`), which was deliberately **not** rewritten.
* **CP-2 — Example 13 (`ex:certify`, rendered Example 8.12, p. 33).** It credited
  the support search (M2), which was never run for that code (M1 completes; M2 is
  `n/a`). Method attribution corrected only. Generator matrix, parameters and all
  12 displayed numbers untouched and independently recomputed — including a
  complete enumeration of the 16 codewords of `Q = D^{⊥_E}` reproducing
  `d = 10` (weight distribution `{0:1, 10:6, 20:9}`).
* **CP-3 — appendix table numbering.** The two appendix tables rendered as
  `Table 5` / `Table 6`; per the FFA guide for authors they are now
  `Table A.1` / `Table A.2`. Main-text Tables 1–4 unchanged; no duplicate
  numbers; the appendices contain no figures and no numbered display equations,
  so `\thefigure` and `\theequation` needed no change. **Table contents
  unchanged.**
* **CP-4 — DOIs not rendered: retained, not fixed.** 9 of 13 entries carry
  `doi=`, but `plain.bst` has no `doi` field, so the PDF shows none. Retained
  deliberately because FFA applies reference formatting at proof stage. Recorded
  as a documented limitation in `OPEN_ISSUES_AND_LIMITATIONS.md` §5.1.

**Defect found and fixed during Phase 15:** the first CP-2 correction gave the
wrong reason for M2's absence ("not applicable to the entanglement-assisted
route"). The source shows M2 is skipped because **M1 already completed**,
regardless of route. The wording was corrected in three places before the final
build.

**Validation.** `tools/validate_latex.py`: 13 checks, 11 PASS / 2 FAIL — both
FAILs (V9, V11) are **pre-existing Phase 14 heuristic false positives**, present
identically before the Phase 15 edits. `tools/verify_examples.py`:
**56 checks, 0 mismatches**.

**Build** (TeX Live 2024, genuine `BibTeX 0.99d`, `plain.bst`): 0 errors, 0
undefined citations, 0 undefined references, 0 overfull, 0 underfull, 0 missing
glyphs, 0 duplicate labels (116 unique), **42 pages**, 579 531 bytes,
SHA-256 `b619cf6cb0678ab15de54c5b61536840bdaf2951aa70292ffd741a2cd01859b7`.

**Documentation.** `PHASE15_FINAL_CORRECTIONS_REPORT.md`; Phase 15 addenda
appended (append-only) to `MANUSCRIPT_SELF_AUDIT.md` and
`OPEN_ISSUES_AND_LIMITATIONS.md`; claim **T-225** corrected in place in
`CLAIM_TRACEABILITY_MATRIX.md`.

**Known open documentation defect (not fixed, deliberate).**
`PAPER/supplementary/CERTIFICATION_PROCEDURE.md` §3 still states "Every headline
code is certified by three structurally different methods." It was **not** edited
because that file is part of the committed, hash-verified supplementary package
(85-entry `MANIFEST.sha256`); rewriting it would break manifest verification and
destroy the audit trail showing where the overclaim originated. Correcting it is
a one-line change requiring a manifest regeneration, and awaits authorisation.

**Safeguards.** Canonical `PAPER/` sources, historical logs and Phase 0–14
documents untouched; `PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` (114 files)
preserved unchanged; all 23 protected baseline hashes re-verified identical.

**Stopping point.** Phase 15 is complete. No submission, no Elsevier upload, no
cover letter, no repository release, no licence change, no new research phase.
Deferred and still awaiting the researcher's separate decision: the
generative-AI declaration (researcher says language-only vs records showing
broader use), the data-availability statement (GitHub-only; supplementary data
absent from `main`), and the licence (recommendation only; nothing applied).

---

## Phase 16 — Supplementary certification documentation correction, validator resolution and package reproducibility

**Branch** `arena/59de606f-matrix-ring` · **Scope** certification documentation,
validation tooling and package reproducibility only. No new mathematical
research; no submission, no Elsevier upload, no release, no tag, no licence
change.

**Task A — method reconstruction (28 of 28, 0 discrepancies).** The
certification logic was reconstructed from the committed source, not from
summary descriptions. `phase7_extended_search.py::part6_certification`
(lines 1670–1681) runs **M2 if and only if M1 did not complete**; M3 always
runs. Every one of the 28 codes was checked against four independent sources —
the source code, Part 6 of the Phase 7 log (lines 449–478),
`parameter_tables/certified_codes.csv`, and the generator-matrix records — with
**0 discrepancies**.

| | M1 completes | M1 does not complete | total |
|---|---|---|---|
| codes | 24 | 4 | 28 |
| exact-distance method | M1 | M2 | — |
| M2 | conditionally skipped | run (exact) | — |
| M3 | run | run | 28 |
| methods executed | M1 + M3 | M2 + M3 | 2 per code |

**0 of 28 codes executed all three methods.** M3's cross-check is exact for 11
codes and a proved lower bound for 17. Applicability is **per code, not per
route**: the four M2 codes are two SO, one DC and **one EA**
(`[[24,6,4;18]]_9`), so "M2 is not applicable to the EA route" is false.
Table: `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.

**Task B — `CERTIFICATION_PROCEDURE.md` corrected.** Its §3 asserted "Every
headline code is certified by three structurally different methods", which is
false. A **second, previously unrecorded defect** was also found in the same
section: it claimed "agreement between them is a genuine cross-check", implying
M1 and M2 both run — they never run on the same code. Both corrected. The
rewritten section states what M1/M2/M3 do, quotes the conditional logic
verbatim, explains that M2 is a **fallback for M1, not a third opinion**, gives
which methods provide the exact distance and which provide cross-checks, adds a
new section on how to determine the methods used for a particular code, and
states explicitly that applicability is per code and not per route.

**Task C — historical package preserved; new authoritative version created.**
`PAPER/supplementary/` left **byte-for-byte unchanged** (manifest still 85/85).
`PAPER/SUPPLEMENTARY_V2/` created as a full copy with **exactly one file
replaced** (`CERTIFICATION_PROCEDURE.md`) plus an append-only
`SUPPLEMENTARY_CORRECTION_NOTE.md`. The other **85 files are byte-identical**,
verified by per-file SHA-256. New manifest: **86 entries, all verified**. The
Phase 7 log line 478 (`[EXH] E1`), the origin of the overclaim, was deliberately
**not** rewritten.

**Task D — a genuine inconsistency found and fixed.** M3 scans increasing
symplectic weight and returns the first hit, so a returned value is *exact*.
Appendix A asserted the blanket claim "M3 is therefore a cross-check rather than
an exact method", which **11 of the 28 records contradict**. Appendix A and
§8.5 now state the split explicitly: M3 is an independent exact determination
for 11 codes and a consistent proved lower bound for the other 17. The abstract
("each by two applicable independent methods, one exact and one a cross-check")
is accurate at the level of roles and was **left unchanged** at 235/250 words;
the precise split is carried in §8.5 and Appendix A. **No distance value or
quantum parameter changed** — all 34 parameter tuples in Appendix A are
identical to Phase 15, and no data line was touched.

**Task E — validator false positives resolved.** Both were diagnosed and both
were fixable:
* **V9** — `BUILTIN` is a hand-written closed whitelist, so format-provided
  commands (`\penalty`, `\setcounter`, `\textsuperscript`) were reported
  undefined. Fixed by adding `LATEX_KERNEL`, a bounded, named, auditable set of
  93 TeX primitives and LaTeX kernel commands. No wildcards, no per-file
  exemptions, no size-based suppression; everything else is still reported.
* **V11** — the check was **stale**, asserting the obsolete
  `\AUTHORPLACEHOLDER` regime and therefore firing on the researcher-confirmed
  metadata installed in Phase 14. Fixed by testing **conformance to the
  confirmed metadata** instead, which is **strictly stronger**: it now also
  catches a wrong name, affiliation or e-mail.

`tools/validate_latex_v2.py` was added, reporting **13 PASS / 0 FAIL**, with
`--selftest` running **12 positive and negative cases, 0 failures**. The original
`tools/validate_latex.py` is **preserved byte-for-byte** and still reports its
historic 11/2, so no earlier report is invalidated. Two harness defects were
found and fixed during this work (synthetic documents lacking `\documentclass`;
and `main.tex` containing the string `\begin{document}` twice, once inside a
comment, which truncated the preamble) — **neither affected the validator
itself**.

**Task F — final build.** `validate_latex_v2.py` **13/13 PASS**;
`verify_examples.py` **56 checks, 0 mismatches**; four-pass TeX Live 2024 build
with genuine `BibTeX 0.99d` / `plain.bst`: **0 errors, 0 undefined citations, 0
undefined references, 0 overfull, 0 underfull, 0 missing glyphs, 0 duplicate
labels, 42 pages**, 580 555 bytes,
SHA-256 `9c23bd8cdb539f0ed53ef2ae949bd6db1326dfdccf7ebc70c2b395b965bb838a`.
Appendix tables verified as **Table A.1 / A.2** with Tables 1–4 preserved;
Example 13 verified on p. 33.

**Deliverables.** `PHASE16_CERTIFICATION_DOCUMENTATION/` (8 files);
`PAPER/SUPPLEMENTARY_V2/` (86 files + 86-entry manifest);
`PAPER/tools/validate_latex_v2.py`; refreshed
`PAPER/FINAL_RESEARCHER_REVIEW_V2/` (80-entry manifest, all verified).

**Safeguards.** All Phase 0–15 files preserved; no computational log rewritten;
no generator matrix, mathematical result, distance value or quantum parameter
changed; no author metadata, funding or competing-interest declaration touched;
the original 85-entry package not overwritten; historical validator outputs not
deleted; all protected-file hashes verified before and after.

**Stopping point.** Phase 16 is complete. No submission, no Elsevier upload, no
cover letter, no repository release, no tag, no licence, no new research phase.
Deferred items (generative-AI declaration, data availability, licence, four
GitHub fixes) are carried forward with status unchanged.

---

## Phase 17 — Final certification claim review and manuscript freeze

**Branch** `arena/59de606f-matrix-ring` · decision-support and archival task
only. **The canonical manuscript was not modified.** No submission, no
publication, no release, no tag, no licence, no new research phase.

**Task A — certification logic restated mathematically.** M1 (complete
enumeration, `ENUM_CAP = 262144`, `slow_cap = 50000`); M2 (support search,
`maxw = min(8, max(3, d+1))`, exhaustive, `None` = rigorous lower bound); M3
(`w3 = 3 if N<=8 else 2`, scans symplectic weights in increasing order, so a
returned value is the true minimum and `None` proves `d >= w3+1`). M2 executes
**if and only if M1 did not complete**; M3 always executes. The distinction
between **skipped** and **inapplicable** is stated explicitly: for the 24 codes
where M1 completed, M2 is *skipped* (the branch is on `comp1`, not on the route,
and one of the four M2 codes is EA), whereas for the 4 codes where M1 returned
`(None, False)` it *did not complete* — a computational limit, not a routing
decision. Distribution confirmed: **M1+M3 = 24, M2+M3 = 4, M3 exact = 11, M3
lower bound = 17, three methods completed = 0.**

**Task B — abstract wording options prepared, none applied.** The current
sentence is accurate for all 28 records at the level of roles but silent on the
11/17 split. Three options were costed under all three established word-count
conventions (C1/C2/C3; C3 is strictest, limit 250):

| | C1 | C2 | C3 | margin |
|---|---|---|---|---|
| A — retain current | 222 | 208 | 235 | 15 |
| B — state 11/17 explicitly | 231 | 217 | 244 | 6 |
| C — most conservative | 224 | 210 | 237 | 13 |

**Material constraint found:** the natural, fuller phrasing of Option B
("...one an ambient quantum search that is itself exact for $11$ codes and a
proved lower bound for the other $17$...") measures **253 words under C3 — over
the limit**. Option B as offered is a tightened variant that fits with 6 words
to spare. **Recommendation: Option B**, because it is the only option that
removes the ambiguity at abstract level, is the most accurate of the three, and
costs 9 words. Selecting A requires **no edit at all**; B or C change **one
sentence of the abstract** and nothing else.

**Task C — consistency verified, no changes needed.** No statement anywhere
implies all three methods ran: the only "all three" occurrences in a
certification context are negations, and a rendered-PDF scan for the strings
"certified by all three methods", "all three methods ran" and "every code is
certified by three" returns **0**. M2 is described as conditionally skipped
(`08_certification.tex:357`, `appendix_tables.tex:15-17`); M3 is described as
exact for 11 and a lower bound for 17 (`08_certification.tex:179-184`,
`appendix_tables.tex:19-26`). Section 7 makes **no** method claims, so there is
nothing there to conflict. All 34 parameter tuples in Appendix A are identical to
the Phase 14 canonical file.

**Task D — referee-facing method note.** Explains why the three methods are not
all run (M2 is a *fallback for M1*, not a third opinion — M1 is already
exhaustive, so the compute is spent on M3, the only structurally independent
check), why that is appropriate, how exact distance is distinguished from a
lower bound, how the 28 records permit independent reproduction (four shipped
sources plus step-by-step re-certification), and where every artefact lives. It
states plainly what is **not** claimed, and flags that Phase 7 log line 478
(`[EXH] E1`) is wrong and was deliberately not rewritten.

**Task E — decision sheet** at
`PHASE17_RESEARCHER_DECISION/PHASE17_RESEARCHER_DECISION_SHEET.md`, with the
distribution, the three options, the recommendation and reasoning, the exact
changes each option would entail, confirmation that all mathematical parameters
are unchanged, and the remaining review items. **No option was applied
automatically.**

**Task F — visual review material preserved and indexed.** Verified that the
Phase 15 visual package remains accessible, and **regenerated the page images
from the Phase 16 build**, because Phase 16 added the 11/17 sentences to §8.5
(p31) and Appendix A (pp38-39) — pagination did not shift (abstract p1,
methodology p31, Example 13 p33, Appendix A pp38-39 in **both** builds), but
those three pages changed content, so the Phase 15 images were stale there. The
Phase 15 set was preserved alongside as `visual_review_phase15/`. Page index
provided. **Arena has no vision capability and did not inspect any page**; the
index is derived from text extraction, and the visual review is the
researcher's to perform.

**Deliverables.** `PHASE17_RESEARCHER_DECISION/` — 6 documents plus a SHA-256
manifest (6 entries, all verified):
`PHASE17_CERTIFICATION_LOGIC.md`,
`PHASE17_ABSTRACT_WORDING_OPTIONS.md`,
`PHASE17_REFEREE_METHOD_NOTE.md`,
`PHASE17_MANUSCRIPT_CONSISTENCY_REPORT.md`,
`PHASE17_VISUAL_REVIEW_INDEX.md`,
`PHASE17_RESEARCHER_DECISION_SHEET.md`.
`PAPER/FINAL_RESEARCHER_REVIEW_V2/` refreshed: 131-entry manifest, all verified.

**Safeguards.** Canonical `PAPER/main.tex` and all 13 section files verified
unchanged; `PAPER/supplementary/` (including `CERTIFICATION_PROCEDURE.md`, the
Phase 7 log, the Phase 7 script and `certified_codes.csv`) unchanged; the
original `tools/validate_latex.py` unchanged; the Phase 14 package unchanged;
all Phase 16 documents unchanged. 41 protected hashes recorded before and after;
the only change is the refreshed `FINAL_RESEARCHER_REVIEW_V2` manifest, which is
expected because the visual set was regenerated.

**Stopping point.** Awaiting the researcher's choice of abstract wording (A, B
or C) before any manuscript edit. No rebuild was performed, since no manuscript
change was made. Deferred items (generative-AI declaration, GitHub data access,
licence) carried forward with status unchanged.
