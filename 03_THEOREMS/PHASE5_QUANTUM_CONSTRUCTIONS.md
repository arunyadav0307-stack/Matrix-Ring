# PHASE 5 — QUANTUM ERROR-CORRECTING CODE CONSTRUCTION

**Status:** complete (Tasks A–H).  Every statement below is labelled
**PROVED** (a proof is given in this file), **COMPUTATIONALLY VERIFIED ONLY**
(the statement is checked exhaustively or on a seeded sample, no proof),
**CONJECTURE**, or **OPEN**.

**Companion artefacts**

| file | content |
|---|---|
| `04_COMPUTATION/phase5_quantum_constructions.py` | the verification script (Parts A–G), `SEED = 20261120` |
| `04_COMPUTATION/phase5_quantum_log.txt` | its log: **88 checks, 88 PASS, 0 FAIL**, 491 lines, byte-reproducible |

**Dependencies (read-only, never modified in this phase):**
`RING_AND_GALOIS_FOUNDATIONS.md` (§6, the pairing package),
`PHASE2_STAGE2C_GALOIS_DUALITY.md` (Thm 3.8, `C^{\perp_s} = rev(ann_r(theta_s C))`),
`PHASE3_STAGE3A_GALOIS_HULL_STRUCTURE.md` (`Hull_s(C) = I_{W∩W'}`),
`PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md` (O-3.1 refuted by T-173: hulls need not be principal),
`PHASE4_GRAY_MAP_COMPATIBILITY.md` (the Gray map `phi_n` and the transported form, T-176 … T-189).

---

## 0. Conventions and imported input

Throughout, `q = p^r`, `A_t = F_q[u]/<u^t>`, `R = M_2(A_t)`, `R_n = R^n` as a
**right** `R_n`-module (the standing right-module convention of this project).

* `theta_s` is the established Galois anti-automorphism, `sigma_s = (a ↦ a^{p^s})`
  on `F_q`, `Lambda = lambda ∘ tr` the standard character, `b_s = Lambda ∘ B_s`
  the Phase-1 pairing.  (`RING_AND_GALOIS_FOUNDATIONS.md` §6: `b_s` is additive,
  `F_p`-bilinear, right-`F_q`-linear, **left-`sigma_s`-semilinear**, right
  non-degenerate; `dim C + dim C^{\perp_s} = N`; `(C^{\perp_s})^{\perp_s} =
  sigma_{2s}(C)`.)
* `phi_n : R^n → F_q^N`, `N = 4tn`, is the Phase-4 Gray map
  (`phi_A(a) = (a_0,…,a_{t−1})`, `phi_R` entrywise, flat index
  `((e·4+k)·t + a)`).  It is an `F_q`-linear bijection (T-176).
* **T-177 (imported).** The form transported by `phi_n` is

  $$\langle u,v\rangle^{\widehat{\ }}_s \;=\; u^{[s]}\,J\,v^{\mathsf T},
  \qquad J = I_{4n}\otimes H_t,\qquad
  (H_t)_{ab} = \begin{cases}1 & a+b = t-1\\ 0 & \text{else.}\end{cases}$$

  `J` is non-singular, Hankel, symmetric, `J^2 = I`, `J = I ⟺ t = 1`, and `J` is
  alternating ⟺ `t` is even.  Write `u^{[s]} = (sigma_s(u_1),…,sigma_s(u_N))`
  and `D^{\perp^{\widehat{}}}_s = \{v : \langle u,v\rangle^{\widehat{}}_s = 0\ \forall u \in D\}`
  for `D = phi_n(C)`.
* **T-178/T-179 (imported).** `phi_n(C^{\perp_s}) = D^{\perp^{\widehat{}}}_s` and
  `phi_n(Hull_s(C)) = D ∩ D^{\perp^{\widehat{}}}_s` — with **no** principality
  hypothesis, hence valid for the non-principal (`mu_B ≥ 3`) O-3.1 witnesses.
* **T-183 (imported).** `D` is quasi-cyclic of index `4t` and co-index `n`.

**The quantum framework (set up from scratch in this phase; nothing is imported
for it).**  The physical system is `N_phys` qudits of dimension `q`.  For
`a, b ∈ F_q^{N}` put

$$X(a)|v\rangle = |v+a\rangle,\qquad
  Z(b)|v\rangle = \chi\big(\operatorname{Tr}_{F_q/F_p}(b\cdot v)\big)|v\rangle,
  \qquad \chi(x) = e^{2\pi i x/p},$$

and `E(a|b) = X(a)Z(b)` (phase conventions are irrelevant below).  Then

> **Lemma Q1 (PROVED, verified `[EXH]`).**  `X(a)Z(b) = chi(Tr(a·b)) Z(b)X(a)`,
> hence two Weyl operators `E(a|b)`, `E(a'|b')` commute **iff**
> `Tr_{F_q/F_p}(a·b' − a'·b) = 0`.

Write `omega((a|b),(a'|b')) = a·b' − a'·b` (an element of `F_q`) and
`sw(a|b) = #{i : (a_i,b_i) ≠ (0,0)}` (the symplectic = *quantum* weight).

> **Lemma Q2 (PROVED, standard, re-derived and verified).**  Let
> `C ⊆ F_q^{2N}` be an additive (i.e. `F_p`-linear) subgroup, `S` the group it
> generates.  Then:
> 1. `S` is abelian ⟺ `Tr(omega(x,y)) = 0` for all `x,y ∈ C`;
> 2. `dim` of the code space `= q^N/|C|`, i.e. writing `K = log_q(q^N/|C|)`,
>    `K = N − log_q|C|`;
> 3. with `C_0 = C ∩ C^{\perp_{Tr∘omega}}`, the code detects every error of
>    symplectic weight `< d` and corrects every error of weight `≤ ⌊(d−1)/2⌋`,
>    where
>    $$d = \min\{\,\mathrm{sw}(v) : v \in C^{\perp_{Tr∘omega}}\setminus C_0\,\};$$
> 4. (Knill–Laflamme, group form — PROVED equivalent to the operator form)
>    the code corrects an error set `E` iff for all `E,F ∈ E` either
>    `E^†F ∈ ±S` or some element of `S` anti-commutes with `E^†F`.

