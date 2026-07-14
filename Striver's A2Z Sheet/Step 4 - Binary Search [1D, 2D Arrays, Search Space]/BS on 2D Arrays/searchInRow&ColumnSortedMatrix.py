# mypy: disable-error-code="empty-body"
# QUESTION: Search in a 2D Matrix II
# You are given an m x n integer matrix with two properties:
#   1. Each row is sorted in ascending order (left to right).
#   2. Each column is sorted in ascending order (top to bottom).
# Given an integer target, return True if target is in the matrix, else False.
# (Unlike "Search in a 2D Matrix", rows here are NOT one flat sorted sequence.)
# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
#                  [10,13,14,17,24],[18,21,23,26,30]], target = 32
# Output: False
# Explanation: 32 does not appear anywhere in the matrix.
# Constraints:
# 1 <= m, n <= 300
# -10^9 <= matrix[i][j], target <= 10^9

"""
#Brute Force:
1. Traverse every cell with two nested loops and compare to target.
2. Return True on a match, else False after the full scan.
TC -> O(N*M), SC -> O(1)

#Better Approach:
1. Each row is individually sorted, so binary search each of the N rows for target.
2. Return True as soon as one row contains it, else False.
TC -> O(N * logM), SC -> O(1)

#Optimal Approach:
1. Start from the top-right corner (row = 0, col = M-1). This cell is the largest
   in its row and the smallest in its column, so a comparison eliminates a whole
   row or a whole column each step.
2. If matrix[row][col] == target return True.
3. If matrix[row][col] > target the target cannot be in this column (everything
   below is larger), so move left: col -= 1.
4. If matrix[row][col] < target the target cannot be in this row (everything to
   the left is smaller), so move down: row += 1.
5. Stop when we walk off the grid; return False.
TC -> O(N + M), SC -> O(1)

#KEY INSIGHT:
- The top-right (or bottom-left) corner is a pivot where "greater" and "less"
  point in orthogonal directions, letting each comparison discard an entire
  row or column.
"""

from typing import List


class Solution:
    def search_matrix_ii_brute(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False

    def _binary_search(self, arr: List[int], target: int) -> bool:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def search_matrix_ii_better(self, matrix: List[List[int]], target: int) -> bool:
        return any(self._binary_search(row, target) for row in matrix)

    def search_matrix_ii_optimal(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m - 1
        while row < n and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            if value < target:
                row += 1
            else:
                col -= 1
        return False


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(sol.search_matrix_ii_optimal(grid, 32))
