# Phase 15 — Final manuscript corrections, certification-claim accuracy and visual review package

**Repository** `arunyadav0307-stack/Matrix-Ring` · **Branch** `arena/59de606f-matrix-ring`
**Target journal** *Finite Fields and Their Applications* (Elsevier)
**Manuscript** *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*

Scope: **final correction phase only.** No new mathematical research. No journal
submission, no Elsevier upload, no cover letter, no repository release, no licence
change. All corrections live in a new working copy; `PAPER/` canonical sources and
`PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` (114 files) are untouched.

---

## 0. Executive summary

| Task | Item | Result |
|---|---|---|
| A | CP-1 three-method claim | **Corrected.** 0 of 28 codes have all three methods; 28 of 28 have exactly two. Per-code table produced and verified. |
| B | CP-2 Example 13 (`ex:certify`, rendered 8.12) | **Corrected.** Method attribution only; generator matrix, parameters and all arithmetic untouched and independently recomputed. |
| C | CP-3 appendix table numbering | **Corrected.** Now `Table A.1` / `Table A.2`; main-text Tables 1–4 unchanged; table contents unchanged. |
| D | CP-4 DOIs not rendered | **Retained** as a documented formatting limitation. Not fixed, by design. |
| E | Claim consistency + validators | `validate_latex.py` 11 PASS / 2 pre-existing heuristic FAILs; `verify_examples.py` **56 checks, 0 mismatches**. |
| F | Compile (TeX Live 2024, genuine BibTeX) | 0 errors, 0 undefined refs/citations, 0 overfull, 0 underfull, 0 missing glyphs. **42 pages.** |
| G | Visual review package | 42 page images + 8 high-resolution key pages + contact sheet. **Arena did not view them** (no vision capability). |
| H | Documentation | 3 audit documents updated (append-only); this report. |
| I | Final package | `PAPER/FINAL_RESEARCHER_REVIEW_V2/`, 12 items, SHA-256 manifest. |

**One defect was found and fixed during Phase 15 that Phase 14 had not recorded:**
my first CP-2 correction gave the wrong *reason* for M2's absence (it said "not
applicable to the entanglement-assisted route"). The committed source shows M2 is
skipped because **M1 already completed**, not because of the route. This changed
the corrected wording in three places. See §2.3.

---

## 1. Starting conditions (verified)

* Branch `arena/59de606f-matrix-ring`; local == remote == `dce4ba7`; tree clean.
* 23 protected baseline hashes recorded to `/tmp/p15_pre.txt` (canonical
  `main.tex`, `references.bib`, `main.pdf`, `main.bbl`, 12 section files, 3 Phase
  8/8A/8B ZIPs, `supplementary/MANIFEST.sha256`, the Phase 14 package manifest and
  both Phase 14 reports).
* `PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` present with **114 files**, untouched.
* New working copy created at `PAPER/PHASE15_WORKCOPY/` (from the Phase 14 copy,
  not from canonical `PAPER/`).

---

## 2. Task A + B — the three accuracy corrections

### 2.1 CP-1: the "three independent methods" claim

The claim appeared in **six** places, not the three found in Phase 14:

| # | Location | Text |
|---|---|---|
| 1 | `main.tex` abstract | "certifies $28$ codes by three independent methods" |
| 2 | `01_introduction.tex:124` | same claim, in "What the paper does and does not claim" |
| 3 | `01_introduction.tex:201` | same claim, in the contributions hierarchy |
| 4 | `08_certification.tex:172` | "Three independent methods are used, and every headline code is certified by all three." |
| 5 | `08_certification.tex:228` | "the headline codes, all certified by the three methods" |
| 6 | `appendix_tables.tex:12,16` | column description + "all three methods that completed" |

**The decisive evidence** is the committed source of the computation itself,
`supplementary/scripts/phase7_extended_search.py`, `part6_certification`
(lines 1664–1708):

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"      # M2 NOT RUN
else:
    d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd, maxw=...)   # M2 run instead
