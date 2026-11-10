# Phase 14 — Correction proposals

Four issues were found. **None has been applied.** Per instruction, substantive
changes await explicit researcher approval.

Status: **PROPOSED — NOT APPLIED** (all four)

---

## CP-1 — "Three independent methods" overstates the certification

| | |
|---|---|
| **Status** | **RESEARCHER REVIEW REQUIRED** |
| **Severity** | Medium — affects the abstract, the introduction and one supplementary document |
| **Type** | Presentation of results, not a mathematical error |

### The claim as it stands

| location | wording |
|---|---|
| `PAPER/main.tex:131` (abstract, **canonical**) | "…certifies $28$ codes by **three independent methods**…" |
| `PAPER/sections/01_introduction.tex:124` | "…certifies $28$ codes by **three independent methods**…" |
| `PAPER/supplementary/CERTIFICATION_PROCEDURE.md` | "**Every** headline code is certified by **three structurally different methods**." |

### What the committed data show

From `supplementary/parameter_tables/certified_codes.csv`:

| route | codes | M1 | M2 | M3 | methods applicable |
|---|---:|---|---|---:|---:|
| SO / DC (stabilizer) | 4 | **`-`** (did not complete) | value | lower bound | **2** |
| EA | 24 | value | **`n/a`** | lower bound | **2** |

**Codes with all three methods: 0 of 28.** Every code has exactly 2.

The pattern is route-dependent and complementary: for stabilizer codes the
complete enumeration (M1) is too large, so the support search (M2) carries the
exact value; for EA codes the quotient is small enough to enumerate (M1), and
the support search is recorded `n/a`.

### Corroboration from the project's own records

`PAPER/OPEN_ISSUES_AND_LIMITATIONS.md`, §2 item 4, states correctly:

> "**M3 is a lower bound for most codes.** The ambient quantum search reaches
> only weight 2 or 3 for 22 of the 28 certified codes; **the exact distances
> come from M1 (complete enumeration) and M2 (support search)**."

And `PAPER/sections/appendix_tables.tex:16` is carefully hedged:

> "The column ``exact'' says yes when **all three methods that completed**
> agree with the reported value…"

So the appendix and the open-issues file are accurate; the abstract, the
introduction and `CERTIFICATION_PROCEDURE.md` are not.

### Proposed correction (not applied)

Abstract and introduction:

> "…certifies $28$ codes, each by two independent methods drawn from three
> (complete enumeration, support search, and an ambient quantum search)…"

`CERTIFICATION_PROCEDURE.md`:

> "Every headline code is certified by two independent methods. Three methods
> are employed across the set: M1 and M2 give exact distances and are
> complementary by route; M3 is an independent cross-check that is complete
> only up to the weight reached and is reported as a lower bound otherwise."

### Why this matters

The claim is load-bearing in the abstract — it is one of the paper's headline
methodological strengths. As written, a referee checking the table would find
dashes and `n/a` entries and could read the claim as overstated. The corrected
form is equally strong and is accurate.

---

## CP-2 — `ex:certify` attributes agreement to method M2, which is `n/a` there

| | |
|---|---|
| **Status** | **RESEARCHER REVIEW REQUIRED** |
| **Severity** | Low-Medium — one sentence in Example 13 |
| **Type** | Text/evidence mismatch |

### Location

`PAPER/sections/08_certification.tex`, lines 343–346 (Example 13, `ex:certify`).

### The text

> "Its $4^2=16$ codewords are enumerated completely (method M1), and the
> minimum weight found is $10$; **the independent support search (M2)** and the
> ambient quantum search (M3, which certifies $d\ge3$ as a lower bound)
> **agree with the reported value**."

### The data

`certified_codes.csv`, row `[[20,2,10;18]]_4`:

```
M1 = 10,  M2 = n/a,  M3_lower_bound = >2,  all_methods_agree = yes
```

Phase-7 log line 454 confirms: `(4,1,5,20,EA) | 18 2 10 18 | 10 | n/a | >2 | yes`.

**M2 was not run for this code.** Attributing agreement to it is inaccurate.

### Everything else in the example is correct

Independently recomputed and confirmed:

