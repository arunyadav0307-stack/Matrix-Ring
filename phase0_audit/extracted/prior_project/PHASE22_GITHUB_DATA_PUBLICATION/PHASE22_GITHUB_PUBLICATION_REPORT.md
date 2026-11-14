# Task F — GitHub publication report

## 1. Outcome

The curated `research-data/` directory was published to the existing public
GitHub repository's **`main`** branch.

| | |
|---|---|
| repository | `https://github.com/arunyadav0307-stack/Matrix-Ring` |
| visibility | **public** (unchanged) |
| default branch | `main` |
| **starting `main` commit** | `ea43e959e94b540041f94976615fec579392ceba` |
| **new `main` commit** | **`3752a6c0e921ab21a6f78877f154e7e959f4c418`** |
| push type | **fast-forward** (`ea43e95..3752a6c`), no force |
| commit subject | `Publish curated research data and reproducibility package` |
| files added | **88** (86 research data + `README.md` + `PUBLICATION_MANIFEST.sha256`) |
| files modified or deleted | **0** |

## 2. How the push was made

The instruction was to base the change on the latest `origin/main`, add only the
curated directory, and use normal fast-forward operations only.

1. `git fetch origin` — confirmed `origin/main` was still `ea43e959…` before
   starting.
2. A **detached** `git worktree` was created at `origin/main` in a temporary
   directory. This was done so that the session's checked-out branch was never
   switched: `arena/59de606f-matrix-ring` remained checked out throughout, and
   **no new named branch was created**.
3. Only `research-data/` was staged and committed in that worktree. The two
   files already present on `main` (`Matrix Ring.zip`, `README.md`) were left
   untouched — the status output showed **1 added path, 0 modifications, 0
   deletions**.
4. Pushed with `git push origin HEAD:main`. Git refuses non-fast-forward pushes
   by default, so the push succeeding is itself proof that it was a
   fast-forward.
5. The temporary worktree was removed.

**No force push was used. No branch was merged. No tag or release was created.**

### Incident note — recorded because it happened

While writing the first draft of this report file, an **unquoted** shell
here-document caused the backticks in the markdown to be interpreted as command
substitutions. Among the text executed was a stray
`git push origin HEAD:main`, issued from the session branch rather than from the
publication worktree.

**It was rejected by GitHub as non-fast-forward, so nothing was pushed.**
Verification immediately afterwards confirmed:

* `origin/main` still `3752a6c0e921ab21a6f78877f154e7e959f4c418` — unchanged;
* the session branch still `3753e59e…` — unchanged;
* `research-data/` still 88 files, manifest 87 OK / 0 FAILED — unchanged;
* the publication worktree at `/tmp/p22_main` still present and intact.

The affected file was rewritten with a properly quoted here-document. No
repository state was altered by the incident. It is recorded here rather than
quietly corrected, because the report should be complete.

## 3. What was deliberately NOT brought onto `main`

| not published | reason |
|---|---|
| the entire research branch | explicitly forbidden; would carry 21 phases of internal material |
| all phase directories and audit reports | internal audit history, not needed to reproduce the research |
| AI-declaration discussions and confirmation registers | explicitly forbidden; unpublished author matter |
| internal decision sheets and researcher decision reports | internal, personal |
| cover letter draft, submission checklist, highlights | pre-submission documents, not research data |
| manuscript sources and compiled PDFs | instructed not to modify manuscript files; none were |
| V1 / V2 / V3 reviewer packages | historical manuscript versions |
| Phase 21 private-data documents and the draft editorial email | internal, and the editorial email is unsent |
| the compilation toolchain | not research data |

**Verified after the push:** the only paths on `main` outside `research-data/`
are the two pre-existing files. 90 blobs total on `main` at this commit = 88
published + 2 pre-existing.

## 4. Licence status — unchanged

| | |
|---|---|
| `LICENSE` / `LICENCE` / `COPYING` file created | **No** |
| MIT, BSD, Apache or Creative Commons text added | **No** |
| licence applied to any file | **No** |
| third-party licence text copied into the repository | **No** |
| repository licence (GitHub API) | **`NONE`** — unchanged |

The published `research-data/README.md` states accurately that no licence has
been applied and that public availability does not by itself grant permission
to copy, modify or distribute the files.

## 5. Repository state after publication

| property | value |
|---|---|
| licence | `NONE` (unchanged) |
| visibility | public (unchanged) |
| default branch | `main` (unchanged) |
| releases | **0** |
| tags | **0** |
| branches | **2** — `main`, `arena/59de606f-matrix-ring` (unchanged) |
| `main` commit | `3752a6c0e921ab21a6f78877f154e7e959f4c418` |
| research branch commit | `3753e59…` (unchanged by the push) |

## 6. Commit-pinned location

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data
```

Commit-pinned, not floating: `3752a6c0e921ab21a6f78877f154e7e959f4c418` is
content-immutable, whereas a branch name can be repointed. Verified to resolve
with **HTTP 200** unauthenticated.

Repository path: `research-data/`
