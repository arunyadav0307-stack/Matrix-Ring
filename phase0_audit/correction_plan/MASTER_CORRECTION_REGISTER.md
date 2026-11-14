# Master correction register

**Recorded planning execution:** 2026-11-13 UTC.  
**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**

## 1. Counts, severity and provenance

This register expands **all 43 CR01–CR43 issue families** from the independent review into **CP01–CP43**, one to one. It does not silently modify that review. There are **8 CRITICAL HOLD blockers**, **29 MAJOR** actions and **6 MINOR** actions. CR03 is escalated from the audit's MEDIUM to MAJOR because direct source reading finds inconsistent ring/example/proof typing in the current failure lemma. Other source-reading refinements stay inside their existing issue families and do not create a misleading extra count.

**Blocking-count definition:** the 8 inherited BLOCKING findings are the 8 CRITICAL actions below. Six are mathematical theorem/proof/route failures, one is physical-alphabet benchmarking, and one is author/provenance/submission control. MAJOR prerequisites still must be satisfactorily closed, restricted or withdrawn before their dependent blocker can close; “not CRITICAL” does **not** mean optional. 43 is not a count of 43 false current manuscript theorems: several rows are ancillary errors, boundary controls or already-corrected historical overclaims.

Severity is separate from the independent audit's six mathematical classifications, which remain unchanged. All requested repairs/tests are **future obligations conditional on explicit implementation approval**. No proof, theorem, code, dataset or manuscript has been repaired by this plan.

| Critical ID | Audit ID | Blocker |
|---|---|---|
| CP10 | CR10 | Nonprincipal-hull theorem's failed direct-sum family |
| CP23 | CR23 | Stabilizer lemma hypotheses and nonbinary phases |
| CP24 | CR24 | EA Bob completion and Alice-only logical errors |
| CP25 | CR25 | Route-specific label groups and orthogonals |
| CP27 | CR27 | DC relative quotient and coset-distance scope |
| CP29 | CR29 | All-route bookkeeping identities |
| CP32 | CR32 | Physical-alphabet benchmark reconstruction |
| CP40 | CR40 | Authoritative staging baseline, submission status and author-only gates |

### Exact-path conventions and evidence

Every target below is expanded to the exact recovered manuscript path. `CAN/` targets explicitly mean the historical canonical source, not MS03. An ancillary-only issue lists the related manuscript consistency check and says no direct MS03 error was located; that is not a fabricated theorem defect.

- Primary baseline and complete version/time/hash inventory: [AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md](AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md).
- Independent [correction register](evidence/audit_reports/DISCREPANCY_AND_CORRECTION_REGISTER.md), [claim ledger](evidence/audit_reports/MATHEMATICAL_CLAIM_VERIFICATION.md), [pairing audit](evidence/audit_reports/PAIRING_AND_DUALITY_CRITICAL_AUDIT.md), [Gray audit](evidence/audit_reports/GRAY_MAP_EVIDENCE_AUDIT.md), [literature audit](evidence/audit_reports/LITERATURE_AND_NOVELTY_RECHECK.md).
- References to `independent_core_checks.json`, `critical_followup_checks.json`, `remaining_scope_checks.json` and `independent_28_code_checks.json` are the **existing** copied audit evidence under `evidence/audit_reports/evidence/`, not new execution results.
- Fresh source locators/refinements: [source-reading observations](evidence/source_reading_observations.md) and [statement locators](evidence/manuscript_statement_locators.csv).
- Machine-readable [action index](evidence/master_correction_register.csv) and [authored action definitions](evidence/correction_actions.json).
- Planned B00–B08 tests are specified in [COMPUTATIONAL_REPAIR_PLAN.md](COMPUTATIONAL_REPAIR_PLAN.md). All are **NOT RUN / NOT AUTHORIZED** in this task.

## 2. Action index

| ID ↔ audit | Group | Severity | Current disposition / scope | Dependencies |
|---|---|---|---|---|
| CP01 ↔ CR01 | A | MAJOR | ACTIVE PROOF RECONCILIATION; original summary remains immutable. | CP40 |
| CP02 ↔ CR02 | A | MAJOR | SUMMARY ERROR; MANUSCRIPT PROOF INTEGRATION GUARD. | CP01 |
| CP03 ↔ CR03 | A | MAJOR | ACTIVE MANUSCRIPT EXAMPLE/PROOF DEFECT; not merely a wording change. | CP01, CP02 |
| CP04 ↔ CR04 | A | MAJOR | ACTIVE SLOT-CLAIM DEFECT plus frozen-summary mirror error. | CP01 |
| CP05 ↔ CR05 | A | MAJOR | ACTIVE PROOF DEFECT; conditional result retained. | CP01, CP02 |
| CP06 ↔ CR06 | A | MAJOR | ANCILLARY-ONLY ERROR / MANUSCRIPT BOUNDARY GUARD. | CP04, CP05 |
| CP07 ↔ CR07 | A | MAJOR | ANCILLARY ERROR / ACTIVE NOTATION AND HYPOTHESIS GUARD. | CP01 |
| CP08 ↔ CR08 | A | MAJOR | STALE REPORT STATUS plus ACTIVE MANUSCRIPT SIDE/QUANTIFIER OBLIGATIONS. | CP05, CP07 |
| CP09 ↔ CR09 | A | MAJOR | ACTIVE MANUSCRIPT FALSE PREMISE. | CP07 |
| CP10 ↔ CR10 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 1. | CP08, CP09, CP11, CP12 |
| CP11 ↔ CR11 | B | MAJOR | ACTIVE REPRODUCIBILITY/PROVENANCE DEFECT; later helper already exists. | CP05, CP20 |
| CP12 ↔ CR12 | A | MINOR | VALID RESULT / REQUIRED ASSUMPTION AND PROOF-REFERENCE GUARD. | CP04, CP05 |
| CP13 ↔ CR13 | A | MAJOR | VALID RESTRICTED THEOREM / OVERBROAD READING AND TERMINOLOGY GUARD. | CP05, CP12 |
| CP14 ↔ CR14 | A | MAJOR | ACTIVE FALSE UNIVERSAL CLAUSE. | CP13 |
| CP15 ↔ CR15 | B | MAJOR | IMPLEMENTATION-SCOPE GUARD; no blanket withdrawal of the bilinear example. | CP13, CP14, CP20 |
| CP16 ↔ CR16 | A | MAJOR | ACTIVE OVERBROAD ROUTE CONSEQUENCE. | CP13, CP15 |
| CP17 ↔ CR17 | C | MINOR | ANCILLARY ERROR; CORRECT MANUSCRIPT LAW TO PRESERVE. | CP01, CP05 |
| CP18 ↔ CR18 | B | MINOR | SCRIPT DIAGNOSTIC ONLY; LOW NUMERICAL IMPACT. | CP12 |
| CP19 ↔ CR19 | B | MAJOR | ACTIVE EVIDENCE-SCOPE CORRECTION. | CP18 |
| CP20 ↔ CR20 | B | MAJOR | ACTIVE DOCUMENTATION/REPRODUCIBILITY DEFECT. | CP40 |
| CP21 ↔ CR21 | B | MAJOR | ACTIVE SCOPE/COMPLETENESS QUALIFICATION. | CP19, CP20 |
| CP22 ↔ CR22 | A | MAJOR | ACTIVE ODD-CHARACTERISTIC PROOF ERROR. | CP20, CP40 |
| CP23 ↔ CR23 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 2. | CP22 |
| CP24 ↔ CR24 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 3. | CP05, CP23 |
| CP25 ↔ CR25 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 4. | CP12, CP16, CP23, CP24 |
| CP26 ↔ CR26 | A | MAJOR | CORRECT R3 DEFINITION TO PRESERVE / UNAUTHORIZED-BRIDGE GUARD. | CP05, CP13, CP24 |
| CP27 ↔ CR27 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 5. | CP25 |
| CP28 ↔ CR28 | A | MAJOR | ACTIVE METRIC/PROOF DEFECT; RESTRICTED RESULT NOT REFUTED. | CP27 |
| CP29 ↔ CR29 | A | CRITICAL | OPEN CRITICAL MATHEMATICAL BLOCKER 6. | CP25, CP27 |
| CP30 ↔ CR30 | C | MINOR | ALREADY CORRECTED IN MS03 — PRESERVE, do not count as an unrepaired MS03 proof. | CP20, CP21 |
| CP31 ↔ CR31 | B | MAJOR | UNRECERTIFIED EXTRA SCOPE; explicit retain/withdraw author decision required. | CP10, CP11, CP20, CP25, CP27, CP29 |
| CP32 ↔ CR32 | D | CRITICAL | OPEN CRITICAL BENCHMARK BLOCKER 7. | CP20, CP25, CP27, CP29, CP31, CP33 |
| CP33 ↔ CR33 | D | MAJOR | ACTIVE FALSE AVAILABILITY CLAIM. | CP40 |
| CP34 ↔ CR34 | D | MAJOR | ACTIVE WRONG CITATION IDENTITY. | CP40 |
| CP35 ↔ CR35 | D | MAJOR | ACTIVE METADATA CORRECTIONS plus already-correct values to preserve. | CP34 |
| CP36 ↔ CR36 | D | MAJOR | ACTIVE ATTRIBUTION/CLAIM-SCOPE REVIEW; external novelty remains unverified. | CP10, CP12, CP24, CP25, CP28, CP31, CP32, CP34, CP35 |
| CP37 ↔ CR37 | D | MAJOR | ANCILLARY PROPOSAL QUARANTINE / NOT A NEW MANUSCRIPT RESULT. | CP26, CP36 |
| CP38 ↔ CR38 | D | MAJOR | ANCILLARY PROPOSAL QUARANTINE. | CP07, CP36 |
| CP39 ↔ CR39 | D | MAJOR | ANCILLARY PROPOSAL QUARANTINE. | CP04, CP36 |
| CP40 ↔ CR40 | C | CRITICAL | OPEN CRITICAL AUTHOR/PROVENANCE BLOCKER 8; current status AUTHOR CONFIRMATION REQUIRED. | Author gate; no predecessor |
| CP41 ↔ CR41 | C | MINOR | ACTIVE COUNTING-BASIS CLARIFICATION. | CP40 |
| CP42 ↔ CR42 | C | MAJOR | ACTIVE PROVENANCE/BUILD SCOPE LIMIT; no TeX compilation authorized now. | CP40 |
| CP43 ↔ CR43 | C | MINOR | ATTRIBUTION/PRESERVATION CONTROL. | CP19, CP21, CP30 |

## 3. Detailed action cards — eleven explicitly numbered fields

### CP01 — Right action and polynomial-module closure

**Group:** A. **Disposition:** ACTIVE PROOF RECONCILIATION; original summary remains immutable.

