# Task E — Final submission checklist

**Status legend:** ✅ Completed · ⏳ Pending researcher confirmation ·
➖ Not applicable · ⚠️ Unverified / unresolved

**The manuscript is NOT described as fully submission-ready.** Mandatory items
remain unresolved (research data, generative-AI declaration, and the author's
own originality/exclusivity confirmations).

---

## A. Files to upload

| item | status | note |
|---|---|---|
| Manuscript PDF | ✅ | `build/manuscript.pdf`, 42 pp, SHA-256 `a87491e2ac5071a896b4fd29d25054dc3de9a51275bd2d9dda32975a7f1bff68` |
| LaTeX sources (`.tex`) | ✅ | `main.tex` + 13 section files — **mandatory**; a PDF alone is not an acceptable source file |
| Bibliography (`.bib` + `.bbl`) | ✅ | `references.bib`; `plain` style, acceptable at submission |
| Figures | ➖ | The manuscript contains **0** figures |
| Tables | ✅ | 6 tables, editable text, all cited and captioned |
| Supplementary code and data | ⏳ | 86 files in `PAPER/SUPPLEMENTARY_V2/`. **Per-file captions not yet written** (FFA asks for a concise caption per file) |
| Highlights file | ⏳ | `HIGHLIGHTS.md` prepared (encouraged, not required) — author confirmation needed |
| Cover letter | ⏳ | `COVER_LETTER_DRAFT.md` drafted; **not sent**, and contains items pending author confirmation |

## B. Manuscript content

| item | status | note |
|---|---|---|
| Title | ✅ | unchanged and approved |
| Abstract | ✅ | Option B2 applied; 231 / 217 / **244** words (C1/C2/C3), limit 250 |
| Keywords | ✅ | 7 (FFA allows 1–7) |
| MSC classes | ➖ | not required by FFA; present |
| Sections and subsections | ✅ | numbered |
| Theorem / lemma / definition / proof environments | ✅ | 83 theorem-like environments |
| Equation numbering | ✅ | 12, consecutive; `exp` notation applied |
| Appendix numbering | ✅ | A, B; **Table A.1**, **Table A.2** |
| 13 worked examples | ✅ | 13 present; Example 13 verified on p. 33 |
| Quantum parameter tables | ✅ | 34 tuples identical to canonical |
| References resolve | ✅ | 13 entries, 13 cited, 0 undefined |

## C. Author and declarations

| item | status | note |
|---|---|---|
| Author name | ✅ | Arun Kumar Yadav (single author) |
| Affiliation with postal address and country | ✅ | K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India |
| Corresponding-author email on title page | ✅ | arunyadav0307@gmail.com |
| Funding statement | ✅ | "did not receive any specific grant…" |
| Competing-interest statement | ✅ | present; the Elsevier declarations tool should also be completed at upload |
| CRediT author statement | ⏳ | encouraged, not required; not invented for a single author |
| Acknowledgements section | ✅ | present, before the reference list |
| **Declaration of generative AI** | ⏳ | **REQUIRED where applicable and currently UNRESOLVED.** The researcher states language-enhancement-only; the records show broader use. Not reconciled. **Deferred — do not invent text.** |
| **Research-data statement (Option C)** | ⏳ | **REQUIRED.** Deposit in a repository + link, or a statement why not. Currently: existing public GitHub repository only; supplementary data absent from the default branch. **Unresolved.** |
| Originality / exclusive submission / no simultaneous submission | ⏳ | **Author's own confirmation required** — not asserted in the cover letter |

## D. Technical verification (this phase)

| check | status | result |
|---|---|---|
| 4-pass build, genuine BibTeX 0.99d | ✅ | 0 errors |
| Undefined references | ✅ | 0 |
| Undefined citations | ✅ | 0 |
| Missing glyphs | ✅ | 0 |
| Overfull boxes | ✅ | 0 |
| `validate_latex_v2.py` | ✅ | 13 PASS / 0 FAIL |
| `verify_examples.py` | ✅ | 56 checks / 0 mismatches |
| Abstract < 250 words | ✅ | 244 (C3) |
| Option B2 unchanged | ✅ | verified in rendered PDF |
| Appendix A.1 / A.2 | ✅ | verified |
| Author metadata unchanged | ✅ | verified |
| Funding / competing interests unchanged | ✅ | verified |
| **Visual inspection** | ⚠️ | **NOT PERFORMED** — Arena has no vision capability. The researcher must review the rendered PDF. |

## E. Mandatory items still outstanding

1. **Research-data deposit and link** (FFA Option C) — required, unresolved.
2. **Generative-AI declaration** — required where applicable, unresolved.
3. **Author confirmations** of originality, exclusive submission, no
   simultaneous submission — required, not asserted.
4. **Supplementary per-file captions** — recommended, not written.
5. **Highlights** — encouraged, drafted, awaiting confirmation.
6. **Visual review of the rendered PDF** — cannot be performed by Arena.

## F. Explicitly out of scope for this phase

Generative-AI declaration, GitHub data-access arrangements, licence selection,
Zenodo deposit, GitHub releases/tags — all **deferred at their existing status**
and untouched. No submission has been made; no Editorial Manager account has
been created; nothing has been uploaded to Elsevier.
