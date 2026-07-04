# mypy: disable-error-code="empty-body"
# QUESTION: Minimum sum path in the matrix, (count paths and similar type do, also backtrack to find the Minimum path)
# Given an m x n grid filled with non-negative numbers, find a path from
# top-left to bottom-right which minimizes the sum of all numbers along
# its path. You can only move either DOWN or RIGHT at any point in time.
# Return that minimum sum.
#
# (The Striver sheet groups several related variants here: count of
# unique paths, also backtrack to recover the actual minimum path, etc.)
#
# Examples:
# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
# Explanation: 1 → 2 → 3 → 6 (path sum 12).
#
# Constraints:
# m == grid.length, n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200


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
    def minimum_sum_path_in_the_matrix_count_paths_and_similar_type_do_also_backtrack_to_find_the_minimum_path_brute(  # noqa: E501
        self,
        grid: List[List[int]],
    ) -> int:
        pass

    def minimum_sum_path_in_the_matrix_count_paths_and_similar_type_do_also_backtrack_to_find_the_minimum_path_better(  # noqa: E501
        self,
        grid: List[List[int]],
    ) -> int:
        pass

    def minimum_sum_path_in_the_matrix_count_paths_and_similar_type_do_also_backtrack_to_find_the_minimum_path_optimal(  # noqa: E501
        self,
        grid: List[List[int]],
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(
        sol.minimum_sum_path_in_the_matrix_count_paths_and_similar_type_do_also_backtrack_to_find_the_minimum_path_optimal(
            grid
        )
    )
