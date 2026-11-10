# Task A — Publication eligibility report

Every candidate file was inspected individually. No file was published merely
because it existed in the working tree.

**Result: 86 files eligible and published · 4 artefacts excluded · 0 files
withheld as "needs review".**

---

## 1. Method

1. The Phase 21 inventory (`PHASE21_PRIVATE_DATA_INVENTORY.csv`, 86 rows) was
   used as the authoritative starting point, as instructed.
2. Every one of those 86 files was then re-hashed and re-inspected
   independently — the inventory was not trusted blindly.
3. The working tree was scanned separately for artefacts that are **not** in
   the inventory (`__pycache__`, `.pyc`, editor temporaries, dotfiles).
4. Every file was scanned for credential-like content.
5. Each file was then classified **Eligible / Excluded / Needs review**.

## 2. Scans performed and their results

| scan | result |
|---|---|
| `__pycache__` directories in the source tree | **1 found** → excluded |
| `.pyc` files | **3 found** → excluded |
| editor temporaries (`*~`, `*.swp`, `*.tmp`, `*.bak`) | **0** |
| dotfiles / `.env` / environment files | **0** |
| credentials, tokens, passwords, API keys, private keys | **0** — regex scan for `api[_-]?key`, `secret`, `token`, `password`, `passwd`, `BEGIN RSA/OPENSSH/PRIVATE`, `ghp_`, `github_pat_`, `AKIA…`, `Bearer ` across all 86 files |
| third-party material | **1 file flagged** — see §4 |
| private author information | **0** — the only personal data in the package is the corresponding-author name, affiliation and email, which appear in the manuscript itself and are required for correspondence |
| AI-declaration discussions | **0** — none of the 86 files mentions generative AI |
| internal decision forms / correspondence | **0** |

## 3. The 4 excluded artefacts

These were never part of the 86-file package. They are Python bytecode caches
created locally when the scripts were run in this workspace; they are untracked
in git and are pure build artefacts.

| artefact | reason |
|---|---|
| `PAPER/supplementary/scripts/__pycache__/` (directory) | build artefact |
| `…/phase7_extended_search.cpython-311.pyc` | build artefact |
| `…/ring_structure_checks.cpython-311.pyc` | build artefact |
| `…/phase2_stage2c_galois_duality.cpython-311.pyc` | build artefact |

They are recorded as **Excluded** rows in
`PHASE22_FINAL_DATA_INVENTORY.csv` — which is why that CSV has **90 rows for
86 published files**.

## 4. Third-party material — one file, flagged and resolved

**File:** `parameter_tables/comparison_grassl_q9.csv`
**Destination:** `research-data/quantum_code_records/comparison_grassl_q9.csv`

**What it actually is** — inspected, not assumed. Four lines including the
header, i.e. **three data rows**:

```
our_code,route,best_known,bounds_lower_upper,gap,log_line
"[[24,8,4]]_9",SO,"[[24,8]]_9",6..8,2 below,
"[[24,12,3]]_9",DC,"[[24,12]]_9",5..6,2 below,
"[[16,8,3]]_9",DC,"[[16,8]]_9",4..4,1 below,
```

**Classification: Eligible (third-party-derived)** — with the following
reasoning recorded, so the researcher can overrule it.

Points in favour of inclusion:

1. **The content is numerical fact, not copyrightable expression.** Three rows
   of published bounds on code minimum distances. Facts are not protected by
   copyright in any jurisdiction; the amount taken is de minimis.
2. **No new exposure is created.** The file is **already publicly visible** in
   this same public repository — it is at
   `PAPER/supplementary/parameter_tables/comparison_grassl_q9.csv` on the public
   research branch `arena/59de606f-matrix-ring`. Publishing it under
   `research-data/` on `main` discloses nothing that is not already public in
   the same repository.
3. **Provenance and attribution are preserved.** The file is cited in the
   manuscript as reference [5] (Grassl, codetables.de), and the published README
   states the retrieval date (2026-11-04) and that the page changes.

Points that argue for caution, recorded honestly:

1. The values originate from a third-party website (codetables.de), not from
   this computation.
2. No licence from that source has been obtained.

**Conclusion.** Included, with provenance, citation and a retrieval date stated
in the README. If the researcher prefers, this single file can be removed and
the three rows restated in the manuscript text alone. **Flagged for the
researcher's decision.**

By contrast, `comparison_grassl_q4.csv` is **not** third-party: those values are
derived from this project's own run log (Part 8).

## 5. Files with unclear ownership or redistribution rights

**None.** No file in the package originates from anyone other than the author,
except the single file discussed in §4, whose content is de minimis factual data
already public in this repository.

## 6. What was deliberately NOT published

The instruction was explicit and was followed: only the curated 86-file
`research-data/` directory was added to `main`.

Not published — **all** of the following remain only on the research branch:

* the 21 phase directories and their internal audit reports;
* the AI-declaration discussions and confirmation registers;
* the internal decision sheets and researcher decision reports;
* the cover letter draft, submission checklist and highlights;
* the manuscript sources and compiled PDFs;
* the V1 / V2 / V3 reviewer packages;
* the Phase 21 private-data documents and the draft editorial email;
* the compilation toolchain.

Verified after the fact: the only paths on `main` outside `research-data/` are
the two files that were already there (`Matrix Ring.zip` and `README.md`).
