# mypy: disable-error-code="empty-body"
# QUESTION: Split Array - Largest Sum
# Given an array nums and an integer m, split nums into m non-empty contiguous
# subarrays. Minimize the largest sum among these m subarrays and return it.
# Example 1:
# Input: nums = [25,46,28,49,24], m = 4
# Output: 71
# Explanation: The best split yields a largest subarray sum of 71.
# Constraints:
# 1 <= m <= len(nums) <= 10^5
# 1 <= nums[i] <= 10^6

"""
#Brute Force:
1. If m > n return -1. The answer lies in [max(nums), sum(nums)].
2. For each candidate max-sum, greedily count the subarrays required (start a new
   subarray when the running sum would exceed the candidate).
3. Return the first candidate needing <= m subarrays.
TC -> O((sum - max + 1) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the max-sum is the improvement.

#Optimal Approach:
1. Subarrays-needed is monotone non-increasing in the allowed max-sum, so
   "subarrays(x) <= m" is monotone. Binary search x in [max(nums), sum(nums)].
2. If subarrays(mid) <= m, mid is feasible; record it and try smaller (high=mid-1).
3. Else mid too small -> low = mid + 1.
TC -> O(N * log(sum - max)), SC -> O(1)

#KEY INSIGHT:
- This is identical to Book Allocation / Painter's Partition: minimize the maximum
  block sum where more allowed sum means fewer blocks (a monotone predicate).
"""

from typing import List


class Solution:
    def _subarrays(self, nums: List[int], max_sum: int) -> int:
        count = 1
        running = 0
        for x in nums:
            if running + x <= max_sum:
                running += x
            else:
                count += 1
                running = x
        return count

    def split_array_brute(self, nums: List[int], m: int) -> int:
        if m > len(nums):
            return -1
        for x in range(max(nums), sum(nums) + 1):
            if self._subarrays(nums, x) <= m:
                return x
        return -1

    def split_array_better(self, nums: List[int], m: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def split_array_optimal(self, nums: List[int], m: int) -> int:
        if m > len(nums):
            return -1
        low, high = max(nums), sum(nums)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if self._subarrays(nums, mid) <= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.split_array_optimal([25, 46, 28, 49, 24], 4))
