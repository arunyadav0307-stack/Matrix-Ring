# What "certified" means here, and how to re-certify a code

> **This is the corrected version (Phase 16).**
> It supersedes the version shipped in the original supplementary package, whose
> Section 3 asserted that *"Every headline code is certified by three
> structurally different methods."* That statement is **false** and is
> contradicted by the committed source of the computation. The original file is
> preserved byte-for-byte in the historical package as evidence of the earlier
> documentation state. See `SUPPLEMENTARY_CORRECTION_NOTE.md` for the
> append-only record of this supersession.

This note fixes the meaning of the word *certified* as used in the
manuscript, and gives the procedure used for every code in
`parameter_tables/certified_codes.csv` and in Tables 1 and 3 of the paper.

## 1. What is being certified

Two different things, and the distinction is maintained everywhere:

* **Exact distance.** A number $d$ such that the code provably has minimum
  distance exactly $d$.
* **Proved lower bound.** A number $d_0$ such that the code provably has
  minimum distance $\ge d_0$, with no claim about equality.

In the search, $4\,418$ of the $5\,055$ distances are exact and $637$ are
proved lower bounds. The two are never merged, and every table column
records which is which.

## 2. What the distance is

For the CSS routes (SO and DC) and for the entanglement-assisted route (EA),
the quantum distance equals the minimum Hamming weight of the *classical*
difference set:

| route | group | difference set |
|---|---|---|
| SO | $\mathcal C = D\oplus D$, $D\subseteq D^{\perp_E}$ | $D^{\perp_E}\setminus D$ |
| DC | $\mathcal C = D^{\perp_E}\oplus D^{\perp_E}$, $D^{\perp_E}\subseteq D$ | $D\setminus D^{\perp_E}$ |
| EA | $V = D\oplus D$, arbitrary $D$ | $D^{\perp_E}\setminus \mathrm{Hull}_E(D)$ |

By Theorem 8.1 of the manuscript (the coset-distance characterisation) the
EA difference set is the set of **nonzero elements of the quotient code**
$D^{\perp_E}/\mathrm{Hull}_E(D)$, a linear code of length $N$ and dimension
$K=N-k-h_E$. This is what makes a complete enumeration possible.

For route R1 (the Galois-native twisted embedding) only the upper bound
$d\le\min\mathrm{wt}(D^{\perp_E})$ is proved; R1 is never claimed to be
certified by the procedure below.

## 3. The three methods, and which ones actually run

**Three methods exist in the pipeline. They are not all run for every code.**
For every one of the 28 certified codes, **exactly two** methods are executed:
one exact classical method (M1 or M2) and the ambient quantum search (M3).

The distribution over the 28 certified codes is:

| | M1 completes | M1 does not complete | total |
|---|---|---|---|
| codes | **24** | **4** | **28** |
| exact method used | **M1** | **M2** | — |
| M2 | conditionally skipped | run (exact) | — |
| M3 | run (all 28) | run (all 28) | 28 |
| **methods actually executed** | **M1 + M3** | **M2 + M3** | **2 per code** |

**No code is certified by all three methods.**

### M1 — complete enumeration

Enumerate the relevant classical difference set completely and take the
minimum weight. Complete when $q^{\dim}\le 3\cdot10^6$ (the constant
`ENUM_CAP = 262144` in the script bounds a single complete enumeration of a
code; the difference-set enumerations quoted as complete are those for which
the enumeration finished within that cap). Output: exact.

Implementation: `phase6_quantum_parameter_enhancement.enum_min_weight`,
returning a pair `(d, complete)`. If the fast enumeration does not complete and
the field has odd characteristic, a slower enumeration is attempted with
`slow_cap = 50000`. If neither completes, it returns `(None, False)`.

**M1 is attempted for every certified code.** It completes for 24 of the 28.

### M2 — increasing-weight support search

A different algorithm. For each support $S\subseteq\{1,\dots,N\}$ of size
$w=1,2,3,\dots$ in increasing order, solve the left-kernel problem "does the
difference set contain a vector supported inside $S$?". The first $w$ at
which a solution exists is the distance.

Implementation: `phase5_quantum_constructions.min_weight_in`, called with
`maxw = min(8, max(3, d+1))`. It is exhaustive up to that weight: a return of
`None` means "no codeword of weight $\le$ `maxw`", which is a rigorous lower
bound and never a guess.

