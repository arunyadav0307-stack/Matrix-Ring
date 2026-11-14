# PHASE 0 — Literature review, novelty assessment and mathematical feasibility

**Project:** Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes
over Noncommutative Matrix Rings
**Agent:** Arena AI (development agent, blueprint §6/§8A)
**Date:** 2026-11-04
**Status:** Phase 0 executed; **stopping for independent ChatGPT audit** (blueprint
§7 step 4, §8A "PHASE CONTROL").

> **Epistemic key used throughout this report**
> * **[EST]** Established mathematics (textbook / cited theorem).
> * **[PRP]** Proposed by me in this report, with a proof sketch that must be
>   written out in full in Phase 1/3.
> * **[CMP]** Computational observation from `04_COMPUTATION/` with a stated,
>   exhaustive parameter range.
> * **[LIT]** Claim read in a located source, with the source given.
> * **[OPN]** Open / unresolved; carries an explicit next action.

---

## 0. Scope, sources and what was actually done

| Activity | Detail |
|---|---|
| Literature search | Web search + direct retrieval of arXiv abs pages, DOI landing pages (MDPI *Entropy*, Springer *Cryptogr. Commun.*, AIMS *AMC* / *AIMS Math.*, Project MUSE). ca. 25 sources located, of which **17 are confirmed DIRECT** and 8 are marked SECONDARY/TO CONFIRM in `01_LITERATURE/annotated_bibliography.md`. |
| Repository inspection | `git log --all --name-only --diff-filter=A` on the connected repo returns exactly two files ever: `README.md` and `Matrix Ring.zip`. **`Matrix Ring.zip` contains a single empty directory entry — no papers are present in the repository.** Action required from the researcher (see §9, U1). |
| Computation | `04_COMPUTATION/matrix_ring_lib.py` (exact arithmetic: $\mathbb F_q$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$, $M_m(A_t)$, $R^n$, $\mathbb F_q$-linear algebra) + `phase0_feasibility.py` (5 experiments). Runtime 18.8 s, Python 3.11.2. Log: `04_COMPUTATION/phase0_results.txt`. |

**Not done (deliberately, per blueprint §8D):** no theorems of Phases 1–8 are
proved here, no quantum code is constructed, no manuscript text is written.

---

## 1. Deliverable 1 — Verified annotated bibliography
→ `01_LITERATURE/annotated_bibliography.md` (17 confirmed entries, 4 clusters,
plus a "do not cite until checked" list). Machine-readable version:
`01_LITERATURE/references.bib` (every entry carries a `note = {VERIFY: …}`
field).

## 2. Deliverable 2 — Literature comparison matrix
→ `01_LITERATURE/comparison_matrix.md` (13 rows × 9 columns + a 4-point
reading).

## 3. Deliverable 3 — The closest papers and exactly what they already prove

