# mypy: disable-error-code="empty-body"
# QUESTION: M Coloring Problem
# Given an undirected graph with V vertices and a number m, determine if the graph
# can be colored with at most m colors such that no two adjacent vertices share
# the same color. Return True if such a coloring is possible, else False.
# Example 1:
# Input: V = 4, m = 3, edges = [[0,1],[1,2],[2,3],[3,0],[0,2]]
# Output: True
# Explanation: A valid 3-coloring assignment exists for the given graph.
# Example 2:
# Input: V = 3, m = 2, edges = [[0,1],[1,2],[2,0]] (triangle)
# Output: False
# Constraints:
# 1 <= V <= 20
# 1 <= m <= V
# 0 <= number of edges <= V*(V-1)/2

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
    def graph_coloring_brute(self, edges: List[List[int]], v: int, m: int) -> bool:
        pass

    def graph_coloring_better(self, edges: List[List[int]], v: int, m: int) -> bool:
        pass

    def graph_coloring_optimal(self, edges: List[List[int]], v: int, m: int) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     e = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
#     print(sol.graph_coloring_optimal(e, 4, 3))