**1. Issue ID:** CP01 (audit CR01).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:21-36 (def:code, eq:morita)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:9-40 (def:pairing, lem:sesqui); 52-117 (thm:duality(a))`

**3. Relevant theorem / equation / proof:** def:code; eq:morita; def:pairing; lem:sesqui; thm:duality(a), especially its polynomial-closure proof.

**4. Defect explanation:** The frozen PHASE0_PAIRING_OPTIONS.md P1 uses ax instead of xa. MS03 correctly types central-field sesquilinearity, but its polynomial-closure proof at lines 69-93 asserts an unestablished trace/Frobenius/convolution equality. A correct theorem in the supporting proofs does not validate this particular derivation.

**5. Independent-audit evidence / source-reading refinement:** CR01; D01/D02/D07; pairing audit §2; independent_core_checks.json: summary_ax_formula_counterexample; supplemental source observations CP01.

**6. Required mathematical / editorial correction — future only:** After approval, retain the first-slot theta/right-module convention and rebuild the constant-R closure and cyclic-shift/R_n closure argument from the correctly sided supporting proof. Check convolution indices separately. Amend the manuscript only in the authorized successor; record frozen-summary errata separately.

**7. New proof required?:** YES — a manuscript proof rewrite/reconciliation, using existing validated material; no new theorem or left-module research is requested.

**8. Computational verification required — NOT RUN:** B02: reproduce the recorded E12/E21 wrong-action negative control; verify constant right multiplication and cyclic shifts for retained small codes, including a nonreflexive example. No such test is run in this planning task.

**9. Impact on quantum-code parameters:** No automatic change to N,k,K,c,d of the 28 independently checked records. This is a foundational dependency for any ring-origin/closure claims.

**10. Severity:** MAJOR.

**11. Dependencies:** CP40

### CP02 — Nondegeneracy probe versus perfect-duality argument

**Group:** A. **Disposition:** SUMMARY ERROR; MANUSCRIPT PROOF INTEGRATION GUARD.

**1. Issue ID:** CP02 (audit CR02).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:62-95 (lem:lambda)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:52-117 (thm:duality(b))`

**3. Relevant theorem / equation / proof:** eq:Lambda / lem:lambda; thm:duality(b); ancillary P1 nondegeneracy probe versus the existing supporting Proposition 2.2.

**4. Defect explanation:** The summary's E_ba probe can give zero after transpose; elementwise nondegeneracy itself is valid. Neither that invalid probe nor nondegeneracy alone supplies the required same-module cardinality theorem.

**5. Independent-audit evidence / source-reading refinement:** CR02; D03/D04/D09; pairing audit §§3-4; core test summary_matrix_unit_nondegeneracy_probe_fails. The supporting S Proposition 2.2 uses a valid identity probe.

**6. Required mathematical / editorial correction — future only:** Make the manuscript's probe/functional arguments and proof imports explicit and consistent; distinguish nondegeneracy from size/perfect-pairing hypotheses. Preserve the valid top-coefficient/matrix-trace functional.

**7. New proof required?:** YES — explicit proof integration/justification of the existing claim, not discovery of a new result.

**8. Computational verification required — NOT RUN:** B02: retain the failing proposed probe as a negative control and separately test nonzero-coordinate/identity probes in both variables; keep size tests distinct.

**9. Impact on quantum-code parameters:** No direct numerical parameter change established; incorrect size reasoning would undermine dimension provenance downstream.

**10. Severity:** MAJOR.

**11. Dependencies:** CP01

### CP03 — Plain-product failure lemma and incompatible example data

**Group:** A. **Disposition:** ACTIVE MANUSCRIPT EXAMPLE/PROOF DEFECT; not merely a wording change.

**1. Issue ID:** CP03 (audit CR03).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:97-128 (lem:failure, rem:convention)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:86-97 (duality novelty wording)`

**3. Relevant theorem / equation / proof:** lem:failure and its printed example/proof; rem:convention; duality-origin wording in section 9.

**4. Defect explanation:** Unqualified 'degenerate' conflates elementwise and same-sided perfect duality. Fresh source inspection also finds lem:failure naming M2(F2), t=2 and C=uR simultaneously, then mixing ring-product and trace-scalar annihilators; the generic finite-Frobenius-ring quantifier is proved using Fq-specific objects. These are not a coherent typed example/proof.

**5. Independent-audit evidence / source-reading refinement:** CR03; D05/D06; pairing audit §3; core test plain_pairing_nondegenerate_but_wrong_same_side_size; supplemental source observations CP03. Severity raised from the audit's MEDIUM to MAJOR because the current lemma itself needs reconciliation.

**6. Required mathematical / editorial correction — future only:** Use one consistently specified existing counterexample and correctly sided annihilator theorem, distinguishing the ring-valued and scalar products. State what fails without denying all plain/opposite-sided duality. Do not characterize the choice of right rather than left codes as mathematically forced in every framework.

**7. New proof required?:** YES — repair the existing failure lemma and its scope; cite an applicable foundation rather than asserting an invalid balance argument.

**8. Computational verification required — NOT RUN:** B02: recheck the audit's finite example and each claimed size using exactly the selected ring/module/product; use the historical plain-product failure counts only at their recorded scope.

**9. Impact on quantum-code parameters:** No supplied tuple is numerically refuted by this issue; it changes justification and overbroad origin/necessity claims.

**10. Severity:** MAJOR.

**11. Dependencies:** CP01, CP02

### CP04 — Slot/mirror convention and double-twist orientation

**Group:** A. **Disposition:** ACTIVE SLOT-CLAIM DEFECT plus frozen-summary mirror error.

**1. Issue ID:** CP04 (audit CR04).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:43-48 (slot-immaterial paragraph); 52-117 (thm:duality(c))`

**3. Relevant theorem / equation / proof:** Unnumbered slot-immaterial paragraph, section 4 lines 43–48; thm:duality(c); alternate-left mirror in the frozen pairing-options summary.

**4. Defect explanation:** The summary transfers a positive double twist to a different left mirror. MS03 additionally says placing theta in the other slot gives the same dual and calls the map an involution without the reflexivity condition. This is incompatible with the audit's convention-sensitive positive/negative twist distinction.

**5. Independent-audit evidence / source-reading refinement:** CR04; D10-D15; pairing audit §§5-6; follow-up alternate_left_mirror_has_negative_double_twist; supplemental source observations CP04.

**6. Required mathematical / editorial correction — future only:** Keep one explicit right-module first-slot convention. Remove or precisely qualify the slot-immaterial claim; if alternate/left conventions are retained, state their own side, inverse parameter and DD convention with proof. Safest correction-only option is to omit unused alternatives, not develop them.

**7. New proof required?:** YES if an equivalence/alternate is retained; otherwise delete the unsupported equivalence and integrate the existing first-slot proof. Do not replace +sigma_2s by a negative twist in the primary convention.

**8. Computational verification required — NOT RUN:** B02: use the recorded F8 positive-versus-negative DD and alternate-left negative-control cases; compare actual subspaces, not dimensions alone.

**9. Impact on quantum-code parameters:** A convention change can change dual/hull spaces and route hypotheses. Any actual convention migration would require separate recertification; none is authorized here.

**10. Severity:** MAJOR.

**11. Dependencies:** CP01

### CP05 — Scalar/ring orthogonal equality and its printed proof

**Group:** A. **Disposition:** ACTIVE PROOF DEFECT; conditional result retained.

**1. Issue ID:** CP05 (audit CR05).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:62-95 (eq:Lambda, lem:lambda)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:209-228 (prop:twoorth)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:111-148 (thm:grayduality, thm:grayhull)`

**3. Relevant theorem / equation / proof:** eq:Lambda; lem:lambda; prop:twoorth, especially full-Hom-surjectivity proof; thm:grayduality and thm:grayhull dependencies.

**4. Defect explanation:** The valid orthogonal equality needs right-module closure and the functional/ideal-catching step. MS03 prop:twoorth instead asserts surjectivity onto full Hom_Fq(C,R) from nondegeneracy, which does not justify the required dimension count; semilinearity/codomain types also need attention.

**5. Independent-audit evidence / source-reading refinement:** CR05; D08/D09; pairing audit §4; remaining-scope scalar_orthogonal_requires_module_hypothesis; supplemental source observations CP05.

**6. Required mathematical / editorial correction — future only:** Replace the unsupported surjectivity proof by a correctly typed module/functional argument or an applicable cited Frobenius result; explicitly retain the right-R hypothesis. Keep matrix trace, top coefficient and absolute field trace distinct.

**7. New proof required?:** YES — repair the printed proof of an already conditionally verified equality; the theorem is not being declared false.

**8. Computational verification required — NOT RUN:** B02/B04: retain the non-module subspace negative control (dual dimensions 2 versus 3), and compare ring/scalar orthogonals on retained actual modules and the exact Gray ordering.

**9. Impact on quantum-code parameters:** Foundational for transporting ring-origin hulls. No automatic substitution of transported hull dimension for Euclidean h_E is permitted.

**10. Severity:** MAJOR.

**11. Dependencies:** CP01, CP02

### CP06 — Unused A-valued candidate and inverse-parameter reconciliation

**Group:** A. **Disposition:** ANCILLARY-ONLY ERROR / MANUSCRIPT BOUNDARY GUARD.

**1. Issue ID:** CP06 (audit CR06).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:9-48 (def:pairing and fixed slot convention); consistency guard only`

**3. Relevant theorem / equation / proof:** def:pairing / fixed slot convention: manuscript consistency guard only. The disputed P3 candidate is ancillary, not an existing MS03 theorem to replace.

**4. Defect explanation:** The separate frozen pairing-options P3 candidate is not established as the same +s right-module dual; its trace comparison involves the inverse parameter and its side sketch is wrong. No such alternate construction needs to be added to MS03.

**5. Independent-audit evidence / source-reading refinement:** CR06; D15; pairing audit §6.

**6. Required mathematical / editorial correction — future only:** Exclude the unused candidate from the manuscript's asserted framework or, only with separate approval, reconcile all sides/parameters. Add an append-only ancillary clarification; do not edit the six frozen reports.

**7. New proof required?:** NO for exclusion. YES if the author insists on retaining a claimed equivalence; that extension is not automatically part of a correction-only authorization.

**8. Computational verification required — NOT RUN:** No new test required if excluded; if retained, B02 must compare actual ring/scalar orthogonals with the inverse-parameter convention.

**9. Impact on quantum-code parameters:** None for the existing first-slot 28-record campaign if this unused candidate is excluded.

**10. Severity:** MAJOR.

**11. Dependencies:** CP04, CP05

### CP07 — Base matrix ring versus cyclic ambient ring

**Group:** A. **Disposition:** ANCILLARY ERROR / ACTIVE NOTATION AND HYPOTHESIS GUARD.

