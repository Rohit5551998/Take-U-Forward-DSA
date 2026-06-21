#!/usr/bin/env python3
"""Sync docstrings and questions from .py solution files into index.html DATA entries."""

from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).parent


def extract_docstring(py_file: Path) -> str | None:
    """Extract the module-level docstring from a .py file."""
    source = py_file.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    docstring = ast.get_docstring(tree)
    return docstring if docstring else None


def filename_to_key(filename: str) -> str:
    """Convert filename to a normalized key for matching.

    e.g. 'setMatrixZeroes.py' -> 'setmatrixzeroes'
         'set-matrix-zeroes.py' -> 'setmatrixzeroes'
    """
    return re.sub(r"[^a-z0-9]", "", filename.removesuffix(".py").lower())


def problem_name_to_key(name: str) -> str:
    """Convert problem name to a normalized key for matching.

    e.g. 'Set Matrix Zeroes' -> 'setmatrixzeroes'
         'Pow(X,n)' -> 'powxn'
    """
    return re.sub(r"[^a-z0-9]", "", name.lower())


def escape_for_js(text: str) -> str:
    """Escape a string for embedding in a JS string literal."""
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("\n", "\\n")
    text = text.replace("\r", "")
    return text


def _has_skip_comment(py_file: Path, func_name: str) -> bool:
    """Check if a function has a # SKIP comment in its source."""
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
    """Check if all 3 approaches (_brute, _better, _optimal) are implemented.

    A function counts as done if it has real code, or has a '# SKIP: <reason>'
    comment. The _optimal function is always required to have real code.
    """
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
        # Skip docstring if present
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
            # _optimal is always required
            if suffix == "_optimal":
                return False
            # Allow skip if # SKIP comment is present
            if not _has_skip_comment(py_file, node.name):
                return False
    return True


def extract_question(py_file: Path) -> str | None:
    """Extract the # QUESTION: comment block from the top of a .py file."""
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
    if not question_lines:
        return None
    return "\n".join(question_lines).strip()


def extract_question_title(py_file: Path) -> str | None:
    """Return just the first line of the `# QUESTION:` block (the canonical title)."""
    for line in py_file.read_text().splitlines():
        if line.startswith("# QUESTION:"):
            return line.removeprefix("# QUESTION:").strip() or None
    return None


def collect_solutions() -> tuple[dict[str, str], set[str], dict[str, str]]:
    """Collect docstrings, solved status, and questions from .py files.

    Walks one level deep — `<Day Directory>/<problem>.py`.
    """
    notes: dict[str, str] = {}
    solved: set[str] = set()
    questions: dict[str, str] = {}
    for py_file in ROOT.glob("*/*.py"):
        # Skip dotfiles / cache directories
        if py_file.parent.name.startswith("."):
            continue
        # Prefer matching by the `# QUESTION:` block title (verbatim from DATA),
        # fall back to filename — handles cases like "3 Sum" -> threeSum.py
        title = extract_question_title(py_file)
        key = problem_name_to_key(title) if title else filename_to_key(py_file.name)
        docstring = extract_docstring(py_file)
        if docstring:
            notes[key] = docstring
        if is_fully_solved(py_file):
            solved.add(key)
        question = extract_question(py_file)
        if question:
            questions[key] = question
    return notes, solved, questions


def _find_entry_end(html: str, start: int) -> int:
    """Given `start` at the `{` of an entry, return the index just past the
    matching `}`. Tracks string state so braces inside "..." don't count."""
    depth = 0
    i = start
    in_string = False
    escape = False
    while i < len(html):
        c = html[i]
        if in_string:
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError("Unbalanced braces starting at " + str(start))


def _strip_existing_fields(rest: str) -> str:
    """Strip `, q: "..."`, `, n: "..."`, `, s: true` from an entry's inner
    text, quote-state-aware (so embedded { } don't confuse anything; we
    rely on the alternation [^"\\]|\\. for escape handling)."""
    for field in ("q", "n"):
        rest = re.sub(
            rf',\s*{field}:\s*"(?:[^"\\]|\\.)*"',
            "",
            rest,
        )
    rest = re.sub(r",\s*s:\s*true", "", rest)
    return rest


def sync() -> int:
    """Sync docstrings and solved status into index.html. Returns count of updated entries."""
    notes, solved, questions = collect_solutions()
    if not notes and not solved and not questions:
        return 0

    index_path = ROOT / "index.html"
    html = index_path.read_text()

    # Walk all entries with a quote-aware parser. Patterns like `{ name: "X", d: "Y", q: "{a,b}" }`
    # with embedded braces in q used to break the previous regex-only approach.
    entry_head = re.compile(r'\{\s*name:\s*"((?:[^"\\]|\\.)*)"')
    pieces: list[str] = []
    cursor = 0
    updated = 0
    for m in entry_head.finditer(html):
        start = m.start()
        try:
            end = _find_entry_end(html, start)
        except ValueError:
            continue
        # Suffix is whitespace + `,` or `]` if present (kept verbatim)
        suffix_m = re.match(r"\s*[,\]]", html[end:])
        suffix = suffix_m.group() if suffix_m else ""
        whole = html[start:end]
        name = m.group(1)
        key = problem_name_to_key(name)

        if key not in notes and key not in solved and key not in questions:
            # Leave as-is
            continue

        # Inner: text between the opening `{` and the closing `}` (exclusive).
        # The opening `{` is at index 0 of `whole`; closing `}` at -1.
        inner = whole[1:-1]
        # Split off the name field at the start (we already have name)
        inner_after_name = inner[m.end() - m.start() - 1 :]  # everything after `name: "X"`
        rest_clean = _strip_existing_fields(inner_after_name)

        extras = ""
        if key in questions:
            extras += ', q: "' + escape_for_js(questions[key]) + '"'
        if key in notes:
            extras += ', n: "' + escape_for_js(notes[key]) + '"'
        if key in solved:
            extras += ", s: true"

        new_whole = "{ name: \"" + name + "\"" + rest_clean + extras + " }"
        # Emit everything before this entry, then the rewritten entry + suffix
        pieces.append(html[cursor:start])
        pieces.append(new_whole)
        pieces.append(suffix)
        cursor = end + len(suffix)
        updated += 1

    pieces.append(html[cursor:])
    index_path.write_text("".join(pieces))
    return updated


if __name__ == "__main__":
    count = sync()
    print(f"Synced {count} problem note(s) to index.html")
