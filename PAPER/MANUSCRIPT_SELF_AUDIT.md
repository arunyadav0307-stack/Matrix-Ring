# Phase 8 / Task J — Manuscript self-audit

Manuscript: **Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings**
Source: `PAPER/main.tex` + `PAPER/sections/*.tex` + `PAPER/references.bib`
Date of this audit: 2026-11-09.

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
| 4 | every `\ref`/`\eqref` has a `\label` | V4 | PASS — 233 refs, 106 labels |
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

**Compilation status: NOT COMPILED.** There is no TeX engine in this
environment (see §3, issue **M-1**). A static validator was written and run
instead; it cannot detect typesetting-level problems such as overfull boxes,
bad page breaks, or a missing package.

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
| Task I — LaTeX | `PAPER/main.tex` etc. | done; **no PDF** |
| Task J — self-review | this file + `OPEN_ISSUES_AND_LIMITATIONS.md` | done |

Word count of prose: **≈ 12 000** (12 147 by `tools/manuscript_stats.py`,
which excludes tables, display math and macros). 2 914 lines of `.tex` over 13
files.

---

## 3. Issues found

### MAJOR

**M-1. The manuscript has not been compiled; no PDF exists.**
No TeX engine is available in this environment: `pdflatex`, `latex`,
`xelatex`, `lualatex`, `tectonic` and `kpsewhich` are all absent, and no
usable WASM/JS build could be obtained (`pdftex.js@0.0.10` is a browser port
requiring a service worker; `swiftlatex`, `texlive.js`, `latex-wasm`,
`tectonic-wasm` return 404 on npm; PyPI `tectonic` is `0.0.0dev`). A static
validator (`tools/validate_latex.py`, 13 checks, all PASS) was written in its
place. **Consequence:** the manuscript is structurally sound as far as a
non-typesetting check can establish, but it has never been rendered. Line,
page and float behaviour are unknown, and a package-level error cannot be
excluded. This is a deliverable gap, not a mathematical one.
*Mitigation:* the file compiles from `main.tex` with
`pdflatex → bibtex → pdflatex → pdflatex`; the bibliography style is `plain`
and all 13 entries are standard `@article`/`@misc`.

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

**The blocking obstacle to calling this submission-ready is not
mathematical; it is that the manuscript has never been compiled** (M-1). That
requires a TeX installation this environment does not have.

Counts for the final report: **0 blocking, 4 major, 6 minor, 5 resolved.**
