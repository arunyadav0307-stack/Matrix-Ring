# Core A closed formula — theory/computation comparison

The all-parameter proof and the following finite observations are separate evidence classes. No finite table proves novelty, Q1 suitability or universality. The a74f33f checkpoint and all earlier source/output bytes remain preserved.

## 1. Existing full q16 census versus theorem

Preserved run: `../computations/results/distribution_v1/summary.json`, SHA-256 `1c46baab6e7ae0ab5fe4a3291a0248d97fd79a4b7a4405eb54c9aeccb09c72ac`.

It actually examined all166,521 embedded modules at q16 and all four twists:666,084 complete generic-vs-structural hull-space comparisons. The current proof-finalisation checker reads this as **existing executed evidence**, not as a new rerun.

|s|g,Q,r|Theorem (N0,N1,N2,N3)|Observed full census|Outcome|
|---|---|---|---|---|
|0|4,16,1|(65538,29730,71252,1)|(65538,29730,71252,1)|Exact match|
|1|1,2,4|(57346,33490,75682,3)|(57346,33490,75682,3)|Exact match|
|2|2,4,2|(49154,48386,68976,5)|(49154,48386,68976,5)|Exact match|
|3|1,2,4|(57346,33490,75682,3)|(57346,33490,75682,3)|Exact match|

Every row sums to166,521. The census also checks the three disjoint μ1 strata, not only their sum:

|s|Primitive, theory/observed|Radical K-line, theory/observed|Radical K=V, theory/observed|
|---|---:|---:|---:|
|0|12833 /12833|8737 /8737|8160 /8160|
|1|20345 /20345|8225 /8225|4920 /4920|
|2|27233 /27233|7713 /7713|13440 /13440|
|3|20345 /20345|8225 /8225|4920 /4920|

Full q16 case stream hash (bulk not stored): `3a7417fd6536629e6aff17dc1bbd4a8deb1f2d62e5afc66f51f523d0aeca28d2`. Saved deterministic176-case input stream hash: `e01eab3d2a0d44bfbcb44913da245014f6e46c98f428b968d687da87b546823f`.

## 2. Earlier full small-field evidence

The preserved `structure_v1` run exhausts q2 (auxiliary),q4 andq8; it is not relabelled as a fresh run.

|q,s|Theorem and observed (N0,N1,N2,N3)|Scope|
|---|---|---|
|2,0|(18,78,62,1)|159 auxiliary inputs, outside m≥2|
|4,0|(258,522,440,1)|1,221 inputs|
|4,1|(130,538,550,3)|1,221 inputs|
|8,0|(4098,3858,5036,1)|12,993 inputs|
|8,1 and2|(4098,3534,5360,1)|12,993 inputs each twist|

These are complete structural/generic comparisons in those fields, not all-field evidence. The old q4 global audit is preserved, and q4 global checks are additionally rerun in the new proof-finalisation route below.

## 3. Fresh proof-finalisation execution

Driver: `../computations/verify_closed_formula_proof.py`. Saved run: `closed_formula_proof_v1`. It uses the alternative audit arithmetic, not primary field/module/descriptor code. Integer predictions are compared with an independently assembled formula, raw geometry and original global spaces.

|Check|Actual completed coverage|What it does not imply|
|---|---|---|
|Exact sparse polynomial identities|5 identities: odd/even trace-vector counts, odd/even base-incidence F, full descriptor total|Not a formal proof assistant or a proof of all intermediate geometry|
|Integer formula regressions|2,080 pairs m1…64,0≤s<m; includes explicit expanded N2|Not computations over all those fields or modules|
|New trace/graph route|17 field/twist cases; trace-zero hyperplanes, all projective a-directions, descended-plane projection-rank charts and base/extended incidences|q32/q64 remain geometry only|
|Original global transport|4,608 field-basis/scalar/twist cases at q4/q8/q16, checking both polynomial coefficients and cyclic-shift/global tests|Finite confirmation of the separately proved transport identity|
|Fresh original-global code check|All2,442 q4 cases and176 q16 recorded cases; complete dual/hull spaces inside the alternative global/local route and primary hull bases compared|q16 global check is a subset, not a full global census|
|Nonreflexivity control|Original-global q8,s1 free line slope2 has double dual slope6|Invalidates an involutive-law shortcut, not the actual σ² law|

Fresh original-global complete-basis stream hash (hash only): `007b4e2ca7166f7ecda7c29e19b172f5b02874a51ed3c361c5ce716b3412c6c9`.

Fresh trace/graph records hash: `d5039892c5b218034227875237494d9e345456725de39a792121da489390dc6a`.

Checker source hash: `5525dc37579aa858f1027817eb363a0fa2a6116024c45ec0db305a7ab8a1d148`.

## 4. Earlier independent geometry evidence, carefully scoped

`distribution_audit_v1` exhausts all layer subspaces T≤k⁴ at q4/q8/q16 and all twists:334,413 cases. It checks U, self-dual-plane types, F and the direct K=V μ1 count, using alternative field tables. This is not a second full B² enumeration.

|q,s|U, theory/observed|F, theory/observed|K=V μ1, theory/observed|
|---|---:|---:|---:|
|4,0|60 /60|300 /300|120 /120|
|4,1|24 /24|72 /72|96 /96|
|8,1 or2|72 /72|84 /84|708 /708|
|16,0|4080 /4080|69360 /69360|8160 /8160|
|16,1 or3|276 /276|324 /324|4920 /4920|
|16,2|960 /960|4800 /4800|13440 /13440|

At q32 s1,2,3,4 andq64 s1,2,4,5, the earlier run enumerates1,200,520 projective-point field/twist cases and all descended self-dual-plane candidates. The new run checks trace-direction kernels and graph/base incidences at those same twists. Neither run exhausts B² modules at q32/q64; q64 s0/s3 are not part of these higher-field runs. Geometry records hash: `2570268bf64f82f7bde2cf014caa9848195da6eaddd1de6a9c7b2a93886886d6`.

## 5. Reproduction, immutable sources and limitations

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_core_a_distribution.py NEW_CENSUS_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_distribution.py NEW_CENSUS_LABEL NEW_GEOMETRY_AUDIT_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_closed_formula_proof.py NEW_PROOF_LABEL
```

The final command intentionally compares the preserved `distribution_v1`, `distribution_audit_v1` and `structure_v1` baseline data; the first two commands create successor reruns, not replacements. Always use fresh labels and enabled assertions; no `-O`. Source/input hashes and the finalisation input manifest guard the frozen evidence. No failures occurred in these recorded distribution/finalisation runs. Hash/AST/ZIP/finite checks are not external human review, originality clearance or publication-readiness certification.
