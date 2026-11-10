# PHASE 23 — RESEARCHER DECISION SHEET

> # 🟡 OVERALL STATUS: **CONDITIONALLY READY — RESEARCHER DECLARATIONS PENDING**

**Branch:** `arena/59de606f-matrix-ring` · **Base commit:** `8b7f2e6`
**Date:** 2026-11-10
**Nothing has been submitted. Nothing has been sent. No licence, DOI, release or
tag has been created. `main` and `research-data/` are untouched.**

---

## Why this status and not "READY FOR RESEARCHER FINAL APPROVAL"

Sixteen decisions are yours to make. Seven of them — the originality,
exclusive-submission, authorship, accuracy, ethics and competing-interest
attestations — are author attestations that no agent can make on your behalf.
Until they are given, the package cannot honestly be called ready.

Everything that *can* be verified has been verified: the package compiles
cleanly, all 13 references resolve, all 13 worked examples check, all 28
certified codes are present, the data are public and hash-verified, and nothing
mathematical changed.

---

# PART A — The sixteen decisions

## A. Blocking — must be answered before submission

| # | decision | what you must choose | where documented |
|---|---|---|---|
| **1** | **Generative-AI declaration** | **(a)** "language enhancement only" → under Elsevier's policy, **no statement is needed**; **(b)** the broader record (drafting, proof exposition, script generation, abstract revision, literature discovery, language) → a declaration **naming every tool you actually used** is required. Only the Arena AI agent is verifiable from the project record; if you used ChatGPT or anything else, **you** must name it. | `PHASE23_GENERATIVE_AI_DECLARATION.md` |
| **2** | **Originality** | Confirm the work is your own and properly attributed. | `PHASE23_AUTHOR_ORIGINALITY_CONFIRMATION.md` §1 |
| **3** | **Exclusive submission** | Confirm it is not under consideration elsewhere. | §2 |
| **4** | **No prior publication** | Confirm no prior publication — and tell me if any preprint, thesis chapter or arXiv posting exists. | §3 |
| **5** | **Authorship** | Confirm you are sole author, or name the co-authors **now** rather than later. | §4 |
| **6** | **Accuracy of results** | Confirm the results are accurately reported. Note the two things you must **not** assert: not all three methods ran on every code, and 17 of 28 distances have only an M3 lower bound. | §5 |
| **7** | **Ethics and third-party rights** | Confirm — but see decision 12 first. | §6 |
| **8** | **Competing interests and funding** | Confirm no competing interests and no specific grant. | §7 |
| **9** | **Data-availability wording** | Approve the proposed statement, or amend it. It is marked **PROPOSED — FFA POLICY CONFIRMATION PENDING.** | `PHASE23_DATA_AVAILABILITY_STATEMENT.md` |
| **10** | **Send the editorial clarification email?** | Authorise me to send it, amend it, or drop it. It asks whether a commit-pinned GitHub repository satisfies Option C, and whether a release/tag/DOI or a licence is required. **It has not been sent.** | `PHASE23_FFA_OPTION_C_COMPLIANCE.md`, Appendix E |

## B. Required for correctness — one is an error in the paper

| # | decision | what you must choose | where documented |
|---|---|---|---|
| **11** | **Correct the entanglement-assisted claim** | §9 currently says "There is no entanglement-assisted table: the corresponding endpoint returns HTTP 404." **That is false** — EA bounds are tabulated at eaqecc.codetables.de (q = 2, q = 3; last changed 2025-07-10). Your EA codes are q = 4, 8, 9, so **none is benchmarked and your conclusion stands** — but the stated reason is wrong. Replacement wording is drafted and **not applied**. | `PHASE23_THIRD_PARTY_DATA_REVIEW.md` §E5 |
| **12** | **The third-party file** | Keep `comparison_grassl_q9.csv` with provenance; email `codes@codetables.de` for confirmation; or **remove it from the deposit** and restate the three bound pairs in the text with a citation. All three values were **re-verified live and are correct**. codetables.de asserts copyright and grants no reuse licence. | `PHASE23_THIRD_PARTY_DATA_REVIEW.md` §E4 |

## C. Licence — five sub-decisions

| # | decision | options | recommendation |
|---|---|---|---|
| **13a** | Apply a licence at all? | Yes / No | Current state is **No licence** — viewable, not reusable |
| **13b** | Licence for the 22 scripts | MIT / BSD-3-Clause / Apache-2.0 | **MIT** — shortest, most recognised; Apache-2.0 if you want an explicit patent grant |
| **13c** | Licence for data, logs and documentation | CC BY 4.0 / CC0 1.0 | **CC BY 4.0** — keeps the citation link; CC0 is irrevocable and waives your right to be credited |
| **13d** | Licence headers in the scripts? | Yes / No | Optional |
| **13e** | How the change reaches `main` | Direct commit / via the session branch | Your call — `research-data/` currently lives on `main` |

**No licence has been applied.** See `PHASE23_LICENCE_RECOMMENDATION.md`.

## D. Approval

| # | decision |
|---|---|
| **14** | Approve, amend or reject the **cover letter** draft. Not sent. |
| **15** | Confirm the **highlights** (5 drafted, marked PENDING AUTHOR CONFIRMATION in Phase 19). |
| **16** | Authorise a **DOI-bearing deposit** (Zenodo or similar) if the editorial answer, or your own judgement, requires one. **Not created.** |

---

# PART B — What was verified this phase

