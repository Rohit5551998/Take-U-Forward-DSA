# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Spanning Tree (Sum of Weights)
# A spanning tree of a connected, undirected, weighted graph with V vertices is a
# subgraph that includes all V vertices and exactly V-1 edges, forming a tree (no
# cycles) that keeps every vertex connected. A Minimum Spanning Tree (MST) is the
# spanning tree whose total edge weight is the smallest among all possible
# spanning trees. Given V vertices (numbered 0 to V-1) and a list of edges where
# each edge is [u, v, w] denoting an undirected edge between u and v of weight w,
# return the sum of the weights of the edges in the Minimum Spanning Tree.
#
# Example 1:
# Input: V = 5, edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2],
#                        [3, 4, 1], [4, 2, 2]]
# Output: 5
# Explanation: One MST picks the edges (0-2, w=1), (1-2, w=1), (3-4, w=1),
# (2-3, w=2), giving a total weight of 1 + 1 + 1 + 2 = 5, which connects all 5
# vertices with the minimum possible total cost.
#
# Example 2:
# Input: V = 2, edges = [[0, 1, 5]]
# Output: 5
# Explanation: The only edge must be included to connect both vertices, so the
# MST weight is 5.
#
# Constraints:
# 1 <= V <= 10^4
# V - 1 <= number of edges <= V * (V - 1) / 2
# 0 <= u, v < V
# 1 <= w <= 10^4
# The graph is connected.


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
    def minimum_spanning_tree_brute(self, V: int, edges: List[List[int]]) -> int:
        pass

    def minimum_spanning_tree_better(self, V: int, edges: List[List[int]]) -> int:
        pass

    def minimum_spanning_tree_optimal(self, V: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.minimum_spanning_tree_optimal(
    #     5,
    #     [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]],
    # )
