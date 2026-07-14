# mypy: disable-error-code="empty-body"
# QUESTION: Prim's Algorithm (Minimum Spanning Tree)
# Given a weighted, undirected and connected graph of V vertices and E edges,
# find the sum of the weights of the edges of the Minimum Spanning Tree (MST).
# The graph is given as an adjacency list where adj[i] contains a list of
# [node, weight] pairs representing an edge from vertex i to node with the
# given weight.
# A Minimum Spanning Tree is a subset of edges that connects all V vertices
# together, without any cycles, and with the minimum possible total edge weight.
#
# Example 1:
# Input:
#   V = 3, E = 3
#   adj = [
#     [[1, 5], [2, 1]],   # edges from vertex 0
#     [[0, 5], [2, 3]],   # edges from vertex 1
#     [[0, 1], [1, 3]]    # edges from vertex 2
#   ]
# Output: 4
# Explanation: The MST picks edge (0-2) with weight 1 and edge (1-2) with
# weight 3. Total weight = 1 + 3 = 4, which connects all 3 vertices.
#
# Constraints:
# 1 <= V <= 1000
# V - 1 <= E <= (V * (V - 1)) / 2
# 1 <= weight <= 1000
# The graph is connected and undirected.

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
    def prims_algorithm_brute(self, V: int, adj: List[List[List[int]]]) -> int:
        pass

    def prims_algorithm_better(self, V: int, adj: List[List[List[int]]]) -> int:
        pass

    def prims_algorithm_optimal(self, V: int, adj: List[List[List[int]]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.prims_algorithm_optimal(3, [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[0, 1], [1, 3]]])
