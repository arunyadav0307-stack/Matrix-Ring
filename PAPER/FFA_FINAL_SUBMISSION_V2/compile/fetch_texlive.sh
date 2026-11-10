#!/bin/sh
# ---------------------------------------------------------------------
#  (Re-)assemble the recovered TeX tree from npm.
#
#  Needs outbound access to registry.npmjs.org only.  Idempotent: if the
#  tree already exists it does nothing unless FORCE=1.
#
#  What it does, and why, is documented in compile/README.md.
# ---------------------------------------------------------------------
set -e

TL=${TL:-/home/user/.texlive}
WORK=${WORK:-/tmp/texlive_build}
PKG_URL="https://registry.npmjs.org/texlive/-/texlive-1.2.0.tgz"
PKG_SHA="d36d70c9b869530939ae771e244e5a3241a4ae8a8d4b68b4b6b83195fee01cf5"

if [ -x "$TL/bin/pdftex" ] && [ "$FORCE" != "1" ]; then
    echo "fetch_texlive.sh: tree already present at $TL (FORCE=1 to rebuild)"
    exit 0
fi

mkdir -p "$WORK"
cd "$WORK"

echo "== downloading texlive.js 1.2.0 (44 MB) =="
[ -f texlive.tgz ] || curl -sSL -o texlive.tgz "$PKG_URL"
echo "$PKG_SHA  texlive.tgz" | sha256sum -c -

echo "== unpacking =="
rm -rf package
mkdir -p package
tar xzf texlive.tgz -C package

echo "== extracting the native pdftex binary from binary.zip =="
rm -rf binary
mkdir -p binary
( cd package/package && unzip -q -o binary.zip \
    "binary/pdftex-1.40.11/build-pdftex/texk/web2c/pdftex" -d "$WORK/binary" )

echo "== assembling $TL =="
rm -rf "$TL"
mkdir -p "$TL/bin" "$TL/texmf-dist" "$TL/texmf-var" "$TL/texmf-config"
cp "$WORK/binary/binary/pdftex-1.40.11/build-pdftex/texk/web2c/pdftex" "$TL/bin/pdftex"
chmod +x "$TL/bin/pdftex"
cp -r package/package/texlive/texmf-dist/. "$TL/texmf-dist/"
cp -r package/package/texlive/texmf-var/.  "$TL/texmf-var/"
[ -d package/package/texlive/texmf-config ] &&
    cp -r package/package/texlive/texmf-config/. "$TL/texmf-config/" || true
chmod -R u+w "$TL"

cat > "$TL/mytexmf.cnf" <<EOF
% local overrides for the recovered TeX Live 2015 texmf tree
TEXMFROOT      = $TL
TEXMFDIST      = \$TEXMFROOT/texmf-dist
TEXMFMAIN      = \$TEXMFDIST
TEXMFSYSVAR    = \$TEXMFROOT/texmf-var
TEXMFSYSCONFIG = \$TEXMFROOT/texmf-config
TEXMFVAR       = \$TEXMFROOT/texmf-var
TEXMFCONFIG    = \$TEXMFROOT/texmf-config
TEXMFLOCAL     = \$TEXMFROOT/texmf-local
TEXMFHOME      = \$TEXMFROOT/texmf-home
EOF

echo "== three packages absent from the tree: booktabs, enumitem, xcolor =="
echo "   (retrieved from GitHub mirrors of the CTAN sources; see README.md)"
mkdir -p "$TL/texmf-dist/tex/latex/booktabs" \
         "$TL/texmf-dist/tex/latex/enumitem" \
         "$TL/texmf-dist/tex/latex/xcolor"
if command -v gh >/dev/null 2>&1; then
    gh api "repos/swimmingbrain/texbrain/contents/static/texlive/cache/booktabs.sty" \
        --jq .content | base64 -d > "$TL/texmf-dist/tex/latex/booktabs/booktabs.sty"
    gh api "repos/SeanDaBlack/KelloggBot/contents/resumeSrc/packages/enumitem.sty" \
        --jq .content | base64 -d > "$TL/texmf-dist/tex/latex/enumitem/enumitem.sty"
    gh api "repos/oetiker/lshort/contents/src/xcolor.sty" \
        --jq .content | base64 -d > "$TL/texmf-dist/tex/latex/xcolor/xcolor.sty"
else
    echo "   gh not available: place booktabs.sty, enumitem.sty and xcolor.sty"
    echo "   manually in $TL/texmf-dist/tex/latex/{booktabs,enumitem,xcolor}/"
fi

echo
echo "== verifying =="
. "$(dirname "$0")/texenv.sh" 2>/dev/null || true
"$TL/bin/pdftex" --version 2>&1 | head -1
ls -l "$TL/texmf-dist/tex/latex/booktabs/booktabs.sty" \
      "$TL/texmf-dist/tex/latex/enumitem/enumitem.sty" \
      "$TL/texmf-dist/tex/latex/xcolor/xcolor.sty" 2>/dev/null || true
sha256sum "$TL/texmf-dist/tex/latex/booktabs/booktabs.sty" \
          "$TL/texmf-dist/tex/latex/enumitem/enumitem.sty" \
          "$TL/texmf-dist/tex/latex/xcolor/xcolor.sty" 2>/dev/null || true
echo "fetch_texlive.sh: done -> $TL"
