# mypy: disable-error-code="empty-body"
# QUESTION: DFS Traversal of Graph
# Given an undirected graph with V vertices (numbered from 0 to V-1) represented
# as an adjacency list, return the Depth First Search (DFS) traversal of the graph
# starting from vertex 0.
# DFS explores as far as possible along each branch before backtracking: it visits
# the start vertex, then recursively visits its first unvisited neighbour, going
# deeper until no unvisited neighbour remains, then backtracks.
#
# Example 1:
# Input:
#   V = 5
#   adj = [[1, 2, 3], [0], [0, 4], [0], [2]]
# Output:
#   [0, 1, 2, 4, 3]
# Explanation:
#   Starting at 0 we go to 1, backtrack, go to 2 then deep to 4, backtrack, then
#   go to 3. The resulting DFS order is 0 1 2 4 3.
#
# Constraints:
#   1 <= V <= 10^4
#   0 <= adj[i][j] < V
#   The graph does not contain self-loops or multiple edges between the same pair.

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
    def dfs_traversal_brute(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def dfs_traversal_better(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def dfs_traversal_optimal(self, V: int, adj: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.dfs_traversal_optimal(5, [[1, 2, 3], [0], [0, 4], [0], [2]])
