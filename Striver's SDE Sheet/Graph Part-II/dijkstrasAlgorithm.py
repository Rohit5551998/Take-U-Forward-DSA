# mypy: disable-error-code="empty-body"
# QUESTION: Dijkstra's algorithm
# Given a weighted, undirected graph of V vertices, numbered from 0 to V-1, and a 2D
# vector/array which represents the edges. Each entry in edges[i] is of the form
# [u, v, weight], where u, v represent the vertices having an undirected edge between them,
# and weight is the weight of the edge between u and v.
# Given a source node S, find the shortest distance of all the vertices from the source
# vertex S. Return a list of integers denoting the shortest distance between each node and
# source vertex S. If a vertex is not reachable from the source then its distance will
# be 10^9.
#
# Examples:
# Example 1:
# Input: V = 2, edges = [[0, 1, 9]], S = 0
# Output: [0, 9]
# Explanation: The shortest distance from node 0 (source) to node 0 is 0, and the shortest
# distance from node 0 to node 1 is 9.
#
# Example 2:
# Input: V = 3, edges = [[0, 1, 1], [0, 2, 6], [1, 2, 3]], S = 2
# Output: [4, 3, 0]
# Explanation:
# For node 0, the shortest path is 2->1->0 (distance=4).
# For node 1, the shortest path is 2->1 (distance=3).
# For node 2 (the source), the distance is 0.
#
# Constraints:
# 1 <= V <= 10000
# 0 <= edges[i][j] <= 10000
# 1 <= edges.size() <= (V*(V-1))/2
# 0 <= S < V


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
    def dijkstras_algorithm_brute(self, v: int, edges: List[List[int]], s: int) -> List[int]:
        pass

    def dijkstras_algorithm_better(self, v: int, edges: List[List[int]], s: int) -> List[int]:
        pass

    def dijkstras_algorithm_optimal(self, v: int, edges: List[List[int]], s: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    v = 3
    edges = [[0, 1, 1], [0, 2, 6], [1, 2, 3]]
    s = 2
    print(sol.dijkstras_algorithm_optimal(v, edges, s))
