# Task J — Final submission checklist

**Status: 🟡 CONDITIONALLY READY — RESEARCHER DECLARATIONS PENDING**

Every item below is marked COMPLETE / PENDING / BLOCKED. Nothing is marked
complete that is not.

---

## 1. Manuscript

| # | item | status | evidence |
|---|---|---|---|
| 1.1 | Manuscript compiles cleanly | ✅ COMPLETE | 0 errors, 0 undefined citations/ref s, 0 overfull/underfull, 0 missing chars |
| 1.2 | Built with pdflatex → bibtex → pdflatex → pdflatex | ✅ COMPLETE | TeX Live 2024, pdfTeX 1.40.26, BibTeX 0.99d |
| 1.3 | 42 pages | ✅ COMPLETE | `build/main.pdf` |
| 1.4 | Abstract ≤ 250 words | ✅ COMPLETE | 240 words |
| 1.5 | Keywords 1–7 | ✅ COMPLETE | 7 |
| 1.6 | Highlights 3–5, each ≤ 85 chars | ✅ COMPLETE | 5; 75/78/75/73/75 |
| 1.7 | 13 references, all cited, `plain` style | ✅ COMPLETE | 13/13 |
| 1.8 | 10 sections + Appendices A and B | ✅ COMPLETE | appendix tables numbered A.1, A.2 |
| 1.9 | 13 worked examples, numbering correct | ✅ COMPLETE | `verify_examples.py` 56/56 |
| 1.10 | 28 certified codes present | ✅ COMPLETE | Table A.1; re-derived from the published CSV |
| 1.11 | 125 `[[…]]_q` tuples unchanged | ✅ COMPLETE | sorted list identical to Phase 19 |
| 1.12 | No vertical rules; booktabs throughout | ✅ COMPLETE | `\vline` = 0 |
| 1.13 | No unresolved placeholders | ✅ COMPLETE | `??` = 0; author metadata present |
| 1.14 | Author details complete | ✅ COMPLETE | name, institution, address, country, e-mail |
| 1.15 | Funding declaration present | ✅ COMPLETE | p. 37 |
| 1.16 | Competing-interests declaration present | ✅ COMPLETE | p. 37 |
| 1.17 | Acknowledgements present | ✅ COMPLETE | p. 37 |
| 1.18 | Option B2 abstract preserved verbatim | ✅ COMPLETE | byte-identical to Phase 19 |
| 1.19 | `validate_latex_v2.py` | ✅ COMPLETE | 13/13 PASS |
| 1.20 | `verify_examples.py` | ✅ COMPLETE | 56/56, 0 mismatches |
| 1.21 | **Comparison-section wording on EA tables corrected** | ❌ **PENDING — researcher decision** | inaccurate as worded; see `PHASE23_THIRD_PARTY_DATA_REVIEW.md` §E5 |

## 2. Research data

| # | item | status | evidence |
|---|---|---|---|
| 2.1 | 86 files published on `main` | ✅ COMPLETE | commit `3752a6c` |
| 2.2 | Publicly accessible without authentication | ✅ COMPLETE | 87/87 manifest entries downloaded, no auth header |
| 2.3 | SHA-256 manifest published and verified | ✅ COMPLETE | 87 entries, 87 OK |
| 2.4 | Commit-pinned URL | ✅ COMPLETE | resolves HTTP 200 |
| 2.5 | Reproduction instructions present | ✅ COMPLETE | `research-data/README.md` |
| 2.6 | Per-file descriptions produced | ✅ COMPLETE | `PHASE23_SUPPLEMENTARY_FILE_DESCRIPTIONS.csv`, 86 rows, all hashes match |
| 2.7 | Certification distribution re-derived | ✅ COMPLETE | 24 / 4 / 11 / 17 / 0 — all five match |
| 2.8 | **DOI obtained** | ❌ **NOT DONE — not authorised** | — |
| 2.9 | **Release or tag created** | ❌ **NOT DONE — not authorised** | — |
| 2.10 | **Licence applied** | ❌ **PENDING — researcher decision** | repo reports `license: null` |
| 2.11 | **Third-party file cleared** | ❌ **PENDING — researcher decision** | `comparison_grassl_q9.csv` |

## 3. Data availability statement