M2 shares no code with M1, so had the two been run together their agreement
would have been a genuine cross-check. **They are not run together** — see the
conditional execution logic below.

### M3 — ambient quantum search

Search the ambient symplectic space $\mathbb F_q^{2N}$ in increasing
symplectic weight for a vector $v$ with $v\in V^{\perp_\omega}$ and
$v\notin V$. This certifies the distance in the quantum language directly,
without passing through the coset-distance theorem.

Implementation: `phase6_quantum_parameter_enhancement.ambient_quantum_search`,
called with `maxw = w3`, where **`w3 = 3` if $N\le 8$ and `w3 = 2` otherwise**.
Because the search proceeds in increasing weight from $w=1$, the first hit is
the true minimum. Two outcomes are possible, and they mean different things:

* **A vector is found at weight $w$.** Then $d=w$ **exactly**: M3 has
  independently determined the distance in the quantum language. This happens
  for **11 of the 28** codes.
* **No vector is found at any weight $\le w3$.** Then the proved statement is
  $d\ge w3+1$ — a **lower bound only**, recorded in the table as `$>2$' or
  `$>3$'. This happens for the other **17 of the 28** codes.

So M3 is a full independent determination for 11 codes and a corroborating
lower bound for 17. It is run for all 28.

### The conditional execution logic (verbatim from the source)

The whole of the per-code behaviour follows from these lines of
`phase7_extended_search.py`, function `part6_certification` (lines 1670–1681):

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"
else:
    # M2 is run only when M1 could not finish; searching up to the
    # reported value is what an INDEPENDENT confirmation needs (it
    # must find a codeword of exactly that weight and none below)
    d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd,
                             maxw=min(8, max(3, (r["d"] or 0) + 1)))
w3 = 3 if N <= 8 else 2
d3, wit3 = P6.ambient_quantum_search(F, N, YV, Vgen, w3)
```

Read literally:

1. **M1 is always attempted.**
2. **M2 runs if and only if M1 did not complete.** When M1 completes, `d2` is
   set to `None` and the table entry is written as `n/a`.
3. **M3 always runs**, independently of what M1 and M2 did.

The `agree` flag that produces the `exact` column is computed as
`agree = (not comp1 or d1 == rep) and (d2 is None or d2 == rep) and (...)`,
which is exactly the statement "every method that actually ran agrees with the
reported value".

### Why not all three methods are executed for every code

Because M2 exists as a **fallback for M1, not as a third opinion**. M1
(complete enumeration) is tried first; when it finishes it has already
established the minimum weight exhaustively, so running the support search
would add no information — it is a different algorithm for the *same*
question, and the pipeline spends the compute on M3 instead, which is a
genuinely independent check in the quantum language. When M1 cannot finish,
M2 is the method that recovers an exact answer.

It follows that **the number of methods executed per code is two, by
construction, and the pair is (M1, M3) or (M2, M3) — never (M1, M2, M3) and
never (M1, M2)**.

### Which methods provide what

| role | method | for how many of the 28 codes |
|---|---|---|
| **exact distance** | M1 (24 codes) or M2 (4 codes) — whichever ran | 28 of 28 |
| **independent cross-check, itself exact** | M3, when it finds a vector at weight $\le w3$ | 11 of 28 |
| **independent cross-check, lower bound only** | M3, when it finds nothing below $w3$ | 17 of 28 |

The exact distance of each certified code therefore rests on **one** exact
classical method plus an independent quantum cross-check that is exact for 11
codes and a proved lower bound for the other 17. It never rests on agreement
of three methods, because three methods never run.

### Applicability is per code, not per route

It is tempting to suppose that the choice of M1 versus M2 follows the
construction route (SO / DC / EA). **It does not.** The rule is per code and
depends only on whether that code's M1 enumeration completed. The four codes
for which M2 ran are:

| code | family | route |
|---|---|---|
| $[[24,8,4]]_9$ | $(9,1,6)$ | SO |
| $[[20,4,4]]_4$ | $(4,1,5)$ | SO |
| $[[20,4,4]]_4$ | $(4,1,5)$ | DC |
| $[[24,6,4;18]]_9$ | $(9,3,2)$ | **EA** |

The last of these is an entanglement-assisted code, so "M2 is not applicable
to the EA route" is **false**. Equally, 24 EA codes used M1 while one did not,
so "EA codes use M1" is *usually but not always* true. Only the per-code
record settles it.

### Additional checks

For every certified code the pipeline also verifies:

* the stabilizer group is abelian **on an $\mathbb F_p$-basis** (Theorem 7.3
  of the manuscript; testing on an $\mathbb F_q$-generating set is invalid
  and yields $d=1$ instead of $d=3$ for $[[16,4,3]]_4$);
* $K$ and $c$ recompute from $k$ and $h_E$ via $c=k-h_E$ and $K=N-k-h_E$;
* the entanglement-assisted Singleton and Hamming bounds hold (check G1,
  0 violations on all $5\,055$ codes);
* the coset Singleton bound $K+d\le N+1$ holds (check H1, 0 violations).

## 4. How to determine the methods actually used for a particular code

Three independent sources agree, and all three are shipped:

1. **The per-code table.** `parameter_tables/certified_codes.csv` has columns
   `M1`, `M2` and `M3_lower_bound`. Read them as:

   | entry in column M1 | entry in column M2 | meaning |
   |---|---|---|
   | a number | `n/a` | M1 ran and gave the exact distance; M2 was skipped |
   | `-` | a number | M1 did not complete; M2 ran and gave the exact distance |

   In the `M3_lower_bound` column, a number is an exact result from M3;
   `$>2$' or `$>3$' is a proved lower bound $d\ge3$ or $d\ge4$ respectively.

