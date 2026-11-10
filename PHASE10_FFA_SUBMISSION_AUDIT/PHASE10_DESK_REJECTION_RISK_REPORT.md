# Phase 10 — Editorial and desk-rejection risk report (FFA)

**Journal:** *Finite Fields and Their Applications*
**Date:** 2026-11-10
**Scope of this report:** risks at FFA only. It does not compare journals and
does not recommend an alternative venue.
**Standard applied:** every risk is classified **GENUINE** (visible in the
manuscript or the verified record) or **SPECULATIVE** (a plausible editorial
reaction with no direct evidence). Remedies are **content-based** — framing,
signposting and emphasis — and **do not rewrite the mathematics**.

---

## 0. The editorial bar, in FFA's own words

> "… maintains **very strict refereeing standards, accepting only those papers
> which receive excellent referee reports**."
> "Your submission will initially be assessed by our editors. If your
> submission is deemed suitable, it will typically be sent to be reviewed by a
> minimum of two reviewers."

Two gates, therefore: an **editorial suitability screen** (desk-rejection
territory) and then a **two-referee quality gate** that FFA sets unusually
high. The risks below are tagged **[SCREEN]** or **[REFEREE]** or both.

---

## 1. The six risks named in the brief

### R-1. "The paper's mathematical focus may be too broad" — **GENUINE, moderate** — [SCREEN] [REFEREE]

**Why it is real.** The manuscript genuinely spans ring theory → coding theory
→ finite-field duality → module theory → expansion maps → quantum code
construction → computational certification. That is seven layers, ~13 300
words, 83 theorem-like environments, 6 tables, 2 appendices. An editor scanning
it may not know which of those layers is the contribution.

**Why it is only moderate, not severe.** The manuscript already answers the
objection in its own introduction: §1 displays the chain

> noncommutative matrix ring → cyclic codes → Galois duality and hulls →
> Gray map → quantum codes

and §1.2 states what the paper does and does not claim. The chain is explicit,
so the breadth is *declared* rather than accidental.

**Content-based remedy (no rewriting).**
* In the cover letter, name the **one** layer that is the contribution — the
  Galois duality and hull theory (§4–§5) — and describe the other layers as
  machinery and application. Do not present the paper as seven contributions.
* Signpost §1's chain diagram and §9.4's six-item novelty list as the two
  places where the scope is delimited. Both already exist.
* Point to Appendix B early: it shows the computational layer is supporting
  material, not a second paper.

### R-2. "The quantum applications may appear secondary to algebraic coding theory" — **SPECULATIVE as stated; the truth is the reverse and is a strength** — [SCREEN]

**Why the framing is wrong.** The risk as stated assumes FFA wants quantum
content to be primary. It does not. FFA's scope is finite fields, with
algebraic coding theory as a **named application area**; the quantum material
is downstream of that. For FFA, "the algebra is the paper and the quantum codes
are the application" is the *correct* shape, not a defect.

**The real risk in this area is the inverse:** that a reader arrives for the
quantum codes (the title leads with them), finds `[[24,8,4]]_9` against a best
known of 6, and judges the paper on that. That risk is **GENUINE** and is
covered by R-3.

**Content-based remedy.**
* Keep the title as it is for now (changing it is a manuscript modification and
  is not authorised), but in the cover letter **lead with the algebra** and
  introduce the quantum codes as the application that motivates it.
* Cite §1.2 and §9.3, where the manuscript already says the codes "are
  presented for their origin, not for their position in the tables".

### R-3. "The distance improvements may not be record-setting" — **GENUINE, and the most serious risk** — [REFEREE]

**Why it is real.** This is not speculative; it is in the manuscript's own
comparison table (§9.2). Every stabilizer code is at best equal to the best
known distance, and only at `d = 2` where equality is uninformative. Every code
with `d ≥ 3` is **one or two below** the best known value. The manuscript
states this itself and adds "No record parameters are claimed."

**Why it bites at FFA specifically.** FFA's coding-theory papers skew
parameter-forward: Vol 112 carries "linear codes with **new parameters**";
Vol 111 carries "**Quantum MDS** codes"; Vol 110 carries "large cyclic subspace
codes". And the competing 2026 papers in this exact niche all claim improved
parameters — Zhang–Kong–Zheng (*Entropy* **28**(4) 407) reports "new QECCs that
are better than the best known ones"; the AMC paper doi 10.3934/amc.2025054
reports EAQECCs that "outperform existing codes in terms of parameters".

**Content-based remedy (the honest one).**
* **Do not** try to make the parameters sound better. Any such attempt is
  contradicted by §9.2 in the first referee report.
* Reframe explicitly: the deliverable is the **algebraic origin** of the codes,
  not their table position, and the paper says so. Point to §9.3, which already
  makes this argument.
* Emphasise the **EA codes** as the paper's strongest numbers (`d = 10`) while
  stating plainly that they are unbenchmarkable — and note that the absence of
  an EA table is a gap in the literature, which is the manuscript's own
  argument and is factually correct.
