# Phase 13 / Task A — Title-page verification report

**STATUS: VERIFIED.** The confirmed author information has been incorporated
into the staging copy and renders correctly.

Date: 2026-11-10 · Staging copy: `PAPER/FFA_SUBMISSION_STAGING/`

---

## A1. Values used — verbatim from the researcher

| field | value | source |
|---|---|---|
| Author count | **1** | Phase 13 instruction; consistent with the Phase 12 confirmation |
| Full name | **Arun Kumar Yadav** | researcher |
| Institution (school) | **School of Basic and Applied Sciences** | researcher |
| University | **K.R. Mangalam University** | researcher |
| Address | **Sohna Road, Gurugram, Haryana, 122103** | researcher |
| Country | **India** | researcher |
| Corresponding author | **Arun Kumar Yadav** | researcher |
| Email | **arunyadav0307@gmail.com** | researcher |

**Nothing was altered.** Spelling, institutional name, postal code and email
are used exactly as supplied.

**Nothing was invented.** No ORCID was added. No additional department,
affiliation or author contribution was created.

---

## A2. Compliance with the official FFA title-page instructions

Requirements verified 2026-11-10 from the FFA guide for authors.

| requirement | official wording | compliance |
|---|---|---|
| Author names | "Provide the given name(s) and family name(s) of each author… Carefully check that all names are accurately spelled." | ✅ `Arun Kumar Yadav` |
| Author order | "The order of authors should match the order in the submission system." | ✅ single author, trivially satisfiable — **must still be checked at submission** |
| Affiliations | "Indicate affiliations using a **lowercase superscript letter** immediately after the author's name and in front of the corresponding address. Ensure that you provide the **full name and postal address of each affiliation, including the country name**." | ✅ superscript `a` after the name and before the address; full postal address **with country** |
| Corresponding author | "Clearly indicate who will handle correspondence… The email address of the corresponding author **must be included on the title page and will be published** in the article." | ✅ rendered as "Corresponding author. E-mail: arunyadav0307@gmail.com" |
| Present/permanent address | "…can be indicated by a footnote… Use superscript Arabic numerals." | ✅ **NOT APPLICABLE** — no separate present/permanent address was supplied |
| Article title | "concise and informative… avoid abbreviations and formulae" | ✅ unchanged from the approved title |

---

## A3. Rendered title page — extracted from the compiled PDF

```
Quantum Error-Correcting Codes from Galois Hulls of Cyclic
Codes over Noncommutative Matrix Rings

Arun Kumar Yadavᵃ

ᵃ School of Basic and Applied Sciences, K.R. Mangalam University,
  Sohna Road, Gurugram, Haryana, 122103, India.

Corresponding author. E-mail: arunyadav0307@gmail.com
```

Verified by text extraction from page 1 of `build_modern/main.pdf` after a
clean four-pass build.

---

## A4. Placeholder removal

| placeholder | status |
|---|---|
| `[GIVEN NAME] [FAMILY NAME]` | ✅ removed |
| `[DEPARTMENT OR SCHOOL]` | ✅ removed |
| `[UNIVERSITY OR ORGANISATION]` | ✅ removed |
| `[FULL POSTAL ADDRESS]` | ✅ removed |
| `[COUNTRY]` | ✅ removed |
| `[CORRESPONDING AUTHOR EMAIL]` | ✅ removed |

`grep` for all six placeholder strings in `main.tex` returns **no matches**.

The second-author macro block, previously commented out, was **removed**
(rather than left as a dangling template) in Phase 12 once single authorship
was confirmed.

---

## A5. Mathematical integrity — nothing changed

| check | result |
|---|---|
| Canonical `PAPER/main.tex` | **untouched** — SHA-256 `ee47ce7e…4501737c` |
| All 12 canonical `sections/*.tex` | **untouched** — hashes unchanged |
| Citations | 13/13, 0 undefined |
| Theorem statements | unchanged |
| Numerical examples | 13/13 present |
| Abstract | **preserved** — Phase 11 revision, 213/199/226 words |

Only the title-page macros, the affiliation block and the two declaration
sections were edited in the staging copy.

---

## A6. Outstanding items on the title page

| item | status |
|---|---|
| **ORCID** | **NOT SUPPLIED** — encouraged, not mandatory. None was invented. |
| **Author contributions (CRediT)** | **PENDING** — encouraged, not mandatory. With a single author this is nearly vacuous but may still be worth a sentence. Researcher's call. |
| **Present/permanent address** | **NOT APPLICABLE** — none supplied; correctly omitted |

---

## A7. Status

**VERIFIED.** The title page carries the researcher's confirmed name,
affiliation and email verbatim, satisfies every official FFA title-page
requirement that applies, and renders correctly in a clean 42-page build.
