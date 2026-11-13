# Phase 8 / Tasks C and D — Final quantum-code table, reconciliation and comparison

All tuples are $[[N,K,d]]_q$ (stabilizer) or $[[N,K,d;c]]_q$
(entanglement-assisted, $c$ maximally entangled $q$-ary pairs). Length
$N=4tn$; $k=\dim_{\mathbb F_q}D$ for the Gray image $D=\varphi_n(C)$;
$h_E=\dim(D\cap D^{\perp_E})$; $c=k-h_E$; $K=N-k-h_E$. Every row below was
recomputed from those four quantities in Phase 8.

---

## 1. Reconciliation of the five tuples named in the Task-C brief

| tuple | origin | status after the exhaustive Phase-7 run | disposition |
|---|---|---|---|
| $[[16,4,3]]_4$ | Phase 5 §4 row 5; reproduced in Phase 6 and Phase 7 | **Reproduced, non-dominated.** Produced twice at $(4,1,4)$, $N=16$: by R2-SO with $k=6$ and by R2-DC with $k=10$; in both cases $h_E=k$, $c=0$, $K=16-2k$ resp. $2k-16$ $=4$. Exact by complete enumeration. | **kept** — it is the Phase-5 headline and the witness for T-203 |
| $[[12,2,6;10]]_4$ | Phase 6; family $(4,1,3)$, $N=12$ | **Reproduced, non-dominated.** $k=10$, $h_E=0$, $c=10$, $K=2$. Exact by complete enumeration of the difference set ($4^2$ codewords). $d/N=0.500$. | **kept** — largest $d/N$ among the exhaustively enumerated families |
| $[[16,4,5;8]]_4$ | Phase 6; family $(4,1,4)$, $N=16$ | **Reproduced, non-dominated.** $k=10$, $h_E=2$, $c=8$, $K=4$. Exact by complete enumeration ($4^6$). | **kept** |
| $[[24,4,5;12]]_4$ | Phase 6; family $(4,2,3)$, $N=24$, obtained on a **300-code sample** | **Not reproduced, and dominated.** Phase 7 enumerates $(4,2,3)$ **exhaustively** (35 937 codes) and the best entanglement-assisted distance there is $d=6$, attained by $[[24,4,6;20]]_4$ ($k=20$, $h_E=0$, $c=20$, $K=4$; exact by complete enumeration). Phase 6's $d=5$ was a sampled lower bound, not an optimum. The tuple is dominated by $[[20,4,6;12]]_4$ (from $(4,1,5)$). | **replaced by $[[24,4,6;20]]_4$** in the headline table; the original tuple and the reason for the change are reported in the manuscript (§8.5) and in `OPEN_ISSUES_AND_LIMITATIONS.md` |
| $[[24,10,4;2]]_9$ | Phase 7; family $(9,1,6)$, $N=24$ | **Reproduced, non-dominated.** $k=8$, $h_E=6$, $c=2$, $K=10$. The distance is a **proved lower bound** $d\ge4$ (support search to weight 4), not an exact value. $(9,1,6)$ is a *counted-only* family scanned as a seeded 2000-code sample of $1\,048\,576$ codes. | **kept, labelled $d\ge4$** — it is the O-6.1 frontier point, and its status as a bound is stated wherever it appears |

**Recalculation check (Phase 8, independent).** For each of the five:

* $[[16,4,3]]_4$: $N=4\cdot1\cdot4=16$; SO: $h_E=k=6$, $c=0$, $K=16-6-6=4$ ✓.
  DC: $h_E=k=10$, $c=0$, $K=2\cdot10-16=4$ ✓.
* $[[12,2,6;10]]_4$: $N=12$; $c=10$, $K=2$ $\Rightarrow$ $k+h_E=10$, $k-h_E=10$
  $\Rightarrow$ $k=10$, $h_E=0$ ✓.
* $[[16,4,5;8]]_4$: $N=16$; $k+h_E=12$, $k-h_E=8$ $\Rightarrow$ $k=10$, $h_E=2$ ✓.
* $[[24,4,6;20]]_4$: $N=24$; $k+h_E=20$, $k-h_E=20$ $\Rightarrow$ $k=20$, $h_E=0$ ✓.
* $[[24,10,4;2]]_9$: $N=24$; $k+h_E=14$, $k-h_E=2$ $\Rightarrow$ $k=8$, $h_E=6$ ✓.

