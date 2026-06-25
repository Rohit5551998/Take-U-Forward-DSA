# QUESTION: N Queen
# The n-queens puzzle is the problem of placing n queens on an n × n
# chessboard such that no two queens attack each other (no two queens
# share the same row, column, or diagonal).
# Given an integer n, return all distinct solutions to the n-queens
# puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
# Examples:
# Example 1:
# Input: n = 4
# Output: [[".Q..", "...Q", "Q...", "..Q."],
#          ["..Q.", "Q...", "...Q", ".Q.."]]
# Explanation: There are exactly two distinct solutions to the 4-queens
# puzzle.
#
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# 1 <= n <= 9
#
# Approach: backtracking. Place a queen in a row, then recurse to the
# next row. Track conflicting columns and both diagonals (via column
# index and (row+col) / (row-col+n) markers) to prune.
#
# Examples:
# Input: N = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown below
#
# Input : N = 1
# Output: [["Q"]]
# Explanation : There is only one way to place 1 queen on 1x1 chessboard.


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
    def n_queen_brute(self) -> None:
        pass

    def n_queen_better(self) -> None:
        pass

    def n_queen_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
