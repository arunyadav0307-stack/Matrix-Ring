# Author final scope decision — proposed freeze, awaiting author choice

**BLUEPRINT REVIEW ONLY. This is a decision form, not a signed scope freeze or Phase 1 authorization.**

All ten numbered blueprint documents and all 18 NAD entries were reviewed against the 43-family constraint crosswalk. **Every author choice remains PENDING / NOT RECORDED.** Arena's recommendations below do not approve themselves, adopt definitions, establish novelty or close audit findings.

## Executive summary — minimum response before Phase 1

The recommended **review-only scope freeze** needs four explicit confirmations, covering six NAD entries:

1. **Direction — NAD01:** P2-S, P1, P3, or defer.
2. **Review scope — NAD03–NAD05:** proposed Core A, matrix size 2, all twists, using the provisional conventions in §§3–4; or specify changes.
3. **Prior-source treatment — NAD02:** confirm the exact source and factual editorial status; identify a later version; or explicitly leave them unknown and use MS03 as a **provisional staging reference only**.
4. **Authority — NAD18:** approve **Phase 1 only: primary-literature, source-authority and scope review**, or request revisions/hold.

**Arena recommends:** P2-S; Core A/all twists; factual source confirmation where available and an explicit uncertainty flag otherwise; bounded Phase 1-only approval **if the author agrees**. No such approval is recorded here. One clear author response can cover all four confirmations; eighteen separate approvals are unnecessary.

The old-paper freeze and no-Git/publication boundary already bind this task. Remaining decisions may be deferred as specified in §10, not silently decided. Unknown source facts need not prevent limited source/literature review, but they block a definitive old/new overlap or priority conclusion. Blank fields, agreement with a title, or receipt of this file are not authorization.

## 1. Recommended research title

**Generator Profiles of Galois Hulls of Principal Cyclic Codes over Matrix Rings**

This working title assumes neither generator growth nor a quantum application. A narrower eventual title must follow the surviving theorem. **Author's final title: PENDING.**

## 2. Primary problem and reassessment of P2-S

For **principal** matrix-ring cyclic inputs, seek a structural description of hull generator profiles: when does the hull remain principal, and, if it does not, what pairing/embedding mechanism permits a nonprincipal hull? An internal open question, MS03 O-3.1b, motivates the proposal; **it is not an external novelty certificate**.

| Direction | Existing advisory score /100 | Reassessment from the completed blueprint |
|---|---:|---|
| **P2-S** | **73.6** | Best bounded starting point: principal-input structure, rather than known nonprincipal-input witnesses. Main risk: scalar hull classification, MT/intersection generators or Artinian theory may already imply the answer routinely. |
| P3 | 65.6 | Reserve alternative. Requires a genuinely new, well-defined Ore quotient/adjunction compatibility result; skew + Galois and matrix/form transport are occupied ingredients. |
| P1 | 50.8 | Reserve alternative. Needs a new trace-compatible physical mechanism, not the inherited double-twist identity, R1/EA routes or another q8 example. |

These are the original **subjective planning scores**, not fresh measurements or probabilities. No new literature search or rescoring was performed for this review. P2-S falls to **60.8** under the blueprint's novelty/headroom sensitivity downgrade, below P3. Thus its recommendation is conditional: if Phase 1 finds only known/routine content, **stop or return a revised proposal to the author**; do not automatically switch direction.

**Arena recommendation:** P2-S for the gap-review gate only. **Author's final direction: PENDING.** See [comparison](01_CANDIDATE_DIRECTION_COMPARISON.md) and [novelty positioning](02_LITERATURE_AND_NOVELTY_POSITIONING.md).

## 3. Exact proposed mathematical scope — review target, not adopted theory

