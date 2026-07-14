# mypy: disable-error-code="empty-body"
# QUESTION: Word Search
# Given an m x n grid of characters board and a string word, return True if word
# exists in the grid. The word can be constructed from letters of sequentially
# adjacent cells (horizontally or vertically neighboring). The same cell may not
# be used more than once.
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: True
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: False
# Constraints:
# m == board.length, n == board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consist of only lowercase and uppercase English letters.

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
    def word_search_brute(self, board: List[List[str]], word: str) -> bool:
        pass

    def word_search_better(self, board: List[List[str]], word: str) -> bool:
        pass

    def word_search_optimal(self, board: List[List[str]], word: str) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
#     print(sol.word_search_optimal(grid, "ABCCED"))
