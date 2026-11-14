# Core A — independent re-derivation and line-by-line proof audit

**Meaning of “independent” here:** a second mathematical route and separately implemented arithmetic/global checks by the **same agent**. No second human author/referee, proof-assistant certificate or external peer review is claimed. The user-requested filename does not change that limitation.

Audited statement: `../phase3/CORE_A_CLOSED_FORMULA_THEOREM.md`, SHA-256 `6d42ef6b6b2caa1038b91ec28352a40880c7b00287e083217d0a12c972c7ae7d`.

Audited full proof: `../phase3/CORE_A_CLOSED_FORMULA_FULL_PROOF.md`, SHA-256 `9ba7f910bc19c88cc2eba055d42d6d2209b0183ea2d0241ccca98bb6b9efcae7`,364 lines. The ranges below cover every proof unit and displayed equation; document headers introduce notation only. Range checking is textual provenance, **not** automated logical validation.

## 1. Line-by-line obligation register

Every row was checked for hypotheses, direction, dimension/count and dependence on preceding rows. “PASS” means the conventional argument is supplied and the audit found no unresolved step in this scope.

| Proof unit / lines | Obligation checked and resolution | Result |
|---|---|---|
|P01,9–20|Fixed fields via gcd, explicit s0 identity boundary; nonzero trace polynomial of degree<q; im(1+σ)=ker Tr by ranks; nondegenerate trace pairing; cyclic-group norm/root counts.|PASS|
|P02,21–34|Nilpotent Nakayama gives equality of minimum generator number and top dimension. Both lower and upper two-column packing bounds proved, including zero ideal.|PASS|
|P03,35–44|Central length2 quotient equals M₂(B); matrix units prove a bijection with all embedded column modules, not only principal ideals.|PASS|
|P04,45–58|Original global form is the constant coefficient of x†y; the other cyclic shift tests its remaining coefficient; dagger fixes w and transpose tests every column pair. No scalar isometry assumed.|PASS|
|P05,59–68|Socle functional is nondegenerate; testing all B-multiples converts scalar-zero to B-valued-zero. Dimensions and positive σ² double dual follow; no false reflexivity.|PASS|
|P06,69–83|Full scalar ideal list, line ideals principal, exact annihilator cases, including n=0/unit/nonzero-socle/mixed-radical.|PASS|
|P07,84–93|Both projections of T lie in K; f is quotient-valued and unique. Converse reconstruction closed under u,w, with no omitted lift data.|PASS|
|P08,94–112|JW=zP(T), exact β multiplication gives Ω, retained K and restricted f, hence hull μ formula for all twists.|PASS|
|P09,113–122|Residue rank2 forces full module; residue rank1 has unique ideal and slope coset in disjoint deterministic charts. Vertical chart not lost.|PASS|
|P10,123–140|Solve actual dual then input membership; all four ideal cases handled. Representative independence follows because bσ(j)=0 and remaining norm change lies in I.|PASS|
|P11,141–149|Normalize isotropic residue line; σ² fixes its slope; odd/even restriction on E yields d1/Q+1 and cyclic root count. Neither coordinate zero.|PASS|
|P12,150–161|Nonradical and K-line bounds; K=V radical dimension≤2. The only μ>2 case forces T=L⊕L isotropic; equal dimensions give actual self-duality. No μ4 hull.|PASS|
|P13,162–172|Projective points/hyperplanes and ordered two-frame count, then all-dimensional Grassmann sum G4.|PASS|
|P14,173–187|Count each unique K,T,f and each slope coset once, add disjoint residue ranks. L is derived, not inferred from a numerical census.|PASS|
|P15,188–195|Every nonzero radical retains socle; nonzero primitive kernel always has hull; free anisotropic lines plus zero/full give N0. N3/nonexistence≥4 already proved.|PASS|
|P16,196–208|Nonzero-I μ1 complement; expand actual free-line norm; exactly Q²(q−Q) pure nonzero-socle lifts per isotropic residue.|PASS|
|P17,209–216|K-line T0/1 contributions always μ1; only full T at isotropic K has μ2, with all q² lift maps counted.|PASS|
|P18,217–230|Right-radical flag condition uses the left-annihilator hyperplane correctly. Counts1,q+1,1; unique right radical except self-dual two-plane flags, which are subtracted with multiplicity.|PASS|
|P19,231–251|New trace-hyperplane derivation; equality of scaled hyperplanes iff their ratio lies in F_Q; exceptional a-directions exactly P¹(E); count zero a separately. Non-involutive σ never replaced by an involution.|PASS|
|P20,252–263|Unique Segre factorization of rank1 points; product of actual self-pairing factors gives precisely d(q+1)+(q+1−d)(Q+1).|PASS|
|P21,264–269|σ²-stability follows from the actual double-dual law; uniqueness of reduced rows proves descent and uniqueness. Converse extension checked by basis pairings/dimension.|PASS|
|P22,270–283|Plane counts from point/quotient incidence; nondegenerate Hermitian quotient has Q+1 isotropic lines by a supplied norm proof. No circular use of F.|PASS|
|P23,284–293|Rank≤1 matrix two-space has a common factor; the two rulings give disjoint contained-plane families and counts Q+2 or2(Q+1).|PASS|
|P24,294–304|Odd-degree extension cannot add quadratic roots; only contained planes gain q−Q rank1 points. Base rank1 point/plane count gives F directly.|PASS|
|P25,305–324|Separate projection ranks0,1,2. Hermitian graph criterion exact; quadratic normalization has constant Norm(x)/(h+j)² in F_Q and hence absolute trace0 in E. All boundary coefficients handled. No external plane assumed away.|PASS|
|P26,325–335|Even-order base rank1 incidence and contained correction q−Q², justified by P25 even when extension degree is even; expanded F checked.|PASS|
|P27,336–347|Three disjoint μ1 strata summed; N2 complement justified by complete family and μ≥4 exclusion; expanded N2 identity exact.|PASS|
|P28,348–355|s0 reductions include trace image0; order2 descent E=k has zero extension correction; non-involutive odd/even orders explicitly retained.|PASS|
|P29,356–359|Only marginal gcd dependence follows; matrix generator conversion and exact self-dual exceptions preserve the original pairing.|PASS|
|P30,360–364|All definitions/hypotheses retained; no claim about joint profiles, other lengths/ranks/forms or novelty follows from proof closure.|PASS|

