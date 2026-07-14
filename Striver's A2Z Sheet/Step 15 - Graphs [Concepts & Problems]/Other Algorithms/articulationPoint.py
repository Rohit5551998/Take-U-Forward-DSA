# mypy: disable-error-code="empty-body"
# QUESTION: Articulation Point in Graph
# You are given an undirected graph with V vertices numbered from 0 to V-1 and a
# list of edges. A vertex is called an "articulation point" (or cut vertex) if
# removing that vertex, along with all edges incident to it, increases the number
# of connected components of the graph, i.e. disconnects some previously
# connected part of the graph. Return a sorted list of all articulation points.
# If there are no articulation points, return a list containing a single element
# -1.
#
# Example 1:
# Input:
#   V = 5
#   edges = [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]]
#   Adjacency:
#       0 -- 1 -- 4 -- 2
#                 |    |
#                 3 -- 2  (3 -- 4 and 2 -- 3)
# Output: [1, 4]
# Explanation: Removing vertex 4 disconnects {0, 1} from {2, 3}, so 4 is an
#   articulation point. Removing vertex 1 disconnects vertex 0 from the rest, so
#   1 is also an articulation point. Removing any other single vertex keeps the
#   remaining graph connected.
#
# Constraints:
#   1 <= V <= 10^5
#   0 <= edges.length <= min(10^5, V * (V - 1) / 2)
#   edges[i].length == 2
#   0 <= edges[i][0], edges[i][1] < V
#   There are no parallel edges and no self-loops.

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
    def articulation_point_brute(self, V: int, edges: List[List[int]]) -> List[int]:
        pass

    def articulation_point_better(self, V: int, edges: List[List[int]]) -> List[int]:
        pass

    def articulation_point_optimal(self, V: int, edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.articulation_point_optimal(5, [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]])
