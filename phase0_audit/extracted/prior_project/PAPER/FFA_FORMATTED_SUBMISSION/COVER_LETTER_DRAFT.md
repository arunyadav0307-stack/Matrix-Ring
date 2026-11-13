# Cover letter — DRAFT

> **DRAFT — NOT SENT.** Prepared for the researcher's review and approval.
> Items marked **[PENDING CONFIRMATION]** are statements only the author can
> make; they are left unconfirmed rather than asserted.

---

To the Editor,
*Finite Fields and Their Applications*

Dear Editor,

I am writing to submit the manuscript entitled

**"Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings"**

for consideration for publication as a Research Article in *Finite Fields and
Their Applications*.

## Relevance to the journal

The paper lies at the intersection the journal was founded to serve: the
arithmetic and combinatorics of finite fields, and their applications to coding
theory. It develops the duality and hull theory of cyclic codes over a
*noncommutative* finite ring — the matrix ring $R = M_2(A_t)$ over
$A_t = \mathbb F_q[u]/\langle u^t\rangle$ — and applies it to construct
$q$-ary quantum codes. All computations are over finite fields
($q\in\{4,8,9\}$), and the main structural results concern finite rings, their
anti-automorphisms, and the Hermitian forms they induce under a Gray map. I
believe this is squarely within the aims and scope of the journal.

## Principal contributions, in order of emphasis

**(1) Galois duality and hull theory over $M_2(A_t)$.** Duality is driven by the
anti-automorphism $\theta_s = \sigma_s\circ(\cdot)^T$, where $\sigma_s$ is the
coefficient Frobenius. I prove the duality and hull theory for **arbitrary right
ideals**, with no principality hypothesis. I also **refute** the conjecture that
Galois hulls over this ring are necessarily principal: hulls with minimal
generator number $\mu_B = 3$ exist, and $\mu_B \ge 3$ forces $t\ge 2$ and
$p \mid n$.

**(2) Non-principal hull structure and verified counterexamples.** Explicit
witness families are enumerated, and the obstruction is proved: $\mu_B\ge 3$
cannot occur for $t=1$, nor when $p \nmid n$.

**(3) A duality-preserving Gray-map representation.** The coefficient-expansion
map to $\mathbb F_q^{4tn}$ transports the Galois pairing to an explicit
$b_{\sigma_s}$-Hermitian form with Hankel Gram matrix $I_{4n}\otimes H_t$ —
**not** the Euclidean form unless $t=1$ — and preserves duality and hulls,
including the non-principal ones. Every Galois hull is self-orthogonal for the
transported form, with no reflexivity hypothesis.

**(4) Quantum-code constructions from Galois hulls.** Three routes of length
$N = 4tn$ follow: a twisted stabilizer route, a Euclidean/CSS route, and an
entanglement-assisted route $[[N,\, N-k-h_E,\, d;\, k-h_E]]_q$. A
characteristic-two obstruction delimits the Euclidean route. I show that the
distance is the minimum weight of the quotient code
$D^{\perp_E}/\mathrm{Hull}_E(D)$, and derive a coset Singleton bound
$K + d \le N+1$ that is neither the entanglement-assisted Singleton bound nor
implied by it.

**(5) Exact-distance certification and parameter analysis.** Exhaustive
computation over the accessible family list certifies 28 codes. The distance of
each code is determined **exactly** by one of two methods — complete enumeration
(M1) where it finishes, or an increasing-weight support search (M2) run
precisely when M1 cannot finish — and every code is cross-checked by an
independent ambient quantum search (M3). That cross-check is itself **exact for
11 of the 28 codes** and yields a **proved lower bound for the remaining 17**.
Two methods run per code; no code is certified by all three, and the paper says
so explicitly.

## On the significance of the noncommutative framework

Over a commutative ring, the hull theory of cyclic codes is governed by
principal-generation arguments that quietly fail here. I use the right-module
convention throughout, because it is the one under which the Galois pairing
behaves and under which the counterexample is visible. The Morita identification
$R_n \cong M_2(B)$ is used **only** as a computational device: it converts hull
structure theory into a computation with submodules of $B^2$. It does **not**
carry the duality — Morita equivalence is an equivalence of module categories,
not of rings with involution — and the paper is explicit that the duality and
hull statements are proved for $R$ and $\theta_s$ *before* any Morita
translation. The noncommutativity is therefore not cosmetic: it is what makes
the $\mu_B = 3$ hulls possible.

## On the comparison with known codes — stated honestly

**I do not claim that the codes constructed here improve on established
records.** The codes are new in *origin*, not in parameters. Every stabilizer
code constructed whose parameters can be compared against the published tables
is **at best equal** to the best known distance, and the manuscript states this
plainly. The contribution is the algebraic framework and the rigorously verified
constructions it produces — not new record parameters.

## Reproducibility

The paper is accompanied by a complete supplementary package: 22 computational
scripts, 23 execution logs, 29 generator matrices and 8 parameter tables (86
files total), certified by a SHA-256 manifest. The certification of every
distance is reproducible from the shipped generator matrices independently of
the code base, and the per-code record of which methods ran is tabulated in
full. I am happy for this material to be examined alongside the manuscript.

## Statements requiring author confirmation

The following are standard submission declarations which **I have not completed
on the author's behalf** and which require confirmation before submission:

* **[PENDING CONFIRMATION]** that the work is original and has not been
  published previously.
* **[PENDING CONFIRMATION]** that the manuscript is not under consideration by
  any other journal.
* **[PENDING CONFIRMATION]** that its publication is approved by all authors and,
  where applicable, by the responsible authorities at the institution where the
  work was carried out.
* **[PENDING CONFIRMATION]** that, if accepted, it will not be published
  elsewhere in the same form, in English or in any other language, without the
  written consent of the copyright holder.
* **[PENDING CONFIRMATION]** the declaration of generative AI and AI-assisted
  technologies in the manuscript preparation process — **required**, and
  currently unresolved.
* **[PENDING CONFIRMATION]** the research-data statement. FFA requires
  **Option C**: deposit in a relevant data repository and a link provided during
  submission, or a statement explaining why sharing is not possible. This is
  currently unresolved.

I hope the manuscript will be of interest to the readers of *Finite Fields and
Their Applications*, and I look forward to your decision.

Yours sincerely,

**Arun Kumar Yadav**
School of Basic and Applied Sciences
K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India
Corresponding author — arunyadav0307@gmail.com

---

### Notes on what this letter deliberately does **not** say

* It does **not** claim that every code is a new record.
* It does **not** claim that all parameters outperform the best known.
* It does **not** claim that three certification methods were completed for
  every code — it states the accurate 11/17 split.
* It does **not** claim that the work has been accepted or previously endorsed
  by the journal.
* It does **not** confirm originality, exclusive submission or absence of
  simultaneous submission; those are marked pending.
* It does **not** resolve the generative-AI declaration or the research-data
  statement.
