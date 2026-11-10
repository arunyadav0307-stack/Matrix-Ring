# Supplementary data — reference (not duplicated here)

The supplementary package is **not copied** into this review package. It lives in
the repository at **`PAPER/supplementary/`** and is unchanged by Phase 15. This
file records where each artefact is and how to verify it.

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

## Note on `CERTIFICATION_PROCEDURE.md`

`PAPER/supplementary/CERTIFICATION_PROCEDURE.md` §3 still contains the sentence
*"Every headline code is certified by three structurally different methods."*
This is **canonically wrong** for the same reason as CP-1. It was **not** edited,
because it is part of the committed, hash-verified supplementary package that
records what the computation actually did; silently rewriting it would break the
`MANIFEST.sha256` verification above and would destroy the audit trail showing
where the overclaim originated.

**It is therefore a known open documentation defect** and is recorded as such.
Correcting it is a one-line change that the researcher may authorise; doing so
requires regenerating `MANIFEST.sha256`, which is why it was not done unilaterally.
