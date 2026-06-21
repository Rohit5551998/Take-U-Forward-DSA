# CLAUDE.md — Striver's A2Z Sheet

Sheet-specific guidance. Shared conventions live in `../CLAUDE.md` (Python style, skills, hooks, git rules).

## Sheet Overview

Comprehensive DSA sheet from takeuforward.org. 17 steps, ~455 problems planned. Step directories are nested two levels deep: `Step N - Topic/Sub-Topic/file.py`.

## Directory Structure

```
Striver's A2Z Sheet/
  CLAUDE.md            (this file)
  index.html           (progress tracker; localStorage key: striver-a2z-tracker-v1)
  sync_notes.py        (filesystem -> tracker DATA generator + docstring sync)
  Step 1 - Basics/
    Basic Hashing/
      countFrequencies.py
      highest&lowestFrequency.py
    Basic Maths/
    Basic Recursion/
    Patterns/
  Step 2 - Sorting Techniques/
    Sorting - I/
    Sorting - II/
  ...
  Step 17 - Tries/
```

Step + sub-step directories are created on demand.

## Steps

1. Basics (Hashing, Maths, Recursion, Patterns)
2. Sorting Techniques
3. Arrays (Easy / Medium / Hard)
4. Binary Search (1D / 2D / on Answers)
5. Strings
6. Linked Lists (Singly, Doubly, Hard)
7. Recursion
8. Bit Manipulation
9. Stacks and Queues (Learning, Implementation, Monotonic, Prefix/Infix/Postfix)
10. Sliding Window & Two Pointer Combined (Medium, Hard)
11. Heaps
12. Greedy Algorithms
13. Binary Trees
14. Binary Search Trees
15. Graphs
16. Dynamic Programming (1D / 2D / DP on LIS / DP on Stocks / DP on Strings / DP on Subsequences / MCM / DP on Squares)
17. Tries

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
