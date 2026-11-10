# Phase 19 — FFA journal-specific formatting and cover-letter preparation

**Branch** `arena/59de606f-matrix-ring` · Target journal: *Finite Fields and
Their Applications* (Elsevier)

Scope: journal formatting, presentation, cover-letter drafting and
submission-document preparation. **No new mathematical research; no mathematical
result changed. No submission was made.**

---

## 1. Starting conditions

| check | result |
|---|---|
| branch / remote | `arena/59de606f-matrix-ring`, local == remote == `c5e7574` |
| Phase 18 commit `c5e7574` | present |
| working tree | clean (0 uncommitted) |
| V3 package | 72 manifest entries, **72/72 OK** |
| 13 worked examples | **13** `\begin{example}` environments |
| quantum parameter tables | **34** tuples, identical to the canonical file |
| V3 PDF | `c87381bc…d16ec0c` |
| supplementary manifests | historical **85/85 OK**; corrected **86/86 OK** |
| protected hashes recorded | **51** |

## 2. Task A — official requirements re-verified

Primary source, **accessed 2026-11-10**:
<https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/guide-for-authors>

Supporting: journal home, submission portal (<https://submit.elsevier.com/FFA>),
Elsevier LaTeX support (<https://www.elsevier.com/latex>), and the research-data
guidelines (Option C) — all accessed 2026-11-10.

**Finding: the official guidelines are UNCHANGED** from the Phase 10 audit.
Every requirement was re-read from the live page this phase and matches the
Phase 10 record verbatim. The Phase 10 *compliance score* was **not** relied
upon.

Notable confirmations:

* **Abstract** — *"does not exceed 250 words… stand alone… Avoid references."*
* **Keywords** — *"1 to 7 keywords"*, avoid "and"/"of".
* **Tables** — *"Avoid vertical rules and shading within table cells."*
* **Appendices** — *"Identify individual appendices… A, B, etc."* and *"give
  separate numbering to tables and figures using formats such as Table A.1;
  Fig. A.1"* — confirming the Phase 16 CP-3 fix.
* **References** — *"This journal does not set strict requirements on reference
  formatting at submission… any style or format as long as the style is
  consistent… Our journal reference style will be applied… at proof stage."*
  So **`plain.bst` is acceptable for initial submission**; it was retained.
  (The guide separately says *"Where available include DOIs"*; 9 of 13 entries
  carry a DOI in `references.bib` but `plain.bst` renders none. Recorded as a
  documented limitation, not changed.)
* **Research data** — **Option C is required**: deposit in a repository and
  provide a link, or state why not. **Unresolved.**

Full table with per-item status: `PAPER/FFA_FORMATTED_SUBMISSION/FFA_GUIDELINE_VERIFICATION.md`.

## 3. Task B — FFA-specific copy

Created `PAPER/FFA_FORMATTED_SUBMISSION/` from V3.

**Exactly one change to the manuscript source** (`diff -rq` reports one
differing file):

| file | before | after | requirement |
|---|---|---|---|
| `sections/07_quantum.tex` | `\chi(x)=e^{2\pi i x/p}` | `\chi(x)=\exp(2\pi i x/p)` | *"Denote powers of $e$ by exp."* |

Mathematically identical. No other occurrence of Euler's number as a superscript
exists (remaining `e^{` matches are `\widehat{}`).

**Preserved unchanged:** the approved title; the approved Option B2 abstract;
the confirmed single-author information; affiliation and corresponding-author
email; funding and competing-interest declarations; all definitions and
theorems; all proofs; all 13 worked examples; all quantum parameters; all
references and appendices.

**Compliance verified without change:** 7 keywords; abstract 231/217/**244**;
title-page elements complete; 0 vertical rules and 0 shading macros in tables;
all 6 tables cited; equation numbering consecutive (12, none in appendices);
appendices A and B with Table A.1/A.2; 0 figures (N/A).

**Declined, with reasons recorded:** migration to the Elsevier CAS LaTeX template
(encouraged, not required — declined to avoid reworking a zero-error build for
no compliance gain); changing the bibliography style (explicitly acceptable);
adding a CRediT statement (single author; inventing contribution roles is
prohibited).

## 4. Task C — scientific presentation

All required elements are present in the Introduction and the manuscript: the
ring framework $R=M_2(A_t)$; the **right-module convention**; Galois duality and
hull theory; the non-principal hull contributions; the Gray-map compatibility
result; the quantum-code constructions; and an explicit statement of
contributions **and limitations**.

**Morita equivalence is described accurately.** The manuscript states that
Morita equivalence *"is an equivalence of module categories, not of rings with
involution, and it does not carry the duality"*, that the duality and hull
statements are proved for $R$ and $\theta_s$ *before* any Morita translation,
and that Morita is used only to convert hull structure theory into a computation
with submodules of $B^2$. This is correct and appropriately hedged.

**No overclaiming.** A scan for *improve the best known*, *outperform*, *new
record*, *state of the art*, *superior to all known* returned **zero** matches.
The manuscript affirmatively states it is *"at best equal to the best known
distance"*, that it *"does not claim"* record parameters, and *"No record
parameters are claimed."*

## 5. Task D — cover letter

`PAPER/FFA_FORMATTED_SUBMISSION/COVER_LETTER_DRAFT.md` — **draft, not sent.**

It follows the required contribution hierarchy (Galois duality and hull theory →
non-principal hull structure → Gray-map representation → quantum constructions →
exact-distance certification and parameter analysis), explains the significance
of the noncommutative framework and the Morita relationship accurately, and
states the certification result precisely — two methods per code, M3 exact for 11
and a lower bound for 17, **no code certified by all three**.

It explicitly states that **no improvement over established quantum records is
claimed**, and it marks as **PENDING CONFIRMATION** the originality, exclusive
submission and no-simultaneous-submission statements, the generative-AI
declaration and the research-data statement. It makes no claim of acceptance or
prior endorsement.

## 6. Tasks E–F — checklist, compile and validation

`FINAL_SUBMISSION_CHECKLIST.md` distinguishes ✅ Completed · ⏳ Pending · ➖ Not
applicable · ⚠️ Unverified, and states plainly that the manuscript is **not**
fully submission-ready.

Compilation (TeX Live 2024, genuine `BibTeX 0.99d`, `plain.bst`, 78-line `.bbl`):

| check | result |
|---|---|
| errors (`^! `) | **0** |
| undefined citations / references | **0 / 0** |
| missing glyphs | **0** |
| Overfull / Underfull `\hbox` | **0 / 0** |
| `validate_latex_v2.py` | **13 PASS / 0 FAIL** |
| `verify_examples.py` | **56 checks / 0 mismatches** |
| pages | **42** |
| bytes | 580 175 |
| **PDF SHA-256** | `a87491e2ac5071a896b4fd29d25054dc3de9a51275bd2d9dda32975a7f1bff68` |

Verified after the change: abstract still 231/217/**244** (margin 6); Option B2
unchanged in the rendered PDF; 13 examples present; Example 13 correct on p. 33;
Table A.1/A.2 correct; 34 parameter tuples identical to canonical; all
references resolve.

**No visual inspection was performed** — Arena has no vision capability. All
results are programmatic.

## 7. Task G — package

`PAPER/FFA_FORMATTED_SUBMISSION/`: `main.tex`, **12** section/appendix files,
`references.bib`, compiled `main.pdf`, `COVER_LETTER_DRAFT.md`,
`FINAL_SUBMISSION_CHECKLIST.md`, `FFA_GUIDELINE_VERIFICATION.md`,
`FORMATTING_CHANGE_RECORD.md`, `main.log`, `SHA256_MANIFEST.txt`, `README.md`,
plus `HIGHLIGHTS.md`, `main.bbl`, `build_modern/` and `compile/`.

**55 manifest entries, all verified.** Size 1.8 MB.
`PAPER/FINAL_RESEARCHER_REVIEW_V3/` preserved unchanged (72/72).

## 8. Deferred matters — untouched

Generative-AI declaration, GitHub data-access arrangements, licence selection,
Zenodo deposit, GitHub releases/tags: **status unchanged**; documents untouched;
no declaration text invented.

## 9. Remaining blockers

1. **Research-data deposit and link** (FFA Option C) — required, unresolved.
2. **Generative-AI declaration** — required where applicable, unresolved.
3. **Author confirmations** of originality, exclusive submission, no
   simultaneous submission.
4. **Supplementary per-file captions** — recommended.
5. **Visual review of the rendered PDF** — cannot be performed by Arena.

## 10. Stopping point

Phase 19 is complete. **No submission, no Elsevier upload, no Editorial Manager
account, no cover letter sent, no journal change, no public-repository
modification, no external release.** Awaiting explicit researcher approval.
