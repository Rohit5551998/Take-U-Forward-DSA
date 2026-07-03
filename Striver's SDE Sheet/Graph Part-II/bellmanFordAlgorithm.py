# QUESTION: Bellman ford algorithm
# Given a weighted and directed graph of V vertices and E edges. An edge is represented as
# [ai, bi, wi], meaning there is a directed edge from ai to bi having weight wi. Find the
# shortest distance of all the vertices from the source vertex S. If a vertex can't be
# reached from S then mark the distance as 10^9.
# If the graph contains a negative cycle then return -1 in a list.
#
# Examples:
# Example 1:
# Input: V = 6, Edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2],
#        [2, 4, 3]], S = 0
# Output: 0 5 3 3 1 2
# Explanation:
# For node 1, shortest path is 0->1 (distance=5).
# For node 2, shortest path is 0->1->2 (distance=3).
# For node 3, shortest path is 0->1->5->3 (distance=3).
# For node 4, shortest path is 0->1->5->3->4 (distance=1).
# For node 5, shortest path is 0->1->5 (distance=2).
#
# Example 2:
# Input: V = 2, Edges = [[0, 1, 9]], S = 0
# Output: 0 9
# Explanation: For node 1, the shortest path is 0->1 (distance=9).
#
# Constraints:
# 1 <= V <= 500
# 1 <= E <= V*(V-1)
# -1000 <= wi <= 1000
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


class Solution:
    def bellman_ford_algorithm_brute(self) -> None:
        pass

    def bellman_ford_algorithm_better(self) -> None:
        pass

    def bellman_ford_algorithm_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
