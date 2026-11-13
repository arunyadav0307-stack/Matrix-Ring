# Phase 16 / Final report for the researcher

**Branch** `arena/59de606f-matrix-ring`. Scope: certification documentation,
validation tooling and package reproducibility only. No submission, no upload,
no release, no tag, no licence, no new research phase.

---

## 1. Headline results

| item | result |
|---|---|
| Codes independently reconstructed | **28 of 28** |
| M1 completed / did not complete | **24 / 4** |
| M2 run / conditionally skipped | **4 / 24** |
| M3 exact / lower bound | **11 / 17** |
| Methods executed per code | **exactly 2** (M1+M3 for 24, M2+M3 for 4) |
| Codes with all three methods | **0** |
| Four-way cross-check discrepancies | **0** |
| `CERTIFICATION_PROCEDURE.md` corrected | **yes** |
| Historical package unchanged | **yes** (85/85 manifest OK) |
| Corrected package | **86 files, 86-entry manifest, all verified** |
| Validator false positives | **resolved** — 13/13 PASS, original preserved |
| LaTeX build | **clean** — 42 pp, 0 errors, 0 undefined refs |
| Example verification | **56 checks, 0 mismatches** |

## 2. What was wrong, in one sentence

The supplementary documentation said every code was certified by three methods,
but the committed source runs M2 **only when M1 fails**, so every code has
exactly two — and a second sentence in the same section implied M1 and M2 ran
together and agreed, which never happens.

## 3. The one thing worth your attention

**M3's cross-check is not uniform, and the manuscript now says so.** M3 scans
increasing symplectic weight and returns the first hit, so when it returns a
value that value is *exact* — this happens for **11** codes. For the other
**17** it finds nothing below the search weight and gives only a proved lower
bound. Appendix A previously asserted the blanket claim "M3 is … rather than an
exact method", which those 11 records contradict; it now states the split
explicitly.

The abstract still reads "each by two applicable independent methods, one exact
and one a cross-check". That is accurate at the level of roles, and at 235 words
against the 250 limit I did **not** expand it — the precise 11/17 split lives in
§8.5 and Appendix A. If you would prefer the abstract to carry the split, say so
and it can be done within the remaining word budget.

## 4. Decisions taken, for your confirmation

1. **The historical Phase 7 log was not rewritten.** Line 478 (`[EXH] E1`) still
   contains the overclaim. It is the evidence of where the defect came from; the
   corrected documentation flags it as wrong rather than erasing it.
2. **`PAPER/supplementary/` was not modified.** A parallel corrected package
   `PAPER/SUPPLEMENTARY_V2/` is now authoritative; the original remains as
   historical evidence, manifest intact.
3. **The original validator was not modified.** A corrected
   `validate_latex_v2.py` sits beside it with a 12-case self-test; the original
   still reports its historic 11/2 so no earlier report is invalidated.
4. **V11 was strengthened, not relaxed.** It no longer merely requires the
   absence of a placeholder — it now checks conformance to your confirmed author
   metadata and would catch a wrong name, affiliation or e-mail.
5. **The abstract was left unchanged** (see §3).

## 5. What was not touched

No theorem, proof, generator matrix, mathematical result, distance value or
quantum parameter. No author metadata, funding statement or competing-interest
declaration. No computational log. No Phase 0–15 file.

## 6. Remaining open items (carried forward, not reopened)

* Generative-AI declaration — researcher says language-only vs records showing
  broader use. Status **unchanged (pending)**.
* Data availability — GitHub-only; supplementary data absent from `main`.
  Status **unchanged**.
* Licence — recommendation only, nothing applied. Status **unchanged**.
* Four GitHub fixes (merge into `main`, release/tag, branch protection, licence)
  — still **awaiting authorisation**.
* CP-4 (DOIs not rendered by `plain.bst`) — **retained deliberately**; FFA
  applies reference formatting at proof stage.

## 7. Recommendation

The manuscript and its supplementary package are now mutually consistent: every
claimed verification method is supported by the execution record, and the record
is independently traceable from four sources.

Suggested reading: `PAPER/SUPPLEMENTARY_V2/CERTIFICATION_PROCEDURE.md` §3, then
`PAPER/PHASE16_WORKCOPY/build_modern/main.pdf` p31 (§8.5), p33 (Example 13) and
pp38–39 (Appendix A).

**Stopping here.** Awaiting your approval before any external action.
