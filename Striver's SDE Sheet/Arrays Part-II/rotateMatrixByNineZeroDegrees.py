# QUESTION: Rotate matrix by 90 degrees
# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly.
#
# Examples:
# Input :matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Output :matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
#
# Explanation :First, we transpose the matrix: rows become columns. Then, we reverse each row to simulate 90° clockwise rotation. So element at (0,0) goes to (0,2), (0,1) goes to (1,2), and so on, achieving the rotated layout.
#
# Input :matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
#
# Output :matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
#
# Explanation :First, the matrix is transposed: rows become columns. Then, each row is reversed. This moves the last column to the first row, the second last column to the second row, and so on. The original position of each element is rotated 90° clockwise into its new location.


"""
#Brute Force:
1. Allocate a fresh n×n matrix `ans` to hold the result — this extra matrix is
   exactly what the in-place requirement forbids, so it's only the baseline.
2. Work out where each element lands: in a 90° clockwise rotation the value at
   (i, j) moves to row j, column n-1-i (the top row becomes the right column, the
   left column becomes the top row, etc.).
3. Walk every cell (i, j) of the input and copy matrix[i][j] into ans[j][n-1-i],
   placing each element directly at its rotated destination.
4. Return `ans` (the rotated copy; the original is left untouched).
TC -> O(n^2), SC -> O(n^2)

#Better Approach:
SKIPPED — no distinct "better" tier; it's a direct jump from the extra-matrix
brute force to the in-place transpose-and-reverse optimal.

#Optimal Approach:
1. Key identity: a 90° clockwise rotation equals two reflections done in order —
   first transpose (reflect across the main diagonal), then reverse each row
   (reflect left↔right). Both reflections can be done in place, so no copy needed.
2. Transpose in place: for each row i, loop j from i+1 and swap
   matrix[i][j] <-> matrix[j][i]. Starting j at i+1 (strictly above the diagonal)
   is essential — starting at 0 would swap every pair twice and cancel the
   transpose, and it also skips the diagonal which never moves.
3. Reverse each row: for every row, two-pointer swap from both ends inward
   (the reverse_row helper) so each row is mirrored left-to-right.
4. After transpose + row-reversal the matrix is rotated 90° clockwise, entirely
   in place using only a couple of index variables.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- 90° clockwise = transpose, then reverse every row. Transposing only the upper
  triangle (j from i+1) swaps each off-diagonal pair exactly once; reversing the
  rows then completes the turn with no extra matrix — O(1) space.
"""

from typing import List


class Solution:
    def rotate_matrix_by_ninezero_degrees_brute(self, matrix: List[List[int]]) -> None:
        ans = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                ans[j][len(matrix) - 1 - i] = matrix[i][j]

        return ans

    def rotate_matrix_by_ninezero_degrees_better(self) -> None:
        # SKIP: no distinct "better" tier — it's a direct jump from the
        # extra-matrix brute force to the in-place transpose-and-reverse optimal.
        pass

    def reverse_row(self, row: List[int]) -> None:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    def rotate_matrix_by_ninezero_degrees_optimal(self, matrix: List[List[int]]) -> None:
        # Transpose Matrix
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse Matrix Rows
        for i in range(0, len(matrix)):
            self.reverse_row(matrix[i])

        return matrix


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
    print(sol.rotate_matrix_by_ninezero_degrees_brute(mat))
    mat = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
    print(sol.rotate_matrix_by_ninezero_degrees_optimal(mat))
