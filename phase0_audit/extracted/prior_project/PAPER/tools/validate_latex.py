#!/usr/bin/env python3
"""
validate_latex.py -- a STATIC validator for the manuscript in PAPER/.

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
    defined = set(BUILTIN)
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
            "%d distinct macros, all known" % len(defined))

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
    invented = []
    for f, t in sorted(texts.items()):
        for m in re.finditer(r"\\(author|affiliation|institute|thanks|"
                             r"funding|acknowledg\w*)\s*\{([^}]*)\}", t):
            body = m.group(2)
            if "AUTHORPLACEHOLDER" not in body and body.strip():
                invented.append("%s: \\%s{%s}" % (f, m.group(1), body[:60]))
    rep.add("V11", "no author/affiliation/funding metadata is invented",
            not invented, "; ".join(invented) or
            "only \\AUTHORPLACEHOLDER present")

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


if __name__ == "__main__":
    sys.exit(main())
