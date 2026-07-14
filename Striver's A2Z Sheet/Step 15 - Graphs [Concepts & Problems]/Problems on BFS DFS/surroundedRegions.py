# mypy: disable-error-code="empty-body"
# QUESTION: Surrounded Regions (Replace O with X)
# You are given an m x n board containing the characters 'X' and 'O'. A region is
# a group of 'O' cells that are connected 4-directionally (up, down, left, right).
# A region is said to be captured if it is completely surrounded by 'X' cells,
# i.e. none of its 'O' cells lie on the border of the board and it cannot reach
# the border through other 'O' cells.
# Flip every captured 'O' to 'X'. Any 'O' connected (directly or indirectly) to a
# border 'O' must remain 'O'. Modify the board accordingly and return it.
#
# Example 1:
# Input: board = [["X", "X", "X", "X"],
#                 ["X", "O", "O", "X"],
#                 ["X", "X", "O", "X"],
#                 ["X", "O", "X", "X"]]
# Output: [["X", "X", "X", "X"],
#          ["X", "X", "X", "X"],
#          ["X", "X", "X", "X"],
#          ["X", "O", "X", "X"]]
# Explanation: The middle region of 'O's is fully surrounded and gets flipped.
# The 'O' on the bottom border is not surrounded, so it stays 'O'.
#
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'

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
    def surroundedRegions_brute(self, board: List[List[str]]) -> List[List[str]]:
        pass

    def surroundedRegions_better(self, board: List[List[str]]) -> List[List[str]]:
        pass

    def surroundedRegions_optimal(self, board: List[List[str]]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.surroundedRegions_optimal(
    #     [
    #         ["X", "X", "X", "X"],
    #         ["X", "O", "O", "X"],
    #         ["X", "X", "O", "X"],
    #         ["X", "O", "X", "X"],
    #     ]
    # )
