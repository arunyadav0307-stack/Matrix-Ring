# 03 — Updated theorem and claim register (supersedes `theorem_register.md`)

**Status of this revision:** post **independent self-audit** of the Phase-0 revision
(Tasks 1–3). `theorem_register.md` (the original, Phase-0-only version) is **kept
unchanged** for the audit trail; this file supersedes it and is the live register.

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
* `needs correction` — the register previously recorded this incorrectly; see the note.

**Counts after the audit:** 12 proved (in this repo), 2 proved-conditional,
9 established-from-literature, 6 computational-only, 6 open, 3 corrected.
*(Was, after the Phase-0 revision: 12 proved, 2 conditional, 5 lit, 4 computational, 6 open.)*

**Counts after Phase 1** (rows T-030 … T-043 added below): 22 proved, 3
proved-conditional, 9 established-from-literature, 7 computational-only, 7 open,
4 corrected.

---

## Register

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-001** | $R=M_m(A_t)$ is a finite Frobenius ring; $\Lambda=\lambda\circ\mathrm{tr}$, $\lambda$ = coefficient of $u^{t-1}$, is symmetric, associative, non-degenerate and ideal-catching | $m\ge1,t\ge1,q=p^r$, $X$ central | §1 Lemma 1.4 of `PAIRING_COMPLETE_PROOFS.md` (the $\Lambda$ part); "$R$ is Frobenius" is imported | Wood 1999 (B1) | **proved** ($\Lambda$ part) + `established (lit)` (Frobenius property) | **confirmed** (Gram rank of $\Lambda(XY)$ full: 4/4 at $t=1$, 8/8 at $t=2$) | §2.2, §2.6 |
| **T-002** | Entrywise extension of an automorphism of $A_t$ to $M_m(A_t)$ is an automorphism; $\sigma_s(a)=a^{p^s}$ ($u$ fixed) $\in\operatorname{Aut}(A_t)$; $\theta_s=\sigma_s\circ{}^{\mathsf T}$ is an **anti**-automorphism | — | §1 Lemmas 1.1, 1.2 | — | **proved** (+ `computational only` corroboration, 7 parameter sets) | **confirmed**; **hidden assumption now recorded:** $\mathrm{Aut}(A_t)\supsetneq\{\sigma_s\}$ (an automorphism may move $u$); we use only the coefficient-Frobenius subgroup. Everything generalises to $\tau\in\mathrm{Aut}(A_t)$ with $\theta_\tau=\tau\circ{}^{\mathsf T}$, $\theta_\tau^2=\tau^2$ (T-027) | §2.4 |
| **T-003** | $\sigma_s$ is nontrivial $\iff r\nmid s$; order $r/\gcd(r,s)$; no nontrivial field-Frobenius twist when $q=p$ | $q=p^r$ | §1 Lemma 1.1 | T-002 | **proved** | **confirmed** (q=4: all 256² pairs; q=8 sampled 4000) | §2.4, §3.1 |
| **T-004** | $R_n\cong M_m(B)$, $B=A_t[X]/\langle X^n-1\rangle$ commutative | $X$ central | — | — | `established (lit)` | **confirmed** | §2.5, §5.1 |
| **T-005** | **Morita classification:** right ideals of $R_n$ ⇄ $B$-submodules of $B^m$; two-sided ideals ⇄ ideals of $B$ | $B$ commutative | standard Morita; coding translation still to be written | T-004 | `established (lit)` + `computational only` (validated at $q=2$, $n=1,3$: two independent enumerations agree, 5 and 35) | **confirmed and strengthened:** at $q=2,n=3$ the CRT+Morita prediction ($R_3\cong M_2(\mathbb F_2)\times M_2(\mathbb F_4)$, dims $2v_1+4v_2$) reproduces the enumerated distribution `[(0,1),(2,3),(4,6),(6,15),(8,6),(10,3),(12,1)]` **exactly** | §5.2, §5.3 |
| **T-006** | **Failure lemma:** with $\sum_i x_iy_i$ the dual of a **left** module is perfect but the dual of a **right** module need not be | $R$ Frobenius | §5 Prop. 5.1 (+ explicit $M_2(\mathbb F_2)$ counterexample: $C=uR$, $\lvert C\rvert\lvert C^\perp\rvert=4\ne16$) | T-001 | **proved** (+ `computational only`: plain size formula fails 8/343, 4/737, 4/144, 2/1200, 3/33) | **confirmed** | §3.2 (warning) |
| **T-007** | **$\theta$-duality:** for a right $R$-module $C$, $C^{\perp_s}$ is a right $R$-module and $\lvert C\rvert\cdot\lvert C^{\perp_s}\rvert=\lvert R\rvert^n$ | $\theta_s=\sigma_s\circ{}^{\mathsf T}$ | §3 Thms 3.4, 3.5 | T-001, T-002 | **proved** (+ `computational only`: 343/343, 737/737 ×2, 144/144, 5000/5000 `[SMP]`, **33/33** at $t=2$, 5/5, 7/7, 11/11, 12/12, 35/35) | **confirmed**; size formula *proved* (non-degeneracy + dimension count), 6 961/6 961 on supplied code paths | §3.2–§3.3 |
| **T-008** | **Cyclicity of the $\theta$-dual:** $C$ cyclic ⇒ $C^{\perp_s}$ cyclic | — | §3 Thm 3.7(1) | T-007 | **proved** | **confirmed**, with a shorter direct proof: $B_s(x,Ty)=B_s(T^{-1}x,y)$, so $C^{\perp_s}$ is shift-invariant (no Morita needed) | §3.4 |
| **T-009** | **Hull theorem:** $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R$-module, cyclic if $C$ is | — | §3 Thm 3.8 | T-007, T-008 | **proved** (structure) | **confirmed**; intersection of right ideals of $R_n$ is a right ideal — *no* principality needed. Computation note: the hull must be obtained as the nullspace of the Gram matrix $G_{ji}=B_s(c_j,c_i)$, **not** as the span of the basis vectors of $C$ lying in $C^{\perp_s}$ | §4.2–§4.4 |
| **T-010** | The $\mathbb F_q$-valued form $[x,y]_s=\Lambda(\sum_i\theta_s(x_i)y_i)$ defines the **same** dual as the $R$-valued one, hence is perfect on right modules | — | §4 Prop. 4.1 | T-001, T-007 | **proved** | **confirmed with a cleaner proof:** $C^{\perp,R}\subseteq C^{\perp,\mathbb F_q}$ trivially, and both have dimension $N-\dim C$ (non-degeneracy for the trace form; size formula for the $R$-valued one) ⇒ equal. Verified **6 961/6 961** (code, $s$) instances. The slot convention (θ in the first or the second argument) is immaterial — both were tested | §3.2, §6, §7 |
| **T-011** | Hull-dimension formulas for meaningful families | T-005, T-009 | Phase 4 | T-009 | `open` (hull-dim distributions recorded: $q=4,n=3$: `0:64, 2:144, 4:108, 6:27`; $q=4,t=2$: `0:?`; $q=2,n=3$ Euclidean: `0:16, 2:4, 4:12, 6:3`) | unchanged | §4.4 |
| **T-012** | Gray/Bachoc-type map $\Phi$ with a precise duality relation | — | Phase 5 | T-010 | `open` (highest technical risk, R3) | unchanged | §6 |
| **T-013** | CSS / EAQECC construction from the image hulls; parameter formulas | T-012 **and** reflexivity ($r\mid 2s$) unless derived by direct counting | Phase 6 | T-012 | `open` | **new caveat:** see U9 decision — prove in the reflexive regime; a non-reflexive derivation must avoid any $C^{\perp\perp}$ step | §7 |
| **T-014** | Quantum Singleton bound and defect analysis for the obtained families | T-013 | Phase 6 | T-013 | `open` | unchanged | §7.6 |

