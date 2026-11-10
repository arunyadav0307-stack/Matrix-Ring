# Phase 9 — Journal comparison

**Date:** 2026-11-10
**Every fact below traces to `PHASE9_EVIDENCE_REGISTER.md`**, which records the
source URL and access date. Anything not confirmed on an official page is
marked **UNVERIFIED** and is scored as such, never filled in.

---

## 1. What this document is

A comparison of ten candidate venues for the manuscript profiled in
`PHASE9_MANUSCRIPT_PROFILE.md`. It contains:

* §2 — how the candidate set was chosen;
* §3 — the scoring framework, stated before the scores, with its limits;
* §4 — one profile per journal;
* §5 — the comparison table and the ranked result.

It does **not** estimate acceptance probabilities, and it does **not** claim
any venue will accept the paper.

## 2. How the candidate set was selected

The task asks for 8–12 candidates, prioritising (a) algebraic coding theory,
(b) finite fields and rings, (c) coding + cryptography applications, and
(d) QI/QEC only where the scope genuinely fits. Ten venues were chosen to
cover all four, including two deliberately marginal fits so the comparison is
not a foregone conclusion.

| # | journal | why it is on the list | priority group |
|---|---|---|---|
| 1 | Finite Fields and their Applications | (a)+(b) — scope names algebraic coding theory; the manuscript cites two FFA papers | core |
| 2 | Designs, Codes and Cryptography | (a) — the field's own specialist venue | core |
| 3 | IEEE Transactions on Information Theory | (a) — highest-prestige venue the paper already cites (twice); included mainly as a length/stress test | stretch |
| 4 | Cryptography and Communications | (c) — scope "strongly encourages" finite fields/algebraic structures; the manuscript cites a paper from it | core |
| 5 | Advances in Mathematics of Communications | (a)+(c) — coding theory + algebra/number theory, with the densest 2025–26 hull cluster found | core |
| 6 | Quantum Information Processing | (d) — QEC is in scope; included to test whether the quantum framing carries the paper | marginal |
| 7 | Journal of Algebra and its Applications | (b) — applied algebra with an application-field link; the manuscript cites a JAA paper | core |
| 8 | Applicable Algebra in Engineering, Communication and Computing | (a)+(c) — algebra for communications and coding | core |
| 9 | Discrete Mathematics | (a) — scope names coding theory and matrices; published the single closest recent neighbour | core |
| 10 | Entropy | (d) — fully OA information-theory venue; included as an OA-model contrast | marginal |

**Deliberate exclusions.** General mega-journals and preprint-only servers were
not considered. Physics-first QEC venues were not considered beyond QIP,
because the manuscript contains no decoder, noise model or threshold and would
be a scope mismatch. No venue was excluded because of its quartile.

## 3. Scoring framework

Stated before any score is assigned, so that the ranking can be audited and
re-weighted by the author.

| criterion | weight | what a 5 means | what a 1 means |
|---|---|---|---|
| **A. Scope match** | 30 % | the manuscript's subject is named in the journal's stated aims and scope | the subject is outside the stated scope |
| **B. Mathematical fit** | 25 % | the venue publishes structural ring/module-theoretic work at this depth and length, and tolerates negative results | the venue wants applications, performance gains or physical results, not structure |
| **C. Recent related work** | 20 % | verified 2025–26 papers in the journal on the same or adjacent topic | no verified related papers found |
| **D. Practical fit** | 15 % | no page cap, no mandatory author charge, fast and predictable process, low formatting friction | hard page cap or mandatory APC or very slow process |
| **E. Indexing / visibility** | 10 % | Q1 with broad abstracting coverage | Q3 / narrow coverage |

**Why criterion E is weighted at only 10 %.** The task states that journal
selection must not be based on quartile alone. Weighting indexing at 10 % and
scope at 30 % makes that instruction structural rather than rhetorical: the
highest-SJR venue in the set (IEEE TIT, SJR 1.323) does **not** win, and the
two highest-scoring venues differ in quartile band from each other.

**Scores are 1–5 integers.** Weighted score = `0.30A + 0.25B + 0.20C + 0.15D +
0.10E`.

