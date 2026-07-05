# mypy: disable-error-code="empty-body"
# QUESTION: Fractional Knapsack
# You are given N items, each with a value val[i] and a weight wt[i], and a knapsack with a
# total weight capacity W. Fill the knapsack so that the total value of the items placed in it
# is maximized, and return that maximum total value.
# Unlike 0/1 Knapsack, you are allowed to break an item: you may take any fraction of an item,
# and the value obtained is proportional to the fraction of its weight taken. Each item can be
# taken at most once (fully or partially).
#
# Examples:
# Example 1:
# Input: N = 3, W = 50, val = [60, 100, 120], wt = [10, 20, 30]
# Output: 240.0
# Explanation: Take item 1 fully (wt 10, val 60) and item 2 fully (wt 20, val 100). Capacity
# left = 50 - 30 = 20, so take 20/30 of item 3, worth 120 * 20/30 = 80.
# Total value = 60 + 100 + 80 = 240.0.
#
# Example 2:
# Input: N = 2, W = 25, val = [60, 100], wt = [10, 20]
# Output: 135.0
# Explanation: Value/weight ratios are 6.0 and 5.0. Take item 1 fully (wt 10, val 60). Capacity
# left = 25 - 10 = 15, so take 15/20 of item 2, worth 100 * 15/20 = 75.
# Total value = 60 + 75 = 135.0.


"""
#Brute Force:
SKIPPED — there is no meaningful brute-force tier here. Because items can be
split, greedily taking the best value/weight ratio is provably optimal, so
there is no naive "try all subsets" step to improve on (that is the 0/1
knapsack, a different problem). We go straight to the greedy solution.

#Better Approach:
SKIPPED — same reason: the greedy-by-ratio approach is already optimal, with no
distinct intermediate tier between it and a (non-existent) brute force.

#Optimal Approach:
1. Intuition: since we can take fractions, every unit of capacity should be
   spent on the item that gives the most value per unit weight. So rank items
   by their value/weight ratio and consume them from richest ratio to poorest.
2. Build `items` = zip(val, wt) sorted by `val/wt` descending. Now the front of
   the list is the most "value-dense" item.
3. Walk the sorted items, carrying a running `total` value and shrinking
   `capacity` as we consume weight.
4. If the whole current item fits (`wt <= capacity`), take it fully: add its
   entire value to `total` and subtract its weight from `capacity`. Full items
   are free wins — we never regret taking a denser item completely.
5. Otherwise the item cannot fit whole, so take the fraction that fills the
   remaining capacity: add `(val/wt) * capacity` (value of exactly `capacity`
   worth of weight) and `break` — the knapsack is now full, and every later
   item has a worse ratio so there is nothing better to swap in.
6. Return `total`. Example: val=[60,100,120], wt=[10,20,30], cap=50 → ratios
   6,5,4; take item0 full (+60, cap40), item1 full (+100, cap20), then 20/30 of
   item2 (+80) → 240.0.
TC -> O(N log N) — the sort dominates; the single sweep is O(N).
SC -> O(N) for the sorted list of (val, wt) pairs.

#KEY INSIGHT:
- Fractional-ability is what makes greedy exact: because any item can be split,
  filling capacity with the highest value/weight ratio first is always optimal
  — there is never a reason to skip a denser item for a less dense one. (This is
  exactly why the same greedy fails for 0/1 knapsack, where you can't split.)
"""

from typing import List


class Solution:
    def fractional_knapsack_brute(self, val: List[int], wt: List[int], capacity: int) -> float:
        # SKIP: no brute-force tier — fractions make greedy-by-ratio provably
        # optimal, so there is no "try all subsets" step to beat (that's 0/1).
        pass

    def fractional_knapsack_better(self, val: List[int], wt: List[int], capacity: int) -> float:
        # SKIP: no intermediate tier — greedy-by-ratio is already optimal.
        pass

    def fractional_knapsack_optimal(self, val: List[int], wt: List[int], capacity: int) -> float:
        items = sorted(zip(val, wt), key=lambda item: item[0] / item[1], reverse=True)

        total = 0.0

        for i in range(0, len(items)):
            if items[i][1] <= capacity:
                total += items[i][0]
                capacity -= items[i][1]
            else:
                total += (items[i][0] / items[i][1]) * capacity
                break

        return total


if __name__ == "__main__":
    sol = Solution()
    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50
    print(sol.fractional_knapsack_optimal(val, wt, capacity))
