# mypy: disable-error-code="empty-body"
# QUESTION: Longest Consecutive Sequence
# Given an unsorted array nums, return the length of the longest run of
# consecutive integers (they need not be adjacent in the array).
# Example 1:
# Input: nums = [100, 200, 1, 3, 2, 4]
# Output: 4
# Explanation: The consecutive run 1, 2, 3, 4 has length 4.
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

"""
#Brute Force:
1. For each element x, keep searching the array (linear search) for x+1, x+2, ...
   counting the run length; track the maximum.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Sort the array. Walk it once tracking the last value; when the current value
   is exactly last+1 extend the run, on a duplicate skip, otherwise restart the
   run at 1.
TC -> O(n log n), SC -> O(1)

#Optimal Approach:
1. Insert all elements into a hash set.
2. Only start counting a run from an element x that is a sequence start, i.e.
   x-1 is NOT in the set. This guarantees each run is walked once.
3. From such a start keep checking x+1, x+2, ... in the set and track the max
   length.
TC -> O(n) (each element visited at most twice), SC -> O(n)

#KEY INSIGHT:
- Only launching the count from sequence starts (x with no x-1 present) makes the
  total work linear despite the inner while-loop.
"""

from typing import List


class Solution:
    def linear_search(self, element: int, arr: List[int]) -> bool:
        return any(arr[i] == element for i in range(len(arr)))

    def longest_consecutive_brute(self, nums: List[int]) -> int:
        max_len = 1 if nums else 0
        for i in range(len(nums)):
            x = nums[i]
            cnt = 1
            while self.linear_search(x + 1, nums):
                x += 1
                cnt += 1
            max_len = max(max_len, cnt)
        return max_len

    def longest_consecutive_better(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = sorted(nums)
        max_len, cnt = 1, 0
        last_smaller = float("-inf")
        for i in range(len(arr)):
            if arr[i] == last_smaller + 1:
                last_smaller = arr[i]
                cnt += 1
                max_len = max(max_len, cnt)
            elif arr[i] != last_smaller:
                last_smaller = arr[i]
                cnt = 1
        return max_len

    def longest_consecutive_optimal(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        max_len = 1
        for key in hash_set:
            if key - 1 not in hash_set:
                curr, cnt = key, 1
                while curr + 1 in hash_set:
                    curr += 1
                    cnt += 1
                max_len = max(max_len, cnt)
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_consecutive_optimal([100, 200, 1, 3, 2, 4]))