| # | Paper | What it already proves | What it leaves open that we need |
|---|-------|------------------------|----------------------------------|
| **A1** | Alahmadi–Sboui–Solé–Yemen 2013, *Cyclic codes over $M_2(\mathbb F_2)$*, J. Franklin Inst. 350(9) 2837–2847 | [LIT] cyclic codes over $A=M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$ = **right ideals** of $A[X]/(X^n-1)$; structure theorem $C=(fh)+u(fg)$ for $X^n-1=fgh$ over $\mathbb F_4$ ($n$ odd); Euclidean dual generators; Euclidean self-duality criterion $h=h^*$, $g=f^*$; no Hermitian self-dual cyclic code of odd length; Bachoc map $\phi(a+ub)=(a+b,b)$ is Hermitian-duality-compatible and sends a cyclic code to a Plotkin sum of its residue and torsion code | Galois duality; hulls; the side-convention problem (§6, O1/O2); quantum codes |
| **A3** | Dinh–Gaur–Kumar–Singh–Singh 2024, *Cyclic codes over rings of matrices*, AMC 18(4) 1100–1122 | [LIT] structure theorem for cyclic codes of odd length over $M_2(\mathbb F_2[u]/\langle u^k\rangle)$ via isometry onto $\mathbb F_4[u,v]/\langle u^k,v^2,uv-vu\rangle$; a map to length-$2kn$ codes over $\mathbb F_4$ | **This is our ring family ($m=2$, general $t$).** It proves nothing about duality beyond Euclidean/Hermitian, nothing about hulls, nothing about quantum codes |
| **A7** | Joshi–Patel–Prakash 2026, arXiv:2602.18255 | [LIT] $M_4(\mathbb F_2[u]/\langle u^k\rangle)$: ideals, cyclic codes as sums of submodules, cardinality formulas, Euclidean + Hermitian duals, Bachoc + Gray map to $\mathbb F_{16}$, good codes | Same three gaps (Galois / hull / quantum). Sets the bar for what a "matrix-ring + $u$-adic" paper must contain in 2026 |
| **B1** | Wood 1999, *Duality for modules over finite rings*, Amer. J. Math. 121 555–575 | [EST] finite **Frobenius** rings are exactly the alphabets for which MacWilliams extension + identities hold; character-theoretic duality for modules over **not necessarily commutative** finite rings | It is a framework paper: it does not treat cyclicity, hulls or quantum codes — we must do that ourselves |
| **C1** | Fan–Zhang 2017, *Galois self-dual constacyclic codes*, DCC 84 473–492 | [EST] the Galois inner product $\langle a,b\rangle_h=\sum a_ib_i^{p^h}$ (Frobenius on the **second** argument) over $\mathbb F_{p^\ell}$; $h=0$ Euclidean, $h=\ell/2$ Hermitian | The definition lives over a **field**. Transporting it to a non-commutative ring is *not* automatic — see §6, O1 |
| **C5** | Zhang–Kong–Zheng 2026, *Entropy* 28(4) 407, DOI 10.3390/e28040407 | [LIT] $\ell$-Galois duals + hulls of constacyclic codes over a **commutative** non-chain ring; Gray map with $\phi(C)^{\perp_\ell}=\phi(C^{\perp_\ell})$; construction X of the Galois inner product ⇒ QECC, EAQECC, QMDS | Everything here is commutative (CRT-split ring). This is the *template* our Phase 5–6 must match, and it is 7 months old |
| **C6** | Debnath–Islam–Martínez-Moro–Prakash, arXiv:2412.08512 | [LIT] $k$-Galois hulls over affine-algebra / **serial** (commutative) rings; hull-dimension formula; EAQECCs | Commutative; no matrix ring |

**Bottom line of §3:** the matrix-ring literature (A1–A7) and the Galois-hull
literature (C1–C6) are **disjoint**. Nothing found in Phase 0 sits in their
intersection, and nothing found in Phase 0 constructs a quantum code from a code
over a matrix ring.

---

## 4. Deliverable 4 — Comparison of candidate rings $M_m(A_t)$

Notation as fixed by the blueprint: $A_t=\mathbb F_q[u]/\langle u^t\rangle$,
$u^t=0$; $q=p^r$; $R=M_m(A_t)$; $t$ = nilpotency exponent; $s$ or $\ell$ =
Galois parameter (never $k$).

| Property | $m=2$ | $m=3$ | $m=4$ |
|---|---|---|---|
| $|R|$ | $q^{4t}$ | $q^{9t}$ | $q^{16t}$ |
| Non-commutative for $m\ge2$ | yes | yes | yes |
| Frobenius (⇒ duality well-behaved, B1) | yes **[EST]** | yes | yes |
| Chain ring? | **no** for every $m\ge2$ **[EST]** | no | no |
| Anti-automorphism available (transpose) | yes **[CMP]** | yes **[CMP]** | yes **[CMP]** |
| Literature precedent | **A1, A2, A3, A4, A6** (rich) | thin | A7 (2026) |
| Exhaustive computation feasible in Phase 0/7 | yes | up to $n\approx3$ | borderline |

| Property | $q=p$ ($r=1$) | $q=p^r$, $r\ge2$ |
|---|---|---|
| Nontrivial **field** Frobenius $\sigma_s(a)=a^{p^s}$ | **none** (all $s\equiv0 \bmod r$) **[CMP]** — E1 shows `nontrivial=False` for every $s$ | **yes** for $1\le s\le r-1$ **[CMP]** — E1: `nontrivial=True` for $q=4,9,16$ |
| $u$-scaling $\mu_c:u\mapsto cu$ | only $c=1$ ⇒ trivial | nontrivial for $c\neq1$ **[CMP]** (E1, $q=4,t=2$: `nontrivial=True`) |
| Inner automorphisms ($PGL_m$) | exist but are **hull-trivial** (see §5 remark) | same |

