# mypy: disable-error-code="empty-body"
# QUESTION: Frog Jump
# A frog climbs from stair 0 to stair n-1. heights[i] is the height of stair i.
# From stair i it can jump to i+1 or i+2; cost = abs(heights[i]-heights[j]).
# Find the minimum total energy to reach the last stair.
#
# Example 1:
# Input: heights = [10,20,30,10]
# Output: 20
# Explanation: 0->1->3 costs 10+10 = 20.
#
# Constraints:
# 1 <= n <= 10^5
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
    def frog_jump_brute(self, heights: List[int]) -> int:
        pass

    def frog_jump_better(self, heights: List[int]) -> int:
        pass

    def frog_jump_optimal(self, heights: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.frog_jump_optimal([10, 20, 30, 10])
