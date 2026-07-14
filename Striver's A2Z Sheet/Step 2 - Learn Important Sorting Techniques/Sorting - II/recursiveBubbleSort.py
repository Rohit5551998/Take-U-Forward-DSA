# mypy: disable-error-code="empty-body"
# QUESTION: Recursive Bubble Sort
# Given an array of N integers, sort it in ascending order using a recursive
# implementation of Bubble Sort. Instead of an outer loop, recursion shrinks the
# problem: one pass bubbles the largest element of arr[0..n-1] to index n-1, then
# the same routine is called on the first n-1 elements.
#
# Example 1:
# Input: arr = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
# Explanation: Each recursive call performs one bubbling pass and reduces the
# effective size by one until a single element remains.
#
# Constraints:
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^6

"""
#Brute Force:
SKIPPED — recursive bubble sort is itself the baseline; no simpler variant.

#Better Approach:
SKIPPED — no distinct intermediate approach.

#Optimal Approach:
1. Recursive routine takes the current effective size n.
2. Base case: n == 1 (or 0) -> nothing to sort, return.
3. Do one pass over j in [1..n-1]; if arr[j] < arr[j-1], swap and mark didSwap.
   This bubbles the largest of arr[0..n-1] to index n-1.
4. Early exit: if a full pass made no swap, the array is already sorted -> return.
5. Otherwise recurse on size n-1 to sort the remaining prefix.
TC -> O(n^2) average/worst, O(n) best (already sorted), SC -> O(n) recursion stack

#KEY INSIGHT:
- The recursion replaces the outer loop; the didSwap early-exit still delivers the
  O(n) best case. It uses O(n) stack depth, unlike the O(1)-space iterative form.
"""

from typing import List


class Solution:
    def recursiveBubbleSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: recursive bubble sort is the baseline itself
        pass

    def recursiveBubbleSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach
        pass

    def _bubble(self, arr: List[int], n: int) -> None:
        if n <= 1:
            return
        didSwap = False
        for j in range(1, n):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                didSwap = True
        if not didSwap:  # already sorted -> stop recursing
            return
        self._bubble(arr, n - 1)

    def recursiveBubbleSort_optimal(self, arr: List[int]) -> List[int]:
        self._bubble(arr, len(arr))
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.recursiveBubbleSort_optimal([13, 46, 24, 52, 20, 9]))
