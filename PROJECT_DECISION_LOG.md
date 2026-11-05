# PROJECT DECISION LOG (blueprint §9)

Format: **date | phase | decision | rationale | approver**.

| # | Date | Phase | Decision | Rationale | Approver |
|---|------|-------|----------|-----------|----------|
| D-001 | 2026-11-04 | Setup | Created the blueprint folder structure `00_BLUEPRINT … 06_AUDIT`, `PROJECT_DECISION_LOG.md`, `CHANGELOG.md` inside the repo `Matrix-Ring` (branch `arena/59de606f-matrix-ring`). | Blueprint §9 file discipline. No approved result was overwritten (the repo contained no prior results). | Arena (self-executed structural action) |
| D-002 | 2026-11-04 | Phase 0 | **Started Phase 0 only**; deliberately did not begin Phase 1 or any later phase. | Blueprint §8D: “Do NOT prove later-phase theorems, construct quantum codes, or write the paper. Stop after Phase 0.” | Arena |
| D-003 | 2026-11-04 | Phase 0 | The controlling document is stored as `00_BLUEPRINT/Research_Blueprint.pdf` (PDF, as supplied) rather than the `.docx` named in the blueprint §9, plus a text extract for searchability. | Only the PDF was supplied by the researcher. | Arena |
| D-004 | 2026-11-04 | Phase 0 | **Repository contains no source papers** (`git log --all` shows only `README.md` and `Matrix Ring.zip`; the zip holds one empty directory entry). Literature work therefore proceeded on **web-verified sources only**, and every entry records how it was verified. | Cannot cite what cannot be read. Blueprint rule 5 forbids inventing references. | Arena — **needs researcher confirmation (U1)** |
| D-005 | 2026-11-04 | Phase 0 | Adopted the **epistemic tagging scheme** `[EST] / [PRP] / [CMP] / [LIT] / [OPN]` in the Phase-0 report. | Blueprint §8A.7: explicitly distinguish established facts, proposed definitions, conjectures, computational observations and open questions. | Arena |
| D-006 | 2026-11-04 | Phase 0 | **Proposed (not yet decided)** the $\theta_s=\sigma_s\circ{}^{\mathsf T}$ Galois pairing as the core of the framework, because the naive Euclidean/Galois dot product provably-ish fails for right ideals. | Phase-0 experiments E3/E4: 31 of 35 cyclic codes over $M_2(\mathbb F_2)$, $n=3$, have a broken duality under $\sum x_iy_i$; 0 of 35 under $\theta$. | **Pending: researcher + ChatGPT audit** |
| D-007 | 2026-11-04 | Phase 0 | **Recommendation issued: MODIFY (conditional GO)** with modifications M1–M4 (see report §8). | See report §8. | **Pending: researcher** |
| D-008 | 2026-11-04 | Phase 0 | Recorded the E5 / Alahmadi-2013 discrepancy as a **caveated observation only**; explicitly blocked any manuscript claim about that paper until a hand re-derivation is done. | Blueprint rule 5 / §8A.5: never invent or assert unverified claims about the literature. | Arena |

