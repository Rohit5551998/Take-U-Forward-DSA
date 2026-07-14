# mypy: disable-error-code="empty-body"
# QUESTION: Number of Ways to Arrive at Destination
# You are in a city with n intersections numbered from 0 to n-1 with bidirectional
# roads between some intersections. You are given an integer n and a 2D array roads
# where roads[i] = [u, v, time] means there is a road between intersections u and v
# that takes time minutes to travel. You want to know in how many ways you can
# travel from intersection 0 to intersection n-1 in the shortest amount of time.
# Return the number of ways modulo 10^9 + 7.
#
# Example 1:
# Input:
#   n = 7
#   roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],
#            [6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
# Explanation: The shortest time from intersection 0 to 6 is 7 minutes, and there
# are 4 distinct shortest paths achieving that time.
#
# Constraints:
# 1 <= n <= 200
# n - 1 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 3
# 0 <= u, v < n, u != v
# 1 <= time <= 10^9
# There is at most one road between any two intersections; the graph is connected.

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
    def number_of_ways_to_arrive_at_destination_brute(self, n: int, roads: List[List[int]]) -> int:
        pass

    def number_of_ways_to_arrive_at_destination_better(self, n: int, roads: List[List[int]]) -> int:
        pass

    def number_of_ways_to_arrive_at_destination_optimal(
        self, n: int, roads: List[List[int]]
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.number_of_ways_to_arrive_at_destination_optimal(
    #     7,
    #     [
    #         [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
    #         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2],
    #     ],
    # )
