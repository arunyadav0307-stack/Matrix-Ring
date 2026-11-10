# Cover letter — FINAL DRAFT (Phase 23)

> # ⚠️ DRAFT — NOT SENT
> Prepared for the researcher's review. **Every item marked
> `[RESEARCHER CONFIRMATION REQUIRED]` is an author attestation and remains
> unconfirmed.** Nothing here has been sent, uploaded, or entered into any
> submission system, and no journal account has been created.

**Supersedes:** `PAPER/FFA_FORMATTED_SUBMISSION/COVER_LETTER_DRAFT.md`
(Phase 19). That file is **retained unchanged**; the present document is a new
draft, not an overwrite.

**What changed in this revision:** the reproducibility paragraph now gives the
commit-pinned public location of the data (the Phase 19 letter predated the
publication and pointed at nothing); the research-data statement now reports the
deposit and the outstanding editorial question rather than an unresolved
blank; and the list of pending author attestations is complete.

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
$A_t = \mathbb F_q[u]/\langle u^t\rangle$ — and applies it to construct $q$-ary
quantum codes. All computations are over finite fields ($q\in\{4,8,9\}$), and
the main structural results concern finite rings, their anti-automorphisms, and
the Hermitian forms they induce under a Gray map. I believe this is squarely
within the aims and scope of the journal.

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

I should also be straight about the limits of that comparison. The comparison is
against the tables of Grassl (codetables.de), which cover **stabilizer codes
over $q = 4$ and $q = 9$ only**: $q = 8$ is not tabulated, and the
entanglement-assisted tables cover $q = 2$ and $q = 3$, so **no
entanglement-assisted code of this paper is benchmarked at all** — which is a
real blind spot, since that is where the largest distances occur. The manuscript
says so in the comparison section, and I would rather say it here than have a
referee find it.

## Reproducibility and research data

The paper is accompanied by a complete public data deposit: 22 computational
scripts, 23 execution logs, 29 generator matrices, 8 tables of quantum-code
records and distance certificates, and 4 documentation and verification files —
86 files in total, each verified by a SHA-256 manifest. The materials are
available at the commit-pinned location

```
https://github.com/arunyadav0307-stack/Matrix-Ring/tree/3752a6c0e921ab21a6f78877f154e7e959f4c418/research-data
```

which is accessible without authentication. The pinning is deliberate: the URL
resolves to an immutable commit, so a reader who follows it obtains exactly the
materials described here. The certification of every distance is reproducible
from the shipped generator matrices independently of the code base, and the
per-code record of which methods ran is tabulated in full. I am happy for this
material to be examined alongside the manuscript.

**One point of transparency.** I have not yet obtained a DOI for the deposit,
and the repository currently carries no licence, so the materials are viewable
but no formal reuse permission has been granted. If the journal requires a
citable, licensed deposit, I will make one.

## Statements requiring author confirmation

The following are standard submission declarations which **require confirmation
before submission**:

* **`[RESEARCHER CONFIRMATION REQUIRED]`** that the work is original, is the
  author's own, and has not been published previously in any form.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** that the manuscript is not under
  consideration by any other journal, conference or publisher, and that it will
  not be submitted elsewhere while under consideration here.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** that its publication is approved by
  all authors, that no one who qualifies for authorship has been omitted and no
  one who does not qualify has been included, and, where applicable, that it is
  approved by the responsible authorities at the institution where the work was
  carried out.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** that, if accepted, it will not be
  published elsewhere in the same form, in English or in any other language,
  without the written consent of the copyright holder.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** the declaration of generative AI and
  AI-assisted technologies in the manuscript preparation process. **This is
  required and remains unresolved** — see below.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** that the results are presented
  accurately and are reproducible from the deposited scripts and logs.
* **`[RESEARCHER CONFIRMATION REQUIRED]`** that there are no competing financial
  interests or personal relationships that could have appeared to influence the
  work, and that no specific grant was received.

### Two items I wish to flag rather than bury

**The generative-AI declaration is not settled.** The project's records show AI
assistance extending beyond language polishing to manuscript drafting, proof
exposition, computational script generation, abstract revision and literature
discovery. Under Elsevier's policy, the exemption for basic grammar, spelling and
reference checking does not extend to those activities. The wording, and the
tools to be named, are for me to confirm and I will do so before submission.

**The research-data arrangement is not yet confirmed as compliant.** FFA applies
Elsevier **Option C**, which requires deposit in a relevant data repository and a
link provided during submission. I have made a public, commit-pinned,
SHA-256-verified deposit and quote the link above; I have **not** obtained a DOI
and have **not** applied a licence. I am writing separately to the editorial
office to confirm that this satisfies Option C, or whether a release, tag or
DOI-bearing deposit is required. I am not seeking an exemption from the policy —
if a repository deposit with a DOI is what Option C requires, I will make one.

## One correction I intend to make

The comparison section currently states that no entanglement-assisted table
exists. That is inaccurate: entanglement-assisted bounds **are** tabulated at
eaqecc.codetables.de, for qubits and qutrits. Since this paper's
entanglement-assisted codes are over $q = 4$, $8$ and $9$, none is covered and
the conclusion stands — but the stated reason is wrong and I will correct the
wording. I mention it here so that the correction is not mistaken for a
retraction.

I hope the manuscript will be of interest to the readers of *Finite Fields and
Their Applications*, and I look forward to your decision.

Yours sincerely,

**Arun Kumar Yadav**
School of Basic and Applied Sciences
K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India
Corresponding author — arunyadav0307@gmail.com

---

## Notes on what this letter deliberately does **not** say

* It does **not** claim that every code is a new record.
* It does **not** claim that all parameters outperform the best known.
* It does **not** claim that three certification methods were completed for
  every code — it states the accurate 11/17 split.
* It does **not** claim that all three methods ever run together on one code.
* It does **not** claim that the data deposit is licensed, or that it carries a
  DOI.
* It does **not** claim the deposit satisfies Option C — it asks.
* It does **not** claim that the work has been accepted or previously endorsed
  by the journal.
* It does **not** confirm originality, exclusive submission, authorship,
  accuracy, ethics or competing interests; all seven are marked pending.
* It does **not** resolve the generative-AI declaration.

## Status of this document

| | |
|---|---|
| Sent | ❌ **No** |
| Uploaded to any submission system | ❌ **No** |
| Journal account created | ❌ **No** |
| Author attestations completed | ❌ **No — 7 of 7 pending** |
| Data-availability wording approved by the researcher | ❌ **No** |
| Generative-AI declaration resolved | ❌ **No** |
| Editorial confirmation of Option C obtained | ❌ **No** |
