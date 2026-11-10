# Phase 8A / Phase 8B — Final validation report

**Phase 8A, 2026-11-09.** The manuscript is compiled; six transcription defects
fixed; two environment caveats left open.

**Phase 8B, 2026-11-10.** Both caveats closed: the manuscript has been rebuilt
on a current TeX Live with genuine BibTeX. **Status: every check passes; the
build is clean and reproducible from committed sources.**

This file is the record of *what was checked and what it returned*. §0 is
Phase 8B; §§1–7 are the Phase 8A record, kept as written on 2026-11-09. The
corrections are listed in `CHANGELOG.md` and, for Phase 8B, entry by entry in
`compile/BUILD_CORRECTIONS.md`; the issues themselves are classified in
`MANUSCRIPT_SELF_AUDIT.md`.

---

## 0. Phase 8B — modern compilation (2026-11-10)

### 0.1 The two Phase 8A caveats are closed

| Phase 8A caveat | Phase 8B status |
|---|---|
| Built only with a 2010-vintage pdfTeX 1.40.11 | **Closed.** Rebuilt with pdfTeX **1.40.26**, TeX Live 2024. |
| `bibtex` replaced by pybtex | **Closed.** Rebuilt with genuine **BibTeX 0.99d**, `plain.bst`. |

The 2010 engine and the pybtex `.bbl` are preserved untouched as Phase 8A
provenance (`compile/build.sh`, `compile/fetch_texlive.sh`,
`compile/README.md`, `tools/make_bbl.py`, `PAPER/main.bbl`).

### 0.2 Headline

| | |
|---|---|
| Modern compilation | **success** — 39 pages, A4 595 × 842 pt |
| TeX Live | **2024** (`release-texlive.txt`, TinyTeX-based tree) |
| pdfTeX | **3.141592653-2.6-1.40.26** |
| BibTeX | **0.99d (TeX Live 2024)** |
| kpathsea | 6.3.6/dev (`kpsewhich`, built from source) |
| Host | Linux 6.1.158 x86_64, gcc 12.2.0, CPython 3.11.2 |
| Errors | **0** |
| Undefined references | **0** |
| Undefined citations | **0** |
| Missing glyphs | **0** |
| Overfull boxes | **0** |
| Underfull boxes | **0** (Phase 8A: 4) |
| Warnings of any kind | **0** |
| Static validator | **13 PASS / 0 FAIL** |
| Log analysis (`check_log.py`) | **clean** |
| Example re-derivation | **56 checks / 0 mismatches** |
| PDF inspection | **0 issues** (geometry, overlap, fonts, glyphs) |
| Corrections needed to build | **5** (C-1…C-5), none mathematical |
| Phase 0–7 files altered | **0 of 94** (byte-verified) |
| Phase 8 / 8A archives altered | **no** — both published SHA-256s still verify |
| Final PDF | 563 659 B, 39 pages |
| Final PDF SHA-256 | `69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd` |
| Rebuild reproducibility | **byte-identical** across repeated runs |
| Modern-build package | `MatrixRingManuscript_20261110_Phase8B.zip`, 44 entries, 696 599 B, SHA-256 `468ab3861f2cf345a4d46eb34eda867cba859dc79d5201b359d967de122cbb1f` |

### 0.3 The three kinds of evidence, kept separate

**Static validation (source-level, no build).** `tools/validate_latex.py`
reads the `.tex` files.

```
checks: 13 ; PASS 13 ; FAIL 0
  V1   every \input resolves ................ PASS   13 files
  V2   braces balanced ...................... PASS   13 files
  V3a  every egin has a matching \end ...... PASS
  V3b  every environment is provided ......... PASS
  V4   every 
ef/\eqref has a \label ........ PASS   246 refs, 107 labels
  V5   no duplicate \label ................... PASS   107 labels unique
  V6   every \cite key has an entry .......... PASS   32 citations, 13 entries
  V7   no entry is uncited ................... PASS   13 entries all cited
  V8   no DO-NOT-CITE key is cited ........... PASS
  V9   every control sequence is defined ..... PASS   422 distinct macros
  V10  verbatim blocks carry no macros ....... PASS
  V11  no invented author metadata ........... PASS   only \AUTHORPLACEHOLDER
  V12  math delimiters balanced .............. PASS
```