## 2. Independent central point derivation — character sums, not trace hyperplanes

This route does not use P19's conditioning on a-directions or its hyperplane comparison. Let ψ be the nontrivial additive character from the absolute trace. For one coordinate pair, sum over y first:

S_c=Σ_(x,y)ψ(c[σ(x)y+σ(y)x])=q|ker L_c|,
L_c(x)=cσ(x)+σ^(−1)(cx).

The inverse σ is forced by invariance of trace. Orthogonality of additive characters then gives the number of isotropic vectors in k⁴:

Z=q^(−1)[q⁴+q²Σ_(c≠0)|ker L_c|²].

For c≠0, applying σ yields σ(c)σ²(x)+cx=0. A nonzero x exists iff c/σ(c) has norm1 to E=Fix(σ²). This norm-one image characterization follows by the kernel/image sizes of x↦σ²(x)/x in the cyclic group k×. In the odd case σ fixes E=F_Q, so every c is admissible and each kernel has Q elements. In the even case E=F_(Q²); if t=Norm_(k/E)c, the condition is t=t^Q. Exactly (q−1)/(Q+1) nonzero c have this property and kernel size Q²; the rest have kernel size1 (only zero).

Thus Σ|ker|² is (q−1)Q² in the odd case, or (q−1)Q(Q²−Q+1) in the even case. Therefore Z=q³+q(q−1)c, with exactly the c in T3. Removing zero and dividing by q−1 gives P19's I. Removing rank1 points by the direct two-factor condition reproduces U. This derivation remains valid at s0 (all kernels are k) and for every non-involutive order.

## 3. Independent self-dual plane and F derivation — graph strata and plane types

### 3.1 Plane totals without P22's quotient count

Work over the descended field E. Sort a self-dual two-plane by rank of projection onto its a-coordinate. Rank0 contributes1. Rank2 is a graph b=Ma: symmetric M gives Q³ possibilities in the odd case, Hermitian M gives Q⁴ in the even case.

For rank1, choose image line El (Q+1 choices in the odd case, Q²+1 in the even). Its b-kernel must be the line orthogonal to l. A lift (l,t) is determined by t modulo that line; the functional σ(l)·t identifies this quotient with E. Its self-pairing is c+σ(c). This imposes no restriction when σ=id, giving Q choices; with the involution it requires c∈F_Q, again Q choices. Thus rank1 contributes Q(Q+1) or Q(Q²+1), respectively. Summing yields (Q+1)(Q²+1) and (Q+1)(Q³+1), agreeing with P22 without its point-plane count.

### 3.2 Odd-order plane-type derivation

Let L exchange both coordinate pairs and N=L+I. On a symplectic Lagrangian, zero polar restriction of Δ is equivalent to L-stability. Here N²=0, imN=kerN=E0 of dimension2. The stable Lagrangians consist of E0, or T with intersection a line M⊂E0 and N(T)=M. For each of Q+1 M, the quotient N^(−1)(M)/M has Q lines outside E0/M. Their spanning vectors are symplectic-orthogonal: if e=(αh,βh), h=(1,1), and Nv is proportional to e, then Ω0(e,v)=α(b1+b2)+β(a1+a2)=0. Hence zero-polar planes number1+Q(Q+1).

