# Phase 18 — Implementation of approved abstract Option B

**Branch** `arena/59de606f-matrix-ring` · **Commit** (see §9) ·
Target journal: *Finite Fields and Their Applications* (Elsevier)

---

## 1. Researcher approval

The researcher approved **Phase 17 abstract wording Option B**, explicitly
instructing use of the **B2** wording — *not* the earlier 253-word draft, which
exceeded the 250-word limit.

| | |
|---|---|
| Approved option | **B** (B2 variant) |
| Authorising document | `PHASE17_RESEARCHER_DECISION/PHASE17_ABSTRACT_WORDING_OPTIONS.md`, §"Option B — state the 11/17 split explicitly" |
| Approved counts recorded there | C1 231 · C2 217 · C3 244 (margin 6) |
| Independently re-verified before applying | **231 / 217 / 244 — exact match** |

Applying Option B was also the recommendation recorded in
`PHASE17_RESEARCHER_DECISION_SHEET.md` §3.

## 2. Exact sentence before modification

```latex
Exhaustive computation certifies $28$ codes, each by two applicable
independent methods, one exact and one a cross-check, among them this
framework's first distance-$4$ stabilizer codes, $[[24,8,4]]_9$ and
$[[20,4,4]]_4$, and entanglement-assisted codes up to $[[20,2,10;18]]_4$.
```

## 3. Exact sentence after modification

```latex
Exhaustive computation certifies $28$ codes, each by two independent
methods: one exact, and one quantum search exact for $11$ codes and a
lower bound for $17$, among them this framework's first distance-$4$
stabilizer codes, $[[24,8,4]]_9$ and $[[20,4,4]]_4$, and entanglement-assisted
codes up to $[[20,2,10;18]]_4$.
```

The replacement was made with a single-occurrence assertion (`count == 1`) so
that no other text could be caught by accident. Exactly one file differs between
`PHASE16_WORKCOPY/` and `PHASE18_WORKCOPY/`: `main.tex`.

## 4. Word counts

| convention | before (A) | **after (B2)** | approved baseline | limit |
|---|---|---|---|---|
| C1 | 222 | **231** | 231 | — |
| C2 | 208 | **217** | 217 | — |
| C3 (strictest) | 235 | **244** | 244 | **250** |

**Remaining margin under 250: 6 words.** The delta is **+9 under all three
conventions**, attributable solely to the replacement sentence — no other word in
the abstract was altered. Title, keywords and MSC classes are byte-identical
(verified by hash). A fourth supplementary measure, a plain split of the rendered
page-1 text, gives 247 — also under 250.

## 5. Certification distribution communicated by the approved wording

| | value |
|---|---|
| codes certified | 28 |
| exactly two applicable methods per code | 28 of 28 |
| M1 + M3 | 24 |
| M2 + M3 | 4 |
| M3 exact distance | 11 |
| M3 lower bound | 17 |
| all three methods completed | **0** |

