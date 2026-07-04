# QUESTION: Sudoku Solver
# Create a program that fills in the blank cells in a Sudoku puzzle to solve it.
# Every sudoku solution needs to follow these guidelines:
# 1) In every row, the numbers 1 through 9 must appear exactly once.
# 2) In every column, the numbers 1 through 9 must appear exactly once.
# 3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.
# Empty cells are indicated by the '.' character. Fill the board in-place.
#
# Examples:
# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],
#  ["6","7","2","1","9","5","3","4","8"],
#  ["1","9","8","3","4","2","5","6","7"],
#  ["8","5","9","7","6","1","4","2","3"],
#  ["4","2","6","8","5","3","7","9","1"],
#  ["7","1","3","9","2","4","8","5","6"],
#  ["9","6","1","5","3","7","2","8","4"],
#  ["2","8","7","4","1","9","6","3","5"],
#  ["3","4","5","2","8","6","1","7","9"]]
# Explanation: All empty cells are filled so that every row, every column and every 3x3 sub-box
# contains each of the digits 1 through 9 exactly once. This is the only valid solution for the
# given board.
#
# Constraints:
# - board.length = 9
# - board[i].length = 9
# - board[i][j] is a digit or '.'
# - It is guaranteed that input board has only one solution.


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
    def sudoku_solver_brute(self, board: List[List[str]]) -> None:
        pass

    def sudoku_solver_better(self, board: List[List[str]]) -> None:
        pass

    def sudoku_solver_optimal(self, board: List[List[str]]) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.sudoku_solver_optimal(board)
    for row in board:
        print("".join(row))