| Property | $t=1$ | $t=2$ | $t\ge3$ |
|---|---|---|---|
| $A_t$ | $=\mathbb F_q$ (a field) | $\mathbb F_q+u\mathbb F_q$ | longer chain |
| $\mathrm{Aut}(A_t)$ beyond Frobenius | – | $\mu_c$ | $\mu_c$ and $u\mapsto u+c_2u^2+\dots$ |
| Matches literature | A1, A4, A6 | A2, A3 | A3, A7 |

**Recommendation (provisional, to be ratified in Phase 1):**
$$m=2,\qquad q=p^r \text{ with } r\ge 2 \ (\text{e.g. } q=4),\qquad t\ge 1 .$$
Reasons: (i) $r\ge2$ is *necessary* for a genuinely nontrivial Galois parameter
$\sigma_s$ (blueprint §12: "If $q=p$, the field automorphism may be trivial;
this case must not be presented as a nontrivial Galois setting"); (ii) $m=2$
carries the Bachoc map and all precedent; (iii) $t\ge2$ additionally supplies
the $u$-scaling automorphism $\mu_c$, giving a *second* twist parameter.
The blueprint's original candidate list ($m=2,3,4$; $q=p^r$) is retained as
alternatives; $m=4$ is where the newest competitor (A7) lives.

**Hull-triviality of inner automorphisms.** [PRP] If $\theta(X)=PXP^{-1}$ is
inner, then $\langle x,y\rangle_\theta=\sum Px_iP^{-1}y_i$ and
$C^{\perp_\theta}=C^{\perp_E}\!\cdot P$-type objects, so the hull *dimension* is
unchanged. Inner twists therefore cannot generate new hull invariants and are
not a substitute for a Galois parameter. (To be written out in Phase 1.)

---

## 5. Deliverable 5 — Can a nontrivial Galois automorphism and a valid
## non-degenerate pairing exist? (tested, not assumed)

### 5.1 Automorphisms — EXPERIMENT E1 (`phase0_results.txt`, §E1)

Tested on $M_2(\mathbb F_2)$, $M_2(\mathbb F_4)$, $M_2(\mathbb F_2[u]/\langle u^2\rangle)$,
$M_2(\mathbb F_4[u]/\langle u^2\rangle)$, $M_3(\mathbb F_2)$, $M_2(\mathbb F_9)$
(randomised, 400 trials each; exhaustive on the smallest ring):

| Map | Additive | Multiplicative | Nontrivial |
|---|---|---|---|
| $\sigma_s$ = entrywise $a\mapsto a^{p^s}$ (any $m,t$) | ✔ | **✔ ring automorphism** | only if $r\nmid s$ |
| $\mu_c:u\mapsto cu$ | ✔ | **✔ ring automorphism** | if $c\neq1$ |
| $\theta_s=\sigma_s\circ{}^T$ | ✔ | **✔ ANTI-automorphism**: $\theta(XY)=\theta(Y)\theta(X)$ | if $r\nmid s$ |

**[CMP] + [PRP]** The entrywise extension of a ring automorphism of $A_t$ to
$M_m(A_t)$ *is* a ring automorphism (blueprint §12 flags this as something to
prove; the one-line proof is that matrix multiplication is defined by the same
addition/multiplication formulas in the entries, so applying $\sigma$ entrywise
commutes with both). **Feasibility verdict: YES, a nontrivial Galois
automorphism exists — provided $r\ge2$ (or $c\neq1$ for $\mu_c$).**

### 5.2 Pairings — EXPERIMENTS E2, E3, E4

Candidate functionals on $R=M_m(A_t)$:
* $\lambda(a)$ = coefficient of $u^{t-1}$ in $a\in A_t$ — the Frobenius
  functional of the chain ring $A_t$ **[EST]**;
* $\Lambda=\lambda\circ\mathrm{tr}$ on $R$ — verified **[CMP]** (E2) to be
  non-degenerate *and* "ideal-catching" on both sides for
  $(q,t,m)\in\{(2,1,2),(4,1,2),(2,2,2),(4,2,2),(2,1,3),(16,1,2)\}$, i.e.
  $\Lambda$ is a **generating functional** ⇒ $R$ is a symmetric Frobenius
  algebra with form $(X,Y)\mapsto\Lambda(XY)$ **[CMP] + [PRP]**.

Pairings tested on $R^n$ (`dot`, `dotT`, `sigmainv`, `theta`, `trace`,
`tracesigma`, `tracetheta` — see the library docstrings):

| Pairing | Formula | Value | Perfect duality for **left** modules | … for **right** modules | Side of the dual |
|---|---|---|---|---|---|
| `dot` | $\sum x_iy_i$ | $R$ | **YES** | **NO** | opposite |
| `dotT` | $\sum x_i^{\mathsf T}y_i$ | $R$ | NO | **YES** | **right** |
| `sigmainv` | $\sum\sigma^{-1}(x_i)y_i$ (= Fan–Zhang form) | $R$ | YES | **NO** | opposite |
| `theta` | $\sum\theta_s(x_i)y_i$, $\theta_s=\sigma_s\circ{}^{\mathsf T}$ | $R$ | NO | **YES** | **right** |
| `trace` | $\Lambda(\sum x_iy_i)$ | $\mathbb F_q$ | YES | YES | opposite |
| `trace-theta` | $\Lambda(\sum\theta_s(x_i)y_i)$ | $\mathbb F_q$ | YES | **YES** | **right** |

**[CMP]** E3 (exhaustive, $n=1$, all one-sided ideals of $M_2(\mathbb F_2)$,
$M_2(\mathbb F_4)$, $M_2(\mathbb F_2[u]/\langle u^2\rangle)$): the table above is
exactly what the computation returns; "perfect" means
$\dim C+\dim C^\perp=\dim_{\mathbb F_q} R^n$.
**[CMP]** E4 (exhaustive, $m=2,q=2,t=1,n=3$, all $2^{12}$ ambient vectors):
under `dot`, **31 of the 35** right-cyclic codes have a **broken** duality
($\dim C+\dim C^\perp\neq12$; for $\dim C=6$ the dot-dual is $\{0\}$); under
`theta`, **0 of 35** are broken and the hull is a right module in every case.

### 5.3 The central design decision (this is the main Phase-0 finding)

> **[PRP] Proposed framework.** Take cyclic codes to be **right ideals** of
> $R_n=R[X]/\langle X^n-1\rangle$ (the convention of A1–A3, A6, A7) and define
> the Galois pairing with the **anti-automorphism**
> $$\boxed{\ \theta_s=\sigma_s\circ{}^{\mathsf T},\qquad
> \langle x,y\rangle_s=\sum_{i=0}^{n-1}\theta_s(x_i)\,y_i\ \in R,\qquad
> [x,y]_s=\Lambda\!\Big(\sum_i\theta_s(x_i)y_i\Big)\in\mathbb F_q .}$$
>
> Then: (i) $C^{\perp_s}$ is again a **right** $R$-module and again cyclic;
> (ii) $|C|\cdot|C^{\perp_s}|=|R|^n$; (iii) the hull
> $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a **right $R$-module**, hence a
> cyclic code, so hull-dimension formulas make algebraic sense.

Why this works (proof sketches; full proofs are Phase-1/3 deliverables):
1. $\theta_s$ is an anti-automorphism **[CMP]**, so $\theta_s(C)$ is a **left**
   module when $C$ is a right module.
2. $C^{\perp_s}=\{\,y:\Lambda(\theta_s(C)\,y)=0\,\}$ is a **right** ideal:
   for $b\in R$, $\Lambda(uyb)=\Lambda(buy)$ (symmetry $\Lambda(XY)=\Lambda(YX)$)
   and $bu\in\theta_s(C)$ because $\theta_s(C)$ is a left ideal. **[PRP]**
3. Perfection follows from Wood's Frobenius duality (B1) applied to the left
   ideal $\theta_s(C)$. **[PRP]**
4. Cyclicity is preserved because both the shift and $\theta_s$ act
   entrywise/coordinatewise and commute with each other. **[PRP]**

Why the naive choices fail (this is the *reason* the project is not routine):
* The **ring-valued** $\sum x_iy_i$ dual of a **left** module is perfect, but
  the dual of a **right** module is only $\{y:\sum x_iy_i=0\}$, and the set
  $\{\sum x_iy_i:x\in C\}$ is then merely an $\mathbb F_q$-subspace, not an
  ideal, so $\Lambda$ vanishing on it does not force it to be $0$ — the dual is
  strictly too small. **[PRP]** + **[CMP]** (E3/E4).
* Transporting Fan–Zhang literally (Frobenius on the second argument, no
  transpose) has exactly the same defect for right ideals (`sigmainv` row).
* Using the $\mathbb F_q$-valued trace pairing alone gives a perfect duality but
  puts the dual on the **opposite** side, so the hull is only an
  $\mathbb F_q$-subspace — losing the module structure that makes hull
  dimension computable from generator data.

**Feasibility verdict on pairings: YES — a valid, non-degenerate,
module-preserving Galois pairing exists, but only in the $\theta_s$ form above.
This is a genuine mathematical choice, not a notational variant, and it is the
single most important decision coming out of Phase 0.**

---

## 6. Deliverable 6 — Mathematical obstacles (mapped to blueprint §12)

| ID | Obstacle | Status after Phase 0 | Mitigation |
|---|---|---|---|
| **O1** | Side flip: the dual of a one-sided code lands on the other side | **Resolved in principle** by the $\theta_s$ pairing (§5.3) | Must be proved in Phase 1 |
| **O2** | The ring-valued Euclidean dot product used by A1–A7 is **not** a perfect duality for right ideals — 31/35 codes at $(m,q,t,n)=(2,2,1,3)$ | **[CMP] + [PRP]**; this is a *warning about the existing literature*, not just about our setup | Phase 1 must (a) prove the failure, (b) decide how to state it in the paper without over-claiming |
| **O3** | Hull may fail to be a module | Resolved by $\theta_s$ (hull = right module, **[CMP]** all 35 codes) | Prove in Phase 3–4 |
| **O4** | Polynomial centrality / left-right closure for the quotient $R[X]/\langle X^n-1\rangle$ | **[EST]** $X$ is central by construction, so $R[X]/\langle X^n-1\rangle$ is a ring for any $R$; a right ideal = a right $R$-submodule closed under the shift | Fine — but must be stated explicitly (blueprint §2 "Research control") |
| **O5** | $R_n\cong M_m(A_t[X]/\langle X^n-1\rangle)$ | **[EST]** (matrix rings commute with adjoining a central variable and with quotienting by a central polynomial) | Gives the **Morita** classification below |
| **O6** | Two-sided cyclic codes collapse | **[EST]** two-sided ideals of $M_m(B)$ are $M_m(J)$, $J\trianglelefteq B$ ⇒ two-sided cyclic codes over $M_m(A_t)$ are *exactly* the matrix versions of cyclic codes over the **commutative** ring $A_t$. **[CMP]** verified: 4 two-sided cyclic codes at $m=2,q=2,t=1,n=3$ = number of ideals of $\mathbb F_2[X]/\langle X^3-1\rangle$ | **Avoid the two-sided route** — it is Morita-equivalent to a known commutative theory and kills novelty |
| **O7** | $q=p$ has no nontrivial field Frobenius | **[CMP]** E1 | Fix $r\ge2$, or use $\mu_c$ (blueprint §12 explicitly forbids presenting the trivial case as Galois) |
| **O8** | Gray/hull preservation | **open** — blueprint §12: "A Gray map may preserve some properties but not all" | Phase 5 must prove or refute $\Phi(C^{\perp_s})=\Phi(C)^{\perp}$; C5 shows the standard to meet |
| **O9** | CSS / EAQECC hypotheses | **open** — blueprint §12: "A Galois hull alone does not automatically produce a quantum code" | Phase 6; fallback = additive/stabilizer route (C9) |
| **O10** | Minimum distance of the image code | **open** | Phase 7; exhaustive only in a stated range, otherwise bounded/heuristic and labelled as such |

### 6.1 A structural by-product worth recording (Phase 2)

**[EST] + [PRP]** With $B=A_t[X]/\langle X^n-1\rangle$ (commutative) and
$R_n\cong M_m(B)$:
* left ideals of $R_n$ ⇄ $B$-submodules of $B^m$ (via **rows**);
* right ideals of $R_n$ ⇄ $B$-submodules of $B^m$ (via **columns**);
* two-sided ideals of $R_n$ ⇄ ideals of $B$.

Consequently a *complete* classification of one-sided cyclic codes over
$M_m(A_t)$ is equivalent to the classification of $B$-submodules of $B^m$, and
one-sided cyclic codes over $M_m(A_t)$ are precisely the
**$m$-generator "quasi-cyclic-like" codes over the commutative ring $A_t$** —
the same phenomenon as A10 (quasi-cyclic codes as codes over rings of matrices).

**[CMP]** At $(m,q,t,n)=(2,2,1,3)$ the enumeration finds **35** right-cyclic
codes, **35** left-cyclic codes and **4** two-sided ones, matching the Morita
prediction $|{\rm Sub}_B(B^2)|=5\cdot7=35$ and $|\mathrm{Id}(B)|=2^2=4$
($B\cong\mathbb F_2\times\mathbb F_4$).

---

## 7. Deliverable 7 — Candidate research gaps (with falsifiable novelty tests)

### GAP 1 — A valid Galois duality & hull theory for **one-sided** cyclic codes over a **non-commutative** matrix ring
* **Statement to prove (Phase 1–4).** With $\theta_s=\sigma_s\circ{}^{\mathsf T}$
  and $R=M_m(A_t)$: $C^{\perp_s}$ is cyclic; $|C||C^{\perp_s}|=|R|^n$;
  $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R$-module; generator- and
  parity-check-matrix descriptions; hull-dimension formulas (via Hermite/GPM
  normal forms over the chain ring $A_t$).
* **Evidence it is new.** All Galois-duality/hull papers found (C1–C6) are over
  **commutative** alphabets; all matrix-ring papers (A1–A7) use only
  Euclidean/Hermitian duality and never discuss hulls.
* **Falsifiable test.** Search (MathSciNet / zbMATH / arXiv full text) for
  *“Galois dual”* or *“$\sigma$-dual”* **and** a non-commutative (matrix) ring.
  If a paper already proves $|C||C^{\perp_\sigma}|=|R|^n$ for one-sided codes
  over $M_m(A_t)$, GAP 1 collapses to a re-derivation and must be
  re-scoped. — **Status: not executed (no MathSciNet access in this sandbox;
  must be done by the researcher or in Phase 1 with the papers).**

### GAP 2 — Complete classification of one-sided cyclic codes over $M_m(A_t)$, and a duality-corrected foundation
* **Statement (Phase 2).** The Morita classification of §6.1, plus explicit
  generator/parity-check data, plus the correction recorded in O2 (the
  ring-valued dot product is not a perfect duality for right ideals).
* **Evidence.** **[CMP]** At $(m,q,t,n)=(2,2,1,3)$ the complete enumeration
  gives **35** right-cyclic codes with dimension profile
  $\{0{:}1,2{:}3,4{:}6,6{:}15,8{:}6,10{:}3,12{:}1\}$, whereas the generator
  parametrisation of A1 ($C=(fh)+u(fg)$, $X^n-1=fgh$ over $\mathbb F_4$; $3^3=27$
  triples) produces at most **27** objects, and — under the three readings of
  the notation that I implemented — at most **19** of them are right-cyclic
  codes (`phase0_results.txt`, §E5).
* **⚠ Honest caveat.** This is a *computational observation under my reading of
  A1's notation*. Two explanations are possible: (a) my reading of
  "$(fh)+u(fg)$" is wrong; (b) the parametrisation of A1 is incomplete. I have
  **not** read A1's Section 3 line by line, and I have no access to the
  published (non-arXiv) version. **No claim about A1 is to be made in the
  manuscript until this is settled by hand** (blueprint rule 5 / §8A.5).
* **Falsifiable test.** Re-derive A1, Theorem 1 by hand and count cyclic codes
  of length 3 over $M_2(\mathbb F_2)$ independently. If the count is 35 and
  every one has the form $(fh)+u(fg)$, GAP 2 reduces to "re-derivation +
  Morita reformulation" (still publishable as a cleaner foundation, but not as
  a correction).

