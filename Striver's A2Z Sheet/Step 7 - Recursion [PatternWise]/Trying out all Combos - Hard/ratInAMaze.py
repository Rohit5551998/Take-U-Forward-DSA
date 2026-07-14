# mypy: disable-error-code="empty-body"
# QUESTION: Rat in a Maze
# Consider a rat placed at (0, 0) in an n x n square matrix. It has to reach the
# destination at (n-1, n-1). Find all possible paths the rat can take to reach
# from source to destination. Movement is allowed in 4 directions: Down (D),
# Left (L), Right (R), Up (U). A cell value 1 means open, 0 means blocked. A cell
# may not be visited more than once in a single path. Return paths in lexicographic
# order.
# Example 1:
# Input: n = 4, m = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
# Output: ["DDRDRR", "DRDDRR"]
# Example 2:
# Input: n = 2, m = [[1,0],[1,0]]
# Output: [] (no path, destination unreachable)
# Constraints:
# 2 <= n <= 5
# 0 <= m[i][j] <= 1
# m[0][0] == 1 for a path to exist.

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
    def rat_in_maze_brute(self, m: List[List[int]], n: int) -> List[str]:
        pass

    def rat_in_maze_better(self, m: List[List[int]], n: int) -> List[str]:
        pass

    def rat_in_maze_optimal(self, m: List[List[int]], n: int) -> List[str]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
#     print(sol.rat_in_maze_optimal(maze, 4))
