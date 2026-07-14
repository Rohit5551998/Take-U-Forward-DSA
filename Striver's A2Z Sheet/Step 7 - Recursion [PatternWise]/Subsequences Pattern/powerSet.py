# mypy: disable-error-code="empty-body"
# QUESTION: Print all subsequences / Power Set
# Given an array of integers nums of unique elements, return all possible
# subsequences (the power set). The solution set must not contain duplicate subsets.
# Example 1:
# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
# Example 2:
# Input: nums = [0]
# Output: [[], [0]]
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All elements are unique.

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
    def power_set_brute(self, nums: List[int]) -> List[List[int]]:
        pass

    def power_set_better(self, nums: List[int]) -> List[List[int]]:
        pass

    def power_set_optimal(self, nums: List[int]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.power_set_optimal([1, 2, 3]))