### GAP 3 — Quantum codes from matrix-ring codes
* **Statement (Phase 5–6).** Construct a map $\Phi:R^n\to\mathbb F_q^{N}$
  (Bachoc-type for $t=1$, a new $u$-adic Gray map for $t\ge2$) with a proved
  duality relation $\Phi(C^{\perp_s})=\Phi(C)^{\perp_\bullet}$, then apply CSS
  (dual-containing case) and the EA route (hull-dimension case) to obtain
  $[[n',k',d']]_q$ and $[[n',k',d';c]]_q$ families; compare with Grassl's tables.
* **Evidence it is new.** No paper found in Phase 0 constructs **any** quantum
  code from a code over a matrix ring; A1–A7 all stop at classical codes over
  $\mathbb F_4/\mathbb F_{16}/\mathbb F_{p^2}$.
* **Falsifiable test.** Search for *quantum* **and** ($M_2(\mathbb F_2)$ or
  $M_m(A_t)$ or "matrix ring"). If found, GAP 3 must be re-scoped to a
  parameter comparison.

---

## 8. Deliverable 8 — GO / MODIFY / STOP recommendation

# ⚠ RECOMMENDATION: **MODIFY** (conditional GO)

The project is **mathematically feasible** — that is the main Phase-0 result,
and it is backed by computation, not by optimism. But the framework as stated
in the blueprint needs four specific modifications before Phase 1, otherwise
Phases 3–6 would be built on a pairing that silently fails.

