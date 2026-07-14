# CLAUDE.md — Striver's A2Z Sheet

Sheet-specific guidance. Shared conventions live in `../CLAUDE.md` (Python style, skills, hooks, git rules).

## Sheet Overview

Comprehensive DSA sheet from takeuforward.org. 18 steps, 474 problems. Step directories are nested two levels deep: `Step N - Topic/Sub-Topic/file.py`.

## Directory Structure

```
Striver's A2Z Sheet/
  CLAUDE.md            (this file)
  index.html           (progress tracker; localStorage key: striver-a2z-tracker-v1)
  sync_notes.py        (filesystem -> tracker DATA generator + docstring sync)
  Step 1 - Learn the basics/
    Basic Hashing/
      countFrequencies.py
      highest&lowestFrequency.py
    Basic Maths/
    Basic Recursion/
    Patterns/
  Step 2 - Learn Important Sorting Techniques/
    Sorting - I/
    Sorting - II/
  ...
  Step 17 - Tries [Theory and Problems]/
```

Step + sub-step directories are created on demand.

## Folder naming convention

Step folders use `Step N - <Official Title>`, where `<Official Title>` is the exact
section title from the takeuforward A2Z sheet (e.g. `Step 3 - Solve Problems on
Arrays [Easy -> Medium -> Hard]`). The `Step N -` prefix keeps folders ordered on
disk and lets `sync_notes.py` sort them via its `Step (\d+)` regex. The tracker's
section headers (from `STEPS_BY_NUM` in `sync_notes.py`) show the bare official
title without the `Step N -` prefix. Sub-step folder names mirror the sheet's
sub-section names (`Basic Maths`, `Sorting - I`, `Easy`/`Medium`/`Hard`, ...).
Filesystem-illegal characters in a title (e.g. the `/` in Step 12's
`[Easy, Medium/Hard]`) are replaced with `-` in the folder name only.

## Steps

1. Learn the basics (Hashing, Maths, Recursion, Patterns)
2. Learn Important Sorting Techniques
3. Solve Problems on Arrays [Easy -> Medium -> Hard]
4. Binary Search [1D, 2D Arrays, Search Space]
5. Strings [Basic and Medium]
6. Learn LinkedList [Single LL, Double LL, Medium, Hard Problems]
7. Recursion [PatternWise]
8. Bit Manipulation [Concepts & Problems]
9. Stack and Queues [Learning, Pre-In-Post-fix, Monotonic Stack, Implementation]
10. Sliding Window & Two Pointer Combined Problems
11. Heaps [Learning, Medium, Hard Problems]
12. Greedy Algorithms [Easy, Medium/Hard]
13. Binary Trees [Traversals, Medium and Hard Problems]
14. Binary Search Trees [Concept and Problems]
15. Graphs [Concepts & Problems]
16. Dynamic Programming [Patterns and Problems]
17. Tries [Theory and Problems]
18. Strings [Advanced]

## DATA is auto-generated

Unlike the SDE sheet (which has a hand-curated DATA array), the A2Z sheet's DATA is **regenerated from the filesystem on every `sync_notes.py` run**:

- Each `.py` file under `Step N/Sub/*.py` becomes a DATA entry
- Entry name is `camelCase.py` → `Title Case` (e.g., `setMatrixZeroes.py` → `Set Matrix Zeroes`)
- Sub-step name renders as a badge next to the problem
- Difficulty inferred from sub-step name (`Easy` / `Medium` / `Hard`), defaulting to `medium`
- Problems that don't yet exist as files don't appear in the tracker — add the file via `/solve` and rerun `sync_notes.py`

This means: to add a problem, just create the `.py` file in the right Step/Sub-step directory. The tracker picks it up on the next sync.

## Notes Sync

- A file is "fully solved" when `_brute`, `_better`, `_optimal` all have real implementations (use `# SKIP: <reason>` to skip `_brute`/`_better`; `_optimal` is always required)
- `# QUESTION:` block populates the question text; module docstring populates notes
- Run: `python3 sync_notes.py` from this directory
