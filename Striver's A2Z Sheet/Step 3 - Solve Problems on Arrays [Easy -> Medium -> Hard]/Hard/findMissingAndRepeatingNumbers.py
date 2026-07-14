# mypy: disable-error-code="empty-body"
# QUESTION: Find the Repeating and Missing Number
# An array of size n holds the numbers 1..n but one number is missing and one is
# repeated (appears twice). Return [repeating, missing].
# Example 1:
# Input: nums = [3, 1, 2, 5, 4, 6, 7, 5]
# Output: [5, 8]
# Explanation: 5 appears twice and 8 (in range 1..8) is missing.
# Constraints:
# 1 <= n <= 10^5
# nums contains numbers from 1..n with exactly one repeat and one missing

"""
#Brute Force:
1. For each value v in 1..n, count its occurrences in the array.
2. Count 2 -> repeating; count 0 -> missing.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Use a frequency array (hash) of size n+1.
2. The value with frequency 2 is the repeat; the value with frequency 0 is
   missing.
TC -> O(2n), SC -> O(n)

#Optimal Approach (XOR + Bit Manipulation):
1. XOR all array elements together with all numbers 1..n. The result is
   X ^ Y where X = repeating, Y = missing (everything else cancels).
2. Isolate the rightmost set bit of X ^ Y — the bit where X and Y differ.
3. Partition both the array elements and 1..n into two buckets by that bit and
   XOR each bucket; the two buckets yield X and Y (order unknown).
4. Scan the array once to see which of the two actually appears (that is the
   repeating number); the other is missing.
(An alternative O(n)/O(1) method solves the two equations from S-Sn = X-Y and
S2-S2n = X^2-Y^2.)
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- XOR-ing the array with 1..n cancels all correct numbers, leaving X ^ Y; a
  single differing bit then splits X and Y into separately recoverable groups
  with no extra space.
"""

from typing import List


class Solution:
    def missing_repeating_brute(self, nums: List[int]) -> List[int]:
        repeating, missing = -1, -1
        for v in range(1, len(nums) + 1):
            cnt = 0
            for j in range(len(nums)):
                if v == nums[j]:
                    cnt += 1
            if cnt == 2:
                repeating = v
            if cnt == 0:
                missing = v
        return [repeating, missing]

    def missing_repeating_better(self, nums: List[int]) -> List[int]:
        repeating, missing = -1, -1
        freq = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        for i in range(1, len(freq)):
            if freq[i] == 2:
                repeating = i
            if freq[i] == 0:
                missing = i
            if repeating != -1 and missing != -1:
                break
        return [repeating, missing]

    def missing_repeating_optimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= nums[i]
            xor ^= i + 1
        bit = xor & ~(xor - 1)
        zero, one = 0, 0
        for i in range(n):
            if nums[i] & bit != 0:
                one ^= nums[i]
            else:
                zero ^= nums[i]
        for i in range(1, n + 1):
            if i & bit != 0:
                one ^= i
            else:
                zero ^= i
        cnt = 0
        for i in range(n):
            if nums[i] == zero:
                cnt += 1
        return [zero, one] if cnt == 2 else [one, zero]


if __name__ == "__main__":
    sol = Solution()
    print(sol.missing_repeating_optimal([3, 1, 2, 5, 4, 6, 7, 5]))
