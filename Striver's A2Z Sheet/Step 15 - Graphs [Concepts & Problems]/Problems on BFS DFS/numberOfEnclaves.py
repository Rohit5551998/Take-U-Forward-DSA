# mypy: disable-error-code="empty-body"
# QUESTION: Number of Enclaves
# You are given an m x n binary grid where 0 represents a sea cell and 1
# represents a land cell. A move consists of walking from one land cell to
# another adjacent (4-directionally: up, down, left, right) land cell, or walking
# off the boundary of the grid.
# Return the number of land cells from which it is impossible to walk off the
# boundary of the grid in any number of moves. In other words, count the land
# cells belonging to islands that do not touch any border of the grid.
#
# Example 1:
# Input: grid = [[0, 0, 0, 0],
#                [1, 0, 1, 0],
#                [0, 1, 1, 0],
#                [0, 0, 0, 0]]
# Output: 3
# Explanation: The three land cells in the interior cluster cannot reach the
# boundary, so the answer is 3. (The single land cell on the left edge can walk
# off the boundary, so it is excluded.)
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
    def numberOfEnclaves_brute(self, grid: List[List[int]]) -> int:
        pass

    def numberOfEnclaves_better(self, grid: List[List[int]]) -> int:
        pass

    def numberOfEnclaves_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.numberOfEnclaves_optimal(
    #     [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    # )
