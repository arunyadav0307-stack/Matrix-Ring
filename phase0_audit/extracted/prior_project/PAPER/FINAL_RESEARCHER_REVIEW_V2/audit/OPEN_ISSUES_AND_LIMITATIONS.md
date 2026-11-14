# Phase 8 / Task J — Open issues and limitations

Companion to `MANUSCRIPT_SELF_AUDIT.md`. This file collects, in one place,
every limitation of the manuscript and every question left open, so that
neither a reader nor the author mistakes a scoped statement for a general one.

---

## 1. Limitations of the comparison (external)

| limitation | consequence |
|---|---|
| codetables.de has **no** entanglement-assisted table (`QECC-EA.php` → HTTP 404) | **no EA code in this paper is benchmarked**, including the best ($d=10$) |
| codetables.de does not offer $q=8$ | the 14 certified codes over $\mathbb F_8$ are unbenchmarked |
| the site prints the **prime** $p$ in its labels ($[[N,K]]_2$ for $q=4$, $[[N,K]]_3$ for $q=9$) | an earlier phase concluded, wrongly, that $q=9$ was not covered; corrected here as **E-8.1** |
| the retrieved page reports “Last change: 10.06.2024” | the $q=9$ bounds are dated 2026-11-04 and are external data, not an output of this computation |

**Net effect.** Of the 28 certified codes, 7 stabilizer codes over
$\mathbb F_4$ and 3 over $\mathbb F_9$ can be compared; 18 cannot. The
comparison is therefore a *sample* comparison and is presented as such.

---

## 2. Limitations of the computation (internal)

1. **15 of 42 families are unreachable.** Blocked by component BFS size
   ($|S^2|>4\cdot10^6$). Listed with method `component BFS too large` in
   `supplementary/parameter_tables/family_census.csv`.
2. **4 further families are counted but not enumerated** (more than 40 000
   submodules of $\Bq^2$): $(9,1,5)$, $(9,1,6)$, $(9,2,4)$, $(9,3,2)$. Codes
   from three of these are sampled (2 000 each, fixed seed).
3. **The Pareto frontier is a frontier of the scan**, not of the framework.
   88 of 368 distinct tuples are non-dominated *among the scanned families*.
4. **M3 is a lower bound for most codes.** The ambient quantum search reaches
   only weight 2 or 3 for 22 of the 28 certified codes; the exact distances
   come from M1 (complete enumeration) and M2 (support search).
5. **Distances of $5$ are lower bounds in two rows** of the Pareto table
   ($[[24,6,5;2]]_9$, $[[24,10,4;2]]_9$); they are marked $\ge$ wherever they
   appear.

---

## 3. Open mathematical problems

1. **(O-3.1b) Can a *principal* cyclic code have a non-principal Galois hull?**
   Every witness currently known (four at $(4,2,2)$, two at $(9,2,3)$, two at
   $(4,2,4)$) is a code that is itself non-principal —
   $\mu_{\Bq}(W)=3$. For the $(4,2,2)$ and $(9,2,3)$ witnesses one even has
   $\mathrm{Hull}_s(W)=W$, so the hull is non-principal *because* the code is.
   The sharper question is open and is **not** claimed either way.
2. **Hull dimension distribution in the wild families.** The cyclic-code
   enumeration has resisted complete treatment for 15 families; the dimension
   distribution of $\mathrm{Hull}_s(C)$ there is unknown.
3. **Weight enumerator of the quotient code.** Theorem 8.1 identifies the
   quantum distance with the minimum weight of
   $D^{\perp_E}/\mathrm{Hull}_E(D)$. No closed or recursive description of the
   weight distribution of that quotient in terms of the CRT data of $C$ is
   known.
4. **Two conjectures** (end of §5.5), stated and used nowhere:
   $\mathrm{Hull}_s(C)\subseteq\sigma_{2s}(C)$, and
   $\dim\mathrm{Hull}_s(C)=\dim\mathrm{Hull}_s(C^{\perp_s})$. Both hold in
   every instance computed.
5. **Exact domain of the characteristic-two obstruction.**
   Theorem 6.6 proves that no congruence $T^{\mathsf T}H_tT=I_t$ exists for
   $p=2$ and $t$ even. Congruences are *constructed* for $t=1,3,5$ at $q=4,8$
   and at $(q,t)=(9,2)$, but it is not proved that a congruence exists for
   every odd $t$ in characteristic two.
6. **Extending the comparison to $q=8$ and to entanglement-assisted codes** —
   blocked by the absence of tables, not by the mathematics.

---

## 4. Scope decisions recorded here so they are not re-litigated

* **Enumerator theory is supporting material.** The manuscript is *not* a
  paper about enumerators or about counts of codes. The hull and code
  enumerators of Phase 3B are not presented as principal results and appear
  only where they support a construction.
* **Right-module convention is forced**, not chosen: Lemma 3.4 (failure
  lemma) shows the left convention gives the wrong size formula.
* **All dimensions are over $\mathbb F_q$.** The only $\mathbb F_p$-statement
  in the paper is the commutation test (Theorem 7.3), and it is flagged as
  such.
* **Three distinct duals** appear and are never identified:
  $C^{\perp_s}$ (the $\theta_s$-pairing on $R^n$),
  $D^{\perp^{\widehat{}}_s}$ (the transported Hankel form on
  $\mathbb F_q^{4tn}$) and $D^{\perp_E}$ (Euclidean, used by routes R2/R3).
* **The paper is not declared submission-ready.** It *has* now been typeset
  (issue M-1 of the self-audit is resolved and `main.pdf` is shipped), but the
  rendering used a recovered 2010-vintage pdfTeX engine with a Python
  stand-in for the missing `bibtex` binary, and has not been reproduced on a
  current TeX Live. That one recompilation is the outstanding item; see
  `compile/README.md`.
* **No journal is named.** Suitability for any venue, Q1 or otherwise, has not
  been assessed; doing so would require a documented comparison of scope,
  standards and novelty that was not carried out in Phase 8.


---

## 5. Phase 15 addendum — retained limitation and corrected claims

**Append-only.** Three accuracy defects were corrected in Phase 15
(CP-1, CP-2, CP-3); they are recorded in
`PHASE15_FINAL_CORRECTIONS_REPORT.md` and in the Phase 15 addendum to
`MANUSCRIPT_SELF_AUDIT.md`. The one item below is **retained, not fixed**.

5.1 **DOIs are not rendered in the PDF (retained).** Nine of the thirteen
bibliography entries carry a `doi=` field in `references.bib`, but the
bibliography style `plain.bst` has no `doi` field, so the compiled PDF shows
no DOI for any reference. This is a formatting limitation of the style, not a
data defect. It is **deliberately retained** because the FFA guide for authors
states that reference formatting is applied by the publisher at proof stage;
changing `\bibliographystyle` or hand-inserting DOI text into the `.bbl` or
the source would be discarded at proof and could introduce inconsistency
between the submitted and published reference lists. **Action required only if
the author wants DOIs visible before proof stage**, in which case a style that
supports `doi` (e.g. `plainurl`, `elsarticle-num`) should be adopted as a
deliberate, separate change.

5.2 **Method counts, restated precisely (superseding looser earlier wording).**
Per code: exactly **two** independent methods are run — one exact method
(M1 complete enumeration where it completes, otherwise M2 support search,
which is run precisely when M1 cannot finish) plus the ambient quantum search
M3, which for 17 of the 28 codes yields a proved **lower bound** rather than
an exact distance. **No code is certified by all three methods**, and no code
should be described that way. Per-code applicability is tabulated in
`corrected_appendix/CP1_method_applicability_table.csv`.
