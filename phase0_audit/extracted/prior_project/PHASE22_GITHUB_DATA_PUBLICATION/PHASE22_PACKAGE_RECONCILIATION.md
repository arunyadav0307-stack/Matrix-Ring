# Task B — Package reconciliation

## 1. The three counts, explained

Earlier phases recorded the package variously as **86**, **90** and **85**
files. All three numbers are correct; they count different things. This section
reconciles them explicitly so the discrepancy is not repeated.

| figure | what it counts | how it arises |
|---:|---|---|
| **85** | **hash lines in the original package manifest** | `PAPER/supplementary/MANIFEST.sha256` contains 85 lines. It is a *manifest*, and a manifest does not list itself. |
| **86** | **actual files in the package** | 85 manifest lines **+ the manifest file itself** = 86. Confirmed independently: `git ls-files PAPER/supplementary` returns 86, and a directory walk returns 86. |
| **90** | **rows in `PHASE22_FINAL_DATA_INVENTORY.csv`** | 86 eligible files **+ 4 excluded build artefacts** (1 `__pycache__` directory + 3 `.pyc` files) that were found in the working tree, inspected, and deliberately not published. |

So: **86 = 85 + 1 (the manifest)**, and **90 = 86 + 4 (excluded artefacts)**.
There is no contradiction; the numbers were never counting the same set.

A fourth figure appears after publication:

| figure | what it counts |
|---:|---|
| **88** | **files in `research-data/` as published** = 86 data files + `README.md` + `PUBLICATION_MANIFEST.sha256` |
| **87** | **entries in `PUBLICATION_MANIFEST.sha256`** = the 88 files minus the manifest itself (it excludes itself, as it must) |

## 2. Reconciliation of the five inputs

| # | input | result |
|---|---|---|
| 1 | Phase 21 inventory | 86 rows, 22 scripts / 23 logs / 29 generator matrices / 8 parameter tables / 4 documentation |
| 2 | Existing supplementary package (`PAPER/supplementary/`) | 86 files on disk, 89 counting untracked `.pyc` artefacts; 86 tracked by git |
| 3 | Original 85-entry manifest | re-verified: **85/85 OK** when run from the package root |
| 4 | Additional required research-data files | none identified beyond the 86; two new files were *created* (`README.md`, `PUBLICATION_MANIFEST.sha256`) |
| 5 | Final curated publication set | **86 data files**, all byte-identical to the originals |

All five agree. No file was added from outside the verified package, and none
was dropped.

## 3. Counts of the published set

| measure | count |
|---|---:|
| **actual files** (data) | **86** |
| **actual files** (as published, incl. README and publication manifest) | **88** |
| **directories** | **7** subdirectories (`scripts`, `logs`, `generator_matrices`, `quantum_code_records`, `distance_certificates`, `verification_procedures`, `documentation`) plus the package root |
| **scripts** | **22** `.py` |
| **logs** | **23** `.txt` |
| **generator matrices** | **29** (28 codes + `INDEX.json`) |
| **CSV records** | **8** (7 in `quantum_code_records/` + 1 in `distance_certificates/`) |
| **JSON records** | **29** (all in `generator_matrices/`) |
| **CSV + JSON records total** | **37** |
| **documentation files** | **4** (2 in `documentation/`, 2 in `verification_procedures/`) as published; plus the new package `README.md` |
| **manifests** | **2** — `PUBLICATION_MANIFEST.sha256` (87 entries, all OK) and the preserved `documentation/MANIFEST.sha256` (85 entries) |

Group totals: 22 + 23 + 29 + 7 + 1 + 2 + 2 = **86** ✔

## 4. Independent SHA-256 manifest

A **fresh** manifest was created for the final publication set —
`research-data/PUBLICATION_MANIFEST.sha256`.

* generated independently, not copied from the package manifest;
* **87 entries** (it excludes itself);
* verified from the package root: **87 OK, 0 FAILED**.

The preserved original manifest, `research-data/documentation/MANIFEST.sha256`
(85 entries), reflects the **pre-publication** relative layout. Because 11 files
were relocated into `quantum_code_records/`, `distance_certificates/`,
`verification_procedures/` and `documentation/`, **74 of its 85 entries verify
in place**; the other 11 verify against the same content at its new path. Every
relocated file is byte-identical — only its path changed. This is documented in
the published README, and `PUBLICATION_MANIFEST.sha256` is given as the
authoritative check.

## 5. Pre-publication hash verification

Before anything was pushed, each of the 86 files was checked two ways:

1. **SHA-256 match** against the independently recomputed hash in the
   publication inventory;
2. **byte-for-byte comparison** against its original under
   `PAPER/supplementary/`.

```
eligible entries in inventory:                 86
published files verified against originals:    86
problems:                                     NONE
>>> ALL 86 PUBLISHED FILES BYTE-IDENTICAL TO ORIGINALS
```
