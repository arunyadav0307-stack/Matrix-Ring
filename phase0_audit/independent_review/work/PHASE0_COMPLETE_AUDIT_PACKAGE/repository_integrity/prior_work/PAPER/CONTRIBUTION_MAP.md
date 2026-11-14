# Phase 8 / Task A — Contribution map

**Rule applied.** Only results that are (i) **proved** in a committed file of
this repository, or (ii) certified by a **valid committed computational
certificate** (exhaustive, or a proved lower bound, with the method printed),
appear here. Exploratory computations, censuses of code counts and enumerator
distributions are **not** promoted to principal theorems; they appear, if at
all, as supporting remarks. Nothing is promoted from
`COMPUTATIONALLY VERIFIED ONLY` to `PROVED` in this phase.

Status labels are those of the register: **PROVED**, **PROVED + [EXH]**,
**COMPUTATIONALLY VERIFIED ONLY**, **IMPORTED RESULT**, **REFUTED**, **OPEN**.

---

## A1 — Algebraic framework

| # | contribution | label | source |
|---|---|---|---|
| A1.1 | The alphabet chain $A_t=\mathbb F_q[u]/\langle u^t\rangle \twoheadrightarrow R=M_2(A_t) \twoheadrightarrow R_n=R[X]/\langle X^n-1\rangle$, with $R_n\cong M_2(B)$, $B=A_t[X]/\langle X^n-1\rangle$ **commutative**. The matrix ring is non-commutative; the cyclic ambient is not a matrix ring over a commutative ring in a way that makes the code theory commutative, and this is exploited rather than avoided. | PROVED + IMPORTED (Morita) | T-004, T-005; Phase 1 §2.6, §3 |
| A1.2 | **Right-module convention.** Codes are **right** $R_n$-submodules. The plain product $\sum_i x_iy_i$ is the *wrong* pairing on a right module: its dual is not perfect (explicit $M_2(\mathbb F_2)$ counterexample, $C=uR$, $|C||C^\perp|=4\neq 16$). This is a proved failure lemma, not a convention choice. | PROVED (T-006, Prop. 5.1 of `PAIRING_COMPLETE_PROOFS.md`) + [EXH] | T-006 |
| A1.3 | **CRT decomposition of the coefficient ring of the cyclic ambient.** $B\cong\prod_j A_t[X]/\langle g_j^{e_j}\rangle$ with $g_j$ the irreducible factors of $X^n-1$ over $\mathbb F_q$; realised as an $\mathbb F_q$-linear ring isomorphism $\Psi$ with matrix and inverse, multiplicative on all pairs of basis elements. This replaces the earlier three-regime component routine and is what makes $n=5,6$ at $t=1$ and $n=3$ at $q=8$ reachable. | PROVED + [EXH] validated against the Phase-3B exhaustive BFS as a **set** on all 10 previously supported families | T-216 |
| A1.4 | **Component structure.** $B_j$ is a finite chain ring $\iff t=1$ or $e_j=1$; $\mu_B(W)=\max_j\mu_{B_j}(W_j)$; over a chain ring every submodule of $S^2$ is free of rank $\le 2$, hence $2$-generated. | PROVED (T-103, T-104, T-222) | Phase 2 Stage 2B; Phase 7 Part 5 |
| A1.5 | **Principality of right ideals, complete.** Every right ideal of $R_n$ is principal $\iff p\nmid n$ or $t=1$; and when $p\mid n$ and $t\ge2$ a non-principal right ideal exists. | PROVED (both directions) | T-105, T-106, T-107 |

## A2 — Galois duality and hull theory

