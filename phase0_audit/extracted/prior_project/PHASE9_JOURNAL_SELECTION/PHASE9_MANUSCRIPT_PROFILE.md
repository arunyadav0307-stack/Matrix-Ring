# Phase 9 — Manuscript profile

**Date:** 2026-11-10
**Source of every statement below:** the verified Phase 8B package
(`MatrixRingManuscript_20261110_Phase8B.zip`,
sha256 `6d39f643…86fec0`), read from the read-only inspection copy at
`PHASE9_JOURNAL_SELECTION/_inspection/`. Nothing here is inferred from outside
the manuscript or from the journal research.

---

## 1. Identity of the object being placed

| field | value |
|---|---|
| working title | *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings* |
| author metadata | `\AUTHORPLACEHOLDER` — deliberately unresolved; no author/affiliation invented |
| MSC 2020 | 94B05 (linear codes, general), 94B15 (cyclic codes), 94B60 (cryptography), 16S50 (endomorphism rings / matrix rings), 11T71 (algebraic coding theory) |
| keywords | cyclic codes over rings; matrix rings; Galois duality; Galois hulls; Gray map; quantum stabilizer codes; entanglement-assisted quantum codes |
| current source | plain `article` class, 11 pt, A4 — **no journal class or template applied** |
| bibliography style | `plain` (retained by decision D-1, 2026-11-10; DOI display deferred to journal-specific formatting) |
| references | 13 entries, all cited |
| body | 10 numbered sections + 2 appendices; 43 theorem-like environments; 13 worked examples; 107 labels |

Section structure and word counts (measured with `PAPER/tools/manuscript_stats.py`):

| section | words | role |
|---|---|---|
| 1 Introduction | 891 | framing, what is and is not claimed |
| 2 Literature | 752 | positioning against 13 cited works |
| 3 Preliminaries | 1309 | ring, module and code conventions |
| 4 Cyclic and Galois structure | 1115 | right ideals of `R_n`, `θ_s`-duality |
| 5 Hulls | 1506 | hull theory without principality; the refutation |
| 6 Expansion to `F_q` | 1563 | the transported Hermitian form and Hankel Gram |
| 7 Quantum codes | 1452 | three routes, coset-distance theorem, Singleton bound |
| 8 Certification | 1630 | 28 codes, three independent methods, reproducibility |
| 9 Comparison | 787 | contrast with the nearest published work |
| 10 Conclusion | 434 | summary and open problems |
| Appendix A (tables) | 216 | parameter tables |
| Appendix B (reproducibility) | 543 | how the computation is reproduced |

Total main body ≈ 13 827 words; ≈ 13 300 with the front matter and appendices
counted as above. **This is a full-length research article, not a short
communication.**

## 2. The main contribution, stated without inflation

The paper does one thing and then tests it. It sets up a Galois duality for
cyclic codes over the **noncommutative** ring `R = M₂(A_t)` where
`A_t = F_q[u]/⟨u^t⟩`, using the anti-automorphism `θ_s = σ_s ∘ (·)^T`
(`σ_s` = coefficient Frobenius `a ↦ a^{p^s}`), with codes taken as **right
ideals** of `R_n = R[X]/⟨X^n − 1⟩`. It then:

1. proves the duality and hull theory for arbitrary right ideals, **with no
   principality hypothesis**;
2. **refutes** the natural conjecture that Galois hulls are principal —
   hulls with minimal generator number `MU_B = 3` exist, and `MU_B ≥ 3` forces
   `t ≥ 2` and `p | n`;
3. shows the coefficient-expansion map to `F_q^{4tn}` transports the Galois
   pairing to an explicitly identified `σ̂_s`-Hermitian form whose Gram is the
   **Hankel matrix `I_{4n} ⊗ H_t`** — *not* the Euclidean form unless `t = 1` —
   and that this map preserves both duality and hulls, non-principal ones
   included;
4. proves every Galois hull is self-orthogonal for the transported form **with
   no reflexivity hypothesis** (a genuinely one-sided argument);
5. derives three quantum constructions of length `N = 4tn` — a Galois-native
   twisted stabilizer route, a Euclidean/CSS route, and an
   entanglement-assisted route `[[N, N − k − h_E, d; k − h_E]]_q`;
