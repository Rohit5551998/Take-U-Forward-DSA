# mypy: disable-error-code="empty-body"
# QUESTION: Left Rotate an Array by One Place
# Given an array, rotate it left by one position in-place (each element moves one
# slot toward index 0; the first element wraps to the end). A right-rotate helper
# is included as well.
# Example 1:
# Input: arr = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
# Explanation: Every element shifted one step left, 1 wrapped to the tail.
# Constraints:
# 1 <= n <= 10^5

"""
#Brute Force:
1. Copy the whole array into a temp array shifted by one, then copy back.
TC -> O(n), SC -> O(n)

#Better Approach:
SKIPPED — a single saved element already removes the extra array; nothing
between brute and optimal.

#Optimal Approach:
1. Save the boundary element (arr[0] for left, arr[-1] for right) in one temp.
2. Shift every other element one slot in the rotation direction.
3. Drop the saved element into the freed slot.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A one-step rotation only displaces a single element permanently; everyone else
  just slides by one, so one temp variable is all the extra space needed.
"""

from typing import List


class Solution:
    def rotate_left_by1_brute(self, arr: List[int]) -> List[int]:
        n = len(arr)
        temp = [arr[(i + 1) % n] for i in range(n)]
        for i in range(n):
            arr[i] = temp[i]
        return arr

    def rotate_left_by1_better(self, arr: List[int]) -> List[int]:
        # SKIP: one temp variable already reaches optimal; no distinct tier.
        pass

    def rotate_left_by1_optimal(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            temp = arr[0]
            for i in range(1, len(arr)):
                arr[i - 1] = arr[i]
            arr[len(arr) - 1] = temp
        return arr

    def rotate_right_by1_optimal(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            temp = arr[len(arr) - 1]
            for i in range(len(arr) - 2, -1, -1):
                arr[i + 1] = arr[i]
            arr[0] = temp
        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.rotate_left_by1_optimal(arr))
