# mypy: disable-error-code="empty-body"
# QUESTION: Dijkstra's Algorithm (Set)
# Given a weighted, undirected and connected graph with V vertices (0-indexed) and
# an adjacency list adj, where adj[u] is a list of [v, wt] pairs meaning there is
# an edge between u and v with weight wt, find the shortest distance from a given
# source vertex S to every other vertex. All edge weights are non-negative.
# Return an array of length V where the i-th element is the shortest distance from
# S to vertex i. Implement it using an ordered set (which allows deleting a stale,
# larger distance entry when a shorter distance to the same node is found).
#
# Example 1:
# Input:
#   V = 3, S = 2
#   adj = [[[1,1],[2,6]], [[2,3],[0,1]], [[1,3],[0,6]]]
# Output: [4, 3, 0]
# Explanation: Same shortest distances as the priority-queue variant; the set
# lets us erase outdated (distance, node) pairs before re-inserting improved ones.
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= S < V
# 0 <= wt <= 10^3
# All edge weights are non-negative; the graph is connected.

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
    def dijkstra_set_brute(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        pass

    def dijkstra_set_better(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        pass

    def dijkstra_set_optimal(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.dijkstra_set_optimal(
    #     3, [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], 2
    # )
