# Phase 4 — Gray map compatibility and finite-field code construction

**Title of the programme (unchanged):** *Codes over the matrix ring $R=M_2(A_t)$,
$A_t=\mathbb F_q[u]/\langle u^t\rangle$: structure, duality and enumeration.*

**Script:** `04_COMPUTATION/phase4_gray_map_compatibility.py`
**Log:** `04_COMPUTATION/phase4_gray_map_log.txt`
(1106 lines, **463 checks, 463 PASS, 0 FAIL** — 311 `[EXH]`, 152 `[SMP]` —,
seed $20261110$, Python 3.11.2, two consecutive runs **byte-identical**,
log SHA-256 `55656a9d…9a92`).

---

## 0. Scope, conventions, and what is carried in

### 0.1 Standing conventions (unchanged from Phases 0–3B)

* $A_t=\mathbb F_q[u]/\langle u^t\rangle$ ($q=p^r$), $R=M_2(A_t)$,
  $R_n=R[X]/\langle X^n-1\rangle$, $B=A_t[X]/\langle X^n-1\rangle$, $R_n\cong M_2(B)$.
* An element of $A_t$ is written $a=\sum_{a=0}^{t-1}a_iu^i$ and stored as the coefficient
  tuple $(a_0,\dots,a_{t-1})$; an element of $R$ is a $4$-tuple of $A_t$-entries in the
  order $k=2i+j$ ($(1,1),(1,2),(2,1),(2,2)$); a **word** is $x=(x_0,\dots,x_{n-1})\in R^n$.
* **Codes are right ideals of $R_n$**; by Morita $C=I_W$ for a unique $B$-submodule
  $W\le B^2$.  $\theta_s=\sigma_s\circ(\text{transpose})$, $\sigma_s(c)=c^{p^s}$,
  $\sigma_s(u)=u$, $\operatorname{rev}(X)=X^{-1}$, and
  $C^{\perp_s}=\operatorname{rev}(\operatorname{ann}_r(\theta_s(C)))$ (Stage 2C Thm 3.8).
* $\lambda(a)=a_{t-1}$ (the coefficient of $u^{t-1}$), $\Lambda=\lambda\circ\operatorname{tr}$,
  $B_s(x,y)=\sum_e\theta_s(x_e)y_e$, $b_s(x,y)=\Lambda(B_s(x,y))$.
* $(Tx)_e=x_{e-1\bmod n}$ (Phase-1 convention; T-048: $T$ is a Hamming isometry).
* $r=\log_p q$; $s\in\{0,\dots,r-1\}$ is the Galois-shift parameter.

### 0.2 Imported results (used, not re-proved)

| ID | statement |
|---|---|
| T-001 | $\Lambda=\lambda\circ\operatorname{tr}$ is a symmetric, associative, non-degenerate (Frobenius) functional on $R$; it catches every non-zero one-sided ideal |
| T-037 | $b_s$ is non-degenerate; $\dim C+\dim C^{\perp_s}=4tn$ |
| Lemma 6.2 | $b_s(x,y\cdot a)=b_s(x,y)a$, $b_s(x\cdot a,y)=\theta_s(a)b_s(x,y)$: $b_s$ is $\sigma_s$-semilinear in $x$ and $\mathbb F_q$-linear in $y$ |
| Thm 6.8 | $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$; reflexivity $\iff r\mid 2s$ |
| Stage 2C Thm 3.8 | $C^{\perp_s}=\operatorname{rev}(\operatorname{ann}_r(\theta_s(C)))$ |
| Stage 3A Thm 3.3 | $\operatorname{Hull}_s(C)=I_{W\cap W'}$, $\dim\operatorname{Hull}_s(C)=2\dim_{\mathbb F_q}(W\cap W')$ |
| T-173 (3B) | O-3.1 is **false**: at $(4,2,2)$ exactly four codes have $\mu_B(\operatorname{Hull})=3$ (one at $s=0$, three at $s=1$); "hulls are principal" is banned as a hypothesis (D-024) |
| Greferath–Schmidt 1999 | for a finite **chain** ring $S$ with residue field $\mathbb F_q$ and length $m$, $(S,d_{\mathrm{Hom}})\hookrightarrow(\mathbb F_q^{q^{m-1}},d_{\mathrm{Ham}})$ (see §8) |

### 0.3 What Phase 4 does **not** claim

* **No CSS construction, no EAQECC construction, no quantum parameters, no manuscript.**
  Those stages are not started.
* No claim that the coefficient expansion is a *Gray* map in the metric sense: it is
  **not** an isometry for the ring-Hamming weight and **not** an isometry for the
  homogeneous weight (§2.4, §2.5).  It is an isometry only for the weight it defines.
* No claim that the image code is cyclic (it is quasi-cyclic of index $4t$; §5.3).
* No principality hypothesis is used anywhere (§4.3).
* Nothing sampled is called exhaustive: every `[EXH]` line is exhaustive over the family
  named in the line; every `[SMP]` line states the sample size.

### 0.4 The parameter sets

| $(q,t,n)$ | regime | $N=4tn$ | #codes | enumeration |
|---|---|---|---|---|
| $(4,1,1)$ | split, 1 comp. | 4 | 7 | exhaustive BFS |
| $(4,1,2)$ | chain | 8 | 33 | exhaustive BFS |
| $(4,2,1)$ | split, 1 comp. | 8 | 33 | exhaustive BFS |
| $(8,1,2)$ | chain | 8 | 93 | exhaustive BFS |
| $(9,1,2)$ | split, 2 comp. | 8 | 144 | exhaustive BFS ($|B^2|=6561$) |
| $(4,1,3)$ | split, 3 comp. | 12 | 343 | CRT product $7^3$ |
| $(9,2,1)$ | split, 1 comp. | 8 | 113 | exhaustive BFS ($|B^2|=6561$) |
| $(4,2,2)$ | **wild** | 16 | 1221 | exhaustive BFS |
| $(4,2,3)$ | split, 3 comp. | 24 | 400 sampled of $33^3=35\,937$ | CRT product, `[SMP]` |

$s$ runs over $\{0,1\}$ for $q=4,9$ and $\{0,1,2\}$ for $q=8$.
The nine families give **18 (family, $s$)-instances**; the four central identities of
Tasks C and D are verified on **every code of every instance**, i.e. on
$6+6+32+32+32+32+92\cdot3+143\cdot2+342\cdot2+112\cdot2+1220\cdot2+400\cdot2=5\,140$
code/instance pairs (four identities each).

---

## 1. Task A — the candidate maps

### 1.1 Definitions

The **baseline candidate** is the coefficient expansion

$$\varphi_A(a)=(a_0,\dots,a_{t-1})\in\mathbb F_q^{\,t},\qquad
\varphi_R(X)=\bigl(\varphi_A(X_0),\dots,\varphi_A(X_3)\bigr)\in\mathbb F_q^{\,4t},$$
$$\varphi_n(x)=\bigl(\varphi_R(x_0),\dots,\varphi_R(x_{n-1})\bigr)\in\mathbb F_q^{\,N},
\qquad N=4tn,$$

