# mypy: disable-error-code="empty-body"
# QUESTION: Connect N Ropes with Minimal Cost (Minimum Cost of Ropes)
# There are given n ropes of different lengths, connect these ropes into one rope.
# The cost to connect two ropes is equal to the sum of their lengths. Connect the
# ropes with minimum total cost and return that minimum cost.
#
# Example 1:
# Input: arr = [4, 3, 2, 6]
# Output: 29
# Explanation: Connect 2+3=5 (cost 5), then 4+5=9 (cost 9), then 6+9=15 (cost 15);
# total = 5 + 9 + 15 = 29.
#
# Example 2:
# Input: arr = [1, 2, 3, 4, 5]
# Output: 33
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^4


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
    def minCostToConnectRopes_brute(self, arr: List[int]) -> int:
        pass

    def minCostToConnectRopes_better(self, arr: List[int]) -> int:
        pass

    def minCostToConnectRopes_optimal(self, arr: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.minCostToConnectRopes_optimal([4, 3, 2, 6]))
