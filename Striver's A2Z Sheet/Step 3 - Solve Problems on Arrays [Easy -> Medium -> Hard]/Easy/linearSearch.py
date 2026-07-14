# mypy: disable-error-code="empty-body"
# QUESTION: Linear Search
# Given an array and a target k, return the index of the first occurrence of k,
# or -1 if it is not present.
# Example 1:
# Input: arr = [1, 1, 2, 2, 3, 4], k = 4
# Output: 5
# Explanation: 4 first appears at index 5.
# Constraints:
# 1 <= n <= 10^5

"""
#Brute Force:
SKIPPED — linear search IS the baseline; there is no cruder correct variant.

#Better Approach:
SKIPPED — without a sortedness assumption you cannot beat O(n) here.

#Optimal Approach:
1. Scan left to right.
2. Return the index of the first element equal to k.
3. If the loop ends, return -1.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- On an unsorted array every element could be the target, so any correct search
  must, in the worst case, inspect all n elements.
"""

from typing import List


class Solution:
    def linear_search_brute(self, arr: List[int], k: int) -> int:
        # SKIP: linear search is the baseline; no cruder correct variant.
        pass

    def linear_search_better(self, arr: List[int], k: int) -> int:
        # SKIP: cannot beat O(n) on an unsorted array.
        pass

    def linear_search_optimal(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] == k:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2, 2, 3, 4]
    print(sol.linear_search_optimal(arr, 4))
