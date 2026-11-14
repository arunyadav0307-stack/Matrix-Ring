# Mathematical claim verification

**Audit execution:** 2026-11-13 UTC (workspace clock). **Overall mathematical readiness: HOLD — a sound core and reproducible examples coexist with incorrect statements and defective proofs.** This is an independent audit, not a revised manuscript or a new research phase.

## 1. Classification standard and scope

Exactly these six classifications are used in the ledger:

| Classification | Meaning in this review |
|---|---|
| **VERIFIED** | The particular stated fact/witness was independently established within its stated finite or explicit scope |
| **VERIFIED UNDER CONDITIONS** | The result is valid with the listed algebra/module/metric/quantum hypotheses; those conditions cannot be omitted |
| **COMPUTATIONALLY SUPPORTED ONLY** | Finite experimental/log evidence exists, but does not prove the general claim, or the wider census was not independently revalidated |
| **INCOMPLETE** | An argument, identification or required bridge is missing; not treated as a theorem |
| **INCORRECT** | A stated identity, universal claim, proof step or interpretation has a direct contradiction/counterexample |
| **UNVERIFIABLE** | Available evidence cannot establish the stated existence/status/priority/novelty assertion |

The ledger separates **a theorem's truth, the validity of a particular proof, a finite computation, and a novelty claim**. For example: nonprincipal hulls really exist, but the manuscript's particular construction is wrong. The EA parameter formula is valid under the standard construction, but the printed EA proof contains false steps. A passing finite example does not repair either proof. A [machine-readable index](evidence/claim_classification_index.csv) preserves each ledger row's classification and evidence/conditions.

This review traces the mathematical claim families made by the six mandatory reports and their decisive supporting sources. It is **not** a claim to have independently reproved every entry of the entire historical theorem register, every competing paper, or every scanned code. Each broader residual is marked accordingly.

Notation: \(A=\mathbb F_{p^m}[u]/(u^t)\), \(R=M_r(A)\), \(r\ge2,t\ge1,n\ge1\), coefficient Frobenius fixing \(u\), \(\theta_k=\sigma_k\circ T\), **right modules**, central cyclic variable. \(N=tr^2n\). Matrix-size-2 manuscript notation uses \(r_{old}=m,m_{old}=r,s=k\).

## 2. Evidence locators

All source-relative paths below start at `work/PHASE0_COMPLETE_AUDIT_PACKAGE/` in this review (also preserved byte-for-byte in the nested original ZIP).

- **S** = `mathematical_evidence/prior_project/03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`.
- **S2A/S2B/S3B/G** = same directory's `PHASE2_STAGE2A_MORITA_GENERATORS.md`, `PHASE2_STAGE2B_CRT_PRINCIPALITY.md`, `PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md`, `PHASE4_GRAY_MAP_COMPATIBILITY.md`.
- **M05/M06/M07/M08/M09** = `repository_integrity/prior_work/PAPER/sections/05_hulls.tex`, `06_gray.tex`, `07_quantum.tex`, `08_certification.tex`, `09_comparison.tex`.
- **D** = `computational_evidence/research-data/`.
- **E1** = [independent_core_checks.json](evidence/independent_core_checks.json): 17 assertions.
- **E2** = [critical_followup_checks.json](evidence/critical_followup_checks.json): 7 assertions.
- **E3** = [remaining_scope_checks.json](evidence/remaining_scope_checks.json): 5 assertions, with the last clearly labelled a disposable-source reproduction.
- **E28** = [independent_28_code_checks.json](evidence/independent_28_code_checks.json) and [CSV](evidence/independent_28_code_summary.csv).
- **ER** = [included_source_run_summary.json](evidence/included_source_run_summary.json), three completed original-source reruns.
- **L/B** = literature/benchmark evidence IDs in [preserved web notes](evidence/LITERATURE_WEB_RECHECK_NOTES.md).

Independent arithmetic in E1/E2 and the first four E3 tests imports **no project arithmetic**. These 29 focused assertions include negative controls and checker support facts; they are not “29 universal theorems.” The source reruns and generator reconstruction are a distinct evidence layer.

### 2.1 Explicit resolution of the historical N1–N12 references

