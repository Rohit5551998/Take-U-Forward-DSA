# mypy: disable-error-code="empty-body"
# QUESTION: 0/1 Knapsack
# Given weights and values of n items and capacity W, maximize total value.
# Each item may be taken at most once.
#
# Example 1:
# Input: weights = [1,2,3], values = [10,15,40], W = 6
# Output: 65
#
# Constraints:
# 1 <= n <= 1000
# 1 <= W <= 1000

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
    def knapsack_brute(self, weights: List[int], values: List[int], W: int) -> int:
        pass

    def knapsack_better(self, weights: List[int], values: List[int], W: int) -> int:
        pass

    def knapsack_optimal(self, weights: List[int], values: List[int], W: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.knapsack_optimal([1, 2, 3], [10, 15, 40], 6)
