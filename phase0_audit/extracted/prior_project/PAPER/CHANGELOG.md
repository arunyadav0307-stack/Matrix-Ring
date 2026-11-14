# Changelog

All entries are dated 2026-11-09 unless stated. The archive `MatrixRingManuscript_20261109.zip` is the **Phase 8** release
and is retained byte for byte; nothing inside it was touched. Its SHA-256 is
quoted in `README.md` and still verifies. Everything below is part of the
**Phase 8A** revision, shipped as
`MatrixRingManuscript_20261109_Phase8A.zip` (127 entries; its
SHA-256 is in the sidecar `.sha256` file, and is not quoted
inside the archive, since quoting it would change it).

---

## Phase 8A — the manuscript is compiled, and six numerical defects are fixed

### 1. The manuscript now renders (`main.pdf`, 39 pages)

The previous release shipped no PDF: no TeX engine existed in the environment
in which it was written. **M-1 of `MANUSCRIPT_SELF_AUDIT.md` is resolved.**

* New directory `compile/`:
  * `README.md` — exactly how the PDF was made, what is a substitute, and how
    to reproduce it on a current TeX Live;
  * `fetch_texlive.sh` — rebuilds the recovered engine from npm;
  * `texenv.sh` — the kpathsea environment;
  * `build.sh` — the whole build (`.bbl`, then three pdftex passes).
* New tool `tools/make_bbl.py` — writes `main.bbl` with `pybtex`, standing in
  for the absent `bibtex` binary. LaTeX only ever reads the `.bbl`.
* New tool `tools/check_log.py` — analyses `main.log`, attributes every
  warning to the file that produced it, and reports a self-audit of its own
  file tracking.
* New tool `tools/verify_examples.py` — recomputes, from the Phase scripts'
  own library, the numbers quoted in the worked examples and in the parameter
  tables.

### 2. `main.tex`

| change | why |
|---|---|
| removed `\usepackage[T1]{fontenc}` | the recovered tree has no EC/T1 font metrics; `T1` silently fell back to `nullfont` and dropped 70 564 glyphs. All sources are pure ASCII, so OT1 is equivalent here. A comment in the preamble records this. |
| removed `\usepackage{mathtools}` | zero uses anywhere in the manuscript |
| removed `\usepackage{multirow}` | zero uses anywhere in the manuscript |
| kept `\usepackage{xcolor}` | used by `\blanksymbol`; `xcolor.sty` was retrieved and installed |
| `\blanksymbol` redefined without `xcolor` dependency left in place | — |
| added `\usepackage{url}` and `\newcommand{\filepath}{\path}` | file names such as `phase7_extended_search_log.txt` cannot break in `\texttt` and ran into the margin |
| added `\emergencystretch=2em` | last-resort interword stretch, used only on lines that would otherwise be overfull |
| added `\filepath` usage in the appendices | replaces 8 `\texttt{…\_…}` occurrences |

### 3. Corrections to the mathematics as presented

Every one of these is a **transcription** error: the underlying computation in
the Phase logs is correct, and the manuscript misquoted it. Each is also
recorded in `MANUSCRIPT_SELF_AUDIT.md` with its evidence.

| id | location | was | now |
|---|---|---|---|
| **M-5** | `08_certification.tex`, Table `tab:headline`, row `$[[16,4,3]]_4$ / $(4,1,4)$ / R2-DC` | `h_E = 10` | `h_E = 6`. For a dual-containing code $h_E = N-k$; $10$ is impossible. Confirmed by exhaustive scan: all 21 DC codes of the family with $k=10$ have $h_E=6$, $K=4$, best exact $d=3$. |
| **m-7** | `06_gray.tex`, Example `ex:obstruction` | “the minimum distance changed under $\Psi$ for **3 of the 5** codes tested” | “**4 of the 7** self-orthogonal codes transformed” (Phase-5 log, check C3) |
| **m-8** | `07_quantum.tex` Example `ex:routes`; `08_certification.tex` Example `ex:certify` | each said its code was “**the** largest-distance code found anywhere in the search” | both name the tie: $[[20,2,10;18]]_4$ and $[[24,2,10;18]]_9$ both have $d=10$, and nothing in the search exceeds it |
| **m-9** | `03_preliminaries.tex`, Example `ex:crt` | $\dim_{\F_4}\ann(\mathfrak m)=2$ | $\dim_{\F_4}\ann_{\Bq^2}(\mathfrak m)=2$ (the value $2$ is the annihilator in $\Bq^2$; $\ann_\Bq$ is $1$-dimensional) |
| **m-10** | `08_certification.tex`, Table `tab:budget` caption | “minimum entanglement $c$ for **each** distance” | the range $d=2,\dots,8$ is stated, with a pointer to `tab:headline` for $d=9$ ($c=16$) and $d=10$ ($c=18$) |
| **m-11** | `09_comparison.tex` | the largest distances occur “at $N=20$” | they occur at $N=20$ **and** $N=24$; both codes named |