### Rows added by the Phase-0 revision (audit outcomes appended)

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-015** | $\theta_s^2=\sigma_{2s}$; $\theta_s$ is an involution $\iff r\mid 2s$ (**never assumed without check**) | — | §1 Lemma 1.3 | T-002 | **proved** (+ `[EXH]` check on all 256 elements of $M_2(\mathbb F_4[u]/\langle u^2\rangle)$; `False` at $q=8$ for $s=1,2$) | **confirmed** | §2.4, §3.1 |
| **T-016** | **Double dual:** $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$ for every right $R$-module $C$ | — | §3 Thm 3.6; alternative proof from the identity $\theta_s(B_s(x,y))=B_s(y,\sigma_{2s}x)$ | T-007, T-015 | **proved** (+ `computational only`: 343/343, 737/737 ×2, 144/144, 5000/5000 `[SMP]`, **33/33** ($t=2$), 5/5, 35/35) | **confirmed**; cleaner proof: inclusion from the key identity + dimension count from the size formula. Verified 100 % **including at $q=8$ where $\sigma_{2s}\ne\mathrm{id}$** | §3.3 |
| **T-017** | **Reflexivity criterion:** $C\mapsto C^{\perp_s}$ is reflexive (i.e. $(C^{\perp_s})^{\perp_s}=C$ for *all* right $R$-submodules) $\iff r\mid 2s$ | $m\ge2$ | §3 Thm 3.9 (counterexample $W=A_t(e_1+ae_2)$, $a$ not fixed by $\sigma_{2s}$) | T-016 | **proved** (+ `[EXH]`: 343/343 at $q=4$; 144/144, 5000/5000 `[SMP]` at $q=9$; **35/737** at $q=8$) | **confirmed, with two clarifications now mandatory:** (i) $m\ge2$ is *essential* — for $m=1$ every ideal of $A_t$ is $\sigma$-invariant, so the duality is always reflexive; (ii) "$r\nmid 2s$" does **not** mean "no code is reflexive": 35 of 737 codes at $q=8$ satisfy $\sigma_{2s}(C)=C$ | §3.3, §8 |
| **T-018** | **Enumeration formula ($t=1$):** if $X^n-1=\prod_j f_j$ over $\mathbb F_q[X]$ with $\deg f_j=d_j$, then cyclic codes of length $n$ over $M_m(\mathbb F_q)$ correspond to tuples of subspaces, and $\#\{\text{cyclic codes}\}=\prod_j\sum_{i=0}^{m}\bigl[\begin{smallmatrix}m\\ i\end{smallmatrix}\bigr]_{q^{d_j}}$ | $t=1$, $X$ central, factorization over the **centre** $\mathbb F_q$, **and $X^n-1$ squarefree** (equivalently $\gcd(n,p)=1$) | T-004 + T-005 (CRT over $\mathbb F_q[X]$ + Morita) | T-004, T-005 | **proved (conditional)** — **hypothesis added by the audit** | **corrected (F-04):** the squarefree hypothesis is essential. Counterexample $q=4$, $n=2$, $m=2$: $X^2-1=(X+1)^2$, the formula predicts $49=(1+5+1)^2$, the true count is **33**. Validated where it applies: $343=7^3$, $144=12^2$, $5$, $35=5\cdot7$ | §5.2 |
| **T-019** | **Centrality diagnosis:** in the $M_2(\mathbb F_2)$ setting of A1, a triple $(f,g,h)$ with $f,g,h\in\mathbb F_4[X]$ produces a right ideal (reading R1 of their Thm 1) **iff** $f,g,h\in\mathbb F_2[X]=Z(A)[X]$ | $A=M_2(\mathbb F_2)$, $n\in\{1,3\}$ | `04_COMPUTATION/alahmadi_reconciliation.py` §4 | — | `computational only` (**[EXH]** over all $27+3$ triples; 9 vs 0 vs 0 vs 18 at $n=3$, 3 vs 0 vs 0 vs 0 at $n=1$) | **adjudication requested (U8)**; see `06_AUDIT/PHASE0_U8_U9_DECISIONS.md` | §5 (reconciliation) |
| **T-020** | **Exhaustive census for $A=M_2(\mathbb F_2)$:** $n=1$ → 5 cyclic codes (dims $0,2,2,2,4$); $n=3$ → 35 cyclic codes (dims $0{:}1,2{:}3,4{:}6,6{:}15,8{:}6,10{:}3,12{:}1$); the paper form $\sum x_jy_j$ is degenerate there ($\dim C+\dim C^\perp$ not constant), while $\sum x_j^{\mathsf T}y_j$ satisfies $\dim C+\dim C^\perp=12$ for all 35 and admits **3** self-dual codes | $n$ odd | `04_COMPUTATION/alahmadi_reconciliation.py` §2, §5; re-derived independently in `04_COMPUTATION/u8_n3_selfdual_check.py` | — | `computational only` (**[EXH]**, three independent routes) | **confirmed and extended:** (i) the 35 and their dimension distribution are now *predicted* by CRT+Morita and matched exactly; (ii) the 3 self-dual codes are exhibited explicitly; (iii) with the paper's form $\sum x_j y_j$ there are **0** self-dual codes and $\dim C+\dim C^\perp$ takes the values `[(6,15),(8,10),(10,6),(12,4)]`; (iv) the **quaternary** family (A1's $F_4$-correspondence, 8 codes, dims $0,4,4,4,8,8,8,12$) contains **no** non-zero self-orthogonal and **no** self-dual code — this is what A1's "8" counts | §5 |
| **T-021** | **Principality:** every right ideal of $R_n$ is principal | $t=1$ **and** $X^n-1$ squarefree over $\mathbb F_q$ ($\gcd(n,p)=1$) | §3 Thm 3.7(3) | T-005 | **proved (conditional)**; **[OPEN]** for $t\ge2$ or $p\mid n$ | unchanged; the audit adds the warning that at $q=4,n=2$ the ring $B=\mathbb F_4[\varepsilon]/\langle\varepsilon^2\rangle$ is a chain ring whose submodule lattice is strictly richer than a product of subspace lattices | §3.4 |
| **T-022** | The $t=2$ case behaves identically: for $R=M_2(\mathbb F_4[u]/\langle u^2\rangle)$, $n=1$, $s=1$, all right ideals satisfy right-module-ness, dual closure, $\lvert C\rvert\lvert C^{\perp_s}\rvert=\lvert R\rvert^n$, hull closure and reflexivity; the plain product pairing fails the size formula 2/33 | — | `04_COMPUTATION/galois_t2_check.py` | T-001–T-003 | `computational only` (**[EXH]**) | **CORRECTED (F-03):** the supplied script omitted the zero submodule (it skipped zero vectors and never seeded `seen`), reporting **32**; the correct count is **33**, with $F_q$-dim distribution `[(0,1),(2,5),(4,21),(6,5),(8,1)]`, and all checks now read **33/33**. Structurally confirmed: right ideals of $M_2(A)$, $A=\mathbb F_q[u]/\langle u^2\rangle$, ↔ $A$-submodules of $A^2$, counted as $1+(q+1)+(q^2+q+1)+(q+1)+1=q^2+3q+5=33$ for $q=4$ | §2, §3 |
| **T-023** (new) | **Key identity:** $\theta_s\big(B_s(x,y)\big)=B_s\big(y,\sigma_{2s}(x)\big)$, where $B_s(x,y)=\sum_e\theta_s(x_e)y_e$. Hence $B_s(x,y)=0\iff B_s(y,\sigma_{2s}x)=0$, and $B_s$ is symmetric **iff** $\sigma_{2s}=\mathrm{id}$ | — | `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` §3 | T-002, T-015 | **proved** | new; consequence: for $r\nmid 2s$ the self-orthogonality shortcut "$G\theta_s(G)^{\mathsf T}=0$" (checking only $i\le j$) is **invalid** — all ordered pairs must be tested | §3.1 |
| **T-024** (new) | **Semilinear isometry:** for every $k$, $B_s(\sigma_kx,\sigma_ky)=\sigma_k\big(B_s(x,y)\big)$; orthogonality and Hamming weight are preserved; $\sigma_k(C^{\perp_s})=(\sigma_kC)^{\perp_s}$; $\mathrm{Hull}_s(\sigma_kC)=\sigma_k\,\mathrm{Hull}_s(C)$ | — | `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` §8; verified in `04_COMPUTATION/audit_pairing_equivalence.py` | T-002, T-007 | **proved** (+ `computational only`: E1–E3 300/300 random pairs per parameter set; E4, E5 343/343, 737/737 ×2, 144/144, 5000/5000) | new; this is what settles **U9** | §3.1, §8 |
| **T-025** (new) | **Parameter invariance in the non-reflexive regime:** if $r\nmid 2s$ then $C^{\perp_s\perp_s}=\sigma_{2s}(C)\ne C$ in general, but $C^{\perp_s\perp_s}$ has the **same size, weight enumerator, minimum distance and hull dimension** as $C$ | — | immediate from T-016 + T-024 | T-016, T-024 | **proved** | new; the reason reflexivity is *not* needed for hull-based parameter counting, and the reason it *is* needed for $C^{\perp\perp}$-style proofs | §8 (U9) |
| **T-026** (new) | **Non-squarefree counterexample:** at $q=4$, $n=2$, $m=2$ ($X^2-1=(X+1)^2$) there are exactly **33** cyclic codes, not the $49$ predicted by T-018's squarefree formula | $p\mid n$ | `04_COMPUTATION/independent_audit_checks.py` §C | T-005 | `computational only` (**[EXH]**) | new; the same 33 arises as the $t=2$ count of T-022, since $\mathbb F_4[X]/\langle(X+1)^2\rangle\cong\mathbb F_4[u]/\langle u^2\rangle$ — two independent derivations of one number | §5.2 (warning) |
| **T-027** (new) | **Generality of the framework:** for any $\tau\in\operatorname{Aut}(A_t)$, $\theta_\tau=\tau\circ{}^{\mathsf T}$ is an anti-automorphism with $\theta_\tau^2=\tau^2$, the $\theta_\tau$-dual of a right module is a right module with $\lvert C\rvert\lvert C^{\perp}\rvert=\lvert R\rvert^n$, and $(C^{\perp})^{\perp}=\tau^2(C)$; reflexive $\iff\tau^2=\mathrm{id}$ | — | `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` §1, §5 | T-002, T-007 | **proved** (straightforward generalisation) | new; exhibits the unstated restriction in T-002 (we only use $\tau=\sigma_s$) and shows the $r\mid 2s$ criterion is the specialisation $\tau^2=\mathrm{id}$ | §2.4 (remark) |
| **T-028** (new) | **Reflexive-parameter trichotomy:** (i) $r=1$ ($q=p$): $\sigma_s=\mathrm{id}$ for all $s$ — **no Galois action**; (ii) $r$ odd: non-trivial Galois action and reflexivity are **mutually exclusive** ($r\mid2s\iff r\mid s\iff\sigma_s=\mathrm{id}$); (iii) $r$ even: $s=r/2$ is the unique non-trivial reflexive choice ($\sigma_s$ of order 2, $\theta_s$ an involution) | $q=p^r$ | `06_AUDIT/PHASE0_U8_U9_DECISIONS.md` §4 | T-003, T-015, T-017 | **proved** | new; governs the standing hypothesis $r\ge2$ and the choice of parameters for §7 | §1, §8 |
| **T-029** (new) | **Prior-art position:** duality for codes over a finite Frobenius ring defined by a non-degenerate form attached to an anti-automorphism, together with the module structure of the dual, the double-dual property, cardinality complementarity and the MacWilliams identities, is **published** (Wood 2010; Szabo–Wood 2017; Nebe–Rains–Sloane 2006); left/right orthogonal theory over non-commutative Frobenius rings is published (Dougherty–Leroy 2016); cyclic self-dual codes over $M_2(\mathbb F_2)$ are published (Solé, MMS 2011) | — | `06_AUDIT/PHASE0_NOVELTY_REASSESSMENT.md` | — | `established (lit)` | new; **the novelty claim must be narrowed accordingly** (see the novelty file §6) | §1 |

