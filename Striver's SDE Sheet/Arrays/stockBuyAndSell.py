# QUESTION: Stock Buy and Sell
# You are given an array of prices where prices[i] is the price of a given
# stock on the i-th day. You want to maximize your profit by choosing a
# single day to buy one stock and choosing a different day in the future to
# sell that stock. Return the maximum profit you can achieve from this
# transaction. If you cannot achieve any profit, return 0.
#
# Examples:
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
# profit = 6 - 1 = 5. Note that buying on day 2 and selling on day 1 is
# not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done and the max profit = 0.
#
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4


"""
#Brute Force:
1. The profit for buying on day i and selling on a later day j is arr[j] - arr[i],
   and we must have j > i (buy before sell). So literally try every valid pair.
2. Fix a buy day i with the outer loop, then with the inner loop scan every later
   day j (j from i+1) and compute arr[j] - arr[i], keeping the running best `maxi`.
3. Start `maxi` at 0 so that if no pair yields a positive profit (prices only
   fall), we return 0 — matching the "no transaction" rule.
   This re-examines every pair independently, which is why it is quadratic.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct "better" tier exists; the problem goes straight from the
O(n^2) brute force to the O(n) single-pass optimal.

#Optimal Approach:
1. The key shift: for any sell day i, the best possible profit is arr[i] minus the
   CHEAPEST price seen on any earlier day. So we never need the inner loop — we just
   need to remember the minimum price so far while walking left to right.
2. Initialise `mini = arr[0]` (cheapest buy seen) and `maxi = 0` (best profit so far).
3. For each day i from 1: first update `maxi = max(maxi, arr[i] - mini)` — i.e. "what
   if I sell today, having bought at the cheapest earlier day?" — THEN update
   `mini = min(mini, arr[i])` so future days can buy at today's price if it's lower.
   (Order matters: updating maxi before mini guarantees the buy day is strictly
   before the sell day.)
4. One pass yields the answer because each day only needs the best buy-price to its left.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The best sell at day i only depends on the minimum price to its left, so carry that
  minimum forward in one pass instead of re-scanning all earlier days. Update the
  profit using the old minimum BEFORE folding today's price in, which enforces
  buy-before-sell.
"""

from typing import List


class Solution:
    def stock_buy_and_sell_brute(self, arr: List[int]) -> int:
        maxi = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                maxi = max(maxi, arr[j] - arr[i])
        return maxi

    def stock_buy_and_sell_better(self) -> None:
        # SKIP: no distinct "better" tier exists — the problem goes straight from
        # the O(n^2) brute force to the O(n) single-pass optimal.
        pass

    def stock_buy_and_sell_optimal(self, arr: List[int]) -> int:
        maxi = 0
        mini = arr[0]

        for i in range(1, len(arr)):
            maxi = max(maxi, arr[i] - mini)
            mini = min(mini, arr[i])
        return maxi


if __name__ == "__main__":
    sol = Solution()
    arr = [7, 1, 5, 3, 6, 4]
    print(sol.stock_buy_and_sell_brute(arr))
    arr = [7, 1, 5, 3, 6, 4]
    print(sol.stock_buy_and_sell_optimal(arr))
