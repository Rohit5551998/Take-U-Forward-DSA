# mypy: disable-error-code="empty-body"
# QUESTION: Best Time to Buy and Sell Stock
# Given an array prices where prices[i] is the price of a stock on day i, find the
# maximum profit from a single buy and a later single sell. If no profit is
# possible return 0.
# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 1 (price 1) and sell on day 4 (price 6), profit = 5.
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

"""
#Brute Force:
1. For every buy day i, try every later sell day j and track max(prices[j] - prices[i]).
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; the jump from the O(n^2) scan to the single
pass below is direct.

#Optimal Approach:
1. Sweep left to right tracking the minimum price seen so far (the best day to
   have bought).
2. At each day compute the profit if we sold today (price - minSoFar) and update
   the running max profit.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The best sell day only cares about the cheapest price before it, so tracking a
  single running minimum collapses the pairwise search into one pass.
"""

from typing import List


class Solution:
    def stock_brute(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    def stock_better(self, prices: List[int]) -> int:
        # SKIP: no distinct better approach between brute and the single-pass optimal.
        pass

    def stock_optimal(self, prices: List[int]) -> int:
        max_profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - mini)
            mini = min(mini, prices[i])
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.stock_optimal([7, 1, 5, 3, 6, 4]))
