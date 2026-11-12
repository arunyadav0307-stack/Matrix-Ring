# Methodology and feasibility audit

## Overall assessment

The blueprint identifies reasonable work categories—structure, cardinality, duality, a Gray map, and a later parameter study—but the dependency order is unsound. The proposed computations assume a commutative local component model that is not the specified matrix ring. Consequently, the search pipeline cannot currently validate its algebraic inputs. This document assesses the plan only; no research execution or parameter/code search was performed.

## Dependency audit

### A. Factorization and component decomposition

The blueprint factors \(x^n-\lambda\) over \(\mathbb F_{16}\), invokes Hensel lifting, and writes a CRT sum of commutative rings \(K_i[u,v]/(u^k,v^4)\). This requires the correct coefficient ring, a valid central polynomial relation, and the appropriate factorization/lifting theorem. The actual \(M_4(A_k)\) has radical quotient \(M_4(\mathbb F_2)\), not \(\mathbb F_{16}\). A module decomposition may be possible in a corrected framework, but the displayed commutative CRT argument is not established.

**Feasibility gate:** stop until the ring model, side conventions, and decomposition have been fixed and proved or explicitly restricted to a valid subproblem.

### B. Ideal classification and cardinality

Monomial ideals in the proposed commutative truncated polynomial ring are finite and countable by monomial basis elements. This is a feasible restricted family **if** that ring is genuinely the component algebra. It cannot be advertised as classification of all constacyclic codes or used to prove a general necessary-and-sufficient condition. A Gröbner-basis plan would need a specified coefficient field, monomial order, quotient ideal, reduction rules, and a proof that the computed normal forms cover every desired component. No such implementation was attempted.

### C. Duality and component pairing

The component map, conjugate reciprocal, annihilator direction, and root pairing depend on the valid algebra and inner product. A single field-level rule is not enough for a noncommutative right module. The blueprint needs to define left/right annihilators and show that the chosen dual operation preserves or permutes the actual components. The dual-containing test must be proved before it can drive enumeration.

### D. Gray map and metric

The plan correctly recognizes that map definitions must be read before reuse. It nevertheless treats four distinct properties as if they were a single “Gray map” result:

- bijectivity/cardinality;
- additivity and \(\mathbb F_{16}\)-linearity;
- Hamming-distance preservation for the chosen ring weight;
- preservation of the exact dual/orthogonality relation required by the quantum construction.

Each needs a separate statement and proof. The quasi-twisted index also requires an intertwining calculation for the shift. The 2026 \(M_3\) quantum paper uses a special inner product and a separate Gray map precisely because its earlier map does not transfer the required dual.

### E. Quantum parameters and distance

If the field image is a valid \([N,K]_{16}\) code and is Hermitian dual-containing, the standard construction gives quantum dimension \(2K-N\). The quantum distance is not automatically the exact classical minimum distance: it is determined by nontrivial logical cosets and is at least the classical minimum distance in the usual setup. The blueprint should report exact distance only when established; otherwise report a certified lower bound and use consistent notation. The Singleton defect formula itself is standard.

### F. Proposed computation grid

The stated range \(k\in\{2,3,4\}\), odd \(n\le25\), gives \(N=4kn\le400\). This arithmetic is fine, but the grid overlaps direct prior work at \(k=2\) and \(k=3\), and its fifth-root multipliers cannot be treated as central. Distance computation can be expensive at those lengths; no runtime/equivalence/certification plan is supplied. A database comparison must include a timestamp, exact versus lower-bound status, quantum dimension convention, and a reproducible record of each generator and map.

**Constraint observed:** no codeword enumeration, Magma/GAP/Python run, quantum-parameter search, or code-table search was performed.

## Literature and publication feasibility

The blueprint's references and gap discussion omit direct \(k=3\) ISIT 2025 work, the corrected status of the 2022 \(k=2\) paper, and current 2026 quantum matrix-ring literature. Target journal names are not a substitute for a completed novelty audit. Q1 quartiles depend on database/category/year and were not certified here. In its present state, the blueprint is not ready for a Q1 submission or even research execution.

## Feasible order after explicit approval

1. Decide and state the actual algebraic object, its center/radical, and the \(\mathbb F_{16}\)-action.
2. Define left/right code modules and a constacyclic shift that is compatible with that choice; distinguish central and noncentral multipliers.
3. Choose a valid polynomial, skew-polynomial, or endomorphism framework. Do not assume ordinary quotient ideals for noncentral \(\lambda\).
4. Prove a restricted structural/cardinality result in that framework. Clearly label monomial or other subclasses as partial.
5. Define the dual form/involution and prove the dual operation for the same shift.
6. Define the exact field map and verify linearity, distance, shift, and dual transfer separately.
7. Apply the appropriate field quantum construction and define exact distance versus lower bound.
8. Re-run the literature review and novelty comparison before any code search.
9. Only then, if approved, conduct a reproducible search and compare exact parameters.

This is a recommendation roadmap, not execution or permission to modify the blueprint.
