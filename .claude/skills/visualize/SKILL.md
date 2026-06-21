---
name: visualize
description: Generate a self-contained HTML animation for the optimal algorithm in a Striver .py solution. Frames + play/pause/step controls + color-coded states (current/left/right/visited/result) + captions per frame, using a hardcoded sample.
---

# Visualize an Algorithm

Produce ONE self-contained HTML file (no external assets) that animates the **optimal** approach in a `.py` solution file, step-by-step, with captions and color-coded states.

## Arguments

- `<file-path>`: Path to the solution `.py` file, relative to repo root. Example: `"Striver's SDE Sheet/Arrays/setMatrixZeroes.py"`.

## Output

Write the HTML to `{same-dir}/{same-basename}.html` next to the `.py` file.
Example: `Striver's SDE Sheet/Arrays/setMatrixZeroes.py` → `Striver's SDE Sheet/Arrays/setMatrixZeroes.html`.

## Workflow

1. **Read the `.py` file.** Identify:
   - Problem name (from `# QUESTION:` block)
   - Optimal approach (from the `#Optimal Approach:` section of the docstring or the `*_optimal` function body)
   - Data structure (array / 2D grid / linked list / binary tree / graph / stack / etc.)

2. **If the optimal approach is empty/stubbed**, ask the user:
   - Whether to visualize a different approach (brute/better)
   - OR to first run `/solve` to flesh out the approach
   - Do NOT invent an algorithm the user hasn't written.

3. **Pick a sample input** small enough to animate clearly (5–10 elements typical, 4×4 grid max, ~6 list nodes, ~7 tree nodes). Use one of the problem's official examples if available, else a small representative case.

4. **Trace the optimal algorithm** on the sample by simulating it in your head (or in Python via Bash if the function is implemented). Produce a `FRAMES` array — one entry per meaningful step (pointer move, comparison, swap, push/pop, recursive call, etc.). Each frame includes:
   - `caption`: a single sentence explaining what just happened (≤ 100 chars)
   - state fields specific to the data structure (see "State conventions" below)

5. **Pick a renderer** based on data shape — see "Renderer templates" below. Adapt or combine; do NOT generate a kitchen-sink renderer.

6. **Write the HTML file** using the template in "HTML scaffold" below. The same scaffold works for all data shapes — only `FRAMES` and `render(frame)` change.

7. **Verify** the file is valid HTML (open it in a headless check or just confirm structure). The page must work when opened directly via `file://` — no servers, no external CDNs.

## State conventions (use consistent class names so colors work)

- `current` (yellow) — element being examined right now
- `left` (green) — left pointer / `i`
- `right` (red) — right pointer / `j` (or `r`)
- `visited` (dimmed) — already processed, no longer relevant
- `result` (purple) — confirmed part of the answer
- `compare` (orange flash) — two elements being compared this step
- `window` (translucent overlay) — sliding-window range

The HTML scaffold below defines all these classes. Use them by setting per-element class names in your renderer.

## Renderer templates

Pick ONE of these to start; tweak as needed:

### Array (1D)

`state: { arr, idxClasses, pointers }`
- `arr`: full array values
- `idxClasses`: `{ [index]: ["current"|"left"|"right"|"visited"|"result"|"compare"] }`
- `pointers`: `{ [index]: ["l"|"r"|"i"|"j"|"slow"|"fast"] }` — label below the cell

```js
function render(f) {
  const stage = document.getElementById('stage');
  stage.innerHTML = '';
  const row = document.createElement('div');
  row.style.display = 'flex'; row.style.flexWrap = 'wrap'; row.style.gap = '6px';
  f.state.arr.forEach((v, i) => {
    const cell = document.createElement('div');
    cell.className = 'cell';
    (f.state.idxClasses?.[i] || []).forEach(c => cell.classList.add(c));
    cell.innerHTML = `<span class="idx">${i}</span>${v}`;
    (f.state.pointers?.[i] || []).forEach(p => {
      const lab = document.createElement('span');
      lab.className = `pointer ${p}`; lab.textContent = p;
      cell.appendChild(lab);
    });
    row.appendChild(cell);
  });
  stage.appendChild(row);
}
```

### Grid (2D)

`state: { grid, cellClasses }` — `cellClasses: { "r,c": ["current"|...] }`. Render with `display:grid; grid-template-columns: repeat(cols, 1fr)`.

### Linked List

`state: { nodes, ptrs }` — `nodes: [{val, classes}]`; `ptrs: { [nodeIndex]: ["head"|"slow"|"fast"|"prev"|"curr"|"next"] }`. Render nodes as boxes with `→` arrows between.

