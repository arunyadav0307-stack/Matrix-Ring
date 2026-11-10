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

## D-023 — Phase 3, Stage 3A: Galois hull structure and dimension (Tasks A–G)

**Authorised scope (Phase 3 §2–§8 only).** Tasks A–G: the definition and structure of
`Hull_s(C) = C ∩ C^{⊥_s}` (A), the hull formula (B), hull dimension theory (C), the
general versus reflexive Galois regimes (D), the LCD / self-orthogonal / self-dual
characterisations (E), computation (F) and literature comparison (G). **Excluded, by
instruction:** hull enumeration (Phase 4), Gray maps (Phase 5), CSS/EAQECC
constructions and quantum parameter claims (Phase 6), manuscript writing. **No claim is
made that a Galois hull produces a quantum code**; warning B3.5 is retained in full.

**Deliverable.** `03_THEOREMS/PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md` (922 lines, §0–§9)
with `04_COMPUTATION/phase3_stage3a_hull_structure.py` → `phase3_stage3a_hull_log.txt`
(**583 checks, 583 PASS, 0 FAIL**, 117 `[EXH]` / 467 `[SMP]`, seed `20261108`, two
consecutive runs byte-identical, log SHA-256 `478d62ff31f6…acfe2`, 792 lines).

**Main results proved.** (1) `Hull_s(C) = I_{W∩W'}` with `W = W(C)`,
`W' = W(C^{⊥_s})`, hence `dim Hull = 2 dim(W∩W')` — so the hull dimension is **always
even** — and `Hull` is principal iff `μ_B(W∩W') ≤ 2` (T-148, T-149). (2) The
non-principal formula `Hull = C ∩ rev(⋂ᵢ ann_r(θ_s(gᵢ)))`, with the side discipline
(`θ_s(ann_r I) = ann_l(θ_s I)`, `ann_r` not `ann_l`, `rev` load-bearing for `n ≥ 3` and
provably vacuous for `n ≤ 2`) and a proof that the `1`-generator formula is wrong for
non-principal codes (T-141, T-145). (3) The CRT permutation `τ = π⁻¹∘ρ` with
`(C^{⊥_s})_j = (C_{τ(j)})^{⊥_s}` and the **exact criterion `n ∣ p^s+1`** for
componentwise decomposition; when `τ ≠ id` the naive `Σ_j dim Hull_s(C_j)` fails (9/20
codes at `(4,1,3)`, `s = 0`; witness with `dim Hull = 2` versus `0`) (T-151). (4) The
three regimes are kept distinct: `dim`-equality (all `s`, T-155), set equality (reflexive
`r ∣ 2s` or codewise `σ_{2s}`-stability, T-157/T-158). (5) LCD ⟺ `C ⊕ C^{⊥_s} = R^n` ⟺
`W ∩ W' = 0`; SO ⟺ `θ_s(rev g)g = 0`; SD ⟺ SO and `2 dim C = 4tn` (T-161–T-163).
(6) **No universal closed (gcd-type) hull formula exists**: the hull need not be
principal (Stage-2C's wild `M_2(m)`), so the strongest universal statement is the
structural formula of (1) (T-154).

**Two statements were downgraded during the audit of this own document.** (i) The
dimension equality `dim Hull_s(C^{⊥_s}) = dim Hull_s(C)` was initially written as a
theorem; the proof conflated `C^{⊥_s}` with `(σ_{2s}C)^{⊥_s}`. It is now **Conjecture
H-3A.2** (T-160) and the gap is recorded in §4.1 rather than papered over. (ii) The
closed-formula question is now stated as a proved impossibility plus open problem O-3.1
rather than as an aspiration.

**Conjectures and open problems.** H-3A.1 (`Hull_s(C) ⊆ σ_{2s}(C)`, 68 nonzero hulls
tested, ~10% of them not `σ_{2s}`-stable, 0 violations) and H-3A.2 (≈680 sample codes
plus 64 probe hulls, 0 violations); **O-3.1** (is `μ_B(W_hull) ≤ 2` always? 120 wild
probes found none with `μ_B ≥ 3`) and **O-3.2** (O-3.2: the closed-formula obstruction).
Carried forward unchanged: O-2.2, O-2.4 (partially), O-2.5, O-2.6, O-2.9, the unconfirmed
import L-6.6 (now unused), T-006, T-027, T-011–T-014, warning B3.5, the Phase-1 coverage
gaps, the `n ≥ 2` left-submodule gap, C-2.1d/e/f/g.

**Novelty is narrowed (T-167).** Galois hulls over fields (Liu–Pan 2020), over
commutative chain rings (Talbi–Batoul–Fotue Tabue–Martínez-Moro, arXiv:2102.06995) and
cyclic codes over matrix rings (Alahmadi *et al.*; Islam–Prakash–Bhunia) are each
established; none of the references found treats **Galois hulls of cyclic codes over
`M_2(A_t)`**, and the absence statement is explicitly limited to this targeted search.
The candidate contribution is the combination in §7.3 — the Morita hull formula and its
parity/principality consequences, the non-principal annihilator/reversal formula, the
`τ`-permutation criterion, the regime separation and the wild-regime obstruction.

**Repo safeguards.** All Phase-1/2 files, scripts, logs and audit packages are preserved
byte-for-byte; the register grew by insertion only (+32 rows, T-137 … T-168); the
documentation index and this decision log grew by appending only; no log was
overwritten; the commit is a normal fast-forward. The Stage-3A script imports the
Stage-2C module read-only, so Stage-2A/2B/2C are unaffected. A passing script is
treated as supporting evidence only: 20 rows are `PROVED IN PHASE 3 STAGE 3A` on the
strength of the proofs in the deliverable, 3 are `PROVED IN PHASE 1`, 1 is an
`IMPORTED RESULT`, 6 are `COMPUTATIONALLY VERIFIED ONLY`, 2 are `CONJECTURE` and 1 is
`OPEN`.

**Stopping point.** Stage 3A is complete as authorised. No further phase is begun
without explicit approval.

## D-024 — Phase 3, Stage 3B: enumeration of Galois hull dimensions (Tasks A–H)

**Decision taken (2026-11-06).** Complete Phase 3 Stage 3B — exhaustive enumeration of
Galois hull dimensions, hull-dimension distributions and LCD/SO/SD counts for codes over
`R = M_2(A_t)` — and **stop there**, pending explicit approval for Phase 4/5/6. Gray maps
(Phase 5), CSS/EAQECC constructions and quantum parameters (Phase 6) and the manuscript
are **not** started, and no hull enumerator is read as a quantum-code parameter.

**Deliverables.** `03_THEOREMS/PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md`;
`04_COMPUTATION/phase3_stage3b_hull_enumeration.py` and
`04_COMPUTATION/phase3_stage3b_hull_log.txt` (696 lines, **206 checks, 206 PASS, 0 FAIL**;
189 `[EXH]`, 19 `[SMP]`; seed `20261109`; Python 3.11.2; two consecutive runs
byte-identical; SHA-256 `c8904a23…59814`).

**Task map used.** A = the four counting problems; B = the code family and its exhaustive
enumeration; C = two independent hull routes; D = hull-dimension distributions;
E = LCD/SO/SD counts; F = the split-regime closed form and the open questions;
G = O-3.1 (resolved, negatively) and the left-ideal gap; H = negative controls, boundary
cases, traceability and limitations.

**Decisions that need recording.**

1. **The four counting problems are kept separate** (T-171): distinct right ideals,
   distinct generator matrices, unit-equivalence classes, Morita-equivalent submodules.
   They are four different numbers and no table mixes them.
2. **Unit equivalence = left multiplication by `R_n^× = GL_2(B)`** (`W ↦ UW` under
   Morita). The two naive candidates are trivial and the log says so on every case:
   right multiplication fixes every right ideal, and the scalar action `W ↦ uW`
   (`u ∈ B^×`) fixes every `B`-submodule.
3. **O-3.1 is REFUTED** (T-173). An exhaustive scan over every code of every enumerable
   family found 1 hull with `μ_B = 3` at `(4,2,2)`, `s = 0` and 3 at `s = 1`; all four
   witnesses are self-dual codes, each verified by two hull routes, by the Nakayama
   identity computed from `rad(B) = B \ B^×`, and by a randomised search for a
   2-element generating set. **"Hulls are principal" may not be used as a hypothesis in
   later phases.** The restricted (split/chain) question survives as **O-3.5**.
4. **The τ-orbit product formula (T-169) is the only Stage-3B row carrying a proof**, and
   it is not a data fit: states, transitions, initialisation, exactly-once counting and
   the absence of inadmissible tuples all come from Morita/CRT plus Stage 3A Thm 3.5.
   It is proved and tested only in the split regime; in the chain regime it degenerates
   (the log says so instead of printing a tautological pass) and in the wild regime it is
   undefined (**O-3.4**).
5. **New open items:** O-3.3 (Morita classes in the wild regime — no SNF), O-3.4 (closed
   form outside the split regime), O-3.5 (hull principality in the split/chain regimes).
   O-3.1 is discharged (negatively).
6. **Bugs caught by the negative-control discipline** (recorded in the inventory §13.1):
   `μ` computed from a `B`-generating set instead of an `F_q`-basis; a missing factor 2
   in the transfer matrix (which reproduced every coefficient and half of every
   exponent); the trivial unit action; and a structural edit that deleted a function.

**Repo safeguards.** All Phase-0/1/2/3A files are preserved byte-for-byte (77-file
baseline re-checked: 77/77 identical); the register grew by insertion only (+7 rows,
T-169 … T-175); the inventory, the README and this decision log grew by appending only;
no log was overwritten; the commit is a normal fast-forward on
`arena/59de606f-matrix-ring`. Regressions re-run in this stage: Stage 2A no failures,
Stage 2B 460/460, Stage 2C 596/596, Stage 3A 583/583, each reproducing its committed log
byte-for-byte.

**Stopping point.** Stage 3B is complete as authorised. No further phase is begun without
explicit approval.

---

## D-025 — Phase 4 (Gray map compatibility): the coefficient expansion is the map, the
## transported form is Hermitian-with-Hankel, and no homogeneous-weight isometry exists

**Context.** Phase 4 (Tasks A–H) had to decide which finite-field map $R^n\to\mathbb F_q^N$
to study, which target orthogonality to use, and how to report the weight situation
honestly. Register rows **T-176 … T-189**; deliverable
`03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md`; log `phase4_gray_map_log.txt`
(463 checks, 0 FAIL, byte-reproducible).

**Decisions.**

1. **The baseline candidate is the coefficient expansion**, treated as a *hypothesis*
   (additivity, $\mathbb F_q$-linearity, bijectivity, shift-compatibility, and
   multiplication behaviour are each measured, not assumed). It is **not** called a Gray
   map: it is an isometry only for the weight it defines ($w_{\mathrm{coef}}$), not for
   the ring-Hamming weight and not for the homogeneous weight.
2. **The target orthogonality is the transported one**, computed explicitly rather than
   assumed Euclidean: $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$
   (T-177). The duality correspondence $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$
   (T-178) is then a transport statement whose *content* is T-177.
3. **Hull compatibility (T-179) uses only bijectivity and T-178**, so it holds for
   non-principal hulls as well; the four $\mu_B=3$ witnesses of T-173 are re-checked
   explicitly. "Hulls are principal" is never assumed (D-024 stands).
4. **The homogeneous weight is reported with an obstruction, not a construction.** Its
   closed form on $M_2(\mathbb F_q)$ is proved (T-181) and verified exhaustively for
   $q=4,8,9$; since its values are non-integral, **no** map into a Hamming space can be an
   isometry for it (T-182). The rescaled/linear variant is left OPEN with the necessary
   conditions recorded (O-4.4).
5. **The image is quasi-cyclic of index $4t$, not cyclic** (T-183); the number of codes
   whose image is invariant under the shift by 1 is measured per family and is small.
6. **"Coefficient reversal makes the Gram the identity" is REFUTED** (the reversal *is*
   $J$); the correct replacement is the congruence question, where a genuine trade-off
   appears: at $(9,2)$ a Gram-standardising change of coordinates exists and commutes with
   the block shift, but it is non-monomial and therefore loses the Hamming weight
   (T-185).
7. **Two symmetry notions that had been conflated are separated** (T-186): reflexivity of
   the orthogonality relation needs $r\mid2s$, while symmetry of the form *as a value*
   needs $r\mid s$.
8. **The literature search limitation is recorded, not hidden** (§8.3): no PDF was
   retrieved and no bibliography was followed, so the novelty claim is evidence-based, and
   five references (Greferath–Schmidt 1999, Honold, Oggier–Belfiore–Viterbo,
   arXiv:1409.7228, arXiv:2602.18255) still need to be added to `references.bib` with
   VERIFY tags before any manuscript is written.

**Consequences for later phases.** T-012 is partially resolved (duality yes, isometry no);
T-013 remains open and now has F1–F8 (§6 of the deliverable) as its preconditions. Any
CSS/EA step must either use the $\widehat\sigma_s$-Hermitian-with-Hankel form or pay the
weight cost of the congruence map.

**Repo safeguards.** All Phase-0/1/2/3A/3B files are preserved byte-for-byte (80-file
start-of-stage baseline re-checked at the end of the phase: 80/80 identical); the register
grew by insertion only (+15 rows, T-176 … T-189, plus annotations to T-012/T-013); the
inventory, the README and this decision log grew by appending only; no log was
overwritten; the commit is a normal fast-forward on `arena/59de606f-matrix-ring`.
Regressions re-run in this phase: Stage 2A no failures, Stage 2B 460/460, Stage 2C
596/596, Stage 3A 583/583, Stage 3B 206/206, each reproducing its committed log
byte-for-byte.

**Stopping point.** Phase 4 is complete as authorised. No further phase is begun without
explicit approval.

---

## D-026 — Phase 5: the quantum construction routes and the Hankel obstruction

**Decision (Phase 5).** The quantum codes are built from the Gray image through
three routes, and the route is chosen by the arithmetic of `(t, s)`, not by
convenience:

1. **R1 — Galois-native twisted stabilizer embedding** $\mathcal C_T=\{(u\mid T_su)\}$,
   $T_s(u)=(u^{[s]}J)^{\mathsf T}$. Valid for **every** `t` and `s` provided the
   image code is self-orthogonal for the transported form; yields $[[N,N-k,d]]_q$;
   needs no coordinate transformation and no reflexivity hypothesis (T-193).
2. **R2 — Euclidean/CSS**, $\mathcal C=D'\times D'$, valid when the transported
   form *is* Euclidean (`t=1` and `r|s`) or when a congruence $\Psi$ exists;
   yields $[[N,N-2k,d]]_q$ (self-orthogonal) or $[[N,2k-N,d]]_q$
   (dual-containing) — T-196.
3. **R3 — entanglement-assisted**, $\mathcal C=D\times D$ for an arbitrary code;
   $[[N,N-k-h_E,d;k-h_E]]_q$ — T-197.

**Reason for the record.** Two facts decided the ranking and both are proved, not
assumed:

* R1's distance is **capped** by $\min\mathrm{wt}(D^{\perp_E})$ (T-194), because
  $(0\mid b)\in\mathcal C_T^{\perp_\omega}$ for every $b\in D^{\perp_E}$. In every
  instance scanned this cap is $1$ or $2$, so R1 alone cannot produce a good code.
* R2 needs the Euclidean form, and for `p = 2`, `t` even **no congruence exists at
  all** — $H_t$ is alternating there, hence not congruent to $I_t$ (T-200,
  verified exhaustively over all $4\times4$ matrices over $\mathbb F_4$). This is
  an **obstruction, not a gap**: for `(q,t) = (4,2)` — which is precisely the
  family carrying the non-principal ($\mu_B\ge3$) O-3.1 hull witnesses — the
  Euclidean/CSS route is impossible in principle, so R1 is the only route attached
  to the Galois structure.

**Consequence recorded.** The recommendation is R2 where available (best
distances: $[[16,4,3]]_4$), R1 for the obstructed `t≥2` characteristic-2 cases
(where it still delivers $[[16,10,2]]_4$ from a **non-principal** hull), and R3
when entanglement may be spent (best distance overall: $[[8,4,3;4]]_4$).

**Two subtler points that are now enforced by negative controls.**

* Commutation of the Weyl operators must be tested on an $\mathbb F_p$-basis of
  the stabilizer, never on an $\mathbb F_q$-basis: $\operatorname{Tr}_{\mathbb
  F_4/\mathbb F_2}(1)=0$, so the naive test would report $d=1$ for a code whose
  true distance is $3$ (T-203, control N5).
* In the reflexive regime ($r\mid2s$) the twisted group is abelian for **every**
  code (T-195), so "self-orthogonal" is sufficient always but necessary only
  outside that regime; the extra abelian groups have distance $1$ by T-194.

**Repo safeguards.** All Phase-0/1/2/3A/3B/4 files preserved byte-for-byte
(83-file start-of-stage baseline, list SHA-256 `4e3814b1…9b66`, re-checked at the
end of the phase); the register grew by insertion only (+14 rows, T-190 … T-203,
plus annotations to T-013, T-184/T-185 and O-3.1); the inventory, the README,
`01_LITERATURE/references.bib` and this decision log grew by appending only; no
log was overwritten; the commit is a normal fast-forward on
`arena/59de606f-matrix-ring`. Regressions re-run in this phase: Stage 2A no
failures, Stage 2B 460/460, Stage 2C 596/596, Stage 3A 583/583, Stage 3B 206/206,
Phase 4 463/463, each reproducing its committed log byte-for-byte.

**Stopping point.** Phase 5 is complete as authorised. No manuscript text and no
journal-submission material has been produced; no further phase is begun without
explicit approval.

---

## D-027 — Phase 6: parameter enhancement, exact certification, and the
## literature comparison (2026-11-06)

**Decision.** Execute Phase 6 exactly as authorised: a systematic search over
the whole accessible parameter range with **exact** distance certification, the
re-derivation of the O-3.1 witnesses, the exact domain of the characteristic-two
obstruction, parameter verification, and the comparison against Grassl's code
tables — and then **stop**, without manuscript text.

**What was decided, and why.**

* *Exactness over coverage.* The Phase-5 distance search was capped at
  symplectic weight 4, which silently truncated every larger distance. Phase 6
  replaces it with a three-pass computation: a cheap weight-2 filter, then
  **complete enumeration** of the relevant classical code (every codeword, via a
  reflected mod-$q$ Gray code with bit-packed XOR updates for $q=2^r$), then a
  support search to weight 6. Every reported distance is therefore exact with an
  explicit witness, or a proved lower bound labelled as such. The enumerator was
  cross-checked against brute force on 110 instances (0 disagreements) before
  being trusted.
* *Certify the code that is reported.* The first version of the certification
  re-selected "a code with the same invariants" and then certified that one —
  which silently certified a **different** code (2 failures). Fixed: the search
  now stores the image basis of every reported code. This is recorded in the
  completion report as a defect found and fixed, not as a silent patch.
* *The entanglement-assisted distance.* The ambient quantum search initially
  tested commutation with $\mathrm{rad}\,V$ only and reported $d=1$ for codes
  whose true distance is 6. The correct set is $V^{\perp_\omega}\setminus V$:
  with entanglement the **whole** group $V$ is measurable, so an undetected
  error must commute with all of $V$. Corrected (T-207); at the same time it was
  checked that Phase 5's T-197 formula is the **same number**, because
  $D^{\perp_E}\setminus D=D^{\perp_E}\setminus\mathrm{Hull}_E(D)$ — so T-197 is
  clarified, not refuted.
* *The obstruction is delimited, not extended.* T-200 is strengthened (it holds
  for **every** linear coordinate transformation, T-210) and at the same time
  bounded (for $t$ **odd** a congruence exists and is constructed, T-211). The
  scope note is explicit: nothing here says that good characteristic-two codes
  are impossible; one route is closed, and three bypasses are measured.
* *Novelty: none in parameters.* Grassl's tables **are** reachable
  (`http://www.codetables.de`), which resolves O-5.4 and **corrects** Phase 5
  §6. Three of the eight comparable stabilizer tuples meet the best known
  distance exactly; five are 1–3 below. No record is claimed; the defensible
  claim remains the **origin** of the codes (non-commutative matrix ring,
  Galois hulls, Gray map).

**Results (register rows T-204 … T-215).** Maximum certified distances:
$d=3$ for the stabilizer routes ($[[16,4,3]]_4$, unchanged from Phase 5),
$d\le2$ for R1 (the cap $d_{R1}\le\min\mathrm{wt}(D^{\perp_E})$ is attained), and
**$d=6$** for the entanglement-assisted route ($[[12,2,6;10]]_4$) with
$d=5$ at $[[16,4,5;8]]_4$ and $[[24,4,5;12]]_4$. Every $d\ge4$ requires
entanglement, and $c+K=N-k$. The four O-3.1 witnesses are re-derived (1 at
$s=0$, 3 at $s=1$, $\mu_B=3$ by two implementations); the $\mu_B$ census shows
no $\mu_B\ge3$ hull outside $(4,2,2)$.

**Honesty constraints imposed on this phase (all enforced in the script).**
No random search is used as a certificate; the two sampled families are labelled
`[SMP]` and never passed off as exhaustive; commutation is tested on an
$\mathbb F_p$-basis with the trace-symplectic form; O-5.6's negative answer is
reported as "no improvement is possible", not as a search that found nothing;
and the failure of one coordinate transformation is explicitly **not** presented
as the impossibility of the characteristic-two regime.

**Repo safeguards.** Phase 0–5 files preserved (86-file Phase-6 start baseline,
re-checked at the end); the register grew by insertion only (+12 rows,
T-204 … T-215, plus annotations to T-197, T-200, T-202 and corrections of Phase 5
§4/§6); inventory, README, `references.bib`, CHANGELOG and this log grew by
appending only; no log overwritten; commits are normal fast-forwards on
`arena/59de606f-matrix-ring`.

**Stopping point.** Phase 6 is complete as authorised. No manuscript text and no
journal-submission material has been produced; no further phase is begun without
explicit approval.

---

## D-028 — Phase 7: extended search, entanglement efficiency and the structure of the attainable frontier

**Authorisation.**  Phase 6 stopped at O-6.1 … O-6.4.  This decision records
the authorisation and the *method* of Phase 7, in particular the four
deliberate constraints below, which were fixed **before** the run and are
enforced in `phase7_extended_search.py`.

**What was done.**  The Phase-2C component routine covers three regimes of
`X^n − 1` and raises `no component routine` outside them.  It is **replaced**
(not extended) by the Chinese remainder theorem
`B = A_t[X]/(X^n−1) ≅ ∏_j A_t[X]/(g_j^{e_j})`, realised as an `F_q`-linear
isomorphism so that it composes unchanged with the Gray map, the Morita hull
and the three quantum routes of Phases 4–5.  The replacement is validated
**against the old routine** (as a set of submodules of `B^2`) on every family
the old routine supports — ten families, all `YES` — before it is allowed to
produce a single new number.  Only then is the search re-run over the enlarged
list (25 families, 120721 codes with invariants, 5055 with a distance).

**Result.**  17 checks, 17 PASS, 0 FAIL.  `d = 10` entanglement-assisted
(`[[20,2,10;18]]_4`, `[[24,2,10;18]]_9`); the first **stabilizer** distance 4 in
this framework (`[[24,8,4]]_9` SO, `[[20,4,4]]_4` DC); O-6.3 resolved (three
families newly enumerable); O-6.4 answered (`µ_B(Hull_s) ≥ 3` at `(9,2,3)` and
`(4,2,4)`, not at `(8,2,2)`); O-6.1 and O-6.2 answered quantitatively.

**Honesty constraints imposed on this phase (all enforced in the script).**
1. *No number without a completeness label.*  Every family is `[EXH]`,
   `[SMP]` (seeded 2000-code sample, printed as `#codes < total`) or
   `COUNTED-ONLY`/blocked with the reason printed.  Samples are never printed
   as exhaustive.
2. *No distance without an exhaustive or proved computation.*  4418 of the
   5055 distances are exact; the other 637 are printed as lower bounds (`>= d`)
   with the method that proved them.
3. *No record claim, and no false benchmark.*  The `q = 4` reference values
   were read off `codetables.de` one page at a time, and the entries that could
   not be checked (all of `q = 8`, `q = 9`, and every entanglement-assisted
   code) are declared unbenchmarked rather than omitted.
4. *Every obstruction statement of Phase 6 is re-examined, not trusted.*  This
   produced one erratum (E-7.1: `c + K = N − 2h_E`, not `N − k`), one
   re-scoping ("no stabilizer `d ≥ 4`" holds for `N ≤ 16`), and one correction
   of a claim about the tables (`q = 8` is not available there).

**Errors found and fixed in this phase's own verification (recorded, not
patched silently).**  The seeded sampling branch of the product enumeration
passed *indices* where the exhaustive branch passes *submodules* (a crash on
the four sampled families, fixed and re-tested on all four); `main()` stood
before the parts it calls (a `NameError` at the first full run); and the
per-family elapsed times were computed from `time.time()`, which the sandbox
clock moved by 63 hours mid-run — replaced by `time.monotonic()`.  Two dead and
partly wrong helpers (`poly_pow_mod`, `is_irreducible`) were deleted rather
than left in place.

