# Pairing and duality — independent critical audit

**Audit execution:** 2026-11-13 UTC (recorded workspace clock). **Disposition: retain the core right-module duality, reject several frozen summaries.** Originals are unchanged. Claim IDs and the six required classifications are consolidated in [MATHEMATICAL_CLAIM_VERIFICATION.md](MATHEMATICAL_CLAIM_VERIFICATION.md).

## 1. Exact convention and evidence map

Throughout this review,
\[
q=p^m,\quad A=\mathbb F_q[u]/(u^t),\quad R=M_r(A),\quad r\ge2,\ t\ge1,\ n\ge1.
\]
The blueprint's candidate lane has \(t\ge2\); some existing examples legitimately have \(t=1\). The historical sources use \(r_{old}\) for the field extension degree, \(m_{old}\) for matrix size, and \(s\) for the Galois parameter. Here \((m,r,k)=(r_{old},m_{old},s)\). This is an **audit notation choice**, not a claim that the original blueprint used these exact letters.

\(\sigma_k(\sum a_j u^j)=\sum a_j^{p^k}u^j\) fixes \(u\), acts entrywise on matrices, and \(\theta_k=\sigma_k\circ T\). This is **not** the whole-ring power map \(a\mapsto a^{p^k}\): for example at characteristic two, \(\sigma_1(u)=u\) whereas \(u^2=0\) when \(t=2\).

A code \(C\) is a **right** \(R\)-submodule of \(R^n\). For cyclic codes the variable \(X\) is central and
\[
R_n=R[X]/(X^n-1)\simeq M_r(B),\quad B=A[X]/(X^n-1);
\]
cyclic codes are right ideals of \(R_n\). Do not replace them by arbitrary field subspaces, left ideals, or two-sided ideals.

Source abbreviations (all inside the included original package, expanded at `work/PHASE0_COMPLETE_AUDIT_PACKAGE/`):

- **S:** `mathematical_evidence/prior_project/03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`.
- **S2B:** same directory, `PHASE2_STAGE2B_CRT_PRINCIPALITY.md`.
- **S3B:** same directory, `PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md`.
- **M:** `repository_integrity/prior_work/PAPER/sections/` (canonical manuscript); staged deltas have separate mappings.
- **D:** `computational_evidence/research-data/`.
- Independent arithmetic: [scripts/independent_math_checks.py](scripts/independent_math_checks.py), [core results](evidence/independent_core_checks.json), [follow-up results](evidence/critical_followup_checks.json), [scope results](evidence/remaining_scope_checks.json). These do not import project arithmetic, **except** the last scope test, explicitly labelled a disposable-source reproduction of the Phase-5 bug.

## 2. Well-defined maps and module law

**VERIFIED UNDER CONDITIONS — D01/F03/F04.** Coefficient Frobenius preserves truncated multiplication, transpose reverses matrix products, and the maps commute. Thus
\[
\theta_k(ab)=\theta_k(b)\theta_k(a),\qquad\theta_k^2=\sigma_{2k}.
\]
Its being an anti-automorphism does not make it an involution. The latter requires \(m\mid2k\). Source: S, Lemmas 1.1–1.3.

The primary pairing is
\[
B_k(x,y)=\sum_{i=1}^n\theta_k(x_i)y_i,\qquad
C^{\perp_k}=\{y:B_k(x,y)=0\text{ for all }x\in C\}.
\]
The correct identities are
\[
B_k(xa,y)=\theta_k(a)B_k(x,y),\qquad B_k(x,yb)=B_k(x,y)b.
\]
This proves additivity and right closure of the dual. It also explains why the transpose resolves the **same-sided** duality issue in this framework.

**INCORRECT — D02.** The frozen `PHASE0_PAIRING_OPTIONS.md`, P1, prints \(B_k(ax,y)=\theta_k(a)B_k(x,y)\). For \(a=E_{12},x=E_{21},y=I\), the left side is \(E_{11}\), the printed right side is \(E_{22}\); the correct \(B_k(xa,y)\) is \(E_{22}\). This error is in the summary, not S Proposition 2.1(3), which uses the right action correctly. The independent counterexample is `summary_ax_formula_counterexample`.

“Transpose is unavoidable” must be read as a statement about this desired same-sided construction, not as a theorem that no other bilinear, character-valued, or opposite-sided duality can exist.

## 3. Nondegeneracy is not the cardinality proof

