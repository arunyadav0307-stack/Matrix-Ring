# Phase 13 / Task E — Licence recommendation

**STATUS: RECOMMENDATION ONLY. No licence has been selected or applied.**

The researcher asked for a recommendation before choosing. Nothing in this
document has been executed: no `LICENSE` file was created, no licence applied
to any file, no repository metadata changed.

Date: 2026-11-10

---

## E0. Why this cannot be a single licence

The repository holds **six materially different classes** of content, and they
do not all licence the same way. Applying one licence to everything would be
simple but wrong.

| class | what it is | how it licences |
|---|---|---|
| **Source code** | 22 Python scripts | Software licence (MIT / BSD / Apache) — Creative Commons licences are **not appropriate** for code |
| **Mathematical documentation** | `README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, the manuscript itself | CC BY 4.0 or CC0 — attribution-style licence |
| **Generator matrices** | 29 JSON files — *computational output*, but also arguably *data* | CC BY 4.0 or CC0 |
| **Computational output / logs** | 23 logs, 8 CSV tables | CC BY 4.0 or CC0 (facts and data are generally not copyrightable, but the arrangement may be) |
| **Bibliographic material** | 13 references in `references.bib` | **Metadata about third-party works — not ours to licence** |
| **Third-party material** | any content derived from cited papers | **NOT ours — must not be relicensed** |

---

## E1. Software and computational scripts (22 files)

### Options compared

| licence | reuse | attribution | patent grant | notes |
|---|---|---|---|---|
| **MIT** | Permissive: use, copy, modify, merge, publish, distribute, sublicense, sell | Must include the copyright notice and licence text | **No express patent grant** | Shortest and most widely used in research code. Maximum reuse with minimal friction. |
| **BSD 2-Clause** | Same as MIT, effectively | Must retain notice | **No** | Nearly identical to MIT in effect; slightly different wording. |
| **BSD 3-Clause** | Same | Must retain notice; **no endorsement clause** — you may not use the authors' names to endorse derivatives | **No** | Adds the non-endorsement protection MIT lacks. |
| **Apache 2.0** | Same | Must retain notice **and** state changes; must include NOTICE if present | **YES — express patent grant from contributors** | Longest and most legalistic, but the only one here with explicit patent protection. |

### Practical research-reproducibility implications

* **MIT** — lowest friction. Anyone can rerun, fork, or incorporate the scripts
  into a larger codebase with almost no conditions. Best for reproducibility,
  because it removes every barrier except attribution.
* **Apache 2.0** — best if there is **any** chance the methods are patented or
  commercialised. It also requires modified files to be marked, which
  materially helps reproducibility (a reader can tell whether the script they
  have is the original).
* **BSD 3-Clause** — a middle option if you want to prevent anyone implying
  your endorsement of their derivative work.

### Dependency compatibility

The scripts are self-contained Python (the environment is recorded in
`PAPER/supplementary/ENVIRONMENT.md`). MIT, BSD and Apache 2.0 are all
permissive and mutually compatible for this purpose; none imposes copyleft that
could conflict with anything here.

---

## E2. Documentation and research data

| licence | reuse | attribution | notes |
|---|---|---|---|
| **CC BY 4.0** | Unrestricted reuse, including commercial, including modification | **Attribution required** — credit the author, link the licence, indicate changes | The academic default. Maximises reuse while ensuring the work is credited. |
| **CC0 1.0** | Public-domain dedication — anyone may use it for anything | **None required** | Maximum freedom; you give up attribution. Irrevocable — you cannot later demand credit. |
| **Alternative** | — | — | If the content includes third-party material that cannot be relicensed, that specific material must be **excluded** or separately attributed; CC BY/CC0 cannot be applied to it. |

### The distinction that matters

| material | what is actually protectable |
|---|---|
| **Source code** | The *expression* is copyrightable. Needs a software licence. |
| **Mathematical documentation** | The exposition is copyrightable; **the mathematics itself is not** — mathematical truths are not subject to copyright. |
| **Generator matrices** | These are **facts/outputs**, arguably not copyrightable at all. A licence here operates as a *statement of intent* about reuse rather than a grant of rights. |
| **Computational output / logs** | Same — largely factual, minimally protectable. |
| **Bibliographic material** | **Not ours.** A reference list is metadata about others' works. Do not apply a licence to it. |
| **Third-party material** | **Not ours.** Any figure, table or text derived from a cited paper remains the property of that publisher; it may be present only under fair use/quotation, and cannot be relicensed. |

⚠️ **Important:** applying CC BY or CC0 to generator matrices and logs does not
"create" copyright where none exists. It signals reuse intent. This is normal
and harmless practice, but it should be understood rather than assumed.

---

## E3. Recommendation

### Preferred (dual licence)

| class | licence | applies to |
|---|---|---|
| **Source code** | **MIT** | 22 files in `PAPER/supplementary/scripts/` |
| **Documentation, data, matrices, logs** | **CC BY 4.0** | `README.md`, `ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, `MANIFEST.sha256`, 29 generator matrices, 23 logs, 8 parameter tables |
| **Bibliography / third-party** | **no licence applied** | `PAPER/references.bib`, and any content derived from cited works |

