# mypy: disable-error-code="empty-body"
# QUESTION: Length of the Longest Subarray with Sum Zero
# Given an array nums (which may contain negatives), return the length of the
# longest contiguous subarray whose elements sum to 0.
# Example 1:
# Input: nums = [9, -3, 3, -1, 6, -5]
# Output: 5
# Explanation: [-3, 3, -1, 6, -5] sums to 0 and has length 5.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^3 <= nums[i] <= 10^3

"""
#Brute Force:
1. For each start i, extend a running sum over j and record the length whenever
   the running sum hits 0.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — the prefix-sum hashmap below is the direct next step and is optimal;
there is no meaningful intermediate tier.

#Optimal Approach (Prefix Sum + Hashmap):
1. Track the running prefix sum. If it is 0 at index i the subarray [0..i] sums
   to 0, giving length i+1.
2. Otherwise, if the same prefix sum was seen earlier at index p, then the
   subarray (p, i] sums to 0; update the max length with i - p.
3. Store each prefix sum's FIRST index only (do not overwrite) so the recovered
   subarray is as long as possible.
TC -> O(n) average, SC -> O(n)

#KEY INSIGHT:
- Two positions sharing the same prefix sum bracket a zero-sum subarray; keeping
  the earliest index for each prefix maximizes that span.
"""

from typing import List


class Solution:
    def longest_zero_sum_brute(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            total = nums[i]
            if total == 0:
                max_len = max(max_len, 1)
            for j in range(i + 1, len(nums)):
                total += nums[j]
                if total == 0:
                    max_len = max(max_len, j - i + 1)
        return max_len

    def longest_zero_sum_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier; prefix-sum hashmap is the optimal.
        pass

    def longest_zero_sum_optimal(self, nums: List[int]) -> int:
        max_len, total = 0, 0
        first_index: dict[int, int] = {}
        for i in range(len(nums)):
            total += nums[i]
            if total == 0:
                max_len = max(max_len, i + 1)
            else:
                if total in first_index:
                    max_len = max(max_len, i - first_index[total])
                else:
                    first_index[total] = i
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_zero_sum_optimal([9, -3, 3, -1, 6, -5]))
