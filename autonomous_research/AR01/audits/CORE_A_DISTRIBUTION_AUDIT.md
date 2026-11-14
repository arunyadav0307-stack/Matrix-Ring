# M5 — Core A closed-distribution theorem: internal proof and computation audit

**Disposition:** A13's closed marginal hull-generator distribution is proved in the exact Core A working note and survives this same-agent obligation audit. Executed finite checks PASS. **External originality/sufficient paper depth, independent human review, final manuscript and submission readiness are NOT certified.** A new proof and separately written programs are not a referee report.

Proof: `../phase3/CORE_A_HULL_DISTRIBUTION.md`. Integer implementation: `../computations/core_a_distribution.py`. Prior A11 proof/results remain immutable. Calendar/provenance sources remain distinguished in the M4 addendum; no raw timestamp is normalized.

## 1. What is counted, and what is not

For each one fixed s, the theorem counts **all embedded** B-submodules W≤B² by μ_B(H_s(W))=0,1,2,3. It is not an isomorphism/GL quotient, a count of chosen generator matrices with multiplicity, or a joint distribution of all twists on the same W. Matrix right-ideal minimum generators are ceil(μ_B/2); column values1/2 both mean matrix-principal. The m=1,q2 historical comparison is auxiliary, outside m≥2.

The new closed μ1 formula is not just the generic rank formula: it resolves actual point/plane/quadric incidences and descents for all Frobenius orders. N0,N3,total and the μ≥4 exclusion are earlier A11 results, not newly discovered numerical observations.

## 2. Proof obligations actually audited

| Obligation | Internal resolution |
|---|---|
| Parameter endpoints | g=gcd(s,m), including g=m when s=0; Q=2^g; r=m/g. Odd/even r branches give d=1/Q+1 and match the earlier norm-root formula. |
| Exhaustive disjoint module classes | Primitive residue rank1; radical K=0, line, or V; whole ambient. Their unique embedded descriptors prevent missing lift maps, overcounting or a hidden equivalence quotient. |
| Primitive μ1 count | All nonzero kernel ideals contribute A0 except the d q² socle-kernel μ2 cases. For free lines use t=a(1+xu+yw+hz), expand the actual norm, and count pure nonzero-socle norms by x,y∈F_Q and h∉F_Q. No assumption σ²=id. |
| Radical K-line count | T dimensions0/1 always give μ1, irrespective of the layer line's isotropy; dimension2 gives μ2 exactly for isotropic K. Every lift map is counted with q^(dim T) choices. |
| Radical K=V μ1 criterion | Exact layer formula gives μ1 iff T_s is a line with two-dimensional projection sum. It does not assume the layer form is reflexive. |
| Incidence correction | For each such isotropic line ℓ, T lies between ℓ and its left-annihilator hyperplane: one each in dimensions1/3 and q+1 in dimension2. A two-plane must be subtracted exactly when it is self-dual; all other μ1 right-radical lines are unique. Hence (q+3)U−B_inc. |
| Arbitrary-order isotropic points | Additive-character orthogonality gives q³+qΣ_(c≠0)|ker L_c|² isotropic vectors. Trace moves σ on the second factor with σ^(−1), not σ. The displayed equation σ²(x)/x=c/σ(c) and cyclic-group norm image give the exact odd/even kernel sizes and good-c counts. |
| Remove rank1 projections | Unique residue line/coefficient line factorization, with self-pairing equal to the product of its two factors. Count d(q+1)+(q+1−d)(Q+1); no GL equivalence. |
| Self-dual plane descent | D_s^Ω²(T)=σ²(T). Uniqueness of reduced rows proves fixed-field descent to F_Q or F_(Q²), where σ restricts to identity or its nontrivial involution. Extension back preserves dimension and basis pairings. |
| Fixed quadric/operator | Δ=a1 b2+a2 b1 is literally the projection-rank-one quadric. Its polar form is Ω0(Lv,t), L=diag(swap,swap). This auxiliary identity does not transform a code or replace its actual form. |
| Odd-order contained/tangent planes | Rank≤1 matrix-space rulings give Q+2 contained planes. L-stability reduces to N=L+I with imN=kerN; exactly1+Q(Q+1) Lagrangians have zero polar restriction. Tangents Q²−1. |
| Odd-order secants/external planes | Count rank-one point/plane incidences to obtain Q²(Q+1)/2 secants and Q²(Q−1)/2 external planes. Quadratics irreducible over F_Q remain so across the odd extension degree r. |
| Even-order zero-polar descent | L(T)=σ(T) is τ=Lσ invariance. Explicit trace-one α and u=v+τv, h=(α+1)v+ατv prove fixed-space dimension and extension in characteristic two. Ω_Q on its fixed space is a nondegenerate alternating trace form. No division by2 or diagonalization of the swapping operator. |
| Hermitian quotient/plane count | The added norm-surjectivity argument supplies Q+1 quotient isotropic lines. Point-plane incidence yields (Q+1)(Q³+1) self-dual planes. |
| Even-order intersection types | Contained2(Q+1), tangent(Q+1)(Q²−1); rank-one incidence gives exactly Q²(Q²−1) secants, exhausting all remaining planes. Therefore no external plane is silently assumed away. All roots are already over F_(Q²). |
| Final assembly | Sum the three μ1 strata, add the previous N0/N3/total, take the complement N2. At s0 this algebraically gives N1=7q³+4q²+2q+2 and N2=q⁴+q³+6q²+5q+4. Aggregate gcd(s,m)-dependence follows, not equality of individual hulls across twists. |

