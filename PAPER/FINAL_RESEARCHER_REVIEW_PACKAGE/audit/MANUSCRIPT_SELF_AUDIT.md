# Phase 8 / Task J — Manuscript self-audit

Manuscript: **Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings**
Source: `PAPER/main.tex` + `PAPER/sections/*.tex` + `PAPER/references.bib`
Date of this audit: 2026-11-09.  **Revised 2026-11-09 after Phase 8A**
(the manuscript has since been compiled; §3 M-1 is therefore rewritten and
§3.1 records what the compilation itself turned up).

This file is the honest self-review demanded by Task J. It lists what was
checked, what the checks returned, and every issue found, classified
**BLOCKING / MAJOR / MINOR / RESOLVED**. It is written to be read by someone
who wants to find the weak points, not by someone who wants to be reassured.

---

## 1. What was checked, and how

| # | check | method | result |
|---|---|---|---|
| 1 | every `\input` resolves | `tools/validate_latex.py` V1 | PASS — 13 files |
| 2 | braces balanced | V2 | PASS |
| 3 | environments matched and known | V3a, V3b | PASS |
| 4 | every `\ref`/`\eqref` has a `\label` | V4 | PASS — 246 refs, 107 labels |
| 5 | no duplicate `\label` | V5 | PASS |
| 6 | every `\cite` key has a bib entry | V6 | PASS — 32 citations, 13 keys |
| 7 | no uncited bib entry | V7 | PASS — 13/13 cited |
| 8 | no DO-NOT-CITE key cited | V8 | PASS |
| 9 | every macro defined | V9 (heuristic) | PASS |
| 10 | no invented author metadata | V11 | PASS — only `\AUTHORPLACEHOLDER` |
| 11 | math delimiters balanced | V12 | PASS |
| 12 | every claim resolves to a source | `CLAIM_TRACEABILITY_MATRIX.md` | 10/10 checks performed |
| 13 | no theorem promoted from computational to proved | manual, register | no promotion found |
| 14 | every number traceable to a log line | `supplementary/parameter_tables/*.csv` carry `log_line` | PASS |
| 15 | generator matrices are the certified codes, not re-selections | `extract_certified_generators.py` re-ran Parts 2/3/6 and reproduced all 28 rows | PASS |
| 16 | the manuscript renders without error | `compile/build.sh` + `tools/check_log.py` | PASS — 39 pp., 0 errors, 0 undefined refs/citations, 0 overfull boxes |
| 17 | the numbers in the worked examples are not transcription errors | `tools/verify_examples.py` | PASS — 56 checks, 0 mismatches |

**Compilation status: COMPILED.** `main.pdf`, 39 pages, was produced in this
environment by a recovered pdfTeX engine; see §3 M-1 and `compile/README.md`.
`tools/check_log.py` reports 0 errors, 0 missing characters, 0 undefined
references, 0 undefined citations, 0 overfull boxes and **0 package or
LaTeX warnings** (14 hyperref `Token not allowed in a PDF string` warnings,
from mathematics in five subsection titles, and 3 `'h' float specifier
changed'` warnings, were removed by `\texorpdfstring` and by `[h]` → `[ht]`). The static validator is
still run and still reports 13 PASS / 0 FAIL.

Word count of prose at the time of the Phase 8A revision: **12 447**
(`tools/manuscript_stats.py`), 3 006 lines of `.tex` over 13 files.

---

## 2. Structure and content, against the Phase-8 brief