### 4. Typesetting

27 overfull boxes (worst 134.9 pt) → **0**. The fixes were structural, not
cosmetic:

* the two `\boxed{…} \longrightarrow …` chains (§1 and §10) were split over
  two lines with `gathered`;
* four display equations that ran past the text block were split with
  `aligned` / `gathered` (§3 Lemma proof, §5 the four-way `⟺`, §5 the
  $(4,2,4)$ ideal dimensions, §8 the R3 parameter display);
* the §5 witness table was set `\small`;
* one theorem item and one remark were given displays for their long formulae;
* the long section title in §3 was given an explicit break;
* the remaining sub-15pt overruns are absorbed by `\emergencystretch`;
* the 14 `Token not allowed in a PDF string` warnings — mathematics in five
  subsection titles, which hyperref cannot put in a PDF bookmark — were
  removed with `\texorpdfstring`, and the 3 "'h' float specifier changed to
  'ht'" warnings by writing `[ht]`. **The log is now warning-free.**

### 5. Verification added

| check | result |
|---|---|
| `tools/validate_latex.py` | 13 / 13 PASS (246 refs, 107 labels, 32 citations, 13 bib entries) |
| `tools/check_log.py` | 0 errors · 0 missing characters · 0 undefined references · 0 undefined citations · **0 overfull boxes** · 4 underfull · **0 package/LaTeX warnings** |
| `tools/verify_examples.py` | 56 checks, 0 mismatches |
| `tools/manuscript_stats.py` | 3 006 lines, 12 447 words, 43 theorem-like statements, 13 examples, 107 labels, 13/13 entries cited |
| PDF | 39 pages, A4, `%PDF-1.4`, Type 1 fonts embedded, 74 TOC entries |

The 56 checks of `verify_examples.py` cover: the ideal dimensions
$\dim\mathfrak m^i$ and $\dim\ann_{\Bq^2}(\mathfrak m)$ at $(4,2,2)$,
$(9,2,3)$ and $(4,2,4)$; the count $1221$ of $\Bq$-submodules of $\Bq^2$ at
$(4,2,2)$ (exhaustive BFS); the $92$ nonzero codes and $14$ $\sigma_2$-stable
codes at $(8,1,2)$; and every row of `tab:headline` (18) and `tab:cert` (28)
against the route identities, the CSV tables and a recomputed Singleton defect.

### 6. Documents

* `MANUSCRIPT_SELF_AUDIT.md` — M-1 rewritten as RESOLVED; new §3.1 records the
  six Phase-8A defects and their dispositions; checks 16 and 17 added to §1;
  verdict updated.
* `OPEN_ISSUES_AND_LIMITATIONS.md` — the “not typeset” limitation rewritten.
* `README.md` — compilation section rewritten, counts refreshed, new tools
  listed, both archives described.
* `FINAL_VALIDATION_REPORT.md` — **new**: the full Phase-8A validation record.
* `CHANGELOG.md` — **new**: this file.
* `compile/README.md` — **new**: how the PDF was made.
* `tools/make_package.py` — **new**: builds a shipped archive and writes its
  `.sha256` sidecar (`python3 tools/make_package.py 20261109_Phase8A`).

### 7. Not changed

* No Phase 0–7 file was touched (94 files, verified byte-identical).
* The Phase 8 archive `MatrixRingManuscript_20261109.zip` is unchanged and its
  published SHA-256 still verifies.
* No mathematics of the manuscript changed: all six corrections are
  transcription fixes to numbers already correct in the Phase logs.

---

## Phase 8B — modern compilation (2026-11-10)

**The one outstanding Phase 8A item is closed.** The manuscript has been
rebuilt on a **current TeX Live with genuine BibTeX**, in an isolated copy, and
the build is clean. Shipped as
`MatrixRingManuscript_20261110_Phase8B.zip` — 44 entries. **The archive's
SHA-256 and size are in the sidecar
`MatrixRingManuscript_20261110_Phase8B.zip.sha256`, deliberately outside the
archive so that the hash is checkable against the file as shipped; quoting it
here would change it.**

