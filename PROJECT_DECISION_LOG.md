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
