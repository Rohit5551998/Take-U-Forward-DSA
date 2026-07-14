# mypy: disable-error-code="empty-body"
# QUESTION: Graph and Its Representation
# A graph is a non-linear data structure consisting of a set of vertices (nodes)
# and a set of edges connecting pairs of vertices. Graphs can be directed or
# undirected and may be weighted or unweighted.
# Given the number of vertices V and a list of edges, build the adjacency-list
# representation of the graph. In an undirected graph, for every edge (u, v) the
# vertex v is added to the adjacency list of u and u is added to the adjacency
# list of v.
#
# Example 1:
# Input:
#   V = 5
#   edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
# Output:
#   0 -> [1, 4]
#   1 -> [0, 2, 3, 4]
#   2 -> [1, 3]
#   3 -> [1, 2, 4]
#   4 -> [0, 1, 3]
# Explanation:
#   Each vertex's list contains all vertices directly connected to it. Because the
#   graph is undirected, every edge contributes to two adjacency lists.
#
# Constraints:
#   1 <= V <= 10^4
#   0 <= number of edges <= V * (V - 1) / 2
#   0 <= u, v < V

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
    def graph_representation_brute(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass

    def graph_representation_better(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass

    def graph_representation_optimal(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.graph_representation_optimal(5, [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]])
