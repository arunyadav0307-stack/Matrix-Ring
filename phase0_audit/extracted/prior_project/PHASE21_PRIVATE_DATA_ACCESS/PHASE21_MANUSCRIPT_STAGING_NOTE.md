# Task F — Manuscript staging note

## 1. Status of the staged data-availability section

> **PROPOSED** — **POLICY VERIFIED** — **PENDING EDITORIAL CONFIRMATION** —
> **NOT COMPLIANT** (as a final statement)

These four labels are used exactly as the task specifies:

| label | meaning here |
|---|---|
| **PROPOSED** | The wording is put forward for the researcher and the editor. It is not adopted. |
| **POLICY VERIFIED** | The FFA Option C requirement has been re-read from the official source on 2026-11-10; see `PHASE21_FFA_OPTION_C_POLICY_VERIFICATION.md`. |
| **PENDING EDITORIAL CONFIRMATION** | Whether private access on request is acceptable is **not** settled by the policy text; the question is put to the editorial office in `PHASE21_EDITORIAL_CLARIFICATION_EMAIL.md`. |
| **NOT COMPLIANT** | On the strict reading of Option C (deposit + link required; the statement branch is conditioned on sharing being impossible), this arrangement does **not** satisfy the mandatory policy. |

## 2. The canonical manuscript: not modified

**No final Data Availability Statement has been inserted into the canonical
manuscript.** `PAPER/FINAL_RESEARCHER_REVIEW_V3/` and
`PAPER/FFA_FORMATTED_SUBMISSION/` are untouched by this phase (verified by
hash — see §6).

### ⚠️ Finding that must be acted on before submission

The canonical manuscript **already contains** a `\section*{Data availability}`
block which asserts the now-withdrawn GitHub route and prints a public URL:

> "The researcher has elected to use the project's existing public GitHub
> repository *instead of* a dedicated data repository such as Zenodo. The data
> are publicly readable at the commit-pinned address
> `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary` …"

This is rendered on **page 37** of
`PAPER/FFA_FORMATTED_SUBMISSION/main.pdf`, verified by text extraction.

The researcher has **withdrawn authorisation** for that link. That section is
therefore superseded and **must be replaced before submission regardless of
which route is finally chosen** — private access on request, or a repository
deposit. Leaving it as it stands would publish a link the researcher no longer
authorises, in a statement the journal publishes with the article.

It was **not** removed from the canonical manuscript in this phase, because
Task F forbids inserting a final statement and because removing it without
replacing it would leave a mandatory section empty. The replacement is prepared
in the staging copy only (§3).

## 3. The staging copy

| | |
|---|---|
| path | `PHASE21_PRIVATE_DATA_ACCESS/staging/` |
| base | `PAPER/FFA_FORMATTED_SUBMISSION/` (the FFA-formatted copy, Phase 19) |
| files | `main.tex`, `sections/` (13 files), `references.bib`, `compile/` |
| change | **one** — the `\section*{Data availability}` block in `main.tex` |
| source diff vs the FFA copy | `main.tex` only; all **12** section files byte-identical |
| compiled | `staging/build/main.pdf`, 42 pages, 580,540 bytes |
| PDF SHA-256 | `7fd0896a2e715afd050f1fb1c84f00423d6b3bf64a51f93a007b4bbd37626ae3` |

The staged section reads:

