# mypy: disable-error-code="empty-body"
# QUESTION: Search Insert Position
# Given a sorted array of distinct integers nums and a target x, return the index
# where x is found. If not found, return the index where it would be inserted to
# keep the array sorted.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7,9,10], x = 8
# Output: 7
# Explanation: 8 is not present; inserting it at index 7 keeps nums sorted.
# Constraints:
# 1 <= len(nums) <= 10^4
# nums is sorted in ascending order with distinct values.

"""
#Brute Force:
1. Linear scan; return the first index with nums[i] >= x, else n.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the direct improvement.

#Optimal Approach:
1. The insert position is exactly the lower bound of x (smallest index with
   nums[i] >= x): if x is present it returns its index, otherwise the slot it
   should occupy.
2. ans = n. Binary search: if nums[mid] >= x record ans = mid and go left,
   else go right.
3. Return ans.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- Search-insert-position IS the lower bound; reusing that primitive handles both
  the "found" and "would-insert" cases with one search.
"""

from typing import List


class Solution:
    def search_insert_brute(self, nums: List[int], x: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= x:
                return i
        return len(nums)

    def search_insert_better(self, nums: List[int], x: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def search_insert_optimal(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.search_insert_optimal([1, 2, 3, 4, 5, 6, 7, 9, 10], 8))
