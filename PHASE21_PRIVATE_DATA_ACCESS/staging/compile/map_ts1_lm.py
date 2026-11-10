#!/usr/bin/env python3
"""Supply the missing TS1 (text-companion) fonts from Latin Modern.

Background
----------
Since the LaTeX kernel release 2020/02/02 the text-companion symbols are
declared with TS1 as their default encoding:

    \\DeclareTextSymbolDefault{\\textbullet}{TS1}

Before that, \\textbullet (and hence every `\\begin{itemize}' bullet) came from
the OMS maths-symbol font.  The TS1 shapes of the Computer Modern families
(`tcrm1095' etc.) belong to the `cm-super' collection, which this TeX tree does
not contain: only the .tfm metrics are present, with no Type1 outline.  pdfTeX
then aborts the run with

    !pdfTeX error: pdflatex (file tcrm1095): Font tcrm1095 at 600 not found

Because TinyTeX's `pdflatex.fmt' already has the TS1/cmr font definitions baked
in (the kernel preloads `ts1cmr.fd' at format-dump time), an NFSS-level `ssub'
substitution in a local `ts1cmr.fd' is never read.  The substitution therefore
has to be made one level lower, in the pdfTeX font map -- which is also the
most conservative choice: the format, the metrics, the hyphenation patterns and
hence the line- and page-breaking are left exactly as shipped.

Latin Modern is the outline successor of Computer Modern and shares its
metrics, so the substitution is visually invisible.  Only TS1 glyphs are
affected; the body font of the manuscript remains OT1/cmr.

The script is idempotent: it appends its block to `pdftex.map' once and skips
the work if the block is already present.

Usage:  python3 compile/map_ts1_lm.py [TL]
"""
import os
import re
import sys

# EC TS1 font family -> Latin Modern Type1 family (pfb stem).
FAMILY = {
    'tcrm': 'lmr',       # medium roman
    'tcsl': 'lmro',      # slanted
    'tcti': 'lmri',      # italic  (also tcit)
    'tcit': 'lmri',
    'tcbx': 'lmbx',      # bold extended
    'tcrb': 'lmb',       # demi bold
    'tcbi': 'lmbxi',     # bold italic
    'tcbl': 'lmbxo',     # bold slanted
    'tcui': 'lmu',       # unslanted italic
    'tcci': 'lmcsc',     # caps italic
    'tcss': 'lmss',      # sans serif
    'tcsi': 'lmsso',     # sans slanted/italic
    'tcsx': 'lmssbx',    # sans bold extended
    'tcso': 'lmssbo',    # sans bold oblique
    'tctt': 'lmtt',      # typewriter
    'tcst': 'lmtl',      # typewriter light
    'tcvt': 'lmvtt',     # variable typewriter
    'tcvi': 'lmvtlo',    # variable typewriter oblique
}

MARKER = '%% --- begin: TS1 -> Latin Modern substitution'


def main():
    tl = sys.argv[1] if len(sys.argv) > 1 else '/home/user/texlive2024'
    mapfile = os.path.join(tl, 'texmf-var', 'fonts', 'map', 'pdftex',
                           'updmap', 'pdftex.map')
    if not os.path.exists(mapfile):
        sys.exit('map_ts1_lm.py: no pdftex.map at %s' % mapfile)

    body = open(mapfile, encoding='utf-8', errors='replace').read()
    if MARKER in body:
        print('map_ts1_lm.py: %s already patched' % mapfile)
        return
    body = body.rstrip('\n') + '\n'

    # pfb stem -> {design size in pt: (PostScript name, encoding file, pfb)}
    lm = {}
    for line in body.splitlines():
        if not line.startswith('ts1-'):
            continue
        m = re.match(r'^ts1-([a-z]+)(\d+)\s+(\S+)\s+"([^"]*)"\s+<(\S+)'
                     r'\s+<(\S+)\s*$', line)
        if m:
            lm.setdefault(m.group(1), {})[int(m.group(2))] = \
                (m.group(3), m.group(5), m.group(6), m.group(4))

    tfmdir = os.path.join(tl, 'texmf-dist', 'fonts', 'tfm', 'jknappen', 'ec')
    tfms = sorted(f for f in os.listdir(tfmdir)
                  if re.match(r'^tc[a-z]+\d+\.tfm$', f))

    out = [MARKER + ' (added by compile/map_ts1_lm.py) ---',
           '%% Substitute every TS1 (text-companion) EC font with the matching',
           '%% Latin Modern outline.  cm-super is absent from this tree and',
           '%% pdfTeX cannot generate the fonts: only the .tfm metrics exist.',
           '%% Affects TS1 glyphs only (e.g. \\textbullet); OT1/cmr body text,',
           '%% metrics, hyphenation and page breaking are unchanged.', '']
    n = skipped = 0
    for tfm in tfms:
        m = re.match(r'^(tc[a-z]+)(\d+)\.tfm$', tfm)
        ecfam, size = m.group(1), int(m.group(2))
        if ecfam not in FAMILY:
            skipped += 1
            continue
        stem = FAMILY[ecfam]
        if stem not in lm:
            skipped += 1
            continue
        want = round(size / 100.0)
        best = min(lm[stem], key=lambda s: (abs(s - want), s))
        psname, enc, pfb, extra = lm[stem][best]
        out.append('%s%s %s "%s" <%s <%s'
                   % (ecfam, size, psname, extra, enc, pfb))
        n += 1
    out += ['', '%% --- end: TS1 -> Latin Modern substitution ---', '']

    open(mapfile, 'w', encoding='utf-8').write(body + '\n'.join(out))
    print('map_ts1_lm.py: added %d TS1 font substitutions to %s (%d skipped)'
          % (n, mapfile, skipped))


if __name__ == '__main__':
    main()
