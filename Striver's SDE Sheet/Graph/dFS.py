# mypy: disable-error-code="empty-body"
# QUESTION: DFS
# Given an undirected graph (represented as an adjacency list), starting
# from vertex 0, return a list of all nodes obtained by traversing the
# graph using Depth-First Search (DFS). The order should be the standard
# DFS order: visit a node, then recursively visit its unvisited
# neighbors in adjacency-list order.
#
# Examples:
# Example 1:
# Input: V = 5, adj = [[2,3], [1,4,5], [1], [2,5], [4,5]]
# Output: [1, 2, 4, 5, 3]
# Explanation: Start at 1; DFS visits 2, then 4, then 5, backtracks, then 3.
#
# Example 2:
# Input: V = 4, adj = [[2,3], [1,4], [1], [2]]
# Output: [1, 2, 4, 3]
# Explanation: Start at 1; DFS visits 2, then 4, backtracks, then 3.


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
    def dfs_brute(self, v: int, adj: List[List[int]]) -> List[int]:
        pass

    def dfs_better(self, v: int, adj: List[List[int]]) -> List[int]:
        pass

    def dfs_optimal(self, v: int, adj: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    v = 5
    adj = [[2, 3], [1, 4, 5], [1], [2, 5], [4, 5]]
    print(sol.dfs_optimal(v, adj))
