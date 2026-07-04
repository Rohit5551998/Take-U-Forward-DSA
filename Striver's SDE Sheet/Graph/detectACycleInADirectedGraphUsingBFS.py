# mypy: disable-error-code="empty-body"
# QUESTION: Detect A cycle in a Directed Graph using BFS
# Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an
# adjacency list where adj[i] lists all nodes connected to node i (via a directed edge i -> j).
# Determine if the graph contains any cycles.
#
# Examples:
# Example 1:
# Input: V = 6, adj = [[1], [2, 5], [3], [4], [1], []]
# Output: True
# Explanation: The graph contains a cycle: 1 -> 2 -> 3 -> 4 -> 1.
#
# Example 2:
# Input: V = 4, adj = [[1, 2], [2], [], [0, 2]]
# Output: False
# Explanation: The graph does not contain a cycle.
#
# Constraints:
# 1 <= V <= 10^4
# adj.size() == V
# 0 <= adj[i][j] < V
# 1 <= sum(adj[i].size()) <= 10^4


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
    def detect_a_cycle_in_a_directed_graph_using_bfs_brute(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass

    def detect_a_cycle_in_a_directed_graph_using_bfs_better(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass

    def detect_a_cycle_in_a_directed_graph_using_bfs_optimal(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    v = 6
    adj = [[1], [2, 5], [3], [4], [1], []]
    print(sol.detect_a_cycle_in_a_directed_graph_using_bfs_optimal(v, adj))
