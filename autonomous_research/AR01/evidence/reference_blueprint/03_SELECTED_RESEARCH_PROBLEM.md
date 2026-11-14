# 03 — Recommended research problem

## RECOMMENDED ONLY — AUTHOR SELECTION PENDING

The requested filename is not a selection record. **No primary problem has been formally chosen or approved.** See NAD01, NAD03–NAD07 and NAD18 in the [decision register](09_AUTHOR_DECISION_REGISTER.md).

[Master](10_MASTER_NEW_RESEARCH_BLUEPRINT.md) · [Framework](04_MATHEMATICAL_FRAMEWORK.md) · [Theorem targets](05_THEOREM_ROADMAP.md)

## 1. Working title

**Generator Profiles of Galois Hulls of Principal Cyclic Codes over Matrix Rings**

This neutral title does not presume that generator growth exists. If a preservation theorem is eventually the main result, the title should reflect it; if nonprincipal hulls are structurally classified, the title may then say so. Neither stronger title is adopted now.

## 2. Motivation and difference from MS03

A principal right ideal of M₂(B) corresponds to a B-submodule W⊆B² with μ_B(W)≤2. Its hull is controlled by an intersection involving the Galois/reversal dual module. Over the non-chain repeated-root factors, being a submodule of a two-generated module does **not** alone control generator number. This motivates asking what the **special dual-pairing relation**, rather than arbitrary intersection, forces.

MS03 already supplies the framework, the intersection reduction, the threshold and nonprincipal hull existence for nonprincipal inputs. Repeating these is not the new paper. Its failed direct-sum proof also cannot be turned into a new contribution by repair. The proposed advance is an **explanatory classification/bound/criterion for the principal-input subclass**, with dependence on embedding data and twist made visible.

The original1,221-module audit is a finite anchor at (4,2,2), not a theorem for all q. Scalar repeated-root hulls, MT hull generators and Artinian generator invariants are occupied literature (NL02, NL03, NL10, NL11). The external gap remains X, not established novelty.

## 3. Primary objective

Determine which hull generator profiles can occur for principal cyclic right ideals over M₂(F_q[u]/u²), first in a **bounded repeated-root local family**, and identify structural conditions that decide whether the hull remains principal. Seek a theorem with an interpretable input invariant/normal form, not only an algorithm that computes an already known intersection.

Recommended scope order, pending author choice:

1. **Core A:** q=2^m, m≥2, t=2, n=2, all s modulo m; local B=F_q[u,X]/(u²,(X−1)²). The inherited q4 family is a regression reference; it is not a new census.
2. **Core B, only after a useful Core A theorem:** t=2 and one repeated-root factor of multiplicity e=p^a; a restricted family of two-generated embedded modules, not classification of every wild module. Odd-characteristic comparison may begin with p=3,e=3 if justified.
3. **Extension C, conditional:** several CRT factors and their Galois/reversal coupling, **only** if it produces a theorem beyond existing CRT/max-μ assembly.

Matrix rank stays2 initially. r=3 or all r is a later structural corollary/extension only if new content remains; parameter substitution is not the objective.

## 4. Research questions and evidence status

| ID | Precise question | Status now | Why it is differentiated |
|---|---|---|---|
| RQ1 | For μ_B(W)≤2, can μ_B(H_s(W)) exceed2, where H_s(W)=W(C∩C^(⊥s)) for C=I_W? | **U/RQ**, internal O-3.1b; external X | Restricts the input, unlike known nonprincipal hull examples |
| RQ2 | What module/embedding/pairing data determine the attainable pairs (μ(W), μ(H_s(W))) and local hull profiles? | **RQ; X** | Requires structural information beyond field dimension or generic GPM construction |
| RQ3 | Is principal-hull preservation forced in Core A for every field/twist, or is there a describable obstruction? | **RQ**, not a yes/no prediction | The old q4 census is insufficient for a universal field-parameter statement |
| RQ4 | Which layer/extension data distinguish equal-dimension/equal-μ inputs with different hull generator behavior? | **RQ**; no example promised | Prevents claiming a dimension-only formula without testing embedding dependence |
| RQ5 | If growth occurs, what is the sharp attainable generator bound in the retained class, and what realizes it? If not, what forces preservation? | **RQ** | Accepts a substantial negative/preservation theorem, not a forced positive example |
| RQ6 | How do coefficient Frobenius and reversal affect these conditions, including m∤2s? | **RQ** | Non-reflexivity is a variable to study, not a new DD theorem |
| RQ7 | Does a local classification survive or change under actual CRT coupling, rather than a naive product of independent hulls? | **RQ**, extension only | Must exceed the already known permuted-intersection and max-μ facts |
| RQ8 | Can the structural result support a certificate-producing method meaningfully better than ambient enumeration, with a proved bound on the stated input class? | **RQ**, conditional | A new wrapper around row reduction is not enough |
| RQ9 | Is there a proved, metric-qualified connection to an ordinary Euclidean/Hermitian/trace hull giving a useful quantum consequence? | **RQ**, optional | μ_B and transported h_s are not entanglement cost by definition |