### Rows added by Phase 1 (`03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`)

Proof location for every row of this block is `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`
(abbreviated **RGF**); corroboration is `04_COMPUTATION/ring_structure_checks.py`
(**401/401 PASS**) and `04_COMPUTATION/module_actions_checks.py` (**276/276 PASS**).

| ID | Claim / theorem | Assumptions | Proof / file | Dependencies | Status | Audit | Manuscript section |
|----|-----------------|-------------|--------------|--------------|--------|-------|--------------------|
| **T-030** | $A_t=\mathbb F_q[u]/\langle u^t\rangle$: $\lvert A_t\rvert=q^t$; $a$ is a unit $\iff a_0\ne0$; $A_t$ is a chain ring with $\mathrm{Jac}=(u)$, nilpotency $t$, socle $\langle u^{t-1}\rangle$; $\lambda$ (coefficient of $u^{t-1}$) is non-degenerate and ideal-catching; $\lvert\mathrm{Aut}(A_t)\rvert=r$ for $t=1$ and $r(q-1)q^{t-2}$ for $t\ge2$ (so $\mathrm{Aut}(A_t)\supsetneq\{\sigma_s\}$, cf. T-002) | $q=p^r$, $t\ge1$ | RGF §1 L1.1–L1.6 | — | **proved** | **confirmed** ($\lvert\mathrm{Aut}(A_t)\rvert$ measured by brute force: $2,6,24,2,3,4$ for $(q,t)=(4,1),(4,2),(4,3),(9,1),(8,1),(16,1)$) | §2.1 |
| **T-031** | $R=M_2(A_t)$: $\lvert R\rvert=q^{4t}$; $Z(R)=A_t\cdot I$; $\lvert\mathrm{GL}_2(A_t)\rvert=q^{4(t-1)}(q^2-1)(q^2-q)$; $R/\mathrm{Jac}(R)\cong M_2(\mathbb F_q)$ is simple; exactly $t+1$ two-sided ideals $u^iR$ | — | RGF §2 L2.1–L2.5 | T-030, E-003 | **proved** | **confirmed** ($180,5760,3528,46080$ at $(q,t)=(4,1),(9,1),(8,1),(4,2)$; ideals by the unit criterion $1-xy\in R^\times$) | §2.2 |
| **T-032** | **Morita, column convention:** right ideals of $R$ ⇄ $A_t$-submodules $W\subseteq A_t^2$ (columns), $I_W=\{X:\text{every column of }X\in W\}$, $\dim I_W=2\dim W$; hence $q+3$ right ideals at $t=1$ and $q^2+3q+5$ at $t=2$ | — | RGF §2 Prop. 2.6, Cor. 2.7; handedness completed in §5.6.1 | E-005, T-031 | **proved** | **confirmed** ($7,12,11$ at $q=4,9,8$, $t=1$; **33** at $q=4,t=2$); the **left**-ideal family (rows) is equinumerous and $X\mapsto X^{\mathsf T}$ is a bijection between them (`module_actions_log.txt` part A) | §2.3, §5.2 |
| **T-033** | $R_n=R[X]/\langle X^n-1\rangle\cong M_2(B)$, $B=A_t[X]/\langle X^n-1\rangle$; $X$ is central, so left = right multiplication by $X$, and both are the cyclic shift $T$, $(Tx)_e=x_{e-1}$; $T$ is right-$R$-linear and $T^n=1$ | — | RGF §3 L3.1–L3.2; verified in `module_actions_log.txt` part B | T-004 | **proved** | **confirmed** (centrality of $X$ and $X^n=1$ checked exhaustively in $B$ for five parameter sets) | §2.5, §5.1 |
| **T-034** | $\mathrm{ord}(\sigma_s)=r/\gcd(r,s)$; $\theta_s=\sigma_s\circ{}^{\mathsf T}$ is a $\sigma_s$-semilinear **anti**-automorphism; $\theta_s^{2k}=\sigma_{2ks}$ and $\mathrm{ord}(\theta_s)=2r/\gcd(r,2s)$; $\theta_s$ is an involution $\iff r\mid2s$ | — | RGF §4 L4.1–L4.4, Thm 4.5, Cor. 4.6 | T-002, T-015 | **proved** | **confirmed** ($\mathrm{ord}\,\sigma_s=[1,2],[1,3,3],[1,4,2,4]$ and $\mathrm{ord}\,\theta_s=[2,2],[2,6,6],[2,4,2,4]$ at $q=4,8,16$; involutive $s$: $\{0,1\}$ at $q=4$, $\{0,2\}$ at $q=16$, $\{0\}$ at $q=8,27$) | §2.4 |
| **T-035** | **Action/pairing compatibility (Lemma 5.6a):** for $x,y\in R^n$, $a\in R$: (1) $B_s(x\cdot a,y)=\theta_s(a)B_s(x,y)$; (2) $B_s(x,y\cdot a)=B_s(x,y)a$; (3) $B_s(a\cdot x,y)=B_s(x,\theta_s(a)\cdot y)$; (4) $B_s(x,a\cdot y)=B_s(\theta_s^{-1}(a)\cdot x,y)$; (5) $B_s(x,Ty)=B_s(T^{-1}x,y)$. Also the column/row mixing formulas for the two actions on $R$ and the coordinate formulas on $R^n$ | — | RGF §5.6.1–5.6.3 | T-002, T-033 | **proved** | **confirmed** (all five identities, $[SMP]$, at $q=4,8,9$, $t=1,2$, $n=1,2,3$, $s=0,1$) | §5.1, §5.6 |
| **T-036** | **Sides of the orthogonals (Lemma 5.6b):** for an **arbitrary** subset $S\subseteq R^n$ both $S^{\perp_s}$ and ${}^{{\perp_s}}\!S$ are right $R$-submodules; if $S$ is a **left** $R$-submodule, both are left $R$-submodules as well (hence subbimodules). At $n=1$ the orthogonal of a left ideal is two-sided, i.e. one of the $t+1$ ideals $u^iR$ (Remark 5.6c) | — | RGF §5.6.3, Remark 5.6c | T-035 | **proved** | **confirmed**: part 1 for arbitrary subsets ($[SMP]$); part 2 for **every** left ideal enumerated ($0$ failures out of $7,33,343,12,144,11,93,33$) and for randomly generated left submodules; Remark 5.6c at $q=4,9,8$, $t=1,2$. Non-vacuity: the cyclic code generated by $E_{11}$ is a right, not a left, module. Part 1 strengthens Lemma 5.5 (its right-module hypothesis is unnecessary) | §5.2, §5.6 |
| **T-037** | **The $\theta_s$-pairing package:** sesquilinearity ($b_s$ is $\sigma_s$-sesquilinear over $\mathbb F_q$, $\mathbb F_p$-bilinear, $\mathbb F_q$-bilinear only when $r\mid s$); key identity $\theta_s(B_s(x,y))=B_s(y,\sigma_{2s}x)$; the dual of a cyclic code is cyclic; ideal-catching for $\Lambda$ on **both** sides; non-degeneracy and $\dim C+\dim C^{\perp_s}=4tn$, $\lvert C\rvert\lvert C^{\perp_s}\rvert=\lvert R\rvert^n$; the $R$-valued and $\mathbb F_q$-valued orthogonals coincide; $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$; reflexivity $\iff r\mid2s$; hull and $\sigma_k$-isometry | — | RGF §6 L6.2–L6.11, Thm 6.6, 6.8, Cor 6.4, 6.9 | T-001, T-002, T-007, T-015, T-016, T-023, T-024 | **proved** | **confirmed** (Gram rank $=4t$; size formula on **every** enumerated right ideal; double dual in both the reflexive and the non-reflexive regime, with $6/11$, $24/30$, $12/19$ non-$\sigma_{2s}$-invariant codes at $q=8,27,16$). **Correction made:** $b_s$ is $\sigma_s$-**sesquilinear**, not $\mathbb F_q$-bilinear (RGF Lemma 6.2(iii)) | §3, §6 |
| **T-038** | **Regime-independent statements (Thm 7.1):** for every right $R_n$-submodule $C$: $C^{\perp_s}$ is cyclic; the size formula; $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$; $\mathrm{Hull}_s(C)$ is cyclic; $\sigma_k$-equivariance; parameter invariance under $\sigma_{2s}$; ${}^{{\perp_s}}\!C=(\sigma_{-2s}C)^{\perp_s}$ | — | RGF §7 Thm 7.1 | T-037 | **proved** | **confirmed**; holds in **all** regimes R0–R3, i.e. also when $r\nmid2s$ | §3, §7 |
| **T-039** | **Regime-dependent statements (Thm 7.2, 7.3):** if $r\mid2s$ then $\theta_s$ is an involution, the duality is reflexive, $b_s$ is $\sigma_s$-Hermitian and $\mathrm{Tr}\circ b_s$ is a symmetric $\mathbb F_p$-bilinear form (so CSS/EA machinery applies); if $r\nmid2s$ these fail in general ($35/737$ reflexive codes at $q=8,n=3$) | — | RGF §7 Thm 7.2, 7.3 | T-037, T-028 | **proved** | **confirmed**, with the warning (B3.5) that nothing licenses the quantum construction for an arbitrary non-reflexive code | §7, §8 |
| **T-040** | **Per-code rescue in R3 (Thm 7.4):** if $r\nmid2s$ but $\sigma_{2s}(C)=C$, then $C^{\perp_s\perp_s}=C$ and all conclusions of Thm 7.2 hold **for that code**; such codes are exactly those obtained by Galois descent to the fixed field of $\sigma_{2s}$ ($5\times7=35$ of $737$ at $q=8,n=3$; $6$ of $30$ at $q=27,n=1$) | $\sigma_{2s}(C)=C$ | RGF §7 Thm 7.4 | T-038, T-039 | **proved (conditional)** | **confirmed**; the hypothesis is a genuine restriction and is **not** assumed away — see the warning B3.5 | §7 |
| **T-041** | **Cyclic-code counts (Morita + $B$-submodule enumeration):** $7$ at $(q,t,n)=(4,1,1)$; $33$ at $(4,1,2)$; $343=(q+3)^3$ at $(4,1,3)$; $12$ at $(9,1,1)$; $144=(q+3)^2$ at $(9,1,2)$; $11$ at $(8,1,1)$; $93$ at $(8,1,2)$; $33$ at $(4,2,1)$ | — | `04_COMPUTATION/module_actions_checks.py` part C | T-005, T-018, T-026 | `computational only` (**[EXH]** over the $B$-submodule lattice; enumeration skipped for $q=9,n=3$ and $q=4,t=2,n=2$ — see the log) | **new corroboration of T-018**: $343$ and $144$ confirm the formula where $X^n-1$ is squarefree ($3\mid q-1$ at $q=4,n=3$; $\mathrm{char}=3$ at $q=9,n=2$); **new counterexamples**: $93\ne121$ at $q=8,n=2$ (second data point, after $33\ne49$, that the squarefree hypothesis is essential) | §5.2 |
| **T-042** | **Withdrawn claim:** the final clause of Remark 5.6 ("for a left module the analogous closure fails in general") is **false**: by T-036 the orthogonal of a left module *is* a left module. The premise — that $B_s(a\cdot x,y)$ is not, in general, a left multiple of $B_s(x,y)$ — is correct | — | RGF §5.6.4 (correction and witness) | T-035, T-036 | `needs correction` (claim withdrawn, not replaced by any left-module duality theory) | found during the Phase-1 final verification; nothing in §§6–8 depends on it (all those statements concern right modules) | §5.2 |
| **T-043** | **Scope of Phase 1 (§8):** no hull-dimension formula (Phase 4); no Gray map / metric statements (Phase 5); no quantum construction (Phase 6); no novelty claim for anti-automorphism duality (decision **B2**, T-029); no restatement or challenge of Alahmadi et al.'s Theorem 1 (decision **B1**); $q=2$ used only as an enumerator check, never as Galois evidence | — | RGF §8 | — | `open` / scoped | unchanged; the same scope is carried into the Phase-1 exit gate (RGF §6.8), which is **satisfied** under the recorded regime restriction (decision **B3**) | §1, §8 |