**Clean rebuild verified.** The package was unpacked into an empty directory, a
fresh TeX Live 2024 tree was bootstrapped from the packaged script, and the
manuscript was rebuilt from `sources/`. The result is **byte-identical** to the
shipped PDF (`69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd`);
all 43 manifest entries verified, 0 bad.

Two earlier packagings of the same sources and scripts were verified the same
way, with the same byte-identical result, and are superseded by this one: the
first closed the build, the second added decision `D-1`. Their SHA-256 values
are retained in the git history.

### 1. Tool chain

| | |
|---|---|
| TeX Live | **2024** |
| pdfTeX | **3.141592653-2.6-1.40.26** |
| BibTeX | **0.99d** — genuine, `plain.bst`, not pybtex |
| kpathsea | 6.3.6/dev (`kpsewhich`, built from source) |
| host | Linux 6.1.158 x86_64, gcc 12.2.0, CPython 3.11.2 |

CTAN and tug.org are unreachable here, so `install-tl`/`tlmgr` were impossible.
`compile/bootstrap_texlive.sh` assembles the tree from the reachable hosts only
and verifies every artefact by SHA-256: a PyPI wheel bundling a real TinyTeX
(TeX Live 2024) release supplies the texmf tree and `pdflatex`; npm
`texlive@1.2.0` supplies the version-stable files the TinyTeX tree omits
(`amsfonts`, `amsthm`, `plain.bst`); `booktabs.sty` comes from a GitHub blob;
`kpathsea` and `bibtex` are compiled from `tex-mirror/tex-live`. `bibtex` is
compiled from the TeX Live 2024 Pascal sources with `tangle` and `web2c`,
because substituting pybtex again is exactly what Phase 8B forbids.

### 2. Build result

Four passes (`pdflatex` → `bibtex` → `pdflatex` → `pdflatex`) in
`build_modern/`, from a **fresh genuine-BibTeX `.bbl`**:

* **39 pages**, A4 595 × 842 pt — the same page count as Phase 8A.
* **0 errors, 0 missing glyphs, 0 undefined references, 0 undefined citations,
  0 overfull boxes, 0 underfull boxes, 0 warnings of any kind.**
* 563 659 B, SHA-256
  `69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd`.
* **Byte-reproducible**: `build_modern.sh` pins `SOURCE_DATE_EPOCH`, so repeated
  builds return the identical SHA-256 rather than a fresh timestamp each time.
* `tools/validate_latex.py` — **13 PASS / 0 FAIL**.
* `tools/verify_examples.py` — **56 checks / 0 mismatches**.
* `tools/inspect_pdf.py` — **0 issues**.

### 3. Five corrections — none of them mathematical

Recorded entry by entry in `compile/BUILD_CORRECTIONS.md` (append-only).

* **C-1** `main.tex` — `\AUTHORPLACEHOLDER` was used at line 39 and defined at
  line 68. Current `hyperref` expands PDF metadata when `\hypersetup` runs, so
  this is a hard error; the 2010 release deferred the expansion.
* **C-2** `main.tex` — **`\Hom` was never defined** but was used in §3 and §4.
  The 2010 engine silently dropped the operator name: the shipped Phase 8A PDF
  contains the word "Hom" **zero** times, and two sentences do not parse. Fixed
  with `\newcommand{\Hom}{\operatorname{Hom}}`, matching the file's convention.
* **C-3** `sections/08_certification.tex:324` — an unbraced `]]` in
  `\begin{example}[certifying $[[20,2,10;18]]_4$]` broke LaTeX's
  optional-argument scanner, so the 8A PDF read "Example 8.12 (certifying
  [[20, 2, 10; 18). ]4]". The argument is now braced. A sweep of all 13 sources
  found exactly this one site.
* **C-4** distribution, not source — the TS1 text-companion fonts (`cm-super`)
  are absent. Since kernel release 2020/02/02 `itemize` bullets come from TS1
  rather than the OMS maths font, so the run died with
  `Font tcrm1095 at 600 not found`. Substituted in the pdfTeX font map with
  Latin Modern TS1 outlines (`compile/map_ts1_lm.py`). The map is patched
  rather than the format rebuilt, so hyphenation, line breaking and page
  breaking are exactly as shipped.
