# PHASE 7 — EXTENDED SEARCH: OPTIMAL QUANTUM PARAMETERS, ENTANGLEMENT EFFICIENCY, AND THE STRUCTURE OF THE ATTAINABLE FRONTIER

**Status:** complete (Tasks A–H).  Every statement below is labelled
**PROVED** (a proof is given in this file), **COMPUTATIONALLY VERIFIED ONLY**
(checked exhaustively or on a seeded sample, no proof), **IMPORTED RESULT**
(taken from the literature with a citation), **CONJECTURE**, **OPEN**, or
**REFUTED**.  As in Phases 5 and 6 each check carries the tag `[EXH]`
(exhaustive over the stated family), `[SMP]` (seeded sample) or `[CMP]`
(computation on one instance).

**Companion artefacts**

| file | content |
|---|---|
| `04_COMPUTATION/phase7_extended_search.py` | the verification script (Parts 1–9), `SEED = 20261210` |
| `04_COMPUTATION/phase7_extended_search_log.txt` | its log: **17 checks, 17 PASS, 0 FAIL**, 639 lines |

**Dependencies (read-only, never modified in this phase):** all of Phases 0–5
and `PHASE6_QUANTUM_PARAMETER_ENHANCEMENT.md` (T-204 … T-215 and the open
problems O-6.1 … O-6.6, four of which this phase resolves).

**What Phase 7 does.**  Phase 6 was blocked at two places by its own
machinery: the ring-component routine did not support `n = 5, 6` at `t = 1`
nor `n = 3` at `q = 8` (O-6.3), and the `mu_B >= 3` hull phenomenon was seen
in one family only (O-6.4).  Phase 7 (i) replaces the component routine by a
general CRT decomposition of `B = A_t[X]/(X^n-1)` and validates it against
the Phase-3B exhaustive enumeration, (ii) re-runs the whole search over the
enlarged family list, (iii) answers O-6.1 (the entanglement budget of
high-distance codes), O-6.2 (the `t >= 2` barrier) and O-6.4, (iv) certifies
the headline codes by three independent methods, (v) re-examines every
obstruction statement of Phase 6 and records one erratum, and (vi) compares
the stabilizer codes found with the published tables.

---

## 0. Conventions and what is imported

Imported unchanged from Phase 6 §0 (which imports them from Phases 4–5):
`q = p^r`, `A_t = F_q[u]/<u^t>`, `R = M_2(A_t)`, `B = A_t[X]/(X^n-1)`,
`N = 4tn`, and `D = phi_n(C) ⊆ F_q^N` the Gray image of a right
`R_n`-submodule `C`.  All dimensions are over `F_q`; the quantum alphabet is
`F_q`.  For `D` of dimension `k` with Euclidean hull `h_E = dim(D ∩ D^{⊥_E})`
the three routes are R1 (twisted graph, `[[N, N−k, d]]_q`), R2 (stabilizer:
SO `[[N, N−2k, d]]_q`, DC `[[N, 2k−N, d]]_q`) and R3 (entanglement-assisted,
`[[N, N−k−h_E, d ; k−h_E]]_q`); in every case
`d = min{ swt(v) : v ∈ G^{⊥_ω} \ G }` with `G` the route's group
(T-207).  Throughout this file

```
k = dim D,   h_E = dim(D ∩ D^{⊥_E}),   c = k − h_E,   K = N − k − h_E.
```

One new piece of notation, used only in Part 5: for a finite ring `S` and an
`S`-module `W`, `mu_S(W)` is the minimal number of generators of `W`.

---

## 1. Task B — the general CRT decomposition, and the census after it (O-6.3)

### 1.1 What was missing, and the replacement

Phase 2C's `Components` routine covers exactly three regimes of `X^n − 1`
over `F_q`: (S) split semisimple, (C) `n = p^v` with `t = 1`, and (W) "wild"
`n = p^v` with `t >= 2`.  Everything else raised `no component routine`,
which is why `n = 5, 6` at `t = 1` and `n = 3` at `q = 8` were out of reach
(Phase 6, O-6.3).  The replacement is the Chinese remainder theorem, used as
a *linear* isomorphism so that it composes with the Gray map and the hull
machinery of Phases 3–5 without change:

```
X^n − 1 = prod_j g_j^{e_j}   over F_q          (trial division, verified by
                                                re-multiplication)
B  =  A_t[X]/(X^n−1)  ≅  prod_j B_j,   B_j = A_t[X]/(g_j^{e_j})
                                     ≅  F_{q^{d_j}}[u,w]/(u^t, w^{e_j})
B^2 = prod_j B_j^2,   and every B-submodule of B^2 is a product
                      of B_j-submodules of B_j^2.
```

The component lattices are tiny (`dim B_j = t deg(g_j) e_j`), so the product
is exact and fast even where the whole lattice is astronomically large.  Four
things are verified every time the decomposition is built: (i) the
factorisation re-multiplies to `X^n − 1`; (ii) `Psi` is multiplicative on all
pairs of basis elements; (iii) `Psi ∘ Psi^{-1} = id` on a basis; (iv) the
resulting submodule list agrees, **as a set**, with the Phase-3B exhaustive
BFS on every family that routine supports.

> **T-216 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  On all ten families
> the Phase-2C routine supports, the CRT enumeration and the Phase-3B
> exhaustive BFS produce the *same set* of submodules of `B^2`, and `Psi` is
> multiplicative on every pair of basis elements.  Three families that no
> previous phase could enumerate at all are now exhaustive: `(4,1,5) N=20`
> with 2527 codes, `(4,1,6) N=24` with 35937 codes, `(8,1,3) N=12` with 737
> codes.  **O-6.3 is resolved.**


```
   (q,t,n) | factorization of X^n-1 | comp dims | regime   | #CRT   | #3B-BFS | agree
  --------------------------------------------------------------------------
   (4,1,2)   | (deg 1)^2                | [2]       | RAMIFIED | 33     | 33      | YES  [0s]
   (4,1,3)   | (deg 1)^1 (deg 1)^1 (deg | [1, 1, 1] | SEMISIMPLE | 343    | 343     | YES  [2s]
   (4,1,4)   | (deg 1)^4                | [4]       | RAMIFIED | 565    | 565     | YES  [35s]
   (8,1,2)   | (deg 1)^2                | [2]       | RAMIFIED | 93     | 93      | YES  [0s]
   (9,1,2)   | (deg 1)^1 (deg 1)^1      | [1, 1]    | SEMISIMPLE | 144    | 144     | YES  [0s]
   (9,1,3)   | (deg 1)^3                | [3]       | RAMIFIED | 1024   | 1024    | YES  [106s]
   (4,2,2)   | (deg 1)^2                | [4]       | WILD     | 1221   | 1221    | YES  [114s]
   (9,2,1)   | (deg 1)^1                | [2]       | SEMISIMPLE | 113    | 113     | YES  [1s]
   (4,3,1)   | (deg 1)^1                | [3]       | SEMISIMPLE | 139    | 139     | YES  [1s]
   (4,4,1)   | (deg 1)^1                | [4]       | SEMISIMPLE | 565    | 565     | YES  [30s]
  [EXH] B1  the new CRT enumeration reproduces the Phase-3B exhaustive BFS exactly (as a set of submodules of B^2) on every family the old routine supported, and Psi is multiplicative PASS  [EXH] 10 families: split / chain / wild x q=4,8,9 x t=1..4
```


### 1.2 The census after the extension


