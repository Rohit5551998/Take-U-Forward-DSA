# Take U Forward — DSA

My Python solutions and progress trackers for the [takeuforward.org](https://takeuforward.org) DSA sheets.

## 📊 Live progress

**→ https://rohit5551998.github.io/Take-U-Forward-DSA/**

The root [`index.html`](index.html) is a landing page linking to a self-contained tracker per sheet. Each tracker stores your progress in the browser's `localStorage` (a distinct key per sheet, so they don't collide) and shows the problem statement, notes, and time/space complexity synced from each solution file.

| Sheet | Scope | Tracker |
|-------|-------|---------|
| **Striver's SDE Sheet** | Interview-focused — 191 problems across 27 topics | [open](Striver's%20SDE%20Sheet/index.html) |
| **Striver's A2Z Sheet** | Comprehensive — ~455 problems across 17 steps | [open](Striver's%20A2Z%20Sheet/index.html) |

> **Enabling GitHub Pages:** in the repo's **Settings → Pages**, set the source to **GitHub Actions**. The included [`deploy-pages.yml`](.github/workflows/deploy-pages.yml) workflow then redeploys the site on **every push to `master`** — including changes inside either sheet directory (solving a problem, re-running `sync_notes.py`, etc.) — so the live site always reflects the latest progress. You can also trigger it manually from the **Actions** tab.

## 🗂 Repository layout

```
.
├── index.html                 # landing page (links to both trackers)
├── Striver's SDE Sheet/
│   ├── index.html             # SDE progress tracker
│   ├── sync_notes.py          # syncs solution docstrings → tracker
│   └── <Topic>/<problem>.py   # solutions
└── Striver's A2Z Sheet/
    ├── index.html             # A2Z progress tracker
    ├── sync_notes.py
    └── <Step>/<Category>/<problem>.py
```

## ✍️ Solution conventions

- **Python**, with type annotations on every method.
- Each solution file defines a `class Solution` (LeetCode-style). Approaches and shared helpers are methods (helpers invoked via `self.<helper>(...)`), and a trailing `if __name__ == "__main__":` block runs sample input.
- Method naming differs by sheet: the SDE sheet uses `<name>_brute` / `<name>_better` / `<name>_optimal`; the A2Z sheet uses `findSolution` / `findSolution1` / `findSolution2` … (brute → optimal).
- Every file starts with a `# QUESTION:` block (the source of truth for problem text) followed by a multi-approach docstring with `TC -> O(), SC -> O()` per approach. Use `# SKIP: <reason>` for a tier with no distinct approach.

## 🛠 Tooling

```bash
ruff format .          # format
ruff check . --fix     # lint + autofix
mypy .                 # type check

# from inside a sheet directory:
python3 sync_notes.py  # sync solution docstrings/questions into that sheet's tracker
open index.html        # open that sheet's tracker
```
