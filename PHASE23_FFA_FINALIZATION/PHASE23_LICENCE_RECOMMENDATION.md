# Task F — Licence options for the public `research-data` deposit

> # 🟡 FINAL DECISION: **RESEARCHER APPROVAL REQUIRED**
> **No licence has been applied. Nothing has been committed. No LICENSE file
> exists in the repository.** Applying a licence is an irreversible act with
> legal consequences and is the author's decision alone.

**Current state of the repository: NO LICENCE.** GitHub reports `license: null`.
Under default copyright, the materials are viewable but **no reuse is
permitted** — not by a reader, not by a referee, not by a repository, not by
anyone who wants to extend the work.

This document compares the requested options and recommends a mixed licence.
It is a draft. **The final choice is the researcher's.**

---

## F1. Why this matters now

The data are public. Without a licence, "public" means readable, not reusable.
That gap has three concrete consequences already visible elsewhere in this
phase:

1. **Option C compliance.** A "data repository" whose contents carry no reuse
   rights is a weaker thing than the policy contemplates (see
   `PHASE23_FFA_OPTION_C_COMPLIANCE.md`, §A4).
2. **The editorial question.** Question 3 of the draft clarification email asks
   the journal whether a licence is expected. If the journal says yes, the
   decision must already be made.
3. **The third-party file.** `comparison_grassl_q9.csv` is third-party data
   under an asserted copyright. **No licence granted by this project can
   lawfully cover it** — it must be excluded or separately cleared (see
   `PHASE23_THIRD_PARTY_DATA_REVIEW.md`).

---

## F2. Candidate licences — code

| criterion | **MIT** | **BSD-3-Clause** | **Apache-2.0** |
|---|---|---|---|
| Type | permissive | permissive | permissive |
| Length | ~170 words | ~75 words | ~11 kB, verbose |
| Attribution required | ✅ yes | ✅ yes | ✅ yes |
| **Patent grant** | ❌ none (implicit only) | ❌ none | ✅ **explicit, with a defensive termination clause** |
| Trademark grant | ❌ none | ❌ none | ✅ explicit (does not grant trademark rights; states that) |
| **Must state changes made** | ❌ no | ❌ no | ✅ **yes — modified files must carry prominent notices** |
| Must ship the licence text | ✅ yes | ✅ yes | ✅ yes, plus a NOTICE file if one exists |
| Requires a NOTICE file | ❌ no | ❌ no | ✅ if the project has one |
| Endorsement restriction | ❌ no | ✅ **yes — cannot use the author's name to endorse derivatives without permission** | ✅ yes, via the trademark clause |
| Compatible with GPLv2 | ✅ yes | ✅ yes | ❌ **no** (GPLv3 only) |
| Widely recognised | ✅ extremely | ✅ extremely | ✅ extremely |
| Typical home | research code, utilities | research code, academic releases | larger projects, industry-facing code |

## F3. Candidate licences — data and documentation

| criterion | **CC BY 4.0** | **CC0 1.0** |
|---|---|---|
| Type | permissive, **attribution** | **public-domain dedication** |
| Attribution required | ✅ **yes — mandatory, and this is the point** | ❌ **no — none whatsoever** |
| Credit to this project | ✅ preserved in every downstream use | ❌ not required; anyone may reuse without naming the source |
| Commercial reuse | ✅ permitted | ✅ permitted |
| Derivative works | ✅ permitted | ✅ permitted |
| Irrevocable | ✅ yes | ✅ yes, and **not reliably reversible** |
| Waives moral/related rights | ❌ no | ✅ yes, to the extent possible |
| Fallback licence if the waiver fails | n/a | ✅ a permissive fallback licence applies |
| **Fit for academic data** | ✅ **strong** — this is why citation-based credit exists | ⚠️ weaker for an author who wants credit |
| Database rights (EU) | covered by CC BY 4.0 | waived |

---

## F4. Recommendation: a mixed licence

The deposit contains two different kinds of thing, and one licence does not fit
both well.

