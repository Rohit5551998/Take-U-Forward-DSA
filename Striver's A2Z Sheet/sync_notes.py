#!/usr/bin/env python3
"""Sync A2Z .py files into index.html DATA entries.

Unlike the SDE sheet's sync_notes.py, this script REBUILDS the DATA array
from the filesystem on every run (the A2Z sheet has ~455 problems across
17 steps and 60+ sub-steps — hand-curating DATA isn't practical).

DATA entry shape:
  { name: "<Title>", sub: "<sub-step>", d: "easy|medium|hard",
    q: "<question text>", n: "<docstring notes>", s: true }
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

STEPS_BY_NUM = {
    1: "Step 1 - Basics",
    2: "Step 2 - Sorting Techniques",
    3: "Step 3 - Arrays",
    4: "Step 4 - Binary Search",
    5: "Step 5 - Strings",
    6: "Step 6 - Linked Lists",
    7: "Step 7 - Recursion",
    8: "Step 8 - Bit Manipulation",
    9: "Step 9 - Stacks And Queues",
    10: "Step 10 - Sliding Window & Two Pointer Combined",
    11: "Step 11 - Heaps",
    12: "Step 12 - Greedy Algorithms",
    13: "Step 13 - Binary Trees",
    14: "Step 14 - Binary Search Trees",
    15: "Step 15 - Graphs",
    16: "Step 16 - Dynamic Programming",
    17: "Step 17 - Tries",
}

SHORT_WORDS = {"of", "a", "the", "in", "on", "and", "or", "for", "to", "with", "at", "by"}


def camel_to_title(filename: str) -> str:
    """setMatrixZeroes.py -> Set Matrix Zeroes"""
    s = filename.removesuffix(".py")
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    s = s.replace("&", " & ").replace("_", " ")
    s = re.sub(r"\s+", " ", s).strip()
    parts: list[str] = []
    for w in s.split():
        if w.lower() in SHORT_WORDS:
            parts.append(w.lower())
        else:
            parts.append(w[0].upper() + w[1:])
    if parts:
        parts[0] = parts[0][0].upper() + parts[0][1:]
    return " ".join(parts)


def infer_difficulty(sub_step: str) -> str:
    s = sub_step.lower()
    if "hard" in s:
        return "hard"
    if "medium" in s:
        return "medium"
    if "easy" in s:
        return "easy"
    return "medium"


def extract_docstring(py_file: Path) -> str | None:
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    return ast.get_docstring(tree) or None


def extract_question(py_file: Path) -> str | None:
    lines = py_file.read_text().splitlines()
    question_lines: list[str] = []
    started = False
    for line in lines:
        if line.startswith("# QUESTION:"):
            started = True
            question_lines.append(line.removeprefix("# QUESTION:").strip())
        elif started and line.startswith("#"):
            question_lines.append(line.removeprefix("#").removeprefix(" "))
        elif started:
            break
    return "\n".join(question_lines).strip() if question_lines else None


def _has_skip_comment(py_file: Path, func_name: str) -> bool:
    in_func = False
    for line in py_file.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith(f"def {func_name}("):
            in_func = True
            continue
        if in_func:
            if stripped.startswith("def ") or (
                stripped
                and not stripped.startswith("#")
                and not stripped.startswith("pass")
                and not stripped == ""
            ):
                break
            if stripped.upper().startswith("# SKIP"):
                return True
    return False


def is_fully_solved(py_file: Path) -> bool:
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    suffixes = ("_brute", "_better", "_optimal")
    found: dict[str, ast.FunctionDef] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for s in suffixes:
                if node.name.endswith(s):
                    found[s] = node
    if len(found) != 3:
        return False
    for suffix, node in found.items():
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
        if len(stmts) == 1 and isinstance(stmts[0], ast.Pass):
            if suffix == "_optimal":
                return False
            if not _has_skip_comment(py_file, node.name):
                return False
    return True


def discover() -> dict[int, list[dict[str, str | bool]]]:
    """Walk steps and collect problem entries grouped by step number."""
    by_step: dict[int, list[dict[str, str | bool]]] = {n: [] for n in STEPS_BY_NUM}
    for step_dir in sorted(ROOT.iterdir()):
        if not step_dir.is_dir() or step_dir.name.startswith("."):
            continue
        m = re.match(r"Step (\d+)", step_dir.name)
        if not m:
            continue
        step_n = int(m.group(1))
        if step_n not in STEPS_BY_NUM:
            continue
        # Files directly under step dir
        direct = sorted(step_dir.glob("*.py"))
        # Files under sub-step dirs
        nested: list[tuple[Path, str]] = []
        for sub in sorted(step_dir.iterdir()):
            if sub.is_dir() and not sub.name.startswith("."):
                for f in sorted(sub.glob("*.py")):
                    nested.append((f, sub.name))
        for f in direct:
            by_step[step_n].append(_entry(f, ""))
        for f, sub_name in nested:
            by_step[step_n].append(_entry(f, sub_name))
    return by_step


def _entry(py_file: Path, sub: str) -> dict[str, str | bool]:
    e: dict[str, str | bool] = {
        "name": camel_to_title(py_file.name),
        "sub": sub,
        "d": infer_difficulty(sub),
    }
    q = extract_question(py_file)
    if q:
        e["q"] = q
    n = extract_docstring(py_file)
    if n:
        e["n"] = n
    if is_fully_solved(py_file):
        e["s"] = True
    return e


def render_data(by_step: dict[int, list[dict[str, str | bool]]]) -> str:
    sections: list[str] = []
    for n, name in STEPS_BY_NUM.items():
        problems = by_step.get(n, [])
        problem_lines = []
        for p in problems:
            # Serialize fields in stable order: name, sub, d, q, n, s
            fields = [f'name: {json.dumps(p["name"])}']
            if p.get("sub"):
                fields.append(f'sub: {json.dumps(p["sub"])}')
            fields.append(f'd: {json.dumps(p["d"])}')
            if "q" in p:
                fields.append(f'q: {json.dumps(p["q"])}')
            if "n" in p:
                fields.append(f'n: {json.dumps(p["n"])}')
            if p.get("s"):
                fields.append("s: true")
            problem_lines.append("      { " + ", ".join(fields) + " }")
        body = ",\n".join(problem_lines)
        if body:
            body = "\n" + body + "\n    "
        sections.append(
            f'  {{\n    name: {json.dumps(name)}, problems: [{body}]\n  }}'
        )
    return "const DATA = [\n" + ",\n".join(sections) + "\n];"


DATA_BLOCK_RE = re.compile(r"const DATA = \[.*?\];", re.DOTALL)


def sync() -> int:
    by_step = discover()
    total = sum(len(v) for v in by_step.values())

    index_path = ROOT / "index.html"
    html = index_path.read_text()
    new_data = render_data(by_step)

    if not DATA_BLOCK_RE.search(html):
        raise RuntimeError("Could not find `const DATA = [...]` block in index.html")

    html = DATA_BLOCK_RE.sub(lambda _: new_data, html, count=1)
    index_path.write_text(html)
    return total


if __name__ == "__main__":
    count = sync()
    print(f"Synced {count} problem(s) into index.html")
