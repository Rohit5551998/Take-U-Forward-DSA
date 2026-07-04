# mypy: disable-error-code="empty-body"
# QUESTION: Subsets II
# Given an integer array nums which may contain duplicate entries, return the power set
# (all subsets). The solution set must not contain duplicate subsets. Return the subsets
# in any order.
#
# Examples:
# Input: array[] = [1,2,2]
# Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
# Explanation: We can have subsets ranging from length 0 to 3, which are listed above.
# Also the subset [1,2] appears twice but is printed only once as we require unique subsets.
#
# Input: array[] = [1]
# Output: [ [ ], [1] ]
# Explanation: Only two unique subsets are available.


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
    def subsets_ii_brute(self, nums: List[int]) -> List[List[int]]:
        pass

    def subsets_ii_better(self, nums: List[int]) -> List[List[int]]:
        pass

    def subsets_ii_optimal(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2]
    print(sol.subsets_ii_optimal(nums))
