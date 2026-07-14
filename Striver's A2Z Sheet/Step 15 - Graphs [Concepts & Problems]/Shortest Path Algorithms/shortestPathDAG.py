# mypy: disable-error-code="empty-body"
# QUESTION: Shortest Path in a DAG
# Given a Directed Acyclic Graph (DAG) with V vertices (0-indexed) and E edges,
# where each edge (u, v, wt) goes from u to v with weight wt, find the shortest
# distance from source vertex 0 to every other vertex. If a vertex is
# unreachable from vertex 0, its distance should be reported as -1 (or infinity).
# Edges are given as a list of [u, v, wt] triples.
#
# Example 1:
# Input:
#   V = 6, E edges =
#   [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
# Output: [0, 2, 3, 6, 1, 5]
# Explanation: Using a topological order and relaxing edges in that order gives
# the shortest distance from vertex 0 to each vertex 0..5.
#
# Constraints:
# 1 <= V <= 10^4
# 0 <= E <= 10^5
# 0 <= u, v < V
# 0 <= wt <= 10^3
# The graph is guaranteed to be a DAG (no cycles).

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
    def shortest_path_dag_brute(self, edges: List[List[int]], V: int) -> List[int]:
        pass

    def shortest_path_dag_better(self, edges: List[List[int]], V: int) -> List[int]:
        pass

    def shortest_path_dag_optimal(self, edges: List[List[int]], V: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.shortest_path_dag_optimal(
    #     [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]],
    #     6,
    # )