---

### Rows added by Phase-2 planning (source: `PHASE2_PROPOSAL_v2.md`, commit `1327b26`)

**Read this first.** Phase 2 is **NOT STARTED**. This block registers *planning* items:
definitions, proposed statements, proof obligations, conjectures, open problems and
computational tests. **Nothing in this block is a theorem, a proved result, or evidence for
one.** No Phase-2 computation has been run (CT-0 … CT-6 are all *pending*), the Phase-2
theorem document `03_THEOREMS/CYCLIC_CODE_STRUCTURE.md` does not exist yet, and no
Phase-2 result may be cited anywhere.

**IDs.** Items keep the IDs of `PHASE2_PROPOSAL_v2.md` (`D-2.x`, `P-2.x`, `L-2.x`, `C-2.1`,
`O-2.x`, `CT-x`) so that proposal and register are traceable to each other. Rows for
Phase-2 **results** (once proved or refuted) will be added as `T-044 …` during execution,
per v2 §10 deliverable (3).

**Source discipline.** v2 is authoritative; `PHASE2_PROPOSAL.md` (v1, commit `13fa2fa`) is
**superseded, not deleted** — see `PHASE1_COMPLETION_AND_APPROVAL_GATE.md` §10. v1's
uniform bound `$\mu_B(W)\le4$` is withdrawn and survives only as **O-2.2**.

#### Phase-2 status vocabulary (added to the Phase-0/1 vocabulary above)

| Status | Meaning |
|---|---|
| `PROVED IN PHASE 1` | already proved in `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`; the Phase-2 row is a cross-reference, not a new claim |
| `IMPORTED RESULT` | taken from the literature or from standard algebra, **with a reference** (`E-0xx` below or a citation); the *application* to our rings is still to be written out and checked |
| `PROPOSED / UNPROVED` | a proof (or a complete proof strategy) exists **only in the proposal**; not transcribed into a theorem file; **may not be cited as a result** |
| `CONJECTURE` | stated with a derivation/sketch, explicitly unproved; **numerical agreement is not evidence of truth** |
| `OPEN PROBLEM` | no claim made; recorded so it cannot be silently dropped (decision **D3**) |
| `COMPUTATIONAL TEST PENDING` | a test is specified but **has not been run**; nothing has been verified |
| `DEFINITION` (added for completeness) | fixes notation/convention; true by stipulation, carries no truth claim |

**Counts in this block (77 rows, each assigned exactly one primary status):** 10
`DEFINITION`, 5 `PROVED IN PHASE 1`, 6 `IMPORTED RESULT`, 33 `PROPOSED / UNPROVED`, 3
`CONJECTURE`, 9 `OPEN PROBLEM`, 11 `COMPUTATIONAL TEST PENDING` (the 9 `CT-` rows plus
`C-2.1g`, with `C-2.1f` additionally carrying that label), and **1 withdrawn claim**
(`P-2.5-W`, no status). **0 proved Phase-2 results.**

#### D-2.x — definitions adopted for Phase 2 (`DEFINITION`; v2 §1.2, §3, §4, §6.0)

| ID | Object | Definition / convention | Source | Status |
|----|--------|------------------------|--------|--------|
| **D-2.1** | `$\rho_a,\lambda_a$` | coordinate-wise right / left actions on `$R^n$` | v2 §1.2 = RGF §5.6.1 | `DEFINITION` |
| **D-2.2** | `$T$` | `$(Tx)_e := x_{e-1\ \mathrm{mod}\ n}$` (Phase-1 direction, Cor. 6.4) | v2 §1.2 | `DEFINITION` (matches T-033) |
| **D-2.3** | `$\mathrm{rev}$` | `$\mathrm{rev}(x)_e := x_{-e}$` on `$R^n$`; `$\mathrm{rev}(\sum u_eX^e):=\sum u_{-e}X^e$` on `$R_n$` | v2 §1.2, P-2.1f | `DEFINITION` |
| **D-2.4** | `$\mu_B(W)$`, `$\mu_S(I)$` | minimal number of `$B$`- resp. right-ideal generators; `$\mu(0)=0$`; principal `$\iff\mu\le1$` | v2 §3 | `DEFINITION` |
| **D-2.5** | `$\mathrm{ann}_r,\mathrm{ann}_l$` | `$\mathrm{ann}_r(v)=\{w:vw=0\}$` (`$v$` on the left); `$\mathrm{ann}_l(v)=\{w:wv=0\}$` | v2 §6.0 | `DEFINITION` |
| **D-2.6** | `$B_j,m_j,K_j$` | `$n=p^vn'$` with `$\gcd(n',p)=1$`; `$X^{n'}-1=\prod f_j$`; `$B_j=A_t[X]/\langle F_j^{p^v}\rangle$`, `$m_j=(u,F_j)$`, `$K_j=\mathbb F_{q^{d_j}}$` | v2 §4 | `DEFINITION` |
| **D-2.7** | case names | **squarefree** `$p\nmid n$`; **repeated-root** `$p\mid n,t=1$`; **wild** `$p\mid n,t\ge2$` | v2 §4 | `DEFINITION` |
| **D-2.8** | `$N(t,Q)$` | number of `$S$`-submodules of `$S^2$`, `$S=\mathbb F_Q[u]/\langle u^t\rangle$` | v2 §7 | `DEFINITION` |
| **D-2.9** | commutation convention | "$R$-linearity" = the scalar is untouched; "$\theta_s$-compatibility" = commutation `$T\theta_s=\theta_sT$`; "intertwining" = `$\theta_s\rho_a=\lambda_{\theta_s(a)}\theta_s$` | v2 §1.3 | `DEFINITION` |

