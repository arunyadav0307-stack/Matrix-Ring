# Task D — Originality and exclusive-submission confirmations

> # 🟡 DRAFT — ALL SEVEN STATEMENTS REQUIRE `[RESEARCHER CONFIRMATION REQUIRED]`

**Nothing on this page has been submitted.** These are the author's own
attestations. An agent cannot truthfully make them: originality, exclusive
submission and authorship are facts known only to the author, and Elsevier
holds the author — not any assistant — responsible and accountable for them.

Each statement below is drafted in the author's name so that it can be
accepted, amended or rejected. **Until the researcher confirms each one, it
must not be used, signed, or carried into any submission system.**

**Manuscript:** "Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings"
**Author:** Arun Kumar Yadav, School of Basic and Applied Sciences, K.R.
Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India
**Intended submission venue:** *Finite Fields and Their Applications* (Elsevier)

---

## 1. Originality of the work

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that this manuscript is the author's own original work, that all
> mathematical results, proofs, constructions and interpretations presented
> herein are the author's own, and that no part of the work has been copied,
> paraphrased or reproduced from another source without full attribution.
> Where the work of others is used, it is cited.

**Status: NOT CONFIRMED.**
**Note for the researcher:** this statement is straightforward as to the
mathematics, but it coexists with the unresolved AI-declaration question in
`PHASE23_GENERATIVE_AI_DECLARATION.md`. Confirming originality here does not
resolve that question — the two are separate attestations and both are needed.

---

## 2. Exclusive submission — not under consideration elsewhere

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that this manuscript, or any part of it, is not currently under
> consideration for publication by any other journal, conference or publisher,
> and that no substantially similar manuscript has been submitted elsewhere. I
> undertake not to submit it elsewhere while it is under consideration by
> *Finite Fields and Their Applications*.

**Status: NOT CONFIRMED.**
**Note for the researcher:** if any preprint, thesis chapter, conference
abstract or arXiv posting exists — or if one is planned — this statement must
be amended to disclose it. The agent has no knowledge of any such posting and
has not checked for one.

---

## 3. No prior publication

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that this manuscript has not been published previously in any
> form — in print or electronically — and that it does not contain material
> that has been published previously, except where that material is explicitly
> quoted and cited with its source.

**Status: NOT CONFIRMED.**
**Note for the researcher:** the project repository is public and contains
earlier drafts of the manuscript and its sections. Making a draft publicly
viewable is not the same as publishing it, but if the researcher considers any
repository content to constitute prior publication, this statement must say so.
The agent takes no position on that characterisation.

---

## 4. Authorship and author approval

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that I am the sole author of this manuscript; that I qualify for
> authorship under Elsevier's authorship criteria; that I have approved the
> final version of the manuscript and agree to its submission; and that no
> person who qualifies for authorship has been omitted and no person who does
> not qualify has been included.

**Status: NOT CONFIRMED.**
**Note for the researcher:** if any collaborator, supervisor, student or
funding-body representative contributed in a way that merits authorship, they
must be added **before** submission, and the statement rewritten in the plural.
Adding authors after submission is far more difficult. This is the item most
often got wrong, and only the researcher can answer it.
**Separately:** no AI tool has been listed or cited as an author, in accordance
with Elsevier's policy.

---

## 5. Integrity and accuracy of the reported results

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that the results reported in this manuscript are presented
> accurately and without fabrication, falsification or inappropriate data
> manipulation; that the computational results are reproducible from the
> deposited scripts and logs; and that the claims made are supported by the
> evidence presented.

**Status: NOT CONFIRMED.**
**Note for the researcher — what can be evidenced and what cannot:**

| claim | evidence available |
|---|---|
| 28 certified quantum codes reproduce from the deposited scripts | ✅ 22 scripts + 23 logs deposited, SHA-256-verified, at the commit-pinned location |
| The 28 codes were certified by three methods | ✅ re-derived this phase from the published `certified_codes.csv`: M1+M3 = 24, M2+M3 = 4, M3 exact = 11, M3 lower bound = 17, all three = 0 |
| **"All three methods applied to every code"** | ❌ **NOT TRUE — do not assert it.** M2 is conditionally skipped; it runs only for the 4 codes where M1 did not complete |
| **"Every distance is exact"** | ❌ **NOT TRUE — do not assert it.** 17 codes carry only an M3 lower bound |
| 125 quantum-code parameter tuples in the text match the source | ✅ verified programmatically |
| No record parameter is claimed | ✅ the manuscript states this explicitly |

**The agent confirms the evidence table; the author confirms the attestation.**

---

## 6. Ethics, consent and third-party rights

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that the work involves no human or animal subjects requiring
> ethical approval or consent; that it does not infringe the copyright,
> intellectual property or other rights of any third party; and that any
> third-party material used is either quoted with attribution or has been
> cleared for reuse.

**Status: NOT CONFIRMED — and qualified by an open item.**
**Note for the researcher:** one file in the deposited package contains
third-party material — `research-data/quantum_code_records/comparison_grassl_q9.csv`,
three rows of best-known q = 9 bounds read from codetables.de on 2026-11-04.
It carries provenance but **no redistribution permission** from its source. See
`PHASE23_THIRD_PARTY_DATA_REVIEW.md`. This statement should not be confirmed
until the researcher has decided whether to retain that file with attribution,
seek permission, or remove it and restate the three values in the text with a
citation.

---

## 7. Competing interests and funding

**`[RESEARCHER CONFIRMATION REQUIRED]`**

> I confirm that I have no known competing financial interests or personal
> relationships that could have appeared to influence the work reported in this
> paper, and that no funding was received for this work beyond the author's
> institutional support.

**Status: NOT CONFIRMED.**
**Note for the researcher:** the manuscript as compiled already states that the
author "declares no known competing financial interests" and that the work "did
not receive any specific grant from funding agencies in the public, commercial,
or not-for-profit sectors". Both were verified present in the compiled PDF.
**This confirmation reconciles that manuscript text with the author's own
attestation — it does not add anything new.** If either is now inaccurate, the
manuscript must be amended, not just this sheet.

---

## Summary

| # | statement | status |
|---|---|---|
| 1 | Originality | `[RESEARCHER CONFIRMATION REQUIRED]` |
| 2 | Exclusive submission | `[RESEARCHER CONFIRMATION REQUIRED]` |
| 3 | No prior publication | `[RESEARCHER CONFIRMATION REQUIRED]` |
| 4 | Authorship and approval | `[RESEARCHER CONFIRMATION REQUIRED]` |
| 5 | Integrity and accuracy of results | `[RESEARCHER CONFIRMATION REQUIRED]` |
| 6 | Ethics and third-party rights | `[RESEARCHER CONFIRMATION REQUIRED]` + open third-party item |
| 7 | Competing interests and funding | `[RESEARCHER CONFIRMATION REQUIRED]` |

**Seven of seven unconfirmed.** These items are the reason the overall phase
status cannot be "READY FOR RESEARCHER FINAL APPROVAL": they are author
attestations, and nothing in this workspace can supply them.
