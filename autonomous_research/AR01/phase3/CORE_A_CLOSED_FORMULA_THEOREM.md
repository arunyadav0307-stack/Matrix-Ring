# Core A closed-formula theorem — exact statement

**Mathematical status:** conventional proof supplied in [the full proof](CORE_A_CLOSED_FORMULA_FULL_PROOF.md). Proof audit, executed tests and literature novelty have distinct statuses in [the status report](../audits/CORE_A_PROOF_STATUS_REPORT.md). Neither computational agreement nor this statement certifies external originality or Q1 suitability.

## T1. Exact family and form

Let m≥2, k=F_q with q=2^m, A=k[u]/(u²), R=M₂(A), and let X be central. Count **all cyclic right-linear codes of length2 over R**, equivalently all right ideals of

S=R[X]/(X²−1)=M₂(B),  B=k[u,w]/(u²,w²),  w=X+1.

They are counted as distinct embedded codes, not up to a GL action, isomorphism, column permutation or Gray equivalence. No principal-input restriction is imposed.

For 0≤s<m let σ=σ_s be coefficient Frobenius: σ(a+ub)=a^(2^s)+u b^(2^s). It fixes u; on B it also fixes w. Set θ_s(M)=σ(M)^T. Use the **original first-slot matrix-valued global pairing**

⟨x,y⟩_s=θ_s(x₀)y₀+θ_s(x₁)y₁ ∈ R,
C^(⊥s)={y:⟨x,y⟩_s=0 for all x∈C}.

Its hull is C∩C^(⊥s). σ is not assumed involutive. In general the double dual is σ_(2s)(C), not C.

## T2. Column invariant and exact interpretation

Every C is uniquely I_W={matrices over B whose two columns lie in W}, for an embedded B-submodule W≤B². Put

D_s(W)={y∈B²:σ(v₁)y₁+σ(v₂)y₂=0 for every v∈W},
H_s(W)=W∩D_s(W),
μ_B(M)=dim_k(M/JM),  J=(u,w).

The global dual/hull correspond exactly to I_(D_s(W)) and I_(H_s(W)); this is proved from cyclic shifts and the original matrix product, not an assumed local isometry.

Define

N_j(q,s)=#{embedded W≤B²: μ_B(H_s(W))=j}.

The **matrix right-ideal** minimum number of generators is ceil(μ_B(H_s(W))/2). Thus column values1 and2 both give a nonzero principal matrix ideal; column value3 gives two matrix generators.

## T3. Explicit integer parameters

Let

g=gcd(s,m), with gcd(0,m)=m;  Q=2^g;  r=m/g;
e=Q if r is odd, and e=Q² if r is even;
d=1 if r is odd, and d=Q+1 if r is even.

Then e=|Fix(σ²)| and d=gcd(2^s+1,q−1). Define

c=e(Q−1)+Q = Q² (r odd), or Q(Q²−Q+1) (r even),

U=q²+q+1+qc−[(q+1)(Q+1)+d(q−Q)],

F=q(Q³+Q²−1)−Q²                         if r is odd,
F=(Q²−1)[q(Q²+Q+1)−Q²]                  if r is even,

A₀=(q+1)(2q²+q+1),
G₄=q⁴+3q³+4q²+3q+5,
L=2q⁴+8q³+10q²+7q+9.

U counts Ω_s-isotropic projective points of projection rank2 in k²⊕k². F counts their incidences with Ω_s-self-dual two-planes. In the earlier working note/code, F is named `B_inc` / `selfdual_two_plane_rank_two_point_incidences_B`; it is **not** the ring B.

## T4. Complete closed distribution

For every field and twist in T1,

**N₀=(q+1−d)q³+2,**

**N₁=2A₀+d[q³−2q²−Q²(q−Q)]+(q+3)U−F,**

**N₂=G₄+d[2q²+Q²(q−Q)−1]−(q+3)U+F,**

**N₃=d,**

**N_j=0 for j≥4.**

All quantities on the right are explicitly given integer expressions. Equivalently N₂=L−N₀−N₁−N₃; the displayed N₂ is its expanded closed form. The total family size is L. The proof gives a disjoint reconstruction/count of the entire family and identifies precisely which classes contribute each value.

## T5. Consequences, exceptions and scope

1. The marginal histogram depends on s only through gcd(s,m). This is **not** a joint same-input all-twist distribution, and does not identify the individual hulls for two twists with the same gcd.
2. Exactly d inputs have a nonprincipal matrix hull. They are

   W=J K+uw·k², where K=k(1,a) and aσ(a)=1.

   In each case W=H_s(W)=D_s(W), dim_k W=4 and μ_B(W)=3. All proper hulls are matrix-principal in this exact family.
3. Matrix minimum-generator counts, as opposed to column μ, have histogram

   0 generators: N₀;  1 generator: N₁+N₂;  2 generators: d;  ≥3:0.

4. At s=0, Q=q,r=1,d=1, and the formulas reduce to

   (N₀,N₁,N₂,N₃)=(q⁴+2, 7q³+4q²+2q+2, q⁴+q³+6q²+5q+4, 1).

5. Order2 twists and all non-involutive odd/even orders are covered. q2,m1 is only an explicitly labelled auxiliary check, not part of T1. Lengths>2, nonsplit factors, higher coefficient nilpotency, other matrix ranks, left codes, alternate slots/forms and physical/Gray applications are not asserted.

The exact exceptional/boundary register, independent mathematical re-derivations and theory/evidence comparison are linked from the status report. No hidden freeness, full-GL equivalence, reflexivity or literature-novelty assumption is used in the theorem.