We write `[[N, K, d]]_q` for a `q`-ary quantum code of length `N`,
`dim = q^K` and distance `d`; `[[N,K,d;c]]_q` denotes an
**entanglement-assisted** code consuming `c` maximally entangled `q`-ary pairs.
No `q`-ary/`p`-ary mixing occurs anywhere: the qudits have dimension `q` and the
commutation phase is `chi ∘ Tr_{F_q/F_p}`.

---

## 1. Task A — the inner product induced on the Gray image

The induced form is T-177's form, `⟨u,v⟩^{\widehat{}}_s = u^{[s]} J v^T`.  Three
distinct regimes occur, and **they are not equivalent**.  Keeping them apart is
mandatory: collapsing them silently re-introduces exactly the error the
safeguards forbid (assuming the induced form is Euclidean).

### A1 — the general Galois regime (all `s`)

`⟨·,·⟩^{\widehat{}}_s` is additive, right-`F_q`-linear and **left-`sigma_s`-semilinear**
(sesquilinear), with Gram matrix `J = I_{4n} ⊗ H_t`.  It is *not* symmetric and
*not* Hermitian in the naive sense: by T-186,

$$\langle v,u\rangle^{\widehat{}}_s = \sigma_s\big(\langle u,v\rangle^{\widehat{}}_s\big)
\iff r \mid 2s .$$

The double dual is `D^{\perp^{\widehat{}}\perp^{\widehat{}}} = \widehat{\sigma}_{2s}(D)`
(T-177), where `widehat{sigma}_{2s}` is the componentwise `sigma_{2s}` on `F_q^N`.

### A2 — the reflexive regime (`r | 2s`)

Then `sigma_{2s} = id`, so the Galois duality is **reflexive**: `D^{\perp\perp} = D`
for every code.  Equivalently (T-186) the orthogonality *relation* is symmetric.
Note that reflexivity of the duality is **not** the same as symmetry of the form
as a *value* (`⟨u,v⟩ = ⟨v,u⟩`), which holds iff `r | s` (T-186); for `r = 2`,
`s = 1` the form is Hermitian (`⟨v,u⟩ = sigma_1⟨u,v⟩`) but not symmetric.

### A3 — per-code `sigma_{2s}`-invariance (strictly weaker)

For a **single** code `D` the condition `\widehat{\sigma}_{2s}(D) = D` already gives
`D^{\perp\perp} = D`, without any hypothesis on `r, s`.  It is strictly weaker
than A2.

> **T-190 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]`).**  At `(q,t,n,s) = (8,1,2,1)`
> one has `r = 3`, `2s = 2`, so `r ∤ 2s`: **not** reflexive.  Of the `92` nonzero
> image codes exactly `14` satisfy `\widehat{\sigma}_2(D) = D`, and exactly those
> `14` satisfy `D^{\perp\perp} = D`; the other `78` do not.  In the reflexive
> instances `(4,1,2,1)`, `(9,2,1,1)`, `(4,2,2,1)` all codes are
> `\widehat{\sigma}_{2s}`-invariant (32/32, 112/112, 1220/1220) and all satisfy
> `D^{\perp\perp} = D`.
>
> Consequently the three regimes A1 ⊋ A2 ⊋ A3 are **pairwise non-equivalent**,
> and the count `14 = 14` independently re-confirms T-177's double-dual formula.

> **T-191 (PROVED).**  `⟨·,·⟩^{\widehat{}}_s` is Euclidean **iff** `t = 1` **and**
> `r | s` (then `J = I` and `sigma_s = id`).  In every other case the induced
> form is a genuine `sigma_s`-Hermitian Hankel form.  *Verified* `[EXH]` on 7
> parameter sets (Part B3 of the log): the transported form is Euclidean exactly
> at `t = 1, s = 0`.

---

## 2. Task B — self-orthogonality of hulls, and the three routes

### 2.1 The Galois hull is always self-orthogonal

> **T-192 (PROVED; verified `[EXH]` on 226 hulls in 8 parameter sets).**
> For every right `R_n`-submodule `C` and every `s`,
> $$\varphi_n(\mathrm{Hull}_s(C)) \subseteq
>   \varphi_n(\mathrm{Hull}_s(C))^{\perp^{\widehat{}}_s},$$
> i.e. every Galois hull is self-orthogonal for the transported form.
> **No reflexivity hypothesis and no principality hypothesis is needed.**

*Proof.*  Let `H = Hull_s(C) = C ∩ C^{\perp_s}` and `x, y ∈ H`.  Then `x ∈ C`
and `y ∈ C^{\perp_s}`; by the definition of `C^{\perp_s}` (`b_s(c,y) = 0` for
all `c ∈ C`) we get `b_s(x,y) = 0`.  Transporting with `phi_n` (T-178) gives
`⟨phi_n x, phi_n y⟩^{\widehat{}}_s = 0`.  ∎

This is a *one-sided* argument: it uses `y ∈ C^{\perp_s}` and `x ∈ C`, and never
interchanges the two slots.  It therefore does **not** require the symmetry of
the orthogonality relation (`r | 2s`), which is exactly the subtlety the
safeguards warn about.  Note also what it does **not** say: a nonzero hull
dimension never implies that `C` itself is self-orthogonal.

### 2.2 Route R1 — the Galois-native twisted stabilizer embedding

For `D ⊆ F_q^N` put `T_s(u) := (u^{[s]} J)^{\mathsf T}` (an additive,
`sigma_s`-semilinear map) and

$$\mathcal C_T := \{(u \mid T_s u) : u \in D\}\ \subseteq\ F_q^{2N}.$$

> **T-193 (PROVED).**  For all `u,u' ∈ D`,
> $$\omega\big((u|T_su),(u'|T_su')\big)
>   = \langle u',u\rangle^{\widehat{}}_s - \langle u,u'\rangle^{\widehat{}}_s .$$
> Consequently, if `D` is self-orthogonal (`⟨u,u'⟩ = 0` for all `u,u' ∈ D`) then
> `omega = 0` on `C_T`, the operators `E(u|T_su)` pairwise commute, and each has
> order `p` because `u · (T_s u) = ⟨u,u⟩^{\widehat{}}_s = 0`.  Since
> `|C_T| = |D| = q^k`, Lemma Q2 gives
> $$\boxed{\ [[\,N,\ N-k,\ d\,]]_q\ },\qquad
>   d = \min\{\mathrm{sw}(v) : v \in \mathcal C_T^{\perp_{Tr∘omega}}\setminus\mathcal C_T\ \text{(mod }\mathcal C_{T,0})\}.$$
> **No coordinate transformation and no reflexivity hypothesis is used.**

