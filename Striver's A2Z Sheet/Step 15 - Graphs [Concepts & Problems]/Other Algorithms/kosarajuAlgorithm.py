# mypy: disable-error-code="empty-body"
# QUESTION: Strongly Connected Components (Kosaraju's Algorithm)
# You are given a directed graph with V vertices numbered from 0 to V-1,
# represented as an adjacency list adj where adj[u] is the list of vertices v
# such that there is a directed edge u -> v. A Strongly Connected Component (SCC)
# is a maximal set of vertices such that for every pair of vertices (a, b) in the
# set, there exists a directed path from a to b AND a directed path from b to a.
# Return the number of strongly connected components in the graph.
#
# Example 1:
# Input:
#   V = 5
#   adj = [[2, 3], [0], [1], [4], []]
#   Edges: 0 -> 2, 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 4
# Output: 3
# Explanation: The strongly connected components are {0, 1, 2} (since
#   0 -> 2 -> 1 -> 0 forms a cycle), {3}, and {4}. That gives 3 SCCs in total.
#
# Constraints:
#   1 <= V <= 5 * 10^4
#   0 <= total number of edges <= 10^5
#   0 <= adj[u][i] < V
#   The graph is directed and may contain cycles.

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
    def kosaraju_algorithm_brute(self, V: int, adj: List[List[int]]) -> int:
        pass

    def kosaraju_algorithm_better(self, V: int, adj: List[List[int]]) -> int:
        pass

    def kosaraju_algorithm_optimal(self, V: int, adj: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.kosaraju_algorithm_optimal(5, [[2, 3], [0], [1], [4], []])
