# 06 — Phase-0 **revision** audit request (blueprint §8B)

> **Researcher (Arun): copy everything below the line into ChatGPT together with the
> files listed under “Attachments”.** This is the audit for the *revision* pass
> (`Phase0_audit_request.md` is the earlier, Phase-0-only request and is kept for the
> record; the two can be answered together).
> **Do not ask Arena to start Phase 1 before this audit comes back with a GO.**

---

I am providing the revised **Phase 0** output of the project

> *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative
> Matrix Rings.*

Act as an **independent mathematical referee and research auditor**, not as a supportive
proofreader. Three tasks were executed; please audit all three.

**Setting (fixed once).** $p$ prime, $q=p^{r}$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$,
$R=M_m(A_t)$, $R_n=R[X]/\langle X^n-1\rangle$ with $X$ **central**. A *code* is a **right
ideal** of $R_n$ (a shift-closed right $R$-submodule of $R^n$); two-sided codes are
excluded. $\sigma_s(a)=a^{p^s}$ entrywise on the $\mathbb F_q$-coefficients ($u$ fixed),
$\theta_s=\sigma_s\circ{}^{\mathsf T}$, $\lambda(\sum a_iu^i)=a_{t-1}$,
$\Lambda=\lambda\circ\operatorname{tr}$, and
$$\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i,\qquad
C^{\perp_s}=\{y:\langle x,y\rangle_s=0\ \forall x\in C\}.$$

## Attachments (repository `Matrix-Ring`, branch `arena/59de606f-matrix-ring`)

1. `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` — **Task 2**: the complete proofs. Please
   check every one.
2. `02_PHASE_REPORTS/Phase_0/NONTRIVIAL_GALOIS_EXPERIMENTS.md` + `04_COMPUTATION/
   galois_duality_experiments.py`, `galois_experiments_log.txt`, `galois_t2_check.py`,
   `galois_t2_log.txt` — **Task 1**.
3. `02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md` +
   `04_COMPUTATION/alahmadi_reconciliation.py`, `alahmadi_reconciliation_log.txt` —
   **Task 3**.
4. `02_PHASE_REPORTS/Phase_0/PHASE0_REVISION_REPORT.md` and
   `02_PHASE_REPORTS/Phase_0/UPDATED_PHASE0_FINAL_RECOMMENDATION.md` — the summary and the
   updated GO/MODIFY/STOP.
5. `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` (the live register; the original
   `theorem_register.md` is retained for comparison).
6. `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` (including the list of 13 bugs
   found and fixed — please scrutinise it).
7. `01_LITERATURE/annotated_bibliography.md`, `references.bib`, `comparison_matrix.md`.

## TASK

1. **Check the proofs** in `PAIRING_COMPLETE_PROOFS.md`, especially:
   * Thm 3.4 — the dual of *any* subset (in particular of a right module) is a **right**
     module (this is the load-bearing statement; please verify the side bookkeeping);
   * Thm 3.5 — $|C||C^{\perp_s}|=|R|^n$ for right submodules (where is the
     Frobenius/non-degeneracy of $\Lambda$ used?);
   * Thm 3.6 — $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$;
   * **Thm 3.9 — the reflexivity criterion “$(C^{\perp_s})^{\perp_s}=C$ for all right
     $R$-submodules $\iff r\mid 2s$”**, including the counterexample
     $W=A_t(e_1+ae_2)$ when $r\nmid2s$ (is the Morita step, and the claim
     $\sigma_{2s}(I_W)=I_{\sigma_{2s}(W)}$, airtight for every $t\ge1$, $m\ge2$?);
   * Prop 4.1 — the $R$-valued and the $\Lambda$-valued duals coincide;
   * Prop 5.1 — the plain product $\sum x_iy_i$ is perfect for **left** modules and broken
     for **right** ones.
   If anything is wrong or incomplete, say **exactly** what is missing; do not repair it
   silently.