| D-009 | 2026-11-04 | Phase 0 (revision) | **Executed the Phase-0 revision (Tasks 1-3)**: nontrivial Galois experiments at $q=4,8,9$ (+ a $t=2$ extension), complete proofs of the pairing properties, and a code-level reconciliation with Alahmadi-Sboui-Sole-Yemen (A1). New files: `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`, `04_COMPUTATION/galois_duality_experiments.py`, `galois_t2_check.py`, `alahmadi_reconciliation.py` (+ logs), `02_PHASE_REPORTS/Phase_0/NONTRIVIAL_GALOIS_EXPERIMENTS.md`, `ALAHMADI_THEOREM_RECONCILIATION.md`, `PHASE0_REVISION_REPORT.md`, `UPDATED_PHASE0_FINAL_RECOMMENDATION.md`, `03_THEOREMS/UPDATED_THEOREM_REGISTER.md`, `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md`. | Requested by the researcher: revise and validate Phase 0 before any Phase 1. | Arena |
| D-010 | 2026-11-04 | Phase 0 (revision) | **D-006 upgraded from "proposed" to "proved".** $\theta_s=\sigma_s\circ{}^{\mathsf T}$ and $\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i$ now have complete proofs (additivity, anti-multiplicativity, non-degeneracy, right-module dual, cyclicity of the dual, size formula, double dual, hull closure, $R$-valued $=\Lambda$-valued). | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` §1-§4. | **Pending: researcher + ChatGPT audit** |
| D-011 | 2026-11-04 | Phase 0 (revision) | **New parameter restriction discovered and imposed (proposed for ratification): $q=p^{2e}$, $s=r/2$.** The duality is reflexive **iff $r\mid2s$** (register T-017); at $q=8$ ($r=3$) reflexivity fails for 702 of 737 codes, so no nontrivial reflexive Galois duality exists there. | `galois_experiments_log.txt` (35/737 at $q=8$ vs 343/343 at $q=4$, 144/144 and 1200/1200 at $q=9$) + `PAIRING_COMPLETE_PROOFS.md` Thm 3.9. | **Pending: researcher (see U9 - is reflexivity actually required?)** |
| D-012 | 2026-11-04 | Phase 0 (revision) | **A1 discrepancy reported as a discrepancy, not as an error.** Our exhaustive censuses give 5 cyclic codes at $n=1$ and 35 at $n=3$ over $M_2(\mathbb F_2)$; A1's Thm 1 parametrizes $3^3=27$ triples and, on three readings, yields at most 15 of the 35. Likely cause identified (factorization over the non-central $\mathbb F_4$ rather than over the centre $\mathbb F_2$). Do **not** import A1's structure theory; use the central factorization (register T-018). | Standing rule: never claim a published theorem is wrong without conclusive proof. `ALAHMADI_THEOREM_RECONCILIATION.md` §0, §6, §7. | **Pending: adjudication (U8)** |
| D-013 | 2026-11-04 | Phase 0 (revision) | All $q=2$ computations demoted to **enumerator-validation only**; they are explicitly not Galois evidence ($\sigma_0=\mathrm{id}$). | Standing rule from the revision request. | Arena |
| D-014 | 2026-11-04 | Phase 0 (revision) | `03_THEOREMS/theorem_register.md` is **superseded but not deleted** by `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` (statuses updated: 12 proved, 2 conditional, 4 computational-only, 6 open). | Standing rule: update without deleting previous versions. | Arena |
| D-015 | 2026-11-04 | Phase 0 (revision) | Recommendation re-issued: **MODIFY - conditional GO**, with M1-M4 (now largely executed) plus new **M5** (do not import A1's Thm 1/Lemma 2) and **M6** (principality statements must carry $t=1$ and $\gcd(n,p)=1$). | See `02_PHASE_REPORTS/Phase_0/UPDATED_PHASE0_FINAL_RECOMMENDATION.md`. | **Pending: researcher** |

## Decisions reserved for the researcher at the Phase-0 gate
* **M1** Adopt the $\theta_s$-Galois pairing (yes / no / modify)?
* **M2** Require $q=p^r$ with $r\ge2$ and take $m=2$, $t\ge1$ as the primary
  setting (yes / no)? Keep $t\ge2$ in scope (U7)?
* **M3** Fix the convention “cyclic = right ideal” and exclude two-sided codes
  (yes / no)?
* **M4** Keep the working title, or rename now?
* **M5** Do not import Alahmadi et al.'s Theorem 1 / Lemma 2 structure theory; use the
  central ($\mathbb F_q[X]$) factorization + Morita (yes / no)?
* **M6** Require the hypothesis "$t=1$ and $\gcd(n,p)=1$" on every principality
  statement until T-021 is proved in general (yes / no)?
* **U8** Adjudicate the A1 convention question (centre vs $\mathbb F_4$; right / left /
  two-sided generation of $(p)$).
* **U9** Is **reflexivity** of $C\mapsto C^{\perp_s}$ actually required for the intended
  quantum construction? If not, D-011's restriction relaxes to $r\ge2$.
* **U1** Upload the source papers to the repository.
* **U4** Run or commission the MathSciNet/zbMATH novelty searches.

---

## Phase 2 — Stage 1 — completion (2026-11-04)

Recorded after the Stage-1 deliverables were committed. **Scope constraint honoured:
definitions and shift structure only.** No P-2.3 (generator numbers), no P-2.4
(CRT/Hensel), no P-2.5/P-2.6 (principality), no P-2.7/P-2.8 (duals and annihilators), no
C-2.1, no manuscript text, and CT-0 … CT-6 were not run as a suite. Stage 2 was **not**
started.

| # | Date | Phase | Decision | Rationale | Approver |
|---|---|---|---|---|---|
| **D-016** | 2026-11-04 | 2 (Stage 1) | **Phase 2, Stage 1 (CYCLIC-CODE DEFINITIONS AND SHIFT STRUCTURE) is closed and committed as `bfb16d7`** (parent `89f00eb`, normal fast-forward; verification `553/553 checks PASS`, 91 `[EXH]` + 462 `[SMP]`, 0 FAIL, seed 20261104, ~100 s, two byte-identical runs, log SHA-256 `98383c76c957b2f4b613d97b8889c4bb39eebecf2c616edf48bc1fb1d9c5c3ef`). Deliverables: (1) `03_THEOREMS/PHASE2_STAGE1_CYCLIC_SHIFT.md` — 773 lines, §0 scope, §2 $R_n$/convolution/centrality/$\iota$, §3 actions and the shift $T$, §4 Theorem 4.1 (right ideals of $R_n$ ↔ $T$-invariant right $R$-submodules) with boundary cases and three negative controls, §5 centrality and $XT=TX$, §6 $\sigma_k$/$\theta_s$ compatibility, §7 status table, §8 computational record, §9 Stage-1 report; (2) `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` — **25 rows inserted, T-044 … T-068, insert-only** (Phase-1 rows T-001 … T-043 and planning rows P-2.x untouched); (3) `04_COMPUTATION/phase2_stage1_shift_checks.py` — 1001 lines; (4) `04_COMPUTATION/phase2_stage1_shift_log.txt` — 734 lines. | The Stage-1 items A–E of `PHASE2_PROPOSAL_v2.md` are answered with proofs (not computations) in the document; the script supplies independent evidence, including negative controls that cannot pass vacuously (non-central $Y=E_{11}$: $59\,760/65\,536$ mismatches at $(4,1,1)$ vs $0/65\,536$ for $Y=XI_2$; $\theta_s\rho_a\neq\rho_{\theta_s(a)}\theta_s$: $60\,480/65\,536$). Phase-1 files and `PHASE1_FINAL_AUDIT_PACKAGE.zip` verified byte-identical (SHA-256 `84389a1a…62c9c`) at commit time; `PHASE2_PROPOSAL_v2.md` untouched. | Researcher |
| **D-017** | 2026-11-04 | 2 (Stage 1) | **A passing script never promotes a statement.** Stage-1 results are recorded in two disjoint classes: **proved** (16 register rows marked `PROVED IN PHASE 2 STAGE 1`, plus T-044/T-046 `PROVED IN PHASE 1` and T-051 mixed), proved independently of the script by the coordinate arguments in `PHASE2_STAGE1_CYCLIC_SHIFT.md` §2–§6; and **`COMPUTATIONALLY VERIFIED ONLY`** (T-056 negative control §4.3(b); T-064 the $(4,1,1)$ subspace census; T-065 the run record), which are claims about no parameter range beyond those actually run. Every check is labelled `[EXH]` or `[SMP]` with the sample size, budget and seed on its line. | The census (exactly $7=q+3$ $T$-invariant right $R$-submodules at $(4,1,1)$, $\mathbb F_q$-dimensions $[0,2,2,2,2,2,4]$) is evidence only: it is brute force over subspaces, **without** Morita, and is not extrapolation to $n\ge2$ or to $t\ge2$. Keeping the two classes separate is what allows later stages to cite Stage-1 items without inherited overclaim. | Researcher |
| **D-018** | 2026-11-04 | 2 (Stage 1) | **Unresolved after Stage 1 — carried forward, deliberately not attempted.** (a) **`rev` (P-2.1f)** — register T-066, `PROPOSED / UNPROVED`. (b) **L-6.1** ($\theta_s$ as an anti-automorphism of $R_n$) — register T-067, `PROPOSED / UNPROVED`; RGF Lemma 4.3 states the ring-level input for $R$ and its matrix proof applies to $M_2(B)$, but the $R_n$ statement is **not** settled. (c) **T-021 principality** — untouched, still `proved (conditional)`; open for $t\ge2$ or $p\mid n$. (d) **Coverage gaps**: pair tests are sampled outside $(4,1,1)$; the only exhaustive subspace census is at $n=1$; $(4,2,2)$ ($p\mid n$, $t\ge2$, wild) is tested but no structural claim is made there. (e) **Carried forward per D3**: T-006, T-027 (the skew-polynomial comparison in §5.3(1) of the Stage-1 document is exactly this gap — $\langle X^n-1\rangle$ two-sided), T-011–T-014, warning B3.5, the Phase-1 enumeration gaps ($q=9,n=3$; no enumeration at $q=4,t=2,n=2$), and the $n\ge2$ left-submodule gap. Register T-068 records this block as `OPEN`. | These are outside Stage-1 scope by construction, not oversights: each either needs machinery Stage 1 forbids (duals/annihilators, skew-polynomial two-sidedness, CRT) or would require claims beyond the sampled parameters. They are named here so that no later stage can inherit them silently. | Researcher |
| **D-019** | 2026-11-04 | 2 | **Next stage requires explicit approval.** Stage 2 (P-2.2/P-2.3) is not started; no further computations were run; the Stage-1 proofs and scripts are frozen as committed. Documentation handover (`04_COMPUTATION/README.md`, `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md`, this log) is **append-only / insertion-only** — no existing row, table, prose or heading was altered. | The regroup plan is binding: this stage is closed on completion and the next stage starts only from an explicit go-ahead. | Researcher |

### Status after Stage 1

| Item | Status |
|---|---|
| Phase-1 tree (files, register rows T-001 … T-043, audit ZIP `84389a1a…62c9c`) | byte-identical, unchanged |
| `PHASE2_PROPOSAL_v2.md` | unchanged (`acc3ff37…`) |
| Stage-1 proofs, script and log | frozen at `bfb16d7` |
| Stage 2 | not started; awaiting approval |

---

## D-020 (2026-11-05) — Phase 2, Stage 2A completed; scope held at the authorised boundary

**Decision.** Execute **Phase 2, Stage 2A** (`PHASE2_PROPOSAL_v2.md` §3 and §5.1 only):
the Morita correspondence, the generator-number identity, and the **individual**
principality criterion. Stage 2A is now complete and the work **stops** at the authorised
boundary: no Stage 2B, no P-2.6, no duality, no hulls, no Gray maps, no quantum
constructions, no C-2.1, no manuscript.

**What was delivered.**

1. `03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md` — the correspondence in both
   directions with the row/column conventions fixed (`P = B^2` **columns**, right
   `$B$`-action by matrix multiplication, `$\mathrm{im}\,M$` = the `$B$`-span of the two
   columns); the inclusion/sum/intersection/cardinality properties; the left-ideal and
   two-sided-ideal dictionaries; the agreement of the Stage-1 cyclic-code representation
   with the Morita correspondence; **L-2.3a** proved by column packing (**no** hypothesis)
   with the projectivity-based lifting route recorded as a second proof, and
   **Proposition 3.3** showing projectivity is **not** removable for a general module
   (`$P' = B\oplus k$` over `$B=F_2[\varepsilon]/\langle\varepsilon^2\rangle$`:
   `$xS'\subsetneq I_{\mathrm{im}\,x}$`, `$2 < 4$`); **L-2.3b**, **L-2.3c**; the identity
   `$\mu_S(I_W)=\lceil\mu_B(W)/2\rceil$` (both inequalities); the individual principality
   criterion `$I_W$` principal `$\iff\mu_B(W)\le2$`; the wild counterexample
   `$(4,2,2)$`, `$W=m\oplus m$`, `$\mu_B=4$`, `$M_2(m)$` not principal; and the reduction
   of the global question.