The notation H_s(W) means **the Morita module of the actual global hull**, not an unproved standard dot-product hull on a conveniently chosen local basis.

## 5. Proposed conjecture — deliberately not an assumption

**PC1 — exploratory principal-hull preservation in Core A:** for q=2^m, m≥2, t=2, n=2, every principal cyclic right ideal C of M₂(F_q[u]/u²)[X]/(X²−1) has principal Hull_s(C), for every0≤s<m.

**Status: PROPOSED CONJECTURE, NOT ADOPTED OR PROVED.** Evidence is limited to the inherited q4 audit and the absence of a principal-input counterexample there. No new computation supports other q. This is a falsification target, not a premise of any theorem or an external novelty assertion. A single valid counterexample would reject PC1; a search without one would not prove it. The author may prefer question-only posture (NAD16; Arena recommends that posture until the gap check is complete).

No analogue for arbitrary t/e/r or physical quantum parameters is conjectured by this blueprint. Old H-3A.1/H-3A.2 remain historical unresolved claims, not freshly adopted premises.

## 6. What would count as a new paper-sized result?

At least one **core structural theorem** must survive both proof review and theorem-level predecessor comparison, together with a nonroutine consequence. Examples of acceptable outcomes, not promises:

- a parameter-uniform principal-hull preservation classification, with the precise hypotheses and a proof mechanism not already a one-line corollary of existing theory;
- a generator-growth obstruction/attainability theorem with an explicit structural family and sharp upper bound in the stated class;
- a complete generator-profile theorem for a meaningful restricted class of embedded two-generated modules, showing why layer/extension/form data matter, and a useful classification or certificate consequence.

**Insufficient alone:** a new q/t/n table, an isolated μ3 witness, a finite exhaustive q4 rerun, matrix-rank substitution, the standard Nakayama formula, the known Morita threshold, or fixing a manuscript proof. A positive or negative answer to RQ1 by a short known corollary may resolve an old question but still fail this paper's novelty/depth gate.

## 7. Expected contributions and examples — all prospective

1. A source-delimited structural theorem for the retained principal-input class.
2. A rigorous principality/growth criterion and sharpness/preservation result, if obtainable.
3. A transparent role for nilpotent layers, embedded generator relations and the twist, rather than dimension-only claims.
4. Explicit certificate-ready examples and counter-controls illustrating **proved** hypotheses. No new parameter tuple is filled in now.
5. Optionally, a justified algorithmic or quantum corollary; neither is required to rescue an otherwise weak algebraic result.

Planned example tables separate input μ, hull μ, field dimensions, Loewy/extension data, generator matrices and proof status. They are specified in [06](06_COMPUTATIONAL_METHODOLOGY.md), not populated with invented outcomes.

## 8. Major risks, alternatives and stopping rules

| Risk | Diagnostic | Bounded alternative | Stop/re-scope trigger |
|---|---|---|---|
| Exact result already exists | Primary theorem comparison with NL03/NL10/NL11 and cited predecessors | Identify a different nonroutine structural question and return to author | No substantive distinction after comparison |
| Core A is too small/routine | Answer follows immediately from standard normal form | Consider approved restricted e>2 class | Do not inflate q/r merely to make another table |
| Wild representation complexity | Proposed normal form requires all arbitrary modules | Restrict to a clearly defined two-generated embedded class | No meaningful tractable theorem class |
| Input invariants insufficient | Same proposed invariant cannot decide behavior | Retain additional pairing/extension/orientation data | Do not assert completeness of a coarse profile |
| PC1 is false | Exact witness verified independently | Seek a growth criterion and sharp family | An isolated computational counterexample is not a Q1 promise |
| PC1 is true but shallow | General theorem already forces it | Report as an old-question resolution; reassess paper aim | Do not repackage standard theory as principal novelty |
| Quantum bridge fails or is old | No metric/orthogonal proof or only old EA formulas | Publish algebra-only if strong enough | Drop quantum claims, not validity conditions |
| Old source/submission conflicts | Author supplies a different baseline/status | Re-inventory and delimit overlap before new project | No implicit reuse or correction of an unknown submitted version |

## 9. What this document does not do

It does not prove PC1 or a new theorem, create examples, implement algorithms, edit MS03, select a journal, certify a quartile, establish priority or approve Phase1. The recommended research problem remains contingent on NAD01/NAD18 and the first-phase novelty gate.

**BLUEPRINT DEVELOPMENT ONLY — WAIT FOR EXPLICIT AUTHOR APPROVAL.**
