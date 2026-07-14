# mypy: disable-error-code="empty-body"
# QUESTION: Distance of Nearest Cell Having 1 (0/1 Matrix)
# You are given an m x n binary grid consisting of only 0s and 1s. For every cell
# in the grid, compute the distance to the nearest cell containing a 1, where the
# distance between two adjacent cells (up, down, left, right) is 1.
# Return a matrix of the same dimensions where each entry holds the shortest such
# distance for the corresponding cell. A cell that already contains a 1 has a
# distance of 0.
#
# Example 1:
# Input: grid = [[0, 1, 1], [0, 0, 0], [0, 0, 1]]
# Output: [[1, 0, 0], [2, 1, 1], [2, 1, 0]]
# Explanation: Each 0 cell is assigned its Manhattan-path distance to the closest
# 1 cell, while each 1 cell has distance 0.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is 0 or 1
# There is at least one 1 in the grid.

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
    def distanceOfNearestCellHaving1_brute(self, grid: List[List[int]]) -> List[List[int]]:
        pass

    def distanceOfNearestCellHaving1_better(self, grid: List[List[int]]) -> List[List[int]]:
        pass

    def distanceOfNearestCellHaving1_optimal(self, grid: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.distanceOfNearestCellHaving1_optimal([[0, 1, 1], [0, 0, 0], [0, 0, 1]])