Every row also satisfies the three proved identities of T-219 ($k$ even;
$K-c=N-2k\equiv0\pmod4$; $c+K=N-2h_E$) and the coset Singleton bound
$K+d\le N+1$ of T-232.

---

## 2. Principal / non-principal hulls

| code | $\mu_B(\mathrm{Hull}_s)$ of the underlying hull | note |
|---|---|---|
| every code of §3 below except the last two | $\le 2$ (principal) | in the non-wild regime $\mu_B\le2$ is **proved** (T-222/T-223: $B_j$ is a chain ring when $t=1$ or $e_j=1$) |
| $[[24,6,2;2]]_9$ from $(9,2,3)$ | **3** — non-principal | O-3.1 witness family; $\mathrm{Hull}_s(W)=W$, $\dim W=5$, $s=0,1$ |
| $[[32,8,2;4]]_4$ from $(4,2,4)$ | **3** — non-principal | $\mathrm{Hull}_s(W)\supsetneq W$, $\dim W=7$, $s=0,1$ |
| $(8,2,2)$ | $2$ — **no** witness found | recorded explicitly; this is the negative half of the answer to O-6.4 |

No principality hypothesis is used anywhere in the chain
(T-179, T-192 and T-197 are all hypothesis-free in this respect), which is
exactly why the non-principal witnesses yield valid quantum codes.

---

## 3. The certified codes (all 28, from Phase 7 Part 6)

`M1` complete enumeration of the classical difference set; `M2` increasing-weight
support search; `M3` exhaustive ambient quantum search (a lower bound — written
`>w` — where not complete). `exact = yes` means M1 or M2 decided the true
minimum. `S-def` $=N-K+c-2(d-1)$, the EA Singleton defect.

| $(q,t,n)$ | $N$ | route | $k$ | $K$ | $d$ | $c$ | $h_E$ | M1 | M2 | M3 | exact | $\mathbb F_p$-abelian | S-def |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $(9,1,6)$ | 24 | SO | 8 | 8 | 4 | 0 | 8 | — | 4 | $>2$ | yes | True | 10 |
| $(4,1,5)$ | 20 | SO | 8 | 4 | 4 | 0 | 8 | — | 4 | $>2$ | yes | True | 10 |
| $(4,1,5)$ | 20 | DC | 12 | 4 | 4 | 0 | 12 | — | 4 | $>2$ | yes | True | 10 |
| $(4,1,5)$ | 20 | EA | 18 | 2 | 10 | 18 | 0 | 10 | n/a | $>2$ | yes | True | 18 |
| $(9,1,6)$ | 24 | EA | 20 | 2 | 10 | 18 | 2 | 10 | n/a | $>2$ | yes | True | 22 |
| $(4,1,1)$ | 4 | EA | 2 | 2 | 2 | 2 | 0 | 2 | n/a | 2 | yes | True | 2 |
| $(4,1,2)$ | 8 | EA | 4 | 4 | 3 | 4 | 0 | 3 | n/a | 3 | yes | True | 4 |
| $(4,1,3)$ | 12 | EA | 10 | 2 | 6 | 10 | 0 | 6 | n/a | $>2$ | yes | True | 10 |
| $(4,1,4)$ | 16 | EA | 10 | 4 | 5 | 8 | 2 | 5 | n/a | $>2$ | yes | True | 12 |
| $(4,1,6)$ | 24 | EA | 20 | 4 | 9 | 20 | 0 | 9 | n/a | $>2$ | yes | True | 24 |
| $(4,2,1)$ | 8 | EA | 4 | 4 | 2 | 4 | 0 | 2 | n/a | 2 | yes | True | 6 |
| $(4,2,2)$ | 16 | EA | 12 | 4 | 4 | 12 | 0 | 4 | n/a | $>2$ | yes | True | 18 |
| $(4,2,3)$ | 24 | EA | 20 | 4 | 6 | 20 | 0 | 6 | n/a | $>2$ | yes | True | 30 |
| $(4,3,1)$ | 12 | EA | 6 | 6 | 2 | 6 | 0 | 2 | n/a | 2 | yes | True | 10 |
| $(4,4,1)$ | 16 | EA | 10 | 6 | 2 | 10 | 0 | 2 | n/a | 2 | yes | True | 18 |
| $(8,1,1)$ | 4 | EA | 2 | 2 | 2 | 2 | 0 | 2 | n/a | 2 | yes | True | 2 |
| $(8,1,2)$ | 8 | EA | 4 | 4 | 3 | 4 | 0 | 3 | n/a | 3 | yes | True | 4 |
| $(8,1,3)$ | 12 | EA | 10 | 2 | 6 | 10 | 0 | 6 | n/a | $>2$ | yes | True | 10 |
| $(8,3,1)$ | 12 | EA | 8 | 4 | 2 | 8 | 0 | 2 | n/a | 2 | yes | True | 14 |
| $(9,1,1)$ | 4 | EA | 2 | 2 | 2 | 2 | 0 | 2 | n/a | 2 | yes | True | 2 |
| $(9,1,2)$ | 8 | EA | 6 | 2 | 4 | 6 | 0 | 4 | n/a | $>3$ | yes | True | 6 |
| $(9,1,3)$ | 12 | EA | 8 | 2 | 5 | 6 | 2 | 5 | n/a | $>2$ | yes | True | 8 |
| $(9,1,4)$ | 16 | EA | 14 | 2 | 8 | 14 | 0 | 8 | n/a | $>2$ | yes | True | 14 |
| $(9,1,5)$ | 20 | EA | 16 | 4 | 9 | 16 | 0 | 9 | n/a | $>2$ | yes | True | 16 |
| $(9,2,1)$ | 8 | EA | 4 | 4 | 2 | 4 | 0 | 2 | n/a | 2 | yes | True | 6 |
| $(9,2,2)$ | 16 | EA | 12 | 4 | 4 | 12 | 0 | 4 | n/a | $>2$ | yes | True | 18 |
| $(9,3,1)$ | 12 | EA | 8 | 4 | 2 | 8 | 0 | 2 | n/a | 2 | yes | True | 14 |
| $(9,3,2)$ | 24 | EA | 18 | 6 | 4 | 18 | 0 | — | 4 | $>2$ | yes | True | 30 |