**1. Issue ID:** CP07 (audit CR07).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:9-59 (eq:rings, eq:morita, lem:basic)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:79-116 (prop:moritahull and chain-ring discussion)`

**3. Relevant theorem / equation / proof:** eq:rings; eq:morita; lem:basic; prop:moritahull and base-chain-ring versus cyclic-B discussion. Ancillary base-ideal assertion is the direct false claim.

**4. Defect explanation:** The frozen feasibility report's 'most base-R one-sided ideals nonprincipal' claim is false. The manuscript must not confuse A_t-submodules of A_t^2 with B-submodules of B^2, where the wild behavior occurs.

**5. Independent-audit evidence / source-reading refinement:** CR07; F06-F09; pairing audit §7; core base_matrix_ring_ideals_are_principal_in_tested_case.

**6. Required mathematical / editorial correction — future only:** Make the base/cyclic distinction explicit and retain correct Morita column-generator thresholds. Use an append-only erratum for the frozen report rather than rewriting it.

**7. New proof required?:** NO new theorem; provide a correctly cited/justified at-most-two-generation statement where used.

**8. Computational verification required — NOT RUN:** B03: keep the recorded 33-submodule base-ring case as a finite regression, not the general proof.

**9. Impact on quantum-code parameters:** No direct change to supplied tuples; prevents treating a general nonprincipal code as an automatically nonprincipal hull.

**10. Severity:** MAJOR.

**11. Dependencies:** CP01

### CP08 — Principality status, annihilator sides and cyclic/principal distinction

**Group:** A. **Disposition:** STALE REPORT STATUS plus ACTIVE MANUSCRIPT SIDE/QUANTIFIER OBLIGATIONS.

**1. Issue ID:** CP08 (audit CR08).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:185-238 (eq:crt, lem:components)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:59; 114-116; 131-207 (lem:ann, thm:dualformula, cor:rev)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:79-96 (prop:moritahull)`

**3. Relevant theorem / equation / proof:** eq:crt; lem:components; thm:duality(d); lem:ann; thm:dualformula; cor:rev; prop:moritahull. Existing S2B Theorems 4.1/4.3/Corollary 4.4 resolve the old open-status claim.

**4. Defect explanation:** The general matrix-size-2 principality criterion is already proved in S2B, so the frozen open-status claim is stale. MS03 also conflates cyclic with principal, uses unreviewed generator/annihilator-side reductions and asserts principality from a single-element annihilator. Its reversal corollary needs per-code rather than blanket quantifier review.

**5. Independent-audit evidence / source-reading refinement:** CR08; F07-F10/D16; S2B Theorems 4.1/4.3/Corollary 4.4; pairing audit §7; supplemental source observations CP08. These extra manuscript proof obligations were located by source reading, not claimed repaired.

**6. Required mathematical / editorial correction — future only:** Import the existing criterion with exact hypotheses; separate shift-cyclic from one-generator. Reprove the used annihilator/reversal formula with correct left/right generators, and restrict or withdraw unsupported principal-dual/universal reversal consequences. Do not use the failed hull family to fill this gap.

**7. New proof required?:** YES — manuscript side/annihilator proof reconciliation. Any stronger principal-dual assertion lacking an existing valid proof must be withdrawn or separately approved, not invented now.

**8. Computational verification required — NOT RUN:** B02/B03: check retained annihilator/reversal formulas on n>=3 examples, zero/full ideals and wild/nonprincipal cases; compare subspaces and generator numbers separately.

**9. Impact on quantum-code parameters:** Can affect claimed origin/principality of hull examples and code-family coverage. Field-code matrices that already pass independent certification are not automatically invalidated.

**10. Severity:** MAJOR.

**11. Dependencies:** CP05, CP07

### CP09 — Chain-ring generation is not freeness

**Group:** A. **Disposition:** ACTIVE MANUSCRIPT FALSE PREMISE.

**1. Issue ID:** CP09 (audit CR09).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:98-103 (opening sentence of non-principal-hull subsection)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:200-232 (lem:components)`

**3. Relevant theorem / equation / proof:** False freeness premise opening the section 5 non-principal-hull subsection; generation argument used by lem:components.

**4. Defect explanation:** The assertion that every submodule of a free chain-ring module is free is false; only the generation bound needed here survives.

**5. Independent-audit evidence / source-reading refinement:** CR09; F11; pairing audit §7; the audit records uA of size 4 inside an A of size 16.

**6. Required mathematical / editorial correction — future only:** Remove the false freeness premise and justify only the generation bound actually used; check all occurrences of rank/free/generator-number for conflation.

**7. New proof required?:** YES — a valid justification/citation for the replacement premise, not a new structural theorem.

**8. Computational verification required — NOT RUN:** B03: retain torsion submodule examples as regression controls and compute module generator number independently of field rank.

**9. Impact on quantum-code parameters:** No direct change to rank/distance of the 28 field codes; repairs the principality/hull reasoning.

**10. Severity:** MAJOR.

**11. Dependencies:** CP07

### CP10 — Nonprincipal-hull theorem's failed direct-sum family

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 1.

**1. Issue ID:** CP10 (audit CR10).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:118-165 (thm:nonprincipal, eq:witnessfamily); 167-249 (tab:witnesses, rem:o31b, thm:noclosed)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:319-379 (ex:witnessA, ex:witnessB)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:147-166 (abstract); sections/09_comparison.tex:93-116 (novelty items)`

**3. Relevant theorem / equation / proof:** thm:nonprincipal; eq:witnessfamily; tab:witnesses; rem:o31b; thm:noclosed; ex:witnessA/B; dependent abstract and novelty claims.

**4. Defect explanation:** The claimed Be1 direct sum with the full two-dimensional socle has nonzero intersection. The audit obtains sum dimension 5, radical dimension 3 and mu=2, not 3. Assertions of an exhaustively enumerated family do not fix that proof.

**5. Independent-audit evidence / source-reading refinement:** CR10; D18/D19; follow-up manuscript_nonprincipal_i0_family_proof_fails. The separate historical_nonprincipal_selfdual_hull_witness is valid at (4,2,2) with mu=3 and is not this family.

**6. Required mathematical / editorial correction — future only:** Author must choose to withdraw the invalid family and restrict to an already verified explicit witness, or authorize a separately reviewed proof replacement. Audit all dependent no-single-generator, witness-family and abstract claims. Do not assert a new generic family or settle the principal-code hull question.

**7. New proof required?:** YES if hull-existence/refutation is retained: an explicit, correctly justified existing witness and its Morita generator calculation must replace the failed presentation. No replacement theorem/proof is produced by this plan.

**8. Computational verification required — NOT RUN:** B03: reproduce the existing valid witness and the failed-family negative control; any retained extra wild witnesses require full explicit basis, hull and radical checks under CP31, not randomized failure to find generators.

**9. Impact on quantum-code parameters:** The 28 supplied field records remain independently valid. Additional nonprincipal-origin/R1/headline rows, especially the (9,2,3) and (4,2,4) examples, remain qualified until CP31; do not claim repaired ring provenance for them.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP08, CP09, CP11, CP12

### CP11 — Phase5 hull row-representation bug

**Group:** B. **Disposition:** ACTIVE REPRODUCIBILITY/PROVENANCE DEFECT; later helper already exists.

**1. Issue ID:** CP11 (audit CR11).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:167-224 (witness census, rem:mub)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:75-94 (non-principal witnesses)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:56-84 (where numbers come from)`

**3. Relevant theorem / equation / proof:** Phase5 Task D3 lines 1364–1368 and the existing Phase6 hull_mu helper; manuscript rem:mub and witness-mu table interpretation. This is a representation bug, not a new theorem.

**4. Defect explanation:** research-data/scripts/phase5_quantum_constructions.py Task D3 lines 1364-1368 feeds full image rows to a Morita unpair helper. The audit reproduces wrong mu=4 versus correct mu=3; Phase6 already documents and avoids the error. The manuscript's code-mu/hull-mu explanation is not an adequate erratum for this bug.

**5. Independent-audit evidence / source-reading refinement:** CR11; D21; remaining-scope Phase5_hull_mu_coordinate_error_reproduced; phase6_quantum_parameter_enhancement.py:hull_mu.

**6. Required mathematical / editorial correction — future only:** After approval, isolate a corrected successor implementation or use the documented later helper, preserve the historical script/logs, and rebuild only affected mu outputs with clear lineage. Do not rewrite all data or hide the original defect.

**7. New proof required?:** NO new theorem; the mu/Nakayama justification belongs to CP10. A representation invariant/specification is required.

**8. Computational verification required — NOT RUN:** B03: assert expected row widths, compare proper Morita inter rows against full hrows, and cross-check mu on the known audit witness before regenerating affected tables.

**9. Impact on quantum-code parameters:** May change mu census and claimed nonprincipal provenance. It does not by itself change Euclidean rank, K,c or d of the 28 independently checked field generators.

**10. Severity:** MAJOR.

**11. Dependencies:** CP05, CP20

### CP12 — Double-dual, reflexivity and generalization hypotheses

**Group:** A. **Disposition:** VALID RESULT / REQUIRED ASSUMPTION AND PROOF-REFERENCE GUARD.

**1. Issue ID:** CP12 (audit CR12).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:132-183 (def:sigma, lem:theta, arbitrary-automorphism remark)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:52-117 (thm:duality(b,c)); 230-264 (def:regimes, prop:regimes)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:16-77 (thm:hullstruct)`

**3. Relevant theorem / equation / proof:** def:sigma; lem:theta and arbitrary-automorphism remark; thm:duality(b,c); def:regimes / prop:regimes; thm:hullstruct; supporting S Theorems 3.6/3.9.

**4. Defect explanation:** The audit retains the positive DD theorem and the universal criterion; only the short necessity sketch in supporting S Thm3.6 is insufficient by itself. A per-code invariant condition is not a global divisibility condition. The source's unused 'everything generalises verbatim' remark must not extend unverified Gray/metric/quantum claims.

**5. Independent-audit evidence / source-reading refinement:** CR12; D10-D13, N1-N12; S Thm3.9 supplies the valid slope-module argument; core double_dual_positive_not_negative_direction and nonreflexive_zero_relation_witness.

**6. Required mathematical / editorial correction — future only:** Retain +sigma_2s and state right module, coefficient Frobenius fixing u/X, dimension/size and matrix-size hypotheses. Cite the sound necessity argument; separate single-code invariance from universal reflexivity. Restrict unused generalizations rather than opening a new automorphism program.

**7. New proof required?:** NO new theorem. Explicit integration of an existing valid proof/hypothesis chain is required; any stronger unused generalization should be omitted unless separately approved.

