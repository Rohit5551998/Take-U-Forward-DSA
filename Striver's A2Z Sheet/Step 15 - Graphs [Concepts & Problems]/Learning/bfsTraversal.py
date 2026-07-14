# mypy: disable-error-code="empty-body"
# QUESTION: BFS Traversal of Graph
# Given an undirected graph with V vertices (numbered from 0 to V-1) represented
# as an adjacency list, return the Breadth First Search (BFS) traversal of the
# graph starting from vertex 0.
# BFS explores the graph level by level: it visits the start vertex, then all of
# its unvisited neighbours, then their unvisited neighbours, and so on, using a
# queue to track the order of exploration.
#
# Example 1:
# Input:
#   V = 5
#   adj = [[1, 2, 3], [0], [0, 4], [0], [2]]
# Output:
#   [0, 1, 2, 3, 4]
# Explanation:
#   Starting at 0 we visit 0, then its neighbours 1, 2, 3 (level 1), then the
#   unvisited neighbour of 2 which is 4 (level 2). The resulting order is
#   0 1 2 3 4.
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
    def bfs_traversal_brute(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def bfs_traversal_better(self, V: int, adj: List[List[int]]) -> List[int]:
        pass

    def bfs_traversal_optimal(self, V: int, adj: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.bfs_traversal_optimal(5, [[1, 2, 3], [0], [0, 4], [0], [2]])
