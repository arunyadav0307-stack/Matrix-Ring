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
