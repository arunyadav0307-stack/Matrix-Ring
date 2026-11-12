# Corrected algebraic framework

## 1. Design decision

The matrix ring in the original title cannot be used together with the proposed commutative-local-ring calculations. This reconstruction therefore makes an explicit change of alphabet to
\[
\mathcal R_k=\mathbb F_{16}[U,V]/\langle U^k,V^4\rangle,\qquad k\ge2.
\]
This is a new commutative coding alphabet, **not** a representation of the original matrix ring. The choice retains the intended \(\mathbb F_{16}\) scalar field, two nilpotent directions, alphabet size, central order-five multipliers, and potential 4-ary Hermitian construction.

## 2. Why the original matrix ring is not retained

Let \(A_k=\mathbb F_2[u]/\langle u^k\rangle\). The ring \(M_4(A_k)\) is noncommutative. Its Jacobson radical is \(M_4(uA_k)\) (zero if \(k=1\)), and its radical quotient is \(M_4(\mathbb F_2)\), not a field. Its center is \(A_k I_4\); its central units have no element of order 5. A field \(\mathbb F_{16}\) may appear in a cyclic-algebra coordinate description, but that does not make the matrix ring commutative or make its nilpotent coordinate a central polynomial variable.

By contrast, \(\mathcal R_k\) is commutative, with residue field \(\mathbb F_{16}\). Although
\[
|M_4(A_k)|=2^{16k}=16^{4k}=|\mathcal R_k|,
\]
equal cardinality does not imply ring isomorphism. Commutativity alone rules out an isomorphism; the radical quotients also differ. The published \(M_4(\mathbb F_2+u\mathbb F_2)\) paper and its correction, the 2025 \(k=3\) ISIT paper, and the 2026 matrix-ring preprint remain prior art for the abandoned matrix direction, not for an isomorphism to \(\mathcal R_k\).

## 3. Ring structure of \(\mathcal R_k\)

Every element has a unique expansion
\[
a=\sum_{0\le r<k}\sum_{0\le s<4}a_{r,s}U^rV^s,\qquad a_{r,s}\in\mathbb F_{16}.
\]
Consequently:

- \(\dim_{\mathbb F_{16}}\mathcal R_k=4k\), and \(|\mathcal R_k|=16^{4k}\).
- \(\mathcal R_k\) is a commutative Artinian local ring with maximal ideal \(\mathfrak m=(U,V)\) and residue field \(\mathcal R_k/\mathfrak m\cong\mathbb F_{16}\).
- A unit is exactly an element with nonzero constant coefficient \(a_{0,0}\).
- \(\mathfrak m^{k+3}=0\) and \(\mathfrak m^{k+2}\ne0\), since \(U^{k-1}V^3\ne0\). Thus the nilpotency index is \(k+3\).
- The socle is \(\operatorname{Soc}(\mathcal R_k)=\mathbb F_{16}U^{k-1}V^3\).
- The presentation is a zero-dimensional complete intersection, hence Artinian Gorenstein and Frobenius.

These properties are for the revised ring only; they must not be retroactively attributed to \(M_4(A_k)\).

## 4. Involution and Hermitian form

Define
\[
\overline{\sum a_{r,s}U^rV^s}=\sum a_{r,s}^{4}U^rV^s.
\]
Because \(a\mapsto a^4\) has order two on \(\mathbb F_{16}\), this is an involutive ring automorphism of \(\mathcal R_k\), fixing \(U,V\) and with fixed coefficient field \(\mathbb F_4\). For \(x,y\in\mathcal R_k^n\), set
\[
\langle x,y\rangle_{\mathcal R}=\sum_{i=0}^{n-1}x_i\overline{y_i},\qquad
C^{\perp_H}=\{y:\langle c,y\rangle_{\mathcal R}=0\text{ for all }c\in C\}.
\]
Commutativity removes the left/right-module ambiguity. For \(\lambda^5=1\), \(\overline\lambda=\lambda^4=\lambda^{-1}\), so \(\overline\lambda^{-1}=\lambda\). This is the correct multiplier identity for this revised ring.

