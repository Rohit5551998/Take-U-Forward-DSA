---
name: progress
description: Show Striver solve progress across sheets (SDE / A2Z / others) — problems solved per day, totals, and what's in progress
disable-model-invocation: true
---

# Progress

Show a summary of solving progress across all Striver sheet directories under the current repo.

## Arguments
- `[sheet]` (optional): Restrict to a single sheet, e.g., `"Striver's SDE Sheet"`. If omitted, scans every top-level `Striver's *` directory.

## Workflow

1. For each target sheet, run that sheet's `sync_notes.py` (if it exists) to refresh its tracker:
   ```bash
   for sheet in <targets>; do
     [ -f "$sheet/sync_notes.py" ] && (cd "$sheet" && python3 sync_notes.py)
   done
   ```

2. Run a Python script from the repo root to analyze all `.py` solution files and report:

```python
import ast
from pathlib import Path

ROOT = Path(".")
# A sheet is a top-level directory starting with "Striver"
sheet_dirs = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("Striver")]

for sheet in sheet_dirs:
    days = {}
    for py_file in sorted(sheet.glob("*/*.py")):
        if py_file.parent.name.startswith("."):
            continue
        day = py_file.parent.name
        days.setdefault(day, {"total": 0, "solved": 0, "partial": 0, "files": []})

        days[day]["total"] += 1
        source = py_file.read_text()
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue

        suffixes = ("_brute", "_better", "_optimal")
        implemented = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for s in suffixes:
                    if node.name.endswith(s):
                        body = node.body
                        stmts = (
                            body[1:]
                            if (
                                body
                                and isinstance(body[0], ast.Expr)
                                and isinstance(body[0].value, ast.Constant)
                                and isinstance(body[0].value.value, str)
                            )
                            else body
                        )
                        if not (len(stmts) == 1 and isinstance(stmts[0], ast.Pass)):
                            implemented += 1

        if implemented == 3:
            days[day]["solved"] += 1
        elif implemented > 0:
            days[day]["partial"] += 1
            days[day]["files"].append(f"  {py_file.name} ({implemented}/3)")

    if not days:
        continue
    total_solved = sum(d["solved"] for d in days.values())
    total_partial = sum(d["partial"] for d in days.values())
    total_files = sum(d["total"] for d in days.values())
    print(f"\n## {sheet.name}: {total_solved}/{total_files} solved, {total_partial} in progress")
    for name, info in days.items():
        status = f"{info['solved']}/{info['total']} solved"
        if info["partial"]:
            status += f", {info['partial']} in progress"
        print(f"- **{name}**: {status}")
        for f in info["files"]:
            print(f)
```

3. Display the output to the user in a clean format.
