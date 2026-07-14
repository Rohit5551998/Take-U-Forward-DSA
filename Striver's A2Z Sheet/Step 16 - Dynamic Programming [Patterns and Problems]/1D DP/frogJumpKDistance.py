# mypy: disable-error-code="empty-body"
# QUESTION: Frog Jump with K Distances
# A frog climbs from stair 0 to stair n-1. From stair i it may jump to any of
# i+1..i+k; cost of i->j is abs(heights[i]-heights[j]). Find the minimum total
# energy to reach the last stair.
#
# Example 1:
# Input: heights = [10,5,20,0,15], k = 2
# Output: 15
# Explanation: 0->2->4 costs 10+5 = 15.
#
# Constraints:
# 1 <= k <= n <= 10^5
# 0 <= heights[i] <= 10^4

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
    def frog_jump_k_brute(self, heights: List[int], k: int) -> int:
        pass

    def frog_jump_k_better(self, heights: List[int], k: int) -> int:
        pass

    def frog_jump_k_optimal(self, heights: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.frog_jump_k_optimal([10, 5, 20, 0, 15], 2)