6. proves a **coset-distance theorem** (distance = minimum weight of the
   quotient code `D^{⊥_E} / Hull_E(D)`) and from it a **coset Singleton bound
   `K + d ≤ N + 1`**, which the paper shows is neither the EA Singleton bound
   nor implied by it (`prop:newsbound`);
7. certifies **28 codes** by three independent methods over an enlarged family
   list, including the first stabilizer distance `d = 4` in this framework
   (`[[24,8,4]]_9`, `[[20,4,4]]_4`) and EA codes up to `[[20,2,10;18]]_4`.

The abstract says, verbatim: **"No record parameters are claimed."**

## 3. Area and subfields

| axis | placement |
|---|---|
| primary | algebraic coding theory over finite rings (MSC 94B05, 94B15) |
| secondary | associative algebra / matrix rings over finite chain rings (MSC 16S50) |
| secondary | finite fields and their applications (MSC 11T71) |
| application layer | quantum error correction: stabilizer and entanglement-assisted constructions |
| adjacent (declared MSC but lightly used) | cryptography (94B60) — the paper cites no cryptographic construction and proves no cryptographic result |

The honest characterisation: **the paper is an algebra-of-codes paper whose
payoff is a table of quantum code parameters.** Its engine is ring-theoretic
(matrix rings, anti-automorphisms, non-principal modules); its advertised
output is quantum. A venue is a good fit only if it values *both* halves — or
if it values the algebra enough that the quantum table is welcome as an
application rather than judged as the main claim.

## 4. Type of result

* **Structural / theorem-driven.** 43 theorem-like statements (theorems,
  lemmas, propositions, corollaries, definitions, remarks, conjectures).
* **Counterexample-bearing.** The `MU_B = 3` refutation is a genuine negative
  result, and negative results are a good fit for journals that publish
  structural coding theory; they are a poor fit for journals that look for
  performance gains.
* **Computational but not a computation paper.** §8 certifies 28 codes with
  three independent methods and Appendix B gives reproducibility detail, but
  there is no algorithm-complexity analysis, no benchmark against prior art on
  running time, and no software artefact of record.
* **Self-contained and long-form.** Every one of §3–§8 ends with a worked
  example; 13 examples in total. This is a paper that teaches its own
  machinery, which is a virtue for a broad algebra-of-codes readership and a
  length liability for page-limited venues.

## 5. Intended readership

1. Researchers in codes over rings and modules (the `M₂(F_q)` / `M₂(A_t)`
   line: Alahmadi–Solé, Luo–Parampalli, Dinh, Si–Niu, Joshi–Patel–Prakash).
2. Researchers in Galois and Hermitian hulls and their quantum applications
   (the Fan–Zhang, Liu–Pan, Cao, Zhang–Kong–Zheng line).
3. Quantum-coding researchers who consume hull-based constructions and check
   parameters against tables (Grassl).

Not targeted: cryptographic protocol designers, complexity theorists, or the
experimental/physical QEC community. The MSC entry 94B60 notwithstanding,
**there is no cryptographic content in the paper**, and this is a scope
consideration for one candidate below.

## 6. Genuine strengths

1. **A real refutation.** The paper does not merely extend a known
   construction; it disproves a conjecture that a reader of the commutative
   literature would naturally form. That is the kind of result that survives
   review in a mathematics journal even when the parameters are modest.
2. **Honesty about scope.** §1.2 ("What the paper does and does not claim")
   and the self-audit §4 enumerate six explicit non-claims, including that no
   record parameters are claimed, that all components are attributed to prior
   work, and that the paper is not submission-ready while open issue M-1
   stands. This is unusual and it is an asset with careful referees.
3. **A structural novelty with no commutative analogue.** The `MU_B ≥ 3`
   criterion (`t ≥ 2` and `p | n`) is a statement about noncommutative
   modules; §9.4 notes it has no counterpart in the commutative setting.
4. **An exact transported form.** The Hankel Gram `I_{4n} ⊗ H_t` is identified
   exactly, not just up to equivalence, and the paper is explicit that it is
   not the Euclidean form unless `t = 1`. Referees can check this.
5. **Self-orthogonality proved without reflexivity.** A one-sided argument in
   a setting where the two-sided hypothesis is the standard assumption.
