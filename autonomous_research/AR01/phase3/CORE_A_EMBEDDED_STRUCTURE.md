# Core A — embedded descriptors, hull profiles and the exact nonprincipal boundary

**New AR01 mathematical working note. Complete proofs below; execution and explicit audit status belong to separate records. No external originality, paper-sized novelty, Q1 suitability or independent human review is asserted.** This strengthens the bounded preservation result without changing the ring, side, slot or equivalence. The old notes/blueprint/manuscript remain historical originals.

Throughout k=F_(2^m), m≥2, B=k[u,w]/(u²,w²), z=uw, J=(u,w), V=k², σ=σ_s, 0≤s<m. A code is the right ideal I_W of M₂(B) with columns in the same embedded B-submodule W≤B². Use the actual first-slot form β_s(v,y)=Σσ(v_i)y_i and H_s(W)=W∩D_s(W) derived from the global cyclic-code pairing in `../phase2/CORE_A_FOUNDATIONS.md`. V carries its fixed-coordinate dot product; this is used only in the explicitly derived layer form below, not as a replacement for β_s on B².

## 1. Scalar ideals — full elementary list

The ideals of B are exactly

- 0, kz, B and J;
- I_L = k(a u+b w)+kz for each line L=k(a,b) in k².

There are q+1 choices of L, hence q+5 ideals. In particular I_L=B(a u+b w): multiplying by u or w supplies z. To prove completeness, a proper ideal is contained in J. If it is not contained in kz, one of its elements a u+b w+c z has (a,b)≠0; multiplication by u,w gives z, so its image in J/kz is a nonzero subspace of k² and determines the ideal. That subspace is a line or all of k². Conversely each displayed subspace is stable under u,w.

Every I_L is principal with μ=1; μ(kz)=1, μ(J)=2. Direct multiplication also gives

Ann(z)=J,  Ann(J)=kz,  Ann(I_L)=I_L.

Coefficient Frobenius sends I_L to I_(σL), and fixes J,kz. These are scalar-ring statements, not a classification of B² modules up to isomorphism.

## 2. Unique embedded descriptor for radical inputs

Suppose W⊂JB². Every vector is uniquely u a+w b+z c with a,b,c∈V. Define

K={c∈V:z c∈W},
T={(a,b)∈V⊕V: u a+w b+z c∈W for some c}.

If (a,b)∈T, multiplication by w and u shows a,b∈K. Thus T≤K⊕K. For each (a,b)∈T, the coset c+K of a lift in W is unique; define the k-linear map

f:T→V/K,        f(a,b)=c+K.

Conversely any triple **(K,T,f)**, with K≤V, T≤K⊕K and f linear, reconstructs exactly one embedded module

W(K,T,f)={u a+w b+z c : (a,b)∈T, c+K=f(a,b)}.             (R1)

Closure under u,w follows because their images are z b,z a with a,b∈K; k-linearity is immediate. The extracted K,T,f recover the original triple. Hence this is a bijective embedded descriptor, **not an ambient GL quotient or a minimal isomorphism invariant**. No splitting of V/K is part of its intrinsic definition. A chosen quotient representative is only a computational presentation.

For A≤V⊕V let P(A)=π₁(A)+π₂(A)≤V. Multiplication directly yields

JW=z P(T),     dim_k W=dim T+dim K,
μ_B(W)=dim T+dim K−dim P(T).                             (R2)

The lifting map f is needed to reconstruct W, even though it will not affect its hull generator number.

### The induced form and every twist at once

For v=u a+w b+z c and y=u a′+w b′+z c′, the exact B-valued product is

β_s(v,y)=z Ω_s((a,b),(a′,b′)),
Ω_s((a,b),(a′,b′))=σ(a)·b′+σ(b)·a′.                    (R3)

The c,c′ terms vanish because J³=0. Ω_s is the nondegenerate first-slot σ-sesquilinear form with fixed Gram matrix [[0,I₂],[I₂,0]]. It is alternating for s=0, but **not assumed alternating, Hermitian or involutive for arbitrary s**.