| # | item | status | evidence |
|---|---|---|---|
| 3.1 | Outdated link corrected | ✅ COMPLETE | `e41c571…/PAPER/supplementary` → `3752a6c…/research-data` |
| 3.2 | Corrected in a **new** staging copy | ✅ COMPLETE | `PAPER/FFA_FINAL_SUBMISSION_V2/` |
| 3.3 | Historical manuscripts preserved | ✅ COMPLETE | Phase 19, V1, V2, V3 all untouched |
| 3.4 | Only the DA block changed | ✅ COMPLETE | single `diff` hunk; 12 section files + bib byte-identical |
| 3.5 | All stated categories verified present | ✅ COMPLETE | 22/23/29/8/4 |
| 3.6 | Marked PROPOSED — FFA POLICY CONFIRMATION PENDING | ✅ COMPLETE | marker in the manuscript and in the report |
| 3.7 | **Editorial confirmation obtained** | ❌ **PENDING** | email drafted, **NOT SENT** |
| 3.8 | **Statement treated as final** | ❌ **No — correctly not final** | — |

## 4. Generative-AI declaration

| # | item | status | evidence |
|---|---|---|---|
| 4.1 | Discrepancy documented | ✅ COMPLETE | `PHASE23_GENERATIVE_AI_DECLARATION.md` |
| 4.2 | Eight-activity matrix produced | ✅ COMPLETE | 5 of 8 clearly outside the "language only" account |
| 4.3 | Elsevier policy quoted verbatim | ✅ COMPLETE | — |
| 4.4 | Tool identification, with limits stated | ✅ COMPLETE | only the Arena AI agent is verifiable; no model/version/provider/date invented |
| 4.5 | Two candidate declarations drafted | ✅ COMPLETE | neither inserted |
| 4.6 | **Declaration finalised** | ❌ **PENDING — RESEARCHER CONFIRMATION REQUIRED** | manuscript still carries the placeholder |
| 4.7 | **Wording inserted** | ❌ **No — deliberately** | — |

## 5. Author attestations

| # | item | status |
|---|---|---|
| 5.1 | Originality | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.2 | Exclusive submission | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.3 | No prior publication | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.4 | Authorship and approval | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.5 | Integrity and accuracy of results | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.6 | Ethics and third-party rights | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |
| 5.7 | Competing interests and funding | ❌ **`[RESEARCHER CONFIRMATION REQUIRED]`** |

**7 of 7 outstanding.**

## 6. Cover letter

| # | item | status |
|---|---|---|
| 6.1 | Updated final draft produced | ✅ COMPLETE |
| 6.2 | Commit-pinned data location stated | ✅ COMPLETE |
| 6.3 | Honest statement of comparison limits | ✅ COMPLETE |
| 6.4 | All author attestations marked pending | ✅ COMPLETE — 7/7 |
| 6.5 | **Sent** | ❌ **NOT SENT — no authorisation** |

## 7. Prohibited actions — none taken

| action | taken? |
|---|---|
| Manuscript submitted to FFA / Elsevier | ❌ **No** |
| Editorial Manager account created | ❌ **No** |
| Cover letter sent | ❌ **No** |
| Editorial clarification email sent | ❌ **No — drafted only** |
| Zenodo upload | ❌ **No** |
| DOI created | ❌ **No** |
| GitHub release created | ❌ **No** |
| GitHub tag created | ❌ **No** |
| Licence applied | ❌ **No** |
| `main` modified | ❌ **No** |
| `research-data/` modified | ❌ **No** |
| Journal changed | ❌ **No** |
| Force push | ❌ **No** |

## 8. Bottom line

| | |
|---|---|
| Checklist items total | **59** |
| COMPLETE | **42** |
| PENDING — researcher decision or authorisation | **17** |
| Of which: author attestations | **7** (§5, all seven) |
| Of which: awaiting an external answer (editorial / licensor) | **2** (§3.7, §2.11) |
| Of which: not done because not authorised (DOI, release/tag) | **2** (§2.8, §2.9) |
| Blocked or prohibited actions taken | **0** |

**Two counts are worth stating separately.** Of the 17 outstanding items,
**seven are author attestations that only the researcher can supply** — no
amount of further agent work can close them. The remaining ten are decisions or
external answers.

**The package builds, verifies and is internally consistent. It is not
submittable, because thirteen items — seven of them author attestations — are
the researcher's to supply.**
