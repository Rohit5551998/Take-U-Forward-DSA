# mypy: disable-error-code="empty-body"
# QUESTION: Next Greater Element
# Given an array arr of size n, find the next greater element for each element in the array in
# the order of their appearance. The next greater element of an element in the array is the
# nearest element on the right that is greater than the current element. If there does not exist
# a next greater element for the current element, then the next greater element for that element
# is -1.
#
# Examples:
# Example 1:
# Input: arr = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: In the array, the next larger element to 1 is 3, for 3 it is 4, for 2 it is 4, and
# for 4 it is -1, since it does not exist.
#
# Example 2:
# Input: arr = [6, 8, 0, 1, 3]
# Output: [8, -1, 1, 3, -1]
# Explanation: The next larger element to 6 is 8; for 8 there is no larger element, hence -1; for
# 0 it is 1; for 1 it is 3; and for 3 there is no larger element on the right, hence -1.
#
# Constraints:
# - 1 <= n <= 10^5
# - 0 <= arr[i] <= 10^9


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
    def next_greater_element_brute(self, arr: List[int]) -> List[int]:
        pass

    def next_greater_element_better(self, arr: List[int]) -> List[int]:
        pass

    def next_greater_element_optimal(self, arr: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 2, 4]
    print(sol.next_greater_element_optimal(arr))