**Stated limitations of the framework — read these before using the ranking:**

1. **The weights are a judgement, not a measurement.** They encode a
   deliberate preference for topical fit over prestige. Re-weighting to, say,
   40 % on E would change the ordering. The per-criterion scores are reported
   precisely so the author can re-weight.
2. **Score differences below ~0.15 are not meaningful.** The underlying scores
   are integers on a 5-point scale; a 0.05 gap is noise. Where two venues are
   within that band, this document says so instead of pretending to rank them.
3. **Criterion C is limited by what search could verify.** "No verified related
   papers" (score 1–2) is weaker evidence than "verified related papers"
   (score 4–5), because absence of evidence is not evidence of absence. This
   systematically penalises venues whose recent issues were not sampled.
4. **UNVERIFIED fields are not scored.** Where a page limit or APC could not
   be confirmed, criterion D is scored on what *is* known, and the uncertainty
   is reported in §5 rather than silently filled in.
5. **Nothing here predicts editorial outcome.** The framework measures fit,
   not acceptance. No acceptance probability is estimated anywhere in Phase 9.
6. **Quartiles are a 2025 snapshot.** SJR quartiles move; AAECC's quartile, for
   example, has oscillated between Q2 and Q4 across years. A 2025 Q1 is not a
   forecast.

---

## 4. Journal profiles

Scores are given as **A / B / C / D / E** followed by the weighted total.

### 4.1 Finite Fields and their Applications — **5 / 5 / 5 / 4 / 5 = 4.85**

*Elsevier / Academic Press. ISSN 1071-5797 (print), 1090-2465 (online).
Hybrid. SJR 2025 0.906, **Q1** in Algebra and Number Theory, Applied
Mathematics and Theoretical Computer Science. h-index 60. Scopus 1995–2026.*

**Scope.** The journal's own scope text names **algebraic coding theory**,
cryptology and combinatorial design theory. Finite fields, finite rings and
their module categories are the journal's home territory, which is exactly the
manuscript's engine (`R = M₂(A_t)`, `A_t = F_q[u]/⟨u^t⟩`).

**Fit.** The manuscript already cites two FFA papers (Fan–Zhang 2017 Galois
self-dual constacyclic codes; Liu–Pan 2020 Galois hulls of constacyclic
codes), so the paper's lineage runs through this venue. FFA advertises "very
strict refereeing standards" — a risk (see §6.1 of the recommendation) but also
the reason a structural negative result is a credible submission here rather
than an oddity.

**Recent related work.** *Finite Fields Appl.* Vols 109 (Jan 2026), 110
(Feb 2026) and 111 (Mar 2026) all carry constacyclic/cyclic-code papers,
including Graner's closed-form generators and a cyclotomic-coset construction.

**Practical.** No page limit stated on the pages retrieved (**UNVERIFIED**).
Gold OA APC **USD 3 240** (excl. taxes); the subscription route is free.
Preprints are permitted. Submission via Editorial Manager (`ffa`).

**Restrictions found.** None stated.

### 4.2 Designs, Codes and Cryptography — **5 / 5 / 4 / 5 / 4 = 4.70**

*Springer Netherlands. ISSN 0925-1022 / 1573-7586. Hybrid. SJR 2025 0.712,
**Q1** in Discrete Mathematics and Combinatorics; Q2 in Applied Mathematics,
Computer Science Applications, Theoretical Computer Science. h-index 75.
Scopus 1991–2026.*

**Scope.** The field's specialist venue. Scope emphasises algebraic and
geometric aspects, **finite fields and finite geometries** — both directly
relevant.

**Fit.** Any paper on hulls of cyclic codes over rings is *prima facie* on
topic here. The 43 theorem environments and the refutation are normal article
shapes for this journal.

**Recent related work.** Coding theory of this kind is the journal's core
output, but **no specific recent hull-over-rings paper was verified in the
pages sampled**; C is scored 4 rather than 5 to reflect that gap honestly.

**Practical.** **No submission or publication fee** (an explicit statement on
the submission-guidelines page). Open Choice is offered after acceptance at
**USD 3 290 / £2 390 / €2 690** if OA is wanted; the subscription route is
free. **Single-blind peer review.** Time to first decision usually under three
months; online publication 3–5 weeks after acceptance. No page limit stated
(**UNVERIFIED**). No Word template — the publisher typesets.