**Repo safeguards.**  Phase 0–6 files preserved (89-file Phase-7 start
baseline, re-checked at the end of the phase); the register grew by insertion
only (+14 rows, T-216 … T-229, plus annotations to T-205, T-209, T-215 and the
erratum E-7.1); inventory, README, CHANGELOG and this log grew by appending
only; no log overwritten; commits are normal fast-forwards on
`arena/59de606f-matrix-ring`.

**Stopping point.**  Phase 7 is complete as authorised.  No manuscript text and
no journal-submission material has been produced; no further phase is begun
without explicit approval.  Six open problems are carried forward: O-7.1 … O-7.6
(the binding one is O-7.2: the component BFS blocks every `N = 32` family).

---

## D-029 — Phase 7 (v2): the full Task A–H specification, and the decision to report the non-dominated set rather than a single champion

**Authorisation.**  The Phase-7 brief was re-issued in an expanded form
(Tasks A–H) with a fixed deliverable filename,
`03_THEOREMS/PHASE7_LONGER_LENGTH_AND_PARAMETER_OPTIMIZATION.md`.  This
decision records how v2 relates to the v1 deliverable, and the three judgement
calls that v2 adds on top of D-028.

**1. v1 is preserved, not overwritten.**  `03_THEOREMS/PHASE7_EXTENDED_SEARCH.md`
and the v1 log are kept verbatim in the repository — the log under the new name
`04_COMPUTATION/phase7_extended_search_log_v1.txt` (SHA-256 `634a63d3…c35eb`,
639 lines, 17 checks, 17 PASS), because the v2 run necessarily rewrites the
canonical `phase7_extended_search_log.txt`.  Nothing in v1 is retracted; v2
reproduces every v1 number bit for bit and adds to it.  The four additions to
the script are **reporting and verification only** — (f) the dominance table,
(g) the coset Singleton bound with check H1, (h) the four Phase-6 baselines —
plus a `resource`-based peak-memory line; the search loop is untouched.