**Modern compilation (what the 2024 engine actually reported).**
`tools/check_log.py` on `build_modern/main.log`: 0 errors, 0 missing
characters, 0 overfull, 0 underfull, 0 package/LaTeX warnings. `bibtex`
reported `The style file: plain.bst`, 13 entries, 0 warnings. The full
per-line record of every change made to reach this state is
`compile/BUILD_CORRECTIONS.md`.

**Visual inspection.** The PDF was inspected by measurement, not by eye, with
`tools/inspect_pdf.py` (§0.6).

### 0.4 The five corrections

Phase 8B needed five corrections. **None of them changes a mathematical
statement or a numerical result.** Four of the five are defects that the 2010
engine and the pybtex `.bbl` had *silently swallowed* — the modern build found
real pre-existing faults in the released Phase 8A PDF.

| # | defect | where | manifest in the 8A PDF |
|---|---|---|---|
| C-1 | `\AUTHORPLACEHOLDER` used at line 39, defined at line 68 | `main.tex` | build failed (hard error) |
| C-2 | `\Hom` **never defined**, used twice | `main.tex`, §3, §4 | the word "Hom" was **silently dropped** from two sentences |
| C-3 | unbraced `]]` in an optional argument | `08_certification.tex:324` | heading read "Example 8.12 (certifying [[20, 2, 10; 18). ]4]" |
| C-4 | TS1 `cm-super` fonts absent | distribution | build failed: `Font tcrm1095 at 600 not found` |
| C-5 | empty PDF `/Title`; 4 hyperref PDF-string warnings | `main.tex` | `/Title` empty, 4 warnings |

C-2 and C-3 are the important ones: **the Phase 8A PDF was wrong on the page
in two places and the Phase 8A log did not say so.** A log-only check is not
sufficient for this manuscript.

The build is **byte-reproducible**: `build_modern.sh` pins
`SOURCE_DATE_EPOCH`, because pdfTeX stamps `/CreationDate` and `/ModDate` from
the clock and derives the trailer `/ID` from them. Three consecutive builds
returned the same SHA-256, so the value quoted above is checkable rather than
merely recorded.

### 0.5 Reproducing the tool chain

The sandbox is wiped between sessions, so the tool chain has to be
reconstructible from committed sources rather than left on disk.
`compile/bootstrap_texlive.sh` (~40 s, network needed once) rebuilds the whole
tree and verifies every artefact by SHA-256; `compile/build_modern.sh` runs the
four passes. Full instructions and the provenance of each component are in
`compile/README_BUILD.md`.

Getting a current distribution was the gating step. CTAN and tug.org are not
reachable from this environment, so `install-tl`/`tlmgr` were impossible; the
tree was assembled from a PyPI wheel bundling a real TeX Live 2024 release, an
npm TeX Live 2015 texmf for the version-stable files, a GitHub blob for
`booktabs.sty`, and `tex-mirror/tex-live` for `kpathsea` and `bibtex.web`.
`bibtex` is compiled from the TeX Live 2024 Pascal source with `tangle` and
`web2c` — deliberately, because substituting pybtex again is exactly what
Phase 8B forbids.

### 0.5b Clean rebuild from the shipped package

The package was unpacked into an empty directory, a **fresh** TeX Live 2024
tree was bootstrapped from the packaged script, and the manuscript was rebuilt
from `sources/` into a separate output directory — nothing from the original
build was reused.

| check | result |
|---|---|
| `MANIFEST.sha256` of the unpacked archive | **43 files verified, 0 bad** |
| bootstrap from the packaged script | pdfTeX 1.40.26, BibTeX 0.99d |
| four-pass build from `sources/` | 0 errors, 0 warnings, 39 pages |
| rebuilt PDF SHA-256 | `%s` |
| shipped PDF SHA-256 | `%s` |
| verdict | **byte-identical** |

The evidence file is `verification/clean_rebuild.txt` inside the package. It
necessarily records the package as it was before that file was added, so the
archive's own hash is in its sidecar.

### 0.6 Visual inspection (by measurement)

`tools/inspect_pdf.py` — 0 issues.

