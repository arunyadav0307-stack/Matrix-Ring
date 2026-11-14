# Phase 13 / Task D — GitHub-only research-data access plan

**The researcher has chosen the existing public GitHub repository, and has
explicitly NOT authorised a Zenodo deposit. That decision is respected.**
No deposit, DOI, release, tag or licence has been created.

Date: 2026-11-10 · Verified against the live repository and the official
Elsevier policy on this date.

---

## D1. Repository inspection — current state (not assumed)

| property | value |
|---|---|
| Repository URL | `https://github.com/arunyadav0307-stack/Matrix-Ring` |
| Clone URL | `https://github.com/arunyadav0307-stack/Matrix-Ring.git` |
| Visibility | **public** |
| Archived | no |
| Licence | **NONE** |
| Default branch | `main` @ `ea43e959e94b540041f94976615fec579392ceba` |
| Research branch | `arena/59de606f-matrix-ring` @ `e41c5713fec5cce1d7cb51105f25d168dc05ebce` |
| Divergence | research branch **36 commits ahead**, 0 behind |
| Branch protection | **both branches unprotected** |
| Releases | **0** |
| Tags | **0** |

### Data inventory at the pinned commit `e41c571`

| path | files |
|---|---:|---|
| `PAPER/supplementary/scripts/` | 22 |
| `PAPER/supplementary/logs/` | 23 |
| `PAPER/supplementary/generator_matrices/` | 29 (28 + `INDEX.json`) |
| `PAPER/supplementary/parameter_tables/` | 8 |
| `PAPER/supplementary/` (root) | 4 (`README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, `MANIFEST.sha256`) |
| **total** | **86** |

`MANIFEST.sha256` carries **85** hash lines (86 files minus the manifest
itself).

### ⚠️ The critical accessibility problem — re-verified, still present

| check | result |
|---|---|
| `PAPER/supplementary/` on the **default branch `main`** | **404 — ABSENT** |
| `PAPER/supplementary/` on the **research branch** | **present** |

**A reader who opens `https://github.com/arunyadav0307-stack/Matrix-Ring`
lands on `main` and will not find the data at all.** The plain repository URL
is therefore **not** a usable data-access link.

This is the same defect Phase 12 identified; it has **not** changed.

---

## D2. Does GitHub alone satisfy FFA's policy?

### The official requirement (verified 2026-11-10)

FFA applies Elsevier research-data **Option C**, the strictest tier:

> "For this journal, **Option C** instructions from our research data
> guidelines apply. This means that you are **required** to:
> • Deposit your research data in a relevant data repository.
> • Provide a link to the dataset during the submission process.
> • If sharing your research data isn't possible, make a statement explaining
> why during the submission process. The statement will appear in your
> published article."

Elsevier's own research-data guidelines page confirms Option C is **required**,
not encouraged.

### Does the policy mandate a DOI?

**No.** The policy requires deposit in "a relevant data repository" and a link.
It does **not** state that a DOI is mandatory, and it does not name GitHub as
either acceptable or unacceptable.

I will not claim a DOI is required when the official policy does not say so.

### Assessment against the six evaluation criteria

| criterion | assessment |
|---|---|
| **1. Public accessibility** | **PARTIAL.** The data are public — but only on a non-default branch. The front door (`main`) leads nowhere. |
| **2. Stable commit permalink** | **YES, technically.** A commit SHA is content-immutable. |
| **3. Reproducibility** | **EXCELLENT.** 22 scripts, 23 logs, 85 manifest lines, three-method certification of 28 codes. |
| **4. Long-term accessibility** | **WEAK.** Both branches are unprotected; the branch can be deleted or force-pushed. GitHub is a commercial service with no preservation mandate. No DOI, no archive. |
| **5. Ownership and control** | **GOOD.** The researcher owns the repository. |
| **6. Release or tag required?** | **Not stated by Elsevier.** But a release or tag is strongly advisable: it creates a stable, citable, downloadable snapshot and is much harder to lose than a branch reference. **Creating one is NOT authorised and has not been done.** |

### Honest conclusion

> A public GitHub repository with a **commit-pinned** URL is a **defensible**
> but **materially weaker** route than a DOI-bearing archive. It satisfies the
> letter of Option C (data deposited somewhere public; link provided) but not
> its spirit (durable, citable, preservable).
>
> **The single largest obstacle is not the choice of GitHub — it is that the
> data are absent from `main`.** Until that is fixed, the repository cannot
> function as the data-access route at all.

---

## D3. Exact proposed GitHub data-access plan

### Proposed URL (commit-pinned, as the task requires)

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary
```

Commit-pinned, not floating — the SHA `e41c5713…05ebce` is content-immutable,
whereas a branch name can be repointed.

### Currently publicly accessible

| item | accessible at the pinned commit? |
|---|---|
| 22 scripts | **YES** |
| 23 logs | **YES** |
| 29 generator matrices | **YES** |
| 8 parameter tables | **YES** |
| 4 documentation files | **YES** |
| `MANIFEST.sha256` | **YES** |
| Everything, via the **default branch** | **NO — absent** |

### Files NOT reachable through the intended public link

**None of the 86 files are missing from the branch.** The problem is the entry
point, not the contents.

### Proposed data-availability statement — PENDING

> The research data supporting this article — the certified code parameters,
> generator matrices, computational scripts and execution logs — are publicly
> available at
> `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary`
> (86 files, certified by a SHA-256 manifest).

**This statement is NOT yet inserted as final**, because two material
limitations remain (see D4). It is drafted in the staging manuscript marked as
requiring confirmation.

### Reproduction instructions (already in the package)

1. Clone and check out the pinned commit:
   `git clone https://github.com/arunyadav0307-stack/Matrix-Ring.git`
   `git checkout e41c5713fec5cce1d7cb51105f25d168dc05ebce`
2. Read `PAPER/supplementary/README.md` and `ENVIRONMENT.md`.
3. Verify integrity: `sha256sum -c PAPER/supplementary/MANIFEST.sha256`.
4. Run the 22 scripts in the order given in `README.md`; outputs reproduce the
   23 logs.
5. Reproduce the certification per `CERTIFICATION_PROCEDURE.md`.
6. Rebuild the manuscript: `sh PAPER/compile/bootstrap_texlive.sh`, then
   `cd PAPER/FFA_SUBMISSION_STAGING && TL=/home/user/texlive2024 sh compile/build_modern.sh`.

### Remaining risks

| # | risk | severity | mitigation available (but NOT authorised) |
|---|---|---|---|
| R1 | Data absent from `main` — the front door fails | **HIGH** | merge the research branch into `main` |
| R2 | Branch unprotected — deletion or force-push would break the link | **MEDIUM-HIGH** | create a release or tag; enable branch protection |
| R3 | No DOI — not citable as a dataset | **MEDIUM** | Zenodo (excluded by the researcher) |
| R4 | No licence — default "all rights reserved" | **MEDIUM** | add a licence (see `PHASE13_GITHUB_LICENCE_RECOMMENDATION.md`) |
| R5 | No preservation mandate — GitHub is commercial | **LOW-MEDIUM** | release/tag + external archive |
| R6 | Commit-pinned URL is 100+ characters — error-prone if transcribed | **LOW** | release tag would shorten it |

---

## D4. Publication restriction — what has NOT been done

The researcher approved GitHub *instead of* Zenodo, but has **not** authorised
a new public data release. Accordingly, **none** of the following has been
done:

* ❌ no new supplementary files pushed to `main`
* ❌ no GitHub release created
* ❌ no public tag created
* ❌ no merge of the research branch into `main`
* ❌ no change to repository visibility
* ❌ no licence created or applied
* ❌ no upload to any external archive
* ❌ no Zenodo account, deposit or DOI

Only **read-only inspection** was performed (GitHub API and `git`/`gh` reads).

### Actions that would fix the HIGH-severity risk, awaiting authorization

| # | proposed action | effect |
|---|---|---|
| 1 | Merge `arena/59de606f-matrix-ring` into `main` | makes the data reachable from the repository's front door — **fixes R1** |
| 2 | Create a release/tag at `e41c571` | stable citable snapshot — **fixes R2**, and shortens the URL |
| 3 | Enable branch protection on `main` | guards against accidental deletion |
| 4 | Add a licence | removes the "all rights reserved" default — **fixes R4** |

**Prepared, not executed.** Awaiting explicit authorization for each.