*Proof of the identity.*  `(T_s u)_i = Σ_j sigma_s(u_j) J_{ji}`, hence
`u · (T_s u') = Σ_{i,j} u_i sigma_s(u'_j) J_{ji} = ⟨u',u⟩^{\widehat{}}_s`
(relabel `i↔j`, `J` symmetric); likewise `u' · (T_s u) = ⟨u,u'⟩^{\widehat{}}_s`. ∎

> **T-194 (PROVED, `[EXH]`).**  `R1` yields **no** good distances, for a
> structural reason: for every `b ∈ D^{\perp_E}` the vector `(0|b)` lies in
> `C_T^{\perp_omega}`, so
> $$d_{R1} \;\le\; \min \mathrm{wt}\big(D^{\perp_E}\big).$$
> Verified `[EXH]`: in every parameter set scanned the upper bound is `1` or `2`
> (Part B2 of the log; 18 codes).

> **T-195 (PROVED + `[EXH]`).**  *When is `C_T` abelian?*
> 1. In the **reflexive** regime (`r | 2s`) `C_T` is abelian for **every** code,
>    self-orthogonal or not: there `⟨u',u⟩ = sigma_s(⟨u,u'⟩)` and the absolute
>    trace is Galois-invariant, so `Tr(omega) = 0` identically.  Verified: at
>    `(4,1,2,1)` all `32/32` codes give an abelian group (only `12` are
>    self-orthogonal), at `(9,2,1,1)` all `60/60`.
> 2. **Outside** the reflexive regime the group is abelian exactly for the
>    self-orthogonal codes: at `(8,1,2,1)`, `12` abelian out of `92`, and
>    `12` self-orthogonal — the same `12`.
>
> So "self-orthogonal" is sufficient always, necessary only outside the
> reflexive regime; in the reflexive regime extra abelian groups appear, but by
> T-194 their distance is `1`.

### 2.3 Route R2 — the Euclidean / CSS stabilizer route

Take `C = A × B ⊆ F_q^{2N}` with `A, B` classical codes.  Then
`omega((a|0),(0|b)) = a·b`, so `C` is isotropic iff `A ⊆ B^{\perp_E}`, and
`dim C = dim A + dim B`, giving `K = N − dim A − dim B`.

> **T-196 (PROVED).**  Let `D' ⊆ F_q^N` be `F_q`-linear of dimension `k`.
> 1. If `D' ⊆ D'^{\perp_E}` (Euclidean self-orthogonal) then `A = B = D'` gives
>    `[[N, N−2k, d]]_q` with
>    `d = min wt(D'^{\perp_E} \ D')`.
> 2. If `D'^{\perp_E} ⊆ D'` (dual-containing) then `A = B = D'^{\perp_E}` gives
>    `[[N, 2k−N, d]]_q` with
>    `d = min wt(D' \ D'^{\perp_E})`.
>
> (The distance formulas: `C^{\perp_omega} = B^{\perp_E} × A^{\perp_E}`; a vector
> `(a|b)` outside `C` has `a ∉ A` or `b ∉ B`, and `sw(a|b) ≥ max(wt a, wt b)`,
> while `b = 0` resp. `a = 0` attain the bound.)

**When is `D'` allowed to be `D = phi_n(C)` itself?**  By T-191, only when the
transported form is Euclidean, i.e. `t = 1` and `r | s`.  Otherwise a
**coordinate transformation** is needed — this is Task C (§3).

### 2.4 Route R3 — the entanglement-assisted route

> **T-197 (PROVED).**  Let `D ⊆ F_q^N` be any `F_q`-linear code, `dim D = k`,
> and put `C = D × D` (an `F_q`-linear, generally non-isotropic subspace of
> `F_q^{2N}` of dimension `2k`).  Its isotropic part is
> `C_0 = Hull_E(D) × Hull_E(D)`, where `Hull_E(D) = D ∩ D^{\perp_E}`, so the
> commutativity defect is `c = 2k − 2 h_E` over `F_q`, i.e. **`c = k − h_E`**
> maximally entangled `q`-ary pairs, and
> $$\boxed{\ [[\,N,\ N-2k+c,\ d\ ;\ c\,]]_q = [[\,N,\ N-k-h_E,\ d\ ;\ k-h_E\,]]_q\ },
> \qquad d = \min \mathrm{wt}\big(D^{\perp_E}\setminus \mathrm{Hull}_E(D)\big).$$
> For `h_E = k` (`D` Euclidean self-orthogonal) this degenerates to `c = 0` and
> reproduces T-196(1) — a consistency check the script performs.

Verified numerically (Part B2b): at `(4,1,2,0)` the best EA parameters are
`[[8,4,3;4]]_4` (from `k = 4`, `h_E = 0`), at `(4,1,3,0)` `[[12,10,2;2]]_4`, at
`(4,1,4,0)` `[[16,12,2;0]]_4` (i.e. an ordinary stabilizer code).

**Remark (field discipline).**  `C = D × D` is `F_q`-linear, so the
trace-symplectic and the `F_q`-symplectic orthogonal coincide (non-degeneracy of
the trace form) and the entanglement count is `c = k − h_E`, an `F_q`-quantity.
For the **semilinear** group `C_T` of R1 the standard `q`-ary EA formula does
*not* apply unchanged (`C_T` is only `F_p`-linear); that extension is left OPEN
(§10, O-5.3).

### 2.5 Comparison and recommendation

