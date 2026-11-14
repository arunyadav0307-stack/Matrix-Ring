# Phase 8B — how the modern build was made, and how to repeat it

This directory contains everything needed to compile `PAPER/main.tex` on a
**current** TeX Live, in an environment that has no TeX distribution and no
package manager.

| file | what it is |
|---|---|
| `bootstrap_texlive.sh` | assembles a TeX Live 2024 tree from the network sources reachable here |
| `build_modern.sh` | the four-pass build: `pdflatex` → `bibtex` → `pdflatex` → `pdflatex` |
| `mktexlsr.py` | writes the `ls-R` filename databases (no `mktexlsr` ships with `texk/kpathsea`) |
| `map_ts1_lm.py` | supplies the missing TS1 `cm-super` fonts from Latin Modern |
| `texmf-local/` | NFSS-level fallback for the same substitution |
| `BUILD_CORRECTIONS.md` | append-only log of every correction made to build the manuscript |
| `build.sh`, `fetch_texlive.sh`, `texenv.sh`, `README.md` | **Phase 8A provenance — historical, do not modify** |

---

## 1. Why a bootstrap script is needed

The build environment has no TeX installation, no `tlmgr`, no `install-tl`, and
no system package manager. Outbound network access is limited to
`github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`,
`pypi.org` and `files.pythonhosted.org`; CTAN and tug.org are **not** reachable,
so `install-tl` cannot be used.

`bootstrap_texlive.sh` therefore assembles a tree from those hosts only, and
verifies every downloaded artefact against a recorded SHA-256:

| component | source |
|---|---|
| TeX Live **2024** texmf tree, `pdflatex` (pdfTeX 1.40.26) | the PyPI wheel `rendercv-tinytex==0.2.0`, which bundles a real TinyTeX (TeX Live 2024) release |
| `amsfonts`, `amsthm`, `plain.bst` and friends | the npm package `texlive@1.2.0` (TeX Live 2015 texmf) — these files are version-stable |
| `booktabs.sty` | a GitHub blob, verified by SHA-256 |
| `kpsewhich` (kpathsea 6.3.6/dev) | built from `tex-mirror/tex-live` @ `5f7badd9` |
| `bibtex` (**BibTeX 0.99d**) | built from the TeX Live 2024 `bibtex.web` with `tangle` + `web2c` |

`bibtex` is built from source on purpose. Phase 8A had to substitute **pybtex**
for it, and that substitution turned out *not* to be faithful (it added DOI
blocks that genuine `plain.bst` does not emit). Phase 8B is required to use
genuine BibTeX, so the binary is compiled rather than replaced.

Nothing here touches the 2010-vintage engine recovered in Phase 8A; that
provenance is preserved in `build.sh`, `fetch_texlive.sh` and `README.md`.

---

## 2. Building

```bash
cd PAPER
./compile/bootstrap_texlive.sh          # ~40 s; needs network once
./compile/build_modern.sh               # writes build_modern/main.pdf
```

`bootstrap_texlive.sh` installs into `/home/user/texlive2024` by default;
override with `TL=/path ./compile/bootstrap_texlive.sh`. Both scripts are
idempotent and safe to re-run.

On a machine that already has a TeX Live 2023 or later, the manuscript needs no
special handling at all:

```bash
cd PAPER && pdflatex main && bibtex main && pdflatex main && pdflatex main
```

The only environment-dependent step is the TS1 font substitution
(`map_ts1_lm.py`), which is unnecessary on a distribution that ships
`cm-super`.

---

## 3. What a correct run looks like

```
== pass 1: pdflatex ==       errors: 0
== pass 2: bibtex ==         This is BibTeX, Version 0.99d (TeX Live 2024)
                             The style file: plain.bst
== pass 3: pdflatex ==
== pass 4: pdflatex ==

errors ................. 0
missing characters ..... 0
overfull / underfull ... 0 / 0
warnings ............... 0
pdf .................... 39 pages, A4
```

Reference values for the Phase 8B build are recorded in
`FINAL_VALIDATION_REPORT.md`, §0.
