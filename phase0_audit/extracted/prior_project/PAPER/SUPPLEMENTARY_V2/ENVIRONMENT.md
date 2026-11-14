# Environment

Recorded environment of the computation whose outputs are quoted in the
manuscript. Everything below is reported by the scripts themselves or by the
platform; nothing is inferred.

## Interpreter and platform

| item | value |
|---|---|
| Python | `3.11.2 (main, Apr 8 2026, 01:58:00) [GCC 12.2.0]` |
| OS / kernel | Linux `6.1.158+` x86_64, SMP PREEMPT_DYNAMIC |
| CPUs | 2 |
| RAM available | 3939 MB |
| Third-party packages | **none** |

The header printed by `phase7_extended_search.py` records both the seed and
the interpreter version:

```
#  seed   : 20261210        python 3.11.2
```

## Dependencies

Pure Python standard library only. The modules used are:

`sys`, `os`, `time`, `random`, `json`, `csv`, `re`, `itertools`,
`collections`, `resource`, `hashlib`.

No numpy, sympy, Sage, GAP or Magma is used or required. Arithmetic in
$\mathbb F_q$, in $A_t=\mathbb F_q[u]/\langle u^t\rangle$, in $R=M_2(A_t)$
and in $R_n=R[X]/\langle X^n-1\rangle$ is implemented from first principles
in `scripts/matrix_ring_lib.py`, deliberately, so that every step of every
computation can be inspected without trusting a computer-algebra system.

## Resource envelope of the recorded run

Reported by the completion report of `phase7_extended_search_log.txt`:

```
  families scanned: 25 ; codes with computed invariants: 120721 ;
  codes with a computed distance: 5055 (of which 4418 exact and 637 a proved lower bound)

  peak resident memory   : 367.3 MB
  SEED = 20261210 ; every random choice is drawn from random.Random(SEED)
  in a fixed order, so the run is reproducible: two runs of this
  script agree on every line EXCEPT the per-family elapsed-time
  annotations [..s] and the peak-memory line, which are wall-clock
  and resource readings and take no part in any computation.
```

The wall-clock time of the full Phase-7 run was 516.6 s. The
generator-matrix extraction script (`extract_certified_generators.py`), which
re-runs Parts 2, 3 and 6 only, took about 460 s in this environment.

## Determinism

Two sources of non-determinism are excluded:

1. **Randomness.** Fixed seed, single `random.Random(SEED)` instance, fixed
   order of consumption.
2. **Set/dict iteration order.** Python's `set` and `dict` preserve insertion
   order, but the scripts additionally sort every collection whose iteration
   order could affect an output (`sorted(...)` on family lists, candidate
   lists and the codes themselves before selection).

The only lines that differ between two runs are the per-family elapsed-time
annotations `[..s]` and the peak-memory line.
