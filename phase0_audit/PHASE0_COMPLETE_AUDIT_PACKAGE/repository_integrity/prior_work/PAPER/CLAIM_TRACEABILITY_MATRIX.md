# Phase 8 / Task B — Claim-to-source traceability matrix

Columns: **Manuscript claim** · **Theorem ID** (register) · **Source document**
· **Proof location** · **Computational evidence** · **Status**.

Every row was re-checked in Phase 8 against the committed source. Where Phase 8
found a discrepancy it is marked `CORRECTION` and recorded in
`PAPER/OPEN_ISSUES_AND_LIMITATIONS.md` with an erratum number; **nothing was
silently repaired**.

Legend for the status column:
`P` = proved in the named file · `P+[EXH]` = proved and verified exhaustively ·
`CV` = computationally verified only (no proof; never promoted) ·
`IMP` = imported with a citation · `REF` = refuted · `OP` = open.

---

## §3 Preliminaries and the noncommutative matrix-ring framework

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| $A_t=\mathbb F_q[u]/\langle u^t\rangle$ is a finite chain ring; $|A_t|=q^t$; $\lambda(\sum a_iu^i)=a_{t-1}$ | T-030 ff. | `RING_AND_GALOIS_FOUNDATIONS.md` | §1.1–§1.5 | sizes, unit criterion, ideals $[EXH]$ | P |
| $R=M_2(A_t)$: $|R|=q^{4t}$, $Z(R)=A_tI$, $\mathrm{Jac}(R)=M_2(uA_t)$, exactly $t+1$ two-sided ideals $u^iR$; $R$ is Frobenius | T-031, T-001 | `RING_AND_GALOIS_FOUNDATIONS.md` | §2.1–§2.5; `PAIRING_COMPLETE_PROOFS.md` §1 Lemma 1.4 | $|{\rm GL}_2(A_t)|=180,5760,3528,46080$ at the four parameter sets $[EXH]$ | P (Frobenius: IMP, Wood 1999) |
| **Right-module convention**: codes are right $R_n$-submodules; the plain product $\sum x_iy_i$ gives a perfect dual on **left** modules but **not** on right modules | T-006 | `PAIRING_COMPLETE_PROOFS.md` | §5 Prop. 5.1 (explicit $M_2(\mathbb F_2)$ counterexample $C=uR$, $|C||C^\perp|=4\ne16$) | size formula fails 8/343, 4/737, 4/144, 2/1200, 3/33 | P + [EXH] |
| $R_n\cong M_2(B)$, $B=A_t[X]/\langle X^n-1\rangle$ **commutative**; Morita: right ideals of $R_n$ ⇄ $B$-submodules of $B^2$ | T-004, T-005 | `RING_AND_GALOIS_FOUNDATIONS.md` | §3, §2.6 | CRT+Morita prediction reproduces the enumerated distribution at $q=2,n=3$ exactly | IMP (Morita) + CV |
| $\sigma_s(a)=a^{p^s}$ (fixing $u$) is in $\mathrm{Aut}(A_t)$; entrywise extension to $M_2(A_t)$; $\theta_s=\sigma_s\circ(\cdot)^{\mathsf T}$ is an **anti**-automorphism; $\theta_s^2=\sigma_{2s}$; $\theta_s$ is **not** an involution in general | T-002, T-003, T-115…T-120, Lemma 1.3 | `PAIRING_COMPLETE_PROOFS.md` §1; `PHASE2_STAGE2C_GALOIS_DUALITY.md` | Lemma 1.1, 1.2, 1.3 | 7 parameter sets; $256^2$ pairs at $q=4$ $[EXH]$ | P |
| *Hidden assumption, recorded:* $\mathrm{Aut}(A_t)\supsetneq\{\sigma_s\}$; we use only the coefficient-Frobenius subgroup | T-002 annotation | `UPDATED_THEOREM_REGISTER.md` | T-002 note | — | P (scoped) |
| $\Lambda=\lambda\circ\mathrm{tr}$ is symmetric, associative, non-degenerate and ideal-catching | T-001 | `PAIRING_COMPLETE_PROOFS.md` | §1 Lemma 1.4 | Gram rank of $\Lambda(XY)$ full: 4/4 at $t=1$, 8/8 at $t=2$ | P |
| **CRT decomposition**: $B\cong\prod_j A_t[X]/\langle g_j^{e_j}\rangle$ via an $\mathbb F_q$-linear ring isomorphism $\Psi$ | T-216 | `PHASE7_LONGER_LENGTH_AND_PARAMETER_OPTIMIZATION.md` | §1.1 (Part 1 of the script); multiplicativity on all pairs of basis elements; $\Psi\circ\Psi^{-1}=\mathrm{id}$ | reproduces the Phase-3B exhaustive BFS **as a set** on all 10 supported families (33/343/565/93/144/1024/1221/113/139/565) | P + [EXH] |
| $B_j$ chain ring $\iff t=1$ or $e_j=1$; $\mu_B(W)=\max_j\mu_{B_j}(W_j)$ | T-103, T-104, T-222 | `PHASE2_STAGE2B_CRT_PRINCIPALITY.md`; Phase 7 Part 5 | L-2.6.3, L-2.4.5; Phase 7 §4.1 | chain verdict matches the direct test on every component of every enumerable family | P + [EXH] |
| Every right ideal of $R_n$ principal $\iff p\nmid n$ or $t=1$ | T-105, T-106, T-107 | `PHASE2_STAGE2B_CRT_PRINCIPALITY.md` | P-2.6 both directions | 460 checks $[EXH]$ | P |

