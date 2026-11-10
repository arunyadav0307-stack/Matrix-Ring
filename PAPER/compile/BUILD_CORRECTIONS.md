# Build correction log — Phase 8B (append-only)

**Purpose.** Every change made to the manuscript sources in order to build them
with a current TeX Live distribution, with the reason and the evidence.

This file is **append-only**: entries are never edited or removed, only added.
An entry may later be marked `SUPERSEDED`, but the original text stays.

A correction is recorded here whether or not it changes the rendered output.
The rule applied throughout is from the Phase 8B brief: *do not alter
mathematical statements or numerical results merely to silence a compiler
warning.* So far no correction has touched the mathematics.

---

## C-1 — `\AUTHORPLACEHOLDER` used before it is defined — **FIXED**

**Date.** 2026-11-09.

**Symptom.** Pass 1 of the modern build aborted (`pdflatex` exit status 1, no
PDF produced):

```
! Undefined control sequence.
<argument> \AUTHORPLACEHOLDER

l.39 ...e!45!black,pdfauthor={\AUTHORPLACEHOLDER}}
```

**Exact source.** `PAPER/main.tex`. The macro was defined in the *notation*
block at line 68, but consumed by `\hypersetup{pdfauthor={\AUTHORPLACEHOLDER}}`
at line 39 — twenty-nine lines earlier.

**Why it is an error now and was not in Phase 8A.** `hyperref` must convert
`pdfauthor`, `pdftitle` and friends into a PDFDocEncoded string, and it does
that **when `\hypersetup` runs**, not at `\begin{document}`. Current `hyperref`
(2024-11-05, v7.01b) therefore expands the argument immediately, and the
undefined macro raises. The Phase 8A build used `hyperref 2012/11/06 v6.83m`
from TeX Live 2015, whose `\pdfstringdef` deferred the expansion until the
metadata was actually written, by which time the macro existed. The manuscript
was *always* using the macro before defining it; the old engine merely
tolerated the ordering.

This is a latent defect in the source, not an engine incompatibility: LaTeX has
no forward references for macro definitions.

**Correction.** Minimal and order-only. The `\newcommand{\AUTHORPLACEHOLDER}`
line was moved out of the notation block and placed immediately before
`\usepackage[hypertexnames=false]{hyperref}`, with a five-line comment
explaining the ordering constraint so that the line is not moved back. Nothing
else changed: no other line of `main.tex` was touched, the macro's definition
is byte-identical, and the two other use sites (`\author{...}` at line 96 and
the header comment at line 10) are unaffected.

**Effect on the rendered output.** None beyond turning a failed build into a
successful one. The PDF author field still contains the same placeholder text.

**Verification.** `sha256(main.tex)` before: `10eadbd148321d91ec76072a594f7e477ae588bfe272d96c00c33dfd7addc1ae`;
after: `e0886ee5d68b428b7e095289cd31b094593bd96cff0a7f9330fe80f1cd6427c4`.
`git diff main.tex` moves exactly one four-line macro definition and adds a
comment. The Phase 8A PDF is untouched and was not rebuilt.

---

## C-2 — `\Hom` is used but never defined — **FIXED**

**Date.** 2026-11-10.

**Symptom.** Pass 1 of the modern build aborted (exit status 1, no PDF):

```
! Undefined control sequence.
l.111 \Hom
```
at `sections/03_preliminaries.tex:111`, and a second occurrence at
`sections/04_cyclic_galois.tex:224`.

**Exact source.** `sections/03_preliminaries.tex:111`

```latex
\psi_C : C \longrightarrow \Hom(C,\F_q),\qquad
```
and `sections/04_cyclic_galois.tex:224`

```latex
\ldots \text{ and } (C,R) \in \Hom(\ldots)
```