#### P-2.1 — the shift and the commutation table (v2 §1.3, §2)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **L-2.1.1** | `$X$` is central in `$R_n$` (so left = right multiplication by `$X$`) | — | RGF §3 Lemma 3.1 | T-004 | **`PROVED IN PHASE 1`** (= T-033) | CT-0 re-checks it | CCS §2 |
| **P-2.1a** | `$T$` is **right** `$R$`-linear: `$T(x\cdot a)=(Tx)\cdot a$` | — | RGF §3 Lemma 3.2 | L-2.1.1 | **`PROVED IN PHASE 1`** (= T-033); v2 §2 adds a coordinate-level proof | CT-0 | CCS §2 |
| **P-2.1b** | `$T$` is **left** `$R$`-linear: `$T(a\cdot x)=a\cdot(Tx)$` | — | v2 §2 (coordinate proof only) | P-2.1a | **`PROPOSED / UNPROVED`** (new: T-033 proves only the right side) | CT-0 | CCS §2 |
| **P-2.1c** | `$T\sigma_k=\sigma_kT$`, `$T\theta_s=\theta_sT$` (commutation of `$F_p$`-linear maps) | — | v2 §2 | — | **`PROPOSED / UNPROVED`**; not to be confused with Lemma 5.6a(5) `$B_s(x,Ty)=B_s(T^{-1}x,y)$` | CT-0 | CCS §2 |
| **P-2.1d** | `$\sigma_k$` preserves the side | — | v2 §2 | T-002 | **`PROPOSED / UNPROVED`** | CT-0 | CCS §2 |
| **P-2.1e** | `$\theta_s$` **swaps** the side: `$\theta_s\rho_a=\lambda_{\theta_s(a)}\theta_s$` | — | v2 §2 (cross-checked against `$\theta_s^2=\sigma_{2s}$`) | T-002, T-034 | **`PROPOSED / UNPROVED`** | CT-0 | CCS §2 |
| **P-2.1f** | `$\mathrm{rev}$`: (i) `$F_q$`-linear, `$\mathrm{rev}^2=\mathrm{id}$`, `$\mathrm{rev}\,T=T^{-1}\mathrm{rev}$`; (ii) commutes with `$\rho_a,\sigma_k,\theta_s$`; (iii) is a ring **automorphism** of `$R_n$`; (iv) `$\mathrm{rev}(\mathrm{ann}_r(v))=\mathrm{ann}_r(\mathrm{rev}\,v)$` | — | v2 §2 | L-2.1.1 | **`PROPOSED / UNPROVED`**; (iii) **corrects v1**, which treated `$\mathrm{rev}$` as an anti-automorphism | CT-0 (`$\mathrm{rev}(uv)=\mathrm{rev}(u)\mathrm{rev}(v)$`) | CCS §2 |
| **P-2.1g** | `$T$` = right **and** left multiplication by `$X$`; `$T^n=\mathrm{id}$`; `$T$` is a Hamming isometry | `$X$` central | RGF §3 Lemma 3.2 | L-2.1.1 | **`PROVED IN PHASE 1`** (= T-033) | CT-0 | CCS §2 |
| **TBL-2.1** | the commutation table of v2 §1.3 (which maps commute, under which convention, with which linearity type) | — | v2 §1.3, proofs in §2 | P-2.1a–g | **`PROPOSED / UNPROVED`** as a package | CT-0 | CCS §2 |

#### P-2.3 — generator numbers (v2 §3)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **P-2.3(1)** | `$W\mapsto I_W=\{M:\mathrm{im}\,M\subseteq W\}$` is a bijection `$B$`-submodules of `$B^2$` → right ideals of `$S=M_2(B)$`; `$I_W\cong W\oplus W$`; `$\dim I_W=2\dim W$`, `$\lvert I_W\rvert=\lvert W\rvert^2$` | `$B$` commutative; column convention | bijection and `$\mathrm{Hom}$` description: standard Morita; dimension part proved in RGF §2 Prop. 2.6 / Cor. 2.7 | T-005, E-005 | **`IMPORTED RESULT`** (Morita; T-005) — **the dimension/count part is `PROVED IN PHASE 1` (T-032)**; column-convention write-out pending | CT-1a (small rings) | CCS §3 |
| **L-2.3.1** | `$I_W$` is a right ideal and `$W(I_W)=W$` | — | v2 §3 (strategy only) | P-2.3(1) | **`PROPOSED / UNPROVED`** | CT-1a | CCS §3 |
| **P-2.3(2)** | `$\mu_S(I_W)=\lceil\mu_B(W)/2\rceil$` | `$B$` commutative finite | v2 §3, **via L-2.3a + L-2.3b + L-2.3c** | L-2.3a–c, L-2.3.1 | **`PROPOSED / UNPROVED`** — retaining this status is mandatory; it does **not** follow from projectivity alone | CT-1a (exhaustive, three rings) | CCS §3 |
| **L-2.3a** | `$\sum_i x_iS=I_{W'}$` with `$W'=\sum_i\mathrm{im}(x_i)$` (uses **only** freeness/projectivity of `$B^2$`) | `$P=B^2$` projective | v2 §3 | — | **`PROPOSED / UNPROVED`** | CT-1a | CCS §3 |
| **L-2.3b** | `$\min\{k: W=\sum_i U_i,\ \mu_B(U_i)\le2\}=\lceil\mu_B(W)/2\rceil$` (counting) | — | v2 §3 | — | **`PROPOSED / UNPROVED`** | CT-1a | CCS §3 |
| **L-2.3c** | any `$\le2$`-generated submodule of `$B^2$` is `$\mathrm{im}(x)$` for one `$x\in S$` | — | v2 §3 | — | **`PROPOSED / UNPROVED`** | CT-1a | CCS §3 |
| **P-2.3(3)** | `$I_W$` two-sided `$\iff W=J\oplus J$` for an ideal `$J\trianglelefteq B$` | `$B$` commutative | standard Morita | E-003, T-031 (`$n=1$` case: `$t+1$` ideals `$u^iR$`) | **`IMPORTED RESULT`** (E-003) | — | CCS §3 |

#### P-2.4 — CRT / Hensel with precise hypotheses (v2 §4)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **P-2.4** | (1) Hensel lifts `$f_j$` to `$F_j\in A_t[X]$`; (2) `$B\cong\prod_j B_j$`, `$B_j=A_t[X]/\langle F_j^{p^v}\rangle$`; (3) `$B_j$` local with `$m_j=(u,F_j)$`, residue `$K_j$`, `$\dim_{\mathbb F_q}B_j=t\,d_jp^v$`; (4) `$\mu_B(W)=\max_j\mu_{B_j}(W_j)$` | `$n=p^vn'$`, `$\gcd(n',p)=1$`; Hensel applied to the **squarefree part only** | v2 §4 | L-2.4.1–L-2.4.5 | **`PROPOSED / UNPROVED`** (parts 1–2 are imported; the ring-theoretic description 3–4 is the content to be proved) | CT-2 | CCS §4 |
| **L-2.4.1** | Hensel lift of the coprime factorisation `$X^{n'}-1=\prod f_j$` (repeated factor obtained as `$F_j^{p^v}$`, **never lifted directly**) | `$A_t$` finite local, hence `$(u)$`-adically complete; `$f_j$` pairwise coprime monic | standard Hensel | E-012 | **`IMPORTED RESULT`** (E-012); the discipline "squarefree part only" is a **proposed** application rule | CT-2 | CCS §4 |
| **L-2.4.2** | CRT for the pairwise comaximal ideals `$\langle F_j^{p^v}\rangle$` | — | standard CRT | E-011 | **`IMPORTED RESULT`** (E-011) | CT-2 | CCS §4 |
| **L-2.4.3** | `$B_j$` is local, `$m_j=(u,F_j)$` nilpotent, `$B_j/m_j\cong K_j$` | — | v2 §4 | L-2.4.1, L-2.4.2 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §4 |
| **L-2.4.4** | `$\dim_{\mathbb F_q}B_j=t\,d_jp^v$` (normal form `$\sum_{a<t,b<d_jp^v}c_{ab}u^aX^b$`) | — | v2 §4 | L-2.4.3 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §4 |
| **L-2.4.5** | `$\mu_B(W)=\max_j\mu_{B_j}(W_j)$` across CRT components | — | v2 §4 | L-2.4.2 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §4 |
| **L-2.4.6** | **Wild case is genuinely non-chain:** `$t\ge2$` and `$p^v\ge2$` `$\Rightarrow\dim_{K_j}(m_j/m_j^2)=2$`, so `$m_j$` is not principal and `$B_j$` is not a chain ring | `$p\mid n$`, `$t\ge2$` | v2 §4 (strategy) | L-2.4.3 | **`PROPOSED / UNPROVED`** — load-bearing for P-2.6 and for the "no SNF in the wild case" warning | CT-2 (`$\dim_{K_j}(m_j/m_j^2)$` must be `$1$` or `$2$` exactly as predicted) | CCS §4 |
| **CASE-2.4** | Three-case table: squarefree `$p\nmid n$` (chain ring, nilpotency `$t$`); repeated-root `$t=1$` (chain ring, nilpotency `$p^v$`); **wild** `$p\mid n,t\ge2$` (local, **not** chain: no SNF, no shape classification, no product-of-chain-ring counts) | D-2.7 | v2 §4 | L-2.4.6 | `DEFINITION` of the cases + **`PROPOSED / UNPROVED`** classification | CT-2, CT-5 | CCS §4 |