**8. Computational verification required — NOT RUN:** B02: retain the F8 positive/negative/DD-versus-C cases and a per-code invariant example in a nonreflexive regime; test inclusions as sets, not just equal dimensions.

**9. Impact on quantum-code parameters:** No direct change to 28 Euclidean-code records. Misusing reflexivity would affect hull/route applicability, so this is a prerequisite despite MINOR editorial/hypothesis severity.

**10. Severity:** MINOR.

**11. Dependencies:** CP04, CP05

### CP13 — Bilinear versus Hermitian congruence scope

**Group:** A. **Disposition:** VALID RESTRICTED THEOREM / OVERBROAD READING AND TERMINOLOGY GUARD.

**1. Issue ID:** CP13 (audit CR13).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:95-107 (cor:noteuclid); 231-292 (def:congruence, thm:obstruction, rem:obstructionexact)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:257-296 (thm:parameters and route recommendation)`

**3. Relevant theorem / equation / proof:** cor:noteuclid; def:congruence; thm:obstruction; rem:obstructionexact; related thm:parameters scope. Retain the valid restricted bilinear theorem.

**4. Defect explanation:** The bilinear characteristic-two/even-t obstruction is valid under the manuscript's sigma=id congruence definition. It is false when read as a prohibition on all Hermitian/sesquilinear congruences. General first-slot Galois forms must not be called involutive Hermitian without conditions.

**5. Independent-audit evidence / source-reading refinement:** CR13; G08-G10; Gray audit §4; core char2_even_t_Hermitian_congruence_counterexample.

**6. Required mathematical / editorial correction — future only:** Delimit the valid bilinear obstruction and distinguish general Galois sesquilinear, involutive Hermitian and ordinary Euclidean forms. Do not advertise the audit's Hermitian counterexample as a Hamming isometry or a new quantum route.

**7. New proof required?:** YES for any retained enlarged claim; the safe correction is a scope restriction preserving the existing valid bilinear proof.

**8. Computational verification required — NOT RUN:** B04: ordinary versus sigma-conjugate transpose congruence checks in the exact field encoding, plus Hamming-weight checks for any transformation actually retained.

**9. Impact on quantum-code parameters:** Can change route availability and transformed-coordinate distances, not N. No direct transport of d across a nonmonomial matrix is permitted.

**10. Severity:** MAJOR.

**11. Dependencies:** CP05, CP12

### CP14 — Alternatingness is characteristic- and form-dependent

**Group:** A. **Disposition:** ACTIVE FALSE UNIVERSAL CLAUSE.

**1. Issue ID:** CP14 (audit CR14).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:49-93 (thm:gram statement and last proof paragraph); 312-345 (ex:gray)`

**3. Relevant theorem / equation / proof:** thm:gram alternatingness clause and final proof paragraph; ex:gray.

**4. Defect explanation:** MS03 says J is alternating iff t is even without characteristic/type qualifications. Zero diagonal alone is not alternating in odd characteristic or a general Hermitian form.

**5. Independent-audit evidence / source-reading refinement:** CR14; G11; follow-up zero_diagonal_does_not_mean_alternating; Gray audit §4 gives the existing F9/F4 self-value controls.

**6. Required mathematical / editorial correction — future only:** Qualify the alternatingness clause and terminology while preserving the audited Gram matrix/transport identity; check all examples and downstream uses of that clause.

**7. New proof required?:** YES — a correct restricted form-classification argument, not a change to the verified Gram calculation.

**8. Computational verification required — NOT RUN:** B04: retain odd-characteristic bilinear and characteristic-two Hermitian negative controls, alongside the genuine bilinear characteristic-two alternating case.

**9. Impact on quantum-code parameters:** Affects congruence/route inference. Does not change the coefficient image or independently certified Euclidean records by itself.

**10. Severity:** MAJOR.

**11. Dependencies:** CP13

### CP15 — GF9 transformation tested for the correct form

**Group:** B. **Disposition:** IMPLEMENTATION-SCOPE GUARD; no blanket withdrawal of the bilinear example.

**1. Issue ID:** CP15 (audit CR15).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:238-264 (prop:congruence); 282-292 (rem:obstructionexact); 347-374 (ex:obstruction)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:177-203 (thm:R2)`

**3. Relevant theorem / equation / proof:** prop:congruence; rem:obstructionexact; ex:obstruction; thm:R2; actual Phase5 GF9 congruence matrix/form contract.

**4. Defect explanation:** The Phase5 GF9 T is a bilinear congruence, not the Hermitian congruence that a broader application might assume. The manuscript's restricted bilinear use must not be silently extended.

**5. Independent-audit evidence / source-reading refinement:** CR15; G12; follow-up stated_GF9_congruence_not_Hermitian; Gray audit §4.

**6. Required mathematical / editorial correction — future only:** Attach field basis, form type, Frobenius exponent and matrix orientation to each used transformation; restrict it to its proved use and recompute any affected physical-coordinate image.

**7. New proof required?:** NO new theorem for retaining the valid bilinear use. Any broader transformation claim needs proof and separate approval if it creates a new route.

**8. Computational verification required — NOT RUN:** B04: verify T^T H T and sigma(T)^T H T separately, invertibility, transformed G/dual and exact physical-coordinate distance when applicable.

**9. Impact on quantum-code parameters:** An invalid transformation can change CSS inclusion and d; k and N survive invertible linear changes but distance is not presumed invariant.

**10. Severity:** MAJOR.

**11. Dependencies:** CP13, CP14, CP20

### CP16 — Ambient obstruction is not a ban on every CSS code

**Group:** A. **Disposition:** ACTIVE OVERBROAD ROUTE CONSEQUENCE.

**1. Issue ID:** CP16 (audit CR16).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:266-280 (thm:obstruction consequence)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:177-203 (thm:R2); 257-296 (thm:parameters, route recommendation)`

**3. Relevant theorem / equation / proof:** thm:obstruction universal code-level consequence; thm:R2; thm:parameters and route recommendation.

**4. Defect explanation:** The consequence 'for every code the Euclidean/CSS route is not available' does not follow from a lack of ambient form congruence. The original Gray log already contains code-specific Euclidean self-orthogonality.

**5. Independent-audit evidence / source-reading refinement:** CR16; G17; Gray audit §4 and archived/reproduced log.

**6. Required mathematical / editorial correction — future only:** Restrict the impossibility statement to ambient bilinear-form equivalence and allow code-specific ordinary Euclidean inclusion checks. Do not infer new good codes or run a new search.

**7. New proof required?:** NO new theorem needed to remove the false consequence; retain the valid ambient obstruction and justify every actual CSS inclusion.

**8. Computational verification required — NOT RUN:** B04/B05: check ordinary Euclidean SO/DC inclusions for each retained image, independently of the transported-form result.

**9. Impact on quantum-code parameters:** May restore or exclude claimed route applicability for individual examples; the supplied 2 SO/1 DC records already passed actual inclusion checks.

**10. Severity:** MAJOR.

**11. Dependencies:** CP13, CP15

### CP17 — Scalar codomain and trace-level notation

**Group:** C. **Disposition:** ANCILLARY ERROR; CORRECT MANUSCRIPT LAW TO PRESERVE.

**1. Issue ID:** CP17 (audit CR17).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:62-95 (Lambda)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex:9-40 (lem:sesqui)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:14-43 (eq:weyl, eq:omega, lem:Q1)`

**3. Relevant theorem / equation / proof:** Lambda codomain / lem:sesqui; eq:weyl / eq:omega / lem:Q1 trace levels. The direct type error is in the ancillary Gray source, not the correctly typed MS03 central-scalar law.

**4. Defect explanation:** The supporting Gray document §0.2 prints a matrix multiplier on an Fq scalar output. MS03's central-field scalar law is correctly typed; it must stay distinct from the ring-valued matrix action and from the absolute trace.

**5. Independent-audit evidence / source-reading refinement:** CR17; G16; Gray audit §5; primary manuscript lem:sesqui.

**6. Required mathematical / editorial correction — future only:** Keep a codomain/linearity ledger for B_s, b_s, Lambda and Tr_Fq/Fp; use an append-only clarification for the frozen source error rather than changing the independent reports.

**7. New proof required?:** NO new proof if the correctly typed manuscript law is retained.

**8. Computational verification required — NOT RUN:** B02/B04 type-level assertions in a later authorized test harness; no matrix-valued RHS may be compared to a field scalar without an explicit map.

**9. Impact on quantum-code parameters:** Notation/proof applicability only; no established numerical change.

**10. Severity:** MINOR.

**11. Dependencies:** CP01, CP05

### CP18 — Tautological Gray reflexivity diagnostic

**Group:** B. **Disposition:** SCRIPT DIAGNOSTIC ONLY; LOW NUMERICAL IMPACT.

**1. Issue ID:** CP18 (audit CR18).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:43-84 (randomness and numbers); sections/04_cyclic_galois.tex:230-264 (regimes)`

**3. Relevant theorem / equation / proof:** Historical Gray script reflexivity header at line 982 versus actual C5 condition at line 1026; manuscript regime/reproduction description, not a refuted reflexivity theorem.

**4. Defect explanation:** The source script line 982 prints a tautological gcd-based reflexivity header. Its later line 1026 C5 assertion uses the correct criterion; this is not evidence that the substantive reflexivity tests were tautologies.

**5. Independent-audit evidence / source-reading refinement:** CR18; G15; Gray audit §5; research-data/scripts/phase4_gray_map_compatibility.py.

**6. Required mathematical / editorial correction — future only:** Correct the header only in an authorized successor script/log and document the historical diagnostic defect. Preserve old byte-identical rerun evidence.

**7. New proof required?:** NO; criterion/proof retained under CP12.

**8. Computational verification required — NOT RUN:** B04: include a globally nonreflexive header case and verify that actual C5 assertions still use the intended condition.

**9. Impact on quantum-code parameters:** No reported code parameter is invalidated by this diagnostic alone.

**10. Severity:** MINOR.

**11. Dependencies:** CP12

### CP19 — EXH/SMP and finite suite quantifiers

**Group:** B. **Disposition:** ACTIVE EVIDENCE-SCOPE CORRECTION.

