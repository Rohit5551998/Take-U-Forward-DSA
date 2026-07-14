# mypy: disable-error-code="empty-body"
# QUESTION: Merge Two Sorted Arrays Without Extra Space
# Given two sorted arrays arr1 (size n) and arr2 (size m), merge them so arr1
# holds the first n sorted elements and arr2 holds the remaining m, ideally
# without using extra space.
# Example 1:
# Input: n = 4, arr1 = [1, 4, 8, 10], m = 5, arr2 = [2, 3, 5, 6, 9]
# Output: arr1 = [1, 2, 3, 4], arr2 = [5, 6, 8, 9, 10]
# Explanation: The combined sorted order is 1..10 split across the two arrays.
# Constraints:
# 1 <= n, m <= 10^5
# arr1 and arr2 are individually sorted

"""
#Brute Force:
1. Merge both arrays into a third array using the standard two-pointer merge.
2. Copy the first n elements back into arr1 and the rest into arr2.
TC -> O(2*(n+m)), SC -> O(n+m)

#Better Approach (Swap-then-Sort):
1. Point to the end of arr1 and the start of arr2. While arr1[end] > arr2[start],
   swap them and move inward — this pushes the largest of arr1 into arr2 and pulls
   smaller values into arr1.
2. Once no swap is needed the "cross-over" values are placed; sort each array.
TC -> O(min(n,m)) + O(n log n) + O(m log m), SC -> O(1)

#Optimal Approach (Gap / Shell method):
1. Treat the two arrays as one virtual array of length n+m and start with
   gap = ceil((n+m)/2).
2. Compare and swap elements gap apart across the virtual boundary (indices >= n
   map into arr2), sweeping left to right.
3. Halve the gap (ceil) each round until a full pass at gap 1 leaves everything
   sorted.
TC -> O((n+m) log(n+m)), SC -> O(1)

#KEY INSIGHT:
- Comparing elements a shrinking "gap" apart across the concatenated view sorts
  both arrays in place, avoiding the third array entirely.
"""

from typing import List, Tuple


class Solution:
    def merge_brute(
        self, n: int, m: int, arr1: List[int], arr2: List[int]
    ) -> Tuple[List[int], List[int]]:
        merged: List[int] = []
        left, right = 0, 0
        while left < n and right < m:
            if arr1[left] <= arr2[right]:
                merged.append(arr1[left])
                left += 1
            else:
                merged.append(arr2[right])
                right += 1
        while left < n:
            merged.append(arr1[left])
            left += 1
        while right < m:
            merged.append(arr2[right])
            right += 1
        for i in range(len(merged)):
            if i < n:
                arr1[i] = merged[i]
            else:
                arr2[i - n] = merged[i]
        return arr1, arr2

    def merge_better(
        self, n: int, m: int, arr1: List[int], arr2: List[int]
    ) -> Tuple[List[int], List[int]]:
        end, start = len(arr1) - 1, 0
        while end >= 0 and start < len(arr2):
            if arr1[end] > arr2[start]:
                arr1[end], arr2[start] = arr2[start], arr1[end]
                end -= 1
                start += 1
            else:
                break
        arr1.sort()
        arr2.sort()
        return arr1, arr2

    def swap_arr(self, a: List[int], b: List[int], i: int, j: int) -> None:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]

    def merge_optimal(
        self, n: int, m: int, arr1: List[int], arr2: List[int]
    ) -> Tuple[List[int], List[int]]:
        total = n + m
        gap = (total // 2) + (total % 2)
        while gap > 0:
            left = 0
            right = left + gap
            while right < total:
                if left < n and right >= n:
                    self.swap_arr(arr1, arr2, left, right - n)
                elif left >= n:
                    self.swap_arr(arr2, arr2, left - n, right - n)
                else:
                    self.swap_arr(arr1, arr1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)
        return arr1, arr2


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge_optimal(4, 5, [1, 4, 8, 10], [2, 3, 5, 6, 9]))
