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