**1. Issue ID:** CP19 (audit CR19).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:43-84 (scope and numbers)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:147-166 (abstract computation wording)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:168-212 (methodology)`

**3. Relevant theorem / equation / proof:** Finite-suite EXH/SMP quantifiers, appendix reproduction scope and section 8 methodology. No universal theorem is established by the count 463.

**4. Defect explanation:** 463 checks are mixed finite assertions (311 EXH/152 SMP), not 463 independent proofs/codes. Some pairing/symmetry Cartesian loops are capped at 120^2/50^2 despite inherited EXH labels.

**5. Independent-audit evidence / source-reading refinement:** CR19; G13/G14; Gray audit §§1/5; recorded full source rerun.

**6. Required mathematical / editorial correction — future only:** Report actual enumeration objects, samples, budgets and negative-control semantics. Keep proof references independent of check counts; amend labels only in new authorized evidence.

**7. New proof required?:** NO new theorem; any universal claim must cite a real proof rather than a test count.

**8. Computational verification required — NOT RUN:** B04/B06: inspect/log loop budgets and deterministic seeds; compare assertions before/after diagnostic corrections without promoting capped tests to exhaustive pair tests.

**9. Impact on quantum-code parameters:** No automatic numerical change; narrows completeness claims and prevents interpreting finite support as universal compatibility.

**10. Severity:** MAJOR.

**11. Dependencies:** CP18

### CP20 — Generator field encoding

**Group:** B. **Disposition:** ACTIVE DOCUMENTATION/REPRODUCIBILITY DEFECT.

**1. Issue ID:** CP20 (audit CR20).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:34-41 (environment); 56-102 (source and reproduction)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:7-73 (28-code certification table)`

**3. Relevant theorem / equation / proof:** Generator JSON/README environment and integer encoding contract; tab:cert / appendix environment description. No theorem identity needs replacement solely for metadata.

**4. Defect explanation:** Record documentation names matrix_ring_lib but matrices use ring_structure_checks.Field. GF8/GF9 integer labels use different irreducible polynomials in those implementations; an abstract field isomorphism is not an identity on recorded integers.

**5. Independent-audit evidence / source-reading refinement:** CR20; Gray audit §6; follow-up incorrect_field_documentation_has_real_effect: 5 dual mismatches among 15 q8/q9 records under the wrong encoding. The 28 independent checks used the actual encoding.

**6. Required mathematical / editorial correction — future only:** Safest path: preserve all matrix bytes and publish the actual basis/moduli/encoding and code producer. Any conversion to another basis would need explicit extra approval and a complete conversion proof, not silent relabelling.

**7. New proof required?:** NO new theorem for documentation repair. A migration, if separately approved, requires a verified explicit isomorphism.

**8. Computational verification required — NOT RUN:** B01: validate field tables, actual moduli GF8 x^3+x+1 and GF9 x^2+1, reproduce the existing encoding negative control, then compare all 28 matrices/duals with independent arithmetic.

**9. Impact on quantum-code parameters:** Wrong decoding can alter duals, hulls, inclusions and reported K,c,d. Existing correctly decoded records remain valid; do not rewrite their values without a new certificate.

**10. Severity:** MAJOR.

**11. Dependencies:** CP40

### CP21 — Historical census versus independent recertification scope

**Group:** B. **Disposition:** ACTIVE SCOPE/COMPLETENESS QUALIFICATION.

**1. Issue ID:** CP21 (audit CR21).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:214-333 (frontier, headline and budget tables)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:56-108 (numbers and limitations)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:147-166 (abstract scope)`

**3. Relevant theorem / equation / proof:** Frontier/headline/budget/census statements and abstract numerical scope; not an independent proof of every historical scanned code or distance row.

**4. Defect explanation:** Independent checking covers 28 supplied records and focused cases, not all 120721 scanned codes or 5055 distance rows. Historical census counts mix exact, sampled, blocked and counted-only families.

**5. Independent-audit evidence / source-reading refinement:** CR21; Q18; Gray audit §§1/6; included_source_run_summary.json; independent_28_code_checks.json.

**6. Required mathematical / editorial correction — future only:** Create a row-to-source/certificate scope map and limit manuscript claims accordingly. Either authorize bounded recertification of the specific additional retained claims or qualify/remove them; do not silently launch the entire campaign again.

**7. New proof required?:** NO for correct finite labels; theorem-level completeness would require a justified mathematical/enumeration argument outside a mere log total.

**8. Computational verification required — NOT RUN:** B06: reconcile exact/lower-bound flags and seeds from immutable logs; CP31 handles specific extra retained rows. No new family search is part of the default correction plan.

**9. Impact on quantum-code parameters:** May require relabelling unsupported optima/frontiers or lower bounds; does not refute the independently checked 28 exact distances.

**10. Severity:** MAJOR.

**11. Dependencies:** CP19, CP20

### CP22 — Odd-characteristic Weyl phase sign

**Group:** A. **Disposition:** ACTIVE ODD-CHARACTERISTIC PROOF ERROR.

**1. Issue ID:** CP22 (audit CR22).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:14-43 (eq:weyl, eq:omega, lem:Q1)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:45-111 (lem:Q2, thm:fpbasis)`

**3. Relevant theorem / equation / proof:** eq:weyl; eq:omega; lem:Q1; downstream lem:Q2 / thm:fpbasis phase convention.

**4. Defect explanation:** With the displayed X and Z definitions, the printed first XZ/ZX phase sign is wrong at odd p. Its own action calculation does not give the claimed sign after swapping.

**5. Independent-audit evidence / source-reading refinement:** CR22; Q02; follow-up odd_characteristic_Weyl_phase_sign_counterexample; mathematical audit §7.1.

**6. Required mathematical / editorial correction — future only:** Choose and consistently follow one existing Weyl/phase convention in an authorized manuscript successor. Reconcile product, commutator and symplectic signs throughout; do not use characteristic-two tests as proof of the odd-p relation.

**7. New proof required?:** YES — corrected elementary derivation, reviewed before the stabilizer/EA proofs. This plan does not supply replacement proof text.

**8. Computational verification required — NOT RUN:** B05: direct operator-action checks at p=3 and trace checks over GF9, plus characteristic-two controls.

**9. Impact on quantum-code parameters:** Zero-commutation sets are not changed merely by a global sign, so q9 tuples are not automatically false. Stabilizer phases/lifts still need CP23/CP24.

**10. Severity:** MAJOR.

**11. Dependencies:** CP20, CP40

### CP23 — Stabilizer lemma hypotheses and nonbinary phases

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 2.

**1. Issue ID:** CP23 (audit CR23).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:45-81 (lem:Q2 and proof); 83-111 (thm:fpbasis)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:126-203 (R1 and R2 uses)`

**3. Relevant theorem / equation / proof:** lem:Q2 statement/proof; thm:fpbasis; R1/R2 uses of the stabilizer result.

**4. Defect explanation:** The lemma assigns a common-eigenspace dimension to arbitrary additive labels without isotropy and a scalar-free, phase-correct stabilizer lift; the stated Weyl set is not automatically the asserted group. The general ±S/anti-commutes formulation is inappropriate at odd p.

**5. Independent-audit evidence / source-reading refinement:** CR23; Q01/Q03; follow-up arbitrary_additive_group_stabilizer_lemma_missing_isotropy; mathematical audit §7.1.

**6. Required mathematical / editorial correction — future only:** Author/quantum reviewer must provide a valid scoped stabilizer statement with isotropy, phase/lift and trivial-scalar conditions, correct distance/error-set conventions and nontrivial code domain. A standard cited theorem is safer than an unsupported 'nothing imported' derivation.

**7. New proof required?:** YES — rigorous proof rewrite or applicable authoritative theorem with fully checked hypotheses; not performed here.

**8. Computational verification required — NOT RUN:** B05: nonisotropic negative control, phase-closure and scalar-free checks in representative p=2 and p=3 cases; Fp-basis or full Fq-value tests as appropriate.

**9. Impact on quantum-code parameters:** Invalidates the printed universal justification, not the independently recertified matrices. All retained quantum routes depend on a correct stabilizer foundation.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP22

### CP24 — EA Bob completion and Alice-only logical errors

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 3.

**1. Issue ID:** CP24 (audit CR24).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:205-253 (thm:R3 and field-discipline remark)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:12-54 (EA distance use); 106-134 (feasibility)`

**3. Relevant theorem / equation / proof:** thm:R3 proof and field-discipline remark; EA distance uses in thm:cosetdistance / thm:feasibility. Standard conditional formulas are not refuted.

**4. Defect explanation:** The R3 proof gives an incompatible hyperbolic decomposition and claims every unextended v tensor I fixes the code. Nonisotropic Alice generators do not become an ordinary stabilizer without Bob completion; only the relevant Alice-only stabilizer part can be factored out.

**5. Independent-audit evidence / source-reading refinement:** CR24; Q08/Q09; mathematical audit §7.2; independent_28_code_checks.json records Gram rank and Bob commutator cancellation.

**6. Required mathematical / editorial correction — future only:** Supply a correct Bob-completed/phase-correct EA construction and derive its Alice-only error/degeneracy criterion under explicit Fq-linearity. Retain the standard conditional formulas only with that proof/citation; distinguish correctness from novelty.

**7. New proof required?:** YES — complete replacement of the defective argument, not a change of notation. No replacement theorem/proof is generated now.

**8. Computational verification required — NOT RUN:** B05: for retained EA matrices verify commutator rank, Bob cancellation, dimensions, actual h_E and appropriate relative distance; algebraic checks supplement rather than prove the universal quantum construction.

**9. Impact on quantum-code parameters:** Standard conditional EA K,c,d formulas and the 25 supplied EA records survive the audit; any new claim outside those conditions remains on hold.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP05, CP23

### CP25 — Route-specific label groups and orthogonals

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 4.

**1. Issue ID:** CP25 (audit CR25).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:118-203 (eq:V, thm:R1, thm:R1cap, thm:R2)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:257-296 (thm:parameters and proof)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:16-19 (dimension-field convention)`

**3. Relevant theorem / equation / proof:** eq:V; thm:R1; thm:R1cap; thm:R2; thm:parameters; standing dimension-field convention.

**4. Defect explanation:** The final parameter theorem uses an Fq-valued symplectic orthogonal for the generally only Fp-linear R1 graph, and uses V of original D for all R2 cases although DC has a different label group. The blanket Fq-dimension wording hides the distinction.

**5. Independent-audit evidence / source-reading refinement:** CR25; Q04-Q06; remaining-scope R1_trace_and_Fq_orthogonals_are_different; mathematical audit §7.1; the audit does not claim a minimum-distance difference from that set counterexample alone.

**6. Required mathematical / editorial correction — future only:** Make an explicit route contract for R1, SO, DC and EA, naming source/image code, D or transformed D', field of linearity, label group, correct orthogonal and excluded subspace. Ensure every proof and summary uses that contract.

**7. New proof required?:** YES — proof and theorem-scope reconciliation; standard valid SO/DC formulas are retained only with their actual hypotheses.

**8. Computational verification required — NOT RUN:** B05: repeat the R1 trace/Fq negative control and the 2 SO/1 DC inclusion checks; verify route-specific dimension and distance sets. Do not use equal dimensions to infer equal orthogonal spaces.

**9. Impact on quantum-code parameters:** Can change reported R1 distance interpretations and DC formulas. The supplied DC [[20,4,4]]_4 has N20,k12,h8 and must not be relabelled as an EA K0 code.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP12, CP16, CP23, CP24

### CP26 — Euclidean hull versus transported Galois hull in EA

**Group:** A. **Disposition:** CORRECT R3 DEFINITION TO PRESERVE / UNAUTHORIZED-BRIDGE GUARD.

**1. Issue ID:** CP26 (audit CR26).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:111-148 (transported dual/hull)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:113-124; 205-253 (definition of h_E and R3)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:98-126 (quantum bridge/novelty)`

