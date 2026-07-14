# mypy: disable-error-code="empty-body"
# QUESTION: Grid Unique Paths II
# Same as Unique Paths but some cells contain obstacles (marked 1). The robot
# cannot pass through obstacles. Count unique paths top-left to bottom-right
# moving only right or down.
#
# Example 1:
# Input: grid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
#
# Constraints:
# 1 <= m, n <= 100
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
    def unique_paths_ii_brute(self, grid: List[List[int]]) -> int:
        pass

    def unique_paths_ii_better(self, grid: List[List[int]]) -> int:
        pass

    def unique_paths_ii_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.unique_paths_ii_optimal([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
