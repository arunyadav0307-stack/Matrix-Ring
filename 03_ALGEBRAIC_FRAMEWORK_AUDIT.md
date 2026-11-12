# Algebraic framework audit

## 1. The ring actually named in the blueprint

Set \(A_k=\mathbb F_2[u]/\langle u^k\rangle\) and \(R_k=M_4(A_k)\). Its basic structure is:

- \(|A_k|=2^k\), and \(|R_k|=(2^k)^{16}=2^{16k}=16^{4k}\).
- \(Z(R_k)=A_k I_4\), the scalar matrices.
- \(J(R_k)=M_4(uA_k)\); for \(k=1\), this is zero.
- \(R_k/J(R_k)\cong M_4(\mathbb F_2)\), a simple noncommutative matrix ring, not a field.
- \(R_k\) is noncommutative and not local. A matrix is a unit exactly when its reduction in \(M_4(\mathbb F_2)\) is invertible.

The claim that \(R_k\) is the commutative local ring \(\mathbb F_{16}[u,v]/(u^k,v^4)\) is impossible: the latter has residue field \(\mathbb F_{16}\), whereas the matrix ring has quotient \(M_4(\mathbb F_2)\) by its Jacobson radical. Equal cardinality does not imply isomorphism.

## 2. What the \(\mathbb F_{16}\)-coordinate description can mean

A copy of \(\mathbb F_{16}\) can be embedded in \(M_4(\mathbb F_2)\), and the matrix ring can be expressed using cyclic-algebra/module coordinates. Such coordinates are useful but are not central scalars. The 2026 preprint's cyclic-algebra discussion includes \(ae=e\sigma(a)\) and \(e^4=1\); setting \(v=1+e\) gives a nilpotent coordinate, not a central polynomial variable commuting with all of \(\mathbb F_{16}\). Thus
\[
\mathbb F_{16}+v\mathbb F_{16}+v^2\mathbb F_{16}+v^3\mathbb F_{16}
\]
may describe an additive normal form/module, but the blueprint cannot replace the matrix ring by the ordinary commutative ring \(\mathbb F_{16}[v]/(v^4)\). The separate scalar \(u\) commuting with the matrix entries does not make \(v\) central.

## 3. Central versus noncentral constamultipliers

A central unit of \(R_k\) has the form \(aI_4\) with \(a\in A_k^\times\). For \(k=1\), \(A_k^\times=\{1\}\); for \(k>1\), \(|A_k^\times|=2^{k-1}\). There is no central order-5 unit. The four nontrivial fifth roots in an embedded \(\mathbb F_{16}\) are noncentral matrix units.

This is not a claim that no noncentral constacyclic shift can be defined. For right-\(R_k\)-linear codes, the coordinate shift with **left** multiplication by a fixed \(\lambda\) is right-linear. But the blueprint must explicitly choose this convention and prove the desired properties. With the ordinary central-indeterminate polynomial ring \(R_k[x]\), the element \(x^n-\lambda\) is not central for noncentral \(\lambda\); its generated ideal need not be two-sided. Consequently, the usual ideal correspondence and the displayed quotient-ring/CRT argument do not follow. A skew-polynomial, endomorphism, or direct-module formulation would be a different framework requiring approval and proof.

## 4. Why the proposed component rings do not follow

The blueprint moves from factorization over \(\mathbb F_{16}\) to
\[
S_i=K_i[u,v]/\langle u^k,v^4\rangle,\qquad K_i=\mathbb F_{16}[x]/\langle f_i\rangle.
\]
These are commutative local complete intersections. Their cardinalities match the sizes one might expect for some module components, but the quotient \(R_k/J(R_k)\) and the noncentral cyclic-algebra action rule out the claimed ring isomorphism. A module decomposition, if available, has to retain the left/right action and the noncommuting field coordinates; cardinality alone is insufficient.

The following proposed steps are therefore blocked as statements about \(R_k\):

1. Hensel-lifting a factorization in a residue **field** \(\mathbb F_{16}\) to the noncommutative matrix ring as if it were a commutative local algebra.
2. Identifying every code component with an ideal of \(S_i\).
3. Classifying all codes by ideals in \(S_i\) and multiplying component cardinalities.
4. Applying commutative monomial-ideal annihilator formulas directly to matrix-ring codes.

A valid replacement might use right-module decompositions rather than ring CRT components, but this audit does not construct or prove one.

## 5. Duality requires a precise module/form convention

The blueprint needs to specify all of the following before its Euclidean or Hermitian dual formulas can be audited as theorems:

- whether codewords are left or right \(R_k\)-modules;
- whether the constacyclic shift acts by left or right multiplication and on which coordinate;
- the value ring/field of the inner product and multiplication order;
- the map called conjugation, including whether it is a ring automorphism or an involutive anti-automorphism;
- whether the dual is a left or right submodule and which annihilator is meant;
- how the chosen form behaves under the proposed Gray map.

The rule \(a\mapsto a^4\) is a field automorphism of \(\mathbb F_{16}\) with fixed field \(\mathbb F_4\). It is not yet a definition on all of \(R_k\). For a noncommutative Hermitian module form, the extension must respect the skew multiplication and the chosen module side. It is not enough to say that \(u,v\) are fixed.

## 6. What remains mathematically sound

- The size \(|R_k|=16^{4k}\) and the resulting cardinality-compatible field-symbol count are correct.
- The field \(\mathbb F_{16}\) can be used as a coordinate field after a specific module action and map are fixed.
- The commutative ring \(K_i[u,v]/(u^k,v^4)\), if it were the chosen algebra, is a finite local Frobenius ring; monomial ideals there can be counted by their monomial basis.
- The standard field Hermitian construction can be used after an actual \(\mathbb F_{16}\)-linear image and dual-containment statement are proved.

These observations do not rescue the present chain of arguments. **A researcher must first approve a corrected algebraic framework; no alternative construction is implemented here.**

## Source checks

The primary structural source inspected was Joshi–Patel–Prakash, [arXiv:2602.18255v1](https://arxiv.org/abs/2602.18255), particularly its cyclic-algebra relation, ring/module description, and Sections 3–5. It is a preprint, not proof that the blueprint's commutative interpretation is valid. The 2022 \(M_4\) article's publisher abstract and correction were also checked: [article](https://doi.org/10.1007/s12095-022-00572-9), [correction](https://doi.org/10.1007/s12095-022-00584-5).
