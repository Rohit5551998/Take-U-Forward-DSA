# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Sum Increasing Subsequence
# Given an array arr[] of positive integers, find the maximum possible
# sum of a subsequence such that the elements of the subsequence are in
# strictly increasing order. The subsequence does not need to be
# contiguous. You must choose elements such that the resulting sequence
# is strictly increasing AND the sum of the chosen elements is maximum.
#
# Examples:
# Example 1:
# Input: arr = [1, 101, 2, 3, 100, 4, 5]
# Output: 106
# Explanation: The increasing subsequence with max sum is [1, 2, 3, 100],
# sum = 106.
#
# Example 2:
# Input: arr = [3, 4, 5, 10]
# Output: 22
# Explanation: The whole array is increasing; sum = 3 + 4 + 5 + 10 = 22.
#
# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5


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
    def maximum_sum_increasing_subsequence_brute(self, arr: List[int]) -> int:
        pass

    def maximum_sum_increasing_subsequence_better(self, arr: List[int]) -> int:
        pass

    def maximum_sum_increasing_subsequence_optimal(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 101, 2, 3, 100, 4, 5]
    print(sol.maximum_sum_increasing_subsequence_optimal(arr))
