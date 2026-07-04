# mypy: disable-error-code="empty-body"
# QUESTION: Rotten Oranges
# Given an n x m grid, where each cell has the following values:
# 2 - represents a rotten orange, 1 - represents a fresh orange, 0 - represents an empty cell.
# Every minute, if a fresh orange is adjacent to a rotten orange in 4 directions (up, down, left,
# right) it becomes rotten. Return the minimum number of minutes required such that none of the
# cells has a fresh orange. If it's not possible, return -1.
#
# Examples:
# Example 1:
# Input: grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation: The fresh orange in the bottom-left corner can never rot — its only neighbours
# are empty cells, so no rotten orange can ever reach it.
#
# Example 2:
# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4
# Explanation: Rot spreads from (0,0): minute 1 -> (0,1),(1,0); minute 2 -> (0,2),(1,1);
# minute 3 -> (2,1); minute 4 -> (2,2). All fresh oranges are rotten after 4 minutes.
#
# Constraints:
# - 1 <= n, m <= 500
# - grid[i][j] == 0 or 1 or 2


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
    def rotten_oranges_brute(self, grid: List[List[int]]) -> int:
        pass

    def rotten_oranges_better(self, grid: List[List[int]]) -> int:
        pass

    def rotten_oranges_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(sol.rotten_oranges_optimal(grid))
