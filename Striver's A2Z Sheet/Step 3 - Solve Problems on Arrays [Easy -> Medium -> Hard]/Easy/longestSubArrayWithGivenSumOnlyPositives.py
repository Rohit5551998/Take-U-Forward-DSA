# mypy: disable-error-code="empty-body"
# QUESTION: Longest Subarray with Sum K (Positives)
# Given an array of positive integers and a target k, return the length of the
# longest contiguous subarray whose elements sum to exactly k.
# Example 1:
# Input: arr = [1, 2, 3, 1, 1, 1, 1], k = 3
# Output: 3
# Explanation: [1, 1, 1] (or [1, 2]) sums to 3; longest such length is 3.
# Constraints:
# 1 <= n <= 10^5
# arr[i] > 0 (positives only)

"""
#Brute Force:
1. For every start i, extend j and accumulate the sum.
2. Whenever the running sum equals k, update the best length.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Prefix-sum + hashmap: store the earliest index of each prefix sum.
2. At index i with prefix sum s, if (s - k) was seen, that subarray sums to k.
3. Works even with negatives (that is the general solution).
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. Sliding window: grow the window with the right pointer, adding to sum.
2. While sum > k, shrink from the left. When sum == k, record the window length.
3. Valid only because all elements are positive (removing from left always
   reduces the sum monotonically).
TC -> O(2n), SC -> O(1)

#KEY INSIGHT:
- Positivity makes the running sum monotone in window size, so a two-pointer
  window can expand/contract to hit the target without ever backtracking.
"""

from typing import List


class Solution:
    def longest_subarray_brute(self, arr: List[int], k: int) -> int:
        maxLen = 0
        for i in range(len(arr)):
            s = 0
            for j in range(i, len(arr)):
                s += arr[j]
                if s == k:
                    maxLen = max(maxLen, j - i + 1)
        return maxLen

    def longest_subarray_better(self, arr: List[int], k: int) -> int:
        maxLen, s = 0, 0
        prefixSumHash: dict[int, int] = {}
        for i in range(len(arr)):
            s += arr[i]
            if s == k:
                maxLen = max(maxLen, i + 1)
            rem = s - k
            if rem in prefixSumHash:
                maxLen = max(maxLen, i - prefixSumHash[rem])
            if s not in prefixSumHash:
                prefixSumHash[s] = i
        return maxLen

    def longest_subarray_optimal(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == 0:
            return 0
        left, right, maxLen, s = 0, 0, 0, arr[0]
        while right < n:
            while s > k and left <= right:
                s -= arr[left]
                left += 1
            if s == k:
                maxLen = max(maxLen, right - left + 1)
            right += 1
            if right < n:
                s += arr[right]
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 1, 1, 1, 1]
    print(sol.longest_subarray_optimal(arr, 3))
