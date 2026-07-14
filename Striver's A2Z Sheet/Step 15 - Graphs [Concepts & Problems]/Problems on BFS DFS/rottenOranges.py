# mypy: disable-error-code="empty-body"
# QUESTION: Rotten Oranges
# You are given an m x n grid where each cell can have one of three values:
#   0 -> an empty cell,
#   1 -> a cell containing a fresh orange,
#   2 -> a cell containing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent (up, down,
# left, right) to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh
# orange. If this is impossible (some fresh orange can never be rotted), return -1.
#
# Example 1:
# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4
# Explanation: The rotting spreads outward from the top-left rotten orange, and
# after 4 minutes every fresh orange has become rotten.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is 0, 1, or 2

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
    def rottenOranges_brute(self, grid: List[List[int]]) -> int:
        pass

    def rottenOranges_better(self, grid: List[List[int]]) -> int:
        pass

    def rottenOranges_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.rottenOranges_optimal([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