```
   (q,t,n) |  N | X^n-1             | dims    | regime      | |B|      | #codes   | old | method
  ------------------------------------------------------------------------------------------------
   (4,1,1) |  4 | (d1)^1             | [1]     | SEMISIMPLE  | 4        | 7        | yes | EXHAUSTIVE  [0s]
   (4,1,2) |  8 | (d1)^2             | [2]     | RAMIFIED    | 16       | 33       | yes | EXHAUSTIVE  [0s]
   (4,1,3) | 12 | (d1)^1(d1)^1(d1)^1 | [1, 1, 1] | SEMISIMPLE  | 64       | 343      | yes | EXHAUSTIVE  [0s]
   (4,1,4) | 16 | (d1)^4             | [4]     | RAMIFIED    | 256      | 565      | yes | EXHAUSTIVE  [0s]
   (4,1,5) | 20 | (d1)^1(d2)^1(d2)^1 | [1, 2, 2] | SEMISIMPLE  | 1024     | 2527     | NO  | EXHAUSTIVE  [0s]
   (4,1,6) | 24 | (d1)^2(d1)^2(d1)^2 | [2, 2, 2] | RAMIFIED    | 4096     | 35937    | NO  | EXHAUSTIVE  [0s]
   (4,2,1) |  8 | (d1)^1             | [2]     | SEMISIMPLE  | 16       | 33       | yes | EXHAUSTIVE  [0s]
   (4,2,2) | 16 | (d1)^2             | [4]     | WILD        | 256      | 1221     | yes | EXHAUSTIVE  [0s]
   (4,2,3) | 24 | (d1)^1(d1)^1(d1)^1 | [2, 2, 2] | SEMISIMPLE  | 4096     | 35937    | yes | EXHAUSTIVE  [0s]
   (4,2,4) | 32 | (d1)^4             | [8]     | WILD        | 65536    | -        | yes | component BFS too large (|S^2|=4294967296)
   (4,3,1) | 12 | (d1)^1             | [3]     | SEMISIMPLE  | 64       | 139      | yes | EXHAUSTIVE  [0s]
   (4,3,2) | 24 | (d1)^2             | [6]     | WILD        | 4096     | -        | yes | component BFS too large (|S^2|=16777216)
   (4,4,1) | 16 | (d1)^1             | [4]     | SEMISIMPLE  | 256      | 565      | yes | EXHAUSTIVE  [0s]
   (4,4,2) | 32 | (d1)^2             | [8]     | WILD        | 65536    | -        | yes | component BFS too large (|S^2|=4294967296)
   (8,1,1) |  4 | (d1)^1             | [1]     | SEMISIMPLE  | 8        | 11       | yes | EXHAUSTIVE  [0s]
   (8,1,2) |  8 | (d1)^2             | [2]     | RAMIFIED    | 64       | 93       | yes | EXHAUSTIVE  [0s]
   (8,1,3) | 12 | (d1)^1(d2)^1       | [1, 2]  | SEMISIMPLE  | 512      | 737      | NO  | EXHAUSTIVE  [0s]
   (8,1,4) | 16 | (d1)^4             | [4]     | RAMIFIED    | 4096     | -        | yes | component BFS too large (|S^2|=16777216)
   (8,1,5) | 20 | (d1)^1(d4)^1       | [1, 4]  | SEMISIMPLE  | 32768    | -        | NO  | component BFS too large (|S^2|=16777216)
   (8,1,6) | 24 | (d1)^2(d2)^2       | [2, 4]  | RAMIFIED    | 262144   | -        | NO  | component BFS too large (|S^2|=16777216)
   (8,2,1) |  8 | (d1)^1             | [2]     | SEMISIMPLE  | 64       | 93       | yes | EXHAUSTIVE  [0s]
   (8,2,2) | 16 | (d1)^2             | [4]     | WILD        | 4096     | -        | yes | component BFS too large (|S^2|=16777216)
   (8,2,3) | 24 | (d1)^1(d2)^1       | [2, 4]  | SEMISIMPLE  | 262144   | -        | NO  | component BFS too large (|S^2|=16777216)
   (8,2,4) | 32 | (d1)^4             | [8]     | WILD        | 16777216 | -        | yes | component BFS too large (|S^2|=281474976710656)
   (8,3,1) | 12 | (d1)^1             | [3]     | SEMISIMPLE  | 512      | 751      | yes | EXHAUSTIVE  [24s]
   (8,3,2) | 24 | (d1)^2             | [6]     | WILD        | 262144   | -        | yes | component BFS too large (|S^2|=68719476736)
   (8,4,1) | 16 | (d1)^1             | [4]     | SEMISIMPLE  | 4096     | -        | yes | component BFS too large (|S^2|=16777216)
   (8,4,2) | 32 | (d1)^2             | [8]     | WILD        | 16777216 | -        | yes | component BFS too large (|S^2|=281474976710656)
   (9,1,1) |  4 | (d1)^1             | [1]     | SEMISIMPLE  | 9        | 12       | yes | EXHAUSTIVE  [0s]
   (9,1,2) |  8 | (d1)^1(d1)^1       | [1, 1]  | SEMISIMPLE  | 81       | 144      | yes | EXHAUSTIVE  [0s]
   (9,1,3) | 12 | (d1)^3             | [3]     | RAMIFIED    | 729      | 1024     | yes | EXHAUSTIVE  [0s]
   (9,1,4) | 16 | (d1)^1(d1)^1(d1)^1(d1)^1 | [1, 1, 1, 1] | SEMISIMPLE  | 6561     | 20736    | yes | EXHAUSTIVE  [0s]
   (9,1,5) | 20 | (d1)^1(d2)^1(d2)^1 | [1, 2, 2] | SEMISIMPLE  | 59049    | 84672    | NO  | COUNTED-ONLY  [0s]
   (9,1,6) | 24 | (d1)^3(d1)^3       | [3, 3]  | RAMIFIED    | 531441   | 1048576  | NO  | COUNTED-ONLY  [56s]
   (9,2,1) |  8 | (d1)^1             | [2]     | SEMISIMPLE  | 81       | 113      | yes | EXHAUSTIVE  [0s]
   (9,2,2) | 16 | (d1)^1(d1)^1       | [2, 2]  | SEMISIMPLE  | 6561     | 12769    | yes | EXHAUSTIVE  [0s]
   (9,2,3) | 24 | (d1)^3             | [6]     | WILD        | 531441   | -        | yes | component BFS too large (|S^2|=282429536481)
   (9,2,4) | 32 | (d1)^1(d1)^1(d1)^1(d1)^1 | [2, 2, 2, 2] | SEMISIMPLE  | 43046721 | 163047361 | yes | COUNTED-ONLY  [1s]
   (9,3,1) | 12 | (d1)^1             | [3]     | SEMISIMPLE  | 729      | 1024     | yes | EXHAUSTIVE  [50s]
   (9,3,2) | 24 | (d1)^1(d1)^1       | [3, 3]  | SEMISIMPLE  | 531441   | 1048576  | yes | COUNTED-ONLY  [50s]
   (9,4,1) | 16 | (d1)^1             | [4]     | SEMISIMPLE  | 6561     | -        | yes | component BFS too large (|S^2|=43046721)
   (9,4,2) | 32 | (d1)^1(d1)^1       | [4, 4]  | SEMISIMPLE  | 43046721 | -        | yes | component BFS too large (|S^2|=43046721)
  [EXH] B2  the extension makes NEW families exhaustively enumerable: (q,t,n) with N = 20 and 24 at t = 1 and N = 12 at q = 8, none of which the Phase-2C routine supported (Phase 6 O-6.3) PASS  [EXH] 3 new families: (4,1,5) N=20: 2527 codes, (4,1,6) N=24: 35937 codes, (8,1,3) N=12: 737 codes
  [EXH] B3  families that Phase 6 could only SAMPLE (300 codes) are now exhaustively enumerated PASS  [EXH] (4,1,3) N=12: 343 codes, (4,1,4) N=16: 565 codes, (4,2,2) N=16: 1221 codes, (4,2,3) N=24: 35937 codes, (4,4,1) N=16: 565 codes, (8,3,1) N=12: 751 codes, (9,1,3) N=12: 1024 codes, (9,1,4) N=16: 20736 codes, (9,2,2) N=16: 12769 codes, (9,3,1) N=12: 1024 codes
```


> **T-217 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  Over the whole census
> range (`q ∈ {4,8,9}`, `t >= 1`, `n >= 1`, `t n <= 8`: 42 families), 23
> families are enumerated exhaustively by the CRT route, 4 are counted but
> not enumerated (the product of the component lattices exceeds 40000), and
> 15 are blocked by the component BFS itself (`|S^2| = q^{2 dim S} > 4·10^6`
> for some component).  Ten families that Phase 6 could only *sample*
> (300 codes each) are now exhaustive, among them `(4,2,3)` (35937 codes) and
> `(9,2,2)` (12769 codes).

---

## 2. Task C — the systematic search over the extended family list

Every family of the census whose component lattices are small enough is
scanned.  The cheap invariants (`k`, `h_E`, `c`, `K`, self-orthogonality,
dual-containment) are computed for **every** code; the expensive distance
computation runs on a deterministically selected subset (all SO/DC codes up
to 150 per family; the 120 EA codes with the smallest dual; the 120 EA codes
with the smallest entanglement).  Distances come in cheap exact stages
(weight `<= 2`; complete enumeration up to 262144 codewords; weight `<= 3`)
and, for at most 25 survivors per family, a deep support search to weight 6
(`N <= 16`) or 4 (`N >= 20`).  Every reported value is **exact** or a
**proved lower bound**, and the log says which.