with the coordinate index
$$\varphi_n(x)_{(e\cdot4+k)t+a}=\text{the }u^a\text{-coefficient of the }(k)\text{-entry of }x_e .$$
(§1–§2 of the log: $\varphi_R$ is checked against the independently built flat coordinate
map of `ring_structure_checks` on all $|R|$ elements.)

Three variants are studied:

* $P$ — the permutation that **reverses the $t$ coefficients inside each $(e,k)$ block**;
  $\varphi^{\mathrm{rev}}=P\circ\varphi_n$;
* $\varphi^{\mathrm B}$ (only for $t=2$) — the **Bachoc-type** map
  $(a_0,a_1)\mapsto(a_0+a_1,\ a_1)$ on each $A_2$-entry, i.e. $\varphi^{\mathrm B}=S\varphi_n$
  with $S=I_{4n}\otimes\begin{pmatrix}1&1\\0&1\end{pmatrix}$;
* $\varphi^{T}=T\varphi_n$ for an $\mathbb F_q$-linear change of coordinates $T$ (§3.5).

### 1.2 What is measured (and what is true)

Every statement below is proved in §3.1–§3.2 or verified in Part A of the log.

| property | $\varphi_n$ | $\varphi^{\mathrm{rev}}$ | $\varphi^{\mathrm B}$ ($t=2$) |
|---|---|---|---|
| $\mathbb F_q$-linear | **yes** (T-176) | yes ($P$ is $\mathbb F_q$-linear) | yes |
| bijective | **yes** (T-176) | yes | yes |
| additive | yes `[EXH]` | yes | yes `[SMP]` |
| commutes with the shift: $\varphi(Tx)=\widehat T\varphi(x)$, $\widehat T=$ rotation by $4t$ | **yes** `[EXH]` on all $N$ basis words | yes ($P\widehat T=\widehat TP$ `[EXH]`) | yes `[SMP]` |
| a ring homomorphism | **no** ($R$ non-commutative; $\varphi_R(XY)\ne\varphi_R(YX)$ on the sampled pairs) | no | no |
| transported Gram matrix of $b_s$ | $J=I_{4n}\otimes H_t$ | $I_{4n}\otimes H_t$ ($=J$, see §3.5) | $I_{4n}\otimes(S^TH_2S)$ |
| weight relation | $\mathrm{wt}_{\mathrm H}(\varphi_n x)=w_{\mathrm{coef}}(x)$ | same ($P$ permutes coordinates) | $\ne w_{\mathrm{coef}}$ `[SMP]` |

Here $H_t$ is the **Hankel / reversal** matrix $H_t[a][b]=1\iff a+b=t-1$.

**The transport of the module structure.** $\varphi_n$ is $\mathbb F_q$-linear, not
$R$-linear — the target is not an $R$-module. What survives is:

* the **left regular representation**: $\varphi_R(aX)=M_L(a)\varphi_R(X)$, and
  $a\mapsto M_L(a)$ is an **injective** $\mathbb F_q$-algebra homomorphism
  $R\hookrightarrow M_{4t}(\mathbb F_q)$ (T-188; additivity, multiplicativity and injectivity
  checked `[EXH]`);
* for a code, $C$ is invariant under right multiplication by every $a\in R_n$, hence
  $\varphi_n(C)$ is invariant under the conjugate operator $\varphi_n\rho_a\varphi_n^{-1}$.

---

## 2. Task B — the weight structure

### 2.1 Four weights on $R^n$

| symbol | definition |
|---|---|
| $w_{\mathrm H}(x)$ | $\#\{e:x_e\ne0\}$ — the **ring-Hamming** weight (the weight of T-048) |
| $w_{\mathrm{ent}}(x)$ | $\#\{(e,k):(x_e)_k\ne0\}$ — non-zero $A_t$-entries |
| $w_{\mathrm{coef}}(x)$ | $\#\{(e,k,a):(x_e)_{k,a}\ne0\}$ — non-zero $\mathbb F_q$-coefficients |
| $w_{\mathrm{rank}}(x)$ | $\sum_e\operatorname{rank}_{\mathbb F_q}(x_e\bmod u)$ — the matrix (rank) weight |

### 2.2 The chain of inequalities (T-180)

For every $x\in R^n$: $w_{\mathrm H}\le w_{\mathrm{ent}}\le 4w_{\mathrm H}$,
$w_{\mathrm{ent}}\le w_{\mathrm{coef}}\le t\,w_{\mathrm{ent}}$, hence

$$\boxed{\;w_{\mathrm H}(x)\;\le\;\mathrm{wt}_{\mathrm H}\bigl(\varphi_n(x)\bigr)\;\le\;4t\,w_{\mathrm H}(x)\;}$$

and both bounds are attained (verified `[EXH]` over all words for $(4,1,1)$, $(4,1,2)$,
$(4,2,1)$, $(9,1,1)$ and `[SMP]` elsewhere).  Consequently
$\varphi_n$ is an **isometry** $(R^n,d_{\mathrm{coef}})\to(\mathbb F_q^{N},d_{\mathrm{Ham}})$
for $d_{\mathrm{coef}}(x,y)=w_{\mathrm{coef}}(x-y)=\mathrm{wt}_{\mathrm H}(\varphi_nx-\varphi_ny)$
— but this is the weight *defined by the map*, not a preserved pre-existing metric.

**$\varphi_n$ is not a ring-Hamming isometry.** The number of words with
$\mathrm{wt}_{\mathrm H}(\varphi_nx)\ne w_{\mathrm H}(x)$ is $243/256$ at $(4,1,1)$,
$65\,511/65\,536$ at $(4,2,1)$, and $2000/2000$ on the sampled words of the larger families.
Typical witness at $(4,2,1)$: $w_{\mathrm H}=1,\ w_{\mathrm{ent}}=1,\ w_{\mathrm{coef}}=2$.

### 2.3 The homogeneous weight on $R$ (construction)

$R=M_2(A_t)$ is a **finite Frobenius ring** with Frobenius functional $\Lambda=\lambda\circ\operatorname{tr}$
(T-001), so $\chi(X)=\exp\!\bigl(2\pi i\,\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(\Lambda(X))/p\bigr)$
is a generating character of $(R,+)$ and the **homogeneous weight** is

$$w_{\mathrm{hom}}(X)=1-\frac1{|R^\times|}\sum_{u\in R^\times}\chi(Xu).$$

The script computes this in **exact integer arithmetic**: writing
$c_m=\#\{u\in R^\times:\operatorname{Tr}(\Lambda(Xu))=m\}$, the sum
$\sum_m c_m\zeta_p^{\,m}$ is rational iff $c_1=\dots=c_{p-2}=c_{p-1}$, and then it equals
$c_0-c_{p-1}\in\mathbb Z$ (the rationality is re-checked for every $X$ and reported as a
check).  The sum over $R^\times$ is obtained from the sum over the **non-units** through
character orthogonality, $S(X)=|R|\,[X=0]-\sum_{u\notin R^\times}\chi(Xu)$, which makes the
exhaustive computation feasible for $|R|\le6561$.

