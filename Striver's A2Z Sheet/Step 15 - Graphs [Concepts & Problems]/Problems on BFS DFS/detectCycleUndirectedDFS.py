# mypy: disable-error-code="empty-body"
# QUESTION: Detect Cycle in an Undirected Graph (DFS)
# Given an undirected graph with V vertices (labelled 0 to V-1) provided as an
# adjacency list adj (where adj[i] is the list of vertices adjacent to vertex i),
# determine whether the graph contains any cycle.
# The graph may be disconnected, so all components must be checked. Use a DFS
# based traversal (tracking the parent of each vertex) to solve the problem.
# Return True if the graph contains a cycle, otherwise return False.
#
# Example 1:
# Input: V = 4, adj = [[1, 2], [0, 2], [0, 1], []]
# Output: True
# Explanation: The path 0 -> 1 -> 2 -> 0 forms a cycle, so the graph contains a
# cycle.
#
# Constraints:
# 1 <= V <= 10^5
# 0 <= len(adj[i]) < V
# The graph has no self-loops or multiple edges.

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
    def detect_cycle_undirected_dfs_brute(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_undirected_dfs_better(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_undirected_dfs_optimal(self, V: int, adj: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.detect_cycle_undirected_dfs_optimal(4, [[1, 2], [0, 2], [0, 1], []])
