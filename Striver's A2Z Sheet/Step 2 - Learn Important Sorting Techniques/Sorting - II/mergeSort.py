# mypy: disable-error-code="empty-body"
# QUESTION: Merge Sort
# Given an array of N integers, sort it in ascending order using the Merge Sort
# algorithm. Merge Sort is a divide-and-conquer algorithm: it recursively splits the
# array into two halves, sorts each half, and merges the two sorted halves into one
# sorted array.
#
# Example 1:
# Input: arr = [4, 2, 1, 6, 7]
# Output: [1, 2, 4, 6, 7]
# Explanation: The array is split down to single elements, then merged pairwise in
# sorted order until the full array is reassembled sorted.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= arr[i] <= 10^9

"""
#Brute Force:
SKIPPED — merge sort is a single canonical divide-and-conquer algorithm; there is
no simpler variant that is still "merge sort".

#Better Approach:
SKIPPED — no distinct intermediate approach.

#Optimal Approach:
1. mergeSort(low, high): base case is low >= high (0 or 1 elements -> already sorted).
2. Compute mid = (low + high) // 2, recurse on [low..mid] and [mid+1..high].
3. merge(low, mid, high): use two pointers left=low, right=mid+1 into the two sorted
   halves; repeatedly copy the smaller front element into a temp buffer.
4. Drain whichever half still has leftovers into temp.
5. Copy temp back into arr[low..high]. Using <= when comparing keeps it stable.
TC -> O(n log n) all cases, SC -> O(n) for the temp buffer + O(log n) recursion stack

#KEY INSIGHT:
- Merge sort guarantees O(n log n) regardless of input order (no worst-case blowup
  like quicksort) and is stable, at the cost of O(n) extra space for merging.
"""

from typing import List


class Solution:
    def mergeSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: merge sort is a single canonical algorithm
        pass

    def mergeSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach
        pass

    def _merge(self, arr: List[int], low: int, mid: int, high: int) -> None:
        temp: List[int] = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def _mergeSort(self, arr: List[int], low: int, high: int) -> None:
        if low >= high:
            return
        mid = (low + high) // 2
        self._mergeSort(arr, low, mid)
        self._mergeSort(arr, mid + 1, high)
        self._merge(arr, low, mid, high)

    def mergeSort_optimal(self, arr: List[int]) -> List[int]:
        self._mergeSort(arr, 0, len(arr) - 1)
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeSort_optimal([4, 2, 1, 6, 7]))
