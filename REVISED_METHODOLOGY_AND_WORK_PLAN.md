# Revised methodology and work plan

## 1. Scope

This plan is for a possible project over
\[
\mathcal R_k=\mathbb F_{16}[U,V]/\langle U^k,V^4\rangle,
\]
not over \(M_4(\mathbb F_2[u]/\langle u^k\rangle)\). It limits the initial structural theorem to componentwise monomial ideals. The all-ideal classification is a separate and potentially much harder problem. This file is a plan; no proof program, code search, or parameter catalogue has been executed.

## 2. Stage gates

### Gate 0 — researcher approval

Obtain approval for the change of alphabet and revised title. If retaining the matrix ring is a non-negotiable requirement, stop and design a separate noncommutative module theory; do not merge it with this commutative plan.

### Stage 1 — algebra and polynomial model

- Verify the unique monomial basis, local/radical structure, unit test, socle and Frobenius property.
- Fix the involution on the whole ring and the Hermitian form convention.
- Prove the constacyclic shift/polynomial-quotient correspondence for central \(\lambda\).
- For odd \(n\), prove square-freeness over \(\mathbb F_{16}\) and the ordinary CRT decomposition. Because all factors are already over \(\mathbb F_{16}\), do not add an unnecessary Hensel-lifting step.

**Deliverable at this gate:** a self-contained algebra/preliminaries section with no matrix-ring equivalence claim.

### Stage 2 — CRT component duality

- Specify the conjugate-reciprocal factor involution \(\tau\) from \(\alpha\mapsto\overline\alpha^{-1}\).
- Derive the adjoint of the chosen constacyclic shift with the exact product order.
- Identify the component maps \(\theta_i\), any unit multipliers and the orientation of the annihilator formula.
- Cross-check the result on the whole code, zero code and small symbolic component ideals, and confirm the Frobenius cardinality relation.

**Stop condition:** if the dual operation does not restrict to the asserted component/staircase formula, revise or narrow the theorem before enumerating examples.

### Stage 3 — monomial ideal theorem

- Represent each monomial ideal by its upward-closed support in the \(k\times4\) rectangle (equivalently a staircase/antichain).
- Prove its annihilator support and cardinality.
- Combine with \(\tau\) to obtain a necessary-and-sufficient dual-containing condition for the selected monomial family.
- State the boundary of the result explicitly; do not generalize it to arbitrary ideals.

### Stage 4 — duality-adapted map

- Define \(\eta(a)=[U^{k-1}V^3]a\) and compute the Hermitian Gram matrix in the monomial basis.
- Construct an exact matrix \(T_k\) over \(\mathbb F_{16}\) by Hermitian Gram reduction; verify the matrix identity symbolically.
- Define \(\Phi\) blockwise and prove bijectivity, \(\mathbb F_{16}\)-linearity, form isometry, exact dual transfer, and constacyclic block-shift intertwining separately.
- Do not call it distance-preserving for a conventional ring weight unless that weight is explicitly defined and the isometry is proved. The standard Hamming distance is measured on \(\Phi(C)\).

### Stage 5 — novelty gate

Before computational expansion, perform a systematic review of exact quotient-ring notations and equivalent presentations, citation-chaining the 2021–2026 chain/non-chain constacyclic quantum literature and local Frobenius duality papers. Check theses, preprints and proceedings. Record databases, search strings, date and excluded near-matches. If an equivalent theorem exists, sharpen the theorem or stop.

### Stage 6 — approved pilot constructions

Only after Gates 0–5 and explicit approval:

1. Start with a small set of odd lengths and \(k\in\{2,3\}\), and \(\lambda=1\) plus representative order-five multipliers.
2. Enumerate only monomial component staircases, then filter by the proved dual condition.
3. Construct generator/parity-check data; verify ranks independently via CRT cardinalities.
4. Compute exact logical-coset distance by exhaustive enumeration only at feasible lengths; otherwise provide a mathematically certified bound with its hypotheses.
5. Compare against a dated best-known-code database snapshot and classify each entry as new, matched, dominated, or incomparable under a stated rule.

No extensive search is initiated in this blueprint-finalization phase.

## 3. Parameter and reproducibility protocol

For each future example, store: \(k,n,\lambda\); irreducible factors and factor-orbit pairing; component staircase data; code size/dimension; the explicit \(T_k\) matrix; generator and parity-check matrices of the image; dual-containment verification; exact distance method or lower-bound theorem; quantum parameters; software/version; and database snapshot/date. Recompute a subset independently in a second algebra system or by a separate linear-algebra check.

Use
\[
N=4kn,\qquad K=\sum_i d_i m_i,\qquad K_Q=2K-N,
\]
only after the component cardinality and image dimension are verified. Define \(d_Q\) as the minimum weight in \(D\setminus D^{\perp_H}\); never silently replace it with the minimum distance of \(D\).

## 4. Risk controls

- **Wrong ring returns:** keep the notation \(\mathcal R_k\) and explicitly state that it is not \(M_4(A_k)\) in every proposal/paper abstract.
- **Overstated classification:** label monomial ideals as a subfamily; no all-ideal claim without an independent classification proof.
- **Gray-map overclaim:** distinguish field-form isometry, dual transfer, shift preservation and Hamming-distance behavior.
- **Novelty inflation:** no “first” or “unexplored” language until a documented systematic search is complete.
- **Parameter inflation:** report exact quantum distances only when logical-coset distances have been certified.
- **Premature computation:** do not run code searches before the algebra and dual theorems pass.

## 5. Readiness

The revised plan is internally executable as a sequence of proof gates. It is not a completed mathematical result or a submission-ready paper. Actual research begins only after the user approves the revised direction; this turn stops at the blueprint and validation artifacts.
