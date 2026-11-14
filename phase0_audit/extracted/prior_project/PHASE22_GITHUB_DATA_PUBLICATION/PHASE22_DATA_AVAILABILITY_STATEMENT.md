# Task H — Proposed Data Availability Statement

> # 🟡 READY FOR RESEARCHER APPROVAL
>
> This statement is **proposed only**. It has **not** been inserted into the
> canonical manuscript, and nothing has been submitted.
>
> The public accessibility it refers to **has been verified** — see
> `PHASE22_PUBLIC_ACCESS_VERIFICATION.md`. What it does **not** settle is
> whether this arrangement satisfies *Finite Fields and Their Applications*
> Option C. That question remains open; see §6.

---

## 1. Exact proposed statement

> The computational scripts, execution logs, generator matrices, parameter
> tables and certification documentation supporting this study are publicly
> available in the project repository at
> `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data`
> (86 files, verified by a SHA-256 manifest).

### Shorter alternative

> The research data supporting this study are publicly available at
> `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data`.

The longer form is recommended: it names what is actually there, so a reader
knows whether the package is what they need before following the link.

## 2. Exact repository URL

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data
```

## 3. Exact commit SHA

```
3752a6c0e921ab21a6f78877f154e7e959f4c418
```

* parent commit: `ea43e959e94b540041f94976615fec579392ceba`
* commit date: 2026-11-10T10:13:44Z
* commit subject: `Publish curated research data and reproducibility package`
* files added: 88 (86 research data + `README.md` + `PUBLICATION_MANIFEST.sha256`)
* files modified or deleted: 0

**The URL is commit-pinned, not a floating branch reference.** The SHA is
content-immutable; a branch name can be repointed. This matters because the
statement will be published with the article and must keep resolving.

## 4. What the supplementary package contains

| folder | files | contents |
|---|---:|---|
| `scripts/` | 22 | computation scripts — pure Python standard library, no third-party packages |
| `logs/` | 23 | the execution records every computed number in the paper is read from |
| `generator_matrices/` | 29 | one generator matrix per certified code (28) plus `INDEX.json` |
| `quantum_code_records/` | 7 | machine-readable parameter tables (Pareto frontier, entanglement budget, family census and scan, hull witnesses, best-known comparisons) |
| `distance_certificates/` | 1 | `certified_codes.csv` — the 28-code certification table with per-method results and log-line provenance |
| `verification_procedures/` | 2 | `CERTIFICATION_PROCEDURE.md` (what "certified" means and how to re-certify) and `ENVIRONMENT.md` (interpreter, platform, resources) |
| `documentation/` | 2 | the package index and the pre-publication manifest |
| `README.md` | 1 | purpose, folder-to-manuscript map, which script reproduces which result, how to verify and how to run, and the certification-method distribution |
| `PUBLICATION_MANIFEST.sha256` | 1 | SHA-256 of the 86 data files plus `README.md` (87 entries) |

**Total: 86 research-data files.** Integrity check:
`sha256sum -c PUBLICATION_MANIFEST.sha256` → 87 OK, 0 FAILED.

## 5. Confirmation that the referenced files are publicly accessible

Confirmed by read-only verification against the remote repository, without
authentication (full detail in `PHASE22_PUBLIC_ACCESS_VERIFICATION.md`):

* the commit-pinned URL resolves — **HTTP 200** unauthenticated;
* **all 88** published files are present on `main` and match the local copies
  **byte-for-byte** (compared by git blob SHA-1 across the whole tree, not
  sampled);
* ten representative files — README, manifest, two scripts, the principal log,
  the generator index, a generator matrix, the certification table, the
  verification procedure and the package index — were **downloaded with no
  authentication** and matched byte-for-byte, **10/10**;
* no private, internal, AI-declaration or audit material was published; the only
  paths on `main` outside `research-data/` are the two files that were already
  there before this work.

## 6. What this statement does NOT settle — the Option C question

The researcher's position has changed since Phase 21: the data are now public
rather than available only on private request. That removes the largest Phase 21
blocker, but **not** all of them.

**What is now satisfied.** FFA Option C requires authors to deposit research
data in a relevant data repository and to provide a link to the dataset during
the submission process. There is now a public, persistent, commit-pinned
location containing the data, and a link to it. That is a materially stronger
position than "available on request".

**What remains open — stated honestly.**

| open point | why |
|---|---|
| **Is GitHub a "relevant data repository" under Option C?** | The policy does not name GitHub as either acceptable or unacceptable. It requires "a relevant data repository" and a link; it does not mandate a DOI. A commit-pinned public GitHub location is defensible on that wording, but it is not confirmed by the policy text. |
| **Durability.** | Both branches are unprotected and the repository is a commercial service with no preservation mandate. A commit SHA is content-immutable but the branch can be deleted or force-pushed. A release or tag would be stronger — **not created, not authorised**. |
| **No DOI.** | Not required by the wording, but the data are not independently citable as a dataset. **Not created, not authorised.** |
| **No licence.** | The repository licence is `NONE`, i.e. all rights reserved by default. Readers can view the data; reuse permission is not granted. **No licence was applied, as instructed — but this should be a conscious decision, not an accident.** |
| **The third-party file.** | `quantum_code_records/comparison_grassl_q9.csv` contains three rows of bounds read from codetables.de on 2026-11-04. Included with provenance and citation; flagged for the researcher's confirmation. |

**Recommendation.** The statement above can be used, but the researcher should
first decide whether to (a) use it as it stands, (b) ask the editorial office to
confirm that a commit-pinned public GitHub location is acceptable for Option C,
or (c) authorise a release/tag or a DOI-bearing deposit for extra durability.
None of (b) or (c) has been done.

## 7. Status

| | |
|---|---|
| Public accessibility | ✅ **VERIFIED** (Task G) |
| Statement prepared | ✅ **YES** |
| Inserted into the canonical manuscript | ❌ **NO** — not authorised by this task |
| Submitted | ❌ **NO** |
| Option C compliance | 🟡 **Not confirmed** — defensible on the wording, unconfirmed by the policy text |

**READY FOR RESEARCHER APPROVAL.**
