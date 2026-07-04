# mypy: disable-error-code="empty-body"
# QUESTION: Aggressive Cows
# You are given an array 'arr' of size 'n' which denotes the position of
# stalls. You are also given an integer 'k' which denotes the number of
# aggressive cows. You are given the task of assigning stalls to 'k' cows
# such that the minimum distance between any two of them is the maximum
# possible. Find the maximum possible minimum distance.
#
# Examples:
# Example 1:
# Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
# Result: 3
# Explanation: The maximum possible minimum distance between any two cows will be 3 when
# 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4,
# and 3 respectively. We cannot make the minimum distance greater than 3 in any way.
#
# Example 2:
# Input Format: N = 5, k = 2, arr[] = {4,2,1,3,6}
# Result: 5
# Explanation: The maximum possible minimum distance between any two cows will be 5 when
# 2 cows are placed at positions {1, 6}.


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
    def aggressive_cows_brute(self, stalls: List[int], k: int) -> int:
        pass

    def aggressive_cows_better(self, stalls: List[int], k: int) -> int:
        pass

    def aggressive_cows_optimal(self, stalls: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    print(sol.aggressive_cows_optimal(stalls, k))
