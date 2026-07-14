# mypy: disable-error-code="empty-body"
# QUESTION: Recursive Insertion Sort
# Given an array of N integers, sort it in ascending order using a recursive
# implementation of Insertion Sort. Instead of an outer loop over the array,
# recursion advances the index: the routine assumes arr[0..i-1] is already sorted,
# inserts arr[i] into its correct position within that prefix, then recurses on i+1.
#
# Example 1:
# Input: arr = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
# Explanation: Each recursive call inserts the element at index i into the sorted
# prefix arr[0..i-1], then moves on to the next index until the array is sorted.
#
# Constraints:
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^6

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
    def recursiveInsertionSort_brute(self, arr: List[int]) -> List[int]:
        pass

    def recursiveInsertionSort_better(self, arr: List[int]) -> List[int]:
        pass

    def recursiveInsertionSort_optimal(self, arr: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.recursiveInsertionSort_optimal([13, 46, 24, 52, 20, 9]))