**3. Relevant theorem / equation / proof:** thm:grayduality / thm:grayhull versus ordinary-Euclidean h_E in thm:R3. No unproved transported-Galois-hull-to-EA bridge is an existing result.

**4. Defect explanation:** The proposed application layer must not substitute a transported h_s for ordinary Euclidean h_E. MS03's R3 definitions correctly use h_E; no new Galois-to-EA bridge is established by the Gray theorem alone.

**5. Independent-audit evidence / source-reading refinement:** CR26; G03/G04 and Q10; mathematical audit and literature recheck P1 discussion.

**6. Required mathematical / editorial correction — future only:** Keep actual Euclidean h_E in the existing EA route and clearly distinguish it from transported hull dimensions. Omit any unproved equality/bridge. Proving a new twist-dependent bridge is new research and excluded.

**7. New proof required?:** NO if the existing correctly defined Euclidean route is retained and unsupported bridge claims are omitted; YES only under a separate new-research authorization.

**8. Computational verification required — NOT RUN:** B04/B05: compute both hulls separately where displayed, and derive K,c only from the route's actual input form.

**9. Impact on quantum-code parameters:** An unproved hull substitution can change K and c. No such automatic change should be imposed on the 28 validated Euclidean records.

**10. Severity:** MAJOR.

**11. Dependencies:** CP05, CP13, CP24

### CP27 — DC relative quotient and coset-distance scope

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 5.

**1. Issue ID:** CP27 (audit CR27).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:6-60 (thm:cosetdistance, eq:criterion)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:177-203 (thm:R2(b))`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:147-166 (abstract distance claim)`

**3. Relevant theorem / equation / proof:** thm:cosetdistance; eq:criterion; thm:R2(b); abstract universal distance interpretation.

**4. Defect explanation:** The single quotient Ddual/H_E and K=N-k-h_E does not represent DC for original D. The supplied DC record has true K4,d4, while that quotient has dimension 0.

**5. Independent-audit evidence / source-reading refinement:** CR27; Q11/Q13; route_and_bibliography_scope.json; independent_28_code_checks.json for 03_20_4_4_4_(4,1,5)_DC.json.

**6. Required mathematical / editorial correction — future only:** Scope relative quotients by route or explicitly relabel the stabilizer input throughout. Reconcile the low-weight criterion, abstract, certification interpretation and all dependent tables with the selected convention.

**7. New proof required?:** YES — route-correct statement/proof repair; no replacement theorem is drafted in this task.

**8. Computational verification required — NOT RUN:** B05: check the existing DC counterexample end to end, its quotient dimension and target/excluded subspaces; verify the route-specific coset target on all retained SO/DC/EA records.

**9. Impact on quantum-code parameters:** Directly corrects the K0-versus-K4 contradiction in manuscript bookkeeping without changing the independently valid DC tuple to K0.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP25

### CP28 — Coset-leader metric, projection proof and Singleton claim

**Group:** A. **Disposition:** ACTIVE METRIC/PROOF DEFECT; RESTRICTED RESULT NOT REFUTED.

**1. Issue ID:** CP28 (audit CR28).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:6-102 (thm:cosetdistance, thm:cosetsingleton, prop:newsbound)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:107-126 (new-bound claims)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:158-162 (abstract bound claim)`

**3. Relevant theorem / equation / proof:** thm:cosetdistance metric interpretation; thm:cosetsingleton projection proof; prop:newsbound and separate nonimplication/priority claims.

**4. Defect explanation:** A quotient with coset-leader weight is not automatically an ordinary coordinate Hamming linear code. Raw coordinate projection on cosets is not defined into the claimed vector space without specifying a compatible quotient/restriction. The defect is in the printed argument/interpretation, not a refutation of the restricted inequality.

**5. Independent-audit evidence / source-reading refinement:** CR28; Q12/Q14/Q15; remaining-scope quotient_is_not_ordinary_coordinate_Hamming_code (same coset representatives have weights 1 and 3); mathematical audit §7.3.

**6. Required mathematical / editorial correction — future only:** State the correct metric and route domain, including positive-dimensional/nonempty distance cases. If retained, justify the restricted bound by a valid argument identified in the audit or applicable citation; independently reassess prop:newsbound/nonimplication and priority. Do not claim the theorem has now been repaired.

**7. New proof required?:** YES — valid proof/codomain for the retained inequality and separate support for any nonimplication claim. The plan supplies obligations, not a proof.

**8. Computational verification required — NOT RUN:** B05: retain the F2 coset negative control and test quotient dimensions/relative minimum definitions for retained examples. Finite tests cannot establish novelty or the universal inequality.

**9. Impact on quantum-code parameters:** May alter a claimed bound's applicable route/scope, not the already certified example distances. K+d<=N+1 is retained conditionally by the audit, not declared false.

**10. Severity:** MAJOR.

**11. Dependencies:** CP27

### CP29 — All-route bookkeeping identities

**Group:** A. **Disposition:** OPEN CRITICAL MATHEMATICAL BLOCKER 6.

**1. Issue ID:** CP29 (audit CR29).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:106-166 (thm:feasibility, thm:bookkeeping and erratum)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:214-333 (frontier, bounds, budget)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/07_quantum.tex:257-296 (parameter summary)`

**3. Relevant theorem / equation / proof:** thm:feasibility; thm:bookkeeping and erratum; thm:parameters; downstream frontier/budget statements.

**4. Defect explanation:** EA identities are asserted for R1/SO/DC with the original k. R1 has a different K rule and DC requires its own stabilizer-input convention; the explicit audit examples contradict the universal statement.

**5. Independent-audit evidence / source-reading refinement:** CR29; Q16; remaining-scope R1_not_covered_by_EA_bookkeeping_identities; DC route-scope JSON: K-c=4 versus N-2k=-4.

**6. Required mathematical / editorial correction — future only:** Separate route formulas, parity/congruence consequences, entanglement-budget and feasibility claims. Do not silently redefine k halfway through a proof or transfer EA-only restrictions to DC/R1.

**7. New proof required?:** YES — route-scoped algebraic derivations and dependence review of every claimed consequence.

**8. Computational verification required — NOT RUN:** B05/B06: validate the existing R1 and DC counterexamples and check all retained table rows against explicit route contracts; reconcile captions/abstract and earlier errata.

**9. Impact on quantum-code parameters:** Direct effect on claimed K,c identities and feasibility/frontier interpretation. Do not 'correct' valid matrices/tuples to fit the false all-route rule.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP25, CP27

### CP30 — Certification-method historical overclaim already fixed in MS03

**Group:** C. **Disposition:** ALREADY CORRECTED IN MS03 — PRESERVE, do not count as an unrepaired MS03 proof.

**1. Issue ID:** CP30 (audit CR30).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:168-212; 335-368 (methodology and ex:certify)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:7-73 (tab:cert)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:162-167 (11/17 split)`
- `phase0_audit/extracted/prior_project/PAPER/sections/08_certification.tex (historical uncorrected counterpart)`

**3. Relevant theorem / equation / proof:** Section 8 methodology; ex:certify; tab:cert and staged abstract 11/17 split. Historical all-three claim is already corrected in MS03.

**4. Defect explanation:** Canonical §08 and the old certification log say all three methods ran for all examples. MS03 already corrects this. M2 is fallback, not a completed second exact method for every code; M3 is exact for 11 and lower-bound-only for 17.

**5. Independent-audit evidence / source-reading refinement:** CR30; Q17; Gray audit §6; Phase16/17 documents and Phase18 implementation record; source variant diff.

**6. Required mathematical / editorial correction — future only:** Preserve the corrected MS03 wording and its exact/lower-bound distinction. Add a lineage note for historical overclaims rather than repeating the correction as new or editing the old log.

**7. New proof required?:** NO; consistency/attribution check only.

**8. Computational verification required — NOT RUN:** B06: reconcile 24 M1+M3, 4 M2+M3, 11 exact M3, 17 lower-bound M3, 0 all-three; keep run/skipped/inapplicable states distinct.

**9. Impact on quantum-code parameters:** No change to certified distances; changes the strength/independence description of their support.

**10. Severity:** MINOR.

**11. Dependencies:** CP20, CP21

### CP31 — Extra wild/headline/R1 rows beyond the 28 certificates

**Group:** B. **Disposition:** UNRECERTIFIED EXTRA SCOPE; explicit retain/withdraw author decision required.

**1. Issue ID:** CP31 (audit CR31).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex:167-224; 319-379 (witnesses, ex:witnessA/B)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:245-283 (tab:headline)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:75-94 (witness summary)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:112-126 (nonprincipal-origin claim)`

**3. Relevant theorem / equation / proof:** ex:witnessA/B; tab:witnesses; tab:headline; additional nonprincipal-origin quantum claims. Extra rows are not included in the 28-record certificate verdict.

**4. Defect explanation:** The 28 supplied certificates do not certify every headline or wild/R1 row. Further claims based on the failed deterministic family remain unrecertified. Source ex:witnessB also calls an intersection-hull a 'proper superobject', contrary to its own definition.

**5. Independent-audit evidence / source-reading refinement:** CR31; D20/Q18; pairing and Gray audits; supplemental source observation CP31. No additional witness or distance was computed in this plan.

**6. Required mathematical / editorial correction — future only:** Author must list which extra rows to retain. For each, require an explicit immutable basis and complete ring/hull/form/route certificate, or qualify/remove the row and origin claim. Correct the superobject wording only after checking which code the narrative actually names.

**7. New proof required?:** YES for any retained theoretical origin claim depending on a defective family; explicit finite certificates alone do not prove a general family theorem.

**8. Computational verification required — NOT RUN:** B03/B05/B06: bounded checks of named retained witnesses only, full mu calculation, actual hull inclusion/equality, rank/h_E, R1 trace orthogonal and route-specific distance certificate or honest lower-bound label.

**9. Impact on quantum-code parameters:** Extra tuples such as [[24,6,2;2]]_9, [[24,14,2]]_9 and [[32,8,2;4]]_4 remain qualified. Their inclusion in prose does not inherit the 28-record verdict.

**10. Severity:** MAJOR.

**11. Dependencies:** CP10, CP11, CP20, CP25, CP27, CP29

### CP32 — Physical-alphabet benchmark reconstruction