## 5. Constacyclic polynomial model

Use the shift
\[
T_\lambda(c_0,\ldots,c_{n-1})=(\lambda c_{n-1},c_0,\ldots,c_{n-2}).
\]
The map \((c_0,\ldots,c_{n-1})\mapsto\sum_i c_iX^i\) identifies this shift with multiplication by \(X\) in
\[
Q_{n,\lambda}=\mathcal R_k[X]/\langle X^n-\lambda\rangle.
\]
Because \(\mathcal R_k\) is commutative and \(\lambda\) is central, a \(\mathcal R_k\)-linear code is \(\lambda\)-constacyclic exactly when its image is an ideal of \(Q_{n,\lambda}\). This ordinary quotient-ideal description is not being used for a noncentral multiplier in a matrix ring.

## 6. Square-free factorization and exact CRT

Assume \(n\) is odd and \(\lambda\in\mathbb F_{16}^{\times}\). In characteristic two,
\[
(X^n-\lambda)'=nX^{n-1}=X^{n-1},
\]
and \(\gcd(X^n-\lambda,X^{n-1})=1\), since \(\lambda\ne0\). Thus \(X^n-\lambda=\prod_i f_i(X)\) over \(\mathbb F_{16}\) with distinct monic irreducibles. The field Bézout identities persist over \(\mathcal R_k\), so the factors remain pairwise comaximal and the ordinary CRT applies:
\[
Q_{n,\lambda}\cong\prod_i\mathcal R_k[X]/\langle f_i\rangle
\cong\prod_i K_i[U,V]/\langle U^k,V^4\rangle,
\quad K_i=\mathbb F_{16}[X]/\langle f_i\rangle.
\]
This is an actual ring isomorphism for the revised commutative ring, obtained by base extension from a square-free field factorization. No Hensel lifting is required. A future variant with a non-field perturbation of \(\lambda\) would need a separate Hensel-lifting argument and is outside this blueprint.

## 7. Component ideals and their scope

Each CRT component \(S_i=K_i[U,V]/\langle U^k,V^4\rangle\) is local and Frobenius. Its **arbitrary** ideals are not assumed to be all monomial ideals and are not classified here. The proposed tractable family consists of componentwise monomial ideals \(I_i\).

Let \(E_i=\{(r,s):U^rV^s\in I_i\}\), with \(0\le r<k\), \(0\le s<4\), and \(m_i=|E_i|\). Since the monomials in the rectangle form a \(K_i\)-basis,
\[
|I_i|=|K_i|^{m_i},\qquad
|C|=16^{\sum_i d_i m_i},\qquad
\dim_{\mathbb F_{16}}C=\sum_i d_i m_i,
\]
where \(d_i=\deg f_i\) and \(\sum_i d_i=n\). This formula applies only to the specified monomial component family.

For such an ideal, its monomial annihilator has support
\[
E_i^{\operatorname{ann}}=\{(a,b):\text{for every }(r,s)\in E_i,\ a+r\ge k\text{ or }b+s\ge4\}.
\]
This follows from the truncated product rule for monomials. A proof must verify that no cancellation enlarges the annihilator beyond this span.

## 8. CRT duality target

For a root \(\alpha\) of \(X^n-\lambda\), define \(\tau(\alpha)=\overline\alpha^{-1}\). Since \(\overline\lambda^{-1}=\lambda\), \(\tau\) permutes the root set and is an involution. It induces an involution on irreducible factors; denote the paired factor by \(f_{\tau(i)}\). The research theorem must construct the corresponding coefficient-semilinear map \(\theta_i:S_i\to S_{\tau(i)}\), fixing \(U,V\), and prove the exact component dual formula. The expected formula is the image of \(\operatorname{Ann}(I_i)\) in component \(\tau(i)\), with any reciprocal unit made explicit. The dual-containing criterion is not accepted until this component statement is proved from the coordinate Hermitian form.

