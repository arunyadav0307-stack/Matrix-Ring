# Complete proofs for the pairing $\langle x,y\rangle_s=\sum_i\theta_s(x_i)y_i$

**Phase 0 (revised), Task 2.**  Status of this document: every result below
carries one of the tags

* **[PROVED-HERE]** — a complete proof is written out in this file and uses
  nothing beyond the definitions and the two facts marked [STANDARD];
* **[STANDARD]** — a textbook fact, cited;
* **[CONDITIONAL]** — proved under a hypothesis that is stated explicitly and
  is *not* proved here;
* **[COMPUTATIONAL]** — verified by exhaustive/finite computation in a stated
  range only; **not** a theorem.

Nothing below is imported from the commutative theory without proof, and
nothing is claimed for a left/right convention other than the one stated.

---

## 0. Setting, notation, conventions

* $p$ prime, $q=p^{r}$ ($r\ge 1$), $\mathbb F_q$ the field with $q$ elements.
* $A_t:=\mathbb F_q[u]/\langle u^{t}\rangle$, $t\ge1$ (so $A_1=\mathbb F_q$).
  Elements are written $\sum_{j=0}^{t-1}a_ju^j$.
* $R:=M_m(A_t)$, $m\ge1$.  $Z(R)=\{\,cI_m : c\in Z(A_t)\,\}\supseteq\mathbb F_q$.
* $n\ge1$, $\mathcal R_n:=R[X]/\langle X^{n}-1\rangle$.  **$X$ is a central
  variable** (this is the polynomial ring over $R$), and $\mathcal R_n\cong
  M_m(B)$ with $B:=A_t[X]/\langle X^{n}-1\rangle$ **commutative**.
* $R^n$ is a **right** $R$-module: $(x\cdot a)_i=x_ia$.  $\mathcal R_n$ and
  $R^n$ are identified as right $R$-modules by
  $(x_0,\dots ,x_{n-1})\leftrightarrow\sum x_iX^{i}$.
* $T:R^n\to R^n$ is the cyclic shift, $T(x)_i=x_{i-1}$ (indices mod $n$);
  $T$ = right multiplication by $X$.
* **Convention (right convention, matching Alahmadi–Sboui–Solé–Yemen 2013,
  Luo–Parampalli, Dinh et al., Joshi–Patel–Prakash):** a *cyclic code of length
  $n$ over $R$* is a **right ideal** of $\mathcal R_n$, equivalently a right
  $R$-submodule $C\subseteq R^n$ with $T(C)\subseteq C$.
* $\sigma_s$: for $s\in\mathbb Z$, the map
  $\sigma_s\big(\sum a_ju^j\big)=\sum a_j^{p^{s}}u^{j}$ on $A_t$, extended
  **entrywise** to $R$, coordinatewise to $R^n$, and to $\mathcal R_n$ by
  $\sigma_s(X)=X$.  Indices are read mod $r$.
* $\theta_s:=\sigma_s\circ{}^{\mathsf T}$ where ${}^{\mathsf T}$ is transposition;
  $\theta_s$ is extended to $R^n$ coordinatewise and to $\mathcal R_n$ by
  $\theta_s(X)=X$.
* $\lambda:A_t\to\mathbb F_q$, $\lambda\big(\sum a_ju^j\big)=a_{t-1}$
  (for $t=1$: $\lambda(a)=a$); $\ \Lambda:=\lambda\circ\operatorname{tr}:R\to\mathbb F_q$.
* Pairings (all $R$-valued unless stated):
  $$P(x,y):=\sum_i x_iy_i,\qquad
    \langle x,y\rangle_s:=\sum_i\theta_s(x_i)\,y_i = P(\theta_s(x),y),$$
  where $\theta_s(x):=(\theta_s(x_i))_i$.
* $N:=\dim_{\mathbb F_q}R^n=n\,m^{2}t$, so $|R|^{n}=q^{N}$.

Two external facts are used:

* **[STANDARD-1]** $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ for matrices
  over a commutative ring.
* **[STANDARD-2]** If $\beta:V\times V\to\mathbb F_q$ is a non-degenerate
  bilinear form on an $N$-dimensional space and $U\le V$ has dimension $k$,
  then $\dim U^{\perp}=N-k$.

---

## 1. The maps $\sigma_s$ and $\theta_s$

### Lemma 1.1 (Frobenius). [PROVED-HERE]
$\sigma_s$ is a ring automorphism of $A_t$, of $R$, and of $\mathcal R_n$;
$\sigma_s=\mathrm{id}$ on $A_t$ **iff** $r\mid s$; the order of $\sigma_s$ is
$r/\gcd(r,s)$.

*Proof.* Additivity: $a\mapsto a^{p^{s}}$ is additive on $\mathbb F_q$
(Frobenius), so $\sigma_s$ is additive on coefficients, hence on $A_t$.
Multiplicativity: with $x=\sum a_iu^i,\ y=\sum b_ju^j$,
$\sigma_s(xy)=\sum_k\big(\sum_{i+j=k}a_ib_j\big)^{p^{s}}u^{k}
 =\sum_k\big(\sum_{i+j=k}a_i^{p^{s}}b_j^{p^{s}}\big)u^{k}=\sigma_s(x)\sigma_s(y)$,