## §4 Cyclic codes and Galois duality

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| $b_s(x,y)=\Lambda(\sum_i\theta_s(x_i)y_i)$ is additive, $\mathbb F_p$-bilinear, right-$\mathbb F_q$-linear, left-$\sigma_s$-semilinear, non-degenerate | T-007, Prop 2.1–2.3 | `PAIRING_COMPLETE_PROOFS.md` | §2, §3 Thm 3.3 | — | P |
| $C^{\perp_s}$ is a **right** $R_n$-module; $C$ cyclic $\Rightarrow C^{\perp_s}$ cyclic; $\dim C+\dim C^{\perp_s}=N$; $|C||C^{\perp_s}|=|R|^n$ | T-007, T-008 | `PAIRING_COMPLETE_PROOFS.md` | Thm 3.4, 3.5, 3.7 | 343/343, 737/737 ×2, 144/144, 5000/5000 $[SMP]$, 33/33 at $t=2$ | P + [EXH] |
| $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$ | T-133 | `PAIRING_COMPLETE_PROOFS.md` | Thm 3.6 | — | P |
| $C^{\perp_s}=\operatorname{rev}(\operatorname{ann}_r(\theta_s(C)))$ for **arbitrary** right ideals; $\operatorname{rev}$ is load-bearing exactly when $n\ge3$ ($\operatorname{rev}=\mathrm{id}\iff n\le2$) | T-124, T-125, T-126, T-127 | `PHASE2_STAGE2C_GALOIS_DUALITY.md` | P-2.1f, P-2.7 | 596 checks $[EXH]$/$[SMP]$ | P |
| The $R$-valued and the $\mathbb F_q$-valued orthogonals coincide | T-010 | `PAIRING_COMPLETE_PROOFS.md` | §4 Prop. 4.1 | 6961/6961 $(\text{code},s)$ instances | P + [EXH] |
| Three regimes: general Galois $\supsetneq$ reflexive ($r\mid2s$) $\supsetneq$ per-code $\widehat\sigma_{2s}$-invariance; pairwise non-equivalent | T-155…T-158, T-186, T-190 | `PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md`; `PHASE5_QUANTUM_CONSTRUCTIONS.md` §1 | §D; Phase 5 §1 | witness $(8,1,2,1)$: 14 of 92 codes $\widehat\sigma_2$-invariant | P + [EXH] |