2. `04_COMPUTATION/phase2_stage2a_morita_checks.py` (1566 lines) and its log
   `phase2_stage2a_morita_log.txt` (699 lines): **429 checks, 429 PASS, 0 FAIL** (391
   `[EXH]`, 38 `[SMP]`), seed `20261105`, **two consecutive runs byte-identical**
   (SHA-256 `3ef38b17b00ad765bdf1c77779a1481a4ae40951f28521ecb53967b90323abe5`).
3. Register rows **T-069 … T-093** (25 rows, insertion-only): 18 `PROVED IN PHASE 2
   STAGE 2A`, 6 `COMPUTATIONALLY VERIFIED ONLY`, 1 `OPEN` (T-093, the carried-forward
   limitations). No Phase-1 row (T-001 … T-043), no planning row (P-2.x) and no Stage-1
   row (T-044 … T-068) was edited.

**Two decisions taken inside Stage 2A, recorded here because they change plans.**

* **L-2.3a is proved without projectivity** (via column packing), so the identity does not
  depend on the projectivity of `$B^2$`. The projectivity-based route is kept as a second
  proof, and Proposition 3.3 records that projectivity is genuinely needed for the
  general form `$\mathrm{End}_B(P)$` — so the proposal's remark that L-2.3a "uses
  projectivity" is true of that route and false of the statement.
