# mypy: disable-error-code="empty-body"
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
SKIPPED — enumerating all source-to-destination paths is inherently a DFS/
backtracking search; there is no cruder non-recursive baseline. The backtracking
below IS the standard (and only) approach for "return all paths".

#Better Approach:
SKIPPED — no middle tier. Rat-in-a-maze is a single backtracking DFS; nothing
sensible sits between it and a trivial brute.

#Optimal Approach (find_path + rat_in_a_maze_optimal):
1. DFS from (0,0) trying to reach (n-1,n-1), extending a `directions` string one
   move at a time. A `visited` grid (-1 = free, 1 = on current path) stops a path
   from stepping on a cell it already occupies.
2. SEED the start: mark visited[0][0] = 1 BEFORE recursing. If you skip this the
   rat can walk back onto (0,0) (e.g. D then U), producing illegal revisiting
   paths — the whole correctness of "no cell twice" hinges on it.
3. Guard the endpoints: only start if both (0,0) and (n-1,n-1) are open (value 1);
   otherwise no path can exist and ans stays empty.
4. Base case: when (i,j) == (n-1,n-1), the accumulated `directions` string is one
   valid path — append it to ans.
5. Otherwise try the four moves in D, L, R, U order (this fixed order makes the
   collected paths come out lexicographically sorted for free).
6. For each move, it's legal only if the target is in-bounds, open (grid==1) and
   not already on the path (visited==-1). If so: mark it 1, recurse with the
   direction char appended, then UNMARK it back to -1 (backtrack) so other paths
   can use that cell.
7. The mark→recurse→unmark discipline is what lets the same cell belong to many
   different paths without ever appearing twice within one path.
TC -> O(4^(n*n)), SC -> O(n*n) visited + O(n*n) recursion depth
   (up to 4 directions explored per cell across n*n cells in the worst case)

#KEY INSIGHT:
- Standard grid backtracking: mark a cell on entry, explore all four directions,
  unmark on exit. The two make-or-break details are SEEDING the start cell as
  visited (so paths can't loop back to (0,0)) and iterating directions in D<L<R<U
  order, which yields the required lexicographic ordering without a final sort.
"""

from typing import List


class Solution:
    def rat_in_a_maze_brute(self, grid: List[List[int]], n: int) -> List[str]:
        # SKIP: enumerating all paths is inherently a DFS/backtracking search;
        # there is no cruder non-recursive baseline — backtracking is the first tier.
        pass

    def rat_in_a_maze_better(self, grid: List[List[int]], n: int) -> List[str]:
        # SKIP: no middle tier — single backtracking DFS, nothing sits between it
        # and a trivial brute.
        pass

    def find_path(
        self,
        grid: List[List[int]],
        n: int,
        visited: List[List[int]],
        ans: List[str],
        i: int,
        j: int,
        directions: str,
    ) -> None:
        if i == n - 1 and j == n - 1:
            # reached the destination — the accumulated string is one full path
            ans.append(directions)

        # Try moves in D, L, R, U order so the collected paths come out
        # lexicographically sorted (D < L < R < U) without a final sort.
        # Each move fires only if the target is in-bounds, open (grid == 1), and
        # not already on the current path (visited == -1); then mark -> recurse ->
        # unmark so the cell is free again for other paths (backtracking).
        else:
            # Down
            if i + 1 < n and grid[i + 1][j] == 1 and visited[i + 1][j] == -1:
                visited[i + 1][j] = 1
                self.find_path(grid, n, visited, ans, i + 1, j, directions + "D")
                visited[i + 1][j] = -1

            # Left
            if j - 1 >= 0 and grid[i][j - 1] == 1 and visited[i][j - 1] == -1:
                visited[i][j - 1] = 1
                self.find_path(grid, n, visited, ans, i, j - 1, directions + "L")
                visited[i][j - 1] = -1

            # Right
            if j + 1 < n and grid[i][j + 1] == 1 and visited[i][j + 1] == -1:
                visited[i][j + 1] = 1
                self.find_path(grid, n, visited, ans, i, j + 1, directions + "R")
                visited[i][j + 1] = -1

            # Up
            if i - 1 >= 0 and grid[i - 1][j] == 1 and visited[i - 1][j] == -1:
                visited[i - 1][j] = 1
                self.find_path(grid, n, visited, ans, i - 1, j, directions + "U")
                visited[i - 1][j] = -1

    def rat_in_a_maze_optimal(self, grid: List[List[int]], n: int) -> List[str]:
        visited = [[-1 for _ in range(n)] for _ in range(n)]
        ans: List[str] = []
        if grid[0][0] == 1 and grid[n - 1][n - 1] == 1:
            visited[0][0] = 1
            self.find_path(grid, n, visited, ans, 0, 0, "")
            visited[0][0] = -1
        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    n = 4
    print(sol.rat_in_a_maze_optimal(grid, n))
