# Discrepancy and correction register

**Audit execution:** 2026-11-13 UTC (workspace clock). **Append-only review layer: no original material corrected or overwritten.** All actions below are **proposed future corrections**, not implemented manuscript/data revisions and not permission to start Phase1.

Severity: **BLOCKING** prevents a submission-ready/unqualified theory verdict; **HIGH** affects correctness, applicability, interpretation or reproducibility; **MEDIUM** affects wording/provenance/diagnostics. Classification uses the six required labels and applies to the exact disputed claim, not to every result in its source. Claim IDs refer to [MATHEMATICAL_CLAIM_VERIFICATION.md](MATHEMATICAL_CLAIM_VERIFICATION.md).

## A. Algebra, pairing and structure

| ID / severity | Original location and disputed claim | Classification | Independent evidence / impact | Proposed correction, only if later authorized |
|---|---|---|---|---|
| CR01 HIGH | Pairing Options P1: B(ax,y)=θ(a)B(x,y) | **INCORRECT** | D02; E12/E21 gives E11≠E22. Detailed S Prop2.1 correctly uses xa | Use the right action **B(xa,y)**; keep source-versus-summary distinction |
| CR02 HIGH | Same summary: E_ba probe proves nondegeneracy | **INCORRECT** | D04; xE12,yE21 yields0 after transpose. Nondegeneracy itself survives | Replace proof sentence using nonzero coordinate/identity probe, not a blanket theorem withdrawal |
| CR03 MEDIUM | P0 called “degenerate” without distinguishing elementwise from module-perfect duality | **INCORRECT** | D05/D06: identity probe nondegenerate; same-sided size fails4×1≠16 | Say plain product fails the desired same-right-module perfect duality; acknowledge valid opposite-sided annihilator theory |
| CR04 HIGH | Summary left mirror Σxθ(y) inherits positive DD/linearity unchanged | **INCORRECT** | D14; E2 brute-force F8 gives **−2k** twist for this valid alternate | Fix convention explicitly; positive mirror is Σyθ(x); do not call the alternate intrinsically invalid |
| CR05 HIGH | Scalar/ring orthogonal equality read without the right-module hypothesis | **INCORRECT** | D08; non-module F4E11 subspace gives ring/scalar dual dimensions2/3 | State right-R closure and ideal-catching step wherever equality is used |
| CR06 HIGH | A-valued candidate P3 fully equivalent at the same +k, with left-action sketch | **INCOMPLETE** | D15; correct right-action comparison uses **−k**, after λ and σ | Reconcile orientation/side before any use; do not relabel the candidate a new theorem |
| CR07 HIGH | Ring Feasibility §2: most base-R one-sided ideals nonprincipal | **INCORRECT** | F06; chain Morita modules need≤r generators; all base ideals principal | Separate base R=M_r(A) from cyclic R_n=M_r(B); principal does not mean free |
| CR08 HIGH | Ring Feasibility §7 / Decision O1: general principality criterion still open | **INCORRECT** | F09; S2B Thm4.1/4.3/Cor4.4 already proves r2 criterion **t1 OR p∤n** | Update status with theorem/hypotheses; retain genuinely unresolved finer hull/classification questions |
| CR09 HIGH | M05: every submodule of a chain-ring free module is free | **INCORRECT** | F11; uA cardinality4 versus size(A)=16 | Use at-most-r generation, not freeness, in principality arguments |
| CR10 BLOCKING | M05 `thm:nonprincipal`: i0,U=socle(B²),dimU2 gives a direct sum and μ3 | **INCORRECT** | D19/E2: intersection1, actual dimension5/radical3, **μ2**. Valid S3B hull witness remains | Replace/withdraw this proof family in a separate authorized revision; cite/prove an actual explicit witness; recertify other asserted wild witnesses |
| CR11 HIGH | Phase5 TaskD3 hrows→unpair yields hull μ; manuscript μ4/μ3 explanation suffices | **INCORRECT** | D21/E3 reproduces length16 versus8 error, wrongμ4 versus correctμ3 on known hull; Phase6 already fixes it | Do not use faulty Phase5 μ distributions; isolate corrected implementation/evidence, distinguish code μ from hull μ without hiding the bug |
| CR12 MEDIUM | S Thm3.6 necessity sketch alone proves universal reflexivity | **INCOMPLETE** | A changing vector need not generate a changing module; S Thm3.9 slope proof is sound | Point to the correct slope-module proof; do not alter **+σ_2k** DD or reject valid criterion |

