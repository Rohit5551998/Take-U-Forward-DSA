# QUESTION: Grid unique paths
# Given two integers m and n, representing the number of rows and columns
# of a 2D array named matrix, return the number of unique ways to go from
# the top-left cell (matrix[0][0]) to the bottom-right cell
# (matrix[m-1][n-1]). At any point in time, you can only move either right
# or down by one cell.
#
# Examples:
# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation: There are 3 unique ways to go from the top-left to the bottom-right cell:
# 1) right → down → down
# 2) down → right → down
# 3) down → down → right
#
# Example 2:
# Input: m = 2, n = 4
# Output: 4
# Explanation: There are 4 unique ways to go from the top-left to the bottom-right cell:
# 1) down → right → right → right
# 2) right → down → right → right
# 3) right → right → down → right
# 4) right → right → right → down


"""
#Brute Force (recursion — explore every path):
1. Think of it as: "from cell (i, j), how many ways reach the bottom-right?"
   find_path(i, j) answers exactly that, and the grid answer is find_path(0, 0).
2. Two base cases: if (i, j) walks off the grid (i >= n or j >= m) there are 0
   ways; if (i, j) IS the target (n-1, m-1) that's 1 complete path.
3. Otherwise every path from (i, j) first steps either DOWN or RIGHT, and those
   two sets of paths are disjoint, so total = find_path(i+1, j) + find_path(i, j+1).
4. This re-explores overlapping subproblems (the same cell is reached by many
   prefixes), so the call tree is exponential.
TC -> O(2^(n+m)), SC -> O(n+m)  (recursion depth = path length)

#Better Approach (memoized recursion / top-down DP):
1. Same recurrence as brute force, but notice find_path(i, j) depends only on
   (i, j) — the answer for a cell is fixed no matter how we got there.
2. Keep a dp[n][m] table seeded with -1 ("not computed"). Before recursing into a
   cell, return dp[i][j] if it's already filled; after computing, store it.
3. Now each of the n*m cells is solved once and reused, collapsing the exponential
   tree into a linear-in-cells amount of work.
TC -> O(n*m), SC -> O(n*m) table + O(n+m) recursion stack

#Optimal Approach (combinatorics):
1. Any path is a fixed-length sequence of moves: to reach (n-1, m-1) you must take
   exactly (n-1) DOWN moves and (m-1) RIGHT moves, in some order — total
   N = (n-1)+(m-1) = n+m-2 moves.
2. A path is fully determined by WHICH of those N slots are the downs (the rest are
   rights). So the count is "choose the down positions": C(N, n-1), equivalently
   C(N, m-1). Example 2x3 grid: paths RRD, RDR, DRR = C(3,1) = 3.
3. Compute the binomial iteratively to avoid huge factorials: loop r = min(n,m)-1
   times with ans = ans * (N - i) // (i + 1); picking the smaller of n-1/m-1 keeps
   the loop short. O(min(n,m)) multiplications, O(1) space.
4. Exactness: do the work in INTEGERS — multiply first, THEN floor-divide. At step
   i, ans == C(N, i); ans*(N-i) is always divisible by (i+1), yielding exactly
   C(N, i+1). So every partial is a true integer and nothing is truncated. (Order
   matters: `ans * (N-i) // (i+1)` is exact, but `ans *= (N-i)//(i+1)` would divide
   too early and round down. Floating `/` instead of `//` loses precision once the
   value exceeds ~2^53 — Python's arbitrary-precision ints avoid that entirely.)
TC -> O(min(n,m)), SC -> O(1)

#KEY INSIGHT:
- Strip away the grid: a path is just an arrangement of (n-1) downs and (m-1)
  rights, so the number of paths is the number of ways to place the downs among
  all n+m-2 moves — a single binomial coefficient C(n+m-2, n-1), no DP needed.
"""

from typing import List


class Solution:
    def find_path(self, i: int, j: int, n: int, m: int) -> int:
        cnt = 0
        if i >= n or j >= m:
            cnt = 0
        elif i == n - 1 and j == m - 1:
            cnt = 1
        else:
            cnt = self.find_path(i + 1, j, n, m) + self.find_path(i, j + 1, n, m)
        return cnt

    def grid_unique_paths_brute(self, n: int, m: int) -> int:
        return self.find_path(0, 0, n, m)

    def find_path_dp(self, i: int, j: int, n: int, m: int, dp: List[List[int]]) -> int:
        cnt = 0
        if i >= n or j >= m:
            cnt = 0
        elif i == n - 1 and j == m - 1:
            cnt = 1
        elif dp[i][j] != -1:
            cnt = dp[i][j]
        else:
            cnt = self.find_path_dp(i + 1, j, n, m, dp) + self.find_path_dp(i, j + 1, n, m, dp)
            dp[i][j] = cnt
        return cnt

    def grid_unique_paths_better(self, n: int, m: int) -> int:
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.find_path_dp(0, 0, n, m, dp)

    def grid_unique_paths_optimal(self, n: int, m: int) -> int:
        """
        Every path is the SAME multiset of moves in a different order: to reach the
        bottom-right you always take (n-1) downs and (m-1) rights. So counting paths
        = counting orderings of those moves. e.g. a 2x3 grid -> RRD, RDR, DRR.
        Total moves N = (n-1) + (m-1) = n+m-2; a path is fixed once we choose which
        slots are the downs (or rights), so answer = C(N, n-1) = C(N, m-1).
        Below we evaluate that binomial iteratively, looping the smaller of (n-1),
        (m-1) times to keep it cheap.
        """
        N = n + m - 2
        r = min(m, n) - 1
        ans = 1

        for i in range(0, r):
            ans = ans * (N - i) // (i + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    n, m = 4, 2
    print(sol.grid_unique_paths_brute(n, m))
    n, m = 4, 2
    print(sol.grid_unique_paths_better(n, m))
    n, m = 4, 2
    print(sol.grid_unique_paths_optimal(n, m))
