# mypy: disable-error-code="empty-body"
# QUESTION: Count the Number of Subarrays with Given XOR K
# Given an array nums and an integer k, count the contiguous subarrays whose
# elements XOR to exactly k.
# Example 1:
# Input: nums = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: [4,2], [4,2,2,6,4], [2,2,6], [6] all XOR to 6.
# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i], k <= 10^9

"""
#Brute Force:
1. Enumerate every subarray with two loops and XOR it with a third loop.
2. Count when the XOR equals k.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. Fix a start and extend the end with a running XOR, dropping the inner loop.
2. Count when the running XOR equals k.
TC -> O(n^2), SC -> O(1)

#Optimal Approach (Prefix XOR + Hashmap):
1. Track a running prefix XOR. A subarray ending at i XORs to k iff some earlier
   prefix XOR equals (prefixXor ^ k), because XOR is its own inverse.
2. Keep a hashmap prefixXor -> count seen, seeded with {0: 1}.
3. Add prefixCount[prefixXor ^ k] to the answer, then record the current prefix.
TC -> O(n) average, SC -> O(n)

#KEY INSIGHT:
- Since XOR cancels itself, xor(i..j) = prefix[j] ^ prefix[i-1]; counting earlier
  prefixes equal to (prefix ^ k) counts subarrays with XOR k in one pass.
"""

from collections import defaultdict
from typing import List


class Solution:
    def count_xor_brute(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                xor = 0
                for x in range(i, j + 1):
                    xor ^= nums[x]
                if xor == k:
                    cnt += 1
        return cnt

    def count_xor_better(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            xor = 0
            for j in range(i, len(nums)):
                xor ^= nums[j]
                if xor == k:
                    cnt += 1
        return cnt

    def count_xor_optimal(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_count: defaultdict[int, int] = defaultdict(int)
        prefix_count[0] = 1
        prefix_xor = 0
        for i in range(len(nums)):
            prefix_xor ^= nums[i]
            needed = prefix_xor ^ k
            cnt += prefix_count[needed]
            prefix_count[prefix_xor] += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_xor_optimal([4, 2, 2, 6, 4], 6))
