# 03 — Theorem and claim register (blueprint §10)

**Rule (blueprint §8A.7):** every proposed result gets a row; every row states
its assumptions, proof location, dependencies and status; nothing is marked
`proved` unless a complete proof exists in the named file.

**Current state (end of Phase 0):** 0 proved results, 4 established facts
imported from the literature, 10 proposed results (all `conjectural` or
`computational only`). This is expected at Phase 0 — the blueprint forbids
proving later-phase results in Phase 0.

## Status vocabulary
* `established (lit)` — imported, with a citation.
* `proved` — complete proof written in this repository.
* `conjectural` — stated, with a proof sketch; not yet written out.
* `computational only` — verified by exhaustive computation in a stated range;
  **not** a theorem.
* `open` — no claim made.

---

## Register

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-001** | $R=M_m(A_t)$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$, is a finite **Frobenius** ring; $\Lambda=\lambda\circ\mathrm{tr}$ with $\lambda$ = coefficient of $u^{t-1}$ is a symmetric, associative, non-degenerate $\mathbb F_q$-bilinear form (a Frobenius functional) | $m\ge1,t\ge1,q=p^r$ | Phase 1 (to write); evidence `04_COMPUTATION/phase0_results.txt` §E2 | Wood 1999 (B1) | `conjectural` (proof straightforward) + `computational only` for $(q,t,m)\in\{(2,1,2),(4,1,2),(2,2,2),(4,2,2),(16,1,2),(2,1,3)\}$ | pending | §2.2, §2.6 |
| **T-002** | Entrywise extension of a ring automorphism $\sigma$ of $A_t$ to $M_m(A_t)$ is a ring automorphism; entrywise $\sigma_s(a)=a^{p^s}$ (u fixed) is an automorphism of $A_t$; $\theta_s=\sigma_s\circ{}^{\mathsf T}$ is an **anti**-automorphism | — | Phase 1; evidence §E1 | — | `conjectural` + `computational only` (6 parameter sets, randomised 400 trials) | pending | §2.4 |
| **T-003** | $\sigma_s$ is **nontrivial** iff $r\nmid s$; in particular there is no nontrivial field-Frobenius twist when $q=p$ | $q=p^r$ | Phase 1; evidence §E1 | T-002 | `conjectural` + `computational only` | pending | §2.4, §3.1 |
| **T-004** | $R_n:=R[X]/\langle X^n-1\rangle\cong M_m(B)$ with $B=A_t[X]/\langle X^n-1\rangle$ **commutative** | $X$ central | Phase 2 | — | `conjectural` (standard) | pending | §2.5, §5.1 |
| **T-005** | **Morita classification:** left ideals of $R_n$ ⇄ $B$-submodules of $B^m$ (rows); right ideals ⇄ $B$-submodules of $B^m$ (columns); two-sided ideals ⇄ ideals of $B$ | $B$ commutative | Phase 2 | T-004 | `conjectural` (standard Morita theory; coding translation to be written) + `computational only` at $(m,q,t,n)=(2,2,1,3)$: 35 / 35 / 4 | pending | §5.2, §5.3 |
| **T-006** | **Failure lemma:** with the ring-valued pairing $\sum_ix_iy_i$, the dual of a **left** $R$-module $C\subseteq R^n$ is perfect ($|C||C^\perp|=|R|^n$) but the dual of a **right** $R$-module need not be | $R$ Frobenius | Phase 1/3; evidence §E3, §E4 (31 of 35 cyclic codes broken) | T-001 | `conjectural` + `computational only` | pending | §3.2 (warning section) |
| **T-007** | **$\theta$-duality theorem:** for $C$ a right $R$-module, $C^{\perp_s}:=\{y:\sum_i\theta_s(x_i)y_i=0\ \forall x\in C\}$ is again a **right** $R$-module and $|C|\cdot|C^{\perp_s}|=|R|^n$ | $\theta_s=\sigma_s\circ{}^{\mathsf T}$ | Phase 1/3; evidence §E3, §E4 (0 of 35 broken) | T-001, T-002 | `conjectural` + `computational only` | pending | §3.2–§3.3 |
| **T-008** | **Cyclicity of the $\theta$-dual:** if $C$ is cyclic (right ideal) then $C^{\perp_s}$ is cyclic | — | Phase 3 | T-007 | `conjectural` (shift commutes entrywise with $\theta_s$) | pending | §3.4 |
| **T-009** | **Hull theorem:** $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R$-module, hence cyclic; $\dim_{\mathbb F_q}\mathrm{Hull}_s(C)$ computable from generator/Hermite data over $A_t$ | — | Phase 4; evidence §E4 (right module in 35/35 cases) | T-007, T-008, T-005 | `conjectural` + `computational only` | pending | §4.2–§4.4 |
| **T-010** | $\mathbb F_q$-valued version $[x,y]_s=\Lambda(\sum_i\theta_s(x_i)y_i)$ gives a perfect duality with a right-module dual (needed for the quantum step) | — | Phase 3; evidence §E3 | T-001, T-007 | `conjectural` + `computational only` ($n=1$ only — **to be re-tested at $n=3$ in Phase 1**) | pending | §3.2, §6, §7 |
| **T-011** | Hull-dimension formulas for meaningful families (analogue of the lcm/gcd formulas of the commutative case) | T-005, T-009 | Phase 4 | T-009 | `open` | pending | §4.4 |
| **T-012** | Gray/Bachoc-type map $\Phi:R^n\to\mathbb F_q^N$ with $\Phi(C^{\perp_s})=\Phi(C)^{\perp}$ (or a precise non-preservation statement) | — | Phase 5 | T-010 | `open` (highest technical risk, see R3) | pending | §6 |
| **T-013** | CSS / EAQECC construction from the image hulls; parameter formulas | T-012 | Phase 6 | T-012 | `open` | pending | §7 |
| **T-014** | Quantum Singleton bound $2d\le n-K+2$ and defect $\delta=n+2-K-2d$ analysis for the obtained families | T-013 | Phase 6 | T-013 | `open` | pending | §7.6 |

