# mypy: disable-error-code="empty-body"
# QUESTION: Detect Cycle in a Directed Graph (DFS)
# Given a directed graph with V vertices (labelled 0 to V-1) provided as an
# adjacency list adj (where adj[i] is the list of vertices reachable from vertex
# i by a directed edge i -> adj[i][k]), determine whether the graph contains any
# directed cycle.
# The graph may be disconnected, so all components must be checked. Use a DFS
# based traversal that tracks the vertices currently in the recursion stack
# (path) to detect a back edge.
# Return True if the graph contains a directed cycle, otherwise return False.
#
# Example 1:
# Input: V = 4, adj = [[1], [2], [3], [1]]
# Output: True
# Explanation: The directed edges 1 -> 2 -> 3 -> 1 form a cycle, so the graph
# contains a cycle.
#
# Constraints:
# 1 <= V <= 10^5
# 0 <= len(adj[i]) < V
# 0 <= adj[i][k] < V

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
    def detect_cycle_directed_dfs_brute(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_directed_dfs_better(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_directed_dfs_optimal(self, V: int, adj: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.detect_cycle_directed_dfs_optimal(4, [[1], [2], [3], [1]])