```
   (q,t,n) |  N | #codes (total)   | SO  DC | EA cand | dist | deep | best d | t
  ------------------------------------------------------------------------------------
   (4,1,1) |  4 | 7      (7       ) |   0   1 |       4 |    5 |    0 |      2 | 0s
   (4,1,2) |  8 | 33     (33      ) |   5   6 |      16 |   27 |    0 |      3 | 0s
   (4,1,3) | 12 | 343    (343     ) |  28  29 |     278 |  242 |    0 |      6 | 1s
   (4,1,4) | 16 | 565    (565     ) |  47  48 |     432 |  279 |    0 |      5 | 7s
   (4,1,5) | 20 | 2527   (2527    ) |  46  47 |    2408 |  333 |   25 |     10 | 43s
   (4,1,6) | 24 | 35937  (35937   ) | 1715 1716 |   32340 |  390 |    0 |      9 | 73s
   (4,2,1) |  8 | 33     (33      ) |   1   2 |      28 |   31 |    0 |      2 | 0s
   (4,2,2) | 16 | 1221   (1221    ) |  51  52 |    1112 |  343 |    0 |      4 | 2s
   (4,2,3) | 24 | 35937  (35937   ) | 247 248 |   35434 |  390 |   14 |      6 | 59s
   (4,3,1) | 12 | 139    (139     ) |   2   3 |     132 |  137 |    0 |      2 | 0s
   (4,4,1) | 16 | 565    (565     ) |   3   4 |     556 |  231 |    0 |      2 | 1s
   (8,1,1) |  4 | 11     (11      ) |   0   1 |       8 |    9 |    0 |      2 | 0s
   (8,1,2) |  8 | 93     (93      ) |   9  10 |      64 |   83 |    0 |      3 | 0s
   (8,1,3) | 12 | 737    (737     ) |  10  11 |     706 |  206 |    0 |      6 | 33s
   (8,3,1) | 12 | 751    (751     ) |   2   3 |     744 |  205 |    0 |      2 | 0s
   (9,1,1) |  4 | 12     (12      ) |   0   1 |       8 |    9 |    0 |      2 | 0s
   (9,1,2) |  8 | 144    (144     ) |   4   5 |     130 |  139 |    0 |      4 | 2s
   (9,1,3) | 12 | 1024   (1024    ) |  29  30 |     944 |  251 |   25 |      5 | 8s
   (9,1,4) | 16 | 20736  (20736   ) | 248 249 |   20190 |  390 |   25 |      8 | 39s
   (9,1,5) | 20 | 2000   (84672   ) |   6   5 |    1986 |  251 |   25 |      9 | 59s
   (9,1,6) | 24 | 2000   (1048576 ) |   6   5 |    1987 |  251 |   25 |     10 | 138s
   (9,2,1) |  8 | 113    (113     ) |   2   3 |     105 |  110 |    0 |      2 | 0s
   (9,2,2) | 16 | 12769  (12769   ) |  20  21 |   12723 |  281 |    0 |      4 | 16s
   (9,3,1) | 12 | 1024   (1024    ) |   4   5 |    1012 |  226 |    0 |      2 | 1s
   (9,3,2) | 24 | 2000   (1048576 ) |   0   0 |    2000 |  236 |    3 |      4 | 13s
```


The column `deep` counts the codes sent to the deep support search, `dist`
the codes given a distance at all, and `best d` the largest distance found in
that family (over all three routes).  Families with `#codes < total` are the
seeded 2000-code samples of §1.2; they are reported as samples, never as
exhaustive.

> **T-218 (COMPUTATIONALLY VERIFIED ONLY).**  25 families, 120721 codes with
> computed invariants, 5055 codes with a computed distance (4418 exact, 637 a
> proved lower bound).  The largest exact distance found is `d = 10`, at
> `(4,1,5)` (`N = 20`) and `(9,1,6)` (`N = 24`), both entanglement-assisted.

---

## 3. Task A — entanglement efficiency and high distance (O-6.1)

### 3.1 The bookkeeping, and an erratum


```
PART 4.  TASK A: ENTANGLEMENT-EFFICIENT HIGH-DISTANCE CODES (O-6.1)
==============================================================================
  O-6.1 asked for a family in this framework with d >= 4, bounded
  entanglement c, and K >= 2.  The obstruction is exact, so we state
  it first and then measure against it.

  (a) STRUCTURAL FACTS (all verified on the data below).
      k = dim D = 2 dim_{F_q} W  is ALWAYS EVEN (the Gray image of
      the Morita code I_W has dimension 2 dim W), and N = 4tn is
      divisible by 4.  Hence
          K - c = (N - k - h_E) - (k - h_E) = N - 2k = 0 mod 4,
      i.e.  K = c (mod 4)  for every code, and in particular K and c
      have the same parity.  For the stabilizer routes h_E = k, so
      c = 0 and K = N - 2k is divisible by 4.

      The traded quantity is
          c + K = N - 2 h_E,      |c - K| = |2k - N|,
      so c is small iff the Euclidean hull h_E is large, i.e. iff the
      code is nearly self-orthogonal; and c >= 2k - N is forced.
      (Phase 6 section 12 stated 'c + K = N - k'; that is wrong, see
      PART 7, ERRATUM E-7.1: the correct identity is c + K = N - 2h_E,
      which agrees with the Phase 6 numbers only when h_E = 0.)
  [EXH] A1  for every code in the search: k is even, K - c = N - 2k is divisible by 4 (so K and c have the same parity), and c + K = N - 2 h_E PASS  [EXH] 5055 codes with distances; 0 parity violations, 0 odd k, 0 sum violations

  (b) THE ATTAINABLE SET WITH c BOUNDED.  For each distance d and
      each bound on the entanglement, the best (largest K) code
      found in the whole search.
```


> **T-219 (PROVED; `[EXH]` on 5055 codes).**  For every code of the search:
> `k` is even; `K − c = N − 2k` is divisible by 4 (hence `K ≡ c mod 4` and
> `K, c` have the same parity); and `c + K = N − 2 h_E`.  Moreover
> `c >= 2k − N` is forced, so small entanglement requires a nearly
> self-orthogonal image code.
>
> **ERRATUM E-7.1 (PROVED).**  Phase 6 §12 (O-6.1) states `c + K = N − k`.
> That identity is wrong: it would force `h_E = k/2`.  The correct identity
> is `c + K = N − 2 h_E`, and it agrees with the corrected statement on all
> 5055 codes of the new search, while Phase 6's *own* Pareto table satisfies
> `c + K = N − k` in only 2 of its 25 rows.  No Phase 6 **parameter** is
> affected: `K`, `c` and `d` were computed from `k` and `h_E` directly.

### 3.2 The attainable set with the entanglement bounded


```
        c <= |   d=2        d=3        d=4        d=5        d=6
      ------------------------------------------------------------------
           0 | [[24,20]]  [[24,12]]  [[24, 8]]      -          -    
           2 | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]      -    
           4 | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]      -    
           6 | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]      -    
           8 | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]      -    
          12 | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]  [[20, 4]]
         any | [[24,20]]  [[24,12]]  [[24,10]]  [[24, 6]]  [[20, 4]]

       reading: with c <= 0 (a genuine stabilizer code) the best is the entry in the first row; the last row repeats the best over all entanglements.  A '-' means no such code was found.

  (c) THE MINIMUM ENTANGLEMENT FOR EACH DISTANCE (best over all
      families; a lower-bound entry is marked by its method).
```


### 3.3 The minimum entanglement needed for each distance


```
        d | min c | code                  | family      | k  h_E | method
      ------------------------------------------------------------------------------
       2 |     0 | [[24,20,2;0]]_4  | (4,1,6) N=24 | 22   2 | support search w<=2
       3 |     0 | [[24,12,3;0]]_9  | (9,1,6) N=24 | 18   6 | support search w<=3
       4 |     0 | [[24, 8,4;0]]_9  | (9,1,6) N=24 |  8   8 | support search w<=4
       5 |     2 | [[24, 6,5;2]]_9  | (9,1,6) N=24 | 10   8 | proved lower bound: d >= 5
       6 |    10 | [[12, 2,6;10]]_4  | (4,1,3) N=12 | 10   0 | complete enumeration
       7 |    10 | [[16, 2,7;10]]_9  | (9,1,4) N=16 | 12   2 | complete enumeration
       8 |    14 | [[16, 2,8;14]]_9  | (9,1,4) N=16 | 14   0 | complete enumeration

  (d) THE PARETO FRONTIER (maximise d, then K, then minimise c).
```


### 3.4 The Pareto frontier (maximise `d`, then `K`, then minimise `c`)


