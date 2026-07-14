# mypy: disable-error-code="empty-body"
# QUESTION: Sort a K-Sorted (Nearly Sorted) Array
# Given an array arr of n elements, where each element is at most k positions away
# from its target position in the sorted order, sort the array efficiently.
# Sorting such a nearly-sorted array should be faster than a full comparison sort.
#
# Example 1:
# Input: arr = [6, 5, 3, 2, 8, 10, 9], k = 3
# Output: [2, 3, 5, 6, 8, 9, 10]
# Explanation: Every element is within 3 positions of its sorted location.
#
# Example 2:
# Input: arr = [10, 9, 8, 7, 4, 70, 60, 50], k = 4
# Output: [4, 7, 8, 9, 10, 50, 60, 70]
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= k < n
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
    def sortKSortedArray_brute(self, arr: List[int], k: int) -> List[int]:
        pass

    def sortKSortedArray_better(self, arr: List[int], k: int) -> List[int]:
        pass

    def sortKSortedArray_optimal(self, arr: List[int], k: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.sortKSortedArray_optimal([6, 5, 3, 2, 8, 10, 9], 3))