| # | contribution | label | source |
|---|---|---|---|
| A2.1 | **The $\theta_s$-pairing.** $\theta_s=\sigma_s\circ(\cdot)^{\mathsf T}$, $\sigma_s(a)=a^{p^s}$ fixing $u$ and $X$, is an **anti**-automorphism of $R_n$ (not an automorphism, not an involution): $\theta_s^2=\sigma_{2s}$. The pairing $b_s(x,y)=\Lambda\big(\sum_i\theta_s(x_i)y_i\big)$ with $\Lambda=\lambda\circ\mathrm{tr}$ is additive, $\mathbb F_p$-bilinear, right-$\mathbb F_q$-linear, left-$\sigma_s$-semilinear, non-degenerate. | PROVED | T-002, T-003, T-115…T-120; `PAIRING_COMPLETE_PROOFS.md` §1–§2 |
| A2.2 | **Duality theorem (no principality needed).** $C^{\perp_s}$ is a **right** $R_n$-module; $C$ cyclic $\Rightarrow C^{\perp_s}$ cyclic; $|C|\cdot|C^{\perp_s}|=|R|^n$; $\dim C+\dim C^{\perp_s}=N$; $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$. | PROVED | T-007, T-008, T-133 |
| A2.3 | **Explicit dual formula.** For arbitrary (not necessarily principal) right ideals, $C^{\perp_s}=\operatorname{rev}\big(\operatorname{ann}_r(\theta_s(C))\big)$; the reversal $\operatorname{rev}$ is load-bearing **exactly when $n\ge3$** (it is the identity iff $n\le2$). | PROVED | T-124, T-125, T-126, T-127 |
| A2.4 | **The three regimes, distinguished.** General Galois (all $s$) $\supsetneq$ reflexive ($r\mid 2s$) $\supsetneq$ per-code $\widehat\sigma_{2s}$-invariance. The three are **pairwise non-equivalent**, with an explicit witness counting 14 of 92 codes at $(8,1,2,1)$. Reflexivity is the condition for $\mathrm{Hull}_s(C^{\perp_s})=\mathrm{Hull}_s(C)$ as subspaces; per-code invariance is strictly weaker and is a property of the individual code. | PROVED + [EXH] | T-155, T-157, T-158, T-186, T-190 |
| A2.5 | **Hull structure.** $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ is a right $R_n$-submodule, cyclic if $C$ is; Morita form $\mathrm{Hull}_s(C)=I_{W\cap W'}$; it is **not** in general a left ideal, hence not two-sided (explicit witness at $(4,1,1)$, $s=0$). Hull formula for arbitrary finitely generated right ideals. **No principality hypothesis anywhere.** | PROVED | T-009, T-139, T-144, T-145, T-148 |
| A2.6 | **O-3.1 is REFUTED: a Galois hull need not be principal.** Exhaustive over every code of every enumerable family; $\mu_B(\mathrm{Hull}_s)\in\{0,1,2,3\}$ and $\mu_B=3$ occurs (four witnesses at $(4,2,2)$), with explicit witnesses at $(9,2,3)$ and $(4,2,4)$ as well. Related: **$\mu_B(W)\le 2$ is FALSE over non-chain local rings**, and $\mu_B\ge3$ requires $t\ge2$ **and** $p\mid n$. | REFUTED (conjecture) / PROVED (structure) | T-173, T-222, T-224 |
| A2.7 | **Every Galois hull is self-orthogonal** (for the transported form), with **no** reflexivity and **no** principality hypothesis — a one-sided argument that never swaps the two slots. This is the engine of the whole quantum construction. | PROVED + [EXH] (226 hulls, 8 parameter sets) | T-192 |
| A2.8 | LCD / self-orthogonal / self-dual criteria in terms of $W(C)$ and $W(C^{\perp_s})$; and the statement that **no universal closed (gcd-type) hull formula exists**. | PROVED (non-existence in T-154) | T-154, T-161, T-162, T-163 |

## A3 — Gray-map compatibility

| # | contribution | label | source |
|---|---|---|---|
| A3.1 | **The map is the coefficient expansion**, $\varphi_n:R^n\to\mathbb F_q^{N}$, $N=4tn$, an $\mathbb F_q$-linear bijection commuting with the cyclic shift (which becomes the rotation by $4t$). It is **not** a ring homomorphism ($R$ is non-commutative) and this is measured, not assumed. | PROVED | T-176 |
| A3.2 | **The exact induced form.** The transported form is $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}Jv^{\mathsf T}$ with $J=I_{4n}\otimes H_t$, $H_t[a][b]=1\iff a+b=t-1$: a $\widehat\sigma_s$-**Hermitian form with a Hankel Gram matrix**. It is **not** Euclidean and **not** plain Hermitian unless $t=1$. Gram matrix verified element-wise, exact, on 18 instances. | PROVED + [EXH] | T-177 |
| A3.3 | **Duality and hull preservation**, by two independent routes (annihilator route and transported-form route), for **every** code and every $s$: $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$ and $\varphi_n(\mathrm{Hull}_s(C))=\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$. Valid on the $\mu_B=3$ (non-principal) witnesses. | PROVED + [EXH] (2427 codes across 9 families) | T-178, T-179 |
| A3.4 | **The image is quasi-cyclic of index $4t$ and co-index $n$**, invariant under the transported right $R_n$-action, and **not** cyclic in general. | PROVED | T-183 |
| A3.5 | **Weight limitations, stated exactly.** $w_{\mathrm H}\le w_{\mathrm{ent}}\le w_{\mathrm{coef}}\le t\,w_{\mathrm{ent}}$ and $w_{\mathrm H}\le\mathrm{wt}_{\mathrm H}\varphi_n\le 4t\,w_{\mathrm H}$, both sharp; $\varphi_n$ **is** a $d_{\mathrm{coef}}$/Hamming isometry. The claim “$\varphi_n$ preserves the ring-Hamming weight” is **REFUTED**. **No** map into any Hamming space is an isometry for the homogeneous weight (its values are non-integral). | PROVED / REFUTED | T-180, T-180b, T-181, T-182 |
| A3.6 | **Characteristic-two obstruction, exact hypotheses.** For $p=2$ and $t$ **even** the Hankel matrix $H_t$ is alternating, so **no** congruence $T^{\mathsf T}H_tT=I_t$ exists — exhaustive over all $4\times4$ matrices over $\mathbb F_4$ — and the Euclidean/CSS route is obstructed **in principle**, independently of the code. The domain is exactly “$t$ even”: congruences **do** exist for $t=1,3,5$. A congruence at $(9,2)$ exists but is **non-monomial**, so it is not a Hamming isometry and every distance must be recomputed. | PROVED + [EXH] | T-199, T-200; Phase 6 §5 |

