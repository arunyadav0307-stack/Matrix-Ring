# Phase 17 / Task D — Methodological note for a referee

A short, self-contained account of how the 28 quantum-code distances were
certified. It deliberately claims **no more** verification independence than the
algorithms support.

---

## 1. What is certified, and by what

For each of the 28 headline codes the pipeline re-derives the quantum data from
the exact code found by the search (the image basis is carried through; no code
is re-selected by invariants). The quantum distance equals the minimum Hamming
weight of a **classical difference set**
$\langle G_d\rangle\setminus\langle\mathrm{exd}\rangle$, by the coset-distance
theorem (Theorem 8.1 of the manuscript). Three methods are available:

| | what it does | works in |
|---|---|---|
| **M1** complete enumeration | enumerates the difference set exhaustively | the classical difference set |
| **M2** support search | for $w=1,2,\dots$ and each support of size $w$, solves a left-kernel problem | the classical difference set |
| **M3** ambient quantum search | searches for an undetectable error in increasing symplectic weight | the ambient symplectic space $\mathbb F_q^{2N}$ |

M3 is structurally independent of M1 and M2: it never uses the coset-distance
theorem, and it works in a different space. That independence is real and is
claimed for all 28 codes.

## 2. Why the three methods are not all run for every code

Because **M2 is a fallback for M1, not a third opinion**. The source is explicit:

```python
d1, comp1 = enum_min_weight(Gd, F, N, exd, cap=262144, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"
else:
    d2, _ = min_weight_in(Gd, F, N, exclude=exd, maxw=...)
w3 = 3 if N <= 8 else 2
d3, _ = ambient_quantum_search(F, N, YV, Vgen, w3)
```

M1 is tried first. When it finishes, the minimum weight is already established
exhaustively, and running M2 — a different algorithm for the **same** quantity —
would add nothing. M3 is then run instead, because it operates in a genuinely
different space and so *does* add something. When M1 cannot finish, M2 is the
method that recovers an exact answer.

Consequently **exactly two methods run per code**: $(M1, M3)$ for 24 codes and
$(M2, M3)$ for 4. **No code has all three.** This is a property of the design,
not an omission.

### A point of terminology

For the 24 codes where M1 completed, M2 is **skipped**, not inapplicable. M2 is a
general, route-independent algorithm; the program simply does not spend the
compute. Evidence: the branch is on `comp1`, not on the route; and one of the
four codes for which M2 *did* run is entanglement-assisted. Any route-based
account of which method ran is therefore wrong.

## 3. Why the conditional procedure is appropriate

* It is **not** a weaker certification than running all three would be. For the
  24 M1 codes, M1 is exhaustive — there is no residual uncertainty for M2 to
  remove.
* The compute saved is spent on M3, which is the only **structurally independent**
  check available and therefore the one that adds information.
* Where M1 fails, no exact answer would exist at all without M2. Running M2
  conditionally is what makes an exact distance available for all 28 codes.

## 4. Exact distance versus lower bound

The manuscript never conflates them, and the tables record which is which.

* **Exact** comes from M1 (complete enumeration, 24 codes) or M2 (exhaustive
  support search, 4 codes). In both cases the reported value is a two-sided
  determination: a codeword of that weight is exhibited, and no codeword of
  smaller weight exists.
* **M3** scans symplectic weights $1,2,\dots,w3$ in increasing order, so:
  * if it finds a vector at weight $w$, then $d=w$ **exactly** — all smaller
    weights were exhaustively tested — giving an independent exact determination
    (**11 codes**);
  * if it finds nothing, the proved statement is only $d\ge w3+1$ (**17 codes**),
    a corroborating lower bound.

So the cross-check supplied by M3 is **not uniform**: exact for 11 codes, a lower
bound for 17. Every one of the 28 rows records which applies.

## 5. What is *not* claimed

* Not claimed: that three independent methods verified every code. Zero codes
  have three methods.
* Not claimed: that M1 and M2 agree. They never run on the same code.
* Not claimed: that M3 determines the distance for all codes. It does so for 11.
* Not claimed: any record quantum parameter. Every stabilizer code whose
  parameters can be compared with the literature is at best equal to the best
  known distance.

## 6. How the 28 records permit independent reproduction

Every claim above is checkable from shipped artefacts, without trusting this
note:

1. **Per-code table.** `parameter_tables/certified_codes.csv` — columns `M1`,
   `M2`, `M3_lower_bound`. A number in M1 means M1 completed and M2 is `n/a`; a
   dash in M1 means M2 ran. A bare number in M3 is exact; `$>2$' / `$>3$' is a
   lower bound.
2. **Execution log.** Part 6 of `logs/phase7_extended_search_log.txt`
   (lines 449–478) prints one row per code with the same three columns.
3. **Source.** `scripts/phase7_extended_search.py::part6_certification`
   (lines 1670–1681) is the authority on what ran.
4. **Generator matrices.** `generator_matrices/*.json` carry
   `generator_matrix_A`, `generator_matrix_Euclidean_dual`, $k,K,d,c,h_E$ and
   `distance_method`; step 6 of the re-certification procedure recomputes $d$
   from them independently of this code base.
5. **Reconstruction.**
   `PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`
   tabulates all 28 rows against all four sources above, with 0 discrepancies.

### Locations

| artefact | path |
|---|---|
| corrected certification procedure | `PAPER/SUPPLEMENTARY_V2/CERTIFICATION_PROCEDURE.md` |
| original scripts | `PAPER/supplementary/scripts/` (preserved; also in `SUPPLEMENTARY_V2/`) |
| original logs | `PAPER/supplementary/logs/` (preserved; also in `SUPPLEMENTARY_V2/`) |
| generator matrices | `PAPER/supplementary/generator_matrices/` (preserved; also in `SUPPLEMENTARY_V2/`) |
| parameter tables | `PAPER/supplementary/parameter_tables/` (preserved; also in `SUPPLEMENTARY_V2/`) |
| supersession record | `PAPER/SUPPLEMENTARY_V2/SUPPLEMENTARY_CORRECTION_NOTE.md` |

To re-run everything from scratch:

```sh
cd PAPER/SUPPLEMENTARY_V2/scripts
MATRIX_RING_COMP=<repo>/04_COMPUTATION python3 extract_certified_generators.py /tmp/gens
```

This re-runs the census, the family scan and the certification with
`SEED = 20261210`, and must reproduce Part 6 of the log line for line — including
the `n/a` entries in column M2, which are a consequence of the conditional logic
and not a defect.

## 7. One caveat, stated plainly

Line 478 of the Phase 7 log, check `[EXH] E1`, reads *"every headline code is
certified by the three independent methods…"*. That wording is **wrong** for the
reason given in §2. It is a historical record of what the program printed and has
deliberately **not** been rewritten, so that the origin of the claim remains
auditable. The corrected procedure document flags it explicitly.