**Restrictions found.** None stated.

### 4.3 Discrete Mathematics — **4 / 4 / 5 / 3 / 5 = 4.15**

*Elsevier. ISSN 0012-365X. Hybrid. SJR 2025 0.782, **Q1** in Discrete
Mathematics and Combinatorics (Q1 continuously 2016–2025) and **Q1** in
Theoretical Computer Science (2025). h-index 94. Scopus 1971–2026.*

**Scope.** Coding theory, block designs, algebraic combinatorics and matrices
are all named in scope, and the manuscript cites a Discrete Mathematics paper
(Cao 2021, MDS Galois hulls).

**Fit — with a caveat.** This is the strongest recent-work match in the set
but the *venue* is combinatorics-first. The manuscript's ring-theoretic
apparatus and its quantum payoff are both somewhat off the journal's centre of
gravity; A is scored 4, not 5, for that reason.

**Recent related work.** Debnath, Islam, Martínez-Moro and Prakash, *Galois
hulls of constacyclic codes over affine algebra rings*, **Discrete Math. 349
(2026)**, 18 pp., doi 10.1016/j.disc.2025.114750 — the closest published
neighbour to this manuscript found in the entire search.

**Practical.** Gold OA APC **USD 3 530** (excl. taxes) — the highest in the
candidate set; subscription route free. No page limit stated (**UNVERIFIED**).
Submission via Editorial Manager (`DISCM`).

**Restrictions found.** None stated.

### 4.4 Advances in Mathematics of Communications — **5 / 4 / 5 / 2 / 3 = 4.10**

*AIMS. ISSN 1930-5338 / 1930-5346. Hybrid (supports OA). SJR 2025 0.576,
**Q2** in Applied Mathematics, Algebra and Number Theory, Discrete Mathematics
and Combinatorics, and Computer Networks and Communications. h-index 31.
Scopus 2007–2026.*

**Scope.** Coding theory, cryptology, combinatorics, finite geometry, and
algebra and number theory — with **communications relevance**. Coding theory
is core here, not peripheral: A is scored 5.

**Fit — with a caveat.** The journal states it demands high originality, new
techniques and depth, and that "any work that does not conform will be
rejected". The manuscript's structural contribution should meet that bar, but
this is an explicit editorial warning and it is a real gate.

**Recent related work.** The densest cluster found anywhere:
* *Study of small Galois hull dimensions of constacyclic codes*, AMC 22 (2026)
  1–18, doi 10.3934/amc.2025054;
* Debnath & Prakash, *Average dimensions of Galois hulls of constacyclic
  codes*, AMC (Jan 2025);
* Hermitian hulls and EAQECCs, AMC 19(2) (Apr 2025) 588–603,
  doi 10.3934/amc.2024013.
The third of these follows exactly the manuscript's §7 route (hulls → EA
quantum codes).

**Practical — the weak point.** Official journal page: **median time to first
decision 112 days; median review time 138 days.** That is the slowest verified
process in the set, and D is scored 2 for it. No page limit stated
(**UNVERIFIED**). OA APC **UNVERIFIED** (a secondary source suggests
USD 1 800 for AIMS hybrid Open Choice; not confirmed on an official AIMS page
— do not rely on it).

**Restrictions found.** None stated beyond the originality warning.

### 4.5 Journal of Algebra and its Applications — **4 / 5 / 3 / 4 / 3 = 3.95**

*World Scientific. ISSN 0219-4988 / 1793-6829. Hybrid (supports OA). SJR 2025
0.492, **Q2** in Algebra and Number Theory and in Applied Mathematics.
h-index 37.*

**Scope.** Theoretical and applied algebra, with "special interest in papers
that point out innovative links between areas of Algebra and fields of
application" — which describes this manuscript well. The journal runs special
issues on algebraic geometry, coding theory and cryptography.

