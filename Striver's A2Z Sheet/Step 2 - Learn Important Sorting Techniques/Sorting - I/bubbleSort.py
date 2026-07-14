# mypy: disable-error-code="empty-body"
# QUESTION: Bubble Sort
# Given an array of N integers, sort it in ascending order using the Bubble Sort
# algorithm. Bubble Sort repeatedly steps through the list, compares adjacent
# elements and swaps them if they are in the wrong order, "bubbling" the largest
# unsorted element to the end on each pass.
#
# Example 1:
# Input: arr = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
# Explanation: On each pass the largest remaining element moves to its final
# position at the end of the unsorted region.
#
# Constraints:
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^6

"""
#Brute Force:
SKIPPED — bubble sort is itself the naive baseline; there is no simpler variant.

#Better Approach:
SKIPPED — no distinct intermediate approach.

#Optimal Approach:
1. Outer loop i runs from n-1 down to 1: the range [0..i] is the still-unsorted region.
2. Track a didSwap flag, reset to False at the start of each pass.
3. Inner loop j scans [1..i]; if arr[j] < arr[j-1], swap them and set didSwap = True.
   This pushes the largest element in [0..i] to index i.
4. If a full pass performs no swap (didSwap is False), the array is already sorted —
   break early. This is the optimization that gives best-case O(n).
TC -> O(n^2) average/worst, O(n) best (already sorted), SC -> O(1)

#KEY INSIGHT:
- The early-exit didSwap flag is what separates bubble sort from selection sort:
  a single clean pass proves sortedness, giving O(n) on nearly-sorted input.
  Bubble sort is stable (equal elements never jump past each other).
"""

from typing import List


class Solution:
    def bubbleSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: bubble sort is the naive baseline itself
        pass

    def bubbleSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach
        pass

    def bubbleSort_optimal(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1, 0, -1):
            didSwap = False
            for j in range(1, i + 1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    didSwap = True
            if not didSwap:  # array already sorted -> stop early
                break
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.bubbleSort_optimal([13, 46, 24, 52, 20, 9]))
