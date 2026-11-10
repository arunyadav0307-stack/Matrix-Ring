# Updated Phase-0 final recommendation (GO / MODIFY / STOP)
## Part 6 of the revision deliverables — supersedes §8 of `Phase_0_Report.md`

**Date:** 2026-11-04. **Scope:** Phase 0 only. Nothing in Phases 1–8 is proved or written.

---

## 1. Verdict

# ⚠ **MODIFY — conditional GO, with the parameter restriction sharpened**

The first Phase-0 report already recommended MODIFY. The revision **strengthens the
feasibility case** (the pairing is no longer a hypothesis: it is proved, and verified in
seven runs, including one at $t=2$) and **adds one hard new constraint** that was not
visible before:

> **Reflexivity constraint.** $C\mapsto C^{\perp_s}$ is a *reflexive* duality on right
> submodules **iff $r\mid 2s$** (register T-017; `PAIRING_COMPLETE_PROOFS.md` Thm 3.9).
> So a nontrivial **and** reflexive Galois duality exists only for even $r$, with
> $s\equiv r/2 \pmod r$ — the "Hermitian-like" choice. **At $q=8$ ($r=3$) there is no
> nontrivial reflexive choice at all** (reflexivity fails for 702 of 737 codes).

Everything else in the verdict is unchanged in substance, and two of the four original
modifications are now *executed* rather than *proposed*.

---

## 2. What changed since the first Phase-0 report

| Item | Before | Now |
|---|---|---|
| Pairing | proposed $\theta_s=\sigma_s\circ{}^{\mathsf T}$, "experiments support it" | **proved**: additivity, anti-multiplicativity, non-degeneracy, right-module dual, cyclicity of the dual, size formula, double dual, hull closure, $R$-valued $=$ $\mathbb F_q$-valued (register T-002–T-010) |
| $\theta_s$ as involution | implicitly assumed in places | **proved**: $\theta_s^2=\sigma_{2s}$; involution $\iff r\mid2s$ (T-015). Never asserted without the check |
| $q=p$ case | flagged as trivial | proved trivial (T-003) and excluded from all Galois claims |
| $q=2$ experiments | used loosely | explicitly downgraded to *enumerator validation only*; not Galois evidence |
| Parameter advice | "require $r\ge2$, $m=2$" | **sharpened**: require $r$ even and $s=r/2$ (T-017), $m=2$ primary, $t=2$ verified at $n=1$, $t\ge2$ otherwise open-but-uniform-in-$t$ |
| $t=1$ enumeration | 35 cyclic codes at $q=2,n=3$ (one method) | formula $\#=\prod_j\sum_i\bigl[\begin{smallmatrix}m\\i\end{smallmatrix}\bigr]_{q^{d_j}}$ over the **central** factorization (T-018), validated at 343, 737, 144, 5, 35 |
| A1 (Alahmadi et al.) | "closest paper; right-ideal convention confirmed" | direct code verification done: their structure theory, read literally, produces at most 15 of the 35 length-3 codes; discrepancy explained by the non-central $\mathbb F_4$-factorization. **No claim that A1 is wrong.** |

---

## 3. Required modifications (updated)

| # | Blueprint as written | Required modification | Evidence |
|---|---|---|---|
| **M1** | Inner product "candidate formulas are hypotheses" | Adopt $\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i$ (and $\Lambda(\cdot)$ for the $\mathbb F_q$-valued version). **Done — proved.** | T-002–T-010; plain product provably broken (T-006) |
| **M2** | $q=p^r$, $m=2,3,4$ alternatives | **Require $q=p^{2e}$ and $s=r/2$** (equivalently $r\mid2s$ with $r\nmid s$); $m=2$ primary, $t=1$ first, $t\ge2$ second | **T-017** (new, decisive): reflexivity $\iff r\mid2s$; 35/737 at $q=8$ |
| **M3** | "Cyclic codes over noncommutative matrix rings" | Fix **cyclic = right ideal**; never two-sided | O6, A1 convention |
| **M4** | Working title | Keep provisionally; add the qualifier "$\theta$-Galois" once M1 is ratified | — |
| **M5** (new) | (absent) | **Do not import A1's Theorem 1 / Lemma 2 structure theory.** Use the central ($\mathbb F_q[X]$) factorization and Morita (T-018) | `ALAHMADI_THEOREM_RECONCILIATION.md` §4, §7 |
| **M6** (new) | (absent) | Any statement of the form "every cyclic code has a generator polynomial / is principal" must carry the hypothesis $t=1$ **and** $\gcd(n,p)=1$ until T-021 is proved in general | T-021 is conditional |

