# mypy: disable-error-code="empty-body"
# QUESTION: Find Minimum Number of Coins
# Given an infinite supply of coins of the standard Indian denominations
# [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], find the minimum number of coins
# (and/or notes) needed to make up a given value V. Return the list of coins used.
#
# Example 1:
# Input: V = 49
# Output: [20, 20, 5, 2, 2]
# Explanation: 5 coins/notes: 20 + 20 + 5 + 2 + 2 = 49, which is the minimum count.
#
# Constraints:
# 1 <= V <= 10^9
# Denominations are canonical, so a greedy choice is always optimal here.

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
    def minimum_coins_brute(self, V: int) -> List[int]:
        pass

    def minimum_coins_better(self, V: int) -> List[int]:
        pass

    def minimum_coins_optimal(self, V: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.minimum_coins_optimal(49))