| Item | Proposed Core A boundary |
|---|---|
| Parameters | p=2; q=2^m with m≥2; matrix size r=2; nilpotency t=2; cyclic length n=2; 0≤s<m |
| Alphabet and ambient ring | A=F_q[u]/(u²); R=M₂(A); X central; B=A[X]/(X²−1); S=R[X]/(X²−1)≅M₂(B) |
| Inputs | Principal **right** ideals C=gS, including the zero case under μ(0)=0; no freeness or full-rank assumption on g |
| Morita convention | Embedded **column** module W=im_B(g)⊆B², with μ_B(W)≤2; r=2 denotes matrix size, not rank(g) |
| Twist and dual | σ_s acts on coefficients by a↦a^(2^s), fixing u,X; θ_s=σ_s∘transpose; first-slot form B_s(x,y)=Σ_i θ_s(x_i)y_i on R²; C^(⊥s)={y:B_s(x,y)=0 for all x∈C} |
| Hull and generator question | Hull_s(C)=C∩C^(⊥s); H_s(W) denotes its actual Morita module. The principal-input question asks whether μ_B(H_s(W)) can exceed 2, not merely whether μ increases. |
| Proposed local model | T=F_q[u,w]/(u²,w²), w=X−1, as in blueprint 04; its duality must be **induced from the global form**, not replaced by a convenient dot product on T². |

**Not in the initial research scope:** r≥3, arbitrary t/e, odd-characteristic extension, multiple CRT factors, full wild-module classification, skew variables, quantum constructions or scientific computation. Related literature may of course be compared without adopting its broader research scope.

Core B (a specified two-generated class with e=p^a>2) and Core C (nonroutine coupled-CRT synthesis) remain **separate future scope decisions**, not fallback permissions. The q4 census is inherited finite evidence; it does not establish a theorem for every m,s. See [problem](03_SELECTED_RESEARCH_PROBLEM.md) and [framework](04_MATHEMATICAL_FRAMEWORK.md).

## 4. Ring and module assumptions requiring confirmation

Approval of the review target should explicitly address:

- **Side/slot:** right cyclic ideals, column Morita convention and the stated first-slot θ_s dual. A different side or slot needs a translated source comparison, not a cosmetic substitution.
- **Automorphisms:** coefficient Frobenius only, with u,X fixed; no moving-u automorphisms or Ore relation are included.
- **Non-reflexivity:** all twists are questions to review, not assumed involutions. The inherited primary convention gives DD=+σ_(2s)(C); universal reflexivity and codewise invariance are distinct.
- **Scalar level:** b_s is matrix trace followed by coefficient of u, valued in F_q, not the absolute F₂ trace. Ring/scalar orthogonal equality needs its valid module/ideal-catching hypotheses.
- **Embedding/equivalence:** no freeness assumption; no identification of μ with dimension or socle type; no arbitrary ambient GL change treated as a hull-preserving isometry.

The **complete meaning of “generator profile”, sufficient invariants, allowed normal-form equivalences, exact local functional and coefficient-field/coordinate maps remain unsettled**. Layer dimensions, generator relations and pairing/embedding data are candidate descriptors, not an approved complete invariant. Explicit field encodings are deferred under NAD14.

This is a proposed comparison contract. Author agreement to review it does **not** certify inherited proofs, finalize those outstanding definitions, or authorize their development. Final applicability/local-form specifications belong to a separately approved Phase 2.

## 5. Proposed generator-profile questions

1. **Preservation versus nonprincipality (RQ1/RQ3):** within Core A, can μ_B(W)≤2 coexist with μ_B(H_s(W))>2, or is preservation forced?
2. **Structural sufficiency (RQ2/RQ4):** which generator relations, nilpotent layers and embedding/form data actually determine μ and the retained hull profile? Coarse dimensions are not assumed sufficient.
3. **Sharp range (RQ5):** what bounds, attainable profiles or preservation classification hold in the retained class? No positive-growth family is promised.
4. **Twist dependence (RQ6):** what changes with s, including m∤2s, without rebranding the inherited DD identity as new?
5. **Conditional consequences (RQ7/RQ8):** only after renewed approval, does a result support nonroutine CRT synthesis or a certificate-producing structural algorithm?