## §5 Galois hull structure

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R_n$-submodule, cyclic if $C$ is; **not** a left ideal in general | T-009, T-138, T-139 | `PAIRING_COMPLETE_PROOFS.md` §3 Thm 3.8; `PHASE3_STAGE3A` | Thm 3.8; §1.3 | explicit witness at $(4,1,1)$, $s=0$ | P |
| Morita hull formula $\mathrm{Hull}_s(C)=I_{W\cap W'}$; principality criterion $\mu_B(W\cap W')\le2$ | T-147, T-148, T-149 | `PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md` | §C1, §C2, §C4 | 583 checks | P + [EXH] |
| $\mathrm{Hull}_s$ is $\sigma_k$- and $\sigma_{2s}$-equivariant; $\theta_s(\operatorname{ann}_r I)=\operatorname{ann}_l(\theta_s I)$ | T-140, T-141, T-142, T-156 | `PHASE3_STAGE3A` | §A4 | — | P |
| **O-3.1 refuted**: a Galois hull need not be a principal right ideal | T-173 | `PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md` | §5 | exhaustive over **every** code of every enumerable family; $\mu_B(\mathrm{Hull}_s)\in\{0,1,2,3\}$, four witnesses at $(4,2,2)$ | REF (conjecture) / P + [EXH] (witnesses) |
| $\mu_B\ge3$ **requires** $t\ge2$ and $p\mid n$; $\mu_B(W)\le2$ is **false** over non-chain local rings; witnesses at $(9,2,3)$ and $(4,2,4)$, **not** at $(8,2,2)$ | T-222, T-223, T-224 | `PHASE7_LONGER...md` §4 | Part 5 theorem + D3 | the deterministic family $W=m^ie_1\oplus U$, $U\le\operatorname{ann}_{B^2}(m)$, is enumerated exhaustively in each wild family | P (structure) + [EXH] (witnesses) |
| **No universal closed (gcd-type) hull formula exists** | T-154 | `PHASE3_STAGE3A` | §C | — | P (non-existence) |
| LCD / SO / SD criteria | T-161, T-162, T-163 | `PHASE3_STAGE3A` | §E | censuses | P |
| **Conjectures** H-3A.1, H-3A.2 (hull inclusion / hull-dimension symmetry) | T-159, T-160 | `PHASE3_STAGE3A` | §D | — | **CONJECTURE** — stated as such in the manuscript, never used |

## §6 Gray-map compatibility

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| $\varphi_n:R^n\to\mathbb F_q^{N}$, $N=4tn$, is an $\mathbb F_q$-linear bijection, $\varphi_nT=\widehat T\varphi_n$ (rotation by $4t$); **not** a ring homomorphism | T-176 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §1.1, §1.2 | flat-index map checked against `ring_structure_checks` on all $|R|$ elements | P + [EXH] |
| **Exact Gram matrix**: $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}Jv^{\mathsf T}$, $J=I_{4n}\otimes H_t$, $H_t[a][b]=1\iff a+b=t-1$; $\operatorname{tr}(\theta_s(X)Y)=\sum_{k,l}\sigma_s(X_{kl})Y_{kl}$ | T-177 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §3.2 | Gram computed element-wise equals $I_{4n}\otimes H_t$ **exactly** on 18 instances; rank $J=N$; $120^2$ pairs | P + [EXH] |
| **Duality preservation**: $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$ for every code and every $s$ | T-178 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §3.3 | two independent routes; 6/6, 32/32, 32/32, 92/92, 143/143, 342/342, 112/112, 1220/1220 $[EXH]$, 400/400 $[SMP]$ | P + [EXH] |
| **Hull preservation**: $\varphi_n(\mathrm{Hull}_s(C))=\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$, no principality hypothesis | T-179 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §4.1–§4.3 | verified on the four $\mu_B=3$ witnesses of T-173 | P + [EXH] |
| Image is quasi-cyclic of index $4t$, co-index $n$; **not** cyclic in general | T-183 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §5.1, §5.2 | measured counts | P |
| Weight chain $w_{\rm H}\le w_{\rm ent}\le w_{\rm coef}\le t\,w_{\rm ent}$, $w_{\rm H}\le\mathrm{wt}_{\rm H}\varphi_n\le4t\,w_{\rm H}$, both sharp; $\varphi_n$ is a $d_{\rm coef}$/Hamming isometry | T-180 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §2.2 | — | P |
| “$\varphi_n$ preserves the ring-Hamming weight” — **false** | T-180b | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §2 | — | REF |
| **No** Hamming isometry exists for the homogeneous weight (non-integral values) | T-182 | `PHASE4_GRAY_MAP_COMPATIBILITY.md` | §2.5 | — | P |
| **Char-2 obstruction**: $p=2$, $t$ even $\Rightarrow H_t$ alternating $\Rightarrow$ no congruence $T^{\mathsf T}H_tT=I_t$ exists; domain exactly “$t$ even” (congruences exist for $t=1,3,5$); a $(9,2)$ congruence exists but is non-monomial | T-199, T-200, T-185 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` §3.2; `PHASE6...md` §5 | T-200 proof; Phase 6 §5.2 | exhaustive over all $4\times4$ matrices over $\mathbb F_4$; 200 invertible $S$ at each of five parameter pairs | P + [EXH] |
| **Every Galois hull is self-orthogonal** for the transported form; no reflexivity, no principality (one-sided argument) | T-192 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §2.1 | 226 hulls, 8 parameter sets $[EXH]$ | P + [EXH] |
| $N_{\rm phys}=N=4tn$ (derived from $\dim_{\mathbb F_q}R=4t$); no doubling to $2N$ | T-198 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §3.1 | $(4,1,2)\to8$, $(4,2,1)\to8$, $(4,2,2)\to16$, $(4,2,3)\to24$ | P + [EXH] |
| The congruence map $\Psi(u)=u\mathcal T$, $\mathcal T=I_{4n}\otimes T$: eight properties, monomial $\iff t=1$ | T-199 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §3.2 | verified for $(4,1,2),(9,2,1),(9,2,2)$ | P + [EXH] |

## §7 Quantum constructions

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| Weyl relation and the commutation criterion $\mathrm{Tr}(a\cdot b'-a'\cdot b)=0$ | Lemma Q1 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §0 | 256 pairs at $q=4,N=2$ | P + [EXH] |
| Stabilizer lemma Q2 (abelian ⟺ trace-symplectic isotropy; $K=N-\log_q|\mathcal C|$; distance as a symplectic minimum; Knill–Laflamme equivalence) | Lemma Q2 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §0 | $K=(1/|S|)\sum_g\mathrm{Tr}(g)$ reproduces $8,4,2,1$ | P + [EXH] |
| **R1** twisted graph: $\omega((u|T_su),(u'|T_su'))=\langle u',u\rangle-\langle u,u\rangle$; $[[N,N-k,d]]_q$; no congruence, no reflexivity | T-193 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §2.2 | — | P |
| R1 cap $d_{R1}\le\min\mathrm{wt}(D^{\perp_E})$; abelian ⟺ SO outside the reflexive regime; abelian for **every** code inside it | T-194, T-195 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §2.2 | 32/32 at $(4,1,2,1)$; 12 abelian = 12 SO of 92 at $(8,1,2,1)$; 60/60 at $(9,2,1,1)$ | P + [EXH] |
| **R2** CSS: SO $\Rightarrow[[N,N-2k,d]]_q$, $d=\min\mathrm{wt}(D'^{\perp_E}\setminus D')$; DC $\Rightarrow[[N,2k-N,d]]_q$, $d=\min\mathrm{wt}(D'\setminus D'^{\perp_E})$ | T-196 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §2.3 | — | P |
| **R3** EA: $[[N,N-k-h_E,d;k-h_E]]_q$, $c=k-h_E$, $d=\min\mathrm{wt}(D^{\perp_E}\setminus\mathrm{Hull}_E(D))$; degenerates to R2-SO at $h_E=k$ | T-197 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §2.4 | — | P |
| Parameter theorem for all three routes; all dimensions over $\mathbb F_q$; alphabet $\mathbb F_q$ | T-201, T-207 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` §5; `PHASE6...md` §0 | T-201; T-207 proof (radical/hyperbolic-pair argument) | $K$ recomputed row by row and from the Hilbert-space formula | P |
| Commutation must be tested on an $\mathbb F_p$-basis | T-203 | `PHASE5_QUANTUM_CONSTRUCTIONS.md` | §7 | $[[16,4,3]]_4$: 12 $\mathbb F_q$-generators vs 24 $\mathbb F_p$-basis elements | P + [EXH] |

