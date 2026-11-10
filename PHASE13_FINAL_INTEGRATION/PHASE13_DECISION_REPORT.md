# Phase 13 — Researcher decision report

Date: 2026-11-10 · Branch: `arena/59de606f-matrix-ring` · Base commit: `e41c571`

---

## Verdict

> ## CONDITIONALLY READY — 2 BLOCKING ITEMS REMAIN
> (down from 6 in Phase 12)

---

## 1. What got fixed

Your author details are in. The title page now reads:

```
Arun Kumar Yadavᵃ

ᵃ School of Basic and Applied Sciences, K.R. Mangalam University,
  Sohna Road, Gurugram, Haryana, 122103, India.

Corresponding author. E-mail: arunyadav0307@gmail.com
```

Used **verbatim** — no alteration to the name, institution, postal code or
email. No ORCID invented (none was supplied; it is optional). The superscript
letter follows FFA's requirement that affiliations be marked "with a lowercase
superscript letter immediately after the author's name and in front of the
corresponding address", with the full postal address **including country**.

Funding and competing interests are retained and now render in the PDF. The
competing-interest wording was changed to the **singular** ("The author
declares…") to match single authorship.

Clean rebuild: **0 errors, 0 warnings, 42 pages**, triple-validated. Abstract
re-measured and **unchanged at 213/199/226 words**.

## 2. Two things you need to decide

### ⚠️ A. Your GitHub choice does not currently work

You chose GitHub over Zenodo — respected, and nothing was created anywhere.
But I re-checked the live repository, and the problem Phase 12 found is
**still there**:

| check | result |
|---|---|
| `PAPER/supplementary/` on **`main`** (default branch) | **404 — ABSENT** |
| `PAPER/supplementary/` on the research branch | present |

**Anyone opening `https://github.com/arunyadav0307-stack/Matrix-Ring` lands on
`main` and finds no data at all.** The data exist only on
`arena/59de606f-matrix-ring`, 36 commits ahead.

I can cite a commit-pinned URL that *does* resolve:

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary
```

…but I have **not** made this final, because two risks remain: the branch is
**unprotected** (deletable), and the front door still doesn't work.

**To be clear about the policy:** Elsevier's Option C does **not** explicitly
require a DOI. It requires deposit in "a relevant data repository" plus a
link. GitHub is therefore **defensible** — I am not claiming you must use
Zenodo. The issue is purely that the data aren't reachable from the default
branch.

**Four fixes are prepared and waiting for your authorization** — pick any:

1. Merge the research branch into `main` (fixes the front door).
2. Create a release/tag at `e41c571` (stable, citable, shorter URL).
3. Enable branch protection on `main`.
4. Add a licence.

### ⚠️ B. The AI declaration: your account and the project record disagree

This is the one I want to be most direct about.

**You said:** AI tools were used **only for language enhancement**.

**The project records show** AI assistance across:

| activity | evidence |
|---|---|
| Manuscript drafting | 7 commits authored `Arena Agent <agent@arena.ai>`; 12 section files |
| LaTeX development | build scripts written by the agent |
| Proof exposition | decision log D-006/D-010 |
| The 22 computational scripts | `PAPER/supplementary/scripts/` |
| Verification tooling | `tools/validate_latex.py` and three others |
| Literature discovery | the bibliography — **four venue attributions were wrong** and needed correcting |
| Abstract revision | the Phase 11 rewrite |

Under Elsevier's policy, "language enhancement" sits close to the **exemption**
for "basic tools, such as tools used to check grammar, spelling, and
references" — which would mean **little or no disclosure**. The broader
activities are **squarely disclosable**.

**I have not inserted either version.** Filling the section with "language
enhancement only" would insert a statement the commit record contradicts;
filling it with the broader account would state something you haven't
confirmed. Both would be wrong.

One thing worth knowing: **your own blueprint mandates ChatGPT as the
independent auditor.** `06_AUDIT/Phase0_audit_request.md` says *"Researcher
(Arun): copy everything below the line into ChatGPT…"*, and the decision log
marks D-006 and D-010 *"Pending: researcher + ChatGPT audit"*. So ChatGPT's
*role* is documented in your own project — but I **cannot verify from the
repository whether those audits were actually performed**, and I have not
guessed a model name, version, provider or date anywhere.

**What I need:** answer the seven questions in §C6 of
`PHASE13_AI_DECLARATION_RECONCILIATION.md`. The most likely reading is that
you mean the *mathematics* is yours and AI only polished the wording — which
may well be true, but it doesn't make the drafting, scripting and literature
work disappear, and those need a decision.

## 3. Licence — recommendation delivered

You asked for a recommendation before choosing. Short version:

| material | recommendation | alternative |
|---|---|---|
| **22 scripts** | **MIT** | Apache 2.0 if you might patent/commercialise |
| **Data, docs, matrices, logs** (64 files) | **CC BY 4.0** | CC0 1.0 if you don't want attribution |
| **`references.bib`, third-party content** | **apply nothing** — not yours to licence | — |
| **Manuscript source** | **leave unlicensed** — check your Elsevier agreement first | — |

Two cautions: **CC licences are not appropriate for source code**, and
**CC0 is irrevocable**. Also note the repository currently declares **no
licence**, which means everything in it is legally "all rights reserved" —
nobody can reuse any of it today.

**Nothing applied.** No `LICENSE` file created.

## 4. State of the package

| | |
|---|---|
| Package | `PAPER/FFA_FINAL_SUBMISSION_PACKAGE/` |
| Files | 111 + manifest |
| PDF | 42 pp, `a0fea51c…b8bdd509` |
| Protected files | all unchanged — `main.tex`, `references.bib`, `main.pdf`, `main.bbl`, 12 sections, 3 archives |

## 5. What I have not done

No Zenodo deposit, DOI, release, tag, merge, visibility change, licence or
external upload. No submission, no Editorial Manager upload, no journal
account, no cover letter. No invented ORCID, model name, provider or date. No
change to any mathematical claim.

---

## Awaiting your decision on:

1. **AI declaration** — the seven questions in
   `PHASE13_AI_DECLARATION_RECONCILIATION.md` §C6.
2. **Data access** — authorize a merge to `main`, a release/tag, both, or
   neither (and if neither, the statement stays PENDING).
3. **Licence** — MIT + CC BY 4.0, or your alternative.
