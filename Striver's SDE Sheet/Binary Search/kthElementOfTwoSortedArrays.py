# mypy: disable-error-code="empty-body"
# QUESTION: Kth element of 2 sorted arrays
# Given two sorted arrays `a` and `b` of size m and n respectively, find
# the k-th element (1-indexed) of the final sorted array obtained by
# merging them.
#
# Examples:
# Example 1:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th
# element of this array is 6.
#
# Example 2:
# Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
# Output: 256
# Explanation: The final sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445,
# 770, 892]. The 7th element of this array is 256.


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
    def kth_element_of_two_sorted_arrays_brute(self, a: List[int], b: List[int], k: int) -> int:
        pass

    def kth_element_of_two_sorted_arrays_better(self, a: List[int], b: List[int], k: int) -> int:
        pass

    def kth_element_of_two_sorted_arrays_optimal(self, a: List[int], b: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(sol.kth_element_of_two_sorted_arrays_optimal(a, b, k))
