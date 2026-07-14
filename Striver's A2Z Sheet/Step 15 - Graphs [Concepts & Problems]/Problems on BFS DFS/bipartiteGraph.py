# mypy: disable-error-code="empty-body"
# QUESTION: Bipartite Graph
# Given an undirected graph with V vertices (labelled 0 to V-1) provided as an
# adjacency list adj (where adj[i] is the list of vertices adjacent to vertex i),
# determine whether the graph is bipartite.
# A graph is bipartite if its vertices can be partitioned into two disjoint sets
# such that every edge connects a vertex in one set to a vertex in the other set
# (equivalently, the graph can be coloured using exactly two colours so that no
# two adjacent vertices share the same colour).
# The graph may be disconnected. Return True if the graph is bipartite, otherwise
# return False.
#
# Example 1:
# Input: V = 4, adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
# Output: True
# Explanation: The vertices can be split into sets {0, 2} and {1, 3}; every edge
# goes between the two sets, so the graph is bipartite.
#
# Constraints:
# 1 <= V <= 10^5
# 0 <= len(adj[i]) < V
# The graph has no self-loops.

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
    def bipartiteGraph_brute(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def bipartiteGraph_better(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def bipartiteGraph_optimal(self, V: int, adj: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.bipartiteGraph_optimal(4, [[1, 3], [0, 2], [1, 3], [0, 2]])
