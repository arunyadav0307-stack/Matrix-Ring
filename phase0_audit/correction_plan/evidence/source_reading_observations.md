# Supplemental source-reading observations for the correction plan

These observations refine existing CP/CR action scopes. They are not repaired proofs, new theorems, new computations, or alterations of the independent audit. Exact line numbers refer to the frozen MS03 bytes in the inventory.

## CP01 — sections/04_cyclic_galois.tex:63–93

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

The printed polynomial closure proof uses an equality not established by the coefficient-level right action; require a side/index-complete proof review. Do not transplant the valid source theorem without its proof.

```text
63: \begin{proof}
64: (a) Let $y\in C^{\perp_s}$ and $a\in\Rn$; we must show $ya\in C^{\perp_s}$.
65: For $x\in C$ we have $xa\in C$ (as $C$ is a right ideal), hence
66: \[
67:   0=\bb_s(xa,y)=\Lambda\Bigl(\sum_e\theta_s\bigl((xa)_e\bigr)y_e\Bigr).
68: \]
69: We claim $\bb_s(x,ya)=\bb_s(xa,y)$. Indeed, writing
70: $(xa)_e=\sum_{i+j=e}x_ia_j$ (indices modulo $n$),
71: \[
72:   B_s(xa,y)=\sum_e\theta_s\Bigl(\sum_{i+j=e}x_ia_j\Bigr)y_e
73:   =\sum_{i,j}\theta_s(a_j)\theta_s(x_i)y_{i+j},
74: \]
75: while
76: \[
77:   B_s(x,ya)=\sum_i\theta_s(x_i)(ya)_i
78:   =\sum_{i,j}\theta_s(x_i)y_{i+j}a_j .
79: \]
80: These are not literally equal in the non-commutative ring $R$, but their images
81: under $\Lambda$ agree: by Lemma~\ref{lem:lambda}, $\Lambda$ is symmetric, so
82: $\Lambda(\theta_s(a_j)\theta_s(x_i)y_{i+j})
83: =\Lambda(\theta_s(x_i)y_{i+j}\theta_s(a_j))$, and summing over $i,j$ gives
84: $\bb_s(xa,y)=\bb_s(x,ya)$ up to applying $\sigma_s$ to the entries of $a_j$
85: inside a symmetric trace --- explicitly,
86: \[
87:   \bb_s(x,ya)=\sum_{i,j}\Lambda\bigl(\theta_s(x_i)y_{i+j}a_j\bigr)
88:   =\sum_{i,j}\Lambda\bigl(a_j\theta_s(x_i)y_{i+j}\bigr)
89:   =\sum_{i,j}\sigma_s\!\bigl(\Lambda(\theta_s(a_j)\theta_s(x_i)y_{i+j})\bigr),
90: \]
91: the last step because $\Lambda(\sigma_s(z))=\sigma_s(\Lambda(z))$ and
92: $\Lambda$ is symmetric; since $\bb_s(xa,y)=0$ and $\sigma_s$ is injective,
93: $\bb_s(x,ya)=0$. Hence $ya\in C^{\perp_s}$.
```

