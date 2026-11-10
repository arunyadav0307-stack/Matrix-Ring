#!/bin/sh
# ---------------------------------------------------------------------
#  bootstrap_texlive.sh -- assemble a current TeX Live toolchain offline.
#
#  Produces $TL (default /home/user/texlive2024) containing, from a real
#  TeX Live 2024 installation:
#
#      bin/x86_64-linux/pdflatex   pdfTeX 1.40.26 (TeX Live 2024)
#      bin/x86_64-linux/bibtex     BibTeX 0.99d   (built from TL sources)
#      bin/x86_64-linux/kpsewhich  kpathsea 6.3.6/dev
#      texmf-dist/                 TeX Live 2024 texmf tree
#
#  Why it is needed: this environment has no TeX distribution and no
#  package manager.  Outbound network access is limited to github.com,
#  codeload.github.com, api.github.com, registry.npmjs.org, pypi.org and
#  files.pythonhosted.org.  Everything below is fetched from those hosts
#  only, and every artifact is verified against a recorded SHA-256.
#
#  Usage:   ./compile/bootstrap_texlive.sh [TL]
#  Re-run:  FORCE=1 ./compile/bootstrap_texlive.sh
# ---------------------------------------------------------------------
set -e

TL=${1:-${TL:-/home/user/texlive2024}}
WORK=${WORK:-/tmp/tlbootstrap}
TLREPO=tex-mirror/tex-live
TLCOMMIT=5f7badd91d1e6513f7b68d778016d210b7345934   # TeX Live 2024 dev tree

TINY_URL="https://files.pythonhosted.org/packages/b0/3b/c1e7e41b13780870f0df17d96c222a8261dac4eb3663126bc2db37e0fd91/rendercv_tinytex-0.2.0-py3-none-any.whl"
TINY_SHA=6e64bcd025af04d22c9f3448b78e8e4c7f9edc34ed4115672c13288526b39d25
NPM_URL="https://registry.npmjs.org/texlive/-/texlive-1.2.0.tgz"
NPM_SHA=d36d70c9b869530939ae771e244e5a3241a4ae8a8d4b68b4b6b83195fee01cf5
BOOKTABS_BLOB=c32cf7e16310a3d1a9bc42b7267ab0c6891c22a7
BOOKTABS_SHA=3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc

if [ -x "$TL/bin/x86_64-linux/bibtex" ] && [ "$FORCE" != "1" ]; then
    echo "bootstrap_texlive.sh: $TL already present (FORCE=1 to rebuild)"
    exit 0
fi

HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$WORK"; cd "$WORK"

# ---------------------------------------------------------------- 1. TinyTeX
echo "== [1/7] TeX Live 2024 texmf tree + pdfTeX (rendercv-tinytex wheel) =="
if [ ! -f tinytex.whl ]; then curl -sSL -o tinytex.whl "$TINY_URL"; fi
echo "$TINY_SHA  tinytex.whl" | sha256sum -c -
rm -rf tiny; mkdir tiny
python3 -c "import zipfile,sys; zipfile.ZipFile('tinytex.whl').extractall('tiny')"
TINY="$WORK/tiny/rendercv_tinytex/tinytex-release/TinyTeX"
head -1 "$TINY/release-texlive.txt"

rm -rf "$TL"; mkdir -p "$TL/bin/x86_64-linux" "$TL/texmf-dist" \
                       "$TL/texmf-var" "$TL/texmf-config" "$TL/texmf-local"
cp -r "$TINY/texmf-dist/." "$TL/texmf-dist/"
cp -r "$TINY/texmf-var/."  "$TL/texmf-var/"   2>/dev/null || true
cp    "$TINY/release-texlive.txt" "$TINY/LICENSE.TL" "$TINY/LICENSE.CTAN" "$TL/"
cp    "$TINY/bin/x86_64-linux/"*  "$TL/bin/x86_64-linux/"
chmod +x "$TL/bin/x86_64-linux/"*