Put

T_s={t∈T:Ω_s(x,t)=0 for every x∈T}=T∩D_s^Ω(T).

Equation (R3), including all socle elements of W, proves the exact embedded reconstruction

H_s(W)=W(K,T_s,f|_(T_s)).                               (R4)

In particular

dim_k H_s(W)=dim T_s+dim K,
μ_B(H_s(W))=dim T_s+dim K−dim P(T_s).                   (R5)

This is not just μ=dim H−dim JH after a generic 8-coordinate hull calculation: it identifies which layer form to restrict, proves that the same K survives, and proves that **all lifting maps f give the same simultaneous generator profile for fixed embedded K,T**. Nevertheless the field intersection/rank computation itself is routine and not claimed as a novel algorithm. The formula need not classify all possible T profiles in closed scalar terms.

## 3. Unique graph/ideal descriptor for nonradical inputs

Let ρ:B²→V be reduction modulo J. If dim ρ(W)=2, then W=B²: W+JB²=B², and the nilpotent Nakayama argument in the foundations applied to B²/W gives equality. Its hull is zero for every s.

Otherwise ρ(W) is a line. Choose the first coordinate as projection if this line has nonzero first coordinate; only for the line k(0,1) use the second coordinate. This is a deterministic choice in the **original coordinates**, not an active change of W or pairing.

For the first-coordinate chart, W contains a primitive vector with first entry 1 (scale a unit first entry by its inverse). There is a unique ideal I≤J (proper as an ideal of B, but allowing I=J) and a unique coset t+I∈B/I such that

W=B(1,t)+(0,I)={(a,t a+i):a∈B,i∈I}.                    (P1)

Indeed I consists of the second entries of vectors in W with first entry zero; subtracting a(1,t) gives the claimed description. A second lift (1,t′) differs by (0,I), so t′−t∈I. The residue t₀ specifies the finite residue line k(1,t₀). In the second chart the formula is W=B(t,1)+(I,0), with t₀=0. All these descriptors are disjoint between charts.

The sum in (P1) is an abstract direct sum B⊕I; consequently μ(W)=1+μ(I), taking μ(0)=0. No module is declared free when I≠0. The vector (1,t) is primitive, not a declaration that W is cyclic.

### Exact hull as a scalar ideal, in the same coordinates

Define

n_s(t)=1+t σ(t),
L_s(I,t)=Ann(σ(I)) ∩ (I:n_s(t)),
(I:n)={b∈B:n b∈I}.                                    (P2)

Testing (1,t) and (0,i) in the actual β_s gives

D_s(W)={(σ(t)b,b):b∈Ann(σ(I))},
H_s(W)={(σ(t)b,b):b∈L_s(I,t)}.                          (P3)

The map b↦(σ(t)b,b) is a B-linear isomorphism from the scalar ideal L_s to the hull. For the second chart exchange the two displayed coordinates; this is an explicit symmetric calculation of the original dot sum, not a blanket GL-invariance claim. Thus dim H=dim L_s and μ(H)=μ(L_s).

**Representative independence:** replace t by t+j, j∈I. For b∈Ann(σ(I)), σ(j)b=0; hence (n_s(t+j)−n_s(t))b=σ(t)j b∈I. The ideal L_s is unchanged, and (σ(t+j)b,b)=(σ(t)b,b). The descriptor/hull formula therefore depends only on the unique coset, not a convenient lift.

### Generator-profile table without a full 8-dimensional hull

Write n=n_s(t), and n₀=1+t₀σ(t₀). With the exact scalar ideals of §1, (P2) gives:

| Kernel ideal I | μ(W) | Exact rule for μ(H_s(W)) |
|---|---:|---|
| 0 | 1 | 0 if n is a unit; 2 if n∈k×z; 1 otherwise |
| kz | 2 | 2 if n₀=0; 1 otherwise |
| I_L, dim I_L=2 | 2 | always 1 |
| J | 3 | always 1 |