## CP03 — sections/03_preliminaries.tex:99–121

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex`

The failure lemma mixes M2(F2), t=2, a nilpotent u, ring versus trace orthogonals, and a generic finite Frobenius ring with an Fq-specific proof. Require a consistent example and typed proof; no new counterexample was computed here.

```text
99: \begin{lemma}[failure lemma]\label{lem:failure}
100: Let $S$ be a finite Frobenius ring and let
101: $C$ be a \textbf{left} ideal. Then the dual of $C$ with respect to the plain
102: product $\sum_ix_iy_i$ satisfies $|C|\cdot|C^{\perp}|=|S|^n$. For a
103: \textbf{right} ideal this fails in general. Concretely, for
104: $S=R=M_2(\F_2)$, $C=uR$ (with $t=2$, $q=2$, $n=1$, so that $u$ denotes a
105: nilpotent generator of $A_2$ embedded diagonally) one has
106: $|C|\cdot|C^{\perp}|=4\ne16=|R|$.
107: \end{lemma}
108: 
109: \begin{proof}
110: For a left ideal $C$, the map
111: $\psi_C:C\to\Hom_{\F_q}(S/C^{\perp},\F_q)$, $c\mapsto(y\mapsto\Lambda(cy))$, is
112: an $\F_q$-linear isomorphism by the non-degeneracy of $\Lambda$, and the
113: standard dimension count gives the size formula.
114: 
115: For right ideals the argument breaks: $\psi_C$ is no longer $\F_q$-balanced in
116: the way required, because the plain product is not compatible with the
117: right action. The stated counterexample is a direct computation: with
118: $R=M_2(\F_2)$ and $C=uR$ one has $|C|=4$ while the plain-product dual
119: $C^{\perp}=\{y:\tr(xy)=0\ \forall x\in C\}$ has size $1$, giving
120: $|C||C^{\perp}|=4\ne 16$.
121: \end{proof}
```

## CP04 — sections/04_cyclic_galois.tex:43–48

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

The slot-immaterial sentence calls theta an involution without the reflexivity condition and transfers slots without convention translation. The independent audit already warns about positive/negative twists.

```text
43: The slot convention --- $\theta_s$ acting on the \emph{first} argument --- is
44: immaterial for the resulting dual: placing $\theta_s$ on the second argument
45: produces the same subspace, because the two pairings differ by the
46: $\F_q$-semilinear involution $\sigma_s$ composed with transposition, which does
47: not change vanishing. We fix the convention of
48: Definition~\ref{def:pairing} throughout.
```

## CP05 — sections/04_cyclic_galois.tex:209–228

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

The printed proof asserts surjectivity to full Hom_Fq(C,R) from nondegeneracy. The audited module/functional argument must replace this unsupported reasoning; the equality result itself is conditionally retained.

```text
209: \subsection{Equality of the two orthogonals}
210: 
211: There are two natural duals of $C\le R^n$: the $R$-valued one,
212: $C^{\perp,R}=\{y:B_s(x,y)=0\ \forall x\in C\}$, and the $\F_q$-valued one
213: $C^{\perp_s}$ of Definition~\ref{def:pairing}.
214: 
215: \begin{proposition}\label{prop:twoorth}
216: $C^{\perp,R}=C^{\perp_s}$ for every $C$ and every $s$.
217: \end{proposition}
218: 
219: \begin{proof}
220: The inclusion $C^{\perp,R}\subseteq C^{\perp_s}$ is immediate since
221: $\bb_s=\Lambda\circ B_s$. For the converse, both are $\F_q$-subspaces of $R^n$;
222: $\dim_{\F_q}C^{\perp_s}=\Nlen-\dim C$ by Theorem~\ref{thm:duality}(b), and the
223: same dimension count applies to $C^{\perp,R}$: the map
224: $y\mapsto(x\mapsto B_s(x,y))$ into $\Hom_{\F_q}(C,R)$ is $\F_q$-linear with
225: kernel $C^{\perp,R}$, and it is surjective because $\Lambda$ is
226: non-degenerate and $B_s$ is non-degenerate in $y$. Hence the two subspaces have
227: the same dimension and the inclusion is an equality.
228: \end{proof}
```

## CP08 — sections/04_cyclic_galois.tex:52–60

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

The text equates cyclic with principal although its own standing definition allows all right ideals. A principality assertion needs a separate theorem and hypotheses.

```text
52: \begin{theorem}[Galois duality on right modules]\label{thm:duality}
53: Let $C\le\Rn$ be a right $\Rn$-submodule. Then:
54: \begin{enumerate}[label=\textnormal{(\alph*)},leftmargin=*]
55: \item $C^{\perp_s}$ is a right $\Rn$-submodule;
56: \item $\dim_{\F_q}C+\dim_{\F_q}C^{\perp_s}=\Nlen$, equivalently
57:   $|C|\cdot|C^{\perp_s}|=|R|^n$;
58: \item $(C^{\perp_s})^{\perp_s}=\sigma_{2s}(C)$;
59: \item if $C$ is cyclic (a principal right ideal) then so is $C^{\perp_s}$.
60: \end{enumerate}
```

## CP08 — sections/04_cyclic_galois.tex:131–145

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

Generator/annihilator sidedness must be reconciled explicitly. A right generating set cannot be passed through ann_r using the printed intuition alone.

```text
131: \begin{lemma}\label{lem:ann}
132: $\ann_r(\sum_i\Rn x_i)=\bigcap_i\ann_r(x_i)$; for a right ideal
133: $I$, $\ann_r(I)$ is determined by any generating set, whereas $\ann_l(I)$ is
134: not. Moreover $\theta_s(\ann_r(I))=\ann_l(\theta_s(I))$.
135: \end{lemma}
136: 
137: \begin{proof}
138: The first identity is the definition of an annihilator of a sum. The asymmetry
139: between left and right is a right-ideal phenomenon: a right ideal is generated
140: as a right ideal, and $\ann_r$ sees right multiplication, which is the side on
141: which the generators act. The last identity: $a\in\ann_r(I)$ iff $xa=0$ for all
142: $x\in I$; applying the anti-automorphism $\theta_s$ gives
143: $\theta_s(a)\theta_s(x)=0$ for all $x\in I$, i.e.
144: $\theta_s(a)\in\ann_l(\theta_s(I))$; conversely by applying $\theta_s^{-1}$.
145: \end{proof}
```

## CP08 — sections/04_cyclic_galois.tex:189–207

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/04_cyclic_galois.tex`