**VERIFIED UNDER CONDITIONS — D03.** If \(x\ne0\), choose a nonzero coordinate \(x_i\), and let \(y\) be zero except \(y_i=I_r\). Then \(B_k(x,y)=\theta_k(x_i)\ne0\). The reverse-variable argument uses \(x_i=I_r\). This proves elementwise nondegeneracy in each variable over this ring. Source S Proposition 2.2 gives this valid probe.

**INCORRECT — D04.** The frozen summary's \(E_{ba}\) probe is not valid as stated. With \(x=E_{12}\), its proposed \(y=E_{21}\) gives \(\theta_k(x)y=E_{21}E_{21}=0\). This refutes that proof sentence, **not** nondegeneracy of the pairing.

**VERIFIED — D05 (finite counterexample); INCORRECT — D06 (unqualified degeneracy inference).** The plain product \(P(x,y)=\sum x_i y_i\) is also elementwise nondegenerate (the identity probe works), but its annihilator does not have the required perfect **same-right-module** size law. An independent finite counterexample is
\[
R=M_2(\mathbb F_2),\quad n=1,\quad
C=\left\{\begin{pmatrix}a&b\\0&0\end{pmatrix}:a,b\in\mathbb F_2\right\}.
\]
Here \(|C|=4\), the plain right-variable annihilator has size 1, and the \(\theta\)-dual has size 4, with \(|R|=16\). Thus plain-product same-sided size fails, although the product itself is not elementwise degenerate. S Proposition 2.3 explicitly distinguishes the appropriate **opposite-sided** annihilator identities. The original “degenerate” wording conflates these notions.

The historical E4 experiment was rerun in this audit: the reported **31/35** size-law failures for plain products at \(M_2(\mathbb F_2),n=3\) recur. This is a finite example, not a theorem that every possible plain-product annihilator is invalid.

## 4. Scalar companion and size law: where the module hypothesis enters

Put
\[
\lambda(a)=[u^{t-1}]a,\quad\Lambda(Z)=\lambda(\operatorname{Tr}_{matrix}Z),\quad
b_k(x,y)=\Lambda(B_k(x,y)).
\]
The matrix trace is \(A\)-valued; \(\Lambda\) is \(\mathbb F_q\)-valued. Only after the **field trace** \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}\) is applied is the result an \(\mathbb F_p\)-valued commutation test. These are three distinct operations.

**VERIFIED UNDER CONDITIONS — D08/D09.** For a right \(R\)-module \(C\), the scalar and ring-valued orthogonals coincide. One inclusion is immediate. For the other, if \(b_k(x,y)=0\) for all \(x\in C\), right closure gives
\[
\Lambda(\theta_k(a)B_k(x,y))=0\quad\text{for every }a\in R.
\]
No nonzero \(Z\in R\) is annihilated by all these tests. To see this, select a nonzero entry of \(Z\), take its lowest nonzero \(u\)-degree \(j\), multiply by an appropriate matrix unit times \(u^{t-1-j}\), and take \(\Lambda\). Its top trace coefficient is nonzero. Since \(\theta_k\) is onto, the displayed identities force \(B_k(x,y)=0\). This is the ideal-catching argument in S Lemma 1.4 and Proposition 4.1.

The transported scalar form is a perfect field sesquilinear form of dimension \(N=tr^2n\); its Gram matrix is invertible. Therefore
\[
\dim_{\mathbb F_q}C+\dim_{\mathbb F_q}C^{\perp_k}=N,
\qquad |C|\,|C^{\perp_k}|=|R|^n.
\]
Source S Theorem 3.5 also proves this through correctly sided Frobenius annihilators. **Elementwise nondegeneracy alone is not the justification.**

The module restriction cannot be dropped. The independent scope test takes the field subspace \(C=\mathbb F_4E_{11}\subset M_2(\mathbb F_4)\), which is not a right \(R\)-submodule. Its ring-valued orthogonal has field dimension 2, while its trace-scalar orthogonal has dimension 3. See `scalar_orthogonal_requires_module_hypothesis`.

## 5. Double dual: the positive twist is correct

**VERIFIED UNDER CONDITIONS — D10.** Apply \(\theta_k\) to \(B_k(x,y)=0\). Anti-multiplicativity gives
\[
0=\theta_k(B_k(x,y))=\sum_i\theta_k(y_i)\sigma_{2k}(x_i)
=B_k(y,\sigma_{2k}(x)).
\]
Hence \(\sigma_{2k}(C)\subseteq(C^{\perp_k})^{\perp_k}\). The size law gives equal cardinalities, so
\[
\boxed{(C^{\perp_k})^{\perp_k}=\sigma_{2k}(C).}
\]
This is the **positive** composition direction for the stated definition. Source S Theorem 3.6 has the same result; its main annihilator proof is valid. It must not be changed to \(\sigma_{-2k}(C)\) by importing a second-argument-twist field convention.

