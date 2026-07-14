# mypy: disable-error-code="empty-body"
# QUESTION: Power Set
# Given an array of distinct integers nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Subsets may be returned in any order.
# Example 1:
# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
# Explanation: All 2^3 = 8 subsets of the set {1, 2, 3}.
# Example 2:
# Input: nums = [0]
# Output: [[], [0]]
# Explanation: The two subsets of a single-element set.
# Constraints:
# 1 <= len(nums) <= 16
# All elements of nums are distinct.

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
    def powerSet_brute(self, nums: List[int]) -> List[List[int]]:
        pass

    def powerSet_better(self, nums: List[int]) -> List[List[int]]:
        pass

    def powerSet_optimal(self, nums: List[int]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.powerSet_optimal([1, 2, 3]))
