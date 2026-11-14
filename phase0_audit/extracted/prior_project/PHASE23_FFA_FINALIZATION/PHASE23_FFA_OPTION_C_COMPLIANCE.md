# Task A — FFA Research Data Option C compliance

**Access date for all official sources: 2026-11-10.**

## A0. Assigned status

> # 🟡 CONDITIONALLY ACCEPTABLE — EDITORIAL CONFIRMATION REQUIRED

This is one of the three permitted classifications and it is the honest one.
It is **not** "ACCEPTABLE" — the policy text does not establish that — and it
is **not** "NOT ACCEPTABLE" — the deposit-and-link obligation is now
substantially met, and the arrangement is far stronger than Phase 21's
"available on request".

The researcher's willingness to publish is one thing; the journal's acceptance
is another. Publishing the data does not, by itself, make the arrangement
compliant.

---

## A1. Independent verification of the published data

| # | check | result |
|---|---|---|
| 1 | repository public accessibility | ✅ `private: False`, `visibility: public` |
| 2 | commit exists on `main` | ✅ `3752a6c0e921ab21a6f78877f154e7e959f4c418`, parent `ea43e95`, 88 files |
| 3 | `research-data/` at that exact commit | ✅ 88 blobs under `research-data/` |
| 4 | all 86 selected research-data files | ✅ 86 present, **0 missing, 0 mismatched** (git blob SHA-1 across the whole tree) |
| 5 | README and publication manifest | ✅ both fetched; 10,062 and 9,212 bytes; byte-identical to local |
| 6 | unauthenticated file access | ✅ **87/87** manifest entries downloaded with **no Authorization header**; SHA-256 match 87/87 |
| 7 | file hashes against the published manifest | ✅ 87 OK / 0 FAILED |
| 8 | reproduction instructions | ✅ `README.md` states software requirements, exact commands, expected runtime and the expected diff |
| 9 | certification-method distribution | ✅ verified below |

### The five certification numbers — recomputed, not copied

Recomputed from the **published** file
`research-data/distance_certificates/certified_codes.csv` (28 rows) and
cross-checked against the canonical copy under `PAPER/supplementary/`:

| | verified | stated | |
|---|---:|---:|---|
| **M1 + M3** (M1 completed; M2 skipped) | **24** | 24 | ✅ |
| **M2 + M3** (M1 did not complete; M2 ran) | **4** | 4 | ✅ |
| **M3 exact distance** | **11** | 11 | ✅ |
| **M3 lower bound only** | **17** | 17 | ✅ |
| **All three methods completed together** | **0** | 0 | ✅ |

**M2 is conditionally skipped.** It runs only when M1 has not completed — the
`M2` column reads `n/a` for exactly the 24 codes where M1 finished, and carries
a value for exactly the 4 where M1 did not. That is why the final figure is 0.

**This report does not claim that all three methods were applied to every code,
and does not claim that every distance is exact:** 17 codes have only an
M3-proved lower bound. The distance reported for those codes is exact by virtue
of M1 or M2; M3 corroborates it from below.

## A2. Official policy — re-read, not assumed

| source | URL |
|---|---|
| FFA Guide for Authors | <https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/guide-for-authors> |
| Elsevier Research data guidelines | <https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines> |
| Elsevier Research data policy | <https://www.elsevier.com/about/policies-and-standards/research-data> |
| Elsevier Research data FAQs | <https://www.elsevier.com/about/policies-and-standards/research-data/faq> |

The FFA requirement is unchanged from Phases 10, 19 and 21:

> "For this journal, **Option C** instructions from our research data guidelines
> apply. This means that you are **required** to:
> * Deposit your research data in a relevant data repository.
> * Provide a link to the dataset during the submission process.
> * If sharing your research data isn't possible, make a statement explaining
>   why during the submission process."

The Elsevier options page confirms Option C is "**required**" (Options A and B
say "encouraged"; C, D and E say "required").

## A3. Assessment against the five distinctions requested

