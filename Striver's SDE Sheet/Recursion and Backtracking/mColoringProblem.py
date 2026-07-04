# mypy: disable-error-code="empty-body"
# QUESTION: M Coloring Problem
# Given an integer M and an undirected graph with N vertices (zero indexed) and E edges. The goal
# is to determine whether the graph can be coloured with a maximum of M colors so that no two of
# its adjacent vertices have the same colour applied to them. In this context, colouring a graph
# refers to giving each vertex a colour. If the colouring of vertices is possible then return
# true, otherwise return false.
#
# Examples:
# Example 1:
# Input: N = 4, M = 3, E = 5, Edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
# Output: true
# Explanation: Consider the three colors to be red, green, blue.
# We can color vertex 0 with red, vertex 1 with blue, vertex 2 with green, vertex 3 with blue.
# In this way we can color the graph using 3 colors at most.
#
# Example 2:
# Input: N = 3, M = 2, E = 3, Edges = [(0, 1), (1, 2), (0, 2)]
# Output: false
# Explanation: Consider the two colors to be red, green.
# We can color vertex 0 with red and vertex 1 with green.
# As vertex 2 is adjacent to both vertex 1 and vertex 0, it can be colored with neither red nor
# green. Hence, as we could not color all vertices of the graph, we return false.
#
# Constraints:
# - 1 <= N <= 20
# - 1 <= E <= (N*(N-1)/2)
# - 1 <= M <= N


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
    def m_coloring_problem_brute(self, n: int, m: int, edges: List[List[int]]) -> bool:
        pass

    def m_coloring_problem_better(self, n: int, m: int, edges: List[List[int]]) -> bool:
        pass

    def m_coloring_problem_optimal(self, n: int, m: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 4
    m = 3
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
    print(sol.m_coloring_problem_optimal(n, m, edges))
