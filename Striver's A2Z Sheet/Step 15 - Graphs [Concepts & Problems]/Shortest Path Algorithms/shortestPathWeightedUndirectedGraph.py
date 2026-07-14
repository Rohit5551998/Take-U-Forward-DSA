# mypy: disable-error-code="empty-body"
# QUESTION: Shortest Path in a Weighted Undirected Graph
# You are given a weighted, connected, undirected graph of n vertices (numbered
# from 1 to n) and m edges. Each edge is given as [u, v, w] denoting an
# undirected edge between vertex u and vertex v with a positive weight w. Find
# the shortest path (minimum total weight) from vertex 1 to vertex n and return
# the actual path as the sequence of vertices from 1 to n. If no such path
# exists, return [-1]. The first element of the returned list should be the total
# weight of the path, followed by the vertices in order.
#
# Example 1:
# Input: n = 5, m = 6,
#        edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1],
#                 [4, 3, 3], [3, 5, 1]]
# Output: [5, 1, 4, 3, 5]
# Explanation: The path 1 -> 4 -> 3 -> 5 has total weight 1 + 3 + 1 = 5, which is
# the minimum possible cost to travel from vertex 1 to vertex 5. The first value
# 5 is the total weight, followed by the vertices on the path.
#
# Example 2:
# Input: n = 2, m = 0, edges = []
# Output: [-1]
# Explanation: There is no edge, so vertex 2 is unreachable from vertex 1.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= m <= (n * (n - 1)) / 2
# 1 <= u, v <= n
# 1 <= w <= 10^5


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
    def shortest_path_weighted_undirected_brute(
        self, n: int, m: int, edges: List[List[int]]
    ) -> List[int]:
        pass

    def shortest_path_weighted_undirected_better(
        self, n: int, m: int, edges: List[List[int]]
    ) -> List[int]:
        pass

    def shortest_path_weighted_undirected_optimal(
        self, n: int, m: int, edges: List[List[int]]
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.shortest_path_weighted_undirected_optimal(
    #     5, 6,
    #     [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]],
    # )
