# Phase 16 / Task B — Correction of `CERTIFICATION_PROCEDURE.md`, Section 3

## 1. The defect

`CERTIFICATION_PROCEDURE.md` in the original supplementary package opened
Section 3 with:

> Every headline code is certified by three structurally different methods.

This is **false**. `scripts/phase7_extended_search.py::part6_certification` runs
M2 **if and only if M1 did not complete**, so no code can have all three methods:
for every code either M1 ran and M2 was skipped, or M1 failed and M2 ran instead.

### A second defect, not previously recorded

Section 3 also stated (lines 58–59):

> Because M2 shares no code with M1, agreement between them is a genuine
> cross-check and not a tautology.

The premise is sound, but the sentence implies that M1 and M2 are both run and
agree. **They never run on the same code**, so there is no agreement between them
to report. This second defect was found during Phase 16 and is corrected here
alongside the first.

---

## 2. What the corrected Section 3 now states

The rewritten Section 3, "The three methods, and which ones actually run",
covers every point required:

| required content | where in the corrected section |
|---|---|
| 1. What M1 does | §"M1 — complete enumeration", with its implementation and completion caps |
| 2. What M2 does | §"M2 — increasing-weight support search", with `maxw` and the meaning of `None` |
| 3. What M3 does | §"M3 — ambient quantum search", with `w3 = 3 if N<=8 else 2` and both outcomes |
| 4. The exact conditional execution logic | §"The conditional execution logic (verbatim from the source)" — quoted, then read out as three numbered rules |
| 5. Why M2 is skipped when M1 has completed | §"Why not all three methods are executed for every code" — M2 is a **fallback for M1, not a third opinion** |
| 6. Which methods provide the exact distance | §"Which methods provide what" — M1 for 24 codes, M2 for 4 |
| 7. Which provide independent cross-checks | §"Which methods provide what" — M3 for all 28; exact for 11, lower bound for 17 |
| 8. Why not all three are executed | §"Why not all three methods are executed for every code" |
| 9. How to determine the methods used for a particular code | new **Section 4**, giving three shipped sources and a reading table for the `n/a` / `-` entries |

### Constraints honoured

* **Does not say M2 is route-inapplicable.** Section 3 now carries an explicit
  subsection, "Applicability is per code, not per route", listing the four M2
  codes (two SO, one DC, **one EA**) and stating directly that "M2 is not
  applicable to the EA route" is **false**.
* **Does not claim three methods verified every code.** The section opens with
  "Three methods exist in the pipeline. They are not all run for every code" and
  closes the summary table with "**No code is certified by all three methods.**"
* **Uses precise wording consistent with the 28 records.** Every count in the
  document (24, 4, 11, 17, 28) is taken from
  `PHASE16_28_CODE_APPLICABILITY_TABLE.csv` and was verified against the source,
  the log, the CSV and the generator records with 0 discrepancies.
* **Removes the false "agreement between them" claim**, replacing it with: M2
  shares no code with M1, so had they run together the agreement would have been
  a genuine cross-check — "**They are not run together**".

---

## 3. What was not changed in the document

Sections 1, 2, 5 and 6 (What is being certified; What the distance is; The defect
that was found and fixed; How to re-certify from scratch) were carried over
verbatim. Only content required to correct the defect was altered or added. The
re-certification section was renumbered 5 → 6 to accommodate the new Section 4.

---

## 4. Note on the historical log

The corrected document explicitly flags, rather than silently fixes, the wrong
log line:

> Line 478 … check `[EXH] E1` … That wording is **wrong** … The log is a
> historical record of what the program printed and has deliberately **not** been
> rewritten; this note is the correction of it.

---

## 5. Verification

| check | result |
|---|---|
| `diff -r` historical package vs corrected package | exactly **1** file differs |
| that file | `CERTIFICATION_PROCEDURE.md` |
| all other files byte-identical | 85 of 85 |
| corrected file SHA-256 | `d844d1af012d823c4572541e935a4b4e5e872cdcc996d6a9633e46d0046bc6d4` |
| original file preserved | `02c1a8906f4a733612386d2273f68864070de237ae55dc39dc74c2d1a7e791c0` (unchanged) |
| historical manifest still verifies | 85/85 OK |
| new manifest | 86 entries, all verified |
