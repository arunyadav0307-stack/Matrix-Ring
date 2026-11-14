# Core A — line-indexed mathematical scrutiny, review M8

**Independent-scrutiny gate: NOT ESTABLISHED.** The required filename is retained, but this is a fresh adversarial, line-by-line **same-agent** review, with alternative derivations and a new no-repository-import finite checker. It is neither a second independent researcher nor a formal verification of the complete proof. No unqualified “proved” verdict is issued under the user's present gate.

Audited [candidate statement](CORE_A_CLOSED_FORMULA_THEOREM.md): SHA-256 `3b360c24cbccbd40fc4b46c92efb6b9842c7b069758f2b5bdb24ce66028d2f7b`. Audited [full candidate derivation](CORE_A_CLOSED_FORMULA_FULL_PROOF.md): SHA-256 `44bdf307ecf4cf4297283e4b27115c3cc7078977134f6fddd0ee7ae435933a7c`, **368 lines**. The [machine obligation ledger](CORE_A_PROOF_OBLIGATIONS.json) records every block hash/dependency; headers only introduce conventions. Line coverage/hash checks are not logical proof checking. Previous M5 review/status wording is historical; the [M8 status](CORE_A_PROOF_STATUS_REPORT.md) controls current acceptance.

## 1. Every proof unit, hypotheses and challenged deduction

Every line/equation in the ranges below was reread against its definitions and stated dependencies. **I-CLEAR** means only “the supplied conventional implication was internally replayed and no unresolved mathematical step was identified”; it is not independent acceptance. The unit-level argument below is supplemented by the alternative derivations and concrete risks in §§2–5.

