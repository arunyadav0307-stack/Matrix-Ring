#!/bin/sh
# ---------------------------------------------------------------------
#  build.sh -- compile the manuscript with the local TeX Live 2024 tree.
#
#  Runs the four-pass cycle required for a complete document:
#      pdflatex  -> bibtex -> pdflatex -> pdflatex
#
#  The bibliography is produced by genuine BibTeX 0.99d from
#  references.bib; no pre-existing .bbl is used or required.
#
#  Usage:  ./compile/build_modern.sh [build-directory] [jobname]
# ---------------------------------------------------------------------
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
PAPER=$(cd "$HERE/.." && pwd)
BUILD=${1:-$PAPER/build_modern}
JOB=${2:-main}
TL=${TL:-/home/user/texlive2024}

# Sources live at $PAPER/main.tex in the repository and at $PAPER/sources/
# inside the shipped Phase 8B package; accept either.
SRC=$PAPER
[ -f "$SRC/main.tex" ] || SRC=$PAPER/sources
[ -f "$SRC/main.tex" ] || { echo "build_modern.sh: no main.tex under $PAPER" >&2; exit 1; }

[ -x "$TL/bin/x86_64-linux/bibtex" ] || \
    { echo "build_modern.sh: run $HERE/bootstrap_texlive.sh first" >&2; exit 1; }

# --- local texmf additions and font-map fix (TS1 cm-super -> Latin Modern) ---
mkdir -p "$TL/texmf-local/tex/latex"
cp -r "$HERE/texmf-local/tex/latex/." "$TL/texmf-local/tex/latex/"
python3 "$TL/mktexlsr.py" "$TL" texmf-local
python3 "$HERE/map_ts1_lm.py" "$TL"

echo "== clean build directory =="
# verification/ holds the recorded evidence for a previous build, not build
# output, so it is carried across rather than deleted.
keep=$(mktemp -d)
if [ -d "$BUILD/verification" ]; then mv "$BUILD/verification" "$keep/"; fi
rm -rf "$BUILD"
mkdir -p "$BUILD"
if [ -d "$keep/verification" ]; then mv "$keep/verification" "$BUILD/"; fi
rm -rf "$keep"
cp "$SRC/main.tex" "$SRC/references.bib" "$BUILD/"
cp -r "$SRC/sections" "$BUILD/"
ls "$BUILD"

# Reproducibility: pdfTeX stamps /CreationDate, /ModDate and derives the
# trailer /ID from the clock.  Pinning SOURCE_DATE_EPOCH makes byte-identical
# rebuilds possible, so that the published PDF SHA-256 is checkable.
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-1794268800}   # 2026-11-10T00:00:00Z

. "$TL/texenv.sh"
cd "$BUILD"

echo
echo "== pass 1: pdflatex =="
pdflatex -interaction=nonstopmode "$JOB.tex" >/dev/null 2>&1 || true
grep -cE "^! " "$JOB.log" | sed 's/^/   errors: /'
[ -s missfont.log ] && { echo "   missfont.log:"; sed 's/^/     /' missfont.log; }

echo "== pass 2: bibtex =="
bibtex "$JOB" 2>&1 | sed 's/^/   /'
[ -f "$JOB.bbl" ] || { echo "   FATAL: no .bbl produced" >&2; exit 1; }
wc -l < "$JOB.bbl" | sed 's/^/   bbl lines: /'

echo "== pass 3: pdflatex =="
pdflatex -interaction=nonstopmode "$JOB.tex" >/dev/null 2>&1 || true
echo "== pass 4: pdflatex =="
pdflatex -interaction=nonstopmode "$JOB.tex" >/dev/null 2>&1 || true

[ -f "$JOB.pdf" ] || { echo "   FATAL: no PDF produced" >&2; exit 1; }

echo
echo "== summary =="
for pat in '^! ' 'Citation .* undefined' 'Reference .* undefined' \
           'Overfull .hbox' 'Underfull .hbox' 'Missing character' \
           'LaTeX Warning: .*hyperref' 'Font Warning'; do
    printf "   %-34s %s\n" "$pat" "$(grep -cE "$pat" "$JOB.log")"
done
echo "   $(ls -l "$JOB.pdf" | awk '{print "pdf bytes:", $5}')"
echo "   pdf sha256: $(sha256sum "$JOB.pdf" | cut -d' ' -f1)"
