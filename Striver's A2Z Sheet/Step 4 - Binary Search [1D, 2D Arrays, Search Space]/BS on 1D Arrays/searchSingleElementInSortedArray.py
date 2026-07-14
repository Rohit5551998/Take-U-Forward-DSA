# mypy: disable-error-code="empty-body"
# QUESTION: Single Element in a Sorted Array
# In a sorted array where every element appears exactly twice except one, find the
# single element that appears only once.
# Example 1:
# Input: nums = [1,1,2,2,3,3,4,5,5,6,6]
# Output: 4
# Explanation: Every value is paired except 4.
# Constraints:
# 1 <= len(nums) <= 10^5
# Exactly one element appears once; all others appear exactly twice.

"""
#Brute Force:
1. XOR all elements; pairs cancel out leaving the single element.
   (Or scan and compare neighbours.)
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; index-parity binary search is the improvement.

#Optimal Approach:
1. Handle edges: length 1, or the single element being at index 0 or n-1.
2. Search [1, n-2]. Before the single element pairs are (even, odd) indices; after
   it the pairing flips to (odd, even).
3. If nums[mid] differs from both neighbours it IS the single element.
4. Else use parity: if (mid even and nums[mid] == nums[mid+1]) or
   (mid odd and nums[mid] == nums[mid-1]), the single element is to the RIGHT
   -> low = mid + 1; otherwise it is to the LEFT -> high = mid - 1.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- The single element flips the even/odd index pairing pattern, so parity at mid
  tells us which side of it we are standing on.
"""

from typing import List


class Solution:
    def single_element_brute(self, nums: List[int]) -> int:
        x = 0
        for v in nums:
            x ^= v
        return x

    def single_element_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier between XOR scan and binary search.
        pass

    def single_element_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low, high = 1, n - 2
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (
                mid % 2 == 0 and nums[mid] == nums[mid + 1]
            ):
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.single_element_optimal([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
