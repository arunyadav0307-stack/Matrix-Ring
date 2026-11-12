# Mathematical correctness audit

**Verdict:** the blueprint contains a correct cardinality calculation and several standard field-level formulas, but its central ring model and the transfer of those formulas to the matrix ring are incorrect or unproved. This is a mathematical audit, not a repair or proof-development exercise.

## Claim-by-claim review

### 1. Cardinality and symbol count — correct, narrowly

For \(A_k=\mathbb F_2[u]/\langle u^k\rangle\), \(|A_k|=2^k\). Therefore
\[
|M_4(A_k)|=|A_k|^{16}=2^{16k}=16^{4k}.
\]
A bijection from one ring symbol to \(4k\) symbols of \(\mathbb F_{16}\) would be cardinality-compatible, and a length-\(n\) word would map to \(4kn\) symbols. This establishes neither a ring isomorphism nor a linear, isometric, or orthogonality-preserving map.

### 2. Local-ring and residue-field claims — false

The blueprint treats \(M_4(A_k)\) as a local commutative ring with residue field \(\mathbb F_{16}\). In fact, its Jacobson radical is \(M_4(uA_k)\) (zero for \(k=1\)) and its quotient is \(M_4(\mathbb F_2)\). This quotient is a noncommutative matrix ring, not a field. The center of \(M_4(A_k)\) is \(A_k I_4\). Since the claimed residue field and maximal ideal are wrong, the blueprint's unit criterion, Hensel/CRT components, and local-ideal model do not apply as stated.

### 3. Unit test — false as stated

A matrix in \(M_4(A_k)\) is invertible exactly when its reduction modulo \(u\) is invertible in \(M_4(\mathbb F_2)\). It is not enough that a purported \(\mathbb F_{16}\)-component be nonzero. The latter test is for a commutative local ring with residue field \(\mathbb F_{16}\), which is not this ring.

### 4. Order-5 multiplier family — field fact true, ring use invalid

The multiplicative group \(\mathbb F_{16}^{\times}\) has order 15, so it has exactly four nonidentity elements of order 5. That field fact is correct. But the embedded \(\mathbb F_{16}\) in \(M_4(\mathbb F_2)\) is not central. The central units of \(M_4(A_k)\) are scalar matrices from \(A_k^{\times}\); this group has order 1 for \(k=1\) and \(2^{k-1}\) for \(k>1\), so it contains no element of order 5. Thus the proposed order-5 family cannot be used as central scalars in the blueprint's ordinary quotient/ideal framework.

A noncentral multiplier may still define a right-linear shift if the code is a right \(R\)-module and the multiplier acts on the left. That possibility requires an explicit definition and a separate module treatment; it does not validate \(R[x]/\langle x^n-\lambda\rangle\) as an ordinary quotient ring or the proposed CRT argument.

### 5. Separability and Hensel lifting — conditional only

In characteristic two, for odd \(n\) and nonzero field \(\lambda\), the derivative of \(x^n-\lambda\) is \(x^{n-1}\), so the polynomial is separable over a field. This is a valid field-level observation. Hensel lifting as used in the blueprint additionally requires a valid commutative coefficient ring (or a rigorously specified noncommutative analogue), a central polynomial/quotient setup, and compatible factorization. The blueprint has not supplied those prerequisites for \(M_4(A_k)\).

### 6. Component rings and ideal counts — conditional on a false premise

The ring \(K_i[u,v]/\langle u^k,v^4\rangle\) is a finite commutative local complete-intersection/Frobenius ring. For a monomial ideal in that quotient, its additive size can be counted as \(|K_i|^{m_i}\), where \(m_i\) counts the monomial basis elements in the ideal. Those statements concern the proposed commutative quotient, not automatically the matrix-ring code components. The blueprint has not established the asserted component-ring isomorphism. Its monomial count also covers only monomial ideals; it is not a classification of all ideals or codes.

### 7. Dual of a constacyclic code — correct in the usual field setting, not transferred

For a field code with a specified conventional \(\lambda\)-shift and standard Hermitian conjugation \(z\mapsto z^4\) on \(\mathbb F_{16}\), the corresponding Hermitian dual multiplier is \(\overline\lambda^{-1}=\lambda^{-4}\). If \(\lambda^5=1\), then \(\lambda^{-4}=\lambda\). This explains the proposed field-level motivation.

It does not establish the same formula for a noncommutative matrix-ring right module. The blueprint must first define the shift side, inner product, coefficient involution (or anti-involution), and any induced operation on \(\lambda\). An entrywise field Frobenius on an embedded subfield is not, by itself, a specified involution on the full matrix ring.

### 8. Component pairing and annihilator criterion — not verified

The root rule \(j\mapsto-4j\) is a plausible reciprocal-conjugate rule in a particular field factorization, but the blueprint gives no root parametrization, lift, or proof that it describes the proposed components. “\(\mathrm{Ann}\)” also needs a left/right convention for a noncommutative ring. The displayed equivalence between dual containment and component annihilator inclusion is a target, not a verified theorem.

### 9. Gray-map claims — unproved

The statements “\(\Phi(C)\) is \(\mathbb F_{16}\)-linear,” “index \(4k\) quasi-twisted,” “\(\Phi(C^{\perp_H})=\Phi(C)^{\perp_H}\),” and Hamming-distance preservation are independent obligations. A cardinality-compatible encoding or a Gray isometry for some weight does not imply any of them. The 2026 matrix-ring quantum paper (for \(M_3\)) explicitly distinguishes a first Gray map that fails to transfer duals from a different map/product pair designed to do so; this illustrates the issue.

### 10. Quantum parameters — standard theorem, conditional application

If \(D\) is a genuine \([N,K]_{16}\) linear code with \(D^{\perp_H}\subseteq D\), the usual Hermitian construction over \(\mathbb F_{16}=\mathbb F_{4^2}\) gives a 4-ary stabilizer code of dimension \(K_q=2K-N\). Its quantum distance is the minimum weight of a nontrivial logical coset (commonly represented by \(D\setminus D^{\perp_H}\)); it is at least the minimum distance of \(D\), but equality is not automatic. The quantum Singleton bound \(K_q+2D_q\le N+2\) and defect \(N+2-K_q-2D_q\) are standard once actual parameters are known. No such \(D\) or parameters have been established here.

### 11. “New lengths” — unsupported

For a fixed map to \(\mathbb F_{16}^{4kn}\), the image length is \(N=4kn\), independent of \(\lambda\). A different multiplier may alter code existence or dimensions only after a valid construction is defined. The claim that lengths are reachable only for \(\lambda\ne1\) is not established by the blueprint and conflicts with its own length formula if it means the resulting quantum block length.

## Bottom line

The only unconditional numerical identity in the blueprint's main algebraic chain is the cardinality/symbol-count identity. Field-level separability, the fifth-root count, the \(\lambda^{-4}=\lambda\) identity, and the quantum Singleton formula are conditionally correct. Their application to \(M_4(A_k)\) depends on foundational structures the blueprint has not defined and, in the local-ring case, contradicts the actual matrix-ring quotient.
