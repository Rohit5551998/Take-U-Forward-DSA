# mypy: disable-error-code="empty-body"
# QUESTION: Next Permutation
# Given an array nums, rearrange it in-place into the lexicographically next
# greater permutation. If no greater permutation exists (array is in descending
# order), rearrange it to the smallest (ascending) permutation.
# Example 1:
# Input: nums = [2, 1, 5, 4, 3, 0, 0]
# Output: [2, 3, 0, 0, 1, 4, 5]
# Explanation: The next permutation after 2154300 is 2300145.
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

"""
#Brute Force:
1. Generate all permutations in sorted order, locate the current one, and return
   the following permutation (wrapping to the first if current is the last).
TC -> O(n! * n), SC -> O(n! * n)

#Better Approach:
SKIPPED — the library helper (C++ next_permutation) is not a distinct algorithm
in Python; the in-place three-step method below is the intended solution.

#Optimal Approach:
1. Scan from the right and find the first index i where nums[i] < nums[i+1] (the
   "break point"). If none exists the array is descending — reverse it and stop.
2. From the right, find the first element greater than nums[break] and swap them.
   This is the smallest possible increase at the break point.
3. Reverse the suffix after the break point so it becomes the smallest ordering,
   giving the very next permutation.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The longest descending suffix is already maximal; the next permutation is made
  by bumping the element just before it to the next larger suffix value, then
  minimizing that suffix by reversing it.
"""

from typing import List


class Solution:
    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def next_permutation_brute(self, nums: List[int]) -> List[int]:
        # SKIP: generating all permutations is O(n! * n); use the optimal instead.
        pass

    def next_permutation_better(self, nums: List[int]) -> List[int]:
        # SKIP: no distinct better tier; library next_permutation is not Pythonic here.
        pass

    def next_permutation_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        break_point = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                break_point = i - 1
                break
        if break_point == -1:
            self.reverse(nums, 0, n - 1)
        else:
            for i in range(n - 1, break_point, -1):
                if nums[i] > nums[break_point]:
                    nums[i], nums[break_point] = nums[break_point], nums[i]
                    break
            self.reverse(nums, break_point + 1, n - 1)
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.next_permutation_optimal([2, 1, 5, 4, 3, 0, 0]))