using additivity **and** multiplicativity of the field Frobenius.
$\sigma_s(u^t)=u^t$, so $\sigma_s$ is well defined mod $u^t$; it is bijective
with inverse $\sigma_{-s}$ (as $r\mid (s+(-s))$). Entrywise application to
$M_m(A_t)$ preserves addition and multiplication because the field automorphism
$\sigma_s$ is applied to every product entrywise:
$(\sigma_s(XY))_{ik}=\sigma_s(\sum_jX_{ij}Y_{jk})=\sum_j\sigma_s(X_{ij})\sigma_s(Y_{jk})$.
Finally $\sigma_s(X^n-1)=X^n-1$, so it passes to $\mathcal R_n$.
On $A_t$, $\sigma_s=\mathrm{id}$ iff $a^{p^{s}}=a$ for all $a\in\mathbb F_q$,
i.e. iff $r\mid s$; the order statement follows. $\square$

> **Consequence (must be remembered).** If $q=p$ (i.e. $r=1$) *every*
> $\sigma_s$ is the identity: **there is no nontrivial Galois parameter at
> $q=p$**.  Nontriviality needs $r\nmid s$, and the experiments of Task 1 use
> $q=4,9$ ($r=2$, $s=1$) and $q=8$ ($r=3$, $s=1,2$).  **[COMPUTATIONAL
> corroboration: 04_COMPUTATION/galois_experiments_log.txt, §A.]**

### Lemma 1.2 ($\theta_s$ is an anti-automorphism). [PROVED-HERE]
$\theta_s$ is additive, bijective, and $\theta_s(XY)=\theta_s(Y)\theta_s(X)$
on $R$; the same holds on $\mathcal R_n$.

*Proof.* Additivity is clear.  With $\tau={}^{\mathsf T}$:
$\theta_s(XY)=\sigma_s\tau(XY)=\sigma_s(\tau(Y)\tau(X))
 =\sigma_s(\tau(Y))\sigma_s(\tau(X))=\theta_s(Y)\theta_s(X)$,
using Lemma 1.1 and $\tau(XY)=\tau(Y)\tau(X)$.  Bijective: $\sigma_s$ and
$\tau$ are bijections and they commute, so $\theta_s^{-1}=\tau\circ\sigma_s^{-1}$.
For $\mathcal R_n$: with $x=\sum x_iX^i,\ y=\sum y_jX^j$ and $X$ central,
$\theta_s(xy)=\sum_{i,j}\theta_s(x_iy_j)X^{i+j}
 =\sum_{i,j}\theta_s(y_j)\theta_s(x_i)X^{i+j}=\theta_s(y)\theta_s(x)$. $\square$

### Lemma 1.3 ($\theta_s^{2}$; **no involution in general**). [PROVED-HERE]
$\theta_s^{2}=\sigma_{2s}$ (on $R$, on $R^n$ and on $\mathcal R_n$).
Consequently $\theta_s$ is an involution $\iff\sigma_{2s}=\mathrm{id}\iff r\mid 2s$.

*Proof.* $\sigma_s$ and $\tau$ commute and $\tau^{2}=\mathrm{id}$, so
$\theta_s^{2}=(\sigma_s\tau)^{2}=\sigma_s^{2}\tau^{2}=\sigma_{2s}$.
The second statement is Lemma 1.1. $\square$

> **[COMPUTATIONAL]** Verified for all $(q,m,t,n,s)$ tested: $q=4,s=1$ and
> $q=9,s=1$ give $\theta_s^2=\mathrm{id}$; $q=8$ with $s=1$ and $s=2$ gives
> $\theta_s^{2}=\sigma_{2},\sigma_{1}\neq\mathrm{id}$ — **at $q=8$ the map
> $\theta_s$ is not an involution for any nontrivial $s$**
> (`galois_experiments_log.txt`, §B).  We therefore never call $\theta_s$ an
> involution without the hypothesis $r\mid 2s$.

### Lemma 1.4 ($\Lambda$ is a Frobenius functional). [PROVED-HERE]
$\Lambda:R\to\mathbb F_q$ satisfies
(i) $\Lambda$ is $\mathbb F_q$-bilinear (as a form $(X,Y)\mapsto\Lambda(XY)$);
(ii) $\Lambda(XY)=\Lambda(YX)$;
(iii) **ker $\Lambda$ contains no non-zero left ideal and no non-zero right
ideal of $R$** ("ideal-catching").

