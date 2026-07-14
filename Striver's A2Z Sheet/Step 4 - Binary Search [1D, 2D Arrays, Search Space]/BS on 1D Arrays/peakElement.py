# mypy: disable-error-code="empty-body"
# QUESTION: Find Peak Element
# A peak element is one strictly greater than its neighbours. Given nums where
# nums[-1] and nums[n] are treated as -infinity, return the index of any peak.
# Example 1:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: nums[5] = 6 is greater than both neighbours (5 and 4). Index 1 is
# also a valid peak; any one is accepted.
# Constraints:
# 1 <= len(nums) <= 10^5
# nums[i] != nums[i+1] for all valid i.

"""
#Brute Force:
1. Scan every index; return the first i strictly greater than both neighbours
   (with virtual -infinity outside the array).
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the slope is the improvement.

#Optimal Approach:
1. Handle edges: single element, or index 0 / n-1 being a peak vs its one neighbour.
2. Search [1, n-2]. Compute mid:
   - if nums[mid] > both neighbours, return mid.
   - if nums[mid] > nums[mid-1] we are on an increasing slope; a peak lies to the
     RIGHT -> low = mid + 1.
   - else (decreasing slope) a peak lies to the LEFT -> high = mid - 1.
3. The tie/valley branch also moves right to keep making progress.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- On an increasing slope a peak must exist to the right (values keep rising until
  something turns down); this lets us binary search even without global sortedness.
"""

from typing import List


class Solution:
    def peak_element_brute(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            left = nums[i - 1] if i > 0 else float("-inf")
            right = nums[i + 1] if i < n - 1 else float("-inf")
            if nums[i] > left and nums[i] > right:
                return i
        return -1

    def peak_element_better(self, nums: List[int]) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def peak_element_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low, high = 1, n - 2
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[mid - 1]:
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.peak_element_optimal([1, 2, 1, 3, 5, 6, 4]))