| | R1 (twisted, Galois-native) | R2 (Euclidean/CSS) | R3 (EA) |
|---|---|---|---|
| hypothesis on the code | `D ⊆ D^{\perp^{\widehat{}}}_s` | `D'` Euclidean SO or DC | none |
| hypothesis on `(t,s)` | **none** | `t = 1, r\|s`, or a congruence exists (§3) | none |
| uses the Galois structure | yes (the twist `sigma_s`) | only via `phi_n` + the congruence | no (Euclidean hull) |
| dimension | `K = N − k` | `K = N − 2k` (SO), `2k−N` (DC) | `K = N − k − h_E` |
| cost | — | — | `c = k − h_E` ebits |
| distance bound | `≤ min wt(D^{\perp_E})` (T-194) | `min wt(D'^{\perp_E}\setminus D')` | `min wt(D^{\perp_E}\setminus Hull_E)` |
| best `d` found | 2 | **3** (`[[16,4,3]]_4`) | **3** (`[[8,4,3;4]]_4`) |

> **Recommendation (Task B).**  Use **R2 as the primary route** whenever the
> transported form is already Euclidean (`t = 1`, `r | s`) or a congruence
> exists (`§3`): it is the only route whose distance is *not* capped by
> `min wt(D^{\perp_E})`, and it needs no extra physical resource.  Use **R1 as
> the Galois-native route** for `t ≥ 2` when **no** congruence exists — this is
> exactly the case of the non-principal O-3.1 hull witnesses at `(4,2,·)` —
> accepting the distance cap of T-194.  Use **R3** when one is willing to spend
> entanglement: it converts *any* image code, including LCD ones (`h_E = 0`),
> into a code, and at `N = 8` it buys `d = 3` where R2 only reaches `d = 2`,
> at the price of `4` ebits.

---

## 3. Task C — from the Gray image to physical coordinates

### 3.1 How many physical coordinates?  (derived, not assumed)

`phi_n : R^n → F_q^N` is an `F_q`-linear bijection onto `F_q^N` with
`N = dim_{F_q} R^n = (dim_{F_q} R)·n`, and
`dim_{F_q} R = 4·dim_{F_q} A_t = 4t`.  One qudit of dimension `q` carries one
`F_q`-coordinate, hence

$$\boxed{N_{\rm phys} = N = 4tn.}$$

> **T-198 (PROVED, verified `[EXH]`).**  `N_phys = 4tn` for every instance:
> `(4,1,2) → 8`, `(4,2,1) → 8`, `(4,2,2) → 16`, `(4,2,3) → 24`
> (`dim_{F_q} A_t = t`, `dim_{F_q} R = 4t` verified from the module structure).

There is **no** doubling to `2·4tn` (that would be the *symplectic* space
`F_q^{2N}` in which the stabilizer group lives — a bookkeeping space, not a set
of qudits), and **no** `4tn` → `8tn` inflation.  The `[[N,K,d]]_q` codes below
have length `N = 4tn` and no more.

### 3.2 Converting the Hankel form

Assume `sigma_s = id` (i.e. `r | s`), so the transported form is the **bilinear**
form with matrix `J`.  Let `T` be a `t×t` matrix with `T^{\mathsf T} H_t T = I_t`
and `TT := I_{4n} ⊗ T` (block-diagonal in the `((e·4+k)·t + a)` ordering), and
define

$$\Psi : F_q^N \to F_q^N,\qquad \Psi(u) := u\,\mathcal T .$$

Since `TT·TT^{\mathsf T} = J^{-1}` and `J^2 = I` (T-177),

$$\Psi(u)\cdot\Psi(v) = u\,\mathcal T\mathcal T^{\mathsf T} v^{\mathsf T}
 = u\,J^{-1}v^{\mathsf T} = u\,J\,v^{\mathsf T} = \langle u,v\rangle^{\widehat{}}_s .$$

> **T-199 (PROVED; the eight properties verified `[EXH]` for
> `(q,t,n) = (4,1,2), (9,2,1), (9,2,2)`; Part C2 of the log).**
> 1. `T^{\mathsf T}H_tT = I_t`;
> 2. `\mathcal T\mathcal T^{\mathsf T} = J`;
> 3. `J^2 = I` (used essentially);
> 4. `\mathcal T` is invertible;
> 5. `\mathcal T` is **monomial iff `t = 1`**; for `t = 2` and `p` odd it is not
>    monomial (`(9,2,1)`: `T = [[3,2],[3,1]]`; `(9,2,2)`: likewise);
> 6. `\Psi` transports the form to the Euclidean form (verified on all pairs of
>    basis vectors, hence by bilinearity everywhere);
> 7. `\mathcal T` commutes with the block shift `\widehat T` (so the
>    quasi-cyclic index `4t` structure is preserved);
> 8. `\Psi` is `F_q`-linear (not merely semilinear) — hence it maps `F_q`-linear
>    codes to `F_q`-linear codes and preserves `F_q`-dimension.

**Consequence (the congruence trade-off).**  By property 5 a non-monomial
`\Psi` is **not** a Hamming isometry, so every distance must be recomputed in the
physical coordinates.  Measured (Part C3 of the log, `[EXH]`/`[SMP]`):

| instance | congruence | monomial | codes transformed | codes whose `d` changes |
|---|---|---|---|---|
| `(4,1,2)` | yes | **yes** | — | distances preserved |
| `(9,2,1)` | yes | no | 13 | 0/13 (but a weight-changing vector exists, `[SMP]`) |
| `(9,2,2)` | yes | no | 5 | **3/5** |
| `(4,2,1)`, `(4,2,2)`, `(4,2,3)` | **none exists** | — | — | Euclidean route blocked |

> **T-200 (PROVED, `[EXH]` exhaustive over all `4×4` matrices over `F_4`).**
> For `p = 2` and `t` even **no** `T` with `T^{\mathsf T}H_tT = I_t` exists,
> because `H_t` is then alternating (T-177) and an alternating matrix cannot be
> congruent to the identity.  Hence for `(q,t) = (4,2)` (and every `q` a power
> of `2` with `t` even) **the Euclidean/CSS route R2 is obstructed outright**,
> independently of the code: no coordinate change whatsoever converts the
> transported Hankel form into the Euclidean form.  In those cases R1 (§2.2) is
> the *only* route attached to the Galois structure.

