# mypy: disable-error-code="empty-body"
# QUESTION: Binary Search to find X in Sorted Array
# Given a sorted array of integers nums and an integer target, return the index
# of target if it exists in nums, otherwise return -1.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7,8,9,10], target = 4
# Output: 3
# Explanation: nums[3] == 4, so index 3 is returned.
# Constraints:
# 1 <= len(nums) <= 10^5
# nums is sorted in ascending order.

"""
#Brute Force:
1. Linear scan: walk every index and compare nums[i] with target.
2. This ignores the sorted property entirely.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; the jump from linear scan to binary search
is the only meaningful improvement for this problem.

#Optimal Approach:
1. Keep a search window [low, high] = [0, n-1].
2. mid = low + (high - low) // 2 (overflow-safe midpoint).
3. If nums[mid] == target, we found it -> return mid.
4. If nums[mid] < target, the answer (if any) is strictly right -> low = mid + 1.
5. Else the answer is strictly left -> high = mid - 1.
6. If the window empties (low > high), target is absent -> return -1.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Because the array is sorted, one comparison at mid tells us which half can
  possibly contain the target, so we discard half the search space each step.
"""

from typing import List


class Solution:
    def binary_search_brute(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def binary_search_better(self, nums: List[int], target: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def binary_search_optimal(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.binary_search_optimal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
