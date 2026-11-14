# Task I — Preservation and validation report

## 1. The eight required verifications

| # | verification | result |
|---|---|---|
| 1 | All 86 intended data files are accounted for | ✅ **86/86** published, all present on `main`, all byte-identical to their originals |
| 2 | All published file hashes match | ✅ **88/88** match the remote byte-for-byte (git blob SHA-1 across the whole tree); `PUBLICATION_MANIFEST.sha256` 87 OK / 0 FAILED |
| 3 | No original research files were modified | ✅ **0 modifications** — `git diff` against the pre-publication commit shows only additions |
| 4 | No manuscript or theorem document was changed | ✅ **0 changes** to `PAPER/main.tex`, `PAPER/sections/`, `PAPER/references.bib`, or any reviewer package |
| 5 | No historical computational log was overwritten | ✅ **0 changes** to `PAPER/supplementary/` — the 23 logs are byte-identical, verified individually |
| 6 | No unrelated internal audit material was published | ✅ the only paths added to `main` are under `research-data/`; filename and content scans found no AI-declaration, decision-form or correspondence material |
| 7 | No licence was added | ✅ no `LICENSE`/`LICENCE`/`COPYING` file anywhere in `research-data/`; repository licence remains `NONE` |
| 8 | No Zenodo deposit was created | ✅ none; no DOI, no release, no tag |

**All eight pass.**

## 2. Protected-hash verification

**114 hashes** were recorded before any work in this phase, covering:

* the canonical manuscript (`PAPER/main.tex`, `references.bib`, `main.pdf`,
  `main.bbl`), all 12 section files;
* all 86 files of `PAPER/supplementary/` (22 scripts, 23 logs, 29 generator
  matrices, 8 parameter tables, 4 documents);
* both supplementary manifests;
* the V2 and V3 reviewer-package manifests;
* all four archive zips, including the Phase 22 bundle zip;
* the Phase 19 formatted manuscript and its PDF;
* the Phase 22 compiled PDF;
* the Phase 21 inventory.

After all work:

```
protected files recorded before : 114
protected files present now     : 114
MISSING                         : NONE
CHANGED                         : NONE

RESULT: *** ALL 114 PROTECTED HASHES HOLD ***
```

## 3. Files changed on the session branch

Exactly one commit, `3753e59`, containing **89 added paths, 0 modified, 0
deleted**:

* `research-data/` — 88 files (86 data + `README.md` +
  `PUBLICATION_MANIFEST.sha256`);
* `PHASE22_GITHUB_DATA_PUBLICATION/PHASE22_FINAL_DATA_INVENTORY.csv`.

That commit is purely additive. Nothing that existed before it was altered.

## 4. Files changed on `main`

Exactly one commit, `3752a6c`, containing **88 added paths, 0 modified, 0
deleted**:

* `research-data/` — 88 files.

The two files already on `main` (`Matrix Ring.zip`, `README.md`) are untouched.
`main` now holds 90 blobs: 88 published + 2 pre-existing.

## 5. Research branch — untouched by the push

The research branch `arena/59de606f-matrix-ring` remains at `3753e59…`. Nothing
was merged from it into `main`, and nothing was removed from it. All 21 phases
of audit material, all manuscript versions, all submission documents and the
Phase 21 private-data package remain exactly where they were.

## 6. Actions explicitly not taken

| not done | confirmed |
|---|---|
| Zenodo upload | ✅ none |
| DOI creation | ✅ none |
| GitHub release | ✅ 0 releases (GitHub API) |
| GitHub tag | ✅ 0 tags (GitHub API) |
| licence application | ✅ repository licence `NONE`, unchanged |
| repository visibility change | ✅ still public, unchanged |
| private author documents published | ✅ none |
| AI-declaration discussions published | ✅ none — content scan clean |
| research branch merged | ✅ not merged |
| canonical manuscript modified | ✅ not modified |
| submission to FFA | ✅ none |
| upload to Elsevier | ✅ none |
| force push | ✅ none; the only push was fast-forward |

## 7. Incident record

As described in `PHASE22_GITHUB_PUBLICATION_REPORT.md` §2, an unquoted shell
here-document while drafting that report caused a stray
`git push origin HEAD:main` to be issued from the session branch.

**It was rejected by GitHub as non-fast-forward, so nothing was pushed.**
`origin/main` was confirmed unchanged immediately afterwards, and the
publication worktree was found intact. The affected report file was rewritten.
No repository state was altered. Recorded here for completeness.

## 8. What remains outstanding

| # | item | status |
|---|---|---|
| 1 | Researcher approval of the proposed Data Availability Statement | ⏳ pending |
| 2 | Whether a commit-pinned public GitHub location satisfies FFA Option C | ⏳ not confirmed by the policy text |
| 3 | Licence decision for the research data | ⏳ deferred — repository remains `NONE` |
| 4 | Confirmation on the one third-party-derived file (`comparison_grassl_q9.csv`) | ⏳ flagged |
| 5 | Generative-AI declaration | ⏳ deferred at its existing status |
| 6 | The canonical manuscript still carries the superseded GitHub-link Data availability section (p. 37) and must be replaced before submission | ⏳ pending |
| 7 | Cover-letter author confirmations (originality, exclusive submission) | ⏳ pending |

Publishing the data removes the Phase 21 blocker on *availability*, but the
manuscript is **not** submission-ready: items 2, 5, 6 and 7 are unresolved.