---

## 4. Task D — explicit codes

For each parameter set the table lists: (1) `(q,t,n,s)`; (2) the ring; (3) the
code `C` and its image `D = phi_n(C)`; (4) `N, k`; (5) the transported form and
its regime; (6) the hull (`dim`, `mu_B`); (7) the self-orthogonality status;
(8) commutation (direct verification); (9) the route; (10) the parameters;
(11) the distance evidence; (12) the bounds; (13) the comparison status.
Items (1)–(7), (9)–(12) are tabulated; items (3), (8), (11) are verified per
code in Parts D2/D3 of the log.

### 4.1 The required families

| # | `(q,t,n,s)` | `N` | route | `k` | hull `dim` / `mu_B` | SO? | commutation | `[[N,K,d]]_q` | distance evidence | Singleton defect | Hamming |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `(4,1,2,0)` | 8 | R2-SO | 2 | 2 / — | yes | `[EXH]` 8×8 `F_p`-basis pairs | **`[[8,4,2]]_4`** | `[EXH]` sw ≤ 2 | 2 | ok |
| 2 | `(4,1,2,0)` | 8 | R2-DC | 6 | 2 / — | DC | `[EXH]` | **`[[8,4,2]]_4`** | `[EXH]` sw ≤ 2 | 2 | ok |
| 3 | `(4,1,3,0)` | 12 | R2-SO | 2 | 2 / — | yes | `[EXH]` | **`[[12,8,2]]_4`** | `[EXH]` sw ≤ 2 | 2 | ok |
| 4 | `(4,1,3,0)` | 12 | R2-DC | 10 | 2 / — | DC | `[EXH]` | **`[[12,8,2]]_4`** | `[EXH]` | 2 | ok |
| 5 | `(4,1,4,0)` | 16 | R2-SO | 6 | 6 / — | yes | `[EXH]` 24×24 | **`[[16,4,3]]_4`** | `[EXH]` sw ≤ 3 + K-L `t=1` ✓ (58 081 pairs) | 8 | ok |
| 6 | `(4,1,4,0)` | 16 | R2-DC | 10 | 6 / — | DC | `[EXH]` 24×24 | **`[[16,4,3]]_4`** | `[EXH]` sw ≤ 3 + K-L ✓ | 8 | ok |
| 7 | `(8,1,2,0)` | 8 | R2-SO | 2 | 2 / — | yes | `[EXH]` 12×12 | **`[[8,4,2]]_8`** | `[EXH]` | 2 | ok |
| 8 | `(9,1,2,0)` | 8 | R2-SO | 2 | 2 / — | yes | `[EXH]` 8×8 | **`[[8,4,2]]_9`** | `[EXH]` | 2 | ok |
| 9 | `(4,2,1,1)` | 8 | R1 | 2 | 2 / — | yes | `[EXH]` (twisted) | `[[8,4,1]]_4` | `[EXH]` d = 1 | 4 | ok |
| 10 | `(9,2,1,0)` | 8 | **R2 + `\Psi`** | 2 | 2 / — | yes (after `\Psi`) | `[EXH]` | **`[[8,4,2]]_9`** | `[EXH]` | 2 | ok |
| 11 | `(4,2,2,1)` | 16 | **R1, non-principal hull** | 6 | 6 / **`mu_B = 4`** | yes | `[EXH]` 12 `F_p`-elements | **`[[16,10,2]]_4`** | `[EXH]` sw ≤ 2 + upper bound 2 | 2 | ok |
| 12 | `(4,2,2,1)` | 16 | R1, non-principal hull | 8 | 8 / **`mu_B = 4`** | yes | `[EXH]` 16 `F_p`-elements | **`[[16,8,2]]_4`** | `[EXH]` | 6 | ok |
| 13 | `(4,2,2,0)` | 16 | R2 (accidental) | 10 | 6 / — | DC | `[EXH]` | `[[16,4,2]]_4` | `[EXH]` | 10 | ok |
| 14 | `(4,2,3,0)` | 24 | R2 (accidental) | 16 | 8 / — | DC | `[EXH]` | **`[[24,8,2]]_4`** | `[EXH]` | 14 | ok |
| 15 | `(4,2,3,0)` | 24 | R2 (accidental) | 4 | 4 / — | SO | `[EXH]` | **`[[24,16,2]]_4`** | `[EXH]` | 6 | ok |
| 16 | `(4,1,2,0)` | 8 | **R3 (EA)** | 4 | `h_E = 0` (LCD) | n/a | `[EXH]` | **`[[8,4,3;4]]_4`** | `[EXH]` | (EA) | ok |
| 17 | `(4,1,3,0)` | 12 | R3 (EA) | 2 | `h_E = 0` | n/a | `[EXH]` | `[[12,10,2;2]]_4` | `[EXH]` | (EA) | ok |

**Notes on rows 13–15 (honesty requirement).**  For `(q,t) = (4,2)` the
transported form is *not* Euclidean and **no** congruence exists (T-200).  The
codes in rows 13–15 are those image codes that happen to be **Euclidean**
self-orthogonal / dual-containing; the Galois form is **not** used in their
construction, and the log says so explicitly.  The route genuinely attached to
`(4,2,·)` is R1 — rows 9, 11, 12.

**Rows 11–12 are the priority examples of Task D.**  At `(q,t,n,s) = (4,2,2,1)`
there are `166` self-orthogonal codes with nonzero hull, of which **66 have a
non-principal Galois hull** (`mu_B = 4 ≥ 3`, the O-3.1 witness family of
T-173: hulls are *not* always principal).  Their images give, via the
Galois-native route R1, `[[16,10,2]]_4` and `[[16,8,2]]_4`, with the stabilizer
group verified abelian on an `F_p`-basis and the generators verified of order
`p`.  No principality hypothesis enters (T-179).

### 4.2 The four required parameter sets, with the missing data

* **`(q,t,n) = (4,1,2)`** — rows 1–2, plus the EA row 16.  `N = 8`, form
  Euclidean (`t = 1`, `s = 0`), `10` self-orthogonal and `6` dual-containing
  image codes; best `[[8,4,2]]_4` (stabilizer) and `[[8,4,3;4]]_4` (EA).
