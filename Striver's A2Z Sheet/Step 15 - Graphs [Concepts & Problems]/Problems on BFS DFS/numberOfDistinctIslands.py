# mypy: disable-error-code="empty-body"
# QUESTION: Number of Distinct Islands
# You are given an m x n binary grid where 1 represents land and 0 represents
# water. An island is a maximal group of 1s connected 4-directionally (up, down,
# left, right).
# Two islands are considered the same if and only if one can be translated
# (shifted without rotation or reflection) to exactly overlap the other.
# Return the number of distinct islands (i.e. distinct shapes) in the grid.
#
# Example 1:
# Input: grid = [[1, 1, 0, 0, 0],
#                [1, 1, 0, 0, 0],
#                [0, 0, 0, 1, 1],
#                [0, 0, 0, 1, 1]]
# Output: 1
# Explanation: There are two islands, but both are 2x2 squares with the same
# shape, so they count as a single distinct island.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is 0 or 1

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
    def numberOfDistinctIslands_brute(self, grid: List[List[int]]) -> int:
        pass

    def numberOfDistinctIslands_better(self, grid: List[List[int]]) -> int:
        pass

    def numberOfDistinctIslands_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.numberOfDistinctIslands_optimal(
    #     [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    # )
