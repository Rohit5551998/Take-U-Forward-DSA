# mypy: disable-error-code="empty-body"
# QUESTION: Cheapest Flights Within K Stops
# There are n cities (0-indexed) connected by some number of flights. You are given
# an array flights where flights[i] = [from_i, to_i, price_i] indicates a flight
# from city from_i to city to_i with cost price_i. Given src, dst and an integer k,
# return the cheapest price to travel from src to dst using at most k stops
# (i.e. at most k intermediate cities, equivalently k+1 edges). If there is no such
# route, return -1.
#
# Example 1:
# Input:
#   n = 4
#   flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
#   src = 0, dst = 3, k = 1
# Output: 700
# Explanation: The route 0 -> 1 -> 3 costs 100 + 600 = 700 with 1 stop. The
# cheaper route 0 -> 1 -> 2 -> 3 costs 400 but uses 2 stops, which exceeds k = 1.
#
# Constraints:
# 1 <= n <= 100
# 0 <= flights.length <= n * (n - 1)
# flights[i].length == 3
# 0 <= from_i, to_i < n, from_i != to_i
# 1 <= price_i <= 10^4
# 0 <= src, dst < n, src != dst
# 0 <= k < n

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
    def cheapest_flights_within_k_stops_brute(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        pass

    def cheapest_flights_within_k_stops_better(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        pass

    def cheapest_flights_within_k_stops_optimal(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.cheapest_flights_within_k_stops_optimal(
    #     4,
    #     [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
    #     0,
    #     3,
    #     1,
    # )
