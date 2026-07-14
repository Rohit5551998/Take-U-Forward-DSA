# mypy: disable-error-code="empty-body"
# QUESTION: Most Stones Removed with Same Row or Column
# On a 2D plane, we place n stones at some integer coordinate points. Each
# coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column
# as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the
# location of the i-th stone, return the largest possible number of stones
# that can be removed.
#
# Example 1:
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: All six stones form a single connected component (linked by
# shared rows/columns). From a connected component of size k, at most k - 1
# stones can be removed, leaving one stone. Here 6 - 1 = 5 stones removed.
#
# Constraints:
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# No two stones are at the same coordinate point.

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
    def remove_stones_brute(self, stones: List[List[int]]) -> int:
        pass

    def remove_stones_better(self, stones: List[List[int]]) -> int:
        pass

    def remove_stones_optimal(self, stones: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.remove_stones_optimal([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
