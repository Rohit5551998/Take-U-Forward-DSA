# QUESTION: Topological Sort BFS
# Given a Directed Acyclic Graph (DAG) with V vertices labeled from 0 to V-1. The graph is
# represented using an adjacency list where adj[i] lists all nodes connected to node i (via a
# directed edge i -> j). Find any Topological Sorting of that Graph.
# In topological sorting, node u will always appear before node v if there is a directed edge
# from node u towards node v (u -> v).
# The function should return an array representing the topological order. The output will be
# validated by driver code, which checks the correctness of your topological sort.
#
# Examples:
# Example 1:
# Input: V = 6, adj = [[], [], [3], [1], [0, 1], [0, 2]]
# Output: [5, 4, 2, 3, 1, 0]
# Explanation: A graph may have multiple topological sortings.
# - Node 5 must appear before 0 and 2
# - Node 2 must appear before 3
# - Node 3 must appear before 1
# - Node 4 must appear before 0 and 1
# One valid topological order is: [5, 4, 2, 3, 1, 0]
#
# Example 2:
# Input: V = 4, adj = [[], [0], [0], [0]]
# Output: [3, 2, 1, 0]
# Explanation: Nodes 1, 2, and 3 must all appear before 0; their internal order doesn't matter.
# One valid topological order is: [3, 2, 1, 0]
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= number of edges <= 10^4


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


class Solution:
    def topological_sort_bfs_brute(self) -> None:
        pass

    def topological_sort_bfs_better(self) -> None:
        pass

    def topological_sort_bfs_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