No unresolved mathematical step was found in these obligations after the explicit characteristic-two descent/quotient addendum. This is a conventional internal proof audit, not formal verification or external peer review.

## 3. Fresh full q16 census — actually executed

`verify_core_a_distribution.py distribution_v1`: **PASS** after approximately a few minutes of exact standard-library computation (the combined reference/audit tool call took340.108 seconds; it is not an isolated timing benchmark).

- All **166,521** q16 embedded input modules: 87,895 radical,78,625 primitive and1 whole ambient.
- All four twists: **666,084** generic B-valued dual/intersection vs structural hull-space comparisons, not just dimensions.
- Every input deduplicated and checked for u,w closure. Input μ and hull μ agree with the structural calculation. Full stream is deterministically hashed, not bulk-stored.
- Every marginal histogram and all three μ1 input-stratum counts match the closed formula.
- Old q2/q4/q8 histograms are read from the preserved `structure_v1` summary as **old executed comparison data**, not claimed as fresh M5 reruns. They agree with the formula.

| q16 twist | μ0 | μ1 | μ2 | μ3 |
|---|---:|---:|---:|---:|
|0|65538|29730|71252|1|
|1|57346|33490|75682|3|
|2|49154|48386|68976|5|
|3|57346|33490|75682|3|

| q16 twist | Primitive μ1 inputs | Radical K-line μ1 inputs | Radical K=V μ1 inputs |
|---|---:|---:|---:|
|0|12833|8737|8160|
|1|20345|8225|4920|
|2|27233|7713|13440|
|3|20345|8225|4920|

These **new** observations supersede the *current* q16 coverage limit, but do not alter the old notes/results whose original execution correctly did not exhaust q16.

## 4. Separate arithmetic/incidence/global audit — actually executed

`audit_core_a_distribution.py distribution_v1 distribution_audit_v1`: **PASS**. It imports no primary field/module/descriptor/hull implementation. It shares the new **integer prediction function only**, and compares its predictions to separately enumerated actual geometry. Alternative field tables, canonicalization and hyperplane restriction are from the unchanged original audit implementation.

### Full small-field layer geometry

All T≤k⁴, all twists at q4,q8,q16: **334,413 field/twist/subspace cases**. The audit checks the raw isotropic-point count, U, self-dual-plane quadric intersection types, B_inc and direct K=V μ1 count. Self-dual planes are also checked to be fixed by σ². The enumerator operates in width4, not by copying the reference B² descriptor enumeration.

Selected independent observations:

| q,s | U | B_inc | Direct K=V μ1 count |
|---|---:|---:|---:|
|4,0|60|300|120|
|4,1|24|72|96|
|8,1 or2|72|84|708|
|16,0|4080|69360|8160|
|16,1 or3|276|324|4920|
|16,2|960|4800|13440|

All odd/even plane-type tables in the proof match the full enumeration; numerical evidence does not substitute for the type-count proof.

### Higher fields, explicitly narrower scope

At q32, s1,2,3,4 and q64, s1,2,4,5, all projective points and all descended self-dual-plane candidates were enumerated: **1,200,520 projective-point field/twist cases**. This exercises non-involutive orders5,6 and3. It checks U and the full plane-type/B_inc formulas, not all T or all B² modules. q64 s0/s3 are not covered by this higher-field run. New q32/q64 field tables have294,912 exhaustive distributivity triple checks in total, full nonzero primitive cycles, explicit inverses and commutativity checks. No q32/q64 code census is claimed.

### Original global pairing subset at q16

**176** recorded deterministic cases: every4,096th module index at every twist (164 cases), plus all12 exceptional nonprincipal hull cases. Each code is rebuilt by original right polynomial matrix products in R²; all coordinates of the original matrix-valued first-slot form are enforced. Full global/local dual and hull spaces agree inside the alternative route, and its local dual and hull bases equal the saved primary bases. This is not an exhaustive q16 global-pairing census.

## 5. Evidence hashes and preservation

- Integer formula source: `5a8276e58f3cc33fd209739ff34328e01bb66ff59a7d7cddbc12e126a190cbd7`.
- Reference census source: `49025cce5c1558f77c44873202f67d3ef32478ac7a3f565090aca6dd579e160a`.
- Separate audit source: `9559c9ed0c261a6d6dee881cdfd0b51f501d4a2b22ecff15e591b3cb280a88e8`.
- Full q16 deterministic case stream (hash only): `3a7417fd6536629e6aff17dc1bbd4a8deb1f2d62e5afc66f51f523d0aeca28d2`.
- Selected q16 input stream: `e01eab3d2a0d44bfbcb44913da245014f6e46c98f428b968d687da87b546823f`.
- Independent geometry records: `2570268bf64f82f7bde2cf014caa9848195da6eaddd1de6a9c7b2a93886886d6`.
- Independent global q16 records: `0b235bf6542ed719ec43677ea251545e20350c49c79ee53cb9e09cbb729768fc`.

All old result/source hashes and 2,059-file intake preservation are rechecked by the M5 precommit evidence. No hashed computation source has been edited after these successful executions.

## 6. Scientific gate

A13 is a stronger same-ring **candidate contribution** than the rejected impossible Core A principal-input counterexample search or A12's scalar CRT witness alone. Its closed distribution has substantive finite-geometry obligations, but those use classical machinery and may be known or insufficiently deep as a paper. Complete theorem-level closest-source and geometry comparison is still essential. Retrieval of a noisy GitHub lead is not primary-version validation, and lack of access is not a gap. The accompanying Phase-1 gate record defines exactly what evidence remains unavailable before promoting a publication manuscript. No Gray/quantum/distance/journal/quartile/application is manufactured to bypass that gate.