The principal reduction and universal dropping-reversal corollary need side/quantifier review, not an inference from the fact that an annihilator is a right ideal.

```text
189: apply $\Lambda$'' is the trace pairing that detects annihilation, and the index
190: reversal is precisely $\rev$. Therefore $v\in\ann_r(\theta_s(C))$ and
191: $y=\rev(v)$, which is the assertion.
192: 
193: For the principal case, $\ann_r(\theta_s(C))=\ann_r(\theta_s(g)\Rn)
194: =\ann_r(\theta_s(g))$ by Lemma~\ref{lem:ann}, and an annihilator of a single
195: element is a right ideal generated by one element in this ring, so
196: $C^{\perp_s}$ is cyclic.
197: \end{proof}
198: 
199: \begin{corollary}[the reversal is load-bearing exactly for $n\ge3$]
200: \label{cor:rev}
201: For $n\le2$ the operator $\rev$ is the identity, so
202: $C^{\perp_s}=\ann_r(\theta_s(C))$; for $n\ge3$ dropping $\rev$ changes the dual.
203: \end{corollary}
204: 
205: \begin{proof}
206: Immediate from Lemma~\ref{lem:rev} and Theorem~\ref{thm:dualformula}.
207: \end{proof}
```

## CP12 — sections/03_preliminaries.tex:177–183

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/03_preliminaries.tex`

The unused arbitrary-A-automorphism remark must not be read as a blanket extension of every Gray/metric/quantum assertion; the audit verifies the duality generalization, not all such extensions.

```text
177: 
178: \begin{remark}
179: We use only the coefficient-Frobenius subgroup of $\Aut(A_t)$: an automorphism
180: of $A_t$ may move $u$, and we never use those. Everything in this paper
181: generalises verbatim to $\tau\in\Aut(A_t)$ with $\theta_\tau=\tau\circ(\cdot)^{\mathsf T}$
182: and $\theta_\tau^2=\tau^2$; we keep $\sigma_s$ for concreteness.
183: \end{remark}
```

## CP31 — sections/05_hulls.tex:355–379

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/sections/05_hulls.tex`

The witness-B prose says a proper superobject despite defining a hull as an intersection. Include this wording and every extra witness in the scoped verification/notation pass.

