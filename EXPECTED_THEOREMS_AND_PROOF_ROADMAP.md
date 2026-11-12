# Expected theorems and proof roadmap

**Status convention:** items marked **framework fact** are direct consequences of the chosen definitions and may be verified in the preliminary section. Items marked **proposed theorem** are research targets, not established results. No full proof is supplied here.

## Framework fact 1 — ring structure

**Assumptions.** \(k\ge2\), \(\mathcal R_k=\mathbb F_{16}[U,V]/\langle U^k,V^4\rangle\).

**Intended conclusion.** \(\mathcal R_k\) is a commutative local Artinian complete intersection with maximal ideal \((U,V)\), residue \(\mathbb F_{16}\), socle \(\mathbb F_{16}U^{k-1}V^3\), nilpotency index \(k+3\), Frobenius property, and \(16^{4k}\) elements.

**Significance.** Establishes a valid coefficient ring and the functional needed for duality.

**Proof requirements.** Use the monomial basis; prove the maximal ideal/unit criterion; identify the socle by annihilation by both variables; invoke/prove the Artinian complete-intersection-to-Gorenstein/Frobenius implication.

**Status.** Elementary framework fact; not a statement about the matrix ring.

## Framework fact 2 — constacyclic ideal and CRT model

**Assumptions.** \(n\) odd, \(\lambda\in\mathbb F_{16}^{\times}\), and the shift convention \(T_\lambda(c)=(\lambda c_{n-1},c_0,\ldots,c_{n-2})\).

**Intended conclusion.** \(T_\lambda\)-invariant \(\mathcal R_k\)-linear codes correspond to ideals of \(Q=\mathcal R_k[X]/\langle X^n-\lambda\rangle\). The polynomial \(X^n-\lambda\) is square-free over \(\mathbb F_{16}\), and if \(X^n-\lambda=\prod_i f_i\), then
\[
Q\cong\prod_i K_i[U,V]/\langle U^k,V^4\rangle,\qquad K_i=\mathbb F_{16}[X]/\langle f_i\rangle.
\]

**Significance.** Gives the exact component model required for code construction.

**Proof requirements.** Verify the coefficient/vector identification; compute the derivative in characteristic two; use the field Bézout identities to prove pairwise comaximality over \(\mathcal R_k\); apply the ordinary commutative CRT. Do not invoke Hensel lifting unnecessarily.

**Status.** Standard algebraic consequence; the manuscript must show the details.

## Proposed theorem 1 — Hermitian dual shift and factor pairing

**Assumptions.** \(n\) odd; \(\lambda\in\mathbb F_{16}\) with \(\lambda^5=1\); coefficient involution \(a\mapsto a^4\); ring form \(\langle x,y\rangle=\sum_i x_i\overline{y_i}\).

**Intended conclusion.** The Hermitian dual of a \(\lambda\)-constacyclic code is \(\lambda\)-constacyclic. The induced factor permutation is the involution whose root action is \(\alpha\mapsto\overline\alpha^{-1}\). Under CRT, the dual component at \(\tau(i)\) is the image of the annihilator of the component at \(i\) under a specified coefficient-semilinear reciprocal map, up to any explicitly identified unit that does not change the ideal.

**Significance.** Converts coordinate orthogonality into componentwise algebra.

**Proof requirements.** Check \(\overline\lambda^{-1}=\lambda\); derive the adjoint of the constacyclic shift under the exact product order; establish the reciprocal-conjugate action on the quotient and CRT idempotents; track unit factors and component directions. The formula must not be imported from a commutative field theorem without this derivation.

**Status.** Proposed; this is a principal proof gate.

## Framework lemma 3 — monomial annihilator

**Assumptions.** \(K\) is a finite extension of \(\mathbb F_{16}\), \(S=K[U,V]/\langle U^k,V^4\rangle\), and \(I\) is a monomial ideal with support \(E\).

**Intended conclusion.**
\[
\operatorname{supp}(\operatorname{Ann}_S(I))=
\{(a,b):\forall(r,s)\in E,\ a+r\ge k\text{ or }b+s\ge4\}.
\]
Also \(|I|=|K|^{|E|}\).

**Significance.** Gives a finite staircase calculation for the monomial subfamily.

**Proof requirements.** Use the truncated monomial basis. Prove both directions of annihilation and show distinct surviving monomials cannot cancel under multiplication by a fixed monomial generator.

