# Phase 11 / Task C1 — Author information confirmation

**Status: RESEARCHER CONFIRMATION REQUIRED. NOTHING HAS BEEN ENTERED.**

This document states what FFA/Elsevier requires and records exactly what the
project currently holds. **No name, affiliation, address, country, email or
ORCID has been filled in, inferred or guessed.** Inference from the repository
owner's account name, from prior conversation, or from institutional
references in the manuscript is explicitly forbidden and was not performed.

## 1. What FFA/Elsevier requires (verified 2026-11-10)

Retrieved from the official FFA guide for authors.

| requirement | official policy |
|---|---|
| Names | Given name(s) + family name, presented **exactly** as they should appear. |
| Author order | The order in the manuscript **must match** the order entered in the submission system. |
| Affiliations | Each author's affiliation(s) on the title page as **lowercase superscript letters**, immediately after the name, with the **full postal address of each affiliation including the country**. |
| Corresponding author | **Exactly one** author designated as corresponding author, with a **publishable** email address. |
| Email visibility | The corresponding author's email address **is published** in the article. |
| Addresses | Present/permanent addresses, if different from the affiliation, as **numbered footnotes** on the title page. |
| ORCID | Encouraged to be supplied in the submission system. |

## 2. What the manuscript currently contains

| item | value in `PAPER/main.tex` | status |
|---|---|---|
| Author line | `\AUTHORPLACEHOLDER` (a macro defined as a placeholder, at lines 43, 53, 103) | **BLANK — blocking** |
| Affiliation | absent | **BLANK — blocking** |
| Postal address / country | absent | **BLANK — blocking** |
| Corresponding author | absent | **BLANK — blocking** |
| Email | absent | **BLANK — blocking** |
| ORCID | absent | **not mandatory; recommended** |

There is a comment in `main.tex` (lines 8–10) noting that the author metadata
is deliberately left as a placeholder. Nothing has been recorded anywhere in
the project that would allow any of these fields to be filled truthfully.

## 3. What the staging copy provides

`PAPER/FFA_SUBMISSION_STAGING/main.tex` adds an author-metadata block with
**visible, bracketed placeholders** so that the structure can be checked and
compiled:

```
\newcommand{\AUTHORONE}{[GIVEN NAME] [FAMILY NAME]}
\newcommand{\AUTHORONEINST}{[DEPARTMENT OR SCHOOL]}
\newcommand{\AUTHORONEORG}{[UNIVERSITY OR ORGANISATION]}
\newcommand{\AUTHORONEADDR}{[FULL POSTAL ADDRESS]}
\newcommand{\AUTHORONECOUNTRY}{[COUNTRY]}
\newcommand{\CORRESPONDINGEMAIL}{[CORRESPONDING AUTHOR EMAIL]}
```

Commented-out blocks for a second author are provided, since the manuscript
uses "we" throughout and may be multi-author. **Nothing is asserted about the
number of authors either way.**

Affiliations are typeset as a centred block after `\maketitle` rather than via
`\thanks`, because `\thanks` invokes a footnote symbol from a TS1 font at 6pt
that the font map used by this build does not provide; `\thanks` caused a hard
pdfTeX failure (`Font tcrm0600 at 600 not found`) during the Phase 11 build.
The centred block is cosmetically equivalent and avoids the missing glyph.

## 4. Researcher action items

1. Give the **given name(s) and family name** of every author, and the author
   order to be used in the submission system.
2. Give, for each author, the **department/school, institution, full postal
   address and country**.
3. Designate **exactly one** corresponding author and give a **publishable**
   email address (it will appear in the article).
4. Supply **ORCID iDs** (encouraged; not mandatory).
5. Confirm whether the author order in the manuscript matches the order that
   will be entered in the submission system.
6. Confirm whether any author has a present/permanent address differing from
   the affiliation (goes in a numbered footnote).
7. Decide on the **CRediT author-contribution statement** (encouraged, not
   mandatory) — see `PHASE11_FFA_FINALIZATION`.

**Until items 1–4 are answered, the manuscript cannot be submitted.** This is
a BLOCKING item.