The six reports' N-labels resolve to `mathematical_evidence/prior_project/06_AUDIT/PHASE0_FINAL_NOVELTY_STATEMENT.md`, §1B. They are not missing theorem numbers. That historical table's **NEW** flags are not accepted as independent novelty findings.

| Historical label | Exact proof trail and present interpretation | Classification |
|---|---|---|
| N1 | S §1, θ² and automorphism laws; F03/F04 | **VERIFIED UNDER CONDITIONS** |
| N2 | `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` §3, θ(B(x,y))=B(y,σ_2k x); D10. This is theta-Hermitian symmetry when reflexive, not ordinary value symmetry | **VERIFIED UNDER CONDITIONS** |
| N3 | S Props2.1/2.2 and Thms3.4/3.5; D01/D03/D07/D09 | **VERIFIED UNDER CONDITIONS** |
| N4 | S Thm3.6 and historical proof audit §5; positive double twist D10 | **VERIFIED UNDER CONDITIONS** |
| N5 | S Thm3.9 and proof audit §6; universal quantifier and matrix size≥2 essential | **VERIFIED UNDER CONDITIONS** |
| N6 | Historical proof audit §8; coefficient σ commutes with θ and preserves zero/nonzero entries; D17 | **VERIFIED UNDER CONDITIONS** |
| N7 | N4+N6: DD=σ_2k(C) preserves size, coefficient/ring-Hamming enumerator, distance and hull dimension. No arbitrary metric-change claim | **VERIFIED UNDER CONDITIONS** |
| N8 | Historical proof audit §7; S Thm3.7 shift identity; D07/D16 | **VERIFIED UNDER CONDITIONS** |
| N9 | S Prop4.1 and proof audit §9; right-module hypothesis; D08 | **VERIFIED UNDER CONDITIONS** |
| N10 | Historical proof audit §§1/5: for entrywise τ∈Aut(A), θ_τ=τ∘T has θ_τ²=τ²; the same correctly sided annihilator argument gives DD=τ²(C). Universal reflexivity criterion needs r≥2. This is existing source generalization, not newly implemented research | **VERIFIED UNDER CONDITIONS** |
| N11 | `06_AUDIT/PHASE0_U8_U9_DECISIONS.md` §4; field-degree trichotomy, D12 | **VERIFIED UNDER CONDITIONS** |
| N12 | S Thm3.8 plus proof audit §8; cyclic right hull/σ-equivariance D17 | **VERIFIED UNDER CONDITIONS** |

## 3. Claim ledger — ring and cyclic structure

| ID | Claim as audited | Classification | Evidence / decisive qualification |
|---|---|---|---|
| F01 | A is a finite commutative chain/Frobenius ring, ideals (u^i), size p^(mt) | **VERIFIED UNDER CONDITIONS** | Polynomial truncation with field coefficients; S §0/Lemma1.4; standard top-coefficient argument |
| F02 | R is noncommutative for r≥2, center A I, radical M_r((u)), size p^(mtr²) | **VERIFIED UNDER CONDITIONS** | Matrix units and reduction modulo u; source ring feasibility §2 |
| F03 | Coefficient σ_k is an automorphism, fixes u, order m/gcd(m,k) | **VERIFIED UNDER CONDITIONS** | S Lemma1.1; E1 coefficient-lift countercheck. Not whole-ring powering; a nontrivial residue k needs m>1 |
| F04 | θ_k is anti-multiplicative and θ_k²=σ_2k | **VERIFIED UNDER CONDITIONS** | S Lemmas1.2–1.3; transpose/Frobenius commute; not automatically an involution |
| F05 | Top coefficient composed with matrix and field traces gives a generating-character framework | **VERIFIED UNDER CONDITIONS** | S Lemma1.4; nonzero-ideal detection; L03/L04/L20. Distinguish scalar functional from exponentiated character |
| F06 | “Most one-sided ideals of the base R are nonprincipal” | **INCORRECT** | Chain-ring Morita modules in A^r need ≤r generators, hence all base left/right ideals are principal; E1 checks all33 for F4/u²,r2 |
| F07 | Cyclic right R-modules correspond to right ideals of R_n≅M_r(B) and B-submodules of B^r | **VERIFIED UNDER CONDITIONS** | Central X, X^n−1; S2A Morita/column convention. Not arbitrary left or two-sided ideals |
| F08 | I_W is principal iff μ_B(W)≤r; dim_Fq I_W=r dim_Fq W | **VERIFIED UNDER CONDITIONS** | Columns of one r×r generator versus r arbitrary column vectors; S2A generator dictionary (r2 form) |
| F09 | For matrix-size2, all cyclic right ideals principal iff t=1 **or** p∤n | **VERIFIED UNDER CONDITIONS** | S2B Thms4.1/4.3/Cor4.4. The reports' “general principality still open” is stale, not a missing theorem |
| F10 | Clean squarefree/split CRT enumeration needs p∤n; repeated-root cases need separate treatment | **VERIFIED UNDER CONDITIONS** | S2B explicitly treats t1 repeated roots and wild t≥2 cases. The valid warning does not make all t≥2 principality theory open; see F09 |
| F11 | Every submodule of a chain-ring free module is itself free | **INCORRECT** | M05 sentence; uA⊂A with A=F4[u]/u² has4 elements, incompatible with nonzero free A-rank. The needed ≤r-generation result is valid |

