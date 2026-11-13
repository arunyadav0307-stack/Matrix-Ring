# Phase 16 / Task A — Certification-method audit

**Objective.** Reconstruct, for each of the 28 certified codes, which of the three
certification methods actually executed — from the committed source, without
relying on any summary description.

---

## 1. The execution logic, read from the source

All per-code behaviour follows from `scripts/phase7_extended_search.py`,
function `part6_certification` (lines 1670–1681), quoted verbatim:

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"
else:
    # M2 is run only when M1 could not finish; searching up to the
    # reported value is what an INDEPENDENT confirmation needs (it
    # must find a codeword of exactly that weight and none below)
    d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd,
                             maxw=min(8, max(3, (r["d"] or 0) + 1)))
w3 = 3 if N <= 8 else 2
d3, wit3 = P6.ambient_quantum_search(F, N, YV, Vgen, w3)
```

Read literally, three rules:

1. **M1 is attempted for every code.**
2. **M2 executes if and only if M1 did not complete.** When M1 completes, `d2` is
   `None` and the table records `n/a`.
3. **M3 always executes**, independently of M1 and M2.

It follows that the number of methods executed per code is **two, by
construction**, and the pair is (M1, M3) or (M2, M3). Never (M1, M2, M3); never
(M1, M2).

### What each method returns

| | implementation | returns | meaning of the result |
|---|---|---|---|
| **M1** | `phase6…enum_min_weight(Gd, F, N, exd, cap=262144, slow_cap=50000)` | `(d, complete)` | `complete=True` → exact. Falls back to a slower enumeration (`slow_cap=50000`) for odd characteristic. `(None, False)` if neither completes. |
| **M2** | `phase5…min_weight_in(Gd, F, N, exclude=exd, maxw=min(8,max(3,d+1)))` | `d` or `None` | Exhaustive up to `maxw`; `None` means "no codeword of weight ≤ maxw", a rigorous lower bound, never a guess. |
| **M3** | `phase6…ambient_quantum_search(F, N, Y, Vgen, maxw=w3)`, `w3 = 3 if N<=8 else 2` | `(w, witness)` or `(None, None)` | Scans symplectic weights 1…`w3` **in increasing order**, so a returned `w` is the true minimum → **exact**. `None` → proved `d ≥ w3+1`, a **lower bound**. |

The `exact` column is `agree = (not comp1 or d1 == rep) and (d2 is None or d2 == rep) and (M3 consistent) and abelian and (K == r["K"]) and (c == r["c"])` — i.e. "every method that actually ran agrees".

---

## 2. Result for the 28 certified codes

| | M1 completes | M1 does not complete | total |
|---|---|---|---|
| codes | **24** | **4** | **28** |
| exact-distance method | M1 | M2 | — |
| M2 | conditionally skipped | run (exact) | — |
| M3 | run | run | 28 |
| **methods executed** | **M1 + M3** | **M2 + M3** | **2 per code** |

* **0 of 28 codes executed all three methods. 28 of 28 executed exactly two.**
* M3's cross-check is **exact for 11** codes and a **proved lower bound for 17**.
  The 11 are precisely those where M3 returned a value; in every one of them the
  returned value equals the reported `d`.
* The 17 lower-bound results are all consistent with the reported `d`
  (verified individually: `d > w3` in every case).

### Applicability is per code, not per route

The four codes for which M2 ran are:

| code | family | route |
|---|---|---|
| $[[24,8,4]]_9$ | $(9,1,6)$ | SO |
| $[[20,4,4]]_4$ | $(4,1,5)$ | SO |
| $[[20,4,4]]_4$ | $(4,1,5)$ | DC |
| $[[24,6,4;18]]_9$ | $(9,3,2)$ | **EA** |

One of the four is entanglement-assisted, so **"M2 is not applicable to the EA
route" is false**; and 24 EA codes used M1 while one did not, so "EA codes use
M1" is usually but not universally true. Only the per-code record settles it.
This is why the corrected documentation states the rule per code rather than per
route.

---

## 3. Four-way cross-check

Every one of the 28 rows was verified against four independent sources:

| source | what it establishes |
|---|---|
| `scripts/phase7_extended_search.py` | the conditional rule (M2 runs iff M1 fails) |
| `logs/phase7_extended_search_log.txt`, Part 6 (lines 449–478) | what the program actually printed |
| `parameter_tables/certified_codes.csv` | the tabulated M1/M2/M3 columns |
| `generator_matrices/*.json` | `k, K, d, c, h_E, distance_method` per code |

Checks performed per row: M1/M2 consistency with the conditional rule; M3 exact
⇔ no `>` prefix; log row located and M1/M2/M3/d matching the CSV; `exact == yes`;
generator JSON present and `k, K, d, c` matching the CSV.

**Result: 28 rows, 0 discrepancies.**

Two lookups were corrected during the audit and are noted for transparency:

* an initial generator-JSON key of `(code, q, t, n)` collided on the two codes
  sharing the identifier $[[20,4,4]]_4$ (routes SO and DC); the key was extended
  to include `route`, which resolved it. It was a lookup defect, not a data
  discrepancy.
* `scripts/__pycache__/` (4 `.pyc` files) existed in the working tree, produced
  by the verification runs themselves. It is generated bytecode, gitignored and
  not part of the package; it was removed before manifesting.

---

## 4. Where the overclaim came from

Line 478 of `logs/phase7_extended_search_log.txt`, check `[EXH] E1`:

> "every headline code is certified by the three independent methods (classical
> enumeration, support search, ambient quantum search)"

That wording is wrong and is the origin of both the manuscript's Phase 15 CP-1
defect and this package's `CERTIFICATION_PROCEDURE.md` defect. It is a historical
record of what the program printed and has **not** been rewritten.

---

## 5. Deliverable

`PHASE16_28_CODE_APPLICABILITY_TABLE.csv` — 28 rows × 15 columns, giving per
code: identifier, family, route, $N,k,K,c,d$, M1 execution status, M2 execution
status, M3 execution status, methods actually completed, exact-distance evidence,
cross-check result, and the JSON `distance_method`.
