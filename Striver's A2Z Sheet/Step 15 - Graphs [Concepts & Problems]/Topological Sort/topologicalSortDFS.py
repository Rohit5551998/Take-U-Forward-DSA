# mypy: disable-error-code="empty-body"
# QUESTION: Topological Sort (DFS)
# Given a Directed Acyclic Graph (DAG) with V vertices labelled from 0 to V-1 and
# a list of edges represented as an adjacency list, return any valid topological
# ordering of its vertices.
# A topological ordering is a linear ordering of vertices such that for every
# directed edge u -> v, vertex u comes before vertex v in the ordering.
# (A valid topological ordering exists if and only if the graph is a DAG.)
#
# Example 1:
# Input: V = 6, adj = [[], [], [3], [1], [0, 1], [0, 2]]
#        (edges: 5->0, 5->2, 4->0, 4->1, 2->3, 3->1)
# Output: [5, 4, 2, 3, 1, 0]
# Explanation: For every edge u -> v, u appears before v. Multiple valid orderings
# exist; any one of them is accepted.
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= number of edges <= V * (V - 1) / 2
# The graph is a Directed Acyclic Graph (no cycles).

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
    def topological_sort_dfs_brute(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def topological_sort_dfs_better(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def topological_sort_dfs_optimal(self, V: int, adj: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.topological_sort_dfs_optimal(6, [[], [], [3], [1], [0, 1], [0, 2]])
