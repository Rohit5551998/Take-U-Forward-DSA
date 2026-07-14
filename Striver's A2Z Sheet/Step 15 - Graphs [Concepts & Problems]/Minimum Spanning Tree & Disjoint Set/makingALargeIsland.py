# mypy: disable-error-code="empty-body"
# QUESTION: Making A Large Island
# You are given an n x n binary grid. You are allowed to change at most one
# cell from 0 to 1.
# Return the size of the largest island in the grid after applying this
# operation.
# An island is a 4-directionally connected group of 1s.
#
# Example 1:
# Input: grid = [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 to connect the two existing islands of size 1
# each. The resulting island has size 3.
#
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.

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
    def largest_island_brute(self, grid: List[List[int]]) -> int:
        pass

    def largest_island_better(self, grid: List[List[int]]) -> int:
        pass

    def largest_island_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.largest_island_optimal([[1, 0], [0, 1]])