**Evidence that the macro was never defined.** A `grep` for `\Hom` over
`main.tex` and every file in `sections/` returns the two *use* sites and no
`\newcommand`, `\DeclareMathOperator` or `\def`. An audit of all 91 macros used
in the sources against the loaded packages found `\Hom` to be the only genuinely
undefined one.

**Why this is a real defect and not merely an engine difference.** The Phase 8A
PDF was read with PyMuPDF and its text extracted: the word `Hom` occurs **zero**
times in the shipped 39-page PDF, and the two affected sentences read

```
ψC : C −→ Fq(S/C⊥,Fq)      (Section 3)
... into Fq (C,R) ...      (Section 4)
```

i.e. the 2010-vintage engine silently dropped the operator name, leaving two
sentences that do not parse. This is a **pre-existing typographical defect in
the released manuscript**, not something introduced by the modern build. It is
worth stressing that no TeX error appeared in the Phase 8A log for this, so the
defect was invisible to a log-only check.

**Correction.** One line added to `main.tex`, in the notation block immediately
after the analogous `\ann` operator:

```latex
\newcommand{\Hom}{\operatorname{Hom}}
```

This is the same idiom already used by the manuscript for `\tr`, `\Tr`, `\ann`,
`\rev`, `\Hull`, `\swt`, `\wt`, `\Aut`, `\GL`, `\Jac` and `\rad`, so the new
macro is consistent with the file's existing conventions.

**Effect on the rendered output.** The two sentences now read
`ψ_C : C −→ Hom(C, F_q)` and the corresponding `Hom(C,R)`; i.e. the PDF becomes
*correct* where before it was wrong. No other text moves.

**Verification.** `sha256(main.tex)` after: `d680c57d1b3e6e320009d0e61696a71a3054d5e196fd2e5a8a18a4cf8817baf6`.
Both occurrences confirmed present in the rebuilt PDF text. The Phase 8A PDF
was **not** rebuilt and remains byte-for-byte as shipped.

---

## C-3 — unbraced `]]` inside an optional argument — **FIXED**

**Date.** 2026-11-10.

**Symptom.** After C-2 the build aborted with four hard errors, all from one
line:

```
! Extra }, or forgotten $.
! Missing $ inserted.
! Missing } inserted.
! Missing $ inserted.
l.324 \begin{example}[certifying $[[20,2,10;18]]_4$]
```

**Exact source.** `sections/08_certification.tex:324`:

```latex
\begin{example}[certifying $[[20,2,10;18]]_4$]\label{ex:certify}
```

**Cause.** LaTeX scans an optional argument with TeX's `[...]` matcher, which
stops at the **first** `]` that is not inside a brace group. The quantum-code
tuple `[[20,2,10;18]]` contains two consecutive `]`. The first one terminates
the optional argument, so `\begin{example}` receives `[certifying $[[20,2,10;18`
and the remainder `]]_4$]` is typeset as body text — producing the four errors
above.

This is a general hazard for this manuscript, whose central object is written
`[[n,k,d;c]]_q`. A sweep of **every** `\begin/\end{...}[...]` and
`\section[...]`/`\subsection[...]` in `main.tex` and all twelve section files
found exactly **one** unbraced-`]` site, namely the one above: all other
`[[...]]` tuples appear in maths mode in the body, where no optional-argument
scan is involved.

**Correction.** One brace pair and a two-line comment:

```latex
% NOTE: the optional argument is braced as [{...}].  LaTeX's [ ... ] scanner
% stops at the first unbraced ']', and [[20,2,10;18]] contains two.
\begin{example}[{certifying $[[20,2,10;18]]_4$}]\label{ex:certify}
```

The braces are stripped by the argument scanner, so the typeset heading is
identical to what was intended.

**Effect on the rendered output.** The example heading now reads
"Example (certifying $[[20,2,10;18]]_4$)" instead of being mangled. No
mathematics altered.

**Verification.** `sha256(sections/08_certification.tex)` after:
`fb853d83b391a1f60377d311e37d2d437d3d5ba363449bbdbc68b14c9443a8af`.

