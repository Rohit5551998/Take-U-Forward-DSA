# mypy: disable-error-code="empty-body"
# QUESTION: Lemonade Change
# At a lemonade stand, each lemonade costs $5. Customers stand in a queue and pay with
# a $5, $10, or $20 bill. You must give each customer correct change so they pay a net
# of $5. You start with no change. Given an integer array bills where bills[i] is the
# bill the i-th customer pays with, return true if you can provide every customer with
# correct change, otherwise return false.
#
# Example 1:
# Input: bills = [5, 5, 5, 10, 20]
# Output: true
# Explanation: Collect three $5, give $5 change for the $10, then give $10 + $5 for the $20.
#
# Constraints:
# 1 <= bills.length <= 10^5
# bills[i] is either 5, 10, or 20

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
    def lemonade_change_brute(self, bills: List[int]) -> bool:
        pass

    def lemonade_change_better(self, bills: List[int]) -> bool:
        pass

    def lemonade_change_optimal(self, bills: List[int]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.lemonade_change_optimal([5, 5, 5, 10, 20]))