## B. Gray transport, congruence, computation

| ID / severity | Original location and disputed claim | Classification | Independent evidence / impact | Proposed correction, only if later authorized |
|---|---|---|---|---|
| CR13 HIGH | Unrestricted characteristic2/even-t obstruction applied to Hermitian twists | **INCORRECT** | G10/E1 explicit F4 σ(T)^T H2T=I. Canonical M06's **bilinear** definition is restricted and valid | Separate ordinary bilinear and σ-Hermitian congruence. No weight-isometry conclusion from the counterexample |
| CR14 HIGH | M06: zero diagonal / even t automatically means alternating for all q/forms | **INCORRECT** | G11/E2: F9 bilinear self-value2; F4 Hermitian self-value1 | Qualify by characteristic and bilinear versus Hermitian form type |
| CR15 HIGH | Phase5 GF9 displayed T serves as a Hermitian congruence | **INCORRECT** | G12/E2: T^THT=I, σ1(T)^THT≠I | Restrict that matrix to its proved bilinear use; recompute any use outside that scope |
| CR16 HIGH | M06 no ambient Euclidean congruence ⇒ no Euclidean/CSS route for any code | **INCORRECT** | G17; original Gray data contains nonzero Euclidean-SO codes | Limit to ambient-form equivalence; test each code's actual ordinary-Euclidean inclusion |
| CR17 MEDIUM | Gray document §0.2 scalar form law multiplies scalar output by arbitrary matrix | **INCORRECT** | G16; Fq-valued codomain makes that identity type-invalid | Use central-Fq scalar sesquilinearity; keep arbitrary-matrix rule at ring-valued B level |
| CR18 MEDIUM | Gray script header `r%gcd(r,2s)==0` is a reflexivity test | **INCORRECT** | G15; tautology at line982. Actual C5 `2s%r==0` is correct | Correct the diagnostic in any later code revision; do not falsely invalidate the actual C5 assertions |
| CR19 HIGH | EXH labels mean all ambient pairs tested /463checks prove all parameters | **INCORRECT** | G13/G14; first120²/50² pairs, sampled families,311EXH+152SMP | Report literal quantifiers/budgets; keep proof separate from finite evidence |
| CR20 HIGH | Generator JSONs/README point to `matrix_ring_lib` integer field encoding | **INCORRECT** | E2: wrong GF8/GF9 modulus labelling changes dual calculations in **5/15** tested q8/q9 records | Publish actual `ring_structure_checks.Field` bases or an explicit conversion; data matrices verified under actual encoding remain valid |
| CR21 HIGH | All wider search/census outputs independently certified by this review | **COMPUTATIONALLY SUPPORTED ONLY** | E28 independently covers28records, ER regenerates those via original pipeline; not an independent120721/5055 re-audit | Bound all numerical claims to actual enumeration/sampling and verification scope |

## C. Quantum proofs and route-scoping

Both canonical and latest staged §07 retain the same substantive proof defects; their only difference there is exponential typesetting. Later staged §08 **does** fix certification-method wording, but not its quotient/route/bookkeeping errors. The exact [source-variant diff](evidence/manuscript_variant_comparison.diff) and [source hashes](evidence/manuscript_variant_comparison.json) preserve that distinction.