```

**M2 is executed only when M1 fails to complete.** Therefore no code can have all
three methods: for every code, either M1 ran and M2 was skipped, or M1 failed and
M2 ran instead.

Reconstructed for all 28 codes and cross-checked row by row against
`supplementary/parameter_tables/certified_codes.csv` **and** Part 6 of
`supplementary/logs/phase7_extended_search_log.txt` (lines 449–478). The complete
table is `corrected_appendix/CP1_method_applicability_table.csv`. Summary:

| | M1 completes | M1 does not complete | **total** |
|---|---|---|---|
| codes | **24** | **4** | **28** |
| exact method | M1 | M2 | — |
| M2 column | `n/a` — not run | exact value | — |
| M3 | run (all 28) | run (all 28) | 28 |
| methods run per code | 2 | 2 | — |

* **0 of 28 codes** have all three methods. **28 of 28** have exactly **two**.
* M3 returns an **exact** distance for only 11 of 28; for the other 17 it
  terminates at weight 2 or 3 and is a proved **lower bound** only.
* Routes: SO 2, DC 1, EA 25. Note the pattern is **per code, not per route**:
  3 of the 4 M2-certified codes are SO/DC, but the fourth (`[[24,6,4;18]]_9`,
  family $(9,3,2)$) is an **EA** code whose M1 did not complete.

**Origin of the overclaim:** it is in the historical log itself — line 478, check
`[EXH] E1`: *"every headline code is certified by the three independent methods
(classical enumeration, support search, ambient quantum search)"*. That log line
is committed evidence and was **not** rewritten.

**Corrections applied (all preserves *applicable* vs *not run*):**

* Abstract → *"Exhaustive computation certifies $28$ codes, each by two applicable
  independent methods, one exact and one a cross-check, …"*
* Introduction (both places) → *"certifies $28$ codes, the exact distance of each
  by an applicable exact method cross-checked by an independent ambient quantum
  search, …"*
* Certification methodology → states that each code's exact distance comes from
  exactly one of M1/M2 (M2 running precisely when M1 cannot finish), that every
  code is additionally cross-checked by M3, that M3 is a lower bound for most
  codes, and that **no code is certified by all three**.
* Appendix A → dash = M1 could not complete (so M2 was run); `n/a` = M2 was not
  run because M1 had already finished.

Abstract word count: **235** by the strictest of the three counting conventions
(233 / 219 / 235), against the 250-word limit — compliant, margin 15.

### 2.2 CP-2: Example 13 (`ex:certify`, rendered **Example 8.12**, p. 33)

Reconstructed from committed source data
(`supplementary/generator_matrices/04_20_2_10-18_4_(4,1,5)_EA.json`):

| Item | Value | Source |
|---|---|---|
| code identifier | $[[20,2,10;18]]_4$ | `code` |
| family | $(q,t,n)=(4,1,5)$ | `q,t,n` |
| generator matrix | `generator_matrix_A`, **18 × 20** over $\mathbb F_4$; `generator_matrix_Euclidean_dual` **2 × 20** | JSON |
| construction route | EA (R3) | `route` |
| $N=4tn$ | $4\cdot1\cdot5=20$ | `N` |
| $k=\dim D$ | 18 | `k` (rows of $A$) |
| $h_E$ | 0 | `h_E` |
| $c=k-h_E$ | 18 | `c` |
| $K=N-k-h_E$ | $20-18-0=2$ | `K` |
| $d$ | 10 | `d` |
| entanglement consumption $c$ | 18 (of $N=20$) | `c` |
| quantum dimension $K$ | 2 | `K` |
| M1 / M2 / M3 | 10 / `n/a` / $>2$ | CSV row, log line 454 |
| `distance_method` | `complete enumeration` | JSON |

**Independent recomputation (all 12 displayed numbers re-derived from the
generator matrices, not copied):**

* $N=4\cdot1\cdot5=20$ ✓ · $c=18-0=18$ ✓ · $K=20-18-0=2$ ✓
* $h_E=0$ so $\mathrm{Hull}_E(D)=\{0\}$ and $\mathcal Q=D^{\perp_E}$, a
  $[20,2]_4$ code. Complete enumeration of all $4^2=16$ codewords gives weight
  distribution $\{0{:}1,\ 10{:}6,\ 20{:}9\}$ → **minimum weight $=10$** ✓ (matches $d=10$).
* EA Singleton: $N-K+c=36\ge2(d-1)=18$, defect $(36-18)=\mathbf{18}$ ✓
* EA Hamming: $4^{-16}\sum_{i=0}^{4}\binom{20}{i}(4^2-1)^i\approx0.058\le4^{20}$ ✓
* coset Singleton: $K+d=12\le N+1=21$ ✓
* bookkeeping: $k=18$ even ✓; $K-c=-16=N-2k$ ✓ and $-16\equiv0\pmod 4$ ✓;
  $c+K=20=N-2h_E$ ✓; the erroneous $c+K=N-k$ would give $20=2$ ✗ (as stated)
* EA Singleton alone gives only $K\le N+c-2d+2=20$ ✓

**Correction (before → after):**

| | Text |
|---|---|
| **Before** | "…the minimum weight found is $10$; the independent support search (M2) and the ambient quantum search (M3, which certifies $d\ge3$ as a lower bound) agree with the reported value." |
| **After** | "…the minimum weight found is $10$. The support search (M2) is run only when M1 cannot finish, so it was not run here and contributes nothing; the ambient quantum search (M3) independently certifies $d\ge3$ as a lower bound, consistent with this value." |

Only the attribution changed. The generator matrix was **not** altered; no code
with identical parameters was substituted; no number was changed.

### 2.3 A defect found *during* Phase 15, in my own first correction

My first CP-2 fix read *"The support search (M2) is not applicable to the
entanglement-assisted route"*. Reading `part6_certification` showed this is
**wrong**: M2 is skipped when M1 completes, regardless of route. The same wrong
reason had been written into `appendix_tables.tex`. Both were corrected before the
final build, and the CP-1 applicability table was regenerated with the correct
semantics ("not run (M1 already complete)" rather than "not applicable").

### 2.4 CP-3: appendix table numbering

The FFA guide for authors states the convention verbatim: *"Identify individual
appendices … A, B, etc."* and *"give separate numbering to tables and figures
using formats such as **Table A.1**; Fig. A.1"*.

* The two appendix tables rendered as `Table 5` and `Table 6`. Now **Table A.1**
  (`tab:cert`) and **Table A.2** (`tab:grassl`).
* Implemented at `\appendix` by resetting the table counter and redefining
  `\thetable`. Main-text **Tables 1–4 unchanged**; no duplicate numbers.
* **Appendices contain 0 figures and 0 numbered display equations**, so
  `\thefigure` and `\theequation` needed no corresponding change. (The appendix
  *subsections* already rendered as A.1, A.2, A.3 via `\Alph{section}`.)
* All references are made with `\ref{}`, so every cross-reference updated
  automatically — verified in the PDF on pages 32, 38, 40 and 41.
* **Table contents and numerical data unchanged.**

### 2.5 CP-4: DOIs — retained, not fixed

9 of 13 bibliography entries carry `doi=`; `plain.bst` has no `doi` field, so the
PDF renders **0** DOIs. Retained deliberately: the FFA guide for authors states
reference formatting is applied at proof stage, so changing the style or
hand-inserting DOI text would be discarded. Recorded in
`OPEN_ISSUES_AND_LIMITATIONS.md` §5.1.

---

## 3. Task E — validation

```
tools/validate_latex.py --root PHASE15_WORKCOPY
  V1  \input resolves                 PASS   (13 files)
  V2  braces balanced                 PASS
  V3a \begin/\end matched             PASS
  V3b environments known              PASS
  V4  every \ref has a \label         PASS   (264 refs, 116 labels)
  V5  no duplicate \label             PASS   (116 unique)
  V6  every \cite has a bib entry     PASS   (32 citations, 13 entries)
  V7  no uncited bib entry            PASS
  V8  nothing on the DO-NOT-CITE list PASS
  V9  control sequences defined       FAIL   (heuristic, see below)
  V10 verbatim blocks clean           PASS
  V11 no invented author metadata     FAIL   (heuristic, see below)
  V12 math delimiters balanced        PASS
  checks: 13 ; PASS 11 ; FAIL 2
