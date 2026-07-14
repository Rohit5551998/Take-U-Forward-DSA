# mypy: disable-error-code="empty-body"
# QUESTION: Number of Provinces
# You are given an undirected graph of V vertices (cities) represented as an
# adjacency matrix isConnected of size V x V, where isConnected[i][j] = 1 means
# city i and city j are directly connected, and 0 means they are not.
# A province is a group of directly or indirectly connected cities such that no
# city outside the group is connected to any city inside it.
# Return the total number of provinces (i.e. the number of connected components).
#
# Example 1:
# Input: isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# Output: 2
# Explanation: Cities 0 and 1 are connected forming one province. City 2 is
# isolated forming another province. Total = 2.
#
# Constraints:
# 1 <= V <= 200
# isConnected[i][j] is 0 or 1
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

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
    def numberOfProvinces_brute(self, isConnected: List[List[int]]) -> int:
        pass

    def numberOfProvinces_better(self, isConnected: List[List[int]]) -> int:
        pass

    def numberOfProvinces_optimal(self, isConnected: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.numberOfProvinces_optimal([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
