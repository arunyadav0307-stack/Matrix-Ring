# FINAL RESEARCHER REVIEW PACKAGE

*Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*

**This is a researcher-review archive. It is NOT an authorization for journal
submission, and no submission has been made.**

Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring` · Base commit: `19a76e1`

---

## What this is

A complete, internally consistent snapshot of the manuscript and every artefact
needed to check it, assembled after a full integrity audit. Purpose: to let the
researcher read and verify the finished work.

## Contents

| directory | what |
|---|---|
| `source/` | final reviewed LaTeX: `main.tex`, `references.bib`, `main.bbl`, `sections/` (12 files) |
| `build/` | compiled `manuscript.pdf` (42 pp), plus `main.log`, `main.bbl`, `main.blg` |
| `supplementary/` | 86 files: 22 scripts, 23 logs, 29 generator matrices, 8 parameter tables, 4 docs |
| `audit/` | 7 documents: claim traceability, mathematical self-audit, final validation, open issues, novelty comparison, parameter comparison, contribution map |
| `SHA256_MANIFEST.txt` | one hash per file |
| `README.md` | this file |

## Exact reproduction instructions

### 1. Rebuild the manuscript

```bash
cd source/..
sh compile/bootstrap_texlive.sh          # only if /home/user/texlive2024 is absent
cd <staging copy>
TL=/home/user/texlive2024 sh compile/build_modern.sh
```

Four-pass cycle (`pdflatex → bibtex → pdflatex → pdflatex`) with genuine
BibTeX 0.99d, `SOURCE_DATE_EPOCH=1794268800` pinned for byte-reproducibility.

Expected result: **42 pages, 0 errors, 0 warnings**,
`sha256(manuscript.pdf) = a021cf4b456377725f5db099368fe2ce6aa3a999339f3f93a9ea09b52c9db64c`

### 2. Verify the supplementary package integrity

```bash
cd supplementary
sha256sum -c MANIFEST.sha256
```

Expected: **85 lines verified, 0 failures**.

### 3. Re-verify the worked examples and parameter tables

```bash
cd ../..
python3 tools/verify_examples.py
```

Expected: **56 checks, 0 mismatches**. Covers `ex:crt`, `ex:witnessA`,
`ex:witnessB`, `ex:nonreflexive`, the 18 headline table rows and all 28
certified codes against `certified_codes.csv`.

### 4. Re-run the certification from scratch

```bash
cd supplementary/scripts
MATRIX_RING_COMP=<repo>/04_COMPUTATION python3 extract_certified_generators.py /tmp/gens
```

Must reproduce `generator_matrices/` and agree line-for-line with Part 6 of
`logs/phase7_extended_search_log.txt`.

### 5. Independently check one generator matrix

See `supplementary/CERTIFICATION_PROCEDURE.md`, §5.

---

## Unresolved items the researcher must decide

These are recorded, not resolved. See `PHASE14_FINAL_RESEARCHER_REVIEW_REPORT.md`.

| # | item | status |
|---|---|---|
| 1 | **"Three independent methods" claim** in the abstract and introduction — the data show **two** methods per code | **RESEARCHER REVIEW REQUIRED** |
| 2 | `ex:certify` attributes agreement to method M2, but M2 = `n/a` for that code | **RESEARCHER REVIEW REQUIRED** |
| 3 | Appendix tables numbered 5–6, not A.1–A.2 as FFA's guide specifies | **OPEN** |
| 4 | 9 DOIs present in `references.bib` but not rendered (`plain.bst` drops them) | **OPEN** (minor — FFA restyles at proof stage) |
| 5 | Generative-AI declaration: researcher's account contradicts the project record | **BLOCKING** (carried from Phase 13) |
| 6 | Data availability: GitHub-only route; data absent from the `main` branch | **BLOCKING** (carried from Phase 13) |

## Not included / not done

No submission, no Editorial Manager upload, no journal account, no cover
letter, no Zenodo deposit, no DOI, no release, no tag, no merge, no licence.