**Arena recommends question-only posture.** PC1 remains an unadopted, unproved exploratory conjecture; old H-3A.1/H-3A.2 are not premises. Formal conjecture adoption is NAD16, not implied by Phase 1 review.

## 6. Expected theorem-level contributions — targets, not results

The intended core is **NT03–NT05**: a nonroutine structural profile theorem, a principal-input criterion/preservation-or-growth classification, and a meaningful sharpness or attainable-spectrum consequence. NT06 twist/embedding dependence is conditional; NT07–NT08 extensions/algorithms need further scope and execution approval.

**Paper-depth gate:** at least one substantial structural main theorem plus a meaningful proved consequence/classification must survive independent proof and predecessor review. A preservation theorem is acceptable if substantial; a known/routine answer or isolated counterexample may resolve a question without supporting the intended paper.

NT01–NT02 are source-validity/local-form infrastructure, normally not novelty. Standard Morita packing, Nakayama, CRT, a generic nullspace/GPM computation, a parameter table or repaired old proof is insufficient alone. **No theorem work is authorized here or by a Phase 1-only approval.** See [roadmap](05_THEOREM_ROADMAP.md).

## 7. Explicit exclusions from MS03 and the inherited audit

Do not present the existing matrix/Galois/Gray/quantum chain, DD formula, principality threshold, chain/non-chain boundary, generic hull intersection, valid nonprincipal-input witnesses or existing quantum records as this project's new contributions. In particular:

- Do not repair/relabel the failed generic μ3 family; the audited family has μ2. Separate valid witnesses do not repair its proof.
- Do not confuse a nonprincipal **dual** of a principal input with a nonprincipal **hull** of that input.
- No manuscript editing/building, old-script repair, rerun, data replacement, benchmark installation or correction authorization follows from this scope review.
- No “first q8 EA”, “first matrix-ring quantum”, generic new Singleton-bound or rank-substitution novelty claim.
- Retain E/U/PC/RQ/X and finite-evidence distinctions; printed-proof validity, theorem truth, numerical certification and priority remain separate.

The old project stays **CONDITIONAL HOLD**. Its 20 author decisions and all 43 correction families remain open/unimplemented; this review cannot close them.

## 8. Literature verification requirements and Phase 1 exit

**Present status: external gap X — unverified.** A later authorized Phase 1 must compare exact primary statements, not infer absence from previews or failed searches:

- MS03/later author-identified source; foundational anti-isomorphism/Frobenius duality and relevant module algebra.
- NL01–NL02 serial/repeated-root theory; **NL03–NL04** MT/intersection generators; **NL10** scalar repeated-root hulls; **NL11** Artinian μ/type/duality and their decisive predecessors.
- NL05–NL06 for the P3 comparison; NL07–NL09 and inherited A8/Cao/C5/C6 if a skew/quantum expansion is later proposed.

For each core target NT03/NT04/NT05 record exact hypotheses, side/slot, input class, output invariant, theorem/version locator, access level and whether it is already a routine specialization. Preserve unresolved MT2025/2026 relationships, A5a author order, A11 metadata and preview-limited cells; do not invent resolutions.

**Exit:** at least 12 substantive source/theorem comparison rows covering the required groups; a direct comparison for each core target or an explicit blocked/X label; a source/overlap boundary; scope revision/stop recommendation; author confirmation of acceptable outcomes and the independent-review route before seeking Phase 2 approval. A row count alone is not sufficient. Unknown baseline facts or inaccessible load-bearing texts prevent the affected affirmative gap conclusion.

Phase 1 may end **GO-for-consideration / NARROW / BLOCKED / STOP**, followed by an author decision. It does not prove a new theorem, establish all-literature absence, certify Q1 status or start Phase 2 automatically. This review performed **no fresh primary-literature verification or Phase 1 execution**.

## 9. Optional quantum extension and approval gate

**Arena recommendation (NAD07):** algebra first; quantum conditional, or omit it. **Author's final quantum choice: PENDING.** It is not part of Phase 1 execution and is not required to rescue a weak algebraic result.