**2. The optimisation deliverable is the non-dominated set, not one champion.**
Task C asks for optimisation against four named baselines over
`(N, K, d, K/N, d/N, c)`.  No tuple is best in all six coordinates, so
reporting a single winner would be a choice the data does not support.  v2
therefore computes the dominance frontier
(`N ≤ N'`, `K ≥ K'`, `d ≥ d'`, `c ≤ c'`, one strict, inside one alphabet):
368 distinct tuples with a distance, 88 non-dominated, 280 dominated.  A
dominated tuple is never the right choice under any monotone weighting, so the
frontier is the honest answer; §12.1 then ranks the frontier by *purpose*
(largest distance / largest distance with bounded `c` / best stabilizer / best
`d/N` / best rate / non-principal hull) instead of declaring a champion.

**3. O-6.1 is answered by a *proof*, not only by a measurement.**  v1 measured
the entanglement budget; v2 proves the criterion behind the question:
T-230 (the distance is the minimum weight of the coset code
`D^{⊥_E}/Hull_E(D)`, of dimension `K` and length `N`), T-232 (the resulting
**coset Singleton bound** `K + d ≤ N + 1`, which is neither the EA Singleton
bound nor implied by it — for `[[20,2,10;18]]_4` it gives `K ≤ 11` where
EA-Singleton allows `K ≤ 20`) and T-233 (the feasibility inequality
`2k ≤ N + c_0 − K_0`).  Check **H1** verifies T-232 exhaustively on all 5055
codes (0 violations), which is the 18th check.

