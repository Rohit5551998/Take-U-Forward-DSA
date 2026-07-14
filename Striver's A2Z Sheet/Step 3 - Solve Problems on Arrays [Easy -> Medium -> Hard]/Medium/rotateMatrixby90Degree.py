# mypy: disable-error-code="empty-body"
# QUESTION: Rotate Image (Matrix by 90 Degrees Clockwise)
# Given an n x n matrix, rotate it 90 degrees clockwise in-place.
# Example 1:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# Explanation: Each column (top to bottom) becomes a row (left to right).
# Constraints:
# 1 <= n <= 1000
# -10^9 <= matrix[i][j] <= 10^9

"""
#Brute Force:
1. Allocate a new n x n matrix and place matrix[i][j] at output[j][n-1-i], the
   position it lands after a clockwise rotation.
TC -> O(n^2), SC -> O(n^2)

#Better Approach:
SKIPPED — no distinct middle tier; the transpose-then-reverse trick below is the
direct in-place improvement.

#Optimal Approach (Transpose + Reverse):
1. Transpose the matrix: swap matrix[i][j] with matrix[j][i] for j > i.
2. Reverse each row. Transpose flips across the main diagonal; reversing rows
   then produces the clockwise rotation, all in-place.
TC -> O(2 * n^2), SC -> O(1)

#KEY INSIGHT:
- A clockwise 90-degree rotation equals a transpose followed by a horizontal
  flip of each row, so no extra matrix is needed.
"""

from typing import List


class Solution:
    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate_brute(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        output = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                output[j][(n - 1) - i] = matrix[i][j]
        return output

    def rotate_better(self, matrix: List[List[int]]) -> List[List[int]]:
        # SKIP: no distinct better approach; transpose+reverse is the optimal.
        pass

    def rotate_optimal(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            self.reverse(matrix[i], 0, n - 1)
        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate_optimal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
