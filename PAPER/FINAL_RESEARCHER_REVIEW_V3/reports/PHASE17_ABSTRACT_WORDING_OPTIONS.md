# Phase 17 / Task B — Abstract wording options

**Nothing here has been applied.** The canonical manuscript is untouched; this
document exists so the researcher can choose.

## The sentence under review

Current text (in `main.tex`, abstract):

> Exhaustive computation certifies $28$ codes, each by two applicable
> independent methods, one exact and one a cross-check, among them this
> framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
> $[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.

The tail ("among them … $[[20,2,10;18]]_4$.") is identical in all three options.

## Is the current wording strictly accurate for all 28 records?

**Yes, at the level of roles — and that is the whole question.**

* "two applicable independent methods" — true for all 28 (M1+M3 for 24, M2+M3 for 4).
* "one exact" — true for all 28: exactly one of M1/M2 runs, and it is exhaustive.
* "one a cross-check" — true for all 28: M3 always runs and always corroborates.

The wrinkle is that **M3's cross-check is not uniform in strength**. For 11 codes
M3 returns the exact minimum (it scans weights 1…w3 in increasing order and
returns the first hit), so those codes have two independent *exact*
determinations. For the other 17 it returns nothing below the search weight and
yields only a proved lower bound.

So the current wording is not **false**; it is **silent** on a distinction a
reader could resolve either way — inferring that the cross-check is always a
lower bound (understating 11 codes) or that it always confirms exactly
(overstating 17). §8.5 and Appendix A now state the 11/17 split explicitly, so
the manuscript as a whole is not misleading. The question is only whether the
abstract should carry it.

## Word counts

Three conventions, as established in Phase 14/15. **C3 is the strictest** and is
the one to judge against the 250-word limit.

| | C1 | C2 | C3 | margin (C3) | limit 250 |
|---|---|---|---|---|---|
| current (= Option A) | 222 | 208 | **235** | 15 | compliant |
| **Option A** | 222 | 208 | **235** | 15 | compliant |
| **Option B** | 231 | 217 | **244** | 6 | compliant |
| **Option C** | 224 | 210 | **237** | 13 | compliant |
| Option B, first draft (rejected) | 240 | 226 | **253** | −3 | **over limit** |

> **Note.** The obvious first draft of Option B ("…one an ambient quantum search
> that is itself exact for $11$ codes and a proved lower bound for the other
> $17$…") came out at **253 words under C3 — over the limit**. Option B below is
> a tightened variant that fits with 6 words to spare. This is recorded because
> it constrains the choice: the fully explicit phrasing does **not** fit without
> cutting elsewhere in the abstract.

---

## Option A — retain the current wording

> Exhaustive computation certifies $28$ codes, each by two applicable
> independent methods, one exact and one a cross-check, among them this
> framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
> $[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.

**Counts:** C1 222 · C2 208 · C3 **235** (margin 15).

**Mathematical accuracy.** Accurate for all 28 records at the level of roles.
Does not misstate any count. Silent on the 11/17 split.

**Advantages.**
* Shortest and least cluttered of the three; leaves 15 words of headroom.
* Roles are stated correctly; nothing in it is false.
* The precise split is already carried in §8.5 and Appendix A, which is where a
  referee looking for the detail will find it.
* No change to a manuscript that has now been through two correction phases.

**Limitations.**
* A referee reading *only* the abstract cannot tell whether the cross-check is
  exact or a lower bound, and might assume uniformity in either direction.
* Carries a mild risk that the abstract is read as claiming more uniform
  corroboration than the records show.

## Option B — state the 11/17 split explicitly

> Exhaustive computation certifies $28$ codes, each by two independent
> methods: one exact, and one quantum search exact for $11$ codes and a
> lower bound for $17$, among them this framework's first distance-$4$
> stabilizer codes, $[[24,8,4]]_9$ and $[[20,4,4]]_4$, and entanglement-assisted
> codes up to $[[20,2,10;18]]_4$.

**Counts:** C1 231 · C2 217 · C3 **244** (margin 6).

**Mathematical accuracy.** Fully accurate and complete at abstract length: two
methods per code, one exact, and the cross-check's strength quantified. Drops
"applicable" (all methods that ran were applicable) and "independent" for length;
independence is asserted in §8.5 and is genuine (M3 works in the ambient
symplectic space, M1/M2 in the classical difference set).

**Advantages.**
* Removes the ambiguity entirely; the abstract alone is self-contained on the
  point most likely to draw a referee's question.
* Pre-empts the obvious review question "were all three methods run on every
  code?" by quantifying instead of hedging.

**Limitations.**
* Only 6 words of headroom under the strictest count; any other abstract edit
  risks breaching 250.
* Denser prose. Drops "independent" from the abstract (still stated in §8.5).
* Needs the tightened phrasing — the natural, more explicit version is over the
  limit.

## Option C — most conservative

> Exhaustive computation certifies $28$ codes, the distance of each by one
> exact method and corroborated by one further method, among them this
> framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
> $[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.

**Counts:** C1 224 · C2 210 · C3 **237** (margin 13).

**Mathematical accuracy.** Accurate for all 28 and deliberately under-claims:
"one exact method" is true, "corroborated by one further method" is true for all
28 whether M3 was exact or a lower bound.

**Advantages.**
* Hardest to attack: asserts the minimum that all 28 records support, and
  declines to lean on either independence or uniformity.
* Robust if a referee interprets "cross-check" or "independent" strictly.
* 13 words of headroom.

**Limitations.**
* Least informative: does not convey that M3 is independent of M1/M2 (which it
  genuinely is), nor that the corroboration is exact for 11 codes.
* Understates the certification: a reader cannot tell that 11 codes have two
  independent exact determinations.
* "one further method" is vaguer than "a cross-check".

---

## Summary comparison

| | A (retain) | B (explicit) | C (conservative) |
|---|---|---|---|
| C3 words / margin | 235 / 15 | 244 / 6 | 237 / 13 |
| states two methods per code | yes | yes | yes |
| states one exact method | yes | yes | yes |
| quantifies M3's 11/17 split | **no** | **yes** | no |
| asserts independence | yes | no (in §8.5) | no |
| risk of overstating | low | **lowest** | lowest |
| risk of understating | low | **lowest** | **high** |
| headroom for other edits | most | least | second |

## What each option would change if selected

| option | files touched | change |
|---|---|---|
| **A** | **none** | No edit. §8.5 and Appendix A already carry the 11/17 split; nothing further is required. |
| **B** | `main.tex` abstract (1 sentence) | Replace the certification sentence; **no other change** — §8.5, Appendix A, the supplementary procedure and the applicability table already state the split and need no edit. |
| **C** | `main.tex` abstract (1 sentence) | Replace the certification sentence; no other change. |

In **all three** cases: no theorem, proof, generator matrix, distance value,
quantum parameter, author metadata, funding statement or competing-interest
declaration is touched. The change is one sentence of the abstract, or none at
all.

**Awaiting the researcher's choice. Nothing has been applied.**
