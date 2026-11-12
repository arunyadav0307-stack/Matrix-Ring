# Complete blueprint audit

**Audited document:** *Blueprint A: Constacyclic codes over \(M_4(\mathbb F_2[u]/\langle u^k\rangle)\) and quantum codes over \(\mathbb F_4\)*, 7 pages, dated 12 November 2026.  
**Audit date:** 12 November 2026.  
**Scope:** independent review of the supplied blueprint and targeted source/literature verification. This is an audit only. No construction, proof development, parameter search, code search, or change to the original blueprint was undertaken. The uploaded original PDF was not modified.

## Final decision

**REJECT AS SUBMITTED — do not proceed with this blueprint in its current form.** The proposed ring model is incompatible with the stated matrix ring, and that error propagates into the proposed constacyclic decomposition, ideal classification, duality, Gray-map and quantum-code claims. The research direction is not declared impossible; it would require a new algebraic formulation and a fresh novelty review after researcher approval.

## Executive findings

1. **Critical algebra error.** For \(A_k=\mathbb F_2[u]/(u^k)\), the ring \(M_4(A_k)\) is noncommutative and is not local. Its Jacobson radical is \(M_4(uA_k)\) (zero for \(k=1\)); its quotient is \(M_4(\mathbb F_2)\), not \(\mathbb F_{16}\). Its center is the scalar matrices \(A_k I_4\). The claimed commutative local presentation \(\mathbb F_{16}[u,v]/(u^k,v^4)\) therefore cannot be a ring presentation of the stated matrix ring.
2. **The proposed order-5 multipliers conflict with centrality.** The four nonidentity fifth roots in an embedded \(\mathbb F_{16}\) are units, but that embedded field is not central in the matrix ring. Central units are scalar matrices from \(A_k^\times\), whose order is a power of 2; none has order 5. A noncentral shift can be defined with a side convention, but the blueprint's ordinary polynomial-quotient/ideal and CRT route does not follow from it.
3. **The structure/cardinality plan is conditional on the wrong ring.** The proposed factors \(K_i[u,v]/(u^k,v^4)\), local ideals, monomial counts, and Hensel/CRT argument cannot be used for \(M_4(A_k)\) without a separate, correctly sided module-theoretic derivation.
4. **Duality and quantum transfer are not established.** The field-level identity \(\overline\lambda^{-1}=\lambda\) for \(\lambda^5=1\) is correct when \(\overline\lambda=\lambda^4\) in \(\mathbb F_{16}\). It does not by itself define an involution or Hermitian form on the noncommutative matrix ring, prove a dual formula, or show a Gray map preserves orthogonality.
5. **Novelty is not established.** Direct prior work exists for the \(k=2\) ring (2022) and a 2025 ISIT paper covers the \(k=3\) cyclic-code case. A 2026 arXiv preprint treats cyclic codes for general \(k\), and a 2026 *Quantum Information Processing* article develops quantum codes from cyclic codes over \(M_3\)-rings. These do not, by themselves, settle the novelty of a valid \(M_4\) constacyclic/quantum extension; the claimed gap is nevertheless too narrow and insufficiently checked.

## Section-by-section audit

### Page 1 — overview, abstract, preliminaries, choice of \(\lambda\)

- The cardinality identity \(|M_4(A_k)|=2^{16k}=16^{4k}\) is correct. It permits a **set-size** count of \(4k\) field symbols per ring entry. It does not imply a local-ring isomorphism, a canonical \(\mathbb F_{16}\)-vector-space structure, or any Gray-map property.
- “Local with residue field \(\mathbb F_{16}\)” and maximal ideal \(\langle u,v\rangle\) are false for the stated matrix ring. See the algebra audit.
- “A unit exactly when its image in \(\mathbb F_{16}\) is nonzero” is false for \(M_4(A_k)\). A matrix is a unit exactly when its reduction modulo \(u\) is invertible in \(M_4(\mathbb F_2)\).
- The four nontrivial order-5 elements exist in \(\mathbb F_{16}^{\times}\), but they cannot be treated as central scalars in \(M_4(A_k)\). The draft abstract's phrase “units \(\lambda\) with \(\lambda^5=1\) in the residue field \(\mathbb F_{16}\)” uses a residue field the matrix ring does not have.
- The opening claim that constacyclic codes “give quantum codes that cyclic codes cannot reach” is a hypothesis, not an established consequence. No construction or parameter comparison supports it.

### Pages 2–3 — conjugation, factorization, code structure, cardinality, duals

- The source's \(\mathbb F_{16}\)-coordinate normal form must not be read as a commutative truncated polynomial ring. The 2026 preprint describes the cyclic-algebra relation \(ae=e\sigma(a)\), with \(e^4=1\); its nilpotent coordinate \(v=1+e\) is not a central indeterminate. The distinction is foundational.
- The claim that the extension \(a\mapsto a^4\), fixing \(u,v\), is a ring automorphism “only if” \(\mathbb F_{16}\) commutes with \(v\) is not a valid general criterion. In a skew presentation one must check the defining relations. More importantly, a Hermitian form on a noncommutative module requires a specified involution/anti-involution, side convention, and scalar target; none is supplied.
- For a commutative field polynomial in characteristic two, odd \(n\) and nonzero \(\lambda\) do make \(x^n-\lambda\) separable. The Hensel/CRT argument in the blueprint, however, is applied to an asserted commutative local ring and cannot be transferred to the actual matrix ring by cardinality or by a module normal form.
- The displayed \(S_i=K_i[u,v]/\langle u^k,v^4\rangle\) decomposition, the classification of its ideals, and the product formula for \(|C|\) are therefore **not verified theorems about the stated \(R\)**. The monomial-ideal count is valid only inside the proposed commutative quotient after that quotient has been justified; it does not classify all ideals even there.
- The Euclidean/Hermitian constacyclic-dual rules and component pairing are conditional on the exact shift, module side, and form. The proposed annihilator criterion also leaves left/right annihilators and the component conjugation map unspecified.

