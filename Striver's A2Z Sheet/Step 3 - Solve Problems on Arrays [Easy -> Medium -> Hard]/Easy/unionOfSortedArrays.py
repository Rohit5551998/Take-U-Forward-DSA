# mypy: disable-error-code="empty-body"
# QUESTION: Union of Two Sorted Arrays
# Given two sorted arrays, return their union (all distinct elements from both,
# in sorted order).
# Example 1:
# Input: arr1 = [1, 2, 3, 4, 5, 6], arr2 = [1, 7, 10, 15, 19]
# Output: [1, 2, 3, 4, 5, 6, 7, 10, 15, 19]
# Explanation: Every distinct value from either array, sorted.
# Constraints:
# 1 <= m, n <= 10^5
# Both arrays sorted in non-decreasing order.

"""
#Brute Force:
1. Insert every element of both arrays into a set.
2. Sort the set to produce the union.
TC -> O((m+n) log(m+n)), SC -> O(m+n)

#Better Approach:
SKIPPED — since the inputs are already sorted, the merge below is directly
optimal; the set approach is the only meaningfully worse tier.

#Optimal Approach:
1. Two pointers i, j over the sorted arrays.
2. Append the smaller current element, but only if it differs from the last value
   already placed in the union (dedupe).
3. Advance the pointer of the value taken.
4. Drain the remaining tail of whichever array is left, deduping the same way.
TC -> O(m + n), SC -> O(m + n) for the output

#KEY INSIGHT:
- Sorted inputs let a linear merge produce sorted output; comparing each
  candidate against the union's last element removes duplicates for free.
"""

from typing import List


class Solution:
    def union_brute(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(set(arr1) | set(arr2))

    def union_better(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # SKIP: sorted inputs make the merge directly optimal.
        pass

    def union_optimal(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        union: List[int] = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
        while i < len(arr1):
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        while j < len(arr2):
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        return union


if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [1, 7, 10, 15, 19]
    print(sol.union_optimal(arr1, arr2))
