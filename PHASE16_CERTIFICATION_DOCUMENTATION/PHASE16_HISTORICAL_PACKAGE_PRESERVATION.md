# Phase 16 / Task C — Historical package preservation

## 1. Principle

The original supplementary package is a hash-verified artefact (85-entry
`MANIFEST.sha256`) and is the evidence of the earlier documentation state. It was
**not modified in place**. A new corrected version was created beside it.

| | path | role | status |
|---|---|---|---|
| historical | `PAPER/supplementary/` | evidence of the earlier documentation state | **unchanged**, 85/85 manifest OK |
| authoritative | `PAPER/SUPPLEMENTARY_V2/` | corrected version for future researcher review | new, 86-entry manifest, all verified |

---

## 2. How the new version was built

1. `cp -a supplementary SUPPLEMENTARY_V2` — a full recursive copy.
2. `diff -r supplementary SUPPLEMENTARY_V2` → no differences (all 86 files
   byte-identical before any edit).
3. Replaced **exactly one** file, `CERTIFICATION_PROCEDURE.md`, with the
   corrected text.
4. Added the append-only note `SUPPLEMENTARY_CORRECTION_NOTE.md`.
5. Removed generated `scripts/__pycache__/` (4 `.pyc` files, produced by the
   verification runs themselves; gitignored, not package content) from **both**
   trees before manifesting.
6. Generated `SUPPLEMENTARY_V2/MANIFEST.sha256` (self-excluding) and verified
   every entry.

---

## 3. Verification

| check | result |
|---|---|
| files differing from the historical package | **1** (`CERTIFICATION_PROCEDURE.md`) |
| other content files byte-identical | **85 of 85** (verified by per-file SHA-256 comparison, not by `diff` alone) |
| scripts / logs / generator matrices / parameter tables | **retained byte-for-byte** |
| historical package `MANIFEST.sha256` | **85/85 OK** — still verifies |
| new package `MANIFEST.sha256` | **86 entries, 86 OK**, 0 mismatches |
| historical `CERTIFICATION_PROCEDURE.md` hash | `02c1a8906f4a7336…` — identical to the Phase 15 baseline |
| `__pycache__` / `.pyc` in either package | none |

Inventory of the corrected package (86 content files):

| directory | files |
|---|---|
| `scripts/` | 22 |
| `logs/` | 23 |
| `generator_matrices/` | 29 |
| `parameter_tables/` | 8 |
| root (3 original docs + correction note) | 4 |
| **total** | **86** |

---

## 4. The append-only correction note

`SUPPLEMENTARY_V2/SUPPLEMENTARY_CORRECTION_NOTE.md` records, as a dated
append-only entry:

* what was wrong (both defects, with the source excerpt that disproves them);
* what is true (the 24 / 4 / 11 / 17 distribution, the per-code-not-per-route
  rule, the four M2 codes listed explicitly);
* what was changed (one file; Sections 3 and 4 rewritten/inserted; other
  sections untouched);
* what was **deliberately not** changed and why — the historical package, the
  Phase 7 log line 478, and every script, log, generator matrix, parameter table,
  mathematical result, distance value and quantum parameter;
* the consequence for re-running the pipeline: `extract_certified_generators.py`
  will reproduce the `n/a` entries exactly, because **the computation was never
  wrong — only its description was**.

---

## 5. Which version should be used

**`PAPER/SUPPLEMENTARY_V2/` is authoritative for future researcher review.**

`PAPER/supplementary/` must continue to be cited when the question is "what did
the project state at the time of the Phase 7 run" — for example when auditing
how the overclaim arose. Both are shipped; neither is deleted.
