# mypy: disable-error-code="empty-body"
# QUESTION: Next Smaller Element
# Given an array of integers arr, find the Next Smaller Element (NSE) for every element in the
# array. The Next Smaller Element of an element x is the first element to the right of x in the
# array that is strictly smaller than x. If no such element exists, the answer for x is -1.
# Return an array where the i-th value is the NSE of arr[i].
#
# Examples:
# Example 1:
# Input: arr = [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]
# Explanation:
# - For 4, the first smaller element to its right is 2.
# - For 8, the first smaller element to its right is 5.
# - For 5, the first smaller element to its right is 2.
# - For 2, no smaller element exists to its right -> -1.
# - For 25, there is no element to its right -> -1.
#
# Example 2:
# Input: arr = [10, 9, 8, 7]
# Output: [9, 8, 7, -1]
# Explanation: The array is strictly decreasing, so each element's immediate right neighbour is
# its next smaller element; the last element has nothing to its right -> -1.


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
    def next_smaller_element_brute(self, arr: List[int]) -> List[int]:
        pass

    def next_smaller_element_better(self, arr: List[int]) -> List[int]:
        pass

    def next_smaller_element_optimal(self, arr: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [4, 8, 5, 2, 25]
    print(sol.next_smaller_element_optimal(arr))
