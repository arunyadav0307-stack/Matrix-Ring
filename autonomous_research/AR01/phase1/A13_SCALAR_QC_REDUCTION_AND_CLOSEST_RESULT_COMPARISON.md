# A13 after proof finalisation — exact scalar QC reduction and closest-result comparison

**Starting checkpoint:** proof milestone `eef4ab6ab3461745dafadbcf4211aa79286344b6`, remotely verified with all2,196 blobs/modes and46 changed paths. This is an additional scientific comparison, not a revision of the six frozen proof-finalisation records. Same-agent alternative derivation/computation is not independent human review.

## 1. Why the scalar comparison must be made exactly

Matrix coefficients, transpose/Frobenius notation and a generator-packing factor do not by themselves create a new algebraic-coding contribution. We prove here that the **whole Core A family and actual hulls**, not just A12's diagonal witness, have a precise commutative scalar quasi-cyclic interpretation. Thus literature/depth assessment must concern that scalar problem as well. This is a conventional comparison lemma, not advertised as a new theorem or Gray/quantum application.

Keep A=k[u]/u² and B=A[X]/(X²−1), w=X+1, with k=F_(2^m),m≥2. Coefficient σ fixes u,X,w. For v=(v₁,v₂)∈B² write v_j=a_(0j)+a_(1j)X and define the fixed-coordinate A-linear bijection

ρ(v)=(a_(01),a_(02),a_(11),a_(12))∈A⁴.

Let τ swap the two blocks of size2. Then ρ(Xv)=τρ(v). In k-coordinates a B entry(c₀,c_u,c_w,c_z) becomes A entries

(c₀+c_w)+(c_u+c_z)u,  c_w+c_z u.                        (QC1)

All additions are in characteristic2; this is invertible and involves no arbitrary GL orbit or discarded nilpotent coordinate.

## 2. Exact family bijection

An embedded B-submodule W≤B² maps to an A-submodule Q=ρ(W) closed under τ. Conversely every A-linear length4 **index2 quasi-cyclic code** Q (shift by2 coordinates) is closed under multiplication by X and hence by every element of B; its inverse image is a B-submodule. The bijection is on all embedded objects, not merely free/one-generator ones.

For a cyclic right ideal C=I_W≤M₂(B), independently read its two columns in the original polynomial word. Each has image in Q, and the column independence proved using matrix units gives

C ↔ Q×Q as an A-linear space, with fixed row/column/time reordering. (QC2)

This does not assert C is a commutative ring or that a matrix-valued pairing is scalar-valued on arbitrary words.

## 3. Exact original-global dual/hull bridge, arbitrary σ

Use the scalar **A-valued**, first-slot form on A⁴

h_s(a,b)=Σ_(i=0,1)Σ_(j=1,2) σ(a_(ij))b_(ij).

For original matrix words x,y, the (p,q) entry of their actual global matrix pairing is exactly h_s applied to column p of x and column q of y. Since C contains each source column Q independently with the other column zero, all matrix entries vanish for all x∈C iff **each target column lies in Q^(⊥h_s)**. Therefore

C^(⊥s) ↔ Q^(⊥h_s)×Q^(⊥h_s),
C∩C^(⊥s) ↔ (Q∩Q^(⊥h_s))×(Q∩Q^(⊥h_s)).               (QC3)

This derives the original-global result directly, without assuming σ²=id. The scalar dual is A-linear; it is τ-invariant because h_s(a,τb)=h_s(τa,b) and τQ=Q.

For completeness the B-valued description is the same one. The constant X-coefficient of Σσ(v_j(X^(−1)))y_j(X) equals h_s(ρv,ρy); its X-coefficient equals h_s(τρv,ρy). Here X^(−1)=X. Orthogonality to both v and Xv is thus equivalent to the full B-valued product being zero. Consequently

ρ(D_s(W))=Q^(⊥h_s),  ρ(H_s(W))=Q∩Q^(⊥h_s).             (QC4)

It would be wrong to assert that ρ sends the entire B-valued product to **one** scalar dot product for arbitrary v,y; the shift test is essential. No field/Gray/Euclidean/CSS/EA isometry follows.

## 4. Which generator invariant is preserved

The invariant in A13 becomes the minimum number of **QC polynomial-module generators**, not the minimum number of A-linear generators or a free rank. If H_Q=Q∩Q^(⊥h_s), the exact identity is