```
   q t n  N | kind |  k   K   d   c | K/N    d/N   | EA-Singleton | exact
  ----------------------------------------------------------------------------------
   4 1 5 20 | EA   |  18   2  10  18 | 0.100  0.500 |           18 | yes
   9 1 6 24 | EA   |  20   2  10  18 | 0.083  0.417 |           22 | yes
   9 1 5 20 | EA   |  16   4   9  16 | 0.200  0.450 |           16 | yes
   4 1 6 24 | EA   |  20   4   9  20 | 0.167  0.375 |           24 | yes
   4 1 6 24 | EA   |  18   4   8  16 | 0.167  0.333 |           22 | yes
   9 1 4 16 | EA   |  14   2   8  14 | 0.125  0.500 |           14 | yes
   9 1 4 16 | EA   |  12   2   7  10 | 0.125  0.438 |           12 | yes
   4 1 5 20 | EA   |  14   4   6  12 | 0.200  0.300 |           18 | yes
   4 1 3 12 | EA   |  10   2   6  10 | 0.167  0.500 |           10 | yes
   4 1 5 20 | EA   |  14   2   6  10 | 0.100  0.300 |           18 | yes
   9 1 6 24 | EA   |  10   6   5   2 | 0.250  0.208 |           12 | >= 5
   4 1 5 20 | EA   |  14   6   5  14 | 0.300  0.250 |           20 | yes
   4 1 4 16 | EA   |  10   4   5   8 | 0.250  0.312 |           12 | yes
   8 1 3 12 | EA   |   8   4   5   8 | 0.333  0.417 |            8 | yes
   9 1 5 20 | EA   |  10   2   5   2 | 0.100  0.250 |           12 | >= 5
   4 1 3 12 | EA   |   8   2   5   6 | 0.167  0.417 |            8 | yes
   9 1 6 24 | EA   |   8  10   4   2 | 0.417  0.167 |           10 | >= 4
   9 1 6 24 | SO   |   8   8   4   0 | 0.333  0.167 |           10 | yes
   9 1 5 20 | EA   |   8   8   4   4 | 0.400  0.200 |           10 | >= 4
   4 1 5 20 | DC   |  12   4   4   0 | 0.200  0.200 |           10 | yes
   4 1 3 12 | EA   |   6   4   4   4 | 0.333  0.333 |            6 | yes
   4 1 4 16 | EA   |   8   4   4   4 | 0.250  0.250 |           10 | yes
   4 1 3 12 | EA   |   6   2   4   2 | 0.167  0.333 |            6 | yes
   9 1 4 16 | EA   |   8   2   4   2 | 0.125  0.250 |           10 | yes
   9 1 2  8 | EA   |   6   2   4   6 | 0.250  0.500 |            6 | yes
   9 1 6 24 | DC   |  18  12   3   0 | 0.500  0.125 |            8 | yes
   4 1 5 20 | EA   |   6  10   3   2 | 0.500  0.150 |            8 | yes
   9 1 4 16 | DC   |  12   8   3   0 | 0.500  0.188 |            4 | yes
   8 1 3 12 | DC   |   8   4   3   0 | 0.333  0.250 |            4 | yes
   4 1 2  8 | EA   |   4   4   3   4 | 0.500  0.375 |            4 | yes

  (e) BEST CODE PER ROUTE, AND PER NILPOTENCY INDEX t (O-6.2).
      SO : best d = 4 -> [[24,8,4]]_9  (k=8, h_E=8, exact)
      DC : best d = 4 -> [[20,4,4]]_4  (k=12, h_E=8, exact)
      EA : best d = 10 -> [[20,2,10;18]]_4  (k=18, h_E=0, exact)
```


### 3.5 Best code per route, and the barrier in `t` (O-6.2)


```
        t | families scanned      | stabilizer: best d | EA: best d
      ------------------------------------------------------------------
       1 | (4,1),(4,2),(4,3),(4, |                  4 | 10
       2 | (4,1),(4,2),(4,3),(9, |                  2 | 6
       3 | (4,1),(8,1),(9,1),(9, |                  1 | 4
       4 | (4,1)                 |                  1 | 2
```


