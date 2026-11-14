# Compiling the manuscript

## 0. The recommended route: a normal TeX distribution

On any machine with a working TeX Live / MiKTeX / MacTeX, from `PAPER/`:

```bash
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

That is the authoritative build. Everything below describes how the PDF
shipped with this package was produced in an environment where **no TeX
distribution was installed and none could be installed** (all general internet
access was blocked).

## 1. What was actually available

The environment had outbound network access to exactly five hosts
(`github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`,
`pypi.org`, `files.pythonhosted.org`). No TeX engine was present
(`pdflatex`, `latex`, `xelatex`, `lualatex`, `tectonic`, `kpsewhich`,
`bibtex`: all absent), and `apt` could not reach a Debian mirror.

A working engine was nevertheless recovered, from npm:

* the npm package **`texlive` (texlive.js) v1.2.0**
  (`https://registry.npmjs.org/texlive/-/texlive-1.2.0.tgz`, 44 320 912 bytes,
  SHA-256 `d36d70c9b869530939ae771e244e5a3241a4ae8a8d4b68b4b6b83195fee01cf5`)
  ships a **TeX Live 2015 `texmf` tree** *and*, inside its `binary.zip`, a
  **native x86-64 Linux `pdftex` binary**
  (`binary/pdftex-1.40.11/build-pdftex/texk/web2c/pdftex`, 6 075 392 bytes):

  ```
  pdfTeX 3.1415926-1.40.11 (TeX Live 2010)
  kpathsea version 6.0.0
  ```

  (texlive.js uses this tree for its Emscripten build; the intermediate
  native binary was left in the published archive.)

* the tree also ships a **`latex.fmt`** dump (LaTeX2e `<2015/10/01> patch
  level 1`), which pdfTeX 1.40.11 loads without complaint.

Three packages used by the manuscript were **not** in that tree
(`booktabs`, `enumitem`, `xcolor`) and were retrieved from GitHub mirrors of
the CTAN sources:

| file | source | SHA-256 |
|---|---|---|
| `enumitem.sty` | `SeanDaBlack/KelloggBot` `resumeSrc/packages/enumitem.sty` (v3.9, 2019/06/20, Javier Bezos) | `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3` |
| `booktabs.sty` | `swimmingbrain/texbrain` `static/texlive/cache/booktabs.sty` (docstrip-generated) | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| `xcolor.sty` | `oetiker/lshort` `src/xcolor.sty` (v2.11, 2016/05/11, Uwe Kern) | `041d96ac888647cd482f69e7f8d4e7ccb137f37541c1a3b970946eb18eda29dd` |

`mathtools` and `multirow` were **removed** from the preamble: no command from
either is used anywhere in the manuscript (verified by grep: zero uses of
`multirow`, zero mathtools-only macros). Removing them changes nothing in the
output. `xcolor` was kept — it is used by the `\blanksymbol` helper — and the
file above was fetched for it.

## 2. What is still missing, and how it is worked around

| missing | workaround |
|---|---|
| **`bibtex`** | `tools/make_bbl.py` generates `main.bbl` with **pybtex** (plain style). LaTeX only ever reads the `.bbl`, so the result is equivalent to a real `bibtex main` run. See the docstring of that script. |
| **`pdflatex.fmt`** | the tree ships only `latex.fmt` (DVI mode). A native `pdflatex.fmt` could not be dumped (the reduced tree lacks several hyphenation pattern files). The build instead feeds pdfTeX a one-line driver whose first token is `\pdfoutput=1`, which switches the engine to PDF mode before `\documentclass`. This is a documented pdfTeX feature and the output is a genuine pdfTeX PDF with embedded Type 1 fonts. |

## 3. Files in this directory

```
compile/
├── README.md     this file
├── texenv.sh     the kpathsea environment for the recovered tree
├── build.sh      the whole build: .bbl, then 3 pdflatex passes
└── fetch_texlive.sh   (re-)downloads and assembles the tree from npm
```

`fetch_texlive.sh` documents exactly how the tree was assembled; it needs
network access to `registry.npmjs.org` (for the engine) and `api.github.com`
(for the three `.sty` files) only. It installs into `/home/user/.texlive` —
not under `~/.cache`, which this environment wipes between sessions — and both
it and `texenv.sh` take the location from the `TL` variable, so change it in
one place if you want the tree elsewhere. Run it if the build fails with
`texenv.sh: no tree at …`.

## 4. Building

```bash
cd PAPER
./compile/build.sh
```

The build does:

1. `python3 tools/make_bbl.py` (substitute for `bibtex main`) — needs
   **pybtex** (`pip install pybtex`); set `PY=/path/to/python` if that Python
   is not the default one;
2. `pdftex -fmt=latex -progname=pdflatex -jobname=main <driver>` — pass 1;
3. the same command — pass 2 (resolves `\ref`, `\cite` and the TOC);
4. the same command — pass 3 (settles page references).

It writes `main.pdf`, `main.log`, `main.aux`, `main.toc`, `main.out` and
`main.bbl` into `PAPER/`.

## 5. Verifying the result is a real PDF

```bash
python3 - <<'EOF'
d = open('main.pdf','rb').read()
print('header      :', d[:8])
print('trailer/EOF :', d.rstrip()[-6:])
print('bytes       :', len(d))
EOF
```

Do **not** count pages by grepping the raw file for `/Type /Page`: that counts
object definitions and reports 49 for a 39-page document. Use a PDF library
(`pymupdf`, `pypdf`) or `pdfinfo`.

Then read the log for the usual quality signals — or let
`tools/check_log.py` do it:

```bash
python3 tools/check_log.py            # 0 errors, 0 warnings, 0 overfull
python3 tools/check_log.py main.log --tol 5    # only boxes worse than 5pt
```

`check_log.py` attributes each warning to the file that produced it, prints an
excerpt of the offending line, and audits its own file tracking. When it says
`UNRELIABLE ATTRIBUTION` it means one `(` in the log is unmatched, so the
attribution of a warning to a file can be off by one file near a source-file
boundary; the counts are always exact.

## 6. Honest statement of the limitation

The recovered engine is **pdfTeX 1.40.11 (2010) with a TeX Live 2015
`texmf` tree**, driven through a `\pdfoutput=1` prefix rather than a native
`pdflatex` format, and with `bibtex` replaced by a pybtex-generated `.bbl`.
It is a real TeX engine and the artefact is a real PDF, but it is **not** a
contemporary TeX Live. The manuscript should be re-compiled on a current
distribution before circulation; `pdflatex main && bibtex main && pdflatex
main && pdflatex main` is expected to succeed unchanged.