* **`(4,2,1)`** — row 9 (R1) and, in the accidental-Euclidean reading,
  `[[8,4,1]]_4`.  `N = 8`, form `I_{4n}⊗H_2`, `p = 2`, `t` even ⟹ **no**
  congruence (T-200); R1 is the only Galois route and its distance is `1`–`2`
  here (T-194).
* **`(4,2,2)`** — rows 11–13.  `N = 16`, `1220` nonzero image codes, `356`
  self-orthogonal, `208` dual-containing; `66` non-principal hulls with
  `mu_B = 4`.
* **`(4,2,3)`** — rows 14–15.  `N = 24`; enumeration is infeasible in full, so a
  **sample of 300 codes** was used (`[SMP]`, seed `20261120`): `12`
  self-orthogonal and `12` dual-containing among the sampled codes.  The
  reported parameters are therefore verified only on that sample.
* **Admissible `q = 8, 9`** — rows 7 (`q = 8`) and 8, 10 (`q = 9`).

---

## 5. Task E — the parameter theorem

> **T-201 (PROVED).**  Let `C ≤ R_n` be a right `R_n`-submodule,
> `D = phi_n(C) ⊆ F_q^N`, `N = 4tn`, `k = dim_{F_q} D`.  Then:
>
> 1. **(R1)** if `D ⊆ D^{\perp^{\widehat{}}}_s` then there is a `q`-ary
>    stabilizer code `[[N, N−k, d]]_q` with
>    `d = min{sw(v) : v ∈ \mathcal C_T^{\perp_{Tr∘omega}}\setminus \mathcal C_T}`
>    and `d ≤ min wt(D^{\perp_E})`.
> 2. **(R2-SO)** if `D'` is Euclidean self-orthogonal of dimension `k` then
>    `[[N, N−2k, d]]_q` with `d = min wt(D'^{\perp_E}\setminus D')`; if `D'` is
>    dual-containing then `[[N, 2k−N, d]]_q` with
>    `d = min wt(D'\setminus D'^{\perp_E})`.  Here `D' = D` when `t = 1` and
>    `r | s`, and `D' = \Psi(D)` when a congruence `\Psi` as in §3.2 exists.
> 3. **(R3)** for arbitrary `D`, `[[N, N−k−h_E, d ; k−h_E]]_q` with
>    `h_E = dim(D ∩ D^{\perp_E})` and
>    `d = min wt(D^{\perp_E}\setminus Hull_E(D))`.
>
> All dimensions are over `F_q`, all lengths are `N = 4tn`, and the alphabet of
> the quantum code is `F_q` (no `p`-ary substitution anywhere).  The
> verification script recomputes `K` from `K = N − dim_{F_q}\mathcal C`
> (row by row, `[EXH]`) and, for the small instances, independently from the
> Hilbert-space formula `K = (1/|S|)Σ_{g∈S} Tr(g)` (Part A3).

---

## 6. Task F — bounds, defects and comparison with the literature

> **T-202 (COMPUTATIONALLY VERIFIED ONLY, `[EXH]` on all 17 constructed codes).**
> Every code of §4 satisfies the **quantum Singleton bound**
> `N − K ≥ 2(d−1)` and the **quantum Hamming bound**
> `q^K Σ_{j=0}^{⌊(d−1)/2⌋} C(N,j)(q²−1)^j ≤ q^N`.  The Singleton defects
> `N − K − 2(d−1)` are tabulated in §4.1 (smallest: `2`, attained by
> `[[8,4,2]]_{4,8,9}`, `[[12,8,2]]_4` and `[[16,10,2]]_4`).

**No code found here meets the quantum Singleton bound with equality except in
the degenerate `d = 2`, `K = N−2` cases** (`[[N,N−2,2]]_q`, which exist for every
`N` from any `1`-dimensional self-orthogonal code).  The best distance found is
`d = 3`: `[[16,4,3]]_4` (stabilizer, defect `8`) and `[[8,4,3;4]]_4`
(entanglement-assisted, `c = 4`).

**Comparison with the literature — and the limits of this comparison.**  The
sandbox has no access to Grassl's code tables; the comparison below is therefore
against *bounds* and against the *structural* literature, not against a table of
best-known codes.  Consequently:

* **No claim of record parameters is made.**  The novelty claim is about the
  **origin** of the codes (§8), not about their parameters.
* The relevant structural comparison is the commutative `l`-Galois literature
  (Zhang–Kong–Zheng; arXiv:2106.07962; MDPI 2023/2026), where Gray images of
  (consta)cyclic codes are quasi-cyclic, duality and hulls are preserved, and
  CSS/EA quantum codes are built — always over **commutative** rings and with
  the **Euclidean or plain Hermitian** form.  The differences are listed in §8.2.
* Within the non-commutative matrix-ring literature (arXiv:1409.7228,
  arXiv:1008.1387, arXiv:2602.18255) **no** quantum construction was found at
  all; the quantum step in those papers is absent.

---

## 7. Task G — verification, negative controls, labelling

**Verification.**  `04_COMPUTATION/phase5_quantum_constructions.py`
(`SEED = 20261120`, Python 3.11.2) runs in ≈ 80 s and produces
`04_COMPUTATION/phase5_quantum_log.txt`: **88 checks, 88 PASS, 0 FAIL**,
byte-identical over repeated runs (verified).  Structure:

* **Part A** — the quantum framework on a genuine Hilbert space
  (`q = 4`, `N = 2`, `dim = 16`): the Weyl relation (`[EXH]`, 256 pairs);
  commutation ⟺ `Tr(omega) = 0` (`[SMP]`, 60×60);
  `K = (1/|S|)Σ_g Tr(g) = q^N/|C|` (`[EXH]`, `K = 8,4,2,1`);
  the Knill–Laflamme criterion.
* **Parts B, B2b** — the hull theorem and the three routes with parameters.
* **Part C** — the physical-coordinate map: `N_phys = 4tn`, the eight
  properties, the weight-change measurement.