---

## 4. Ring comparison ($m=2,3,4$) — updated with the revision's data

| | $m=2$ | $m=3$ | $m=4$ |
|---|---|---|---|
| Alphabet size $|R|$ (at $q=4,t=1$) | 256 | 6561 | 65536 |
| #cyclic codes, $n=3$, $q=4$ (T-018) | $7^3=343$ | $(\sum_i[\begin{smallmatrix}3\\i\end{smallmatrix}]_4)^3=(1+21+21+1)^3=44^3$ | $(1+85+3570+85\ldots)^3$ — grows fast |
| Computational tractability | exhaustive enumeration feasible ($n\le4$) | enumeration feasible only via Morita+CRT; per-code checks still cheap | same as $m=3$, but $|\!\operatorname{Hom}|$ data larger |
| Duality (T-007, T-017) | verified exhaustively at $q=4,8,9$ (+ $t=2,n=1$) | proved for all $m$; **not** computed | proved for all $m$; **not** computed |
| Novelty target | primary (A1–A3, A6, A7 are all $m=2$; $m=4$ now appears in arXiv:2602.18255) | secondary | secondary (partially occupied) |
| **Recommendation** | **primary** | keep as a Phase-3+ extension | keep as a Phase-3+ extension |

The revision adds no reason to change the $m=2$ priority; it does add a reason to be
explicit that **all duality statements are proved for every $m$** (they are uniform in
$m$), while the *computations* are $m=2$ only.

---

## 5. Obstacles (updated)

| ID | Obstacle | Status after revision |
|---|---|---|
| O1 | Side convention | **resolved by decision**: right ideals (M3) |
| O2 | Entrywise Frobenius vs matrix multiplication | **resolved**: proved to be an automorphism (T-002, T-003); the transpose twist is what makes it an anti-automorphism (T-002) |
| O3 | Plain product pairing broken for right modules | **resolved**: proved failure (T-006) + working replacement (T-007) |
| O4 | $X^n-1$ must be factored over the **centre** | **new / confirmed by A1 reconciliation** (T-018, T-019) |
| O5 | Reflexivity | **new**: only when $r\mid2s$ (T-017) |
| O6 | Two-sided codes kill novelty | unchanged — excluded |
| O7 | Principality | **partially resolved**: conditional at $t=1$ & $\gcd(n,p)=1$ (T-021); open otherwise |
| O8 | Gray map / field-linearity for the quantum step | **unchanged — still open, highest risk** (T-012) |
| O9 | Hull-dimension formulas | **unchanged — open** (T-011); distributions recorded |
| O10 | $t\ge2$ | **partially closed**: all duality statements are uniform in $t$ and verified at $t=2,n=1$ (T-022); structure theory (principality, enumeration) open |

---

## 6. Decision table with falsifiable tests (for the auditor)

| If | Then |
|---|---|
| You accept T-007, T-016, T-017 and M1–M6 | **GO to Phase 1** with $q=p^{2e}$, $s=r/2$, $m=2$, $t=1$ first |
| You reject T-017's *interpretation* (reflexivity not needed for hull/quantum work) | **GO with M2 relaxed** to $r\ge2$: the size formula, dual closure and hull closure hold without reflexivity (100 % in all parameter sets). State this explicitly, because it changes the title/abstract |
| You find a flaw in T-007 (size formula / right-module dual) | **STOP** — the whole duality collapses |
| You find a flaw in T-006 (plain product failure) | **downgrade** the novelty claim (the "warning" section of the paper disappears) but keep the rest |
| You consider the A1 discrepancy (§7 of the reconciliation) a defect of our model | **STOP until resolved** — our enumeration underpins T-018 and every count in the project |

**Falsifiable novelty tests (unchanged in spirit, sharpened):**