### 2.4 The homogeneous weight on $R=M_2(\mathbb F_q)$ — closed form (T-181)

**Theorem.** Let $t=1$, $R=M_2(\mathbb F_q)$. Then
$$w_{\mathrm{hom}}(X)=\begin{cases}
0,&X=0,\\[2pt]
1+\dfrac1{q^2-1},&\operatorname{rank}X=1,\\[6pt]
1-\dfrac1{(q-1)^2(q+1)},&X\in R^\times .
\end{cases}$$

*Proof.* $S(X):=\sum_{U\in R^\times}\chi(XU)$.
(i) $X=0$: $S=|R^\times|$, $w=0$.
(ii) $X$ a unit: $U\mapsto XU$ permutes $R^\times$, so $S=\sum_{V\in R^\times}\chi(V)=
\sum_{V\in\mathrm{GL}_2(\mathbb F_q)}\psi_0(\operatorname{tr}V)=q$, the standard $\mathrm{GL}_2$
Gauss sum (imported identity; corroborated below for $q=4,8,9$); with
$|R^\times|=q(q-1)^2(q+1)$ this gives the stated value.
(iii) $\operatorname{rank}X=1$: the substitution $U\mapsto A^{-1}UB$ ($A,B\in\mathrm{GL}_2$,
$\det(AB)=1$) is a bijection of $R^\times$ and replaces $X$ by $AXB$, so we may take
$X=E_{11}$; then $S=\sum_{U\in R^\times}\psi_0(U_{11})$ and, counting invertible matrices
with a prescribed $(1,1)$-entry ($q^3-q^2$ for each non-zero value, $q(q-1)^2$ for zero),
$S=-(q^3-q^2)+q(q-1)^2=-q(q-1)$, whence
$w=1+\frac{q(q-1)}{q(q-1)^2(q+1)}=1+\frac1{q^2-1}$. $\square$

**Verification** `[EXH]` over the whole ring for $q=4$ ($|R|=256$), $q=8$ ($4096$),
$q=9$ ($6561$): the closed form matches on every element; the mean of $w_{\mathrm{hom}}$ over
$R$ is exactly $1$; $w_{\mathrm{hom}}$ is $\mathbb F_q^{\times}$-homogeneous and invariant under
left multiplication by units; the triangle inequality holds on $60^2$ pairs.

| $q$ | $w_{\mathrm{hom}}$ on units | on rank $1$ | denominators |
|---|---|---|---|
| 4 | $44/45$ (180 elements) | $16/15$ (75) | $\{1,15,45\}$ |
| 8 | $440/441$ (3528) | $64/63$ (567) | $\{1,63,441\}$ |
| 9 | $639/640$ (5760) | $81/80$ (800) | $\{1,80,640\}$ |

For $t=2$, $q=4$ (sampled, `[SMP]`) the values are $\{0,\ 1,\ 16/15,\ 44/45\}$:
$w_{\mathrm{hom}}(X)=1$ for every $X\notin uM_2(A_2)$, and for $X=uY\ne0$ it equals the
$M_2(\mathbb F_4)$-value of $Y$ (e.g. $uI\mapsto44/45$, $uE_{11}\mapsto16/15$).
A closed form for general $t\ge2$ over $M_2(A_t)$ is **not** claimed (§11, O-4.3).

### 2.5 Obstruction: no Hamming isometry for the homogeneous weight (T-182)

**Theorem.** There is **no** map $\psi:R\to\mathbb F_q^{\,N}$ (for any $N$, linear or not)
with $d_{\mathrm{Ham}}(\psi(X),\psi(Y))=w_{\mathrm{hom}}(X-Y)$ for all $X,Y$.

*Proof.* Hamming distances are integers; by §2.4, $w_{\mathrm{hom}}$ takes the value
$1+\frac1{q^2-1}\notin\mathbb Z$ (for every $q\ge2$), attained on any rank-one matrix.
Taking $Y=0$ and $X$ of rank $1$ gives a contradiction. $\square$

The same argument applies to $R^n$ with the position-wise extension
$d_{\mathrm{hom}}(x,y)=\sum_ew_{\mathrm{hom}}(x_e-y_e)$.
For a **rescaled** weight $\gamma\,w_{\mathrm{hom}}$ with an $\mathbb F_q$-linear isometry the
average-over-$R$ identity forces $N=\gamma q/(q-1)$, i.e. integrality constraints on $\gamma$;
for $q=4$ this forces $N\equiv0\pmod{15}$ and $N\ge4t$.  Whether such a map exists is
**OPEN** (§11, O-4.4); the necessary conditions recorded in the log are: integrality,
$\mathbb F_q^{\times}$-homogeneity (holds), the triangle inequality (holds `[EXH]`),
and $N\ge\log_q|R|$.

**Remark (honest positioning).** For a *chain* ring $A_t$ the Greferath–Schmidt theorem
gives an isometry $(A_t,d_{\mathrm{Hom}})\hookrightarrow(\mathbb F_q^{q^{t-1}},d_{\mathrm{Ham}})$;
$R=M_2(A_t)$ is **not** a chain ring, and that theorem says nothing about $R$.
The obstruction above shows the naive extension to $R$ is impossible for the *normalised*
homogeneous weight.

---

## 3. Task C — the finite-field form transported by $\varphi_n$ (central task)

### 3.1 Definition of the target form

Since $\varphi_n$ is an $\mathbb F_q$-linear bijection, the form

$$\boxed{\;\langle u,v\rangle^{\widehat{}}_s:=b_s\bigl(\varphi_n^{-1}(u),\varphi_n^{-1}(v)\bigr),
\qquad u,v\in\mathbb F_q^{N}\;}$$

is the **only** form for which $\varphi_n$ is a form-isometry, and the correspondence
$y\in C^{\perp_s}\iff\varphi_n(y)\in\varphi_n(C)^{\perp^{\widehat{}}_s}$ holds *by
construction*. The whole content of Task C is therefore to **identify that form
explicitly** and to verify the correspondence by a **second, independent route**.
Nothing is assumed Euclidean.

### 3.2 The Gram matrix (T-177)

**Theorem.** $\operatorname{tr}\bigl(\theta_s(X)Y\bigr)=\sum_{k,l}\sigma_s(X_{kl})Y_{kl}$
(the transpose disappears in the trace), hence
$$b_s(x,y)=\sum_{e}\sum_{k,l}\lambda\bigl(\sigma_s((x_e)_{kl})\,(y_e)_{kl}\bigr)
=\sum_{e,k}\sum_{a=0}^{t-1}\sigma_s\bigl((x_e)_{k,a}\bigr)\,(y_e)_{k,t-1-a},$$
so in the standard basis of $\mathbb F_q^{N}$
$$\langle u,v\rangle^{\widehat{}}_s=u^{[s]}\,J\,v^{\mathsf T},\qquad
J\;=\;I_{4n}\otimes H_t,\qquad u^{[s]}=(u_i^{p^s}) .$$