* **P-2.5(b) is proved for individual ideals only.** The `(4,2,2)` counterexample is an
  individual non-principal ideal; it does **not** settle the global P-2.6 and does **not**
  discharge T-021.

**Still out of scope / carried forward (T-093).** P-2.4 (CRT/Hensel) — not used;
**P-2.6 and L-2.6.1 … L-2.6.8 — untouched, `PROPOSED / UNPROVED`**; **T-021 — not
discharged** (still `proved (conditional)`, open for `$t\ge2$` or `$p\mid n$`); L-6.1 and
P-2.7/P-2.8 (register T-067); hulls, Gray maps, quantum constructions, C-2.1; CT-0 … CT-6
not run as a suite; `O-2.2` (`$\mu_B(W)\le4$` uniformly) remains open — the largest value
observed in Stage 2A is `$4$`. Carried forward from Stage 1: T-066 (`rev`), T-006, T-027,
T-011 … T-014, warning B3.5, the Phase-1 coverage gaps, the `$n\ge2$` left-submodule gap.

**Files changed by the Stage-2A commit** (all additive): the new theorem document, the new
script, the new log, `UPDATED_THEOREM_REGISTER.md` (+65), `04_COMPUTATION/README.md`
(+69), `UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` (+81), and this decision log. **Nothing
was deleted, rewritten or moved**: Phase-1 files, `PHASE2_PROPOSAL_v2.md`, the audit ZIP
and all Stage-1 files are byte-for-byte unchanged, and the push is a normal fast-forward.


