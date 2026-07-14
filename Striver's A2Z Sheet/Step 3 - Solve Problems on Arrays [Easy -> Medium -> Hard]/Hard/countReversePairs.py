# mypy: disable-error-code="empty-body"
# QUESTION: Count Reverse Pairs
# Given an array nums, count the number of reverse pairs: pairs (i, j) with i < j
# and nums[i] > 2 * nums[j].
# Example 1:
# Input: nums = [1, 3, 10, 2, 3, 1]
# Output: 4
# Explanation: The reverse pairs are (10,2), (10,3), (10,1) and (3,1) with the
# first 3 given 10 > 2*x.
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1

"""
#Brute Force:
1. Check every pair (i, j) with i < j and count when nums[i] > 2 * nums[j].
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; merge sort jumps straight from O(n^2) to
O(n log n).

#Optimal Approach (Modified Merge Sort):
1. Run merge sort. Before merging each pair of sorted halves, count reverse pairs
   with a separate two-pointer sweep: for each i in the left half advance a right
   pointer while arr[i] > 2 * arr[right], adding (right - (mid+1)) to the count.
2. The counting must precede the actual merge (both halves are individually
   sorted at that point), then perform the standard merge.
3. Sum the counts from both recursive halves and this level.
TC -> O(n log n), SC -> O(n)

#KEY INSIGHT:
- Counting must be a SEPARATE pass before merging (unlike inversions) because the
  2*nums[j] condition isn't the same comparison used to order the merge; both
  halves being sorted keeps that pre-merge sweep linear.
"""

from typing import List


class Solution:
    def count_reverse_pairs_brute(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    cnt += 1
        return cnt

    def count_reverse_pairs_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier; merge-sort counting is the optimal.
        pass

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> None:
        left, right = low, mid + 1
        temp: List[int] = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
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

    def count_pairs(self, arr: List[int], low: int, mid: int, high: int) -> int:
        cnt = 0
        right = mid + 1
        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += right - (mid + 1)
        return cnt

    def merge_sort(self, arr: List[int], low: int, high: int) -> int:
        cnt = 0
        if low < high:
            mid = (low + high) // 2
            cnt += self.merge_sort(arr, low, mid)
            cnt += self.merge_sort(arr, mid + 1, high)
            cnt += self.count_pairs(arr, low, mid, high)
            self.merge(arr, low, mid, high)
        return cnt

    def count_reverse_pairs_optimal(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_reverse_pairs_optimal([1, 3, 10, 2, 3, 1]))
