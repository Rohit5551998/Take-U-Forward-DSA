# mypy: disable-error-code="empty-body"
# QUESTION: Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in
# the array. Note that it is the kth largest element in sorted order, not the kth
# distinct element.
#
# Example 1:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
# Explanation: Sorted descending -> [6, 5, 4, 3, 2, 1]; the 2nd largest is 5.
#
# Example 2:
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
#
# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


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
    def findKthLargest_brute(self, nums: List[int], k: int) -> int:
        pass

    def findKthLargest_better(self, nums: List[int], k: int) -> int:
        pass

    def findKthLargest_optimal(self, nums: List[int], k: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.findKthLargest_optimal([3, 2, 1, 5, 6, 4], 2))
