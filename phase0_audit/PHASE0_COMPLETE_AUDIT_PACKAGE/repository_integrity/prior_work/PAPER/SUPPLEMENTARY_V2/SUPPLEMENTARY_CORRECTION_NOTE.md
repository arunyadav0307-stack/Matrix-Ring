# Append-only correction note — supplementary package, corrected version

**Date of this entry:** Phase 16.
**Package:** `PAPER/SUPPLEMENTARY_V2/` — **authoritative version for future
researcher review.**
**Historical package:** `PAPER/supplementary/` — **preserved unchanged**, as
evidence of the earlier documentation state.

This file is **append-only**. Nothing in the historical package is deleted,
rewritten or overwritten; every correction is recorded as a new entry here.

---

## Entry 1 (Phase 16) — correction of the certification-method description

### What was wrong

`CERTIFICATION_PROCEDURE.md`, Section 3, opened with:

> Every headline code is certified by three structurally different methods.

This is **false**. The committed source of the computation,
`scripts/phase7_extended_search.py`, function `part6_certification`, executes:

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"      # M2 NOT RUN
else:
    d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd, maxw=...)
w3 = 3 if N <= 8 else 2
d3, wit3 = P6.ambient_quantum_search(F, N, YV, Vgen, w3)
```

**M2 runs if and only if M1 did not complete.** Hence no code can have all three
methods: for every code either M1 ran and M2 was skipped, or M1 failed and M2
ran instead.

A **second** defect was found in the same section, which had not previously been
recorded. Lines 58–59 stated:

> Because M2 shares no code with M1, agreement between them is a genuine
> cross-check and not a tautology.

The premise of that sentence is sound, but the sentence implies that M1 and M2
are both run and agree. They never run on the same code, so there is no
agreement between them to report.

### What is true

Reconstructed per code and cross-checked against four independent sources (the
source code, Part 6 of the Phase 7 log, `parameter_tables/certified_codes.csv`,
and the 28 generator-matrix records) — **0 discrepancies**:

| | M1 completes | M1 does not complete | total |
|---|---|---|---|
| codes | **24** | **4** | **28** |
| exact method | M1 | M2 | — |
| M2 | conditionally skipped | run (exact) | — |
| M3 | run | run | 28 |
| **methods executed** | **M1 + M3** | **M2 + M3** | **2 per code** |

* **0 of 28 codes have all three methods. 28 of 28 have exactly two.**
* M3 yields an **exact** independent determination for **11** codes and a
  **proved lower bound** for the other **17**.
* Applicability is **per code, not per route**: the four M2-certified codes are
  two SO, one DC and **one EA** ($[[24,6,4;18]]_9$).

The per-code reconstruction is
`PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.

### What was changed

In this corrected package, **exactly one file** differs from the historical
package: `CERTIFICATION_PROCEDURE.md`. All other **85 files — 26 scripts, 23
logs, 29 generator matrices, 8 parameter tables and 2 further documentation
files — are byte-for-byte identical** to the originals, as verified by
`diff -r`.

Section 3 was rewritten to state, with source citations:

1. what M1, M2 and M3 each do, and their implementations;
2. the conditional execution logic, quoted verbatim from the source;
3. **why M2 is skipped** — because M1 already completed, not because of any
   route inapplicability;
4. which methods provide the exact distance (M1 for 24 codes, M2 for 4);
5. which provide cross-checks (M3 for all 28; exact for 11, lower bound for 17);
6. why not all three run — M2 is a fallback for M1, not a third opinion;
7. how to determine the methods used for any given code, from any of three
   shipped sources;
8. that applicability is per code and not per route, with the four M2 codes
   listed explicitly.

New Section 4 ("How to determine the methods actually used for a particular
code") was inserted; the re-certification section was renumbered to Section 6.
No other section was altered.

### What was deliberately NOT changed

* **The historical package.** `PAPER/supplementary/` is untouched; its 85-entry
  `MANIFEST.sha256` still verifies 85/85.
* **The Phase 7 log.** Line 478, check `[EXH] E1`, still reads *"every headline
  code is certified by the three independent methods …"*. That line is a
  historical record of what the program printed; rewriting it would destroy the
  evidence of the defect's origin. It is explicitly flagged as wrong in the
  corrected `CERTIFICATION_PROCEDURE.md` instead.
* **Any script, log, generator matrix, parameter table, mathematical result,
  distance value or quantum parameter.** None was touched.

### Consequence for anyone re-running the pipeline

Re-running `extract_certified_generators.py` regenerates the certification
table from the source, so it will **reproduce the `n/a` entries** in column M2
exactly as before. The computation was never wrong; only its description was.

---

## Verification of this package

| check | result |
|---|---|
| files | 86 |
| `diff -r` against the historical package | 1 file differs (`CERTIFICATION_PROCEDURE.md`) |
| all other files byte-identical | 85 of 85 |
| historical package intact | `MANIFEST.sha256` 85/85 OK |
| new manifest | `MANIFEST.sha256` in this directory, 85 entries (self-excluding), all verified |
| `__pycache__` / `.pyc` | removed before manifesting (generated bytecode, gitignored, not package content) |