*Proof.* (i) $\lambda$ is $\mathbb F_q$-linear and the matrix product is
$\mathbb F_q$-bilinear.
(ii) $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ [STANDARD-1] and $\lambda$
is linear.
(iii) Let $X=(X_{ij})\neq0$, $X_{ij}=\sum_ka_{ijk}u^{k}$.  Pick
$(i_0,j_0)$ with $X_{i_0j_0}\ne0$ and put
$k_0:=\min\{k: a_{i_0j_0k}\ne0\}$, $c:=u^{\,t-1-k_0}\in A_t$,
$Y:=E_{j_0i_0}\,c$ (matrix unit times $c$).  Then $XY$ has $i$-th column equal
to $X_{ij_0}c$ and all other columns $0$, hence
$\operatorname{tr}(XY)=(XY)_{i_0i_0}=X_{i_0j_0}c=a_{i_0j_0k_0}u^{t-1}$
(the terms of degree $>k_0$ are killed by $u^{t-1-k_0}$ and the terms of degree
$<k_0$ do not exist), so $\Lambda(XY)=\lambda(\ldots)=a_{i_0j_0k_0}\ne0$.
Thus no non-zero **right** ideal $J$ satisfies $\Lambda(J)=0$: pick $0\ne X\in
J$ and $Y$ as above; then $XY\in J$ (right ideal) and $\Lambda(XY)\ne0$.
For a non-zero **left** ideal $L$ pick $0\ne X\in L$; the right ideal $XR$ is
non-zero (it contains $X$) and, by (ii),
$\Lambda(XR)=\Lambda(RX)\subseteq\Lambda(L)$; if $\Lambda(L)=0$ then
$\Lambda(XR)=0$, contradicting the right-ideal case. $\square$

> **[COMPUTATIONAL corroboration]** For $t=1$: the Gram matrix of
> $(X,Y)\mapsto\operatorname{tr}(XY)$ on $M_2(\mathbb F_q)$ has full rank $4$
> for $q=4,8,9$ (`galois_experiments_log.txt`, §C).

---

## 2. Elementary properties of the $\theta$-pairing

### Proposition 2.1. [PROVED-HERE]
For all $x,y\in R^n$, $a\in R$, $c\in\mathbb F_q$:

1. $\langle x+x',y\rangle_s=\langle x,y\rangle_s+\langle x',y\rangle_s$ and
   $\langle x,y+y'\rangle_s=\langle x,y\rangle_s+\langle x,y'\rangle_s$
   (**additivity in both arguments**);
2. $\langle x,y\,a\rangle_s=\langle x,y\rangle_s a$ (**right $R$-linearity in
   $y$**);
3. $\langle x\,a,y\rangle_s=\theta_s(a)\,\langle x,y\rangle_s$
   ($\theta_s$-semilinearity in $x$);
4. $\langle x,c\,y\rangle_s=c\,\langle x,y\rangle_s$ and
   $\langle c\,x,y\rangle_s=\sigma_s(c)\langle x,y\rangle_s$;
5. $\langle T x,\,y\rangle_s=\langle x,\,T^{-1}y\rangle_s$, equivalently
   $\langle x,Ty\rangle_s=\langle T^{-1}x,y\rangle_s$.

*Proof.* (1) $\theta_s$ is additive (Lemma 1.2) and multiplication is
distributive.
(2) $\sum_i\theta_s(x_i)(y_ia)=\big(\sum_i\theta_s(x_i)y_i\big)a$ by
associativity.
(3) $\theta_s(x_ia)=\theta_s(a)\theta_s(x_i)$ (Lemma 1.2), and
$\theta_s(a)$ factors out of the sum **on the left**.
(4) $c$ is $cI_m$, which is central in $R$, so it commutes past
$\theta_s(x_i)$; and $\theta_s(cI_m)=\sigma_s(c)I_m$.
(5) $\langle x,Ty\rangle_s=\sum_i\theta_s(x_i)y_{i-1}=\sum_j\theta_s(x_{j+1})y_j
 =\sum_j\theta_s\big((T^{-1}x)_j\big)y_j$. $\square$

> **Remark (this is the whole point).** By 2.1(2) the pairing is linear in $y$
> **for the right module structure of $R^n$**; there is no way to make
> $\sum_ix_iy_i$ behave this way, because in $P(x,ya)=\sum x_iy_ia$ the
> factor $a$ multiplies on the right of the whole product (that direction is
> fine) but $P(x,ay)=\sum x_iay_i$ has $a$ trapped between $x_i$ and $y_i$.
> See §5.

### Proposition 2.2 (non-degeneracy). [PROVED-HERE]
For $y\ne0$ there is $x$ with $\langle x,y\rangle_s\ne0$, and for $x\ne0$ there
is $y$ with $\langle x,y\rangle_s\ne0$.

*Proof.* Fix $y\ne0$, say $y_{i_0}\ne0$.  Take $x=e_{i_0}\cdot 1$
(the vector with $I_m$ in position $i_0$). Then
$\langle x,y\rangle_s=\theta_s(I)y_{i_0}=y_{i_0}\ne0$.  Symmetrically, for
$x\ne0$ pick $i_0$ with $x_{i_0}\ne0$ and $y=e_{i_0}\cdot1$:
$\langle x,y\rangle_s=\theta_s(x_{i_0})\ne0$. $\square$