```text
355: \begin{example}[the $(4,2,4)$ witness]\label{ex:witnessB}
356: Let $q=4$, $t=2$, $n=4$. Then $X^4-1=(X-1)^4$ over $\F_4$ and
357: \[
358:   \begin{gathered}
359:     \Bq\cong\F_4[u,w]/\langle u^2,w^4\rangle,\\
360:     \dim_{\F_4}\mathfrak m=7,\ \dim\mathfrak m^2=5,\
361:       \dim\mathfrak m^3=3,\ \dim\mathfrak m^4=1,\\
362:     \dim_{\F_4}\ann_{\Bq^2}(\mathfrak m)=2 .
363:   \end{gathered}
364: \]
365: The same construction \eqref{eq:witnessfamily} has $36$ members with
366: $\MU_{\Bq}(W)\ge3$, and for $s=0$ and $s=1$ the best witness satisfies
367: \[
368:   \MU_{\Bq}(W)=3,\qquad \MU_{\Bq}\bigl(\Hull_s(W)\bigr)=3,\qquad
369:   \Hull_s(W)\ne W .
370: \]
371: Here $\Nlen=4tn=32$, $k=14$, $h_E=10$, so route R3 gives
372: \[
373:   [[32,\,32-14-10,\,2\,;\,14-10]]_4=[[32,8,2;4]]_4 .
374: \]
375: Unlike Example~\ref{ex:witnessA}, the hull is a proper superobject of the
376: code one started from. It is nonetheless carried unchanged through the Gray
377: map by Theorem~\ref{thm:grayhull}, which is precisely the statement that needs
378: no principality.
379: \end{example}
```

## CP40 — main.tex:237–290

**Source:** `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/main.tex`

Data availability remains PROPOSED, the text says referred for editorial confirmation while the documentary email is unsent, and the AI declaration awaits author confirmation. These are author gates, not facts to invent.

```text
237: \section*{Data availability}
238: \label{sec:dataavailability}
239: 
240: [\emph{PROPOSED --- FFA POLICY CONFIRMATION PENDING.}] \emph{Finite Fields
241: and Their Applications} applies Elsevier research-data \textbf{Option~C},
242: under which authors are required to deposit their research data in a relevant
243: data repository and to provide a link to the dataset during the submission
244: process.
245: 
246: The computational scripts, verification logs, generator matrices, quantum-code
247: records, distance certificates, verification procedures and supporting
248: documentation used in this study are publicly available in the
249: \emph{research-data} directory of the project's GitHub repository at
250: 
251: \begin{quote}\small\raggedright
252: \texttt{https://github.com/}\penalty0
253: \texttt{arunyadav0307-stack/}\penalty0
254: \texttt{Matrix-Ring/tree/}\penalty0
255: \texttt{3752a6c0e921ab21a6f78877f154e7e959f4c418}\penalty0
256: \texttt{/research-data}
257: \end{quote}
258: 
259: which is pinned to an immutable commit and comprises $86$ files: $22$
260: computational scripts, $23$ execution logs, $29$ generator matrices, $8$ tables
261: of quantum-code records and distance certificates, and $4$ documentation and
262: verification files, each verified by a SHA-256 manifest. A description of every
263: file and instructions for reproducing the computations are given in the
264: \texttt{README.md} at that location.
265: 
266: \emph{Status: PROPOSED --- FFA POLICY CONFIRMATION PENDING.} The location is
267: public and has been verified to be accessible without authentication. Whether a
268: commit-pinned public repository satisfies Option~C is not established by the
269: official policy text, which does not name GitHub as either an acceptable or an
270: unacceptable repository; the matter has been referred for editorial
271: confirmation. The repository carries no licence, so public availability does
272: not by itself grant permission to reuse the materials.
273: 
274: \section*{Declaration of generative AI and AI-assisted technologies in the
275: manuscript preparation process}
276: \label{sec:genai}
277: 
278: [\emph{Researcher confirmation required --- mandatory where applicable.}] Elsevier
279: requires authors to declare the use of generative AI and AI-assisted
280: technologies in the manuscript preparation process, in a new section placed
281: before the reference list. AI assistance \textbf{was} used extensively in the
282: preparation of this manuscript and therefore a declaration is required; the
283: exemption for basic grammar, spelling and reference checking does not cover
284: this use. The exact wording, the tools to be named and the scope of the
285: disclosure are set out in
286: \texttt{PHASE12\_CONFIRMATION\_REGISTER.md} (category A8) and must be confirmed by
287: the author before submission.
288: 
289: 
290: \appendix
```

