# mypy: disable-error-code="empty-body"
# QUESTION: N Queen
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other (no two share a row, column, or
# diagonal). Return all distinct solutions; each solution is a board configuration
# where 'Q' marks a queen and '.' marks an empty square.
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
# Example 2:
# Input: n = 1
# Output: [["Q"]]
# Constraints:
# 1 <= n <= 9

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
    def solve_n_queens_brute(self, n: int) -> List[List[str]]:
        pass

    def solve_n_queens_better(self, n: int) -> List[List[str]]:
        pass

    def solve_n_queens_optimal(self, n: int) -> List[List[str]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.solve_n_queens_optimal(4))