Proof details: for I=0, L_s=Ann(n). A nonzero n∈J\kz has annihilator I_(k(n_u,n_w)); n∈k×z has annihilator J; n=0 has annihilator B. If n is a unit its annihilator is zero. For I=kz, Ann(σI)=J; if n₀≠0 then L_s=kz, while if n∈J then nJ⊂kz and L_s=J. For I=I_L, Ann(σI)=I_(σL); a unit n gives L_s=I_L∩I_(σL), either that two-dimensional principal ideal or kz, and a radical n gives L_s=I_(σL). For I=J, L_s=kz. In every nonzero-I case the hull is nonzero, with no freeness assumption.

Sections 2–3 and the whole-ambient case cover **every embedded W**. They yield a deterministic simultaneous generator-profile prescription, not a claim of a scalar closed enumeration of every field-subspace profile or minimal descriptor.

## 4. Exact classification of every nonprincipal hull

**Theorem (bounded Core A obstruction).** For every W≤B² and every allowed s,

μ_B(H_s(W))>2

holds if and only if

W=J L+zV  for a line L≤V with Σ_(i=1)^2 σ(l_i)l_i=0 for l∈L.    (N1)

In that event W=H_s(W)=D_s(W), dim_k W=4 and μ_B(W)=μ_B(H_s(W))=3. In particular **every proper hull in Core A is principal**, even when its input is nonprincipal. The only nonprincipal hulls are specified nonprincipal self-dual inputs; no hull has μ≥4.

### Proof

A nonradical input has μ(H)≤2 by the scalar-ideal description (or the primitive-vector argument in the preservation note). Suppose W⊂JB² and use (K,T,f). If dim K≤1, then T≤K⊕K has dimension at most 2. If T_s=0, (R5) is at most 1. Otherwise dim P(T_s)≥1, so (R5) is at most dim T_s≤2.

Let dim K=2, so K=V and f=0. By nonsingularity of Ω_s, dim D_s^Ω(T)=4−dim T. Hence

dim T_s≤min(dim T,4−dim T)≤2.

If dim T_s=0, (R5) gives 2. If dim T_s=1, its projection sum has dimension at least 1, again giving at most 2. To exceed 2 we must have dim T_s=2, which forces dim T=2 and T_s=T, and dim P(T)=1. Write L=P(T). Since T≤L⊕L and both have dimension 2, T=L⊕L. Formula (R1) now gives W=J L+zV and μ(W)=3.

For a nonzero l∈L, the restriction of Ω_s to L⊕L is

Ω_s((a l,b l),(c l,d l))=[σ(l)·l][σ(a)d+σ(b)c].

It vanishes identically exactly when σ(l)·l=0 (test a=d=1,b=c=0). This is precisely (N1), and (R4) then gives H_s(W)=W. The foundations give dim D_s(W)=8−4=4, so self-orthogonality and equal dimensions imply D_s(W)=W. The converse and μ=3 follow from the same equations. ∎

The original principal-input preservation theorem is an immediate consequence, but its shorter direct proof remains independently useful. The known W_* in that note is L=k(1,1), not a newly discovered witness. The old q4 exceptional counts 1 and 3 agree with the theorem; prior proper nonprincipal hulls at **n=4**, not this n=2 ring, do not contradict it or extend this result.

### Number and same-input twist support

Neither coordinate of an isotropic l can be zero. Normalize L=k(1,a), a∈k×. Its condition is

a^(2^s+1)=1.                                            (N2)

There are exactly

d_s=gcd(2^s+1,q−1)                                      (N3)

such lines, because k× is cyclic; different lines give different embedded W through their first radical layers. Thus exactly d_s input modules/cyclic right ideals have a nonprincipal s-hull.

