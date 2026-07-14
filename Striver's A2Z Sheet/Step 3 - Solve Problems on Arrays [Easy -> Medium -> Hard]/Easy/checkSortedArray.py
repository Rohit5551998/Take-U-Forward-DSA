# mypy: disable-error-code="empty-body"
# QUESTION: Check if the Array is Sorted
# Given an array, determine whether it is sorted in non-decreasing order.
# (Extended variant: check if it is sorted AND rotated.)
# Example 1:
# Input: arr = [1, 2, 3, 4, 5]
# Output: True
# Explanation: Each element is >= the previous one.
# Example 2:
# Input: arr = [3, 4, 5, 1, 2]
# Output: True   (sorted and rotated)
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
SKIPPED — a nested-loop comparison is wasteful; the linear scan below is the
natural first solution.

#Better Approach:
SKIPPED — no intermediate tier exists between the linear scan and itself.

#Optimal Approach:
1. Plain sorted check: walk the array, and if any arr[i-1] > arr[i], it is not sorted.
2. Sorted-and-rotated check: count the "drop" positions where arr[i-1] > arr[i]
   (indices taken cyclically). A sorted-rotated array has at most ONE such drop.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A rotation of a sorted array introduces exactly one place where the value
  decreases; counting those drops (cyclically) distinguishes rotated-sorted
  from truly unsorted arrays.
"""

from typing import List


class Solution:
    def check_sorted_brute(self, arr: List[int]) -> bool:
        # SKIP: a nested-loop O(n^2) check adds nothing over the linear scan.
        pass

    def check_sorted_better(self, arr: List[int]) -> bool:
        # SKIP: no distinct middle tier between the linear scan and itself.
        pass

    def check_sorted_optimal(self, arr: List[int]) -> bool:
        return all(arr[i - 1] <= arr[i] for i in range(1, len(arr)))

    def check_sorted_and_rotated_optimal(self, arr: List[int]) -> bool:
        # Count cyclic drops; a sorted-rotated array has at most one.
        count = 0
        for i in range(len(arr)):
            if arr[i - 1] > arr[i]:
                count += 1
        return count <= 1


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 4, 5, 1, 2]
    print(sol.check_sorted_optimal(arr), sol.check_sorted_and_rotated_optimal(arr))