* Lead with contributions 1–3 of
  `PHASE10_SCOPE_AND_NOVELTY_ASSESSMENT.md` §3, none of which depends on
  parameters.

### R-4. "Some field-size benchmarks are unavailable" — **GENUINE, low severity** — [REFEREE]

**Why it is real.** Verified: codetables.de offers no entanglement-assisted
table (`QECC-EA.php` → HTTP 404) and does not offer `q = 8`. Consequence: of 28
certified codes, 10 can be benchmarked and **18 cannot**, including all 14
`q = 8` codes and every EA code.

**Why severity is low.** This is an external-data limitation, not a defect in
the work, and the manuscript discloses it in §9.1 in unusual detail — it even
records that an earlier phase of the project misread the prime-versus-field
labelling convention and logged the correction as erratum **E-8.1**. A referee
who reads §9.1 sees a limitation stated before any number is quoted.

**Content-based remedy.**
* Signpost §9.1 explicitly in the cover letter: the benchmark gaps are stated
  up front, not buried.
* Do not quote `q = 8` or EA parameters as achievements; quote them as
  constructions and note they are unbenchmarked.

### R-5. "Some constructions use substantial entanglement" — **GENUINE as a fact, SPECULATIVE as a risk** — [REFEREE]

**Why the fact is real.** The EA route is `[[N, N − k − h_E, d; k − h_E]]_q`,
and several headline codes carry large `c`: `[[20,2,10;18]]_4` and
`[[24,2,10;18]]_9` consume 18 ebits. `[[24,6,4;18]]_9` and `[[24,4,9;20]]_4`
are similar. Some readers treat high entanglement consumption as diminishing
the practical value of a code.

**Why the risk is speculative.** FFA is not a quantum-engineering venue; there
is no verified editorial preference there about entanglement budgets, and the
EA framework (Brun–Devetak–Hsieh lineage) is standard in the coding literature.
The `c = k − h_E` formula is exact, not a compromise.

**Content-based remedy.**
* Present the EA route as one of **three** routes, with R2 (Euclidean/CSS)
  available whenever the transported form is Euclidean or a congruence exists —
  the manuscript already says R2 "is the only route whose distance is not
  capped by `min wt(D^{⊥_E})`, and it consumes no entanglement" (§7 remark).
* Make the trade-off explicit rather than hiding it: distance `d = 10` at
  `c = 18` is a stated point on a trade-off curve, and `thm:bookkeeping` and
  the entanglement-budget CSV give the full picture.
* Note `thm:feasibility`, which constrains when `d ≥ 4` can coexist with a
  bounded `c` — the paper has thought about the trade-off algebraically.

### R-6. "The manuscript includes several connected mathematical layers" — **GENUINE, moderate** — [SCREEN] [REFEREE]

**Why it is real.** Same root cause as R-1. Ten sections, ~60 subsections,
83 theorem-like environments, 13 worked examples (one closing each of §3–§8),
39 pages. There is a readability risk: an editor may not reach the result.

**Why it is survivable.** The layering is deliberate and the paper teaches its
own machinery; every one of §3–§8 ends with a worked example, which is exactly
the device that makes a layered paper readable.

**Content-based remedy.**
* In the cover letter, give the reader a **reading route**: §4 (duality) →
  §5 (hulls and the refutation) → §9.4 (what is new), with §6–§8 as transport,
  construction and verification.
* Point to §9.4's six numbered novelty items as the one-page summary.
* Do not apologise for the length. There is **no verified length limit** at FFA
  (see `PHASE10_FFA_OFFICIAL_GUIDELINES.md` §3, UNVERIFIED/not stated), and the
  examples are a feature.

---

## 2. Further risks found by this audit

### R-7. The "noncommutative" framing is deflatable by Morita — **GENUINE, high** — [REFEREE]

**The risk.** The title and the advertised novelty rest on noncommutativity,
but `03_preliminaries.tex` l.26–38 states `R_n ≅ M_2(B_q)` with `B_q`
commutative and notes the Morita correspondence is used "repeatedly" and is not
reproved. A referee can write: "by Morita this is a paper about submodules of
`B_q^2` over a commutative ring; what does the noncommutative framing add?" If
the paper has no answer ready, that is the review.

**There is a good answer, and the paper has it.** Noncommutativity is
load-bearing in the *pairing*: `lem:failure` shows the plain product fails on
right modules, and the transpose in `θ_s` is exactly what repairs the size
formula. `prop:twoorth` records two orthogonalities coinciding. That is real
content, not packaging.

**Content-based remedy.** State the division of labour up front: the
anti-automorphism is needed to *set up* the duality; the Morita equivalence is
what makes the *structure theory* tractable; and the residue — submodules of
`B_q^2` with `B_q = F_q[u,X]/⟨u^t, X^n−1⟩` — is where the finite-field content
lives, since the CRT decomposition is governed by the factorisation of
`X^n − 1` over `F_q`. This turns R-7 into the paper's FFA-native argument
rather than its weakness.

