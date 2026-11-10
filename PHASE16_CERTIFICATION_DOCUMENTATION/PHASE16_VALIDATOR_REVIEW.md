# Phase 16 / Task E — Validator review and false-positive resolution

## 1. The two failures

Phase 15 reported `validate_latex.py`: 13 checks, 11 PASS / 2 FAIL (V9, V11),
both identified as pre-existing heuristic false positives, with a clean genuine
LaTeX build as the counter-evidence. This phase inspected both and determined
that **both can be corrected safely**.

---

## 2. V9 — "every control sequence is defined (heuristic)"

### Root cause

```python
defined = set(BUILTIN)
```

`BUILTIN` is a **hand-written, closed whitelist**. Any control sequence provided
by the TeX/LaTeX format but absent from that list is reported as undefined.
`\penalty`, `\setcounter` and `\textsuperscript` are all genuine commands; the
list simply omits them. This is a structural false-positive generator: it will
fire again on any valid manuscript that uses a kernel command not yet listed.

### Correction

A bounded, named, auditable set `LATEX_KERNEL` (93 entries) of TeX primitives
and LaTeX kernel commands was added, and the check now uses
`defined = set(BUILTIN) | LATEX_KERNEL`.

**Why this is not a broad exclusion.** The set contains no wildcards, no
per-file exemptions, no "ignore the remainder of this file" rules and no
size-based suppression. Every entry is a named command genuinely provided by the
format. Everything not in `BUILTIN`, `LATEX_KERNEL`, the preamble, or a local
`\newcommand` / `\def` is **still reported**. The check remains fully active.

The report line was also made more informative:

```
V9  every control sequence is defined (heuristic)     PASS
    493 distinct macros, all known (384 from BUILTIN, 93 from LATEX_KERNEL, rest user-defined)
```

so the contribution of the kernel set is visible rather than silent.

---

## 3. V11 — "no author/affiliation/funding metadata is invented" (original)

### Root cause

```python
if "AUTHORPLACEHOLDER" not in body and body.strip():
    invented.append(...)
```

The check asserted the **obsolete placeholder regime**: it flagged *any*
`\author{...}` that did not contain `\AUTHORPLACEHOLDER`. Phase 14 replaced the
placeholder with researcher-confirmed metadata (`\AUTHORONE` and companions), so
the check began firing on exactly the intended content. The check is **stale**,
not merely incomplete — it assumes a document state that no longer exists.

### Correction — a strictly stronger check

V11 now tests **conformance to the confirmed metadata** instead of absence of a
placeholder. Author metadata may contain only:

* the confirmed macros `\AUTHORONE`, `\AUTHORONEINST`, `\AUTHORONEORG`,
  `\AUTHORONEADDR`, `\AUTHORONECOUNTRY`, `\CORRESPONDINGEMAIL`
  (or the legacy `\AUTHORPLACEHOLDER`, still accepted);
* a small set of formatting/structure macros (`\textsuperscript`, `\texttt`,
  `\texorpdfstring`, `\\`, …);
* the confirmed literal values themselves, read from the preamble, plus
  permitted connectives (`Corresponding author.`, `E-mail:`, punctuation).

Anything else is reported as unconfirmed.

This is **stronger than the original**, not weaker: the original would have
accepted `\author{Anyone At All}` provided the placeholder was also present, and
could not detect a *wrong* name or e-mail. The new check detects a wrong name, a
wrong e-mail and an invented affiliation.

---

## 4. Self-test: positive and negative cases

`validate_latex_v2.py --selftest` injects a fragment into the **real** manuscript
preamble (so the baseline is clean and only the fragment can move the result) and
asserts the V9/V11 outcome.

| case | expect V9 | expect V11 | result |
|---|---|---|---|
| V9+ counter commands (the CP-3 fix: `\setcounter`, `\renewcommand`, `\Alph`, `\arabic`) | PASS | PASS | PASS |
| V9+ `\penalty` line breaking | PASS | PASS | PASS |
| V9+ `\textsuperscript` in author line | PASS | PASS | PASS |
| V9+ confirmed author block (real form) | PASS | PASS | PASS |
| V9− misspelled `\setcounte` | **FAIL** | PASS | PASS |
| V9− misspelled `\textsuperscrip` | **FAIL** | — | PASS |
| V9− unknown macro `\zzznotreal` | **FAIL** | PASS | PASS |
| V11+ confirmed author line | PASS | PASS | PASS |
| V11+ placeholders still accepted (legacy regime) | PASS | PASS | PASS |
| V11− invented author name `Jane Q. Smith` | PASS | **FAIL** | PASS |
| V11− wrong e-mail inside author block | PASS | **FAIL** | PASS |
| V11− invented affiliation text | PASS | **FAIL** | PASS |

**12 cases, 0 failures.** Crucially, every negative case still fails — genuine
errors are still detected.

### Two harness defects found and fixed (recorded for transparency)

1. The first harness generated synthetic minimal documents, which failed V9 for
   unrelated reasons (`\documentclass`, `\begin{document}` are not in `BUILTIN`).
   Fixed by injecting into the real preamble.
2. `main.tex` contains the string `\begin{document}` **twice** (once inside a
   comment), so `split()` truncated the preamble and lost the `\AUTHORONE`
   definitions, producing spurious V9/V11 failures. Fixed by locating the last
   line-initial occurrence. Neither defect affected the validator itself.

---

## 5. Result on the real manuscript

| validator | result |
|---|---|
| `tools/validate_latex.py` (original, **preserved unchanged**) | 13 checks, **11 PASS / 2 FAIL** — behaviour identical to Phase 15 |
| `tools/validate_latex_v2.py` (corrected) | 13 checks, **13 PASS / 0 FAIL** |

The original is preserved byte-for-byte (SHA-256
`037d7ae0a511192bb0b240bcab4f9c493b88d8cde792e62b01929f74b3603624`, 0 references
to `LATEX_KERNEL`), and its Phase 15 output is not altered or deleted. Both
versions are shipped; the corrected one is recommended for future use.

`tools/verify_examples.py` was **not** modified — it already reports 56 checks /
0 mismatches.

---

## 6. Recommendation

Adopt `validate_latex_v2.py` for future runs, and run `--selftest` whenever
`BUILTIN` or `LATEX_KERNEL` is edited, so that any future extension is
demonstrably safe rather than silently permissive.
