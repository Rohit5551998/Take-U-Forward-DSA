# mypy: disable-error-code="empty-body"
# QUESTION: Insertion Sort
# Given an array of N integers, sort it in ascending order using the Insertion Sort
# algorithm. Insertion Sort builds the sorted array one element at a time by taking
# each element and inserting it into its correct position within the already-sorted
# prefix.
#
# Example 1:
# Input: arr = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
# Explanation: Each element is picked and shifted left past all larger elements
# until it sits in its correct spot within the sorted prefix.
#
# Constraints:
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^6

"""
#Brute Force:
SKIPPED — insertion sort is itself the simple baseline; no simpler variant.

#Better Approach:
SKIPPED — no distinct intermediate approach.

#Optimal Approach:
1. Treat arr[0..i-1] as the sorted prefix; outer loop i runs from 1 to n-1.
2. For each i, walk j down from i; while j > 0 and arr[j-1] > arr[j], swap the pair.
   This slides arr[i] leftward past every larger element into its correct slot.
3. Stop the inner walk as soon as arr[j-1] <= arr[j] — the element is placed.
4. After all i, the whole array is sorted.
TC -> O(n^2) average/worst, O(n) best (already sorted), SC -> O(1)

#KEY INSIGHT:
- Insertion sort is adaptive: on nearly-sorted data the inner while-loop exits
  almost immediately, giving near-linear time. It is stable and sorts in place,
  making it the go-to for small or almost-sorted arrays.
"""

from typing import List


class Solution:
    def insertionSort_brute(self, arr: List[int]) -> List[int]:
        # SKIP: insertion sort is the simple baseline itself
        pass

    def insertionSort_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct intermediate approach
        pass

    def insertionSort_optimal(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.insertionSort_optimal([13, 46, 24, 52, 20, 9]))
