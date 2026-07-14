# mypy: disable-error-code="empty-body"
# QUESTION: Largest Element in an Array
# Given an array of integers, return the value of the largest element.
# Example 1:
# Input: arr = [5, 4, 10, 3, 1, 6, 17, 2]
# Output: 17
# Explanation: 17 is the maximum value in the array.
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
1. Sort the array in ascending order.
2. The last element is the largest.
TC -> O(n log n), SC -> O(1)

#Better Approach:
SKIPPED — a single linear scan is already optimal; there is no meaningful middle tier.

#Optimal Approach:
1. Track a running maximum, initialized to the first element.
2. Walk the array once; whenever an element exceeds the running max, update it.
3. Return the running max.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The maximum is a fold over the array: you only need to remember the best value
  seen so far, so one pass with O(1) extra state suffices.
"""

from typing import List


class Solution:
    def largest_element_brute(self, arr: List[int]) -> int:
        arr = sorted(arr)
        return arr[-1]

    def largest_element_better(self, arr: List[int]) -> int:
        # SKIP: single linear scan is already optimal; no distinct better tier.
        pass

    def largest_element_optimal(self, arr: List[int]) -> int:
        maximum = arr[0]
        for i in range(len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 4, 10, 3, 1, 6, 17, 2]
    print(sol.largest_element_optimal(arr))