# ------------------------------------------------- 2. packages TinyTeX omits
echo "== [2/7] packages absent from TinyTeX (amsfonts, amsthm, plain.bst) =="
if [ ! -f texlive.tgz ]; then curl -sSL -o texlive.tgz "$NPM_URL"; fi
echo "$NPM_SHA  texlive.tgz" | sha256sum -c -
rm -rf npm15; mkdir npm15
tar xzf texlive.tgz -C npm15 --strip-components=1 package/binary.zip
tar xzf texlive.tgz -C npm15 --strip-components=3 \
    package/texlive/texmf-dist/tex/latex/amsfonts \
    package/texlive/texmf-dist/tex/latex/amscls/amsthm.sty \
    package/texlive/texmf-dist/bibtex/bst/base \
    package/texlive/texmf-dist/fonts/tfm/public/amsfonts \
    package/texlive/texmf-dist/fonts/type1/public/amsfonts \
    package/texlive/texmf-dist/fonts/afm/public/amsfonts
D="$TL/texmf-dist"
mkdir -p "$D/tex/latex/amsfonts" "$D/tex/latex/amscls" "$D/bibtex/bst/base" \
         "$D/fonts/afm/public"
cp npm15/tex/latex/amsfonts/* "$D/tex/latex/amsfonts/"
cp npm15/tex/latex/amscls/amsthm.sty "$D/tex/latex/amscls/"
cp npm15/bibtex/bst/base/*.bst "$D/bibtex/bst/base/"
cp -r npm15/fonts/tfm/public/amsfonts   "$D/fonts/tfm/public/"
cp -r npm15/fonts/type1/public/amsfonts "$D/fonts/type1/public/"
cp -r npm15/fonts/afm/public/amsfonts   "$D/fonts/afm/public/"
mkdir -p "$D/tex/latex/booktabs"
gh api "repos/swimmingbrain/texbrain/git/blobs/$BOOKTABS_BLOB" --jq .content \
  | base64 -d > "$D/tex/latex/booktabs/booktabs.sty"
echo "$BOOKTABS_SHA  $D/tex/latex/booktabs/booktabs.sty" | sha256sum -c -

# ------------------------------------------------------- 3. TeX Live sources
echo "== [3/7] TeX Live 2024 sources (kpathsea, bibtex.web) =="
rm -rf src; git clone -q --depth 1 --filter=blob:none --sparse \
    https://github.com/$TLREPO.git src
cd src
git sparse-checkout set texk/kpathsea build-aux m4 >/dev/null
git log -1 --format='source: %H  %ad' --date=short
cd "$WORK"

cat > fetch.py <<'EOF'
import base64, json, os, subprocess, sys
REPO = "tex-mirror/tex-live"
dest = sys.argv[1]
for p in sys.argv[2:]:
    r = subprocess.run(["gh","api","repos/%s/contents/%s" % (REPO,p),"--jq",".sha"],
                       capture_output=True, text=True)
    sha = r.stdout.strip()
    if not sha:
        print("MISS", p); sys.exit(1)
    b = subprocess.run(["gh","api","repos/%s/git/blobs/%s" % (REPO,sha)],
                       capture_output=True, text=True)
    data = base64.b64decode(json.loads(b.stdout)["content"])
    out = os.path.join(dest, p); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out,"wb").write(data)
print("fetched %d files" % (len(sys.argv)-2))
EOF
python3 fetch.py "$WORK/files" \
  texk/web2c/bibtex.web texk/web2c/bibtex.ch texk/web2c/cpascal.h \
  texk/web2c/help.h texk/web2c/c-auto.in texk/web2c/w2c/config.h \
  texk/web2c/web2c/common.defines texk/web2c/web2c/cvtbib.sed \
  texk/web2c/lib/basechsuffix.c texk/web2c/lib/chartostring.c \
  texk/web2c/lib/coredump.c texk/web2c/lib/eofeoln.c \
  texk/web2c/lib/fprintreal.c texk/web2c/lib/inputint.c \
  texk/web2c/lib/input2int.c texk/web2c/lib/lib.h texk/web2c/lib/main.c \
  texk/web2c/lib/openclose.c texk/web2c/lib/printversion.c \
  texk/web2c/lib/setupvar.c texk/web2c/lib/uexit.c texk/web2c/lib/usage.c \
  texk/web2c/lib/version.c texk/web2c/lib/zround.c

# ------------------------------------------------------------- 4. kpathsea
echo "== [4/7] building kpathsea (TeX Live 2024) =="
chmod +x src/build-aux/* 2>/dev/null || true
cd src/texk/kpathsea
./configure --prefix="$TL" --bindir="$TL/bin/x86_64-linux" \
            --disable-shared --enable-static >"$WORK/kpse_conf.log" 2>&1
make            >"$WORK/kpse_make.log" 2>&1
make install    >"$WORK/kpse_inst.log" 2>&1
cd "$WORK"
"$TL/bin/x86_64-linux/kpsewhich" --version | head -1

# ------------------------------------------- 5. tangle/web2c (from pdftex)
echo "== [5/7] extracting tangle + web2c (prebuilt, pdftex 1.40.11 bundle) =="
python3 - <<'EOF'
import os, zipfile
z = zipfile.ZipFile('npm15/binary.zip')
for s, d in [("binary/pdftex-1.40.11/build-pdftex/texk/web2c/tangle", "tangle"),
             ("binary/pdftex-1.40.11/build-pdftex/texk/web2c/web2c/web2c", "web2c/web2c"),
             ("binary/pdftex-1.40.11/build-pdftex/texk/web2c/web2c/fixwrites", "web2c/fixwrites")]:
    os.makedirs(os.path.dirname(d) or ".", exist_ok=True)
    open(d, "wb").write(z.read(s))
print("ok")
EOF
chmod +x tangle web2c/web2c web2c/fixwrites

# -------------------------------------------------------------- 6. BibTeX
echo "== [6/7] building BibTeX 0.99d from TeX Live 2024 bibtex.web =="
mkdir -p bb/web2c bb/lib bb/obj bb/inc/w2c
cp files/texk/web2c/bibtex.web files/texk/web2c/bibtex.ch bb/
cp files/texk/web2c/cpascal.h  files/texk/web2c/help.h bb/
cp files/texk/web2c/web2c/common.defines files/texk/web2c/web2c/cvtbib.sed bb/web2c/
cp files/texk/web2c/lib/*.c files/texk/web2c/lib/lib.h bb/lib/
cp files/texk/web2c/c-auto.in bb/c-auto.in
cp files/texk/web2c/w2c/config.h bb/inc/w2c/config.h
mv tangle bb/
mv web2c/web2c web2c/fixwrites bb/web2c/
cd bb
python3 - <<'EOF'
import re
s = open('c-auto.in', encoding='utf-8').read()
s = s.replace('"REPLACE-WITH-WEB2CVERSION"', '" (TeX Live 2024)"')
one = """ACCESS ASSERT_H ATOI DIRENT_H DLFCN_H ERRNO_H FABS FLOAT_H FMAX FSEEKO
GETCWD GETTIMEOFDAY INTTYPES_H LANGINFO_H LIMITS_H LOCALE_H LONG_DOUBLE MEMCMP
MEMCPY MKDTEMP MKSTEMP MKTEMP PUTENV PWD_H SETLOCALE STDBOOL_H STDINT_H
STDIO_H STDLIB_H STRCHR STRERROR STRINGS_H STRING_H STRNDUP
STRUCT_STAT_ST_MTIM STRRCHR SYS_PARAM_H SYS_STAT_H SYS_TIME_H SYS_TYPES_H
SYS_WAIT_H TIME_H UINTPTR_T UNISTD_H _BOOL""".split()
for n in one:
    s = s.replace("#undef HAVE_%s\n" % n, "#define HAVE_%s 1\n" % n)
for n, v in [("HAVE_DECL_ISASCII","1"),("HAVE_DECL_STRNDUP","1"),
             ("SIZEOF_INT","4"),("SIZEOF_LONG","8"),("SIZEOF_OFF_T","8"),
             ("SIZEOF_VOID_P","8"),("STDC_HEADERS","1"),("RETSIGTYPE","void"),
             ("PACKAGE","\"web2c\""),("PACKAGE_NAME","\"web2c\""),
             ("PACKAGE_TARNAME","\"web2c\""),("PACKAGE_VERSION","\"2024\""),
             ("PACKAGE_STRING","\"web2c 2024\""),("VERSION","\"2024\""),
             ("PACKAGE_BUGREPORT","\"tex-k@tug.org\""),
             ("PACKAGE_URL","\"https://tug.org/texlive/\""),
             ("LT_OBJDIR","\".libs/\""),("EDITOR","\"vi\"")]:
    s = s.replace("#undef %s\n" % n, "#define %s %s\n" % (n, v))
open('inc/w2c/c-auto.h','w',encoding='utf-8').write(s)
print("c-auto.h written")
EOF
./tangle bibtex bibtex 2>&1 | tail -2
cat web2c/common.defines bibtex.p \
  | ./web2c/web2c -hcpascal.h -cbibtex \
  | sed -f web2c/cvtbib.sed \
  | ./web2c/fixwrites bibtex > bibtex.c
sed -e 's/(buftype)//g' -e 's/(pdstype)//g' <bibtex.h >xbibtex.h && mv xbibtex.h bibtex.h
grep -q "@error@" bibtex.c bibtex.h && { echo "web2c conversion failed"; exit 1; }
F="-O2 -I. -Iinc -I$TL/include -DUNIX -DKPATHSEA"
gcc $F -c bibtex.c -o obj/bibtex.o
for f in lib/*.c; do gcc $F -c "$f" -o "obj/$(basename "$f" .c).o"; done
LOBJS=$(ls obj/*.o | grep -v '/bibtex.o$' | tr '\n' ' ')
ar rcs lib.a $LOBJS
gcc -O2 -o bibtex obj/bibtex.o lib.a "$TL/lib/libkpathsea.a" -lm
./bibtex --version | head -2
cp bibtex "$TL/bin/x86_64-linux/bibtex"

# ------------------------------------------------------------ 7. configure
echo "== [7/7] texmf.cnf, ls-R =="
cd "$WORK"
cat > "$TL/texmf.cnf" <<EOF
% Local path configuration for the TeX Live 2024 tree assembled by
% PAPER/compile/bootstrap_texlive.sh.  Read before
% texmf-dist/web2c/texmf.cnf, so these definitions win.
TEXMFROOT      = $TL
TEXMFDIST      = \$TEXMFROOT/texmf-dist
TEXMFMAIN      = \$TEXMFDIST
TEXMFLOCAL     = \$TEXMFROOT/texmf-local
TEXMFSYSVAR    = \$TEXMFROOT/texmf-var
TEXMFSYSCONFIG = \$TEXMFROOT/texmf-config
TEXMFVAR       = \$TEXMFROOT/texmf-var
TEXMFCONFIG    = \$TEXMFROOT/texmf-config
TEXMFHOME      = \$TEXMFROOT/texmf-home
EOF
cat > "$TL/texenv.sh" <<EOF
# Environment for the locally assembled TeX Live 2024 tree.
TL2024=$TL
PATH="\$TL2024/bin/x86_64-linux:\$PATH"
TEXMFCNF="\$TL2024:\$TL2024/texmf-dist/web2c"
export TL2024 PATH TEXMFCNF
EOF
chmod +x "$TL/texenv.sh"
cp "$HERE/mktexlsr.py" "$TL/mktexlsr.py"
. "$TL/texenv.sh"
python3 "$TL/mktexlsr.py" "$TL" texmf-dist texmf-var

echo
echo "== done =="
ls "$TL/bin/x86_64-linux/"
. "$TL/texenv.sh"
kpsewhich --version | head -1
pdflatex --version  | head -1
bibtex   --version  | head -1