|Unit and exact lines|Obligation challenged and disposition|Internal result|
|---|---|---|
|P01,9–20|**Fixed fields, trace and cyclic norms.** Separate s=0 before a polynomial root argument. For positive s, gcd(2s,m) gives E. The ordinary trace polynomial has degree<q and is nonzero, including r=1; rank-nullity gives im(1+σ)=ker Tr. Multiplication proves trace-pairing nondegeneracy. Cyclic-group root/kernel counts justify every norm use.|I-CLEAR; independent review open|
|P02,21–34|**Localness, Nakayama and both packing bounds.** Explicit finite geometric inverse proves B local with radical J, not merely that J is nilpotent. Iterate M/L=J(M/L) three times. A matrix supplies at most two column generators; packing a minimal list supplies the reverse bound, also at zero.|I-CLEAR; independent review open|
|P03,35–44|**Exact family, all right ideals.** Central X and characteristic2 give M₂(B). Matrix units isolate/place columns; summing arbitrary isolated columns proves surjectivity and injectivity of the embedded correspondence. No GL quotient or principal-input assumption.|I-CLEAR; independent review open|
|P04,45–58|**Original-global dual transport.** For each arbitrary codeword test x and Xx. These test both coefficients of x†y, not just a constant. Dagger fixes w only at length2. Its (i,j) entry is the first-slot scalar B product between the source/target columns; matrix units make source columns independent.|I-CLEAR; independent review open|
|P05,59–70|**Dimension and positive double twist.** The [z] functional is explicitly auxiliary, not equal to the original global [u]trace functional. Complementary monomials make its product Gram invertible. Testing all B-multiples makes its orthogonal equal to the B-valued one. D_s=σD₀, D₀²=id and commutation imply positive σ², never id by default. The same Gram argument applies to Ω.|I-CLEAR; independent review open|
|P06,71–85|**Complete scalar ideal/annihilator table.** Every proper ideal is radical. A nonzero first radical layer forces z and determines a line/full image. au+bw generates its line ideal. A mixed-radical annihilator has zero constant, one layer equation and arbitrary socle; unit/zero/nonzero-socle cases are disjoint.|I-CLEAR; independent review open|
|P07,86–95|**Unique radical descriptor.** Closure under w/u forces respectively a,b into K. Lift differences lie exactly in zK; f is quotient-valued and linear. Converse reconstruction is u,w stable and extraction returns the data. Counting representatives does not quotient embeddings.|I-CLEAR; independent review open|
|P08,96–114|**Actual radical hull and μ.** Direct product leaves only z[σ(a)·b′+σ(b)·a′]. Socle zK is always retained. Restricting T and f is exactly membership plus all source tests. JW=zP(T) and top dimension give μ; f affects embeddings but not this value.|I-CLEAR; independent review open|
|P09,115–124|**All nonradical residue ranks.** Nakayama on B²/W forces the ambient module at residue rank2. At rank1 a unit-coordinate projection is onto; a unit in its kernel ideal would contradict residue rank1. Normalized lift differences are precisely I. The vertical chart is disjoint and not omitted.|I-CLEAR; independent review open|
|P10,125–142|**Primitive dual/colon table and lifts.** Solve β((1,t),y)=0, then every (0,i) test, then actual membership. This gives the injective B-linear ideal map in (11). Unit multiplication preserves every ideal; distinct line ideals intersect in kz. For t→t+j, σ(j)b=0 and the remaining norm difference is σ(t)jb∈I, so both L_s and the embedded hull agree.|I-CLEAR; independent review open|
|P11,143–151|**Isotropic slope count d.** Axis lines are anisotropic. aσ(a)=1 implies σ²(a)=a. On E, σ=id or Q-involution. Odd case gives a=1 in characteristic2; even case gives a norm-one kernel of size Q+1. The cyclic root count equals the stated gcd even at s=0.|I-CLEAR; independent review open|
|P12,152–163|**Only μ3 and exact exceptional inputs.** Primitive table excludes μ>2. For dimK≤1 use h≤2 and nonzero projection sum. At K=V, h≤min(t,4−t); the sole >2 case forces t=h=2 and p=1, hence T=L⊕L. Test one cross basis pairing to force isotropic L. dimW=dimD=4 promotes actual self-orthogonality to equality.|I-CLEAR; independent review open|
|P13,164–174|**All Grassmann dimensions.** Count nonzero vectors/functionals modulo q−1, and independent ordered pairs modulo ordered bases. Add dimensions0 through4 to obtain G₄; these are integer cardinalities, not field divisions.|I-CLEAR; independent review open|
|P14,175–189|**All inputs exactly once.** Sum unique K,T,f data; for a K-line each f has q^(dimT) choices. Sum slope cosets with fixed residue using q^(3−dim I) for every proper ideal including J. The full ambient is separate. Algebra gives L, not a fitted numerical total.|I-CLEAR; independent review open|
|P15,190–197|**Zero and μ3 strata.** Any nonzero radical input retains a nonzero socle. Every nonzero-I primitive hull is nonzero. I=0 is zero precisely for anisotropic residue; q³ lifts each, plus zero/full. μ3 follows from the earlier classification, not a census observation.|I-CLEAR; independent review open|
|P16,198–210|**Primitive μ1 strata.** Nonzero-I total equals A₀, with exactly d q² μ2 exceptions. Expand the actual coefficient Frobenius norm on all free isotropic lifts. Pure nonzero socle iff x,y fixed and h nonfixed; cross term vanishes in char2. n=0 is not miscounted as μ2.|I-CLEAR; independent review open|
|P17,211–218|**Radical K-line μ1 strata.** At T dimensions0/1 the socle and projection formula always give μ1, even if the line is not isotropic. At T dimension2, the restriction is a nonzero scalar times an invertible semilinear symplectic Gram, unless K is isotropic; only the latter d q² lift maps give μ2.|I-CLEAR; independent review open|
|P18,219–232|**Directed right-radical flag count.** For ℓ in the right radical every source x satisfies Ω(x,ℓ)=0. Applying σ⁻¹ gives an ordinary nonzero linear equation, so A_ℓ is a hyperplane. The 1/3-dimensional radicals must equal ℓ by dimensions. The q+1 two-plane flags have right radical ℓ unless wholly self-orthogonal; exactly the latter self-dual flags are subtracted with incidence multiplicity.|I-CLEAR; independent review open|
|P19,233–253|**Arbitrary-order point count.** Condition on a-directions. Each active coordinate has image a_iσ(a_i)T₀. Trace-pairing annihilators prove equality of scaled hyperplanes iff the scalar ratio is fixed, equivalently σ²(t)=t. Axes and a=0 are separate. Rescaling a and b together proves equal kernel size for every representative; homogeneous self-isotropy justifies projectivizing.|I-CLEAR; independent review open|
|P20,254–265|**Rank1 subtraction.** A rank1 point has a unique image line and coefficient line. Its self-pairing factors exactly. Isotropic image lines allow all q+1 coefficient directions, others only the Q+1 F_Q-rational directions, including infinity. Every nonzero point has projection rank1 or2.|I-CLEAR; independent review open|
|P21,266–271|**Self-dual planes, and only those, descend.** The actual positive double-dual law forces σ²(T)=T. The unique RREF basis then has entries fixed by σ². Its E-row space is unique. Conversely extending a totally isotropic E-two-plane gives a k-two-plane contained in its two-dimensional right dual. No involutivity on k is inferred.|I-CLEAR; independent review open|
|P22,272–287|**Plane totals, no circular F argument.** Only over the descended involutive field use ℓ⊥/ℓ and (ℓ⊥)⊥=ℓ. A Hermitian two-space has a vector with nonzero self-pairing (otherwise scaling contradicts nondegeneracy); diagonal splitting and norm surjectivity give Q+1 isotropic lines. P19 gives point totals independently of any plane/F formula. Divide actual incidences in the integers.|I-CLEAR; independent review open|
|P23,288–297|**Contained quadric planes.** Two rank-one basis matrices with independent image and coefficient factors would sum to rank2. Hence one common factor is necessary and sufficient. The two rulings are distinct as two-planes; actual restricted form gives counts1,Q+1 in the odd case and Q+1,Q+1 in the even.|I-CLEAR; independent review open|
|P24,298–308|**Odd incidence correction.** A nonzero binary quadratic on the descended projective line can only acquire roots of degree≤2. Odd [k:F_Q] excludes new quadratic roots. All base rank1 points are symplectic-isotropic, each on Q+1 planes. Only contained planes gain q−Q roots. Subtract their exact incidences to derive F.|I-CLEAR; independent review open|
|P25,309–328|**Even graph splitting, including non-graphs.** Projection rank0 is contained, rank1 gives a displayed product of linear forms. Rank2 is a Hermitian graph and Δ becomes (27). x=0 and h+j=0 are separate; otherwise z=x^Q(a₁/a₂)/(h+j) gives Artin–Schreier constant Norm(x)/(h+j)²∈F_Q. Its absolute trace in E is zero, hence it splits. This works when [k:E] is even.|I-CLEAR; independent review open|
|P26,329–339|**Even incidence correction.** Rank1 base point count is (Q+1)(2Q²−Q+1); each lies on Q+1 Hermitian generators. P25 ensures noncontained planes gain no new roots, without an invalid parity argument. Contained ones gain q−Q², giving the displayed F.|I-CLEAR; independent review open|
|P27,340–351|**N1 sum and expanded N2.** Three disjoint μ1 input classes sum to (29); coverage and μ≥4 exclusion make N2 the complement, not a conjecture. Exact five-variable polynomial assembly checks (30) independently of evaluating any field.|I-CLEAR; independent review open|
|P28,352–359|**Endpoints and non-involutive orders.** s0 has Q=q, r1, trace image0; formulas simplify to the stated polynomials. r2 makes the contained extension correction zero. r>2 uses the trace and descent lemmas, never a polarity on all k.|I-CLEAR; independent review open|
|P29,360–363|**Gcd marginal and matrix conversion.** Parameters depend only on q,gcd(s,m). This does not identify hulls of the same W across twists. Two-column packing gives the matrix histogram. All μ3 cases are equal to input and dual under P04, so the proper-hull assertion has its actual side/form.|I-CLEAR; independent review open|
|P30,364–368|**Scope and acceptance.** Every all-parameter deduction above has been internally replayed; no counterexample or unresolved mathematical implication was found. This row does not promote a same-agent reread into genuinely independent acceptance. The full proof still needs the independent-scrutiny gate required by the user. Other lengths/ranks/forms, joint profiles, novelty and applications are excluded.|I-CLEAR; independent review open|

