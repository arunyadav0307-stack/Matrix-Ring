# Supplementary package

Reproducibility material for the manuscript

> **Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
> Noncommutative Matrix Rings**

Everything here is either a byte-identical copy of a file committed in the
project repository (`04_COMPUTATION/`) or an artefact produced from those
files by a script that is itself included. No number in the manuscript was
transcribed by hand from a screen: the CSV tables in `parameter_tables/`
carry the log line number each row was parsed from, and
`tools/build_parameter_tables.py` regenerates them from the log.

## Contents

```
supplementary/
├── README.md                        this file
├── ENVIRONMENT.md                   exact interpreter, platform, resources
├── CERTIFICATION_PROCEDURE.md       what "certified" means; how to re-certify
├── MANIFEST.sha256                  SHA-256 of every file in this package
├── scripts/                         the computation scripts
│   ├── matrix_ring_lib.py           F_q, A_t, R = M_2(A_t), R_n  (start here)
│   ├── phase0_feasibility.py
│   ├── phase2_stage1_shift_checks.py
│   ├── phase2_stage2a_morita_checks.py
│   ├── phase2_stage2b_crt_principality.py
│   ├── phase2_stage2c_galois_duality.py
│   ├── phase3_stage3a_hull_structure.py
│   ├── phase3_stage3b_hull_enumeration.py
│   ├── phase4_gray_map_compatibility.py
│   ├── phase5_quantum_constructions.py
│   ├── phase6_quantum_parameter_enhancement.py
│   ├── phase7_extended_search.py    the search that produced the headline codes
│   ├── extract_certified_generators.py   NEW: dumps the 28 generator matrices
│   └── ...                          audit / control scripts
├── logs/                            the committed logs
│   ├── phase7_extended_search_log.txt        (727 lines, 18/18 checks PASS)
│   ├── phase7_extended_search_log_v1.txt     (v1, preserved unchanged)
│   ├── phase6_quantum_parameter_log.txt
│   ├── phase5_quantum_log.txt
│   ├── phase4_gray_map_log.txt
│   ├── extract_certified_generators_run.txt  NEW: output of the extraction
│   └── ...
├── generator_matrices/              28 JSON files + INDEX.json
└── parameter_tables/                8 CSV tables, parsed from the log
```

## Where each number in the manuscript comes from

| Manuscript item | Source |
|---|---|
| Theorems 4.1–4.6, 5.1–5.5, 6.1–6.9, 7.1–7.6, 8.1–8.5 | proved in the text; no computation enters |
| Table 1 (headline codes) | Part 4(d) Pareto frontier, Part 4(e) best-per-route, Part 6 of `phase7_extended_search_log.txt` |
| Table 2 (entanglement budget) | Part 4(c), lines 195–201 |
| Table 3 (`$\mu_B=3$` witnesses) | Part 5 (D3), lines 409–416 |
| Appendix A, Table 4 (28 certified codes) | Part 6, lines 451–478 |
| Appendix A, Table 5 (best known) | `parameter_tables/comparison_grassl_q4.csv` (log Part 8) and `comparison_grassl_q9.csv` (codetables.de, retrieved 2026-11-04) |
| $120\,721$ / $5\,055$ / $4\,418$ / $637$ | completion report, line 711–712 |
| $368$ tuples, $88$ non-dominated | Part 4(f) |
| 42 families (23 exhaustive, 4 counted-only, 15 blocked) | Part 2, lines 59–100 |
| 25 families scanned | Part 3, lines 124–148 |
| 0 violations of the bookkeeping identities | check A1, line 172 |
| 0 violations of the coset Singleton bound | check H1, line 318 |
| 0 violations of the Singleton / Hamming bounds | check G1, line 646 |

Line numbers refer to `logs/phase7_extended_search_log.txt` (727 lines).

## Reproducing

```bash
cd supplementary/scripts
python3 phase7_extended_search.py > out.txt 2>&1
diff <(grep -v '\[[0-9]*s\]' out.txt) \
     <(grep -v '\[[0-9]*s\]' ../logs/phase7_extended_search_log.txt)
```

About 9 minutes, about 370 MB RSS. The `grep -v` removes the elapsed-time
annotations; the peak-memory line is the only other difference.

The scripts write their log file next to themselves, i.e. into `scripts/`
when run from there; they also print to stdout, so the redirect above is
equivalent.

The earlier phases run the same way; see `04_COMPUTATION/README.md` in the
repository for the dependency order (`matrix_ring_lib.py` first).

To regenerate the generator matrices:

```bash
cd supplementary/scripts
python3 extract_certified_generators.py ../generator_matrices
```

It locates the repository `04_COMPUTATION/` directory automatically, or via
the environment variable `MATRIX_RING_COMP`.

To regenerate the CSV tables:

```bash
cd PAPER
python3 tools/build_parameter_tables.py
```

## Verifying the package

```bash
cd supplementary
sha256sum -c MANIFEST.sha256
```

## What is *not* reproducible from this package

The $q=9$ best-known bounds in `parameter_tables/comparison_grassl_q9.csv`
were read from codetables.de, a page that changes. They are quoted verbatim
as retrieved on **2026-11-04** (the page reported "Last change: 10.06.2024").
They are external data, not an output of this computation, and they are the
only such data in the manuscript.

## Known limitations carried forward

* $q=8$ is not tabulated at codetables.de, so no $q=8$ code of this paper is
  benchmarked.
* There is no entanglement-assisted quantum code table (the corresponding
  endpoint returned HTTP 404), so **no entanglement-assisted code of this
  paper is benchmarked at all**, including the best ones.
* 15 of the 42 families in the census could not be enumerated (component BFS
  too large); they are listed with method `component BFS too large` in
  `parameter_tables/family_census.csv`. No claim is made about codes in those
  families.
