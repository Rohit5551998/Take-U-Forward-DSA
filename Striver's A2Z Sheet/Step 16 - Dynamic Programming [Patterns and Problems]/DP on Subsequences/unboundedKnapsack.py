# mypy: disable-error-code="empty-body"
# QUESTION: Unbounded Knapsack
# Given weights and values of n items and capacity W, maximize total value.
# Each item may be chosen an unlimited number of times.
#
# Example 1:
# Input: weights = [2,4,6], values = [5,11,13], W = 10
# Output: 27
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
    def unbounded_knapsack_brute(self, weights: List[int], values: List[int], W: int) -> int:
        pass

    def unbounded_knapsack_better(self, weights: List[int], values: List[int], W: int) -> int:
        pass

    def unbounded_knapsack_optimal(self, weights: List[int], values: List[int], W: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.unbounded_knapsack_optimal([2, 4, 6], [5, 11, 13], 10)