**Why MIT for code:** maximum reuse with only an attribution condition, which
is exactly what reproducibility needs. The scripts' whole purpose is to be run
and checked by others.

**Why CC BY 4.0 for data:** the academic default for research data. It lets
anyone reuse the matrices and tables while guaranteeing the work is credited —
which matters when the data underpins a journal article.

### Alternative (if maximum freedom is preferred)

| class | licence |
|---|---|
| Source code | **BSD 3-Clause** (adds non-endorsement) **or Apache 2.0** (adds patent grant) |
| Data and documentation | **CC0 1.0** |

Choose **Apache 2.0** over MIT if there is any prospect of patenting or
commercialising the constructions. Choose **CC0** over CC BY if you do not care
about attribution — but note it is **irrevocable**.

### Practical advantages of the recommendation

* Removes the current default of **"all rights reserved"** — at present the
  repository declares no licence, so legally nobody may reuse anything in it.
* Satisfies the intent of Elsevier's Option C (make data available and
  reusable).
* Standard, machine-readable, recognised by GitHub.

### Obligations and limitations

| obligation | detail |
|---|---|
| MIT | Anyone reusing the code must retain the copyright notice and licence text |
| CC BY 4.0 | Anyone reusing the data must credit you, link the licence, and indicate if they changed it |
| Neither | Neither licence prevents commercial reuse; neither is copyleft, so downstream work need not be open |
| Both | Once applied and published, **revocation is not practical** — choose deliberately |

### Files each licence would apply to — exact list

**MIT** (22): everything under `PAPER/supplementary/scripts/`.

**CC BY 4.0** (64): `PAPER/supplementary/README.md`,
`ENVIRONMENT.md`, `CERTIFICATION_PROCEDURE.md`, `MANIFEST.sha256`;
all 29 under `generator_matrices/`; all 23 under `logs/`; all 8 under
`parameter_tables/`.

**No licence** (2+): `PAPER/references.bib`; any third-party-derived content.

**Separate consideration:** the manuscript `main.tex` and the 12 section files.
If you publish the article **subscription** (no APC) with Elsevier, you
normally transfer or licence copyright to the publisher, so **do not apply a
licence to the manuscript source** without checking your publishing agreement.
Recommended: leave the manuscript **unlicensed** in the repository, or add a
README note that the manuscript is © the author and licensed to Elsevier upon
publication.

### Copyright and third-party-content issues to inspect

1. **`PAPER/references.bib`** — bibliographic metadata about others' works.
   Not licensable by you.
2. **`00_BLUEPRINT/Research_Blueprint.pdf`** — supplied by the researcher;
   confirm you own it before applying any repository-wide licence.
3. **Any table or figure reproduced from a cited paper** — the manuscript has
   0 figures, but verify the 6 tables are your own output before licensing.
4. **The `Matrix Ring.zip` file** — origin unknown from the record; inspect
   before licensing.
5. **Third-party code dependencies** — check `ENVIRONMENT.md`; if any script
   vendors third-party code, its licence travels with it.

---

## E4. Status

**PENDING — researcher's choice.** Three decisions:

1. Which software licence for the 22 scripts (recommendation: **MIT**).
2. Which licence for data and documentation (recommendation: **CC BY 4.0**).
3. Whether to licence the manuscript source at all (recommendation: **no**).

**Nothing has been applied.** No `LICENSE` file created; no repository metadata
changed.