**Status.** Elementary target; does not classify nonmonomial ideals.

## Proposed theorem 2 — monomial component dual-containment criterion

**Assumptions.** The hypotheses of Proposed theorem 1, plus a CRT code \(C\) whose component ideals \(I_i\) are monomial.

**Intended conclusion.** For the factor involution \(\tau\) and induced component maps \(\theta_i\),
\[
C^{\perp_H}\subseteq C
\quad\Longleftrightarrow\quad
\theta_i(\operatorname{Ann}(I_i))\subseteq I_{\tau(i)}\text{ for every }i.
\]
If \(\theta_i\) fixes the nilpotent monomial basis, this is equivalent to inclusion of the annihilator staircase in the paired component staircase.

**Significance.** A necessary-and-sufficient test within the precisely bounded family.

**Proof requirements.** Combine the component-dual result with the annihilator calculation; verify that \(\theta_i\) preserves \(U,V\) and how it acts on coefficients. Confirm the inclusion orientation by a dimension/cardinality check as an independent consistency test. State clearly if a unit twist or an additional hypothesis is needed.

**Status.** Proposed; do not describe as a result until proved.

## Proposed theorem 3 — duality-adapted field image

**Assumptions.** \(\mathcal R_k\) as above, the involution fixes \(U,V\), and \(C\subseteq\mathcal R_k^n\) is \(\mathcal R_k\)-linear.

**Intended conclusion.** With \(\eta(a)=[U^{k-1}V^3]a\) and \(B(x,y)=\eta(\langle x,y\rangle_{\mathcal R})\), construct a blockwise \(\mathbb F_{16}\)-linear isometry \(\Phi:\mathcal R_k^n\to\mathbb F_{16}^{4kn}\). Then
\[
\Phi(C^{\perp_H})=\Phi(C)^{\perp_H}.
\]
The image is invariant under the block \(\lambda\)-constacyclic shift of index \(4k\) whenever \(C\) is \(\lambda\)-constacyclic with \(\lambda\in\mathbb F_{16}\).

**Significance.** Supplies an exact field-Hermitian bridge without assuming that a coefficient Gray map preserves duals.

**Proof requirements.** Show the monomial pairing gives a nonsingular Hermitian Gram matrix; construct \(T_k\) over \(\mathbb F_{16}\) and verify the congruence; prove \((a,z)\mapsto\eta(az)\) is nondegenerate; use closure of \(C\) under all ring scalars to identify \(B\)-orthogonality with ring-valued orthogonality; check the shift intertwining. No standard Lee-weight equality is part of this theorem.

**Status.** Strongly motivated and reducible to standard Hermitian-form theory, but the explicit map and all compatibility checks remain to be done.

## Proposed corollary 4 — 4-ary stabilizer construction

**Assumptions.** \(D=\Phi(C)\) is \([N,K]_{16}\), \(D^{\perp_H}\subseteq D\), and \(K>N/2\).

**Intended conclusion.** The Hermitian construction yields a 4-ary stabilizer code with parameters
\[
[[N,2K-N,d_Q]]_4,\quad N=4kn,\quad
 d_Q=\min\{\operatorname{wt}_H(z):z\in D\setminus D^{\perp_H}\}.
\]

**Significance.** Connects proved classical dual containment to a valid quantum code.

**Proof requirements.** Verify the standard Hermitian construction hypotheses, the dimension formula, and the logical-coset distance. Do not substitute \(d_H(D)\) for \(d_Q\) without a proof; report certified bounds if exact distance is unavailable.

**Status.** Standard conditional corollary, not an existing code instance.

## Consistency checks built into the proof plan

- Whole-space code: its dual must be zero; zero code: its dual must be whole space.
- Component sizes must multiply to \(|C|\), and \(\sum_i\deg(f_i)=n\).
- CRT dual sizes must agree with the Frobenius cardinality identity \(|C||C^{\perp_H}|=|\mathcal R_k|^n\).
- The image dimension must equal \(\log_{16}|C|\); the field dual must have dimension \(4kn-K\).
- Dual containment must imply \(2K-4kn\ge0\).
- Every reported quantum distance must be measured on \(D\setminus D^{\perp_H}\), not inferred from ring cardinality or a different Gray map.
