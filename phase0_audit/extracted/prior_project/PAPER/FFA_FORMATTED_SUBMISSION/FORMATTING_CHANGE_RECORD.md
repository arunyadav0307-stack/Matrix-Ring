# Task B — Formatting change record (before / after)

Base: `PAPER/FINAL_RESEARCHER_REVIEW_V3/source/` (Phase 18, Option B2 applied).
Target: `PAPER/FFA_FORMATTED_SUBMISSION/`.

**Exactly one change was made to the manuscript source.** Everything else is
byte-identical to V3 (verified by `diff -rq`: one differing file).

## The single change

| | |
|---|---|
| file | `sections/07_quantum.tex`, equation `eq:weyl` |
| requirement | FFA "Math formulae": *"Denote powers of $e$ by exp."* |
| before | `\chi(x)=e^{2\pi i x/p}` |
| after | `\chi(x)=\exp(2\pi i x/p)` |
| mathematical content | **unchanged** — $\chi(x)=\exp(2\pi i x/p)$ and $e^{2\pi i x/p}$ denote the same additive character |
| rationale | Euler's number raised to a power; FFA requests `exp` notation |

Verified: no other occurrence of `e^{...}` as Euler's number exists in the
manuscript (the remaining `e^{` matches are `\widehat{}`, a different macro).

## Everything else: verified compliant, no change made

| item | checked | change needed |
|---|---|---|
| Approved title | present, unchanged | no |
| Approved Option B2 abstract | present verbatim; 231/217/244 | no |
| Single-author information | Arun Kumar Yadav | no |
| Affiliation | School of Basic and Applied Sciences, K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India | no |
| Corresponding-author email | arunyadav0307@gmail.com | no |
| Funding declaration | "did not receive any specific grant…" | no |
| Competing-interest declaration | present | no |
| Keywords | 7, no "and"/"of" | no |
| Section / subsection formatting | numbered sections | no |
| Theorem / lemma / definition / proof environments | 83 theorem-like environments | no |
| Equation numbering | 12, consecutive | no |
| Appendix numbering | A, B; Table A.1, Table A.2 | no |
| Table numbering | 1–4 main, A.1–A.2 appendix; all cited; no vertical rules; no shading | no |
| Figures | none | n/a |
| References / appendices | 13 entries, all cited | no |
| Bibliography style | `plain` — explicitly acceptable at submission | no |
| All mathematical definitions and theorems | unchanged | no |
| All proof arguments | unchanged | no |
| All 13 worked examples | 13 present, unchanged | no |
| All quantum parameters | 34 tuples identical to canonical | no |
| Distance certifications | unchanged | no |
| Novelty claims | not inflated (0 overclaim phrases found) | no |
| Record-parameter claims | none present | no |

## Not done, and why

* **Elsevier CAS template migration** — encouraged only; declined (see
  `FFA_GUIDELINE_VERIFICATION.md`).
* **`plain` → DOI-capable bibliography style** — not required at submission;
  FFA applies its own style at proof stage.
* **CRediT statement** — not invented; single author.
* **Highlights** — provided as a **separate** file (`HIGHLIGHTS.md`), not inside
  the manuscript, as the guide requires a separate editable file.
