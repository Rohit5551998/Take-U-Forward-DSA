# mypy: disable-error-code="empty-body"
# QUESTION: Sort an Array of 0s, 1s and 2s
# Given an array nums containing only 0s, 1s and 2s, sort it in-place in
# ascending order without using any sorting algorithm.
# Example 1:
# Input: nums = [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: All 0s come first, then 1s, then 2s.
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is 0, 1 or 2

"""
#Brute Force:
1. Simply sort the whole array with a comparison sort.
TC -> O(n log n), SC -> O(1)

#Better Approach:
1. Count the occurrences of 0, 1 and 2 in one pass.
2. Overwrite the array with that many 0s, then 1s, then 2s in a second pass.
TC -> O(2n), SC -> O(1)

#Optimal Approach (Dutch National Flag):
1. Keep three pointers: low, mid, high. The invariant is
   [0..low-1] = 0s, [low..mid-1] = 1s, [high+1..] = 2s, [mid..high] unknown.
2. If nums[mid] == 0 swap with low, advance both low and mid.
3. If nums[mid] == 1 just advance mid.
4. If nums[mid] == 2 swap with high and decrement high (do NOT advance mid, the
   swapped-in value still needs inspection).
5. Stop when mid crosses high.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Three pointers maintain three sorted regions simultaneously, so a single pass
  with in-place swaps fully partitions the array — no counting, no sort.
"""

from typing import List


class Solution:
    def sort012_brute(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    def sort012_better(self, nums: List[int]) -> List[int]:
        cnt = {0: 0, 1: 0, 2: 0}
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        for i in range(0, cnt[0]):
            nums[i] = 0
        for i in range(cnt[0], cnt[0] + cnt[1]):
            nums[i] = 1
        for i in range(cnt[0] + cnt[1], len(nums)):
            nums[i] = 2
        return nums

    def sort012_optimal(self, nums: List[int]) -> List[int]:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.sort012_optimal([2, 0, 2, 1, 1, 0]))
