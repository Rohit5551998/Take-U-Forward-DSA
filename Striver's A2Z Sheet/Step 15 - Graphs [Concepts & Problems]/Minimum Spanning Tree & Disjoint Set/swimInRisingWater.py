# mypy: disable-error-code="empty-body"
# QUESTION: Swim in Rising Water
# You are given an n x n integer matrix grid where each value grid[i][j]
# represents the elevation at that point (i, j).
# It starts raining. At time t, the depth of the water everywhere is t. You can
# swim from a square to another 4-directionally adjacent square if and only if
# the elevation of both squares individually are at most t. You can swim
# infinite distances in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
# Return the least time until you can reach the bottom right square (n-1, n-1)
# if you start at the top left square (0, 0).
#
# Example 1:
# Input: grid = [[0, 2], [1, 3]]
# Output: 3
# Explanation: At time 0, you are at (0, 0). You cannot move to (0, 1) which
# has elevation 2 until time 2, and to (1, 1) with elevation 3 until time 3.
# The earliest you can reach the bottom right (1, 1) is at time 3.
#
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n * n
# Each value grid[i][j] is unique.

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
    def swim_in_water_brute(self, grid: List[List[int]]) -> int:
        pass

    def swim_in_water_better(self, grid: List[List[int]]) -> int:
        pass

    def swim_in_water_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.swim_in_water_optimal([[0, 2], [1, 3]])
