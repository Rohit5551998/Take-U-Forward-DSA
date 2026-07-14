# mypy: disable-error-code="empty-body"
# QUESTION: Find Minimum in Rotated Sorted Array
# A sorted array of distinct integers is rotated at an unknown pivot. Find the
# minimum element.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2,3]
# Output: 0
# Explanation: The array was rotated; the smallest value is 0.
# Constraints:
# 1 <= len(nums) <= 10^4
# All values of nums are distinct.

"""
#Brute Force:
1. Linear scan tracking the smallest value.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the improvement.

#Optimal Approach:
1. Binary search maintaining a running mini.
2. If the current window nums[low..high] is already sorted (nums[low] <= nums[high]),
   its minimum is nums[low]; take min and stop — no rotation remains here.
3. Else find the sorted half: if nums[low] <= nums[mid] the left half is sorted, so
   its minimum is nums[low]; record it and discard left (low = mid + 1).
4. Otherwise the right half holds the pivot; nums[mid] is a candidate minimum,
   record it and discard right (high = mid - 1).
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- The minimum sits at the rotation pivot; always move toward the UNSORTED half
  because that half contains the pivot, while collecting the sorted half's start
  as a candidate.
"""

import math
from typing import List


class Solution:
    def find_min_brute(self, nums: List[int]) -> int:
        return min(nums)

    def find_min_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def find_min_optimal(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mini = math.inf
        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] <= nums[high]:
                mini = min(mini, nums[low])
                break
            if nums[low] <= nums[mid]:
                mini = min(mini, nums[low])
                low = mid + 1
            else:
                mini = min(mini, nums[mid])
                high = mid - 1
        return int(mini)


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_min_optimal([4, 5, 6, 7, 0, 1, 2, 3]))