## 4. Claim ledger — pairing, duality and hulls

| ID | Claim as audited | Classification | Evidence / decisive qualification |
|---|---|---|---|
| D01 | B_k(xa,y)=θ_k(a)B_k(x,y), B_k(x,yb)=B_k(x,y)b | **VERIFIED UNDER CONDITIONS** | Right action; S Prop2.1. Full derivation in pairing audit §2 |
| D02 | Frozen P1 summary: B_k(ax,y)=θ_k(a)B_k(x,y) | **INCORRECT** | E1 `summary_ax_formula_counterexample`, E12/E21 witness. Detailed S has the correct law |
| D03 | B_k is elementwise nondegenerate in both variables | **VERIFIED UNDER CONDITIONS** | S Prop2.2: select a nonzero coordinate and use I_r there |
| D04 | Summary's E_ba probe always proves nondegeneracy | **INCORRECT** | E1 x=E12,y=E21 gives0 after transpose; theorem survives via identity probe |
| D05 | Plain product can fail the same-right-module size law | **VERIFIED** | E1 M2(F2), top-row right ideal: size(C)=4, plain dual1, theta dual4, ambient16; ER reproduces31/35 historical failures |
| D06 | Therefore the plain product is elementwise degenerate / all opposite-sided duality invalid | **INCORRECT** | Identity probe is nondegenerate; S Prop2.3 gives correctly sided annihilator theory. “Degenerate” requires qualification |
| D07 | C^perp_k is a right R-module, cyclic when C is cyclic | **VERIFIED UNDER CONDITIONS** | S Thm3.4/3.7; correct right law and B(x,Ty)=B(T^-1x,y) |
| D08 | λTr ring-orthogonal equals scalar-orthogonal | **VERIFIED UNDER CONDITIONS** | C must be right R-module; S Prop4.1. E3 non-module subspace gives dimensions2 versus3 |
| D09 | size(C)·size(C^perp_k)=size(R)^n, dimensions sum to N | **VERIFIED UNDER CONDITIONS** | S Thm3.5; module-side scalar equality/perfect Gram form, not nondegeneracy alone |
| D10 | Same-convention double dual is **+σ_2k(C)** | **VERIFIED UNDER CONDITIONS** | S Thm3.6; apply θ to B=0 then size. E1 F8 brute force distinguishes positive/negative/C |
| D11 | Same-twist double dual is always C | **INCORRECT** | E1 explicit F8 slope ideal: DD≠C. General result is D10 |
| D12 | Universal reflexivity iff m divides2k | **VERIFIED UNDER CONDITIONS** | r≥2 and universal quantifier; S Thm3.9 slope proof. Thm3.6's short necessity sketch alone is insufficient |
| D13 | For an individual code, inclusion in DD implies equality and holds iff σ_2k(C)=C | **VERIFIED UNDER CONDITIONS** | Finite equal cardinality. Particular invariant codes can be reflexive when global duality is not |
| D14 | Left mirror Σx_i θ(y_i) can inherit the positive DD and same linearity unchanged | **INCORRECT** | It is a valid different left convention with **negative σ_-2k DD**; S's positive mirror is Σy_i θ(x_i). E2 brute-force distinction |
| D15 | A-valued trace candidate is fully reconciled with the same k P1/P2 dual | **INCOMPLETE** | Its correct right-action identity and scalar comparison involve **−k**, not automatic +k. Pairing audit §6; original sketch uses the wrong side |
| D16 | Cyclic dual equals reversal of the right annihilator of θ(C) | **VERIFIED UNDER CONDITIONS** | Central-variable quotient; Stage2C Thm3.8, cyclic/right conventions required |
| D17 | Hull is a cyclic right module, σ-equivariant, self-orthogonal; dual-hull formula uses σ_2k(C) | **VERIFIED UNDER CONDITIONS** | S Thm3.8, M05 `thm:hullstruct`; intersection arguments; no reflexivity needed for hull self-orthogonality |
| D18 | A nonprincipal self-dual hull exists at (4,2,2) | **VERIFIED** | S3B §7 explicit witness; E1 dimW4, dimradW1, μ3>2, dimC8, self-dual for k0,1 |
| D19 | M05 i0,dimU2 “direct-sum” family has μ3 | **INCORRECT** | E2 intersection dimension1; actual sum dimension5, radical dimension3, μ2. Does not refute D18 |
| D20 | Full hull-μ distributions / all additional wild-family witnesses are independently established here | **COMPUTATIONALLY SUPPORTED ONLY** | Historical S3B/Phase6 data; not a new independent full census. Only D18 and focused representation checks recertified |
| D21 | Phase5 D3 hrows→unpair computes the hull Morita generator number correctly | **INCORRECT** | Script lines1364–1368 uses wrong-length row representation; E3 reproduces wrongμ4 vs correctμ3; Phase6 already warns/fixes this route |

