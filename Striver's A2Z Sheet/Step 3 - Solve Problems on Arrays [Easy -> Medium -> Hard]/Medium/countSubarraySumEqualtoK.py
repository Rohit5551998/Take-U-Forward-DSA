# mypy: disable-error-code="empty-body"
# QUESTION: Count Subarrays with Sum Equal to K
# Given an array nums and an integer k, count the number of contiguous subarrays
# whose elements sum to exactly k. The array may contain negatives.
# Example 1:
# Input: nums = [3, 1, 2, 4], k = 6
# Output: 2
# Explanation: The subarrays [1, 2, 4]... actually [3, 1, 2] (=6) and [2, 4] (=6).
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

"""
#Brute Force:
1. Enumerate every subarray with two loops and sum each with a third loop.
2. Increment the count whenever the sum equals k.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. Fix a start index and extend the end index, maintaining a running sum so the
   inner summation loop is removed.
2. Count whenever the running sum equals k.
TC -> O(n^2), SC -> O(1)

#Optimal Approach (Prefix Sum + Hashmap):
1. Track the running prefix sum. A subarray ending at i sums to k iff some
   earlier prefix equals (prefixSum - k).
2. Keep a hashmap of prefixSum -> how many times it has occurred, seeded with
   {0: 1} so subarrays that start at index 0 are counted.
3. For each element add prefixSum[prefixSum - k] to the answer, then record the
   current prefix sum.
TC -> O(n) average, SC -> O(n)

#KEY INSIGHT:
- sum(i..j) = prefix[j] - prefix[i-1], so counting how many earlier prefixes
  equal (current prefix - k) directly counts subarrays summing to k, even with
  negatives.
"""

from collections import defaultdict
from typing import List


class Solution:
    def count_subarray_brute(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = 0
                for x in range(i, j + 1):
                    total += nums[x]
                if total == k:
                    cnt += 1
        return cnt

    def count_subarray_better(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    cnt += 1
        return cnt

    def count_subarray_optimal(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_count: defaultdict[int, int] = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            cnt += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_subarray_optimal([3, 1, 2, 4], 6))
