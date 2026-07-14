# mypy: disable-error-code="empty-body"
# QUESTION: Path With Minimum Effort
# You are given a rows x columns grid heights where heights[r][c] is the height of
# cell (r, c). You start at the top-left cell (0, 0) and want to reach the
# bottom-right cell (rows-1, columns-1). You can move up, down, left, or right.
# The effort of a path is the maximum absolute difference in heights between two
# consecutive cells along that path. Return the minimum effort required to travel
# from the top-left to the bottom-right cell.
#
# Example 1:
# Input:
#   heights = [[1,2,2],
#              [3,8,2],
#              [5,3,5]]
# Output: 2
# Explanation: The route [1,3,5,3,5] has a maximum consecutive difference of 2.
# This is better than the route [1,2,2,2,5] whose maximum difference is 3.
#
# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6

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
    def path_with_minimum_effort_brute(self, heights: List[List[int]]) -> int:
        pass

    def path_with_minimum_effort_better(self, heights: List[List[int]]) -> int:
        pass

    def path_with_minimum_effort_optimal(self, heights: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.path_with_minimum_effort_optimal(
    #     [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    # )