Plus the O-6.1 frontier point, which is **not** in this table because its
distance is a proved bound rather than an exact value:
$[[24,10,4;2]]_9$ from $(9,1,6)$, $k=8$, $h_E=6$, $K=10$, $c=2$, $d\ge4$
(support search to weight 4), S-defect $24-10+2-2\cdot3=10$.

---

## 4. Comparison with `codetables.de` (retrieved 2026-11-04)

Only **stabilizer** codes ($c=0$) can be compared: `QECC-EA.php` returns HTTP
404, so **no entanglement-assisted table exists** and every EA code above is
unbenchmarked. Only $q=4$ and $q=9$ are tabulated; $q=8$ is not
(“currently not available for q=8”), so the $(8,\cdot,\cdot)$ codes are
unbenchmarked as well.

| code | family | route | best known $[[N,K]]_q$ (lower .. upper) | gap |
|---|---|---|---|---|
| $[[8,4,2]]_4$ | $(4,1,2)$ | DC/SO | 2 .. 2 | **meets** |
| $[[12,8,2]]_4$ | $(4,1,3)$ | DC/SO | 2 .. 2 | **meets** |
| $[[16,12,2]]_4$ | $(4,1,4)$ | DC/SO | 2 .. 2 | **meets** |
| $[[20,16,2]]_4$ | $(4,1,5)$ | DC/SO | 2 .. 2 | **meets** |
| $[[24,20,2]]_4$ | $(4,1,6)$ | DC | 2 .. 2 | **meets** |
| $[[12,4,2]]_4$ | $(4,1,3)$ | DC | 4 .. 4 | 2 below |
| $[[16,4,3]]_4$ | $(4,1,4)$ | SO/DC | 5 .. 5 | 2 below |
| $[[20,12,2]]_4$ | $(4,1,5)$ | DC/SO | 3 .. 3 | 1 below |
| $[[20,4,4]]_4$ | $(4,1,5)$ | SO/DC | 6 .. 6 | 2 below |
| $[[24,16,2]]_4$ | $(4,1,6)$ | DC | 3 .. 3 | 1 below |
| $[[8,4,2]]_9$ | $(9,1,2)$ | — | 3 .. 3 | 1 below |
| $[[16,8,3]]_9$ | $(9,1,4)$ | DC | 4 .. 4 | 1 below |
| $[[24,8,4]]_9$ | $(9,1,6)$ | SO | 6 .. 8 | 2 below (best known lower bound 6) |
| $[[24,12,3]]_9$ | $(9,1,6)$ | DC | 5 .. 6 | 2 below (best known lower bound 5) |

