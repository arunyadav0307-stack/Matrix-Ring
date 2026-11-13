# Task B — Data Availability Statement

**Status: PROPOSED — FFA POLICY CONFIRMATION PENDING**
**Applied to:** `PAPER/FFA_FINAL_SUBMISSION_V2/` (the new authoritative staging
copy) **only**. The canonical manuscript, the V2 and V3 reviewer packages and
the Phase 19 FFA copy are **untouched**.

---

## B1. The problem that was corrected

The Phase 19 manuscript carried a Data availability section pointing at

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/e41c5713fec5cce1d7cb51105f25d168dc05ebce/PAPER/supplementary
```

That link is **withdrawn and wrong on two counts**: it points at the old
`PAPER/supplementary/` path rather than the curated `research-data/` directory,
and it points at a commit on the research branch, not at the published commit
on `main`. It has been replaced.

## B2. The exact statement now in the staging copy

> **Data availability**
>
> [*PROPOSED — FFA POLICY CONFIRMATION PENDING.*] *Finite Fields and Their
> Applications* applies Elsevier research-data **Option C**, under which authors
> are required to deposit their research data in a relevant data repository and
> to provide a link to the dataset during the submission process.
>
> The computational scripts, verification logs, generator matrices, quantum-code
> records, distance certificates, verification procedures and supporting
> documentation used in this study are publicly available in the
> *research-data* directory of the project's GitHub repository at
>
> `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data`
>
> which is pinned to an immutable commit and comprises 86 files: 22
> computational scripts, 23 execution logs, 29 generator matrices, 8 tables of
> quantum-code records and distance certificates, and 4 documentation and
> verification files, each verified by a SHA-256 manifest. A description of
> every file and instructions for reproducing the computations are given in the
> `README.md` at that location.
>
> *Status: PROPOSED — FFA POLICY CONFIRMATION PENDING.* The location is public
> and has been verified to be accessible without authentication. Whether a
> commit-pinned public repository satisfies Option C is not established by the
> official policy text, which does not name GitHub as either an acceptable or an
> unacceptable repository; the matter has been referred for editorial
> confirmation. The repository carries no licence, so public availability does
> not by itself grant permission to reuse the materials.

## B3. Every stated material category — verified present

The task requires that no stated category be claimed unless the files exist.
Each was checked against the published directory at the pinned commit:

| category claimed in the statement | present? | count | where |
|---|---|---:|---|
| computational scripts | ✅ | **22** | `scripts/` |
| verification logs (execution logs) | ✅ | **23** | `logs/` |
| generator matrices | ✅ | **29** (28 codes + `INDEX.json`) | `generator_matrices/` |
| quantum-code records | ✅ | **7** | `quantum_code_records/` |
| distance certificates | ✅ | **1** (`certified_codes.csv`) | `distance_certificates/` |
| verification procedures | ✅ | **1** (`CERTIFICATION_PROCEDURE.md`) | `verification_procedures/` |
| supporting documentation | ✅ | **3** (`ENVIRONMENT.md`, `SUPPLEMENTARY_PACKAGE_README.md`, `MANIFEST.sha256`) | `verification_procedures/`, `documentation/` |
| **total** | ✅ | **86** | |

**No category is claimed that is not present, and no file is claimed to be
available that is not.** The counts in the statement (22 / 23 / 29 / 8 / 4) were
recomputed this phase and match the published directory exactly.

## B4. The link itself

| | |
|---|---|
| URL | `https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data` |
| commit | `3752a6c0e921ab21a6f78877f154e7e959f4c418` |
| branch | `main` (default) |
| immutability | commit-pinned, not a floating branch reference |
| resolves | ✅ **HTTP 200**, unauthenticated |
| files accessible | ✅ **87/87** manifest entries downloaded without authentication |

## B5. Does the statement satisfy the exact FFA requirement?

**No — not demonstrably.** It satisfies the *form* of Option C's first branch
(deposit + link), but:

* the policy does not establish that GitHub is a "relevant data repository";
* there is no DOI and no preservation commitment;
* there is no licence, so "availability" means viewable, not reusable.

Hence the marker **PROPOSED — FFA POLICY CONFIRMATION PENDING**, which appears
both in the manuscript section and in this document. The question has been put
to the editorial office in the draft email at
`PHASE23_FFA_OPTION_C_COMPLIANCE.md` (Appendix E). **That email has not been
sent.**

## B6. What this phase did and did not do

| | |
|---|---|
| Replaced the outdated link | ✅ in `PAPER/FFA_FINAL_SUBMISSION_V2/` only |
| Preserved the canonical manuscript | ✅ untouched |
| Preserved V2 / V3 reviewer packages | ✅ untouched |
| Preserved the Phase 19 FFA copy | ✅ untouched |
| Inserted the statement as final | ❌ **No** — it is marked PROPOSED |
| Submitted anything | ❌ **No** |

## B7. Verification in the compiled PDF

The staging copy was compiled and the rendered text checked:

| check | result |
|---|---|
| new commit hash `3752a6c0` present in PDF | ✅ |
| old commit hash `e41c571` present in PDF | ❌ correctly **absent** |
| `/research-data` path present | ✅ |
| "FFA POLICY CONFIRMATION PENDING" marker present | ✅ |
| PDF | 42 pages, 580,019 bytes, SHA-256 `d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1` |

## B8. Awaiting

1. Researcher approval of the wording.
2. Editorial confirmation that the commit-pinned GitHub location satisfies
   Option C — **or** authorisation of a DOI-bearing deposit / release.
3. Only then should the marker be removed and the statement treated as final.
