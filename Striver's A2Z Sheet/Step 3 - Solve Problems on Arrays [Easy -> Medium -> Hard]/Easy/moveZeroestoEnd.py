# mypy: disable-error-code="empty-body"
# QUESTION: Move Zeros to End
# Given an array, move all zeros to the end while keeping the relative order of
# the non-zero elements. Do it in-place.
# Example 1:
# Input: arr = [1, 0, 2, 3, 0, 4, 0, 1]
# Output: [1, 2, 3, 4, 1, 0, 0, 0]
# Explanation: Non-zero order preserved; zeros pushed to the tail.
# Constraints:
# 1 <= n <= 10^5

"""
#Brute Force:
1. Copy all non-zero elements into a temp array (preserving order).
2. Write them back to the front of the array.
3. Fill the remaining slots with zeros.
TC -> O(n) (2 passes), SC -> O(n)

#Better Approach:
SKIPPED — the two-pointer swap below removes the temp array with no
intermediate step in between.

#Optimal Approach:
1. Find the first zero index j (if none, array is already done).
2. From j+1, whenever a non-zero is found, swap it into slot j and advance j.
3. j always points at the leftmost zero, so swaps compact non-zeros forward.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Keeping j on the leftmost zero turns the problem into a partition: every
  non-zero encountered slides left into the zero region, preserving order.
"""

from typing import List


class Solution:
    def move_zeroes_brute(self, arr: List[int]) -> List[int]:
        temp = [x for x in arr if x != 0]
        for i in range(len(temp)):
            arr[i] = temp[i]
        for i in range(len(temp), len(arr)):
            arr[i] = 0
        return arr

    def move_zeroes_better(self, arr: List[int]) -> List[int]:
        # SKIP: two-pointer swap is directly optimal; no distinct middle tier.
        pass

    def move_zeroes_optimal(self, arr: List[int]) -> List[int]:
        j = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i
                break
        if j != -1:
            for i in range(j + 1, len(arr)):
                if arr[i] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 0, 2, 3, 0, 4, 0, 1]
    print(sol.move_zeroes_optimal(arr))
