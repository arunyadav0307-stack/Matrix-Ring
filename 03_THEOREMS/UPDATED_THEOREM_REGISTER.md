# 03 — Updated theorem and claim register (supersedes `theorem_register.md`)

**Status of this revision:** end of the *Phase-0 revision* (Tasks 1–3 complete).
`theorem_register.md` (the original, Phase-0-only version) is **kept unchanged** for the
audit trail; this file supersedes it and is the live register.

**Rule (unchanged, blueprint §8A.7):** every proposed result gets a row; every row states
its assumptions, proof location, dependencies and status; nothing is marked `proved`
unless a complete proof exists in the named file.

## Status vocabulary

* `established (lit)` — imported from the literature, with a citation.
* `proved` — complete proof written in this repository (`03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`).
* `proved (conditional)` — complete proof under explicitly stated extra hypotheses.
* `conjectural` — stated, with a proof sketch; not written out.
* `computational only` — verified by exhaustive/bounded/sampled computation in a stated
  range; **not** a theorem. The range and the completeness label (`[EXH]` / `[SMP]`) are
  mandatory.
* `open` — no claim made.

**Counts after this revision:** 12 proved (in this repo), 2 proved-conditional,
5 established-from-literature, 4 computational-only, 6 open. *(Was: 0 proved.)*

---

## Register

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-001** | $R=M_m(A_t)$ is a finite Frobenius ring; $\Lambda=\lambda\circ\mathrm{tr}$, $\lambda$ = coefficient of $u^{t-1}$, is symmetric, associative, non-degenerate and ideal-catching | $m\ge1,t\ge1,q=p^r$, $X$ central | §1 Lemma 1.4 of `PAIRING_COMPLETE_PROOFS.md` (the $\Lambda$ part); "$R$ is Frobenius" is imported | Wood 1999 (B1) | **proved** ($\Lambda$ part) + `established (lit)` (Frobenius property) | pending | §2.2, §2.6 |
| **T-002** | Entrywise extension of an automorphism of $A_t$ to $M_m(A_t)$ is an automorphism; $\sigma_s(a)=a^{p^s}$ ($u$ fixed) $\in\operatorname{Aut}(A_t)$; $\theta_s=\sigma_s\circ{}^{\mathsf T}$ is an **anti**-automorphism | — | §1 Lemmas 1.1, 1.2 | — | **proved** (+ `computational only` corroboration, 7 parameter sets) | pending | §2.4 |
| **T-003** | $\sigma_s$ is nontrivial $\iff r\nmid s$; order $r/\gcd(r,s)$; no nontrivial field-Frobenius twist when $q=p$ | $q=p^r$ | §1 Lemma 1.1 | T-002 | **proved** | pending | §2.4, §3.1 |
| **T-004** | $R_n\cong M_m(B)$, $B=A_t[X]/\langle X^n-1\rangle$ commutative | $X$ central | — | — | `established (lit)` (standard; $M_m$ of a quotient) | pending | §2.5, §5.1 |
| **T-005** | **Morita classification:** right ideals of $R_n$ ⇄ $B$-submodules of $B^m$; two-sided ideals ⇄ ideals of $B$ | $B$ commutative | standard Morita; coding translation still to be written | T-004 | `established (lit)` + `computational only` (validated at $q=2$, $n=1,3$: two independent enumerations agree, 5 and 35) | pending | §5.2, §5.3 |
| **T-006** | **Failure lemma:** with $\sum_i x_iy_i$ the dual of a **left** module is perfect but the dual of a **right** module need not be | $R$ Frobenius | §5 Prop. 5.1 (+ explicit $M_2(\mathbb F_2)$ counterexample: $C=uR$, $|C\|\|C^\perp|=4\ne16$) | T-001 | **proved** (+ `computational only`: plain size formula fails 8/343, 4/737, 4/144, 2/1200, 2/32) | pending | §3.2 (warning) |
| **T-007** | **$\theta$-duality:** for a right $R$-module $C$, $C^{\perp_s}$ is a right $R$-module and $|C|\cdot|C^{\perp_s}|=|R|^n$ | $\theta_s=\sigma_s\circ{}^{\mathsf T}$ | §3 Thms 3.4, 3.5 | T-001, T-002 | **proved** (+ `computational only`: 343/343, 737/737 ×2, 144/144, 1200/1200 `[SMP]`, 32/32 at $t=2$, 5/5, 35/35) | pending | §3.2–§3.3 |
| **T-008** | **Cyclicity of the $\theta$-dual:** $C$ cyclic ⇒ $C^{\perp_s}$ cyclic | — | §3 Thm 3.7(1) | T-007 | **proved** | pending | §3.4 |
| **T-009** | **Hull theorem:** $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R$-module, cyclic if $C$ is | — | §3 Thm 3.8 | T-007, T-008 | **proved** (structure) | pending | §4.2–§4.4 |
| **T-010** | The $\mathbb F_q$-valued form $[x,y]_s=\Lambda(\sum_i\theta_s(x_i)y_i)$ defines the **same** dual as the $R$-valued one, hence is perfect on right modules | — | §4 Prop. 4.1 | T-001, T-007 | **proved** (supersedes the old "to be re-tested at $n=3$" caveat — now proved for all $n$) | pending | §3.2, §6, §7 |
| **T-011** | Hull-dimension formulas for meaningful families | T-005, T-009 | Phase 4 | T-009 | `open` (hull-dim distributions recorded: $q=4,n=3$: `0:64, 2:144, 4:108, 6:27`) | pending | §4.4 |
| **T-012** | Gray/Bachoc-type map $\Phi$ with a precise duality relation | — | Phase 5 | T-010 | `open` (highest technical risk, R3) | pending | §6 |
| **T-013** | CSS / EAQECC construction from the image hulls; parameter formulas | T-012 | Phase 6 | T-012 | `open` | pending | §7 |
| **T-014** | Quantum Singleton bound and defect analysis for the obtained families | T-013 | Phase 6 | T-013 | `open` | pending | §7.6 |

