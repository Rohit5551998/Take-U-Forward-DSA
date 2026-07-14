# mypy: disable-error-code="empty-body"
# QUESTION: Selection Sort
# Given an array of N integers, sort it in ascending order using the Selection Sort
# algorithm. Selection Sort repeatedly selects the minimum element from the unsorted
# portion of the array and places it at the front of that portion.
#
# Example 1:
# Input: arr = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
# Explanation: The smallest element (9) is placed first, then 13, and so on until sorted.
#
# Constraints:
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^6

"""
#Brute Force:
SKIPPED — Selection Sort has a single canonical formulation; there is no naive
predecessor that is meaningfully worse yet still "selection sort".

#Better Approach:
SKIPPED — no distinct intermediate approach exists for selection sort.

#Optimal Approach:
1. Outer loop i runs from 0 to n-2: it fixes the boundary of the sorted prefix.
2. Assume the minimum of the unsorted suffix [i..n-1] is at index i (mini = i).
3. Inner loop j scans [i..n-1]; whenever arr[j] < arr[mini], update mini = j.
4. After the scan, swap arr[i] with arr[mini] so the true minimum lands at position i.
5. Each pass grows the sorted prefix by one, so after n-1 passes the array is sorted.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Selection sort does the minimum number of SWAPS (at most n-1) among the simple
  quadratic sorts, because it commits to one swap per pass regardless of comparisons.
  It is NOT stable in this swap-based form.
"""

from typing import List


class Solution:
    def selectionSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: no naive predecessor distinct from the canonical selection sort
        pass

    def selectionSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach for selection sort
        pass

    def selectionSort_optimal(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1):
            mini = i
            for j in range(i, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.selectionSort_optimal([13, 46, 24, 52, 20, 9]))
