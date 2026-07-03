# QUESTION: Bipartite graph
# Given an undirected graph with V vertices labeled from 0 to V-1. The graph is represented using
# a 2D vector `edges`, where edges[i] represents an undirected edge between edges[i][0] and
# edges[i][1]. Determine if the graph is bipartite or not.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
# every edge in the graph connects a node in set A and a node in set B.
#
# Examples:
# Example 1:
# Input: V = 4, edges = [[0, 1], [0, 3], [1, 2], [2, 3]]
# Output: True
# Explanation: The given graph is bipartite since we can partition the nodes into two sets:
# {0, 2} and {1, 3}.
#
# Example 2:
# Input: V = 4, edges = [[0, 1], [0, 2], [0, 3], [2, 1], [3, 2]]
# Output: False
# Explanation: The graph is not bipartite. If we attempt to partition the nodes into two sets, we
# encounter an edge that connects two nodes within the same set, which violates the bipartite
# property.
#
# Constraints:
# 1 <= V, E <= 10^4 (E = number of edges)


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
    def bipartite_graph_brute(self) -> None:
        pass

    def bipartite_graph_better(self) -> None:
        pass

    def bipartite_graph_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
