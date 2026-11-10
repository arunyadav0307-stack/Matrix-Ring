# Phase 21 — Final decision report

**Private research data access and FFA Option C compliance**
Branch `arena/59de606f-matrix-ring` · Date 2026-11-10
Journal: *Finite Fields and Their Applications* (Elsevier)

---

## 1. Status classification

The five defined states, applied honestly — several apply at once, because the
researcher's position and the journal's position are different things.

| status | applies? | why |
|---|---|---|
| **PRIVATE ACCESS APPROVED BY RESEARCHER** | ✅ **YES** | The researcher has explicitly approved private access upon reasonable request, and has explicitly declined public deposit, a public GitHub data link, a Zenodo deposit, a DOI, a GitHub release, a public tag and a branch merge. |
| **ACCEPTABLE UNDER FFA OPTION C** | ❌ **NO — not demonstrated** | No official source states that access upon request satisfies Option C. The policy offers two branches — deposit plus link, or a statement explaining why sharing *isn't possible* — and this arrangement is neither. |
| **EDITORIAL CONFIRMATION REQUIRED** | ✅ **YES** | The policy is genuinely silent on author-request arrangements (ambiguity identified in Task A, Q3/Q6). Only the editorial office can settle it. A draft clarification email is prepared and **not sent**. |
| **NOT ACCEPTABLE UNDER CURRENT POLICY** | ⚠️ **YES on the strict reading** | Option C says "**required**". The fallback is conditioned on sharing being impossible, and the materials here are plainly depositable (86 files, ~2.4 MB, all original work, pure stdlib, no third-party restriction). |
| **SUBMISSION BLOCKER** | ⚠️ **YES, until resolved** | On the strict reading, the manuscript cannot be submitted compliantly. One Editor's email could clear it. |

**The distinction that must not be blurred:** the researcher's *willingness* to
share privately is a decision the researcher is entitled to make and has made.
The journal's *acceptance* of that arrangement is a separate question, and it
has not been obtained. Nothing in this phase treats the first as the second.

### The second blocker: no truthful "why" exists

Independent of the above, the Option C fallback requires the author to
"make a statement explaining **why**" sharing isn't possible. The researcher
has given **no reason**. This phase did not invent one. Every candidate —
confidentiality, proprietary status, legal restriction, institutional
restriction, privacy, security, third-party restriction, technical
impossibility — was checked and found either untrue or unsupported (Task B §3).
So even on the lenient reading, the statement is incomplete until the
researcher supplies a reason or the editor accepts one without it.

---

## 2. Task-by-task outcome

### Task A — policy verification

Official wording re-read live on 2026-11-10 from six Elsevier/FFA pages. The
Option C text is **unchanged** from Phases 10–13. Findings:

* Option C is **required**, not encouraged — "required" appears in both the
  journal guide and the Elsevier options page.
* The statement branch is a **fallback for impossibility**, not a free
  alternative: it is conditioned on "**If sharing your research data isn't
  possible**".
* "On request" / "upon reasonable request" appears in **none** of the six
  sources. The ambiguity is explicit and is not resolved by inference.