## §8 Distance certification and parameter analysis

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| **Coset-distance characterisation**: $d$ = min weight of the quotient code $D^{\perp_E}/\mathrm{Hull}_E(D)$, dim $K$, length $N$ | **T-230** | `PHASE7_LONGER...md` | **§3.0** | — | **P** |
| **Coset Singleton bound** $K+d\le N+1$; neither EA-Singleton nor implied by it | **T-232** | `PHASE7_LONGER...md` | **§3.0** (injectivity of puncturing $N-d+1$ coordinates) | check **H1**: 5055 codes, 0 violations $[EXH]$ | **P + [EXH]** |
| **Feasibility inequality** $d\ge4,\ c\le c_0,\ K\ge K_0\Rightarrow2k\le N+c_0-K_0$ | **T-233** | `PHASE7_LONGER...md` | **§3.0** (from $c=k-h_E$, $K=N-k-h_E$) | — | **P** |
| $k$ even; $K-c=N-2k\equiv0\pmod4$; $c+K=N-2h_E$; $c\ge2k-N$ | T-219 | `PHASE7_LONGER...md` | §3.1 | 5055 codes, 0 violations | P + [EXH] |
| **ERRATUM E-7.1**: Phase 6 §12's $c+K=N-k$ is wrong (2 of its own 25 rows satisfy it); correct is $c+K=N-2h_E$ | E-7.1 | `PHASE7_LONGER...md` | §6.1 | 25 Phase-6 rows re-parsed; 23 violate | ERRATUM (recorded) |
| Certification by three independent methods (M1 complete enumeration, M2 support search, M3 ambient quantum search); the **exact** code is certified (image basis carried) | T-225 | `PHASE7_LONGER...md` | §5 (Part 6) | 28 codes; Phase 6: 22 codes | P (methods) + [EXH] |
| O-6.1 frontier: $c\le4\Rightarrow d=4$ ($[[24,10,4;2]]_9$, proved lower bound); $d=5$ at $c=2$, $K=6$; $d=6$ at $c=10$ | T-220 | `PHASE7_LONGER...md` | §3.2–§3.3 | min-$c$-per-$d$ table | CV |
| O-6.2: stabilizer $d=4/2/1/1$, EA $d=10/6/4/2$ for $t=1,2,3,4$ | T-221 | `PHASE7_LONGER...md` | §3.5 | — | CV |
| Non-dominated frontier: 368 tuples, 88 non-dominated, 280 dominated | **T-231** | `PHASE7_LONGER...md` | §2.2 | Part 3(f) of the log | CV |
| EA Singleton and EA Hamming: 0 violations on 5055 codes | T-227 | `PHASE7_LONGER...md` | §7 | Part 8 | CV $[EXH]$ |
| New search reproduces or improves every shared Phase-6 Pareto distance (8 pairs: 3 improved, 5 equal); Phase 6's “no stabilizer $d\ge4$” re-scoped to $N\le16$ | T-226, T-205 annotation | `PHASE7_LONGER...md` | §6.3, §6.4 | F2, F3 of the log | CV |
| **Phase 5 generator-number correction**: Phase 5 §4's $\mu_B=4$ is $\mu_B$ of the **code** $W$; the hull census (O-3.1/T-173) is $\mu_B$ of the **hull**, in $\{0,1,2,3\}$ | Phase 5 §4 / T-173 | `PHASE7_LONGER...md` | **§4.4** | hull values $\le3$ over the extended enumeration; $\mu_B(\mathrm{Hull}_s)=3$ at $(4,2,2)$, $(9,2,3)$, $(4,2,4)$ | CORRECTION (recorded, append-only) |

