# mypy: disable-error-code="empty-body"
# QUESTION: Replace Each Array Element by its Corresponding Rank
# Given an array arr of n integers, replace each element by its rank. The rank of
# an element is its position (starting from 1) in the sorted order of the distinct
# values of the array; equal elements share the same rank.
#
# Example 1:
# Input: arr = [20, 15, 26, 2, 98, 6]
# Output: [4, 3, 5, 1, 6, 2]
# Explanation: Sorted distinct -> [2, 6, 15, 20, 26, 98]; ranks assigned 1..6.
#
# Example 2:
# Input: arr = [2, 6, 2, 8, 6]
# Output: [1, 2, 1, 3, 2]
# Explanation: Distinct sorted -> [2, 6, 8]; duplicates share the same rank.
#
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9


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
    def replaceByRank_brute(self, arr: List[int]) -> List[int]:
        pass

    def replaceByRank_better(self, arr: List[int]) -> List[int]:
        pass

    def replaceByRank_optimal(self, arr: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.replaceByRank_optimal([20, 15, 26, 2, 98, 6]))
