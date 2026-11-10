# Data availability statement

**STATUS: PENDING — cannot be finalized until a deposit exists with a
persistent identifier.**

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