| ID / severity | Original location and disputed claim | Classification | Independent evidence / impact | Proposed correction, only if later authorized |
|---|---|---|---|---|
| CR22 HIGH | M07 LemmaQ1 uses plus sign in XZ=χ(ab)ZX for stated operators | **INCORRECT** | Q02/E2 odd-p action gives minus sign; zero commutation relation unaffected | Correct sign consistently; rerun odd-characteristic phase tests; do not infer all q9 parameter rows are false |
| CR23 BLOCKING | M07 LemmaQ2 gives common eigenspace/distance for arbitrary additive labels; uses ±S/anti-commutes generally | **INCORRECT** | Q03/E2 nonisotropic F2² example gives claimed dimension1/2. Odd-p phases not just±1 | State isotropy, scalar-free phase-correct stabilizer lift and code-space hypotheses; use appropriate nonbinary commutation/Knill–Laflamme formulation |
| CR24 BLOCKING | M07 R3 proof's hyperbolic decomposition and v⊗I fixing the code | **INCORRECT** | Q09; nonisotropic V cannot have the asserted isotropic span. Bob correction essential | Supply a correct Bob-completed stabilizer argument and distinguish Alice-only stabilizer radical. Parameter formulas Q08 survive under correct construction |
| CR25 BLOCKING | M07 `thm:parameters`: all routes use Fq-value orthogonal; R2 always uses V of original D | **INCORRECT** | Q05/E3 trace-only R1 orthogonal larger; DC uses D_E^perp⊕D_E^perp | Keep R1 trace/Fp convention; branch SO/DC group definitions explicitly |
| CR26 HIGH | Proposed EA application reads c from transported h_k automatically | **INCORRECT** | Q10; standard Euclidean EA formula uses h_E; Gray theorem targets J/k | Prove a bridge or compute ordinary h_E directly; no automatic Galois-hull substitution |
| CR27 BLOCKING | M08 `thm:cosetdistance`: same D_E^perp/H_E and K for DC with original D | **INCORRECT** | Q13; supplied DC N20,k12,h8,actualK4,d4 gives quotient dimension0 | DC uses D/D_E^perp, or explicitly relabel the stabilizer input; reconcile every dependent parameter statement |
| CR28 HIGH | M08 quotient is an ordinary length-N Hamming code; raw projection on cosets proves Singleton | **INCORRECT** | Q12/E3 coset reps weights1/3; projection not representative-independent. Restricted inequality Q14 can be proved by a linear complement | Describe coset-leader metric, correct proof/codomain, retain only justified route-specific inequality; no automatic novelty claim |
| CR29 BLOCKING | M08 `thm:bookkeeping`: EA identities apply to all R1/SO/DC with original k | **INCORRECT** | Q16/E3 R1:K4 versus N−2k0; supplied DC:4 versus−4 | State separate route formulas; EA/SO specialization valid, DC needs relabelled input, R1 K=N−k,c0 |
| CR30 MEDIUM | Canonical §08 / old log: every record ran all three certification methods | **INCORRECT** | Q17; M1exact24, M2fallback4, M3exact11/lower17. **Staged §08 already corrects this wording** | Keep append-only correction/history, use authoritative staged wording; do not count lower-bound M3 as a second exact distance |
| CR31 HIGH | Additional manuscript wild-witness/headline rows all recertified here | **COMPUTATIONALLY SUPPORTED ONLY** | Explicit S3B witness and28matrix records recertified; additional wild/R1 rows were not independently rederived | Recertify or qualify them in a correction pass; do not extrapolate the valid finite witness to a failed proof family |

## D. Literature, benchmarking, novelty and package claims

