# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository

DSA practice from takeuforward.org. One git repo, multiple sheet directories:

- `Striver's SDE Sheet/` — 27 topics, 191 problems (interview-focused, official takeuforward list; topic-only naming since each takes longer than a day)
- `Striver's A2Z Sheet/` — 17 steps, ~455 problems (comprehensive)

Each sheet directory has its own `index.html` tracker, `sync_notes.py`, and sheet-specific `CLAUDE.md` with the day/step structure.

## Solution File Conventions (apply to every sheet)

- Language: Python
- All functions must have type annotations
- Each solution file defines a `class Solution` (LeetCode-style). The approaches are its methods, and shared helpers are methods invoked via `self.<helper>(...)`. A trailing `if __name__ == "__main__":` block instantiates `Solution()` and runs sample input.
- Method naming differs by sheet (both are class-based): the `Striver's SDE Sheet/` uses `<name>_brute`, `<name>_better`, `<name>_optimal`; the `Striver's A2Z Sheet/` uses `findSolution`, `findSolution1`, `findSolution2`, … (brute → optimal).
- "Implement-a-class" problems (linked lists, LRU/LFU cache, stacks/queues) keep their domain class — `Node`, `LRUCache`, etc. — alongside or instead of `Solution`.
- Filenames are camelCase, matching the problem name (e.g., `setMatrixZeroes.py`, `nextPermutation.py`)
- Every solution file MUST start with a `# QUESTION:` block (the source of truth for problem text — synced to the sheet's tracker) followed by a multi-approach docstring, then the `class Solution`:

```python
# QUESTION: <Problem Name>
# <problem description>
# Example 1:
# Input: ...
# Output: ...

"""
#Brute Force:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#Better Approach:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#Optimal Approach:
1. <step-by-step in pseudo-code + english>
TC -> O(), SC -> O()

#KEY INSIGHT:
- <core idea that makes the optimal solution work>
"""


class Solution:
    def <name>_brute(self) -> None:
        pass

    def <name>_better(self) -> None:
        pass

    def <name>_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.<name>_optimal(...)
```

- Only fill in notes for approaches the user has actually written — do NOT pre-fill or reveal approaches they haven't implemented yet
- Notes style: numbered steps in pseudo-code + english, with `TC -> O(), SC -> O()` at end
- Use `# SKIP: <reason>` inside a `_brute` or `_better` method to mark it intentionally skipped (the `_optimal` method is always required)

## Skills (in `.claude/skills/`, shared across sheets)

- `/solve <problem-name> <sheet/topic-or-step>` — creates the file with docstring scaffold and guides with hints; does NOT write the solution
- `/validate <file-path>` — classifies the user's solution as brute/better/optimal with complexity analysis, suggests improvements, syncs notes to the sheet's `.py` file and tracker
- `/progress [sheet]` — prints per-topic/step solve stats across one or all sheets
- `/visualize <file-path>` — generates a self-contained HTML animation of the optimal algorithm next to the `.py` file (color-coded states, step controls, captions, hardcoded sample)

## Hooks (in `.claude/settings.json`, apply repo-wide)

- **PostToolUse**: After every Write/Edit on a `.py` file, runs `ruff format` + `ruff check --fix`, then `mypy`
- **PreToolUse**: Blocks Write/Edit on any `index.html` or `sync_notes.py` — requires explicit user confirmation before either is modified

## Per-sheet tracker

- Each sheet's `index.html` is a self-contained progress tracker (open in a browser). Each sheet uses a distinct localStorage key so trackers don't collide.
- Each sheet's `sync_notes.py` syncs that sheet's `.py` docstrings into that sheet's `index.html` DATA entries. Run from inside the sheet directory: `python3 sync_notes.py`.

## Lint Considerations

- `C0200` (consider-using-enumerate) is disabled — `for i in range(len(...))` is intentional in DSA code where index access matters
- Do NOT suggest `enumerate` replacements in solution files unless the user asks
- Both camelCase and snake_case are allowed for function, argument, and variable names (`N802`/`N803`/`N806` are ignored in ruff) — do NOT rename identifiers to snake_case

## Git

- Do NOT add `Co-Authored-By` lines in commits
- Commit message style: `<Problem Name 1>, <Problem Name 2> ... Completed`

## Commands

```bash
ruff check .          # lint
ruff check . --fix    # lint and auto-fix
ruff format .         # format all files
mypy .                # type check

# from inside a sheet directory:
python3 sync_notes.py # sync docstrings into that sheet's tracker
open index.html       # open that sheet's progress tracker
```