**Group:** D. **Disposition:** OPEN CRITICAL BENCHMARK BLOCKER 7.

**1. Issue ID:** CP32 (audit CR32).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:6-78 (terms, tab:comparison, reading)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:96-120 (tab:grassl)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:214-333 (benchmark-dependent interpretation)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/01_introduction.tex and main.tex (summary benchmark language)`

**3. Relevant theorem / equation / proof:** tab:comparison; tab:grassl; all same-alphabet gap/record/ratio interpretations and related abstract/introduction claims.

**4. Defect explanation:** The legacy query q=4/9 was construction alphabet and returned physical q=2/3. MS03 explicitly relabels those headers as physical q=4/9 and uses invalid same-alphabet gaps/meets/factor comparisons.

**5. Independent-audit evidence / source-reading refinement:** CR32; Q19; literature audit §4; saved B01-B03. Correct physical-q4 N20,K4 probe has lower/upper 7..8; supplied d4 is at least 3 below a known d7 construction, not the old 2-gap claim.

**6. Required mathematical / editorial correction — future only:** Rebuild a bounded comparison for only the retained verified tuples using returned physical q, N,K, stabilizer/EA and entanglement conventions. Preserve old tables as historical, not silently patch them; remove unsupported record/gap/ratio claims pending verification.

**7. New proof required?:** NO new code-construction theorem; any optimality assertion requires valid external bound evidence and matching resource definitions.

**8. Computational verification required — NOT RUN:** B07: source/query/returned-header/date/bound/citation capture and row-by-row comparability checks. Do not produce the replacement benchmark dataset in this planning task.

**9. Impact on quantum-code parameters:** No construction tuple changes solely because a comparator was wrong. Claimed competitiveness/optimality/gaps change and must not be inferred from incompatible alphabets.

**10. Severity:** CRITICAL.

**11. Dependencies:** CP20, CP25, CP27, CP29, CP31, CP33

### CP33 — Availability claims about q8 and EA tables

**Group:** D. **Disposition:** ACTIVE FALSE AVAILABILITY CLAIM.

**1. Issue ID:** CP33 (audit CR33).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:12-27; 69-78 (table availability)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_tables.tex:96-120 (comparison notes)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/references.bib:187-end (GrasslCodetables)`

**3. Relevant theorem / equation / proof:** Table-availability prose and GrasslCodetables entry; no mathematical construction theorem is directly changed by an endpoint correction.

**4. Defect explanation:** An old 404 at a guessed endpoint does not prove no EA table exists, and physical-q8 stabilizer tables are available at least at the audit's checked tuple. Existing qubit/qutrit EA tables do not automatically benchmark q4/q8/q9 EA codes.

**5. Independent-audit evidence / source-reading refinement:** CR33; Q20; saved literature probes B04-B07.

**6. Required mathematical / editorial correction — future only:** Use precise endpoint/alphabet/query-specific statements and retrieval dates. Say 'no comparable bound established for this tuple' where appropriate, not universal table nonexistence.

**7. New proof required?:** NO; metadata/comparability verification, not a coding theorem.

**8. Computational verification required — NOT RUN:** B07: in a later approved comparison pass, save actual returned headers and alphabet/resource filters; a failed query stays a failed query.

**9. Impact on quantum-code parameters:** None directly; affects benchmarking eligibility and limitations, not validity of a q8 EA generator.

**10. Severity:** MAJOR.

**11. Dependencies:** CP40

### CP34 — Alahmadi DOI points to an unrelated article

**Group:** D. **Disposition:** ACTIVE WRONG CITATION IDENTITY.

**1. Issue ID:** CP34 (audit CR34).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/references.bib:20-31 (Alahmadi2013CyclicM2F2)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/02_literature.tex (citation of this key)`

**3. Relevant theorem / equation / proof:** Bibliographic key Alahmadi2013CyclicM2F2 and its section 2 citation; direct citation-identity defect, not a theorem counterexample.

**4. Defect explanation:** The manuscript's .008 DOI is not an alternate coding-paper DOI; it resolves to an unrelated control-systems paper.

**5. Independent-audit evidence / source-reading refinement:** CR34; saved L14a/L14b/L09 and bibliography_recheck_by_entry.csv.

**6. Required mathematical / editorial correction — future only:** After approval, change the successor bibliography to the supported coding-paper DOI .023 with an explicit change record; ensure regenerated bibliography and cited identity match. No original bibliography is altered now.

**7. New proof required?:** NO.

**8. Computational verification required — NOT RUN:** B08: exact key/author/title/journal/pages/DOI consistency and resolved-citation check after later authorized typesetting.

**9. Impact on quantum-code parameters:** None; attribution/traceability defect.

**10. Severity:** MAJOR.

**11. Dependencies:** CP40

### CP35 — Other bibliographic identities, dates and missing DOI metadata

**Group:** D. **Disposition:** ACTIVE METADATA CORRECTIONS plus already-correct values to preserve.

**1. Issue ID:** CP35 (audit CR35).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/references.bib:101-116 (GreferathSchmidt1999GrayIsometry); 118-184 (Fan/LiuPan/Cao/Ketkar)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/02_literature.tex; sections/09_comparison.tex:80-126 (related-work claims)`
- `phase0_audit/extracted/prior_project/01_LITERATURE/references.bib (ancillary Oggier/affine/placeholder records, not a manuscript edit target)`

**3. Relevant theorem / equation / proof:** GreferathSchmidt1999GrayIsometry / Fan / LiuPan / Cao / Ketkar records and attributed comparisons; ancillary Oggier/affine/placeholder identities. No automatic proof validation from metadata.

**4. Defect explanation:** Unsupported full names and stale/wrong broader-bibliography metadata remain. Fan volume is already correct in both BibTeX files and must not be 'corrected' there to match the erroneous report. Missing DOI does not make a paper nonexistent.

**5. Independent-audit evidence / source-reading refinement:** CR35; literature audit §3; saved L03-L07/L10/L13/L15/L17-L19; entry-by-entry CSV. A9b DOI must not be attached to the distinct A11 PDF.

**6. Required mathematical / editorial correction — future only:** Use the bounded verified metadata: Avanti Ketkar, verified S.E. Schmidt initials, Oggier-Sole-Belfiore 2012, correct journal/preprint years and confirmed DOI fields. Record unverified entries/identities explicitly and do not invent full names or venues.

**7. New proof required?:** NO mathematical proof; technical claims attributed to a paper still require source reading under CP36.

**8. Computational verification required — NOT RUN:** B08: reconcile all retained bibliography keys and duplicate themes; keep publisher/registry/search-only/inherited evidence levels distinct.

**9. Impact on quantum-code parameters:** None directly; may alter which novelty comparisons/claims are supportable.

**10. Severity:** MAJOR.

**11. Dependencies:** CP34

### CP36 — Nearest-neighbour, priority and new-bound claims

**Group:** D. **Disposition:** ACTIVE ATTRIBUTION/CLAIM-SCOPE REVIEW; external novelty remains unverified.

**1. Issue ID:** CP36 (audit CR36).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/02_literature.tex (all related-work comparisons)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/09_comparison.tex:80-126 (specific-and-proved novelty, no-commutative-analogue and two-new-bounds claims)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:86-102 (prop:newsbound)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/01_introduction.tex; sections/10_conclusion.tex; main.tex:147-166 (contribution summaries)`

**3. Relevant theorem / equation / proof:** Specific-and-proved novelty list; prop:newsbound / new-bound independence claim; contribution summaries in abstract/introduction/conclusion and related-work comparison.

**4. Defect explanation:** The 37-entry inventory is not an exhaustive verified priority search; Q1/LOW-risk/firstness claims are unsupported. QIP2026 matrix-ring/Gray/CSS predecessor and noncommutative anti-automorphism foundations must be discussed. A true elementary bound is not thereby a novel contribution, and commutativity alone does not establish that no principality question can be asked.

**5. Independent-audit evidence / source-reading refinement:** CR36; Q15/Q23; literature audit §§1-5 and saved L01-L22; 18 repository entries not freshly reverified; all 13 manuscript entries only boundedly metadata/endpoint checked.

**6. Required mathematical / editorial correction — future only:** After mathematical closure, rebuild the contribution-to-nearest-theorem comparison with exact ring/module/form/code/Gray/quantum hypotheses; cite the authentic QIP and foundations. Remove priority/ranking guarantees and qualify or withdraw unsupported newness/nonimplication claims. No new novelty paragraph is drafted now.

**7. New proof required?:** Not for metadata; YES for any retained mathematical nonimplication/new-theorem assertion lacking a valid existing argument. Priority needs literature evidence, not a proof fabricated by this plan.

**8. Computational verification required — NOT RUN:** B08 plus CP32 comparability evidence; no finite code test proves novelty or journal rank.

**9. Impact on quantum-code parameters:** No automatic tuple changes. The defensible contribution may narrow after proof/benchmark repairs; no replacement record claim is presumed.

**10. Severity:** MAJOR.

**11. Dependencies:** CP10, CP12, CP24, CP25, CP28, CP31, CP32, CP34, CP35

### CP37 — P1 'first q8 EA' proposal overlaps existing records

**Group:** D. **Disposition:** ANCILLARY PROPOSAL QUARANTINE / NOT A NEW MANUSCRIPT RESULT.

**1. Issue ID:** CP37 (audit CR37).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/01_introduction.tex and sections/09_comparison.tex:80-126 (guard against importing proposal claims)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/10_conclusion.tex (future-work boundary)`

**3. Relevant theorem / equation / proof:** Ancillary first-q8-EA proposal; manuscript/future-work boundary only. No existing MS03 theorem is being replaced by new P1 research.

**4. Defect explanation:** The frozen research-gap/decision proposal says a q8 EA layer is absent, while four supplied q8 EA records are already independently checked. This is not an error requiring a new construction inside MS03.

**5. Independent-audit evidence / source-reading refinement:** CR37; Q21; literature audit §6 P1; independent 28-code summary.

**6. Required mathematical / editorial correction — future only:** Exclude the first-q8-EA claim and do not rebrand existing examples. Any genuinely twist-dependent bridge/family requires a separate future proposal/authorization, not this correction pass.

**7. New proof required?:** NO for exclusion. New P1 theory is NOT authorized.

**8. Computational verification required — NOT RUN:** B06: inventory the four existing q8 EA records and their already-recorded certificates only; no new parameter search.

**9. Impact on quantum-code parameters:** Preserve the four valid existing examples; changes originality claims, not their certified tuples.

**10. Severity:** MAJOR.

**11. Dependencies:** CP26, CP36

### CP38 — P2 size-three threshold/index/complexity claims

**Group:** D. **Disposition:** ANCILLARY PROPOSAL QUARANTINE.

