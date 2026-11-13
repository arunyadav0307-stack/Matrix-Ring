# Data availability statement

**STATUS: PENDING — researcher has chosen GitHub-only; two material
limitations remain before the statement can be final.**

**Update 2026-11-10 (Phase 13):** the researcher has elected to use the
existing public GitHub repository **instead of** a Zenodo deposit. That
decision is respected; no Zenodo deposit, DOI, release or tag has been created.

Proposed commit-pinned URL:

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary
```

Two limitations keep this PENDING:

1. **The supplementary data are absent from the repository's default branch
   `main`** (verified 404). A reader opening the repository landing page will
   not find the data.
2. **Both branches are unprotected**, so long-term availability is not
   assured.

Note that Elsevier's Option C does **not** explicitly mandate a DOI — it
requires deposit in "a relevant data repository" plus a link. GitHub is
therefore defensible, but the two limitations above are real.

See `PHASE13_GITHUB_RESEARCH_DATA_ACCESS_PLAN.md`.

---

## Historical record (Phase 12 status — superseded)

## Official FFA requirement (Option C, verified 2026-11-10)

> "For this journal, **Option C** instructions from our research data
> guidelines apply. This means that you are **required** to:
> • Deposit your research data in a relevant data repository.
> • Provide a link to the dataset during the submission process.
> • If sharing your research data isn't possible, make a statement explaining
> why during the submission process. The statement will appear in your
> published article."

## Why this statement is still pending

The research data exist and are reproducible — 86 files under
`PAPER/supplementary/`, covered by 85 SHA-256 manifest lines. But:

| requirement | status |
|---|---|
| Deposit in a data repository | **NOT DONE** — no authorization given |
| Persistent identifier (DOI) | **NONE EXISTS** — none may be invented |
| Licence | **NOT CHOSEN** — a legal decision for the researcher |
| Public accessibility verified | **PARTIAL** — a GitHub *branch* is public but mutable and carries no DOI |

Because the data are plainly depositable, the fallback ("sharing isn't
possible") **does not apply** and must not be used.

## Proposed statement — to be completed once a DOI exists

> The research data supporting this article — the certified code parameters,
> the generator matrices, the computational scripts and the execution logs —
> are deposited at [REPOSITORY NAME] under [DOI/LINK].

**This cannot be submitted with a placeholder link.** Doing so would be a
false statement, published in the article.

## Recommended route

Direct Zenodo upload of the `PAPER/supplementary/` bundle (route R2 in
`PHASE12_RESEARCH_DATA_DEPOSIT_PLAN.md`), because the repository as a whole
contains audit and working documents not intended for publication.

## What is needed from the researcher

1. Authorization to create the deposit (explicit).
2. Choice of licence (CC BY 4.0 / CC0 / other).
3. Confirmation of scope: `PAPER/supplementary/` only (recommended).
4. Confirmation of the final statement wording once the DOI is minted.
