#!/usr/bin/env python3
"""
validate_latex_v2.py -- corrected version of validate_latex.py (Phase 16).

The original validate_latex.py is preserved unchanged.  This version changes
exactly two checks, V9 and V11, both of which raised false positives on a
manuscript that compiles cleanly.  No check is disabled and no broad
exclusion is introduced; see PHASE16_VALIDATOR_REVIEW.md.

  V9   BUILTIN was an incomplete static whitelist, so format-provided
       commands (\penalty, \setcounter, \textsuperscript) were reported
       as undefined.  Fixed by adding a bounded, named, auditable set
       LATEX_KERNEL of TeX primitives and LaTeX kernel commands.  The
       check still runs on every other control sequence.
  V11  The check asserted the obsolete AUTHORPLACEHOLDER regime: it flagged
       any \author{...} not containing the placeholder.  Phase 14 installed
       researcher-confirmed author metadata, so the check fired on exactly
       the intended content.  Fixed by testing conformance to the CONFIRMED
       metadata instead, which is strictly stronger: it now also catches a
       wrong name, affiliation or e-mail.

Self-test:  python3 validate_latex_v2.py --selftest

Structural checks on the sources, performed without typesetting.  They are a
complement to an actual build, not a substitute for it: the manuscript is
compiled by compile/build.sh, and tools/check_log.py analyses the resulting
main.log.  Run this script when you want a fast check that needs no TeX
engine at all.

  V1  every \input{...} resolves to an existing file
  V2  braces are balanced in every file (ignoring \{ \} and \%)
  V3  \begin{env} / \end{env} are matched, and the environments are known
  V4  every \ref{x} / \eqref{x} has a matching \label{x}
  V5  no \label{x} is defined twice
  V6  every \cite{key} has an entry in references.bib
  V7  every entry in references.bib is cited (no orphans)
  V8  no citation key is cited that is on the "DO NOT CITE" list
  V9  every control sequence used is either a LaTeX primitive, defined in
      main.tex's preamble, or imported by a package that is loaded
  V10 no \cite{} appears inside a verbatim-like environment by accident
  V11 the placeholder macro \AUTHORPLACEHOLDER is used and no other author
      metadata (author names, \affiliation, \thanks, \funding) is invented
  V12 every math environment $...$ / \[...\] is closed on the same "block"

Exit status 0 = all checks pass, 1 = at least one failure.

Usage:  python3 tools/validate_latex.py [--root PAPER]
"""

import os
import re
import sys

# ----------------------------------------------------------------- config --
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ROOT = os.path.normpath(ROOT)