6. **A new bound with a stated independence.** `K + d ≤ N + 1` is proved from
   the coset-distance theorem and the paper argues it is not implied by the EA
   Singleton bound.
7. **Triple certification.** 28 codes verified by three independent methods,
   with the reproducibility path written out, is more verification effort than
   most coding papers carry.
8. **Bibliography is already inside the target community.** Five of the
   candidate journals are venues the paper already cites (see
   `PHASE9_SOURCE_VERIFICATION.md`, §4).

## 7. Genuine limitations — the ones a referee will find

These are taken from the manuscript's own self-audit and from the profile
above. They are listed because journal choice should be made with them in
view.

**Limitations the manuscript itself declares (§1.2 and self-audit §4):**

1. **No record parameters.** By the paper's own admission. A venue whose
   editorial culture rewards improved tables will read this as a weakness.
2. **All components are attributed to prior work.** The contribution is
   architectural: the assembly, the noncommutative setting, the refutation,
   and the two new theorems. There is no new primitive.
3. **Not submission-ready while M-1 stands** (the untypeset-supplement issue).
4. **The Pareto frontier is a frontier of the scanned families only**, not of
   all codes in the framework.
5. **The characteristic-two obstruction is limited to `p = 2` with `t` even** —
   a partial, not general, statement.

**Open minor issues recorded in the self-audit (m-1 … m-6):**

| id | issue |
|---|---|
| m-1 | one code value (`[[24,4,5;12]]_4`) changed between passes |
| m-2 | the Phase-7 comparison table is incomplete |
| m-3 | M3 is a **lower bound** for most codes, not an exact value |
| m-4 | 15 of 42 scanned families are unreachable by the method |
| m-5 | two conjectures are stated but never used |
| m-6 | witness-dimension bookkeeping is ambiguous in places |

**Limitations visible from the profile that the self-audit does not list:**

7. **Length.** ≈ 13 300 words of body with 43 theorem-like environments and 13
   worked examples. This is comfortably over IEEE TIT's 25-page final
   two-column limit, and it will invite a "please shorten" request anywhere
   the journal has an implicit norm.
8. **The quantum payoff is modest relative to the algebraic effort.** The
   headline stabilizer result is `d = 4`. Readers who arrive for the quantum
   parameters and leave with `[[24,8,4]]_9` may judge the return thin.
9. **The 94B60 (cryptography) MSC entry is not matched by cryptographic
   content.** If the paper is sent to a cryptography-flavoured venue on the
   strength of that MSC code, a referee can reasonably object on scope.
10. **No preprint/DOI and no stated author metadata.** Venues that require
    ORCID for all authors, or that ask for a competing-interests / data
    statement at submission, will need those supplied before submission.
11. **Bibliography of 13 entries for a paper of this length is narrow.** A
    referee working in hulls may expect the broader hulls-and-QEC literature
    to be engaged; this is an easy objection to raise at desk stage.

## 8. What the paper is *not*

* Not a parameters paper. It does not claim to beat a table.
* Not a cryptography paper, despite MSC 94B60.
* Not a physical/experimental QEC paper. The quantum content is the
  *construction* of codes from algebraic data; there is no decoder, no noise
  model, no threshold, no hardware.
* Not a short communication. Any venue with a strict article-type or page cap
  will require a cut, and the paper's own §8/Appendix B certification material
  is the natural thing a page-limited venue would ask to drop — which would
  remove one of its real strengths.

## 9. Consequences for journal selection

Read straight off §§3, 6 and 7:

* The best-fit venues are those where **algebraic coding theory over rings is a
  core subject in its own right** and where a structural negative result plus
  an application section is a normal article shape.
* The next-best fits are **finite-fields / algebra journals** that accept
  coding-theoretic applications and where the word count and the 43 theorem
  environments are not a problem.
* The weakest fits are venues whose editorial culture is (**a**) quantum-physics
  or engineering-weighted, where the algebra would read as unmotivated and the
  parameters as unimpressive; (**b**) cryptography-weighted, where the scope
  mismatch in §7.9 is exposed; or (**c**) page-capped, where §7.7 bites first.
* Quartile is deliberately **not** used as a selection criterion — see
  `PHASE9_JOURNAL_COMPARISON.md`, §3, for the scoring framework and its stated
  limits.