All seven values re-verified in Phase 18 against
`PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.
The conditional execution logic was **not** reinterpreted: M2 runs iff M1 did not
complete; M2 is *skipped*, not route-inapplicable; one of the four M2 codes is
entanglement-assisted.

## 6. Confirmation that all other content is unchanged

| check | result |
|---|---|
| files differing from the Phase 16 base | **1** (`main.tex`) |
| theorems, proofs, equations | unchanged |
| 13 worked examples | unchanged (13 `\begin{example}`; 13 rendered) |
| distance values, $k$, $K$, $c$, $h_E$ | unchanged |
| quantum parameter tables (34 tuples) | unchanged |
| generator matrices / construction routes | unchanged |
| 28-code certification records | unchanged |
| Appendix tables | contents unchanged; still numbered A.1 / A.2 |
| title, keywords, MSC | unchanged (verified by hash) |
| author metadata | **Arun Kumar Yadav**, K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India; arunyadav0307@gmail.com — unchanged |
| funding declaration | unchanged |
| competing-interest declaration | unchanged |
| generative-AI / data-availability sections | unchanged (deferred) |

## 7. Validation and compilation results

`tools/validate_latex_v2.py --root PHASE18_WORKCOPY` → **13 checks, 13 PASS, 0 FAIL**
(V4: 264 refs / 116 labels all resolve; V5: 116 labels, 0 duplicates).

`tools/verify_examples.py` (full run, corrected sources) → **56 checks, 0 mismatches**.

Four-pass build, TeX Live 2024, genuine `BibTeX 0.99d`, `plain.bst`, 78-line `.bbl`:

| | |
|---|---|
| errors (`^! `) | 0 |
| undefined citations | 0 |
| undefined references | 0 |
| Overfull `\hbox` | 0 |
| Underfull `\hbox` | 0 |
| missing glyphs | 0 |
| hyperref warnings | 0 |
| font warnings | 0 |
| pages | 42 |
| page size | A4, 595.3 × 841.9 pt |

Appendix tables confirmed as **Table A.1** / **Table A.2** with Tables 1–4
preserved. Example 13 (rendered **Example 8.12**) confirmed on **p. 33** with the
Phase 15 correction intact: *"The support search (M2) is run only when M1 cannot
finish, so it was not run here and contributes nothing…"*.

**No visual inspection was performed** — Arena has no vision capability. Page
images were regenerated from this build into
`PAPER/FINAL_RESEARCHER_REVIEW_V3/visual_review/` for the researcher's own
review.

## 8. New PDF and package hashes

| artefact | SHA-256 |
|---|---|
| `FINAL_RESEARCHER_REVIEW_V3/build/manuscript.pdf` (580 584 B, 42 pp) | `c87381bc29a2955c2f5822cbbbae0e80a4226e3e44ed50e3d89d595a0d16ec0c` |
| `PHASE18_WORKCOPY/main.tex` (revised) | `41b5683cef735f22a70af116f3ba331be86cb67fd0bfcb3dcbfe38db3dd258e1` |
| `PHASE16_WORKCOPY/main.tex` (pre-edit base) | `c876aa73b114ed7bbba3a9d78e4a6e8e04b9b5349fddcbea27163c55c642537e` |
| `FINAL_RESEARCHER_REVIEW_V3/SHA256_MANIFEST.txt` | `3ec3439969d865dfc5caa8701e926992f1bb819b4bd2efdb4d37bf92ee3bb8df` |

The V3 package carries **72 manifest entries, all verified OK**.
`PAPER/FINAL_RESEARCHER_REVIEW_V2/` is preserved unchanged (131 entries, all OK).

## 9. Traceability of the single authorized edit

The edit is traceable end-to-end:

1. Approval → `PHASE17_RESEARCHER_DECISION/PHASE17_ABSTRACT_WORDING_OPTIONS.md` (Option B, B2 text and counts).
2. Base → `PAPER/PHASE16_WORKCOPY/main.tex`.
3. Edit → `PAPER/PHASE18_WORKCOPY/main.tex` (one sentence; `diff -rq` shows exactly one differing file).
4. Verification → `FINAL_RESEARCHER_REVIEW_V3/reports/ABSTRACT_WORD_COUNT_REPORT.md` and `…/CERTIFICATION_CONSISTENCY_REPORT.md`.
5. Build → `FINAL_RESEARCHER_REVIEW_V3/build/manuscript.pdf` + `main.log`.
6. Record → this file.

## 10. Deferred items — unchanged

Generative-AI declaration, GitHub data-access arrangements, licence selection,
Zenodo deposit, GitHub release/tag, public-repository publication and journal
submission all remain **deferred at their existing status**. Nothing in Phase 18
touched them.

## 11. Stopping point

Phase 18 is complete. The approved Option B has been applied, validated and
packaged. **No submission, no publication, no release, no tag, no licence, no new
research.** Awaiting explicit researcher approval.