* **C-5** `main.tex` — the PDF `/Title` was empty because `hyperref` does not
  read `\title` without `pdfusetitle`; added it, and wrapped the author
  placeholder in `\texorpdfstring` so the PDF string is plain text. All four
  `hyperref` warnings are gone.

**C-2 and C-3 are corrections to the released Phase 8A PDF, not merely to the
sources.** No error appeared in the Phase 8A log for either: the manuscript was
wrong on the page and the log did not say so.

### 4. The DOI question — DECIDED 2026-11-10: keep `plain`

The Phase 8A PDF printed `doi:10.1016/…` for nine references. That was the
pybtex substitute, not `plain.bst`: genuine BibTeX with the `plain` style that
`main.tex` requests prints no DOI, and `FINAL_VALIDATION_REPORT.md` §5 already
recorded this on 2026-11-09. The modern build therefore drops nine DOIs that
appeared in the 8A PDF — the only Phase 8B change that removes information.

**Decision (author, 2026-11-10): keep `plain`.** Recorded as `D-1` in
`compile/BUILD_CORRECTIONS.md` and in `FINAL_VALIDATION_REPORT.md` §0.7.

1. `ibliographystyle{plain}` is retained. **No change made** — `main.tex:165`
   is untouched by Phase 8B.
2. No switch to `plainurl`, `plainnat` or any other DOI-aware style.
3. `references.bib` is **unmodified** and byte-identical to the Phase 8A file;
   all `doi` fields are preserved, so a journal style that prints them needs no
   further editing.
4. **DOI display is deferred to journal-specific formatting**: the target
   venue's class or bibliography style governs how, and whether, DOIs appear.

With this, Phase 8B has **no open items**.

### 4b. Status

**CLOSED 2026-11-10.** No open items.

Final state:

| | |
|---|---|
| corrections | 5 (C-1…C-5), none mathematical |
| decisions | 1 (D-1: keep `plain`), **no file changed** |
| modern PDF | 39 pages, 563 659 B, SHA-256 `69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd` |
| final package | `MatrixRingManuscript_20261110_Phase8B.zip`, 44 entries — SHA-256 and size in its `.sha256` sidecar |
| clean rebuild | **byte-identical**, 43/43 manifest entries verified |
| validator / examples / inspection | 13/13 · 56/56 · 0 issues |

Nothing further is authorised in this phase: no journal selection, no
submission preparation, no further manuscript changes.

### 5. New files

* `compile/bootstrap_texlive.sh` — assembles the TeX Live 2024 tree.
* `compile/build_modern.sh` — the four-pass modern build.
* `compile/mktexlsr.py`, `compile/map_ts1_lm.py`,
  `compile/texmf-local/tex/latex/ts1-cmr-lm-subst/ts1cmr.fd` — support.
* `compile/README_BUILD.md` — build instructions and provenance.
* `compile/BUILD_CORRECTIONS.md` — append-only correction log (C-1…C-5).
* `tools/inspect_pdf.py` — measures the built PDF (geometry, overlap, fonts,
  glyphs, environment and tuple inventory) and can diff two PDFs.

`PAPER/build_modern/` is generated and is git-ignored.

### 6. Decision register

| # | decision | date | effect on the build |
|---|---|---|---|
| D-1 | keep `\bibliographystyle{plain}`; do not switch to a DOI-aware style; leave `references.bib` untouched; DOI display deferred to journal-specific formatting | 2026-11-10 | **none** — no file changed; the PDF SHA-256 is unchanged |

Full text in `compile/BUILD_CORRECTIONS.md`.

### 7. Not changed

* No Phase 0–7 file was touched (94 files, verified byte-identical).
* The Phase 8 archive `MatrixRingManuscript_20261109.zip`
  (`d1ba4c82…4b29a80d`, 543 086 B) and the Phase 8A archive
  (`14ecac0e…342910`, 1 096 851 B) both still verify against their sidecars.
* `PAPER/main.pdf` is still the Phase 8A build
  (`b2ba1fee…8641a03`); the modern PDF ships in the Phase 8B package.
* The Phase 8A provenance (`compile/README.md`, `compile/build.sh`,
  `compile/fetch_texlive.sh`, `compile/texenv.sh`) is byte-identical. One file,
  `compile/build.sh`, was overwritten early in Phase 8B and restored from the
  Phase 8A commit before the Phase 8B commit was made.
* **No mathematics of the manuscript changed.**
