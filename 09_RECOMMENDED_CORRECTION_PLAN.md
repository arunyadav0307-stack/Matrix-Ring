# Recommended correction plan

**Status:** recommendations only. The audit is complete; no correction, construction, proof, or computation has been carried out. Stop here and wait for explicit researcher approval before any follow-up work.

## Phase 0 — freeze the current blueprint

Do not use the current \(\mathbb F_{16}[u,v]/(u^k,v^4)\) local-ring model, order-5 “scalar” family, component cardinality formulas, Gray-map duality claim, or quantum parameters as established results. Preserve the uploaded PDF unchanged. Mark the current statements as rejected/conditional in any future draft.

**Gate 0:** researcher approves a revised algebraic direction before work resumes.

## Phase 1 — settle the algebra before coding theory

1. Fix the object \(R=M_4(\mathbb F_2[u]/(u^k))\) and document its center, radical, quotient, units, and cyclic-algebra presentation, including all cross-relations.
2. State whether codes are left or right \(R\)-submodules.
3. Define the exact constacyclic shift, multiplier side, and what “\(\lambda\)-constacyclic” means for central and noncentral \(\lambda\).
4. If the multiplier is noncentral, do not use an ordinary central-variable quotient as if it were a ring. Choose and justify a compatible module, skew-polynomial, or shift-operator model.
5. Revisit the proposed order-5 values. If centrality is required, remove that family for this ring; if noncentral shifts are intentionally used, state that explicitly and rework every later theorem accordingly.

**Gate 1:** a coherent object/shift/module definition and correct ring facts.

## Phase 2 — establish structure and cardinality in the corrected setting

1. Prove the exact decomposition used; do not replace a module decomposition with a ring CRT isomorphism without proof.
2. State the classification scope precisely. If only monomial ideals or a selected class is treated, say so in the theorem title and novelty claim.
3. Derive code sizes from the actual component/module structure and verify no components are double-counted.
4. Treat Hensel lifting only after identifying a valid commutative central coefficient subring or a proved noncommutative analogue.

**Gate 2:** independently checked structure and cardinality statements for the chosen scope.

## Phase 3 — define duality and prove the exact dual statement

1. Specify the value of the form, multiplication order, module side, and involution/anti-involution on the whole ring.
2. Define Euclidean and Hermitian duals distinctly; name left/right annihilators.
3. Derive the dual shift parameter from the chosen convention rather than importing \(\lambda^{-1}\) or \(\lambda^{-4}\) without checking.
4. Establish any reciprocal/conjugate component permutation and prove the dual-containment criterion.

**Gate 3:** a precise dual theorem and a proved dual-containing condition.

## Phase 4 — validate the field-image route

1. Give the exact map \(\Phi\) and the \(\mathbb F_{16}\)-action on its domain.
2. Prove bijectivity/cardinality, additivity/field-linearity, and metric preservation as separate properties.
3. Compute the induced image of the constacyclic shift; state the quasi-twisted structure only if the block action proves it.
4. Prove the exact dual-transfer identity (or a sufficient inclusion plus verified cardinality relation) for the chosen field Hermitian product. If this cannot be done, do not claim the Hermitian quantum route.

**Gate 4:** a genuine \(\mathbb F_{16}\)-linear dual-containing image or a different approved quantum framework.

## Phase 5 — quantum statements and literature positioning

1. State quantum dimension as \(2K-N\) only after a valid \([N,K]_{16}\) image and Hermitian dual containment are established.
2. Define quantum distance via nontrivial logical cosets. Label a certified lower bound separately from an exact distance; prove any “pure” equality claim.
3. Update the prior-art comparison to include the corrected 2022 \(k=2\) paper, 2025 ISIT \(k=3\) paper, general-\(k\) 2026 preprint, 2026 \(M_3\) quantum paper, and current constacyclic/non-chain quantum literature.
4. Replace “new lengths cyclic cannot reach” with a precise, theorem-supported comparison or remove it.

**Gate 5:** a defensible contribution statement and novelty claim, reviewed by the researcher.

## Phase 6 — computation and submission readiness (only if later approved)

Only after Gates 0–5 pass should a researcher approve any Magma/GAP/Python enumeration or code-table comparison. The search must specify field encoding, generator convention, exact/lower-bound distance status, the database snapshot, dominance rule, and reproducibility data. Q1 venue selection and quartile claims come last and must be checked by year/category/source.

## Stop conditions

Stop and return to the researcher if the desired \(\lambda\)-family is required to be central but no nontrivial order-5 central multiplier exists; if the intended Gray map fails the needed dual transfer; or if the corrected ring cannot support the claimed component decomposition. These are research-direction decisions, not automatic invitations to change the user's project.