### Proposition 2.3 (plain-product annihilators). [PROVED-HERE]
For $S,D\subseteq R^{n}$ put
$$A_2(S):=\{y: P(w,y)=0\ \forall w\in S\},\qquad
  A_1(D):=\{w: P(w,y)=0\ \forall y\in D\}.$$
Then

1. $A_2(S)$ is always a **right** $R$-submodule; if $S$ is a right
   $R$-submodule then $A_2(S)$ is also a **left** $R$-submodule.
   Dually, $A_1(D)$ is always a left submodule, and a right submodule if $D$ is
   a right submodule. ($P(w,ya)=P(w,y)a$, $P(w,ay)=P(wa,y)$,
   $P(aw,y)=aP(w,y)$.)
2. The form $\beta(x,y):=\Lambda(P(x,y))$ is $\mathbb F_q$-bilinear and
   non-degenerate; consequently $A_2(S)=\{y:\beta(w,y)=0\ \forall w\in S\}$
   whenever $S$ is a **left** submodule, and
   $A_1(D)=\{w:\beta(w,y)=0\ \forall y\in D\}$ whenever $D$ is a **right**
   submodule.
3. If $S$ is a left submodule: $|A_2(S)|=|R|^{n}/|S|$; if $D$ is a right
   submodule: $|A_1(D)|=|R|^{n}/|D|$.
4. If $S$ is a left submodule then $A_1(A_2(S))=S$; if $D$ is a right
   submodule then $A_2(A_1(D))=D$.

