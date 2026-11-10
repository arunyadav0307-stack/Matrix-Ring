# Task E — Special review of `comparison_grassl_q9.csv` (third-party data)

**Status: 🟠 TWO FINDINGS REQUIRING RESEARCHER ACTION.**
**File reviewed:** `research-data/quantum_code_records/comparison_grassl_q9.csv`
(published at commit `3752a6c0e921ab21a6f78877f154e7e959f4c418`)
**SHA-256:** `6898cbb907c4e6f3b0a62c40de22ff4834249d944a3a027bbfc73937a7f33dbc`
(agrees with `research-data/PUBLICATION_MANIFEST.sha256` and with
`PHASE23_SUPPLEMENTARY_FILE_DESCRIPTIONS.csv`)
**Size:** 197 bytes
**Reviewed: 2026-11-10.**

---

## E1. What the file contains

Three data rows, quoted in full:

| our_code | route | best_known | bounds_lower_upper | gap | log_line |
|---|---|---|---|---|---|
| `[[24,8,4]]_9` | SO | `[[24,8]]_9` | `6..8` | `2 below` | *(empty)* |
| `[[24,12,3]]_9` | DC | `[[24,12]]_9` | `5..6` | `2 below` | *(empty)* |
| `[[16,8,3]]_9` | DC | `[[16,8]]_9` | `4..4` | `1 below` | *(empty)* |

Two structural signals confirm these rows are external, not computed:

* the `log_line` column is **empty** for all three — the q = 4 comparison file
  (`comparison_grassl_q4.csv`) carries log lines 660–671, because those values
  came from this project's own run log;
* the project README states plainly that these three rows are "external
  third-party data … read verbatim from codetables.de on 2026-11-04 … the only
  external data in the paper and the only such data in this package."

**That characterisation is accurate, and the file is the only third-party
content in the deposited package.** The other 85 files are this project's own
scripts, logs, matrices, tables and documentation.

## E2. Provenance — verified

| item | status |
|---|---|
| Source named | ✅ codetables.de (Markus Grassl) |
| Retrieval date recorded | ✅ 2026-11-04, in the README, the supplementary README, `appendix_tables.tex` and `references.bib` |
| Cited in the manuscript | ✅ as `\cite{GrasslCodetables}`, reference [5]; used in §9, §10, Table A.2 and Appendix B |
| Values used consistently | ✅ all three rows appear identically in the manuscript's comparison table (§9) and in Table A.2 |
| Label-convention hazard documented | ✅ the site prints the **prime** p in `[[N,K]]_p` while the construction block says "over GF(p²)", so q = 9 appears as `[[N,K]]_3`. This is recorded in `references.bib` and in the Table A.2 caption. An earlier phase misread it and wrongly concluded q = 9 was not covered; that error is recorded as an erratum in §9. |

## E3. Values re-verified live against the source — all three correct

Each of the three rows was re-fetched from codetables.de on **2026-11-10** and
compared with the file:

| row | query | live lower..upper | in file | |
|---|---|---|---|---|
| 1 | `QECC.php?q=9&n=24&k=8` | **6 .. 8** | `6..8` | ✅ |
| 2 | `QECC.php?q=9&n=24&k=12` | **5 .. 6** | `5..6` | ✅ |
| 3 | `QECC.php?q=9&n=16&k=8` | **4 .. 4** | `4..4` | ✅ |

**All three values are verbatim correct.** The source page reports "Last change:
10.06.2024", matching the note in `references.bib`, so the values have not moved
since retrieval.

## E4. Finding 1 — redistribution permission is NOT established

