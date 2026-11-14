# A13 — closed marginal distribution of Core A hull generator numbers

**Mathematical working proof, not an external originality or publication claim.** This retains exactly Core A, rather than changing nilpotency, matrix rank, side, form or equivalence. Its formulas count embedded inputs for one twist; they do **not** give the full joint distribution of all twists on the same input. Execution and internal audit are separate records; no numerical result is claimed merely by writing this note.

## 1. Contract and statement

Let k=F_q, q=2^m, m≥2, B=k[u,w]/(u²,w²), z=uw, J=(u,w), V=k². For each embedded B-submodule W≤B² use the actual first-slot form β_s(v,y)=Σσ_s(v_i)y_i and H_s(W)=W∩D_s(W), 0≤s<m. The corresponding length2 matrix-ring cyclic code is the right-column ideal I_W, as proved in the foundations. Let

N_j(q,s)=#{W≤B²: μ_B(H_s(W))=j}.

These are column-module generator numbers. Matrix right-ideal generator numbers are ceil(j/2); j=1 and j=2 both mean a nonzero principal matrix ideal.

Put g=gcd(s,m) (so g=m at s=0), Q=2^g, r=m/g and

d=1 if r is odd, and d=Q+1 if r is even.

Then d=gcd(2^s+1,q−1), as already proved for the exceptional residue lines. Define

C = Q²                              if r is odd,
C = Q(Q²−Q+1)                       if r is even,

U = q²+q+1+qC − [(q+1)(Q+1)+d(q−Q)],                    (D1)

B_inc = q(Q³+Q²−1)−Q²               if r is odd,
B_inc = (Q²−1)[q(Q²+Q+1)−Q²]        if r is even.          (D2)

Here B_inc is an integer incidence count, **not the coefficient ring B**. Finally set A₀=(q+1)(2q²+q+1) and L(q)=2q⁴+8q³+10q²+7q+9.

**Theorem (closed marginal distribution).**

N₀=(q+1−d)q³+2,
N₁=2A₀+d[q³−2q²−Q²(q−Q)]+(q+3)U−B_inc,
N₃=d,
N₂=L(q)−N₀−N₁−N₃,
N_j=0 for j≥4.                                           (D3)

In particular the marginal histogram depends on s only through gcd(s,m), not its particular exponent class. This does not identify individual embedded hulls under different twists. The μ0/μ3/total formulas are the earlier A11 results; the development here is the complete μ1 count and hence μ2 count, including arbitrary non-involutive σ_s.

## 2. Structural reduction to one incidence problem

Use the unique descriptors and exact hull formulas in `CORE_A_EMBEDDED_STRUCTURE.md`.

### 2.1 Primitive inputs

For a residue-rank-one module W=B(1,t)+(0,I) in its deterministic chart, the previous scalar-ideal table gives μ(H)=1 except for the listed μ0/μ2 cases. Sum the nonzero-kernel-ideal contributions over all q+1 residue lines: the total is

A₀=(q+1)[q²+(q+1)q+1].

Among these, exactly d q² (I=kz with isotropic residue) have μ2 instead of μ1.

For I=0, only the d isotropic residue lines give a nonzero hull. Normalize their slope to a with aσ(a)=1, and write

t=a(1+xu+yw+hz),       x,y,h∈k.

Multiplication gives n=1+tσ(t) with coefficients

n_u=x+σ(x),  n_w=y+σ(y),
n_z=h+σ(h)+xσ(y)+yσ(x).

The hull has μ2 exactly when n∈k×z. This requires x,y in the fixed field F_Q; then the cross term is zero, and h must be outside F_Q. Thus there are Q²(q−Q) such lifts per isotropic residue line. The remaining q³−Q²(q−Q) lifts have μ1. The vertical chart is anisotropic and contributes no omitted isotropic residue. Consequently

N₁^(primitive)=A₀+d[q³−q²−Q²(q−Q)].                     (D4)

This uses actual coordinates/norms, not an active GL change of the form.

### 2.2 Radical inputs with dim K≤1

For K=0 there is only the zero module. If K is a line, T≤K⊕K and the lifting maps have q^(dim T) choices. For dim T=0,1 the hull has μ1, regardless of whether the restricted layer line is isotropic: the surviving zK supplies one generator and the projection formula gives no second generator. For dim T=2, the hull has μ2 if K is σ-isotropic, and μ1 otherwise. There are d isotropic K and q+1−d anisotropic K. Hence

N₁^(K line)=(q+1)(1+q(q+1)+q²)−d q²=A₀−d q².            (D5)

### 2.3 Radical inputs with K=V

Here f=0 and every field subspace T≤V⊕V corresponds to exactly one input. The layer form is

