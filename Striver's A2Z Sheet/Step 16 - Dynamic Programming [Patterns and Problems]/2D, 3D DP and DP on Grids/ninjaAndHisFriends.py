# mypy: disable-error-code="empty-body"
# QUESTION: Ninja and His Friends (Cherry Pickup II)
# Two robots start at (0,0) and (0,c-1) of an r x c grid and move to the last
# row; each step moves down-left, down, or down-right. Collect maximum
# chocolates; a cell is counted once if both robots stand on it.
#
# Example 1:
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
#
# Constraints:
# 2 <= r, c <= 70
# 0 <= grid[i][j] <= 100

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
    def cherry_pickup_brute(self, grid: List[List[int]]) -> int:
        pass

    def cherry_pickup_better(self, grid: List[List[int]]) -> int:
        pass

    def cherry_pickup_optimal(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.cherry_pickup_optimal([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])
