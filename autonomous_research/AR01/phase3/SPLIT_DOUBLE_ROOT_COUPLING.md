# A12 — fully split double-root factor coupling

**Reconstructed working note at M4, with fresh executed certificates.** The earlier local-only note was absent on continuation; this successor reconstructs its proof and records the new execution separately. See `../evidence/M4_CHRONOLOGY_AND_CONTINUATION.md`. This is not a recovered historical file, external originality clearance or a publication claim.

The length change is explicit: a local same-input hull uses W against its own dual, whereas cyclic reversal/Frobenius may couple **different** CRT factors. CRT transport and scalar repeated-root hulls are occupied territory. These results resolve a bounded applicability question, not by themselves a Q1 paper.

## 1. Exact changed hypothesis, unchanged form

Retain k=F_(2^m), m≥2, A=k[u]/u², R=M₂(A), a central X, cyclic **right** ideals, θ_s(M)=σ_s(M)^T and the actual first-slot pairing

B_s(x,y)=Σ_(i=0)^(n−1) θ_s(x_i)y_i,     0≤s<m.

Now **n=2N with N an odd positive divisor of q−1**. This is the fully split odd part, not arbitrary irreducible degree or length. N=1 is Core A. Let μ_N be the Nth roots of unity in k. Set B=k[u,w]/(u²,w²), J=(u,w), z=uw and V=k². Write S=M₂(A[X]/(X^(2N)−1)).

## 2. Explicit CRT coordinates and the actual adjunction

For λ∈μ_N, define Γ_λ by X↦λ(1+w), u↦u and a↦a for a∈k. Since N is odd, [λ(1+w)]^N=1+w. Thus the **same global polynomial w=X^N−1** is the local w in every factor. The product map is

Γ:A[X]/(X^(2N)−1) ≅ ∏_(λ∈μ_N) B.

An explicit inverse follows from

e_λ(X)=Σ_(j=0)^(N−1) λ^(−2j) X^(2j).

At a root μ this evaluates to Σ(μ²/λ²)^j: it is 1 at μ=λ and 0 otherwise, because N is 1 as a field element. Consequently these are orthogonal idempotents with sum 1, and the inverse sends (b_λ)_λ to Σ e_λ b_λ(u,X^N−1). These are ring coordinates, not Gray isometries. Apply entrywise to matrix rings.

Define x^†s(X)=Σ θ_s(x_i)X^(−i). The constant coefficient of x^†s y is B_s(x,y). Testing every cyclic shift X^a x tests **every coefficient** of x^†s y. Therefore global orthogonality to a cyclic right ideal is exactly x^†s y=0 for every codeword x; a single unshifted constant coefficient is insufficient.

At each λ,

Γ_λ(x^†s)=σ_s(Γ_(δ_s(λ))(x))^T,
δ_s(λ)=σ_(−s)(λ⁻¹).                                    (C1)

Indeed X⁻¹ evaluates to λ⁻¹(1+w); pulling coefficient Frobenius outside evaluation requires the **inverse** Frobenius on λ⁻¹. Frobenius fixes u,w. The map δ_s need not be an involution.

If the component column modules are W_λ≤B², their dual/hull modules are

(W(C^(⊥s)))_λ = D_s(W_(δ_s(λ))),
H_λ = W_λ ∩ D_s(W_(δ_s(λ))).                            (C2)

Here D_s(U)={y:Σσ_s(v_i)y_i=0 for all v∈U}, exactly as in the foundations. This is not a switch of slot, side or form. At N=1 it reduces to Core A. The same-input local theorem cannot be applied to (C2) when δ_s(λ)≠λ.

## 3. Generator bookkeeping and sharp ambient bound

For a finite product, the minimum module-generator number is the maximum of the component numbers: project any generating list for the lower bound, and pad local lists with zeros and assemble using idempotents for the upper bound. Packing columns in pairs then gives

μ_(∏B)(W)=max_λ μ_B(W_λ),
μ_(∏M₂(B))(I_W)=ceil((max_λ μ_B(W_λ))/2).                 (C3)

Thus a global cyclic right ideal is principal exactly when all its column components have μ≤2. These are routine product/Morita facts, not novelty claims.

Every B-submodule M≤B² has μ_B(M)≤4. A nonradical proper input is abstractly B⊕I with μ≤3. For a radical input, use the proved descriptor (K,T,f), with t=dim T, k₀=dim K≤2 and r=dim(π₁T+π₂T)≤2. Then t≤2r and μ=t+k₀−r≤r+k₀≤4. Equality forces k₀=r=2,t=4 and hence M=JB². This bound concerns arbitrary submodules, not just same-input hulls.

## 4. Exact principality-preservation dichotomy in this split family

**Theorem.** Every principal cyclic right ideal in §1 has a principal s-hull **if and only if**

**N divides 2^s+1.**                                    (C4)

If (C4) holds, the attainable maximum component hull-μ values are exactly {0,1,2}. If it fails they are exactly {0,1,2,3,4}. At values 3 and 4 the global right-ideal hull requires **two matrix generators**, not three or four.

### Preservation direction and values 0,1,2

The permutation δ_s fixes every λ exactly when σ_s(λ)=λ⁻¹ for all λ∈μ_N, equivalently N|(2^s+1), since μ_N is cyclic. Under that condition (C2) is the same-input Core A hull in every factor. Apply the proved principal-input preservation theorem and (C3). The constant generators I₂, diag(u,0), uI₂ attain 0,1,2 for every δ_s, respectively.