> **Data availability**
>
> [*PROPOSED — POLICY VERIFIED — PENDING EDITORIAL CONFIRMATION — NOT COMPLIANT
> AS A FINAL STATEMENT.*] *Finite Fields and Their Applications* applies
> Elsevier research-data **Option C**, under which authors are required to
> deposit their research data in a relevant data repository and to provide a
> link to the dataset during the submission process, or, if sharing the
> research data is not possible, to make a statement explaining why.
>
> The computational scripts, execution logs, generator matrices, parameter
> tables and certification documentation supporting this study are not publicly
> available. The corresponding author will make the relevant materials
> available on reasonable request.
>
> *Staging status — not part of the final statement.* The researcher has
> approved private access upon reasonable request and has **not** authorised a
> public deposit, a public repository link, a Zenodo deposit, a DOI, a GitHub
> release or a public tag. Whether this arrangement satisfies Option C is
> **not** established by the official policy text, which does not mention
> access upon request; editorial confirmation is required before submission.
> The complete package comprises 86 files — 22 computational scripts, 23
> execution logs, 29 generator matrices, 8 parameter tables and 4 documentation
> files — certified by a SHA-256 manifest and inventoried in
> `PHASE21_PRIVATE_DATA_INVENTORY.csv`. See
> `PHASE21_FFA_OPTION_C_POLICY_VERIFICATION.md` and
> `PHASE21_MANUSCRIPT_STAGING_NOTE.md`.

The bracketed status marker and the "Staging status" paragraph are scaffolding.
**Both are removed** when the section is finalised; only the middle paragraph
is the proposed statement.

## 4. Build and validation of the staging copy

TeX Live 2024, genuine `BibTeX 0.99d`, `plain.bst`, 78-line `.bbl`, four
passes.

| check | result |
|---|---|
| errors | **0** |
| undefined citations | **0** |
| undefined references | **0** |
| missing glyphs | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **0** |
| pages | **42** |
| `validate_latex_v2.py` | **13 PASS / 0 FAIL** |
| `verify_examples.py` | **56 checks / 0 mismatches** |
| `github.com` / `e41c571` in rendered PDF | **0 / 0** |
| `??` in rendered PDF | **0** |
| 13 worked examples | **13** rendered; Example 8.12 on p. 33 |
| Tables A.1 / A.2 | present |
| abstract, title, author, affiliation, email | unchanged |
| "two independent methods", "exact for 11 codes and a lower bound for 17", "No record parameter is claimed", "at best equal" | all present |

One overfull box appeared on the first build, caused by a long
`\texttt{PHASE21_…}` filename; it was fixed with `\penalty0` break points, the
same device the superseded URL used. The rebuild is clean.

### Proof that nothing else changed

Comparing the staging PDF against
`PAPER/FFA_FORMATTED_SUBMISSION/main.pdf`:

* both are **42 pages**;
* with the Data availability block removed from both, the documents are the
  same length to the character (**117,301** characters each) and differ only in
  **page numbers** — the table of contents entries `B.2 Environment`,
  `B.3 Randomness`, `B.4 Where the numbers come from` shift from page 39/40 to
  40/41, and the running footers shift accordingly. That is pagination drift
  caused by inserting a slightly longer paragraph, not a content change.

## 5. What was deliberately not altered

Per Task F, none of the following was touched, in either the canonical or the
staged manuscript:

* the approved abstract (Option B2);
* any theorem, lemma, definition or proof;
* any quantum parameter, generator matrix or table value;
* author details, affiliation, corresponding-author email;
* the funding declaration;
* the competing-interest declaration;
* the CRediT placeholder;
* the generative-AI declaration placeholder.

## 6. Protected-file verification

**77 baseline hashes** were recorded before this phase. After all Phase 21
work, **all 77 are unchanged** — including `PAPER/main.tex`,
`PAPER/main.pdf`, all **12** section files, both supplementary manifests, the three
archive zips, and every Phase 10, 13, 17, 19 document and manifest.

## 7. What the researcher must do next

1. Decide whether to send the clarification email
   (`PHASE21_EDITORIAL_CLARIFICATION_EMAIL.md`) — **not sent**.
2. If the editor confirms the arrangement: authorise insertion of statement S1
   (without the staging scaffolding) into the canonical manuscript.
3. If the editor requires a deposit: the private-access route is blocked, and a
   repository deposit must be arranged — **this phase did not and must not
   create one**.
4. Either way: the superseded GitHub-link section must be replaced. It must not
   be left in a submitted manuscript.
