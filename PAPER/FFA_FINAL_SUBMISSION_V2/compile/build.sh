#!/bin/sh
# ---------------------------------------------------------------------
#  Build PAPER/main.pdf with the recovered TeX tree.
#  See compile/README.md for what this does and why.
#
#  On a machine with a normal TeX distribution, use instead:
#      pdflatex main && bibtex main && pdflatex main && pdflatex main
# ---------------------------------------------------------------------
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
PAPER=$(cd "$HERE/.." && pwd)
cd "$PAPER"

. "$HERE/texenv.sh"

PY=${PY:-python3}

echo "== [1/5] locating the engine =="
command -v "$PDFLATEX" >/dev/null 2>&1 || {
    echo "build.sh: '$PDFLATEX' not found. Set PDFLATEX=... or run compile/fetch_texlive.sh" >&2
    exit 3
}
"$PDFLATEX" --version 2>&1 | head -1

echo "== [2/5] writing the PDF-mode driver =="
# The recovered tree has no pdflatex.fmt; \pdfoutput=1 before
# \documentclass switches pdfTeX into PDF mode.
cat > .build_main.tex <<'EOF'
\pdfoutput=1
\input main.tex
EOF

echo "== [3/5] generating main.bbl (substitute for 'bibtex main') =="
rm -f main.bbl
"$PY" tools/make_bbl.py --aux main.aux --bib references.bib --out main.bbl

echo "== [4/5] pdflatex pass 1 (writes main.aux with the \\citation keys) =="
"$PDFLATEX" -fmt=$PDFLATEX_FMT -progname=pdflatex \
    -interaction=nonstopmode -file-line-error -jobname=main .build_main.tex \
    > /dev/null 2>&1 || true
[ -f main.aux ] || { echo "build.sh: pass 1 produced no main.aux" >&2; exit 4; }

echo "== [4b] regenerating main.bbl with the real citation order =="
"$PY" tools/make_bbl.py --aux main.aux --bib references.bib --out main.bbl --check

echo "== [5/5] pdflatex passes 2 and 3 (resolve refs, citations, TOC) =="
"$PDFLATEX" -fmt=$PDFLATEX_FMT -progname=pdflatex \
    -interaction=nonstopmode -file-line-error -jobname=main .build_main.tex > /dev/null 2>&1 || true
"$PDFLATEX" -fmt=$PDFLATEX_FMT -progname=pdflatex \
    -interaction=nonstopmode -file-line-error -jobname=main .build_main.tex > build_pass3.log 2>&1 || true

rm -f .build_main.tex

echo
echo "--- result -------------------------------------------------------"
if [ -f main.pdf ]; then
    ls -l main.pdf
    "$PY" - <<'EOF'
d = open('main.pdf','rb').read()
print('header      :', d[:8])
print('trailer/EOF :', d.rstrip()[-5:])
print('bytes       :', len(d))
print('/Type /Page :', d.count(b'/Type /Page') + d.count(b'/Type/Page'))
EOF
else
    echo "main.pdf NOT produced -- see main.log"
fi
echo "--- log summary --------------------------------------------------"
echo "Overfull  box warnings : $(grep -c '^Overfull' main.log || true)"
echo "Underfull box warnings : $(grep -c '^Underfull' main.log || true)"
echo "Undefined citations    : $(grep -c 'Citation .* undefined' main.log || true)"
echo "Undefined references   : $(grep -c 'Reference .* undefined' main.log || true)"
echo "Missing characters     : $(grep -c 'Missing character' main.log || true)"
echo "Errors (lines with !)  : $(grep -c '^!' main.log || true)"
echo "------------------------------------------------------------------"
