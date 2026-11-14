# Supplementary data — reference (not duplicated here)

The supplementary package is **not copied** into this review package. Two
versions exist; both are preserved.

| | path | role |
|---|---|---|
| **authoritative** | `PAPER/SUPPLEMENTARY_V2/` | corrected certification documentation (Phase 16). **Use this one.** |
| historical | `PAPER/supplementary/` | preserved unchanged, as evidence of the earlier documentation state |

They differ in **exactly one file out of 86** (`CERTIFICATION_PROCEDURE.md`); the
other 85 are byte-for-byte identical. Neither was modified in Phase 18.

Verify either package:

```sh
cd PAPER/supplementary     && sha256sum -c MANIFEST.sha256   # 85 entries, all OK
cd PAPER/SUPPLEMENTARY_V2  && sha256sum -c MANIFEST.sha256   # 86 entries, all OK
```

## Artefacts cited

| artefact | location |
|---|---|
| 22 computational scripts | `PAPER/SUPPLEMENTARY_V2/scripts/` |
| 23 execution logs | `PAPER/SUPPLEMENTARY_V2/logs/` |
| 29 generator matrices (+ `INDEX.json`) | `PAPER/SUPPLEMENTARY_V2/generator_matrices/` |
| 8 parameter tables | `PAPER/SUPPLEMENTARY_V2/parameter_tables/` |
| corrected certification procedure | `PAPER/SUPPLEMENTARY_V2/CERTIFICATION_PROCEDURE.md` |
| supersession record | `PAPER/SUPPLEMENTARY_V2/SUPPLEMENTARY_CORRECTION_NOTE.md` |

## Artefacts bearing on the certification claims

* **Conditional execution logic** — `scripts/phase7_extended_search.py`,
  `part6_certification` (lines 1670–1681). M2 runs **iff** M1 did not complete.
* **Execution record** — Part 6 of `logs/phase7_extended_search_log.txt`
  (lines 449–478), 28 rows. Line 478 (`[EXH] E1`) carries the historical
  overclaim and was deliberately **not** rewritten; the corrected procedure
  document flags it as wrong.
* **Per-code data** — `parameter_tables/certified_codes.csv` (28 rows; columns
  `M1`, `M2`, `M3_lower_bound`).
* **Definitive per-code reconstruction** —
  `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.

## Distribution (unchanged by Phase 18)

| | |
|---|---|
| M1 + M3 | 24 |
| M2 + M3 | 4 |
| M3 exact | 11 |
| M3 lower bound | 17 |
| three methods completed | **0** |