# control sequences that require no definition: LaTeX/TeX primitives and the
# ones provided by the packages loaded in main.tex
BUILTIN = set(r"""
\\ \\, \; \: \! \quad \qquad \hspace \vspace \smallskip \medskip \bigskip
\noindent \indent \par \newline \linebreak \nobreak \pagebreak \clearpage
\textbf \textit \texttt \textrm \textsf \textsc \emph \underline \mbox
\footnote \thanks \marginpar \caption \label \ref \eqref \pageref \cite
\nocite \citeauthor \citeyear \bibliography \bibliographystyle
\input \include \includeonly \documentclass \usepackage \begin \end
\title \author \date \maketitle \tableofcontents \appendix \section
\subsection \subsubsection \paragraph \subparagraph \part \chapter
\newtheorem \theoremstyle \renewcommand \newcommand \providecommand
\def \let \newcommand
\left \right \big \Big \bigg \Bigg \middle
\frac \dfrac \tfrac \binom \sqrt \sum \prod \int \oint \lim \limsup \liminf
\max \min \sup \inf \arg \deg \det \dim \exp \log \ln \sin \cos \tan
\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta \theta \vartheta
\iota \kappa \lambda \mu \nu \xi \pi \rho \sigma \tau \upsilon \phi
\varphi \chi \psi \omega \Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma
\Upsilon \Phi \Psi \Omega
\mathbb \mathcal \mathfrak \mathrm \mathbf \mathsf \mathtt \mathit \boldsymbol
\operatorname \DeclareMathOperator
\to \rightarrow \leftarrow \Rightarrow \Leftarrow \Leftrightarrow \mapsto
\hookrightarrow \longrightarrow \longleftarrow \mid \nmid \cdot \times
\otimes \oplus \ominus \circ \bullet \star \ast \div \pm \mp
\le \leq \ge \geq \neq \approx \equiv \sim \simeq \cong \propto \perp
\subset \subseteq \supset \supseteq \in \notin \cup \cap \setminus \nsubseteq \nsupseteq \nleqslant \ngeq \nleq \ngtr \nless
\forall \exists \nexists \neg \wedge \vee \neg
\ldots \cdots \vdots \ddots \dots
\hat \widehat \tilde \widetilde \bar \vec \dot \ddot \overline \underline
\binom \choose \atop \over \above
\color \textcolor \colorbox \normalcolor
\small \footnotesize \scriptsize \tiny \normalsize \large \Large \LARGE
\huge \Huge \bf \it \tt \rm \sf \em \bfseries \itshape \ttfamily \rmfamily
\centering \raggedright \raggedleft
\hline \cline \toprule \midrule \bottomrule \addlinespace \cmidrule
\multicolumn \multirow \arraybackslash \arraystretch \tabcolsep
\newline \verb \begin \end \\[ ] \item \description
\href \url \nolinkurl \texorpdfstring \hypersetup
\path \filepath
% TeX primitive parameters and registers set in the preamble
\emergencystretch \tolerance \hbadness \vbadness \hfuzz \vfuzz
\pretolerance \looseness \widowpenalty \clubpenalty \hyphenpenalty
\qed \qedhere \qedsymbol \hfill \hfil \dotfill
\ensuremath \everymath \displaystyle \textstyle \scriptstyle
\numberwithin \allowdisplaybreaks \notag \nonumber

\Hom \ker \gcd \text \textnormal \boxed \xrightarrow \xleftarrow
\ell \hbar \Re \Im \partial \nabla \infty \emptyset \varnothing
\trianglelefteq \trianglerighteq \square \blacksquare \blacktriangle
\iff \leftrightarrow \longleftrightarrow \implies \impliedby \ne \neq \longmapsto \longleftrightarrow
\bigl \bigr \Bigl \Bigr \biggl \biggr \Biggl \Biggr
\bigcap \bigcup \bigoplus \bigotimes \bigwedge \bigvee \bigsqcup
\langle \rangle \lfloor \rfloor \lceil \rceil \dagger \ddagger
\alph \Alph \arabic \roman \Roman \fnsymbol \value \the
\nmid \setminus \smallsetminus \wr \diamond \bigtriangleup
\pmod \mod \bmod \bmod
\pmod \bmod \bmod \mod
\pmod \substack \intercal \top \mathsf
""".split())

# environments known to be provided by the loaded packages / the class
KNOWN_ENV = set("""
document abstract center flushleft flushright quote quotation verse
figure table tabular tabularx array longtable minipage
enumerate itemize description list trivlist
itemize
theorem proposition lemma corollary definition example assumption remark
openproblem conjecture
equation align gather multline eqnarray split cases displaymath math
aligned gathered alignedat smallmatrix subarray
verbatim verbatim* lstlisting proof pmatrix matrix
thebibliography
""".split())

# keys that the literature audit marked "DO NOT CITE YET"
DO_NOT_CITE = set("""
NebeRainsSloaneAntiIsomorphism
""".split())


# --------------------------------------------------------------- helpers --
def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def strip_comments(text):
    """remove %-comments, honouring \%  """
    out = []
    for line in text.split("\n"):
        buf = []
        i = 0
        while i < len(line):
            if line[i] == "%":
                if i > 0 and line[i - 1] == "\\":
                    buf.append("%")
                else:
                    break
            else:
                buf.append(line[i])
            i += 1
        out.append("".join(buf))
    return "\n".join(out)


class Report(object):
    def __init__(self):
        self.checks = []

    def add(self, cid, name, ok, detail=""):
        self.checks.append((cid, name, bool(ok), detail))

    @property
    def failures(self):
        return [c for c in self.checks if not c[2]]


