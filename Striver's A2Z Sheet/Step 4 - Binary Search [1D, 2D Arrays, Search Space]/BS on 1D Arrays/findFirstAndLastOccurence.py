# mypy: disable-error-code="empty-body"
# QUESTION: Find First and Last Position of Element in Sorted Array
# Given a sorted array nums and a target, return [first, last] — the first and
# last indices where target appears. Return [-1, -1] if target is not present.
# Example 1:
# Input: nums = [3,4,13,13,13,20,40], target = 13
# Output: [2, 4]
# Explanation: 13 first appears at index 2 and last at index 4.
# Constraints:
# 1 <= len(nums) <= 10^5
# nums is sorted in ascending order.

"""
#Brute Force:
1. Linear scan; record the first index where nums[i] == target and keep updating
   the last index while values equal target.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; two boundary binary searches are the improvement.

#Optimal Approach:
1. First occurrence: binary search; on nums[mid] == target record it and keep
   going LEFT (high = mid - 1) to find any earlier match; on nums[mid] > target go
   left, else go right.
2. Last occurrence: binary search; on nums[mid] == target record it and keep going
   RIGHT (low = mid + 1); on nums[mid] < target go right, else go left.
3. If first == -1, target is absent -> return [-1, -1].
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Duplicates are handled by not stopping on a match: bias the search toward the
  boundary (leftmost / rightmost) instead of returning immediately.
"""

from typing import List


class Solution:
    def occurrence_brute(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]

    def occurrence_better(self, nums: List[int], target: int) -> List[int]:
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

    def occurrence_optimal(self, nums: List[int], target: int) -> List[int]:
        first = self._first(nums, target)
        if first == -1:
            return [-1, -1]
        return [first, self._last(nums, target)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.occurrence_optimal([3, 4, 13, 13, 13, 20, 40], 13))