2. **Check the enumeration formula (register T-018).** We claim that for $t=1$, if
   $X^n-1=\prod_j f_j$ over $\mathbb F_q$ with $\deg f_j=d_j$, then the cyclic codes of
   length $n$ over $M_m(\mathbb F_q)$ are in bijection with tuples of subspaces and
   $$\#\{\text{cyclic codes}\}=\prod_j\sum_{i=0}^{m}\begin{bmatrix}m\ i\end{bmatrix}_{q^{d_j}}.$$
   Our validations: $343=7^3$ ($q=4,m=2,n=3$), $737=11\cdot67$ ($q=8,m=2,n=3$),
   $144=12^2$ ($q=9,m=2,n=2$), $5$ and $35=5\cdot7$ ($q=2,m=2,n=1,3$), plus a second,
   independent enumeration at $q=2$. Is the formula (and the claim that the factorization
   must be taken over the **centre** $\mathbb F_q$, not over a non-central subfield) correct?
3. **Adjudicate U8 (the Alahmadi et al. 2013 question).** We rebuilt their ring
   $A=M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$, $u=1+i$, $i\omega=\omega^2i$,
   $u^2=0$, $u$ not central, and computed exhaustively: **5** cyclic codes at $n=1$ and
   **35** at $n=3$. Their Theorem 1 parametrises $3^3=27$ triples $(f,g,h)$ with
   $fgh=X^n-1$ over $\mathbb F_4[X]$; under three readings of $C=(fh)+u(fg)$ we obtain
   9, 4 or 15 cyclic codes — never 35 — and we found that a triple yields a right ideal
   **iff** $f,g,h\in\mathbb F_2[X]=Z(A)[X]$ (9 vs 0 vs 0 vs 18 at $n=3$; 3 vs 0 vs 0 vs 0
   at $n=1$). Their Lemma 2's list of right $A$-submodules $\{(0),(u),(1)\}$ is incomplete
   at $n=1$ (we find 5). We make **no claim that their theorem is wrong**; we ask:
   (i) which reading of $(fh)+u(fg)$ is correct, (ii) is our computation or our reading at
   fault, (iii) may anything about that paper be claimed in our manuscript?
4. **Answer U9 — is reflexivity actually required?** Our Thm 3.9 says the duality is
   reflexive iff $r\mid2s$, which would force $q=p^{2e}$, $s=r/2$ and exclude $q=8$. For a
   hull-based quantum construction (LCD / hull-dimension / CSS / EAQECC style), do we need
   $(C^{\perp_s})^{\perp_s}=C$ for all $C$, or is the size formula + hull closure enough?
   This single answer changes our parameter family, so please be explicit.
5. **Novelty checks (unchanged, still open).**
   * **U3:** is there a published Nebe–Rains–Sloane-type (or Wood-type) treatment of
     duality for codes over rings via an **anti-isomorphism** (as opposed to an
     automorphism)? Exact reference, please — it would be the conceptual precursor of the
     $\theta$-duality.
   * **U4:** do you know of any paper defining a **Galois / $\sigma$-dual or Galois hull
     over a non-commutative ring**, or constructing a **quantum code from a code over a
     matrix ring**? (These are the falsifiable novelty tests for GAP 1 and GAP 3.)
6. **Sanity-check the parameter advice.** Given the results, we recommend $q=p^{2e}$,
   $s=r/2$, $m=2$, $t=1$ first, $t\ge2$ second. Is there a reason to prefer a different
   family (e.g. $t=2$ directly, or $m=4$)?

## RETURN A STRUCTURED AUDIT

**A. Overall verdict:** ACCEPT / ACCEPT WITH MINOR REVISIONS / MAJOR REVISION / REJECT /
INSUFFICIENT EVIDENCE.
**B. Correct results** (what Arena got right).
**C. Critical mathematical errors** (if any) — with file and theorem number.
**D. Missing lemmas / proofs.**
**E. Literature and novelty concerns**, including the U3 / U4 answers.
**F. U8 adjudication** (reading, fault, permitted claims).
**G. U9 adjudication** (is reflexivity required? which parameter family?).
**H. Required corrections, prioritised.**
**I. GO / REVISE / STOP phase-gate recommendation** for the Phase-0 → Phase-1 gate.
**J. The exact next Arena prompt** (Phase 1), but only if progression is justified.

Do not advance to the next phase if foundational assumptions or proofs fail. Explain the
audit in accessible Hindi/Hinglish, but write replacement mathematics and paper-ready text
in formal academic English/LaTeX.
