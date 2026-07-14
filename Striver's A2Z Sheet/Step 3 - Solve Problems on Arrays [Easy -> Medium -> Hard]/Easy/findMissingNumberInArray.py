# mypy: disable-error-code="empty-body"
# QUESTION: Find the Missing Number
# An array contains n distinct numbers taken from the range [0, n] (one value in
# that range is missing). Return the missing number.
# Example 1:
# Input: arr = [3, 1, 0, 2]   (n = 4, range 0..4)
# Output: 4
# Explanation: 0,1,2,3 present; 4 is missing.
# Example 2:
# Input: arr = [0, 1]
# Output: 2
# Constraints:
# n == len(arr)
# 0 <= arr[i] <= n, all distinct

"""
#Brute Force:
1. For each candidate value 0..n, scan the array to see if it is present.
2. Return the first candidate not found.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Build a hash/frequency array of size n+1.
2. Mark each present element; return the index whose count stays 0.
TC -> O(2n), SC -> O(n)

#Optimal Approach:
1. XOR trick: xor all indices 0..n together, and xor all array elements together.
2. XOR the two results; pairs cancel and the missing number survives.
   (Sum formula n(n+1)/2 minus array sum also works but can overflow for huge n.)
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- a ^ a = 0, so XOR-ing the full range against the present elements annihilates
  every value that appears in both, leaving exactly the missing one.
"""

from typing import List


class Solution:
    def missing_number_brute(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n + 1):
            if not any(arr[j] == i for j in range(n)):
                return i
        return -1

    def missing_number_better(self, arr: List[int]) -> int:
        hashArray = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            hashArray[arr[i]] += 1
        for i in range(len(hashArray)):
            if hashArray[i] == 0:
                return i
        return -1

    def missing_number_optimal(self, arr: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        for i in range(len(arr)):
            xor1 ^= i
            xor2 ^= arr[i]
        xor1 ^= len(arr)
        return xor1 ^ xor2


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 1, 0, 2]
    print(sol.missing_number_optimal(arr))