---

## C-4 — missing TS1 (text-companion) fonts: `tcrm1095 at 600 not found` — **FIXED**

**Date.** 2026-11-10.

**Symptom.** After C-1/C-2/C-3 the log contained **no** TeX error, but the run
still ended fatally after page 37 with no PDF:

```
!pdfTeX error: pdflatex (file tcrm1095): Font tcrm1095 at 600 not found
 ==> Fatal error occurred, no output PDF file produced!
```
and `missfont.log` contained
`mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095`.

**Cause.** `tcrm1095` is TS1/cmr/m/n at 10.95 pt (10.95 pt = `\small` in an
11 pt `article`). The `.tfm` metrics are present
(`texmf-dist/fonts/tfm/jknappen/ec/tcrm1095.tfm`) but there is **no Type1
outline, no `.map` entry and no Metafont source** anywhere in the tree, so
pdfTeX can neither embed nor generate the font.

The font is *requested at all* because of a kernel change. Since the LaTeX
kernel release 2020/02/02 the text-companion symbols are declared with TS1 as
their default encoding:

```latex
\DeclareTextSymbolDefault{\textbullet}{TS1}
```

Previously `\textbullet` — and therefore the bullet of every
`\begin{itemize}` — came from the OMS maths-symbol font, which is present. This
is why the 2010 engine never needed `tcrm`. The TS1 shapes of Computer Modern
belong to the `cm-super` collection, which is not part of the TeX tree
available in this environment (see Task A); cm-super cannot be fetched, and
Metafont is not available either.

**Identification.** The trigger was located by bisection: each section file was
compiled alone, and `02_literature`, `07_quantum` and
`appendix_reproducibility` each requested `tcrm`. Binary search inside
`02_literature` reduced this to line 89, the first `\begin{itemize}`. A
three-line document consisting only of `\begin{itemize}\item a\end{itemize}`
reproduces the failure; the same document without the `itemize` compiles.

**Why an NFSS-level substitution does not work here.** The natural fix is a
local `ts1cmr.fd` that silently substitutes TS1/cmr with TS1/lmr
(`\DeclareFontShape{TS1}{cmr}{m}{n}{<->ssub * lmr/m/n}{}`). `kpsewhich -all
ts1cmr.fd` confirms the local copy wins over `texmf-dist/tex/latex/base`. It is
nevertheless **not read**: the kernel *preloads* `ts1cmr.fd` when the format is
dumped, and TinyTeX ships a prebuilt `pdflatex.fmt` in which `TS1/cmr/m/n` is
already defined. This was verified directly — the control sequence is defined
*before* `\documentclass`:

```
@@@PRE=macro:->\<5><6><7><8><9><10><10.95><12>...>genb*tcrm
```

**Correction.** The substitution is therefore made one level lower, in the
pdfTeX font map: `compile/map_ts1_lm.py` appends 237 entries mapping every
`tcrm`/`tcbx`/`tcsl`/… `.tfm` in the tree to the corresponding Latin Modern TS1
outline, e.g.

```
tcrm1095 LMRoman10-Regular " enclmts1 ReEncodeFont " <lm-ts1.enc <lmr10.pfb
```

Latin Modern is the outline successor of Computer Modern and shares its
metrics, so the substitution is visually invisible.

**Deliberate choice of the map over a format rebuild.** Rebuilding
`pdflatex.fmt` would also pick up a local `ts1cmr.fd`, but it would have to
reload the hyphenation patterns; if they were not reloaded identically the line
and page breaking would change, and the whole point of Phase 8B is to confirm
that the manuscript still sets the way it did. Patching the map leaves the
format, the metrics, the patterns and hence every line break exactly as
shipped.

**Scope.** TS1 only. The body font remains OT1/cmr, so the main text, the
headings and all mathematics are untouched. This is a property of the
*distribution*, not of the manuscript: **no manuscript source was modified.**

