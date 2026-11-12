# Theorem verification audit

**Scope:** verify the blueprint's proposed theorem statements against the ring structure and the supplied/cited source material. No new theorem is developed or proved here. “Conditional” means a standard statement may hold after its missing hypotheses are supplied; it is not verified for the blueprint's matrix ring as written.

## A. Proposed ring and unit statements

### Claim A1 — \(M_4(\mathbb F_2[u]/(u^k))\) is a local ring with residue \(\mathbb F_{16}\)

**Verdict: false.** For \(A_k=\mathbb F_2[u]/(u^k)\), \(J(M_4(A_k))=M_4(uA_k)\), and the quotient is \(M_4(\mathbb F_2)\), not a field. The center is \(A_kI_4\). The commutative local ring proposed in the blueprint cannot be isomorphic to the matrix ring.

### Claim A2 — unit iff the \(\mathbb F_{16}\)-residue is nonzero

**Verdict: false for the stated ring.** The correct matrix-ring criterion is invertibility after reduction modulo \(u\) in \(M_4(\mathbb F_2)\). The blueprint's criterion would require the false local-ring model.

### Claim A3 — four order-5 elements are permissible central \(\lambda\)'s

**Verdict: field count correct; central-ring use false.** \(\mathbb F_{16}^{\times}\) has four elements of order 5, but an embedded \(\mathbb F_{16}\) is noncentral. The central-unit group comes from \(A_k^\times\), of order 1 for \(k=1\) and \(2^{k-1}\) for \(k>1\); it has no element of order 5.

## B. Proposed structure/cardinality theorems

### Claim B1 — odd length gives a separable factorization and a CRT decomposition into \(S_i=K_i[u,v]/(u^k,v^4)\)

**Verdict: field separability is conditionally correct; the ring decomposition is unsupported and conflicts with the matrix ring.** Odd \(n\) makes \(x^n-\lambda\) separable over a characteristic-2 field when \(\lambda\ne0\). It does not turn \(M_4(A_k)\) into a commutative local algebra or justify the displayed factor rings. For noncentral \(\lambda\), the ordinary polynomial-quotient setup also needs a separate definition.

### Claim B2 — classify ideals by monomial/principal ideals and count by monomial bases

**Verdict: conditional for the proposed commutative quotient, not verified for \(R_k\).** In a justified component \(K_i[u,v]/(u^k,v^4)\), monomial ideals can be counted by monomial basis elements. This only treats that subfamily. A Gröbner-basis suggestion is a research method, not a proof of completeness or feasibility. The ring-component premise has not been established.

### Claim B3 — \(|C|=\prod_i |K_i|^{m_i}\)

**Verdict: conditional.** It follows from an actual direct-product component decomposition and the stated component sizes. Neither condition has been proved for the matrix-ring codes as formulated.

## C. Proposed duality and dual-containment theorems

### Claim C1 — Euclidean dual is \(\lambda^{-1}\)-constacyclic; Hermitian dual is \(\lambda^{-4}\)-constacyclic

**Verdict: conditional field-level result, not verified for the matrix ring.** Under the usual field shift/form convention, the Hermitian multiplier is \(\overline\lambda^{-1}=\lambda^{-4}\). If \(\lambda^5=1\), then \(\lambda^{-4}=\lambda\). For the noncommutative ring one must define the module side, multiplier action, involution/anti-involution, form, and product order first.

### Claim C2 — components pair under a shifted root map \(j\mapsto-4j\)

**Verdict: unproved and underspecified.** It requires an explicit root parametrization, a valid factorization model for \(x^n-\lambda\), and an induced conjugate-reciprocal action on the actual components.

### Claim C3 — dual containment iff \(\overline{\mathrm{Ann}(C_{i'})}\subseteq C_i\) for all \(i\)

**Verdict: target only.** No proof is supplied. “Ann” must be designated left or right, and the dual/component identification must be established. The result cannot be inferred from a commutative model that is not the stated ring.