*Proof.* $\operatorname{tr}(\sigma_s(X^{\mathsf T})Y)=\sum_{i,j}\sigma_s(X_{ji})Y_{ji}$, and
$(i,j)\mapsto(j,i)$ is a bijection, giving $\sum_{k,l}\sigma_s(X_{kl})Y_{kl}$. Then
$\lambda(\sigma_s(u^a)u^b)=\lambda(u^{a+b})=[a+b=t-1]$, and $b_s$ is $\sigma_s$-semilinear in
the first slot and $\mathbb F_q$-linear in the second. $\square$

**Verified** `[EXH]` for all 18 instances: the Gram matrix computed element-wise from
$b_s$ (i.e. $J_{ij}=b_s(\varepsilon_i,\varepsilon_j)$ for the $N$ standard basis words) equals
$I_{4n}\otimes H_t$ **exactly**; $\operatorname{rank}J=N$ (non-degeneracy);
$\langle\varphi_nx,\varphi_ny\rangle^{\widehat{}}_s=b_s(x,y)$ on $120^2$ pairs
(`[EXH]` where $|R^n|\le70\,000$, `[SMP]` otherwise).

**The target form is a $\widehat\sigma_s$-Hermitian form with a Hankel Gram matrix —
not the Euclidean form, and not the plain Hermitian form, unless $t=1$.**

### 3.3 The duality correspondence (T-178, central result)

**Theorem.** For every code $C\le R^n$ (right ideal of $R_n$) and every $s$,
$$\varphi_n\bigl(C^{\perp_s}\bigr)=\varphi_n(C)^{\perp^{\widehat{}}_s},
\qquad\text{equivalently}\qquad
y\in C^{\perp_s}\iff\langle u,\varphi_n(y)\rangle^{\widehat{}}_s=0\ \ \forall u\in\varphi_n(C).$$

*Proof.* $\varphi_n$ is bijective and $\langle\cdot,\cdot\rangle^{\widehat{}}_s$ is its
transport, so for $y$: $y\in C^{\perp_s}\iff b_s(x,y)=0\ \forall x\in C
\iff\langle\varphi_nx,\varphi_ny\rangle^{\widehat{}}_s=0\ \forall x\in C
\iff\varphi_n(y)\in\varphi_n(C)^{\perp^{\widehat{}}_s}$. $\square$

**Two independent computational routes** (Part C of the log, per family):

1. **annihilator route** — $C^{\perp_s}=I_{W'}$ with $W'=\bigcap_i\ker\theta_s(\operatorname{rev}g_i)$
   (Stage 2C Thm 3.8), which never uses the transported form or $J$;
2. **transported-form route** — the nullspace of $\sigma_s(\text{basis of }\varphi_n(C))\cdot J$.

The two are compared as subspaces (reduced row-echelon form). Result:

| instance | codes | $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$ |
|---|---|---|
| $(4,1,1,0/1)$ | 6 | 6 / 6 `[EXH]` |
| $(4,1,2,0/1)$ | 32 | 32 / 32 `[EXH]` |
| $(4,2,1,0/1)$ | 32 | 32 / 32 `[EXH]` |
| $(8,1,2,0/1/2)$ | 92 | 92 / 92 `[EXH]` |
| $(9,1,2,0/1)$ | 143 | 143 / 143 `[EXH]` |
| $(4,1,3,0/1)$ | 342 | 342 / 342 `[EXH]` |
| $(9,2,1,0/1)$ | 112 | 112 / 112 `[EXH]` |
| $(4,2,2,0/1)$ | 1220 | 1220 / 1220 `[EXH]` |
| $(4,2,3,0/1)$ | 400 | 400 / 400 `[SMP]` |

Also `[EXH]`: $\dim\varphi_n(C)+\dim\varphi_n(C)^{\perp^{\widehat{}}_s}=N$ for every code
(0 violations anywhere), and $\varphi_n(\sigma_sx)=\widehat\sigma_s(\varphi_nx)$ `[SMP]`.

### 3.4 Symmetry: three different notions (T-186)

These are genuinely different and the phase distinguishes them explicitly:

| | property | holds iff | verified |
|---|---|---|---|
| (a) | $\langle v,u\rangle^{\widehat{}}=\sigma_s\bigl(\langle u,v\rangle^{\widehat{}}\bigr)$ | $r\mid 2s$ | `[EXH]` per instance |
| (b) | the orthogonality **relation** is symmetric ($\langle u,v\rangle=0\Rightarrow\langle v,u\rangle=0$) — *reflexivity* | $r\mid 2s$ | `[EXH]` per instance |
| (c) | the form is symmetric **as a value** | $r\mid s$ | `[EXH]` per instance |

(Proof of (a): $\langle v,u\rangle=\sum\sigma_s(v_i)(Ju)_i$ and
$\sigma_s(\langle u,v\rangle)=\sum\sigma_{2s}(u_i)\sigma_s(v_i)J_{ij}$, equal for all $u,v$
iff $\sigma_{2s}=\mathrm{id}$. (b) follows from (a) and the converse is by counting
dimensions: $\dim C^{\perp\perp}=\dim\sigma_{2s}(C)=\dim C$. (c): take $u,v$ supported on one
coordinate.)

### 3.5 Can the target form be made "standard"? — a trade-off (T-185)

A natural wish is that the target form be the **plain** $\widehat\sigma_s$-Hermitian form
$\sum_i\sigma_s(u_i)v_i$ (Gram $I$), because that is what CSS/EA constructions consume.
Findings:

* $J=I$ $\iff$ $t=1$ `[EXH]`; the form is Euclidean $\iff$ ($t=1$ **and** $r\mid s$);
  plain $\widehat\sigma_s$-Hermitian $\iff t=1$ `[EXH]` (T-184).  The measured counts of codes
  for which the Euclidean (resp. plain-Hermitian) orthogonal of the image differs from
  $\varphi_n(C^{\perp_s})$ are in §7.
* **A permutation of coordinates cannot do it.** Reversing the coefficients inside each
  block is $P=I_{4n}\otimes H_t=J$, and $P^{\mathsf T}JP=J$: the $u$-adic pairing really does
  pair $a$ with $t-1-a$, and no relabelling changes that. (Checked `[EXH]`: $PJP=I$ fails
  for $t\ge2$; the earlier "reversal" conjecture is **refuted** and recorded here.)
* **A general $\mathbb F_q$-linear change of coordinates $T$** needs $T^{\mathsf T}JT=I$
  (bilinear case $r\mid s$) resp. $\sigma_s(T)^{\mathsf T}JT=I$ (sesquilinear case):
  * $q$ **even**, $t$ **even**: $J$ is alternating and $I$ is not $\Rightarrow$ **impossible**
    `[EXH]` (checked: "$J$ alternating $\iff t$ even");
  * $(q,t)=(4,2)$: an **exhaustive** search over all $4^4=256$ matrices finds **no**
    $T$ with $T^{\mathsf T}H_2T=I_2$;
  * $(q,t)=(9,2)$ ($q\equiv1\bmod4$): such a $T$ **exists**, $I_{4n}\otimes T$ **commutes
    with the block shift** (so the image stays quasi-cyclic of index $4t$) and satisfies
    $\sigma_s(T)^{\mathsf T}JT=I$ for $s=1$ as well — but $T$ is **not monomial**, hence
    $\varphi^{T}=T\varphi_n$ does **not** preserve the Hamming weight.
  * the $t=1$ cases are trivial ($J=I$).
* **Conclusion (trade-off).** For $t\ge2$ one may have *either* the standard Gram matrix
  *or* Hamming-weight preservation, but the log shows no map that has both; a
  weight-preserving (monomial) $T$ would have to satisfy $T^{\mathsf T}H_tT=I_t$ with $T$
  monomial, and no such $T$ exists for the tested $t\ge2$ cases.  General $(q,t)$: **OPEN**
  (O-4.2).

---

## 4. Task D — hull compatibility

### 4.1 The identity (T-179)

**Theorem.** For every code $C\le R^n$ and every $s$,
$$\boxed{\;\varphi_n\bigl(\operatorname{Hull}_s(C)\bigr)
=\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}\;}$$
and $\dim_{\mathbb F_q}\varphi_n(\operatorname{Hull}_s(C))=\dim_{\mathbb F_q}\operatorname{Hull}_s(C)$.

