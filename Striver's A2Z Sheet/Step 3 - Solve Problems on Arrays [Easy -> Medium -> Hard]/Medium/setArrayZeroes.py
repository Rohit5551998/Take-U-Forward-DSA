# mypy: disable-error-code="empty-body"
# QUESTION: Set Matrix Zeroes
# Given an m x n matrix, if any cell is 0 set its entire row and column to 0.
# Do it in-place.
# Example 1:
# Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# Explanation: The 0 at (1,1) zeroes row 1 and column 1.
# Constraints:
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1

"""
#Brute Force:
1. For every original 0, mark all non-zero cells in its row and column with a
   sentinel (-1) so we don't confuse them with genuine input zeroes.
2. In a second pass turn every -1 into 0.
TC -> O((n*m)*(n+m)) + O(n*m), SC -> O(1)

#Better Approach:
1. Use a row[] array and col[] array of flags.
2. First pass: for every 0 cell mark row[i]=0 and col[j]=0.
3. Second pass: zero any cell whose row or column flag is set.
TC -> O(2*n*m), SC -> O(n+m)

#Optimal Approach:
1. Reuse the matrix's own first row and first column as the flag arrays; use two
   scalars to remember whether the first row / first column themselves must be
   zeroed (since matrix[0][0] is shared).
2. Mark flags in the first row/column for zeros found in the inner submatrix,
   then zero the submatrix based on those flags.
3. Finally zero the first row and/or first column using the two scalars.
TC -> O(2*n*m) + O(2*(n+m)), SC -> O(1)

#KEY INSIGHT:
- The first row and column can double as the flag storage, dropping the extra
  O(n+m) space to O(1) — only the shared corner needs two dedicated scalars.
"""

from typing import List


class Solution:
    def mark_row(self, matrix: List[List[int]], m: int, i: int) -> None:
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    def mark_col(self, matrix: List[List[int]], n: int, j: int) -> None:
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    def set_zeroes_brute(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.mark_row(matrix, m, i)
                    self.mark_col(matrix, n, j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        return matrix

    def set_zeroes_better(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        row, col = [1] * n, [1] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i], col[j] = 0, 0
        for i in range(n):
            for j in range(m):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        return matrix

    def set_zeroes_optimal(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        first_col, first_row = 1, 1
        for i in range(n):
            if matrix[i][0] == 0:
                first_col = 0
                break
        for j in range(m):
            if matrix[0][j] == 0:
                first_row = 0
                break
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row == 0:
            for j in range(m):
                matrix[0][j] = 0
        if first_col == 0:
            for i in range(n):
                matrix[i][0] = 0
        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.set_zeroes_optimal([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
