# mypy: disable-error-code="empty-body"
# QUESTION: Bridges in Graph (Tarjan's Algorithm)
# You are given an undirected connected graph with V vertices numbered from 0 to
# V-1 and a list of edges. An edge (u, v) is called a "bridge" (or critical
# connection) if removing that single edge increases the number of connected
# components of the graph, i.e. it disconnects the graph (or the part it belongs
# to). Return a list of all bridges in the graph. The order of the returned
# edges and the order of the two endpoints within an edge do not matter.
#
# Example 1:
# Input:
#   V = 5
#   edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
#   Adjacency:
#       0 -- 1
#       |  / |
#       2    3 -- 4
# Output: [[3, 4], [1, 3]]
# Explanation: Vertices 0, 1, 2 form a cycle, so none of the edges among them
#   are bridges (removing any one still leaves the trio connected). The edge
#   (1, 3) is a bridge because removing it isolates {3, 4} from the rest. The
#   edge (3, 4) is a bridge because removing it isolates vertex 4.
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
    def bridges_in_graph_brute(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass

    def bridges_in_graph_better(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass

    def bridges_in_graph_optimal(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.bridges_in_graph_optimal(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]])
