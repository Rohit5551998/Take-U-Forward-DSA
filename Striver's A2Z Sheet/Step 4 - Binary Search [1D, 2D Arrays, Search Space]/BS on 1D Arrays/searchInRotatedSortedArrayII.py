# mypy: disable-error-code="empty-body"
# QUESTION: Search in Rotated Sorted Array II (with duplicates)
# A sorted array that MAY contain duplicates is rotated at an unknown pivot. Given
# the rotated array nums and a target, return True if target is present, else False.
# Example 1:
# Input: nums = [1,0,1,1,1], target = 0
# Output: True
# Explanation: 0 is present at index 1.
# Constraints:
# 1 <= len(nums) <= 10^4
# nums may contain duplicate values.

"""
#Brute Force:
1. Linear scan; return True as soon as nums[i] == target.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; modified binary search is the improvement.

#Optimal Approach:
1. Same as the distinct version, with one extra case for duplicates.
2. If nums[mid] == target return True.
3. If nums[low] == nums[mid] == nums[high], we cannot tell which side is sorted;
   shrink both ends (low += 1, high -= 1) and continue. This is the only step that
   costs the worst case.
4. Otherwise identify the sorted half exactly as in the distinct version and keep
   the half that can contain target.
TC -> O(logN) average, O(N) worst (all equal), SC -> O(1)

#KEY INSIGHT:
- Duplicates at both ends destroy the "one half is sorted" guarantee; the only
  safe move is to peel one element off each side, which degrades the worst case
  to linear but keeps correctness.
"""

from typing import List


class Solution:
    def search_rotated_ii_brute(self, nums: List[int], target: int) -> bool:
        return target in nums

    def search_rotated_ii_better(self, nums: List[int], target: int) -> bool:
        # SKIP: no distinct better tier between linear scan and modified BS.
        pass

    def search_rotated_ii_optimal(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
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
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.search_rotated_ii_optimal([1, 0, 1, 1, 1], 0))
