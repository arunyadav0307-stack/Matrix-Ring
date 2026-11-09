# The manuscript

> **Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
> Noncommutative Matrix Rings**
>
> Phase 8 deliverable. Branch `arena/59de606f-matrix-ring`.

---

## 1. What this directory is

The complete, self-contained research manuscript, together with its
supplementary reproducibility package and its self-review. Nothing here has
been submitted anywhere, and no journal has been selected.

```
PAPER/
├── main.tex                       the manuscript root
├── references.bib                 13 verified references, all cited
├── sections/                      11 section files + 2 appendices
├── compile/                       build scripts + how the PDF here was made
├── tools/                         validation and build scripts (see §5)
├── supplementary/                 reproducibility package (see §6)
│
├── main.pdf                       the compiled manuscript (39 pages)
├── main.bbl                       the generated bibliography (read by LaTeX)
│
├── CONTRIBUTION_MAP.md            Task A
├── CLAIM_TRACEABILITY_MATRIX.md   Task B
├── PARAMETER_COMPARISON.md        Tasks C and D
├── LITERATURE_VERIFICATION.md     Task D (bibliographic records)
├── NOVELTY_COMPARISON.md          Task D (novelty table)
├── MANUSCRIPT_SELF_AUDIT.md       Task J (self-review, issues classified)
├── OPEN_ISSUES_AND_LIMITATIONS.md Task J (limitations and open problems)
├── FINAL_VALIDATION_REPORT.md     Phase 8A: compile + verification record
├── CHANGELOG.md                   what changed in Phase 8A, and why
├── SHA256_MANIFEST.md             hashes of every file here + the package
├── README.md                      this file
└── MatrixRingManuscript_*.zip     the shipped archive (see §7)
```

---

## 2. Author metadata

**No author name, affiliation, funding acknowledgement or declaration has been
supplied.** None has been invented. The manuscript carries a single visible
placeholder macro, `\AUTHORPLACEHOLDER`, in three places: the `\author`
command, the `pdfauthor` hyperref field, and nowhere else. Static check V11 of
`tools/validate_latex.py` fails if any other author-like metadata
(`\author`, `\affiliation`, `\institute`, `\thanks`, `\funding`,
`\acknowledg*`) is introduced.

Search for `\AUTHORPLACEHOLDER` and replace it before any circulation.

---

## 3. Compilation

**`main.pdf` (39 pages) is included: the manuscript has been compiled.**

On any machine with a current TeX distribution:

```bash
cd PAPER
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

The document class is plain `article` (11pt, a4paper). **No journal template is
used and none is claimed.** Loaded packages: `geometry`, `inputenc`, `amsmath`,
`amssymb`, `amsthm`, `array`, `booktabs`, `longtable`, `enumitem`, `xcolor`,
`url`, `hyperref`. Bibliography style: `plain`, 13 entries.

The PDF shipped here was produced in an environment with **no TeX
distribution**, by recovering a real engine and substituting for the missing
`bibtex` binary. Read `compile/README.md` for exactly what was done, what is
still a substitute, and why you should recompile on a current TeX Live before
circulating it. In short:

| missing piece | substitute used here |
|---|---|
| a TeX engine | pdfTeX 1.40.11 recovered from npm `texlive@1.2.0` (a real x86-64 ELF binary shipped inside that archive), driven as `pdftex -fmt=latex -progname=pdflatex` with `\pdfoutput=1` on the first line |
| `bibtex` | `tools/make_bbl.py`, which writes `main.bbl` with **pybtex**'s `plain` style — LaTeX only ever reads the `.bbl` |
| `booktabs.sty`, `enumitem.sty`, `xcolor.sty` | absent from that tree; retrieved from GitHub mirrors of the CTAN sources, hashes recorded in `compile/README.md` |
| `fontenc` | **not loaded**: the recovered tree has no EC/T1 font metrics, so `T1` would silently fall back to `nullfont`. All sources are pure ASCII, so OT1 is equivalent here. |

`python3 tools/validate_latex.py` performs 13 static structural checks and
reports **13 PASS / 0 FAIL**; `python3 tools/check_log.py` analyses the TeX log
and reports **0 errors, 0 missing characters, 0 undefined references or
citations, 0 overfull boxes**.

---

## 4. Structure of the manuscript

| § | title | content |
|---|---|---|
| 1 | Introduction | the chain, the contributions, what is not claimed |
| 2 | Related work | each ingredient attributed; the gap stated |
| 3 | Preliminaries | $A_t$, $R=M_2(A_t)$, $R_n$, Morita, CRT, the failure lemma, $\theta_s$ |
| 4 | Cyclic codes and Galois duality | duality theorem, dual formula, three regimes |
| 5 | Galois hulls | hull structure, **refutation of O-3.1**, witnesses, LCD/SO/SD |
| 6 | Gray maps | exact Gram matrix, duality and hull preservation, char-2 obstruction |
| 7 | Quantum constructions | Weyl operators from scratch, R1/R2/R3, parameters |
| 8 | Certification | coset-distance theorem, coset Singleton bound, feasibility, tables |
| 9 | Comparison | codetables.de comparison with its limitations, novelty |
| 10 | Conclusion | summary, open problems |
| A | Appendix | the 28-row certification table, the witnesses, the comparison data |
| B | Appendix | reproducibility |

Counts: **21 theorems, 9 propositions, 11 lemmas, 2 corollaries, 8 definitions,
13 worked examples, 19 remarks** (43 theorem-like statements, 107 labels);
12 447 words of prose (3 006 lines of `.tex` over 13 files); 13 references, all
cited at least once.

---

## 5. The tools

| script | what it does |
|---|---|
| `tools/validate_latex.py` | 13 static LaTeX checks (V1–V12); exit 0 iff all pass |
| `tools/manuscript_stats.py` | word count, theorem/example/remark counts, citation coverage |
| `tools/build_parameter_tables.py` | regenerates the 8 CSV tables by **parsing the log** |
| `tools/make_manifest.py` | writes `supplementary/MANIFEST.sha256` and `SHA256_MANIFEST.md` |
| `tools/make_bbl.py` | writes `main.bbl` with pybtex — a stand-in for `bibtex main` |
| `tools/check_log.py` | analyses `main.log`: errors, missing glyphs, overfull boxes, per-file attribution |
| `tools/verify_examples.py` | **recomputes** the numbers quoted in the worked examples and the parameter tables |
| `tools/make_package.py` | builds a shipped archive and writes its `.sha256` sidecar |
| `compile/build.sh` | the whole build: `.bbl`, then three pdftex passes |

```bash
python3 tools/validate_latex.py        # 13/13 PASS
python3 tools/manuscript_stats.py
python3 tools/build_parameter_tables.py
python3 tools/make_manifest.py
python3 tools/check_log.py             # 0 overfull, 0 errors
python3 tools/verify_examples.py       # 56 checks, 0 mismatches
```

All of the `tools/` scripts are pure standard-library Python 3.
`tools/make_bbl.py` additionally needs `pybtex` (`pip install pybtex`), and only
if you do not have a real `bibtex`.

---

## 6. The supplementary package

`PAPER/supplementary/` contains the scripts (byte-identical copies of the
committed `04_COMPUTATION/` scripts), the logs, the **generator matrices of all
28 certified codes** (`generator_matrices/*.json`, produced by re-running the
search end-to-end with the committed seed), 8 CSV parameter tables each row of
which carries the log line it was parsed from, the certification procedure, the
environment record, and a SHA-256 manifest.

```bash
cd supplementary && sha256sum -c MANIFEST.sha256     # 85 files
```

See `supplementary/README.md`.

---

## 7. The archive

Two archives are shipped:

| archive | contents | files | uncompressed | SHA-256 |
|---|---|---|---|---|
| `MatrixRingManuscript_20261109.zip` | the **Phase 8** release: LaTeX sources, bibliography, tools, self-review documents, supplementary package — **no PDF** (none existed) | 121 | 2 144 791 B | `d1ba4c821b1af01b8105eff702315957e692cfcaed21d5491a8ea03e4b29a80d` |
| `MatrixRingManuscript_20261109_Phase8A.zip` | the **Phase 8A** release: the corrected and now-compiled manuscript, `main.pdf`, the build and verification tools | 127 entries | see the sidecar |

The Phase 8 archive is retained **byte for byte** so that the published hash
still verifies; nothing inside it was touched. Each archive's SHA-256 is in a
sidecar `.sha256` file which is deliberately **not** inside the archive, so
that the hash is checkable against the archive as shipped. (For the same
reason the Phase 8A hash is **not** quoted in any file inside that archive —
quoting it would change it.) Verify immediately after any transfer:

```bash
sha256sum -c MatrixRingManuscript_20261109.zip.sha256
sha256sum -c MatrixRingManuscript_20261109_Phase8A.zip.sha256
unzip -t MatrixRingManuscript_20261109.zip
```

Integrity at build time: `unzip -t` reports no errors on either archive.

---

## 8. What the manuscript does not claim

1. No record quantum parameter.
2. Matrix rings, Galois hulls, Gray maps, quasi-cyclic images, stabilizer
   codes and entanglement-assisted codes are each attributed and none is
   claimed as new; the novelty claim is the specific proved combination
   (§9.3 and `NOVELTY_COMPARISON.md`).
3. No journal suitability, Q1 or otherwise, is asserted.
4. The paper is **not** declared submission-ready. It now *is* typeset, and it
   compiles cleanly, but the build used a recovered 2010-vintage pdfTeX with a
   stand-in for `bibtex` (§3, `compile/README.md`); a recompile on a current
   TeX Live has not been performed.

See `MANUSCRIPT_SELF_AUDIT.md` §4 and `OPEN_ISSUES_AND_LIMITATIONS.md`.