For monomial components, the expected criterion is
\[
C^{\perp_H}\subseteq C
\quad\Longleftrightarrow\quad
\theta_i(\operatorname{Ann}(I_i))\subseteq I_{\tau(i)}\quad\text{for every }i,
\]
which reduces to a staircase-support inclusion if \(\theta_i\) fixes the monomial basis and only changes field coefficients. This is an expected result, not a completed proof.

## 9. Duality-adapted \(\mathbb F_{16}\)-linear map

Define the socle functional \(\eta(a)=a_{k-1,3}\) and
\[
B(x,y)=\eta(\langle x,y\rangle_{\mathcal R}).
\]
The monomial basis pairs \(U^rV^s\) with \(U^{k-1-r}V^{3-s}\), so the Gram matrix of \(B\) is a nondegenerate Hermitian permutation matrix on each ring symbol. The pairing \((a,z)\mapsto\eta(az)\) on \(\mathcal R_k\) is nondegenerate; it is the Frobenius pairing associated with the one-dimensional socle.

Every nondegenerate Hermitian form of a fixed dimension over \(\mathbb F_{16}/\mathbb F_4\) is equivalent to the standard one. Thus there exists an invertible \(\mathbb F_{16}\)-linear transformation \(T_k\) on the \(4k\) coefficient coordinates that is an isometry from \(B\) to the standard field Hermitian form. Set
\[
\Phi(x_0,\ldots,x_{n-1})=(T_k\kappa(x_0),\ldots,T_k\kappa(x_{n-1})),
\]
where \(\kappa\) lists the coefficients \(a_{r,s}\). The transformation must be explicitly constructed and its Gram identity checked in the eventual research. It is not justified by cardinality alone.

For an \(\mathcal R_k\)-linear code \(C\), if \(B(c,y)=0\) for all \(c\in C\), then for every \(a\in\mathcal R_k\), \(B(ac,y)=\eta(a\langle c,y\rangle_{\mathcal R})=0\). Nondegeneracy of \((a,z)\mapsto\eta(az)\) forces \(\langle c,y\rangle_{\mathcal R}=0\). Hence the ring dual is exactly the orthogonal complement under \(B\), and an isometry \(\Phi\) gives exact field-dual transfer. This argument relies on the code being \(\mathcal R_k\)-linear.

Because \(T_k\) is used blockwise and commutes with scalar multiplication by \(\lambda\in\mathbb F_{16}\), the image intertwines the ring shift with a block \(\lambda\)-constacyclic shift of index \(4k\). No ordinary Lee-weight preservation is claimed; output Hamming distances must be measured after applying \(\Phi\).

## 10. Quantum applicability

The image \(D=\Phi(C)\) is \(\mathbb F_{16}\)-linear, of length \(N=4kn\), and satisfies \(D^{\perp_H}=\Phi(C^{\perp_H})\) once the isometry theorem is proved. If \(C^{\perp_H}\subseteq C\), then \(D^{\perp_H}\subseteq D\) and the standard Hermitian construction over \(\mathbb F_{16}=\mathbb F_{4^2}\) applies. For \(K=\dim_{\mathbb F_{16}}D\), the quantum dimension is \(2K-N\), and the exact distance is the minimum weight in \(D\setminus D^{\perp_H}\). The dimension formula, containment, and distance must all be checked; no numerical quantum parameter is asserted here.

## 11. Explicit exclusions

- No assertion that \(\mathcal R_k\cong M_4(A_k)\).
- No use of a noncentral order-five matrix as an ordinary polynomial scalar.
- No classification of all ideals of \(S_i\) from monomial enumeration.
- No Hensel lift where field factors already give the exact factorization.
- No Gray-map distance or dual-preservation claim without the stated Gram proof.
- No quantum distance equality, parameter tuple, or novelty claim without its own verification.