| question | answer |
|---|---|
| Is the source under a known open licence? | ❌ **No.** No licence statement was found on the codetables.de home page or on its "How to cite" page. |
| Is redistribution permitted? | ❌ **Not established.** The "How to cite" page (<http://www.codetables.de/citation.php>) gives a citation format and nothing about reuse or redistribution. |
| Is copyright asserted? | ✅ **Yes.** The table pages carry "Copyright © Markus Grassl (codes@codetables.de)". |
| Is there a contact address for permission? | ✅ **Yes** — `codes@codetables.de`, given on the home page. |

**Assessment.** Three rows of bounds, quoted with attribution and a retrieval
date, is a *de minimis* quotation of factual data and would ordinarily be
unobjectionable. But the file is being **published in a public data deposit**,
not merely quoted in a paper, and the source asserts copyright without granting
a reuse licence. The safest course costs almost nothing.

**Options for the researcher (decision required):**

1. **Keep the file**, with the existing provenance. Defensible as a minimal
   factual quotation with attribution. Small residual risk.
2. **Keep the file, and email `codes@codetables.de`** to confirm that quoting
   three bound pairs with attribution in a public data deposit is acceptable.
   Cheap, and removes the doubt. *(The agent has not sent this and will not
   without authorisation.)*
3. **Remove the file from the deposit** and restate the three bound pairs in the
   manuscript text with the citation, which is a quotation in the article rather
   than a redistribution in a data package. Lowest risk; the science is
   unaffected in either case.
4. **Keep the file but mark it explicitly** as third-party, with the copyright
   notice and the source URL carried in the file itself.

**Recommendation: option 2 (ask) or option 3 (remove and restate).** Option 3 is
the conservative choice and loses nothing, since the values are already in the
manuscript as Table A.2 with full attribution.

## E5. Finding 2 — a manuscript claim about entanglement-assisted tables is inaccurate as worded

**This is the more consequential finding, and it concerns the manuscript, not
the deposit.**

### What the manuscript says

`sections/09_comparison.tex`:

> "**The tables cover stabilizer codes only.** There is no
> entanglement-assisted table: the corresponding endpoint returns HTTP 404.
> Every entanglement-assisted code of this paper is therefore
> *unbenchmarked*."

`research-data/README.md` repeats it: "No entanglement-assisted table exists
(the corresponding endpoint returned HTTP 404)."

### What is actually the case

An entanglement-assisted table **does exist**, and did so before the
2026-11-04 retrieval date:

* URL: <https://eaqecc.codetables.de/>
* Title: "Bounds on the minimum distance of entanglement-assisted quantum codes"
* Lists `[[n, k, d_lower-d_upper; c]]_q` — exactly the format this paper needs
* Tables: **qubit** (q = 2) and **qutrit** (q = 3)
* **Last change: 2025-07-10** — i.e. live and predating the retrieval
* It is **linked from the codetables.de home page** under "Entanglement-Assisted
  Quantum Error-Correcting Codes"
* Backed by Luo–Ezerman–Grassl–Ling, *Quantum Information Processing* 23:4
  (2024), DOI 10.1007/s11128-023-04211-x

### Why the substantive conclusion survives

The EA table covers **q = 2 and q = 3 only**. Every entanglement-assisted code
in this paper is over **q = 4, q = 8 or q = 9**. So the operative conclusion —
that this paper's entanglement-assisted codes are unbenchmarked — **remains
correct**. What is wrong is the stated *reason*.

### Why it matters

The current wording asserts a fact that is false and checkable in one click. A
referee working in quantum codes will very likely know of the EA tables, and
"the endpoint returns HTTP 404" will read as a failure to look. That is a cheap
own goal on an otherwise careful comparison section, and it sits in the one
section of the paper where the author's care is most on display.

### Suggested replacement wording (DRAFT — NOT APPLIED)

> "**The entanglement-assisted tables cover q = 2 and q = 3 only.** Bounds on
> entanglement-assisted codes are tabulated at eaqecc.codetables.de for qubits
> and qutrits. Every entanglement-assisted code of this paper is over q = 4,
> q = 8 or q = 9, none of which is tabulated; all of them are therefore
> *unbenchmarked*. This is a substantial blind spot, since the
> entanglement-assisted route is where the largest distances of this paper
> occur."

**This change has NOT been made.** Task G restricts `FFA_FINAL_SUBMISSION_V2`
to the data-availability change alone, and this sentence is a substantive
statement about prior work, not a data-availability matter. It is submitted to
the researcher as a decision.

**Whether the same correction should flow to any other copy of the manuscript
is likewise the researcher's call.**

## E6. Summary

| | |
|---|---|
| File identified as the only third-party content in the package | ✅ |
| Provenance recorded and cited | ✅ |
| All three values re-verified live against the source | ✅ **3/3 correct** |
| Values consistent with the manuscript | ✅ |
| Redistribution permission established | ❌ **No** — decision required |
| Manuscript's EA-table claim accurate | ❌ **No** — decision required; conclusion survives, wording does not |

**Neither finding alters a theorem, a proof, a generator matrix, a quantum
parameter, a distance certificate or any mathematical conclusion.** Finding 2
concerns a sentence of factual framing in the comparison section; the
comparison itself, and every number in it, stands.