Later separate author authority and all [QG1–QG6](07_QUANTUM_CONSTRUCTION_STRATEGY.md) are required: a genuine structural consequence; the correct form/field bridge; metric preservation or physical-coordinate distance recertification; trace isotropy and phase/scalar-free lift or valid Bob completion; exact named-object certification; and incremental novelty beyond standard EA/CSS formulas.

μ_B(H_s), transported h_s, ordinary h_E and a trace commutator radical are **not interchangeable**. SO/DC/EA/R1 use different inputs, orthogonals and logical-error sets. Match physical alphabets/resources and exact-versus-bound distances. Failure of the bridge means **omit/defer**, not assume Gray compatibility or discard an audit condition.

## 10. Author decisions and proposed freeze record

### A. Essential entry decisions — six NAD entries, four response blocks

**Every “Author choice” field below is PENDING.** Option letters retain their meanings in [register 09](09_AUTHOR_DECISION_REGISTER.md).

**NAD01 — Direction.** A: P2-S → bounded principal-input structural review, novelty still open. B: P1 → new physical-mechanism comparison needed. C: P3 → new quotient/adjunction contract needed. D: defer → no Phase 1.

**Arena:** A, because the internal question is sharper and more manageable, not because literature absence is known. **Author choice: PENDING.** Selecting B/C requires a revised review scope before execution; the P2-S assumptions do not carry over automatically.

**NAD02 — Prior source/status.** A: confirm MS03's exact identity **and actual editorial facts** → meaningful baseline. B: identify a later version → re-inventory and reassess overlap. C: explicitly unknown → MS03 staging reference only; definitive overlap/submission/priority claims blocked.

**Arena:** factual confirmation; C if facts are unavailable, rather than invent them. Baseline identity affects whether a proposed contribution already exists internally. **Author choice/facts: PENDING.** Preparation folders are not submission evidence.

**NAD03 — Matrix size.** A: r=2 → focused principal-input class. B: r=3 → larger scope; nonprincipality requires μ>3, not μ3, and rank substitution is insufficient novelty. C: all r → larger classification burden and packing-threshold overlap risk.

**Arena:** A, because the structural question, not matrix enlargement, should supply content. **Author choice: PENDING.**

**NAD04 — Initial family.** A: Core A in §3 → precise small starting class, possibly routine. B: specified two-generated t=2,e>2 class → richer but requires named restrictions/transport. C: arbitrary t,e/modules → full-wild complexity and poor initial feasibility.

**Arena:** A; B only after an explicit revised scope, not automatic escalation if A is shallow. **Author choice: PENDING.**

**NAD05 — Twists.** A: all s → review non-reflexive as well as reflexive cases. B: m|2s only → simpler symmetry, weaker Galois scope. C: s=0 only → bilinear control, not an all-twist contribution.

**Arena:** A as a question range; exact side/form hypotheses must survive review. **Author choice: PENDING.**

**NAD18 — Phase authority.** A: bounded Phase 1-only review → source/gap/scope report, then stop. B: blueprint revisions → planning only. C: hold/stop → no research execution.

**Arena:** A only if the author explicitly accepts the selected review target and safeguards. The unresolved gap is why review must precede proof/code. **Author choice: PENDING.** No proof, research implementation/experiment, manuscript edit/build, old correction, Git write, release, deposit, editorial contact or submission is included.

### B. Other twelve decisions — retained, not obstacles manufactured at entry

The full alternatives/justifications in register 09 remain controlling. Below are their timing and consequences for this proposed freeze. **All final author choices remain PENDING.**

