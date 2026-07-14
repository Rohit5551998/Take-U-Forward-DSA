# mypy: disable-error-code="empty-body"
# QUESTION: Quick Sort
# Given an array of N integers, sort it in ascending order using the Quick Sort
# algorithm. Quick Sort is a divide-and-conquer algorithm: it picks a pivot,
# partitions the array so that elements smaller than the pivot come before it and
# larger ones after it, then recursively sorts the two partitions.
#
# Example 1:
# Input: arr = [4, 6, 2, 5, 7, 9, 1, 3]
# Output: [1, 2, 3, 4, 5, 6, 7, 9]
# Explanation: The pivot is placed at its final sorted index each partition step;
# recursion then sorts the left and right sub-arrays around it.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= arr[i] <= 10^9

"""
#Brute Force:
SKIPPED — quick sort is a single canonical divide-and-conquer algorithm.

#Better Approach:
SKIPPED — no distinct intermediate approach.

#Optimal Approach:
1. quickSort(low, high): base case low >= high (0 or 1 element).
2. partition(low, high): choose pivot = arr[low]. Advance i from low while
   arr[i] <= pivot; retreat j from high while arr[j] > pivot.
3. While i < j, swap arr[i] and arr[j] so smaller elements gather on the left and
   larger on the right.
4. When i and j cross, swap the pivot (arr[low]) with arr[j]; j is now the pivot's
   final sorted position — return j.
5. Recurse on [low..j-1] and [j+1..high].
TC -> O(n log n) average, O(n^2) worst (already-sorted with end pivot), SC -> O(log n)
recursion stack; sorts in place with no extra array.

#KEY INSIGHT:
- Quick sort sorts in place (no O(n) merge buffer) and is usually the fastest in
  practice due to cache locality, but its worst case is O(n^2) when the pivot is
  consistently the min/max. Randomized/median pivots avoid that. It is NOT stable.
"""

from typing import List


class Solution:
    def quickSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: quick sort is a single canonical algorithm
        pass

    def quickSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach
        pass

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while j > low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def _quickSort(self, arr: List[int], low: int, high: int) -> None:
        if low >= high:
            return
        p = self._partition(arr, low, high)
        self._quickSort(arr, low, p - 1)
        self._quickSort(arr, p + 1, high)

    def quickSort_optimal(self, arr: List[int]) -> List[int]:
        self._quickSort(arr, 0, len(arr) - 1)
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.quickSort_optimal([4, 6, 2, 5, 7, 9, 1, 3]))
