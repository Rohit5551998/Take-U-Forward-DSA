# mypy: disable-error-code="empty-body"
# QUESTION: Find the City With the Smallest Number of Neighbours
# There are n cities numbered from 0 to n-1. Given an array edges where
# edges[i] = [from_i, to_i, weight_i] represents a bidirectional and weighted edge
# between cities from_i and to_i, and an integer distanceThreshold, return the city
# with the smallest number of cities reachable through some path whose total edge
# weight is at most distanceThreshold. If there are multiple such cities, return
# the city with the greatest number (largest index).
#
# Example 1:
# Input:
#   n = 4
#   edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
#   distanceThreshold = 4
# Output: 3
# Explanation: The reachable-within-threshold neighbour counts are:
#   City 0 -> [1, 2] (2 cities)
#   City 1 -> [0, 2, 3] (3 cities)
#   City 2 -> [1, 3] (2 cities)
#   City 3 -> [1, 2] (2 cities)
# Cities 0, 2 and 3 all have 2 neighbours; the answer is the greatest index, 3.
#
# Constraints:
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= from_i, to_i < n, from_i != to_i
# 1 <= weight_i, distanceThreshold <= 10^4
# All (from_i, to_i) pairs are distinct.

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
    def find_the_city_brute(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        pass

    def find_the_city_better(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        pass

    def find_the_city_optimal(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.find_the_city_optimal(
    #     4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4
    # )