**Fit.** The strongest pure-algebra home in the set. The manuscript cites a
JAA paper (Dinh 2024, cyclic codes over rings of matrices), so the immediate
predecessor work appeared here. The journal publishes module- and
ring-theoretic work at this depth without requiring a performance gain, so the
"no record parameters" limitation is much less damaging here than elsewhere.

**A concrete formatting advantage.** The submission guidelines require
references to be **numbered consecutively in arabic numerals in alphabetical
order of the first author** — which is precisely what `\bibliographystyle{plain}`
produces. Under decision D-1 the manuscript already satisfies this.

**Recent related work.** Coding-theory special issues exist (Vol 24 No 13n14;
a Rosenthal Festschrift), but **no regular-issue hull paper was verified**; C
is scored 3.

**Practical.** **"There will be no page charge for the journal."** LaTeX style
files are supplied by the publisher. Submission via Editorial Manager (`jaa`),
where the author selects the editorial-board member closest to the subject.
The only stated formatting constraint is **abstract ≤ 200 words**, which the
current abstract exceeds.

**Restrictions found.** Abstract ≤ 200 words; introduction should be
understandable to a broad scientific audience, not only specialists.

### 4.6 Cryptography and Communications — **3 / 4 / 3 / 3 / 4 = 3.35**

*Springer. ISSN 1936-2447 / 1936-2455. Hybrid. SJR 2025 0.853, **Q1** in
Applied Mathematics, Computational Theory and Mathematics, and Computer
Networks and Communications. h-index 28. Scopus 2009–2026.*

**Scope.** Discrete structures in stream and block ciphers, CDMA, RNG, Boolean
functions and sequences — with the scope text adding that **finite fields and
other algebraic structures are "strongly encouraged"**. The manuscript cites a
paper from this journal (Luo–Parampalli 2018, M₂(F₂+uF₂)).

**Fit — the honest objection.** Despite the manuscript's MSC 94B60 entry,
**the paper contains no cryptographic result**: no cipher, no protocol, no
attack, no security reduction. A is scored 3 to reflect that the "strongly
encouraged" algebraic-structures clause supports an algebraic coding paper
only weakly, and that a referee could raise scope.

**Recent related work.** No recent hull-over-rings paper was verified; C = 3.

**Practical.** OA APC **USD 3 290 / £2 390 / €2 690**; subscription route free.
No page limit stated (**UNVERIFIED**). Peer-review model **UNVERIFIED**.

**Restrictions found.** None stated.

### 4.7 IEEE Transactions on Information Theory — **3 / 5 / 2 / 1 / 5 = 3.20**

*IEEE. ISSN 0018-9448 / 1557-9654. Hybrid. SJR 2025 **1.323 — the highest in
the set**; Q1 in every listed category, continuously 1999–2025. h-index 310.*

**Scope.** Information theory. The manuscript cites two TIT papers
(Greferath–Schmidt 1999 Gray isometry; Ketkar et al. 2006 nonbinary
stabilizer), so the ingredients have appeared here — but TIT's centre is not
ring-theoretic algebra, and A is scored 3.

**Fit.** B is scored 5: TIT tolerates depth and rigour better than any other
venue in the set, and would not object to a negative result.

**Practical — the decisive problem.** The manuscript is ≈ 13 300 words with 43
theorem environments. TIT enforces a **50-page single-column submission limit
(since 2025-05-01)** and a **25-page final two-column limit**. The paper as it
stands does not fit the final limit, and cutting it to fit would remove §8 and
Appendix B — the triple-certification material that is one of its real
strengths. Additionally: abstract must be **≤ 250 words in one paragraph with
no displayed mathematics** (the current abstract is longer and contains
displayed mathematics in the source); **ORCID is required for all authors**
and the manuscript has no author metadata at all. D is scored 1.

**APC.** **Conflicting official figures**: IEEE Xplore lists USD 2 800; the IT
Society author-information page states a "discounted USD 1 750". Unresolved.

**Restrictions found.** 50-page submission cap; 25-page final cap; abstract ≤
250 words, one paragraph, no displayed math; 5–10 index terms; single-column
submission; single-anonymous review; ORCID required for all authors.

### 4.8 Applicable Algebra in Engineering, Communication and Computing — **4 / 3 / 2 / 3 / 2 = 3.00**

