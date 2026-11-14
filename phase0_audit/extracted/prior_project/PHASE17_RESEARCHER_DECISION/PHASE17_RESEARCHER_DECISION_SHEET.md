# Phase 17 — Researcher decision sheet

**Branch** `arena/59de606f-matrix-ring` · **Commit** `48f507c` (Phase 16) ·
Phase 17 adds decision documents only.

**Nothing has been applied.** The canonical manuscript is untouched. This sheet
exists so you can make the one remaining decision.

---

## 1. Certification-method distribution (confirmed, 28/28, 0 discrepancies)

| | count |
|---|---|
| M1 + M3 | **24** |
| M2 + M3 | **4** |
| M3 exact (independent exact determination) | **11** |
| M3 lower bound (corroborating bound only) | **17** |
| **three methods completed** | **0** |
| total certified codes | **28** |

Reconstructed from the committed source, not from summaries, and cross-checked
against four independent sources — the source code, Part 6 of the Phase 7 log,
`certified_codes.csv`, and the 28 generator-matrix records.

**Key distinctions, stated precisely:**

* **M2 is *skipped*, not inapplicable**, for the 24 codes where M1 completed. The
  source branches on `comp1`, not on the route, and one of the four codes where
  M2 *did* run is entanglement-assisted ($[[24,6,4;18]]_9$). Route-based accounts
  of the rule are wrong.
* **M1 "did not complete"** for 4 codes: it was attempted and its enumeration cap
  was insufficient — a computational limit, not a routing decision.
* **M3 always runs** and is structurally independent of M1/M2 (ambient symplectic
  space vs classical difference set). Its *strength* is what varies: exact for 11,
  lower bound for 17.

## 2. Abstract wording options

Current sentence (unchanged since Phase 15):

> Exhaustive computation certifies $28$ codes, each by two applicable
> independent methods, one exact and one a cross-check, among them this
> framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
> $[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.

### Option A — retain the current wording

No change. Counts: **C1 222 · C2 208 · C3 235** (margin 15).
Accurate for all 28 at the level of roles. Silent on the 11/17 split, which is
already stated in §8.5 and Appendix A.

### Option B — state the 11/17 split explicitly

> Exhaustive computation certifies $28$ codes, each by two independent
> methods: one exact, and one quantum search exact for $11$ codes and a
> lower bound for $17$, among them this framework's first distance-$4$
> stabilizer codes, $[[24,8,4]]_9$ and $[[20,4,4]]_4$, and entanglement-assisted
> codes up to $[[20,2,10;18]]_4$.

Counts: **C1 231 · C2 217 · C3 244** (margin 6).

### Option C — most conservative

> Exhaustive computation certifies $28$ codes, the distance of each by one
> exact method and corroborated by one further method, among them this
> framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
> $[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.

Counts: **C1 224 · C2 210 · C3 237** (margin 13).

> ⚠️ The natural, fuller phrasing of Option B ("…one an ambient quantum search
> that is itself exact for $11$ codes and a proved lower bound for the other
> $17$…") came out at **253 words under C3 — over the 250 limit**. Option B above
> is a tightened variant that fits with 6 words to spare. If you prefer the fuller
> phrasing, ~4 words must be cut elsewhere in the abstract.

| | A | B | C |
|---|---|---|---|
| C3 words / margin | 235 / 15 | 244 / 6 | 237 / 13 |
| quantifies 11/17 | no | **yes** | no |
| asserts independence | yes | no (in §8.5) | no |
| risk of overstating | low | **lowest** | lowest |
| risk of understating | low | **lowest** | **high** |

## 3. Recommended option: **B**

Reasoning:

1. **The ambiguity is the only real defect left, and B is the only option that
   removes it.** A reader of the abstract alone currently cannot tell whether the
   cross-check is exact or a bound. §8.5 fixes it for anyone who reads on, but
   the abstract is what a referee reads first — and what an indexing service
   reproduces.
2. **It is the most accurate of the three for all 28 records.** B is the only
   option whose abstract-level statement is exact rather than merely
   non-misleading.
3. **It costs 9 words and stays within the limit** (244/250 under the strictest
   convention), so the gain is nearly free.
4. **It pre-empts the predictable referee question** — "were all three methods
   run?" — by quantifying rather than hedging. A and C both require the reader to
   go to §8.5 to get the answer.
5. **C understates the work.** Eleven codes have two independent exact
   determinations; C conveys none of that. Conservative wording is right when the
   evidence is thin, not when it is strong and simply non-uniform.

**If you would rather keep the abstract short, A is a perfectly defensible
second choice** — it is accurate for all 28 records, and the split is stated in
§8.5 and Appendix A. Choose C only if you want the manuscript to assert the
minimum that every record supports, accepting that it understates 11 codes.

## 4. Exact changes that would follow from each option

| option | files changed | change |
|---|---|---|
| **A** | **none** | No edit required. §8.5, Appendix A, the supplementary procedure and the applicability table already carry the 11/17 split. |
| **B** | `main.tex`, one sentence of the abstract | Replace the certification sentence with the Option B text. **No other file changes** — every other location already states the split. One rebuild + manifest refresh. |
| **C** | `main.tex`, one sentence of the abstract | Replace the certification sentence with the Option C text. No other file changes. One rebuild + manifest refresh. |

In **all three cases** no theorem, proof, generator matrix, distance value,
quantum parameter, author metadata, funding statement or competing-interest
declaration is touched. Selecting A requires no rebuild at all.

## 5. Confirmation: mathematical parameters unchanged

| check | result |
|---|---|
| 34 `[[…]]` parameter tuples in Appendix A vs the Phase 14 canonical file | **identical** |
| distance values, $k$, $K$, $c$, $h_E$, generator matrices | **unchanged** (Phases 15–17) |
| mathematical results, theorems, proofs | **unchanged** |
| author metadata, funding, competing interests | **unchanged** |
| Phase 0–16 files and historical packages | **preserved** |
| original supplementary package (`PAPER/supplementary/`) | **untouched**, manifest 85/85 OK |
| Phase 7 log and scripts | **not rewritten** |

## 6. Remaining researcher-review items

**Decision required now:**

1. **Abstract wording — A, B or C.** (Recommended: B.) Nothing will be applied
   until you choose.

**Your visual review (Arena cannot do this — no vision capability):**

2. Pages **1, 31, 33, 38–39** of `PAPER/FINAL_RESEARCHER_REVIEW_V2/build/manuscript.pdf`
   (or the images in `visual_review/`). Programmatic checks confirm the expected
   *text*; typography, layout and table presentation need your eyes. Index:
   `PHASE17_VISUAL_REVIEW_INDEX.md`.

**Still open, unchanged, out of scope for Phase 17:**

3. Generative-AI declaration — you state language-enhancement-only; the records
   show broader use. **Pending reconciliation.**
4. Data availability — GitHub-only; supplementary data absent from `main`.
5. Licence — recommendation only; **nothing applied**.
6. Four GitHub fixes awaiting authorisation: merge into `main`, release/tag,
   branch protection, licence.
7. CP-4 — 9 DOIs in `references.bib`, none rendered (`plain.bst` has no `doi`
   field). **Retained deliberately**; FFA applies reference formatting at proof
   stage.

## 7. Status of this phase

Phase 17 is complete as a decision-support and archival task. **No manuscript
edit, no rebuild, no submission, no release, no tag, no licence, no external
action.** Awaiting your choice of abstract wording.