---

## D-021 — Phase 2, Stage 2B: CRT/Hensel (P-2.4) and the global principality criterion (P-2.6)

**Date of decision.** 2026-11-05. **Scope.** `PHASE2_PROPOSAL_v2.md` §4 (P-2.4), §5.2
(P-2.6), and the Task-D Galois-compatibility question — **and nothing else**.

**1. P-2.6 is proved as proposed.** "Every right ideal of `R_n` is principal `⟺ p ∤ n` or
`t = 1`" is **true**; no counterexample to the statement was found, and both directions
are proved (register T-105, T-106, T-107). **O-2.1 is discharged.**

**2. P-2.4 is sharpened, not corrected.** The Hensel lifts are the base-field factors
themselves: `F_j = f_j` (T-096). The proposal asserted only `F_j ≡ f_j mod u`; the
identification is what makes `B_j = A_t[X]/⟨f_j^{p^v}⟩` with `f_j ∈ F_q[X]` and
`m_j = (u, f_j)` explicit. No error in the proposal.

**3. T-021 is superseded, not deleted.** It proved principality under `t = 1` **and**
`p ∤ n`; the correct hypothesis is the **disjunction** `p ∤ n` **or** `t = 1`, and the
converse is now proved too. T-021 keeps its own row as
`PROVED IN PHASE 1 (conditional)`; T-107 records the supersession.

**4. The three regimes are separated as instructed (mandatory point 6).** Squarefree
(`p ∤ n`), repeated-root chain ring (`t = 1`, `p ∣ n`) and **wild** (`t ≥ 2`, `p ∣ n`).
The wild components are local but **not** chain rings: `dim_{K_j}(m_j/m_j²) = 2`, so `m_j`
is not principal. No Smith normal form, no uniformizer, no shape classification and no
`(Q²+3Q+5)`-type count is used or claimed there. In particular **E-015 is cited as prior
art only and does not carry the proof** of L-2.6.4 (which is proved in full), and **E-012
is deliberately not used**: the Hensel instance needed here is proved from scratch
(T-095) because E-012's reference is unconfirmed.