* **Parts D, D2, D3** — the explicit codes, each verified individually:
  abelian (on an `F_p`-basis), `|C| = q^{dim C}`, `K = N − dim C`, the distance
  by exhaustive increasing symplectic weight, and Knill–Laflamme for the
  correction radius when `d ≥ 3`.
* **Part E** — the bounds.
* **Part F** — the negative controls.

**Negative controls (each must fail, and does).**

| id | control | outcome |
|---|---|---|
| N1a | in the reflexive regime `C_T` is abelian for **every** code (so "self-orthogonal" is not necessary there) | `[EXH]` 32/32 abelian, 12/32 SO ✓ |
| N1b | outside the reflexive regime abelian ⟺ self-orthogonal | `[EXH]` (8,1,2,1): 12 abelian = 12 SO of 92 ✓ |
| N2 | at `(4,2,1)` some transported-self-orthogonal codes are **not** Euclidean self-orthogonal, so R2 is invalid without a transformation | `[EXH]` 8 such codes ✓ |
| N3 | at `(q,t) = (4,2)` **no** congruence exists (Euclidean route obstructed) | `[EXH]` all 4×4 matrices over `F_4` ✓ |
| N4 | the twisted embedding admits a weight-1 operator commuting with the group and not in it ⟹ `d = 1` | `[EXH]` witness exhibited ✓ |
| N5 | testing commutation on an `F_q`-basis is **not** sufficient | `[EXH]` ✓ (see below) |
| A4b | a distance-1 code fails Knill–Laflamme with `t = 1` | `[EXH]` ✓ |

> **T-203 (PROVED + `[EXH]`).**  For the `[[16,4,3]]_4` code of row 5 the
> weight-1 operator `(0|e_0)` commutes with all `12` `F_q`-generators of the
> stabilizer yet not with all `24` elements of an `F_p`-basis, because
> `Tr_{F_4/F_2}(1) = 0`.  Hence the naive test "commutes with every
> `F_q`-generator" would report `d = 1` instead of the correct `d = 3`.
> The correct criterion is `omega(v,c) = 0` **as an element of `F_q`** for all
> `c ∈ C` (equivalently: commutation with every element of an `F_p`-basis); for
> `F_q`-linear `C` this is exactly the `F_q`-symplectic orthogonal
> `C^{\perp_omega} = B^{\perp_E} × A^{\perp_E}`.

**Labelling.**  In this file and in the register: **PROVED** = T-191…T-203 (with
the proof given), **COMPUTATIONALLY VERIFIED ONLY** = T-190, T-202 and all
`[SMP]` rows (the `(4,2,3)` sample), **OPEN** = O-5.1…O-5.6 (§10).  No statement
here is left unlabelled.

---

## 8. Task H — literature, novelty, and `references.bib`

### 8.1 What exists (carried forward from Phase 4 §8, plus the QECC side)

| source | content | distance to Phase 5 |
|---|---|---|
| Greferath–Schmidt, *Gray isometries for finite chain rings*, IEEE IT **45** (1999) 2522–2524 | isometry `(S,d_Hom) ↪ (F_q^{m−1}, d_Ham)`, **chain rings only** | not applicable to `M_2(A_t)` |
| Honold; Constantinescu–Heise; Greferath–O'Sullivan | homogeneous weight on finite (Frobenius) rings | weights, no duality-to-quantum step |
| Oggier–Belfiore–Viterbo (arXiv:1008.1387); arXiv:1409.7228 | Bachoc weight on `M_2(F_p)` / `M_2(F_2[i])`; Euclidean + Hermitian duals; `p ≡ 2,3 mod 5` | closest matrix-ring prior work; `t = 1`, **no** Galois-shift dual, **no** hulls, **no** quantum codes |
| arXiv:2602.18255 (`M_4(F_2[u]/<u^k>)`) | Gray + Bachoc maps, cyclic codes | matrix alphabet, no Galois duality, no hulls, no quantum codes |
| Ketkar–Klappenecker–Kumar–Sarvepalli (2006) | non-binary (`q`-ary) stabilizer formalism | **the framework used in §0** (adapted here to `chi ∘ Tr_{F_q/F_p}`) |
| Calderbank–Shor–Steane; Gottesman | CSS and stabilizer constructions | T-196 is the `q`-ary CSS statement |
| Wilde–Brun / Lai–Brun–Wilde | entanglement-assisted stabilizer codes | T-197 is re-derived here in symplectic language, not imported |
| Zhang–Kong–Zheng; arXiv:2106.07962; MDPI 2023/2026 | `l`-Galois duals over **commutative** rings; `phi(C^⊥) = phi(C)^⊥`, hull = lcm, CSS + EA | the commutative template; Euclidean/Hermitian only |

### 8.2 What was **not** found (novelty gap)

No source was found that combines

1. a **non-commutative matrix-ring alphabet** `M_2(A_t)`, `t ≥ 1`;
2. **`sigma_s`-Galois duality transported through a Gray map**, with the target
   form identified as `u^{[s]}(I_{4n}⊗H_t)v^T` — Hermitian-with-**Hankel**, not
   Euclidean (T-177/T-191);
3. **hull compatibility including non-principal hulls** (`mu_B ≥ 3`, T-173 /
   O-3.1) — the priority examples of §4 (rows 11–12);
4. the **obstruction** of T-200: for `p = 2`, `t` even the Hankel form is
   alternating, so **no** coordinate change converts it into the Euclidean form
   and the CSS route is impossible in principle;
5. a **quantum** construction (stabilizer or entanglement-assisted) whose
   classical ingredient is a Galois hull over a non-commutative ring.

Items 2–5 are the novelty claim of Phase 5, relative to arXiv:1409.7228 and
arXiv:2602.18255 (matrix alphabets, no Galois hulls, no quantum step) and to the
commutative `l`-Galois literature (hulls and quantum codes, but commutative and
Euclidean/Hermitian).

### 8.3 Search limitation (stated explicitly, as in Phase 4 §8.3)

The search was performed with a general web-search tool: titles, abstracts and
excerpts were read, but **no PDF was downloaded and no reference list was
followed**; Grassl's code tables were **not** reachable.  Hence (i) "not found"
is evidence, not proof; (ii) no claim of record parameters is made (§6); (iii)
the entries added to `references.bib` are tagged `VERIFY` where the bibliographic
detail (pages, year, exact title) has not been confirmed against the publisher
record.