Remove Q+2 contained planes to get Q²−1 tangents. Total rank1 base incidence is (Q+1)³. Removing contained contributions (Q+2)(Q+1) and tangents leaves twice the secant count, so secants=Q²(Q+1)/2. The remaining planes number Q²(Q−1)/2 and are external. Since the extension degree r is odd, these external quadratics stay rootless. The rank2-point incidence is

F=q(Q²−1)+(q−1)Q²(Q+1)/2+(q+1)Q²(Q−1)/2,

which is P24's F. The halves are ordinary integer counts, never field division by2.

### 3.3 Even-order plane-type derivation without P25's splitting test

For a Hermitian self-dual T, D0(T)=σ(T). Zero polar restriction is equivalent to invariance under τ=Lσ. Its fixed vectors are ((x,x^Q),(y,y^Q)), x,y∈E, on which Ω becomes a nondegenerate alternating F_Q-valued trace form.

Choose α∈E with α+α^Q=1. For v in a τ-stable T, both v+τv and (α+1)v+ατv are fixed and span v as v=h+αu. Splitting an E-relation into F_Q+αF_Q and applying τ shows F_Q-independent fixed vectors are E-independent. Thus stable E-two-planes correspond bijectively to F_Q-Lagrangians. Their number is (Q+1)(Q²+1), independently counted in §3.1. Remove2(Q+1) contained planes: tangents=(Q+1)(Q²−1).

Base rank1 isotropic points number (Q+1)(2Q²−Q+1), by the direct rank1 factorization; each is on Q+1 planes. Remove contained/tangent incidences and divide by2: the secant count is Q²(Q²−1). This equals every remaining plane, proving the external count is0 without using the graph-quadratic trace argument. Consequently

F=q(Q+1)(Q²−1)+(q−1)Q²(Q²−1),

which is P26's F. Thus the two proofs use genuinely different central intermediate counts, not just the same integer formula twice.

## 4. Independent check of the flag subtraction and nonreflexive direction

Fix a nonzero rank2 isotropic vector v spanning ℓ. Choose w∈A_ℓ\ℓ: q³−q possibilities. On T=span(v,w), the Gram matrix has first column zero and entries [[0,Ω(v,w)],[0,Ω(w,w)]]. It has rank1 unless T is wholly self-orthogonal. Each two-plane through ℓ has q²−q such choices of w, so there are (q³−q)/(q²−q)=q+1 candidates, excluding self-dual flags. Adding dimensions1 and3 gives exactly (q+3)U−F, with no assumption Ω(w,v)=Ω(v,w) or σ²=id. This independently checks the right/left direction in P18.

## 5. Original global pairing and executed verification

The symbolic derivation P03–P05 is part of the proof, not a claim inferred from a convenient representation. The fresh `closed_formula_proof_v1` run additionally performs:

- **4,608** basis/scalar/twist tests of the full polynomial product, its constant coefficient equal to the original global form, and its other coefficient equal to the cyclic-shift test, at q4/q8/q16.
- All **2,442** q4 original-global cases (the whole q4 family/both twists) and **176** saved q16 cases, using alternative field tables and direct right polynomial matrix products. Complete global/local dual/hull spaces agree; primary hull bases agree in all cases; saved primary dual bases are compared where exported at q16.
- An actual original-global q8,s1 counterexample to reflexivity: the free input line with slope2 has double-dual slope6=σ²(2), not2.
- **17** new trace/graph geometry cases agreeing with the older raw point/incidence observations, plus five exact sparse polynomial identities. The2,080 integer regressions for m1…64 are algebraic regression checks, **not** field/module censuses.

The existing q16 full666,084-case census is compared as existing evidence, not falsely reported as rerun. q32/q64 are geometry only. See the required theory/computation comparison for all coverage/hashes.

## 6. Clarifications found, necessary assumptions and verdict

No theorem counterexample or failed numerical case was found. Proof-completeness improvements are recorded rather than hidden: the full proof now supplies the previously referenced structural foundations; explicitly treats s0 before any simple-root argument (T−T is the zero polynomial); and supplies the even-extension no-external-plane lemma by all graph projection ranks. These do not weaken hypotheses or change the formula.

Necessary assumptions are exactly T1: characteristic2, u²=w²=0, matrix rank2, central length2, all embedded right codes and the displayed first-slot coefficient-Frobenius transpose pairing. Every counting lemma needed within that scope is justified above/P01–P30. Extending to other lengths/ranks/forms, inferring reflexivity for r>2, a joint multi-twist histogram, external originality, or human review would introduce **unjustified** assumptions and is not done.

**Verdict:** conventional all-parameter mathematical proof supplied and internally audited, independently re-derived in the stated algorithmic/mathematical sense. No open mathematical gap remains identified in the exact theorem. External human review and novelty/Q1 assessment remain separate and incomplete.
