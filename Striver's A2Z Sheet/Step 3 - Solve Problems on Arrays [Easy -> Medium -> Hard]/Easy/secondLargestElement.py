# mypy: disable-error-code="empty-body"
# QUESTION: Second Largest Element in an Array without sorting
# Given an array, find the second largest distinct element. If it does not
# exist (all elements equal, or array too small), return -1.
# Example 1:
# Input: arr = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: 35 is largest, 34 is the second largest distinct value.
# Example 2:
# Input: arr = [10, 10, 10]
# Output: -1
# Explanation: No second distinct value exists.
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
1. Sort the array in ascending order.
2. Scan from the end for the first value strictly less than the last (largest).
TC -> O(n log n), SC -> O(1)

#Better Approach:
1. First pass: find the largest element.
2. Second pass: find the max element that is strictly less than the largest.
TC -> O(2n), SC -> O(1)

#Optimal Approach:
1. Keep two running values: max and secondMax (secondMax starts at -1).
2. For each element, if it beats max, push old max down into secondMax and update max.
3. Else if it beats secondMax AND is not equal to max, update secondMax.
4. Return secondMax.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The "!= max" guard keeps secondMax strictly distinct from the maximum, so
  duplicates of the largest value never masquerade as the second largest.
"""

from typing import List


class Solution:
    def second_largest_brute(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return -1
        arr = sorted(arr)
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] != arr[-1]:
                return arr[i]
        return -1

    def second_largest_better(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return -1
        largest = max(arr)
        second = -1
        for i in range(len(arr)):
            if arr[i] != largest and arr[i] > second:
                second = arr[i]
        return second

    def second_largest_optimal(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return -1
        maximum = arr[0]
        secondMax = -1
        for i in range(1, len(arr)):
            if arr[i] > maximum:
                secondMax = maximum
                maximum = arr[i]
            if arr[i] > secondMax and arr[i] != maximum:
                secondMax = arr[i]
        return secondMax


if __name__ == "__main__":
    sol = Solution()
    arr = [12, 35, 1, 10, 34, 1]
    print(sol.second_largest_optimal(arr))
