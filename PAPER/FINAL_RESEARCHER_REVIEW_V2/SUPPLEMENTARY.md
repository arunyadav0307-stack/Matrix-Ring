# Supplementary data — reference (not duplicated here)

There are **two** supplementary packages. Both are **not copied** into this
review package; this file records where each is and how to verify it.

| | path | role |
|---|---|---|
| **authoritative** | `PAPER/SUPPLEMENTARY_V2/` | corrected certification documentation (Phase 16). **Use this one.** |
| historical | `PAPER/supplementary/` | preserved unchanged, as evidence of the earlier documentation state |

They differ in **exactly one file out of 86** (`CERTIFICATION_PROCEDURE.md`);
the other 85 are byte-for-byte identical. The historical package was created in
Phase 15 and is unchanged by Phase 16.

| Item | Location |
|---|---|
| 22 computational scripts | `PAPER/supplementary/scripts/` |
| 23 execution logs | `PAPER/supplementary/logs/` |
| 29 generator matrices (+ `INDEX.json`) | `PAPER/supplementary/generator_matrices/` |
| 8 parameter tables | `PAPER/supplementary/parameter_tables/` |
| 4 documentation files | `PAPER/supplementary/*.md` |

**Total: 86 files**, verified by `PAPER/supplementary/MANIFEST.sha256`
(85 entries; the manifest excludes itself).

Verify:

```sh
cd PAPER/supplementary && sha256sum -c MANIFEST.sha256
```

Expected: 85 entries, all `OK`, 0 missing, 0 mismatches.

## Artefacts cited by the Phase 15 corrections

* **CP-1 evidence** — `PAPER/supplementary/parameter_tables/certified_codes.csv`
  (28 rows; columns `M1`, `M2`, `M3_lower_bound`), corroborated by Part 6 of
  `PAPER/supplementary/logs/phase7_extended_search_log.txt`, lines 449–478.
* **CP-1 root cause** — `PAPER/supplementary/scripts/phase7_extended_search.py`,
  function `part6_certification`, lines 1664–1708. Lines 1672–1679 show that M2
  is executed **only when M1 fails to complete**; line 1705–1708 is the
  `[EXH] E1` check whose wording overclaimed. That log line is historical
  evidence and was deliberately **not** rewritten.
* **CP-2 evidence** —
  `PAPER/supplementary/generator_matrices/04_20_2_10-18_4_(4,1,5)_EA.json`
  (generator matrices, `k`, `K`, `d`, `c`, `h_E`, `distance_method`), plus the
  CSV row at log line 454.
* **Method definitions** — `PAPER/supplementary/CERTIFICATION_PROCEDURE.md`
  (M1/M2/M3 definitions; §5 re-certification commands).

## Resolution in Phase 16

Phase 15 flagged `CERTIFICATION_PROCEDURE.md` §3 (the sentence *"Every headline
code is certified by three structurally different methods"*) as a known open
documentation defect, left unfixed because the file sits inside the
hash-verified historical package.

**Phase 16 resolved it without disturbing the historical package**, by the
preserve-and-supersede route:

* `PAPER/supplementary/` left **byte-for-byte unchanged**, manifest still 85/85.
* `PAPER/SUPPLEMENTARY_V2/` created as a full copy, with
  `CERTIFICATION_PROCEDURE.md` replaced and an append-only
  `SUPPLEMENTARY_CORRECTION_NOTE.md` added.
* New `SUPPLEMENTARY_V2/MANIFEST.sha256` — **86 entries, all verified**.

Verify either package:

```sh
cd PAPER/supplementary     && sha256sum -c MANIFEST.sha256   # 85 entries, all OK
cd PAPER/SUPPLEMENTARY_V2  && sha256sum -c MANIFEST.sha256   # 86 entries, all OK
```

The Phase 7 log line 478 (`[EXH] E1`) still carries the overclaim. It is a
historical record of what the program printed and was **deliberately not
rewritten**; the corrected documentation flags it as wrong.