## A4 — Quantum constructions

| # | contribution | label | source |
|---|---|---|---|
| A4.1 | **Physical-qudit count derived, not assumed.** $N_{\rm phys}=N=4tn$: one qudit of dimension $q$ carries one $\mathbb F_q$-coordinate, $\dim_{\mathbb F_q}R=4t$. No doubling to $2N$ (that is the symplectic bookkeeping space), no $p$-ary substitution; the alphabet is $\mathbb F_q$ throughout. | PROVED + [EXH] | T-198, T-201 |
| A4.2 | **Three routes, all proved in symplectic language** (not imported): **R1** Galois-native twisted graph $\mathcal C_T=\{(u\mid T_su)\}$, $[[N,N-k,d]]_q$, no congruence and no reflexivity needed; **R2** Euclidean/CSS, $[[N,N-2k,d]]_q$ (SO) and $[[N,2k-N,d]]_q$ (DC); **R3** entanglement-assisted $\mathcal C=D\times D$, $[[N,N-k-h_E,d;k-h_E]]_q$. | PROVED | T-193, T-196, T-197, T-201, T-207 |
| A4.3 | **Commutation must be tested on an $\mathbb F_p$-basis.** For the $[[16,4,3]]_4$ code the weight-1 operator $(0\mid e_0)$ commutes with all 12 $\mathbb F_q$-generators (because $\mathrm{Tr}_{\mathbb F_4/\mathbb F_2}(1)=0$) but not with all 24 elements of an $\mathbb F_p$-basis; the naive $\mathbb F_q$-generator test would report $d=1$ instead of $d=3$. | PROVED + [EXH] | T-203 |
| A4.4 | **The normalizer / stabilizer-quotient bookkeeping.** $K=N-\dim_{\mathbb F_q}\mathcal S-c$, $2c=\dim V-\dim\operatorname{rad}V$, $\operatorname{rad}V=H_E\oplus H_E$; for R3 the entanglement makes the **whole** group $V$ measurable, so an error is undetected exactly when it lies in $V^{\perp_\omega}\setminus V$ (not $\setminus\operatorname{rad}V$). | PROVED | T-207 |
| A4.5 | **A structural cap on R1.** $d_{R1}\le\min\mathrm{wt}(D^{\perp_E})$ because $(0\mid b)\in\mathcal C_T^{\perp_\omega}$ for every $b\in D^{\perp_E}$; measured value $\le2$ everywhere. This is why R1 is never the distance route. | PROVED + [EXH] | T-194 |
| A4.6 | **Exact distance certification, three independent methods.** M1 complete enumeration of the classical difference set; M2 increasing-weight support search (a left-kernel problem per support); M3 exhaustive search of the ambient quantum space $\mathbb F_q^{2N}$ in increasing **symplectic** weight, testing $v\in V^{\perp_\omega}$ and $v\notin V$. The certified code is the **exact** code found by the search (the image basis is carried through), so the certification cannot silently certify a different code with the same invariants. Stabilizer groups verified abelian on an $\mathbb F_p$-basis; $K$ and $c$ recomputed. | PROVED (methods) + [EXH] | T-225; Phase 6 §3; Phase 7 Part 6 |

## A5 — Quantum parameter improvement