### R-8. No visible lineage into FFA — **GENUINE, low-to-moderate** — [SCREEN]

**The risk.** The manuscript cites **zero** FFA papers. (Verified: the 13
entries run to IEEE TIT ×3, DCC ×2, Entropy, AMC, Cryptogr. Commun., J. Franklin
Inst., AIMS Math., Amer. J. Math., arXiv, codetables.de.) An editor scanning
the bibliography sees no connection to the journal's community.

**Why severity is limited.** Scope fit is judged on content, not on who is
cited, and FFA publishes adjacent work — Vol 110 carries cyclic codes over
finite chain rings; Vol 112 carries hull dimensions and a nonexistence paper.

**Content-based remedy.**
* In the cover letter, connect the paper to FFA's own recent content
  explicitly: repeated-root cyclic codes over chain rings and hull-dimension
  work.
* If any of the 13 cited works has an FFA companion paper the researcher knows
  of, adding it is a bibliography decision **for the researcher**, not for this
  audit — Phase 10 modifies nothing.

### R-9. Crowded 2026 niche — **GENUINE, moderate** — [REFEREE]

**The risk.** "Quantum codes from hulls of cyclic/constacyclic codes over
finite rings" is being actively worked in 2026, and the competitors claim
better parameters: Zhang–Kong–Zheng (*Entropy* **28**(4) 407, April 2026,
commutative non-chain ring); Debnath–Islam–Martínez-Moro–Prakash (*Discrete
Math.* **349**(2) 114750, Feb 2026, affine algebra rings); AMC
doi 10.3934/amc.2025054 (small Galois hull dimensions, "outperform existing
codes"). A referee may read this manuscript as one more entry in a busy genre.

**Content-based remedy.** Differentiate on the two things none of those papers
have: the **noncommutative alphabet** with its anti-automorphism duality, and
the **refutation** (`MU_B ≥ 3` ⇐ `t ≥ 2` and `p | n`) plus the exact Hankel
Gram and the two bounds. The manuscript's own §9.4 already lists four concrete
differences from Zhang–Kong–Zheng. Lead with those.

### R-10. Abstract at or over the 250-word limit — **GENUINE, trivial** — [SCREEN]

Counted three ways: 257 / 246 / 230 words, against a verified hard limit of
250. This is a compliance defect, not a scientific one, but screeners notice.
Remedy: trim to ≤250 with margin. **Not done in Phase 10** — it is a manuscript
modification.

### R-11. FFA's stated acceptance bar — **GENUINE, structural** — [REFEREE]

"Accepting only those papers which receive excellent referee reports" is an
unusually explicit quality gate. Combined with R-3 (parameters below best
known), the practical implication is that the paper must be carried by
contributions 1–3 of the novelty assessment, and those must be unmistakable in
the first two pages. Everything in this report that concerns emphasis serves
this one risk.

### R-12. No preprint posted — **SPECULATIVE, low** — [SCREEN]

No preprint exists. FFA **permits** preprints and they do not count as prior
publication, so posting one is optional. It can help establish priority in the
crowded 2026 niche (R-9) but is a researcher decision, not a requirement.

---

## 3. Genuine versus speculative — summary

| risk | classification | severity |
|---|---|---|
| R-1 focus too broad | **GENUINE** | moderate |
| R-2 quantum appears secondary | **SPECULATIVE as stated** (the real risk is the inverse, covered by R-3) | low |
| R-3 distances not record-setting | **GENUINE** | **highest** |
| R-4 benchmarks unavailable | **GENUINE** | low |
| R-5 substantial entanglement | **GENUINE fact / SPECULATIVE risk** | low |
| R-6 several connected layers | **GENUINE** | moderate |
| R-7 Morita deflates "noncommutative" | **GENUINE** | **high** |
| R-8 no FFA lineage | **GENUINE** | low–moderate |
| R-9 crowded 2026 niche | **GENUINE** | moderate |
| R-10 abstract word count | **GENUINE** | trivial (fixable) |
| R-11 FFA's "excellent referee reports" bar | **GENUINE** | structural |
| R-12 no preprint | **SPECULATIVE** | low |

## 4. What this report does not say

* It does **not** say the paper will be desk-rejected. No prediction of any
  editorial outcome is made or implied.
* It does **not** say the paper is submission-ready. It is not: five
  submission-time artefacts are missing (author metadata, research-data Option C
  compliance, competing interests, funding, generative-AI declaration) — see
  `PHASE10_MANUSCRIPT_COMPLIANCE_MATRIX.md`.
* It does **not** propose any change to the mathematics. Every remedy above is
  a matter of emphasis, signposting or a submission-time artefact.
* It does **not** name an alternative journal.