| brief item | where | verdict |
|---|---|---|
| Task A — contribution map | `CONTRIBUTION_MAP.md` | done (A1–A5) |
| Task B — claim-to-source matrix | `CLAIM_TRACEABILITY_MATRIX.md` | done, 10 checks + 9 special-attention items |
| Task C — final quantum-code table | `PARAMETER_COMPARISON.md`, §9, Appendix A | done |
| Task D — verified literature/novelty | `LITERATURE_VERIFICATION.md`, `NOVELTY_COMPARISON.md`, §2, §9.3 | done, 13 references |
| Task E — 10-section structure | §1–§10 + 2 appendices | done |
| Task F — main theorems with full proofs | §4–§8 | 21 theorems, 9 propositions, 11 lemmas, 2 corollaries |
| Task G — full worked examples | Examples 1–13 | 13 examples |
| Task H — supplementary package | `PAPER/supplementary/` | done (scripts, logs, generator matrices, CSV tables, procedures, manifest, environment) |
| Task I — LaTeX | `PAPER/main.tex` etc. | done; `main.pdf` produced (39 pp.) |
| Task J — self-review | this file + `OPEN_ISSUES_AND_LIMITATIONS.md` | done |

Word count of prose: **≈ 12 000** (12 147 by `tools/manuscript_stats.py`,
which excludes tables, display math and macros). 2 914 lines of `.tex` over 13
files.

---

## 3. Issues found

### MAJOR

**M-1. — RESOLVED (2026-11-09).** The previous version of this audit recorded
that the manuscript had never been compiled, because no TeX engine was
available. A real engine has since been recovered and **`main.pdf` (39 pages)
now exists**; see `compile/README.md` for the full provenance. In outline: the
npm package `texlive@1.2.0` (texlive.js) ships, inside its `binary.zip`, a
native x86-64 Linux **pdfTeX 1.40.11** binary together with a TeX Live 2015
`texmf` tree and a `latex.fmt` dump; `bibtex` is genuinely absent and is
replaced by `tools/make_bbl.py` (pybtex, `plain` style), which produces the
`.bbl` that LaTeX reads anyway; `booktabs.sty`, `enumitem.sty` and
`xcolor.sty` were absent from that tree and were retrieved from GitHub mirrors
of the CTAN sources.

*What this resolves:* the manuscript renders. There are no package-level
errors, no missing glyphs, no undefined references or citations, and after the
Phase-8A line-breaking pass **no overfull boxes** (27 of them stood before, the
worst 134.9 pt).

*What it does not resolve:* the engine is a **2010-vintage pdfTeX** driven
through a `\pdfoutput=1` prefix rather than a native `pdflatex` format, with
`bibtex` replaced by a Python stand-in; it is **not** a current TeX Live. The
output is a genuine pdfTeX PDF with embedded Type 1 fonts, but the manuscript
must be recompiled on a current distribution
(`pdflatex main && bibtex main && pdflatex main && pdflatex main`) before it is
circulated. That recompile is expected to succeed unchanged and has **not**
been carried out. This is now a *portability* caveat, not a deliverable gap.

**M-2. O-3.1 as originally recorded is ambiguous, and only the weaker reading
is refuted.**
The register (T-168) states O-3.1 as “is $\mu_B(W_{\mathrm{hull}})\le2$
always, i.e. is the hull of a **principal** code always principal even in the
wild regime?”. Every witness currently known — the four at $(4,2,2)$ and the
four at $(9,2,3)$ and $(4,2,4)$ — has $\mu_B(W)=3$ for the *code*, i.e. the
witness codes are themselves non-principal. So:
* (O-3.1a) “every hull of every right ideal is principal” — **refuted**;
* (O-3.1b) “the hull of a principal code is principal” — **open**.

The manuscript now states both readings explicitly
(§5.2), refutes (a), and records (b) as open (Remark 5.6, and open problem
(vi) in §10). Nothing downstream depends on (b).
*Risk if unaddressed:* a reader would have taken the refutation to be stronger
than it is.

**M-3. No entanglement-assisted code in the paper is benchmarked.**
codetables.de has no EAQECC table (the endpoint `QECC-EA.php` returns HTTP
404). The largest distances in this paper are EA ($d=10$), so the strongest
numerical results are precisely the ones with no external comparison. This is a
limitation of the literature, not of the construction, but it means the
comparison in §9 covers only the stabilizer codes, and the EA codes must be
judged against the EA-Singleton defect alone.

**M-4. $q=8$ codes are entirely unbenchmarked.**
codetables.de returns “currently not available for q=8”. Fourteen of the 28
certified codes are over $\mathbb F_8$ and none of them can be compared.

