# mypy: disable-error-code="empty-body"
# QUESTION: Spiral Matrix
# Given an m x n matrix, return all its elements in spiral order (clockwise,
# starting from the top-left).
# Example 1:
# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
# Explanation: Walk the outer ring clockwise, then the inner ring.
# Constraints:
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

"""
#Brute Force:
SKIPPED — there is no simpler naive variant; the four-boundary simulation is the
canonical single approach.

#Better Approach:
SKIPPED — same reason.

#Optimal Approach (Four Boundaries):
1. Maintain top, bottom, left, right boundaries of the not-yet-printed region.
2. Traverse the top row left->right, then the right column top->bottom, then the
   bottom row right->left, then the left column bottom->top, shrinking the
   relevant boundary after each leg.
3. Guard the bottom and left legs with a check so single-row / single-column
   leftovers are not printed twice.
4. Repeat until the boundaries cross.
TC -> O(n*m), SC -> O(n*m) for the output.

#KEY INSIGHT:
- Four shrinking boundaries turn "spiral order" into four straight-line passes
  per ring; the extra guards prevent double-visiting a lone middle row/column.
"""

from typing import List


class Solution:
    def spiral_brute(self, matrix: List[List[int]]) -> List[int]:
        # SKIP: no naive variant distinct from the boundary simulation.
        pass

    def spiral_better(self, matrix: List[List[int]]) -> List[int]:
        # SKIP: no better variant distinct from the boundary simulation.
        pass

    def spiral_optimal(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        top, right, bottom, left = 0, m - 1, n - 1, 0
        output: List[int] = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiral_optimal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