| # | contribution | label | source |
|---|---|---|---|
| A5.1 | **Coset-distance characterisation (NEW, proved).** For every route, $d$ is the **minimum weight of the quotient (coset) code** $D^{\perp_E}/\mathrm{Hull}_E(D)$, of dimension $K=N-k-h_E$ and length $N$: $d=\min\{\mathrm{wt}(x):x\in D^{\perp_E}\setminus\mathrm{Hull}_E(D)\}$. Equivalently $d\ge4$ iff every vector of weight $\le3$ in $D^{\perp_E}$ lies in $\mathrm{Hull}_E(D)$. | **PROVED** | **T-230** (Phase 7 §3.0) |
| A5.2 | **Coset Singleton bound (NEW, proved).** $K+d\le N+1$, from the injectivity of puncturing $N-d+1$ coordinates on the $q^K$-element quotient. It is **neither** the EA Singleton bound **nor** implied by it ($[[20,2,10;18]]_4$: it gives $K\le11$ where EA-Singleton allows $K\le20$). Verified exhaustively on all 5055 codes with a distance, 0 violations (check H1). | **PROVED + [EXH]** | **T-232** |
| A5.3 | **Feasibility inequality (NEW, proved).** $d\ge4$ with $c\le c_0$ and $K\ge K_0$ forces $2k\le N+c_0-K_0$: the image dimension cannot exceed half the length by more than half the entanglement budget. Together with A5.1 this converts O-6.1 from a search question into a proved criterion. | **PROVED** | **T-233** |
| A5.4 | **Bookkeeping identities and an erratum.** $k$ even; $K-c=N-2k\equiv0\pmod 4$; $c+K=N-2h_E$; $c\ge2k-N$. **Erratum E-7.1:** Phase 6 §12 states $c+K=N-k$; that is wrong (only 2 of its own 25 rows satisfy it). No Phase-6 parameter changes. | PROVED + [EXH] (5055 codes) | T-219, E-7.1 |
| A5.5 | **O-6.1 resolved (quantitative frontier).** With $c\le4$ the best attainable distance is $d=4$ ($[[24,10,4;2]]_9$, $K=10$, $c=2$; a proved lower bound); $d=5$ first appears at $c=2$ with $K=6$; $d=6$ only at $c=10$ ($[[12,2,6;10]]_4$, $h_E=0$). Minimum entanglement per distance: $d=2:c=0$; $3:0$; $4:0$; $5:2$; $6:10$; $7:10$; $8:14$. | COMPUTATIONALLY VERIFIED ONLY | T-220 |
| A5.6 | **O-6.2 resolved.** Stabilizer best $d=4/2/1/1$ and EA best $d=10/6/4/2$ for $t=1,2,3,4$: for $t\ge3$ **every** stabilizer code found detects nothing at all ($d=1$). | COMPUTATIONALLY VERIFIED ONLY | T-221 |
| A5.7 | **New codes.** EA: $[[20,2,10;18]]_4$, $[[24,2,10;18]]_9$, $[[20,4,9;16]]_9$, $[[24,4,9;20]]_4$, $[[16,2,8;14]]_9$, $[[16,2,7;10]]_9$, $[[12,2,6;10]]_4$. Stabilizer: $[[24,8,4]]_9$ (SO) and $[[20,4,4]]_4$ (DC) — the **first stabilizer distance 4** in this framework, which **re-scopes** Phase 6's “no stabilizer point has $d\ge4$” to the families Phase 6 scanned ($N\le16$). From a **non-principal** ($\mu_B=3$) hull: $[[24,6,2;2]]_9$ and $[[32,8,2;4]]_4$ — included as witnesses that the phenomenon survives into quantum parameters, **not** for their parameters ($d=2$). | COMPUTATIONALLY VERIFIED ONLY (certified) | T-224, T-226; Phase 7 §12.1 |
| A5.8 | **The optimisation deliverable is the non-dominated set, not one champion.** 368 distinct tuples with a distance, 88 non-dominated, 280 dominated; dominance is $N\le N'$, $K\ge K'$, $d\ge d'$, $c\le c'$ with at least one strict, inside one alphabet. | COMPUTATIONALLY VERIFIED ONLY | **T-231** |
| A5.9 | **All 5055 codes with a distance satisfy** the EA quantum Singleton bound $N-K+c\ge2(d-1)$ **and** the EA quantum Hamming bound with effective dimension $K-c$: 0 violations of either. | COMPUTATIONALLY VERIFIED ONLY ([EXH]) | T-227 |

## Deliberately NOT presented as principal theorems

These are recorded in the register and in the phase deliverables, and are used
as supporting material only:

* code-count censuses and hull-dimension distributions (T-170, T-171, T-011);
* the four-counting-problems analysis (T-171) and the quasi-cyclic index counts;
* the homogeneous-weight closed form (T-181) — used only to state the
  isometry limitation (A3.5);
* the Bachoc-type map at $t=2$ (T-189) — a variant, not used in the final chain;
* the R1 cap measurement (A4.5 is the proved part; its measured values are not);
* the Pareto frontier as a table (T-231 replaces it by the proved-dominance
  frontier);
* O-7.1 … O-7.6 and O-6.5, O-6.6 — stated as open problems in §10 of the
  manuscript.
