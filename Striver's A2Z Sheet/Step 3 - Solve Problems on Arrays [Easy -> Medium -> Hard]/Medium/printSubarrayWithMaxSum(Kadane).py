# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Subarray Sum (Kadane's Algorithm) + Print the Subarray
# Given an integer array nums, find the contiguous subarray with the largest sum
# and return that sum. Also print the subarray itself.
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

"""
#Brute Force:
1. Enumerate every subarray with two loops and sum it with a third loop.
2. Track the maximum sum found.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. Fix a start index and extend the end index, maintaining a running sum so the
   third loop is unnecessary.
2. Track the maximum over all (start, end) pairs.
TC -> O(n^2), SC -> O(1)

#Optimal Approach (Kadane's Algorithm):
1. Keep a running sum. When it drops below 0, reset it to 0 because a negative
   prefix can only hurt any subarray that extends past it; record a new start.
2. Add the current element, then update the max sum and remember the current
   start/end whenever a new best is seen.
3. Slice nums[ansStart:ansEnd+1] to print the actual subarray.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A negative running prefix is never worth carrying forward; dropping it the
  moment the running sum goes negative is exactly what lets one pass find the
  best contiguous window.
"""

from typing import List


class Solution:
    def max_subarray_brute(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = 0
                for k in range(i, j + 1):
                    total += nums[k]
                max_sum = max(max_sum, total)
        return int(max_sum)

    def max_subarray_better(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                max_sum = max(max_sum, total)
        return int(max_sum)

    def max_subarray_optimal(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        total = 0
        start = 0
        ans_start, ans_end = -1, -1
        for i in range(len(nums)):
            if total < 0:
                total = 0
                start = i
            total += nums[i]
            if total > max_sum:
                max_sum = total
                ans_start = start
                ans_end = i
        print("Subarray with Max Sum:", nums[ans_start : ans_end + 1])
        return int(max_sum)


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_subarray_optimal([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