## 5. Claim ledger — Gray evidence and form changes

| ID | Claim as audited | Classification | Evidence / decisive qualification |
|---|---|---|---|
| G01 | Coefficient Gray map is an Fq-linear bijection to Fq^N | **VERIFIED UNDER CONDITIONS** | Fixed matrix/u/position ordering; G T176; not automatically R-linear |
| G02 | Transported scalar Gram matrix J=I_(r²n)⊗H_t | **VERIFIED UNDER CONDITIONS** | G T177; top-coefficient calculation; E1 direct matrix/trace calculation |
| G03 | φ(C^perp_k)=φ(C)^perp_(k,J) | **VERIFIED UNDER CONDITIONS** | Right-module scalar equality + specified map/form; G T178; not arbitrary Gray maps or Euclidean target |
| G04 | Gray map carries hull to transported-hull intersection even if nonprincipal | **VERIFIED UNDER CONDITIONS** | Injectivity plus G03; G T179 |
| G05 | Coefficient/Hamming isometry and stated ring-weight inequalities | **VERIFIED UNDER CONDITIONS** | G T180; coefficient metric, not symbol-Hamming/homogeneous metric |
| G06 | Normalized nonintegral homogeneous weight has no ordinary Hamming isometry | **VERIFIED UNDER CONDITIONS** | G T181/T182, stated normalization and source character-sum identity; not all rescalings settled |
| G07 | Image is QC of index tr² (4t at r2), not generally cyclic | **VERIFIED UNDER CONDITIONS** | G T183; transported block shift |
| G08 | Transported form is literally Euclidean iff t1 and σ_k=id | **VERIFIED UNDER CONDITIONS** | G T184 and E1 Euclidean-dual counterexample outside that corner. This literal-form statement does not forbid a particular code from also satisfying an ordinary-Euclidean inclusion |
| G09 | Characteristic2/even-t **bilinear** form not congruent to I | **VERIFIED UNDER CONDITIONS** | G T185, M06 definition restricts σ=id; alternatingness invariant under ordinary congruence |
| G10 | Same obstruction rules out all Hermitian/sesquilinear congruences | **INCORRECT** | E1 explicit F4 T has σ(T)^T H2 T=I, but T^T H2 T≠I; no Hamming isometry claimed |
| G11 | Zero diagonal means alternating for all characteristics/form types | **INCORRECT** | E2 F9 bilinear and F4 Hermitian self-values nonzero; M06 statement is overbroad |
| G12 | Displayed Phase5 GF9 T is a Hermitian congruence | **INCORRECT** | E2 T^THT=I but σ1(T)^THT≠I. Valid bilinear scope remains |
| G13 | The463-check suite supplies finite experimental support for its tested Gray scopes | **COMPUTATIONALLY SUPPORTED ONLY** | ER exactly reproduces log,311EXH/152SMP; verified execution does not prove universal Gray/quantum compatibility. G02/G03 need their proof, not the count |
| G14 | Every EXH-labelled pairing/symmetry assertion tested all ambient pairs | **INCORRECT** | Script limits to first120² and50² pairs, even with exhaustive ambient enumeration |
| G15 | Script reflexivity header uses a meaningful m divides2k test | **INCORRECT** | Line982 uses m%gcd(m,2k)==0, always true; actual line1026 C5 test is correct. Do not claim the C5 checks are tautologies |
| G16 | Fq-valued scalar form has θ(matrix)-semilinear scalar output for arbitrary R multipliers | **INCORRECT** | G §0.2 type mismatch; only central-field scalar sesquilinearity is valid |
| G17 | Lack of an ambient Euclidean congruence prohibits every code-specific CSS inclusion | **INCORRECT** | Nonzero Euclidean-SO codes occur in original Gray log; code-specific inclusion must be tested, not inferred from ambient classification |

