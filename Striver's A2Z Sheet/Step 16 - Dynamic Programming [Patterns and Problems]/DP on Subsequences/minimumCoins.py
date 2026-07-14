# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Coins (Coin Change)
# Given coins (infinite supply) and an amount, return the fewest coins needed
# to make the amount, or -1 if impossible.
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 5+5+1.
#
# Constraints:
# 1 <= n <= 12
# 0 <= amount <= 10^4

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
    def coin_change_brute(self, coins: List[int], amount: int) -> int:
        pass

    def coin_change_better(self, coins: List[int], amount: int) -> int:
        pass

    def coin_change_optimal(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.coin_change_optimal([1, 2, 5], 11)
