# Core A closed formula — exceptional, boundary and assumption register

This register accompanies the exact theorem and full proof. It records the proof-completeness clarifications as well as genuine mathematical boundary cases. It is not a register of falsely labelled failed numerical runs.

| ID | Case / risk | Exact disposition and evidence |
|---|---|---|
|EX01|s=0; gcd(0,m)|Define g=m,Q=q,r1. σ=id, E=k, im(1+σ)=0. The trace is identity. P01/P28 handle this directly. The polynomial T−T is zero, so the generic simple-root wording is explicitly not applied to it. Formula unchanged.|
|EX02|Order2 twist|Requires even m and s=m/2. E=k=F_(Q²). The contained-plane extension correction q−Q² is zero; ordinary Hermitian counts apply. No omitted limit or division.|
|EX03|Odd non-involutive order r>1|E=F_Q, but σ is not identity on k. Count isotropic points through trace hyperplanes or independent character sums. Self-dual planes alone descend to E. Irreducible base quadratics remain irreducible because r is odd.|
|EX04|Even non-involutive order r>2|E=F_(Q²), σ on E is an involution, not on all k. [k:E] can be even. The no-external-plane graph lemma, not an invalid odd-extension argument, justifies the incidence correction. q16,s1/s3 and q64,s1/s5 checks exercise this.|
|EX05|q2,m1|Outside theorem m≥2. Preserved auxiliary census and integer formulas agree, but this does not change the stated family silently.|
|EX06|Zero input and full ambient|Both have zero hull; contribute the two additional N0 cases. Minimum generators of zero is0, although zero is a principal ideal.|
|EX07|Primitive vertical residue line|Unique second-coordinate chart, residue slope0 there. It is anisotropic. It contributes to counts exactly once and is not omitted by normalization (1,a) of isotropic lines.|
|EX08|Primitive kernel I=J|Allowed: I is proper as a B-ideal but need not be strictly contained in J. Its hull has μ1. Excluding I=J would omit inputs and change L.|
|EX09|I=0 and n=1+tσ(t)|Unit→μ0; zero→μ1; pure nonzero socle→μ2; other radical→μ1. Zero n is not included in the nonzero-socle count Q²(q−Q).|
|EX10|Scalar radical ideals|0,kz,I_L,J exhaust the proper ideals. Distinct line ideals intersect in kz; they are not disjoint. No failed historical direct-sum argument is reused.|
|EX11|Radical K=0|Necessarily T=0,f=0, so W=0. There is no nonzero radical input with missing socle.|
|EX12|Radical dim K=1 and T_s=0|The socle survives, so hull μ1, not0. All f:T→V/K maps are counted. Dim T1 remains μ1 whether its layer line is isotropic or not.|
|EX13|K=V, T=0 or T=k⁴|Both give μ2 hulls (socle-only at the first endpoint and a smaller socle hull at the second). The ambient input JB² has μ4 but its same-input hull does not.|
|EX14|All μ3 hulls|Exactly W=J K+uw·k² with a σ-isotropic line K. They equal their input and dual, dimension4, μ3. Count d. No proper μ3 hull in Core A.|
|EX15|Hypothetical μ≥4 hull|Excluded by the full structural proof P12, not merely unobserved in finite tests. Larger-length moving-factor μ4 hulls in A12 are outside this theorem.|
|EX16|Projection-rank0/1 graph degeneracy|The no-external-plane lemma explicitly handles a-projection ranks0 and1 before using b=Ma at rank2. It does not assume all self-dual planes are graphs.|
|EX17|Quadratic coefficients x=0 or h+j=0|Handled separately in P25: split/zero or square, respectively. The Artin–Schreier normalization is used only when both are nonzero.|
|EX18|Contained Δ-plane|It has q+1 rank1 points after extension, not a fixed root count1/2. Its correction is C(q−|E|), with C=Q+2 or2(Q+1).|
|EX19|Division by2 in plane-type audit|These are integer finite-set cardinalities Q²(Q±1)/2, never inversion of2 in characteristic2. The main proof's base-incidence route does not require these halves.|
|EX20|False involutive double dual|Actual law is D_s²=σ_(2s). Fresh original-global q8,s1 example has slope2→6, not2. No polarity formula is applied on all k for non-involutive s.|
|EX21|Frobenius on nilpotents|Coefficient σ fixes u,w; whole-ring squaring would kill them and is a different map. The theorem and all code use coefficient Frobenius.|
|EX22|Side/slot/transpose changes|Right ideals and first-slot θ_s are fixed. Generic left-action claims or a second-slot parameter with the same s are not imported. P04 derives the actual global transport.|
|EX23|GL/isomorphism equivalence|Inputs are embedded. Counting descriptor cosets and vector subspaces is not division by an ambient GL orbit. Auxiliary graph/quotient bases are counting coordinates, not new code equivalences.|
|EX24|Column versus matrix generator numbers|Column μ1/2 both mean nonzero matrix-principal; μ3 means two matrix generators. No claim of a three-generator matrix hull.|
|EX25|Joint all-twist profile|Only each marginal distribution is closed here. Dependence of a marginal on gcd(s,m) does not identify hulls of one fixed W or provide the full joint distribution.|
|EX26|q16 numerical scope|166,521 inputs/all four twists,666,084 cases are the preserved full generic/structural census. Original-global q16 checks cover176 cases, not a full global census.|
|EX27|q32/q64 numerical scope|Only projective-point, trace-kernel and descended-plane geometry checks at specified twists. No full B² module/code census. m1…64 integer regressions are also not field censuses.|
|EX28|Proof self-containment clarification|Earlier working text referred to A11 structure. The final full proof now supplies the entire descriptor, hull, scalar-ideal and global correspondence arguments; there is no unproved dependency on a missing source.|
|EX29|s0 simple-root wording clarification|During final line audit, the generic simple-root rationale was separated from s0 explicitly. This was a proof-wording boundary clarification, not a failed formula/census case or a changed hypothesis.|
|EX30|Independent review / novelty|Separate derivations and programs are by the same agent. No independent human/referee or formal proof certificate is completed. Closest-source technical comparison, external originality and Q1 suitability remain open.|

**Numerical failures in the preserved distribution/proof-finalisation runs:** none. **Identified uncorrected mathematical assumptions necessary for the stated theorem:** none. **Unsupported extensions:** those listed above are expressly excluded, not silently assumed.

No original manuscript, historical correction register, failed Git-recovery record, source hash, old output or checkpoint a74f33f is overwritten by this register.