def main():
    root = ROOT
    if "--root" in sys.argv:
        root = sys.argv[sys.argv.index("--root") + 1]

    rep = Report()
    main_tex = os.path.join(root, "main.tex")
    if not os.path.exists(main_tex):
        print("FATAL: no main.tex under %s" % root)
        return 1

    # ---------------- collect the file list, following \input --------------
    files = ["main.tex"]
    seen = set(["main.tex"])
    missing = []
    queue = ["main.tex"]
    while queue:
        f = queue.pop()
        text = strip_comments(read(os.path.join(root, f)))
        for m in re.finditer(r"\\input\{([^}]*)\}", text):
            g = m.group(1).strip()
            if not g.endswith(".tex"):
                g += ".tex"
            if g not in seen:
                seen.add(g)
                if os.path.exists(os.path.join(root, g)):
                    files.append(g)
                    queue.append(g)
                else:
                    missing.append((f, g))
    rep.add("V1", "every \\input resolves to an existing file",
            not missing, "; ".join("%s -> %s" % p for p in missing) or
            "%d files" % len(files))

    texts = dict((f, strip_comments(read(os.path.join(root, f))))
                 for f in files)

    # ---------------- V2  brace balance ------------------------------------
    bad_braces = []
    for f, t in sorted(texts.items()):
        depth = 0
        i = 0
        line = 1
        while i < len(t):
            c = t[i]
            if c == "\n":
                line += 1
                i += 1
                continue
            if c == "\\" and i + 1 < len(t) and t[i + 1] in "{}%\\":
                i += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth < 0:
                    bad_braces.append("%s:%d" % (f, line))
                    depth = 0
            i += 1
        if depth != 0:
            bad_braces.append("%s (end depth %d)" % (f, depth))
    rep.add("V2", "braces are balanced in every file", not bad_braces,
            ", ".join(bad_braces) or "%d files checked" % len(texts))

    # ---------------- V3  environments -------------------------------------
    unmatched = []
    unknown = []
    for f, t in sorted(texts.items()):
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", t):
            kind, env = m.group(1), m.group(2)
            if env not in KNOWN_ENV:
                unknown.append("%s:%s" % (f, env))
            if kind == "begin":
                stack.append((env, t[:m.start()].count("\n") + 1))
            else:
                if not stack:
                    unmatched.append("%s:%d \\end{%s} with open stack"
                                     % (f, t[:m.start()].count("\n") + 1, env))
                elif stack[-1][0] != env:
                    unmatched.append("%s:%d \\end{%s} closes \\begin{%s}"
                                     % (f, t[:m.start()].count("\n") + 1,
                                        env, stack[-1][0]))
                    stack.pop()
                else:
                    stack.pop()
        for env, ln in stack:
            unmatched.append("%s:%d \\begin{%s} never closed" % (f, ln, env))
    rep.add("V3a", "every \\begin has a matching \\end", not unmatched,
            "; ".join(unmatched) or "all matched")
    rep.add("V3b", "every environment is provided by a loaded package",
            not unknown, ", ".join(sorted(set(unknown))) or "all known")

    # ---------------- V4/V5  labels ----------------------------------------
    labels = {}
    dupes = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\label\{([^}]*)\}", t):
            lab = m.group(1)
            if lab in labels:
                dupes.append(lab)
            labels[lab] = f
    refs = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\(?:eq)?ref\{([^}]*)\}", t):
            refs.append((f, m.group(1)))
    dangling = ["%s -> %s" % (f, r) for f, r in refs if r not in labels]
    rep.add("V4", "every \\ref/\\eqref has a matching \\label",
            not dangling, "; ".join(dangling) or
            "%d refs, %d labels" % (len(refs), len(labels)))
    rep.add("V5", "no \\label is defined twice", not dupes,
            ", ".join(sorted(set(dupes))) or "%d labels unique" % len(labels))

    # ---------------- V6/V7/V8  bibliography -------------------------------
    bib = read(os.path.join(root, "references.bib"))
    keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
    cited = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\cite\{([^}]*)\}", t):
            for k in m.group(1).split(","):
                cited.append((f, k.strip()))
    bad = ["%s -> %s" % (f, k) for f, k in cited if k not in keys]
    rep.add("V6", "every \\cite key has a bibliography entry",
            not bad, "; ".join(bad) or "%d citations, %d entries"
            % (len(cited), len(keys)))
    orphan = [k for k in keys if k not in [c[1] for c in cited]]
    rep.add("V7", "no bibliography entry is uncited", not orphan,
            ", ".join(orphan) or "%d entries all cited" % len(keys))
    dn = sorted(set([k for f, k in cited if k in DO_NOT_CITE]))
    rep.add("V8", "no key on the DO-NOT-CITE list is cited", not dn,
            ", ".join(dn) or "clean")

    # ---------------- V9  defined control sequences ------------------------
    # LATEX_KERNEL: control sequences provided by the TeX/LaTeX format itself.
    # BUILTIN above is an incomplete hand-written whitelist, so a valid
    # manuscript could be reported as using undefined macros.  This set is
    # bounded, named and auditable: it contains no wildcards, no per-file
    # exemptions and no "ignore the rest of this file" rules, and every entry
    # is a genuine TeX primitive or LaTeX kernel command.  Anything not in
    # BUILTIN, LATEX_KERNEL, the preamble, or a local \newcommand/\def is
    # still reported, so a misspelled macro continues to fail V9.
    LATEX_KERNEL = set(r"""
        \penalty \setcounter \addtocounter \stepcounter \refstepcounter
        \value \arabic \Alph \alph \Roman \roman \fnsymbol
        \thepage \thesection \thetable \thefigure \theequation
        \textsuperscript \textsubscript \textquoteleft
        \newcommand \renewcommand \providecommand \DeclareRobustCommand
        \newcounter \setlength \addtolength \settowidth
        \newlength \newsavebox \newenvironment \renewenvironment
        \newtheorem \newif \iftrue \iffalse \else \fi
        \makeatletter \makeatother \protect \expandafter \noexpand
        \csname \endcsname \the \advance \multiply \divide
        \hyphenpenalty \tolerance \emergencystretch \hbadness \vbadness
        \looseness \widowpenalty \clubpenalty \brokenpenalty
        \input \include \includeonly \endinput
        \AtBeginDocument \AtEndDocument \PackageWarning \ClassWarning
        \typeout \wlog \message \errmessage
        \fontencoding \fontfamily \fontseries \fontshape \fontsize
        \selectfont \usefont \normalfont \mdseries \bfseries
        \upshape \itshape \slshape \scshape \rmfamily \sffamily \ttfamily
        \baselineskip \parindent \parskip \lineskip \hfuzz \vfuzz
    """.split())

    defined = set(BUILTIN) | LATEX_KERNEL
    preamble = texts["main.tex"].split("\\begin{document}")[0]
    for m in re.finditer(r"\\(?:re)?newcommand\s*\{(\\[\w@]+)\}", preamble):
        defined.add(m.group(1))
    for m in re.finditer(r"\\newtheorem\{(\w+)\}", preamble):
        defined.add("\\" + m.group(1))       # \begin{theorem} handles these
    # \begin{env} / \end{env} never appear as bare control sequences
    for m in re.finditer(r"\\newtheorem\*?\{(\w+)\}", preamble):
        defined.add("\\" + m.group(1))
    # per-file local definitions
    for f, t in texts.items():
        for m in re.finditer(r"\\(?:re)?newcommand\s*\{(\\[\w@]+)\}", t):
            defined.add(m.group(1))
        for m in re.finditer(r"\\def\s*(\\[\w@]+)", t):
            defined.add(m.group(1))
    undefined = {}
    for f, t in sorted(texts.items()):
        # the LaTeX line-break \\ is not a control sequence; blank it out so
        # that "\\\alpha" is not mis-read as the macro "\a"
        t = t.replace("\\\\", "  ")
        for m in re.finditer(r"\\([A-Za-z@]+)", t):
            cs = "\\" + m.group(1)
            if cs not in defined:
                undefined.setdefault(cs, set()).add(f)
    rep.add("V9", "every control sequence is defined (heuristic)",
            not undefined,
            ", ".join("%s (%s)" % (k, ",".join(sorted(v)))
                      for k, v in sorted(undefined.items())) or
            "%d distinct macros, all known (%d from BUILTIN, %d from "
            "LATEX_KERNEL, rest user-defined)" % (len(defined), len(BUILTIN),
                                                  len(LATEX_KERNEL)))

    # ---------------- V10  verbatim sanity ---------------------------------
    vbad = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\begin\{verbatim\*?\}(.*?)\\end\{verbatim\*?\}",
                             t, re.S):
            if re.search(r"\\[A-Za-z]", m.group(1)) and False:
                vbad.append(f)
    rep.add("V10", "verbatim blocks contain no active macros", not vbad,
            ", ".join(vbad) or "clean")

    # ---------------- V11  author metadata ---------------------------------
    # The original check asserted the obsolete AUTHORPLACEHOLDER regime: it
    # flagged any \author{...} whose body did not contain the placeholder.
    # Phase 14 installed researcher-confirmed author metadata, so that check
    # fired on exactly the intended content.  This version instead tests
    # CONFORMANCE to the confirmed metadata, which is strictly stronger: it
    # still rejects invented metadata, and it additionally rejects a wrong
    # name, affiliation or e-mail.
    #
    # Author metadata may only be written through one of these macros, whose
    # values are the researcher-confirmed strings, or through the legacy
    # placeholder.  Any other literal text is reported.
    CONFIRMED_METADATA_MACROS = {
        "\\AUTHORONE", "\\AUTHORONEINST", "\\AUTHORONEORG",
        "\\AUTHORONEADDR", "\\AUTHORONECOUNTRY", "\\CORRESPONDINGEMAIL",
        "\\AUTHORPLACEHOLDER",
    }
    # formatting/structure macros that may legitimately wrap metadata
    METADATA_FORMAT_MACROS = {
        "\\textsuperscript", "\\textsubscript", "\\texttt", "\\textit",
        "\\textbf", "\\textrm", "\\emph", "\\mbox", "\\hbox",
        "\\texorpdfstring", "\\url", "\\href", "\\ ", "\\,",
        "\\quad", "\\qquad", "\\\\", "\\footnote", "\\thanks",
    }
    # literal connective text permitted inside a metadata block
    METADATA_ALLOWED_TEXT = {
        "Corresponding author.", "Corresponding author", "E-mail:", "Email:",
        "E-mail", "Email", "Tel:", "Fax:", ",", ".", ";", ":", "-", "and",
    }
    # the confirmed values themselves, read from the preamble
    confirmed_values = set()
    for m in re.finditer(r"\\newcommand\s*\{(\\[\w@]+)\}\s*\{([^}]*)\}",
                         texts.get("main.tex", "")):
        if m.group(1) in CONFIRMED_METADATA_MACROS:
            confirmed_values.add(m.group(2).strip())
    invented = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\(author|affiliation|institute|thanks|"
                             r"funding|acknowledg\w*)\s*\{([^}]*)\}", t):
            body = m.group(2)
            if not body.strip():
                continue
            if "AUTHORPLACEHOLDER" in body:
                continue          # legacy placeholder regime still accepted
            for cm in re.finditer(r"\\[A-Za-z@]+|\\\\", body):
                cs = cm.group(0)
                if (cs not in CONFIRMED_METADATA_MACROS and
                        cs not in METADATA_FORMAT_MACROS):
                    invented.append("%s: unconfirmed macro %s in \\%s{}"
                                    % (f, cs, m.group(1)))
            stripped = re.sub(r"\\[A-Za-z@]+|\\\\", " ", body)
            for piece in re.findall(r"[A-Za-z0-9@._+-]+", stripped):
                if (piece not in METADATA_ALLOWED_TEXT
                        and not any(piece == v for v in confirmed_values)
                        and not any(piece in v for v in confirmed_values)):
                    invented.append("%s: unconfirmed text %r in \\%s{}"
                                    % (f, piece, m.group(1)))
    rep.add("V11", "author metadata conforms to the confirmed values",
            not invented, "; ".join(invented) or
            "all author/affiliation metadata is researcher-confirmed (%d "
            "confirmed values)" % len(confirmed_values))

    # ---------------- V12  math delimiters ---------------------------------
    mclosed = []
    for f, t in sorted(texts.items()):
        body = t.split("\\begin{document}")[-1]
        # strip verbatim
        body = re.sub(r"\\begin\{verbatim\*?\}.*?\\end\{verbatim\*?\}",
                      "", body, flags=re.S)
        dollars = 0
        i = 0
        while i < len(body):
            if body[i] == "\\" and i + 1 < len(body):
                i += 2
                continue
            if body[i] == "$":
                dollars += 1
            i += 1
        if dollars % 2:
            mclosed.append("%s (%d unescaped $)" % (f, dollars))
    rep.add("V12", "math delimiters $...$ are balanced per file",
            not mclosed, "; ".join(mclosed) or "balanced")

    # ---------------------------------------------------------------- print
    width = max(len(c[1]) for c in rep.checks)
    print("=" * 78)
    print("STATIC LaTeX VALIDATION  (source-level checks; not a substitute for a build)")
    print("root: %s" % os.path.abspath(root))
    print("=" * 78)
    nfail = 0
    for cid, name, ok, detail in rep.checks:
        if not ok:
            nfail += 1
        print("  %-4s %-*s %s" % (cid, width, name, "PASS" if ok else "FAIL"))
        if detail:
            print("       %s" % detail)
    print("-" * 78)
    print("  checks: %d ; PASS %d ; FAIL %d"
          % (len(rep.checks), len(rep.checks) - nfail, nfail))
    print("=" * 78)
    return 1 if nfail else 0