### A sharp μ4 counterexample when any factor moves

Let η=δ_s(λ)≠λ. Specify g_λ=I₂, g_η=zI₂ and g_ν=0 otherwise, assembling the **single** matrix generator

g(X)=[e_λ(X)+u(X^N−1)e_η(X)]I₂.                          (C5)

The input is principal, with W_λ=B² and W_η=zV. Testing the two socle coordinate vectors gives D_s(zV)=JB² (Ann(z)=J and σ_s(z)=z). Thus H_λ=JB² and μ_B(H_λ)=4. The ambient bound proves sharpness. The other component hulls cannot increase it.

### A μ3 witness, with the actual intersection checked

In the fixed B² coordinates put

P=B(1,1)+zV,      P′=B(1,1+u)+zV,      Q=J(1+u,1).

The dimensions are 5,5,3 and the generator numbers 2,2,2. All displayed coefficients are fixed by σ_s. The generators (u,u) and (w+z,w) of Q force

y₂=(1+u)y₁+c z, c∈k,

so D_s(Q)=P′. For example the first test forces the remaining error into (u), the second into (w), and (u)∩(w)=kz. This is a direct equation solve, not an unjustified dimension argument.

Also P∩P′=J(1,1)+zV=W_*. In the two graph descriptions the condition is u a∈kz on the first coordinate a; equivalently a∈J. Hence this is precisely the known μ3, dimension4, self-dual Core A module.

Assign W_λ=P, W_η=Q and all other W_ν=0. Formula (C2) gives H_λ=W_* with μ=3. At the only other nonzero input component the hull is a submodule of Q, inside the primitive free line B(1+u,1), so the scalar-ideal bound gives μ≤2. Thus the global maximum is exactly3. Explicit component matrices are

p=[[1,0],[1,z]],     q=[[u,w+z],[u,w]],

g=e_λ p+e_η q,

where w is globally X^N−1. This is an explicitly intersected module and a proved dual; it does **not** repair or reuse the different failed historical direct-sum argument. Together with the constant controls, all asserted values occur. ∎

## 5. Same embedded code at q4, n6 — now numerically checked

Let k=F4 with ω²+ω+1=0, N=3, λ=ω, η=ω². Then

e_ω=1+ωX²+ω²X⁴,     e_(ω²)=1+ω²X²+ωX⁴.

For (C5), the scalar coefficients of the generator, in ascending X order, are

**(1+u, ωu, ω+ω²u, u, ω²+ωu, ω²u).**                     (C6)

The **same** input has dimension20 over F4 in the dimension48 ambient. At s=0, δ swaps ω and ω², and the hull is the right ideal generated by the two matrices

**e_ω uI₂,  e_ω (X³−1)I₂**.

It has dimension12, maximum component μ4, and needs two matrix generators. At s=1, δ is identity, and the hull has the single generator

**e_(ω²) u(X³−1)I₂**.

It has dimension4 and maximum component μ2. Both global duals have dimension28.

These were initially proof-derived targets. They are **now actually checked** by the fresh `split_resumed_v1` and `split_global_resumed_v1` runs. The latter reconstructs the right ideal by original cyclic matrix products, enforces all eight field coordinates of the original matrix-valued pairing, compares complete input/dual/hull spaces, and verifies that the displayed hull generators generate the entire hull. The alternative field/linear-algebra route is a same-agent separate implementation, not independent human review.

## 6. Actual finite evidence

There are 41 named field/length/twist cases at q4 (N1,3), q8 (N1,7) and q16 (N1,3,5,15), with all twists for each listed family. Every case passes the original-global audit. This is **not an exhaustive all-code census at n>2**. CRT full rank was tested for each of the eight field/length pairs. Negative controls detect both omission of reversal and forward instead of inverse Frobenius: each incorrectly predicts maximum μ2 instead of the actual μ4 in its named control.

The saved stream/certificate SHA-256 values are in both summaries and the audit. Old M2/M3 source/results remain byte-preserved. Reconstruction and fresh execution do not retroactively create the missing old local files.

## 7. Contribution reduction and disposition

For clarity, the μ4 mechanism already exists in the **scalar** repeated-root ideal problem. If T=A[X]/(X^(2N)−1), h∈T and C=hM₂(T), then cyclic adjunction gives

C^(⊥s)=M₂(Ann(h^†s)),
H_s(C)=M₂((h)∩Ann(h^†s)).

This follows by testing matrix units and shifts; h is central so the entrywise scalar annihilator is exact. If L=(h)∩Ann(h^†s), its column module is L⊕L and (C3) gives μ_(M₂(T))(M₂(L))=μ_T(L). In (C5) the moving factor has scalar hull J, which already needs two scalar generators. The matrix μ4 witness therefore does not establish a genuinely noncommutative mechanism or independent novelty.

A12 is a rigorous boundary to overextending n=2 preservation, and an exact split-family criterion, but its core CRT/scalar mechanisms are routine. Do **not** promote it alone to an original Q1 main contribution. Complete technical comparison with scalar repeated-root hull literature (especially S01/NL10) and same-ring QC work (S09) remains unavailable. Search/access failure is not a research gap. Non-split factors, higher multiplicities, arbitrary skew quotients, Gray compatibility, quantum consequences and distance claims remain outside this note.