*Proof.* (1) direct from the three identities, which are immediate
consequences of associativity.
(2) $\beta$ is $\mathbb F_q$-bilinear because $\mathbb F_q$ is central
(cf. Prop. 2.1(4) with $\theta_s=\mathrm{id}$).  Non-degenerate: if $x\ne0$
then $J:=\sum_ix_iR$ is a non-zero right ideal of $R$ (take $y=e_i\cdot a$ to
see that $\{P(x,y):y\}=\sum_ix_iR$, and $x_{i_0}\ne0\Rightarrow
x_{i_0}\cdot1\in J\setminus0$); by Lemma 1.4(iii) some element of $J$ has
non-zero $\Lambda$, so $\beta(x,y)\ne0$ for some $y$; symmetrically in $y$.
For the identification: let $S$ be a left submodule and $y\in R^n$ with
$\beta(w,y)=0$ for all $w\in S$.  The set $\{P(w,y):w\in S\}$ is a left ideal
of $R$ (by (1)'s identity $P(aw,y)=aP(w,y)$ and $aw\in S$); if it were
non-zero, Lemma 1.4(iii) would give $w$ with $\beta(w,y)\ne0$.  Hence it is
$0$, i.e. $y\in A_2(S)$.  The other inclusion is trivial, and the statement
for $A_1$ is the mirror image (there $\{P(w,y):y\in D\}$ is a right ideal).
(3) follows from (2) and [STANDARD-2] applied to $\beta$
($\dim A_2(S)=N-\dim S$).
(4) $S\subseteq A_1(A_2(S))$ holds by definition; $A_2(S)$ is a right
submodule by (1), so by (3) $\dim A_1(A_2(S))=N-(N-\dim S)=\dim S$; hence
equality.  Mirror for $D$. $\square$

---

## 3. The $\theta_s$-dual: the six required properties

**Definition.** For $C\subseteq R^{n}$,
$$C^{\perp_s}:=\{y\in R^{n}:\ \langle x,y\rangle_s=0\ \ \forall x\in C\}
   =A_2\big(\theta_s(C)\big),\qquad
  \mathrm{Hull}_s(C):=C\cap C^{\perp_s}.$$
(The equality with $A_2(\theta_s(C))$ is the definition of $P$ and
$\theta_s(C):=\{\theta_s(x):x\in C\}$.)

### Theorem 3.1 (additivity — Task 2, item 1). [PROVED-HERE]
Proposition 2.1(1). $\square$

### Theorem 3.2 ($\theta_s(AB)=\theta_s(B)\theta_s(A)$ — Task 2, item 2).
[PROVED-HERE]  Lemma 1.2. $\square$

### Theorem 3.3 (non-degeneracy — Task 2, item 3). [PROVED-HERE]
In the strongest sense needed:
(a) Proposition 2.2 (no non-zero vector is orthogonal to everything);
(b) $y\mapsto\big(x\mapsto\theta_s^{-1}\langle x,y\rangle_s\big)$ is a
bijection $R^{n}\to\operatorname{Hom}_R(R^{n}_R,R_R)$;
(c) $|C|\cdot|C^{\perp_s}|=|R|^{n}$ for **every** $C$ that is a right
$R$-submodule (Theorem 3.5 below).

*Proof of (b).* $\theta_s^{-1}\langle x,y\rangle_s
 =\theta_s^{-1}\big(\sum_i\theta_s(x_i)y_i\big)
 =\sum_i\theta_s^{-1}(y_i)\,x_i$ (apply the anti-automorphism $\theta_s^{-1}$
 term by term).  For fixed $y$ the map $x\mapsto\sum_i\theta_s^{-1}(y_i)x_i$ is
 right $R$-linear, and every right $R$-linear map $R^{n}_R\to R_R$ is of this
 form (it is determined by the images of the standard basis vectors, and
 $f(x)=\sum_if(e_i)x_i$).  The correspondence $y\leftrightarrow
 (\theta_s^{-1}(y_i))_i$ is bijective. $\square$

### Theorem 3.4 (left/right module compatibility — Task 2, item 4). [PROVED-HERE]
1. For **every** subset $C\subseteq R^{n}$ (no hypothesis!), $C^{\perp_s}$ is
   a **right** $R$-submodule of $R^{n}$ and an $\mathbb F_q$-subspace.
2. If $C$ is $T$-invariant then $C^{\perp_s}$ is $T$-invariant.
3. If $C$ is a cyclic code (right ideal of $\mathcal R_n$) then
   $C^{\perp_s}$ is a right ideal of $\mathcal R_n$, i.e. **the $\theta$-dual
   of a cyclic code is cyclic**.
4. *Mirror statement (left convention).* If one instead uses **left** ideals,
   the correct pairing is $\langle x,y\rangle^{L}_s:=\sum_i y_i\,\theta_s(x_i)$:
   it is left-$R$-linear in $y$, and the dual of **any** set is a left
   $R$-submodule; the dual of a left-cyclic code is left-cyclic.
   The pairing $\sum_ix_i\theta_s(y_i)$ is **not** left-linear in $y$
   ($\theta_s(a)$ is trapped between $x_i$ and $\theta_s(y_i)$) and must not be
   used.

*Proof.* (1) $y\in C^{\perp_s}$, $a\in R$ $\Rightarrow$
$\langle x,ya\rangle_s=\langle x,y\rangle_sa=0$ by 2.1(2); additivity and
$\mathbb F_q$-closure by 2.1(1),(4).
(2) If $y\in C^{\perp_s}$ and $x\in C$ then, by 2.1(5),
$\langle x,Ty\rangle_s=\langle T^{-1}x,y\rangle_s=0$ because $T^{-1}x\in C$.
(3) Combine (1), (2) and the characterisation "right ideal = right
$R$-submodule + $T$-invariant".
(4) $\langle x,ay\rangle^{L}_s=\sum_i ay_i\theta_s(x_i)=a\langle x,y\rangle^L_s$
(left $R$-linearity in $y$), so $ay\in C^{\perp}$ whenever $y\in C^{\perp}$;
$T$-invariance is the same computation as in (2). $\square$

### Theorem 3.5 (size/dimension formula). [PROVED-HERE]
If $C$ is a right $R$-submodule of $R^{n}$ then
$$|C|\cdot|C^{\perp_s}|=|R|^{n}\qquad\big(\dim_{\mathbb F_q}C+\dim_{\mathbb F_q}
  C^{\perp_s}=N\big).$$

*Proof.* $C$ right submodule $\Rightarrow$ $\theta_s(C)$ is a **left**
submodule (for $a\in R$: $\theta_s(xa)=\theta_s(a)\theta_s(x)$, i.e. $\theta_s(C)$
is closed under *left* multiplication, and $\theta_s$ is onto $R$).  By
Prop. 2.3(3), $|A_2(\theta_s(C))|=|R|^{n}/|\theta_s(C)|=|R|^{n}/|C|$, and
$C^{\perp_s}=A_2(\theta_s(C))$. $\square$

> **[COMPUTATIONAL]** Verified for **every** cyclic code in every case tested:
> 343/343 ($q=4,n=3$), 737/737 for each of $s=1,2$ ($q=8,n=3$),
> 144/144 ($q=9,n=2$), 1200/1200 sampled ($q=9,n=4$), 5/5 and 35/35
> ($q=2$, enumeration validation).

### Theorem 3.6 (double dual — Task 2, item 5; **conditional**). [PROVED-HERE]
For every right $R$-submodule $C\subseteq R^{n}$,
$$\big(C^{\perp_s}\big)^{\perp_s}=\theta_s^{2}(C)=\sigma_{2s}(C)
   :=\{(\sigma_{2s}(x_i))_i : x\in C\}.$$
In particular $C\subseteq(C^{\perp_s})^{\perp_s}$ for all $C$ **iff**
$\sigma_{2s}=\mathrm{id}$, i.e. **iff $r\mid 2s$**; and then
$(C^{\perp_s})^{\perp_s}=C$ for all $C$.

*Proof.* Write $D:=C^{\perp_s}=A_2(\theta_s(C))$, a right submodule by
Theorem 3.4(1).
*Step 1.* For any right submodule $D$ and any $z$:
$z\in A_2(\theta_s(D))\iff \theta_s^{-1}(z)\in A_1(D)$.
Indeed $z\in A_2(\theta_s(D))\iff P(\theta_s(y),z)=0\ \forall y\in D$; applying
the bijection $\theta_s^{-1}$ and using anti-multiplicativity,
$\theta_s^{-1}\big(P(\theta_s(y),z)\big)=\sum_i\theta_s^{-1}(z_i)\,
\theta_s^{-1}(\theta_s(y_i))=P(\theta_s^{-1}(z),y)$, which vanishes for all
$y\in D$ exactly when $\theta_s^{-1}(z)\in A_1(D)$.
Hence $A_2(\theta_s(D))=\theta_s(A_1(D))$.
*Step 2.* $(C^{\perp_s})^{\perp_s}=A_2(\theta_s(D))=\theta_s(A_1(D))
 =\theta_s\big(A_1(A_2(\theta_s(C)))\big)=\theta_s(\theta_s(C))$ by
Prop. 2.3(4) applied to the **left** submodule $\theta_s(C)$.
*Step 3.* $\theta_s^2=\sigma_{2s}$ (Lemma 1.3).
For the last claim: $C\subseteq\sigma_{2s}(C)$ with $|\sigma_{2s}(C)|=|C|$
forces equality, so $C\subseteq(C^{\perp_s})^{\perp_s}$ for all $C$ iff
$\sigma_{2s}(C)=C$ for all $C$, which holds for all $C$ iff
$\sigma_{2s}=\mathrm{id}$ (take $C=e_1\cdot A_t\,I_m$ … more simply, apply
$\sigma_{2s}$ to a vector with a single entry $a\notin\mathbb F_{p^{\gcd(r,2s)}}$).
By Lemma 1.1 this is $r\mid 2s$. $\square$

> **[COMPUTATIONAL]** $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$ holds in
> **every** case tested (343/343, 737/737 ×2, 144/144, 1200/1200, 5/5, 35/35).
> Reflexivity $(C^{\perp_s})^{\perp_s}=C$ holds 343/343 at $q=4,s=1$,
> 144/144 at $q=9$, 1200/1200 at $q=9,n=4$ — but only **35/737** at $q=8$,
> $s=1$ and $s=2$, with explicit witnesses printed in the log.  This is the
> computational counterpart of "$r\mid 2s$".

> **Design consequence (important).** A *reflexive* Galois duality on right
> ideals therefore requires $2s\equiv0\pmod r$.  The nontrivial solutions are
> exactly $r$ even and $s\equiv r/2\pmod r$ — the "Hermitian-like" choice.
> **Recommendation: take $q=p^{2e}$ and $s=r/2$ (or $s\equiv0$).**  At $q=8$
> ($r=3$) there is *no* nontrivial reflexive choice.

### Theorem 3.7 (cyclicity of the dual — Task 2, item 6). [PROVED-HERE]
*Hypotheses under which the dual is cyclic:*
1. If $C$ is a right $R$-submodule and $T$-invariant (i.e. $C$ is a cyclic
   code), then $C^{\perp_s}$ is cyclic — **no further hypothesis**
   (Theorem 3.4(3)).
2. $C^{\perp_s}$ is a right $R$-submodule for **every** $C$; the only extra
   ingredient for cyclicity is the $T$-invariance of $C$.
3. *Principality* (i.e. the dual is generated by one element as a right ideal)
   needs more: it holds if the corresponding $B$-submodule of $B^{m}$ is
   $m$-generated.  This is proved in the semisimple case:

   **[CONDITIONAL]** Suppose $t=1$ and $X^{n}-1$ is squarefree over
   $\mathbb F_q$ (equivalently $\gcd(n,p)=1$).  Then
   $B\cong\prod_{i=1}^{k}K_i$ with $K_i=\mathbb F_q[X]/\langle f_i\rangle$
   fields, every $B$-submodule of $B^{m}$ is $\prod_iV_i$ with $V_i\le K_i^{m}$
   a subspace, hence generated by $\max_i\dim_{K_i}V_i\le m$ elements; and a
   right ideal of $M_m(B)$ is principal iff the corresponding submodule of
   $B^{m}$ is $m$-generated.  Hence **every right ideal of $\mathcal R_n$ is
   principal** in this case.  For $t\ge2$ (or $p\mid n$) principality is
   **[OPEN]**.

*Proof of the principality criterion.* For $M\in M_m(B)$, the right ideal
$M\cdot M_m(B)$ consists exactly of the matrices all of whose columns lie in
the $B$-span of the columns of $M$; so $M\cdot M_m(B)=I_W$ with
$W=\sum_jB\,\mathrm{col}_j(M)$, and $I_W$ is principal iff $W$ is generated by
$\le m$ elements. $\square$

### Theorem 3.8 (the hull is a right module — Task 2, item 7). [PROVED-HERE]
1. If $C$ is a right $R$-submodule then $\mathrm{Hull}_s(C)=C\cap
   C^{\perp_s}$ is a right $R$-submodule (intersection of two right
   submodules).  **No condition on $s$ is needed.**
2. If moreover $C$ is $T$-invariant then $\mathrm{Hull}_s(C)$ is
   $T$-invariant, hence a right ideal of $\mathcal R_n$ — **the Galois hull of
   a cyclic code is cyclic**.
3. If $C$ is merely an $\mathbb F_q$-subspace (not a right $R$-submodule) then
   the hull need **not** be a right module; the hypothesis "$C$ is a right
   $R$-module" is exactly what is needed.
4. $\dim_{\mathbb F_q}\mathrm{Hull}_s(C)$ is *not* determined by $\dim C$
   alone; hull-dimension formulas for specific families are **Phase-4 work**
   (register T-011, still [OPEN]).

> **[COMPUTATIONAL]** Hull is a right $R$-submodule and cyclic in
> 343/343, 737/737 (×2), 144/144, 1200/1200, 5/5, 35/35 cases.

### Theorem 3.9 (reflexivity criterion — **exactly when is $C\mapsto
C^{\perp_s}$ a duality?**). [PROVED-HERE]

