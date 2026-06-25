# QUESTION: Strongly Connected Component (using Kosaraju's algo)
# Given a Directed Graph with V vertices (numbered 0 to V-1) and E edges,
# find the number of Strongly Connected Components (SCCs) in the graph.
# A Strongly Connected Component is a maximal set of vertices such that
# every vertex in the set is reachable from every other vertex in the
# set via directed paths.
# Use Kosaraju's algorithm:
#   1. Run DFS on the original graph; push each vertex onto a stack when
#      its DFS completes (i.e., in order of decreasing finish time).
#   2. Transpose the graph (reverse every edge direction).
#   3. Pop vertices from the stack one by one; for each unvisited
#      vertex, run DFS on the transposed graph — each such DFS tree is
#      one SCC. Increment the SCC count.


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
    def strongly_connected_component_using_kosarajus_algo_brute(self) -> None:
        pass

    def strongly_connected_component_using_kosarajus_algo_better(self) -> None:
        pass

    def strongly_connected_component_using_kosarajus_algo_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
