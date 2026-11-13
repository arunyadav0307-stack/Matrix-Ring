# What "certified" means here, and how to re-certify a code

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

## 3. The three methods

Every headline code is certified by three structurally different methods.

### M1 — complete enumeration

Enumerate the relevant classical difference set completely and take the
minimum weight. Complete when $q^{\dim}\le 3\cdot10^6$ (the constant
`ENUM_CAP = 262144` in the script bounds a single complete enumeration of a
code; the difference-set enumerations quoted as complete are those for which
the enumeration finished within that cap). Output: exact.

### M2 — increasing-weight support search

A different algorithm. For each support $S\subseteq\{1,\dots,N\}$ of size
$w=1,2,3,\dots$ in increasing order, solve the left-kernel problem "does the
difference set contain a vector supported inside $S$?". The first $w$ at
which a solution exists is the distance. Because M2 shares no code with M1,
agreement between them is a genuine cross-check and not a tautology.

### M3 — ambient quantum search

Search the ambient symplectic space $\mathbb F_q^{2N}$ in increasing
symplectic weight for a vector $v$ with $v\in V^{\perp_\omega}$ and
$v\notin V$. This certifies the distance in the quantum language directly,
without passing through the coset-distance theorem. It is complete only up
to the weight reached, and is reported as a **lower bound** otherwise: the
table entry `$>2$' means "no vector of symplectic weight $\le 2$ was found",
i.e. $d\ge3$ as a proved lower bound.

### Additional checks

For every certified code the pipeline also verifies:

* the stabilizer group is abelian **on an $\mathbb F_p$-basis** (Theorem 7.3
  of the manuscript; testing on an $\mathbb F_q$-generating set is invalid
  and yields $d=1$ instead of $d=3$ for $[[16,4,3]]_4$);
* $K$ and $c$ recompute from $k$ and $h_E$ via $c=k-h_E$ and $K=N-k-h_E$;
* the entanglement-assisted Singleton and Hamming bounds hold (check G1,
  0 violations on all $5\,055$ codes);
* the coset Singleton bound $K+d\le N+1$ holds (check H1, 0 violations).

## 4. The defect that was found and fixed, and why it cannot recur

An earlier version of this project certified a code that was *re-selected by
invariants* — a different code with the same $(q,t,n,N,\text{route},k,K,d,c)$
— instead of the code the search had actually found. The current pipeline
carries the image basis `A` of the exact code from the search stage into the
certification stage (`part6_certification` consumes the row produced by
`part3_search`), and the generator matrices shipped in
`generator_matrices/` are that same object, serialised.

## 5. How to re-certify from scratch

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