Assume $m\ge2$ and $n\ge1$.  The following are equivalent:

1. $(C^{\perp_s})^{\perp_s}=C$ for **every** right $R$-submodule
   $C\subseteq R^{n}$ (the duality is *reflexive*);
2. $\sigma_{2s}=\mathrm{id}$ on $R$;
3. $r\mid 2s$.

*Proof.* $(3)\Rightarrow(2)$ is Lemma 1.1 ($\sigma_s=\mathrm{id}\iff r\mid s$,
applied to $2s$).  $(2)\Rightarrow(1)$ is Theorem 3.6.

$(1)\Rightarrow(2)$.  Suppose $\sigma_{2s}\ne\mathrm{id}$.  Since
$\sigma_{2s}$ acts entrywise on the $\mathbb F_q$-coefficients and fixes $u$,
it is nontrivial on $R$ iff it is nontrivial on $\mathbb F_q$; pick
$a\in\mathbb F_q$ with $\bar a:=\sigma_{2s}(a)\ne a$.  Let
$v:=e_1+a\,e_2\in A_t^{m}$ and $W:=A_t\,v$ (an $A_t$-submodule of $A_t^{m}$;
$A_t$ is commutative, so no left/right ambiguity).  Let $I_W:=\{M\in
M_m(A_t): \text{all columns of }M\text{ lie in }W\}$ be the corresponding
right ideal of $R$ (Morita).  Then $\sigma_{2s}(I_W)=I_{\sigma_{2s}(W)}$ and
$\sigma_{2s}(W)=A_t\,(e_1+\bar a\,e_2)$.  These two $A_t$-submodules differ:
$v\in\sigma_{2s}(W)$ would force $c\cdot1=1$ and $c\cdot\bar a=a$ for some
$c\in A_t$, i.e. $c=1$ and $\bar a=a$, a contradiction.  Now put
$C:=\{(x,0,\dots,0)\in R^{n}: x\in I_W\}$, a right $R$-submodule of $R^{n}$
(it is $T$-invariant iff $n=1$; $T$-invariance is not needed here).  By
Theorem 3.6,
$(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)=\{(\sigma_{2s}(x),0,\dots,0):
x\in I_W\}\ne C$.  So (1) fails. $\square$

