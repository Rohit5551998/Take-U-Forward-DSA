# QUESTION: Rat in a Maze
# Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at
# coordinates (n-1, n-1). Find all possible paths that rat can take to travel from (0, 0) to
# (n-1, n-1). The directions in which rat can move are 'U' (up), 'D' (down), 'L' (left),
# 'R' (right).
# The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for
# travelling, whereas value 1 represents that rat can travel through the cell. If the cell
# (0, 0) has 0 value, then mouse cannot move to any other cell.
# Note:
# - In a path no cell can be visited more than once.
# - If there is no possible path then return empty vector.
#
# Examples:
# Example 1:
# Input: n = 4, grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
# Output: [ "DDRDRR" , "DRDDRR" ]
# Explanation: The rat has two different paths to reach (3, 3).
# The first path is (0, 0) => (1, 0) => (2, 0) => (2, 1) => (3, 1) => (3, 2) => (3, 3).
# The second path is (0, 0) => (1, 0) => (1, 1) => (2, 1) => (3, 1) => (3, 2) => (3, 3).
#
# Example 2:
# Input: n = 2, grid = [ [1, 0] , [1, 0] ]
# Output: []
# Explanation: There is no path that rat can choose to travel from (0, 0) to (1, 1).
#
# Constraints:
# - 2 <= n <= 5
# - 0 <= grid[i][j] <= 1


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


class Solution:
    def rat_in_a_maze_brute(self) -> None:
        pass

    def rat_in_a_maze_better(self) -> None:
        pass

    def rat_in_a_maze_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