| dimension | assessment |
|---|---|
| **Public repository accessibility** | ✅ **Fully met.** Repository is public; all 87 manifest entries downloaded with no authentication; commit-pinned URL returns HTTP 200. |
| **Repository suitability for research data** | 🟡 **Not established.** The policy requires "a relevant data repository" and does **not** name GitHub as either acceptable or unacceptable. GitHub is a general-purpose software-hosting service without a curation or preservation mandate. Defensible, unconfirmed. |
| **Commit-pinned reproducibility** | ✅ **Strong.** The URL pins a content-immutable commit SHA, not a branch name. Every file is SHA-256-verified against a published manifest. |
| **Persistent data archiving** | ⚠️ **Weak.** Both branches are unprotected; the branch could be deleted or force-pushed. GitHub is a commercial service with no preservation mandate. A release or tag would be stronger — **not created, not authorised**. |
| **DOI requirement, if any** | ⚠️ **Not explicitly required, but absent.** The Option C wording requires deposit and a link; it does **not** say a DOI is mandatory. This report does **not** claim a DOI is required. Without one the data are not independently citable as a dataset. **Not created, not authorised.** |

## A4. Why "conditionally acceptable" and not "acceptable"

**What is now satisfied.** There is a public, permanent, content-addressed
location holding the data, with a link. The Phase 21 problem — that the
materials existed but were reachable only by private request, and that no
truthful "why not" could be written — is resolved. The deposit-and-link branch
of Option C is, on its wording, substantially met.

**What is not settled.**

1. The policy does not say GitHub counts as a "relevant data repository".
2. Durability depends on an unprotected branch of a commercial service.
3. There is no DOI, so no independent dataset citation.
4. There is **no licence**, so readers can view but have no reuse permission.
   A purported data repository whose contents carry no reuse rights is a weaker
   thing than the policy contemplates.
5. The third-party extract (`comparison_grassl_q9.csv`) carries provenance but
   no redistribution permission from its source.

**Do not claim full policy compliance merely because GitHub is public.**
Public visibility and policy compliance are different tests; the first is met,
the second is not established.

## A5. Clarification email

Because the official wording does not clearly establish whether GitHub
qualifies, a formal clarification email to the FFA editorial office is included
below. It is marked **DRAFT — NOT SENT** and will not be sent without the
researcher's explicit authorisation.

---

# Appendix E — Editorial clarification email

> # ⚠️ DRAFT — NOT SENT

**To:** the Editorial Office, *Finite Fields and Their Applications*
**Subject:** Research data policy (Option C) — repository suitability

Dear Editorial Office,

I am preparing a submission to *Finite Fields and Their Applications* and would
be grateful for a short clarification on the journal's research-data policy.

**Manuscript title:** "Quantum Error-Correcting Codes from Galois Hulls of
Cyclic Codes over Noncommutative Matrix Rings"

**What I have done.** I have deposited the research data underlying the paper
in a curated `research-data/` directory of a public GitHub repository, and I
intend to cite the commit-pinned location:

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data
```

The directory contains 86 files — 22 computation scripts, 23 execution logs, 29
generator matrices, 8 tables of quantum-code records and distance certificates,
and 4 documentation and verification files — each listed with its SHA-256 in a
published manifest, together with a README stating the software requirements
and the commands needed to reproduce the results.

**My questions.**

1. Does a **commit-pinned public GitHub repository** qualify as a "relevant
   data repository" for the purposes of Option C? The policy does not name
   GitHub, and I would rather ask than assume.
2. If it does qualify, is a commit-pinned URL acceptable, or does the journal
   require a **release, tag or DOI** so that the data are independently citable
   and durably preserved? I have not created a release, a tag or a DOI, and I
   am happy to if the journal requires one.
3. The repository currently carries **no licence**, so the materials are
   viewable but reuse is not permitted. Would the journal expect a licence to
   be applied before the data can be accepted as a deposit?
4. One file in the package, `quantum_code_records/comparison_grassl_q9.csv`,
   contains three rows of best-known q = 9 bounds read from codetables.de. If
   redistribution of that extract is a concern, I can remove the file and
   restate the three values in the text with a citation to the source. Please
   advise.

I should add that I am not seeking an exemption from the policy. If a
repository deposit with a DOI is what Option C requires, I will make one; I
simply want to comply correctly rather than guess.

Thank you for your help.

Yours sincerely,

**Arun Kumar Yadav**
School of Basic and Applied Sciences
K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India
arunyadav0307@gmail.com

---

**Reminder: this email has not been sent. No exception has been granted or
informally requested. Nothing in this phase constitutes journal acceptance of
the arrangement.**