*Springer. ISSN 0938-1279 / 1432-0622. Hybrid. SJR 2025 0.389, **Q3** in
Algebra and Number Theory and in Applied Mathematics (its quartile has
oscillated Q2–Q4 across years). h-index 40. Scopus 1990–2026.*

**Scope.** Algebraic methods in computers, intelligent systems and
communications — **coding, cryptography and networks** are named explicitly.

**Fit — with a stated risk.** The scope text says "purely theoretical papers
will not primarily be sought" and that engineering and technology-transfer
papers are in scope. This manuscript is theoretical with an application
section, which sits right on that boundary. B is scored 3.

**Recent related work.** None verified; C = 2.

**Practical.** **Single-blind.** Springer LaTeX macro package, option
`smallextended`. OA APC **USD 3 190 / £2 290 / €2 590**; subscription route
free. Author Contribution and Competing Interest statements must be entered
through the submission interface, and a Data Availability Statement is required
for original research — **neither exists in the manuscript today**, though
both are easy to add at submission time (Phase 9 does not add them).

**Restrictions found.** Contribution statement, Competing Interest statement,
Data Availability Statement.

### 4.9 Quantum Information Processing — **2 / 2 / 2 / 3 / 3 = 2.25**

*Springer. ISSN 1570-0755 / 1573-1332. Hybrid. SJR 2025 0.441, **Q2** in
Electrical and Electronic Engineering, Theoretical Computer Science, Signal
Processing and Modeling and Simulation; Q3 in Materials Science. h-index 85.
Scopus 2004–2026.*

**Scope.** Quantum error correction and fault tolerance are in scope, as are
quantum cryptography and entanglement.

**Fit — the honest verdict.** This venue was included to test whether the
manuscript's quantum framing carries it, and it does not. QIP is
physics- and electrical-engineering-weighted, not algebra-weighted. A referee
from that community would see 43 theorem environments of ring theory as
unmotivated machinery, and would judge the payoff — first stabilizer distance
`d = 4`, `[[24,8,4]]_9` — as thin. A and B are both scored 2.

**Practical.** OA APC **USD 3 090 / £2 190 / €2 490**; subscription free. No
page limit stated (**UNVERIFIED**).

**Restrictions found.** None stated.

### 4.10 Entropy — **2 / 2 / 1 / 3 / 3 = 2.05**

*MDPI. ISSN 1099-4300. **Fully open access** (no subscription route). SJR 2025
0.475, **Q2** in Information Systems, Electrical and Electronic Engineering,
Mathematical Physics, and Physics and Astronomy (misc.). h-index 123.*

**Scope.** Entropy and information-theoretic concepts, including Shannon
entropy, **coding and compression**, information transfer and quantum
mechanics.

**Fit.** Included as an OA-model contrast, and it is a poor home. Coding and
compression in this venue means source coding and information measures, not
ring-theoretic code construction. A and B are both scored 2; C is 1 (no
related work verified).

**Practical.** **APC CHF 2 600 is mandatory** — there is no free route, which
is the single distinguishing practical fact about this venue. Publisher
statistics claim 21 days submission-to-first-decision and 4 days
acceptance-to-publication (publisher-asserted).

**Restrictions found.** None stated.

---

## 5. Comparison table

Sorted by weighted score. All time-sensitive values were accessed 2026-11-10;
sources in `PHASE9_EVIDENCE_REGISTER.md`.

