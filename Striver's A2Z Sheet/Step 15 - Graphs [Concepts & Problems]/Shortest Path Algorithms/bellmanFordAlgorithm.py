# mypy: disable-error-code="empty-body"
# QUESTION: Bellman-Ford Algorithm
# Given a weighted directed graph with V vertices (0-indexed) and a list of edges,
# where each edge is [u, v, wt] representing a directed edge from u to v with weight
# wt (weights may be negative), compute the shortest distance from a given source
# vertex S to every other vertex. Unlike Dijkstra, Bellman-Ford handles negative
# edge weights. If the graph contains a negative-weight cycle reachable such that
# distances can be reduced indefinitely, return [-1] to signal its presence.
# Unreachable vertices should have distance infinity (commonly 10^8).
#
# Example 1:
# Input:
#   V = 6, S = 0
#   edges = [[3,2,6],[5,3,1],[0,1,5],[1,5,-3],[1,2,-2],[3,4,-2],[2,4,3]]
# Output: [0, 5, 3, 3, 1, 2]
# Explanation: After relaxing all edges V-1 times, these are the shortest
# distances from source 0 to vertices 0..5.
#
# Constraints:
# 1 <= V <= 500
# 1 <= edges.length <= V * (V - 1)
# edges[i].length == 3
# 0 <= u, v < V
# -1000 <= wt <= 1000
# 0 <= S < V

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
    def bellman_ford_algorithm_brute(self, V: int, edges: List[List[int]], S: int) -> List[int]:
        pass

    def bellman_ford_algorithm_better(self, V: int, edges: List[List[int]], S: int) -> List[int]:
        pass

    def bellman_ford_algorithm_optimal(self, V: int, edges: List[List[int]], S: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.bellman_ford_algorithm_optimal(
    #     6,
    #     [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]],
    #     0,
    # )
