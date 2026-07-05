# DP Patterns — Recursion → Memoization → Tabulation → Space Optimization

A reusable playbook for dynamic-programming problems. The whole ladder is
mechanical once step 1 (the recursion) is correct: get the brute recursion
right, then each later rung is a near-automatic transformation, not a redesign.

Running example: **Coin Change** — `f(i, T)` = fewest coins from `coins[0..i]`
that sum to `T`, infinite supply of each coin.

---

## 1. Recursion Pattern (the brute force)

**1. STATE — Express everything as `f(index, target)`.**
Pick the smallest set of parameters that fully describes a subproblem: usually
an `index` (which items/coins are still in play) plus whatever you're building
toward (`T` = amount left, capacity left, …).
> coin change: `f(i, T)` = fewest coins from `coins[0..i]` summing to `T`.

**2. EXPLORE — At the current index, try EVERY choice and recurse on the rest.**
Enumerate the options available on `index`; for each, recurse on the subproblem
it leaves behind. Two common shapes:
- **take / not-take** — each item used at most once.
- **take-and-stay / move-on** — infinite supply, so you may reuse `index`.
> coin change: `skip = f(i-1, T)`; `take = 1 + f(i, T - coins[i])` (stay on `i`
> because coins are unlimited). Only try `take` when `coins[i] <= T`.

**3. COMBINE — Merge the choices per what the problem asks.**
- `min(...)` / `max(...)` → optimization ("fewest coins", "max value")
- `sum(...)` → counting ("number of ways")
- `any(...)` / OR → feasibility ("is it possible?")
> coin change: `return min(take, skip)`.

**4. BASE CASE — Smallest solvable subproblem + the IMPOSSIBLE marker.**
Handle `index == 0` (or `T == 0`) directly. For a MIN problem, represent
"can't be done" as **+infinity (`1e9`)** so `min()` rejects it — never `-1`/`0`,
which `min()` would wrongly prefer. Convert that sentinel to the required output
(e.g. `-1`) only at the very end, in the wrapper.
> coin change, `i == 0`: `T % coins[0] == 0 ? T // coins[0] : 1e9`.

**5. MEMOIZE — Once 1–4 are correct, cache `f(state)`.**
The recursion revisits the same `(index, target)` via many paths — that's the
exponential cost. Store each result in a `dp` table keyed by the state so it's
computed once. Nothing about the logic changes; this is the brute → better step.
> `dp[i][T]` seeded to `-1` ("not computed"); check it before recursing, store
> before returning. `-1` is a safe sentinel because real answers are `>= 0` and
> impossible is `1e9`.

**Complexity:** recursion `O(exponential)` → memoization `O(#states × work per state)`.

---

## 2. Tabulation Pattern (the iterative DP)

Memoization is top-down (recurse, cache on the way back). Tabulation is
bottom-up: fill the same table with plain loops, no recursion. Three
mechanical steps to convert a correct memoized solution:

**1. BASE CASE → initial table values.**
Whatever the recursion returned at its base case, *write it into the table
first* as the seed row/cell. Everything else builds on top of it.
> coin change: fill the `i == 0` row — for every `T`, put `T // coins[0]` if
> `coins[0]` divides `T`, else `1e9`.

**2. Find the changing parameters (`index`, `target`) → loops, in the OPPOSITE
direction.**
Each recursion parameter becomes a loop dimension. The recursion peels state
*downward* (from `n-1`, from full `T`) toward the base; tabulation builds
*upward* from the base you just seeded. So iterate in the reverse order the
recursion unwinds — outer loop over `index` starting just past the base row,
inner loop over `target`.
> coin change: `for i in 1..n-1: for T in 0..amount:`

**3. Copy the recurrence, swapping `f(...)` calls for table lookups.**
The body is identical to the memoized recurrence — just replace each recursive
call `f(a, b)` with the already-filled cell `dp[a][b]`. Same `min`/`max`/`sum`,
same choices, same guards.
> coin change: `skip = dp[i-1][T]`; `take = coins[i] <= T ? 1 + dp[i][T-coins[i]] : 1e9`;
> `dp[i][T] = min(take, skip)`. Answer = `dp[n-1][amount]` (convert `1e9` → `-1`).

**Why bother if the complexity is the same as memoization?**
No recursion stack (no depth limit / call overhead), and it sets up the next
rung: space optimization.

---

## 3. Space Optimization

Look at what the recurrence in step 2.3 *actually reads*. If `dp[i][…]` only
ever depends on `dp[i-1][…]` (and possibly the current row), you don't need the
whole 2D table — keep just the previous row (and current row), or collapse to a
single 1D array updated in place. This is what turns an `O(index × target)`
space table into `O(target)`.

- Identify the dependency window (previous row? previous cell? a fixed offset?).
- Replace the 2D table with one or two 1D arrays of size `target + 1`.
- Watch the inner-loop direction — updating in place forward vs backward matters
  when a state depends on an already-updated cell in the same pass.

> This is the difference between the "better" (full table) and "optimal"
> (1D) tiers on many DP problems.

**The prev/curr recipe (when `dp[i]` depends only on `dp[i-1]` and `dp[i]`):**

1. Two 1D arrays of length `target + 1`: `prev` (row `i-1`) and `curr` (row `i`),
   instead of the `n × (target+1)` matrix.
2. Seed the base case into **`prev`**.
3. In the loops, read `prev[...]` wherever the 2D version read `dp[i-1][...]`,
   and `curr[...]` wherever it read `dp[i][...]`.
4. After each `i`, roll forward: `prev = curr`.
5. Return **`prev[target]`**, not `curr[target]` — if the `i`-loop never runs
   (e.g. only one item), the answer is still the base row in `prev`; and after
   the loop, `prev` also points at the last computed row.

> Coin change: base row = `prev[T] = T // coins[0] if divisible else +inf`;
> then `skip = prev[T]`, `take = 1 + curr[T-coins[i]]` (take stays on the
> current row for infinite supply), `curr[T] = min(skip, take)`.

**Two traps this exact optimization sprung (both real bugs worth remembering):**

- **Reading the answer from the wrong array.** `curr` is written only inside the
  `i`-loop; if that loop never executes (single item), `curr` stays at its init
  value and you get a wrong/`-1` answer. Read from `prev` (rule 5).
- **`prev = curr` aliases in Python (it copies in C++).** After `prev = curr`
  both names point to the *same* list, so writes to `curr` also change `prev`.
  It happens to be harmless when `take` reads already-updated cells and `skip`
  reads `prev[T]` before `curr[T]` is overwritten — but if you need genuinely
  independent rows, use `prev = curr[:]` (copy) or swap in a fresh `curr`.

---

## Quick checklist

- [ ] State `f(index, target)` captures a full subproblem?
- [ ] Every choice explored; guards on invalid choices?
- [ ] Combine matches the ask (min / max / sum / any)?
- [ ] Base case correct, impossible = `+inf` for min problems?
- [ ] Sentinel converted to the required output only in the wrapper?
- [ ] Memoized on the exact state tuple?
- [ ] Tabulation: base seeded, loops reversed, recurrence copied with lookups?
- [ ] Space: dropped unused rows once the dependency window is clear?