Detailed calculations, scope distinctions and execution evidence appear in [GRAY_MAP_EVIDENCE_AUDIT.md](GRAY_MAP_EVIDENCE_AUDIT.md).

## 6. Claim ledger — quantum constructions, certification and reporting

| ID | Claim as audited | Classification | Evidence / decisive qualification |
|---|---|---|---|
| Q01 | Trace-symplectic isotropic labels with a phase-correct scalar-free stabilizer lift yield the standard dimension/distance rule | **VERIFIED UNDER CONDITIONS** | Actual isotropy, phase lift and nontrivial code conventions required; Fp commutation basis or equivalent Fq value tests |
| Q02 | Printed Weyl relation X(a)Z(b)=χ(+Tr(ab))Z(b)X(a) with the stated operators | **INCORRECT** | M07 LemmaQ1; direct action gives **negative** sign. E2 p3 witness; zero commutation criterion is unaffected |
| Q03 | LemmaQ2 gives joint-eigenspace dimension q^N/size(C) for arbitrary additive C without isotropy/lift conditions | **INCORRECT** | E2 C=F2²,N1 would give1/2 dimension, while X and Z do not commute. The ±S/anti-commutes language also fails as general odd-p statement |
| Q04 | R1 graph from a transported-self-orthogonal D gives K=N−k | **VERIFIED UNDER CONDITIONS** | M07 `thm:R1`, pairwise vanishing and correct phase convention. Graph only Fp-linear in general; use trace orthogonal |
| Q05 | M07 final parameter theorem can use Fq-symplectic orthogonal for all routes, including R1 | **INCORRECT** | E3 explicit R1 example has trace-orthogonal labels not Fq-orthogonal. It also uses wrong V for un-relabelled DC |
| Q06 | Euclidean SO/DC CSS parameters and respective distance differences | **VERIFIED UNDER CONDITIONS** | M07 `thm:R2`: SO requires D⊂D_E^perp, DC requires D_E^perp⊂D. E28 checks actual inclusions |
| Q07 | All28 supplied field-generator records have their claimed exact parameters/distances | **VERIFIED** | E28 independent arithmetic,24 complete enumerations+4 complete support searches. Finite records only; no optimality claim |
| Q08 | EA c=k−h_E, K=N−k−h_E, d=min wt(D_E^perp\Hull_E(D)) | **VERIFIED UNDER CONDITIONS** | Fq-linear D; standard Bob completion. Independent Gram-rank/Bob cancellation for E28; proof explained below |
| Q09 | M07 R3 proof's hyperbolic decomposition and “v⊗I fixes codespace” steps | **INCORRECT** | V is nonisotropic when c>0; hyperbolic pairs must both occur in its nondegenerate part, and Bob completion is essential. This does not refute Q08 |
| Q10 | EA entanglement count can use the transported Galois hull h_k with no further bridge | **INCORRECT** | Q08 uses **ordinary Euclidean h_E**. Gray preservation is for J/k; no automatic equality with h_E |
| Q11 | EA/SO relative distance equals the minimum nonzero **coset-leader** weight in the appropriate quotient | **VERIFIED UNDER CONDITIONS** | M08 valid metric portion; target and excluded subspace must match the route; positive quotient dimension |
| Q12 | That quotient is automatically an ordinary length-N Hamming linear code with representative-independent coordinate weights | **INCORRECT** | E3 same coset001+span(110) has representatives001,111 of weights1,3. Coset-leader metric is different |
| Q13 | M08 uses D_E^perp/H_E and K=N−k−h_E for R2-DC with the original D | **INCORRECT** | Supplied DC N20,k12,h8 has actualK4,d4, but that quotient has dimension0. Need D/D_E^perp or explicit D relabelling; scope JSON |
| Q14 | K+d≤N+1 for the correctly chosen positive-dimensional relative quotient | **VERIFIED UNDER CONDITIONS** | A linear complement plus ordinary Singleton proves it; manuscript's raw projection on cosets is not well-defined without a quotient codomain |
| Q15 | This elementary relative-quotient bound is a verified new/independent novelty contribution | **UNVERIFIABLE** | No sufficient priority/literature proof; source's “ordinary quotient code” argument is defective |
| Q16 | EA identities K−c=N−2k and c+K=N−2h_E hold for **all** R1/SO/DC routes with the original D | **INCORRECT** | M08 `thm:bookkeeping`; E3 R1 N8,k4,K4,c0 contradicts first; supplied DC N20,k12,K4,c0 gives4≠−4. EA/SO/relabelled conventions need separation |
| Q17 | Historically every one of28 examples ran all three distance methods | **INCORRECT** | Phase16/source logic: M1 completes24, M2 fallback4, M3 all28 (11exact/17lower). Later staged §08 already corrects this; canonical/log retain false text |
| Q18 | Wider120721/5055/4418-exact/637-lower/frontier counts constitute independently proved completeness here | **COMPUTATIONALLY SUPPORTED ONLY** | Inherited census/search scope, partly re-executed original pipeline; not independent full recertification. Blocked/count-only/sampled families remain excluded |
| Q19 | Legacy Grassl q4/q9 headers can be relabelled physicalq4/q9 | **INCORRECT** | B01/B02 actually physicalq2/q3. B03 gives physicalq4 N20,K4 bound7..8; old record/gap labels invalid |
| Q20 | Physicalq8 stabilizer tables and EA tables do not exist | **INCORRECT** | B04/B06 physicalq8 probe; B07 actual EA qubit/qutrit tables. No same-q4/8/9 EA optimality follows |
| Q21 | A first q8 EA application remains wholly unimplemented in the campaign | **INCORRECT** | Four supplied q8 EA records independently pass; twist-specific differentiation still an open proposal |
| Q22 | P1/P2/P3 new theorem programs are already proved/ready to implement without a new gate | **INCOMPLETE** | P1 overlaps; P2 needs μ>3/index9t/structural novelty; P3 needs valid Ore quotient and compatibility theory. None authorized |
| Q23 | Q1 viability, firstness, full external nonoccupation, actual FFA submission/acceptance | **UNVERIFIABLE** | Bounded literature/current sources do not establish these. Author confirmation and further authorized review required |

