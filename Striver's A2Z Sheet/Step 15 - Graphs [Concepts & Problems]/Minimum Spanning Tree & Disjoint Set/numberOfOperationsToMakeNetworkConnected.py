# mypy: disable-error-code="empty-body"
# QUESTION: Number of Operations to Make Network Connected
# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# forming a network, where connections[i] = [a, b] represents a cable between
# computers a and b. Any computer can reach any other computer directly or
# indirectly through the network.
# You are given the initial layout of connections. You can extract certain
# cables between two directly connected computers and place them between any
# pair of disconnected computers to make them connected.
# Return the minimum number of operations to connect all the computers. If it
# is not possible, return -1.
#
# Example 1:
# Input: n = 4, connections = [[0, 1], [0, 2], [1, 2]]
# Output: 1
# Explanation: Remove the cable between computers 1 and 2 and place it between
# computers 1 and 3. There is exactly one extra cable and two components need
# joining, so one operation suffices.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= connections.length <= min(n * (n - 1) / 2, 10^5)
# connections[i].length == 2
# 0 <= a, b < n
# a != b
# There are no repeated connections and no self-loops.

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
    def make_connected_brute(self, n: int, connections: List[List[int]]) -> int:
        pass

    def make_connected_better(self, n: int, connections: List[List[int]]) -> int:
        pass

    def make_connected_optimal(self, n: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.make_connected_optimal(4, [[0, 1], [0, 2], [1, 2]])
