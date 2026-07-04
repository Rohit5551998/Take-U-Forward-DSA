# mypy: disable-error-code="empty-body"
# QUESTION: Maximum XOR of two numbers in an array
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
# where 0 <= i <= j < n.
#
# Examples:
# Example 1:
# Input: nums = [3, 9, 10, 5, 1]
# Output: 15
# Explanation: The maximum XOR value is 10 XOR 5 => 15.
#
# Example 2:
# Input: nums = [26, 49, 30, 15, 69]
# Output: 116
# Explanation: The maximum XOR value is 69 XOR 49 => 116.
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - 0 <= nums[i] <= 2^31 - 1


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
    def maximum_xor_of_two_numbers_in_an_array_brute(self, nums: List[int]) -> int:
        pass

    def maximum_xor_of_two_numbers_in_an_array_better(self, nums: List[int]) -> int:
        pass

    def maximum_xor_of_two_numbers_in_an_array_optimal(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 9, 10, 5, 1]
    print(sol.maximum_xor_of_two_numbers_in_an_array_optimal(nums))