## 7. Quantum proof audit — distinguish correct formulas from incorrect proofs

### 7.1 Weyl and stabilizer discipline

For the manuscript's definitions, acting on |v⟩ directly gives
\[
Z(b)X(a)=\chi(\operatorname{Tr}(a\cdot b))X(a)Z(b),\quad
X(a)Z(b)=\chi(-\operatorname{Tr}(a\cdot b))Z(b)X(a).
\]
The sign error disappears in characteristic2 and does not change the **zero trace** commutation condition, but it invalidates the printed first relation at odd characteristic. Q2 also needs a trace-isotropic label space and an appropriate stabilizer subgroup with no nonidentity scalar; mere additive closure is insufficient. Odd-p phases are not limited to ±1, and “does not commute” is not synonymous with “anti-commutes.”

For an Fq-linear label space, testing **Fq-valued symplectic products equal0** on an Fq basis is valid. Testing only their **traces** on that basis is not generally enough; scale through an Fp basis or use trace nondegeneracy. The R1 graph is only Fp-linear in general, so its trace-orthogonal cannot silently be replaced by its Fq-value orthogonal. E3 gives an explicit counterexample with D=φ(uM2(F4[u]/u²)), N8. This diagnoses an incorrect formula, not a proved wrong minimum distance for all R1 codes.

