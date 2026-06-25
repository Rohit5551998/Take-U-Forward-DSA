# QUESTION: Topological Sort BFS
# Given a Directed Acyclic Graph (DAG) with V vertices and E edges
# (represented as an adjacency list), return any valid topological
# ordering of the nodes. Topological sort: a linear ordering of vertices
# such that for every directed edge (u, v), u appears before v in the
# ordering.
# Use BFS — Kahn's algorithm:
#   1. Compute in-degree of every node.
#   2. Enqueue all nodes with in-degree 0.
#   3. Repeatedly dequeue, append to result, and decrement in-degrees of
#      successors (enqueue any that drop to 0).
#   4. If the result contains all V nodes, return it; otherwise the
#      graph has a cycle.


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
    def topological_sort_bfs_brute(self) -> None:
        pass

    def topological_sort_bfs_better(self) -> None:
        pass

    def topological_sort_bfs_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