#### P-2.5 / P-2.6 — principality: individual criterion and global claim (v2 §5)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **P-2.5** | (a) `$\mu_S(I_W)=\lceil\mu_B(W)/2\rceil$`; (b) `$I_W$` principal `$\iff\mu_B(W)\le2$`; (c) `$I_W$` is `$2$`-generated whenever `$\mu_B(W)\le4$` | `$B$` commutative finite | v2 §5.1 | L-2.3.1, L-2.3a–c | **`PROPOSED / UNPROVED`** ((c) is a conditional corollary of (a)) | CT-1a, CT-1 | CCS §5 |
| **P-2.5-W** | **Withdrawn (v1):** the uniform bound "$\mu_B(W)\le4$ for every `$W$`" | — | withdrawn in v2 §5.1 | — | **not a claim**; retained as **O-2.2** (`OPEN PROBLEM`) | — | — |
| **P-2.6** | **Global:** every right ideal of `$R_n$` is principal `$\iff p\nmid n$` or `$t=1$` | D-2.7 | v2 §5.2 | L-2.6.1 … L-2.6.8 | **`PROPOSED / UNPROVED`** — retaining this status is mandatory (it is the sharp form of T-021, which stays open) | CT-1 (incl. the explicit `$M_2(m_j)$` test) | CCS §5 |
| **L-2.6.1** | every right ideal of `$R_n$` is `$I_W$` for a unique `$W$` (Morita onto) | — | standard Morita | T-005, E-005 | **`IMPORTED RESULT`** (T-005/E-005); column-convention write-out pending | CT-1 | CCS §5 |
| **L-2.6.2** | CRT/Hensel decomposition with the case analysis | D-2.7 | = P-2.4 | L-2.4.1–L-2.4.6 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §5 |
| **L-2.6.3** | `$B_j$` is a chain ring `$\iff t=1$` or `$p\nmid n$` | — | v2 §5.2 | L-2.4.6 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §5 |
| **L-2.6.4** | over a finite chain ring `$S$`, every submodule of `$S^2$` is `$\cong u^aS\oplus u^bS$`, hence `$2$`-generated (Smith normal form; in a chain ring one of any two elements divides the other) | `$B_j$` a chain ring | v2 §5.2 (strategy); background E-015 | L-2.6.3 | **`PROPOSED / UNPROVED`** — may be upgraded to `IMPORTED RESULT` only if E-015 is verified against the source | CT-1, CT-3 | CCS §5 |
| **L-2.6.5** | `$\mu_B(W)=\max_j\mu_{B_j}(W_j)$` and `$\mu_{B_j}(W_j)=\dim_{K_j}(W_j/m_jW_j)$` (Nakayama) | `$B_j$` local | v2 §5.2; background E-014 | L-2.4.3 | **`PROPOSED / UNPROVED`** | CT-1 | CCS §5 |
| **L-2.6.6** | `$\dim_{K_j}(m_j/m_j^2)=2\iff(t\ge2$` and `$p\mid n)$`, else `$1$` | — | = L-2.4.6 | L-2.4.6 | **`PROPOSED / UNPROVED`** | CT-2 | CCS §5 |
| **L-2.6.7** | `$p\nmid n$` or `$t=1\Rightarrow$` every `$W_j$` is `$2$`-generated `$\Rightarrow\mu_B(W)\le2\Rightarrow$` every `$I_W$` principal (the `$\Leftarrow$` direction of P-2.6) | — | v2 §5.2 | L-2.6.2–L-2.6.5, P-2.5 | **`PROPOSED / UNPROVED`** | CT-1 | CCS §5 |
| **L-2.6.8** | converse: `$p\mid n,t\ge2\Rightarrow W=m_j\oplus m_j$` has `$\mu_B(W)=4\Rightarrow I_W=M_2(m_j)$` has `$\mu_S=2$`, so **not** principal (the `$\Rightarrow$` direction of P-2.6) | — | v2 §5.2 | L-2.6.5, L-2.6.6 | **`PROPOSED / UNPROVED`**; the predicted counterexample is **unverified** | CT-1 at `$(4,2,2)$` | CCS §5 |
| **BC-2.6** | Boundary-case predictions: `$n=1$` all principal (Phase 1 counted `$7/12/11/33$` ideals but **never tested principality**); `$t=1,p\nmid n$` all principal; `$t=1,p\mid n$` all principal (new: `$33$` at `$(4,1,2)$` is consistent but untested); `$t\ge2,p\nmid n$` all principal (new); `$t\ge2,p\mid n$` **not** all principal (new, explicit `$M_2(m_j)$`) | — | v2 §5.2 | L-2.6.1–L-2.6.8 | **`PROPOSED / UNPROVED`** predictions; each entry is `COMPUTATIONAL TEST PENDING` | CT-1 | CCS §5 |

#### P-2.7 / P-2.8 — dual and annihilator (v2 §6)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **L-6.1** | `$\theta_s$` is an **anti-automorphism of `$R_n$`** (`$\theta_s(uv)=\theta_s(v)\theta_s(u)$`, `$\theta_s^{-1}=\sigma_{-2s}\theta_s$`) | `$n\ge1$` | v2 §6.1 (proof via the index swap `$(a,b)\mapsto(b,a)$`) | T-002, T-034 | **`PROPOSED / UNPROVED`** — **retaining this status is mandatory**; Phase 1 proves it only for `$n=1$` (`$R$`, T-002/T-034) | CT-0 (`$n=2,3$`) | CCS §6 |
| **P-2.7** | `$C^{\perp_s}=\mathrm{rev}\big(\mathrm{ann}_r^{R_n}(\theta_s(g))\big)=\mathrm{ann}_r^{R_n}(\theta_s(\mathrm{rev}\,g))=\{y:\theta_s(g)\cdot\mathrm{rev}(y)=0\}$`; in Morita form `$\mathrm{ann}_r(\theta_s(g))=I_{\ker\theta_s(g)}$`, so `$\dim C^{\perp_s}=2\dim\ker\theta_s(g)$` | `$C=gR_n$` **principal**; `$s$` arbitrary | v2 §6.3 (six-step derivation) | L-6.1, T-037 (non-degeneracy / right radical trivial), D-2.3, D-2.5 | **`PROPOSED / UNPROVED`** — retaining this status is mandatory | CT-4 (incl. a mandatory `$\mathrm{rev}$`-sensitive case) | CCS §6 |
| **P-2.8** | explicit generator: with `$v=\theta_s(\mathrm{rev}\,g)$` and `$v_j=U_j\,\mathrm{diag}(\omega^{a_j},\omega^{b_j})\,V_j$` in SNF over the chain ring `$B_j$`, `$C^{\perp_s}=hR_n$` with `$h_j=V_j^{-1}\mathrm{diag}(\omega^{\ell_j-a_j},\omega^{\ell_j-b_j})$` | `$B$` a product of **chain rings** (`$p\nmid n$` or `$t=1$`) | v2 §6.6 | P-2.7, L-2.6.4 | **`PROPOSED / UNPROVED`**; gives **nothing** in the wild case (see O-2.8) | CT-4 | CCS §6 |
| **L-6.5** | for `$x\in M_m(B)$`, `$B$` finite Frobenius: the row module and the column module of `$x$` have equal cardinality (so `$\lvert gR_n\rvert=\lvert R_ng\rvert$`) | `$B$` Frobenius | v2 §6.5 (strategy via `$\mathrm{im}(x)^\perp=\ker(x^{\mathsf T})$`) | L-6.6 | **`PROPOSED / UNPROVED`** | CT-4 (check `$\lvert gR_n\rvert=\lvert R_ng\rvert$`) | CCS §6 |
| **L-6.6** | `$B=A_t[X]/\langle h\rangle$` (`$h$` monic) is Frobenius; `$M_2(B)$` is Frobenius | — | v2 §6.5 (strategy); background E-013 | T-001, E-001 | **`IMPORTED RESULT`** (E-013) **conditional on verifying the reference**; if no source can be verified it reverts to `PROPOSED / UNPROVED` | CT-4 | CCS §6 |
| **CHK-2.7** | Consistency checks C1–C4: sizes (`$\lvert C^{\perp_s}\rvert=\lvert R_n\rvert/\lvert R_ng\rvert$`), `$n=1$` degeneration, extremes `$g=0,1$`, right-ideal property of `$\mathrm{rev}(\mathrm{ann}_r(v))$` | — | v2 §6.5 | P-2.7, L-6.5 | **`PROPOSED / UNPROVED`** (each check is itself a falsification opportunity) | CT-4 | CCS §6 |
| **NOTE-6.5** | **Registration note (not a change to v2).** The identity `$\lvert\mathrm{ann}_r(v)\rvert\cdot\lvert vS\rvert=\lvert S\rvert$` used in v2 §6.5 (C1) is **elementary** for every finite ring (`$m\mapsto vm$` is right `$S$`-linear with kernel `$\mathrm{ann}_r(v)$` and image `$vS$`); the Frobenius hypothesis is needed for **L-6.5**, not for this identity. To be re-examined when §6.5 is transcribed | — | this row | — | `DEFINITION` (clarification of attribution) | — | CCS §6 |

#### C-2.1 — submodule counts over a chain ring (v2 §7)

| ID | Statement | Assumptions | Proof / file | Dependencies | Status | Tests / falsification | Target § |
|----|-----------|-------------|--------------|--------------|--------|-----------------------|----------|
| **C-2.1a** | `$N(1,Q)=Q+3$` | `$t=1$` | RGF §2 Cor. 2.7 | T-032 | **`PROVED IN PHASE 1`** (T-032; verified `$7,12,11$` at `$Q=4,9,8$`) | — | CCS §7 |
| **C-2.1b** | `$N(2,Q)=Q^2+3Q+5$` | `$t=2$` | RGF §2 Cor. 2.7 | T-032 | **`PROVED IN PHASE 1`** (T-032; verified `$33$` at `$Q=4$`) | — | CCS §7 |
| **C-2.1c** | shape classification: every `$S$`-submodule of `$S^2$` is `$\cong u^aS\oplus u^bS$`, `$0\le a\le b\le t$` | `$S$` a finite chain ring | v2 §7; = L-2.6.4 | L-2.6.4 | **`PROPOSED / UNPROVED`** (the SNF existence part) | CT-3 | CCS §7 |
| **C-2.1d** | number of submodules of shape `$(a,b)$` is `$Q^{\,b-a-1}(Q+1)$` for `$a<b$`, and `$1$` for `$a=b$` | C-2.1c | v2 §7 | C-2.1c | **`CONJECTURE`** (the genuinely open part: it requires counting the cosets/orbits parametrising the embeddings) | CT-3 | CCS §7 |
| **C-2.1e** | closed form `$N(t,Q)=(t+1)+(Q+1)\sum_{d=1}^{t}(t+1-d)Q^{\,d-1}$` | C-2.1c + C-2.1d | v2 §7 | C-2.1d | **`CONJECTURE`** for `$t\ge3$`; for `$t=1,2$` it reduces to C-2.1a/C-2.1b (`PROVED IN PHASE 1`) | CT-3 | CCS §7 |
| **C-2.1f** | predicted values `$N(3,2)=37$`, `$N(3,4)=139$`, `$N(3,9)=1024$`, `$N(4,2)=83$` | — | arithmetic from C-2.1e | C-2.1e | **`CONJECTURE`** + **`COMPUTATIONAL TEST PENDING`** (CT-3). These are predictions, **not** computed values | CT-3 | CCS §7 |
| **C-2.1g** | census predictions from **proved** formulas that have **not been run**: `$113$` codes at `$(9,2,1)$` (from C-2.1b) and `$35\,937=33^3$` at `$(4,2,3)$` (from C-2.1b **plus** the `$t\ge2$` product decomposition, which is `PROPOSED`) | — | v2 §5.2, §9 | C-2.1b, P-2.4 | **`COMPUTATIONAL TEST PENDING`** — not known values; the `$(4,2,3)$` figure is **not** a Phase-1 result | CT-1, CT-3 | CCS §7 |

