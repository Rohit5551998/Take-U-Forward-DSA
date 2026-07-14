# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Consecutive Ones
# Given a binary array, return the length of the longest run of consecutive 1s.
# Example 1:
# Input: arr = [1, 1, 0, 1, 1, 1, 0, 0, 1]
# Output: 3
# Explanation: The longest run of 1s has length 3.
# Constraints:
# 1 <= n <= 10^5
# arr[i] in {0, 1}

"""
#Brute Force:
SKIPPED — the single-pass counter below is the natural baseline; no cruder
correct variant is worth writing.

#Better Approach:
SKIPPED — you must read every element at least once, so O(n) is already best.

#Optimal Approach:
1. Keep a running count of the current 1-run and a global maximum.
2. On a 1, increment count and update the max; on a 0, reset count to 0.
3. Return the max.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The answer is the largest window of consecutive 1s; a 0 breaks the window, so
  resetting the counter there and tracking the peak is all that is required.
"""

from typing import List


class Solution:
    def max_consecutive_ones_brute(self, arr: List[int]) -> int:
        # SKIP: single-pass counter is the natural baseline.
        pass

    def max_consecutive_ones_better(self, arr: List[int]) -> int:
        # SKIP: must read every element; O(n) is already best.
        pass

    def max_consecutive_ones_optimal(self, arr: List[int]) -> int:
        count, maxCount = 0, 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        return maxCount


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 0, 1, 1, 1, 0, 0, 1]
    print(sol.max_consecutive_ones_optimal(arr))
