# Research data and reproducibility package

**Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings**

Arun Kumar Yadav — School of Basic and Applied Sciences, K.R. Mangalam
University, Sohna Road, Gurugram, Haryana, 122103, India.
Corresponding author: arunyadav0307@gmail.com

Manuscript prepared for *Finite Fields and Their Applications* (Elsevier).

---

## 1. Purpose of this data

The paper is partly computational. This package contains **86 files** — the
scripts that performed the computation, the logs those scripts produced, the
generator matrices of the certified codes, the machine-readable parameter
tables, and the documents that define what "certified" means here.

Every number in the paper that came from a computation can be traced to a line
of a log in this package. No number was transcribed by hand from a screen: the
CSV tables carry the log line each row was parsed from, and the scripts that
produced the logs are included.

The theorems themselves are proved in the manuscript text; no computation
enters any proof. What the computation does is *corroborate* the theory and
*certify* the parameters of the quantum codes that are constructed.

## 2. Licence

**No licence has been applied.** This repository carries no licence file, and
none is granted here. Under copyright law the default is "all rights reserved":
public availability does **not** by itself grant permission to copy, modify,
distribute or build upon these files. If you wish to reuse them beyond personal
inspection, contact the corresponding author at the address above.

## 3. Contents and their relationship to the manuscript

| folder | files | contents | manuscript |
|---|---:|---|---|
| `scripts/` | 22 | the computation scripts | Appendix B; supports Secs. 3–8 |
| `logs/` | 23 | the verbatim execution records | the source of every computed number |
| `generator_matrices/` | 29 | one generator matrix per certified code (28) plus `INDEX.json` | Sec. 8; Appendix A, Table A.1 |
| `quantum_code_records/` | 7 | machine-readable parameter tables | Tables 1–3; Appendix A, Table A.2; Secs. 5, 8, 9 |
| `distance_certificates/` | 1 | `certified_codes.csv` — the 28-code certification table | Sec. 8; Appendix A, Table A.1 |
| `verification_procedures/` | 2 | `CERTIFICATION_PROCEDURE.md`, `ENVIRONMENT.md` | Sec. 8; Appendix B |
| `documentation/` | 2 | the original package index and the original package manifest | — |
| `PUBLICATION_MANIFEST.sha256` | 1 | SHA-256 of all 86 published files | — |

**Total: 86 published data files**, 2.1 MB.

### Which script reproduces which result

| result | script |
|---|---|
| Arithmetic of $\mathbb F_q$, $A_t$, $R=M_2(A_t)$, $R_n$ — start here | `scripts/matrix_ring_lib.py` |
| Ring structure of $A_t$ and $R$ (cardinality, units, centre, radical) | `scripts/ring_structure_checks.py` |
| Left and right module actions | `scripts/module_actions_checks.py` |
| Galois duality, annihilators, reciprocal generators | `scripts/phase2_stage2c_galois_duality.py`, `galois_duality_experiments.py`, `galois_t2_check.py` |
| Cyclic shift, action conventions, centrality of $X$ | `scripts/phase2_stage1_shift_checks.py` |
| Morita correspondence and generator numbers | `scripts/phase2_stage2a_morita_checks.py` |
| CRT/Hensel decomposition and principality | `scripts/phase2_stage2b_crt_principality.py` |
| Galois hull structure and dimension theory | `scripts/phase3_stage3a_hull_structure.py` |
| Hull enumeration and the $\mu_B\ge 3$ witnesses | `scripts/phase3_stage3b_hull_enumeration.py` |
| Gray-map compatibility | `scripts/phase4_gray_map_compatibility.py` |
| Quantum constructions, routes R1–R3 | `scripts/phase5_quantum_constructions.py` |
| Parameter enhancement, distance certification | `scripts/phase6_quantum_parameter_enhancement.py` |
| The extended search: headline codes, Pareto frontier, entanglement | `scripts/phase7_extended_search.py` |
| Export of the 28 generator matrices | `scripts/extract_certified_generators.py` |
| Independent audit (re-implemented from scratch) | `scripts/independent_audit_checks.py`, `audit_pairing_equivalence.py`, `decision_support_checks.py`, `module_actions_checks.py`, `ring_structure_checks.py` |
| Literature reconciliation (Alahmadi–Sboui–Solé–Yemen) | `scripts/alahmadi_reconciliation.py` |
| Feasibility scoping | `scripts/phase0_feasibility.py` |
| Convention probe (length 3 over $M_2(\mathbb F_2)$) | `scripts/u8_n3_selfdual_check.py` |

## 4. Verifying integrity

```bash
sha256sum -c PUBLICATION_MANIFEST.sha256
```

Expected: **86 lines, all `OK`, 0 `FAILED`.** This is the authoritative check
for this package.