### New rows added by this revision

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-015** | $\theta_s^2=\sigma_{2s}$; $\theta_s$ is an involution $\iff r\mid 2s$ (**never assumed without check**) | — | §1 Lemma 1.3 | T-002 | **proved** (+ `[EXH]` check on all 65536 elements of $M_2(\mathbb F_4[u]/\langle u^2\rangle)$ at $t=2$; `False` at $q=8$ for $s=1,2$) | pending | §2.4, §3.1 |
| **T-016** | **Double dual:** $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$ for every right $R$-module $C$ | — | §3 Thm 3.6 | T-007 | **proved** (+ `computational only`: 100 % in every run: 343/343, 737/737 (x2), 144/144, 1200/1200 `[SMP]`, 32/32 (`t=2`), 5/5, 35/35) | pending | §3.3 |
| **T-017** | **Reflexivity criterion:** $C\mapsto C^{\perp_s}$ is reflexive (i.e. $(C^{\perp_s})^{\perp_s}=C$ for *all* right $R$-submodules) $\iff r\mid 2s$ | $m\ge2$ | §3 Thm 3.9 (counterexample $W=A_t(e_1+ae_2)$, $a$ not fixed by $\sigma_{2s}$) | T-016 | **proved** (+ `[EXH]`: 343/343 at $q=4$; 144/144, 1200/1200 `[SMP]` at $q=9$; **35/737** at $q=8$) | pending | §3.3, §8 |
| **T-018** | **Enumeration formula ($t=1$):** if $X^n-1=\prod_j f_j$ over $\mathbb F_q[X]$ with $\deg f_j=d_j$, then cyclic codes of length $n$ over $M_m(\mathbb F_q)$ correspond to tuples of subspaces, and $\#\{\text{cyclic codes}\}=\prod_j\sum_{i=0}^{m}\bigl[\begin{smallmatrix}m\\ i\end{smallmatrix}\bigr]_{q^{d_j}}$ | $t=1$, $X$ central, factorization over the **centre** $\mathbb F_q$ | T-004 + T-005 (CRT over $\mathbb F_q[X]$ + Morita) | T-004, T-005 | **proved** (+ `[EXH]` validation: $343=7^3$, $144=12^2$, $5$, $35=5\cdot7$) | pending | §5.2 |
| **T-019** | **Centrality diagnosis:** in the $M_2(\mathbb F_2)$ setting of A1, a triple $(f,g,h)$ with $f,g,h\in\mathbb F_4[X]$ produces a right ideal (reading R1 of their Thm 1) **iff** $f,g,h\in\mathbb F_2[X]=Z(A)[X]$ | $A=M_2(\mathbb F_2)$, $n\in\{1,3\}$ | `04_COMPUTATION/alahmadi_reconciliation.py` §4 | — | `computational only` (**[EXH]** over all $27+3$ triples; 9 vs 0 vs 0 vs 18 at $n=3$, 3 vs 0 vs 0 vs 0 at $n=1$) | **adjudication requested** | §5 (reconciliation) |
| **T-020** | **Exhaustive census for $A=M_2(\mathbb F_2)$:** $n=1$ → 5 cyclic codes (dims $0,2,2,2,4$); $n=3$ → 35 cyclic codes (dims $0{:}1,2{:}3,4{:}6,6{:}15,8{:}6,10{:}3,12{:}1$); the paper form $\sum x_jy_j$ is degenerate there ($\dim C+\dim C^\perp$ not constant), while $\sum x_j^{\mathsf T}y_j$ satisfies $\dim C+\dim C^\perp=12$ for all 35 and admits 3 self-dual codes | $n$ odd | `04_COMPUTATION/alahmadi_reconciliation.py` §2, §5 | — | `computational only` (**[EXH]**, two independent methods) | **adjudication requested** | §5 |
| **T-021** | **Principality:** every right ideal of $R_n$ is principal | $t=1$ **and** $X^n-1$ squarefree over $\mathbb F_q$ ($\gcd(n,p)=1$) | §3 Thm 3.7(3) | T-005 | **proved (conditional)**; **[OPEN]** for $t\ge2$ or $p\mid n$ | pending | §3.4 |
| **T-022** | The $t=2$ case behaves identically: for $R=M_2(\mathbb F_4[u]/\langle u^2\rangle)$, $n=1$, $s=1$, all 32 right ideals satisfy right-module-ness, dual closure, $|C\|\|C^{\perp_s}\|=|R|^n$, hull closure and reflexivity; the plain product pairing fails the size formula 2/32 | — | `04_COMPUTATION/galois_t2_check.py` | T-001–T-003 | `computational only` (**[EXH]** over all 32 codes; the general-$t$ statements are proved in `PAIRING_COMPLETE_PROOFS.md`) | pending | §2, §3 |