## D. Gray-map and quantum theorems

### Claim D1 — there is an \(\mathbb F_{16}\)-linear distance-preserving \(\Phi:R^n\to\mathbb F_{16}^{4kn}\)

**Verdict: cardinality is compatible; the map properties are unverified.** A specific \(\mathbb F_{16}\)-action, map, metric, and shift action are required. Isometry, additivity, linearity, quasi-twisted structure, and dual transfer must be checked separately.

### Claim D2 — \(\Phi(C^{\perp_H})=\Phi(C)^{\perp_H}\)

**Verdict: unproved.** Requires the full definition of \(\Phi\), the ring form, the field Hermitian product, and a compatibility proof plus appropriate size/dimension facts. The cited QIP \(M_3\) work uses a specially selected inner product and a different Gray map because its earlier map did not transfer duals.

### Claim D3 — Hermitian construction gives \([[4kn,2K-4kn,\ge d_H(\Phi(C))]]_4\)

**Verdict: standard conditional dimension/lower-bound statement.** It applies only if \(D=\Phi(C)\) is genuinely \(\mathbb F_{16}\)-linear and Hermitian dual-containing. The exact quantum distance is determined by nontrivial logical cosets and may exceed the classical distance; equality/purity must be shown. No eligible \(D\) is established in the blueprint.

### Claim D4 — quantum Singleton defect \(\delta=N+2-K_q-2D_q\)

**Verdict: correct definition under the usual stabilizer-code convention.** The formula is not evidence for the existence or novelty of any parameters.

## E. Source-paper theorem check

The attached [arXiv:2602.18255v1](https://arxiv.org/abs/2602.18255) states Theorem 4.1 for **odd-length cyclic** codes over its matrix-ring model, gives a Euclidean-dual expression, and proves it by a candidate inclusion followed by cardinality comparison. The inspected text supports that scope and proof pattern; extracted/rendered formulas and index conventions must be read carefully. It does not state the blueprint's nontrivial \(\lambda\)-constacyclic theorem, its shifted component criterion, or its \(\mathbb F_4\) quantum result. The source paper is a preprint and cannot be cited as verification of those extensions.

The 2022 \(M_4\) published correction ([DOI](https://doi.org/10.1007/s12095-022-00584-5)) corrects displayed equations and a Gray-map matrix. It does not supply the blueprint's constacyclic/quantum theorem.

### QIP 2026 source claims sampled in the supplied PDF

The extracted source defines a reversed-index product \(\langle a,b\rangle_R=\sum_{i=0}^{n-1}a_i b_{n-1-i}\), described there as nondegenerate. In the sampled sections, Theorem 12 states a dual-size formula; Theorem 13 gives a dual-containing criterion involving self-reciprocal factors and selected ideals; Theorem 14 claims distance-preserving Gray maps \(\phi_1,\phi_2\) for the source's \(k=3,2\) cases, respectively; and Theorem 15 claims \(\phi(C_R^\perp)=\phi(C)_R^\perp\). These are claims in the \(M_3\) paper with its specified product and maps, not results for the blueprint's \(M_4\) setting.

The extracted Theorem 15 proof begins with an orthogonality/product condition (the extracted line reads \(ab=0\)) and expands coordinates, but the available extract ends mid-argument. The product order, side conventions, and complete proof were not independently certified from the rendered source pages here. Therefore the theorem statements are recorded as adjacent-source claims only; this audit does not endorse their proof or transfer them to the blueprint. The reversed-index product must not be silently replaced by the standard coordinatewise Euclidean/Hermitian product.

## Verification conclusion

No proposed theorem that depends on the commutative local-ring model is verified as a theorem about \(M_4(A_k)\). The standard field and quantum statements remain usable only after the researcher supplies and proves the missing algebra, shift, form, and map hypotheses. This audit stops short of constructing those hypotheses or proving replacements.