**5. No uniform generator bound is assumed.** The proof of the `⇐` direction uses only
`μ_{B_j}(W_j) ≤ 2`, which follows from the Smith normal form over a chain ring. The
withdrawn v1 claim `μ_B(W) ≤ 4` (now **O-2.2**) is neither used nor needed, and remains
`OPEN`.

**6. Conventions were policed by negative controls, and one real bug was caught.** Five
controls (T-112) assert that wrong conventions **fail**: reduced modulus, rows-in-`W`,
superset-instead-of-subset, "`σ_1` fixes every component" (false — at `(4,2,3)` the
permutation is `(0,2,1)`), and the vacuity of "all principal". During development an early
version of `I_W` packed basis vectors into **rows**; all dimension and cardinality checks
still passed, and only the containment test `x ∈ I_W` exposed it. Certificate design
lesson recorded: a principality test must check **both** containment and size.

**7. Numerical agreement is not a proof.** The 460/460 result is recorded with the status
`COMPUTATIONALLY VERIFIED ONLY` (T-113) and is corroboration only. Notably, 35 937 = 33³
at `(4,2,3)` was obtained by **building** the submodules componentwise via the CRT
(`|B²| = 1.7·10⁷` forbids element scanning): the count is `[EXH]` over the 33³
combinations, but completeness rests on the theorem (T-099), corroborated by 180 random
submodules of `B²`.

**8. Task D does not anticipate the hull work.** Only the action of `σ_k` on the
components, its stability conditions, and the invariance of `μ` and principality are
established (T-109 … T-111). **No hull dimension, no dual-space formula and no quantum
construction is derived here.** Three observations are recorded for later use: the CRT
decomposition is equivariant only up to `C ↦ p^kC`; the fixed components are those with
`p^kC = C`, on which `σ_k` is an automorphism inducing Frobenius on `K_j`; and the
wild obstruction (T-106) cannot be removed by a Galois twist (T-111).

**9. Carried forward unchanged (T-114).** P-2.7/P-2.8 (hence **L-6.1**, register T-067),
hulls, Gray maps, quantum constructions, C-2.1d/e/f/g; `O-2.2`; the unenumerated wild
lattices at `(4,2,2)` and `(9,2,3)`; T-066 (`rev`), T-006, T-027, T-011 … T-014, warning
B3.5, the Phase-1 coverage gaps, the `n ≥ 2` left-submodule gap.

**10. Files changed by the Stage-2B commit** (all additive): the new theorem document
`03_THEOREMS/PHASE2_STAGE2B_CRT_PRINCIPALITY.md`, the new script and log under
`04_COMPUTATION/`, `UPDATED_THEOREM_REGISTER.md` (+21 rows, T-094 … T-114, insertion-only),
`04_COMPUTATION/README.md`, `UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` (new §10), and this
decision log (D-021). **Nothing was deleted, rewritten or moved**: Phase-1 files,
`PHASE2_PROPOSAL_v2.md`, the audit ZIP and all Stage-1 and Stage-2A files are byte-for-byte
unchanged (re-checked against the end-of-stage baseline), and the push is a normal
fast-forward.

---

## D-022 — Phase 2, Stage 2C: Galois duality, annihilators and reciprocal generators (L-6.1, P-2.7, P-2.8)

**Decision.** Execute `PHASE2_PROPOSAL_v2.md` §6 (Stage 2C) and nothing beyond it:
Task A (L-6.1 on `R_n`, proved on the normal forms rather than quoted from Phase 1),
Task B (annihilator conventions and their exact side laws), Task C (P-2.7 derived from
first principles, in principal and non-principal form), Task D (P-2.8, regime-free and
Smith-normal-form), Task E (cardinality and double-dual, with reflexivity separated),
Task F (computation with negative controls).

**Outcomes.**

1. **L-6.1 is proved** (T-115): `θ_s(uv) = θ_s(v)θ_s(u)` on `R_n`, via the convolution
   `(uv)_e = Σ u_av_b` (needs `X` central), the matrix-order swap from `θ_s(u_av_b) =
   θ_s(v_b)θ_s(u_a)`, and the re-indexing `(a,b) ↦ (b,a)`. The three levels
   `R` / `R[X]` / `R_n` are proved separately (T-116, T-117); the descent rests on
   `θ_s(X^n−1) = X^n−1` together with the centrality of `X^n−1`, which makes the ideal
   two-sided. `θ_s² = σ_{2s}` and `ord(θ_s) = 2r/gcd(r,2s)` are proved, the order being
   the same as on `R` (T-119).
