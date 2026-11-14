# Core A reproducibility

Python **3.11**, standard library only. Run from the checkout root (no environment activation or install needed):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_core_a.py NEW_MAIN_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_independent.py NEW_MAIN_LABEL NEW_AUDIT_LABEL
```

Choose fresh alphanumeric/underscore/hyphen labels: both drivers refuse to overwrite a prior result directory. Do not run with Python `-O`, which disables the assertions used for verification. `SEED=20261112` is a fixed reproducibility parameter, not a claimed execution date. Recorded main/audit runs are `results/main_v1` and `results/audit_v1`.

## Exact scope

- `core_a.py`: GF2/GF4/GF8/GF16 polynomial-basis arithmetic, B ring actions and 8-coordinate Morita modules; not a new hull algorithm.
- `verify_core_a.py`: primary exhaustive auxiliary q2 generator matrices; q2/q4 scalar ideals; named and seeded stratified q4/q8/q16 inputs, all twists. See per-run summaries for counts and source hashes.
- `audit_core_a_independent.py`: no primary/project arithmetic imports; independent binary subspace enumeration and GF tables; original 16-coordinate global matrix pairing, right-ideal multiplication and successive hyperplane restriction. It reads primary case data and compares complete spaces.

Mathematical proofs: `../phase2/CORE_A_FOUNDATIONS.md`, `../phase3/CORE_A_PRESERVATION.md`. Audit/limitations: `../audits/CORE_A_PROOF_AND_COMPUTATION_AUDIT.md`.

PASS means the stated finite assertions ran successfully. It does not certify all fields, external originality, journal fit, independent human review, a quantum bridge or distances. q2 is auxiliary and outside m≥2; q4/q8/q16 main samples are not complete censuses. Original project evidence has not been overwritten or silently rerun.

## Structural successor runs

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_core_a_structure.py NEW_STRUCTURE_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_structure_global.py NEW_STRUCTURE_LABEL NEW_GLOBAL_LABEL
```

The structural verifier reads the preserved `results/audit_v1/binary_all_modules.json` as comparison data. Recorded successors are `structure_v1` and `structure_global_v1`. All q4/q8 embedded inputs/all twists are checked by the structural vs generic route; all q4 cases are additionally checked with the alternative global route. q2 remains auxiliary; q16 has only named line-family checks. q8 full case data are deterministically hashed, not stored in bulk. See `../audits/CORE_A_STRUCTURE_AUDIT.md`. Do not use `-O`.

## Fully split double-root successor — M4

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_split_coupling.py NEW_SPLIT_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_split_global.py NEW_SPLIT_LABEL NEW_SPLIT_GLOBAL_LABEL
```

Current saved runs are `split_resumed_v1` and `split_global_resumed_v1`. They are fresh executions after an explicitly recorded continuation recovery, not recovered old `split_v1` files. The two reconstructed script sources byte-match the hashes in the earlier transcript. The reference uses `core_a.py`; the alternative global driver imports only the separate audit arithmetic and enforces the original variable-length cyclic matrix products/form. Complete input/dual/hull spaces are compared for41 named cases, at eight field/length pairs through n30; no all-code census at n>2 is claimed. Same-input q4n6 certificates include original-coordinate hull bases and explicit minimal matrix generators, verified by their complete right spans. See `../audits/SPLIT_COUPLING_AUDIT.md`. Always use fresh labels and enabled assertions.

## AR01-M5 — closed-formula proof finalisation and audit

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_core_a_distribution.py NEW_CENSUS_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_distribution.py NEW_CENSUS_LABEL NEW_DISTRIBUTION_AUDIT_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/verify_closed_formula_proof.py NEW_PROOF_LABEL
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/tools/check_closed_formula_documents.py NEW_DOCUMENT_CHECK_LABEL
```

Recorded runs are `distribution_v1`, `distribution_audit_v1` and `closed_formula_proof_v1`. Labels refuse overwrite; assertions must stay enabled. The last proof driver intentionally reads the preserved distribution/geometry/structure baselines; the first commands produce successor reruns, not silent replacements.

