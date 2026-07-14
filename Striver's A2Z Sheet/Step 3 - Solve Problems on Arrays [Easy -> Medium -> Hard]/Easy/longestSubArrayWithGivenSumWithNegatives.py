# mypy: disable-error-code="empty-body"
# QUESTION: Longest Subarray with Sum K (Positives and Negatives)
# Given an array that may contain negatives and zeros plus a target k, return
# the length of the longest contiguous subarray summing to exactly k.
# Example 1:
# Input: arr = [1, 2, 3, 1, 3, 1, 1, 1, 1, 3, 3, 2, 6], k = 7
# Output: 3
# Explanation: A subarray such as [3, 1, 3] sums to 7.
# Constraints:
# 1 <= n <= 10^5
# arr[i] can be negative, zero, or positive

"""
#Brute Force:
1. For every start i, extend j accumulating the sum.
2. When the running sum equals k, update the best length.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — the sliding window fails with negatives, so the prefix-sum + hashmap
below is the actual optimal; no separate middle tier applies here.

#Optimal Approach:
1. Prefix-sum + hashmap storing the EARLIEST index of each prefix sum.
2. At index i with prefix sum s: if s == k, the whole prefix qualifies.
3. If (s - k) was seen earlier at index p, the subarray (p+1..i) sums to k.
4. Only insert a prefix sum if unseen, so we keep the earliest index and thus the
   longest subarray (e.g. leading zeros must not be discarded).
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- With negatives the sum is not monotone, so the window trick breaks; instead,
  sum(i..j) = prefix[j] - prefix[i-1], and hashing earliest prefixes turns the
  search for a matching prefix into O(1) lookups.
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
        # SKIP: sliding window is invalid with negatives; prefix-sum hashmap is optimal.
        pass

    def longest_subarray_optimal(self, arr: List[int], k: int) -> int:
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


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 1, 3, 1, 1, 1, 1, 3, 3, 2, 6]
    print(sol.longest_subarray_optimal(arr, 7))