**Effect on the rendered output.** The bullet glyph of `itemize`, which is the
only TS1 glyph the manuscript uses, is drawn from Latin Modern instead of
cm-super. Metrics come from the unchanged CM `.tfm`, so spacing is identical.

**Verification.** `main.pdf` is now produced: 39 pages, 0 errors, 0 missing
characters, 0 `Font Warning`, empty `missfont.log`. The map patch is idempotent
and reproducible (`compile/map_ts1_lm.py`); the NFSS-level fallback is kept in
`compile/texmf-local/` for the case where the format is ever regenerated.

---

## C-5 — empty PDF `/Title` and four `hyperref` PDF-string warnings — **FIXED**

**Date.** 2026-11-10.

**Symptom.** The build succeeded, but the log contained four warnings:

```
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\leavevmode@ifvmode' on input line 47.
(hyperref)                \kern 1.8254pt
(hyperref)                removed on input line 47.
```
(2 x `\leavevmode@ifvmode`, 2 x `\kern 1.8254pt`) and the resulting PDF had

```
/Title  = (empty)
/Author = [AUTHOR METADATA TO BE SUPPLIED]
```

**Cause.** Two separate, minor metadata defects.

1. `pdfauthor={\AUTHORPLACEHOLDER}` expands to `\textbf{[\,AUTHOR METADATA TO
   BE SUPPLIED\,]}`. A PDF document-information string cannot hold formatting,
   so `hyperref` strips `\textbf` (which contributes `\leavevmode@ifvmode`) and
   `\,` (which is `\kern 1.8254pt`) and warns four times. The resulting author
   string was in fact correct, so this was purely noise — but it is noise that
   hides real metadata problems.
2. `hyperref` does **not** read `\title` unless it is given the `pdfusetitle`
   option, so the PDF's `/Title` field was empty even though the manuscript
   sets a title. A submission system or reference manager reading the PDF
   would see an untitled document.

**Correction.** One definition changed and one package option added, in
`main.tex`:

```latex
\newcommand{\AUTHORPLACEHOLDER}{%
  \texorpdfstring{\textbf{[\,AUTHOR METADATA TO BE SUPPLIED\,]}}%
                 {[AUTHOR METADATA TO BE SUPPLIED]}}
% pdfusetitle makes hyperref copy \title and \author into the PDF document
% information dictionary; without it the /Title field of the PDF is empty.
% \texorpdfstring above supplies the plain-text form used there, because a
% PDF string cannot carry \textbf or \, (a kern) -- hyperref silently strips
% them and warns.  See compile/BUILD_CORRECTIONS.md, correction C-5.
\usepackage[hypertexnames=false,pdfusetitle]{hyperref}
```

`\texorpdfstring` is the idiomatic mechanism for "one macro, two forms": the
typeset title block keeps the bold small-caps-spaced placeholder, while the PDF
string gets the plain text. It does not duplicate the literal, so the two forms
cannot drift apart. `\texorpdfstring` is defined by `hyperref` and is only
*expanded* at use time, after `hyperref` has been loaded, so defining
`\AUTHORPLACEHOLDER` in terms of it before `\usepackage{hyperref}` is safe.

**Effect on the rendered output.** The visible title block is unchanged. The
PDF metadata is now

```
/Title  = Quantum Error-Correcting Codes from Galois Hulls of Cyclic
          Codes over Noncommutative Matrix Rings
/Author = [AUTHOR METADATA TO BE SUPPLIED]
```

and all four warnings are gone. No mathematics altered.

**Verification.** The rebuilt log contains **zero** occurrences of the string
`Warning` in any form (`LaTeX`, `Package`, `pdfTeX`, `Font`, `Class`). PDF:
39 pages, 563 659 bytes, sha256
`69265efb21a4c01d4e6b74bcac5e19f954a11e013aaa0eef7856b089ebe522fd`.