| NAD / timing | Alternatives and consequences | Arena recommendation / rationale | Author choice |
|---|---|---|---|
| **NAD06 — before Phase 1 exit / theory scope** | A outcome-neutral → preservation or growth; B growth subquestion only → negative outcome may end project; C defer → no theory programme. | A; truth cannot be chosen, and a routine answer triggers re-scope/stop. | PENDING |
| **NAD07 — optional track** | A conditional quantum → bridge gates; B algebra-only → no physical claims; C quantum-led → revised plan. | A conditionally; B if no useful bridge. μ is not entanglement cost. | PENDING |
| **NAD08 — binding boundary now** | A freeze old work; B request separate correction task; C seek source-backed clarification. B/C do not authorize corrections here. | A; old proof repair is not new research. Current preservation instruction already binds regardless of a future vote. | PENDING |
| **NAD09 — before a positive gap verdict** | A primary texts → exact comparison; B previews only → dependent claims stay X; C defer inaccessible dependencies → blocked verdict. | A with C where necessary; access/provider choices need not all be settled before source review starts. | PENDING |
| **NAD10 — before any pilot** | A bounded proposed pilot; B no science computation; C custom cases/cap → new preflight/approval. | No computation in Phase 1; consider A only later. The old proposed budget is not permission. | PENDING |
| **NAD11 — route by Phase 1 exit; reviewers before later audit** | A independent proof/certificate review; B self-review only → lower assurance, not independent validation; C defer publication. | A, C if unavailable; shared code agreement is insufficient. No verifier implementation now. | PENDING |
| **NAD12 — journal selection deferred** | A provisional DCC; B conditional FFA; C defer final selection. Neither scope nor metrics certify Q1. | Keep DCC only as a scope lead; defer final choice until results/metric verification. | PENDING |
| **NAD13 — before data generation/release as applicable** | A immutable certificates/approved storage and licence; B private initially → disclose limits; C defer → no deposit/licence/public claim. | Plan A later; defer release now. Provenance and access/licence are distinct. | PENDING |
| **NAD14 — before coordinates/implementation** | A preserve inherited encodings; B checked isomorphisms → recertification duties; C defer implementation. | A for reused matrices; no numeric encoding finalized now. Isomorphic fields need not share integer labels. | PENDING |
| **NAD15 — overlap boundary in Phase 1; declarations before drafting/publication** | A accurate own-work disclosure; B wait for facts; C revise scope → remove duplication, not hide it. | A with B for unknown facts; final authorship/declarations need not be invented to start literature review. | PENDING |
| **NAD16 — before formal conjecture adoption** | A question-only; B retain exploratory PC1 → still unproved; C defer formulation until approved pilot. | A; absence of a q4 counterexample is not a universal proof. No conjecture is assumed while undecided. | PENDING |
| **NAD17 — binding boundary now** | A preserve/no Git/publication action; B later bounded Git request; C later release/editorial request. B/C need separate authority. | A now; no change to old seals or publication state. | PENDING |

**Entry versus exit:** source-access, negative-outcome and review-route decisions need resolution or explicit blocked dispositions at the Phase 1 exit gate; they do not require selecting computational tools, reviewers, journals or a formal conjecture before a strictly bounded literature/source review. Deferral never waives validity, disclosure or permission requirements.

### C. Consistency check — all 43 consolidated constraints retained

The [43-family crosswalk](evidence/AUDIT_CONSTRAINT_CROSSWALK.csv) was checked against the consolidated source records: identities, severities and open/unimplemented dispositions agree. The table below covers every MC family once. **No scope-level conflict was identified in the recommended review-only package; no mathematical closure is claimed.** All eight critical families—MC10, MC23, MC24, MC25, MC27, MC29, MC32, MC40—remain unresolved.

