# mypy: disable-error-code="empty-body"
# QUESTION: Subset Sums
# Given an array, print the sum of every subset generated from it, in increasing order.
#
# Examples:
# Input: N = 3, arr[] = {5,2,1}
# Output: 0,1,2,3,5,6,7,8
# Explanation: The generated subsets are [], [5], [2], [5,2], [1], [5,1], [2,1], [5,2,1],
# so the subset sums are 0, 5, 2, 7, 1, 6, 3, 8 which sorted give 0,1,2,3,5,6,7,8.
#
# Input: N=3,arr[]= {3,1,2}
# Output: 0,1,2,3,3,4,5,6
# Explanation: The generated subsets are [], [3], [1], [3,1], [2], [3,2], [1,2], [3,1,2],
# so the subset sums are 0, 3, 1, 4, 2, 5, 3, 6 which sorted give 0,1,2,3,3,4,5,6.


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
    def subset_sums_brute(self, nums: List[int]) -> List[int]:
        pass

    def subset_sums_better(self, nums: List[int]) -> List[int]:
        pass

    def subset_sums_optimal(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 1]
    print(sol.subset_sums_optimal(nums))