| check | result |
|---|---|
| page geometry | 595 × 842 pt (A4) on all 39 pages; **0** ink outside an 8 pt bleed |
| overlapping text | **0** meaningful overlaps (maths glyph stacking excluded) |
| fonts | 29 distinct fonts, **all Type 1 and all embedded** |
| unresolved glyphs | **0** pages contain U+FFFD |
| numbered environments | 83, all present: 21 Theorems, 11 Lemmas, 9 Propositions, 2 Corollaries, 8 Definitions, 19 Remarks, **13 Examples**, 0 Conjectures |
| quantum-code tuples | 28 distinct `[[n,k,d;c]]` and 11 distinct `[[n,k,d]]` — **identical sets** to Phase 8A |
| bibliography | 13 entries rendered, all cited |
| landmarks | title, abstract, key words, contents, references all present |
| tables | 1–6 all rendered; column starts consistent |
| figures | none (the manuscript is text and mathematics only) |

**All 13 worked examples were compared sentence by sentence against the Phase
8A PDF.** All 13 are present and agree; the only differences are the two
corrections above. Example 7.11 (`ex:fpbasis`, the `F_p`-basis subtlety — the
example flagged for special attention) is complete and correct.

**Comparison with the Phase 8A PDF.** Both are **39 pages**: no page-count
delta. Text was compared after folding presentation ligatures (pdfTeX 1.40.11
wrote `fi` as the single glyph U+FB01, 1.40.26 writes two characters). Every
remaining difference is one of:

1. the two corrections C-2 (`Hom` restored ×2) and C-3 (Example 8.12 heading);
2. pagination: three short passages moved one page (§8, §9);
3. **the bibliography no longer prints DOIs** — see §0.7.

A 63-occurrence `ϕ`/`φ` difference is **extraction-only, not visual**: the two
glyphs sit at identical coordinates with identical advance widths, and the
rendered pixels of the glyph are **byte-identical** at 1200 dpi.

### 0.7 One open editorial decision: DOIs in the bibliography

The Phase 8A PDF printed `doi:10.1016/…` after nine of the thirteen references.
That was **not** `plain.bst` behaviour: it was an artefact of the pybtex
substitute, which appends a `\href{…}{doi:…}` block. Genuine BibTeX with
`plain.bst` — the style `main.tex` requests — prints no DOI, and
`FINAL_VALIDATION_REPORT.md` §5 already recorded on 2026-11-09 that "the
`plain` style prints no DOI".

The modern build therefore **drops 9 DOIs** that appeared in the 8A PDF. This
is a content difference, and it is the only one that removes information.

It was left as-is rather than silently changed, because fixing it means
departing from the declared bibliography style, which is the author's call:

* **Keep as now (recommended for the declared style).** `plain` is what
  `main.tex` asks for, and the DOIs are absent by design.
* **Restore the DOIs.** Switch to a DOI-aware style (e.g. `plainurl` from
  `urlbst`, or `natbib` + `plainnat`), which keeps `plain` ordering and adds
  the DOI. This needs one new `.bst` and a one-line change to `main.tex`.

The remaining difference in the reference list is typographic only: genuine
`plain.bst` sets the author names on the same line as the number and sets
journal titles in italic, where pybtex broke the line and used `\emph`. Both
are correct `plain` style; the modern rendering is the canonical one.

### 0.8 Repository safeguards

* 94 protected Phase 0–7 files: **0 altered** (hashed before and after).
* Phase 8 archive `MatrixRingManuscript_20261109.zip`,
  `d1ba4c821b1af01b8105eff702315957e692cfcaed21d5491a8ea03e4b29a80d`,
  543 086 B — verifies against its sidecar.
* Phase 8A archive `MatrixRingManuscript_20261109_Phase8A.zip`,
  `14ecac0e8649009ef535f63bc128734335c88ac3c1bbc6ef4e05a5a868342910`,
  1 096 851 B — verifies against its sidecar.
* Phase 8A `main.pdf` (`b2ba1fee72b6e70ae18f3f043c10ac3390673281e1d0ccd35da3f863d8641a03`)
  and its provenance (`compile/build.sh`, `compile/fetch_texlive.sh`,
  `compile/texenv.sh`, `compile/README.md`) are byte-identical. One file,
  `compile/build.sh`, was inadvertently overwritten early in Phase 8B and was
  restored from the Phase 8A commit before the Phase 8B commit was made; the
  Phase 8B script is `compile/build_modern.sh`.
* No historical log overwritten. The build scratch directory
  `PAPER/build_modern/` is generated and is not tracked.
* Corrections are recorded append-only in `compile/BUILD_CORRECTIONS.md`.

---

## 1. Headline

