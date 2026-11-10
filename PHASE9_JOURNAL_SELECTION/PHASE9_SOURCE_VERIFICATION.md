# Phase 9 — Source verification

**Date of this document:** 2026-11-10
**Baseline audited:** `PAPER/MatrixRingManuscript_20261110_Phase8B.zip`
**Phase 9 scope:** journal research and evaluation only. No manuscript file was
modified, and nothing was recompiled.

---

## 1. Baseline verification (performed before any Phase 9 analysis)

| artefact | bytes | SHA-256 | sidecar check |
|---|---|---|---|
| `MatrixRingManuscript_20261110_Phase8B.zip` | 700 055 | `6d39f643f027f6fb8a7129ebf7623456f26386fdca8dac84e4c02dc69b86fec0` | **OK** |
| `MatrixRingManuscript_20261109_Phase8A.zip` | 1 096 851 | `14ecac0e8649009ef535f63bc128734335c88ac3c1bbc6ef4e05a5a868342910` | **OK** |
| `MatrixRingManuscript_20261109.zip` (Phase 8) | 543 086 | `d1ba4c821b1af01b8105eff702315957e692cfcaed21d5491a8ea03e4b29a80d` | **OK** |

All three sidecars live outside their archives, so each hash is a check on the
archive exactly as shipped.

## 2. Read-only guarantees

| guarantee | how enforced | status |
|---|---|---|
| Phase 8B ZIP not edited | opened read-only; extracted with `unzip` into a separate directory | **held** |
| No manuscript source modified | only `sed -n`, `grep` reads on `_inspection/` | **held** |
| `main.tex` untouched | read only; l.165 still `\bibliographystyle{plain}` | **held** |
| `references.bib` untouched | read only; 13 entries, byte-identical to Phase 8A | **held** |
| No mathematics, example, proof or figure changed | no `.tex` write anywhere | **held** |
| No recompilation | `pdflatex` / `bibtex` never invoked in Phase 9 | **held** |
| Phase 0–7 files untouched | outside the Phase 9 working directory | **held** |

Because nothing was recompiled, the Phase 8B PDF hash is unchanged:

```
69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd  main.pdf
```

## 3. Read-only inspection copy

```
PHASE9_JOURNAL_SELECTION/_inspection/     ← unzip of the 8B package
```

Manifest re-verified on extraction: **43/43 entries, 0 bad**. Nothing in this
directory was edited. Files read for the profile:

* `sources/main.tex` — title, author placeholder, abstract, keywords, MSC, bibliography style
* `sources/sections/*.tex` — structure, results, novelty statements
* `sources/references.bib` — the 13 cited works and their venues
* `MANUSCRIPT_SELF_AUDIT.md`, `FINAL_VALIDATION_REPORT.md` — the manuscript's
  own record of its open issues

## 4. Facts carried into the profile (all read from the verified package)

| fact | value |
|---|---|
| title | *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings* |
| author metadata | `\AUTHORPLACEHOLDER` — intentionally unset |
| bibliography entries | 13, all cited |
| bibliography style | `plain` (retained per decision D-1, 2026-11-10) |
| MSC 2020 | 94B05, 94B15, 94B60, 16S50, 11T71 |
| theorem-like environments | 43 |
| numbered examples | 13 |
| labels | 107 |
| LaTeX class | plain `article`, 11pt, a4paper — **no journal template applied** |

The 13 cited works and their venues (from `references.bib`):

