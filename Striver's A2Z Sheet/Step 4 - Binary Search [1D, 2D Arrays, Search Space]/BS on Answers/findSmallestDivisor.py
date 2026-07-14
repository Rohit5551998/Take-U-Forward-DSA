# mypy: disable-error-code="empty-body"
# QUESTION: Find the Smallest Divisor Given a Threshold
# Given an array nums and an integer threshold, find the smallest positive divisor
# d such that sum of ceil(nums[i] / d) over all i is <= threshold.
# Example 1:
# Input: nums = [1,2,3,4,5], threshold = 8
# Output: 3
# Explanation: With d=3 the sum is 1+1+1+2+2 = 7 <= 8, and no smaller d works.
# Constraints:
# 1 <= len(nums) <= 5*10^4
# len(nums) <= threshold <= 10^6

"""
#Brute Force:
1. Try each divisor d from 1 to max(nums); compute sum of ceil(nums[i]/d).
2. Return the first d whose sum <= threshold.
TC -> O(max(nums) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the divisor is the improvement.

#Optimal Approach:
1. The sum of ceilings is monotone NON-increasing as d grows, so the predicate
   "sum(d) <= threshold" is monotone.
2. Binary search d in [1, max(nums)].
3. If sum(mid) <= threshold, mid works; record it and try smaller (high = mid - 1).
4. Else mid too small -> low = mid + 1.
TC -> O(N * log(max(nums))), SC -> O(1)

#KEY INSIGHT:
- A larger divisor never increases the ceiling sum, giving a monotone predicate we
  can binary search for its smallest true point.
"""

import math
from typing import List


class Solution:
    def _sum_div(self, nums: List[int], d: int) -> int:
        return sum(math.ceil(x / d) for x in nums)

    def smallest_divisor_brute(self, nums: List[int], threshold: int) -> int:
        for d in range(1, max(nums) + 1):
            if self._sum_div(nums, d) <= threshold:
                return d
        return -1

    def smallest_divisor_better(self, nums: List[int], threshold: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def smallest_divisor_optimal(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self._sum_div(nums, mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallest_divisor_optimal([1, 2, 3, 4, 5], 8))
