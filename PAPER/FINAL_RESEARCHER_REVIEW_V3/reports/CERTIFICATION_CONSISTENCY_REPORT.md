# Certification consistency report — Phase 18

Verification that the applied Option B2 abstract is supported by the underlying
evidence, and that the conditional execution logic is unchanged.

## 1. Required facts

| item | verified value | required |
|---|---|---|
| Total codes | **28** | 28 ✓ |
| M1 + M3 | **24** | 24 ✓ |
| M2 + M3 | **4** | 4 ✓ |
| M3 exact | **11** | 11 ✓ |
| M3 lower bound | **17** | 17 ✓ |
| All three completed | **0** | 0 ✓ |

Source: `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`,
re-read and re-tallied in Phase 18.

## 2. Abstract claim-by-claim

| abstract claim | holds | evidence |
|---|---|---|
| "certifies $28$ codes" | yes | 28 CSV rows |
| "each by two independent methods" | yes | every row has exactly 2 methods; M1+M3 ×24, M2+M3 ×4 |
| "one exact" | yes | exact evidence: M1 complete enumeration ×24, M2 support search ×4 |
| "one quantum search exact for $11$ codes" | yes | M3 returned a value equal to the reported $d$ for 11 codes |
| "and a lower bound for $17$" | yes | M3 returned nothing below $w3$ for 17 codes; all consistent with $d$ |
| implies no code has all three | yes | 0 rows with three methods |

## 3. Logic confirmations

| required | status | where |
|---|---|---|
| M2 is conditionally skipped when M1 has already completed | confirmed | `part6_certification`: `if comp1: d2, m2 = None, "n/a (M1 already complete)"` |
| M2 applicability determined per code, not per route | confirmed | the branch tests `comp1`, not `kind`; one of the four M2 codes is EA ($[[24,6,4;18]]_9$) |
| M1 non-completion is **not** described as route inapplicability | confirmed | no occurrence of "M2 is not applicable" or "not applicable to the [route]" anywhere in the manuscript |
| M3 exact vs lower-bound outcomes remain distinct | confirmed | §8.5 and Appendix A both state the 11/17 split; Appendix A states the per-row reading |

## 4. Evidence sources consulted (none rewritten)

1. `PAPER/supplementary/scripts/phase7_extended_search.py` — `part6_certification`.
2. `PAPER/supplementary/logs/phase7_extended_search_log.txt` — Part 6, lines 449–478
   (28 rows). The `[EXH] E1` line remains historically wrong and is deliberately
   preserved.
3. `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.
4. `PAPER/SUPPLEMENTARY_V2/CERTIFICATION_PROCEDURE.md` (corrected).
5. `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_MANUSCRIPT_CONSISTENCY_REPORT.md`.
6. `PHASE17_RESEARCHER_DECISION/PHASE17_ABSTRACT_WORDING_OPTIONS.md`.

## 5. Unchanged

No distance value, quantum parameter, generator matrix, construction route,
certification record, theorem, proof or equation was altered by Phase 18. The
only change in the entire manuscript is one sentence of the abstract.