### Phase 8A — issues found by compiling and by re-deriving the numbers

The first rendering made it possible to check things a static validator cannot,
and prompted a line-by-line re-derivation of every number quoted in the worked
examples and in the parameter tables (`tools/verify_examples.py`, 56 checks).
Six defects were found; **all six are fixed in the current sources**, and each
is listed here with its disposition, because repairing them silently would have
been the wrong thing to do.

**M-5. `h_E` was wrong in one row of the headline table — FIXED.**
Table `tab:headline` (§8) gave the row `$[[16,4,3]]_4$ / $(4,1,4)$ / R2-DC`
as `k = 10, h_E = 10`. For a dual-containing code at $N=16$ with $k=10$ one has
$D^{\perp_E}\subseteq D$, hence
$h_E=\dim(D\cap D^{\perp_E})=\dim D^{\perp_E}=N-k=6$; the value $10$ is not
merely wrong, it is impossible, since $h_E\le N-k$ always. Independent
recomputation (`tools/verify_examples.py`, plus a direct exhaustive scan of all
565 codes of the family) returns **21** DC codes with $k=10$, **all** with
$h_E=6$, $K=2k-N=4$, and best exact distance $d=3$. The row now reads $h_E=6$.
Nothing else in the row changed ($K=4$, $d=3$, $c=0$ and defect $8$ were
already right), and no other row of any table is affected: the same script
checks all 18 rows of `tab:headline` and all 28 rows of `tab:cert` against the
route identities ($K=N-2k$ for SO, $K=2k-N$ for DC, $K=N-k-h_E$ and $c=k-h_E$
for R3, $K=N-k$ for R1) and against the CSVs, recomputing the Singleton defect
each time; 46/46 consistent.

**m-7. A measured count in Example 10 was quoted wrongly — FIXED.**
Example `ex:obstruction` (§6) stated that at $(9,2,2)$ "the minimum distance
changed under $\Psi$ for 3 of the 5 codes tested". The Phase-5 log it cites
(`phase5_quantum_log.txt`, check C3) records **7** self-orthogonal codes
transformed, of which **4** change their minimum distance. The example now
says "4 of the 7".

**m-8. Two examples each claimed to be *the* largest-distance code — FIXED.**
Examples `ex:routes` (§7) and `ex:certify` (§8) each ended by saying their
code was "the largest-distance code found anywhere in the search", naming
$[[24,2,10;18]]_9$ and $[[20,2,10;18]]_4$ respectively. Both have $d=10$, and
no code in the search has $d>10$ (checked over `certified_codes.csv` and
`pareto_frontier.csv`), so neither is unique. Both now say that the two codes
are tied at $d=10$ and that nothing found exceeds it.

**m-9. An annihilator was written without its ambient module — FIXED.**
Example `ex:crt` (§3) wrote $\dim_{\F_4}\ann(\mathfrak m)=2$ while the two
parallel examples (`ex:witnessA`, `ex:witnessB`) write $\ann_{\Bq^2}$. The
value $2$ is the annihilator **in $\Bq^2$**; $\ann_{\Bq}(\mathfrak m)$ is
$1$-dimensional in all three rings. The subscript has been added. (The values
themselves were re-derived from scratch and are correct: $\dim\mathfrak m^i$
is $3,1$ at $(4,2,2)$; $5,3,1$ at $(9,2,3)$; $7,5,3,1$ at $(4,2,4)$; and
$\dim\ann_{\Bq^2}(\mathfrak m)=2$ in all three — as is the count $1221$ of
$\Bq$-submodules of $\Bq^2$ at $(4,2,2)$, recomputed by exhaustive BFS, and
the $92$ nonzero codes with $14$ of them $\sigma_2$-stable at $(8,1,2)$.)

**m-10. The entanglement-budget table's caption over-claimed — FIXED.**
Table `tab:budget` (§8) was captioned "minimum entanglement $c$ for each
distance, over the whole search", but Part 4(c) of the Phase-7 log records such
a minimum only for $d=2,\dots,8$. The caption now states the range and points
to `tab:headline` for $d=9$ ($c=16$) and $d=10$ ($c=18$).

