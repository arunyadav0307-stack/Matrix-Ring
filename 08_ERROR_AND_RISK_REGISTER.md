# Error and risk register

Severity key: **P0 = foundational stop issue**; **P1 = major theorem/novelty blocker**; **P2 = execution, reproducibility, or publication risk**. “Required action” means a recommendation for a future researcher-approved revision, not work performed in this audit.

| ID | Severity | Blueprint claim / location | Finding and consequence | Required action after approval |
|---|---|---|---|---|
| E01 | P0 | pp. 1–2: \(R\) is local with residue \(\mathbb F_{16}\), maximal ideal \(\langle u,v\rangle\) | **False.** \(J(M_4(A_k))=M_4(uA_k)\); quotient is \(M_4(\mathbb F_2)\). Invalidates the proposed residue-field, Hensel, local-component, and unit arguments. | Re-state ring, center, radical, quotient, and exact cyclic-algebra/module presentation. |
| E02 | P0 | p. 1: unit iff nonzero \(\mathbb F_{16}\)-residue | **False for the matrix ring.** Unit status is determined by invertibility of the mod-\(u\) matrix in \(M_4(\mathbb F_2)\). | Replace with the correct matrix-ring criterion in the approved setup. |
| E03 | P0 | pp. 1–3, 5: order-5 \(\lambda\)'s used as scalar constamultipliers | The order-5 elements of an embedded \(\mathbb F_{16}\) are noncentral. The center's unit group has no order-5 element. Ordinary quotient/ideal machinery for noncentral \(\lambda\) is not defined. | Choose central multipliers or explicitly define a noncentral shift and a compatible skew/module framework. |
| E04 | P0 | pp. 2–3: commutative \(S_i=K_i[u,v]/(u^k,v^4)\) CRT components | No ring isomorphism from the stated matrix ring has been shown; the proposed local component ring has a field residue, unlike the matrix-ring quotient. | Rebuild component decomposition with correct side/action; do not infer from cardinality. |
| E05 | P0 | pp. 2–4: Hermitian conjugation on all of \(R\) | The field automorphism \(a\mapsto a^4\) is not a complete definition of an involution on the noncommutative matrix ring or of a Hermitian module form. | Specify and verify the full-ring involution/anti-involution, module side, form, and output field pairing. |
| E06 | P0 | p. 4: \(\Phi(C^{\perp_H})=\Phi(C)^{\perp_H}\) | No map/form compatibility proof. Without it, a ring dual-containing code need not give the field dual-containing code required by the quantum construction. | Define the map and prove linearity, metric, and exact dual-transfer properties separately. |
| E07 | P1 | pp. 2–3: Hensel/CRT classification and all-ideal theorem | The steps rely on the wrong residue/component ring and do not resolve noncentral multiplier quotient issues. | Re-derive only after the algebraic framework passes a stop gate; state scope if partial. |
| E08 | P1 | p. 2: monomial ideals followed by principal/all ideals | Monomial enumeration is a restricted subfamily. It cannot prove a classification or global necessary-and-sufficient criterion. The Gröbner-basis sentence is a plan, not a theorem. | Separate a proved subclass theorem from any all-ideal claim; give completeness proof. |
| E09 | P1 | p. 3: component map \(j\mapsto-4j\), annihilator criterion | Root parametrization, component action, left/right annihilator, and proof are missing. | Define component indices and annihilator side; prove the dual/component correspondence. |
| E10 | P1 | p. 4: \(\mathbb F_{16}\)-linearity, quasi-twisted index, distance preservation | A size-compatible or weight-isometric Gray map does not imply these properties. | State the scalar action and prove each map property, including shift intertwining. |
| E11 | P1 | pp. 1, 5: constacyclic gives new lengths inaccessible to cyclic codes | Unsupported. The formula \(N=4kn\) is independent of \(\lambda\); no comparison or example is supplied. | Rephrase as a testable hypothesis and compare actual valid parameter families. |
| E12 | P1 | pp. 1, 6: novelty gap stated from two introductions | Misses direct \(k=2\) corrected article and \(k=3\) ISIT 2025 paper; current \(M_3\) quantum and broad constacyclic work is adjacent prior art. | Complete a current, systematic literature review after the object is defined. |
| E13 | P1 | p. 4: exact quantum distance from \(d_H(\Phi(C))\) | Standard construction gives a distance controlled by nontrivial logical cosets; the classical distance is a lower bound, not automatically exact. | Define the quotient distance; report certified bounds unless exactness is proved. |
| E14 | P2 | pp. 5–6: Magma/GAP/Python and length range | Feasibility, exact-distance certification, runtime, and reproducibility are unspecified. Computation cannot validate the algebraic premises. | Defer all search until proofs/maps are validated; document tools and exactness. |
| E15 | P2 | p. 5: Grassl status “new/matches/dominated” | Comparison rules and snapshot date are not fixed; “new” requires exact parameter and code-table criteria. | Record database/version/date, exact versus lower-bound distances, and dominance rule. |
| E16 | P2 | p. 7: candidate Q1 venues | Quartile varies by source/category/year; journal list does not establish readiness. | Verify current category-specific rankings only after a valid theorem and novelty case exist. |
| E17 | P2 | 2022 source cited without correction | The publisher lists a correction with twelve equation/display corrections, including a Gray-map matrix. | Cite and use the corrected record; do not reuse the uncorrected display blindly. |

## Critical contradiction log

1. **Locality vs matrix quotient:** the blueprint says residue field \(\mathbb F_{16}\); the actual radical quotient is \(M_4(\mathbb F_2)\). These statements cannot both hold for the same ring.
2. **Central order-5 scalar vs matrix center:** fifth roots exist in a noncentral embedded field; central units of \(R\) have 2-power order. The proposed order-5 scalar family cannot be central in the stated ring.
3. **Commutative CRT components vs skew cyclic-algebra model:** the field-coordinate normal form does not make the ring commutative; the stated local component rings are not established.
4. **Ring dual vs field Hermitian dual:** a Gray map's cardinality/weight properties do not imply the exact orthogonality transfer required by the quantum theorem.
5. **“New lengths” vs fixed image length:** \(N=4kn\) does not depend on \(\lambda\).

## Overall risk rating

**Critical / no-go for current execution.** E01–E06 block the central mathematical chain. No computational search or blueprint modification was performed.
