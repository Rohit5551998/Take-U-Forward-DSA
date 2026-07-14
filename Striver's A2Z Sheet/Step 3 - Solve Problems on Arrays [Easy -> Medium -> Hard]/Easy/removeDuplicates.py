# mypy: disable-error-code="empty-body"
# QUESTION: Remove Duplicates from Sorted Array
# Given a sorted array, remove duplicates in-place so each unique element appears
# once. Return the number of unique elements; the first k slots hold them in order.
# Example 1:
# Input: arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
# Output: 4  (array becomes [1, 2, 3, 4, ...])
# Explanation: 4 unique values.
# Constraints:
# 1 <= n <= 10^5
# Array is sorted in non-decreasing order.

"""
#Brute Force:
1. Insert every element into an ordered set (dedupes + keeps order).
2. Copy the set back into the front of the array.
3. Return its size.
TC -> O(n log n), SC -> O(n)

#Better Approach:
SKIPPED — for a sorted array the two-pointer method is directly optimal; no
distinct intermediate exists.

#Optimal Approach:
1. Pointer i marks the last unique slot (starts at 0); j scans ahead.
2. When arr[j] differs from arr[i], advance i and copy arr[j] into arr[i].
3. Return i + 1 (count of uniques).
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Because the array is sorted, equal values are adjacent, so comparing each new
  element only against the last kept unique is enough to detect duplicates.
"""

from typing import List


class Solution:
    def remove_duplicates_brute(self, arr: List[int]) -> int:
        uniques = sorted(set(arr))
        for i in range(len(uniques)):
            arr[i] = uniques[i]
        return len(uniques)

    def remove_duplicates_better(self, arr: List[int]) -> int:
        # SKIP: two-pointer is directly optimal for a sorted array.
        pass

    def remove_duplicates_optimal(self, arr: List[int]) -> int:
        i = 0
        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        return i + 1


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
    print(sol.remove_duplicates_optimal(arr))
