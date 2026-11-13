# Phase 12 / Task E — Final abstract and manuscript check

**The Phase 11 approved abstract is preserved unchanged.** No stylistic change
was made. Any further change would require a guideline violation or a factual
error; neither was found.

## 1. Abstract word count — reverified

| convention | rule | count | limit | margin |
|---|---|---:|---:|---:|
| C1 | strip `\commands`, drop `{}&$`, expand math tokens | **213** | 250 | 37 |
| C2 | each `$…$` block collapses to one token | **199** | 250 | 51 |
| C3 | C1 plus `_^` and braces split (strictest) | **226** | 250 | **24** |

**Compliant under all three.** The canonical (unrevised) abstract is 246/230/**260**
— it fails C3 by 10 words. The revision is load-bearing.

The abstract body was measured with the keywords block **excluded**, since the
keywords are not part of the abstract text. Measured with them included the
figures are 233/219/245 — still compliant, but the correct figure is the
excluded one.

## 2. Abstract content — every claim re-verified

| claim | support | status |
|---|---|---|
| `R=M_2(A_t)`, `A_t=F_q[u]/⟨u^t⟩` | §3 | VERIFIED |
| codes are right ideals of `R_n=R[X]/⟨X^n−1⟩` | §3, §4 | VERIFIED |
| `θ_s=σ_s∘(·)^T` drives duality | Thm 4.3, 4.6 | VERIFIED |
| duality/hull theory for arbitrary right ideals, no principality hypothesis | §4, §5 | VERIFIED |
| `MU_B=3` hulls exist | Thm (nonprincipal) | VERIFIED |
| `MU_B≥3` forces `t≥2` and `p\|n` | Thm (confinement) | VERIFIED |
| expansion to `F_q^{4tn}`; `σ̂_s`-Hermitian; Hankel Gram `I_{4n}⊗H_t` | Thm (gram) | VERIFIED |
| not Euclidean unless `t=1` | §6 | VERIFIED |
| duality and hulls preserved, non-principal included | §6 | VERIFIED |
| hulls self-orthogonal, no reflexivity hypothesis | Thm (hullso) | VERIFIED |
| three routes at `N=4tn`; EA form `[[N,N−k−h_E,d;k−h_E]]_q` | §7 | VERIFIED |
| distance = min weight of `D^{⊥_E}/Hull_E(D)` | Thm (cosetdistance) | VERIFIED |
| coset Singleton bound `K+d≤N+1` | Thm (cosetsingleton) | VERIFIED |
| 28 codes, three independent methods | §8 | VERIFIED |
| `[[24,8,4]]_9`, `[[20,4,4]]_4` | §8, §10 | VERIFIED |
| EA codes up to `[[20,2,10;18]]_4` | §8, §10 | VERIFIED |
| "No record parameters are claimed." | §10 | VERIFIED |

## 3. Manuscript element checklist

| element | expected | found | status |
|---|---|---:|---|
| Title | unchanged | *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings* | VERIFIED |
| Keywords | 1–7 | **7** | VERIFIED |
| Worked examples | 13 | **13** (03:2, 04:2, 05:4, 06:2, 07:2, 08:1) | VERIFIED |
| Section 7 examples | 2 present | `ex:fpbasis` (line 300), `ex:routes` (line 333) | VERIFIED |
| Tables | 6 | **6** (05:1, 08:2, 09:1, appendix:2) | VERIFIED |
| Figures | 0 | **0** | NOT APPLICABLE |
| Appendices | A, B | **A** (certification table + comparison data), **B** (reproducibility) | VERIFIED |
| References in `.bib` | 13 | **13** | VERIFIED |
| Rendered bibliography entries | 13 | **13** | VERIFIED |
| Pages | — | **42** | VERIFIED |

## 4. Final quantum parameter table — checked, unchanged

| family | best codes | relation to literature |
|---|---|---|
| Stabilizer | `[[24,8,4]]_9`, `[[20,4,4]]_4` | every `d≥3` code is **1–2 below** best known; at `d=2` at best equal |
| Entanglement-assisted | `[[20,2,10;18]]_4`, `[[24,2,10;18]]_9` | **unbenchmarkable** — no EA table exists |
| Over `F_8` | several | **unbenchmarked** — no `q=8` entries in Grassl's tables |

**No record parameters are claimed.** No numerical value was altered.

## 5. Supplementary-material references

`PAPER/FFA_SUBMISSION_STAGING/sections/08_certification.tex` line 224 refers
to material "listed in the supplementary material", and line 229 points to
Appendix A. **However**, FFA requires:

> "Cite **all** supplementary files in the manuscript text."
> "Include a **concise caption for each supplementary file**, describing its
> content."

The current text refers to the supplementary material **in general**, not to
individual files, and **no per-file captions exist**. This is a
**PENDING** item requiring a researcher decision about what is supplementary
rather than in-article. It is recorded in
`PHASE12_RESEARCHER_ACTION_ITEMS.md` (B4/B5).

## 6. Declarations — current state

| section | status |
|---|---|
| Acknowledgements | PENDING (optional) |
| Declaration of competing interests | **CONFIRMED** |
| Funding | **CONFIRMED** |
| Author contributions (CRediT) | PENDING (encouraged) |
| Data availability | **PENDING — blocking** |
| Generative AI | **PENDING — blocking** |

Rendered correctly on page 37 of the compiled PDF.

## 7. Highlights — still missing

FFA "encourages" 3–5 bullet points, each ≤ 85 characters, in a separate
editable file with "highlights" in the filename. **Not yet written** — they
should be drafted from the contribution hierarchy in
`PHASE11_MANUSCRIPT_POSITIONING.md` §D3, but they make claims about novelty
and so require researcher confirmation.

## 8. Conclusion

**No guideline violation and no factual error was found.** The abstract is
preserved exactly as Phase 11 approved it. Every mathematical statement and
numerical parameter is unchanged. The outstanding items are declaration
content that only the researcher can supply, plus supplementary-file
captioning — not defects in the manuscript.