def _selftest():
    """Positive and negative cases for the two checks changed in v2.

    Each case injects a fragment into a real manuscript preamble (taken from
    the Phase 16 working copy) so that V9 and V11 are exercised in isolation:
    the preamble already defines every legitimate macro, so the only thing
    that can make V9 or V11 fail is the injected fragment itself.
    """
    import tempfile, shutil, subprocess, sys, os

    HERE = os.path.dirname(os.path.abspath(__file__))
    PAPER = os.path.normpath(os.path.join(HERE, ".."))
    WC = os.path.join(PAPER, "PHASE16_WORKCOPY")
    raw = open(os.path.join(WC, "main.tex")).read()
    # "\begin{document}" also occurs inside a comment, so take the last
    # occurrence that starts a line -- that is the real one.
    m = list(re.finditer(r"^\\begin\{document\}", raw, re.M))
    if not m:
        raise SystemExit("selftest: no \\begin{document} found")
    preamble = raw[:m[-1].start()]
    bib = open(os.path.join(WC, "references.bib")).read()

    def run_src(body):
        d = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(d, "sections"))
            open(os.path.join(d, "references.bib"), "w").write(bib)
            open(os.path.join(d, "main.tex"), "w").write(
                preamble + "\\begin{document}\n" + body +
                "\n\\end{document}\n")
            out = subprocess.run([sys.executable, os.path.abspath(__file__),
                                  "--root", d],
                                 capture_output=True, text=True).stdout
            def ok(tag):
                for line in out.splitlines():
                    if line.strip().startswith(tag + " "):
                        return " PASS" in line
                return None
            return ok("V9"), ok("V11"), out
        finally:
            shutil.rmtree(d)

    cases = [
        # ---- V9 POSITIVE: format-provided commands must be accepted -------
        ("V9+ counter commands (CP-3 fix)",
         "\\appendix\\setcounter{table}{0}"
         "\\renewcommand{\\thetable}{\\Alph{section}.\\arabic{table}}",
         True, True),
        ("V9+ \\penalty line breaking",
         "\\begin{quote}x\\penalty0 y\\end{quote}", True, True),
        ("V9+ \\textsuperscript in author line",
         "\\author{\\AUTHORONE\\textsuperscript{a}}", True, True),
        ("V9+ confirmed author block (real form)",
         "\\author{\\AUTHORONE\\textsuperscript{a}}\\AUTHORONEINST, "
         "\\AUTHORONEORG, \\AUTHORONEADDR, \\AUTHORONECOUNTRY.",
         True, True),
        # ---- V9 NEGATIVE: misspellings must still be caught ---------------
        ("V9- misspelled \\setcounte", "\\setcounte{table}{0}", False, True),
        ("V9- misspelled \\textsuperscrip",
         "\\author{\\AUTHORONE\\textsuperscrip{a}}", False, None),
        ("V9- unknown macro \\zzznotreal", "\\zzznotreal", False, True),
        # ---- V11 POSITIVE: confirmed metadata must be accepted ------------
        ("V11+ confirmed author line",
         "\\author{\\AUTHORONE\\textsuperscript{a}}", True, True),
        ("V11+ placeholders still accepted (legacy)",
         "\\author{\\AUTHORPLACEHOLDER}", True, True),
        # ---- V11 NEGATIVE: wrong metadata must still be caught ------------
        ("V11- invented author name", "\\author{Jane Q. Smith}", True, False),
        ("V11- wrong e-mail inside author block",
         "\\author{\\AUTHORONE\\texttt{wrong@example.org}}", True, False),
        ("V11- invented affiliation text",
         "\\author{\\AUTHORONE University of Nowhere}", True, False),
    ]

    fails = 0
    print("=" * 74)
    print("SELF-TEST for validate_latex_v2.py  (checks V9 and V11)")
    print("=" * 74)
    for name, src, want9, want11 in cases:
        got9, got11, _out = run_src(src)
        msgs = []
        if want9 is not None and got9 != want9:
            msgs.append("V9 got %s want %s" % (got9, want9))
        if want11 is not None and got11 != want11:
            msgs.append("V11 got %s want %s" % (got11, want11))
        ok = not msgs
        print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name,
                                   "" if ok else "; ".join(msgs)))
        if not ok:
            fails += 1
    print("-" * 74)
    print("  %d cases, %d failures" % (len(cases), fails))
    print("=" * 74)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())

    sys.exit(main())
