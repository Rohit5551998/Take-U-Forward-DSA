# mypy: disable-error-code="empty-body"
# QUESTION: Find the Number that Appears Once
# In an array every element appears exactly twice except one, which appears once.
# Return that single element.
# Example 1:
# Input: arr = [1, 4, 2, 1, 4]
# Output: 2
# Explanation: 1 and 4 appear twice; 2 appears once.
# Constraints:
# 1 <= n <= 10^5 (n is odd)
# every value except one appears exactly twice

"""
#Brute Force:
1. For each element, count its occurrences with a nested scan.
2. Return the element whose count is 1.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Build a frequency map of every element.
2. Return the key whose value is 1.
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. XOR all elements together.
2. Every paired value cancels to 0; the unique element remains.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- XOR is associative/commutative and a ^ a = 0, so duplicate pairs vanish
  regardless of order and only the once-appearing value survives.
"""

from collections import defaultdict
from typing import List


class Solution:
    def appears_once_brute(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            cnt = 0
            for j in range(len(arr)):
                if arr[j] == arr[i]:
                    cnt += 1
            if cnt == 1:
                return arr[i]
        return -1

    def appears_once_better(self, arr: List[int]) -> int:
        freq: defaultdict[int, int] = defaultdict(int)
        for i in range(len(arr)):
            freq[arr[i]] += 1
        for k, v in freq.items():
            if v == 1:
                return k
        return -1

    def appears_once_optimal(self, arr: List[int]) -> int:
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
        return xor


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 4, 2, 1, 4]
    print(sol.appears_once_optimal(arr))
