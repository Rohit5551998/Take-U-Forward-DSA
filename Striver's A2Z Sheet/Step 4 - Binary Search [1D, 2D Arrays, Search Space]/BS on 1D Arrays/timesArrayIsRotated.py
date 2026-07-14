# mypy: disable-error-code="empty-body"
# QUESTION: Find out how many times the array has been rotated
# A sorted array of distinct integers is rotated k times. Given the rotated array,
# return k — which equals the index of the minimum element.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2,3]
# Output: 4
# Explanation: The minimum (0) sits at index 4, so the array was rotated 4 times.
# Constraints:
# 1 <= len(nums) <= 10^4
# All values of nums are distinct.

"""
#Brute Force:
1. Linear scan for the index of the smallest value; that index is the rotation count.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the improvement.

#Optimal Approach:
1. Same as "minimum in rotated sorted array" but track the INDEX of the minimum,
   not just the value.
2. If nums[low..high] is sorted, nums[low] is the smallest here; record its index
   if it beats the running minimum, then stop.
3. Otherwise move toward the unsorted (pivot-containing) half, recording the sorted
   half's starting index/value as a candidate.
4. Return the recorded index.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Number of rotations == index of the minimum element, so this reduces to finding
  that index via the same pivot-seeking binary search.
"""

import math
from typing import List


class Solution:
    def rotation_count_brute(self, nums: List[int]) -> int:
        return nums.index(min(nums))

    def rotation_count_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def rotation_count_optimal(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mini = math.inf
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] <= nums[high]:
                if nums[low] < mini:
                    mini = nums[low]
                    index = low
                break
            if nums[low] <= nums[mid]:
                if nums[low] < mini:
                    mini = nums[low]
                    index = low
                low = mid + 1
            else:
                if nums[mid] < mini:
                    mini = nums[mid]
                    index = mid
                high = mid - 1
        return index


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotation_count_optimal([4, 5, 6, 7, 0, 1, 2, 3]))
