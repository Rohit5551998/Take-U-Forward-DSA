# mypy: disable-error-code="empty-body"
# QUESTION: Detect A cycle in Undirected Graph using DFS
# Given an undirected graph with V vertices and E edges, check whether it contains any
# cycle or not using DFS.
#
# Examples:
# Input : V = 8, E = 7
#
# Output : False
# Explanation : No cycle is present in the given graph
#
# Input : V = 8, E = 6
#
# Output : True
# Explanation : 4->5->6->4 is a cycle.


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
    def detect_a_cycle_in_undirected_graph_using_dfs_brute(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass

    def detect_a_cycle_in_undirected_graph_using_dfs_better(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass

    def detect_a_cycle_in_undirected_graph_using_dfs_optimal(
        self, v: int, adj: List[List[int]]
    ) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    v = 5
    adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
    print(sol.detect_a_cycle_in_undirected_graph_using_dfs_optimal(v, adj))
