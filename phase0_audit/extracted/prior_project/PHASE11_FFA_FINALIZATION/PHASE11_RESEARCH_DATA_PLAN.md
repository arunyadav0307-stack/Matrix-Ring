# Phase 11 / Task C2 — Research data plan (FFA Option C)

**Status: RESEARCHER CONFIRMATION REQUIRED. NOTHING HAS BEEN DEPOSITED.**

No repository deposit has been made, no DOI has been created, and no licence
has been applied. Nothing in this plan may be executed without explicit
authorization.

## 1. What FFA requires (verified 2026-11-10)

*Finite Fields and Their Applications* applies Elsevier research-data
**Option C**, which is the most demanding of Elsevier's options:

| requirement | detail |
|---|---|
| Deposit | Authors **must** deposit the research data in a relevant data repository. |
| Link at submission | The link to the deposited data **must be provided at the submission step**. |
| Fallback | If deposition is genuinely impossible, authors **must** submit a statement explaining why; that statement is **published** with the article. |
| Availability statement | Standard statements are available from Elsevier's research-data page. |

The fallback is narrow. "The data are in the paper" is **not** an accepted
justification under Option C when the data are, in fact, depositable.

## 2. What data this project actually has

The manuscript's results are **computational as well as theoretical**, so
there is real data to deposit. `PAPER/supplementary/` contains **86 files**:

| content | count | notes |
|---|---|---|
| JSON result files | 28 | the certified code parameters |
| CSV tables | 8 | includes `certified_codes.csv` |
| Scripts | 24 | generate every number in the paper |
| Logs | 24 | execution records |
| Documentation | 4 | index and descriptions |

`PAPER/supplementary/MANIFEST.sha256` carries **85** hash lines covering the
package. Every numerical claim in the manuscript is reproducible from these
files.

**Assessment: the data are fully depositable.** No justification for
non-deposition exists, so the Option C fallback statement should not be used.

## 3. What is currently missing

| requirement | status |
|---|---|
| Public repository with a persistent identifier | **NOT DONE** |
| DOI | **NOT DONE** — and none may be invented |
| Licence | **NOT DONE** — requires an explicit choice; do not apply one by default |
| Availability statement in the manuscript | **NOT DONE** — the staging copy carries a placeholder marked as requiring confirmation |
| Supplementary captions | **NOT DONE** — Option: FFA requires a concise caption **per file** |

## 4. Routes available — for the researcher to choose

Three routes were identified. **None has been executed.** All require a
deliberate act by the researcher because each has an irreversible or public
consequence.

### Route A — GitHub release → Zenodo (recommended)

The repository `arunyadav0307-stack/Matrix-Ring` is **public** (verified
2026-11-10 via the GitHub API). GitHub integrates with Zenodo: creating a
**release** triggers a Zenodo deposit that receives a **DOI**.

* Advantages: DOI satisfies the persistent-identifier requirement; the
  supplementary package is already version-controlled; the release can be
  scoped to the `PAPER/supplementary/` content.
* Consequences the researcher must accept: the deposit is **public and
  permanent**; a DOI is minted; the released snapshot is fixed.
* Required steps: tag a release → enable Zenodo archiving for the repository →
  Zenodo mints a DOI → cite the DOI in the data-availability statement.

### Route B — direct Zenodo upload

Upload the supplementary package to Zenodo directly, with chosen metadata and
licence.

* Advantages: independent of GitHub; full control over what is deposited; can
  deposit only `PAPER/supplementary/` and not the whole repository.
* Consequences: public, permanent, DOI minted.
* Recommended if the researcher does **not** wish the entire repository
  archived.

### Route C — institutional or domain repository

Deposit in the researcher's institutional repository or a coding-theory data
repository, if one is available and issues persistent identifiers.

## 5. Decision points requiring the researcher

1. **Which route** (A, B or C)?
2. **Licence** — CC BY 4.0? CC0? Something else? **This is a legal choice and
   must not be made by default.**
3. **Scope** — the whole repository, or only `PAPER/supplementary/`?
   Recommendation: **only the supplementary package**, because the repository
   contains audit and working documents not intended for publication.
4. **Embargo** — none needed, but confirm.
5. **Authorize the deposit explicitly.** The agent will not create a release,
   a deposit, or a DOI without this.
6. **Confirm the wording** of the data-availability statement, which must
   quote the actual link.

## 6. Draft availability statement — PENDING A REAL LINK

Once a DOI exists, the statement should read approximately:

> The research data supporting this article — the certified code parameters,
> the generation scripts and the execution logs — are deposited at
> [REPOSITORY NAME] under [DOI / LINK].

**This statement cannot be finalized until the deposit exists.** Submitting it
with a placeholder link would be a false statement.

## 7. Interaction with supplementary material

FFA treats **supplementary material** separately from research data, and both
are relevant here:

* Supplementary material must be **cited in the text**, submitted **together
  with** the manuscript, and each file given a **concise caption**. It is
  published **exactly as received** and **cannot be added later except at
  revision**.
* The current manuscript's appendices hold the parameter tables, so it must be
  decided what is **supplementary** rather than **in-article**. That is a
  researcher decision, not an agent decision.
* A per-file caption list must be prepared for whatever is submitted as
  supplementary. **Not yet done.**

## 8. Status summary

| item | status |
|---|---|
| Data identified and reproducible | VERIFIED |
| Data depositable (fallback not applicable) | VERIFIED |
| Deposit created | **NOT DONE — requires authorization** |
| DOI | **NOT DONE — none may be invented** |
| Licence chosen | **NOT DONE** |
| Availability statement | **NOT DONE** |
| Per-file supplementary captions | **NOT DONE** |