**m-11. §9 named only one of the two $d=10$ codes — FIXED.**
§9 said the largest distances of the paper occur "at $N=20$". They occur at
both $N=20$ and $N=24$; the sentence now names both codes.

*Also noted, not a defect:* `\usepackage[T1]{fontenc}` was removed from
`main.tex`. The recovered tree has no EC/T1 font metrics, so `T1` fell back to
`nullfont` and 70 564 glyphs were dropped in the first build. All sources are
pure ASCII, so OT1 renders this manuscript identically, and on a current TeX
Live either setting compiles. Three packages that were loaded but never used
were removed (`mathtools`, `multirow`); `xcolor`, used only by the
`\blanksymbol` helper, was restored once `xcolor.sty` had been obtained. All
of this is recorded in `compile/README.md` and `CHANGELOG.md`.

### Phase 8B — issues found by compiling on a current TeX Live

Recompiling on TeX Live 2024 with genuine BibTeX found five build defects and
one editorial question. **None of the five touches the mathematics**; all are
recorded entry by entry, with the evidence, in
`compile/BUILD_CORRECTIONS.md`. Four of them were *latent* — the 2010 engine
and the pybtex `.bbl` had swallowed them, and in two cases the Phase 8A PDF was
simply wrong on the page.

**C-1. `\AUTHORPLACEHOLDER` used before it was defined — FIXED.**
`main.tex` consumed the macro in `\hypersetup{pdfauthor=…}` at line 39 but
defined it at line 68. Current `hyperref` expands the PDF metadata strings when
`\hypersetup` runs, so this is a hard error; the 2010 `hyperref` deferred the
expansion and never noticed. Order-only fix.

**C-2. `\Hom` was used but never defined — FIXED (and the 8A PDF was wrong).**
Used in §3 and §4; `grep` finds no definition anywhere. The 2010 engine
**silently dropped the operator name**: the shipped Phase 8A PDF contains the
word "Hom" **zero** times, and the two sentences read `ψ_C : C → F_q(S/C^⊥,F_q)`
and `… into F_q(C,R) …`, neither of which parses. No error appeared in the
Phase 8A log. One line added: `\newcommand{\Hom}{\operatorname{Hom}}`, matching
the file's existing convention for `\ann`, `\Tr`, `\Hull` and friends.

**C-3. An unbraced `]]` broke an optional argument — FIXED (and the 8A PDF was
wrong).** `\begin{example}[certifying $[[20,2,10;18]]_4$]` in §8: LaTeX's
optional-argument scanner stops at the first unbraced `]`, so the 8A PDF reads

> Example 8.12 (certifying [[20, 2, 10; 18). ]4]

The argument is now braced. A sweep of every `\begin/\end{…}[…]` and
`\section[…]` in all 13 sources found exactly this one site. The `[[n,k,d;c]]_q`
notation makes this a standing hazard.

**C-4. The TS1 text-companion fonts are missing — FIXED (distribution, not
source).** Since kernel release 2020/02/02, `\textbullet` — hence every
`itemize` bullet — is taken from **TS1**, not from the OMS maths font. The TS1
shapes of Computer Modern are the `cm-super` collection, absent here, so the
run died with `Font tcrm1095 at 600 not found`. cm-super cannot be fetched and
Metafont is unavailable. The substitution is made in the pdfTeX font map
(`compile/map_ts1_lm.py`): TS1 EC fonts are mapped to Latin Modern TS1
outlines, which share Computer Modern's metrics. The map is patched rather than
the format rebuilt, deliberately — rebuilding `pdflatex.fmt` would re-load the
hyphenation patterns and could change the line and page breaking, which is
exactly what this phase exists to confirm has *not* happened. **No manuscript
source was modified.**