### Required modifications

| # | Blueprint as written | Required modification | Why (evidence) |
|---|---|---|---|
| **M1** | Inner product "candidate formulas are hypotheses"; Galois product presumably $\sum x_i\sigma_s(y_i)$ | Adopt $\theta_s=\sigma_s\circ{}^{\mathsf T}$ and $\langle x,y\rangle_s=\sum\theta_s(x_i)y_i$ (with the $\mathbb F_q$-valued version $\Lambda(\cdot)$ for the quantum step) | E3/E4: the Fan–Zhang shape gives a **broken** duality for right ideals (31/35 codes); $\theta_s$ gives a perfect one with a right-module dual |
| **M2** | $q=p^r$, $m=2,3,4$ "alternatives" | **Require $r\ge2$** for any "Galois" claim; adopt $m=2$, $t\ge1$ as the primary setting, keeping $m=3,4$ as secondary | E1: for $q=p$ every $\sigma_s$ is the identity (blueprint §12 explicitly forbids the trivial case) |
| **M3** | "Cyclic codes over noncommutative matrix rings" | Fix the convention explicitly: **cyclic = right ideal** (matching A1–A3, A6, A7) and **never** use two-sided codes | O6: two-sided cyclic codes are Morita-equivalent to commutative ones (novelty dies); O1: side convention drives the entire duality |
| **M4** | Title: "…from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings" | Keep the title *provisionally*; add the qualifier **"$\theta$-Galois"** (or "anti-automorphism Galois") in the abstract/keywords once M1 is ratified; be ready to change it after Phase 4 | Blueprint §13 allows/encourages a title change; the $\theta$ qualifier is what makes the contribution precise and searchable |

