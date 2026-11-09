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
