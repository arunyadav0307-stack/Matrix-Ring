# Task G — Public accessibility verification

Verification was performed **after** the push, against the remote repository,
using read-only methods. Every check below was made **without authentication**
where that was possible; the two that used the `gh` CLI are marked as such.

**Result: 10 of 10 checks pass. Public access is confirmed.**

Commit verified: `3752a6c0e921ab21a6f78877f154e7e959f4c418`

---

## 1. The ten required checks

| # | check | method | result |
|---|---|---|---|
| 1 | `research-data/README.md` publicly accessible | unauthenticated `curl` to the GitHub contents API | ✅ **HTTP 200**, 10,062 bytes, first line `# Research data and reproducibility package` |
| 2 | every selected file can be opened without authentication | unauthenticated recursive tree API + blob-SHA comparison of **all 88** files | ✅ **88/88 present, 0 mismatches** |
| 3 | the SHA-256 manifest is publicly accessible | unauthenticated download of `PUBLICATION_MANIFEST.sha256` | ✅ **HTTP 200**, downloaded content matches local byte-for-byte |
| 4 | the commit exists on `main` | `git fetch` + `git rev-parse origin/main` | ✅ `origin/main` = `3752a6c0e921ab21a6f78877f154e7e959f4c418` |
| 5 | the commit-pinned URL resolves | unauthenticated `curl` to the GitHub tree URL | ✅ **HTTP 200** |
| 6 | representative scripts download correctly | unauthenticated download of `matrix_ring_lib.py` and `phase7_extended_search.py` | ✅ both **HTTP 200** and byte-identical to local |
| 7 | representative computational logs download correctly | unauthenticated download of `phase7_extended_search_log.txt` | ✅ **HTTP 200**, byte-identical |
| 8 | generator matrices accessible | unauthenticated download of `INDEX.json` and `01_24_8_4_9_(9,1,6)_SO.json` | ✅ both **HTTP 200**, byte-identical |
| 9 | no accidental private files published | full remote tree listing + content scan of the published set | ✅ only `research-data/*` added; the only other paths on `main` are the two pre-existing files |
| 10 | all file hashes match the local publication set | git blob SHA-1 comparison of remote tree vs local files | ✅ **88/88 match, 0 missing, 0 mismatches** |

## 2. Method for check 2 and check 10

Rather than spot-checking, **every** published file was verified.

The GitHub git-trees API returns, for each blob, its git object SHA-1, which is
computed as `sha1("blob " + size + "\0" + content)`. The same value was computed
locally for each of the 88 files and compared:

```
blobs on main at that commit:              90
local files in research-data/:             88
local files MISSING on remote :            NONE
content MISMATCHES            :            NONE
files on main OUTSIDE research-data/:      ['Matrix Ring.zip', 'README.md']

RESULT: *** ALL 88 PUBLISHED FILES MATCH THE REMOTE BYTE-FOR-BYTE ***
```

90 = 88 published + the 2 files that were already on `main`. This is a
complete, content-addressed proof — not a sample.

## 3. Unauthenticated download test

Ten representative files were downloaded through the GitHub contents API with
**no `Authorization` header** and compared byte-for-byte with the local copies:

```
HTTP 200  MATCH  f8a67827810d  README (check 1)
HTTP 200  MATCH  d82f9c6d2225  publication manifest (check 3)
HTTP 200  MATCH  534389fc5128  representative script (check 6)
HTTP 200  MATCH  682e2a36801d  representative script (check 6)
HTTP 200  MATCH  3e1c8d1c368f  representative log (check 7)
HTTP 200  MATCH  5f1842dfb000  generator index (check 8)
HTTP 200  MATCH  79ef93ab2a41  generator matrix (check 8)
HTTP 200  MATCH  8b98d70ea611  certification table
HTTP 200  MATCH  02c1a8906f4a  verification procedure
HTTP 200  MATCH  f4f453581a08  package index

downloaded and matched: 10/10  (all without authentication)
```

## 4. Check 9 — scan for accidentally published private material

Two scans of the published set:

**Filename scan** for anything resembling internal material
(`phase1[0-9]`, `phase2[01]`, `audit`, `decision`, `declara`, `cover_letter`,
`checklist`, `confidential`, `internal`, `personal`). Six hits returned:

```
research-data/scripts/audit_pairing_equivalence.py
research-data/scripts/decision_support_checks.py
research-data/scripts/independent_audit_checks.py
research-data/logs/audit_pairing_equivalence_log.txt
research-data/logs/decision_support_log.txt
research-data/logs/independent_audit_log.txt
```

**All six were examined and cleared.** These are *scientific* audit scripts —
an independent re-implementation of the arithmetic used to test the main code
path, a check that the trace-valued and matrix-valued Galois pairings define the
same duality, and a decision-support check of what survives when the duality is
not reflexive. They are part of the computational evidence for the mathematics,
were in the Phase 21 approved 86-file inventory, and are described as such in
the published README. They are not internal audit reports, decision forms or
correspondence.

**Content scan** for `generative ai`, `ai-assisted`, `chatgpt`, `claude`,
`internal decision`, `cover letter`, `competing interest`, `orcid`:
**no hits**.

## 5. Commit-pinned URL

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data
```

* commit: `3752a6c0e921ab21a6f78877f154e7e959f4c418`
* repository path: `research-data/`
* parent: `ea43e959e94b540041f94976615fec579392ceba`
* commit date: 2026-11-10T10:13:44Z
* resolves: **HTTP 200**, unauthenticated

Commit-pinned rather than a floating branch reference, so the URL is
content-immutable.

## 6. Repository-level state (these used the authenticated `gh` CLI)

| property | value |
|---|---|
| licence | `NONE` |
| visibility | public |
| default branch | `main` |
| releases | **0** |
| tags | **0** |
| branches | **2** — `main`, `arena/59de606f-matrix-ring` |

## 7. Conclusion

**Public accessibility is verified.** Every one of the 88 published files is
reachable without authentication and matches the local publication set
byte-for-byte. No private, internal or AI-declaration material was published.

This verification is the precondition for the proposed Data Availability
Statement in `PHASE22_DATA_AVAILABILITY_STATEMENT.md`.
