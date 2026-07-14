# mypy: disable-error-code="empty-body"
# QUESTION: Intersection of Two Sorted Arrays
# Given two sorted arrays, return their intersection (elements present in both,
# with multiplicity, in sorted order).
# Example 1:
# Input: arr1 = [1, 2, 3, 3, 4, 5, 6], arr2 = [1, 3, 3, 6, 7, 10]
# Output: [1, 3, 3, 6]
# Explanation: Common elements taken with the matching multiplicity.
# Constraints:
# 1 <= m, n <= 10^5
# Both arrays sorted in non-decreasing order.

"""
#Brute Force:
1. For each element of arr1, scan arr2 for an unused equal element.
2. Mark matched positions in arr2 with a visited array so each match is used once.
TC -> O(m * n), SC -> O(n)

#Better Approach:
SKIPPED — sorted inputs make the two-pointer walk directly optimal; the visited
approach is the only meaningfully worse tier.

#Optimal Approach:
1. Two pointers i, j over the sorted arrays.
2. If arr1[i] < arr2[j], advance i; if greater, advance j.
3. If equal, record the value and advance both pointers.
TC -> O(m + n), SC -> O(1) extra (output aside)

#KEY INSIGHT:
- Sortedness means unequal fronts can never match, so advancing the smaller
  pointer safely discards it and the whole scan is linear.
"""

from typing import List


class Solution:
    def intersection_brute(self, arr1: List[int], arr2: List[int]) -> List[int]:
        visited = [0] * len(arr2)
        result: List[int] = []
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i] == arr2[j] and visited[j] == 0:
                    result.append(arr1[i])
                    visited[j] = 1
                    break
        return result

    def intersection_better(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # SKIP: sorted inputs make the two-pointer walk directly optimal.
        pass

    def intersection_optimal(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        result: List[int] = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3, 3, 4, 5, 6]
    arr2 = [1, 3, 3, 6, 7, 10]
    print(sol.intersection_optimal(arr1, arr2))
