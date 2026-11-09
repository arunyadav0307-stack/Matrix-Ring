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
├── tables/                        (reserved; tables are inline in the sections)
├── tools/                         validation and build scripts (see §5)
├── supplementary/                 reproducibility package (see §6)
│
├── CONTRIBUTION_MAP.md            Task A
├── CLAIM_TRACEABILITY_MATRIX.md   Task B
├── PARAMETER_COMPARISON.md        Tasks C and D
├── LITERATURE_VERIFICATION.md     Task D (bibliographic records)
├── NOVELTY_COMPARISON.md          Task D (novelty table)
├── MANUSCRIPT_SELF_AUDIT.md       Task J (self-review, issues classified)
├── OPEN_ISSUES_AND_LIMITATIONS.md Task J (limitations and open problems)
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

**The manuscript has not been compiled. No PDF is included.**

There is no TeX engine in the environment in which this was written:
`pdflatex`, `latex`, `xelatex`, `lualatex`, `tectonic` and `kpsewhich` are all
absent, and no usable WASM/JS build was obtainable. A static validator
(`tools/validate_latex.py`) was written instead; it performs 13 structural
checks and currently reports **13 PASS / 0 FAIL**.

On a machine with a TeX distribution:

```bash
cd PAPER
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

The document class is plain `article` (11pt, a4paper). **No journal template is
used and none is claimed.** Loaded packages: `geometry`, `fontenc`,
`inputenc`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `array`, `booktabs`,
`multirow`, `longtable`, `enumitem`, `xcolor`, `hyperref`. Bibliography style:
`plain`.

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
13 worked examples, 18 remarks**; ≈ 12 000 words of prose; 13 references, all
cited.

---

## 5. The tools

| script | what it does |
|---|---|
| `tools/validate_latex.py` | 13 static LaTeX checks (V1–V12); exit 0 iff all pass |
| `tools/manuscript_stats.py` | word count, theorem/example/remark counts, citation coverage |
| `tools/build_parameter_tables.py` | regenerates the 8 CSV tables by **parsing the log** |
| `tools/make_manifest.py` | writes `supplementary/MANIFEST.sha256` and `SHA256_MANIFEST.md` |

```bash
python3 tools/validate_latex.py        # 13/13 PASS
python3 tools/manuscript_stats.py
python3 tools/build_parameter_tables.py
python3 tools/make_manifest.py
```

All four are pure standard-library Python 3.

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

`MatrixRingManuscript_20261109.zip` contains the manuscript (LaTeX sources,
bibliography, tools, self-review documents) and the supplementary package:
121 files, 2 144 375 bytes uncompressed. Its SHA-256 is in the sidecar file
`MatrixRingManuscript_20261109.zip.sha256`, which is deliberately **not**
inside the archive (so that the hash is checkable against the archive as
shipped). Verify immediately after any transfer:

```bash
sha256sum -c MatrixRingManuscript_20261109.zip.sha256
unzip -t MatrixRingManuscript_20261109.zip
```

Integrity at build time: `unzip -t` reported no errors, 121 entries.

---

## 8. What the manuscript does not claim

1. No record quantum parameter.
2. Matrix rings, Galois hulls, Gray maps, quasi-cyclic images, stabilizer
   codes and entanglement-assisted codes are each attributed and none is
   claimed as new; the novelty claim is the specific proved combination
   (§9.3 and `NOVELTY_COMPARISON.md`).
3. No journal suitability, Q1 or otherwise, is asserted.
4. The paper is **not** declared submission-ready: it has not been typeset.

See `MANUSCRIPT_SELF_AUDIT.md` §4 and `OPEN_ISSUES_AND_LIMITATIONS.md`.
