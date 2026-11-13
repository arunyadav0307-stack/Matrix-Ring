# Task B — Private data availability statement

**Researcher's decision: Option A — private access upon reasonable request.**
No public deposit, no public GitHub data link, no Zenodo deposit, no DOI, no
GitHub release, no public tag, no branch merge.

**This is a proposed statement, not an automatic final declaration.** It is not
yet inserted into the canonical manuscript (Task F).

---

## 1. Statement S1 — the recommended longer form

> The computational scripts, execution logs, generator matrices, parameter
> tables and certification documentation supporting this study are not publicly
> available. The corresponding author will make the relevant materials
> available on reasonable request.

### Accuracy check against the actual inventory

| claim in S1 | true? | evidence |
|---|---|---|
| "computational scripts" | **yes** | 22 `.py` files in `PAPER/supplementary/scripts/` |
| "execution logs" | **yes** | 23 `.txt` files in `PAPER/supplementary/logs/` |
| "generator matrices" | **yes** | 29 files in `PAPER/supplementary/generator_matrices/` (28 codes + `INDEX.json`) |
| "parameter tables" | **yes** | 8 `.csv` files in `PAPER/supplementary/parameter_tables/` |
| "certification documentation" | **yes** | `CERTIFICATION_PROCEDURE.md` (plus `README.md`, `ENVIRONMENT.md`, `MANIFEST.sha256`) |
| "are not publicly available" | **yes, literally true** | no deposit exists; no DOI exists; the supplementary tree is absent from the repository's default branch — verified again this phase |
| "the corresponding author will make the relevant materials available on reasonable request" | **yes, subject to the author honouring it** | the researcher has explicitly confirmed willingness; the request procedure is in `PHASE21_PRIVATE_REQUEST_HANDLING_PROCEDURE.md` |

Total: **86 files**, all covered by `MANIFEST.sha256` (85 hash lines + the
manifest itself), verified this phase at **85/85 OK**.

### What S1 deliberately does not say

It does **not** say the materials are confidential, proprietary, commercially
sensitive, legally restricted, institutionally restricted, embargoed,
privacy-restricted or security-restricted. **None of those has been stated by
the researcher, and none is supported by the material.** No justification of
that kind has been invented.

---

## 2. Statement S2 — the shorter alternative

> The research data supporting this study are available from the corresponding
> author upon reasonable request.

### Difference from S1, and its policy implications

| | S1 | S2 |
|---|---|---|
| length | 2 sentences, enumerates the material | 1 sentence, generic |
| states that no public deposit exists | **yes** ("are not publicly available") | **no** |
| says what "research data" means here | **yes** (scripts, logs, matrices, tables, documentation) | **no** |
| transparency about the absence of a repository | **higher** | **lower** |
| risk of being read as "the data are generally obtainable" | lower | **higher** |

**Policy implication.** Option C asks the author either to deposit and link, or
to "make a statement explaining why" sharing isn't possible (S1/S2 of the
policy verification). Neither S1 nor S2 gives a reason, so **neither satisfies
the literal wording of the fallback branch**. The difference is one of
candour, not of compliance:

* **S1** is candid. It tells the reader exactly what exists, that it is not
  public, and how to get it. If the editor is willing to accept an on-request
  arrangement at all, S1 is the statement most likely to be accepted, because
  it discloses everything the policy cares about except a repository link.
* **S2** is the conventional formula. It is shorter and more familiar, but it
  is vaguer: it does not tell the reader that there is no deposit, and "the
  research data" is undefined. It is also the formula most likely to be
  challenged by a data editor, because it reads like a claim of availability
  without any mechanism behind it.

**Recommendation: use S1.** It is the more honest description of the actual
arrangement that the researcher has approved.

---

## 3. The reason gap — the single largest problem with both statements

Both S1 and S2 omit something the policy requires: **a reason**.

The Option C fallback is "make a statement **explaining why**". The researcher
has decided not to publish, but has given no reason for that decision. This
phase will not supply one. The following candidate reasons were considered and
**rejected as untrue or unsupportable**:

| candidate reason | why it is rejected |
|---|---|
| "the data are confidential" | not stated by the researcher; the material is published mathematics |
| "commercially sensitive / proprietary" | no commercial interest has been declared; the competing-interest declaration states none |
| "legally restricted" | no legal restriction is known to exist; the material is the author's own work |
| "institutionally restricted" | no institutional restriction has been stated |
| "privacy or security" | no personal data are involved |
| "third-party material cannot be shared" | only one file contains external content (`comparison_grassl_q9.csv`, values read from publicly published codetables); it is not restricted |
| "the data cannot be deposited" | **false** — 86 files, ~2.4 MB, pure Python stdlib, fully depositable |

An optional reason slot is therefore left open, to be completed **by the
researcher only**:

```
> [ OPTIONAL — TO BE COMPLETED BY THE RESEARCHER, OR LEFT OUT.
>   Insert a truthful reason here if the researcher wishes to give one.
>   Do not assert confidentiality, proprietary status, legal restriction,
>   institutional restriction, privacy or security unless true. ]
```

---

## 4. Status of both statements

| | |
|---|---|
| Researcher approval of the private-access arrangement | **APPROVED** (Phase 21 instruction) |
| Accuracy against the material inventory | **VERIFIED** (86 files, 85/85 manifest OK) |
| Policy compliance under FFA Option C (strict reading) | **NOT ACCEPTABLE** |
| Policy compliance under FFA Option C (lenient reading) | **EDITORIAL CONFIRMATION REQUIRED** |
| Inserted into the canonical manuscript | **NO** (Task F forbids it) |
| Present in the staging copy only | **YES** — `PHASE21_PRIVATE_DATA_ACCESS/staging/` |
| Sent to the journal | **NO** |

Neither statement may be represented as compliant until the editorial office
confirms the arrangement in writing.
