# 06 — Phase 0 audit request for ChatGPT (blueprint §8B)

> **Researcher (Arun): copy everything below the line into ChatGPT, together
> with the files listed under “Attachments”.** The audit must be returned in the
> structured form A–I requested at the end. Do **not** ask Arena to start
> Phase 1 before this audit comes back with a GO.

---

I am providing the project blueprint and Arena AI's complete output for
**Phase 0** of the project

> *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
> Noncommutative Matrix Rings.*

Act as an **independent mathematical referee and research auditor**, not as a
supportive proofreader. The blueprint requires that no phase is treated as
complete merely because an AI system says it is complete.

## Attachments (all in the repository `Matrix-Ring`)
1. `00_BLUEPRINT/Research_Blueprint.pdf` — the controlling document
   (text extract: `00_BLUEPRINT/Research_Blueprint_extracted_text.txt`).
2. `02_PHASE_REPORTS/Phase_0/Phase_0_Report.md` — Arena's Phase 0 report
   (the document to audit).
3. `01_LITERATURE/annotated_bibliography.md` and `01_LITERATURE/references.bib`.
4. `01_LITERATURE/comparison_matrix.md`.
5. `04_COMPUTATION/matrix_ring_lib.py`, `04_COMPUTATION/phase0_feasibility.py`,
   `04_COMPUTATION/phase0_results.txt`, `04_COMPUTATION/README.md`.
6. `03_THEOREMS/theorem_register.md`, `PROJECT_DECISION_LOG.md`, `CHANGELOG.md`.

## TASK
1. Read the blueprint and the supplied Phase-0 output.
2. Check every definition, assumption, theorem statement, proof sketch,
   equation and computational claim in the Phase-0 report.
3. Identify invalid reasoning, hidden assumptions, notation conflicts,
   **left/right module errors**, non-commutative multiplication issues, invalid
   inner products, incorrect duality claims, and unsupported Gray-map /
   quantum-code implications.
4. Check the closest literature and distinguish what is already known from what
   may be new. **Never call a result novel without evidence.** In particular,
   check the three candidate gaps (GAP 1–3) against your own knowledge of the
   literature.
5. Re-derive the important claims independently where possible. In particular
   please re-derive, by hand:
   * (a) that the entrywise extension of $\sigma_s$ to $M_m(A_t)$ is a ring
     automorphism and that $\theta_s=\sigma_s\circ{}^{\mathsf T}$ is an
     **anti**-automorphism;
   * (b) that $\Lambda=\lambda\circ\mathrm{tr}$ ($\lambda$ = coefficient of
     $u^{t-1}$) is a non-degenerate / ideal-catching Frobenius functional on
     $M_m(A_t)$;
   * (c) that with $\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i$, the dual of a
     **right** $R$-module is again a **right** $R$-module and satisfies
     $|C||C^{\perp_s}|=|R|^n$;
   * (d) that the dual under the *plain* ring-valued product $\sum_ix_iy_i$
     flips sides and is **not** perfect for right modules (Arena claims it
     breaks for 31 of the 35 cyclic codes at $(m,q,t,n)=(2,2,1,3)$).
   If a proof sketch is incomplete, say **exactly** what is missing; do not
   repair it silently.
6. For the code, inspect the algorithms and the completeness claims. Distinguish
   exhaustive verification (E2–E5) from randomised sampling (E1).
7. **Specifically adjudicate the E5 / GAP 2 issue.** Arena reports that at
   $(m,q,t,n)=(2,2,1,3)$ it finds 35 right-cyclic codes, while the generator
   parametrisation $C=(fh)+u(fg)$ of Alahmadi–Sboui–Solé–Yemen (2013) yields at
   most 27 objects, of which at most 19 are right-cyclic under the readings
   implemented. Arena explicitly flags that this may be a misreading of the
   source. Please (i) say which reading of "$(fh)+u(fg)$" is the correct one in
   your judgement, (ii) decide whether Arena's computation or its reading is at
   fault, and (iii) state whether any claim about that paper may be made in the
   manuscript.
8. Please also answer these researcher questions:
   * **U3:** is there a published Nebe–Rains–Sloane-type treatment of
     self-dual codes over rings using an **anti-isomorphism**? If yes, give the
     exact reference — it may be the closest conceptual precursor of the
     $\theta$-duality and must be cited.
   * **U4:** do you know of any paper defining a **Galois / $\sigma$-dual or
     Galois hull over a non-commutative ring**, or constructing a **quantum
     code from a code over a matrix ring**? (These are the falsifiable novelty
     tests for GAP 1 and GAP 3.)

## RETURN A STRUCTURED AUDIT
**A. Overall verdict:** ACCEPT / ACCEPT WITH MINOR REVISIONS / MAJOR REVISION /
REJECT / INSUFFICIENT EVIDENCE.
**B. Correct results** (what Arena got right).
**C. Critical mathematical errors** (if any).
**D. Missing lemmas / proofs.**
**E. Literature and novelty concerns**, including the U3/U4 answers.
**F. Required corrections, prioritised.**
**G. Questions requiring the researcher's decision.**
**H. GO / REVISE / STOP phase-gate recommendation** for the Phase-0 → Phase-1
gate.
**I. The exact next Arena prompt** (Phase 1), but only if progression is
justified.

Do not advance to the next phase if foundational assumptions or proofs fail.
Explain the audit in accessible Hindi/Hinglish, but write replacement
mathematics and paper-ready text in formal academic English/LaTeX.
