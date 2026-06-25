# QUESTION: Dijkstra's algorithm
# Given a weighted, undirected, and connected graph of V vertices and E
# edges (represented as an adjacency list of [neighbor, weight] pairs),
# find the shortest distance of all vertices from a given source vertex S.
# Note: The graph does NOT contain any negative edge weights (Dijkstra
# requires non-negative weights).
# Use a Priority Queue (min-heap) keyed on distance:
#   1. Initialize dist[S] = 0, dist[v] = infinity for v != S.
#   2. Push (0, S) onto the heap.
#   3. Pop the smallest-distance node; for each neighbor, relax the edge
#      (if dist[u] + w < dist[v], update dist[v] and push (dist[v], v)).
#   4. Continue until the heap is empty. The dist[] array is the answer.


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
    def dijkstras_algorithm_brute(self) -> None:
        pass

    def dijkstras_algorithm_better(self) -> None:
        pass

    def dijkstras_algorithm_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