### Binary Tree

`state: { nodes, edges, classes }` where `nodes: [{id, val, x, y}]`, `edges: [[parentId, childId]]`, `classes: { id: [...] }`. Use absolute positioning or SVG. Pre-compute `(x, y)` from the tree's depth/index.

### Stack / Queue

Vertical list (stack: top at top) or horizontal queue. Highlight the most-recent push/pop with `current`.

### Sliding Window

Use the Array renderer plus a translucent overlay rectangle spanning `[l, r]`.

## HTML scaffold

The skeleton below — drop FRAMES + render() in, save the file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{PROBLEM NAME} — Visualization</title>
<style>
  :root {
    --bg:#0f0f13; --surface:#1a1a24; --border:#2a2a3a; --text:#e4e4ed; --dim:#8888a0;
    --accent:#7c5cfc; --yellow:#fbbf24; --green:#34d399; --red:#f87171;
    --orange:#fb923c; --purple:#a78bfa;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:'JetBrains Mono', ui-monospace, Menlo, monospace; background:var(--bg); color:var(--text); padding:32px; min-height:100vh; }
  .container { max-width:1000px; margin:0 auto; }
  h1 { font-size:18px; margin-bottom:4px; }
  .desc { color:var(--dim); font-size:13px; margin-bottom:20px; }
  .desc code { background:var(--surface); padding:2px 6px; border-radius:4px; color:var(--accent); }
  .caption { padding:14px 16px; background:var(--surface); border-left:3px solid var(--accent); border-radius:4px; margin-bottom:20px; font-size:14px; min-height:48px; line-height:1.5; }
  .stage { padding:32px; background:var(--surface); border-radius:8px; margin-bottom:16px; min-height:160px; display:flex; align-items:center; justify-content:center; }
  .controls { display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
  button { padding:8px 14px; background:var(--accent); color:white; border:none; border-radius:6px; cursor:pointer; font-family:inherit; font-size:13px; transition:opacity 0.2s; }
  button:disabled { opacity:0.4; cursor:default; }
  button:hover:not(:disabled) { opacity:0.85; }
  select { padding:7px 10px; background:var(--surface); color:var(--text); border:1px solid var(--border); border-radius:6px; font-family:inherit; font-size:13px; }
  .step-indicator { color:var(--dim); font-size:13px; margin-left:auto; }
  .legend { display:flex; flex-wrap:wrap; gap:12px; margin-top:16px; padding:12px; background:var(--surface); border-radius:8px; font-size:12px; }
  .legend-item { display:flex; align-items:center; gap:6px; }
  .swatch { width:14px; height:14px; border-radius:3px; }

  /* Array / generic cell */
  .cell { position:relative; min-width:52px; height:52px; border:2px solid var(--border); border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:16px; font-weight:600; transition:all 0.3s ease; background:var(--bg); }
  .cell .idx { position:absolute; top:-18px; font-size:10px; color:var(--dim); font-weight:400; }
  .pointer { position:absolute; bottom:-20px; font-size:11px; font-weight:700; }
  .pointer.l, .pointer.slow { color:var(--green); }
  .pointer.r, .pointer.fast { color:var(--red); }
  .pointer.i, .pointer.j, .pointer.curr { color:var(--yellow); }
  .pointer.prev { color:var(--purple); }

  /* States — stack so multiple apply gracefully */
  .cell.current { border-color:var(--yellow); background:rgba(251,191,36,0.18); transform:scale(1.08); }
  .cell.left    { border-color:var(--green);  background:rgba(52,211,153,0.18); }
  .cell.right   { border-color:var(--red);    background:rgba(248,113,113,0.18); }
  .cell.compare { animation: compareFlash 0.6s ease; }
  .cell.visited { color:var(--dim); opacity:0.55; }
  .cell.result  { border-color:var(--accent); background:rgba(124,92,252,0.25); color:#fff; box-shadow:0 0 12px rgba(124,92,252,0.4); }
  .cell.window  { box-shadow: inset 0 0 0 1px var(--accent); }
  @keyframes compareFlash {
    0%,100% { background-color: rgba(251,146,60,0); }
    50% { background-color: rgba(251,146,60,0.4); }
  }

  /* Linked-list arrow */
  .arrow { color:var(--dim); margin:0 4px; font-size:18px; }
  /* SVG tree edges */
  .edge { stroke: var(--border); stroke-width: 2; fill: none; }
</style>
</head>
<body>
<div class="container">
  <h1>{PROBLEM NAME}</h1>
  <div class="desc">{ONE_LINE_APPROACH_SUMMARY} · Input: <code>{SAMPLE_INPUT_REPR}</code></div>

  <div class="caption" id="caption">Press <strong>Play</strong> or <strong>Next</strong> to start.</div>
  <div class="stage" id="stage"></div>

  <div class="controls">
    <button id="prev">⏮ Prev</button>
    <button id="play">▶ Play</button>
    <button id="next">Next ⏭</button>
    <button id="reset">↺ Reset</button>
    <select id="speed">
      <option value="900">Slow</option>
      <option value="500" selected>Normal</option>
      <option value="200">Fast</option>
    </select>
    <span class="step-indicator" id="step">0 / 0</span>
  </div>

  <div class="legend">
    <div class="legend-item"><span class="swatch" style="background:rgba(251,191,36,0.3); border:2px solid var(--yellow)"></span> current</div>
    <div class="legend-item"><span class="swatch" style="background:rgba(52,211,153,0.3); border:2px solid var(--green)"></span> left / slow</div>
    <div class="legend-item"><span class="swatch" style="background:rgba(248,113,113,0.3); border:2px solid var(--red)"></span> right / fast</div>
    <div class="legend-item"><span class="swatch" style="background:rgba(251,146,60,0.3)"></span> comparing</div>
    <div class="legend-item"><span class="swatch" style="background:var(--dim); opacity:0.5"></span> visited</div>
    <div class="legend-item"><span class="swatch" style="background:rgba(124,92,252,0.4); border:2px solid var(--accent)"></span> result</div>
  </div>
</div>

<script>
  // ====== FRAMES — fill this in based on the algorithm trace ======
  const FRAMES = [
    // { caption: "...", state: { /* problem-specific */ } },
  ];

  // ====== RENDERER — pick the one that fits the data shape ======
  function render(frame) {
    // Implement based on data shape. See SKILL.md "Renderer templates".
  }

  // ====== PLAYBACK ENGINE — generic; do not change unless needed ======
  let cur = 0, playing = false, timer = null;
  const $ = id => document.getElementById(id);
  function show(idx) {
    cur = Math.max(0, Math.min(FRAMES.length - 1, idx));
    const f = FRAMES[cur];
    $('caption').innerHTML = f.caption || '';
    render(f);
    $('step').textContent = `${cur + 1} / ${FRAMES.length}`;
    $('prev').disabled = cur === 0;
    $('next').disabled = cur === FRAMES.length - 1;
  }
  function play() {
    if (playing) { stop(); return; }
    if (cur >= FRAMES.length - 1) cur = -1;
    playing = true; $('play').textContent = '⏸ Pause';
    const tick = () => {
      if (!playing) return;
      if (cur >= FRAMES.length - 1) { stop(); return; }
      show(cur + 1);
      timer = setTimeout(tick, +$('speed').value);
    };
    tick();
  }
  function stop() { playing = false; clearTimeout(timer); $('play').textContent = '▶ Play'; }
  $('prev').onclick = () => show(cur - 1);
  $('next').onclick = () => show(cur + 1);
  $('play').onclick = play;
  $('reset').onclick = () => { stop(); show(0); };
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') show(cur + 1);
    else if (e.key === 'ArrowLeft') show(cur - 1);
    else if (e.key === ' ') { e.preventDefault(); play(); }
  });
  show(0);
</script>
</body>
</html>
```

## Frame-building checklist

Before writing the file, sanity-check your `FRAMES`:

- [ ] First frame shows the initial state with a caption like *"Input: [...]. Initialize pointers l = 0, r = n-1."*
- [ ] Each frame's caption describes what changed *since the previous frame* (not a static description of the state)
- [ ] Every meaningful algorithm step has a frame — don't skip pointer moves, comparisons, or branching decisions
- [ ] No "dead" frames where nothing visible changes
- [ ] The final frame highlights the answer with `result` class and a caption like *"Answer: 42 (returned)."*
- [ ] Total frames between 6 and ~40 — fewer feels rushed, more drags

## When the algorithm doesn't fit array/grid/list/tree/graph

For unusual visualizations (e.g., bit manipulation, math, DP table fill), use a custom renderer but reuse the playback engine, caption area, and color CSS variables (`--yellow`, `--green`, `--red`, etc.) so the visual language is consistent across problems.

## Do NOT

- Generate the optimal solution if it's not in the file — visualize what's there or ask first
- Add external CDN imports, web fonts, fetched data — must work offline via `file://`
- Skip the legend — the user needs to learn the color code
- Animate via CSS-only loops — the user needs frame-by-frame control
- Use emojis in the caption text (per repo convention)