**No record is claimed.** Every stabilizer code found here is at best equal to
the best known distance (and then only with $d=2$, where equality is
uninformative), and every code with $d\ge3$ is 1–2 below. The novelty claim of
the manuscript concerns the **origin** of the codes (§9.3 of the manuscript and
`NOVELTY_COMPARISON.md`), not their parameters.

---

## 5. The examples selected for the manuscript, and why

Selection is **not** by the size of the parameter tuple. Each entry is included
because it settles a mathematical point.

| # | code | why it is in the paper |
|---|---|---|
| 1 | $[[24,8,4]]_9$ (SO, $(9,1,6)$) | the **first stabilizer distance 4** in this framework; it shows that the Phase-6 ceiling $d\le3$ for stabilizer routes was an artefact of the scanned range ($N\le16$), not a property of the construction. $c=0$: no entanglement is consumed. |
| 2 | $[[20,4,4]]_4$ (SO **and** DC, $(4,1,5)$) | the **shortest** stabilizer distance 4 ($N=20$), and it comes from the family $(4,1,5)$ — i.e. from $n=5$ at $t=1$, which was **unreachable before the CRT extension** of Phase 7. It is therefore a direct, checkable fruit of the algebraic contribution, not of a longer search. Both the SO and the DC branch produce it ($k=8$ and $k=12$), which is a non-trivial consistency check of T-196. |
| 3 | $[[16,4,3]]_4$ (SO/DC, $(4,1,4)$) | the code on which the $\mathbb F_p$-basis subtlety (T-203) was found: the weight-1 operator $(0\mid e_0)$ commutes with all 12 $\mathbb F_q$-generators because $\mathrm{Tr}_{\mathbb F_4/\mathbb F_2}(1)=0$, yet not with all 24 elements of an $\mathbb F_p$-basis. The naive test reports $d=1$. |
| 4 | $[[12,2,6;10]]_4$ (EA, $(4,1,3)$) | the extreme point of the entanglement trade-off: $h_E=0$, i.e. the image code is **LCD**, which no stabilizer route can use at all; the EA route converts it into a code with $d/N=0.5$. It is also the cheapest distance-6 code: complete enumeration over only $4^2$ codewords. |
| 5 | $[[20,2,10;18]]_4$ (EA, $(4,1,5)$) | the largest distance found ($d=10$) at the shortest length that carries it; again from the newly opened $(4,1,5)$. Together with #2 it shows that one new family improves the stabilizer **and** the EA frontier simultaneously. |
| 6 | $[[24,4,6;20]]_4$ (EA, $(4,2,3)$) | the reconciliation of the Task-C tuple $[[24,4,5;12]]_4$: it is what the exhaustive enumeration of a family Phase 6 could only sample actually yields. Reported with the reason for the change. |
| 7 | $[[24,10,4;2]]_9$ (EA, $(9,1,6)$) | the **O-6.1 frontier point**: $d\ge4$ with only $c=2$ ebits and $K=10$ logical qudits. It is the concrete answer to “is there a family with $d\ge4$, bounded $c$ and $K\ge2$?”, and T-233 explains why $K$ cannot be pushed much further at that entanglement. |
| 8 | $[[24,6,2;2]]_9$ ($(9,2,3)$) and $[[32,8,2;4]]_4$ ($(4,2,4)$) | the **non-principal-hull** witnesses ($\mu_B(\mathrm{Hull}_s)=3$). Their significance is structural, not parametric ($d=2$): they prove that the O-3.1 phenomenon survives the whole chain into valid quantum parameters, which is the point of having removed every principality hypothesis. |
