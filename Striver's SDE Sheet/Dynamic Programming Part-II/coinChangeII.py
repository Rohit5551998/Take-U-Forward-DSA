# mypy: disable-error-code="empty-body"
# QUESTION: Coin change II
# We are given an array Arr with N distinct coins and a target. We have
# an infinite supply of each coin denomination. We need to find the
# number of distinct ways we can sum up coin values to make the target.
# Order of coins does NOT matter (i.e., [1, 2, 1] and [1, 1, 2] count as
# the same combination).
#
# Examples:
# Example 1:
# Input: coins = [2, 4,10], amount = 10
# Output: 4
# Explanation: The four combinations are:
# 10 = 10
# 10 = 4 + 4 + 2
# 10 = 4 + 2 + 2 + 2
# 10 = 2 + 2 + 2 + 2 + 2
#
# Example 2:
# Input: coins = [5], amount = 5
# Output: 1
# Explanation: There is one combination: 5 = 5.


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
    def coin_change_ii_brute(self, coins: List[int], amount: int) -> int:
        pass

    def coin_change_ii_better(self, coins: List[int], amount: int) -> int:
        pass

    def coin_change_ii_optimal(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    coins = [2, 4, 10]
    amount = 10
    print(sol.coin_change_ii_optimal(coins, amount))
