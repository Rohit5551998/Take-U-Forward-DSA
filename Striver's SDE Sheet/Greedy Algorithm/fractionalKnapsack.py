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
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def fractional_knapsack_brute(self, val: List[int], wt: List[int], capacity: int) -> float:
        pass

    def fractional_knapsack_better(self, val: List[int], wt: List[int], capacity: int) -> float:
        pass

    def fractional_knapsack_optimal(self, val: List[int], wt: List[int], capacity: int) -> float:
        pass


if __name__ == "__main__":
    sol = Solution()
    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50
    print(sol.fractional_knapsack_optimal(val, wt, capacity))
