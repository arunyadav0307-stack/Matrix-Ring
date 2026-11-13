#!/bin/sh
# ---------------------------------------------------------------------
#  kpathsea environment for the recovered TeX tree (see README.md).
#  Source this file; it sets the search paths explicitly so that the
#  stale ls-R databases shipped in the recovered tree cannot interfere.
# ---------------------------------------------------------------------
TL=${TL:-/home/user/.texlive}

[ -d "$TL/texmf-dist" ] || { echo "texenv.sh: no tree at $TL" >&2; return 1 2>/dev/null || exit 1; }

export TEXMFCNF="$TL:$TL/texmf-dist/web2c"
export TEXFORMATS=".;$TL/texmf-var/web2c/pdftex//;$TL/texmf-var/web2c//;$TL/texmf-dist/web2c//"
export TEXINPUTS=".;$TL/texmf-dist/tex//;$TL/texmf-dist/dvips//;$TL/texmf-var/tex//;$TL/texmf-config//"
export TEXFONTMAPS=".;$TL/texmf-var/fonts/map//;$TL/texmf-dist/fonts/map//"
export TFMFONTS=".;$TL/texmf-dist/fonts/tfm//;$TL/texmf-var/fonts/tfm//"
export PKFONTS=".;$TL/texmf-dist/fonts/pk//;$TL/texmf-var/fonts/pk//"
export VFFONTS=".;$TL/texmf-dist/fonts/vf//"
export ENCFONTS=".;$TL/texmf-dist/fonts/enc//"
export TEXPSHEADERS=".;$TL/texmf-dist/dvips//;$TL/texmf-dist/fonts/enc//;$TL/texmf-dist/fonts/type1//;$TL/texmf-dist/fonts/type42//;$TL/texmf-dist/fonts/truetype//"
export TEXPOOL=".;$TL/texmf-dist/web2c//"
export VARTEXFONTS="$TL/texmf-var/fonts"
export PATH="$TL/bin:$PATH"

# The recovered engine: pdfTeX 1.40.11, driven in PDF mode by the
# \pdfoutput=1 prefix (the tree ships only the DVI-mode latex.fmt).
PDFLATEX=${PDFLATEX:-pdftex}
PDFLATEX_FMT=latex

latex_run() {
    # $1 = jobname, stdin = nothing; compiles $1.tex from the CWD
    "$PDFLATEX" -fmt=$PDFLATEX_FMT -progname=pdflatex \
        -interaction=nonstopmode -file-line-error -jobname="$1" "$1.tex"
}
