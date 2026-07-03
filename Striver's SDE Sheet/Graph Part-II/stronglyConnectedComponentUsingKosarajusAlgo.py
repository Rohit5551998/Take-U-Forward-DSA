# QUESTION: Strongly Connected Component (using Kosaraju's algo)
# You are given a directed graph with V vertices, numbered from 0 to V-1, and its adjacency
# list Adj, where Adj[i] contains all vertices j such that there is a directed edge from
# vertex i to vertex j. Your task is to find the number of strongly connected components
# (SCCs) in the graph. A strongly connected component is a maximal set of vertices such
# that every vertex in the set is reachable from every other vertex in the set via
# directed paths.
#
# Examples:
# Example 1:
# Input: V = 5, Adj = [[2, 3], [0], [1], [4], []]
# Output: 3
# Explanation: The three SCCs are {0, 1, 2} (the cycle 0->2->1->0), {3} and {4}.
#
# Example 2:
# Input: V = 8, Adj = [[1], [2], [0, 3], [4], [5, 7], [6], [4, 7], []]
# Output: 4
# Explanation: The four SCCs are {0, 1, 2}, {3}, {4, 5, 6} and {7}.
#
# Constraints:
# 1 <= V <= 5000
# 0 <= E <= V*(V-1)
# 0 <= ai, bi <= V-1


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
    def strongly_connected_component_using_kosarajus_algo_brute(self) -> None:
        pass

    def strongly_connected_component_using_kosarajus_algo_better(self) -> None:
        pass

    def strongly_connected_component_using_kosarajus_algo_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
