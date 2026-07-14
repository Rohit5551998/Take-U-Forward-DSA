# mypy: disable-error-code="empty-body"
# QUESTION: Rotate Array by K Places
# Given an array and an integer k, rotate the array by k positions in-place.
# Both left and right variants are implemented.
# Example 1:
# Input: arr = [1, 2, 3, 4, 5, 6, 7], k = 3  (left)
# Output: [4, 5, 6, 7, 1, 2, 3]
# Explanation: The first 3 elements move to the back.
# Constraints:
# 1 <= n <= 10^5
# 0 <= k <= 10^9  (reduce with k % n)

"""
#Brute Force:
SKIPPED — the block-shift with a temp array below is the standard first
solution; a per-step k-times rotation is strictly worse and omitted.

#Better Approach:
1. Reduce k = k % n.
2. Copy the k boundary elements into a temp array.
3. Shift the remaining n-k elements into place.
4. Copy the temp block into the vacated slots.
TC -> O(n), SC -> O(k)

#Optimal Approach:
1. Reduce k = k % n.
2. For a left rotate: reverse arr[0..k-1], reverse arr[k..n-1], reverse the whole.
   (Right rotate mirrors the segment boundaries.)
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Rotation is three reversals: reversing the two halves separately and then the
  whole array swaps the blocks without any temporary buffer.
"""

from typing import List


class Solution:
    def rotate_by_k_brute(self, arr: List[int], k: int) -> List[int]:
        # SKIP: rotating one step k times is O(n*k); the reversal method dominates.
        pass

    def rotate_left_by_k_better(self, arr: List[int], k: int) -> List[int]:
        if len(arr) > 1:
            k = k % len(arr)
            temp = [arr[i] for i in range(k)]
            for i in range(k, len(arr)):
                arr[i - k] = arr[i]
            for i in range(k):
                arr[len(arr) - k + i] = temp[i]
        return arr

    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate_left_by_k_optimal(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        k = k % n
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)
        self.reverse(arr, 0, n - 1)
        return arr

    def rotate_right_by_k_optimal(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        k = k % n
        self.reverse(arr, n - k, n - 1)
        self.reverse(arr, 0, n - k - 1)
        self.reverse(arr, 0, n - 1)
        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(sol.rotate_left_by_k_optimal(arr, 3))
