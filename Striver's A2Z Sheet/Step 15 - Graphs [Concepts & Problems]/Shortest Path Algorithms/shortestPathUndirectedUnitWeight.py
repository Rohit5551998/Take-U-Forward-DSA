# mypy: disable-error-code="empty-body"
# QUESTION: Shortest Path in Undirected Graph with Unit Weights
# Given an undirected graph with V vertices (0-indexed) and E edges, where every
# edge has unit weight (weight = 1), find the shortest distance from a given
# source vertex src to every other vertex. If a vertex is unreachable from the
# source, its distance should be reported as -1.
# The graph is given as an edge list; build an adjacency list from it.
#
# Example 1:
# Input:
#   V = 9, E edges =
#   [[0,1],[0,3],[3,4],[4,5],[5,6],[6,7],[6,8],[7,8],[2,1]]
#   src = 0
# Output: [0, 1, 3, 1, 2, 3, 4, 5, 4]
# Explanation: Distance to each vertex 0..8 from source 0, following unit-weight
# edges via BFS. Vertex 0 is the source (distance 0).
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= src < V
# Each edge connects two distinct vertices; the graph may be disconnected.

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
    def shortest_path_undirected_unit_weight_brute(
        self, edges: List[List[int]], V: int, src: int
    ) -> List[int]:
        pass

    def shortest_path_undirected_unit_weight_better(
        self, edges: List[List[int]], V: int, src: int
    ) -> List[int]:
        pass

    def shortest_path_undirected_unit_weight_optimal(
        self, edges: List[List[int]], V: int, src: int
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.shortest_path_undirected_unit_weight_optimal(
    #     [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6], [6, 7], [6, 8], [7, 8], [2, 1]],
    #     9,
    #     0,
    # )
