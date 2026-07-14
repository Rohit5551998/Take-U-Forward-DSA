# mypy: disable-error-code="empty-body"
# QUESTION: Best Time to Buy and Sell Stock with Transaction Fee
# Complete unlimited transactions but pay a fee per transaction. Maximize
# profit.
#
# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
#
# Constraints:
# 1 <= n <= 5*10^4
# 0 <= prices[i], fee <= 5*10^4

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
    def max_profit_fee_brute(self, prices: List[int], fee: int) -> int:
        pass

    def max_profit_fee_better(self, prices: List[int], fee: int) -> int:
        pass

    def max_profit_fee_optimal(self, prices: List[int], fee: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.max_profit_fee_optimal([1, 3, 2, 8, 4, 9], 2)