`documentation/MANIFEST.sha256` is the pre-publication manifest, preserved for
provenance. It indexes the files under their earlier relative layout, so
**74 of its 85 entries verify in place**; the remaining 11 were relocated into
`quantum_code_records/`, `distance_certificates/`, `verification_procedures/`
and `documentation/`. Every one of those 11 files is byte-identical — only its
path changed. Use `PUBLICATION_MANIFEST.sha256` for verification.

## 5. Running the computation

### Requirements

* **Python 3** — the recorded run used `3.11.2` on Linux `6.1.158+` x86_64.
* **No third-party packages.** Pure standard library only: `sys`, `os`, `time`,
  `random`, `json`, `csv`, `re`, `itertools`, `collections`, `resource`,
  `hashlib`. No numpy, sympy, Sage, GAP or Magma is used or required.
* Arithmetic in $\mathbb F_q$, $A_t$, $R$ and $R_n$ is implemented from first
  principles in `scripts/matrix_ring_lib.py`, deliberately, so that every step
  can be inspected without trusting a computer algebra system.
* The principal search needs about **370 MB RSS** and about **9 minutes** on the
  recorded 2-CPU machine.

### Reproducing

```bash
cd scripts
python3 phase7_extended_search.py > out.txt 2>&1
diff <(grep -v '\[[0-9]*s\]' out.txt) \
     <(grep -v '\[[0-9]*s\]' ../logs/phase7_extended_search_log.txt)
```

The `grep -v` strips elapsed-time annotations; the peak-memory line is the only
other expected difference. The seed is fixed (`SEED = 20261210`) and every
random choice comes from a single `random.Random(SEED)` instance, so the search
is deterministic.

Regenerate the generator matrices:

```bash
cd scripts
python3 extract_certified_generators.py ../generator_matrices
```

Dependency order is given in `documentation/SUPPLEMENTARY_PACKAGE_README.md`
(`matrix_ring_lib.py` first).

### Path note

The scripts expect `logs/` and `generator_matrices/` to sit next to `scripts/`,
which they do in this layout. The preserved package index in
`documentation/SUPPLEMENTARY_PACKAGE_README.md` refers to the eight CSV tables
under their earlier directory name `parameter_tables/`; in this package they are
split between `quantum_code_records/` (7 files) and `distance_certificates/`
(1 file). Substitute accordingly when following that document.

## 6. Exact-distance certificates and lower-bound certificates

This distinction matters and is stated precisely.

* **M1 — complete enumeration.** Enumerate the whole ambient code and take its
  minimum weight. This is exhaustive and gives the **exact** distance. It is
  only feasible for the smaller parameters.
* **M2 — increasing-weight support search.** Search supports of increasing
  weight until the distance is pinned down. Also exact when it finishes.
* **M3 — independent ambient quantum search.** An independent computation in
  the ambient quantum space. Depending on the parameters it either determines
  the distance exactly or returns a **proved lower bound** (reported with a
  `>` prefix, e.g. `>2`).

**M2 is conditionally skipped.** The pipeline runs M2 **only when M1 has not
completed**. Where M1 finishes, M2 is recorded as `n/a` and is not run. This is
why no code has all three methods: the design is M1-or-M2, then M3.

### Certification-method distribution over the 28 codes

| | codes |
|---|---:|
| **M1 + M3** (M1 completed; M2 skipped) | **24** |
| **M2 + M3** (M1 did not complete; M2 ran) | **4** |
| **M3 gave the exact distance** | **11** |
| **M3 gave a lower bound only** | **17** |
| **All three methods completed together** | **0** |

These five figures are computed directly from
`distance_certificates/certified_codes.csv` (columns `M1`, `M2`,
`M3_lower_bound`).

**Read this carefully.** Two methods run per code. **No code is certified by
all three methods.** For **17 of the 28 codes**, the independent M3 check yields
only a **proved lower bound**, not the exact distance — the reported distance
for those codes is exact by virtue of M1 or M2, and M3 corroborates it from
below. It is **not** the case that three independent methods were completed for
every code, and it is **not** the case that every distance is obtained exactly
by every method.

## 7. Limitations

* **15 of the 42 families resisted complete enumeration**, so the family census
  records `counted-only` or `blocked` for them; no claim is made about codes in
  those families.
* **$q = 8$ is not tabulated** at codetables.de, so the $q=8$ codes of this
  paper are not compared against best-known distances.
* **No entanglement-assisted table exists**, so the entanglement-assisted codes
  cannot be compared against best-known values at all.
* **No record parameters are claimed.** The stabilizer codes are one or two
  below the best known distances; the comparison tables show the gaps.
  (`quantum_code_records/comparison_grassl_q4.csv`,
  `comparison_grassl_q9.csv`.)
* `quantum_code_records/comparison_grassl_q9.csv` contains **external
  third-party data**: three rows of best-known $q=9$ bounds read verbatim from
  codetables.de on **2026-11-04**, cited in the manuscript as reference [5].
  That page changes; the values here are as retrieved on that date. They are the
  only external data in the paper and the only such data in this package.
* The $q=4$ comparison values are derived from this project's own run log
  (Part 8), not read from an external source.