### Page 4 — Gray map and quantum construction

- \(N'=4kn\) is the correct symbol count **if** there is a bijection \(R\to\mathbb F_{16}^{4k}\). It does not prove additivity, \(\mathbb F_{16}\)-linearity, Hamming isometry, a quasi-twisted index, or orthogonality preservation.
- The proposed equalities \(\Phi(C^{\perp_H})=\Phi(C)^{\perp_H}\) and \(\Phi(C)\) being \(\mathbb F_{16}\)-linear are central unproved obligations, not routine properties of a Gray map. The attached 2026 matrix-ring quantum paper uses the reversed-index product \(\langle a,b\rangle_R=\sum_i a_i b_{n-1-i}\); its sampled Theorems 12–15 state a dual-size formula, a dual-containing criterion, distance-preserving maps for its \(k=3,2\) cases, and a dual-transfer identity. The extracted Theorem 15 proof is incomplete mid-argument, so those are recorded as source claims, not independently certified here. Its different product/map pair is a relevant warning, not a proof for \(M_4\).
- The standard Hermitian construction is correctly stated conditionally: an \([N,K,d]_{16}\) linear code \(D\) with \(D^{\perp_H}\subseteq D\) gives a 4-ary quantum code of dimension \(2K-N\). The quantum distance is the minimum weight of a nontrivial logical coset (often \(D\setminus D^{\perp_H}\)); it is at least \(d_H(D)\), but exact distance and equality/purity must be established.
- The quantum Singleton bound and defect formula are standard once the parameters are valid. They do not establish that any such code exists.

### Pages 5–6 — parameter claims, search plan, outline, risks

- The image length \(N=4kn\) does not depend on \(\lambda\). A different multiplier may change algebraic structure or available component choices in a valid setting, but “new lengths reachable only for \(\lambda\ne1\)” is unsupported as written.
- The proposed search grid is arithmetically consistent with \(N\le400\) at \(k=4,n=25\), but its parameter assumptions depend on the invalid order-5 central family and unproved component model.
- Enumeration of monomial ideals would explore only a restricted subfamily. It cannot certify a classification or a necessary-and-sufficient dual-containment theorem for all codes. A finite-field distance computation also cannot validate a flawed algebraic encoding or map.
- Grassl-table comparisons need an explicit convention for exact distance versus lower bounds, domination, field size, and the comparison snapshot/date. No parameter search was performed, as required by the audit-only constraint.
- The work order correctly recognizes the need to inspect maps and full papers before research execution, but the proposed sequence starts from a false ring model. The fallback to monomial ideals does not repair that foundation.

### Page 7 — journals and Q1 readiness

- Journal names and quartiles are targets to check, not evidence of readiness. Quartile depends on database, subject category, and year. The current plan has no valid main theorem, verified orthogonality transfer, complete novelty analysis, or validated examples; it is not Q1-ready.

## Direct answers

- **Reliable? No.** The ring/local/residue-field/unit claims are contradicted by the actual matrix-ring structure, and the later results rely on them.
- **Novel? Not established.** There is substantial direct prior art for cyclic codes over the same ring family, plus closely related quantum constructions. The exact novelty of a correctly reformulated constacyclic/quantum contribution remains unverified; absence of a hit in a targeted search is not proof of novelty.
- **Ready for research execution or Q1 submission? No.** The algebra, shift convention, involution/inner product, component decomposition, Gray map, and literature positioning must be rebuilt and approved first.

## Audit limits and principal references

The audit reviewed the full 7-page blueprint; the 30-page arXiv v1 preprint and its odd-length Euclidean-dual theorem; the attached 30-page 2026 QIP paper's ring/dual/quantum-map sections; publisher metadata and abstract for the 2022 \(M_4\) paper; its published correction; and targeted metadata/abstracts for related 2021–2026 work. The full body of the 2022 subscription article was not available for a line-by-line theorem audit. The extracted QIP Theorem 15 proof ends mid-argument and was not independently verified against rendered pages. The literature search was targeted, not exhaustive. No code-parameter or computational search was run.

- Joshi, Patel & Prakash, [arXiv:2602.18255v1](https://arxiv.org/abs/2602.18255), submitted 20 Feb 2026.
- Patel, Prakash & Islam, [“Cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2)\)”](https://doi.org/10.1007/s12095-022-00572-9), *Cryptography and Communications* 14 (2022); [published correction](https://doi.org/10.1007/s12095-022-00584-5).
- Joshi, Patel & Prakash, [“Quantum codes construction from cyclic codes over matrix rings”](https://doi.org/10.1007/s11128-026-05230-0), *Quantum Information Processing* 25, 207 (2026).
- Joshi, Patel & Prakash, “Construction of new codes over \(\mathbb F_{16}\) from cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2+u^2\mathbb F_2)\),” IEEE ISIT 2025; also cited as Ref. 19 in the 2026 QIP paper.