---

## Imported established facts (not ours to prove)

| ID | Fact | Source |
|----|------|--------|
| **E-001** | Finite Frobenius rings are the alphabets for which the MacWilliams extension theorem and MacWilliams identities hold; duality is character-theoretic and works for non-commutative rings | Wood 1999 (B1) |
| **E-002** | $M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$, $u^2=0$; the Bachoc map $\phi(a+ub)=(a+b,b)$ is an isometry onto $\mathbb F_4^2$ with the Hamming metric and is compatible with Hermitian duality | Bachoc 1997 (A9); Alahmadi et al. 2013 (A1), Prop. 2 |
| **E-003** | Two-sided ideals of $M_m(B)$ are exactly $M_m(J)$, $J\trianglelefteq B$ | standard (Morita) |
| **E-004** | The Galois inner product $\langle a,b\rangle_h=\sum a_ib_i^{p^h}$ over $\mathbb F_{p^\ell}$ generalises Euclidean ($h=0$) and Hermitian ($h=\ell/2$) | Fan–Zhang 2017 (C1) |

---

## Proof-dependency graph (as it stands)

```
E-001 ──► T-001 ──┬──► T-006 (failure lemma)
                  ├──► T-007 (theta duality) ──► T-008 (cyclicity) ──► T-009 (hull)
                  └──► T-010 (F_q-valued form) ──► T-012 (Gray map) ──► T-013 (quantum) ──► T-014
T-002 ──► T-003, T-007
T-004 ──► T-005 ──► T-009, T-011
```

## Audit column
To be filled in by ChatGPT after each phase (blueprint §8B). Nothing in this
register has been independently audited yet.