| key | venue | relevance to journal choice |
|---|---|---|
| Alahmadi2013CyclicM2F2 | *J. Franklin Inst.* | cyclic codes over M₂(F₂) |
| LuoParampalli2018M2F2uF2 | *Cryptogr. Commun.* | M₂(F₂+uF₂) — **candidate journal itself** |
| Dinh2024CyclicRingsOfMatrices | *J. Algebra Appl.* | cyclic codes over matrix rings — **candidate journal itself** |
| JoshiPatelPrakash2026M4 | (2026 preprint/article) | M₄ generalisation |
| SiNiu2023SkewM2F2 | *J. Appl. Math. Comput.* | skew cyclic codes over M₂ |
| Wood1999Duality | *J. Pure Appl. Algebra* | duality over finite rings |
| GreferathSchmidt1999GrayIsometry | *IEEE Trans. Inform. Theory* | Gray isometry — **candidate journal itself** |
| FanZhang2017GaloisSelfDual | *Finite Fields Appl.* | Galois self-dual constacyclic codes — **candidate journal** |
| LiuPan2020GaloisHulls | *Finite Fields Appl.* | Galois hulls of constacyclic codes — **candidate journal** |
| Cao2021MDSGaloisHulls | *Discrete Math.* | MDS Galois hulls — **candidate journal** |
| ZhangKongZheng2026QuantumGaloisHulls | (2026) | direct comparator, quantum Galois hulls |
| KetkarEtAl2006NonbinaryStabilizer | *IEEE Trans. Inform. Theory* | nonbinary stabilizer formalism |
| GrasslCodetables | online tables (misc) | code-table benchmarking |

**Reading:** four of the ten candidate journals under consideration
(*Finite Fields Appl.*, *Discrete Math.*, *Cryptogr. Commun.*, *J. Algebra
Appl.*, plus *IEEE Trans. Inform. Theory*) are already cited in the
manuscript's own bibliography. That is a genuine signal of topical proximity,
not a claim about editorial outcomes.

## 5. Evidence discipline for the journal research

Three rules were applied to every time-sensitive claim:

1. **Official sources only.** Publisher pages (ScienceDirect/Elsevier,
   link.springer.com, AIMS, World Scientific, IEEE Xplore, IEEE IT Society,
   MDPI) and the SCImago/Scopus portal. Aggregator sites (`resurchify`,
   `journalimpact`, `journalsearches`, `scispace`, `wos-journal.info`) were
   **excluded**: several returned mutually contradictory SJR and quartile
   values for the *same* journal in the *same* year (e.g. DCC reported as
   SJR 0.712, 0.743 and 1.033).
2. **Nothing invented.** Where a figure could not be confirmed on an official
   page it is recorded as **UNVERIFIED**, with the closest secondary
   observation noted separately and explicitly labelled as such.
3. **Quartiles reported, not chased.** Quartiles are recorded because the task
   asks for them, with source and year. No journal is ranked here on quartile
   alone (see `PHASE9_JOURNAL_COMPARISON.md`, §3).

All journal pages were accessed on **2026-11-10** unless a document states
otherwise.

## 6. Known gaps — stated rather than guessed

* **AMC (AIMS) open-access APC** — not confirmed from an official AIMS page.
  The AIMS journal home page (`aimsciences.org/AMC`) confirms the journal
  "supports Open Access" but displayed no figure; `aimsciences.org/journals/home.jsp?journalID=10`
  returned HTTP 500. A secondary Chinese-language blog quotes an AIMS
  statement of "USD 1,800" for AIMS hybrid Open Choice. Recorded as
  **UNVERIFIED**; the subscription route carries no author charge.
* **IEEE TIT open-access APC** — two official IEEE pages disagree: IEEE Xplore
  lists **USD 2,800**, the IT Society author-information page states a
  **"discounted USD 1,750"**. Both recorded; the discrepancy is unresolved.
* **Peer-review model** — confirmed single-blind for DCC and AAECC; confirmed
  single-anonymous for IEEE TIT. Not confirmed on the pages retrieved for FFA,
  AMC, QIP, JAA, Discrete Mathematics, Entropy, Cryptogr. Commun.; marked
  UNVERIFIED rather than assumed.
* **Page limits** — only IEEE TIT states one explicitly. Their absence
  elsewhere means "not stated on the guidelines page retrieved", which is
  *not* the same as "no limit exists".
* **World Scientific JAA open-access APC** — the submission-guidelines page
  states "no page charge" and links an OA page; the OA fee amount was not
  recovered. Marked UNVERIFIED.
* **SCIE (Web of Science) indexing** — not individually confirmed on Clarivate
  for any journal (paywalled). Scopus coverage is confirmed for all ten via
  SCImago; SCIE is quoted only where a publisher page asserts it (DCC).