**4. One baseline is reported as *not reproduced*, and that is a finding.**  Of
the four Phase-6 baselines named in the brief, three are reproduced exactly and
are non-dominated.  `[[24,4,5;12]]_4` is neither: Phase 6 obtained it at
`(4,2,3)` from a 300-code **sample**, and v2 enumerates that family
exhaustively (35937 codes) and finds `d = 6` there.  Phase 6's `5` was a
sampled lower bound, not an optimum, so the correct statement is "improved by
this phase", not "refuted" — and it is recorded that way, in §2.1, §6.3 and
T-226, rather than being quietly re-derived.

**Verification.**  18 checks, 18 PASS, 0 FAIL; 727-line log; ≈517 s; peak
resident memory 367.3 MB.  Three consecutive runs of the final script (516.6 s,
519.9 s, 527.8 s) agree on every line except the per-family `[..s]` annotations
and the peak-memory line (367.3 MB, 367.9 MB, 367.3 MB); the committed log is
the 516.6 s run, produced by the committed script (SHA-256
`682e2a36…d932a0`, 2020 lines), so it is byte-reproducible from that script up
to those two lines.
Register grew by insertion only (+4 rows, T-230 … T-233, plus an annotation
reconciling Phase 5's `µ_B = 4` with the Phase-3B hull census).

**Stopping point.**  Phase 7 (v2) is complete as authorised.  No manuscript text
and no journal-submission material has been produced; no further phase is begun
without explicit approval.  Open problems carried forward: O-6.5, O-6.6 and
O-7.1 … O-7.6.

---

## D-030 (2026-11-10) — Researcher decision: retain all existing GitHub materials publicly; no removal or privacy cleanup

**DECISION: RETAIN ALL EXISTING GITHUB MATERIALS PUBLICLY. NO REMOVAL OR PRIVACY CLEANUP IS AUTHORIZED.**

| # | Date | Phase | Decision | Rationale | Approver |
|---|---|---|---|---|---|
| **D-030** | 2026-11-10 | After Phase 23 — repository governance | All existing project materials remain on GitHub and publicly accessible. Nothing is removed, hidden, made private or rewritten. | Decision of the researcher. It overrides previous proposals to remove the uploaded patch or to hide internal project documentation. | **Researcher (Arun Kumar Yadav)** |

**Source.**  Decided by the researcher on 2026-11-10, in the message headed
"RESEARCHER DECISION — PRESERVE ALL GITHUB CONTENT PUBLICLY" (Arena session
branch `arena/582e83ad-matrix-ring`; received at about 14:45 UTC).  The line in
capitals above is the wording the researcher instructed this record to state,
reproduced verbatim.  This entry records the decision.  It does not extend or
qualify it.

**Instructions given with the decision.**

1. Keep the GitHub repository public.
2. Preserve all existing files, including the uploaded patch.
3. Preserve all Phase 0–23 research documents, audit reports, decision records
   and historical packages.
4. Preserve AI declaration discussions and unsent editorial correspondence.
5. Preserve both `main` and the research branch.
6. Do not delete any files.
7. Do not rewrite Git history.
8. Do not force-push.
9. Do not change repository visibility.
10. Do not delete branches, tags or commits.
11. Do not remove the public `research-data` directory.
12. Do not merge the local session branch into `main` without separate approval.

The current repository state is to be preserved, and future work is to continue
without deleting or hiding historical materials.

**What the decision overrides.**  Previous proposals to remove the uploaded
patch or to hide internal project documentation.  The proposal known to this
record is the Arena agent's own: its first report in this session, earlier on
2026-11-10, recommended taking `01a1a47c-f51d-7d7c-810c-207359de606f.patch` off
`main` (by deleting it through the GitHub web interface, or by returning `main`
to `3752a6c`).  **That recommendation is withdrawn and is not to be acted on.**
The patch stays on `main`.  Any other proposal to the same effect, from whatever
source, is overridden in the same way.

**What the decision does not authorise.**  Journal submission, licence
application, DOI creation, or any other external publication action beyond the
GitHub content already approved.  Under instruction 12 it also does not
authorise merging the session branch into `main`.

**Effect on earlier records.**  None of them is edited.

* `PHASE22_GITHUB_DATA_PUBLICATION/PHASE22_GITHUB_PUBLICATION_REPORT.md` §3
  lists what was "deliberately NOT brought onto `main`" when `research-data/`
  was published at `3752a6c`.  Since `b0c5fa7`, the upload of the patch, `main`
  also carries much of that material as diff text inside the patch — for
  example `PHASE13_FINAL_INTEGRATION/PHASE13_AI_DECLARATION_RECONCILIATION.md`,
  `PHASE12_FFA_SUBMISSION_PREP/PHASE12_CONFIRMATION_REGISTER.md`,
  `PHASE17_RESEARCHER_DECISION/PHASE17_RESEARCHER_DECISION_SHEET.md`, and the
  unsent editorial email in Appendix E of
  `PHASE23_FFA_FINALIZATION/PHASE23_FFA_OPTION_C_COMPLIANCE.md`.  By this
  decision that state is accepted and retained.  The Phase 22 report stays as
  written; it remains the record of `main` at `3752a6c`.
* The Phase 22 rule against bringing the research branch onto `main` is **not**
  lifted.  Instruction 12 keeps any merge into `main` subject to separate
  approval.
* The sixteen decisions in
  `PHASE23_FFA_FINALIZATION/PHASE23_RESEARCHER_DECISION_SHEET.md` are **still
  pending**.  This decision answers none of them; in particular it is not an
  answer to decision 1 (generative-AI declaration), 10 (editorial email),
  13a–e (licence) or 16 (DOI deposit).
* Noted for the researcher, not decided here: one option under decision 12 is
  to remove `research-data/quantum_code_records/comparison_grassl_q9.csv` from
  the deposit.  That option would delete a published file, which instruction 6
  forbids, so choosing it would need the researcher's separate and explicit
  approval.
* The Phase 23 documents state that `main` is at `3752a6c`.  That was the state
  before the patch was uploaded; `main` is now at `b0c5fa7`.  The commit-pinned
  data link used in the manuscript
  (`…/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data`) still
  resolves and is unaffected.

**Repository state at the time of the decision.**  Checked against GitHub on
2026-11-10 at 14:50 UTC (authenticated API) and at 14:56 UTC (anonymously, with
no credentials); the two checks agree.

| item | state |
|---|---|
| repository | `https://github.com/arunyadav0307-stack/Matrix-Ring` |
| visibility | **public**; not archived |
| default branch | `main` |
| `main` | `b0c5fa78c0c860487565c2c93662b6f72942e168` — 4 commits, 91 files: `README.md`, `Matrix Ring.zip`, `research-data/` (88 files) and the patch |
| research branch `arena/59de606f-matrix-ring` | `a55e8e6e87cdf8cc8e0e33b2b3433d3044ec8fb0` — 51 commits, 1371 files (Phases 0–23) |
| uploaded patch | `01a1a47c-f51d-7d7c-810c-207359de606f.patch`, on `main` only, added by `b0c5fa7`; 21,271,473 bytes; SHA-256 `342d1acec7c25b788e335c854f084788df7da96e75b205b7eca406efd5f57271` |
| `research-data/` | 88 files on `main`, identical on the research branch; all 87 entries of `PUBLICATION_MANIFEST.sha256` verify |
| tags / releases / pull requests | 0 / 0 / 0 |
| licence | none |
| branch protection | none on either branch |
| session branch `arena/582e83ad-matrix-ring` | not on GitHub; it exists only in the Arena session workspace |

**Action taken on GitHub: none.**  Nothing was deleted, moved, renamed,
rewritten, pushed, force-pushed, merged, tagged, released or licensed, and no
repository setting was changed.  The only change made on this decision is this
entry, appended to this log on the session branch, which is local to the Arena
workspace.

**Note on this log.**  The previous entry, D-029, dates from Phase 7 (v2).
Decisions taken in Phases 8–23 were recorded in the phase documents — among
them the decision register in `PAPER/compile/BUILD_CORRECTIONS.md`,
`PHASE12_FFA_SUBMISSION_PREP/PHASE12_CONFIRMATION_REGISTER.md`,
`PHASE17_RESEARCHER_DECISION/PHASE17_RESEARCHER_DECISION_SHEET.md`,
`PHASE18_ABSTRACT_OPTION_B_IMPLEMENTATION.md` and
`PHASE23_FFA_FINALIZATION/PHASE23_RESEARCHER_DECISION_SHEET.md` — and are not
back-filled here.  This entry was appended; every earlier line of the log is
unchanged (its first 55,081 bytes still have SHA-256
`1781f227396405e85281e1551bfd1ca2c4e102dd1043bae161396fa2defec63f`).

**Stopping point.**  The decision is recorded and work has stopped, as
instructed.  Nothing further is begun without explicit approval.