## 2. Second derivation of arbitrary-Frobenius isotropic points

This route does **not** condition on P19's a-directions. Let ψ(x)=(−1)^Tr_(k/F₂)(x), and use absolute-trace invariance under σ. For fixed c and x,

Σ_y ψ(c[σ(x)y+σ(y)x]) = q if cσ(x)+σ⁻¹(cx)=0, and 0 otherwise.

Thus, writing L_c(x)=cσ(x)+σ⁻¹(cx), character orthogonality on the equation Ω(v,v)=0 gives

Z=q⁻¹[q⁴+q² Σ_(c≠0)|ker L_c|²].

For c≠0, σ(L_c(x))=0 is σ(c)σ²(x)+cx=0. Nonzero solutions require σ²(x)/x=c/σ(c). The map x↦σ²(x)/x on the cyclic k× has kernel E× and image exactly the norm-one kernel to E: it is contained there by telescoping, and both sets have size (q−1)/(e−1). Each admissible right side has e−1 nonzero solutions, hence kernel size e including zero. Otherwise only zero solves, so the kernel size is **1**, not zero.

Norm_(k/E)(c/σ(c))=t/σ(t), t=Norm_(k/E)c. For odd r, E=F_Q and σ fixes every t, so all q−1 coefficients are admissible, each with |ker|=Q. For even r, σ|E is Q-Frobenius and t must lie in F_Q×. Norm surjectivity gives (q−1)/(Q+1) admissible c, with kernel Q²; other c have kernel1. Therefore

