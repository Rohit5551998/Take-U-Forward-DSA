# mypy: disable-error-code="empty-body"
# QUESTION: Implement Upper Bound
# Given a sorted array nums and a target x, find the upper bound: the smallest
# index i such that nums[i] > x. If no such element exists, return n (len(nums)).
# Example 1:
# Input: nums = [1,2,3,4,5,6,7,9,10], x = 5
# Output: 5
# Explanation: The smallest index whose value is strictly > 5 is index 5 (value 6).
# Constraints:
# 1 <= len(nums) <= 10^5
# nums is sorted in ascending order.

"""
#Brute Force:
1. Linear scan left to right; return the first index with nums[i] > x.
2. If none found, return n.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the direct improvement.

#Optimal Approach:
1. ans = n (default when every element is <= x).
2. Binary search on [low, high] = [0, n-1].
3. If nums[mid] > x, mid is a valid candidate; record ans = mid and search left
   for a smaller valid index -> high = mid - 1.
4. Else nums[mid] <= x, so the answer is to the right -> low = mid + 1.
5. Return ans.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Upper bound is identical to lower bound but with a strict '>' predicate, so it
  lands one step past any run of values equal to x.
"""

from typing import List


class Solution:
    def upper_bound_brute(self, nums: List[int], x: int) -> int:
        for i in range(len(nums)):
            if nums[i] > x:
                return i
        return len(nums)

    def upper_bound_better(self, nums: List[int], x: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def upper_bound_optimal(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.upper_bound_optimal([1, 2, 3, 4, 5, 6, 7, 9, 10], 5))