## §9 Comparison

| manuscript claim | register ID | source document | proof location | computational evidence | status |
|---|---|---|---|---|---|
| $q=4$ and $q=9$ stabilizer codes can be compared with `codetables.de`; $q=8$ cannot; **no EA table exists** | T-228, **E-8.1** | `PAPER/LITERATURE_VERIFICATION.md` §2–§3 | — | live retrieval 2026-11-04: $q=9$ returns GF($3^2$) tables; $q=8$ “currently not available”; `QECC-EA.php` → 404 | **CORRECTION E-8.1** |
| 5 of 12 comparable $q=4$ stabilizer entries meet the best known distance (all $d=2$); 7 are 1–2 below; $q=9$ entries are 1–2 below; **no record claimed** | T-228 + E-8.1 recomputation | `PAPER/PARAMETER_COMPARISON.md` | — | table of 13 retrieved bounds | CV |

## Checks performed in Task B (all ten requested items)

1. **Definitions consistent** — one notation sheet is fixed in §3 and used
   verbatim thereafter; the four regimes of Phase 1 §0 and the three regimes of
   Phase 5 §1 are reconciled (they are the same trichotomy, named twice).
2. **Correct assumptions** — every theorem in the manuscript restates its
   hypotheses; in particular T-192 (hull self-orthogonality) is stated **without**
   reflexivity or principality, and T-196/T-197 with their exact isotropy
   hypotheses.
3. **Left/right multiplication conventions** — re-checked in T-006, T-115,
   T-121…T-126, T-141; the failure lemma (T-006) is included in the manuscript
   precisely because the convention is not cosmetic.
4. **Correct scalar field for every dimension** — all dimensions are over
   $\mathbb F_q$; the only $\mathbb F_p$-statement is the commutation test
   (T-203), and it is flagged as such. Re-checked: no $p$-ary substitution
   appears anywhere.
5. **Correct pairing for every dual** — three distinct duals appear and are
   never confused: $C^{\perp_s}$ ($\theta_s$-pairing on $R^n$),
   $D^{\perp^{\widehat{}}_s}$ (transported Hankel form) and $D^{\perp_E}$
   (Euclidean, used by R2/R3). §6 states explicitly which is which.