* The materials **are** research data under the FFA definition ("software,
  code, models, algorithms, protocols, methods, and other relevant materials"),
  so the argument "this is not research data" is unavailable.
* The FAQ answer "Is it compulsory to share my research data? No" does **not**
  help, because FFA is one of the journals that has adopted its own mandatory
  policy — which the same FAQ tells authors to check.
* No official source confirms a reviewer-only file channel. Not assumed.

Recorded in full, with verbatim quotations and URLs:
`PHASE21_FFA_OPTION_C_POLICY_VERIFICATION.md`.

### Task B — the statement

Two forms prepared and compared. **S1** (recommended) enumerates the material
accurately and states that no public deposit exists; **S2** is the conventional
one-line formula and is vaguer. Both were checked line by line against the real
inventory — every noun in S1 corresponds to a real file group. Neither claims
confidentiality, proprietary status or any other restriction.

**Neither is compliant as it stands**, because neither supplies the "why" the
policy asks for. Recorded in
`PHASE21_PRIVATE_DATA_AVAILABILITY_STATEMENT.md`.

### Task C — private-access inventory

`PHASE21_PRIVATE_DATA_INVENTORY.csv` — **86 rows, one per file**, matching the
86-file package exactly. Columns: file group, file, bytes, **full SHA-256**,
purpose, manuscript section, whether it supports a principal result, whether it
can be provided privately, and any third-party or licence restriction.

* 22 scripts · 23 logs · 29 generator matrices · 8 parameter tables · 4
  documentation files
* **80 files** support a principal result of the manuscript
* **1 file** carries external third-party content:
  `parameter_tables/comparison_grassl_q9.csv`, values read from codetables.de
  on 2026-11-04 and quoted verbatim
* **no public download URL** appears anywhere in the inventory
* every script's purpose was read from its own docstring, not guessed

### Task D — request-handling procedure

`PHASE21_PRIVATE_REQUEST_HANDLING_PROCEDURE.md` — contact point
(**arunyadav0307@gmail.com**), how to request, how requests are evaluated
(including the default refusal for material outside the inventory), what can be
shared, transfer method, integrity check (`sha256sum -c MANIFEST.sha256` →
85/85 OK), and the third-party handling rule. Written as a procedure to be
followed; **no service has been established** and none is claimed.

### Task E — editorial clarification email

`PHASE21_EDITORIAL_CLARIFICATION_EMAIL.md` — **DRAFT, NOT SENT.** Addresses the
FFA editorial office, gives the exact title, states the exact proposed
statement, describes the four kinds of material, and asks four specific
questions, including directly whether an on-request arrangement is acceptable
and whether a reviewer-only channel exists. It does not claim any exception has
been granted.

### Task F — manuscript handling

* **Canonical manuscript not modified.** No final statement inserted.
* **Staging copy prepared** at `PHASE21_PRIVATE_DATA_ACCESS/staging/`: one
  change only — the Data availability block. All 13 section files
  byte-identical to the FFA copy. Built clean: 0 errors, 0 undefined citations
  or references, 0 missing glyphs, 0 overfull boxes, 42 pages, PDF SHA-256
  `7fd0896a2e715afd050f1fb1c84f00423d6b3bf64a51f93a007b4bbd37626ae3`.
  Validators: **13 PASS / 0 FAIL** and **56 checks / 0 mismatches**.
* **⚠️ Finding:** the canonical manuscript's existing Data availability section
  (rendered on **page 37**) asserts the now-withdrawn GitHub route and prints a
  live public URL. That section is superseded and must be replaced before
  submission on **either** route. Not removed here, because Task F forbids
  inserting a final statement and leaving the mandatory section empty would be
  worse.
* Nothing else altered: abstract, theorems, proofs, parameters, generator
  matrices, author details, funding and competing-interest declarations all
  untouched.

---

## 3. Repository state — read-only inspection, nothing changed

| property | value |
|---|---|
| repository | `arunyadav0307-stack/Matrix-Ring` |
| visibility | **public** (unchanged) |
| default branch | `main` @ `ea43e959…` |
| research branch | `arena/59de606f-matrix-ring` @ `404f771d…` (start of this phase) |
| licence | **NONE** (unchanged — deferred) |
| branch protection | both branches unprotected (unchanged) |
| releases | **0** |
| tags | **0** |
| `PAPER/supplementary/` on `main` | **0 files — absent** (unchanged defect) |
| `PAPER/supplementary/` on research branch | 86 files |

**Nothing was published.** No public GitHub upload, no release, no tag, no
merge, no visibility change, no Zenodo deposit, no DOI, no licence applied, no
submission.

---

## 4. Safeguards

**77 protected hashes** recorded before the work and re-checked after:
**all 77 unchanged.** This covers `PAPER/main.tex`, `PAPER/main.pdf`, all 13
section files, both supplementary manifests (85/85 and 86/86 verified OK), the
three archive zips, every Phase 10 / 13 / 17 / 19 document and manifest, the
V2 and V3 package manifests (131/131 and 72/72 OK), and both validators.

Deferred matters were **not** reopened and retain their existing status:
generative-AI declaration, licence selection, Zenodo decisions, and the other
previously deferred author declarations.

---

## 5. What the researcher must decide

| # | decision | consequence if not taken |
|---|---|---|
| 1 | Send the clarification email (**or** authorise a repository deposit) | On the strict reading this remains a **submission blocker** |
| 2 | Supply a truthful reason for non-deposition, or ask the editor to accept the statement without one | The statement cannot meet the literal Option C wording |
| 3 | Authorise replacement of the superseded GitHub-link Data availability section in the canonical manuscript (**required either way**) | A link the researcher no longer authorises would be published with the article |
| 4 | Confirm statement S1 (or choose S2) | No final statement can be inserted |

---

## 6. Stopping point

Phase 21 is complete. **Nothing has been sent, uploaded, published, deposited,
tagged, released, merged or submitted.** No Editorial Manager account exists.
No data-sharing service has been created. Awaiting explicit researcher approval.