**1. Issue ID:** CP38 (audit CR38).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:9-36 (matrix-size-2 standing scope)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/06_gray.tex:152-165 (prop:qc)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/10_conclusion.tex (future-work boundary)`

**3. Relevant theorem / equation / proof:** Standing matrix-size-two scope and prop:qc consistency; ancillary P2 threshold/index/complexity assertions, not a defect in the current size-two formula.

**4. Defect explanation:** The separate size-three proposal misstates the nonprincipal threshold, Gray index and example ring-size exponent. These do not make the correct size-two manuscript formulas wrong.

**5. Independent-audit evidence / source-reading refinement:** CR38; F08/G07; literature audit §6 P2: require mu>3, Gray index 9t, exponent p^36 at field degree2,t2,size3.

**6. Required mathematical / editorial correction — future only:** Keep current manuscript scope at size2. If mentioning the proposal, state it as unimplemented/unproved and correct the inherited numerical scope in a separate clarification. Do not extend the manuscript or run size-three research.

**7. New proof required?:** NO within this correction plan; structural P2 theory would be new research and separately gated.

**8. Computational verification required — NOT RUN:** No size-three run. B08 static consistency review of any retained future-work sentence only.

**9. Impact on quantum-code parameters:** None for current N=4tn campaign; no new size-three tuples may be claimed.

**10. Severity:** MAJOR.

**11. Dependencies:** CP07, CP36

### CP39 — P3 Ore quotient and compatibility are not established

**Group:** D. **Disposition:** ANCILLARY PROPOSAL QUARANTINE.

**1. Issue ID:** CP39 (audit CR39).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex:9-36 (central X and R_n definition)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/10_conclusion.tex (future-work boundary)`

**3. Relevant theorem / equation / proof:** Central-X / R_n definition and future-work boundary; ancillary unproved P3 Ore-quotient/compatibility claim, not a current skew theorem.

**4. Defect explanation:** The proposed skew/Galois/matrix/hull/quantum program has not established a two-sided quotient or twist/duality compatibility; a bounded search is not proof of priority. MS03's central-variable ring is a different, already defined scope.

**5. Independent-audit evidence / source-reading refinement:** CR39; Q22; literature audit §6 P3.

**6. Required mathematical / editorial correction — future only:** Retain central X in the existing manuscript and quarantine all unproved skew claims. A future proposal would first have to establish a two-sided Ore quotient and compatibility, but no such proof or implementation is part of this correction authorization request.

**7. New proof required?:** NO for exclusion; YES only as separately approved new P3 research.

**8. Computational verification required — NOT RUN:** No skew code generation or experiments. B08 verifies no unapproved skew theorem has been inserted into the current claim set.

**9. Impact on quantum-code parameters:** None for the current records; no new skew-derived parameters or firstness claims.

**10. Severity:** MAJOR.

**11. Dependencies:** CP04, CP36

### CP40 — Authoritative staging baseline, submission status and author-only gates

**Group:** C. **Disposition:** OPEN CRITICAL AUTHOR/PROVENANCE BLOCKER 8; current status AUTHOR CONFIRMATION REQUIRED.

**1. Issue ID:** CP40 (audit CR40).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:147-167 (abstract); 193-290 (declarations, data availability, AI statement)`
- `phase0_audit/extracted/prior_project/PAPER/main.tex (historical canonical source — not the selected current staging baseline)`

**3. Relevant theorem / equation / proof:** Author/data/AI/declaration blocks and exact manuscript provenance; author-only status decisions, not a mathematical theorem.

**4. Defect explanation:** An immediate-submission verdict cannot follow from preparation folders. Phase23 explicitly designates FFA_FINAL_SUBMISSION_V2 as the new authoritative staging copy, but its data statement is PROPOSED, its editorial email unsent, author declarations unfinished, and no actual current submission receipt/status is verified.

**5. Independent-audit evidence / source-reading refinement:** CR40; Q23; author brief §4; Phase23_DATA_AVAILABILITY_STATEMENT.md opening and §§B5-B8; Phase23_FFA_OPTION_C_COMPLIANCE.md Appendix E; MS03 inventory and source observation CP40.

**6. Required mathematical / editorial correction — future only:** Before any implementation, author confirms MS03 root+14-file source fingerprint as the working baseline and discloses actual submission status/version/receipt if any. Separately decide truthful AI/CRediT/acknowledgement/data/licence/editorial policy matters. Do not send emails, create releases/deposits, remove pending markers or submit by inference.

**7. New proof required?:** NO; author/documentary confirmation is required. Mathematical repairs remain separate gates.

**8. Computational verification required — NOT RUN:** B00 provenance/preservation and B08 source/build checks only after approval. No external submission-system access, account creation or GitHub writes.

**9. Impact on quantum-code parameters:** None directly; controls which source and parameter version any correction would actually apply to.

**10. Severity:** CRITICAL.

**11. Dependencies:** None; first author/provenance gate.

### CP41 — 86/88/87 file-count basis

**Group:** C. **Disposition:** ACTIVE COUNTING-BASIS CLARIFICATION.

**1. Issue ID:** CP41 (audit CR41).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex:237-272 (data-availability file count)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:11-32; 110-end (package layout and hash verification)`

**3. Relevant theorem / equation / proof:** Data-availability / appendix package-count and manifest statements; provenance counting bases, no mathematical theorem.

**4. Defect explanation:** Counts from different layout epochs and self-exclusion rules were mixed. Current 88 files, 86 nonmanifest and 87 publication-manifest entries are different counting bases; historical 86 footprint is different again.

**5. Independent-audit evidence / source-reading refinement:** CR41; independent package audit §2; source inventory and inherited-manifest checks.

**6. Required mathematical / editorial correction — future only:** Identify the exact referenced tree/layout and explicit exclusions in the successor text; preserve historical README/report counts with an append-only explanation rather than overwriting them.

**7. New proof required?:** NO.

**8. Computational verification required — NOT RUN:** B08: enumerate the precise future release tree and verify both manifest coverage and self-exclusions without changing the frozen data package.

**9. Impact on quantum-code parameters:** None; provenance/readability only.

**10. Severity:** MINOR.

**11. Dependencies:** CP40

### CP42 — Qualified reference closure, unavailable binaries and build provenance

**Group:** C. **Disposition:** ACTIVE PROVENANCE/BUILD SCOPE LIMIT; no TeX compilation authorized now.

**1. Issue ID:** CP42 (audit CR42).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:86-end (reproduction and limitations)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex (source-set identity); all input paths in the selected 14-file root`

**3. Relevant theorem / equation / proof:** All literal manuscript inputs, source/build and historical-reference closure; missing-container/partial-mirror qualifications, not universal proof closure.

**4. Defect explanation:** 1017 declared targets existing is not universal historical recovery. Missing ZIP/PDF containers, omitted/unresolved references, curated staged-input reuse and the damaged canonical PDF remain qualified. MS03's full recovered root and the curated audit delta root are not interchangeable build directories.

**5. Independent-audit evidence / source-reading refinement:** CR42; independent package audit §3; manuscript_versions.csv/file inventory; unavailable_manuscript_artifacts.csv and historical sidecar claims.

**6. Required mathematical / editorial correction — future only:** Name the complete MS03 source set, resolve actual retained input/citation/proof references, and disclose unavailable historical binaries. A future approved build may create a new PDF with its own digest but must not label it as a recovered old/submitted PDF.

**7. New proof required?:** NO as a packaging task; any unresolved proof dependency is referred to its mathematical action, never filled by an invented reference.

**8. Computational verification required — NOT RUN:** B08: literal inputs, labels, bibliography and source manifest; compilation/visual checks only after approval. Inherited hashes for missing archives remain unverified historical claims.

**9. Impact on quantum-code parameters:** None directly; inability to identify a row's actual source/certificate prevents a readiness claim for that row.

**10. Severity:** MAJOR.

**11. Dependencies:** CP40

### CP43 — Execution attribution and immutable audit history

**Group:** C. **Disposition:** ATTRIBUTION/PRESERVATION CONTROL.

**1. Issue ID:** CP43 (audit CR43).

**2. Exact manuscript filename / section:**

- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/appendix_reproducibility.tex:56-108 (source of numbers/reproduction)`
- `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/08_certification.tex:168-212 (methodology)`

**3. Relevant theorem / equation / proof:** Reproduction appendix and section 8 methodology execution attribution; audit self-disclosures A01–A04 remain historical checker/date issues, not manuscript counterexamples.

**4. Defect explanation:** Inherited logs, the old Phase0/package feasibility rerun, the independent review's three original-source reruns and its separate arithmetic checks are distinct evidence. A later rerun cannot be attributed to the original package builder or used to certify every historical phase.

**5. Independent-audit evidence / source-reading refinement:** CR43; independent package audit §4; Gray audit §1; recorded run summary. Audit self-disclosures A01-A04 are historical checker/date issues, not new manuscript counterexamples.

**6. Required mathematical / editorial correction — future only:** Maintain an execution/proof/record lineage table with exact commands, environments, dates, scope and digests. Preserve both original reports and independent review verbatim; add a successor correction note only if approved. Keep the disclosed snapshot-date discrepancy, not a silently changed baseline.

**7. New proof required?:** NO.

**8. Computational verification required — NOT RUN:** B06/B08: compare provenance and expected outputs, distinguish scientific equality from byte equality when dates/timing differ. Do not rerun research as part of making this plan.

**9. Impact on quantum-code parameters:** None directly; prevents overstating the evidence supporting retained tuples or general claims.

**10. Severity:** MINOR.

**11. Dependencies:** CP19, CP21, CP30

## 4. Closure evidence and what must not be changed

A future action may close only with a frozen input identity, an authorized successor diff or an explicit restriction/withdrawal, proof/citation review where required, the specified test records where applicable, and an independent reviewer sign-off. A plan, passing old log, or source hash alone never closes a proof defect.

The positive double dual, conditional size/reflexivity results, exact transported Gram form, valid earlier nonprincipal witness, reproduced 463 assertions and 28 recertified field records are **retained at their audited scope**. Do not alter valid tuples merely to fit an erroneous all-route identity. Do not claim that CP28 refutes the restricted Singleton inequality.

Audit self-disclosures **A01–A04** are not four more research defects or blockers. They concern the preserved snapshot date field, a corrected parser artifact, an extraneous first checker assertion and the resolved PDF-parser dependency. Keep the authoritative-v2 evidence and the historical artifacts together; no independent-review file is edited. They are addressed by CP43's lineage control, not by rewriting research proofs.

No issue card authorizes P1/P2/P3, a new code search, manuscript drafting now, old-report edits, publication, Git commit or push. All implementation decisions remain in [AUTHOR_APPROVAL_CHECKLIST.md](AUTHOR_APPROVAL_CHECKLIST.md).

**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**
