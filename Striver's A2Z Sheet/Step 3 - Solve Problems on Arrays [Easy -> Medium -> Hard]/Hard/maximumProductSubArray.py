# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray with the largest
# product and return that product.
# Example 1:
# Input: nums = [2, 3, -2, 4]
# Output: 6
# Explanation: The subarray [2, 3] has the largest product 6.
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10 (products fit in a 32-bit integer)

"""
#Brute Force:
1. Enumerate every subarray with two loops and multiply it out with a third loop.
2. Track the maximum product.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. Fix a start and extend the end with a running product, dropping the inner
   loop.
2. Track the maximum.
TC -> O(n^2), SC -> O(1)

#Optimal Approach (Prefix & Suffix Products):
1. Sweep a prefix product from the left and a suffix product from the right
   simultaneously, taking the max at every step.
2. When either running product hits 0 (a zero splits the array), reset it to 1
   so the next segment starts fresh.
3. This naturally handles negatives: the best product is always achieved at some
   prefix or suffix, since an even count of negatives multiplies positive and
   the extreme is captured from one of the two ends.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The maximum-product window always aligns with a prefix or suffix once zeros
  reset the running products, so sweeping both ends captures it in one pass.
"""

from typing import List


class Solution:
    def max_product_brute(self, nums: List[int]) -> int:
        max_product = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
                max_product = max(max_product, product)
        return int(max_product)

    def max_product_better(self, nums: List[int]) -> int:
        max_product = float("-inf")
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                max_product = max(max_product, product)
        return int(max_product)

    def max_product_optimal(self, nums: List[int]) -> int:
        max_product = float("-inf")
        prefix, suffix = 1, 1
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            max_product = max(prefix, suffix, max_product)
        return int(max_product)


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_product_optimal([2, 3, -2, 4]))
