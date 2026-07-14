# mypy: disable-error-code="empty-body"
# QUESTION: Number of Islands
# Given a grid of size N x M where each cell is either '1' (land) or '0' (water),
# return the number of islands. An island is a group of '1's connected
# horizontally or vertically. In the general version of the problem two cells are
# considered connected if they are adjacent in any of the 8 directions
# (horizontal, vertical, or diagonal). Cells on the boundary are surrounded by
# water on the outside.
#
# Example 1:
# Input: grid = [
#   ['1', '1', '0', '0', '0'],
#   ['1', '1', '0', '0', '0'],
#   ['0', '0', '1', '0', '0'],
#   ['0', '0', '0', '1', '1'],
# ]
# Output: 3
# Explanation: The top-left block of four '1's forms one island, the single '1'
# in the middle forms a second island, and the two connected '1's at the
# bottom-right form a third island.
#
# Example 2:
# Input: grid = [
#   ['1', '1', '1'],
#   ['0', '0', '0'],
#   ['1', '1', '1'],
# ]
# Output: 2
# Explanation: The top row of land and the bottom row of land are separated by a
# full row of water, giving two islands.
#
# Constraints:
# 1 <= N, M <= 300
# grid[i][j] is '0' or '1'


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
    def numberOfIslands_brute(self, grid: List[List[str]]) -> int:
        pass

    def numberOfIslands_better(self, grid: List[List[str]]) -> int:
        pass

    def numberOfIslands_optimal(self, grid: List[List[str]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.numberOfIslands_optimal([["1", "1", "0"], ["0", "0", "0"], ["1", "1", "1"]])
