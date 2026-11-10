# Author metadata

**STATUS: CONFIRMED by the researcher on 2026-11-10 and incorporated.**

| field | value |
|---|---|
| Author count | **1** |
| Full name | **Arun Kumar Yadav** |
| School | School of Basic and Applied Sciences |
| University | K.R. Mangalam University |
| Address | Sohna Road, Gurugram, Haryana, 122103 |
| Country | India |
| Corresponding author | Arun Kumar Yadav |
| Email | arunyadav0307@gmail.com |
| ORCID | **not supplied — none invented** |

This information is rendered on the title page of the compiled manuscript.
See `PHASE13_TITLE_PAGE_VERIFICATION.md`.

---

## Historical record (Phase 12 status — superseded)

## What is confirmed

| field | value | status |
|---|---|---|
| Number of authors | **1** (single author) | **CONFIRMED** 2026-11-10 |
| Author order | n/a with one author | resolved by the count |

## What is still required

| field | value | status |
|---|---|---|
| Given name(s) | — | **PENDING** |
| Family name | — | **PENDING** |
| Institution | — | **PENDING** |
| Department or school | — | **PENDING** |
| Street and postal address | — | **PENDING** |
| City | — | **PENDING** |
| State | — | **PENDING** |
| Country | — | **PENDING** |
| Corresponding-author email (publishable) | — | **PENDING** |

## Why these are blank rather than guessed

* No name was inferred from the GitHub account `arunyadav0307-stack`.
* No affiliation was inferred from institutions named in the cited literature
  (Kent State, University of Delhi, IIT ISM Dhanbad and Lovely Professional
  University all appear in the bibliography) or from earlier conversation.
* No email was invented or substituted.

## Official FFA title-page requirements (verified 2026-11-10)

> "**Author names.** Provide the given name(s) and family name(s) of each
> author. The order of authors should match the order in the submission
> system. Carefully check that all names are accurately spelled."
>
> "**Affiliations**, referring to where the work was carried out, below the
> author names. Indicate affiliations using a **lowercase superscript letter**
> immediately after the author's name and in front of the corresponding
> address. Ensure that you provide the **full name and postal address of each
> affiliation, including the country name**."
>
> "**Corresponding author.** Clearly indicate who will handle correspondence…
> The **email address of the corresponding author must be included on the
> title page and will be published in the article**."
>
> "**Present/permanent address.** If an author has changed affiliation since
> the work described in your article was carried out, or was visiting during
> that time, a 'present address' (or 'permanent address') can be indicated by a
> footnote to the author's name… Use superscript Arabic numerals for such
> footnotes."

## Present state of the manuscript

The source carries placeholder macros:

```latex
\newcommand{\AUTHORONE}{[GIVEN NAME] [FAMILY NAME]}
\newcommand{\AUTHORONEINST}{[DEPARTMENT OR SCHOOL]}
\newcommand{\AUTHORONEORG}{[UNIVERSITY OR ORGANISATION]}
\newcommand{\AUTHORONEADDR}{[FULL POSTAL ADDRESS]}
\newcommand{\AUTHORONECOUNTRY}{[COUNTRY]}
\newcommand{\CORRESPONDINGEMAIL}{[CORRESPONDING AUTHOR EMAIL]}
```

The second-author block has been **disabled** (not merely left unfilled) to
reflect the confirmed single-author count.

Affiliations are typeset as a centred block after `\maketitle` rather than via
`\thanks`, because `\thanks` requires a TS1 footnote glyph at 6pt that the
offline font map cannot supply; `\thanks` caused a hard pdfTeX failure in
Phase 11. This is a rendering choice only and does not affect compliance.

## Note on "we"

The manuscript uses "we" throughout. This is conventional in single-author
mathematics papers and no change was made on that basis.