### Why not plain GO
Because GO would let Phase 1 start from the (incorrect) assumption that the
standard Euclidean/Galois dot product transfers to the matrix ring. Our own
computation says it does not (31/35 broken; for $\dim C=6$ the dot-dual is
$\{0\}$, which would make every hull dimension come out $0$).

### Why not STOP
Because every obstacle (O1–O3, O6, O7) has a concrete, computationally
verified remedy, the ring family is Frobenius (so Wood's duality theory is
available), and the target intersection is empty in the located literature.

---

## 9. Unresolved issues and questions for the researcher

| ID | Issue | Required action |
|---|---|---|
| **U1** | **The connected repository contains no papers.** `git log --all` shows only `README.md` and `Matrix Ring.zip`; the zip holds a single empty directory entry. The user's instruction ("papers are in the git repo, take them when needed") cannot currently be carried out. | **Researcher:** upload the PDFs to the repo (or attach them in chat). Until then, all literature work uses web-verified sources only, and **no** close-reading claim (in particular GAP 2 / E5) may be finalised. |
| **U2** | GAP 2 / E5 discrepancy with A1 (27 vs 35) | Researcher or Phase 1: hand re-derivation of A1 Theorem 1. **Blocker for any claim about A1.** |
| **U3** | The Nebe–Rains–Sloane item (D3 in the bibliography) about self-dual codes over rings **via an anti-isomorphism** may be the closest conceptual precursor to our $\theta$-duality | **High priority:** locate and read before Phase 1 writes Section 2 |
| **U4** | No MathSciNet/zbMATH access in this sandbox ⇒ GAP 1/GAP 3 novelty tests are not fully executed | Researcher to run the two searches listed in §7, or approve proceeding with web-search-level verification |
| **U5** | Whether to use the $R$-valued or the $\mathbb F_q$-valued $\theta$-pairing as *the* definition of $C^{\perp_s}$ (they coincide in dimension but not as sets) | Phase 1 decision; my provisional answer: **both**, with the $R$-valued one for the algebraic theory and the $\mathbb F_q$-valued one for the quantum step, plus a lemma relating them |
| **U6** | Skew-cyclic route (A6) vs. $\theta$-duality route | Phase 1 must position our work relative to A6 (different mechanisms, but overlapping audience) |
| **U7** | Ring scope: is $t\ge2$ worth the extra difficulty, given A3/A7 already cover $M_2(\mathbb F_2[u]/\langle u^k\rangle)$ classically? | Researcher decision at the Phase-1 gate |

