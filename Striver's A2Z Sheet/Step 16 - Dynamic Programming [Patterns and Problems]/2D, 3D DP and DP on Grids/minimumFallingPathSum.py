# mypy: disable-error-code="empty-body"
# QUESTION: Minimum / Maximum Falling Path Sum
# Given an n x n matrix, find the minimum falling path sum. A falling path
# starts at any cell of the first row and each step moves to the cell directly
# below or diagonally below-left/below-right.
#
# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: 1->5->7 = 13.
#
# Constraints:
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def min_falling_path_sum_brute(self, matrix: List[List[int]]) -> int:
        pass

    def min_falling_path_sum_better(self, matrix: List[List[int]]) -> int:
        pass

    def min_falling_path_sum_optimal(self, matrix: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.min_falling_path_sum_optimal([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
