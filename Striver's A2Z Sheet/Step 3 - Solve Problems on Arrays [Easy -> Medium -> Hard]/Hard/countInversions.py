# mypy: disable-error-code="empty-body"
# QUESTION: Count Inversions
# Given an array nums, count the number of inversions: pairs (i, j) with i < j
# and nums[i] > nums[j]. This measures how far the array is from being sorted.
# Example 1:
# Input: nums = [5, 3, 2, 1, 4]
# Output: 7
# Explanation: Inversions are (5,3),(5,2),(5,1),(5,4),(3,2),(3,1),(2,1) = 7 pairs.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

"""
#Brute Force:
1. Check every pair (i, j) with i < j and count when nums[i] > nums[j].
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; the merge-sort counting below jumps straight
from O(n^2) to O(n log n).

#Optimal Approach (Modified Merge Sort):
1. Run merge sort. During each merge of a sorted left half and sorted right half,
   when the right element is smaller than the left element, every remaining
   element in the left half (mid - left + 1 of them) forms an inversion with it.
2. Accumulate these counts across all merges plus the recursive counts of the two
   halves.
TC -> O(n log n), SC -> O(n)

#KEY INSIGHT:
- While merging two sorted halves, a single "right < left" comparison reveals a
  whole block of inversions at once (all remaining left elements), so counting
  piggybacks on the sort for free.
"""

from typing import List


class Solution:
    def count_inversions_brute(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
        return cnt

    def count_inversions_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier; merge-sort counting is the optimal.
        pass

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> int:
        left, right = low, mid + 1
        cnt = 0
        temp: List[int] = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                cnt += mid - left + 1
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        return cnt

    def merge_sort(self, arr: List[int], low: int, high: int) -> int:
        cnt = 0
        if low < high:
            mid = (low + high) // 2
            cnt += self.merge_sort(arr, low, mid)
            cnt += self.merge_sort(arr, mid + 1, high)
            cnt += self.merge(arr, low, mid, high)
        return cnt

    def count_inversions_optimal(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_inversions_optimal([5, 3, 2, 1, 4]))