For g=gcd(s,m), interpreting g=m when s=0, this is 1 when m/g is odd and 2^g+1 when m/g is even. To see it directly, (N2) implies σ(a)=a⁻¹ and σ²(a)=a, so a lies in F_(2^g) if m/g is odd, or F_(2^(2g)) if m/g is even. In the first case σ is identity there, giving a²=1 and a=1. In the second σ is its nontrivial involution, and the norm-one kernel in its cyclic multiplicative group has size 2^g+1. The s=0 formula is also 1.

For the **same W_a=J(1,a)+zV**, its nonprincipal-twist support is exactly {s:a^(2^s+1)=1}. If a=1 this is every twist. If a≠1 has minimal field degree h over F₂, it can occur only if h is even and a^(2^(h/2)+1)=1; when that holds the support is exactly s≡h/2 mod h in 0≤s<m. Proof: Frobenius exponents fixing a are the multiples of h; inversion of a by a Frobenius element has order exactly two, so its unique exponent class is h/2. This makes dependence on the **same embedded line** explicit, rather than replacing it by an isomorphic module between twists.

## 5. Complete count of embedded input modules and an LCD corollary

These are enumerative consequences of the descriptor; no external firstness is claimed.

For radical inputs, sum over dim K=0,1,2:

- K=0: one zero module;
- dim K=1: q+1 choices of K; in K⊕K the dimensions of T are 0,1,2, with respectively 1,q+1,1 subspaces and q^(dim T) choices of f:T→V/K. Contribution (q+1)(1+q(q+1)+q²);
- K=V: f=0; every subspace of V⊕V occurs. The total number is 1+2(q³+q²+q+1)+(q²+1)(q²+q+1)+1 = q⁴+3q³+4q²+3q+5. Here the middle Grassmannian count follows by counting ordered independent pairs and dividing by (q²−1)(q²−q).

Therefore the radical count is q⁴+5q³+7q²+5q+7.

For residue-rank-one modules, a fixed residue line has q^(3−dim I) choices of t+I for each ideal I≤J. The list in §1 gives

Σ_(I≤J) q^(3−dim I)=q³+q²+(q+1)q+1=q³+2q²+q+1.

Multiply by q+1 residue lines, then add the one residue-rank-two module B². In total

**# {W≤B²}=2q⁴+8q³+10q²+7q+9.**                         (E1)

This is an embedded count, not a Morita-isomorphism count. It gives 159 at auxiliary q2, 1,221 at q4, 12,993 at q8 and 166,521 at q16. Numerical agreement or a small-field census does not replace the descriptor/counting proof.

The number with H_s(W)=0 is

**(q+1−d_s)q³+2.**                                      (E2)

Indeed a nonzero radical W has nonzero socle zK⊂H_s(W). A residue-rank-one W with I≠0 also has a nonzero hull by §3. With I=0 the hull is zero exactly when n is a unit, equivalently when the residue line is anisotropic. There are q+1−d_s such lines and q³ free-line lifts per line. Finally W=0 and W=B² each have zero hull. This is the actual s-hull-zero count, not automatically a count for a physical or unrelated Euclidean image.

At q4 this predicts zero-hull counts 258 (s=0) and 130 (s=1), and nonprincipal counts 1 and 3, respectively — already recorded in the inherited census. The all-q proof is not a claim to have newly observed those finite data.

## 6. Boundaries and contribution assessment

- The descriptor is unique in the retained coordinates; it is not a classification under arbitrary GL₂(B), a minimal invariant, a theorem over arbitrary rank/nilpotency/length, or a closed distribution of all T_s dimensions.
- Radical extension data f affect the embedded hull but not its generator profile. Nonradical profiles depend on the **actual** scalar norm and kernel ideal, not only abstract dimensions or input μ.
- The new boundary theorem is stronger than principal-input preservation: it classifies all nonprincipal hulls and excludes proper ones in the exact class. Its proof still uses small-dimensional layer geometry and elementary ideal facts. External originality and sufficient research depth must be judged against primary sources, not inferred from a new working proof or passing programs.
- No scalar Gray map, absolute trace, CSS/EA route, quantum distance/parameter or publication claim follows from these formulas alone. No old issue register is silently closed.