> **[COMPUTATIONAL]** At $q=8$ ($r=3$, $s=1,2$: $r\nmid 2s$) reflexivity fails
> for $702$ of the $737$ cyclic codes, with explicit witnesses; at $q=4$ and
> $q=9$ ($r=2$, $s=1$: $r\mid2s$) it holds for all of them.  The smallest
> instance of the construction above is $m=2$, $n=1$, $W=A_t(e_1+ae_2)$ — a
> "line with a non-fixed slope", whose right ideal is moved by $\sigma_{2s}$.

---

## 4. The $R$-valued and the $\mathbb F_q$-valued duals coincide

### Proposition 4.1. [PROVED-HERE]
For every right $R$-submodule $C$,
$$C^{\perp_s}=\big\{y:\ \Lambda\langle x,y\rangle_s=0\ \forall x\in C\big\}.$$

*Proof.* "$\subseteq$" is trivial.  Conversely let $y$ satisfy
$\Lambda\langle x,y\rangle_s=0$ for all $x\in C$.  The set
$\{\langle x,y\rangle_s:x\in C\}$ is the image of $C$ under the map
$x\mapsto P(\theta_s(x),y)$, which is additive; since $\theta_s(C)$ is a left
submodule, this set is a **left ideal** of $R$ (for $a\in R$:
$P(a\,\theta_s(x),y)=a\,P(\theta_s(x),y)$ and $a\theta_s(x)\in\theta_s(C)$).
If it were non-zero, Lemma 1.4(iii) would give $x$ with
$\Lambda\langle x,y\rangle_s\ne0$.  Hence it is $0$, i.e. $y\in C^{\perp_s}$.
$\square$

*Remark.* This is the statement that makes the quantum step possible later
(one needs an $\mathbb F_q$-valued orthogonality), but it is **not** needed for
any of §3.

---

## 5. What fails for the plain product $\sum_ix_iy_i$ (and why)