**Mandatory recording rule for C-2.1 (decision C-2.1 rule).** When CT-3 is run, the register
row must state **which `$(t,Q)$` values were actually checked**, by which of the three routes
(BFS lattice / brute-force over `$\mathbb F_Q$`-subspaces / closed form), and with which
`[EXH]`/`[SMP]` label. "They matched" is not an acceptable register entry. Agreement of the
enumeration with the closed form is **evidence, not proof**.

#### O-2.x — open problems carried into Phase 2 (v2 §8)

| ID | Problem | Status | Test |
|----|---------|--------|------|
| **O-2.1** | Principality boundary (P-2.6), incl. the predicted counterexample `$M_2(m)$` at `$(4,2,2)$` | `OPEN PROBLEM` | CT-1 |
| **O-2.2** | Wild case: classify `$B_j$`-submodules of `$B_j^2$`; decide whether `$\mu_B(W)\le4$` always (i.e. every right ideal `$2$`-generated). **The v1 claim of this bound is withdrawn** | `OPEN PROBLEM` | CT-1, CT-5 |
| **O-2.3** | Enumeration at `$t\ge2$`: `$N(t,Q)$` (C-2.1) and the product formula over CRT factors | `OPEN PROBLEM` (closed form part is `CONJECTURE`) | CT-2, CT-3 |
| **O-2.4** | Explicit generator of the dual (P-2.8) and its failure mode in the wild case | `OPEN PROBLEM` | CT-4 |
| **O-2.5** | For which `$v$` is `$\ker v$` a direct summand of `$B^2$`? — **not** always (`$v=uI_2$` over `$\mathbb F_4[u]/\langle u^2\rangle$` gives `$\ker v=uS\oplus uS$`, not a summand) | `OPEN PROBLEM` (partially answered: negative in general; classification open) | CT-4 |
| **O-2.6** | Galois action `$\sigma_s$` on the CRT components (preserves each `$B_j$`, induces Frobenius on `$K_j$`); effect on `$\sigma_{2s}$`-invariance and on the per-code rescue (Thm 7.4) | `OPEN PROBLEM` | CT-6 |
| **O-2.7** | `$n=1$` anchor: confirm the theory degenerates to the ideal theory of `$M_2(A_t)$` (`$7/12/11/33$` right ideals, all principal) | `OPEN PROBLEM` | CT-1 |
| **O-2.8** | In the wild case, is `$\mu_B(\ker\theta_s(g))\le2$` for every `$g$` (equivalently, is the dual of every principal code principal)? | `OPEN PROBLEM` | CT-4, CT-5 |
| **CF-D3** | Carried forward per decision **D3**: T-006 (entry-wise form, uncharacterised), T-021 (resolved by P-2.6 **only if P-2.6 is proved**), T-027 (general `$\tau\in\operatorname{Aut}(A_t)$`), hull formulas (Phase 4), Gray map (Phase 5), quantum (Phase 6, warning B3.5), coverage gaps (`$q=9,n=3$`; `$q=4,t=2,n=2$`), `$n\ge2$` left-submodule gap | `OPEN PROBLEM` (recorded, not resolved) | — |

#### CT-0 … CT-6 — computational test plan (v2 §9). **None of these has been run.**

| ID | Test | Refutes / decides | Status |
|----|------|-------------------|--------|
| **CT-0** | P-2.1a–g as vector identities (`[EXH]` where feasible, else `[SMP]` with seed), plus `$\theta_s(uv)=\theta_s(v)\theta_s(u)$` on `$R_n$` for `$n=2,3$` and `$\mathrm{rev}(uv)=\mathrm{rev}(u)\mathrm{rev}(v)$` | P-2.1a–g, L-6.1, P-2.1f(iii) | **`COMPUTATIONAL TEST PENDING`** |
| **CT-1a** | exhaustive check of `$\mu_S(I_W)=\lceil\mu_B(W)/2\rceil$` on `$\mathbb F_2[u]/\langle u^2\rangle$`, `$\mathbb F_2[u]/\langle u^3\rangle$`, `$\mathbb F_2[u,\varepsilon]/\langle u^2,\varepsilon^2\rangle$` | P-2.3(2), L-2.3a–c, P-2.5 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-1** | principality census over the boundary-case table (`$n=1$`; `$t=1$` with/without `$p\mid n$`; `$t\ge2$` with/without `$p\mid n$`) incl. the explicit `$M_2(m)$` test | P-2.6, BC-2.6, O-2.1, O-2.2, O-2.7 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-2** | CRT/Hensel data: `$J$`, `$d_j$`, `$e=p^v$`, `$\dim_{K_j}(m_j/m_j^2)$`, chain-ring predicate | P-2.4, L-2.4.3–L-2.4.6 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-3** | `$N(t,Q)$` census at `$t\ge2$` with `$p\nmid n$` (three counting routes), compared with C-2.1 | C-2.1c–g, O-2.3 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-4** | P-2.7 / P-2.8 on every principal code at six parameter sets; `$\mathrm{rev}$`-sensitivity search; `$\lvert gR_n\rvert=\lvert R_ng\rvert$` | P-2.7, P-2.8, L-6.5, CHK-2.7, O-2.8 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-5** | wild-case census at `$(4,2,2)$`, `$(4,2,4)$`, `$(9,2,3)$`: submodule counts, `$\mu_B$` distribution, principality | O-2.2, O-2.8 | **`COMPUTATIONAL TEST PENDING`** |
| **CT-6** | Galois action on CRT components and `$\sigma_{2s}$`-invariant counts | O-2.6 | **`COMPUTATIONAL TEST PENDING`** |
| **REG-2** | Phase-1 regression: re-run `ring_structure_checks.py` (401/401) and `module_actions_checks.py` (276/276), require byte-identical logs | guards Phase 1 (D1) | **`COMPUTATIONAL TEST PENDING`** |

#### Traceability table — proposed Phase-2 result → obligations → tests → risks

| Proposed result | Status | Proof obligations | Computational tests | Unresolved risks / stop conditions |
|-----------------|--------|-------------------|---------------------|-----------------------------------|
| **P-2.1a–g** (shift) | P-2.1a,g,L-2.1.1 `PROVED IN PHASE 1`; P-2.1b–f, TBL-2.1 `PROPOSED / UNPROVED` | L-2.1.1 (= T-033); coordinate proofs v2 §2 | CT-0 | the direction convention for `$T$` (fixed by Cor. 6.4 and `module_actions_checks.py` part B); a wrong convention shows up immediately in CT-0 |
| **P-2.3** (generator numbers) | `PROPOSED / UNPROVED` (+ `IMPORTED` bijection) | L-2.3.1, L-2.3a, L-2.3b, L-2.3c | CT-1a | L-2.3a uses **only** freeness of `$B^2$`; if it fails the identity fails. Brute-force `$\mu_B$` must itself be validated (Nakayama route vs tuple search) |
| **P-2.4** (CRT/Hensel) | `PROPOSED / UNPROVED` (+ L-2.4.1, L-2.4.2 `IMPORTED`) | L-2.4.1–L-2.4.6, CASE-2.4 | CT-2 | Hensel must be applied to the **squarefree part only**; in the wild case there is **no** SNF and **no** product-of-chain-ring count — any such step invalidates the argument. Reference for E-012 to be confirmed |
| **P-2.5** (individual principality) | `PROPOSED / UNPROVED` | L-2.3.1, L-2.3a–c | CT-1a, CT-1 | the withdrawn uniform bound `$\mu_B\le4$` is **not** available (O-2.2); (c) is conditional on (a) |
| **P-2.6** (global principality) | `PROPOSED / UNPROVED` | L-2.6.1 … L-2.6.8, BC-2.6 | CT-1 | the predicted counterexample `$M_2(m_j)$` at `$(4,2,2)$` is **unverified**; `$n=1$` principality was never tested in Phase 1; T-021 stays open until P-2.6 is proved |
| **L-6.1** (`$\theta_s$` anti on `$R_n$`) | `PROPOSED / UNPROVED` | — (self-contained) | CT-0 | Phase 1 proves only the `$n=1$` case; must be checked before P-2.7 is used |
| **P-2.7** (dual / annihilator) | `PROPOSED / UNPROVED` | L-6.1, T-037 non-degeneracy, D-2.3, D-2.5 | CT-4 | the worked example in v2 §6.4 is `$\mathrm{rev}$`-stable and **does not test the reversal**; a `$\mathrm{rev}$`-sensitive case is mandatory; `$\lvert gR_n\rvert=\lvert R_ng\rvert$` (L-6.5) is unproved |
| **P-2.8** (explicit dual generator) | `PROPOSED / UNPROVED` | P-2.7, L-2.6.4 (SNF), L-6.5, L-6.6 | CT-4 | meaningless in the wild case (no SNF) — see O-2.4/O-2.8; `$\ker v$` need not be a summand (O-2.5) |
| **C-2.1** (counts) | `$t=1,2$` `PROVED IN PHASE 1`; `$t\ge3$` `CONJECTURE` | C-2.1c (shape classification = L-2.6.4) + C-2.1d (per-shape count) | CT-3 (three routes) | agreement is **not** proof; the register must record which `$(t,Q)$` were checked; the `$35\,937$` figure at `$(4,2,3)$` rests on the unproved `$t\ge2$` product decomposition |
| **O-2.1 … O-2.8** | `OPEN PROBLEM` | — | CT-1, CT-4, CT-5, CT-6 | carried forward per **D3**; none may be treated as settled until a proof exists and a row says `proved` |

