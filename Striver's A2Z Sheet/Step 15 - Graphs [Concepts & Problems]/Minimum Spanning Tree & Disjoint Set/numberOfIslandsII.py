# mypy: disable-error-code="empty-body"
# QUESTION: Number of Islands II
# You are given an empty grid of size n rows by m columns, where every cell is
# initially water (0). We may perform an add-land operation which turns the
# water at some position into land (1).
# Given an array operators where operators[i] = [ri, ci] is the position
# (row ri, column ci) at which we operate the i-th operation, return an array
# of integers answer where answer[i] is the number of islands after turning
# the cell (ri, ci) into land.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
# Example 1:
# Input: n = 3, m = 3, operators = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1, 1, 2, 3]
# Explanation:
#   After [0,0]: one island -> 1
#   After [0,1]: adjacent to [0,0], still one island -> 1
#   After [1,2]: a new separate island -> 2
#   After [2,1]: another new separate island -> 3
#
# Constraints:
# 1 <= n, m <= 10^4
# 1 <= n * m <= 10^4
# 1 <= operators.length <= 10^4
# 0 <= ri < n
# 0 <= ci < m

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
    def num_islands2_brute(self, n: int, m: int, operators: List[List[int]]) -> List[int]:
        pass

    def num_islands2_better(self, n: int, m: int, operators: List[List[int]]) -> List[int]:
        pass

    def num_islands2_optimal(self, n: int, m: int, operators: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.num_islands2_optimal(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
