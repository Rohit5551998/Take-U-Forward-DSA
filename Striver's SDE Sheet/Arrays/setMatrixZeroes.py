# QUESTION: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and
# column to 0's. You must do it in place (without allocating a separate
# matrix for the result).
#
# Examples:
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Explanation: Since matrix[1][1] = 0, the 2nd column and 2nd row are set to 0.
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# Explanation: matrix[0][0] = 0 and matrix[0][3] = 0, so the 1st row, 1st
# column, and 4th column are set to 0.
#
# Constraints:
# m == matrix.length, n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
# Follow up: O(m*n) space is trivial. O(m + n) space is the common improvement.
# Can you devise a constant-space solution (use the first row + first column
# as marker storage)?


"""
#Brute Force:
1. The naive idea is "whenever I see a 0, blank out its whole row and column",
   but doing that with literal 0s would create new 0s that trigger more
   blanking. So instead use a sentinel value that cannot occur in the input.
2. Scan every cell; when matrix[i][j] == 0, call markRow(i) and markCol(j).
   markRow/markCol overwrite every NON-zero cell in that row/column with -inf
   (real 0s are left as 0, so only the original zeros ever act as triggers —
   the -inf cells won't, because they aren't equal to 0).
3. After the full scan, sweep the matrix once more and turn every -inf back
   into a real 0.
4. Cost: each original zero may repaint a whole row + column, so worst case is
   (number of cells) * (m + n) work.
TC -> O((m*n)*(m+n)), SC -> O(1)

#Better Approach:
1. Decouple "detecting" zeros from "applying" them so a freshly written 0
   never gets mistaken for an original one. Use two helper arrays: row[] of
   size m and col[] of size n, both initialised to 1 (meaning "keep").
2. Pass 1 (detect): for every cell that is 0, record row[i] = 0 and col[j] = 0
   to flag that entire row i and column j must eventually be zeroed.
3. Pass 2 (apply): for every cell, if its row was flagged (row[i] == 0) OR its
   column was flagged (col[j] == 0), set matrix[i][j] = 0.
TC -> O(m*n), SC -> O(m+n)

#Optimal Approach:
1. The O(m+n) arrays above are redundant — the matrix already has a spare row
   and column we can borrow. Reuse matrix's own first row as col[] and first
   column as row[], so the only extra memory is two scalar flags (row0/col0)
   that remember whether the first column / first row THEMSELVES originally
   held a zero (the marking step will clobber them, so capture this first).
2. Pre-scan: walk the first column and set its flag if any cell is 0; walk the
   first row and set its flag if any cell is 0.
3. Detect (i,j from 1): if matrix[i][j] == 0, write the marker into the
   borrowed storage — matrix[i][0] = 0 (this row needs zeroing) and
   matrix[0][j] = 0 (this column needs zeroing).
4. Apply (i,j from 1): if matrix[i][0] == 0 OR matrix[0][j] == 0, set
   matrix[i][j] = 0. Done from the inside out so the markers stay intact.
5. Finally use the two saved flags to zero the entire first column and/or
   first row if they originally contained a zero.
TC -> O(m*n), SC -> O(1)

#KEY INSIGHT:
- The first row and first column can double as the bookkeeping arrays, so no
  extra space is needed. The only state they cannot store about themselves is
  whether row 0 / col 0 originally had a zero (the marking clobbers them) —
  two scalar flags captured up front recover exactly that.
"""

from typing import List

# Sentinel placed in cells that must become 0 but were NOT originally 0, so the
# second pass can tell them apart from real zeros without re-triggering marking.
# Chosen just outside the input range (-2^31 .. 2^31-1) so it never collides
# with a real value, which keeps the matrix typed as List[List[int]].
MARKED = -(2**31) - 1


class Solution:
    def markRow(self, row: int, matrix: List[List[int]]) -> None:
        for j in range(0, len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = MARKED

    def markCol(self, col: int, matrix: List[List[int]]) -> None:
        for i in range(0, len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = MARKED

    def set_matrix_zeroes_brute(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    self.markRow(i, matrix)
                    self.markCol(j, matrix)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (matrix[i][j]) == MARKED:
                    matrix[i][j] = 0

        return matrix

    def set_matrix_zeroes_better(self, matrix: List[List[int]]) -> List[List[int]]:
        row = [1 for _ in range(len(matrix))]
        col = [1 for _ in range(len(matrix[0]))]

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0

        return matrix

    def set_matrix_zeroes_optimal(self, matrix: List[List[int]]) -> List[List[int]]:
        row0 = 1
        col0 = 1

        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                row0 = 0
                break

        for i in range(0, len(matrix[0])):
            if matrix[0][i] == 0:
                col0 = 0
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0 == 0:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        if col0 == 0:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0

        return matrix


if __name__ == "__main__":
    sol = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(sol.set_matrix_zeroes_brute(matrix))
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(sol.set_matrix_zeroes_better(matrix))
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(sol.set_matrix_zeroes_optimal(matrix))
