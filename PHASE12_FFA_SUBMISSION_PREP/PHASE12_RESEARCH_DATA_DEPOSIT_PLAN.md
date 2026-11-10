# Phase 12 / Task F — Research-data deposit plan

**STATUS: PREPARED, NOT EXECUTED.** No deposit has been created, no DOI
assigned, no licence applied. Each requires explicit researcher
authorization.

## 1. What FFA requires (Option C, verified 2026-11-10)

> "Deposit your research data in a relevant data repository. Provide a link to
> the dataset during the submission process. If sharing your research data
> isn't possible, make a statement explaining why during the submission
> process. The statement will appear in your published article."

The fallback does **not** apply: the data are plainly depositable.

## 2. Current repository state — verified

| check | result |
|---|---|
| Repository | `arunyadav0307-stack/Matrix-Ring` |
| Visibility | **public** |
| Licence | **NONE** |
| Releases | **0** |
| Tags | **0** |
| Default branch | `main` @ `ea43e959` (2026-11-04) |
| Working branch | `arena/59de606f-matrix-ring` @ `a731ac7` (2026-11-10) |
| Divergence | session branch **35 commits ahead**, 0 behind |
| `PAPER/supplementary/` on `main` | **ABSENT** |
| `PAPER/supplementary/` on session branch | present |

## 3. Does the repository satisfy Option C as it stands?

**No.**

| requirement | status | reason |
|---|---|---|
| Data exist and are reproducible | **SATISFIED** | 86 files, 85 manifest lines |
| Publicly accessible | **PARTIAL** | branch is public but **mutable**; can be deleted or force-pushed |
| Persistent identifier | **NOT SATISFIED** | no DOI; no release; no tag |
| Stable, citable snapshot | **NOT SATISFIED** | `main` lacks the data entirely |
| Licence | **NOT SATISFIED** | repository declares none |

A Git branch is **not** a data repository in the sense Option C requires: it
has no persistent identifier and its contents can change.

## 4. Recommendation: a DOI-based archive (route R2)

### R1 — GitHub release → Zenodo

* Tag a release on the session branch; the GitHub–Zenodo integration archives
  it and mints a DOI.
* Advantage: minimal effort; data already version-controlled.
* Disadvantage: archives the **whole repository**, including Phases 0–12 audit
  and working documents not intended for publication.

### R2 — direct Zenodo upload — **RECOMMENDED**

* Build a clean bundle from `PAPER/supplementary/` and upload it to Zenodo
  directly with chosen metadata.
* Advantage: **full control over scope**; only research data is published.
* Disadvantage: slightly more work; the bundle must be assembled.

### R3 — institutional or domain repository

* Viable if the researcher's institution provides persistent identifiers.

## 5. Proposed deposit contents (route R2)

Bundle root: `matrix-ring-quantum-codes-supplementary/`

| path | files | description |
|---|---|---|
| `generator_matrices/` | 29 (28 + INDEX) | certified generator matrices as JSON |
| `parameter_tables/` | 8 | CSV tables incl. `certified_codes.csv` |
| `scripts/` | 22 | every script that produced a number in the paper |
| `logs/` | 23 | execution records |
| `README.md` | 1 | reproduction instructions |
| `ENVIRONMENT.md` | 1 | software environment |
| `CERTIFICATION_PROCEDURE.md` | 1 | how the 28 codes were certified |
| `MANIFEST.sha256` | 1 | 85 hash lines |
| **total** | **86** | |

**Note:** no archive may contain its own SHA-256 or size. The manifest will be
computed over the *contents*, not over the bundle file.

## 6. Proposed metadata (for the researcher to correct)

| field | proposed value |
|---|---|
| Title | Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings — supplementary data and code |
| Authors | *[follows from the confirmed author metadata — PENDING]* |
| Description | (draft in §9) |
| Licence | **TO BE CHOSEN** — CC BY 4.0 or CC0 |
| Version | 1.0.0 |
| Keywords | cyclic codes; matrix rings; Galois hulls; quantum error-correcting codes; finite rings |

## 7. Proposed licence — the researcher must choose

| option | effect |
|---|---|
| **CC BY 4.0** | others may reuse with attribution — the common default for research data |
| **CC0** | public domain dedication; maximal reuse, no attribution required |
| other | any licence the researcher or their institution requires |

**No licence was applied by default.** This is a legal decision.

## 8. Deposit checklist (to be executed only on authorization)

1. Confirm author metadata (name, affiliation, ORCID) — **currently PENDING**.
2. Choose the licence — **currently PENDING**.
3. Confirm scope: `PAPER/supplementary/` only (recommended).
4. Assemble the bundle.
5. Compute `MANIFEST.sha256` over the bundle **contents** (not the bundle file).
6. Write `README.md` with reproduction instructions.
7. Confirm Zenodo metadata (title, authors, description, licence, keywords).
8. **Request explicit authorization.**
9. Upload to Zenodo → obtain the DOI.
10. Insert the DOI into the data-availability statement.
11. Rebuild the manuscript with the final statement.
12. Verify the DOI resolves before submission.

## 9. Draft description

> Supplementary data and code for "Quantum Error-Correcting Codes from Galois
> Hulls of Cyclic Codes over Noncommutative Matrix Rings". The deposit
> contains the generator matrices of 28 certified quantum codes, the parameter
> tables reported in the article, the 22 scripts that produced every numerical
> result, the execution logs, and a SHA-256 manifest. Codes are right ideals of
> `R[X]/⟨X^n−1⟩` with `R = M_2(F_q[u]/⟨u^t⟩)`; quantum codes are obtained from
> Galois hulls via three routes (twisted stabilizer, Euclidean/CSS, and
> entanglement-assisted). Every numerical claim in the article is reproducible
> from these files by running the scripts in the order given in `README.md`.

## 10. Two repository issues the researcher should decide on

1. **`main` does not contain the supplementary data.** If the repository URL
   is to be cited anywhere, the session branch should be merged to `main`
   first. This changes the repository's default presentation, so it is the
   researcher's decision.
2. **No repository licence.** Without one, the repository is "all rights
   reserved" by default — incompatible with the intent of a data deposit.

## 11. Status

**PENDING — REQUIRES AUTHORIZATION.** Nothing has been published, deposited,
tagged, released, licensed, or assigned a DOI.
