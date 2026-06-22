---
name: validate
description: Classify a Striver solution as brute/better/optimal, generate notes in .py file, and trigger sync to that sheet's tracker (if present)
---

# Validate a Striver Solution

## Arguments
- `<file-path>`: Path to the solution file, relative to repo root (e.g., `"Striver's SDE Sheet/Arrays/setMatrixZeroes.py"`)

The sheet is inferred from the file path's first segment.

## Workflow

1. **Read the solution file** and identify the problem name from the filename/docstring.

2. **Look up the problem** — use WebSearch to find the exact problem on takeuforward.org / LeetCode to understand constraints and known optimal complexity. If web search fails, ask the user for the problem link. NEVER guess optimal complexity from memory.

3. **Identify which function was written/changed** — check `_brute`, `_better`, `_optimal` functions. Validate the one that has a real implementation (not `pass`).

4. **Analyze the implementation:**
   - Identify the algorithm/approach used
   - Determine the time complexity (Big O)
   - Determine the space complexity (Big O)

5. **Classify the solution** as one of:

   | Classification | Criteria |
   |---------------|----------|
   | **BRUTE FORCE** | Naive approach, typically O(n^2) or worse, no clever data structures |
   | **BETTER** | Improved over brute force but not optimal (e.g., sorting-based O(n log n) when O(n) exists) |
   | **OPTIMAL** | Best known time/space complexity for this problem |

6. **Output a verdict** in this format:

   ```
   ## Verdict: [BRUTE FORCE / BETTER / OPTIMAL]

   **Your approach:** <one-line description of what the code does>
   **Time:** O(...)
   **Space:** O(...)

   **Why this classification:**
   - <explain why it falls into this category>

   **Can you do better?** [Yes/No]
   - <if yes, give a HINT not the answer — e.g., "Think about trading space for time" or "What data structure gives O(1) lookup?">
   ```

7. **Auto-generate notes in the .py file** for the classified approach in the docstring using this style:

   ```
   #Brute Force:
   1. <step-by-step in pseudo-code + english describing what the user's code does>
   2. <next step>
   TC -> O(...), SC -> O(...)
   ```

   - Write notes ONLY for the approach the user implemented — leave other approaches blank
   - Describe what the user's actual code does, not a textbook description
   - Use numbered steps in pseudo-code + english
   - **Steps must be DESCRIPTIVE, not terse.** Each step should explain the *why* behind the action (the intuition / what problem it solves), not just restate the line of code. Walk through what the code actually does and why it works. A concrete tiny example or the cost reasoning is welcome. Aim for clarity a reader could learn the approach from.
   - End with `TC -> O(), SC -> O()`
   - If the file's functions are actually **separate problem variants** (not brute/better/optimal of one problem — e.g. "value at (r,c)" vs "n-th row" vs "full triangle"), restructure the docstring into per-variant sections (`#Variant I — <name>: <func_name>`) each with its own steps + `TC -> O(), SC -> O()`, instead of forcing them into the Brute/Better/Optimal template.
   - Update the docstring in the file using Edit

8. **Sync notes to that sheet's tracker:**
   - From repo root: `cd "<sheet>" && python3 sync_notes.py` (only if the sheet has `sync_notes.py` + `index.html`)
   - Do NOT edit `index.html` directly — let `sync_notes.py` do it. The PreToolUse hook blocks direct edits anyway.

9. **If the solution is optimal:**
    - Confirm it and congratulate
    - Fill in the `#KEY INSIGHT:` in the docstring

10. **Do NOT:**
    - Write or rewrite the solution code
    - Give away other approaches — only hints
    - Fill in notes for approaches the user hasn't implemented
