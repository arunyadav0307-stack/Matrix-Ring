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
* `03_THEOREMS/PHASE7_EXTENDED_SEARCH.md` — the Phase-7 deliverable (§0
  conventions, §1 Task B + census, §2 Task C, §3 Task A and O-6.1, §4 Task D
  and O-6.4, §5 Task E certification, §6 Task F recheck and errata, §7 Task G
  bounds and literature, §8 Task H controls, §9 register rows, §10 resolution
  of O-6.1 … O-6.6, §11 open problems O-7.1 … O-7.6, §12 completion report).
* `04_COMPUTATION/phase7_extended_search.py` and its log
  `04_COMPUTATION/phase7_extended_search_log.txt` (639 lines, **17 checks, 17
  PASS, 0 FAIL**, seed 20261210, ≈1050 s, SHA-256 `634a63d3…c35eb`).

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