Σ_(c≠0)|ker L_c|² = (q−1)Q² (odd r),
Σ_(c≠0)|ker L_c|² = (q−1)(Q⁴+Q)/(Q+1) = (q−1)Q(Q²−Q+1) (even r).

This yields Z=q³+q(q−1)c and I=(Z−1)/(q−1)=q²+q+1+qc. Subtracting the actual rank1 factorization gives U as in T3. At s0 all kernels are k; the same calculation works, without asserting nontrivial trace image. These are group/character calculations, not a Hermitian-point formula imposed on non-involutive σ.

## 3. Second fixed-field incidence derivation, including even extension degrees

### 3.1 Plane totals from projection charts, not point/quotient incidence

Work over E after σ² descent. A self-dual plane with a-projection rank0 is 0⊕E² (one). At rank2 it is b=Ma: M symmetric in the alternating case, or Hermitian in the involutive case. These give Q³ and Q⁴ matrices, respectively.

At rank1 choose the image line El. Its b-kernel is exactly the one-dimensional annihilator of σ(l). A lift (l,t) is unique modulo that kernel. The functional σ(l)·t identifies this quotient with E; self-pairing imposes c+σ(c)=0. It allows Q values in each case. There are Q+1 possible l-directions in the odd case and Q²+1 in the even case. Totals are

1+Q(Q+1)+Q³=(Q+1)(Q²+1),
1+Q(Q²+1)+Q⁴=(Q+1)(Q³+1).

This recovers P22 without using its point/plane division. Non-graph planes are explicitly counted, not silently excluded by the graph chart.

### 3.2 Odd-order relative quadric types

Let L=diag(swap,swap), so the polar form of Δ is Ω₀(Lv,t). On an alternating Lagrangian T, zero polar restriction means L(T)=T. Set N=L+I. Then N²=0 and imN=kerN=E₀={(αh,βh):h=(1,1)}. If T≠E₀ is stable, dimension forces T∩E₀=N(T)=M, a line. Conversely for each of Q+1 such M, the quotient N⁻¹(M)/M has Q lines outside E₀/M. Their lifts are Lagrangian: for e=(αh,βh) spanning M and Nv proportional to e,

Ω₀(e,v)=α(b₁+b₂)+β(a₁+a₂)=0.

There are 1+Q(Q+1) zero-polar planes. Remove Q+2 contained ones to get Q²−1 tangents. Count base rank1 incidences (Q+1)³. Contained planes contribute (Q+2)(Q+1) and tangents one each; divide the remainder by2 **in the integers** to get Q²(Q+1)/2 secants. Subtract all classes from the plane total to get Q²(Q−1)/2 external planes. Because [k:F_Q] is odd, external quadratics stay rootless. Consequently

F=q(Q²−1)+(q−1)Q²(Q+1)/2+(q+1)Q²(Q−1)/2
 =q(Q³+Q²−1)−Q².

### 3.3 Even-order relative quadric types, independently of the graph-root argument

For a Hermitian self-dual T, D₀(T)=σ(T), so zero polar restriction means L(T)=σ(T), equivalently τ=Lσ stabilizes T. Fixed vectors of τ have form ((x,x^Q),(y,y^Q)); on them Ω is the nondegenerate alternating F_Q form Tr_(E/F_Q)(x^Q t+y^Q z). Nondegeneracy follows from that of the field-trace pairing, and self-pairings vanish.

Choose α∈E with α+α^Q=1. If τT=T, then u=v+τv and h=(α+1)v+ατv are fixed vectors in T and v=h+αu. Splitting an E-linear relation into F_Q+αF_Q and subtracting its τ-image shows that F_Q-independent fixed vectors remain E-independent. Thus τ-stable E-two-planes correspond exactly to alternating F_Q-Lagrangians. The number is (Q+1)(Q²+1), supplied independently in §3.1.

Remove 2(Q+1) contained planes: tangents=(Q+1)(Q²−1). The base Hermitian-isotropic rank1 point count is (Q+1)(2Q²−Q+1); each is on Q+1 planes. Subtract contained/tangent incidences and divide by2 to obtain Q²(Q²−1) secants. This equals **every** remaining nonzero-polar plane, so none is external. Thus all noncontained roots are already over E, even when [k:E] is even. It follows that

