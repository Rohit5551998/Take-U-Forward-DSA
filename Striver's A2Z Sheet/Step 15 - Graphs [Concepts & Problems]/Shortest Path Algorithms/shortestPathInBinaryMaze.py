# mypy: disable-error-code="empty-body"
# QUESTION: Shortest Path in a Binary Maze
# Given an n x m binary grid where a cell with value 1 is open (walkable) and a
# cell with value 0 is blocked, find the length of the shortest path from a given
# source cell to a destination cell. You may move in the 4 cardinal directions
# (up, down, left, right) and only through cells with value 1. The path length is
# the number of cells traversed (or number of steps + 1, per convention). If there
# is no path, return -1. source and destination are given as (row, col) pairs.
#
# Example 1:
# Input:
#   grid = [[1,1,1,1],
#           [1,1,0,1],
#           [1,1,1,1],
#           [1,1,0,0],
#           [1,0,0,1]]
#   source = (0, 1), destination = (2, 2)
# Output: 3
# Explanation: The shortest path (0,1) -> (1,1) -> (2,1) -> (2,2) has 3 steps.
#
# Constraints:
# 1 <= n, m <= 10^4 (n * m <= 10^6)
# grid[i][j] is 0 or 1
# The source and destination cells are open (value 1).

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

from typing import List, Tuple


class Solution:
    def shortest_path_in_binary_maze_brute(
        self,
        grid: List[List[int]],
        source: Tuple[int, int],
        destination: Tuple[int, int],
    ) -> int:
        pass

    def shortest_path_in_binary_maze_better(
        self,
        grid: List[List[int]],
        source: Tuple[int, int],
        destination: Tuple[int, int],
    ) -> int:
        pass

    def shortest_path_in_binary_maze_optimal(
        self,
        grid: List[List[int]],
        source: Tuple[int, int],
        destination: Tuple[int, int],
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.shortest_path_in_binary_maze_optimal(
    #     [
    #         [1, 1, 1, 1],
    #         [1, 1, 0, 1],
    #         [1, 1, 1, 1],
    #         [1, 1, 0, 0],
    #         [1, 0, 0, 1],
    #     ],
    #     (0, 1),
    #     (2, 2),
    # )
