# Task E — Pre-submission policy clarification email

> # ⚠️ DRAFT — NOT SENT
>
> Nothing has been sent to Elsevier, no Editorial Manager account has been
> created, and no submission has been made. This draft exists because the
> official policy text does not resolve the question (see
> `PHASE21_FFA_OPTION_C_POLICY_VERIFICATION.md`, §3 Q3 and Q6). It is prepared
> for the researcher to review, edit and send themselves.
>
> **No exception has been granted.** Nothing below may be read as the journal
> having accepted anything.

---

**To:** the Editorial Office, *Finite Fields and Their Applications*
**Subject:** Research data policy (Option C) — clarification before submission

Dear Editorial Office,

I am preparing a submission to *Finite Fields and Their Applications* and would
be grateful for a short clarification on the journal's research-data policy
before I submit.

**Manuscript title:**
"Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings"

**The question.** The journal's Guide for Authors states that Option C applies
and that authors are **required** to deposit their research data in a relevant
data repository and provide a link to the dataset during the submission
process, or, if sharing the research data isn't possible, to make a statement
explaining why. I have read the Elsevier research-data guidelines and the
research-data FAQs, and I could not find any statement about whether access
provided **privately by the author upon reasonable request** is acceptable in
place of a repository deposit. I would be grateful to know whether it is.

**What the underlying material is.** The results of the paper are partly
computational. The supporting material consists of four kinds of item, and
nothing else:

1. **Mathematical computation scripts** — 22 short Python scripts. These
   implement, from first principles and in exact arithmetic, the rings
   $\mathbb F_q$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$, $R=M_2(A_t)$ and
   $R_n=R[X]/\langle X^n-1\rangle$, and run the searches and checks reported in
   the paper. They use only the Python standard library — no third-party
   package is involved.
2. **Computation logs** — 23 text files, the verbatim outputs of those scripts,
   including the log from which every number in the paper's tables is read
   (each table row carries the log line it was parsed from).
3. **Generator matrices** — 29 files: the generator matrix of each of the 28
   certified codes, plus an index.
4. **Verification certificates and parameter tables** — 8 machine-readable CSV
   tables (certified parameters, comparison data, family census and scan
   results) together with a one-page certification procedure describing exactly
   what "certified" means in the paper and how a code can be re-certified from
   scratch.

In total this is 86 files of roughly 2.4 MB, covered by a SHA-256 manifest so
that any transfer can be verified byte-for-byte. None of it contains
confidential, proprietary or third-party-restricted content.

**My position.** For personal reasons I would prefer not to place this material
in a public data repository at this time. I am, however, entirely willing to
provide any part of it, privately and directly, to any reader, reviewer or
editor who asks, and to do so promptly.

**The exact statement I would propose to include in the article** (and to enter
in the data-statement field during submission) is:

> The computational scripts, execution logs, generator matrices, parameter
> tables and certification documentation supporting this study are not publicly
> available. The corresponding author will make the relevant materials
> available on reasonable request.

**Specifically, I would be grateful to know:**

1. Would the above arrangement — private provision by the corresponding author
   upon reasonable request, with no repository deposit and no DOI — be
   acceptable for this manuscript under Option C?
2. If not, must I make a deposit before the manuscript can be sent to review,
   or may the deposit be arranged at the revision or acceptance stage if the
   paper is favourably received?
3. If a statement is required instead, would the wording quoted above be
   acceptable? I ask because the Option C wording requires the statement to
   explain **why** sharing isn't possible, and in my case the material could be
   shared — I have simply not arranged a public deposit. I do not wish to
   state a reason that is not the true one.
4. Separately: is there a mechanism in the submission system for supplying the
   computational material to the editor and reviewers **for review purposes
   only**, without it being published as supplementary material? My
   understanding from the Guide for Authors is that supplementary material
   "will appear online exactly as received", so that route would publish the
   files, which is what I am trying to avoid.

I am happy to deposit the material if the journal requires it; I simply want to
know the position before I submit, so that I can comply properly rather than
guess.

Thank you for your time and help.

Yours sincerely,

**Arun Kumar Yadav**
School of Basic and Applied Sciences
K.R. Mangalam University, Sohna Road, Gurugram, Haryana, 122103, India
arunyadav0307@gmail.com

---

## Notes for the researcher before sending

| # | note |
|---|---|
| 1 | **"For personal reasons"** is deliberately vague so that it stays truthful. If you would rather state nothing at all, delete that sentence — the rest of the email stands on its own. |
| 2 | The email **does not** ask for an exception it has already assumed. Question 1 asks plainly whether the arrangement is acceptable. |
| 3 | Question 3 is the honest one, and it is the awkward one. It says directly that the material could be shared and that no false reason will be given. That is the accurate position; do not soften it into a claim of impossibility. |
| 4 | Question 4 is genuinely open — no official source confirmed whether a reviewer-only channel exists. It is asked rather than assumed. |
| 5 | Until a written reply is received, the arrangement is **EDITORIAL CONFIRMATION REQUIRED**, not accepted. |
| 6 | Do not submit the manuscript while this is unresolved. On the strict reading of Option C this is a **SUBMISSION BLOCKER**. |
