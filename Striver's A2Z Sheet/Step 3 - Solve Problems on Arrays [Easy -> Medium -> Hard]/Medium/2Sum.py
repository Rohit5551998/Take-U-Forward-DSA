# mypy: disable-error-code="empty-body"
# QUESTION: Two Sum
# Given an array of integers nums and an integer target, return the indices of the
# two numbers such that they add up to target (variant 1), or return "YES"/"NO"
# whether such a pair exists (variant 2). You may not use the same element twice.
# Example 1:
# Input: nums = [2, 6, 5, 8, 11], target = 14
# Output: [1, 3]
# Explanation: nums[1] + nums[3] = 6 + 8 = 14.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i], target <= 10^9

"""
#Brute Force:
1. Fix each element i and scan every later element j.
2. If nums[i] + nums[j] == target return the index pair.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Walk the array once keeping a hashmap of value -> index seen so far.
2. For each element check whether the complement (target - nums[i]) is already
   in the map; if so we found the pair in a single pass.
3. Otherwise store the current value with its index and continue.
TC -> O(n) average, SC -> O(n)

#Optimal Approach:
1. When only YES/NO (or the values, not original indices) is needed, sort the
   array and use two pointers from both ends.
2. If the sum is too small move the left pointer right; if too big move the right
   pointer left; equality means a pair exists.
3. This trades the O(n) hash space for O(1) extra space at the cost of the sort.
TC -> O(n log n), SC -> O(1)

#KEY INSIGHT:
- The complement (target - x) turns a pairwise search into a single-pass lookup;
  sorting + two pointers is the space-optimal variant when original indices are
  not required.
"""

from typing import List


class Solution:
    def two_sum_brute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    def two_sum_better(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return [-1, -1]

    def two_sum_optimal(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        left, right = 0, len(arr) - 1
        pair: List[int] = []
        while left < right:
            total = arr[left] + arr[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                pair = [arr[left], arr[right]]
                break
        if len(pair) != 2:
            return [-1, -1]
        ans: List[int] = []
        for i in range(len(nums)):
            if nums[i] == pair[0] or nums[i] == pair[1]:
                ans.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum_optimal([2, 6, 5, 8, 11], 14))
