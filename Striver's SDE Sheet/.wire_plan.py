#!/usr/bin/env python3
"""One-shot: wire the 12-week study plan into index.html as a
Today / Backlog / Extras panel above the topic sections.

Idempotent: re-running detects existing markers and replaces just the
plan section without duplicating.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"

PLAN_START = "2026-06-22"  # Monday — Week 1 Day 1

# (week, day, [problem-names-as-they-appear-in-DATA])
PLAN: list[tuple[int, str, list[str]]] = [
    # ===== Month 1 (60) =====
    # Week 1 (15)
    (1, "Mon", ["Set Matrix Zeroes", "Pascal's Triangle I"]),
    (1, "Wed", ["Next Permutation", "Kadane's Algorithm"]),
    (
        1,
        "Thu",
        [
            "Rotate matrix by 90 degrees",
            "Merge Overlapping Subintervals",
            "Merge two sorted arrays without extra space",
        ],
    ),
    (1, "Fri", ["Sort an array of 0's 1's and 2's", "Stock Buy and Sell"]),
    (
        1,
        "Sat",
        [
            "Find the Duplicate Number",
            "Find the repeating and missing number",
            "Inversion of Array (Pre-req: Merge Sort)",
        ],
    ),
    (1, "Sun", ["Search in a 2D matrix", "Pow(x, n)", "Majority Element-I"]),
    # Week 2 (15)
    (2, "Mon", ["Majority Element-II", "Grid unique paths"]),
    (2, "Tue", ["Reverse a LL", "Find Middle of Linked List", "Merge two Sorted Lists"]),
    (2, "Wed", ["Reverse Pairs", "Two Sum"]),
    (2, "Fri", ["4 Sum", "Longest Consecutive Sequence in an Array"]),
    (
        2,
        "Sat",
        [
            "Largest Subarray with K sum",
            "Count subarrays with given xor K",
            "Longest Substring Without Repeating Characters",
        ],
    ),
    (
        2,
        "Sun",
        [
            "Remove Nth node from the back of the LL",
            "Add two numbers as LinkedList",
            "Delete Node in a Linked List O(1)",
        ],
    ),
    # Week 3 (15)
    (3, "Mon", ["Find the intersection point of Y LL", "Detect a loop in LL"]),
    (3, "Wed", ["Find the starting point in LL", "Reverse LL in group of given size K"]),
    (3, "Fri", ["Check if LL is palindrome or not", "Flattening of LL"]),
    (3, "Sat", ["Rotate a LL", "Clone a LL with random and next pointer", "3 Sum"]),
    (
        3,
        "Sun",
        [
            "Trapping Rainwater",
            "Remove duplicates from sorted array",
            "Maximum Consecutive Ones",
            "N meetings in one room",
            "Minimum number of platforms required for a railway",
            "Job sequencing Problem",
        ],
    ),
    # Week 4 (15)
    (4, "Mon", ["Fractional Knapsack", "Minimum coins", "Assign Cookies"]),
    (4, "Wed", ["Subset Sums", "Subsets II"]),
    (4, "Fri", ["Combination Sum", "Combination Sum II"]),
    (4, "Sat", ["Palindrome partitioning", "Permutation Sequence", "Permutations of a String"]),
    (
        4,
        "Sun",
        [
            "N Queen",
            "Sudoku Solver",
            "M Coloring Problem",
            "Rat in a Maze",
            "Word Break (print all ways)",
        ],
    ),
    # ===== Month 2 (63) =====
    # Week 5 (14)
    (5, "Mon", ["The N-th root of an integer", "Matrix Median"]),
    (
        5,
        "Wed",
        [
            "Single element in sorted array",
            "Search element in a sorted and rotated array/ find pivot where it is rotated",
        ],
    ),
    (5, "Fri", ["Median of 2 sorted arrays", "Kth element of 2 sorted arrays"]),
    (
        5,
        "Sat",
        [
            "Allocate Minimum Number of Pages",
            "Aggressive Cows",
            "Implement Max Heap",
            "K-th Largest element in an array",
        ],
    ),
    (
        5,
        "Sun",
        [
            "Maximum Sum Combination",
            "Find Median from Data Stream",
            "Merge K Sorted Arrays",
            "Top K Frequent Elements",
        ],
    ),
    # Week 6 (17)
    (
        6,
        "Mon",
        [
            "Implement Stack using Arrays",
            "Implement Queue using Arrays",
            "Implement Stack using Queue (using single queue)",
        ],
    ),
    (6, "Wed", ["Implement Queue using Stack", "Balanced Paranthesis"]),
    (6, "Fri", ["Next Greater Element", "Sort a Stack"]),
    (
        6,
        "Sat",
        ["Next Smaller Element", "LRU Cache", "LFU Cache", "Largest rectangle in a histogram"],
    ),
    (
        6,
        "Sun",
        [
            "Sliding Window Maximum",
            "Implement Min Stack",
            "Rotten Oranges",
            "Stock span problem",
            "Maximum of Minimums for Every Window Size",
            "Celebrity Problem",
        ],
    ),
    # Week 7 (16)
    (7, "Mon", ["Reverse every word in a string", "Longest Palindrome in a string"]),
    (7, "Wed", ["Roman to Integer", "Implement ATOI/STRSTR"]),
    (7, "Fri", ["Longest Common Prefix", "Rabin Karp Algorithm"]),
    (
        7,
        "Sat",
        [
            "Z function",
            "KMP Algorithm or LPS array",
            "Minimum insertions to make string palindrome",
            "Valid Anagram",
        ],
    ),
    (
        7,
        "Sun",
        [
            "Count and say",
            "Compare version numbers",
            "Inorder Traversal",
            "Preorder Traversal",
            "Postorder Traversal",
            "Morris Inorder Traversal",
        ],
    ),
    # Week 8 (16)
    (8, "Mon", ["Morris Preorder Traversal", "Right/Left View of BT"]),
    (8, "Wed", ["Bottom view of BT", "Top View of BT"]),
    (8, "Fri", ["Pre, Post, Inorder in one traversal", "Vertical Order Traversal"]),
    (
        8,
        "Sat",
        [
            "Print root to leaf path in BT",
            "Maximum Width of BT",
            "Level Order Traversal",
            "Maximum Depth in BT",
        ],
    ),
    (
        8,
        "Sun",
        [
            "Diameter of Binary Tree",
            "Check for balanced binary tree",
            "LCA in BT",
            "Check if two trees are identical or not",
            "Zig Zag or Spiral Traversal",
            "Boundary Traversal",
        ],
    ),
    # ===== Month 3 (68) =====
    # Week 9 (14)
    (9, "Mon", ["Maximum path sum", "Construct a BT from Preorder and Inorder"]),
    (9, "Wed", ["Construct a BT from Postorder and Inorder", "Symmetric Binary Tree"]),
    (9, "Fri", ["Flatten Binary Tree to Linked List", "Check for symmetrical BTs"]),
    (
        9,
        "Sat",
        [
            "Children Sum Property in Binary Tree",
            "Populating Next Right Pointers in Each Node",
            "Search in BST",
        ],
    ),
    (
        9,
        "Sun",
        [
            "Construct BST from given keys",
            "Construct a BST from a preorder traversal",
            "Check if a tree is a BST or not",
            "LCA in BST",
            "Inorder successor and predecessor in BST",
        ],
    ),
    # Week 10 (18)
    (10, "Mon", ["Floor in a BST", "Ceil in a BST"]),
    (10, "Wed", ["Find K-th smallest element in BST", "Kth Smallest and Largest element in BST"]),
    (10, "Fri", ["Two sum in BST", "BST iterator"]),
    (
        10,
        "Sat",
        [
            "Size of the largest BST in a Binary Tree",
            "Serialize and De-serialize BT",
            "Binary Tree to Doubly Linked List",
            "Find Median in a Stream",
            "Kth largest element in a stream of running integers",
        ],
    ),
    (
        10,
        "Sun",
        [
            "Distinct Numbers in Each Subarray",
            "K-th largest element in an unsorted array.",
            "Flood-fill Algorithm",
            "Clone Graph",
            "DFS",
            "Traversal Techniques",
            "Detect A cycle in Undirected Graph using BFS",
        ],
    ),
    # Week 11 (18)
    (
        11,
        "Mon",
        [
            "Detect A cycle in Undirected Graph using DFS",
            "Detect A cycle in a Directed Graph using DFS",
        ],
    ),
    (11, "Wed", ["Detect A cycle in a Directed Graph using BFS", "Topological Sort BFS"]),
    (11, "Fri", ["Topological Sort DFS", "Number of islands(Do in Grid and Graph Both)"]),
    (
        11,
        "Sat",
        [
            "Bipartite graph",
            "Bipartite Check using DFS",
            "Strongly Connected Component(using Kosaraju's algo)",
            "Dijkstra's algorithm",
            "Bellman ford algorithm",
        ],
    ),
    (
        11,
        "Sun",
        [
            "Floyd Warshall Algorithm",
            "MST using Prim's Algo",
            "MST using Kruskal's Algo",
            "Max Product Subarray",
            "Longest Increasing Subsequence",
            "Longest common subsequence",
            "0 and 1 Knapsack",
        ],
    ),
    # Week 12 (18)
    (12, "Mon", ["Edit distance", "Maximum Sum Increasing Subsequence"]),
    (
        12,
        "Wed",
        [
            "Matrix chain multiplication",
            "Minimum sum path in the matrix, (count paths and similar type do, also backtrack to find the Minimum path)",
        ],
    ),
    (12, "Fri", ["Coin change II", "Subset sum equals to target"]),
    (
        12,
        "Sat",
        [
            "Rod cutting problem",
            "Super Egg Drop",
            "Word Break",
            "Palindrome Partitioning (MCM Variation)",
            "Maximum Profit in Job Scheduling",
        ],
    ),
    (
        12,
        "Sun",
        [
            "Trie Implementation and Operations",
            "Trie Implementation and Advanced Operations",
            "Longest Word with All Prefixes",
            "Number of distinct substrings in a string",
            "Power Set (this is very important)",
            "Maximum XOR of two numbers in an array",
            "Maximum Xor with an element from an array",
        ],
    ),
]

# Validate counts
TOTAL = sum(len(p[2]) for p in PLAN)
assert TOTAL == 191, f"Plan covers {TOTAL} problems, expected 191"

# ---- Markers used to make the script idempotent ----
START_MARK = "<!-- PLAN_PANEL_START -->"
END_MARK = "<!-- PLAN_PANEL_END -->"
CSS_START = "/* PLAN_PANEL_CSS_START */"
CSS_END = "/* PLAN_PANEL_CSS_END */"
JS_START = "/* PLAN_PANEL_JS_START */"
JS_END = "/* PLAN_PANEL_JS_END */"


CSS = f"""{CSS_START}
  .plan-panel {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 24px;
  }}
  .plan-panel h2 {{
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}
  .plan-panel .plan-meta {{
    font-size: 12px;
    color: var(--text-dim);
    font-weight: 500;
  }}
  .plan-tabs {{
    display: flex;
    gap: 4px;
    margin: 14px 0 10px;
    flex-wrap: wrap;
  }}
  .plan-tab {{
    padding: 6px 12px;
    border-radius: 8px;
    background: transparent;
    color: var(--text-dim);
    border: 1px solid var(--border);
    cursor: pointer;
    font-size: 12px;
    font-family: inherit;
    transition: all 0.2s;
  }}
  .plan-tab:hover {{ color: var(--text); border-color: var(--accent); }}
  .plan-tab.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}
  .plan-tab .badge {{
    display: inline-block;
    background: rgba(255, 255, 255, 0.18);
    padding: 0 6px;
    border-radius: 999px;
    margin-left: 4px;
    font-weight: 700;
    font-size: 11px;
  }}
  .plan-tab:not(.active) .badge {{ background: var(--border); color: var(--text); }}
  .plan-tab.danger .badge {{ background: var(--orange-dim); color: var(--orange); }}
  .plan-tab.danger.active {{ background: var(--orange); color: #000; }}
  .plan-tab.danger.active .badge {{ background: rgba(0,0,0,0.2); color: #000; }}
  .plan-tab.bonus .badge {{ background: var(--accent-glow); color: var(--accent); }}
  .plan-tab.bonus.active {{ background: var(--accent); color: #fff; }}

  .plan-list {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .plan-empty {{
    color: var(--text-dim);
    font-style: italic;
    font-size: 13px;
    padding: 10px 0;
  }}
  .plan-day-group {{
    margin-top: 12px;
    padding-top: 10px;
    border-top: 1px dashed var(--border);
  }}
  .plan-day-group:first-child {{ margin-top: 0; padding-top: 0; border-top: none; }}
  .plan-day-label {{
    font-size: 11px;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    margin-bottom: 6px;
  }}
  .plan-day-label .wk-pill {{
    background: var(--accent-glow);
    color: var(--accent);
    padding: 1px 7px;
    border-radius: 999px;
    margin-right: 6px;
    font-weight: 700;
  }}
  .plan-item {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 13px;
    cursor: pointer;
    transition: background 0.15s;
  }}
  .plan-item:hover {{ background: var(--surface-hover); }}
  .plan-item.done {{ opacity: 0.55; }}
  .plan-item.done .plan-item-name {{ text-decoration: line-through; }}
  .plan-item-check {{
    width: 16px;
    height: 16px;
    min-width: 16px;
    border: 2px solid var(--border);
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
  }}
  .plan-item.done .plan-item-check {{
    background: var(--green);
    border-color: var(--green);
    color: #000;
  }}
  .plan-item-name {{ flex: 1; }}
  .plan-item-tag {{
    font-size: 10px;
    color: var(--text-dim);
  }}

  /* Full Plan tab — collapsible week groups */
  .plan-week {{
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 8px;
    overflow: hidden;
  }}
  .plan-week.current {{ border-color: var(--accent); }}
  .plan-week-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    cursor: pointer;
    user-select: none;
    background: var(--bg);
    transition: background 0.15s;
  }}
  .plan-week-header:hover {{ background: var(--surface-hover); }}
  .plan-week.current .plan-week-header {{ background: var(--accent-glow); }}
  .plan-week-chevron {{
    font-size: 10px;
    color: var(--text-dim);
    transition: transform 0.15s;
  }}
  .plan-week-header.open .plan-week-chevron {{ transform: rotate(90deg); }}
  .plan-week-label {{
    font-size: 13px;
    font-weight: 600;
    flex: 1;
  }}
  .plan-week-tag {{
    font-size: 10px;
    background: var(--accent);
    color: #fff;
    padding: 1px 6px;
    border-radius: 999px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .plan-week-stats {{
    font-size: 12px;
    color: var(--text-dim);
    font-weight: 600;
  }}
  .plan-week-body {{
    padding: 8px 14px 14px;
    background: var(--surface);
  }}
{CSS_END}"""


HTML_PANEL = f"""  {START_MARK}
  <div class="plan-panel" id="plan-panel">
    <h2><span id="plan-title">Plan</span><span class="plan-meta" id="plan-meta"></span></h2>
    <div class="plan-tabs" id="plan-tabs"></div>
    <div class="plan-list" id="plan-list"></div>
  </div>
  {END_MARK}"""


# Build a JS-side plan structure
js_plan = json.dumps([{"wk": w, "dy": d, "ps": ps} for (w, d, ps) in PLAN])

JS = f"""
{JS_START}
const PLAN = {js_plan};
const PLAN_START = "{PLAN_START}";  // YYYY-MM-DD (a Monday)

// Day offsets within a week (Mon=0)
const DAY_OFFSET = {{ Mon: 0, Tue: 1, Wed: 2, Thu: 3, Fri: 4, Sat: 5, Sun: 6 }};
const DOW = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

function parseDate(s) {{
  const [y, m, d] = s.split("-").map(Number);
  return new Date(y, m - 1, d);
}}
function ymd(dt) {{
  return dt.getFullYear() + "-" + String(dt.getMonth() + 1).padStart(2, "0") + "-" + String(dt.getDate()).padStart(2, "0");
}}
function diffDays(a, b) {{
  return Math.floor((a - b) / 86400000);
}}
function plannedDate(wk, dy) {{
  const start = parseDate(PLAN_START);
  start.setDate(start.getDate() + (wk - 1) * 7 + DAY_OFFSET[dy]);
  return start;
}}
function fmtDate(dt) {{
  return DOW[dt.getDay()] + ", " + dt.toLocaleString("en-US", {{ month: "short", day: "numeric" }});
}}

// Build name -> {{si, pi}} lookup against DATA
function buildPlanLookup() {{
  const lookup = {{}};
  DATA.forEach((sec, si) => {{
    sec.problems.forEach((p, pi) => {{
      lookup[p.name] = {{ si, pi }};
    }});
  }});
  return lookup;
}}
const PLAN_LOOKUP = buildPlanLookup();

// Tag every PLAN row: planned ISO date + array of {{name, si, pi}} resolved entries
const PLAN_ROWS = PLAN.map(row => {{
  const dt = plannedDate(row.wk, row.dy);
  return {{
    wk: row.wk,
    dy: row.dy,
    iso: ymd(dt),
    dt: dt,
    items: row.ps.map(name => ({{
      name,
      loc: PLAN_LOOKUP[name] || null,
    }}))
  }};
}});

// All PLANNED problem names -> the row they came from
const NAME_TO_ROW = {{}};
PLAN_ROWS.forEach(r => r.items.forEach(it => NAME_TO_ROW[it.name] = r));

function isSolved(loc) {{
  if (!loc) return false;
  const key = getKey(loc.si, loc.pi);
  const p = DATA[loc.si].problems[loc.pi];
  return key in state ? !!state[key] : !!p.s;
}}

function categorizePlan() {{
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const todayISO = ymd(today);

  const past = [], todays = [], future = [];
  PLAN_ROWS.forEach(row => {{
    if (row.iso < todayISO) past.push(row);
    else if (row.iso === todayISO) todays.push(row);
    else future.push(row);
  }});

  // Backlog = past planned items not yet solved
  const backlog = past.flatMap(row =>
    row.items.filter(it => !isSolved(it.loc)).map(it => ({{ row, item: it }}))
  );

  // Today's items
  const todayItems = todays.flatMap(row =>
    row.items.map(it => ({{ row, item: it }}))
  );

  // Extras: solved problems that are NOT in past/today plan
  //   - solved AND scheduled in future
  //   - solved AND not in PLAN at all
  const extras = [];
  DATA.forEach((sec, si) => {{
    sec.problems.forEach((p, pi) => {{
      if (!isSolved({{si, pi}})) return;
      const row = NAME_TO_ROW[p.name];
      if (!row) {{
        extras.push({{ row: null, item: {{ name: p.name, loc: {{si, pi}} }} }});
      }} else if (row.iso > todayISO) {{
        extras.push({{ row, item: {{ name: p.name, loc: {{si, pi}} }} }});
      }}
    }});
  }});

  // Find next non-empty future day for "Upcoming" preview
  const upcoming = future[0] || null;
  return {{ today, todayISO, past, todayRows: todays, future, backlog, todayItems, extras, upcoming }};
}}

let planTab = null;  // null = auto-pick on first render

function pickInitialTab(cat) {{
  if (cat.todayRows.length > 0) return "today";
  if (cat.backlog.length > 0) return "backlog";
  if (cat.upcoming) return "upcoming";
  return "today";
}}

function renderPlanItem(item, row) {{
  const div = document.createElement("div");
  div.className = "plan-item" + (isSolved(item.loc) ? " done" : "");
  const check = document.createElement("div");
  check.className = "plan-item-check";
  check.textContent = isSolved(item.loc) ? "✓" : "";
  div.appendChild(check);
  const name = document.createElement("div");
  name.className = "plan-item-name";
  name.textContent = item.name;
  div.appendChild(name);
  if (row) {{
    const tag = document.createElement("div");
    tag.className = "plan-item-tag";
    tag.textContent = `W${{row.wk}} ${{row.dy}}`;
    div.appendChild(tag);
  }} else {{
    const tag = document.createElement("div");
    tag.className = "plan-item-tag";
    tag.textContent = "off-plan";
    div.appendChild(tag);
  }}
  if (item.loc) {{
    div.addEventListener("click", () => {{
      const checked = isSolved(item.loc);
      toggleProblem(item.loc.si, item.loc.pi, !checked);
    }});
  }}
  return div;
}}

function renderGroupedByDay(entries) {{
  // entries: [{{ row, item }}, ...]; group by row
  const list = document.getElementById("plan-list");
  list.textContent = "";
  if (!entries.length) {{
    const empty = document.createElement("div");
    empty.className = "plan-empty";
    empty.textContent = "Nothing here — you're all caught up.";
    list.appendChild(empty);
    return;
  }}
  const groups = new Map();
  entries.forEach(e => {{
    const key = e.row ? `${{e.row.wk}}|${{e.row.dy}}` : "off-plan";
    if (!groups.has(key)) groups.set(key, {{ row: e.row, items: [] }});
    groups.get(key).items.push(e.item);
  }});
  groups.forEach(g => {{
    const wrap = document.createElement("div");
    wrap.className = "plan-day-group";
    const label = document.createElement("div");
    label.className = "plan-day-label";
    if (g.row) {{
      const pill = document.createElement("span");
      pill.className = "wk-pill";
      pill.textContent = "W" + g.row.wk;
      label.appendChild(pill);
      label.appendChild(document.createTextNode(g.row.dy + " · " + fmtDate(g.row.dt)));
    }} else {{
      label.textContent = "Off-plan / not in 12-week schedule";
    }}
    wrap.appendChild(label);
    g.items.forEach(it => wrap.appendChild(renderPlanItem(it, g.row)));
    list.appendChild(wrap);
  }});
}}

const fullPlanOpenWeeks = new Set();

function renderFullPlan(cat) {{
  const list = document.getElementById("plan-list");
  list.textContent = "";
  // Group PLAN_ROWS by week number
  const byWeek = new Map();
  PLAN_ROWS.forEach(r => {{
    if (!byWeek.has(r.wk)) byWeek.set(r.wk, []);
    byWeek.get(r.wk).push(r);
  }});
  // Determine current week
  const todayISO = cat.todayISO;
  let curWk = null;
  for (const r of PLAN_ROWS) {{
    if (r.iso >= todayISO) {{ curWk = r.wk; break; }}
  }}
  // Auto-open current week on first render
  if (curWk && fullPlanOpenWeeks.size === 0) fullPlanOpenWeeks.add(curWk);

  const totalAll = PLAN_ROWS.reduce((n, r) => n + r.items.length, 0);
  const done = PLAN_ROWS.reduce(
    (n, r) => n + r.items.filter(it => isSolved(it.loc)).length, 0
  );
  const summary = document.createElement("div");
  summary.className = "plan-empty";
  summary.style.color = "var(--text-dim)";
  summary.style.marginBottom = "10px";
  summary.textContent = `12-week plan · ${{done}} / ${{totalAll}} done`;
  list.appendChild(summary);

  Array.from(byWeek.keys()).sort((a, b) => a - b).forEach(wk => {{
    const rows = byWeek.get(wk);
    const wkTotal = rows.reduce((n, r) => n + r.items.length, 0);
    const wkDone = rows.reduce(
      (n, r) => n + r.items.filter(it => isSolved(it.loc)).length, 0
    );
    const isCurrent = wk === curWk;
    const isOpen = fullPlanOpenWeeks.has(wk);

    const weekWrap = document.createElement("div");
    weekWrap.className = "plan-week" + (isCurrent ? " current" : "");

    const header = document.createElement("div");
    header.className = "plan-week-header" + (isOpen ? " open" : "");
    const chevron = document.createElement("span");
    chevron.className = "plan-week-chevron";
    chevron.textContent = "▶";
    const wkLabel = document.createElement("span");
    wkLabel.className = "plan-week-label";
    wkLabel.textContent = `Week ${{wk}}`;
    if (isCurrent) {{
      const tag = document.createElement("span");
      tag.className = "plan-week-tag";
      tag.textContent = "current";
      wkLabel.appendChild(document.createTextNode(" "));
      wkLabel.appendChild(tag);
    }}
    const wkStats = document.createElement("span");
    wkStats.className = "plan-week-stats";
    wkStats.textContent = `${{wkDone}} / ${{wkTotal}}`;
    header.appendChild(chevron);
    header.appendChild(wkLabel);
    header.appendChild(wkStats);
    header.addEventListener("click", () => {{
      if (fullPlanOpenWeeks.has(wk)) fullPlanOpenWeeks.delete(wk);
      else fullPlanOpenWeeks.add(wk);
      renderPlanPanel();
    }});
    weekWrap.appendChild(header);

    if (isOpen) {{
      const body = document.createElement("div");
      body.className = "plan-week-body";
      rows.forEach(r => {{
        const dayGroup = document.createElement("div");
        dayGroup.className = "plan-day-group";
        const dayLabel = document.createElement("div");
        dayLabel.className = "plan-day-label";
        dayLabel.textContent = `${{r.dy}} · ${{fmtDate(r.dt)}}`;
        dayGroup.appendChild(dayLabel);
        r.items.forEach(it => dayGroup.appendChild(renderPlanItem(it, r)));
        body.appendChild(dayGroup);
      }});
      weekWrap.appendChild(body);
    }}
    list.appendChild(weekWrap);
  }});
}}

function renderPlanPanel() {{
  const cat = categorizePlan();
  const title = document.getElementById("plan-title");
  const meta = document.getElementById("plan-meta");
  const tabsEl = document.getElementById("plan-tabs");

  // Title + meta
  const todayDateStr = fmtDate(cat.today);
  const startDt = parseDate(PLAN_START);
  if (cat.todayISO < PLAN_START) {{
    const dleft = diffDays(startDt, cat.today);
    title.textContent = "Plan";
    meta.textContent = `${{todayDateStr}} · starts ${{fmtDate(startDt)}} (in ${{dleft}} day${{dleft === 1 ? "" : "s"}})`;
  }} else if (cat.todayRows.length) {{
    const r = cat.todayRows[0];
    title.textContent = `Plan — Week ${{r.wk}} · ${{r.dy}}`;
    meta.textContent = todayDateStr;
  }} else {{
    title.textContent = "Plan";
    meta.textContent = `${{todayDateStr}} · rest day (System Design / no DSA)`;
  }}

  if (planTab === null) planTab = pickInitialTab(cat);

  // Tabs
  const tabs = [
    {{ id: "today",    label: "Today",    count: cat.todayItems.length, danger: false, bonus: false }},
    {{ id: "backlog",  label: "Backlog",  count: cat.backlog.length,    danger: cat.backlog.length > 0, bonus: false }},
    {{ id: "upcoming", label: "Upcoming", count: cat.upcoming ? cat.upcoming.items.length : 0, danger: false, bonus: false }},
    {{ id: "extras",   label: "Extras",   count: cat.extras.length,     danger: false, bonus: cat.extras.length > 0 }},
    {{ id: "full",     label: "Full Plan", count: PLAN_ROWS.reduce((n, r) => n + r.items.length, 0), danger: false, bonus: false }},
  ];
  tabsEl.textContent = "";
  tabs.forEach(t => {{
    const btn = document.createElement("button");
    btn.className = "plan-tab" + (t.danger ? " danger" : "") + (t.bonus ? " bonus" : "") + (planTab === t.id ? " active" : "");
    btn.textContent = t.label;
    const badge = document.createElement("span");
    badge.className = "badge";
    badge.textContent = t.count;
    btn.appendChild(badge);
    btn.addEventListener("click", () => {{ planTab = t.id; renderPlanPanel(); }});
    tabsEl.appendChild(btn);
  }});

  // Body
  if (planTab === "today") {{
    if (!cat.todayRows.length && cat.todayISO < PLAN_START && cat.upcoming) {{
      // Before plan starts — show tomorrow / next planned day preview
      const list = document.getElementById("plan-list");
      list.textContent = "";
      const wrap = document.createElement("div");
      wrap.className = "plan-day-group";
      const label = document.createElement("div");
      label.className = "plan-day-label";
      const pill = document.createElement("span");
      pill.className = "wk-pill";
      pill.textContent = "W" + cat.upcoming.wk;
      label.appendChild(pill);
      label.appendChild(document.createTextNode(`Starts ${{cat.upcoming.dy}} · ${{fmtDate(cat.upcoming.dt)}}`));
      wrap.appendChild(label);
      cat.upcoming.items.forEach(it => wrap.appendChild(renderPlanItem(it, cat.upcoming)));
      list.appendChild(wrap);
    }} else {{
      renderGroupedByDay(cat.todayItems);
    }}
  }} else if (planTab === "backlog") {{
    renderGroupedByDay(cat.backlog);
  }} else if (planTab === "upcoming") {{
    if (!cat.upcoming) {{
      const list = document.getElementById("plan-list");
      list.textContent = "";
      const empty = document.createElement("div");
      empty.className = "plan-empty";
      empty.textContent = "No upcoming work — 12-week plan complete.";
      list.appendChild(empty);
    }} else {{
      const items = cat.upcoming.items.map(it => ({{ row: cat.upcoming, item: it }}));
      renderGroupedByDay(items);
    }}
  }} else if (planTab === "full") {{
    renderFullPlan(cat);
  }} else if (planTab === "extras") {{
    renderGroupedByDay(cat.extras);
  }}
}}
{JS_END}
"""


def inject_or_replace(html: str, start: str, end: str, payload: str) -> str:
    """Replace any existing [start..end] block (inclusive of markers) with payload.
    If no existing block, callers handle insertion separately.
    """
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if pat.search(html):
        return pat.sub(payload, html, count=1)
    return html  # caller handles insertion


def main() -> None:
    html = INDEX.read_text()
    # --- CSS ---
    if CSS_START in html:
        html = inject_or_replace(html, CSS_START, CSS_END, CSS)
    else:
        # insert before </style>
        html = html.replace("</style>", f"  {CSS}\n</style>", 1)

    # --- HTML panel ---
    if START_MARK in html:
        html = inject_or_replace(html, START_MARK, END_MARK, HTML_PANEL)
    else:
        html = html.replace(
            '<div id="sections-container"></div>',
            HTML_PANEL + "\n\n  " + '<div id="sections-container"></div>',
            1,
        )

    # --- JS ---
    if JS_START in html:
        html = inject_or_replace(html, JS_START, JS_END, JS)
    else:
        # insert after DATA declaration (and STORAGE_KEY) — before loadState
        html = re.sub(
            r"(const STORAGE_KEY = \"[^\"]+\";\n)",
            r"\1\n" + JS + "\n",
            html,
            count=1,
        )

    # --- Hook renderPlanPanel() into render() ---
    # Ensure render() calls renderPlanPanel at the end.
    if (
        "renderPlanPanel()" not in html.split(JS_END)[1]
        if JS_END in html
        else "renderPlanPanel()" not in html
    ):
        pass  # JS block has its own call inside renderPlanPanel logic via tabs; we still need render() to call it
    # Add the call right after the overall-fill width line
    if "renderPlanPanel();" not in html.split(JS_END, 1)[-1]:
        html = re.sub(
            r"(document\.getElementById\(\"overall-fill\"\)\.style\.width = pctAll \+ \"%\";)",
            r"\1\n  renderPlanPanel();",
            html,
            count=1,
        )

    INDEX.write_text(html)
    print(f"Wired plan: {len(PLAN)} day-slots, {TOTAL} problems total")


if __name__ == "__main__":
    main()
