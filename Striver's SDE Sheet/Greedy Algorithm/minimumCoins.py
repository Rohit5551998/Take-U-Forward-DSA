# mypy: disable-error-code="empty-body"
# QUESTION: Minimum coins
# Given an integer array `coins` representing coins of different
# denominations and an integer `amount` representing a total amount of
# money, return the fewest number of coins that you need to make up that
# amount. If that amount of money cannot be made up by any combination of
# the coins, return -1.
# You have an infinite number of each kind of coin.
# Note: The Striver sheet groups this under Greedy (because the standard
# Indian/US coin systems allow a greedy solution), but for arbitrary
# denominations a DP solution is required for correctness.
#
# Examples:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.
#
# Input : coins = [2, 5], amount = 3
# Output: -1
# Explanation: It's not possible to make amount 3 with coins 2 and 5. Since we can't
# combine coins 2 and 5 to make the amount 3, the output is -1.


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
    def minimum_coins_brute(self, coins: List[int], amount: int) -> int:
        pass

    def minimum_coins_better(self, coins: List[int], amount: int) -> int:
        pass

    def minimum_coins_optimal(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.minimum_coins_optimal(coins, amount))
