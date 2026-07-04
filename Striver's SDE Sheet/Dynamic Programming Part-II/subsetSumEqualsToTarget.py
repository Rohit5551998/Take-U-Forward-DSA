# mypy: disable-error-code="empty-body"
# QUESTION: Subset sum equals to target
# Given an array of non-negative integers `arr` and an integer `target`, determine whether
# there exists a subset of `arr` whose elements sum exactly to `target`. Return true if
# such a subset exists, otherwise false.
#
# Examples:
# Example 1:
# Input: arr = [5, 2, 1], target = 8
# Output: true
# Explanation: The subset [5, 2, 1] sums to 8.
#
# Example 2:
# Input: arr = [2, 3, 5], target = 4
# Output: false
# Explanation: No subset of [2, 3, 5] sums to 4.


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
    def subset_sum_equals_to_target_brute(self, arr: List[int], target: int) -> bool:
        pass

    def subset_sum_equals_to_target_better(self, arr: List[int], target: int) -> bool:
        pass

    def subset_sum_equals_to_target_optimal(self, arr: List[int], target: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 2, 1]
    target = 8
    print(sol.subset_sum_equals_to_target_optimal(arr, target))