#### Phase-2 dependency graph (planning only)

```
T-033 (X central, T right-linear) ──► L-2.1.1 ──► P-2.1a,g (PROVED IN PHASE 1)
                                              └──► P-2.1b–f, TBL-2.1 (PROPOSED) ──► L-6.1 ──► P-2.7
T-005/E-005 (Morita) ──► P-2.3(1) ──► L-2.3.1 ──┬──► L-2.3a ──► P-2.3(2) ──► P-2.5
                                                 ├──► L-2.3b ───┘
                                                 └──► L-2.3c ───┘
E-012 (Hensel) + E-011 (CRT) ──► P-2.4 ──► L-2.4.3–L-2.4.6 ──► CASE-2.4
                                        └──► L-2.6.2, L-2.6.3 ──► L-2.6.4 (SNF) ──► L-2.6.5
                                                                                  └──► L-2.6.7 ──► P-2.6
                                        └──► L-2.4.6 ──► L-2.6.6 ──► L-2.6.8 ──► P-2.6 (counterexample)
P-2.7 + L-2.6.4 ──► P-2.8 ;   P-2.7 + L-6.5 + L-6.6 ──► CHK-2.7
C-2.1c (= L-2.6.4) + C-2.1d ──► C-2.1e ──► C-2.1f ;   C-2.1b + P-2.4 ──► C-2.1g
CT-0 … CT-6, REG-2 : all pending
```

#### Phase-2 imported facts (background; not ours to prove)

| ID | Fact | Source |
|----|------|--------|
| **E-011** | Chinese remainder theorem for pairwise comaximal ideals | standard (Atiyah & MacDonald, *Introduction to Commutative Algebra*, Ch. 1) |
| **E-012** | Hensel's lemma for lifting a factorisation into pairwise coprime monic factors over a complete local ring | standard (Atiyah & MacDonald, Ch. 10; Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*, §7) — **reference to be confirmed against the source in Phase 2** |
| **E-013** | A finite free algebra over a Frobenius ring defined by a monic polynomial is Frobenius; the Frobenius property is transitive and Morita-invariant | standard (Wood 1999 = E-001; Lam, *Lectures on Modules and Rings*, GTM 189, §16) — **reference to be confirmed** |
| **E-014** | Nakayama: for a finite module `$M$` over a local ring `$(B,m,k)$`, elements generate `$M$` iff their images generate `$M/mM$`; hence `$\mu_B(M)=\dim_k(M/mM)$` | standard (Atiyah & MacDonald, Prop. 2.6, Prop. 2.8) |
| **E-015** | Matrices over a chain ring admit a Smith normal form; submodules of free modules over a chain ring | background literature (McDonald, *Finite Rings with Identity*, Dekker 1974) — **cited as prior art, not as a substitute for the proof L-2.6.4** |
| **E-017** | For any **finite** ring `$S$` and `$v\in S$`, `$\lvert\mathrm{ann}_r(v)\rvert\cdot\lvert vS\rvert=\lvert S\rvert$` (elementary: `$m\mapsto vm$` is right `$S$`-linear, kernel `$\mathrm{ann}_r(v)$`, image `$vS$`); **no Frobenius hypothesis needed** | elementary — see NOTE-6.5 |

---

## Imported established facts (not ours to prove)

| ID | Fact | Source |
|----|------|--------|
| **E-001** | Finite Frobenius rings are the alphabets for which the MacWilliams extension theorem and MacWilliams identities hold; duality is character-theoretic and works for non-commutative rings | Wood 1999 (B1) |
| **E-002** | $M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$, $u^2=0$, $u$ not central; the Bachoc map $\phi(a+ub)=(a+b,b)$ is an isometry onto $\mathbb F_4^2$ (Hamming) | Bachoc 1997 (A9); Alahmadi et al. 2013 (A1) |
| **E-003** | Two-sided ideals of $M_m(B)$ are exactly $M_m(J)$, $J\trianglelefteq B$ | standard (Morita) |
| **E-004** | The Galois inner product $\langle a,b\rangle_h=\sum a_ib_i^{p^h}$ generalises Euclidean ($h=0$) and Hermitian ($h=\ell/2$) | Fan–Zhang 2017 (C1) |
| **E-005** | Right ideals of $M_m(K)$ ($K$ a field) ↔ subspaces of $K^m$; hence $\#=\sum_{i=0}^m\bigl[\begin{smallmatrix}m\\i\end{smallmatrix}\bigr]_K$ | standard (Morita) — basis of T-018, T-020 |
| **E-006** (new) | Duality for codes over a non-commutative finite ring obtained by assuming an **anti-isomorphism** of the ring and a well-behaved duality on the module alphabet; elaboration of Nebe–Rains–Sloane | J. A. Wood, Int. J. Inf. Coding Theory **1**(4) (2010) 429–444, doi:10.1504/IJICOT.2010.032867 |
| **E-007** (new) | Over a finite Frobenius ring, duals w.r.t. non-degenerate **sesquilinear** forms (relative to an anti-automorphism) and bilinear forms have a module structure, a double-dual property, complementary cardinality and MacWilliams identities | Szabo & Wood, J. Algebra Comb. Discrete Struct. Appl. **4**(2) (2017) 105–113, doi:10.13069/jacodesmath.284934 (MR3601342) — **hypotheses still to be checked for the non-involutive case (F-13)** |
| **E-008** (new) | Form rings / types over finite rings, including non-commutative examples such as $\mathbb F_q+\mathbb F_qu$ with $u^2=0$; Clifford–Weil genus-$m$ weight enumerators | Nebe, Rains & Sloane, *Self-Dual Codes and Invariant Theory*, Alg. Comput. Math. **17**, Springer 2006 |
| **E-009** (new) | Over a non-commutative Frobenius ring, a code equals its left orthogonal iff it equals its right orthogonal; constructions from self-dual codes over the centre | Dougherty & Leroy, AAECC **27** (2016) 185–203, doi:10.1007/s00200-015-0277-0 |
| **E-010** (new) | Cyclic self-dual codes over $M_2(\mathbb F_2)$ and $M_2(\mathbb F_2[i])$; factorisations of $X^7+1$ and $X^m+1$ over these rings | P. Solé, 11th Mediterranean Microwave Symposium (MMS) 2011, doi:10.1109/MMS.2011.6068573 — closest predecessor on the same alphabet |

---

## Proof-dependency graph (updated)

```
E-001 ──► T-001 ──┬──► T-006 (plain product fails for right modules)
                  ├──► T-007 (theta duality) ──► T-008 (cyclicity) ──► T-009 (hull)
                  │        │                                              │
                  │        ├──► T-016 (double dual = sigma_{2s} C)         │
                  │        │          └──► T-017 (reflexive iff r | 2s, m>=2)
                  │        │                     └──► T-028 (parameter trichotomy)
                  │        └──► T-010 (F_q-valued form) ──► T-012 (Gray) ──► T-013 (quantum) ──► T-014
                  └──────────────────────────────────────────────────────► T-011 (hull dims, open)
T-002 ──► T-003 ──► T-007 ;  T-002 ──► T-015 (theta^2 = sigma_{2s}) ──► T-016
T-023 (key identity) ──► T-016 ,  T-023 ──► (symmetry needs r | 2s)
T-024 (isometry) ──► T-025 (parameter invariance) ──► U9 decision ──► T-013
T-004 ──► T-005 ──► T-018 (enumeration, NEEDS squarefree) ──► T-021 (principality, conditional)
E-005 ──► T-018, T-020
T-026 (q=4,n=2 counterexample) ──► limits T-018, T-021
T-027 (general tau) ──► context for T-002, T-015, T-017
T-019, T-020, T-022, T-026 : computational only (no theorem claimed)
T-029 (prior art) : governs the wording of every novelty claim
```

---

## Audit checklist for the reviewer (updated after the independent audit)

1. **T-016/T-017 are confirmed and are the load-bearing new statements.** Double-dual
   $=\sigma_{2s}(C)$ holds with **no** hypothesis (100 % on 6 961 + 113 independently
   enumerated codes, including at $q=8$); reflexivity holds iff $r\mid2s$
   (343/343, 144/144, 5000/5000 versus **35/737** at $q=8$).
2. **U9 is settled** (see `06_AUDIT/PHASE0_U8_U9_DECISIONS.md`): reflexivity is *not*
   needed for size/dimension/weight/hull data (T-024, T-025), but it *is* needed for
   $C^{\perp\perp}$-style proofs and for the symmetry of the form. **Please confirm the
   recommendation: quantum theorems in the reflexive regime ($s\equiv0$, or $r$ even with
   $s=r/2$), general-$s$ statements as companions.**
3. **U8 is NOT settled (blocking).** Our 35 (right-ideal convention) and A1's 8
   (quaternary convention) count different families; the recorded A1 theorem statement is
   internally inconsistent (its generators divide $X^n-1$ for two different lengths).
   Please choose: **(a)** re-read A1, or **(b)** authorise "cite A1 for the framework
   only, never restate its theorem" (recommended).
4. **Novelty must be narrowed (blocking, T-029/E-006–E-010).** See
   `06_AUDIT/PHASE0_NOVELTY_REASSESSMENT.md` §6 for wording we can defend.
5. **T-018 now carries the squarefree hypothesis** and **T-022 reads 33, not 32**; any
   document still quoting 32 or the unqualified enumeration formula must be corrected.
6. **T-021 (principality)** is conditional; no later phase may use "every cyclic code is
   principal" at $t\ge2$ or when $p\mid n$ until it is proved.
7. **Standing hypotheses to state up front:** $r\ge2$ (otherwise there is no Galois
   action at all), and $r$ even if a non-trivial *reflexive* Galois action is wanted.
8. Everything marked `open` (T-011 … T-014) is out of scope for Phase 0 and must stay so.