- `core_a_distribution.py`: explicit integer predictions only, no field arithmetic or proof-by-fitting claim.
- `verify_core_a_distribution.py`: all166,521 q16 modules and all four twists,666,084 generic/structural complete-hull comparisons, with unique descriptors/closure/strata/histograms checked. Full stream hashed,176 selected original-global inputs retained. Old q2/q4/q8 summaries are read, not rerun.
- `audit_core_a_distribution.py`: separate arithmetic and all334,413 small-field layer-subspace cases; independent higher-field points/descended planes and176 original-global q16 cases. It shares only integer predictions, not primary field/module/hull code. q32s1–4 andq64s1,2,4,5 are geometry checks, never complete B² code censuses.
- `verify_closed_formula_proof.py`: fresh17 trace-hyperplane/graph-chart cases,4,608 original global product/shift basis checks, all2,442 q4 global cases and176 q16 saved cases. Checks a non-involutive original-global double dual, five exact polynomial identities and2,080 integer formula pairs m1…64. The q16 full census is compared as existing evidence, not rerun. Integer pairs are not field/module censuses.
- `../tools/check_closed_formula_documents.py`: six-document existence, exact proof-unit/range/hash/link consistency and an exact five-variable N2 assembly identity, **not** automated logical proof verification.
- `../tools/verify_remote_checkpoint.py`: fixed-branch remote ref/all-blob/mode/expected-path identity checks; fresh receipt or print-only mode. It does not change branches/history or certify mathematics.

See [full proof](../phase3/CORE_A_CLOSED_FORMULA_FULL_PROOF.md), [audit](../audits/CORE_A_INDEPENDENT_PROOF_AUDIT.md), [exact coverage](../audits/CORE_A_THEORY_COMPUTATION_COMPARISON.md) and [status](../audits/CORE_A_PROOF_STATUS_REPORT.md). Same-agent alternative mathematics/programs are not external human review. No finite agreement establishes originality, journal fit, a Gray/physical application or submission readiness.

## AR01-M6 — scalar QC reduction and closest-result continuation

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B autonomous_research/AR01/computations/audit_core_a_scalar_qc.py NEW_SCALAR_QC_LABEL
```

Recorded `scalar_qc_v1`: PASS. The driver constructs scalar A-valued length4/index2 QC inputs using an explicit 1,u,X,uX action span, imposes both A coefficients of the first-slot scalar form, and compares complete hull spaces with primary data and the original-global matrix route. It checks u/shift closure of inputs/duals/hulls, all176 exported q16 dual bases and the radical-quotient generator invariant. Scope is all2,442 q4 cases plus176 q16 subset cases, with1,152 basis/scalar/constant/shift tests at q4/q8/q16. It reuses only the alternative field/row/global checker, not primary field/module/descriptor/hull code. Same-agent verification is not external review; this is a comparison lemma, not a new algorithm, Gray isometry, full q16 census or novelty certificate. The [crosswalk](../phase1/A13_SCALAR_QC_REDUCTION_AND_CLOSEST_RESULT_COMPARISON.md) proves the general statement separately.

## AR01-M7 — preserve a74f33f and continue Core A in scope

Fresh saved continuation labels are `checkpoint_continuation_proof_v1` and `checkpoint_continuation_scalar_qc_v1`, both PASS using the unchanged respective drivers. They rerun the already specified global/trace/graph and scalar-QC checks, not a full q16 census. The same2,442 q4 and176 selected q16 object sets are not counted twice as new distinct-code coverage. Basis-stream and trace/graph hashes reproduce the preserved originals exactly; q32/q64 remain selected-twist geometry only. The six-document checker has a fresh `A74F33F_CONTINUATION_DOCUMENT_CHECKS_V1` receipt. See the [checkpoint preservation/coverage report](../audits/CORE_A_CHECKPOINT_CONTINUATION_REPORT.md). No historical result/source was overwritten or silently relabelled.