An independent brute-force \(M_2(\mathbb F_8),n=1,k=1\) test uses the right ideal with basis
\[
(1,0,\alpha,0),\quad(0,1,0,\alpha),\qquad\alpha=2
\]
in the recorded polynomial basis. It has 64 elements, its dual has 64, the ambient ring has 4096, and its double dual is \(\sigma_2(C)\), **neither \(C\) nor \(\sigma_{-2}(C)\)**. The full bases are in `double_dual_positive_not_negative_direction`.

**VERIFIED UNDER CONDITIONS — D12/D13.** For an individual code,
\[
(C^{\perp_k})^{\perp_k}=C\iff\sigma_{2k}(C)=C.
\]
Because the sets have equal finite size, the weaker inclusion \(C\subseteq(C^{\perp_k})^{\perp_k}\) already forces equality. Thus a particular invariant code can be reflexive in a globally nonreflexive regime.

For **every** right module over this matrix ring, reflexivity holds iff \(m\mid2k\). Sufficiency follows immediately. For necessity, if \(\sigma_{2k}\ne id\), choose a nonfixed \(a\in\mathbb F_q\) and the Morita column module \(A(e_1+a e_2)\subset A^r\); normalization of the first coordinate shows it changes under \(\sigma_{2k}\). This uses \(r\ge2\). Source S Theorem 3.9 supplies the sound slope-module argument. The necessity sketch at the end of Theorem 3.6, which merely mentions a vector with a nonfixed entry, is **insufficient by itself**: a vector can change while the module it generates stays fixed. Do not confuse that gap with failure of the criterion.

For odd \(m\), only \(k=0\pmod m\) is universally reflexive. For even \(m\), the only nontrivial such residue is \(k=m/2\). The independent \(\mathbb F_8\) test also exhibits \(B_k(x,y)=0\) but \(B_k(y,x)\ne0\). No automatic exchange of orthogonal arguments is allowed outside the reflexive regime.

## 6. Left mirrors and the A-valued candidate

Two different left-sided conventions appear in the originals; they must not be merged.