**C-5. Empty PDF `/Title`; four `hyperref` PDF-string warnings — FIXED.**
`hyperref` does not read `\title` unless given `pdfusetitle`, so the PDF's
`/Title` was empty. Added `pdfusetitle`, and wrapped the author placeholder in
`\texorpdfstring` so that the PDF string gets plain text (a PDF string cannot
hold `\textbf` or `\,`). The log now contains **zero** occurrences of the word
`Warning`.

**F-1. The bibliography no longer prints DOIs — CLOSED 2026-11-10, decision:
keep `plain`.**
The 8A PDF printed `doi:10.1016/…` for nine references. That was the pybtex
substitute, not `plain.bst`: genuine BibTeX with the `plain` style that
`main.tex` requests prints no DOI, and §5 below already recorded on 2026-11-09
that "the `plain` style prints no DOI". The modern build therefore drops nine
DOIs present in the 8A PDF — the only Phase 8B change that *removes*
information. It was left alone pending a decision, because restoring the DOIs
means departing from the declared bibliography style.

**Decision (author, 2026-11-10): keep `plain`.** No change to `main.tex`, no
change to `references.bib`; **DOI display is deferred to journal-specific
formatting**, the target venue's style governing how and whether DOIs appear.
The `doi` fields remain in `references.bib`, so a journal style that prints
them needs no further editing. Recorded as decision `D-1` in
`compile/BUILD_CORRECTIONS.md`; see also `FINAL_VALIDATION_REPORT.md` §0.7.

*Also noted, not a defect.* The modern PDF's text layer writes `fi` as two
characters where pdfTeX 1.40.11 wrote the single ligature glyph U+FB01; and it
maps the `\varphi` glyph to U+03C6 where 1.40.11 mapped it to U+03D5. Both are
extraction differences only — the `\varphi` glyph sits at identical
coordinates with identical advance width in both PDFs, and its rendered pixels
are byte-identical at 1200 dpi. Neither is visible on the page.

### MINOR

**m-1. The earlier tuple $[[24,4,5;12]]_4$ changed value.**
Phase 6 reported it from a 300-code sample of $(4,2,3)$. Exhaustive
enumeration of that family (35 937 codes) gives best EA distance $6$, attained
by $[[24,4,6;20]]_4$. The old value is dominated (by $[[20,4,6;12]]_4$) and is
not reproduced. Reported in §9.4 as *improved, not refuted* — nothing in the
earlier derivation was wrong, it was incomplete.

**m-2. The Phase-7 log's own comparison table is incomplete.**
Part 8 of `phase7_extended_search_log.txt` asserts that codetables.de covers
only GF(4). That is wrong: the site tabulates $q=4$ **and** $q=9$ (its page
header prints the *prime*, so $q=9$ appears as $[[N,K]]_3$, which is what
misled the earlier reading). The manuscript's §9 comparison includes the
corrected $q=9$ rows. The log is left untouched (append-only discipline); the
correction is recorded here and in `PARAMETER_COMPARISON.md` §4 as **E-8.1**.

**m-3. M3 is a lower bound for most codes.**
The ambient quantum search (method M3) is complete only up to the weight it
reaches; for 22 of the 28 certified codes it reports “$>2$”, i.e. $d\ge3$. The
exact values come from M1/M2. This is stated in Appendix A and in
`CERTIFICATION_PROCEDURE.md`, but a reader skimming Table 4 could misread
“$>2$” as a certified exact distance. The `exact` column is the authoritative
one.

**m-4. Fifteen of the 42 families are unreachable.**
They are blocked by component BFS size. The Pareto frontier of §8.6 is a
statement about the scanned families only, and the manuscript says so.

**m-5. Two conjectures are stated but unused.**
$\Hull_s(C)\subseteq\sigma_{2s}(C)$ and
$\dim\Hull_s(C)=\dim\Hull_s(C^{\perp_s})$ (end of §5.5). Both hold in every
instance computed; neither is proved; neither is used. They are labelled as
conjectures in the text.