1. *Duality test.* If a commutative-style $\sum x_i\sigma_s(y_i)$ pairing gave a perfect
   duality on **right** ideals of $M_2(\mathbb F_{q})$, our $\theta$-twist would be
   unnecessary. **Falsified**: 31/35 codes break it at $(q,t,m,n)=(2,1,2,3)$, and the
   plain product breaks the size formula in every parameter set tested (8/343 … 2/32).
2. *Reflexivity test.* If reflexivity held at $q=8$, T-017 would be false. **Not
   falsified**: 35/737, with explicit witnesses.
3. *Novelty test.* If there existed a published Galois-hull construction over a
   **non-commutative** alphabet with a proved duality on right ideals, GAP1 would
   collapse. **Not falsified** in the 17-entry verified bibliography (all Galois-hull
   papers found are over commutative rings).

---

## 7. What Phase 1 must do first (not to be started now)

1. Fix the final parameter triple $(p,e,m,t,n)$ with $q=p^{2e}$, $s=r/2=e$.
2. Write the structure theory over the centre: CRT + Morita for $R_n$ at $t=1$ (T-018)
   and, if $t\ge2$ is chosen, the corresponding classification of $A_t$-submodules of
   $A_t^m$.
3. Prove principality (T-021) in the chosen setting, or change the manuscript plan.
4. Only then: hull-dimension formulas (T-011) and the Gray map (T-012).

---

## 8. Unresolved issues (updated list)

| ID | Issue | Where recorded |
|---|---|---|
| U1 | The repository contains no PDFs of the papers (`Matrix Ring.zip` is an empty archive); all literature verification was done against primary web sources | `Phase_0_Report.md` §9 |
| U2 | Publisher DOI of A1 not confirmed (arXiv DOI only) | `01_LITERATURE/references.bib` |
| U3 | Luo–Parampalli (2018) volume/pages to confirm | bibliography |
| U4 | Bhowmick–Bagchi–Bandi ($M_2(\mathbb Z_4)$) — journal unconfirmed, **do not cite** | bibliography (D-list) |
| U5 | Principality for $t\ge2$ or $p\mid n$ | T-021 |
| U6 | Gray map with a duality relation | T-012 |
| U7 | Hull-dimension formulas | T-011 |
| **U8 (new)** | **A1 reconciliation**: is their Lemma 2 / Theorem 1 meant over $\mathbb F_2[X]$ (centre) or $\mathbb F_4[X]$, and does $(p)$ denote a right, left or two-sided generated object? Our 35 vs their 27 at $n=3$ hinges on this. **Adjudication requested.** | `ALAHMADI_THEOREM_RECONCILIATION.md` §6–§7 |
| **U9 (new)** | **Is reflexivity actually required** for the intended quantum construction? If not, the $r$ even / $s=r/2$ restriction can be relaxed (see §6). **Adjudication requested.** | register T-017 audit note |
| **U10 (new)** | $t=2$ computations exist only at $n=1$; $n\ge2$ at $t=2$ is untested | `NONTRIVIAL_GALOIS_EXPERIMENTS.md` §5.3 |

---

## 9. Risks (updated)

| ID | Risk | Level | Mitigation |
|---|---|---|---|
| R1 | Duality subtleties sink the project | **reduced** — duality is now proved, not assumed | T-002–T-010 |
| R2 | Novelty collapse | unchanged (medium) | bibliography + falsifiable tests §6 |
| R3 | Gray map / field-linearity for the quantum step | **unchanged — highest** | Phase 5 spike; do not promise a quantum code earlier |
| R4 | Parameter restriction ($r$ even) shrinks the family | **new, medium** | $q=p^{2e}$ still covers $q=4,9,16,25,\dots$; $q=8$ is out |
| R5 | Enumeration/bugs | **reduced** — two independent enumerations agree; 13 recorded bug fixes with a full audit trail | `UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` §6 |
| R6 | Over-claiming about A1 | **new, managed** — no claim that A1 is wrong; discrepancy reported with three reconciling conventions | reconciliation doc §0, §6 |

---

## 10. Phase control

* **Current phase: Phase 0 (completed, revised).** No Phase 1–8 theorem has been proved
  and no manuscript has been drafted.
* The four items in §7 are the **entry ticket** for Phase 1 and must be approved by the
  researcher before any of them is started.
* **Next action:** stop, push, and wait for the independent audit
  (`06_AUDIT/Phase0_audit_request.md`, updated with U8/U9).
