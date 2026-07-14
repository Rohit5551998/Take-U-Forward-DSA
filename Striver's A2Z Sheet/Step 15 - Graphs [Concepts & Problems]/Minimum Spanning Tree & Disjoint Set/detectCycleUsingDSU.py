# mypy: disable-error-code="empty-body"
# QUESTION: Detect Cycle in an Undirected Graph using Disjoint Set (DSU)
# Given an undirected graph of V vertices (numbered 0 to V-1) and a list of edges
# where each edge is given as [u, v] denoting an undirected connection between u
# and v, determine whether the graph contains a cycle. Use the Disjoint Set Union
# (Union-Find) data structure with union by rank/size and path compression: for
# every edge, if the two endpoints already share the same ultimate parent (i.e.
# they are already connected) before the edge is added, then adding this edge
# closes a cycle. Return True if a cycle exists, otherwise return False.
#
# Example 1:
# Input: V = 3, edges = [[0, 1], [1, 2], [2, 0]]
# Output: True
# Explanation: Vertices 0, 1, 2 form a triangle. When processing edge [2, 0],
# vertices 2 and 0 already belong to the same component, so a cycle is detected.
#
# Example 2:
# Input: V = 4, edges = [[0, 1], [1, 2], [2, 3]]
# Output: False
# Explanation: The edges form a straight chain 0 - 1 - 2 - 3 with no vertex
# reconnecting to an earlier component, so there is no cycle.
#
# Constraints:
# 1 <= V <= 10^5
# 0 <= number of edges <= V * (V - 1) / 2
# 0 <= u, v < V
# There are no self-loops and no multiple edges between the same pair.


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
    def detect_cycle_dsu_brute(self, V: int, edges: List[List[int]]) -> bool:
        pass

    def detect_cycle_dsu_better(self, V: int, edges: List[List[int]]) -> bool:
        pass

    def detect_cycle_dsu_optimal(self, V: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.detect_cycle_dsu_optimal(3, [[0, 1], [1, 2], [2, 0]])
