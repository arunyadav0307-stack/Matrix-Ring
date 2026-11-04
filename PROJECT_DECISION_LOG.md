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

## Decisions reserved for the researcher at the Phase-0 gate
* **M1** Adopt the $\theta_s$-Galois pairing (yes / no / modify)?
* **M2** Require $q=p^r$ with $r\ge2$ and take $m=2$, $t\ge1$ as the primary
  setting (yes / no)? Keep $t\ge2$ in scope (U7)?
* **M3** Fix the convention “cyclic = right ideal” and exclude two-sided codes
  (yes / no)?
* **M4** Keep the working title, or rename now?
* **U1** Upload the source papers to the repository.
* **U4** Run or commission the MathSciNet/zbMATH novelty searches.
