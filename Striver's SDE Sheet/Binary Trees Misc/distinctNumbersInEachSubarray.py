# mypy: disable-error-code="empty-body"
# QUESTION: Distinct Numbers in Each Subarray
# Given an integer array nums of size n and an integer k, construct an array ans of size n-k+1
# where ans[i] represents the number of distinct numbers in the subarray
# nums[i..i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]]. Return the array ans.
#
# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 3, 4, 2, 3], k = 4
# Output: [3, 4, 4, 3]
# Explanation: Window [1, 2, 1, 3] has 3 distinct numbers (1, 2, 3); [2, 1, 3, 4] has 4;
# [1, 3, 4, 2] has 4; [3, 4, 2, 3] has 3 distinct numbers (2, 3, 4).
#
# Example 2:
# Input: nums = [1, 1, 1, 1, 2, 3, 4], k = 3
# Output: [1, 1, 2, 3, 3]
# Explanation: Windows [1, 1, 1] and [1, 1, 1] each have 1 distinct number; [1, 1, 2] has 2;
# [1, 2, 3] has 3; [2, 3, 4] has 3.
#
# Constraints:
# 1 <= k <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5


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
    def distinct_numbers_in_each_subarray_brute(self, nums: List[int], k: int) -> List[int]:
        pass

    def distinct_numbers_in_each_subarray_better(self, nums: List[int], k: int) -> List[int]:
        pass

    def distinct_numbers_in_each_subarray_optimal(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    print(sol.distinct_numbers_in_each_subarray_optimal(nums, k))