| | |
|---|---|
| The manuscript compiles | **yes** — `main.pdf`, 39 pages, A4 |
| Errors | **0** |
| Missing glyphs | **0** |
| Undefined references | **0** |
| Undefined citations | **0** |
| Overfull boxes | **0** (were 27, worst 134.9 pt) |
| Underfull boxes | 4 |
| Package / LaTeX warnings | **0** (were 17) |
| Static validator (`validate_latex.py`) | **13 PASS / 0 FAIL** |
| Example re-derivation (`verify_examples.py`) | **56 checks / 0 mismatches** |
| Phase 0–7 files altered | **0 of 94** (byte-verified) |
| Phase 8 archive altered | **no** — published SHA-256 still verifies |

---

## 2. The two caveats, stated first

**Caveat 1 — the engine is not a current TeX Live.** The environment has no
TeX distribution, so a real but **2010-vintage pdfTeX (1.40.11)** was recovered
from the npm package `texlive@1.2.0`, driven as
`pdftex -fmt=latex -progname=pdflatex` with `\pdfoutput=1` prefixed to the
source. Three packages absent from that tree (`booktabs`, `enumitem`,
`xcolor`) were retrieved from GitHub mirrors of the CTAN sources. The output is
a genuine pdfTeX PDF with embedded Type 1 fonts, and it is warning-free — but
it has **not** been reproduced on a current distribution. Recompile with

```bash
cd PAPER && pdflatex main && bibtex main && pdflatex main && pdflatex main
```

before circulating. The recompile is expected to succeed unchanged. See
`compile/README.md` for the full provenance.

**Caveat 2 — `bibtex` was replaced by Python.** No `bibtex` binary exists in
the recovered tree. `tools/make_bbl.py` writes `main.bbl` using **pybtex**'s
implementation of the `plain` style, which is the style `main.tex` requests.
LaTeX only ever reads the `.bbl`, so the rendering is unaffected by the
substitution; the ordering and punctuation of the reference list were compared
against `plain.bst` semantics and against a manual reading of all 13 entries
(§5 below). The `.bbl` is shipped, so this affects rebuilds only.

Neither caveat touches the mathematics. All six corrections found in Phase 8A
(§4) are **transcription** fixes: the Phase logs were right and the manuscript
had misquoted them.

---

## 3. What was run

| command | result |
|---|---|
| `PY=/tmp/bibvenv/bin/python ./compile/build.sh` | 39 pp., 648 899 B, exit 0 |
| `python3 tools/validate_latex.py` | 13 PASS / 0 FAIL |
| `python3 tools/check_log.py main.log` | clean; 0 errors, 0 warnings |
| `python3 tools/verify_examples.py` | 56 checks, 0 mismatches (45 s) |
| `python3 tools/manuscript_stats.py` | 3 006 lines, 12 447 words, 43 theorem-like statements, 13 examples, 107 labels, 13/13 cited |
| `python3 tools/build_parameter_tables.py` | 8 CSVs regenerated, 25 families, 28 certified codes |
| `python3 tools/make_manifest.py` | 85 supplementary files + 121 package files hashed |
| `sha256sum -c MatrixRingManuscript_20261109.zip.sha256` | OK |
| `unzip -t MatrixRingManuscript_20261109.zip` | no errors, 121 entries |
| `python3 tools/make_package.py 20261109_Phase8A` | 127 entries, `unzip -t` clean |

### 3.1 `validate_latex.py` — 13/13

```
V1   every \input resolves to an existing file          PASS   13 files
V2   braces are balanced in every file                  PASS   13 files
V3a  every \begin has a matching \end                   PASS   all matched
V3b  every environment is provided by a loaded package  PASS   all known
V4   every \ref/\eqref has a matching \label            PASS   246 refs, 107 labels
V5   no \label is defined twice                         PASS   107 labels unique
V6   every \cite key has a bibliography entry           PASS   32 citations, 13 entries
V7   no bibliography entry is uncited                   PASS   13 entries all cited
V8   no key on the DO-NOT-CITE list is cited            PASS   clean
V9   every control sequence is defined (heuristic)      PASS   422 macros, all known
V10  verbatim blocks contain no active macros           PASS   clean
V11  no author/affiliation/funding metadata is invented PASS   only \AUTHORPLACEHOLDER
V12  math delimiters $...$ are balanced per file        PASS   balanced
```

