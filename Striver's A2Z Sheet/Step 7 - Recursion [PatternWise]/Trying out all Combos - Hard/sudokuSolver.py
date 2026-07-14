# mypy: disable-error-code="empty-body"
# QUESTION: Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy: each of the digits 1-9 must occur exactly once
# in each row, exactly once in each column, and exactly once in each of the nine
# 3x3 sub-boxes. Empty cells are denoted by '.'. There is exactly one solution.
# The board is modified in place.
# Example 1:
# Input: board is a 9x9 grid with some cells filled and '.' for blanks.
# Output: the same board with every '.' replaced by the correct digit.
# Constraints:
# board.length == 9, board[i].length == 9
# board[i][j] is a digit '1'-'9' or '.'
# It is guaranteed that the input board has exactly one solution.

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
    def solve_sudoku_brute(self, board: List[List[str]]) -> None:
        pass

    def solve_sudoku_better(self, board: List[List[str]]) -> None:
        pass

    def solve_sudoku_optimal(self, board: List[List[str]]) -> None:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     b = [["5", "3", "."], [".", ".", "."], [".", ".", "."]]  # partial sample
#     sol.solve_sudoku_optimal(b)
#     print(b)