### 7.2 The valid EA mechanism and the defective printed one

Let V=D⊕D with the standard symplectic form, and H=Hull_E(D). Then
\[
\dim V=2k,\quad\operatorname{rad}(V)=H\oplus H,\quad
\dim\operatorname{rad}(V)=2h_E,\quad\operatorname{rank}(\omega|_V)=2(k-h_E)=2c.
\]
The **nondegenerate part of V contains both members of c hyperbolic pairs**, plus its radical. A Bob space of c qudits supplies the opposite symplectic form, making the extended label space isotropic. With a phase-correct stabilizer lift, its dimension is2k in an N+c-qudit ambient space, so
\[
K=N+c-2k=N-k-h_E.
\]
Alice-only errors commute with all extended generators precisely when their Alice label belongs to V^perp. Alice-only stabilizer labels are the radical. Thus the undetected logical labels are
\[
V^{\perp}\setminus\operatorname{rad}(V)
=V^{\perp}\setminus V,
\]
where the equality uses V∩V^perp=rad(V). For V=D⊕D the symplectic minimum is exactly the classical difference in Q08.

This is a check of the existing construction under the necessary standard hypotheses, **not** support for the manuscript's false claim that all unextended v⊗I for v∈V fix the code. The independent arithmetic factorizes the Gram commutator and verifies Bob cancellation for the supplied matrices; it is not a Hilbert-space simulation or an independent universal quantum theorem.

### 7.3 Relative quotient and route bookkeeping

For EA and SO, put E=D_E^perp and H=Hull_E(D); for DC use E=D and H=D_E^perp. With K=dim(E/H)>0,
\[
d=\min\{\operatorname{wt}(x):x\in E\setminus H\}
\]
is the minimum **coset-leader** weight of E/H. It is not the Hamming weight of an arbitrary chosen representative. Ordinary coordinate projection is not a well-defined map from E/H to a coordinate vector space unless a compatible quotient/restriction is specified.

The inequality K+d≤N+1 nevertheless follows: choose an Fq-linear complement T to H in E. Every nonzero vector of T lies outside H, so d(T)≥d. Ordinary Singleton on the length-N code T of dimension K gives d≤d(T)≤N−K+1. This validates the restricted inequality without validating the source's proof or priority claim. It also does not make every quotient an isometric ordinary Hamming code.

The EA identities in Q16 are valid for EA and the SO specialization. For DC one can relabel the stabilizer input to D_E^perp, but one cannot keep k=dim(original D) and use the same equations. R1 instead has c0,K=N−k. These are substantive scope errors in canonical **and** latest staged §08; the later certification-method correction does not fix them.

## 8. Cross-report consistency result

The six reports agree on the broad intended framework, positive twist, coefficient Gray transfer and internal duplication. They do **not** form a fully consistent theorem package:

- Pairing Options abbreviates the right action incorrectly and uses an invalid probe; Ring Feasibility overstates base-ring nonprincipality.
- Ring Feasibility/Decision carry a stale principality obstacle despite S2B's proved criterion.
- “463/463” and “550+ checks” are not evidence that all later Gray/quantum proofs were rerun or valid; exact rerun scope is ER.
- Gray/form assumptions cannot be transferred to ordinary Euclidean CSS without verification.
- Research Gap/Decision promise a first q8 EA layer despite included examples, use wrong r3 threshold/index/complexity language, and infer unsupported novelty risk.
- The manuscript exists but contains the independent defects above. Its existence proves overlap with the blueprint, not immediate submission-readiness.

The explicit source/correction trail is maintained in [DISCREPANCY_AND_CORRECTION_REGISTER.md](DISCREPANCY_AND_CORRECTION_REGISTER.md). None of the original materials was silently changed. No Phase1 or new P1/P2/P3 theory was started.
