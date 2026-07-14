# mypy: disable-error-code="empty-body"
# QUESTION: Reverse an Array using Recursion
# Given an array, reverse it in place using recursion.
# Example 1:
# Input: arr = [1, 2, 3, 4, 5, 6]
# Output: [6, 5, 4, 3, 2, 1]
# Constraints:
# 1 <= len(arr) <= 100000

"""
#Brute Force:
1. Two-pointer iterative swap from both ends towards the middle.
TC -> O(n), SC -> O(1)

#Better Approach:
SKIPPED - no distinct intermediate approach.

#Optimal Approach:
1. Recursive two-pointer: swap arr[l] and arr[r], then recurse (l+1, r-1).
2. Base case: stop when l >= r.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- Each recursive frame fixes one symmetric pair (l, r); when the pointers cross, the
  whole array is reversed.
"""

from typing import List


class Solution:
    def reverse_brute(self, arr: List[int]) -> None:
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def reverse_better(self, arr: List[int]) -> None:
        # SKIP: no distinct intermediate approach.
        pass

    def reverse_optimal(self, arr: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        self.reverse_optimal(arr, left + 1, right - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    sol.reverse_optimal(nums, 0, len(nums) - 1)
    print(nums)