| Journal | Scope Match | Mathematical Fit | Recent Related Work | Indexing | Quartile (Year) | Publication Model | APC | Submission Requirements | Evidence Links |
|---|---|---|---|---|---|---|---|---|---|
| **Finite Fields Appl.** | 5 — scope names algebraic coding theory; we cite 2 FFA papers | 5 — structural, strict refereeing, tolerates negative results | 5 — constacyclic/cyclic papers in Vols 109 (Jan 26), 110 (Feb 26), 111 (Mar 26) | Scopus; SJR 0.906; h-60 | **Q1 (2025)** Algebra & Number Theory; Q1 Applied Math; Q1 TCS | Hybrid (Elsevier) | **USD 3 240** gold OA, all article types; **subscription free** | EM portal `ffa`; preprints allowed; no page limit stated (**UNVERIFIED**); peer-review model **UNVERIFIED** | [home](https://www.sciencedirect.com/journal/finite-fields-and-their-applications) · [OA/APC](https://www.sciencedirect.com/journal/finite-fields-and-their-applications/publish/open-access-options) · [SCImago 26480](https://www.scimagojr.com/journalsearch.php?q=26480) |
| **Designs, Codes Cryptogr.** | 5 — field's specialist venue; finite fields & geometries | 5 — 43 theorems + refutation is a normal shape here | 4 — core output, but no specific recent hull paper verified | SCIE, Scopus, zbMATH, MathSciNet, DBLP, EI, INSPEC, Dimensions; SJR 0.712; h-75 | **Q1 (2025)** Discrete Math & Combinatorics; Q2 Applied Math; Q2 CS Applications; Q2 TCS | Hybrid (Springer) | **No submission or publication fee**; Open Choice **USD 3 290** after acceptance (optional) | **Single-blind**; first decision usually <3 months; online 3–5 weeks post-acceptance; no page limit stated (**UNVERIFIED**) | [home](https://link.springer.com/journal/10623) · [guidelines](https://link.springer.com/journal/10623/submission-guidelines) · [APC](https://link.springer.com/journal/10623/how-to-publish-with-us) · [SCImago 25862](https://www.scimagojr.com/journalsearch.php?q=25862) |
| **Discrete Mathematics** | 4 — coding theory & matrices in scope, but combinatorics-first venue | 4 — algebra of codes published; ring-theoretic depth off-centre | 5 — Debnath et al., *Galois hulls of constacyclic codes over affine algebra rings*, **349 (2026)**, doi 10.1016/j.disc.2025.114750 | Scopus; SJR 0.782; h-94 | **Q1 (2025)** Discrete Math & Combinatorics (Q1 since 2016); **Q1 (2025)** TCS | Hybrid (Elsevier) | **USD 3 530** gold OA, all article types; **subscription free** | EM portal `DISCM`; no page limit stated (**UNVERIFIED**); peer-review model **UNVERIFIED** | [home](https://www.sciencedirect.com/journal/discrete-mathematics) · [OA/APC](https://www.sciencedirect.com/journal/discrete-mathematics/publish/open-access-options) · [SCImago 25892](https://www.scimagojr.com/journalsearch.php?q=25892) |
| **Adv. Math. Commun.** | 5 — coding theory + algebra/number theory with comms relevance | 4 — demands "new techniques and depth"; rejects non-conforming work | 5 — hull cluster: doi 10.3934/amc.2025054 (2026); doi 10.3934/amc.2024013 (2025); Debnath–Prakash (Jan 2025) | Scopus; SJR 0.576; h-31 | **Q2 (2025)** Applied Math; Q2 Algebra & Number Theory; Q2 Discrete Math & Comb.; Q2 Comms | Hybrid (AIMS) | **UNVERIFIED** on official AIMS pages; subscription route carries no author charge | **Median first decision 112 days; median review 138 days**; no page limit stated (**UNVERIFIED**) | [home](https://aimsciences.org/AMC) · [SCImago 18800156711](https://www.scimagojr.com/journalsearch.php?q=18800156711) |
| **J. Algebra Appl.** | 4 — applied algebra with application-field links; coding-theory special issues | 5 — strongest pure-algebra home; we cite Dinh 2024 here | 3 — coding-theory special issues exist; no regular-issue hull paper verified | Scopus; SJR 0.492; h-37 | **Q2 (2025)** Algebra & Number Theory; Q2 Applied Math | Hybrid (World Scientific) | **"There will be no page charge"**; OA APC **UNVERIFIED** | Abstract **≤ 200 words**; references numbered alphabetically — **already satisfied by `plain` (D-1)**; broad-audience introduction; EM portal `jaa`; choose nearest board member | [home](https://www.worldscientific.com/worldscinet/jaa) · [guidelines](https://www.worldscientific.com/page/jaa/submission-guidelines) · [style files](https://www.worldscientific.com/page/authors/journal-stylefiles) · [SCImago 11800154589](https://www.scimagojr.com/journalsearch.php?q=11800154589) |
| **Cryptogr. Commun.** | 3 — algebraic structures "strongly encouraged", but journal centre is ciphers/sequences; **paper has no crypto content** | 4 — SJR 0.853 Q1; we cite Luo–Parampalli 2018 here | 3 — none verified | Scopus; SJR 0.853; h-28 | **Q1 (2025)** Applied Math; Q1 Computational Theory & Math; Q1 Computer Networks & Comms | Hybrid (Springer) | **USD 3 290 / £2 390 / €2 690**; subscription free | No page limit stated (**UNVERIFIED**); peer-review model **UNVERIFIED** | [home](https://www.springer.com/journal/12095) · [APC](https://link.springer.com/journal/12095/how-to-publish-with-us) · [SCImago 19600156814](https://www.scimagojr.com/journalsearch.php?q=19600156814) |
| **IEEE Trans. Inform. Theory** | 3 — information theory; we cite 2 TIT papers, but centre is not ring-theoretic | 5 — deepest venue in the set; SJR 1.323 | 2 — none verified | Scopus; SJR **1.323**; h-310 | **Q1 (2025)** in every category (Q1 1999–2025) | Hybrid (IEEE) | **CONFLICT**: USD 2 800 (Xplore) vs "discounted USD 1 750" (IT Soc.) | **50-page single-column submission cap (since 2025-05-01); 25-page final two-column cap**; abstract ≤ 250 words, one paragraph, no displayed math; 5–10 index terms; single-anonymous; ORCID required for all authors | [IT Soc. author info](https://www.itsoc.org/it-trans/author-info) · [Xplore](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=18) · [SCImago 15107](https://www.scimagojr.com/journalsearch.php?q=15107) |
| **AAECC** | 4 — coding, cryptography, networks named in scope | 3 — "purely theoretical papers will not primarily be sought" | 2 — none verified | Scopus; SJR 0.389; h-40 | **Q3 (2025)** Algebra & Number Theory; Q3 Applied Math (has oscillated Q2–Q4) | Hybrid (Springer) | **USD 3 190 / £2 290 / €2 590**; subscription free | **Single-blind**; Springer LaTeX macro, option `smallextended`; **Author Contribution + Competing Interest + Data Availability Statement required** | [home](https://link.springer.com/journal/200) · [guidelines](https://link.springer.com/journal/00200/submission-guidelines) · [APC](https://link.springer.com/journal/200/how-to-publish-with-us) · [SCImago 28048](https://www.scimagojr.com/journalsearch.php?q=28048) |
| **Quantum Inf. Process.** | 2 — QEC in scope, but venue is physics/EE-weighted | 2 — algebra would read as unmotivated; `d = 4` reads as thin | 2 — none verified | Scopus; SJR 0.441; h-85 | **Q2 (2025)** Electrical & Electronic Eng.; Q2 TCS; Q2 Signal Processing; Q3 Materials | Hybrid (Springer) | **USD 3 090 / £2 190 / €2 490**; subscription free | No page limit stated (**UNVERIFIED**); peer-review model **UNVERIFIED** | [home](https://link.springer.com/journal/11128) · [APC](https://link.springer.com/journal/11128/how-to-publish-with-us) · [SCImago 24831](https://www.scimagojr.com/journalsearch.php?q=24831) |
| **Entropy** | 2 — "coding and compression" here means source coding, not ring-theoretic construction | 2 — no home for structural algebra | 1 — none verified | Scopus; SJR 0.475; h-123 | **Q2 (2025)** Information Systems; Q2 Electrical & Electronic Eng.; Q2 Mathematical Physics | **Fully OA (MDPI)** — no subscription route | **CHF 2 600 mandatory** (+ VAT where applicable) | No page limit stated (**UNVERIFIED**); peer-review model **UNVERIFIED** | [home](https://www.mdpi.com/journal/entropy) · [APC](https://www.mdpi.com/journal/entropy/apc) · [SCImago 13715](https://www.scimagojr.com/journalsearch.php?q=13715) |

## 6. Ranked result

| rank | journal | A | B | C | D | E | **weighted** |
|---|---|---|---|---|---|---|---|
| 1 | **Finite Fields and their Applications** | 5 | 5 | 5 | 4 | 5 | **4.85** |
| 2 | **Designs, Codes and Cryptography** | 5 | 5 | 4 | 5 | 4 | **4.70** |
| 3 | **Discrete Mathematics** | 4 | 4 | 5 | 3 | 5 | **4.15** |
| 4 | **Advances in Mathematics of Communications** | 5 | 4 | 5 | 2 | 3 | **4.10** |
| 5 | Journal of Algebra and its Applications | 4 | 5 | 3 | 4 | 3 | 3.95 |
| 6 | Cryptography and Communications | 3 | 4 | 3 | 3 | 4 | 3.35 |
| 7 | IEEE Transactions on Information Theory | 3 | 5 | 2 | 1 | 5 | 3.20 |
| 8 | Applicable Algebra in E.C.C. | 4 | 3 | 2 | 3 | 2 | 3.00 |
| 9 | Quantum Information Processing | 2 | 2 | 2 | 3 | 3 | 2.25 |
| 10 | Entropy | 2 | 2 | 1 | 3 | 3 | 2.05 |

**Note on ranks 3 and 4.** Discrete Mathematics (4.15) and AMC (4.10) are
separated by 0.05, which is inside the noise band of a 5-point integer scale
(framework limitation 2). They are effectively tied and they trade off in
opposite directions: Discrete Mathematics offers Q1 visibility and a faster
process but is a combinatorics-first venue with the highest APC in the set;
AMC offers the densest topical cluster and coding theory as a core subject but
verifiably takes ~112 days to a first decision. **The author should choose
between them on preference, not on this ranking.**

**Note on rank 7.** IEEE TIT scores 3.20 *despite* having the highest SJR in
the set and a perfect 5 on mathematical fit. That is the scoring framework
working as intended: criterion E carries only 10 %, and the 25-page final cap
is a genuine, verified obstacle for a manuscript of this length. TIT is not
recommended, but if the author's priority is prestige and a substantial cut is
acceptable, the per-criterion row above shows exactly what would have to
change.

## 7. What this comparison does not tell you

* It does not tell you the probability of acceptance anywhere. No such estimate
  is made in Phase 9.
* It does not tell you referee behaviour, editorial load, or current backlog
  beyond the few official timing figures quoted.
* It does not tell you whether the manuscript would survive review — the open
  issues m-1…m-6 and M-1 recorded in
  `PHASE9_MANUSCRIPT_PROFILE.md` §7 are the real constraints on that, and they
  are journal-independent.
* It does not incorporate the author's own constraints (funder OA mandates,
  institutional agreements, indexing requirements for an evaluation exercise).
  Those can change the answer and should be applied on top of the table.

---

## Correction record — Phase 11 (2026-11-10), append-only

**Nothing above is deleted or rewritten.** Three venue attributions in this
comparison table were re-verified against official publisher records in
Phase 11 and found to be **wrong**.

| wrong attribution above | correct venue (verified 2026-11-10) |
|---|---|
| FFA — "the manuscript cites two FFA papers (Fan–Zhang 2017; Liu–Pan 2020)" | **Zero** FFA papers are cited. Fan–Zhang is **DCC 84(3), 473–492**; Liu–Pan is **DCC 88(2), 241–255**. |
| Discrete Math. — "(Cao 2021, MDS Galois hulls)" | Cao 2021 is **IEEE Trans. Inform. Theory 67(12), 7964–7984**. |
| J. Algebra Appl. — "we cite Dinh 2024 here" | Dinh et al. 2024 is **Adv. Math. Commun. 18(4), 1100–1122** (doi 10.3934/amc.2022073). |

The FFA fit score of 5 for "scope names algebraic coding theory" **stands** —
it rests on FFA's published aims-and-scope text, which was verified directly.
The fit score for J. Algebra Appl. **drops**, because its cited-paper argument
was the claim about Dinh 2024 and that claim is false.

Source: `PHASE11_FFA_FINALIZATION/PHASE11_BIBLIOGRAPHIC_CORRECTIONS.md`.
