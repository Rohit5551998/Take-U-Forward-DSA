# mypy: disable-error-code="empty-body"
# QUESTION: M-Coloring Problem (Graph Coloring)
# You are given an undirected graph of V vertices and a number M. The graph is
# provided as an adjacency matrix (or edge list) where an edge between vertex i
# and vertex j means they are directly connected. Determine whether it is
# possible to color all the vertices of the graph using at most M colors such
# that no two adjacent vertices share the same color. Return True if such a
# coloring exists, otherwise return False.
#
# Example 1:
# Input: V = 4, M = 3,
#        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
# Output: True
# Explanation: The graph can be colored with 3 colors so that no two adjacent
# vertices have the same color, e.g. color[0]=1, color[1]=2, color[2]=3,
# color[3]=2. No edge connects two vertices of the same color.
#
# Example 2:
# Input: V = 3, M = 1,
#        edges = [[0, 1], [1, 2], [2, 0]]
# Output: False
# Explanation: A triangle needs at least 3 colors; with only 1 color available,
# adjacent vertices would necessarily share a color, so it is impossible.
#
# Constraints:
# 1 <= V <= 20
# 1 <= M <= V
# 0 <= number of edges <= V * (V - 1) / 2
# There are no self-loops.


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
    def graph_coloring_brute(self, V: int, m: int, edges: List[List[int]]) -> bool:
        pass

    def graph_coloring_better(self, V: int, m: int, edges: List[List[int]]) -> bool:
        pass

    def graph_coloring_optimal(self, V: int, m: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.graph_coloring_optimal(4, 3, [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]])
