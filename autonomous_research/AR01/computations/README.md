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
