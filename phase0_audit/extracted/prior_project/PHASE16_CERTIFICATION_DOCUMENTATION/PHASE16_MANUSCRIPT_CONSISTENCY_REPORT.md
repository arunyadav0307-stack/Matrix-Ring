# Phase 16 / Task D — Manuscript and supplementary documentation consistency

## 1. Scope of the check

Consistency was verified across: abstract, introduction, certification section
(§8.5), Example 13, Appendix A, the supplementary certification documentation,
the claim-traceability matrix, and the final validation report.

The manuscript's corrected statement is that each code is certified by **two
applicable methods**. This is **supported by all 28 records** — verified row by
row, 0 discrepancies.

---

## 2. A genuine inconsistency found: the M3 cross-check is not uniform

Task D asked specifically whether the phrase **"one exact method and one
cross-check"** is accurate for every record. It is accurate at the level of
*roles*, but it is **not uniform in strength**, and one place in the manuscript
asserted uniformity that the records contradict.

### The evidence

`ambient_quantum_search` scans symplectic weights $1,2,\dots,w3$ **in increasing
order** and returns the first hit. Therefore:

* a returned value **is** the true minimum → M3 gives an **exact** determination;
* `None` → proved $d\ge w3+1$, a **lower bound** only.

| M3 outcome | codes |
|---|---|
| returned a value, equal to the reported `d` → **exact** | **11** |
| returned nothing below `w3` → **lower bound**, consistent with `d` | **17** |

All 11 exact cases satisfy `M3 == d` (verified individually); all 17 lower-bound
cases satisfy `d > w3` (verified individually).

### The defect

Appendix A stated:

> M3 is therefore a cross-check rather than an exact method.

That blanket claim is **false for the 11 codes** where M3 independently
determines the distance exactly. §8.5 was, by contrast, correctly hedged
("which for most codes yields a proved lower bound rather than an exact value").

### Correction applied

| location | before | after |
|---|---|---|
| Appendix A | "M3 is therefore a cross-check rather than an exact method." | M3 "searches in increasing symplectic weight from 1, so a returned value is the true minimum: an entry 2 or 3 is therefore M3 *independently determining* the distance exactly, and this happens for 11 of the 28 codes… this happens for the remaining 17 codes. So the cross-check supplied by M3 is an exact independent determination for 11 codes and a consistent proved lower bound for the other 17 — **it is not uniform across the table**, and the per-row entry, not a general rule, settles what M3 gave for a particular code." |
| §8.5 | "which for most codes yields a proved lower bound rather than an exact value" | retains that hedge and adds the explicit split: "a returned value is the true minimum and is an independent exact determination; this occurs for 11 of the 28 codes. For the remaining 17 it finds no vector at or below the search weight and yields a proved lower bound only… **the strength of the M3 cross-check is not uniform: it is exact for 11 codes and a lower bound for 17**." |

### Decision on the abstract

The abstract reads "each by two applicable independent methods, one exact and
one a cross-check". At 235 words against the 250-word limit, this is **accurate
at the level of roles** (M1/M2 establishes the exact distance; M3 corroborates)
and is **left unchanged**. The precise 11/17 split is carried in §8.5 and
Appendix A, which is where it belongs. This is recorded as a deliberate
decision, not an oversight: the instruction was not to force a uniform
description, and the body text now states the distinction explicitly.

---

## 3. Consistency matrix (all items verified against the 28 records)

| item | statement | supported by all 28? |
|---|---|---|
| abstract | "each by two applicable independent methods, one exact and one a cross-check" | **yes** (roles); strength split not claimed there |
| Introduction | "the exact distance of each by an applicable exact method cross-checked by an independent ambient quantum search" | **yes** |
| §8.5 methodology | one exact method (M1 or M2); M3 cross-check; 11 exact / 17 lower bound; no code has all three | **yes** |
| Example 13 | M2 "run only when M1 cannot finish, so it was not run here"; M3 certifies $d\ge3$ as a lower bound | **yes** (this code: M1 exact, M2 skipped, M3 `>2`) |
| Appendix A column notes | dash = M1 did not complete; `n/a` = M2 not run; M3 read per row; 11 exact / 17 lower bound | **yes** |
| supplementary `CERTIFICATION_PROCEDURE.md` (corrected) | 24 M1 / 4 M2; M2 skipped because M1 completed; 11 exact / 17 lower bound; per code not per route | **yes** |
| claim-traceability T-225 | two applicable methods per code; 0 of 28 have all three | **yes** |
| validation report | 56 checks / 0 mismatches; two methods per code | **yes** |

---

## 4. What was not changed

* **No mathematical distance value.** Every `d` in every table is unchanged; the
  corrections concern only how the certification of those values is described.
* **No quantum parameter.** All 34 parameter tuples in Appendix A are
  byte-identical to Phase 15 (verified: 0 data lines changed).
* **No theorem, proof, generator matrix, author metadata, funding statement or
  competing-interest declaration.**

---

## 5. Remaining minor point

The abstract's role-level phrasing is a compression that a reader could
over-interpret in either direction (that the cross-check is always a lower bound,
or that it always confirms exactly). This is judged acceptable given the 250-word
limit and the explicit treatment in §8.5 and Appendix A, and is reported here so
the researcher can decide whether to accept it.
