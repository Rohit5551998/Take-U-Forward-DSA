# mypy: disable-error-code="empty-body"
# QUESTION: Median of 2 sorted arrays
# Given two sorted arrays arr1 and arr2 of size m and n respectively,
# return the median of the two sorted arrays. The median is defined as
# the middle value of a sorted list of numbers. If the total length of
# the combined sorted list (m + n) is even, the median is the average of
# the two middle values.
#
# Examples:
# Example 1:
# Input: arr1 = [1, 3], arr2 = [2]
# Output: 2.0
# Explanation: Merged sorted array = [1, 2, 3]. Median is 2.
#
# Example 2:
# Input: arr1 = [1, 2], arr2 = [3, 4]
# Output: 2.5
# Explanation: Merged sorted array = [1, 2, 3, 4]. Median = (2 + 3) / 2 = 2.5.
#
# Constraints:
# 0 <= m, n <= 1000, 1 <= m + n <= 2000
# -10^6 <= arr1[i], arr2[i] <= 10^6
#
# Follow up: The naive merge is O(m+n). Can you achieve O(log(min(m, n)))?


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
    def median_of_two_sorted_arrays_brute(self, arr1: List[int], arr2: List[int]) -> float:
        pass

    def median_of_two_sorted_arrays_better(self, arr1: List[int], arr2: List[int]) -> float:
        pass

    def median_of_two_sorted_arrays_optimal(self, arr1: List[int], arr2: List[int]) -> float:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 3]
    arr2 = [2]
    print(sol.median_of_two_sorted_arrays_optimal(arr1, arr2))
