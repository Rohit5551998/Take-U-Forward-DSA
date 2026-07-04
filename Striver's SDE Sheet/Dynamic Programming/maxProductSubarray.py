# mypy: disable-error-code="empty-body"
# QUESTION: Max Product Subarray
# Given an integer array nums (containing positive, negative, and zero
# values), find a contiguous non-empty subarray whose product is the
# largest, and return that product. The test cases are generated so that
# the answer fits in a 32-bit integer.
#
# Examples:
# Example 1:
# Input: nums = [2, 3, -2, 4]
# Output: 6
# Explanation: [2, 3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2, 0, -1]
# Output: 0
# Explanation: The result cannot be 2 because [-2, -1] is not contiguous.
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums fits in a 32-bit integer.


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
    def max_product_subarray_brute(self, nums: List[int]) -> int:
        pass

    def max_product_subarray_better(self, nums: List[int]) -> int:
        pass

    def max_product_subarray_optimal(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, -2, 4]
    print(sol.max_product_subarray_optimal(nums))
