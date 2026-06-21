# CLAUDE.md — Striver's SDE Sheet

Sheet-specific guidance. Shared conventions live in `../CLAUDE.md` (Python style, skills, hooks, git rules).

## Sheet Overview

Top coding interview problems from takeuforward.org. 27 topic sections, 191 problems (25 easy / 93 medium / 73 hard). Synced from the official sheet on 2026-06-21. Topic directories follow the original sheet's grouping (the source uses "Day N" labels, but each topic realistically takes longer than a day — directories are named by topic only).

## Directory Structure

```
Striver's SDE Sheet/
  CLAUDE.md            (this file)
  index.html           (progress tracker; localStorage key: striver-sde-tracker-v1)
  sync_notes.py        (docstring -> tracker sync)
  Arrays/
    setMatrixZeroes.py
    pascalsTriangleI.py
    ...
  Arrays Part-II/
  ...
  Trie/
```

All 27 topic directories and 191 scaffold .py files are pre-generated.

## Topics (order matches takeuforward source)

1. Arrays (6)
2. Arrays Part-II (6)
3. Arrays Part-III (6)
4. Arrays Part-IV (6)
5. Linked List (6)
6. Linked List Part-II (6)
7. Linked List and Arrays (6)
8. Greedy Algorithm (6)
9. Recursion (6)
10. Recursion and Backtracking (6)
11. Binary Search (8)
12. Heaps (6)
13. Stack and Queue (7)
14. Stack and Queue Part-II (10)
15. String (6)
16. String Part-II (6)
17. Binary Tree (12)
18. Binary Tree Part-II (8)
19. Binary Tree Part-III (7)
20. Binary Search Tree (7)
21. Binary Search Tree Part-II (8)
22. Binary Trees Misc (6)
23. Graph (12)
24. Graph Part-II (6)
25. Dynamic Programming (7)
26. Dynamic Programming Part-II (8)
27. Trie (7)

## Notes Sync

- `sync_notes.py` walks `Day */*.py`, extracts each file's `# QUESTION:` block and docstring, and writes them as `q` and `n` fields on matching DATA entries in `index.html`
- A file is considered "fully solved" when `_brute`, `_better`, `_optimal` all have real implementations (use `# SKIP: <reason>` to skip `_brute`/`_better`; `_optimal` is always required)
- Run: `python3 sync_notes.py` from this directory