Two lists in this validator were legitimately extended during Phase 8A, because
the manuscript had begun using constructs that *are* valid: the amsmath inner
environments `aligned gathered alignedat smallmatrix subarray` (from the
display-splitting pass) and the TeX register assignments
`\emergencystretch \tolerance \hbadness \vbadness \hfuzz \vfuzz \pretolerance
\looseness \widowpenalty \clubpenalty \hyphenpenalty` plus `\path` and
`\filepath`. Neither is a relaxation of the check; both were previously
unknown names, and an unknown name is what V9 exists to catch.

### 3.2 `check_log.py` — clean

0 errors, 0 missing characters, 0 undefined references, 0 undefined citations,
0 overfull boxes, 4 underfull boxes, **0 LaTeX/package warnings**.

The script attributes each warning to the source file that produced it and
prints an excerpt of the offending line. Its file-tracking self-audit reports
`66 opens, 65 closes, 0 stray, 1 unclosed → UNRELIABLE ATTRIBUTION`: one
`(` in the log is not matched by a `)`, so per-line attribution near a file
boundary can be off by one file. The *counts* are exact; only the assignment of
a warning to a file within one line of a boundary is approximate. This is a
known limitation of parsing TeX logs, and it is reported rather than hidden.

### 3.3 `verify_examples.py` — 56/56

Recomputes, from the Phase scripts' own library (not from the prose), every
number the worked examples quote, and every row of the two parameter tables:

* the ideal dimensions $\dim\mathfrak m^i$ and $\dim\ann_{\Bq^2}(\mathfrak m)$
  at $(4,2,2)$, $(9,2,3)$ and $(4,2,4)$;
* the count $1221$ of $\Bq$-submodules of $\Bq^2$ at $(4,2,2)$ — recomputed by
  exhaustive BFS over the submodule lattice;
* the $92$ nonzero codes and the $14$ $\sigma_2$-stable ones at $(8,1,2)$;
* every row of `tab:headline` (18) and `tab:cert` (28) against the route
  identities ($K=N-2k$ for SO, $K=2k-N$ for DC, $K=N-k-h_E$ and $c=k-h_E$ for
  R3, $K=N-k$ for R1), against the CSV tables, and against a **recomputed**
  Singleton defect $\text{def}=N-K+c-2(d-1)$.

46 of those 56 checks are table rows; all 46 are consistent. The remaining 10
are the example-level recomputations.

### 3.4 PDF inspection

Extracted with PyMuPDF: **39 pages**, 74 table-of-contents entries, ~108 kB of
text, references on pages 38–39 as 13 entries `[1]`–`[13]` running
Alahmadi→ZhangKongZheng with correct journal, volume, pages and DOI. Spot
checks on the extracted text (whitespace-normalised, since PDF extraction
inserts spaces inside `[[24,8,4]]` and similar) confirm the presence of every
headline parameter string: `[[24,8,4]]` ×8, `[[20,2,10;18]]` ×10,
`[[24,2,10;18]]` ×7, `[[32,8,2;4]]` ×5, `[[24,6,2;2]]` ×5, `[[16,4,3]]` ×7,
`O-3.1` ×11, `1221` ×3, `65536` ×1.

(Do **not** count pages by grepping `/Type /Page` in the raw file: it reports
49, because that counts the object definitions. PyMuPDF reports the true 39.)

---

## 4. The six corrections Phase 8A found

Full detail, with evidence, in `MANUSCRIPT_SELF_AUDIT.md` §3.1. Summary:

| id | where | was | now |
|---|---|---|---|
| **M-5** | `08_certification.tex`, `tab:headline`, row $[[16,4,3]]_4$ | `h_E = 10` | `h_E = 6` — $h_E=N-k$ for a dual-containing code, so 10 is impossible; all 21 DC codes of the family with $k=10$ have $h_E=6$, $K=4$, best exact $d=3$ |
| **m-7** | `06_gray.tex`, `ex:obstruction` | “3 of the 5 codes” | “4 of the 7” (Phase-5 log, check C3) |
| **m-8** | `07_quantum.tex` `ex:routes`; `08_certification.tex` `ex:certify` | each “**the** largest-distance code” | both name the tie at $d=10$ |
| **m-9** | `03_preliminaries.tex`, `ex:crt` | $\ann(\mathfrak m)$ | $\ann_{\Bq^2}(\mathfrak m)$ |
| **m-10** | `08_certification.tex`, `tab:budget` caption | “each distance” | $d=2,\dots,8$, with a pointer to `tab:headline` for $d=9,10$ |
| **m-11** | `09_comparison.tex` | largest distances “at $N=20$” | at $N=20$ **and** $N=24$ |

