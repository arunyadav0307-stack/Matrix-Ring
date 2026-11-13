# Phase 17 / Task A — The certification logic, stated mathematically

Everything below is read from the committed source
(`PAPER/supplementary/scripts/phase7_extended_search.py`, function
`part6_certification`) and the three method implementations it calls. No
route-based generalisation is used anywhere in this document.

---

## 1. The objects

For a code produced by the search, `part3_search` yields a row $r$ carrying the
image basis $A$ of the Gray image $D=\varphi_n(C)\subseteq\mathbb F_q^N$, with
$d_{\text{rep}} = r[\texttt{"d"}]$ the distance the search found. The
certification stage re-derives the quantum data:

```
De, X, Y, YV, Vgen, c, K = P6.quantum_group_data(F, N, A, kind)
Gd, exd = (A, De) if kind == "DC" else (De, A)
```

so the object under test is the **classical difference set**
$\langle G_d\rangle \setminus \langle \mathrm{exd}\rangle$, whose minimum
Hamming weight equals the quantum distance by the coset-distance theorem
(Theorem 8.1).

## 2. M1 — complete enumeration

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
```

`enum_min_weight` enumerates $\langle G_d\rangle\setminus\langle\mathrm{exd}\rangle$
and returns $(d, \textit{complete})$. `ENUM_CAP = 262144`. If the fast
enumeration does not complete and $\mathrm{char}\,\mathbb F_q \ne 2$, a slower
enumeration is attempted with `slow_cap = 50000`. If neither completes it returns
$(None, False)$.

**M1 is attempted for every certified code.** When `comp1` is true, $d_1$ is the
exact minimum weight — an exhaustive determination, not a bound.

## 3. M2 — increasing-weight support search

```python
d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd, maxw=min(8, max(3, (r["d"] or 0) + 1)))
```

`min_weight_in` iterates $w = 1, 2, \dots, \texttt{maxw}$ and, for each support
$S\subseteq\{1,\dots,N\}$ of size $w$, solves the left-kernel problem "is there a
codeword supported inside $S$?". The first $w$ with a solution is the minimum
weight. It is **exhaustive up to `maxw`**; a return of `None` means "no codeword
of weight $\le\texttt{maxw}$", a rigorous lower bound, never a guess.

M2 shares no code with M1: it is a different algorithm for the same quantity, so
had both been run their agreement would have been a genuine cross-check.

## 4. M3 — ambient quantum search

```python
w3 = 3 if N <= 8 else 2
d3, wit3 = P6.ambient_quantum_search(F, N, YV, Vgen, w3)
```

`ambient_quantum_search` scans the ambient symplectic space $\mathbb F_q^{2N}$
for a vector $(a|b)$ of symplectic weight $w$ that commutes with every stabilizer
(i.e. $a,b\in Y$) but is **not** in $V\oplus V$ (i.e. not both in $\langle V\rangle$).
Crucially the scan runs **$w = 1, 2, \dots, w3$ in increasing order**, so:

| outcome | returned | mathematical content |
|---|---|---|
| a vector found at weight $w$ | $(w, (a,b))$ | every weight $<w$ was exhaustively tested and none qualified, so $d = w$ **exactly** — an independent determination in the quantum language, without passing through the coset-distance theorem |
| nothing found $\le w3$ | $(None, None)$ | the proved statement is $d \ge w3 + 1$ — a **lower bound only** |

## 5. Conditional execution of M2

The entire per-code behaviour is these lines:

```python
d1, comp1 = P6.enum_min_weight(Gd, F, N, exd, cap=ENUM_CAP, slow_cap=50000)
if comp1:
    d2, m2 = None, "n/a (M1 already complete)"
else:
    # M2 is run only when M1 could not finish
    d2, _ = P5.min_weight_in(Gd, F, N, exclude=exd, maxw=...)
w3 = 3 if N <= 8 else 2
d3, wit3 = P6.ambient_quantum_search(F, N, YV, Vgen, w3)
```

Three rules, read literally:

1. **M1 is always attempted.**
2. **M2 executes if and only if M1 did not complete.**
3. **M3 always executes**, independently of M1 and M2.

Hence the number of methods executed per code is **two by construction**, and the
pair is $(M1, M3)$ or $(M2, M3)$. Never $(M1,M2,M3)$; never $(M1,M2)$.

### Skipped versus inapplicable — the distinction matters

A method is **skipped** when the program declines to run it because another
method already settled the question. A method is **inapplicable** when it is
mathematically undefined for the object, or cannot in principle answer the
question.

**M2, for the 24 codes where M1 completed, is *skipped*, not inapplicable.**
M2 is a general, route-independent algorithm: it works over any $\mathbb F_q^N$
difference set, EA included. The pipeline simply does not spend the compute,
because M1 has already produced an exhaustive minimum. Evidence that this is
skipping rather than inapplicability:

* the source branches on `comp1`, **not** on `kind` (the route);
* one of the four codes for which M2 *did* run is **EA** ($[[24,6,4;18]]_9$,
  family $(9,3,2)$);
* therefore "M2 is not applicable to the EA route" is **false**, and any
  route-based statement of the rule is wrong.

By contrast M1, for the 4 codes where it returned `(None, False)`, **did not
complete**: it was attempted and its enumeration cap was insufficient. That is a
computational limit of the method on that object, not a routing decision.

## 6. Exact-distance certification

The exact distance of each code rests on **exactly one** of M1 and M2 — whichever
ran:

| method ran | codes | what is established |
|---|---|---|
| M1 completed | 24 | $d = \min \mathrm{wt}(\langle G_d\rangle\setminus\langle\mathrm{exd}\rangle)$ by complete enumeration |
| M2 ran | 4 | the same minimum, by exhaustive support search up to `maxw` |

The `agree` flag requires `d1 == rep` (when M1 completed) and `d2 == rep` (when
M2 ran), so the method's value is checked against the search's value; it does not
merely assert it.

## 7. Lower-bound certification

M3 supplies a lower bound for the 17 codes where it returns `None`: the proved
statement is $d\ge w3+1$, i.e. $d\ge3$ for $w3=2$ (16 codes) or $d\ge4$ for
$w3=3$ (1 code, $[[8,2,4;6]]_9$ at $N=8$). These are consistent with, but weaker
than, the exact values from M1/M2. **They corroborate; they do not determine.**

## 8. Independent cross-checks

M3 is the cross-check, and it is **genuinely independent** of M1/M2: it works in
the ambient symplectic space $\mathbb F_q^{2N}$ and does not use the
coset-distance theorem, whereas M1/M2 work in the classical difference set. That
independence holds for all 28 codes. What is **not uniform is its strength**:

| M3 outcome | codes | nature of the cross-check |
|---|---|---|
| returned a value $= d$ | **11** | a second, independent **exact** determination |
| returned `None` | **17** | an independent **lower bound**, consistent with $d$ |

All 11 exact cases satisfy `M3 == d`; all 17 lower-bound cases satisfy `d > w3`
(verified individually, 0 exceptions).

---

## 9. Confirmed distribution

| | count |
|---|---|
| M1 + M3 | **24** |
| M2 + M3 | **4** |
| M3 exact | **11** |
| M3 lower bound | **17** |
| **three methods completed** | **0** |
| total codes | 28 |

Verified against four independent sources — the source code, Part 6 of the Phase 7
log, `certified_codes.csv`, and the 28 generator-matrix records — with **0
discrepancies**. Per-code table:
`PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_28_CODE_APPLICABILITY_TABLE.csv`.
