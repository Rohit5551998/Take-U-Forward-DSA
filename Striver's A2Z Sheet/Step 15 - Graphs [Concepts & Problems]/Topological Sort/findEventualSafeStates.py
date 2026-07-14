# mypy: disable-error-code="empty-body"
# QUESTION: Find Eventual Safe States
# You are given a directed graph with n nodes labelled from 0 to n-1, represented
# as an adjacency list graph, where graph[i] is the list of nodes reachable from
# node i by a single directed edge.
# A node is a terminal node if it has no outgoing edges. A node is a safe node if
# every possible path starting from that node leads to a terminal node (i.e. no
# path from it can ever enter a cycle).
# Return an array containing all safe nodes in ascending order.
#
# Example 1:
# Input: graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
# Output: [2, 4, 5, 6]
# Explanation: Nodes 5 and 6 are terminal. Node 2 only leads to 5, and node 4
# only leads to 5, so both are safe. Nodes 0, 1, 3 can reach the cycle 0->2->5?
# no: 0->1->3->0 forms a cycle, so 0, 1, 3 are unsafe.
#
# Constraints:
# n == len(graph)
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] contains distinct values.
# The total number of edges does not exceed 4 * 10^4.

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
    def find_eventual_safe_states_brute(self, graph: List[List[int]]) -> List[int]:
        pass

    def find_eventual_safe_states_better(self, graph: List[List[int]]) -> List[int]:
        pass

    def find_eventual_safe_states_optimal(self, graph: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.find_eventual_safe_states_optimal([[1, 2], [2, 3], [5], [0], [5], [], []])