6. **Every hull uses the established intersection** — $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$
   throughout; the Euclidean hull $H_E=D\cap D^{\perp_E}$ is a different object
   and is named separately.
7. **Every Gray-map identity uses the exact induced form** — only T-177's
   $J=I_{4n}\otimes H_t$ is used; the Bachoc variant (T-189) is quoted as a
   variant and never used in the main chain.
8. **Commutation requirements** — R1 abelian (T-193), R2 isotropic (T-196),
   R3 radical/hyperbolic-pair accounting (T-207); the $\mathbb F_p$-basis
   requirement (T-203) is applied to every certified code.
9. **Every parameter tuple recalculated from the construction** — yes:
   $N=4tn$, $k=\dim_{\mathbb F_q}D$, $h_E=\dim(D\cap D^{\perp_E})$, $c=k-h_E$,
   $K=N-k-h_E$, recomputed row by row in Part 6 of the Phase-7 script.
10. **Every exact distance has a matching certificate** — the distances quoted
    in the manuscript are exactly those the Phase-7 log reports as `yes` in the
    `exact` column; proved lower bounds are marked $\ge$ and their method printed.

## Special attention items (Task B)

| item | finding |
|---|---|
| **T-230** | Re-proved independently in Phase 8 from T-207; the reduction from the symplectic minimum to the classical coset minimum uses $\mathrm{swt}(a|b)\ge\max(\mathrm{wt}a,\mathrm{wt}b)$ and $(a|0)\in V^{\perp_\omega}\setminus V$ for $a\in D^{\perp_E}\setminus D$. **No gap.** Note it is proved for R2/R3; for R1 only the upper bound T-194 holds, and the manuscript says so. |
| **T-231** | The frontier is a *computational* statement over the scanned families; it is **not** claimed to be the true Pareto frontier of the framework. The manuscript says so (§8.6) and lists the excluded families. |
| **T-232** | The proof is complete and self-contained. Independence from EA-Singleton is demonstrated by $[[20,2,10;18]]_4$ ($K\le11$ vs $K\le20$). **No gap.** |
| **T-233** | Immediate from $c=k-h_E\le c_0$ and $K=N-k-h_E\ge K_0$; the manuscript states it only for $d\ge4$ as the brief requires, and notes it holds verbatim for any $d$ (the distance enters only through the *motivation*, not the inequality). This is flagged explicitly so that no reader infers a false converse. |
| **O-3.1** | **Split into two readings during the Phase-8 audit.** (a) “every hull of every right ideal is principal” — **refuted** by four exhaustive witnesses at $(4,2,2)$ plus two each at $(9,2,3)$ and $(4,2,4)$, with the structural confinement ($t\ge2$ and $p\mid n$); $(8,2,2)$ exhibits none. (b) “the hull of a **principal** code is principal” — **OPEN**: every known witness has $\mu_B(W)=3$ for the code itself, so it is a non-principal code. The manuscript states both (§5.2), refutes (a), and records (b) as open (Remark 5.6, open problem (vi)). |
| **E-7.1** | Recorded, not repaired. The manuscript states $c+K=N-2h_E$ and footnotes the Phase-6 error. |
| **Phase 5 generator-number correction** | $\mu_B=4$ refers to the code, not the hull. Stated in §5.4 of the manuscript with both numbers side by side. |
| **Char-2 obstruction** | Stated with its **exact** hypotheses ($p=2$ and $t$ **even**); the manuscript explicitly refuses to extend it to odd characteristic or to odd $t$, and gives the counter-congruences for $t=1,3,5$. |
| **E-8.1 (new in Phase 8)** | The $q=9$ coverage claim of T-215/T-228 is wrong. Recorded; the comparison recomputed. |

## Result of the audit

* Every claim in the manuscript resolves to a register row with a proof or a
  valid certificate.
* **No theorem was promoted** from `COMPUTATIONALLY VERIFIED ONLY` to `PROVED`.
* **Three corrections were recorded, not silently applied**: E-7.1 (Phase 6),
  the Phase 5 generator-number disambiguation, and the new **E-8.1** (Phase 8).
* Two conjectures (H-3A.1, H-3A.2) appear at the end of §5 labelled
  **conjectures** and are used nowhere.
* **Phase-8 audit additions:** Theorem 5.1(b) was corrected (the hull is
  $T$-invariant; principality is *not* claimed — an early draft asserted it
  with a non-proof). All manuscript tables were re-parsed from the Phase-7 log
  by `tools/build_parameter_tables.py` after a first draft reconstructed them
  from memory and did not match. |