μ_B(H_s(W))=dim_k H_Q/[uH_Q+(τ+1)H_Q].                  (QC5)

Indeed u and τ+1 are respectively multiplication by u,w in the local algebra B, and nilpotent Nakayama gives the minimum generator number. The matrix right ideal still has ceil(μ_B/2) generators because each matrix packs two columns. This ceil conversion is standard packing, not a new noncommutative invariant.

Thus **the complete A13 distribution is equally a scalar A-linear, length4/index2 QC hull-module-generator distribution for all m,s**. The correct originality comparison is not restricted to papers titled “matrix rings.”

The family is genuinely all-generator: for example W=JB² has μ_B(W)=4. One-generator scalar QC formulas cannot simply be asserted to exhaust it. Conversely that observation is not proof that a source's methods/corollaries do not already yield the result.

## 5. Fresh executed check of this comparison lemma

`audit_core_a_scalar_qc.py scalar_qc_v1`: **PASS**. The new driver constructs Q from the fixed-coordinate map and the actions u,τ, imposes both coefficients of the A-valued scalar form directly, and computes full scalar QC dual/hull spaces. It imports no primary field/module/descriptor/hull code. It reuses the alternative field tables/row restriction and the original-global checker, so it is a separate route by the same agent, not wholly dependency-independent software or human review.

- All2,442 q4 inputs/twists and176 saved q16 cases: scalar QC hull spaces agree with saved primary hull spaces and the original-global route. All176 exported q16 primary dual spaces also agree. q16 is a subset, not a full global/QC census.
- Inputs, duals and hulls are checked for u and QC-shift closure. Formula(QC5) agrees in every case.
-1,152 basis/scalar/twist checks at q4/q8/q16 verify both the constant and shift coefficients of the product.
- q4 histograms are(258,522,440,1) and(130,538,550,3).
- Full basis-stream SHA-256(hash only): `c64cfd97e5aeb0c14a78e7d56d61a3255974b679f89e4f0d52053baaba4d0f39`.
- Driver SHA-256: `2848bd2d0f2d3a393c566aa15ae4ca9249d2eece31e146260ab977189a40b38c`.

The proof above, not finite agreement, supplies the all-parameter bridge. It changes no A13 formula/hypothesis or earlier result hash.

## 6. Theorem-level scalar coding crosswalk

The available source scopes are those in `PRIMARY_SOURCE_READING_NOTES.md`; this table does not invent missing full texts.

|Closest lane|Exact positive connection established now|What an originality comparison still must establish|
|---|---|---|
|S01/NL10: scalar cyclic repeated-root hulls over A, length2N with N odd|Its N1 algebra is B, so its scalar cyclic objects are ideals of B, i.e. polynomial-module rank1. A12's scalar reduction and A13's scalar ideal/annihilator constituents are directly in that occupied territory.|Read full component tables/proofs and any QC/module generalizations. A13's arbitrary W≤B² are index2 QC over A, not merely the coordinate direct sums of two B ideals. This is a distinction of objects, not a noncoverage/novelty verdict.|
|S09: one-generator QC over the same nonchain ring B|If its block-length1 specialization is permitted, the polynomial coefficient quotient becomes B itself and its one-generator rank2 modules are exactly the μ_B≤1 subset of W≤B². Check its form and Frobenius action rather than relying on the ring name.|Full text must verify this specialization and compare generator-module number versus a spanning-set size/freeness statistic. Matrix-principal inputs include μ_B2, not just scalar one-generator μ_B1; A13 also counts μ3/4 inputs. Its all-generator consequences and the actual pairing are not yet read.|
|General QC/MT Galois generator matrices, S02/S03|Generic dual/intersection computation and rank methods are existing infrastructure. QC reformulation reinforces that a new “matrix hull algorithm” claim would be inappropriate.|Their inspected field hypotheses do not automatically cover A-valued nilpotent scalar forms. Check exact compatible constants, slot/inverse-twist conventions and any enumerative consequences before claiming a distinct closed histogram.|
|Artinian invariants/duality, S05|μ as a top-dimension/Nakayama invariant is established infrastructure, and(QC5) is its ordinary application.|Compare actual all-generator embedded enumeration, not a renamed μ/type/free-rank invariant. No unrestricted field/chain/Frobenius theorem import.|
|S10 matrix-ring predecessor|Matrix-column/CRT/principal-generation background is prior occupied territory; the matrix packaging itself is not a contribution.|Its coprime-length/field/form hypotheses still require exact comparison. QC equivalence is not permission to discard its conditions or fill unread erratum details.|