| Left pairing (dual in the second variable) | Valid module rule | Same-convention double dual | Classification |
|---|---|---|---|
| \(L_k(x,y)=\sum y_i\theta_k(x_i)\), the mirror in S | \(L_k(ax,y)=L_k(x,y)\theta_k(a)\), \(L_k(x,ay)=aL_k(x,y)\) | \(\sigma_{2k}(C)\) | **VERIFIED UNDER CONDITIONS** for left modules |
| \(L'_k(x,y)=\sum x_i\theta_k(y_i)\), printed in the frozen P1 summary | \(L'_k(ax,y)=aL'_k(x,y)\), \(L'_k(x,ay)=L'_k(x,y)\theta_k(a)\) | \(\sigma_{-2k}(C)\) | **VERIFIED UNDER CONDITIONS**, but it is not the same positive-twist convention |

The alternate is not an invalid pairing. The error is transferring the first pairing's linearity and positive double-dual formula unchanged to it. A fresh \(\mathbb F_8\) matrix-valued brute-force test confirms the negative twist for the alternate; see `alternate_left_mirror_has_negative_double_twist`.

**INCOMPLETE as printed — D15.** The frozen A-valued option
\[
Q_k(x,y)=\sum_i\operatorname{Tr}(x_i\sigma_k(y_i)^T)
\]
is not an independently established new theory. With the correct **right** action,
\(Q_k(x,yb)=Q_k(x\sigma_k(b)^T,y)\), so right closure can be justified. The report's sketch instead uses left multiplication. After applying \(\lambda\),
\[
\lambda Q_k(x,y)=\sigma_k\bigl(b_{-k}(x,y)\bigr).
\]
Right multiplication by powers of \(u\) shows that A-valued vanishing for all \(x\in C\) is equivalent to top-coefficient vanishing. Thus its right-module orthogonal corresponds to **\(-k\)**, not automatically the P1 dual at \(+k\). Its same-convention double dual has the negative twist. This is a convention reconciliation of an existing candidate, not authorization to develop it.

## 7. Cyclicity, hulls, principality: separate the rings

**VERIFIED UNDER CONDITIONS — D16/D17.** The cyclic shift satisfies
\(B_k(x,Ty)=B_k(T^{-1}x,y)\). Therefore cyclic right modules have cyclic right duals and cyclic right hulls. For a right ideal in the central-variable quotient, the reversal/right-annihilator formula in Stage 2C Theorem 3.8 applies. The hull is an intersection, is \(\sigma\)-equivariant, and is self-orthogonal even when the duality is not reflexive: both hull arguments lie respectively in \(C\) and \(C^{\perp_k}\). It need not be a left/two-sided ideal. Also
\[
\operatorname{Hull}_k(C^{\perp_k})=C^{\perp_k}\cap\sigma_{2k}(C),
\]
which equals \(\operatorname{Hull}_k(C)\) in the reflexive regime.

**INCORRECT — F06.** “Most one-sided ideals of \(R=M_r(A)\) are non-principal” is false. A submodule of \(A^r\) over a chain ring needs at most \(r\) generators; those generators can be columns of a single matrix. Thus **every left/right ideal of the base matrix ring is principal**. The independent \(A=\mathbb F_4[u]/u^2,r=2\) enumeration finds 33 Morita submodules and maximum \(\mu_A=2\), consistent with the theorem. This does not imply they are free: \(uA\subset A\) has 4 elements, not \(16^j\) for any positive free rank. M §05's “every submodule ... is free” sentence is wrong; “generated by at most r elements” is what is needed.

**VERIFIED UNDER CONDITIONS — F09.** The cyclic ambient ring is different. S2B Theorems 4.1, 4.3 and Corollary 4.4 already establish for \(M_2(B)\)
\[
\boxed{\text{every right ideal is principal}\iff t=1\ \text{or}\ p\nmid n.}
\]
In the wild case a local component has maximal ideal \(\mathfrak m=(u,w)\), with \(\dim_K\mathfrak m/\mathfrak m^2=2\). Then \(W=\mathfrak m\oplus\mathfrak m\) has \(\mu_B(W)=4>2\), proving a nonprincipal right ideal. This is a general **code** example, not automatically a hull example. The six reports' broad claim that this criterion remains open is stale.

**VERIFIED — D18, explicit hull existence.** S3B §7 gives an actual nonprincipal self-dual hull at \((q,t,n)=(4,2,2)\). For \(B=\mathbb F_4[u,w]/(u^2,w^2),w=X+1\), the supplied generators give \(\dim W=4\), \(\dim\mathfrak mW=1\), hence \(\mu_B(W)=3>2\). The associated right ideal has field dimension 8 in ambient dimension 16 and is self-dual for both \(k=0,1\). Independent arithmetic reconstructs these spaces and both duals. This is a rigorous finite witness; a randomized failure to find two generators is **not** its proof.

**INCORRECT — D19, manuscript's different construction.** In M §05 `thm:nonprincipal`, taking \(i=0\) and \(U=\operatorname{soc}(B^2)\) of dimension 2 does not give the asserted direct sum \(Be_1\oplus U\): their intersection has dimension 1. The actual sum has dimension 5, its radical multiple dimension 3, and \(\mu_B=2\), **not 3**. The independent follow-up verifies this. The theorem that nonprincipal hulls exist survives via the preceding S3B witness, but this manuscript proof and its claimed family need correction. Other printed wild-family witnesses were not independently recertified here.

**INCORRECT — D21, Phase-5 implementation.** In `D/scripts/phase5_quantum_constructions.py`, Task D3 (lines 1364–1368), `hrows` (full ring-image rows of length 16 in this witness) is passed to `unpair`, which expects Morita rows of length 8; the correct return is `inter`. A focused disposable-source test reproduces **wrong \(\mu=4\)** versus **correct \(\mu=3\)** on the same known hull. Phase 6's `hull_mu` already explicitly documents and avoids this bug. Do not use Phase-5 hull-\(\mu\) distributions or the manuscript's explanatory remark as independent proof. A code-\(\mu\) versus hull-\(\mu\) distinction does not repair this representation error.

## 8. Boundary of this verdict

The algebraic backbone is not refuted: correct side conventions, size law, **positive** double dual, conditional reflexivity, cyclicity, scalar transfer and an explicit nonprincipal hull all survive critical checking. Conversely, a clean ZIP and passing scripts do not validate the false summary laws, the defective manuscript nonprincipal proof, or the quantum proof gaps catalogued separately. No original theorem, script, manuscript or report was edited, and no new research direction was implemented.