---

## 10. Phase control block (blueprint §8A)

**(i) Deliverables produced**
1. `01_LITERATURE/annotated_bibliography.md` — 17 verified entries + 4 unchecked.
2. `01_LITERATURE/references.bib` — BibTeX with per-entry verification notes.
3. `01_LITERATURE/comparison_matrix.md` — 13-row comparison matrix + reading.
4. `02_PHASE_REPORTS/Phase_0/Phase_0_Report.md` — this document.
5. `04_COMPUTATION/matrix_ring_lib.py`, `phase0_feasibility.py`,
   `phase0_results.txt` — exact-arithmetic feasibility experiments E1–E5.
6. `04_COMPUTATION/README.md` — reproducibility notes (environment, inputs,
   exhaustive vs. randomised completeness limits).
7. `03_THEOREMS/theorem_register.md` — claim register (T-001…T-014; all
   Phase-0 claims marked `conjectural` / `computational only`).
8. `PROJECT_DECISION_LOG.md`, `CHANGELOG.md`.
9. `06_AUDIT/Phase0_audit_request.md` — the copy-paste audit prompt for the
   independent ChatGPT audit (blueprint §8B).

**(ii) Theorem / proof status**
* **Nothing is proved in the manuscript sense in Phase 0.** Every mathematical
  statement in this report is tagged **[EST]** (cited/standard), **[PRP]**
  (proposed here with a proof sketch), **[CMP]** (computational, stated range)
  or **[OPN]**.
