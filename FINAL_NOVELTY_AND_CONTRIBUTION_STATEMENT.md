# Final novelty and contribution statement

## 1. Novelty position

**Novelty is plausible only for a narrow ring-specific theorem package; it is not certified.** The existing literature already establishes constacyclic codes over many chain and non-chain rings, dual-containing criteria, Gray maps that preserve duality, and quantum constructions. The revised project must not claim to be the first to use constacyclic codes, Hermitian dual containment, Gray maps, or finite rings for quantum codes.

The proposed alphabet is
\[
\mathcal R_k=\mathbb F_{16}[U,V]/\langle U^k,V^4\rangle,
\]
which is a commutative finite local Frobenius ring and is not the original matrix ring. Targeted exact-ring searches did not surface a publication treating this exact ring, odd-length \(\lambda\in\mu_5(\mathbb F_{16})\) constacyclic family, CRT monomial-ideal dual criterion, and duality-adapted field isometry together. This is an observation about the searches performed, **not a first-in-literature claim**.

## 2. What is already established

1. **Matrix-ring cyclic results:** the original \(M_4\) cyclic baseline has published \(k=2\) work (with a correction), a 2025 ISIT \(k=3\) paper, and a 2026 general-\(k\) preprint. The QIP 2026 matrix-ring quantum construction is adjacent \(M_3\) work. The revised project abandons the matrix-ring identification; it does not claim these results for \(\mathcal R_k\).
2. **Chain-ring code-to-quantum pipelines:** cyclic codes over \(\mathbb F_{q^2}[u]/\langle u^k\rangle\), their Hermitian duals, Gray maps and quantum applications were already studied. The revised ring adds a second nilpotent variable, but the generic construction method is not novel.
3. **Non-chain constacyclic quantum methods:** published examples include \(A_{q,r}\) rings, idempotent/non-chain rings, a multi-variable commutative ring with different defining relations [R20], local Frobenius rings of low nilpotency index, Gray-map transfers, hull methods, and 2026 work. The broad methodological combination is established.
4. **General factorization/CRT and quantum construction:** these are standard tools. Their use alone is not a research contribution.

Bibliographic details and source-access status are in `VERIFIED_REFERENCE_LIST.md`.

## 3. Candidate research contributions

### Contribution A — component duality for this complete intersection

Derive the exact conjugate-reciprocal permutation of the CRT factors of \(X^n-\lambda\), for odd \(n\) and \(\lambda^5=1\), and express the Hermitian dual of each component ideal via its annihilator in \(K_i[U,V]/\langle U^k,V^4\rangle\). The result should be stated for all component ideals only if its proof covers them; otherwise the theorem must explicitly be restricted to monomial ideals.

### Contribution B — a finite staircase criterion

For componentwise monomial ideals, translate annihilator inclusion into an exact criterion on upward-closed subsets of the \(k\times4\) exponent rectangle and the factor-pairing involution. The closed-form monomial-annihilator rule is elementary; novelty would lie in the full constacyclic factor-orbit/dual-containment theorem and its consequences, not in merely counting monomials.

### Contribution C — a specified duality-adapted image

Use the top-socle coefficient functional to define a nondegenerate \(\mathbb F_{16}\)-valued Hermitian form and construct an explicit blockwise isometry. The abstract existence of an isometry between finite-field Hermitian forms is standard and is not claimed as novel. The contribution would be an explicit, verifiable map for this ring and its exact compatibility with the ring dual and the constacyclic block shift.

### Contribution D — verified 4-ary codes

If the structural results yield dual-containing images with positive quantum dimension, report exact \([[4kn,2K-4kn,d]]_4\) parameters only when the logical-coset distance is certified. Parameter tuples are a possible applied contribution, not assumed results.

## 4. Distinctions from near matches

- The 2021 chain-ring paper uses one nilpotent variable and studies cyclic codes, not this two-variable complete-intersection monomial CRT criterion.
- General non-chain-ring constructions show the approach is not new in broad terms; the project must compare the exact ideal lattice, involution, multiplier set, component pairing, and field map.
- The original M4 papers concern a noncommutative matrix ring with a skew coordinate presentation. They do not establish results for the revised commutative ring.
- A Gray-map statement is not a contribution unless its source form, target form, duality, shift action and distance interpretation are all stated and proved.

## 5. Novelty gate and fallback

Before any extensive computation or manuscript drafting:

1. Search MathSciNet, zbMATH, Crossref, Google Scholar, arXiv, IEEE Xplore, Springer and citation chains using exact quotient-ring notation and equivalent basis descriptions.
2. Read the full texts of the closest constacyclic/non-chain and chain-ring quantum papers; abstracts alone do not settle theorem overlap.
3. Compare exact hypotheses and conclusions: ring, \(k\), length, multiplier, module/ideal class, involution, component dual, Gray map and quantum construction.
4. If the exact ring or theorem is already covered, sharpen the result (for example, a genuinely new all-ideal dual criterion or a nontrivial higher-\(k\) theorem) or stop. Do not market a parameter search as a structural novelty.

## 6. Honest claim for a future proposal

Until the novelty gate passes, the defensible wording is:

> “We propose to study a specific commutative Frobenius-ring family and a monomial-component subfamily. A targeted search has not identified the exact theorem package, but the surrounding methods are established and priority remains unverified.”

No “first,” “unexplored,” “new best,” or Q1-readiness claim is authorized by this blueprint alone.
