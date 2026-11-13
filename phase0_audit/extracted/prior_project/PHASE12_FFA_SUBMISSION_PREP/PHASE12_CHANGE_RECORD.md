# Phase 12 / Task D — Declaration change record

Append-only record of every change made to the manuscript declarations.
Original text is preserved; nothing was silently overwritten.

Scope: **`PAPER/FFA_SUBMISSION_STAGING/main.tex` only.** The canonical
`PAPER/main.tex` is byte-identical to its pre-Phase-11 state
(`ee47ce7e…4501737c`) and was not touched.

## Change 1 — Declaration of competing interests

| | |
|---|---|
| **Status** | **CONFIRMED** by the researcher, 2026-11-10 |
| **Confirmation source** | direct question, option "Nothing to declare" |

**Original text (Phase 11 placeholder):**

```
\section*{Declaration of competing interests}
\label{sec:competinginterests}

[\emph{Researcher confirmation required}.] Elsevier requires all authors to
disclose any financial and personal relationships with other people or
organisations that could inappropriately influence or bias their work, and
requires the declarations tool at \texttt{declarations.elsevier.com} to be
completed and uploaded at the submission step. Proposed wording,
\textbf{pending confirmation by every author}:

\begin{quote}
The authors declare that they have no known competing financial interests or
personal relationships that could have appeared to influence the work
reported in this paper.
\end{quote}

If any author does have a competing interest, replace the sentence above with
the disclosure. This statement has \textbf{not} been confirmed and must not be
submitted as final.
```

**New text:**

```
\section*{Declaration of competing interests}
\label{sec:competinginterests}

The authors declare that they have no known competing financial interests or
personal relationships that could have appeared to influence the work
reported in this paper.

\emph{Status: CONFIRMED by the researcher on 2026-11-10.} The declarations
tool at \texttt{declarations.elsevier.com} must still be completed and the
generated statement uploaded at the submission step; see
\texttt{PHASE12\_CONFIRMATION\_REGISTER.md}, category A6.
```

**Rationale:** the researcher confirmed "nothing to declare", so the
placeholder scaffolding (the disclaimer, the "must not be submitted as final"
warning, the quote environment) was removed and the declaration promoted to
final text. The procedural note about `declarations.elsevier.com` was
**retained**, because completing that tool is still an outstanding action.

**Approval status:** APPROVED by researcher.

## Change 2 — Funding

| | |
|---|---|
| **Status** | **CONFIRMED** by the researcher, 2026-11-10 |
| **Confirmation source** | direct question, option "No specific grant" |

**Original text (Phase 11 placeholder):**

```
\section*{Funding}
\label{sec:funding}

[\emph{Researcher confirmation required}.] Elsevier requires disclosure of
funding sources and of the role of sponsors. Two permitted outcomes:

\begin{enumerate}
\item If the work was funded: \emph{``Funding: This work was supported by
  [FUNDING AGENCY], [COUNTRY] [grant number [NUMBER]].''}
\item If no funding was received, the Elsevier standard wording:
  \emph{``This research did not receive any specific grant from funding
  agencies in the public, commercial, or not-for-profit sectors.''}
\end{enumerate}

The funding status of this work is \textbf{unconfirmed}. No grant, agency or
award number has been recorded in the project documentation, and none has
been inferred.
```

**New text:**

```
\section*{Funding}
\label{sec:funding}

This research did not receive any specific grant from funding agencies in the
public, commercial, or not-for-profit sectors.

\emph{Status: CONFIRMED by the researcher on 2026-11-10.} The funded
alternative was not used; see
\texttt{PHASE12\_CONFIRMATION\_REGISTER.md}, category A7.
```

**Rationale:** the researcher selected "No specific grant", so option 2 of the
original enumerate was promoted and the enumerate removed. The "unconfirmed"
sentence was replaced with a CONFIRMED note.

**Approval status:** APPROVED by researcher.

## Change 3 — Author-metadata block (structure only)

| | |
|---|---|
| **Status** | **PARTIAL CONFIRMATION** — count confirmed, values pending |
| **Confirmation source** | direct question, option "Single author" |

**Change:** the commented-out second-author macro block was removed and
replaced with a note that the block is **disabled** because the author count
is confirmed as 1. The header comment was updated to record that the count is
confirmed while the name, affiliation and email remain pending.

**No value was filled in.** All six macros still carry their bracketed
placeholders.

**Rationale:** with the author count confirmed, leaving a commented-out
second-author template is misleading — it suggests an unfilled option rather
than a resolved decision. The block is now explicitly disabled with a note
that it should be re-enabled only on instruction to add an author.

**Approval status:** count APPROVED; values PENDING.

## Change 4 — Cross-reference updates (no substantive change)

Two internal pointers were updated from Phase 11 document names to Phase 12
names:

| location | old | new |
|---|---|---|
| Data availability section | `PHASE11_RESEARCH_DATA_PLAN.md` | `PHASE12_RESEARCH_DATA_DEPOSIT_PLAN.md` |
| Generative-AI section | `PHASE11_GENERATIVE_AI_DECLARATION.md` | `PHASE12_CONFIRMATION_REGISTER.md` (category A8) |

**Rationale:** Phase 12 supersedes those Phase 11 documents. No wording of any
declaration changed.

## Changes deliberately NOT made

| section | why untouched |
|---|---|
| **Data availability** | **PENDING.** No deposit exists, so no truthful statement can be inserted. The placeholder remains. |
| **Generative AI** | **PENDING.** The researcher explicitly chose to leave this pending. No tool name was guessed. |
| **Acknowledgements** | **PENDING — optional.** Marked removable if there is nothing to acknowledge. |
| **CRediT contributions** | **PENDING — encouraged, not mandatory.** Cannot be completed without the author name. |

## Verification

After these changes the manuscript was rebuilt: **0 errors, 0 warnings, 42
pages**, PDF SHA-256 `72bfa79dd0f08d11dc559febd923ce4351993f6dfd4989ae80233845946d20e0`.
The two confirmed declarations were verified as correctly rendered on page 37
of the compiled PDF.
