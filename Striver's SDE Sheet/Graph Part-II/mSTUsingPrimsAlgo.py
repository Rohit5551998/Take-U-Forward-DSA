# QUESTION: MST using Prim's Algo
# Given a weighted, undirected, and connected graph of V vertices and E
# edges (represented as an adjacency list of [neighbor, weight] pairs),
# find the sum of weights of the edges of the Minimum Spanning Tree (MST).
# An MST is a subset of E edges that connects all V vertices with the
# minimum total edge weight and contains no cycles.
# Use Prim's algorithm (priority-queue based):
#   1. Start from any vertex (say 0). Mark it in the MST. Push all its
#      edges into a min-heap keyed on edge weight.
#   2. While the heap isn't empty: pop the minimum-weight edge. If the
#      other endpoint isn't yet in the MST, add it, accumulate the weight,
#      and push its outgoing edges into the heap.
#   3. Repeat until V vertices are included.
# (Note: sometimes "the MST" is unique; sometimes multiple MSTs exist
# with the same total weight — any one is acceptable.)


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
    def mst_using_prims_algo_brute(self) -> None:
        pass

    def mst_using_prims_algo_better(self) -> None:
        pass

    def mst_using_prims_algo_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
