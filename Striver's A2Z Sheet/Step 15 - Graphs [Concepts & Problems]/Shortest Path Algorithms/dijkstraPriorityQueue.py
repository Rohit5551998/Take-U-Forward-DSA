# mypy: disable-error-code="empty-body"
# QUESTION: Dijkstra's Algorithm (Priority Queue)
# Given a weighted, undirected and connected graph with V vertices (0-indexed) and
# an adjacency list adj, where adj[u] is a list of [v, wt] pairs meaning there is
# an edge between u and v with weight wt, find the shortest distance from a given
# source vertex S to every other vertex. All edge weights are non-negative.
# Return an array of length V where the i-th element is the shortest distance from
# S to vertex i. Implement it using a min-heap / priority queue.
#
# Example 1:
# Input:
#   V = 3, S = 2
#   adj = [[[1,1],[2,6]], [[2,3],[0,1]], [[1,3],[0,6]]]
# Output: [4, 3, 0]
# Explanation: Shortest distance from source 2 to vertex 0 is 4 (2 -> 1 -> 0 =
# 3 + 1), to vertex 1 is 3 (2 -> 1), and to itself is 0.
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
    def dijkstra_priority_queue_brute(
        self, V: int, adj: List[List[List[int]]], S: int
    ) -> List[int]:
        pass

    def dijkstra_priority_queue_better(
        self, V: int, adj: List[List[List[int]]], S: int
    ) -> List[int]:
        pass

    def dijkstra_priority_queue_optimal(
        self, V: int, adj: List[List[List[int]]], S: int
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.dijkstra_priority_queue_optimal(
    #     3, [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], 2
    # )
