# mypy: disable-error-code="empty-body"
# QUESTION: Floyd-Warshall Algorithm
# Given a weighted directed graph represented as a V x V adjacency matrix, where
# matrix[i][j] is the weight of the edge from vertex i to vertex j, and a value of
# -1 denotes that there is no direct edge from i to j (and matrix[i][i] = 0),
# compute the shortest distance between every pair of vertices. Modify the matrix
# in place so that matrix[i][j] holds the shortest distance from i to j, keeping
# -1 where a pair is unreachable. The algorithm considers each vertex as an
# intermediate point. It can also be used to detect negative-weight cycles.
#
# Example 1:
# Input:
#   matrix = [[0, 25, -1, -1],
#             [-1, 0, 10, -1],
#             [-1, -1, 0, 2],
#             [-1, -1, -1, 0]]
# Output:  [[0, 25, 35, 37],
#           [-1, 0, 10, 12],
#           [-1, -1, 0, 2],
#           [-1, -1, -1, 0]]
# Explanation: Distance from 0 to 2 becomes 25 + 10 = 35 (via vertex 1), and 0 to
# 3 becomes 35 + 2 = 37 (via vertices 1 and 2).
#
# Constraints:
# 1 <= V <= 100 (matrix is V x V)
# -1 <= matrix[i][j] <= 10^3 (with -1 meaning no edge)
# matrix[i][i] == 0

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
    def floyd_warshall_algorithm_brute(self, matrix: List[List[int]]) -> None:
        pass

    def floyd_warshall_algorithm_better(self, matrix: List[List[int]]) -> None:
        pass

    def floyd_warshall_algorithm_optimal(self, matrix: List[List[int]]) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.floyd_warshall_algorithm_optimal(
    #     [
    #         [0, 25, -1, -1],
    #         [-1, 0, 10, -1],
    #         [-1, -1, 0, 2],
    #         [-1, -1, -1, 0],
    #     ]
    # )
