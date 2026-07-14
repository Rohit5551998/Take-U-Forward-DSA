# mypy: disable-error-code="empty-body"
# QUESTION: Floor and Ceil in Sorted Array
# Given a sorted array nums and a target x, find its floor and ceil.
# Floor  = largest element in nums that is <= x (-1 if none).
# Ceil   = smallest element in nums that is >= x (-1 if none).
# Example 1:
# Input: nums = [3,4,4,7,8,10], x = 5
# Output: floor = 4, ceil = 7
# Explanation: 4 is the largest value <= 5; 7 is the smallest value >= 5.
# Constraints:
# 1 <= len(nums) <= 10^5
# nums is sorted in ascending order.

"""
#Brute Force:
1. Linear scan; track the largest value <= x (floor) and smallest value >= x (ceil).
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the direct improvement.

#Optimal Approach:
1. Floor: binary search; when nums[mid] <= x it is a candidate, record it and move
   right (low = mid + 1) to find a larger valid value; else move left.
2. Ceil: binary search; when nums[mid] >= x it is a candidate, record it and move
   left (high = mid - 1) to find a smaller valid value; else move right.
3. Ceil is exactly the lower-bound value; floor is the value just before it.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Floor and ceil are two mirror-image boundary searches: floor pushes right while
  the predicate (nums[mid] <= x) holds, ceil pushes left while (nums[mid] >= x).
"""

from typing import List, Tuple


class Solution:
    def ceil_floor_brute(self, nums: List[int], x: int) -> Tuple[int, int]:
        floor, ceil = -1, -1
        for v in nums:
            if v <= x:
                floor = v
            if v >= x and ceil == -1:
                ceil = v
        return floor, ceil

    def ceil_floor_better(self, nums: List[int], x: int) -> Tuple[int, int]:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def _floor(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= x:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def _ceil(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= x:
                ans = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def ceil_floor_optimal(self, nums: List[int], x: int) -> Tuple[int, int]:
        return self._floor(nums, x), self._ceil(nums, x)


if __name__ == "__main__":
    sol = Solution()
    print(sol.ceil_floor_optimal([3, 4, 4, 7, 8, 10], 5))
