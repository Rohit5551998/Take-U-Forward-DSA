# mypy: disable-error-code="empty-body"
# QUESTION: Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: Flip the two 0's in [...,0,0,1,1,1,1,...] -> longest run is 6.
# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

"""
#Brute Force:
1. Fix start i; extend j counting zeroes inside the window.
2. While zeroes <= k the window is flippable, so update max length; else break.
Why: directly checks every window against the "at most k zeroes" rule.
TC -> O(N*N), SC -> O(1)

#Better Approach:
1. Sliding window with an inner while: expand r counting zeroes.
2. While zeroes > k, shrink from l (decrementing zeroes when leaving a 0).
3. Record r - l + 1 for the now-valid window.
Why: each valid window is measured; l moves forward only.
TC -> O(2N), SC -> O(1)

#Optimal Approach:
1. Same window, but never shrink more than one step: replace the inner while with an if.
2. When zeroes > k, slide both edges by one (window keeps its size, only translates).
3. The recorded max never decreases, so a fixed-then-growing window yields the answer.
Why: the answer window is monotonic in length, so we never need to shrink below the best.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- "Longest window with at most k zeroes" - since we only ever want a longer window,
  the left edge can advance in lockstep with the right (never shrinking past the best).
"""

from typing import List


class Solution:
    def longestOnes_brute(self, nums: List[int], k: int) -> int:
        maxLen = 0
        for i in range(len(nums)):
            zeroes = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeroes += 1
                if zeroes <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen

    def longestOnes_better(self, nums: List[int], k: int) -> int:
        maxLen = 0
        zeroes = 0
        left = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxLen = max(maxLen, r - left + 1)
        return maxLen

    def longestOnes_optimal(self, nums: List[int], k: int) -> int:
        maxLen = 0
        zeroes = 0
        left = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            else:
                maxLen = max(maxLen, r - left + 1)
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes_optimal([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