F=q(Q+1)(Q²−1)+(q−1)Q²(Q²−1)
 =(Q²−1)[q(Q²+Q+1)−Q²].

This route uses semilinear descent and integer incidence, whereas P25 proves splitting from Norm(x)/(h+j)² having absolute trace0. They have different central intermediate obligations; neither is an independent person reviewing the full proof.

## 4. Fresh directed test of the nonreflexive flag step

For v spanning a rank2 isotropic point, choose w∈A_v\kv with **Ω(w,v)=0**. In basis (v,w) the Gram matrix is

[[0,Ω(v,w)],[0,Ω(w,w)]].

Its right kernel is exactly kv unless both remaining entries vanish; only then is the whole plane self-dual. There are (q³−q)/(q²−q)=q+1 planes through kv in A_v. The 1/3-dimensional flags contribute two more each, giving (q+3)U−F with the **right** orientation. No reflexivity is used.

The new [standalone driver](../../computations/audit_core_a_directed_flags.py) imports **no repository code**, separately implements polynomial-long-division field arithmetic and field kernels, and enumerates these flags directly. Fresh [records](../../computations/results/finalisation_m8_directed_flags_v1/directed_flag_cases.json): **101,316** two-plane flags over all twists at q4/q8/q16; all right radicals and raw geometry/stratum counts agree. It separately checks **304 Hermitian graph matrices** in four q4/q16 even-order cases and their base/extended quadratic roots. This is not a B²-module census or a second full-global q16 enumeration.

There are four nonreflexive wrong-direction witnesses. For q8,s1 in the recorded polynomial basis, v=(1,0,0,2), w=(1,1,6,0) satisfy Ω(w,v)=0 but Ω(v,w)=2≠0. For q16,s1 take w=(1,1,5,0); Ω(v,w)=1. Therefore the two hyperplanes cannot be exchanged, even if their aggregate point counts happen to agree.

## 5. Corrections, dependency risks and acceptance verdict

|Challenge|New disposition|Formula/hypothesis change?|
|---|---|---|
|Local ring and Nakayama assumption left tacit|P02 now explicitly supplies the unit inverse and maximal-ideal argument.|No|
|[z] auxiliary functional might be confused with the original [u]trace scalar companion|P04 derives the B-valued/global dual first; P05 explicitly distinguishes equal orthogonal submodules from equal scalar forms. The actual original scalar companion is c_u+c_z, as in the preserved foundations.|No|
|Primitive projection onto B / proper I implicit|P09 explains surjectivity and why a unit in I would force residue rank2; fixes a new draft-only grammatical splice.|No|
|Semilinear “hyperplane” and left/right ambiguity|P18 applies σ⁻¹; new directed flags exhibit counterexamples to exchanging the tests.|No|
|Scaled trace-hyperplane comparison compressed|P19 now supplies annihilator dimensions, inverse scaling, axis cases and simultaneous a,b rescaling.|No|
|Perpendicular quotient assumed nondegenerate|P22 supplies its radical argument explicitly, only over E after involutive descent.|No|
|Normalized Hermitian quadratic coefficient not displayed|P25 now gives z=x^Q(a₁/a₂)/(h+j) and the transitive absolute-trace calculation, with zero coefficients separate.|No|
|Stronger inherited “PROVED” status despite same-agent review only|The six M8 successors retain a candidate derivation and explicitly leave genuinely independent acceptance open. Originals remain immutable historical records.|**Acceptance wording corrected**, not the candidate mathematical content|

The conventional argument was internally replayed for every unit; **no unresolved mathematical implication or theorem counterexample was identified** in this scope. This statement does not guarantee that an independent reviewer will agree. The user's complete-proof independent-scrutiny gate is **not satisfied** by this audit, the standalone checker, reruns, hash checking or Git synchronization.

**Precisely outstanding verification dependency:** an independently attributable mathematical assessment (or an appropriately complete formal derivation) must validate the exact theorem/proof hashes above across P01–P29, especially the directed flag, arbitrary-order trace and even-order relative-incidence steps, and address any resulting objections. No such review/certificate is present or generated here. It is a verification blocker, **not an invented missing lemma or an asserted mathematical counterexample**. Novelty clearance is separately blocked by the authenticated closest-source comparisons in [the literature assessment](CORE_A_PRIMARY_SOURCE_NOVELTY_ASSESSMENT.md). The work must not be labelled externally accepted, formally checked, original, Q1-ready or submission-ready.