```

**The two FAILs are pre-existing Phase 14 false positives, present identically
before any Phase 15 edit** (Phase 14 baseline: 11 PASS / 2 FAIL, same two checks).
Neither is a real defect:

* **V9** flags `\penalty` (pre-existing), `\textsuperscript` (pre-existing) and
  `\setcounter` (added by CP-3). All three are genuine LaTeX/TeX commands; the
  heuristic's whitelist is simply incomplete.
* **V11** flags the intended `\author{\AUTHORONE\textsuperscript{a}` construction
  from the Phase 14 author-metadata fix.

Both are confirmed harmless by a clean 4-pass build with 0 errors.

```
tools/verify_examples.py   →   CHECKS: 56     mismatches: 0
```

Run against the **corrected** sources, full run (not `--fast`), in a sandbox
whose `sections/` is the Phase 15 copy and whose `supplementary/` is the
committed canonical package.

**Scope of the corrections:** no theorem, proof, lemma, proposition, definition,
generator matrix or numerical parameter was changed. Exact distances remain
distinguished from lower bounds; EAQECC vs stabilizer routes remain described
as before; all numbers still match the committed logs.

---

## 4. Task F — build

```
TL=/home/user/texlive2024 sh compile/build_modern.sh
pdflatex → bibtex → pdflatex → pdflatex
```

| Check | Result |
|---|---|
| TeX Live | 2024 (`/home/user/texlive2024`) |
| BibTeX | genuine `BibTeX 0.99d`, style `plain.bst`, 78-line `.bbl` |
| errors (`^! `) | **0** |
| undefined citations | **0** |
| undefined references | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| missing characters (glyphs) | **0** |
| hyperref warnings | **0** |
| font warnings | **0** |
| duplicate labels | **0** (116 labels, 116 unique) |
| pages | **42** |
| page size | A4, 595.3 × 841.9 pt |
| bytes | 579 531 |
| **SHA-256** | `b619cf6cb0678ab15de54c5b61536840bdaf2951aa70292ffd741a2cd01859b7` |

`SOURCE_DATE_EPOCH=1794268800` pinned, so the build is byte-reproducible.

**A successful compile is not a visual review.** Layout was checked
programmatically (no text block exceeds the margins; Computer Modern fonts only;
no empty or near-empty pages), but Arena has **no vision capability** and did not
look at the rendered pages.

---

## 5. Task G — visual review package (and its limitation)

Contents of `PAPER/FINAL_RESEARCHER_REVIEW_V2/visual_review/`:

* `pages/page-01.png … page-42.png` — all 42 pages at 150 dpi.
* `key_pages/` — 8 pages at **300 dpi** for close inspection:
  title/abstract (p1), introduction first page (p3), certification methodology
  (p31), **Example 13 / `ex:certify` (p33)**, Appendix A tables (p38, p39),
  Appendix B (p40), references (p41).
* `contact_sheet.png` — all 42 pages on one 7 × 6 grid, each tile labelled with
  its page number, for rapid navigation.

**Honest limitation.** Arena **cannot see images**: reading a rendered PNG returns
"you do not have vision capabilities". These images were produced **for the
researcher to inspect**. They have *not* been visually reviewed by Arena, and no
statement in this report rests on visual inspection. What *was* verified
programmatically: page count, page geometry, absence of margin overflow, font
set, absence of empty pages, and the text content of every page (via text
extraction), including the corrected sentences and the `Table A.1` / `Table A.2`
strings.

---

## 6. Task H — documentation

* `PHASE15_FINAL_CORRECTIONS/PHASE15_FINAL_CORRECTIONS_REPORT.md` — this file.
* `PHASE15_FINAL_CORRECTIONS/CP1_method_applicability_table.csv` — the 28-row
  per-code M1/M2/M3 applicability table (also copied into the package).
* `audit/MANUSCRIPT_SELF_AUDIT.md` — Phase 15 addendum appended (append-only).
* `audit/OPEN_ISSUES_AND_LIMITATIONS.md` — §5 appendendum: CP-4 retained, method
  counts restated precisely.
* `audit/CLAIM_TRACEABILITY_MATRIX.md` — claim **T-225** corrected in place, plus
  an appendix explaining the change.
* `README.md` in the package — reproduction instructions.
* Correction history is **append-only** throughout: nothing was deleted or
  overwritten; every correction is added as a new dated section.

---

## 7. Deferred — not touched in Phase 15

Unchanged and awaiting the researcher's separate decision:

* **Generative-AI declaration** — the researcher states language-enhancement-only;
  the records show broader use. Still unreconciled; still PENDING.
* **Data availability** — existing public GitHub repository only; no Zenodo
  deposit was created. The supplementary data remain absent from `main`.
* **Licence** — recommendation only (MIT for 22 scripts, CC BY 4.0 for 64 data/doc
  files); **nothing applied**.
* Four unexecuted GitHub fixes still awaiting authorisation: merge branch into
  `main`; release/tag at `e41c571`; branch-protect `main`; add a licence.

---

## 8. Safeguards honoured

* Canonical `PAPER/` sources, historical logs and Phase 0–14 documents untouched.
* `PAPER/FINAL_RESEARCHER_REVIEW_PACKAGE/` (114 files) preserved unchanged.
* No generator matrix altered; no mathematical parameter modified; Example 13 not
  replaced; no lower bound reclassified as an exact distance; no author,
  affiliation, email, funding or competing-interest statement modified.
* All 23 protected baseline hashes re-verified at the end of the phase.

---

## 9. Recommendation

**The three accuracy defects are corrected and the corrected build is clean.**
The manuscript's certification claim is now supported by its own committed data.

Arena recommends the researcher now read the corrected PDF, paying particular
attention to:

1. **p31** — the certification-methodology paragraph (CP-1);
2. **p33** — Example 8.12 (CP-2);
3. **p38–39** — Appendix A, confirming the tables read `Table A.1` / `Table A.2`
   (CP-3);
4. **p1** — the abstract, whose certification clause now reads "each by two
   applicable independent methods, one exact and one a cross-check".

CP-4 (unrendered DOIs) is a deliberate, documented limitation, not an oversight.

**Stopping here.** No submission, no Elsevier upload, no cover letter, no
repository release, no licence change, no new research phase.
