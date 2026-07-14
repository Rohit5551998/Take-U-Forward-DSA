# mypy: disable-error-code="empty-body"
# QUESTION: Fractional Knapsack Problem
# Given the weights and values of N items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. Unlike 0/1 knapsack, you may break
# items: you can take a fraction of an item. Return the maximum total value (as a float).
#
# Example 1:
# Input: N = 3, W = 50, values = [60, 100, 120], weights = [10, 20, 30]
# Output: 240.0
# Explanation: Take items 1 and 2 fully (value 160, weight 30), then 20/30 of item 3
# for value 80. Total = 240.0.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= W <= 10^5
# 1 <= values[i], weights[i] <= 10^4

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
    def fractional_knapsack_brute(self, W: int, values: List[int], weights: List[int]) -> float:
        pass

    def fractional_knapsack_better(self, W: int, values: List[int], weights: List[int]) -> float:
        pass

    def fractional_knapsack_optimal(self, W: int, values: List[int], weights: List[int]) -> float:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.fractional_knapsack_optimal(50, [60, 100, 120], [10, 20, 30]))