Ω_s((a,b),(c,e))=σ(a)·e+σ(b)·c.

Let T_s=T∩D_s^Ω(T), h=dim T_s and p=dim(π₁T_s+π₂T_s). Then μ(H)=2+h−p. Nonsingularity gives h≤2. The only way to obtain μ1 is

h=1 and p=2.                                             (D6)

Let U be the number of projective lines ℓ=k(a,b) with Ω_s(ℓ,ℓ)=0 and a,b linearly independent in k². Fix such an ℓ. The condition ℓ⊂T_s is equivalent to

ℓ⊂T⊂A_ℓ,   A_ℓ={x:Ω_s(x,ℓ)=0}, dim A_ℓ=3.

There is one such T of dimension1, one of dimension3 and q+1 of dimension2. At dimensions1 and3 the right radical is exactly ℓ. A dimension2 T fails (D6) precisely when it is totally self-orthogonal, hence self-dual; otherwise T_s=ℓ and is counted exactly once. Let B_inc count pairs (ℓ,T) where T is a self-dual two-plane and ℓ⊂T has projection rank2. Therefore

N₁^(K=V)=(q+3)U−B_inc.                                 (D7)

This right-radical incidence argument does **not** assume Ω_s is alternating, Hermitian or reflexive for general s. Adding (D4),(D5),(D7), then the previous N₀/N₃/total results, proves (D3) once (D1),(D2) are established.

## 3. Counting isotropic projection-rank-two lines U

### 3.1 All Ω_s-isotropic projective points by additive characters

Let ψ be a nontrivial additive character of k, obtained from the absolute field trace. For c∈k, the character sum of one coordinate pair is

S_c=Σ_(x,y∈k) ψ(c[σ(x)y+σ(y)x])
   =q·|ker L_c|,
L_c(x)=cσ(x)+σ^(−1)(cx).

The second equality follows by moving σ on y through the trace and summing the resulting linear character in y. Thus the number of isotropic vectors in k⁴ is

q^(−1)[q⁴+q²Σ_(c≠0)|ker L_c|²].                         (D8)

For c≠0, applying σ to L_c(x)=0 gives

σ²(x)/x=c/σ(c) for x≠0.

The fixed field of σ² has size Q when r is odd and Q² when r is even. The cyclic multiplicative group shows that σ²(x)/x takes exactly the elements of norm1 to this fixed field: its image and that norm kernel have the same size. Hence a nonzero solution exists exactly when the norm of c/σ(c) is1; the nonzero solutions form a coset of the fixed field's multiplicative group.

- If r is odd, σ acts trivially on F_Q, so this norm condition holds for every c≠0; |ker L_c|=Q.
- If r is even, let t=Norm_(k/F_(Q²))(c). The norm condition is t=t^Q. The norm map is surjective on nonzero elements. Exactly (q−1)/(Q+1) values of c have t∈F_Q× and kernel size Q²; all other c have kernel size1 (only zero).

In the odd case Σ|ker|²=(q−1)Q². In the even case it is

(q−1)(Q⁴+Q)/(Q+1)=(q−1)Q(Q²−Q+1).

Subtract the zero vector in (D8) and divide by q−1. The total number of isotropic projective points is therefore

I=q²+q+1+qC.                                             (D9)

At s=0, Q=q and this is every projective point, as required. No unjustified Hermitian point formula is imported for non-involutive twists.

### 3.2 Remove the projection-rank-one points

Such a nonzero (a,b) is uniquely specified by a line K=kl≤k² and a coefficient line k(α,β)≤k², via (a,b)=(αl,βl). Its self-pairing is

[σ(l)·l][σ(α)β+σ(β)α].

For each of the d isotropic K every coefficient line works: q+1 choices. For an anisotropic K, the coefficient ratio must lie in F_Q, including the vertical line: Q+1 choices. Hence the removed count is

d(q+1)+(q+1−d)(Q+1)=(q+1)(Q+1)+d(q−Q).

Subtracting from (D9) proves (D1).

## 4. Self-dual plane descent and the incidence count B_inc

View v=(a₁,a₂,b₁,b₂) as a two-by-two matrix with columns a,b. Projection rank1 is exactly the fixed hyperbolic quadric

Δ(v)=a₁b₂+a₂b₁=0.

Let S exchange the two entries of k² and L=diag(S,S) on k⁴. The polar form of Δ is Ω₀(Lv,t). Also D_s^Ω²(T)=σ²(T), by the same first-slot dual calculation as in the foundations. Thus every self-dual two-plane is fixed by σ². Its canonical reduced row space has entries in the fixed field E of σ² (apply σ² and use uniqueness of reduced rows), and it is the scalar extension of a unique E-plane.