M-5 is the only one that a reader could have acted on wrongly: it is a wrong
number in a headline table. The other five are misquotations that a careful
reader would have caught, but which should not have been there.

All 13 worked examples were re-derived individually against the Phase logs
during this pass, not sampled.

---

## 5. The bibliography

`PAPER/references.bib` has 13 entries; all 13 are cited; no entry is cited for
a result the manuscript proves itself. Every entry was verified against a
publisher, arXiv or AIMS record — the per-entry record and verdict are in
`LITERATURE_VERIFICATION.md`.

| key | record |
|---|---|
| `Alahmadi2013CyclicM2F2` | *J. Franklin Inst.* **350**(9) 2837–2847 |
| `LuoParampalli2018M2F2uF2` | *Cryptogr. Commun.* **10**(6) 1109–1117, doi 10.1007/s12095-017-0266-1 |
| `Dinh2024CyclicRingsOfMatrices` | *Adv. Math. Commun.* **18**(4) 1100–1122, doi 10.3934/amc.2022073 |
| `JoshiPatelPrakash2026M4` | arXiv:2602.18255 [cs.IT] |
| `SiNiu2023SkewM2F2` | *AIMS Math.* **8**(10) 24434–24445, doi 10.3934/math.20231246 |
| `Wood1999Duality` | *Amer. J. Math.* **121**(3) 555–575, doi 10.1353/ajm.1999.0024 |
| `GreferathSchmidt1999GrayIsometry` | *IEEE Trans. Inform. Theory* **45**(7) 2522–2524, doi 10.1109/18.796395 |
| `FanZhang2017GaloisSelfDual` | *Des. Codes Cryptogr.* **84**(3) 473–492, doi 10.1007/s10623-016-0282-8 |
| `LiuPan2020GaloisHulls` | *Des. Codes Cryptogr.* **88**(2) 241–255 |
| `Cao2021MDSGaloisHulls` | *IEEE Trans. Inform. Theory* **67**(12) 7964–7984 |
| `ZhangKongZheng2026QuantumGaloisHulls` | *Entropy* **28**(4) 407, doi 10.3390/e28040407 |
| `KetkarEtAl2006NonbinaryStabilizer` | *IEEE Trans. Inform. Theory* **52**(11) 4892–4914 |
| `GrasslCodetables` | codetables.de, retrieved 2026-11-04 |

Three entries (`LiuPan2020GaloisHulls`, `Cao2021MDSGaloisHulls`,
`KetkarEtAl2006NonbinaryStabilizer`) have **no `doi` field** in `references.bib`.
They are the standard records listed above and are unambiguous without it; the
DOI was simply not re-retrieved in this environment. This does not affect the
rendering (the `plain` style prints no DOI), but it is listed here rather than
passed over.

Two entries in the *repository* bibliography (`01_LITERATURE/references.bib`)
required correction and were corrected in the copy used by the manuscript:
`LuoParampalli2018M2F2uF2` (volume/pages were `TO CONFIRM`) and
`ZhangKongZheng2026QuantumGaloisHulls` (volume/number/pages/DOI were
`TO CONFIRM`). A third, `LaiBrunWilde2013EADualities`, carries the online-first
year 2013 where the journal issue is 2014 — it is **not cited** in the
manuscript, so the question is moot here, but it is recorded.

---

## 6. What Phase 8A did not change

* **No Phase 0–7 file.** 94 protected files were hashed before and after; all
  identical.
* **The Phase 8 archive.** `MatrixRingManuscript_20261109.zip`,
  `d1ba4c821b1af01b8105eff702315957e692cfcaed21d5491a8ea03e4b29a80d`, 121 files,
  2 144 791 B, is byte-for-byte the file that was published and still verifies.
  The Phase 8A work is shipped alongside it in a separate archive.
* **No mathematics.** Six transcription errors were corrected; no theorem,
  proof, parameter or bound of the manuscript changed.

---

## 7. The one outstanding item

**Closed by Phase 8B (2026-11-10), see §0.** The manuscript has been
recompiled on TeX Live 2024 with genuine BibTeX 0.99d; the build is clean and
every check passes. The recompile found that the Phase 8A PDF had silently
dropped the word "Hom" twice and mangled one example heading, both now
corrected (§0.4). One editorial decision remains open — whether to keep the
`plain` bibliography style, which prints no DOI (§0.7).
