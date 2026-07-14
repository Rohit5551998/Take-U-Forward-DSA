# mypy: disable-error-code="empty-body"
# QUESTION: Find a Peak Element II
# A peak element in a 2D grid is an element strictly greater than all of its
# adjacent neighbours (up, down, left, right). Given an m x n matrix mat where no
# two adjacent cells are equal, return the coordinates [i, j] of ANY peak.
# You may assume the whole grid is surrounded by an outer border of -1, so an
# out-of-bounds neighbour never blocks a cell from being a peak.
# Example 1:
# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: 30 at (1,1) is greater than its neighbours 20, 21, 14, 16.
# Constraints:
# 1 <= m, n <= 500
# 1 <= mat[i][j]
# No two adjacent cells are equal.

"""
#Brute Force:
1. For every cell, check its four neighbours (treating out-of-bounds as -1).
2. Return the first cell strictly greater than all present neighbours.
TC -> O(N*M), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; the jump from full scan to binary-search-on-
columns is the direct optimization.

#Optimal Approach:
1. Binary search over the COLUMN index range [0, M-1]; let mid be the middle column.
2. In column mid, find the row holding the column's maximum element (maxIndex).
3. Compare that maximum with its horizontal neighbours left (mid-1) and right
   (mid+1); out-of-bounds neighbours are treated as -1.
4. If it beats both neighbours it is a 2D peak — return [maxIndex, mid].
5. If the left neighbour is larger, a peak must lie to the left, so high = mid-1;
   otherwise move right with low = mid+1.
TC -> O(logM * N), SC -> O(1)

#KEY INSIGHT:
- Taking the max of a column guarantees that cell already beats its vertical
  neighbours; then a 1D peak-style comparison on the horizontal axis tells us
  which half of columns still contains a peak, halving the search each step.
"""

import math
from typing import List


class Solution:
    def peak_grid_brute(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        def value(i: int, j: int) -> float:
            if 0 <= i < n and 0 <= j < m:
                return mat[i][j]
            return -math.inf

        for i in range(n):
            for j in range(m):
                cur = mat[i][j]
                if (
                    cur > value(i - 1, j)
                    and cur > value(i + 1, j)
                    and cur > value(i, j - 1)
                    and cur > value(i, j + 1)
                ):
                    return [i, j]
        return [-1, -1]

    def peak_grid_better(self, mat: List[List[int]]) -> List[int]:
        # SKIP: no distinct better tier between full scan and column binary search.
        pass

    def _max_row_in_column(self, mat: List[List[int]], col: int) -> int:
        n = len(mat)
        max_el, max_index = -1, -1
        for i in range(n):
            if mat[i][col] > max_el:
                max_el = mat[i][col]
                max_index = i
        return max_index

    def peak_grid_optimal(self, mat: List[List[int]]) -> List[int]:
        m = len(mat[0])
        low, high = 0, m - 1
        while low <= high:
            mid = low + (high - low) // 2
            max_index = self._max_row_in_column(mat, mid)
            max_el = mat[max_index][mid]
            left = mat[max_index][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_index][mid + 1] if mid + 1 < m else -1
            if max_el > left and max_el > right:
                return [max_index, mid]
            if max_el < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.peak_grid_optimal([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