2. **P-2.7 is proved and sharpened** (T-125, T-126): `C^{⊥_s} = rev(ann_r(θ_s(g)))` for
   principal `C`, and `C^{⊥_s} = rev(ann_r(θ_s(C))) = rev(⋂_i ann_r(θ_s(g_i)))` for every
   right ideal. The general form explains why one generator suffices: `θ_s` turns the
   right ideal into a **left** ideal, and left ideals, unlike right ideals, are
   annihilator-determined by their generators (T-122). Three equivalent forms and the
   Morita form `ann_r(θ_s(g)) = I_{ker θ_s(g)}` are proved and all four are tested.
3. **`rev` is proved** (T-124, discharging T-066) and is shown to be **load-bearing
   exactly when `n ≥ 3`** (T-127) — it is the identity for `n ≤ 2`, which closes the gap
   the proposal flagged in §6.4(6).
4. **L-6.5 is proved** (T-128) from P-2.7 and the Phase-1 size formula, **without** the
   import L-6.6 (`B` Frobenius, unconfirmed reference). L-6.6 is now unused.
5. **P-2.8 is proved** in two forms (T-130, T-131): regime-free
   (`C^{⊥_s} = hR_n` with `h = [w_1∣w_2]` from `ker θ_s(rev g)` whenever `μ_B ≤ 2`) and
   the proposal's Smith-normal-form formula `h_j = V_j^{-1}diag(ω^{ℓ−a},ω^{ℓ−b})` in the
   chain-ring regime (`p ∤ n` or `t = 1`).
6. **O-2.8 is answered NO** (T-132): at `(4,2,2)`, `g = diag(uε,uε)` gives
   `C^{⊥_s} = M_2(m)` with `μ_B(ker) = 4`; exhaustive scan of all 16 777 216 elements,
   none generating it. In the wild regime the Galois dual of a principal code need not be
   principal.
7. **Cardinality and double dual** (T-133): `|C||C^{⊥_s}| = |R|^n` for every `s`
   (reflexivity **not** needed); `C^{⊥_s⊥_s} = σ_{2s}(C)` for every `s`, and `= C` for
   all `C` iff `r ∣ 2s`; exhibited at `(8,1,2)` (`r = 3`), where 8 of 60 codes have a
   genuinely different double dual at `s = 1, 2`.
8. **New open problem O-2.9** (T-134): is the set of generators of a principal right
   ideal exactly the orbit `{h·u : u ∈ R_n^×}`? Exhaustively verified at `(4,1,1)`,
   `(4,1,2)`, `(4,2,1)`; unproved in general. The weaker `hR_n = h'R_n ⟺ im h = im h'`
   **is** proved.

**Safeguards honoured.** All Phase-1, Stage-1, Stage-2A and Stage-2B files are
byte-for-byte unchanged (re-checked against the start-of-stage baseline); the register
grew by insertion only (+22 rows, T-115 … T-136); no log was overwritten; the commit is a
normal fast-forward. A passing script is treated as supporting evidence only — 17 rows are
`PROVED IN PHASE 2 STAGE 2C` on the strength of the proofs in the deliverable, 4 rows are
`COMPUTATIONALLY VERIFIED ONLY`, and 1 is `OPEN`.

**Scope boundary (unchanged, T-136).** No hull dimensions (Phase 3), no hull enumeration
(Phase 4), no Gray maps (Phase 5), no quantum or CSS/EAQECC constructions (Phase 6). The
recorded-but-unused observation `Hull_s(C) = C ∩ rev(ann_r(θ_s(C)))` is logged for later
use and is **not** a quantum claim: the existence of a Galois dual does not by itself
produce a quantum code.

**10. Files changed by the Stage-2C commit** (all additive): the new theorem document
`03_THEOREMS/PHASE2_STAGE2C_GALOIS_DUALITY.md`, the new script and log under
`04_COMPUTATION/`, `UPDATED_THEOREM_REGISTER.md` (+22 rows, T-115 … T-136,
insertion-only), `04_COMPUTATION/README.md`,
`UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` (new §11), and this decision log (D-022).
**Nothing was deleted, rewritten or moved**, and the push is a normal fast-forward.
