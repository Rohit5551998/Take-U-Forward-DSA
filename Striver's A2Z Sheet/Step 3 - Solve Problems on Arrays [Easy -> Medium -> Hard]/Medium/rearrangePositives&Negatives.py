# mypy: disable-error-code="empty-body"
# QUESTION: Rearrange Array Elements by Sign
# Given an array nums with an equal number of positive and negative integers,
# rearrange it so signs alternate starting with a positive, preserving the
# relative order within positives and within negatives. (Variant 2 handles the
# case where the counts are unequal by appending the leftovers.)
# Example 1:
# Input: nums = [3, 1, -2, -5, 2, -4]
# Output: [3, -2, 1, -5, 2, -4]
# Explanation: Positives at even indices, negatives at odd indices, order kept.
# Constraints:
# 2 <= nums.length <= 2 * 10^5
# nums contains equal positives and negatives (variant 1)

"""
#Brute Force:
1. Split into two lists: positives and negatives (order preserved).
2. Write positives back at even indices and negatives at odd indices.
3. This uses extra split lists and a second placement pass.
TC -> O(2n), SC -> O(n)

#Better Approach:
SKIPPED — no distinct middle tier for the equal-count case; the single-pass
placement below is the direct improvement.

#Optimal Approach:
1. For the equal-count variant, walk the array once with two write positions:
   pos = 0 (even) for positives, neg = 1 (odd) for negatives.
2. Copy each element into its sign's slot in a result array and advance that
   slot by 2.
(For the unequal variant, place min(len(pos), len(neg)) alternating pairs then
append the remaining longer list at the end.)
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- Two independent write cursors (even for +, odd for -) let a single pass drop
  each element straight into its final alternating slot.
"""

from typing import List


class Solution:
    def rearrange_brute(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums) // 2):
            nums[2 * i] = positive[i]
            nums[2 * i + 1] = negative[i]
        return nums

    def rearrange_better(self, nums: List[int]) -> List[int]:
        # SKIP: no distinct better approach; single-pass placement is the optimal.
        pass

    def rearrange_optimal(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrange_optimal([3, 1, -2, -5, 2, -4]))