- If r is odd, E=F_Q and σ restricts to identity: the descended plane is a Lagrangian for the alternating form Ω₀ on F_Q⁴.
- If r is even, E=F_(Q²) and σ restricts to its nontrivial involution: the descended plane is a totally isotropic plane for the nondegenerate Hermitian form Ω_Q on E⁴.

Conversely extending any such descended plane gives a self-dual k-plane, by direct testing of its basis and the dimension2 complement. This is an exact bijection, not an assumption of involutivity on all of k.

For a descended plane, Δ restricts to a binary quadratic form. Its number of projective roots is q+1 (identically zero),1 (nonzero zero-polar form),2 (split nonzero polar), or0 (irreducible). The resulting numbers of projection-rank-two points are 0,q,q−1,q+1 respectively.

### 4.1 Odd-order descent: symplectic planes over F_Q

There are (Q+1)(Q²+1) Lagrangian two-planes. One elementary count: every projective point of F_Q⁴ is isotropic; through each is Q+1 Lagrangians (the two-dimensional alternating quotient); each plane contains Q+1 points.

**Contained planes.** A two-dimensional space consisting only of rank≤1 two-by-two matrices has a common image line or a common coefficient/kernel line. Otherwise the sum of two rank-one matrices with independent image and coefficient directions would have rank2. The common-image planes are K⊕K and are Ω₀-isotropic exactly when l·l=0: there is one such K, k(1,1). Every common-coefficient plane {(αl,βl):l∈F_Q²} is Ω₀-isotropic: Q+1 choices. Thus the contained count is Q+2.

**Zero-polar planes.** On a Lagrangian T, the polar restriction of Δ vanishes iff L(T)=T. Put N=L+I; then N²=0 and im N=ker N=E₀={(αh,βh):h=(1,1)}. If T=E₀ there is one. Otherwise T∩E₀=M is a line, N(T)=M, and T/M is a line of N^(−1)(M)/M outside E₀/M. There are Q choices for each of the Q+1 lines M. All are Lagrangian: if Nv is a scalar multiple of e=(αh,βh), then Ω₀(e,v)=α(b₁+b₂)+β(a₁+a₂)=0; self-pairings vanish automatically. Hence there are Q²+Q+1 zero-polar planes. Removing the Q+2 contained ones gives Q²−1 tangent planes.

**Secant and external planes.** There are (Q+1)² rank-one projective points, each incident with Q+1 Lagrangians. Count these incidences using contained/tangent/secant contributions. One obtains secants Q²(Q+1)/2 and external planes Q²(Q−1)/2. Their sum is the remaining Q³ planes. Since [k:F_Q]=r is odd, an irreducible quadratic over F_Q stays irreducible over k; no extra roots are introduced.

Thus

B_inc=(Q²−1)q+[Q²(Q+1)/2](q−1)+[Q²(Q−1)/2](q+1)
     =q(Q³+Q²−1)−Q².

### 4.2 Even-order descent: Hermitian planes over F_(Q²)

There are (Q+1)(Q³+1) self-dual planes. For completeness the Hermitian isotropic point count is (Q³+1)(Q²+1), either from §3 with q=Q² or a norm count. Through each isotropic point there are Q+1 such planes: pass to its nondegenerate two-dimensional Hermitian quotient; a split basis gives coefficient ratios in F_Q plus the vertical line. A two-dimensional nondegenerate finite-field Hermitian form has an isotropic line by surjectivity of the norm map (a nondegenerate anisotropic one-dimensional summand can be paired with its orthogonal complement); it admits such a split basis. Dividing point-plane incidences by Q²+1 gives the displayed plane count.

**Contained planes.** The common-image planes require σ(l)·l=0, giving Q+1 choices by the norm equation. The common-coefficient planes require σ(α)β+σ(β)α=0, also Q+1 choices. Thus there are 2(Q+1) contained planes.

**Zero-polar planes.** A Hermitian self-dual T has D₀(T)=σ(T). Thus zero polar restriction is equivalent to L(T)=σ(T), or invariance under the semilinear involution τ=Lσ. Its fixed vector space is explicitly

U_τ={((x,x^Q),(y,y^Q)):x,y∈F_(Q²)}.

It is four-dimensional over F_Q and spans E⁴. On it Ω_Q(v,t)=Ω₀(Lv,t), an F_Q-valued nondegenerate alternating form. For example this is the sum of the two field-trace pairings, which is nondegenerate. A τ-stable E-plane descends to a two-dimensional F_Q-plane in U_τ; choosing any element of E\F_Q gives the elementary real/imaginary-coordinate descent, so the fixed part has the asserted dimension. Its isotropy is exactly the alternating isotropy there. Therefore zero-polar self-dual planes are in bijection with the (Q+1)(Q²+1) Lagrangians over F_Q. Removing contained ones leaves (Q+1)(Q²−1) tangent planes.

