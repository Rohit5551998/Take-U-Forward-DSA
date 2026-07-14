# mypy: disable-error-code="empty-body"
# QUESTION: Number of Connected Components in an Undirected Graph
# Given an integer V representing the number of vertices (labelled 0 to V-1) in
# an undirected graph, and a list of undirected edges where each edge is a pair
# [u, v] denoting a connection between vertex u and vertex v, return the number
# of connected components in the graph.
# A connected component is a maximal set of vertices such that there is a path
# between every pair of vertices within the set.
#
# Example 1:
# Input: V = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2
# Explanation: Vertices {0, 1, 2} form one component and {3, 4} form another.
# Total number of connected components = 2.
#
# Constraints:
# 1 <= V <= 10^5
# 0 <= len(edges) <= 10^5
# 0 <= u, v < V
# There are no self-loops or repeated edges.

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
    def connectedComponents_brute(self, V: int, edges: List[List[int]]) -> int:
        pass

    def connectedComponents_better(self, V: int, edges: List[List[int]]) -> int:
        pass

    def connectedComponents_optimal(self, V: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.connectedComponents_optimal(5, [[0, 1], [1, 2], [3, 4]])
