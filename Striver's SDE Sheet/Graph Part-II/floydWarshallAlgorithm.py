# QUESTION: Floyd Warshall Algorithm
# Given a graph of V vertices numbered from 0 to V-1. Find the shortest distances between
# every pair of vertices in a given edge-weighted directed graph. The graph is represented
# as an adjacency matrix of size n x n. Matrix[i][j] denotes the weight of the edge from
# i to j. If Matrix[i][j] = -1, it means there is no edge from i to j.
#
# Examples:
# Example 1:
# Input: matrix = [[0, 2, -1, -1], [1, 0, 3, -1], [-1, -1, 0, 1], [3, 5, 4, 0]]
# Output: [[0, 2, 5, 6], [1, 0, 3, 4], [4, 6, 0, 1], [3, 5, 4, 0]]
# Explanation: matrix[0][0] is storing the distance from vertex 0 to vertex 0, the distance
# from vertex 0 to vertex 1 is 2, and so on.
#
# Example 2:
# Input: matrix = [[0, 25], [-1, 0]]
# Output: [[0, 25], [-1, 0]]
# Explanation: The matrix already contains the shortest distances.
#
# Constraints:
# 1 <= n <= 100
# -1 <= matrix[i][j] <= 1000


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


class Solution:
    def floyd_warshall_algorithm_brute(self) -> None:
        pass

    def floyd_warshall_algorithm_better(self) -> None:
        pass

    def floyd_warshall_algorithm_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
