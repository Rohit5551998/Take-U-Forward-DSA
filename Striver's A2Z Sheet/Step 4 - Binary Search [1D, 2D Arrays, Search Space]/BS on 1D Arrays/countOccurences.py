# mypy: disable-error-code="empty-body"
# QUESTION: Count Occurrences in Sorted Array
# Given a sorted array nums and a target, count how many times target appears.
# Example 1:
# Input: nums = [3,4,13,13,13,20,40], target = 13
# Output: 3
# Explanation: 13 appears at indices 2, 3, 4 -> 3 times.
# Constraints:
# 1 <= len(nums) <= 10^5
# nums is sorted in ascending order.

"""
#Brute Force:
1. Linear scan, incrementing a counter each time nums[i] == target.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; boundary binary searches are the improvement.

#Optimal Approach:
1. Find first occurrence with a leftmost-biased binary search.
2. If first == -1, target is absent -> count is 0.
3. Find last occurrence with a rightmost-biased binary search.
4. Count = last - first + 1.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- The occurrences of a value in a sorted array form a contiguous block, so the
  count is fully determined by its two endpoints.
"""

from typing import List


class Solution:
    def count_occurrences_brute(self, nums: List[int], target: int) -> int:
        return sum(1 for v in nums if v == target)

    def count_occurrences_better(self, nums: List[int], target: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def _first(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def _last(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def count_occurrences_optimal(self, nums: List[int], target: int) -> int:
        first = self._first(nums, target)
        if first == -1:
            return 0
        return self._last(nums, target) - first + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_occurrences_optimal([3, 4, 13, 13, 13, 20, 40], 13))