---

## 9. Results of Phase 5 (register rows T-190 … T-203)

| ID | statement | status |
|---|---|---|
| **T-190** | the three regimes A1 ⊋ A2 ⊋ A3 are pairwise non-equivalent; witness `(8,1,2,1)`: 14/92 `sigma_2`-invariant and exactly those satisfy `D^{⊥⊥} = D` | **COMPUTATIONALLY VERIFIED ONLY** (`[EXH]`) |
| **T-191** | the transported form is Euclidean ⟺ `t = 1` and `r ∣ s` | **PROVED** (`[EXH]`, 7 instances) |
| **T-192** | every Galois hull is self-orthogonal; no reflexivity, no principality | **PROVED** (`[EXH]`, 226 hulls) |
| **T-193** | R1: `omega = ⟨u',u⟩ − ⟨u,u'⟩`; self-orthogonal `D` ⟹ abelian, order `p`, `[[N,N−k,d]]_q` | **PROVED** |
| **T-194** | `d_{R1} ≤ min wt(D^{⊥_E})`; attained values `1`–`2` | **PROVED** + `[EXH]` |
| **T-195** | reflexive ⟹ `C_T` abelian for every code; non-reflexive ⟹ abelian exactly for SO codes | **PROVED** + `[EXH]` |
| **T-196** | R2: `[[N,N−2k,d]]_q` (SO) / `[[N,2k−N,d]]_q` (DC) with the stated distances | **PROVED** |
| **T-197** | R3: `[[N,N−k−h_E,d;k−h_E]]_q`, `d = min wt(D^{⊥_E}\setminus Hull_E)` | **PROVED** |
| **T-198** | `N_phys = 4tn` (derived from `dim_{F_q} R = 4t`) | **PROVED** (`[EXH]`) |
| **T-199** | the eight properties of `\Psi(u) = u(I_{4n}⊗T)`; non-monomial for `t ≥ 2`, `p` odd | **PROVED** (`[EXH]`) |
| **T-200** | for `p = 2`, `t` even no congruence exists ⟹ the Euclidean route is obstructed | **PROVED** (`[EXH]`) |
| **T-201** | the parameter theorem for all three routes, all over `F_q` | **PROVED** |
| **T-202** | all 17 constructed codes satisfy the quantum Singleton and Hamming bounds | **COMPUTATIONALLY VERIFIED ONLY** (`[EXH]`) |
| **T-203** | the commutation test must be run on an `F_p`-basis (`Tr_{F_4/F_2}(1) = 0`) | **PROVED** + `[EXH]` |

---

## 10. Open problems

* **O-5.1.** Does any Galois-hull-based construction in this pipeline reach
  `d ≥ 3` for `t ≥ 2`?  For `p = 2`, `t` even this is blocked for R2 by T-200,
  and R1 is capped at `d ≤ 2` by T-194; for `p` odd, `t = 2` the congruence
  exists and R2 is available — the instances `(9,2,2)`, `(27,2,2)` are not yet
  scanned.
* **O-5.2.** Is `d_{R1} = min wt(D^{\perp_E})` exactly (not merely `≤`)?  In
  every case scanned the exhaustive search and the upper bound agree.
* **O-5.3.** The entanglement number for the **semilinear** group `C_T` (only
  `F_p`-linear): the correct `q`-ary EA statement requires dividing the
  `F_p`-symplectic defect by `2r`; the divisibility and the resulting parameters
  are not settled here.
* **O-5.4.** Comparison against a table of best-known `q`-ary quantum codes
  (Grassl) is not possible offline; the parameters of §4 may or may not be
  already known.  **This must be done before any manuscript text is written.**
* **O-5.5.** The `mu_B` value is not tracked for the `(4,2,3)` sample nor for
  the `t = 1` families; a per-code `mu_B` census (principal vs non-principal
  hull) across all families is missing.
* **O-5.6.** The distance of the R1 codes is computed by an exhaustive search
  up to symplectic weight `2` plus the upper bound of T-194; for the
  `(4,2,2)`, `N = 16` cases a search at weight `3` would either improve or
  confirm the value `2`.

---

## 11. Completion report for Phase 5

* **Tasks A–H: complete.**  The induced form is identified and the three
  regimes are separated with witnesses (§1); the hull theorem is proved without
  any reflexivity or principality hypothesis (§2.1); the three routes are
  compared and one is recommended (§2.5); the physical coordinate count is
  *derived* as `4tn` and the Hankel→Euclidean conversion is given with eight
  properties and its cost measured, together with the obstruction for `p = 2`,
  `t` even (§3); explicit codes are given for all four required parameter sets
  plus `q = 8, 9`, prioritising non-principal hulls (§4); the parameters are
  proved (§5); the bounds and the literature comparison are given with no
  novelty claim about parameters (§6); verification and negative controls are in
  place with explicit labels (§7); the literature is recorded and
  `references.bib` is updated with `VERIFY` tags (§8).
* **Verification:** 88 checks, 88 PASS, 0 FAIL; log byte-reproducible.
  Artefact hashes (SHA-256): deliverable `8801541f…694bc`,
  script `d18dc66d…9c64` (1637 lines), log `dd4962cc…d03a0` (491 lines).
  Commit `ba95853` on `arena/59de606f-matrix-ring`.
* **Safeguards honoured:** no assumption that the induced form is Euclidean
  (refuted: T-191, T-200); no assumption that a non-monomial transformation
  preserves Hamming distance (measured: 3/5 codes change `d` at `(9,2,2)`);
  no assumption that `phi_n` is an isometry; no assumption that every hull is
  principal (the priority examples have `mu_B = 4`); self-orthogonality is never
  inferred from a nonzero hull dimension (T-192 is proved separately); no
  `q`-ary/`p`-ary mixing; no distance claimed without an exhaustive search or a
  proved bound; no novelty claim without a comparison; no manuscript work.
* **Phases 0–4 untouched:** all Phase 0–4 documents, scripts and logs verified
  byte-identical against the Phase-5 baseline; the register grew by insertion
  only.