2. **The execution log.** Part 6 of `logs/phase7_extended_search_log.txt`
   (lines 449–478) prints one row per certified code with the same three
   columns. It reproduces the CSV by construction.

3. **The generator-matrix records.** Each file in `generator_matrices/`
   carries a `distance_method` field naming the method that produced the
   recorded `d`.

The definitive per-code reconstruction, cross-checked against all three and
against the source, is
`PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.

> **Note on the historical log.** Line 478 of
> `logs/phase7_extended_search_log.txt` carries check `[EXH] E1`, whose text
> reads *"every headline code is certified by the three independent methods
> (classical enumeration, support search, ambient quantum search)"*. That
> wording is **wrong** for the same reason as the original Section 3: the code
> path it summarises runs M2 only when M1 fails. The log is a historical
> record of what the program printed and has deliberately **not** been
> rewritten; this note is the correction of it.

## 5. The defect that was found and fixed, and why it cannot recur

An earlier version of this project certified a code that was *re-selected by
invariants* — a different code with the same $(q,t,n,N,\text{route},k,K,d,c)$
— instead of the code the search had actually found. The current pipeline
carries the image basis `A` of the exact code from the search stage into the
certification stage (`part6_certification` consumes the row produced by
`part3_search`), and the generator matrices shipped in
`generator_matrices/` are that same object, serialised.

## 6. How to re-certify from scratch

```bash
cd supplementary/scripts
MATRIX_RING_COMP=<repo>/04_COMPUTATION \
    python3 extract_certified_generators.py /tmp/gens
```

This re-runs the census (Part 2), the family scan (Part 3) and the
certification (Part 6) with `SEED = 20261210`, and writes the generator
matrices of all 28 certified codes together with an `INDEX.json`. The
certification table it prints must agree, line for line, with Part 6 of
`logs/phase7_extended_search_log.txt`.

To check a single matrix independently of this code base:

1. Read `generator_matrix_A` (a $k\times N$ matrix over $\mathbb F_q$) and
   `generator_matrix_Euclidean_dual`.
2. Verify $\mathrm{rank}(A)=k$ and that $A$ and the dual matrix are mutually
   orthogonal for the standard Euclidean dot product.
3. Compute $H_E = \dim(D\cap D^{\perp_E})$, then $c=k-h_E$ and $K=N-k-h_E$.
4. Compute $d = \min\{\mathrm{wt}(x): x\in D^{\perp_E}\setminus H_E\}$ by
   complete enumeration of the quotient, or bound it by the support search.
5. Check $K+d\le N+1$ and $N-K+c\ge 2(d-1)$.
6. To confirm which methods ran, apply the rule of Section 3 rather than
   assuming a route-based pattern.