* The $\theta_s$-duality framework (§5.3) is **[PRP] + [CMP]**: verified
  exhaustively at $(m,q,t,n)=(2,2,1,1),(2,4,1,1),(2,2,2,1)$ (all one-sided
  ideals) and $(2,2,1,3)$ (all 35 cyclic codes), **not** proved in general.
  Full proofs are Phase-1/Phase-3 deliverables.

**(iii) Unresolved issues** — see §9 (U1–U7).

**(iv) Files created** — see the tree in `CHANGELOG.md`.

**(v) Risks**

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| **R1** | The $\theta$-duality does not generalise beyond the tested parameters | High | Phase 1 must prove it for general $m,t$, or falsify it by a targeted search at $(m,q,t,n)=(2,4,2,3)$ |
| **R2** | GAP 2 / U2 turns out to be a misreading of A1 | Medium | Already stated with caveats; no manuscript claim until settled |
| **R3** | No duality-preserving Gray map exists for $t\ge2$ | High | Fallback: additive/stabilizer route (C9) + EAQECC from the *image* hull computed directly; or restrict the quantum section to $t=1$ (Bachoc map, where A1's Prop. 2 gives a Hermitian precedent) |
| **R4** | Novelty evaporates under a proper MathSciNet search | Medium | GAP 1/3 tests in §7 must be run before Phase 4 |
| **R5** | Parameter tables not competitive with the commutative state of the art (C5/C6, 2026) | Medium | Novelty must be argued structurally (non-commutative duality/hull theory), not only by "better parameters" |
| **R6** | Scope creep (the blueprint's 10-section paper is very large) | Medium | Keep the phase gates; do not open Phases 2–8 early |

**(vi) GO / REVISE / STOP:** **REVISE** the framework per M1–M4, then
**GO to Phase 1**. Awaiting the researcher's decision and the independent
ChatGPT audit (blueprint §7 step 4).

---

*End of Phase 0 report. No further phase is started (blueprint §8D).*
