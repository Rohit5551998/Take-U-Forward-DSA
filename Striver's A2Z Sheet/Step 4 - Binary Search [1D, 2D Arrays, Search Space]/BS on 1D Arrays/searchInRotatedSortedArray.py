# mypy: disable-error-code="empty-body"
# QUESTION: Search in Rotated Sorted Array
# A sorted array of distinct integers is rotated at some unknown pivot. Given the
# rotated array nums and a target, return its index, or -1 if not present.
# Example 1:
# Input: nums = [4,5,1,2,3], target = 2
# Output: 3
# Explanation: 2 is located at index 3.
# Constraints:
# 1 <= len(nums) <= 10^4
# All values of nums are distinct.

"""
#Brute Force:
1. Linear scan every index comparing with target.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; modified binary search is the improvement.

#Optimal Approach:
1. Binary search on [low, high]. Compute mid; if nums[mid] == target return mid.
2. At any mid, at least one half is sorted. If nums[low] <= nums[mid], the LEFT
   half is sorted:
   - if nums[low] <= target < nums[mid], target is in the left -> high = mid - 1,
   - else discard left -> low = mid + 1.
3. Otherwise the RIGHT half is sorted:
   - if nums[mid] < target <= nums[high], target is in the right -> low = mid + 1,
   - else discard right -> high = mid - 1.
4. Return -1 if the window empties.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Rotation breaks global sortedness, but one side of mid is always sorted; check
  the target against that sorted side to decide which half to keep.
"""

from typing import List


class Solution:
    def search_rotated_brute(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def search_rotated_better(self, nums: List[int], target: int) -> int:
        # SKIP: no distinct better tier between linear scan and modified BS.
        pass

    def search_rotated_optimal(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search_rotated_optimal([4, 5, 1, 2, 3], 2))