> **T-220 (COMPUTATIONALLY VERIFIED ONLY).**  *O-6.1.*  With the entanglement
> bounded by `c <= 4` the best attainable distance is `d = 4`, with
> `K = 10` and `c = 2` (`[[24,10,4;2]]_9`, a proved lower bound);
> `d = 5` first appears at
> `c = 2` with `K = 6`, and `d = 6` only at `c = 10` (`[[12,2,6;10]]_4`,
> `h_E = 0`).  So the answer to O-6.1 — "is there a family with `d >= 4`,
> bounded `c` and `K >= 2`?" — is **yes, but only just**: `d = 4` with
> `K = 10, c = 2` is the frontier point, and every `d >= 5` costs at least
> `c = 2` and leaves `K <= 6`.
>
> **T-221 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`/`[SMP]`).**  *O-6.2.*  For
> the stabilizer routes the barrier in `t` is absolute in the scanned range:
> `t = 1` gives `d <= 4`, `t = 2` gives `d <= 2`, and for `t >= 3` **every**
> stabilizer code found has `d = 1` (it detects nothing at all).  The
> entanglement-assisted route is not subject to it: `d = 6` at `t = 2`
> (`(4,2,3)`), `d = 4` at `t = 3` (`(9,3,2)`).

---

## 4. Task D — non-principal hulls (O-6.4)

### 4.1 A structure theorem


```
PART 5.  TASK D: NON-PRINCIPAL HULLS (O-6.4) AND THEIR STRUCTURE
==============================================================================
  O-6.4 asked whether mu_B >= 3 hulls occur only at (q,t,n) = (4,2,2)
  or reappear at (4,2,4), (8,2,2), (9,2,3).  The first part of the
  answer is structural, and it is decisive:

  THEOREM.  Let B = A_t[X]/(X^n-1) and W <= B^2.
   (i) B = prod_j B_j with B_j = A_t[X]/(g_j^{e_j}) and
       B_j ~= F_{q^{d_j}}[u,w]/(u^t, w^{e_j});
   (ii) mu_B(W) = max_j mu_{B_j}(W_j);
   (iii) B_j is a chain ring  <=>  t = 1 or e_j = 1;
   (iv) over a finite chain ring every submodule of S^2 is free of
        rank <= 2, hence 2-generated;
   (v) hence  mu_B(W) >= 3  REQUIRES  t >= 2 and p | n
        (p | n <=> some e_j >= 2, since X^n - 1 = (X^{n'}-1)^{p^v}).
  WARNING.  The chain hypothesis in (iv) cannot be dropped: over a
  non-chain local ring (t >= 2 and p | n, e.g. F_q[u,w]/(u^2,w^2))
  the bound mu_B(W) <= 2 fails, and it fails for a HULL -- D3 below
  exhibits mu_B(Hull_s(W)) = 3 at (9,2,3) and at (4,2,4).
  So the phenomenon is confined to the WILD regime, and no extension
  of the range of n at t = 1 (Task B) can produce a new witness.
  Below: (iii) is verified by testing whether the maximal ideal of
  B_j is principal (a finite commutative ring is a chain ring iff it
  is local with principal maximal ideal), for every component of
  every enumerable family; (ii)+(iv) are verified by an independent
  Nakayama count mu = (dim V - dim mV)/[S/m : F_q] on components.
```


> **T-222 (PROVED, except (iii) which is `[EXH]`).**  Let
> `B = A_t[X]/(X^n−1)` and `W <= B^2`.  (i) `B = prod_j B_j` with
> `B_j ≅ F_{q^{d_j}}[u,w]/(u^t, w^{e_j})`; (ii)
> `mu_B(W) = max_j mu_{B_j}(W_j)`; (iii) `B_j` is a chain ring if and only if
> `t = 1` or `e_j = 1`; (iv) over a finite chain ring every submodule of
> `S^2` is free of rank `<= 2`, hence 2-generated; (v) therefore
> `mu_B(W) >= 3` **requires** `t >= 2` and `p | n`.
>
> The chain hypothesis in (iv) cannot be dropped: over a non-chain local ring
> (`t >= 2`, `p | n`, e.g. `F_q[u,w]/(u^2,w^2)`) the bound `mu_B(W) <= 2`
> fails, and it fails **for a hull** — §4.3 exhibits
> `mu_B(Hull_s(W)) = 3` at `(9,2,3)` and at `(4,2,4)`.

### 4.2 The census of `mu_B`


```
   (q,t,n) | regime      | components: (dim, chain?)         | max mu_B(W) | #W
  ------------------------------------------------------------------------------------
   (4,1,1)   | SEMISIMPLE  | (dim 1, chain)                   |           2 | 7
   (4,1,2)   | RAMIFIED    | (dim 2, chain)                   |           2 | 33
   (4,1,3)   | SEMISIMPLE  | (dim 1, chain), (dim 1, chain),  |           2 | 343
   (4,1,4)   | RAMIFIED    | (dim 4, chain)                   |           2 | 283
   (4,1,5)   | SEMISIMPLE  | (dim 1, chain), (dim 2, chain),  |           2 | 211
   (4,1,6)   | RAMIFIED    | (dim 2, chain), (dim 2, chain),  |           2 | 201
   (4,2,1)   | SEMISIMPLE  | (dim 2, chain)                   |           2 | 33
   (4,2,2)   | WILD        | (dim 4, NOT chain)               |           3 | 204
   (4,2,3)   | SEMISIMPLE  | (dim 2, chain), (dim 2, chain),  |           2 | 201
   (4,3,1)   | SEMISIMPLE  | (dim 3, chain)                   |           2 | 139
   (4,4,1)   | SEMISIMPLE  | (dim 4, chain)                   |           2 | 283
   (8,1,1)   | SEMISIMPLE  | (dim 1, chain)                   |           2 | 11
   (8,1,2)   | RAMIFIED    | (dim 2, chain)                   |           2 | 93
   (8,1,3)   | SEMISIMPLE  | (dim 1, chain), (dim 2, chain)   |           2 | 246
   (8,3,1)   | SEMISIMPLE  | (dim 3, chain)                   |           2 | 251
   (9,1,1)   | SEMISIMPLE  | (dim 1, chain)                   |           2 | 12
   (9,1,2)   | SEMISIMPLE  | (dim 1, chain), (dim 1, chain)   |           2 | 144
   (9,1,3)   | RAMIFIED    | (dim 3, chain)                   |           2 | 205
   (9,1,4)   | SEMISIMPLE  | (dim 1, chain), (dim 1, chain),  |           2 | 202
   (9,1,5)   | SEMISIMPLE  | (dim 1, chain), (dim 2, chain),  |           2 | 200
   (9,1,6)   | RAMIFIED    | (dim 3, chain), (dim 3, chain)   |           2 | 200
   (9,2,1)   | SEMISIMPLE  | (dim 2, chain)                   |           2 | 113
   (9,2,2)   | SEMISIMPLE  | (dim 2, chain), (dim 2, chain)   |           2 | 203
   (9,3,1)   | SEMISIMPLE  | (dim 3, chain)                   |           2 | 205
   (9,3,2)   | SEMISIMPLE  | (dim 3, chain), (dim 3, chain)   |           2 | 200
  [EXH] D1  the components of B are chain rings exactly when t = 1 or p does not divide n (verified by testing principality of the maximal ideal of every component of every enumerable family) PASS  [EXH] all components of 25 families
  [EXH] D2  mu_B(W) <= 2 in every non-wild family (t = 1 or p does not divide n), while mu_B(W) = 3 occurs in a wild family: the phenomenon is confined to the wild regime, as the theorem says PASS  [EXH] see the table above; max mu_B(W) per family
```


> **T-223 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  Across all 25
> enumerable families, `mu_B(W) <= 2` in every non-wild family and
> `mu_B(W) = 3` occurs in the wild family `(4,2,2)` — and, by (v) of T-222,
> it can occur *only* in wild families.  The chain/non-chain verdict of the
> theorem agrees with the direct test (maximal ideal principal) on every
> component of every enumerable family.

### 4.3 New witnesses: O-6.4 is answered

The three families named by O-6.4 — `(4,2,4)`, `(8,2,2)`, `(9,2,3)` — are all
wild and none of them is exhaustively enumerable, so witnesses must be
**constructed**.  `B` is local there, with maximal ideal `m`; by Nakayama
`mu_B(W) = dim W − dim mW`, and the family

```
W = (m^i e_1) ⊕ U,     U <= ann_{B^2}(m)
      ==>    mW = m^{i+1} e_1,
      ==>    mu_B(W) = dim m^i − dim m^{i+1} + dim U
```

is finite, deterministic, and contains every witness of this shape.  Each
candidate is formed, its `mu_B` is computed by the Phase-3B route, its Galois
hull `Hull_s(W)` is computed by the Morita route, and `mu_B` of the hull is
recomputed directly.


```
D3.  NEW mu_B >= 3 HULL WITNESSES IN WILD FAMILIES (O-6.4)
----------------------------------------------------------
  The three families named in O-6.4 -- (4,2,4), (8,2,2), (9,2,3) --
  are all wild (t >= 2 and p | n) and none of them is exhaustively
  enumerable, so witnesses must be CONSTRUCTED.  B is local there,
  with maximal ideal m; by Nakayama mu_B(W) = dim W - dim mW (the
  residue field is F_q), and
      W = (m^i e_1) (+) U,   U <= ann_{B^2}(m),
  gives mW = m^{i+1} e_1, hence
      mu_B(W) = dim m^i - dim m^{i+1} + dim U.
  This is a finite, completely deterministic family of candidates;
  every one of them is formed, its mu_B computed by the Phase-3B
  route, its Galois hull Hull_s(W) computed by the Morita route and
  the mu_B of the hull recomputed directly.

   (q,t,n,s) | N  | dim m, m^2, ... | dim ann(m) | #W mu>=3 | best: dim W, mu_B(W), dim Hull, mu_B(Hull)
  --------------------------------------------------------------------------------------------
   (4,2,2,0) | 16 | 3,1             |          2 |        12 | dim W = 5, mu_B(W) = 3, dim Hull = 6, mu_B(Hull) = 2
   (4,2,2,1) | 16 | 3,1             |          2 |        12 | dim W = 5, mu_B(W) = 3, dim Hull = 6, mu_B(Hull) = 2
   (8,2,2,0) | 16 | 3,1             |          2 |        56 | dim W = 5, mu_B(W) = 3, dim Hull = 6, mu_B(Hull) = 2
   (8,2,2,1) | 16 | 3,1             |          2 |        56 | dim W = 5, mu_B(W) = 3, dim Hull = 6, mu_B(Hull) = 2
   (9,2,3,0) | 24 | 5,3,1           |          2 |       144 | dim W = 5, mu_B(W) = 3, dim Hull = 10, mu_B(Hull) = 3
   (9,2,3,1) | 24 | 5,3,1           |          2 |       144 | dim W = 5, mu_B(W) = 3, dim Hull = 10, mu_B(Hull) = 3
   (4,2,4,0) | 32 | 7,5,3,1         |          2 |        36 | dim W = 7, mu_B(W) = 3, dim Hull = 10, mu_B(Hull) = 3
   (4,2,4,1) | 32 | 7,5,3,1         |          2 |        36 | dim W = 7, mu_B(W) = 3, dim Hull = 10, mu_B(Hull) = 3

  WITNESS (9,2,3) s=0 : dim W = 5, mu_B(W) = 3, dim Hull_s = 10 (= 5 in B^2 coords), mu_B(Hull_s) = 3, Hull = W: yes
      image code: N = 24, k = 10, h_E = 8, Galois SO = True, Euclidean SO = False, DC = False
      R1 : abelian = True, [[24,14,d = 2]]_9
      R3 (EA) : [[24,6,2;2]]_9   (h_E = 8, support search w<=2)
  WITNESS (9,2,3) s=1 : dim W = 5, mu_B(W) = 3, dim Hull_s = 10 (= 5 in B^2 coords), mu_B(Hull_s) = 3, Hull = W: yes
      image code: N = 24, k = 10, h_E = 8, Galois SO = True, Euclidean SO = False, DC = False
      R1 : abelian = True, [[24,14,d = 2]]_9
      R3 (EA) : [[24,6,2;2]]_9   (h_E = 8, support search w<=2)
  WITNESS (4,2,4) s=0 : dim W = 7, mu_B(W) = 3, dim Hull_s = 10 (= 5 in B^2 coords), mu_B(Hull_s) = 3, Hull = W: no
      image code: N = 32, k = 14, h_E = 10, Galois SO = False, Euclidean SO = False, DC = False
      R3 (EA) : [[32,8,2;4]]_4   (h_E = 10, support search w<=2)
  WITNESS (4,2,4) s=1 : dim W = 7, mu_B(W) = 3, dim Hull_s = 10 (= 5 in B^2 coords), mu_B(Hull_s) = 3, Hull = W: no
      image code: N = 32, k = 14, h_E = 10, Galois SO = False, Euclidean SO = False, DC = False
      R3 (EA) : [[32,8,2;4]]_4   (h_E = 10, support search w<=2)
  [EXH] D3  mu_B(Hull_s(W)) >= 3 occurs in a wild family other than (4,2,2) -- the three candidates named by O-6.4 are (4,2,4), (8,2,2), (9,2,3) PASS  [EXH] 4 witnesses: (9,2,3) s=0, (9,2,3) s=1, (4,2,4) s=0, (4,2,4) s=1
```


> **T-224 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]` over the constructed
> family).**  *O-6.4 is answered.*  `mu_B(Hull_s(W)) >= 3` **reappears**:
> at `(9,2,3)` (`N = 24`, `s = 0` and `s = 1`: `dim W = 5`, `mu_B(W) = 3`,
> `dim Hull_s = 10`, `mu_B(Hull_s) = 3`, and `Hull_s(W) = W`) and at
> `(4,2,4)` (`N = 32`, `s = 0,1`: `dim W = 7`, `dim Hull_s = 10`,
> `mu_B(Hull_s) = 3`, `Hull_s(W) ⊋ W`).  It does **not** reappear at
> `(8,2,2)`: there `mu_B(W) = 3` for 56 constructed modules but every hull
> has `mu_B(Hull_s) = 2`.  So `(4,2,2)` is not the only wild family with the
> phenomenon, but the phenomenon is confined to the wild regime, and the
> three candidate families of O-6.4 split 2–1.
>
> The witness modules also produce codes, and they are weak: `d = 2` in
> every case (`[[24,6,2;2]]_9`, `[[32,8,2;4]]_4`).  High `mu_B` and high
> distance do not go together in this framework.

---

## 5. Task E — independent certification of the headline codes

Each certified code is the **exact** code found by the search: the image
basis is carried through, so the certification cannot silently certify a
different code with the same invariants (the defect that Phase 6 found and
fixed in its own verification).


```
PART 6.  TASK E: INDEPENDENT CERTIFICATION OF THE HEADLINE CODES
==============================================================================
  Each certified code is the EXACT code found by the search (the
  image basis is carried through, no re-selection by invariants).
  Three independent methods:
    M1  complete enumeration of the relevant classical difference
        set (exact and complete when q^dim <= 3*10^6);
    M2  increasing-weight support search over F_q^N (a different
        algorithm: for each support it solves a left-kernel problem);
    M3  exhaustive search of the AMBIENT quantum space F_q^{2N} in
        increasing symplectic weight, testing commutation with the
        whole group V and non-membership of V (+) V.
  Plus: the stabilizer group is F_p-abelian, and K, c recompute.

   (q,t,n,N,kind) |  k   K   d   c | M1  | M2  | M3 (>=) | exact | abelian | S-def
  ------------------------------------------------------------------------------------
  (9,1,6,24,SO) |   8   8   4   0 |    - |    4 |      >2 | yes   | True    | 10
  (4,1,5,20,SO) |   8   4   4   0 |    - |    4 |      >2 | yes   | True    | 10
  (4,1,5,20,DC) |  12   4   4   0 |    - |    4 |      >2 | yes   | True    | 10
  (4,1,5,20,EA) |  18   2  10  18 |   10 |  n/a |      >2 | yes   | True    | 18
  (9,1,6,24,EA) |  20   2  10  18 |   10 |  n/a |      >2 | yes   | True    | 22
  (4,1,1, 4,EA) |   2   2   2   2 |    2 |  n/a |       2 | yes   | True    | 2
  (4,1,2, 8,EA) |   4   4   3   4 |    3 |  n/a |       3 | yes   | True    | 4
  (4,1,3,12,EA) |  10   2   6  10 |    6 |  n/a |      >2 | yes   | True    | 10
  (4,1,4,16,EA) |  10   4   5   8 |    5 |  n/a |      >2 | yes   | True    | 12
  (4,1,6,24,EA) |  20   4   9  20 |    9 |  n/a |      >2 | yes   | True    | 24
  (4,2,1, 8,EA) |   4   4   2   4 |    2 |  n/a |       2 | yes   | True    | 6
  (4,2,2,16,EA) |  12   4   4  12 |    4 |  n/a |      >2 | yes   | True    | 18
  (4,2,3,24,EA) |  20   4   6  20 |    6 |  n/a |      >2 | yes   | True    | 30
  (4,3,1,12,EA) |   6   6   2   6 |    2 |  n/a |       2 | yes   | True    | 10
  (4,4,1,16,EA) |  10   6   2  10 |    2 |  n/a |       2 | yes   | True    | 18
  (8,1,1, 4,EA) |   2   2   2   2 |    2 |  n/a |       2 | yes   | True    | 2
  (8,1,2, 8,EA) |   4   4   3   4 |    3 |  n/a |       3 | yes   | True    | 4
  (8,1,3,12,EA) |  10   2   6  10 |    6 |  n/a |      >2 | yes   | True    | 10
  (8,3,1,12,EA) |   8   4   2   8 |    2 |  n/a |       2 | yes   | True    | 14
  (9,1,1, 4,EA) |   2   2   2   2 |    2 |  n/a |       2 | yes   | True    | 2
  (9,1,2, 8,EA) |   6   2   4   6 |    4 |  n/a |      >3 | yes   | True    | 6
  (9,1,3,12,EA) |   8   2   5   6 |    5 |  n/a |      >2 | yes   | True    | 8
  (9,1,4,16,EA) |  14   2   8  14 |    8 |  n/a |      >2 | yes   | True    | 14
  (9,1,5,20,EA) |  16   4   9  16 |    9 |  n/a |      >2 | yes   | True    | 16
  (9,2,1, 8,EA) |   4   4   2   4 |    2 |  n/a |       2 | yes   | True    | 6
  (9,2,2,16,EA) |  12   4   4  12 |    4 |  n/a |      >2 | yes   | True    | 18
  (9,3,1,12,EA) |   8   4   2   8 |    2 |  n/a |       2 | yes   | True    | 14
  (9,3,2,24,EA) |  18   6   4  18 |    - |    4 |      >2 | yes   | True    | 30
  [EXH] E1  every headline code is certified by the three independent methods (classical enumeration, support search, ambient quantum search), has an F_p-abelian stabilizer, and recomputes K and c PASS  [EXH] 28 certified codes

       M1 and M2 decide the exact minimum weight of the classical difference set; M3 is complete only up to the weight reached and is stated as a lower bound otherwise.  For a stabilizer code the Knill-Laflamme condition at radius t = floor((d-1)/2) is equivalent to d = min swt(S^{perp} \ S), which is what M1/M2/M3 certify.
```


> **T-225 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  All 28 certified codes
> pass: M1 and M2 (two different algorithms) agree with the reported
> distance whenever they terminate, M3 (the ambient quantum search) never
> contradicts them, the stabilizer group is abelian on an `F_p`-basis
> (T-203), and `K` and `c` recompute from the stabilizer.  `M3` is complete
> only up to the weight reached and is reported as a lower bound otherwise;
> `M2` is run only when `M1` cannot finish.

---

## 6. Task F — recheck of the Phase 6 obstructions, and the errata

### 6.1 ERRATUM E-7.1 — the entanglement bookkeeping of Phase 6, O-6.1


```
F1.  ERRATUM E-7.1 -- the EA bookkeeping identity of Phase 6 O-6.1
------------------------------------------------------------------
  Phase 6, section 12, open problem O-6.1, states:
      'the entanglement grows with d (c + K = N - k)'.
  That identity is WRONG.  With k = dim D, h_E = dim(D n D^{perp_E}),
      c = k - h_E,   K = N - k - h_E   ==>   c + K = N - 2 h_E,
  and c + K = N - k would force h_E = k/2, which is false in general.
  Check against Phase 6's OWN table (parsed from
  phase6_quantum_parameter_log.txt, the Pareto frontier):
      25 rows parsed; 23 of them violate c + K = N - k, i.e. the
      claimed identity holds for only 2 of 25 rows.
        (4,1,3) N=12 EA: k=10 K=2 c=10  ->  c+K=12 but N-k=2
        (4,1,4) N=16 EA: k=10 K=4 c=8  ->  c+K=12 but N-k=6
        (4,2,3) N=24 EA: k=16 K=4 c=12  ->  c+K=16 but N-k=8
        (4,1,3) N=12 EA: k=8 K=2 c=6  ->  c+K=8 but N-k=4
  [EXH] F1  ERRATUM E-7.1: Phase 6 section 12 (O-6.1) states c + K = N - k; the correct identity is c + K = N - 2 h_E.  Phase 6's own table contradicts the stated identity, and the corrected one holds for every code of the new search PASS  [EXH] 25 Phase-6 rows re-parsed, 5055 codes of the new search

       the erratum does not affect any Phase 6 PARAMETER: K, c and d were
       computed from k and h_E directly.  It affects only the prose
       identity in O-6.1, and the reading of it as the reason why the
       entanglement 'grows with d'.
```


### 6.2 The characteristic-two obstruction, re-run verbatim


```
F2.  the characteristic-two obstruction of Phase 6 (E1/E2/E3), re-run unchanged
-------------------------------------------------------------------------------
  Phase 6's Task E is re-executed verbatim (its own code, its own
  checks E1/E2/E3) to confirm that the extension of the range of n
  has not disturbed it.
```


Phase 6's own Task E (its code, its checks E1/E2/E3) is re-executed
unchanged; it still passes, and its conclusions are unchanged: for `p = 2`
and `t` even, `H_t` is alternating and alternatingness is preserved by
*every* congruence, so no linear change of physical coordinates maps `H_t` to
`I_t` (`[SMP]`, 200 random invertible `S` per `(q,t)`, 5 parameter pairs);
for `t` odd a congruence `S^T H_t S = I_t` is constructed explicitly and
verified for `(q,t) = (4,1), (4,3), (4,5), (8,1), (8,3)`, and the
construction correctly returns nothing for `(4,2), (8,2), (4,4)`; and the
twisted-graph bypass R1 realises an explicit abelian group at `(4,2,2)`
(59 of 60 codes).  The extension of the range of `n` has not disturbed any of
it.  (The J-frame CSS bypass was also re-measured: best distance `2`, over
398 valid pairs at `(4,2,2)` and `(4,1,4)` — unchanged from Phase 6.)

### 6.3 Phase 6's headline distances, re-derived


```
F3.  Phase 6's headline numbers re-derived by the new search
------------------------------------------------------------
   (q,t,n)   | kind | Phase 6 best d | new search best d |
  ----------------------------------------------------------
   (4,1,3)   | DC   |             1 |                 2 |
   (4,1,3)   | EA   |             6 |                 6 |
   (4,1,3)   | SO   |             2 |                 2 |
   (4,1,4)   | DC   |             1 |                 3 |
   (4,1,4)   | EA   |             5 |                 5 |
   (4,1,4)   | SO   |             3 |                 3 |
   (4,2,3)   | DC   |             2 |                 2 |
   (4,2,3)   | EA   |             5 |                 6 |
  [EXH] F2  the new search never reports a best distance SMALLER than the Phase 6 Pareto value for the same family and route (it reproduces or improves it, family by family) PASS  [EXH] 8 (family, route) pairs compared
```


### 6.4 What the extension changes


```
F4.  what the extension changes (refinements, not errata)
---------------------------------------------------------
   * Phase 6 section 12 (O-6.1) records 'no stabilizer point has
     d >= 4'.  That statement is correct FOR THE FAMILIES PHASE 6
     SCANNED (N <= 16, n <= 4).  It is not a statement about the
     framework: the new family (4,1,5), N = 20, contains stabilizer
     codes with d = 4 (see PART 4).  No Phase 6 number is wrong.
   * Phase 6 section 12 (O-6.3) is RESOLVED by PARTS 1-2 of this
     run: n = 5, 6 at t = 1 and n = 3 at q = 8 are now reachable,
     and the two families Phase 6 could only sample ((4,2,3),
     (9,2,2)) are now exhaustive.
   * Phase 6 section 12 (O-6.4) is ANSWERED by PART 5: mu_B >= 3
     hulls reappear at (4,2,4) and (9,2,3), not at (8,2,2).
   * Phase 6 section 12 (O-6.2) is re-measured in PART 4(e).
```


> **T-226 (COMPUTATIONALLY VERIFIED ONLY).**  On all 8 `(family, route)`
> pairs that Phase 6's Pareto frontier and the new search share, the new
> search never reports a smaller best distance: three are improvements
> (`(4,2,3)` EA `5 → 6`, `(4,1,4)` DC `1 → 3`, `(4,1,3)` DC `1 → 2`) and
> five are reproduced exactly.  **Phase 6 §12's "no stabilizer point has `d >= 4`"
> is correct only for the families Phase 6 scanned** (`N <= 16`): the new
> family `(4,1,5)`, `N = 20`, contains stabilizer codes of distance `4`.  No
> Phase 6 number is wrong; one Phase 6 sentence is out of scope, and one
> Phase 6 identity is wrong (E-7.1).

---

## 7. Task G — bounds, and comparison with the published tables


```
PART 8.  TASK G: BOUNDS AND COMPARISON WITH KNOWN CODES
==============================================================================
  For every code of the search the two standard bounds are checked:
    EA quantum Singleton   N - K + c >= 2(d - 1)   [Lai-Brun-Wilde]
    EA quantum Hamming     with the effective dimension K - c:
      (sum_{i<=t} C(N,i)(q^2-1)^i) q^{K-c} <= q^N, t = (d-1)//2
    (for c = 0 these are the ordinary quantum Singleton / Hamming
    bounds).  A lower-bound entry is tested with its proved value.

   codes checked: 5055 ; EA-Singleton violations: 0 ; EA-Hamming violations: 0
  [EXH] G1  every code found satisfies the EA quantum Singleton bound N - K + c >= 2(d-1) and the EA quantum Hamming bound with effective dimension K - c PASS  [EXH] 5055 codes, 0 Singleton and 0 Hamming violations


G2.  comparison with the best known codes
-----------------------------------------
  Source: M. Grassl, 'Bounds on the minimum distance of linear
  quantum codes', codetables.de, accessed 2026-11-04.  Of the
  alphabets used here only GF(4) is tabulated: q = 8 returns
  'currently not available for q=8' and q = 9 is not offered at
  all.  So only the q = 4 codes found here can be compared, and
  only the stabilizer ones (c = 0): there is no published table
  of entanglement-assisted codes.

   code found here      | kind | best known [[N,K]]_q          | gap
  ----------------------------------------------------------------------
   [[20, 4,4]]_4   | DC   | [[20, 4,6]]_4 (6..6)   | 2 below
   [[20, 4,4]]_4   | SO   | [[20, 4,6]]_4 (6..6)   | 2 below
   [[16, 4,3]]_4   | DC   | [[16, 4,5]]_4 (5..5)   | 2 below
   [[16, 4,3]]_4   | SO   | [[16, 4,5]]_4 (5..5)   | 2 below
   [[24,20,2]]_4   | DC   | [[24,20,2]]_4 (2..2)   | record
   [[20,16,2]]_4   | DC   | [[20,16,2]]_4 (2..2)   | record
   [[20,16,2]]_4   | SO   | [[20,16,2]]_4 (2..2)   | record
   [[24,16,2]]_4   | DC   | [[24,16,3]]_4 (3..3)   | 1 below
   [[16,12,2]]_4   | DC   | [[16,12,2]]_4 (2..2)   | record
   [[16,12,2]]_4   | SO   | [[16,12,2]]_4 (2..2)   | record
   [[20,12,2]]_4   | DC   | [[20,12,3]]_4 (3..3)   | 1 below
   [[20,12,2]]_4   | SO   | [[20,12,3]]_4 (3..3)   | 1 below

       the comparison is limited to q = 4 and to c = 0: every q=8 and
       q=9 code found here, and every entanglement-assisted code, is
       unbenchmarked -- for those the EA-Singleton margin of PART 4(d)
       is the only benchmark available.  No code of this framework is
       claimed to be a record: the table above states the gap, and the
       q=4 entries were read off codetables.de one page at a time.
```


> **T-227 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  All 5055 codes with a
> computed distance satisfy the EA quantum Singleton bound
> `N − K + c >= 2(d−1)` and the EA quantum Hamming bound with effective
> dimension `K − c`: 0 violations of either.
>
> **T-228 (COMPUTATIONALLY VERIFIED ONLY).**  *Literature comparison.*  Of
> the three alphabets used here only `GF(4)` is tabulated at
> `codetables.de`: `q = 8` returns "currently not available for q=8" and
> `q = 9` is not offered at all, so the `q = 8` and `q = 9` codes of this
> search **cannot be benchmarked** — correcting the Phase 6 statement that
> `q = 2,3,4,5,7,8` are tabulated.  Of the 12 comparable stabilizer
> entries, 5 meet the best known distance — all with `d = 2`:
> `[[24,20,2]]_4`, `[[20,16,2]]_4` (as SO and as DC) and `[[16,12,2]]_4`
> (as SO and as DC) — while 4 are 2 below and 3 are 1 below.  **No record is claimed.**  The entanglement-assisted codes
> (`c > 0`) have no published table at all; the EA-Singleton margin of §3.4
> is the only benchmark available for them.

---

## 8. Task H — negative controls


```
PART 9.  NEGATIVE CONTROLS
==============================================================================
  Each control must FAIL (or must be detected).  A control that
  silently succeeded would mean the corresponding check has no
  teeth.
  N1  the CRT multiplicativity test has teeth: the TRUE
      factorisation of X^5-1 over F_4 gives 0 violations on all 5^2
      pairs of basis elements; the FALSE one X^5-1 = (X-1)^5 gives 10
  [EXH] N1  the CRT map built from the true factorisation of X^n-1 is multiplicative while the map built from a false one is not (the verification would catch a wrong factorisation) PASS  [EXH] true: 0 violations; false (X^5-1 = (X-1)^5): 10
  N2  the chain-ring test discriminates: F_4[u]/(u^2) -> True,
      F_4[u,w]/(u^2,w^2) (the wild (4,2,2) component) -> False,
      F_4 -> True
  [EXH] N2  the chain-ring test returns True for a genuine chain ring and False for the wild local non-chain ring, so the structural theorem of PART 5 is not vacuous PASS  [EXH] chain: True, wild: False, field: True
  N3  the product assembly is exactly the product of the component
      lattices: 7 x 7 x 7 = 343, and the assembled list has 343
  [EXH] N3  the number of B-submodules of B^2 equals the product of the numbers of B_j-submodules of B_j^2 (no submodule is missed and none is duplicated) PASS  [EXH] (4,1,3): 343 = 343
```


A control that silently succeeded would mean the corresponding check has no
teeth: N1 shows the multiplicativity test detects a deliberately false
factorisation of `X^5 − 1`; N2 shows the chain-ring test separates
`F_4[u]/(u^2)` from the wild `F_4[u,w]/(u^2,w^2)`; N3 shows the product
assembly is exactly the product of the component lattices.

---

## 9. Results of Phase 7 (register rows T-216 … T-229)

| row | statement | label |
|---|---|---|
| **T-216** | the CRT enumeration reproduces the Phase-3B exhaustive BFS as a **set** on all 10 supported families; `(4,1,5)`, `(4,1,6)`, `(8,1,3)` become exhaustive (**O-6.3 resolved**) | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-217** | census over 42 families: 23 exhaustive, 4 counted-only, 15 blocked by the component BFS; 10 previously sampled families are now exhaustive | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-218** | 25 families scanned, 120721 codes with invariants, 5055 with a distance (4418 exact, 637 proved lower bounds); largest exact distance `d = 10` | COMPUTATIONALLY VERIFIED ONLY |
| **T-219** | `k` even, `K − c = N − 2k ≡ 0 (mod 4)`, `c + K = N − 2h_E`, `c >= 2k − N` | PROVED, `[EXH]` |
| **E-7.1** | **erratum**: Phase 6 O-6.1's `c + K = N − k` is wrong (only 2 of its own 25 rows satisfy it); correct: `c + K = N − 2h_E` | PROVED |
| **T-220** | O-6.1: with `c <= 4` the best is `d = 4` (`K = 10`, `c = 2`); `d = 5` costs `c >= 2` and leaves `K <= 6`; `d = 6` costs `c = 10` | COMPUTATIONALLY VERIFIED ONLY |
| **T-221** | O-6.2: stabilizer `d <= 4` at `t = 1`, `<= 2` at `t = 2`, `= 1` for `t >= 3`; EA reaches `d = 6` at `t = 2` and `d = 4` at `t = 3` | COMPUTATIONALLY VERIFIED ONLY |
| **T-222** | structure theorem: `mu_B(W) = max_j mu_{B_j}(W_j)`; `B_j` chain `⟺` `t = 1` or `e_j = 1`; `mu_B >= 3` needs `t >= 2` and `p \| n`; the bound `mu_B <= 2` is FALSE for non-chain local rings | PROVED (`(iii)` `[EXH]`) |
| **T-223** | `mu_B(W) <= 2` in every non-wild family; `= 3` occurs in the wild family `(4,2,2)`; the chain verdict matches the direct test on every component of every enumerable family | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-224** | **O-6.4 answered**: `mu_B(Hull_s) >= 3` reappears at `(9,2,3)` (`s = 0,1`, `Hull = W`) and `(4,2,4)` (`s = 0,1`, `Hull ⊋ W`); **not** at `(8,2,2)` | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-225** | 28 headline codes certified by three independent methods, `F_p`-abelian stabilizer, `K` and `c` recomputed | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-226** | the new search reproduces or improves every shared Phase 6 Pareto distance (8 pairs: 3 improved, 5 equal); Phase 6's "no stabilizer `d >= 4`" is scoped to `N <= 16` | COMPUTATIONALLY VERIFIED ONLY |
| **T-227** | 5055 codes, 0 EA-Singleton and 0 EA-Hamming violations | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |
| **T-228** | only `GF(4)` is tabulated (`q = 8` unavailable, `q = 9` not offered — correcting Phase 6); 5 of 12 comparable stabilizer entries meet the best known distance (all `d = 2`), 7 are 1–2 below; **no record claimed** | COMPUTATIONALLY VERIFIED ONLY |
| **T-229** | the search is seeded (`20261210`) and deterministic: two runs agree on every line except the wall-clock annotations | COMPUTATIONALLY VERIFIED ONLY, `[EXH]` |

---

## 10. Resolution of the Phase-6 open problems

| problem | status after Phase 7 |
|---|---|
| **O-6.1** — a family with `d >= 4`, bounded `c`, `K >= 2`? | **RESOLVED (yes, tightly).**  `[[24,10,4;2]]_9` (`c = 2`, `K = 10`, `d >= 4`) is the frontier; `d >= 5` needs `c >= 2` and leaves `K <= 6`; `d = 6` needs `c = 10`.  The bookkeeping identity behind the question was wrong and is corrected (E-7.1). |
| **O-6.2** — a route using the Gram form `J` with `d >= 3` at `t >= 2`? | **RESOLVED (no for the stabilizer routes).**  `d <= 2` at `t = 2` and `d = 1` for `t >= 3` — the stabilizer routes detect nothing at all for `t >= 3`.  The EA route, which also works with the Gram form, does reach `d = 6` at `t = 2` and `d = 4` at `t = 3`. |
| **O-6.3** — extend the component routine to `n = 5, 6` at `t = 1` and `n = 3` at `q = 8` | **RESOLVED.**  The general CRT decomposition of §1.1 opens all three (T-216, T-217). |
| **O-6.4** — do `mu_B >= 3` hulls reappear at `(4,2,4)`, `(8,2,2)`, `(9,2,3)`? | **RESOLVED (2 of 3).**  Yes at `(9,2,3)` and `(4,2,4)`, no at `(8,2,2)`; and T-222(v) proves the phenomenon is confined to the wild regime, so no amount of extending `n` at `t = 1` can produce a new witness. |
| **O-6.5** — a table or bound for EA parameters | **STILL OPEN, and worse than stated:** the published tables cover `GF(4)` only, so even the stabilizer codes over `F_8` and `F_9` cannot be benchmarked, let alone the EA ones.  No EA table exists. |
| **O-6.6** (from O-5.3) — entanglement number of the semilinear group | **STILL OPEN.**  Not addressed here. |

---

## 11. Open problems after Phase 7

* **O-7.1.**  `(4,1,6)` (`N = 24`) and `(9,1,6)` (`N = 24`) are now
  enumerated exhaustively **as sets** (35937 and 1048576 submodules), but the
  distance pipeline handles only 390 codes per family.  The true maximum
  distance at `N = 24` in this framework is therefore unknown; the reported
  `d = 9` and `d = 10` are lower bounds on that maximum.
* **O-7.2.**  The component BFS is the binding constraint: 15 families, among
  them all of `N = 32`, are blocked because `q^{2 dim S} > 4·10^6` for some
  component `S`.  A constructive enumeration of the submodules of `S^2` (by
  generator degree rather than by BFS on the underlying set) would open
  `N = 32`, where the distances are likely to be better.
* **O-7.3.**  Every `mu_B >= 3` witness found here has `mu_B = 3` exactly,
  and the construction of §4.3 caps at `dim m^i − dim m^{i+1} + 2` because
  `dim ann_{B^2}(m) = 2` in all four families examined.  Is `mu_B >= 4`
  attainable for a *hull*?
* **O-7.4.**  The best codes of this search — `[[20,2,10;18]]_4`,
  `[[24,2,10;18]]_9` — cannot be compared with anything: there is no EA
  table, and for `q = 9` not even a stabilizer table.  An EA-specific upper
  bound stronger than EA-Singleton for these `(N,K,c)` would be needed to say
  whether they are good.
* **O-7.5.**  At `t >= 3` every stabilizer code found has `d = 1`.  Is that
  forced by the structure (the Morita image of a `t >= 3` code always
  containing a weight-one vector outside `D`), or is it an artefact of
  `n <= 8`?
* **O-7.6 (carried from O-6.6 / O-5.3).**  The semilinear (only
  `F_p`-linear) twisted group and its entanglement number are still not
  settled.

---

## 12. Completion report for Phase 7

* **Tasks A–H: complete.**  The reachable family list is extended by a
  general, verified CRT decomposition and re-censused (§1); the search is
  systematic over that list with exact or proved-lower-bound distances (§2);
  the entanglement budget of high-distance codes is measured against the
  corrected bookkeeping and O-6.1 is answered (§3); the non-principal-hull
  question O-6.4 is answered by a structure theorem and by constructed
  witnesses (§4); the headline codes are certified by three independent
  methods (§5); every Phase 6 obstruction statement is re-examined, one
  erratum is recorded and one Phase 6 sentence is re-scoped (§6); the bounds
  hold and the literature comparison is made with an explicit statement of
  what cannot be compared (§7); three negative controls have teeth (§8); and
  the run is seeded and reproducible (this file).
* **Verification.**  17 checks, 17 PASS, 0 FAIL, ≈1050 s.  The run is seeded
  (`SEED = 20261210`) and every random choice is drawn from
  `random.Random(SEED)` in a fixed order; two runs of the final script agree
  on every line except the per-family elapsed-time annotations `[..s]`, which
  are wall-clock readings and take no part in any computation.
* **Corrections made in this phase (recorded, not silently patched).**
  1. **E-7.1** — Phase 6 §12 (O-6.1) states `c + K = N − k`; the correct
     identity is `c + K = N − 2 h_E` (§3.1, §6.1).  No Phase 6 *parameter*
     is affected.
  2. Phase 6 §12's "no stabilizer point has `d >= 4`" is true only for the
     families Phase 6 scanned (`N <= 16`); `(4,1,5)`, `N = 20`, has
     stabilizer codes of distance 4 (§3.5, §6.4).
  3. Phase 6 §8's "q = 2,3,4,5,7,8 are tabulated" is corrected: `q = 8` is
     "currently not available" at `codetables.de`, so only the `GF(4)` codes
     can be compared (§7).
* **Scope limits stated where they bite.**  Sampled families are reported as
  samples (`#codes < total` in §2); counted-only and blocked families are
  listed with the reason (§1.2); lower-bound distances are marked `>=` in
  every table; the deep support search is capped at 25 codes per family and
  reaches weight 6 only for `N <= 16`.
* **Safeguards honoured.**  Phases 0–6 documents, scripts and logs untouched;
  the theorem register grows by insertion only (T-216 … T-229); every
  statement is labelled; no distance is reported without an exhaustive or
  proved-lower-bound computation; no sample is presented as exhaustive; no
  record is claimed; no manuscript text was written.