---

## Imported established facts (not ours to prove)

| ID | Fact | Source |
|----|------|--------|
| **E-001** | Finite Frobenius rings are the alphabets for which the MacWilliams extension theorem and MacWilliams identities hold; duality is character-theoretic and works for non-commutative rings | Wood 1999 (B1) |
| **E-002** | $M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$, $u^2=0$, $u$ not central; the Bachoc map $\phi(a+ub)=(a+b,b)$ is an isometry onto $\mathbb F_4^2$ (Hamming) | Bachoc 1997 (A9); Alahmadi et al. 2013 (A1) |
| **E-003** | Two-sided ideals of $M_m(B)$ are exactly $M_m(J)$, $J\trianglelefteq B$ | standard (Morita) |
| **E-004** | The Galois inner product $\langle a,b\rangle_h=\sum a_ib_i^{p^h}$ generalises Euclidean ($h=0$) and Hermitian ($h=\ell/2$) | Fan–Zhang 2017 (C1) |
| **E-005** | Right ideals of $M_m(K)$ ($K$ a field) ↔ subspaces of $K^m$; hence $\#=\sum_{i=0}^m\bigl[\begin{smallmatrix}m\\i\end{smallmatrix}\bigr]_K$ | standard (Morita) — basis of T-018, T-020 |

---

## Proof-dependency graph (updated)

```
E-001 ──► T-001 ──┬──► T-006 (plain product fails for right modules)
                  ├──► T-007 (theta duality) ──► T-008 (cyclicity) ──► T-009 (hull)
                  │        │                                              │
                  │        ├──► T-016 (double dual = sigma_{2s} C)         │
                  │        │          └──► T-017 (reflexive iff r | 2s)    │
                  │        └──► T-010 (F_q-valued form) ──► T-012 (Gray) ──► T-013 (quantum) ──► T-014
                  └──────────────────────────────────────────────────────► T-011 (hull dims, open)
T-002 ──► T-003 ──► T-007 ;  T-002 ──► T-015 (theta^2 = sigma_{2s}) ──► T-016
T-004 ──► T-005 ──► T-018 (enumeration) ──► T-021 (principality, conditional)
E-005 ──► T-018, T-020
T-019, T-020, T-022 : computational only (no theorem claimed)
```

---

## Audit checklist for the reviewer

1. **T-017 is the load-bearing new statement.** It says the *only* way to get a reflexive
   Galois duality here is $r\mid2s$, so the project must take $q=p^{2e}$, $s=r/2$. If the
   reviewer believes reflexivity is not required for the intended application (hull-based
   quantum constructions usually need only $\mathrm{Hull}_s(C)$ and a size formula, not
   reflexivity of $C\mapsto C^{\perp_s}$), then the parameter restriction can be relaxed —
   please say so explicitly.
2. **T-018 vs A1's Theorem 1.** Our formula uses the factorization of $X^n-1$ over the
   **centre** $\mathbb F_q$; A1's parametrization uses $\mathbb F_4$-factors. At $n=3$,
   $q=2$ the two give 35 and 27 respectively. We claim no error in A1 (see
   `02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md` §6–§7); we do claim that
   **our** enumeration is correct and doubly validated.
3. **T-021 (principality)** is conditional; no later phase may use "every cyclic code is
   principal" at $t\ge2$ or when $p\mid n$ until it is proved.
4. Everything marked `open` (T-011 … T-014) is out of scope for Phase 0 and must stay so.