| claim | verified how | result |
|---|---|---|
| Repository is public | GitHub API, unauthenticated | ✅ `private: False` |
| Published commit | API | ✅ `3752a6c0e921ab21a6f78877f154e7e959f4c418` on `main` |
| All 86 files present and unaltered | git blob SHA-1 across the whole tree | ✅ 86/86, 0 missing, 0 mismatched |
| Unauthenticated download of every file | 87/87 manifest entries, no `Authorization` header | ✅ SHA-256 match 87/87 |
| Certification distribution | re-derived from the **published** CSV, cross-checked against the canonical copy | ✅ 24 / 4 / 11 / 17 / 0 — **all five match** |
| Manuscript compiles cleanly | 4-pass pdflatex/bibtex | ✅ 0 errors, 0 undefined citations or refs, 0 overfull/underfull, 0 missing chars |
| References | BibTeX 0.99d, `plain` | ✅ 13/13 |
| Worked examples | `verify_examples.py` | ✅ 56/56 |
| LaTeX structure | `validate_latex_v2.py` | ✅ 13/13 PASS |
| Only the DA block changed | `diff` + PDF text comparison | ✅ single hunk; 12 section files + bib byte-identical; 125 tuples unchanged |
| Protected files | 137 hashes before and after | ✅ **137 OK, 0 FAILED** |
| Per-file descriptions | 86 rows, hashes compared to the published manifest | ✅ 86/86 |
| The three q = 9 bound values | re-fetched live from codetables.de | ✅ **3/3 correct** |

---

# PART C — What is true and what is not

Stated plainly, so that nothing here is mistaken for reassurance.

**True:**

* The data are public, complete, hash-verified and reachable without
  authentication at a commit-pinned URL.
* The manuscript builds cleanly and every number in it checks.
* No mathematical content changed. No theorem, proof, generator matrix, quantum
  parameter, distance certificate or conclusion was touched.
* Nothing was submitted, sent, uploaded, released, tagged, licensed or given a
  DOI.

**Not true, and not claimed:**

* ❌ That the deposit **satisfies FFA Option C**. It may; the policy does not
  say whether GitHub counts as a "relevant data repository". That question is
  with the editorial office.
* ❌ That the data are **licensed**. They are not. Public means viewable, not
  reusable.
* ❌ That the data are **durably preserved**. Both branches are unprotected.
* ❌ That the data are **independently citable**. There is no DOI.
* ❌ That the **generative-AI declaration** is settled. It is a placeholder and
  the underlying disagreement is unresolved.
* ❌ That **all three certification methods** ran on every code. M2 is
  conditionally skipped; it ran on 4 of 28.
* ❌ That **every distance is exact**. 17 of 28 have only an M3 lower bound;
  their distances are exact by virtue of M1 or M2.
* ❌ That any **record parameter** is claimed. The paper says it claims none.
* ❌ That the **comparison section's EA-table claim** is correct. It is not.

---

# PART D — Deliverables

`PHASE23_FFA_FINALIZATION/`

| file | purpose |
|---|---|
| `PHASE23_FFA_OPTION_C_COMPLIANCE.md` | Task A — Option C assessment + draft editorial email (**not sent**) |
| `PHASE23_DATA_AVAILABILITY_STATEMENT.md` | Task B — corrected statement, marked PROPOSED |
| `PHASE23_GENERATIVE_AI_DECLARATION.md` | Task C — eight-activity matrix, two candidate declarations (**neither inserted**) |
| `PHASE23_AUTHOR_ORIGINALITY_CONFIRMATION.md` | Task D — seven attestations, all marked `[RESEARCHER CONFIRMATION REQUIRED]` |
| `PHASE23_SUPPLEMENTARY_FILE_DESCRIPTIONS.csv` | Task E — 86 rows, description + SHA-256 for every published file |
| `PHASE23_THIRD_PARTY_DATA_REVIEW.md` | Task E — review of `comparison_grassl_q9.csv`; **two findings** |
| `PHASE23_LICENCE_RECOMMENDATION.md` | Task F — licence comparison, mixed-licence recommendation (**not applied**) |
| `PHASE23_COVER_LETTER_FINAL_DRAFT.md` | Task H — updated cover letter (**not sent**) |
| `PHASE23_BUILD_AND_VALIDATION_REPORT.md` | Task G + I — change record, build, validation |
| `PHASE23_FINAL_SUBMISSION_CHECKLIST.md` | Task J — 59-item checklist: 42 complete, 17 pending |
| `PHASE23_RESEARCHER_DECISION_SHEET.md` | this file |
| `MANIFEST.sha256` | SHA-256 of the above |

`PAPER/FFA_FINAL_SUBMISSION_V2/` — the new staging copy: 42-page PDF,
SHA-256 `d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1`.

---

# PART E — What I recommend you do first

1. **Answer decision 11.** There is a false sentence in your comparison section,
   and it is the kind a referee will spot immediately. It is a one-sentence fix
   and the conclusion is unaffected.
2. **Answer decision 1.** The AI declaration is the item most likely to cause
   trouble later, and it is yours to make. The project record and your stated
   account disagree; only you can say which is right.
3. **Answer decisions 2–8.** Seven attestations. They are quick, and nothing can
   be submitted without them.
4. **Then** decide on the licence and the editorial email.

I have stopped here and am waiting for your decisions. I will not send the
email, apply the licence, create the DOI or the release, or submit the
manuscript without explicit authorisation.