| claim | check |
|---|---|
| $c = k-h_E = 18-0 = 18$ | ✅ |
| $K = N-k-h_E = 20-18-0 = 2$ | ✅ |
| $[[20,2,10;18]]_4$ | ✅ |
| EA Singleton $N-K+c = 36 \ge 2(d-1) = 18$, defect 18 | ✅ |
| EA Hamming bound holds ($0.058 \le 1.10\times10^{12}$) | ✅ |
| coset Singleton $K+d = 12 \le N+1 = 21$ | ✅ |
| $k=18$ even | ✅ |
| $K-c = -16 = N-2k$, divisible by 4 | ✅ |
| $c+K = 20 = N-2h_E$; the old formula $N-k=2$ is indeed false | ✅ |
| M3 gives $d\ge3$, consistent with $d=10$ | ✅ |

### Proposed correction (not applied)

> "Its $4^2=16$ codewords are enumerated completely (method M1), and the
> minimum weight found is $10$. The ambient quantum search (M3) independently
> certifies $d\ge3$ as a lower bound, consistent with this value; the support
> search (M2) is not applicable to the entanglement-assisted route. Hence
> $d=10$ exactly."

---

## CP-3 — Appendix tables are numbered 5–6, not A.1–A.2

| | |
|---|---|
| **Status** | **OPEN** |
| **Severity** | Low — formatting convention |
| **Type** | Deviation from a stated FFA convention |

### The requirement (official FFA guide, verified 2026-11-10)

> "Identify individual appendices within your article using the format: A, B,
> etc.
> Give separate numbering to formulae and equations within appendices using
> formats such as Eq. (A.1), Eq. (A.2), etc. … In a similar way, give separate
> numbering to tables and figures using formats such as **Table A.1**; Fig.
> A.1, etc."

### The current state

The two appendix tables render as **Table 5** and **Table 6**, continuing the
main document's numbering rather than restarting as A.1 and A.2.

### Proposed correction (not applied)

Enable per-appendix table numbering, e.g. `\renewcommand{\thetable}{A.\arabic{table}}`
after `\appendix` with `\setcounter{table}{0}`, giving **Table A.1** and
**Table A.2**.

### Note

This is cosmetic and FFA applies its own styling at proof stage. It is
reported for completeness, not as a defect.

---

## CP-4 — 9 DOIs are present in `references.bib` but do not render

| | |
|---|---|
| **Status** | **OPEN** |
| **Severity** | Low |
| **Type** | Bibliography style limitation |

### The facts

9 of the 13 entries carry a `doi` field; 4 do not (`LiuPan2020GaloisHulls`,
`Cao2021MDSGaloisHulls`, `KetkarEtAl2006NonbinaryStabilizer`,
`GrasslCodetables`).

**Zero** DOIs appear in the compiled PDF: `plain.bst` has no `doi` field
support, so the field is silently dropped.

FFA's guide says "Where available include Digital Object Identifiers (DOIs)".

### Mitigating consideration

FFA also states: "This journal does not set strict requirements on reference
formatting at submission… Our journal reference style will be applied to your
article after acceptance, at proof stage."

So at submission this is not a violation. Phase 8B decision D-1 deliberately
retained `plain` (alphabetical order), which also satisfies JAA's requirement.

### Proposed options (not applied)

1. Leave as is — acceptable at submission; the DOI data are preserved in the
   source and will be available at proof stage.
2. Switch to `plainnat`/`unsrtnat` with `natbib` so DOIs render.

Recommendation: **option 1** unless the researcher wants DOIs visible now.

---

## Summary

| id | issue | status | applied? |
|---|---|---|---|
| CP-1 | "three independent methods" overstates per-code certification | RESEARCHER REVIEW REQUIRED | **no** |
| CP-2 | `ex:certify` credits M2, which is `n/a` there | RESEARCHER REVIEW REQUIRED | **no** |
| CP-3 | Appendix tables numbered 5–6, not A.1–A.2 | OPEN | **no** |
| CP-4 | 9 DOIs in source, 0 rendered | OPEN | **no** |

**No mathematical statement, theorem, proof or numerical parameter has been
changed.**