A simple example explains the limit of a *direct-sum-only* import: B(1,1) projects onto B in each coordinate but is not B⊕B. Coupled descriptors cannot be counted by only pairing scalar ideal lists in the fixed coordinates. This disproves that naive reduction, not the possibility that established QC or geometric methods already yield A13.

## 7. Geometry crosswalk — positive known ingredients, not unproved absence

Two additional **third-party mirrored** texts were actually read in bounded portions. Their immutable Git blobs/SHA-256, line ranges and lack of primary/final authentication are in `../evidence/M6_SOURCE_READING_SCOPE.json`.

**M6G1:** header names Bamberg/Bishnoi/Ihringer/Ravi, *New bounds and constructions for large partial m-ovoids and related structures*. Lines276–340 explicitly assume a **reflexive** form and give the classical point/generator products. Substituting rank2, type1 over F_Q gives (Q+1)(Q²+1) symplectic Lagrangians. Type1/2 over F_(Q²) gives (Q+1)(Q³+1) Hermitian generators. These are exactly P22's plane totals, not new A13 geometric constants. This source does not justify applying a polarity to Ω_s on k when σ is non-involutive; P21 first descends its self-dual planes to E.

**M6G2:** header names Subrata Manna, *Functional codes arising from rank n Hermitian varieties and hypersurfaces in low dimensions*. The inspected preliminaries label the Hermitian point counts and line sections as established, and attribute them to Bose–Chakravarti/Chakravarti. Its displayed point formula at projective dimension3 is (Q³+1)(Q²+1), exactly P22's Hermitian point count. The actual form is involutive on F_(Q²); the nilpotent/QC/hull problem is not its stated object. The generic line–Hermitian intersection statement does **not**, without more work, give P25's particular Hermitian-generator-line versus Segre-quadric root restriction: those are different intersection questions.

M6G2's introduction and bibliography provide much closer **unread primary leads**: Bartoli–De Boeck–Fanali–Storme, *On the functional codes defined by quadrics and Hermitian varieties* (reference metadata says DCC71(2014),21–46); Edoukou's 2007 degree2 Hermitian-surface paper and 2009 weight-distribution paper; and Bose–Chakravarti1966. These are secondary-reference locators only, not authenticated/read primary results. The exact intersection/relative-polarity tables and any arbitrary-Frobenius extension must be obtained/compared before calling U,F or their ingredients new.

For example A13's base rank1 isotropic point count at E=F_(Q²) is

(Q+1)(2Q²−Q+1)=2Q³+Q²+1.

This is literally the cardinality of the particular Hermitian-surface/Segre-quadric intersection, so the functional-code intersection literature is a real technical comparison obligation. Total point intersection does not by itself give the full contained/tangent/secant line incidence, but cannot be dismissed as irrelevant.

## 8. Updated scientific decision

1. **Do not market matrix-ring packaging as novelty.** The exact same hull enumeration is scalar QC in(QC1)–(QC5). The original-global proof remains essential for correctness, but correct transport is not automatically an original main result.
2. **Retain A11+A13 as proved research output, not yet a selected original/Q1 paper.** The potential contribution is the exact all-input scalar QC aggregation and its arbitrary-Frobenius geometry, if a complete comparison leaves a sufficiently deep differentiated result. Classical plane products/μ/rank/CRT ingredients are not claimed new.
3. A12 alone remains rejected as sufficient, and the impossible Core A principal-input counterexample search remains closed. No forced quantum section, cosmetic higher parameters or new invariant name repairs originality.
4. Essential source evidence remains unavailable: complete S01/S09/version comparison and exact primary geometry tables. Allowed-host DOI/title/refinement searches yielded either zero or unrelated/mirror leads; neither outcome is evidence of novelty. No off-host bypass, Drive access, external contact or payment occurred.
5. The next comparison targets are specific, not an approval request: acquire authentic complete scalar QC/repeated-root statements and the cited Hermitian/quadric intersection tables, translate(QC1)–(QC5) and P19–P26 into their conventions, then decide known/routine/distinct-and-deep. No positive outcome is promised; no-paper remains legitimate.
