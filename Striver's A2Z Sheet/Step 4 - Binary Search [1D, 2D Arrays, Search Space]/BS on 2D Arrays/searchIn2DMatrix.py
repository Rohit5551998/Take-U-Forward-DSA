# mypy: disable-error-code="empty-body"
# QUESTION: Search in a 2D Matrix
# You are given an m x n integer matrix with two properties:
#   1. Each row is sorted in non-decreasing order.
#   2. The first integer of each row is greater than the last integer of the
#      previous row.
# Given an integer target, return True if target is in the matrix, else False.
# Example 1:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]], target = 8
# Output: True
# Explanation: 8 is present at matrix[1][3].
# Constraints:
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

"""
#Brute Force:
1. Traverse every cell with two nested loops (row i, column j).
2. If matrix[i][j] == target return True; after the full scan return False.
TC -> O(N*M), SC -> O(1)

#Better Approach:
1. The first element of each row is bigger than the last of the previous row, so
   each row is a sorted contiguous range. A row can hold the target only if
   matrix[i][0] <= target <= matrix[i][m-1].
2. Find that candidate row in O(N), then binary search inside it in O(logM).
TC -> O(N + logM), SC -> O(1)

#Optimal Approach:
1. Because rows are sorted AND row-boundaries are ordered, the whole matrix reads
   as one sorted 1D array of length N*M when flattened row by row.
2. Binary search over indices [0, N*M-1]; map a flat index mid to 2D coordinates
   with row = mid // M and col = mid % M, then compare matrix[row][col] to target.
TC -> O(log(N*M)), SC -> O(1)

#KEY INSIGHT:
- The two ordering guarantees make the matrix a single sorted sequence, so the
  index math mid//M, mid%M lets one binary search cover it end to end.
"""

from typing import List


class Solution:
    def search_matrix_brute(self, matrix: List[List[int]], target: int) -> bool:
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

    def search_matrix_better(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                return self._binary_search(matrix[i], target)
        return False

    def search_matrix_optimal(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n * m - 1
        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.search_matrix_optimal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
