# mypy: disable-error-code="empty-body"
# QUESTION: 0 and 1 Knapsack
# A thief wants to rob a store. He is carrying a bag of capacity W. The
# store has 'n' items. Item i has weight wt[i] and value val[i]. He can
# either pick an item entirely or leave it out (0/1 knapsack — items
# cannot be split). What is the maximum value he can carry such that the
# total weight is <= W?
#
# Examples:
# Example 1:
# Input: val = [60, 100, 120], wt = [10, 20, 30], W = 50
# Output: 220
# Explanation: Select items with weights 20 and 30 for a total value of 100 + 120 = 220.
#
# Example 2:
# Input: val = [10, 40, 30, 50], wt = [5, 4, 6, 3], W = 10
# Output: 90
# Explanation: Select items with weights 4 and 3 for a total value of 40 + 50 = 90.


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
    def zero_and_one_knapsack_brute(self, val: List[int], wt: List[int], capacity: int) -> int:
        pass

    def zero_and_one_knapsack_better(self, val: List[int], wt: List[int], capacity: int) -> int:
        pass

    def zero_and_one_knapsack_optimal(self, val: List[int], wt: List[int], capacity: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50
    print(sol.zero_and_one_knapsack_optimal(val, wt, capacity))
