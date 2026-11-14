# Core A — theory and fresh computation, review M8

The [candidate formulas](CORE_A_CLOSED_FORMULA_THEOREM.md), conventional derivation, numerical checks and independent acceptance are different evidence classes. No finite table establishes universality or novelty. This report **does not** promote q32/q64 geometry to a code census. Old outputs and the earlier comparison remain unchanged.

## 1. Fresh exhaustive q16 comparison — actually rerun

Run: [finalisation_m8_distribution_v1](../../computations/results/finalisation_m8_distribution_v1/summary.json), using the unchanged `verify_core_a_distribution.py`.

- **166,521 distinct embedded inputs**: 87,895 radical, 78,625 residue-rank-one, one full ambient.
- Every twist s=0,1,2,3: **666,084 complete generic-versus-structural hull-space comparisons**, not merely dimensions.
- Canonical inputs are deduplicated and checked for u,w closure. Input/hull minimum-generator counts and full hull bases agree.
- This is a fresh execution of the descriptor-based exhaustive census, not a new proof that the descriptors exhaust the family. That exhaustion has its own candidate argument P06–P14. It is not enumeration of every ambient k-subspace at q16.

|s|g,Q,r|Candidate (N0,N1,N2,N3)|Fresh exhaustive observation|Result|
|---|---|---|---|---|
|0|4,16,1|(65538,29730,71252,1)|(65538,29730,71252,1)|Exact match|
|1|1,2,4|(57346,33490,75682,3)|(57346,33490,75682,3)|Exact match|
|2|2,4,2|(49154,48386,68976,5)|(49154,48386,68976,5)|Exact match|
|3|1,2,4|(57346,33490,75682,3)|(57346,33490,75682,3)|Exact match|

Every row sums to166,521. The three **disjoint μ1 input strata** also agree separately:

|s|Primitive: theory / fresh|Radical K-line: theory / fresh|Radical K=V: theory / fresh|
|---|---:|---:|---:|
|0|12833 /12833|8737 /8737|8160 /8160|
|1|20345 /20345|8225 /8225|4920 /4920|
|2|27233 /27233|7713 /7713|13440 /13440|
|3|20345 /20345|8225 /8225|4920 /4920|

Complete q16 case stream SHA-256 (bulk not stored): `3a7417fd6536629e6aff17dc1bbd4a8deb1f2d62e5afc66f51f523d0aeca28d2`.

The fresh summary SHA-256 is `1c46baab6e7ae0ab5fe4a3291a0248d97fd79a4b7a4405eb54c9aeccb09c72ac`, identical to the untouched M5 summary. All four new census files are byte-identical to their deterministic predecessors **because they were rerun**, not copied. The [rerun comparison receipt](../../evidence/M8_REGRESSION_COMPARISON_V1.json) records that identity for every file.

## 2. Fresh small-field foundational and full-census regressions

|Fresh run|Actual coverage|Limit|
|---|---|---|
|`finalisation_m8_foundations_v1`|All65,536 q2 generating matrices,137 principal-input modules;240 stratified sampled generating matrices per q4/q8/q16,2,160 twist cases;72 named controls;scalar ideals and correct functional/double-twist tests|q2 is auxiliary outside m≥2; these q4/q8/q16 samples are not full censuses|
|`finalisation_m8_foundations_audit_v1`|All417,199 q2 ambient RREF subspaces filtered by B-actions give159 modules,137 principal;112 original-global cases and actual scalar-functional checks|Independent arithmetic implementation, not an independent reviewer; core global cases here are selected|
|`finalisation_m8_structure_v1`|All159 q2,1,221 q4,12,993 q8 modules and all respective twists:41,580 full generic/structural cases|Includes159 auxiliary q2 cases; this driver itself does not exhaust q16|
|`finalisation_m8_structure_global_v1`|All2,442 q4 original-global cases plus87 named norm-line family cases across q4/q8/q16|q8/q16 family checks are not full global censuses|

Fresh complete structural histograms:

|q,s|Candidate and fresh observed (N0,N1,N2,N3)|Inputs per twist|
|---|---|---:|
|2,0|(18,78,62,1)|159, auxiliary|
|4,0|(258,522,440,1)|1,221|
|4,1|(130,538,550,3)|1,221|
|8,0|(4098,3858,5036,1)|12,993|
|8,1 and2|(4098,3534,5360,1)|12,993 each|

The inherited Stage3B q4 log already recorded these q4 μ histograms; they are not new discoveries. The earlier 500-input samples in that same log remain samples, while its later exhaustive scan is separately identified in the [input inventory](CORE_A_INPUT_INVENTORY.md).

## 3. Fresh separate raw geometry and original-global checks

`finalisation_m8_distribution_audit_v1` uses alternative field tables/row restriction and no primary field/module/descriptor/hull code. It shares the integer prediction function, so agreement is with separately enumerated **raw** geometry, not a second assertion of the same integer formula.

- **334,413 all-T/twist cases**, T≤k⁴, at q4/q8/q16 and all twists: actual isotropic-point count, rank2 point count U, all self-dual-plane intersection types, incidence F and K=V μ1 count.
- **176 selected q16 original-global cases**, rebuilt by original right polynomial matrix products and every coordinate of the actual matrix-valued form. Complete dual/hull spaces match within the alternative route; saved primary dual/hull spaces match too. They are every4,096th input/twist plus all12 exceptional μ3 input/twist cases. This is **not a full q16 global census**.

