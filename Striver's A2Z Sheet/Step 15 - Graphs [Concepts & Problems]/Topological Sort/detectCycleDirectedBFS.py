# mypy: disable-error-code="empty-body"
# QUESTION: Detect Cycle in a Directed Graph (BFS / Kahn's)
# Given a directed graph with V vertices labelled from 0 to V-1 and its edges
# represented as an adjacency list, determine whether the graph contains a cycle.
# Return True if at least one directed cycle exists, otherwise return False.
# This is to be solved using a BFS based approach (Kahn's Algorithm): a directed
# graph has a valid topological ordering if and only if it is acyclic, so if
# Kahn's algorithm cannot order all V vertices, a cycle is present.
#
# Example 1:
# Input: V = 4, adj = [[1], [2], [3], [1]]
#        (edges: 0->1, 1->2, 2->3, 3->1)
# Output: True
# Explanation: The vertices 1 -> 2 -> 3 -> 1 form a directed cycle, so Kahn's
# algorithm fails to place all 4 vertices into the topological order.
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= number of edges <= V * (V - 1)
# Vertices are labelled from 0 to V-1.

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
    def detect_cycle_directed_bfs_brute(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_directed_bfs_better(self, V: int, adj: List[List[int]]) -> bool:
        pass

    def detect_cycle_directed_bfs_optimal(self, V: int, adj: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.detect_cycle_directed_bfs_optimal(4, [[1], [2], [3], [1]])