| ID / severity | Original location and disputed claim | Classification | Independent evidence / impact | Proposed correction, only if later authorized |
|---|---|---|---|---|
| CR32 BLOCKING | M09 / old benchmark CSVs: legacy q4/q9 bounds are physicalq4/q9 | **INCORRECT** | Q19/B01–B03: actual labels physicalq2/q3; physicalq4 N20,K4 has7..8, suppliedd4 | Retire same-alphabet record/gap labels; rebuild comparison using returned physical q and matching EA resource conventions |
| CR33 HIGH | “q8 not tabulated; no EA table exists (404)” in reports/manuscript/bibs | **INCORRECT** | B04/B06 physicalq8 tables; B07 actual EA qubit/qutrit endpoints | Cite actual endpoints, retrieval dates and alphabet/resource limits. Availability elsewhere is not proved absent by one404 |
| CR34 HIGH | Manuscript Alahmadi DOI `.008` | **INCORRECT** | L14b is unrelated control-systems paper; correct `.023` L14a/L09 | Correct to10.1016/j.jfranklin.2013.06.023 with explicit register, not silent replacement |
| CR35 HIGH | Other metadata: Fan volume85; Andreas Ketkar; Sergio R.Schmidt; Oggier2010/Viterbo | **INCORRECT** | L06 volume84; L17 Avanti; L18 verified S.E.; L19 Oggier–Solé–Belfiore2012 | Correct each exact record; fill confirmed Liu–Pan/Cao/affine/A9b DOI/venue separately; do not attach A9b DOI to A11 |
| CR36 HIGH | “37-entry verified bibliography”, unpublished exact intersection and Q1/LOW-risk assurance | **UNVERIFIABLE** | Inventories/provenance tags overlap; only bounded fresh source check; competitors/internal work overlap | Use precise coverage tags; complete a later authorized literature/technical sweep before priority/ranking claims |
| CR37 HIGH | P1 proposal's “first q8 EA” and application layer absent | **INCORRECT** | Q21: **4 included q8 EA records** pass independently | Require genuinely differentiated twist-dependent application/theorem; do not rebrand existing examples |
| CR38 HIGH | P2 proposal: nonprincipal at μ3, QCindex3, size exponentp18 for m=t2,r3 | **INCORRECT** | F08/G07: principal iffμ≤3; need **μ>3**, index**9t**, size(R)=**p36** | Re-scope around new structure/witnesses/enumeration, not size change |
| CR39 HIGH | P3 Ore quotient/newness/compatibility already ready | **INCOMPLETE** | Q22; quotient ideal must be two-sided (α^n=id sufficient), interaction with θ unproved; search not exhaustive | Require well-defined quotient and compatibility theorem before code/quantum claims; no implementation without author approval |
| CR40 BLOCKING | Immediate submission recommendation / actual FFA status inferred from preparation records | **UNVERIFIABLE** | Q23; no proof of submission/acceptance; blocking corrections remain | Author confirms status, authoritative version and separate correction scope; **HOLD**, not immediate submission |
| CR41 MEDIUM | Current86files alongside87manifest checks | **INCORRECT** | Current88=86nonmanifest+2manifest;87publicationentries excludesitself; historical86 has different footprint | State exact epoch/tree/self-exclusion basis; retain originals unchanged |
| CR42 HIGH |1017targets exist implies every historical reference/source is fully recovered | **INCORRECT** |69omitted/15unavailablecontainer/14unavailablebinary/11inventory/11unresolved/4remote occurrences remain qualified | Report qualified closure and exact exceptions; inventories are not recovered payloads |
| CR43 MEDIUM | Entire earlier campaign/463Gray suite rerun in original Phase0/package build | **INCORRECT** | Original package limitations record only feasibility rerun; current review separately executed3historical reruns | Attribute execution by phase/date; distinguish inherited logs, original-source rerun and independent arithmetic |

## E. This audit's own discrepancies and resolved checker issues

| ID | Issue / classification | What happened and what remains preserved |
|---|---|---|
| A01 | Snapshot date field — **INCORRECT** | `pre_review_snapshot.json` says `review_date=2026-11-12`, but actual capture timestamp is2026-11-13T07:07:51.274681+00:00. Preserve/disclose; new audit execution dates follow recorded workspace clock |
| A02 | First-pass TeX missing-citation diagnostic — **INCORRECT** | Parser retained newline in a cite key. Executed v2 strips whitespace: both variants have **no undefined citations/references**. Initial evidence retained, not attributed to manuscript |
| A03 | First follow-up assertion — **INCORRECT** | An extraneous checker expression failed before producing the final JSON. Fixed checker then passed7focused assertions; initial empty stdout and successful v2 stdout preserved |
| A04 | Initial PDF checker dependency — **INCOMPLETE** | `pdftotext` absent, so first attempt could not run PDF parse. v2 uses locally installed pypdf6.1.1, parses7PDFs and matches actual original members. Dependency install is disposable, not original research data |

## F. What **does not** need to be withdrawn

The following are retained with the precise classifications in the master ledger: the coefficient-Frobenius/transpose anti-automorphism; correct right-module pairing; size law; **positive σ_2k double dual**; conditional universal reflexivity; scalar/Gray transport with module hypothesis; cyclicity and hull intersection; one independently verified nonprincipal self-dual hull; exact463-check reproducibility; and all28 independently recertified supplied field-code records. A blocking proof defect elsewhere is not permission to mislabel these valid results false.

## G. Closure conditions and approval gate

This register is **not** an implemented fix list. Before a submission-ready decision, the author would need to authorize a bounded correction pass, select the authoritative manuscript version, correct/reprove or withdraw blocking items, align scripts/data documentation, recertify affected scope, rebuild physical-alphabet benchmarks, and obtain a new independent check. New theoretical exploration P1/P2/P3 is a **separate** approval.

All1,487baseline originals must remain unchanged in this task; sealing records the comparison in `evidence/final_original_preservation.json`. No commit, push, submission, Phase1 start, or new manuscript drafting is authorized by this audit.