| Families | Safeguard carried into this proposed freeze |
|---|---|
| MC01–MC06, MC12 | Right action/slot, positive DD and exact scalar/ideal-catching hypotheses; no invalid failure example, unestablished alternative pairing, blanket reflexivity or Hom shortcut. |
| MC07–MC10 | Base/cyclic rings and cyclic/principal distinctions; inherited principality boundary is not new; generation is not freeness; failed μ3 family is not imported. |
| MC11, MC18–MC21, MC30–MC31 | Correct Morita/image representation, non-tautological diagnostics, literal finite/sample/method scopes, actual field labels and named-object certificates; no campaign rerun or certificate transfer. These remain later computational gates. |
| MC13–MC17 | Bilinear/Hermitian/Galois form and characteristic distinctions, actual GF9 transformation, code-specific CSS versus ambient obstruction, and F_q versus absolute-trace codomains. |
| MC22–MC29 | Quantum phase/lift/isotropy, Bob completion, actual trace/F_q orthogonal, h_E, route-correct relative sets/coset metrics and bookkeeping. Quantum deferral **does not retire** these constraints; 742 metadata failures are not 742 false distances. |
| MC32–MC33 | Physical-alphabet/resource/header matching; no global table-absence claim from a missing endpoint. No benchmark claim or reconstruction now. |
| MC34–MC36 | Correct source identities and unresolved metadata; exact predecessor/priority comparisons, including A8; no new-bound/firstness/Q1 guarantee. |
| MC37–MC39 | No first-q8 P1, parameter-only P2 or ingredient-only P3; matrix thresholds/index/cost and Ore compatibility remain correct. |
| MC40, MC42 | Staging identity is not submitted/current authority; retain author-only gates, unavailable-PDF/reference-closure limits and separate drafting approval. |
| MC41, MC43 | Preserve counting bases, execution-attribution/date discrepancies, source bytes and completed seals; no retrospective execution claim or gratuitous rerun. |

All 43 remain **OPEN / AUTHOR CHOICE AND REVIEW REQUIRED; NOT AUTHORIZED / NOT IMPLEMENTED** (8 critical, 29 major, 6 minor). The linked 16 RF observations, 30 conflicts and old 20 author choices are not removed or resolved. Counts are issue/evidence classifications, not counts of false theorems. Changed alternatives must be rechecked against these constraints before use.

### D. Author response record — unfilled

| Minimum response block | Author's final response |
|---|---|
| Direction (NAD01) | **PENDING — NOT RECORDED** |
| Review scope, assumptions/changes (NAD03–NAD05; §§3–4) | **PENDING — NOT RECORDED** |
| Exact prior source/editorial facts, or explicit unknown treatment (NAD02) | **PENDING — NOT RECORDED** |
| Phase 1-only approval / revisions / hold (NAD18) | **PENDING — NOT RECORDED** |

A future approval should state that **all 43 constraints and the no-proof/no-science/no-manuscript/no-Git/publication boundary remain in force**, with no automatic next phase. Other NAD choices stay pending unless expressly answered. Disputed facts or a changed direction/scope must be stated, not inferred.

---

**Review basis:** blueprint [01](01_CANDIDATE_DIRECTION_COMPARISON.md), [02](02_LITERATURE_AND_NOVELTY_POSITIONING.md), [03](03_SELECTED_RESEARCH_PROBLEM.md), [04](04_MATHEMATICAL_FRAMEWORK.md), [05](05_THEOREM_ROADMAP.md), [06](06_COMPUTATIONAL_METHODOLOGY.md), [07](07_QUANTUM_CONSTRUCTION_STRATEGY.md), [08](08_PHASE_WISE_EXECUTION_PLAN.md), [09](09_AUTHOR_DECISION_REGISTER.md), [10](10_MASTER_NEW_RESEARCH_BLUEPRINT.md), the [18-decision index](evidence/AUTHOR_DECISIONS.json) and the complete constraint crosswalk. This is a scope/decision review, not a new proof or independent technical re-audit.

**Preservation:** this new addendum is outside the previously sealed ZIP and its 109-file member set. The ZIP, checksum, original ten documents, decision/evidence registers and `SHA256SUMS.txt` are **not rewritten or resealed**. The old manifest does not purport to hash this later addendum. Frozen ZIP SHA-256: `23dcc025177ddbf917abbd00c0d381a2e70d15af56eeb53b11c31fa098e6b0b6`.

**FINAL STATUS: BLUEPRINT REVIEW ONLY. NO PHASE 1 EXECUTION. WAIT FOR THE AUTHOR'S EXPLICIT DECISION.**