|q,s|U: theory / observed|F: theory / observed|K=V μ1: theory / observed|
|---|---:|---:|---:|
|4,0|60 /60|300 /300|120 /120|
|4,1|24 /24|72 /72|96 /96|
|8,1 or2|72 /72|84 /84|708 /708|
|16,0|4080 /4080|69360 /69360|8160 /8160|
|16,1 or3|276 /276|324 /324|4920 /4920|
|16,2|960 /960|4800 /4800|13440 /13440|

Raw geometry SHA-256: `2570268bf64f82f7bde2cf014caa9848195da6eaddd1de6a9c7b2a93886886d6`.

Fresh selected q16 global output SHA-256: `0b235bf6542ed719ec43677ea251545e20350c49c79ee53cb9e09cbb729768fc`.

## 4. q32/q64 are geometry-only, exactly as before

Freshly rerun higher geometry: **q32 s1,2,3,4; q64 s1,2,4,5 only**. Enumerates1,200,520 projective-point field/twist cases and all descended two-plane candidates; checks fixed fields, self-duality, U, plane types and F. Field tables receive294,912 exhaustive distributivity triple checks.

`finalisation_m8_proof_v1` additionally reruns the same17 trace-direction/graph-chart field/twist cases, including those higher twists. q64 s0/s3 are not added. These executions do **not** enumerate all T at q32/q64, all B² modules, all codes or every twist. The standalone directed-flag checker does not change higher-field scope; it runs at q4/q8/q16 only.

## 5. Proof-route, scalar-QC and newly standalone checks

|Fresh run|Actually completed checks|Dependence / limitation|
|---|---|---|
|`finalisation_m8_proof_v1`|5 exact sparse polynomial identities;2,080 integer formula pairs m1…64;17 trace/graph geometry cases;4,608 original-global coefficient/shift basis checks;all2,442 q4 and176 selected q16 global cases;explicit q8,s1 nonreflexive double dual|This driver still intentionally reads the old census/geometry files. The M8 full census was separately rerun in §1 and both old/new files are byte-identical. Integer pairs are not field censuses.|
|`finalisation_m8_scalar_qc_v1`|Same2,442 q4/176 q16 object sets via scalar A-valued QC;complete hulls and176 exported duals;closure,radical-quotient μ;1,152 basis/constant/shift tests|Shares alternative field/row/global helper with the previous audits. No primary arithmetic imported; not wholly dependency-independent software, a Gray isometry or extra distinct codes.|
|`finalisation_m8_directed_flags_v1`|**New**, no repository-code imports:101,316 actual directed two-plane flags over all q4/q8/q16 twists;all right radicals;304 Hermitian graph matrices;four nonreflexive wrong-hyperplane witnesses|Additional finite implementation separation only, not independent complete-proof acceptance or a B²/global census.|
|`finalisation_m8_split_boundary_v1` and `finalisation_m8_split_global_boundary_v1`|41 named original-global split-length boundary cases;inverse-Frobenius/reversal negatives;the same q4,n6 input has hull dimensions12/4 and matrix generator counts2/1|Out-of-Core-A boundary regression only; does not extend the length2 theorem or claim a larger-length census.|

Proof-route global complete-basis stream SHA-256: `007b4e2ca7166f7ecda7c29e19b172f5b02874a51ed3c361c5ce716b3412c6c9`.

QC complete-basis stream SHA-256: `c64cfd97e5aeb0c14a78e7d56d61a3255974b679f89e4f0d52053baaba4d0f39`.

New directed-flag records SHA-256: `bf78c38aee1dcc4075f552decd747e443661f0cebc08c96eacf3005394eabf8a`.

All **10 reruns /39 saved files** reproduce their preserved predecessor bytes exactly. The additional standalone run has four new saved files. These counts are file/run provenance, not new distinct-code counts or proof certificates. No recorded M8 regression failed.

## 6. Reproduction and acceptance limits

All drivers require fresh labels; do not use `-O`. Standard library only, no source edits needed. For example:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_core_a_distribution.py NEW_CENSUS_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_distribution.py NEW_CENSUS_LABEL NEW_GEOMETRY_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_closed_formula_proof.py NEW_PROOF_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_scalar_qc.py NEW_QC_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_directed_flags.py NEW_DIRECTED_FLAG_LABEL
```

The last command intentionally reads the two named fresh M8 distribution/geometry result paths, already preserved in this checkpoint; it creates only its new result directory. The proof/QC drivers retain their older data paths. Input and source hashes identify the exact dependencies, not merely descriptive labels. The remaining foundational/structural/boundary commands and all exact fresh/predecessor identities are in the machine receipt and computation README.

No new execution supplies an independent reviewer or a formal derivation of the complete theorem. The [current status](CORE_A_PROOF_STATUS_REPORT.md) keeps that gate open, and the [primary-source assessment](CORE_A_PRIMARY_SOURCE_NOVELTY_ASSESSMENT.md) separately withholds originality.