### Proposition 5.1. [PROVED-HERE]
Let $P(x,y)=\sum_ix_iy_i$ and $C^{\perp_P}:=\{y:P(x,y)=0\ \forall x\in C\}$.

1. $C^{\perp_P}=A_2(C)$ is **always** a right $R$-submodule, and it is also a
   left $R$-submodule whenever $C$ is a right $R$-submodule
   ($P(w,ay)=P(wa,y)$ and $wa\in C$).
2. If $C$ is a **left** $R$-submodule then $|C|\cdot|C^{\perp_P}|=|R|^{n}$
   (Prop. 2.3(3) with $S=C$) — the plain product is a perfect duality **for
   left ideals**.
3. If $C$ is a **right** $R$-submodule, no size formula holds in general:
   the dual is a left module ($P(w,ay)=P(wa,y)$ with $wa\in C$), it is a
   *different kind of object* from $C$, and $C=C^{\perp_P}$ forces $C$ to be a
   left module as well.

*Counterexample (smallest possible).* $R=M_2(\mathbb F_2)$, $n=1$,
$C=uR=\{\begin{pmatrix}a&b\\0&0\end{pmatrix}\}$ (a right ideal, $|C|=4$).
Then $C^{\perp_P}=\{y:xy=0\ \forall x\in C\}=\{0\}$ (take $x=E_{11}$ and
$x=E_{12}$), so $|C|\cdot|C^{\perp_P}|=4\ne16=|R|$.

> **[COMPUTATIONAL]** Over $M_2(\mathbb F_q)$, $n=3$: the relation
> $|C||C^{\perp_P}|=|R|^{n}$ holds for only **8/343** codes at $q=4$,
> **4/737** at $q=8$, **4/144** at $q=9,n=2$, **2/1200** at $q=9,n=4$; and at
> $q=4$ the plain dual is $\{0\}$ for **216 of the 343** cyclic codes.  At
> $q=2,n=3$ (the Alahmadi setting) it holds for **4/35** and there is **no**
> self-dual cyclic code at all for the form $\sum_jx_jy_j$
> (`alahmadi_reconciliation_log.txt`, §5).

**This is the reason the project cannot simply transport the commutative
Euclidean/Hermitian Galois-hull theory: it is not the Frobenius twist that
fails, it is the side.**

---

## 6. Summary table

| # | Statement | Status | Where |
|---|---|---|---|
| 1.1 | $\sigma_s\in\operatorname{Aut}$, $\sigma_s\ne\mathrm{id}\iff r\nmid s$ | [PROVED-HERE] | §1 |
| 1.2 | $\theta_s$ anti-automorphism | [PROVED-HERE] | §1 |
| 1.3 | $\theta_s^2=\sigma_{2s}$; involution $\iff r\mid 2s$ | [PROVED-HERE] | §1 |
| 1.4 | $\Lambda$ Frobenius functional (symmetric, ideal-catching) | [PROVED-HERE] | §1 |
| 2.1 | additivity / right-$R$-linearity in $y$ / $\theta$-semilinearity in $x$ | [PROVED-HERE] | §2 |
| 2.2 | non-degeneracy (both sides) | [PROVED-HERE] | §2 |
| 2.3 | plain-product annihilator calculus | [PROVED-HERE] | §2 |
| 3.3 | $y\mapsto$ functional is a bijection onto $\operatorname{Hom}_R(R^n_R,R_R)$ | [PROVED-HERE] | §3 |
| 3.4 | dual of **any** set is a right module; dual of cyclic is cyclic | [PROVED-HERE] | §3 |
| 3.5 | $|C|\,|C^{\perp_s}|=|R|^n$ for right submodules | [PROVED-HERE] | §3 |
| 3.6 | $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$; reflexive $\iff r\mid 2s$ | [PROVED-HERE] | §3 |
| 3.7 | cyclicity of the dual; principality | [PROVED-HERE] / **[CONDITIONAL]** for principality | §3 |
| 3.8 | hull is a right module / cyclic iff $C$ is | [PROVED-HERE] | §3 |
| 3.9 | **reflexivity criterion**: $(C^{\perp_s})^{\perp_s}=C$ for all $C$ $\iff$ $r\mid2s$ (counterexample $W=A_t(e_1+ae_2)$ when $r\nmid2s$) | [PROVED-HERE] | §3 |
| 4.1 | $R$-valued dual $=$ $\Lambda$-valued dual | [PROVED-HERE] | §4 |
| 5.1 | plain product: perfect for **left**, broken for **right** | [PROVED-HERE] | §5 |

**Not proved here / still open:** hull-dimension formulas (T-011), the
existence of a duality-preserving Gray map (T-012, R3), everything quantum
(T-013, T-014), the case $t\ge2$ beyond the statements that are uniform in $t$
(1.1–1.4, 2.1–2.3, 3.1–3.6, 3.8, 3.9, 4.1, 5.1 are all valid for every $t\ge1$; the $t=2$ case was additionally verified computationally on all 32 right ideals of $M_2(\mathbb F_4[u]/\langle u^2\rangle)$ at $n=1$, $s=1$).
