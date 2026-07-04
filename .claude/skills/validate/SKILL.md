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

3. **Identify which method was written/changed** — solutions are methods of a `class Solution`. Check the `_brute`/`_better`/`_optimal` methods (SDE sheet) or `findSolution`/`findSolution1`/… methods (A2Z sheet). Validate the one that has a real implementation (not `pass`).

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
   - **Keep each step to ONE idea, and scale the step count to the algorithm.** Don't cram intuition + pointer setup + the loop + the stop condition into one giant step — break it into more, shorter steps (one move/decision each). Conversely, intricate algorithms (e.g. gap/shell merge) need MORE steps and depth — never leave a complex approach with only 2–3 terse lines.
   - End with `TC -> O(), SC -> O()`
   - If the file's functions are actually **separate problem variants** (not brute/better/optimal of one problem — e.g. "value at (r,c)" vs "n-th row" vs "full triangle"), restructure the docstring into per-variant sections (`#Variant I — <name>: <func_name>`) each with its own steps + `TC -> O(), SC -> O()`, instead of forcing them into the Brute/Better/Optimal template.
   - Update the docstring in the file using Edit

8. **Auto-SKIP tiers that genuinely don't exist:** if a `_brute` or `_better` method is a bare `pass` AND there is no meaningful distinct approach at that tier for this problem (e.g. the problem jumps straight from an O(n^2) brute force to the O(n) optimal, with no sensible intermediate), add a `# SKIP: <reason>` comment to that method explaining *why* the tier doesn't exist. This is the one case where you may touch an unimplemented method — you are marking intent, not writing a solution.
   - Place the SKIP exactly like: a `# SKIP: <reason>` comment as the first line(s) of the method body, above the `pass`.
   - Also reflect it in the docstring section (e.g. `#Better Approach:` → `SKIPPED — <reason>`), matching the existing SKIP style in other files.
   - Do this only when the tier is genuinely absent. If a real approach exists at that tier but the user simply hasn't written it yet, leave it as `pass` and do NOT reveal the approach.
   - The `_optimal` method is never auto-skipped — it always requires a real implementation.

9. **Remove the `# mypy: disable-error-code="empty-body"` header when it is no longer needed:** scaffold files carry this directive as line 1 so typed `pass` stubs don't fail mypy's `empty-body` check. Once the user has implemented the solution, remove that line — but ONLY when it is safe:
   - Safe to remove **only if** no method with a **non-`Optional` / non-`None` return type** still has a body of just `pass`. This explicitly includes `# SKIP` tiers (a skipped method is still `pass`) and any tier the user hasn't written yet.
   - So: if every `_brute`/`_better`/`_optimal` method (or every domain-class method, for implement-a-class files) that returns a non-`Optional` type now has real code, delete the header line. Otherwise leave it in place.
   - `Optional[...]`/`None`-returning `pass` stubs never trip `empty-body`, so they don't force the header to stay.
   - After deleting, run `mypy "<file>"` to confirm no `empty-body` error reappeared; if it did, restore the header line (a remaining `pass`/SKIP stub with a non-None return still needs it).

10. **Sync notes to that sheet's tracker:**
   - From repo root: `cd "<sheet>" && python3 sync_notes.py` (only if the sheet has `sync_notes.py` + `index.html`)
   - Do NOT edit `index.html` directly — let `sync_notes.py` do it. The PreToolUse hook blocks direct edits anyway.

11. **If the solution is optimal:**
    - Confirm it and congratulate
    - Fill in the `#KEY INSIGHT:` in the docstring

12. **Do NOT:**
    - Write or rewrite the solution code
    - Give away other approaches — only hints
    - Fill in notes for approaches the user hasn't implemented (auto-SKIP per step 8 is the only exception)