**m-6. The witness dimension bookkeeping in the Phase-7 log is ambiguous.**
The log reports “dim W = 5, … dim Hull = 10 (= 5 in $B^2$ coords)” for
$(9,2,3)$, which mixes $\mathbb F_q$-dimensions and $B^2$-ranks in one line.
The manuscript's Examples 7 and 8 quote only the quantities that are
unambiguous ($\mu_B(W)$, $\mu_B(\mathrm{Hull})$, whether $\mathrm{Hull}=W$,
and the resulting quantum parameters) and do not restate the ambiguous
dimension.

### RESOLVED

**R-1. The hull of a cyclic code was stated to be cyclic.**
An early draft of Theorem 5.1(b) asserted “if $C$ is cyclic then
$\Hull_s(C)$ is cyclic”, with a one-line non-proof. That is incompatible with
the refutation of O-3.1(a) and is not what any downstream result needs.
**Fixed:** (b) now asserts $T$-invariance, with a complete proof, and states
explicitly that principality is *not* claimed.

**R-2. The tables in §8 and §9 and Appendix A were reconstructed from memory
in a first draft and did not match the log.**
**Fixed:** every row of Table 1, Table 2, Table 3, Table 4 and Table 5 is now
parsed from `phase7_extended_search_log.txt` by
`tools/build_parameter_tables.py`, and each CSV row carries the log line it
came from. The tables were then rewritten to match the parsed data.

**R-3. The bookkeeping identity $c+K=N-k$ (Phase 6 §12) is wrong.**
Correct identity: $c+K=N-2h_E$. Recorded as erratum **E-7.1** in §8.4, not
silently repaired. No parameter computed earlier is affected, because $K$ and
$c$ were always computed from $k$ and $h_E$ directly.

**R-4. The Phase-5 generator-number disambiguation.**
$\mu_B=4$ refers to the *code*; the hull census range is $\{0,1,2,3\}$. Stated
in Remark 5.7.

**R-5. Re-selection-by-invariants defect.**
An earlier version certified a different code with the same invariants. The
current pipeline carries the image basis from the search stage into the
certification stage, and `extract_certified_generators.py` re-ran Parts 2/3/6
end-to-end and reproduced all 28 rows of the certification table with the
generator matrices attached.

---

## 4. Claims the manuscript deliberately does **not** make

1. No record quantum parameter is claimed. Every stabilizer code is equal to
   or below the best known distance; the manuscript states the gap.
2. Matrix rings, Galois hulls, Gray maps, quasi-cyclic images, stabilizer
   codes and entanglement-assisted codes are each attributed
   (§2, `NOVELTY_COMPARISON.md` §3) and none is claimed as new.
3. Suitability for any particular journal, and in particular for a Q1 venue,
   is **not** asserted. That would require a documented comparison of scope,
   standards and novelty that has not been carried out.
4. The paper is **not** declared submission-ready while M-1 stands: it has not
   been typeset, and a submission decision should not rest on an unrendered
   manuscript.
5. The Pareto frontier is not claimed to be the true frontier of the
   framework, only of the scanned families.
6. The characteristic-two obstruction is not extended beyond $p=2$ with $t$
   even; counter-congruences for $t=1,3,5$ and for $(q,t)=(9,2)$ are recorded
   so that the hypotheses are seen to be exact.

---

## 5. Verdict

The mathematics is, to the best of this audit, correct and self-contained:
every theorem is proved in the text or attributed, every computational claim
is traceable to a log line, and every correction has been recorded rather than
silently applied. The two known open questions introduced by the audit
(O-3.1b and the unbenchmarked EA/$q=8$ codes) are stated in the paper itself.

**The obstacle to calling this submission-ready is no longer that the
manuscript has never been rendered** — M-1 is resolved and `main.pdf` exists.
What remains is that the rendering used a recovered 2010-vintage engine with a
Python stand-in for `bibtex`, and has not been reproduced on a current TeX
Live. That recompilation is the one outstanding item, and it is expected to
succeed unchanged.

Counts for the final report: **0 blocking, 4 major (M-1 resolved; M-2 to M-4
open), 6 minor, 5 resolved, plus 6 further items (M-5, m-7 to m-11) found and
fixed during Phase 8A.**
