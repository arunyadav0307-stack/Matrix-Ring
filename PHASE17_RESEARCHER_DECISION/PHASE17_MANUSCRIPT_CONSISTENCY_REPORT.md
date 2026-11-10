# Phase 17 / Task C — Consistency verification

Verified across: abstract, introduction, methodology (§8.5), Section 7 examples,
Appendix A, the corrected supplementary certification procedure, and the 28-code
applicability table. **The canonical manuscript was not modified.**

## 1. No statement implies all three methods ran on every code

Scanned the full source and the rendered PDF. Every occurrence of "all three" in
the certification context is a **negation**:

| location | text |
|---|---|
| `08_certification.tex:173` | "…no single code is certified by all three." |
| `08_certification.tex:183` | "No code is certified by all three, and the strength of the M3 cross-check is not uniform…" |

The three remaining occurrences of "all three" in the manuscript are unrelated to
the certification methods (`01_introduction.tex:106` — three results proved from
scratch; `02_literature.tex:110` — three routes; `06_gray.tex:198` — three
regimes).

Rendered-PDF overclaim scan for the strings *"certified by all three methods"*,
*"all three methods ran"*, *"every code is certified by three"*: **0 occurrences**.

## 2. M2 is described as conditionally skipped, not route-inapplicable

| location | text |
|---|---|
| `08_certification.tex:357` (Example 13) | "The support search (M2) is run only when M1 cannot finish, so it was not run here and contributes nothing…" |
| `appendix_tables.tex:15–17` | "a dash in the M1 column means M1 could not complete within its enumeration cap, in which case the support search M2 is run instead; ``n/a'' in the M2 column means M2 was **not run, because M1 had already finished** and M2 is run only when M1 cannot." |

A targeted scan for route-based generalisations ("not applicable to the [route]",
"EA route", "per code, not per route") returned **no** route-based claim about M2
anywhere in the manuscript — consistent with the requirement not to use
route-based generalisations.

## 3. M3 is described accurately as exact for 11 and a lower bound for 17

| location | text |
|---|---|
| `08_certification.tex:179–181` | "M3 searches in increasing symplectic weight from $1$, so a returned value is the true minimum and is an independent exact determination; this occurs for $11$ of the $28$ codes. For the remaining $17$ it finds no vector at or below the search weight and yields a proved lower bound only…" |
| `08_certification.tex:183–184` | "…the strength of the M3 cross-check is not uniform: it is exact for $11$ codes and a lower bound for $17$." |
| `appendix_tables.tex:19–26` | …"an entry $2$ or $3$ is therefore M3 *independently determining* the distance exactly, and this happens for $11$ of the $28$ codes… this happens for the remaining $17$ codes. So the cross-check supplied by M3 is an exact independent determination for $11$ codes and a consistent proved lower bound for the other $17$ — it is not uniform across the table." |

## 4. Rendered-PDF confirmation

| statement | present |
|---|---|
| abstract: "each by two applicable independent methods, one exact and one a cross-check" | yes |
| §8.5: "no single code is certified by all three" | yes |
| §8.5: "run precisely when M1 cannot finish" | yes |
| §8.5: "independent exact determination; this occurs for 11 of the 28 codes" | yes |
| §8.5: "lower bound for 17" | yes |
| Example 13: "The support search (M2) is run only when M1 cannot finish" | yes |
| Appendix A: "M2 was not run, because M1 had already finished" | yes |
| Appendix A: "this happens for 11 of the 28 codes" | yes |

## 5. Section 7 examples

Section 7 (`07_quantum.tex`) contains **no** M1/M2/M3 method claims — a targeted
scan for "M1", "M2", "M3", "support search", "enumeration", "ambient" returned
nothing. There is therefore no certification-method statement in Section 7 that
could conflict with §8.5 or Appendix A.

## 6. Corrected supplementary procedure

| required statement | present |
|---|---|
| "M2 runs if and only if M1 did not complete" | yes |
| M2 characterised as a "fallback for M1" | yes |
| "Applicability is per code" | yes |
| "11 of the 28" | yes |
| "No code is certified by all three methods" | yes |

## 7. 28-code applicability table

| | result |
|---|---|
| rows | 28 |
| methods completed | M1+M3: 24, M2+M3: 4 |
| M3 | exact: 11, lower bound: 17 |
| exact-distance evidence | M1 complete enumeration: 24, M2 support search: 4 |
| rows with three methods | **0** |

## 8. No mathematical change

All 34 `[[…]]` parameter tuples in Appendix A are **identical** to the Phase 14
canonical file (extracted and compared programmatically). No generator matrix,
distance value or quantum parameter was altered in Phase 17 — or in Phases 15–16.

## 9. Conclusion

The manuscript, its appendices and the supplementary documentation are mutually
consistent. The only open item is the **abstract wording decision** (Task B),
which is for the researcher.
