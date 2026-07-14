# mypy: disable-error-code="empty-body"
# QUESTION: Best Time to Buy and Sell Stock with Cooldown
# Complete unlimited transactions but after selling you cannot buy the next day
# (one-day cooldown). Maximize profit.
#
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
#
# Constraints:
# 1 <= n <= 5000
# 0 <= prices[i] <= 1000

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
    def max_profit_cooldown_brute(self, prices: List[int]) -> int:
        pass

    def max_profit_cooldown_better(self, prices: List[int]) -> int:
        pass

    def max_profit_cooldown_optimal(self, prices: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.max_profit_cooldown_optimal([1, 2, 3, 0, 2])