| content | files | recommended licence |
|---|---:|---|
| **Code** | 22 Python scripts | **MIT** (see F5 for the alternative) |
| **Data — generator matrices, parameter tables, distance certificates** | 29 + 7 + 1 = 37 | **CC BY 4.0** |
| **Documentation — README, environment, certification procedure** | 3 | **CC BY 4.0** |
| **Logs** | 23 | **CC BY 4.0** |
| **Third-party data** | 1 (`comparison_grassl_q9.csv`) | ❌ **excluded — cannot be licensed by this project** |

### Why MIT for the code

* Shortest of the three and the most widely recognised in scientific computing.
* Imposes no obligation to state modifications — proportionate for research
  scripts that others will adapt freely.
* The absence of an explicit patent grant is a real but minor drawback here:
  these are mathematical-computation scripts, not a patent-sensitive
  implementation.
* **Choose Apache-2.0 instead if** the researcher wants an explicit patent grant
  and is willing to accept the verbosity and the modification-notice
  obligation. **Choose BSD-3-Clause instead if** the researcher specifically
  wants to forbid use of their name to endorse derivatives.

### Why CC BY 4.0 rather than CC0 for the data

* **Attribution is the currency of academic credit.** CC0 lets anyone reuse the
  28 certified generator matrices and the distance certificates without naming
  this project at all. That is a real cost for a work whose value lies in being
  citable.
* CC BY 4.0 is the standard licence for research data precisely because it
  maximises reuse while preserving the citation link.
* CC0's dedication is **irrevocable and not reliably reversible** — once
  applied, it cannot be taken back if circumstances change. CC BY 4.0 is also
  irrevocable as to licences already granted, but it keeps the attribution
  chain intact.
* **Choose CC0 only if** the researcher specifically wants to place the data in
  the public domain and does not require credit.

### The mixed licence is normal and workable

Separate licences for code and data in one repository are standard practice.
The README should state plainly which files are under which licence. There is
no legal obstacle to shipping MIT-licensed scripts alongside CC BY 4.0-licensed
data in the same directory.

---

## F5. Implementation notes — if and when the researcher decides

**Not done, and not to be done without approval.**

1. Add `LICENSE` (MIT text, copyright "Arun Kumar Yadav", year 2026) at the
   root of `research-data/`.
2. Add `LICENSE-DATA` (CC BY 4.0 text or a clear pointer to
   <https://creativecommons.org/licenses/by/4.0/>) in `research-data/`.
3. State the split in `research-data/README.md`: code → MIT; data, logs and
   documentation → CC BY 4.0; `quantum_code_records/comparison_grassl_q9.csv`
   → third-party, excluded.
4. **Exclude the third-party file from the licence grant explicitly.** No
   licence this project applies can cover it.
5. Add SPDX short identifiers (`MIT`, `CC-BY-4.0`) where practical.
6. Add short licence headers to the 22 scripts.
7. **Conduct the change on the session branch, then commit and push in the
   normal fast-forward way** — but note that `research-data/` currently lives
   on `main`, so this needs a decision about how the change reaches `main`.

**A licence is not applied by silence and not applied by describing one here.
It is applied only by adding the licence files and committing them.**

---

## F6. What the researcher must decide

| # | decision | options |
|---|---|---|
| 1 | **Apply a licence at all?** | Yes / No (current state: No) |
| 2 | **Licence for the 22 scripts** | MIT *(recommended)* / BSD-3-Clause / Apache-2.0 / none |
| 3 | **Licence for data, logs and documentation** | CC BY 4.0 *(recommended)* / CC0 1.0 / none |
| 4 | **The third-party file** | Keep with provenance / email codetables.de / **remove from the deposit** / keep but mark excluded from the licence |
| 5 | **Licence headers in the scripts** | Yes / No |
| 6 | **How the change reaches `main`** | Direct commit / via the session branch |

**Status: all six pending. Nothing has been applied.**

---

## F7. Statement of current fact, for use elsewhere in this phase

> The repository carries **no licence**. The materials are publicly viewable
> and have been verified accessible without authentication, but **no reuse
> permission has been granted**. Readers may read; they may not lawfully
> redistribute or build upon the contents without the author's permission.
> This is stated accurately, and not represented as an open-data deposit,
> anywhere else in these deliverables.
