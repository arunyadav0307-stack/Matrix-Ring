# Phase 17 / Task F — Visual review index

> **Arena has no vision capability and has not visually inspected any page.**
> Every statement below is derived from PDF **text extraction** and file
> inspection, not from looking at the rendered pages. **The researcher must
> perform the visual review.**

## Requested page index

| page | content | text-extraction evidence |
|---|---|---|
| **1** | Title + **Abstract** | begins "Quantum Error-Correcting Codes from Galois Hulls…"; contains "Abstract We construct $q$-ary quantum codes…" |
| **31** | **Methodology** (§8.5, certification methodology) | contains "Certification methodology Every distance reported in this paper is either exact or a proved lower bound…" |
| **33** | **Example 13** (`ex:certify`, rendered Example 8.12) | contains "Example 8.12 (certifying [[20, 2, 10; 18]]₄). Take the family (q, t, n) = (4, 1, 5)…" |
| **38–39** | **Appendix A** (Table A.1, the 28-code certification table; Table A.2 on p39) | p39 contains "Table A.1: All 28 certified codes (Part 6 of the Phase-7 log, verbatim)…"; p38–39 carry the A.1 header and continuation, p39 also carries Table A.2 |

Page numbers were verified in the **current (Phase 16) build**: 42 pages, and the
abstract, §8.5, Example 13 and Appendix A fall on the same pages as in the Phase
15 build (1, 31, 33, 38–39). The pagination did **not** shift.

## Files

| | path | files |
|---|---|---|
| **current** (Phase 16 build) | `PAPER/FINAL_RESEARCHER_REVIEW_V2/visual_review/` | 51 |
| archive (Phase 15 build) | `PAPER/FINAL_RESEARCHER_REVIEW_V2/visual_review_phase15/` | 51 |

Both are accessible; nothing was deleted.

### `visual_review/` (current — use this one)

* `pages/page-01.png … page-42.png` — all 42 pages at **150 dpi**.
* `key_pages/` — 8 pages at **300 dpi**:

| file | page |
|---|---|
| `01_title_and_abstract_p01.png` | 1 |
| `02_introduction_first_p03.png` | 3 |
| `03_certification_methodology_p31.png` | **31** |
| `04_example_13_ex_certify_p33.png` | **33** |
| `05_appendix_A_tables_p38.png` | **38** |
| `06_appendix_A_tables_p39.png` | **39** |
| `07_appendix_B_p40.png` | 40 |
| `08_references_p41.png` | 41 |

* `contact_sheet.png` — all 42 pages on one 7 × 6 grid, each tile labelled with
  its page number, for navigation.

## Important: why the current set was regenerated

The Phase 15 images were rendered from the **Phase 15** PDF. Phase 16 added the
11/17 split to §8.5 (p31) and to Appendix A (pp38–39), so those three pages
changed content even though pagination did not. The Phase 15 images are therefore
**stale on pages 31, 38 and 39** — they do not show the final wording.

Accordingly the set was re-rendered from the Phase 16 build, and the Phase 15 set
was preserved alongside as `visual_review_phase15/`. If you need to compare the
Phase 15 and Phase 16 wording visually, both sets are present; the Phase 15 PDF
itself is at `PAPER/PHASE15_WORKCOPY/build_modern/main.pdf`.

## What was verified programmatically (not visually)

* 42 page images exist and are non-empty (256–338 KB each at 150 dpi); 8 key
  pages at 300 dpi (542–721 KB each); contact sheet present.
* Page geometry: A4, 595.3 × 841.9 pt.
* The four indexed pages contain the expected text, confirmed by extraction.
* No empty or near-empty pages anywhere in the document.

## What was NOT done

No page was looked at. Fonts, spacing, line breaks, figure placement, table
alignment, hyphenation and overall typographic quality are **unverified** and
require your eyes. In particular, please check that:

* the Appendix A table on pp38–39 reads **Table A.1** / **Table A.2**
  (programmatically confirmed as text; visually unconfirmed);
* Example 13 on p33 reads "The support search (M2) is run only when M1 cannot
  finish…" (programmatically confirmed as text; visually unconfirmed);
* the added 11/17 sentences on p31 and pp38–39 did not introduce any layout
  overflow (the build reports **0 overfull and 0 underfull boxes**, which is
  strong evidence but not a visual check).