*Proof.* $\varphi_n$ is a bijection between the underlying $\mathbb F_q$-spaces, and a
bijection preserves intersections:
$\varphi_n(C\cap C^{\perp_s})=\varphi_n(C)\cap\varphi_n(C^{\perp_s})$. Now apply T-178.
Dimension is preserved by injectivity. $\square$

Two independent routes in the log: (1) $\operatorname{Hull}_s(C)=I_{W\cap W'}$ by the Morita
/ annihilator route (Stage 3A Thm 3.3), converted to $R^n$ by $\iota^{-1}$ and then expanded;
(2) the intersection $\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$ computed directly
in $\mathbb F_q^{N}$.  They agree on **every code of every instance** — the table of §3.3
holds verbatim for the hull identity (same counts, 0 mismatches).

### 4.2 The hull of the image *is* the image of the hull

Because $\varphi_n$ is a form-isometry, the hull of the image code computed **in
$\mathbb F_q^{N}$** with the transported form equals $\varphi_n(\operatorname{Hull}_s(C))$
— so all of the Phase-3B hull theory transports verbatim: LCD, self-orthogonal and
self-dual counts, and the hull dimension, are the same numbers on both sides.

### 4.3 Non-principal hulls are included (O-3.1 family)

The four witnesses of T-173 (the only codes in the Phase-3B families with
$\mu_B(\operatorname{Hull})=3$) were re-identified inside the Phase-4 sweep at $(4,2,2)$ and
the hull identity verified for each of them:

| $s$ | $\dim C$ | $\dim\operatorname{Hull}$ | $\mu_B$ | generators of $W\cap W'$ over $B$ | identity holds |
|---|---|---|---|---|---|
| 0 | 8 | 8 | 3 | $((1,1,0,0),(1,1,0,0))$, $((0,0,1,0),(0,0,0,1))$, $((0,0,0,1),(0,0,0,1))$ | **yes** |
| 1 | 8 | 8 | 3 | as above; and with the second component scaled by $2$, resp. $3$ | **yes** (3 witnesses) |

**No principality hypothesis is used**: the proof of T-179 uses only bijectivity and T-178,
and the log confirms the identity on the $\mu_B=3$ hulls (`[EXH]`, 1 witness at $s=0$,
3 at $s=1$).  The $\mu_B$-distribution of the hulls is reported per instance in the log.

---

## 5. Task E — the image codes $\varphi_n(C)\le\mathbb F_q^{4tn}$

### 5.1 Elementary parameters (T-183)

* $\varphi_n(C)$ is $\mathbb F_q$-**linear** of length $N=4tn$ and
  $\dim_{\mathbb F_q}\varphi_n(C)=\dim_{\mathbb F_q}C$ (injectivity).
* $\varphi_n(Tx)=\widehat T\varphi_n(x)$ with $\widehat T$ the rotation by $4t$ coordinates,
  hence **every image is invariant under $\widehat T$**: the image is **quasi-cyclic of
  index $4t$ and co-index $n$** `[EXH]` — verified on every code of every instance
  (0 violations).
* $\varphi_n(C)$ is invariant under the transported right $R_n$-action
  $\varphi_n\rho_a\varphi_n^{-1}$ for every $a\in R_n$ (transport of the module structure;
  not separately instrumented).

### 5.2 The image is *not* cyclic in general

The number of codes whose image is invariant under the coordinate shift by $1$:

| instance | codes | images invariant under shift by 1 |
|---|---|---|
| $(4,1,1)$ | 6 | 2 (both $s$) |
| $(4,1,2)$ | 32 | 4 |
| $(4,2,1)$ | 32 | 2 |
| $(8,1,2)$ | 92 | 4 |
| $(9,1,2)$ | 143 | 15 |
| $(4,1,3)$ | 342 | 26 |
| $(9,2,1)$ | 112 | 3 |
| $(4,2,2)$ | 1220 | **4** |
| $(4,2,3)$ | 400 | **0** |

So cyclicity is the exception, not the rule; the quasi-cyclic index $4t$ is the correct
structural statement. (Consistent with the chain-ring literature, where Gray images of
cyclic/constacyclic codes are quasi-cyclic — §8 — but here the index carries the extra
factor $4$ from $M_2$.)

### 5.3 Minimum distances

$d_{\mathrm H}(\varphi_n C)=\min_{0\ne x\in C}w_{\mathrm{coef}}(x)$ versus the ring-Hamming
distance $d^R_{\mathrm H}(C)=\min_{0\ne x\in C}w_{\mathrm H}(x)$; by §2.2
$d^R_{\mathrm H}(C)\le d_{\mathrm H}(\varphi_nC)\le 4t\,d^R_{\mathrm H}(C)$.
Measured (all codes with $|C|\le4100$, sampled to 120 codes in the three largest families):

| instance | codes compared | $d_{\mathrm H}(\varphi_nC)=d^R_{\mathrm H}(C)$ | examples |
|---|---|---|---|
| $(4,1,1)$ | 6 | 3 | $(1,1),(2,1)$ |
| $(4,1,2)$ / $(4,2,1)$ | 31 | 16 | $(2,2),(4,2)$ |
| $(8,1,2)$ | 82 | 26 | $(2,2),(4,2)$ |
| $(9,1,2)$ | 20 | 4 | |
| $(4,1,3)$ | 120 `[SMP]` | 48 / 39 | $(3,3),(6,3)$ |
| $(4,2,2)$ | 120 `[SMP]` | 75 / 80 | $(3,2),(4,2)$ |
| $(9,2,1)$ | 10 | 2 | |
| $(4,2,3)$ | 8 | 5 | |

**Distances are bounded, not preserved.** The image distance is a genuine new parameter;
it is never claimed to equal the ring distance.

---

## 6. Task F — quantum-relevant sufficient conditions (recorded, not used)

No CSS/EAQECC is constructed and no quantum parameter is derived. What Phase 4
*establishes* — and what a later phase may consume — is the following list. Each item is
proved above and verified in the log (counts per instance in §3.3, §5.2, and the
"NEGATIVE CONTROL" lines).

1. **F1 — finite-field ambient.** $\varphi_n(C)$ is an $\mathbb F_q$-linear $[4tn,\ k,\ d]_q$
   code with $k=\dim_{\mathbb F_q}C$ and $d=d_{\mathrm H}(\varphi_nC)$ computable from
   $w_{\mathrm{coef}}$ (§5.1, §5.3).
2. **F2 — the form is explicit and non-degenerate.**
   $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$; non-degenerate
   with $\dim U+\dim U^{\perp^{\widehat{}}_s}=N$ (§3.2).
3. **F3 — duality is preserved.** $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$
   (T-178). Consequences: $C$ self-orthogonal $\Rightarrow$ $\varphi_n(C)$ self-orthogonal;
   $C$ self-dual $\Rightarrow$ $\varphi_n(C)$ self-dual; $C$ LCD $\Rightarrow$ $\varphi_n(C)$
   LCD — all with respect to the transported form.
4. **F4 — hulls are preserved.** $\varphi_n(\operatorname{Hull}_s(C))=
   \varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$ (T-179), with no principality
   hypothesis; the hull dimension needed by an EA construction is therefore readable
   directly from the image.
5. **F5 — the reflexive case is available.** When $r\mid 2s$ the transported form has a
   symmetric orthogonality relation (§3.4), which is the prerequisite for a "dual-containing"
   argument; when $r\nmid2s$ it is not, and $\bigl(\varphi_n(C)^{\perp^{\widehat{}}_s}\bigr)^{\perp^{\widehat{}}_s}
   =\widehat\sigma_{2s}(\varphi_n(C))$ (T-187, from Thm 6.8 and
   $\varphi_n\sigma_s=\widehat\sigma_s\varphi_n$).
6. **F6 — Euclidean target only in the trivial corner.** The transported form is Euclidean
   exactly when $t=1$ and $r\mid s$; otherwise a CSS-type step in $\mathbb F_q^{N}$ must
   either use the $\widehat\sigma_s$-Hermitian-with-Hankel form, or apply the coordinate
   change of §3.5 (which costs Hamming-weight preservation).
7. **F7 — extra symmetry.** The image is quasi-cyclic of index $4t$ (§5.1), which is
   inherited structure a construction may exploit; it is **not** cyclic in general (§5.2).
8. **F8 — obstruction to the classical route.** The classical "$\varphi$ is a Lee/homogeneous
   isometry" route to quantum codes is **unavailable here**: no Hamming isometry exists for
   the homogeneous weight on $R$ (T-182). Any later construction must carry distances
   through the $w_{\mathrm{coef}}$ bounds of §2.2 instead.

Measured illustration of F6 (counts of self-orthogonal codes, transported form vs. Euclidean
form, over the nonzero codes): $(4,1,2,1)$: 12 vs 10; $(4,1,3,1)$: 63 vs 35;
$(4,2,2,0)$: 356 vs 56; $(4,2,2,1)$: 234 vs 56; $(9,1,2,1)$: 24 vs 8; $(9,2,1,1)$: 23 vs 4.
Using the wrong (Euclidean) target loses most self-orthogonal codes.

---

## 7. Task G — validation methodology

### 7.1 Two independent routes for every critical identity

| identity | route 1 | route 2 |
|---|---|---|
| $C^{\perp_s}$ | annihilator / $\operatorname{rev}$ (Stage 2C Thm 3.8) — never uses $J$ | nullspace of $\sigma_s(\varphi_n(C))\cdot J$ in $\mathbb F_q^{N}$ |
| $\operatorname{Hull}_s(C)$ | Morita intersection $I_{W\cap W'}$ (Stage 3A Thm 3.3) | intersection $\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$ in $\mathbb F_q^{N}$ |
| the Gram matrix $J$ | element-wise $b_s(\varepsilon_i,\varepsilon_j)$ | closed form $I_{4n}\otimes H_t$ |
| $w_{\mathrm{hom}}$ | generating character over $R^\times$ | character orthogonality (sum over non-units) + closed form |

### 7.2 Negative controls (all reported in the log, all must fail and do)

| control | result |
|---|---|
| Euclidean orthogonal of the image $=\varphi_n(C^{\perp_s})$ | **fails** unless $t=1$ and $r\mid s$: e.g. 26/32 at $(4,2,1,0)$, 1188/1220 at $(4,2,2,0)$, 308/342 at $(4,1,3,1)$; and holds (0 mismatches) exactly at $s=0$ for every $t=1$ family |
| plain $\widehat\sigma_s$-Hermitian (Gram $I$) orthogonal $=\varphi_n(C^{\perp_s})$ | **fails** for $t\ge2$: 26/32 at $(4,2,1,0)$, 1188/1220 at $(4,2,2,0)$, 101/112 at $(9,2,1,0)$; holds (0) for every $t=1$ family |
| $\varphi_n$ preserves the ring-Hamming weight | **fails** (§2.2) |
| the image is cyclic | **fails** in general (§5.2) |
| $\varphi_n$ is a ring homomorphism / $R$-linear | **fails** ($R$ is non-commutative; the target is not an $R$-module) |
| a Hamming isometry exists for $w_{\mathrm{hom}}$ | **fails** (T-182) |
| the coefficient-reversal $P$ makes the Gram the identity | **fails** for $t\ge2$ (§3.5) |
| the Bachoc-type map is a $w_{\mathrm{coef}}$-isometry | **fails** (361/500 and 387/500 words differ) |

### 7.3 Reproduction

```
cd 04_COMPUTATION && python3 phase4_gray_map_compatibility.py
```
135 s, seed 20261110, log `phase4_gray_map_log.txt` (1106 lines, 463 checks, 0 FAIL,
311 `[EXH]` / 152 `[SMP]`); timing lines are written to stdout only, so two consecutive
runs are **byte-identical** (SHA-256 `55656a9d…9a92`).

---

## 8. Task H — literature and novelty

### 8.1 What exists (verified through web search; the repo bibliography was thin here)

| source | content | distance to Phase 4 |
|---|---|---|
| Greferath–Schmidt, *Gray isometries for finite chain rings*, IEEE IT **45** (1999) 2522–2524 | $(S,d_{\mathrm{Hom}})\hookrightarrow(\mathbb F_q^{q^{m-1}},d_{\mathrm{Ham}})$ for a finite **chain** ring $S$, residue field $\mathbb F_q$, length $m$ | **chain rings only** — does not apply to $R=M_2(A_t)$ |
| Constantinescu–Heise; Honold; Greferath–O'Sullivan | homogeneous weight on Frobenius rings; normalised values $0,\ \frac q{q-1}$ (socle), $1$ (else) on a chain ring | the definition used in §2.3 |
| Oggier–Belfiore–Viterbo, *Codes over matrix rings for space-time coded modulations* (arXiv:1008.1387) | **Bachoc weight** on $M_2(\mathbb F_2)$: $0\mapsto0$, non-unit $\mapsto\sqrt{2\delta}$, unit $\mapsto\sqrt\delta$; Lee-like weight on $M_2(\mathbb F_2[i])$ | weights on matrix rings, but **no duality map** |
| *Cyclic codes over the matrix ring $M_2(\mathbb F_p)$ and their isometric images over $\mathbb F_{p^2}+u\mathbb F_{p^2}$* (arXiv:1409.7228) | "we derive the homogeneous weight on the Frobenius matrix ring $M_2(\mathbb F_p)$ in terms of the generating character"; left $\mathbb F_p$-module isometry onto $\mathbb F_{p^2}+u\mathbb F_{p^2}$; Euclidean + Hermitian duals; $p\equiv2,3\bmod5$ | **closest prior work**; $t=1$, $p$ prime, no Galois-shift duality, no hulls |
| Zhang–Kong–Zheng (MDPI), commutative non-chain CRT-split ring | $\ell$-**Galois** duals via a new Gray map; key lemma $\phi(C)^{\perp_\ell}=\phi(C^{\perp_\ell})$; hull as an lcm; CSS + construction X; EAQECC | the **template** for Phase 4 — but commutative and Euclidean-flavoured |
| arXiv:2106.07962 ($R_{e,q}=\mathbb F_q[u]/\langle u^e-1\rangle$); MDPI 2023 ($F_qPQ$); *Codes over Frobenius ring* $T$ (MDPI 2026) | $\phi(C^\perp)=\phi(C)^\perp$, $\phi(C)\cap\phi(C)^\perp=\phi(C\cap C^\perp)$, LCD transfer, quantum codes | commutative, Euclidean |
| Qian–Zhang–Zhu / Dinh et al. on $(1+\gamma^e)$-constacyclic and $(1+u)$-constacyclic codes | Gray images are **quasi-cyclic** of index $p^{ke-1}$ resp. $m$ | matches the quasi-cyclic conclusion of §5.1 for chain rings |
| arXiv:2602.18255 (in the repo as "most recent competitor") | $M_4(\mathbb F_2[u]/\langle u^k\rangle)$: Euclidean + Hermitian duals, Bachoc map and Gray map to $\mathbb F_{16}$, cyclic codes; **no Galois duality, no hulls** | matrix-ring alphabet, no $\sigma_s$-duality |
| Bachoc 1997 (repo A9): $\varphi(a+ub)=(a+b,b)$ on $M_2(\mathbb F_2)=\mathbb F_4+u\mathbb F_4$ | the Bachoc map | the $t=2$ variant of §1.1 |

### 8.2 What was **not** found (novelty gap)

No source was found that combines

1. a **non-commutative matrix ring alphabet** $M_2(A_t)$ with $t\ge1$ arbitrary,
2. **$\sigma_s$-Galois (Frobenius-twisted) duality** together with a Gray-type map,
3. **hull compatibility** $\varphi(\operatorname{Hull})=\varphi(C)\cap\varphi(C)^{\perp}$
   including **non-principal** hulls,
4. a ring that is neither a chain ring nor commutative CRT-split (the **wild** regime
   $(4,2,2)$),
5. the explicit identification of the transported Gram matrix as $I_{4n}\otimes H_t$, i.e.
   the statement that the correct target form is *Hermitian-with-Hankel*, not Euclidean.

Items 2, 3, 4 relative to arXiv:1409.7228 (which has the homogeneous weight on $M_2(\mathbb F_p)$
but only Euclidean/Hermitian duals, no hulls, and a restrictive $p\equiv2,3\bmod5$), and
items 2–5 relative to the commutative $\ell$-Galois literature, are the novelty claim of
Phase 4. **This claim is a search-based negative and is stated with the limitation below.**

### 8.3 Search limitation (stated explicitly)

The literature search was performed with a general web-search tool. For each source above
the record (title, authors, venue/arXiv id) and the quoted abstract/excerpt were read, but
**no PDF was downloaded and no reference list was followed**; consequently (i) the absence
of a result is evidence, not proof, and (ii) statements such as the exact normalisation used
by Greferath–Schmidt, or the precise hypotheses of arXiv:1409.7228, are recorded from
secondary excerpts and should be re-verified against the papers before any manuscript text
is written. The repository bibliography (`01_LITERATURE/`) contains no entry for the
homogeneous weight on matrix rings beyond A9; entries for Greferath–Schmidt, Honold,
Oggier–Belfiore–Viterbo and arXiv:1409.7228 are **not** yet in `references.bib` and should
be added (with VERIFY tags) in the phase that writes the manuscript.

---

## 9. Results of Phase 4 (register rows T-176 … T-189)

| ID | statement | status |
|---|---|---|
| **T-176** | $\varphi_A,\varphi_R,\varphi_n$ are $\mathbb F_q$-linear bijections; $\varphi_nT=\widehat T\varphi_n$ with $\widehat T$ the rotation by $4t$; each is additive, injective and surjective | **PROVED** (verified `[EXH]`/`[SMP]`) |
| **T-177** | the form transported by $\varphi_n$ is $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$; $J$ is non-singular | **PROVED** (`[EXH]`, all 18 instances) |
| **T-178** | $\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$ for every code and every $s$ | **PROVED** (two independent routes, `[EXH]` on 8 families, `[SMP]` on 1) |
| **T-179** | $\varphi_n(\operatorname{Hull}_s(C))=\varphi_n(C)\cap\varphi_n(C)^{\perp^{\widehat{}}_s}$; no principality hypothesis; holds for the $\mu_B=3$ witnesses | **PROVED** (`[EXH]`, incl. the O-3.1 family) |
| **T-180** | $w_{\mathrm H}\le w_{\mathrm{ent}}\le w_{\mathrm{coef}}\le t\,w_{\mathrm{ent}}$, $w_{\mathrm H}\le\mathrm{wt}_{\mathrm H}\varphi_n\le4t\,w_{\mathrm H}$ (sharp); $\varphi_n$ is a $d_{\mathrm{coef}}$-isometry | **PROVED** (`[EXH]`/`[SMP]`) |
| **T-180b** | "$\varphi_n$ preserves the ring-Hamming weight" | **REFUTED** (witnesses, counts) |
| **T-181** | closed form of $w_{\mathrm{hom}}$ on $M_2(\mathbb F_q)$: $0,\ 1+\frac1{q^2-1},\ 1-\frac1{(q-1)^2(q+1)}$ by rank | **PROVED** (one imported standard $\mathrm{GL}_2$ Gauss-sum identity); **COMPUTATIONALLY VERIFIED** exhaustively for $q=4,8,9$ |
| **T-182** | no map into any Hamming space is an isometry for the (normalised) homogeneous weight on $R$ | **PROVED** (integrality) |
| **T-183** | $\varphi_n(C)$ is $\mathbb F_q$-linear $[4tn,\dim C]_q$, quasi-cyclic of index $4t$ and co-index $n$, invariant under the transported right $R_n$-action; **not** cyclic in general | **PROVED** (`[EXH]`) |
| **T-184** | transported form = Euclidean $\iff(t=1\wedge r\mid s)$; = plain $\widehat\sigma_s$-Hermitian $\iff t=1$ | **PROVED** (`[EXH]`) |
| **T-185** | congruence to the standard form: impossible for $q$ even, $t$ even; no per-block congruence at $(4,2)$ (exhaustive); exists at $(9,2)$, commutes with the block shift, but is non-monomial (loses Hamming weights) | **PROVED** for the stated cases; **OPEN** in general (O-4.2) |
| **T-186** | (a) $\langle v,u\rangle=\sigma_s\langle u,v\rangle\iff r\mid2s$; (b) orthogonality relation symmetric $\iff r\mid 2s$; (c) value-symmetric $\iff r\mid s$ | **PROVED** (`[EXH]`) |
| **T-187** | $\bigl(\varphi_n(C)^{\perp^{\widehat{}}_s}\bigr)^{\perp^{\widehat{}}_s}=\widehat\sigma_{2s}(\varphi_n(C))$ | **PROVED** (from T-178 + Thm 6.8 + $\varphi_n\sigma_s=\widehat\sigma_s\varphi_n$, the last `[SMP]`-verified) |
| **T-188** | $a\mapsto M_L(a)$ is an injective $\mathbb F_q$-algebra homomorphism $R\hookrightarrow M_{4t}(\mathbb F_q)$ | **PROVED** (`[EXH]`) |
| **T-189** | the Bachoc-type map ($t=2$): additive, $\mathbb F_q$-linear, shift-compatible; transports $b_s$ to the same Hankel form **iff** $\operatorname{char}\mathbb F_q=2$; is **not** a $w_{\mathrm{coef}}$-isometry | **PROVED** (char 2) / **COMPUTATIONALLY VERIFIED** `[SMP]` |

**Annotations to older rows (append-only, no existing row is modified):**
*T-012* ("Gray/Bachoc-type map with a duality relation") is **partially resolved**: the
duality relation holds for the coefficient expansion (T-178) but the isometry requirement
fails for the homogeneous weight (T-182); the remaining open part is O-4.4.
*T-013* (CSS/EA) remains **open**; T-178, T-179 and §6 (F1–F8) are the Phase-4 preconditions
it needs.

---

## 10. Proof-obligation traceability

| obligation (Phase-4 brief) | where it is proved | script section | log evidence |
|---|---|---|---|
| A: candidate maps + properties | §1, T-176, T-188, T-189 | `task_a_maps` | Part A, 7 families |
| B: correct weight structure | §2, T-180, T-181, T-182 | `task_b_weights`, `hom_from_nonunits` | Part B; $w_{\mathrm{hom}}$ tables for $q=4,8,9$ |
| C: scalar form $\langle x,y\rangle_s=\lambda(\operatorname{Tr}(B_s(x,y)))$ and the duality correspondence with an explicit target orthogonality | §3, T-177, T-178 | `gram_transported`, `hat_form`, `orth_hat`, `dual_img` | "the transported Gram matrix is $J=I_{4n}\otimes H_t$" and "$\varphi_n(C^{\perp_s})=\varphi_n(C)^{\perp^{\widehat{}}_s}$" lines |
| D: hull compatibility, non-principal hulls | §4, T-179 | `run_case_p4` (Morita vs. intersection) | "$\varphi_n(\operatorname{Hull}_s(C))=\ldots$" + the $\mu_B\ge3$ witness block |
| E: image code structure | §5, T-183 | `run_case_p4` (shift invariance, cyclicity, `min_distances`) | "#images invariant under shift by 1", "min distances" lines |
| F: quantum-relevant sufficient conditions | §6 (F1–F8) | statistics of `run_case_p4` | per-instance counts of SO / SD / LCD |
| G: two routes, `[EXH]`/`[SMP]`, negative controls | §7 | throughout | "NEGATIVE CONTROL" lines; 311 `[EXH]` / 152 `[SMP]` |
| H: literature / novelty | §8 | — | search limitation recorded in §8.3 |

---

## 11. Risks, open problems, and what Phase 5 would need

* **O-4.1 (closed form of $w_{\mathrm{hom}}$ on $M_2(A_t)$, $t\ge2$).** Values measured at
  $(q,t)=(4,2)$: $1$ off the socle ideal $uR$, and the $M_2(\mathbb F_q)$-values on $uR\setminus0$.
  **CONJECTURE** (H-4.1): $w_{\mathrm{hom}}(X)=w^{M_2(\mathbb F_q)}_{\mathrm{hom}}(Y)$ for
  $X=u^{t-1}Y$, and $w_{\mathrm{hom}}(X)=1$ otherwise.  Needs a proof or a counterexample.
* **O-4.2 (congruence to the standard form).** For which $(q,t)$ does a *monomial*
  (hence weight-preserving) $T$ with $T^{\mathsf T}H_tT=I_t$ exist? None was found for
  $t\ge2$; a proof that none exists (char 2: $H_t$ is alternating for $t$ even — done; for
  $t$ odd the alternating part has the wrong dimension) would settle the trade-off.
  **OPEN / partly proved.**
* **O-4.3 (a Gray isometry for $R$).** Ruled out for the normalised homogeneous weight
  (T-182). For rescaled weights: **OPEN** (necessary conditions in §2.5).
* **O-4.4 (the remaining part of T-012).** A map that is simultaneously weight-preserving
  (in *some* useful metric) and duality-compatible is not excluded by Phase 4; the
  coefficient map is duality-compatible but only $d_{\mathrm{coef}}$-preserving, and the
  congruence map is Gram-standardising but not weight-preserving.
* **O-4.5 (image code parameters).** The minimum distances of §5.3 are computed only for
  $|C|\le4100$; a family-wide distance formula for $\varphi_n(C)$ is not attempted.
* **Carried forward, untouched:** O-3.2, O-3.3 (wild Morita classes), O-3.4, O-3.5,
  H-3A.1, H-3A.2, and the Phase-0/1/2 open items.

**Stopping rule.** Phase 4 stops here. No CSS construction, no EAQECC construction, no
quantum parameters and no manuscript text are produced in this phase.

---

*End of Phase 4. Script `04_COMPUTATION/phase4_gray_map_compatibility.py`, log
`04_COMPUTATION/phase4_gray_map_log.txt` (SHA-256 `55656a9d…9a92`, 463 checks, 0 FAIL).*