**No external planes.** The number of Hermitian-isotropic rank-one points over E is (Q+1)(2Q²−Q+1), from §3.2 at q=Q². Each lies on Q+1 self-dual planes. Subtract the incidences from 2(Q+1) contained planes (each with Q²+1 points) and (Q+1)(Q²−1) tangent planes (one point each). The remainder divided by2 is Q²(Q²−1), exactly the total number of nonzero-polar planes still unclassified. Therefore all of them are secants; none is external. All their roots are already over E, so extension to k adds no roots.

Consequently

B_inc=(Q+1)(Q²−1)q+Q²(Q²−1)(q−1)
     =(Q²−1)[q(Q²+Q+1)−Q²].

This proves (D2), then (D3). ∎

## 5. Checks, consequences and boundaries

At s=0 the formula simplifies to

N₁=7q³+4q²+2q+2,
N₂=q⁴+q³+6q²+5q+4,
N₀=q⁴+2, N₃=1.

The q4/q8 predictions agree algebraically with the preserved census tables. Predicted q16 histograms, in j=0,1,2,3 order, are

- s0: (65538,29730,71252,1),
- s1,s3: (57346,33490,75682,3),
- s2: (49154,48386,68976,5).

These q16 values are **predictions until fresh execution is recorded elsewhere**. Numerical testing must separately inspect U, plane intersection types, B_inc and μ1 input strata, not only the final total, and exercise non-involutive even/odd orders. Old q16 named-family coverage is not retrospectively an exhaustive census.

The fixed-field trace/plane/quadric counts are substantive additional obligations beyond the generic descriptor rank formula, but use standard finite geometry and descent. Their external novelty and sufficient paper depth still require exact primary-source comparison. No joint same-input all-twist count, arbitrary rank/nilpotency theorem, quantum/metric bridge, human review, journal suitability or submission readiness is asserted.

## 6. Proof-completeness addendum and actual execution at M5

To make the characteristic-two descent in §4.2 explicit, choose α∈E=F_(Q²) with α+α^Q=1; any element outside F_Q can be rescaled by its nonzero trace to do this. For any v in a τ-stable E-space T, both

u=v+τ(v),       h=(α+1)v+ατ(v)

are τ-fixed, lie in T, and v=h+αu. Thus the fixed vectors span T over E. Any F_Q-linearly independent fixed vectors are also E-linearly independent: split a supposed E-relation into coefficients in F_Q+αF_Q and subtract its τ-image; since α+α^Q=1, both F_Q-relations must vanish. Therefore dim_(F_Q) T^τ=dim_E T, and extension/restriction are inverse. This supplies the claimed dimension2 fixed plane without dividing by2 or assuming diagonalizability of the swapping operator. The explicit vectors ((x,x^Q),(y,y^Q)) span all of E⁴: in each pair, (1,1) and (α,α^Q) have determinant α+α^Q=1.

Also, the two-dimensional Hermitian quotient count in §4.2 can be verified without importing a classification theorem. A nondegenerate Hermitian form with nontrivial field involution has some v with H(v,v)≠0. Otherwise expansion of H(x+y,x+y) would force H(x,y) into F_Q for all x,y, while scaling x by an element outside F_Q forces H(x,y)=0, contradicting nondegeneracy. Orthogonal splitting then gives a diagonal basis with entries a,b∈F_Q×. Surjectivity of t↦t^(Q+1) gives exactly Q+1 solutions of a+b t^(Q+1)=0. Hence there are Q+1 isotropic lines. The diagonal or split basis is used only to count this auxiliary quotient, not to change the original embedded code/form.

**Fresh execution now recorded:** `distribution_v1` actually exhausts all166,521 q16 inputs/all four twists (666,084 full generic-vs-structural hull-space comparisons). All four histograms in §5 and all three μ1 descriptor-stratum counts match. `distribution_audit_v1` separately exhausts all layer subspaces at q4/q8/q16 (334,413 field/twist/subspace cases), checks all isotropic-point/quadric-plane/incidence formulas, and verifies176 selected q16 inputs with the original global matrix pairing. Additional q32/q64 checks enumerate points and descended planes only, not all B² modules or all twists. See `../audits/CORE_A_DISTRIBUTION_AUDIT.md` for exact coverage and limitations. The universal conclusion rests on the proof; finite checks do not establish external originality or independent human review.
