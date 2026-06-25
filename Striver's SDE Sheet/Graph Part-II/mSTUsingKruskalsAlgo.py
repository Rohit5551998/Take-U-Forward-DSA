# QUESTION: MST using Kruskal's Algo
# Given a weighted, undirected, and connected graph of V vertices and E
# edges, find the sum of weights of the edges of the Minimum Spanning
# Tree (MST). An MST is a subset of E edges that connects all V vertices
# with the minimum total edge weight and contains no cycles.
# Use Kruskal's algorithm:
#   1. Sort all edges in non-decreasing order of weight.
#   2. Initialize Union-Find (Disjoint Set Union) with V components.
#   3. Iterate sorted edges; if the endpoints are in different components,
#      union them and add the edge weight to the MST total.
#   4. Stop when V-1 edges have been added.
#
# Examples:
# Example 1:
# Input: V = 4, edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4]]
# Output: 6
# Explanation:
# Edges included in the MST (Minimum Spanning Tree) are:
# - [0, 1, 1] with weight 1
# - [1, 2, 2] with weight 2
# - [2, 3, 3] with weight 3
# The total weight of the MST is 1 + 2 + 3 = 6. These edges form a spanning tree that connects all vertices (0, 1, 2, 3) with the minimum possible total edge weight, satisfying the MST properties.
#
# Example 2:
# Input: V = 3, edges = [[0, 1, 5], [1, 2, 10], [2, 0, 15]]
# Output: 15
# Explanation:
# Edges included in the MST are:
# - [0, 1, 5] with weight 5
# - [1, 2, 10] with weight 10
# The total weight of the MST is 5 + 10 = 15.


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
    def mst_using_kruskals_algo_brute(self) -> None:
        pass

    def mst_using_kruskals_algo_better(self) -> None:
        pass

    def mst_using_kruskals_algo_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
