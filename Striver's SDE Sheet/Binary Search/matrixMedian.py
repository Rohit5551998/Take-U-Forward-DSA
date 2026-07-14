# mypy: disable-error-code="empty-body"
# QUESTION: Matrix Median
# Given a 2D array matrix that is row-wise sorted (each row is sorted in non-decreasing order).
# The task is to find the median of the given matrix. Note: the total number of elements is
# guaranteed to be odd.
#
# Examples:
# Example 1:
# Input: matrix = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
# Output: 5
# Explanation: If we flatten the matrix into a sorted array, it becomes 1 2 3 4 5 6 7 8 9.
# So, median = 5.
#
# Example 2:
# Input: matrix = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
# Output: 3
# Explanation: If we flatten the matrix into a sorted array, it becomes 1 1 2 2 3 3 4 5 8.
# So, median = 3.
#
# Constraints:
# N == matrix.size, M == matrix[0].size
# 1 <= N, M <= 10^5
# 1 <= N*M <= 10^6
# 1 <= matrix[i][j] <= 10^9
# N*M is odd


"""
#Brute Force:
1. The median is just the middle element of the fully-sorted list of all
   values, so the simplest thing is to materialise that list: walk every cell
   of the matrix and append it into a flat array `nums`.
2. Sort `nums`. Now the elements are in global non-decreasing order, exactly the
   order the problem's definition of "flatten and sort" describes.
3. There are N*M elements and N*M is guaranteed odd, so the median sits at the
   single middle index (N*M)//2 (0-indexed). Return nums[(N*M)//2].
TC -> O(N*M * log(N*M)) (dominated by the sort of all N*M elements),
SC -> O(N*M) (the flattened array)

#Better Approach:
SKIPPED — no distinct middle tier. The problem goes straight from flatten+sort
(brute) to binary-searching the value range while counting per row (optimal);
there is no sensible intermediate algorithm.

#Optimal Approach:
1. Don't search positions, search the VALUE of the answer. Every candidate value
   lies in [min of first column, max of last column] (the smallest possible
   element is in some row's first cell, the largest in some row's last cell), so
   binary search that value range instead of materialising all N*M elements.
2. Define a probe: for a candidate `mid`, count how many matrix elements are
   <= mid. Because each row is sorted, this is an upper_bound binary search per
   row — sum the per-row counts to get the total `cnt` in O(N log M).
3. Characterise the median: with N*M odd, the median is the element sitting just
   past position (N*M)//2, i.e. the SMALLEST value whose "count of elements <=
   value" is strictly greater than (N*M)//2. Values below the median have a
   count <= (N*M)//2; the median is the first value to cross that threshold.
4. Drive the search with that predicate: if cnt > (N*M)//2 the answer is `mid`
   or smaller, so pull high left (high = mid - 1); otherwise mid is too small,
   so push low right (low = mid + 1).
5. When low crosses high, `low` has converged to the smallest value satisfying
   the predicate — that is the median. It is guaranteed to be a real matrix
   element because the count only jumps at values that actually occur.
TC -> O(log(max-min) * N * log M) (log(max-min) binary-search steps, each an
O(N log M) counting pass), SC -> O(1)

#KEY INSIGHT:
- The median is defined by a monotonic predicate on VALUE — "how many elements
  are <= v" only grows as v grows — so we binary search the value range and use
  row-wise counting as the check, sidestepping the O(N*M log(N*M)) full sort. The
  median is the first value whose <=-count exceeds half the total.
"""

import math
from typing import List


class Solution:
    def matrix_median_brute(self, matrix: List[List[int]]) -> int:
        nums = []

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                nums.append(matrix[i][j])

        nums.sort()
        return nums[len(matrix) * len(matrix[0]) // 2]

    def matrix_median_better(self, matrix: List[List[int]]) -> int:
        # SKIP: no distinct middle tier — the problem jumps from flatten+sort
        # (brute) straight to binary-searching the value range (optimal).
        pass

    def upper_bound(self, nums: List[int], element: int) -> int:
        # Upper bound: index of the first element strictly greater than `element`,
        # which equals the count of elements in sorted `nums` that are <= element.
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # For upper bound: if nums[mid] <= element, the boundary is to the
            # right, so discard mid and everything left of it (low = mid + 1).
            if element >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def matrix_median_optimal(self, matrix: List[List[int]]) -> int:
        low = math.inf
        high = -math.inf
        n, m = len(matrix), len(matrix[0])

        for i in range(0, n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m - 1])

        while low <= high:
            cnt = 0
            mid = low + (high - low) // 2

            # Total count of elements <= mid across all rows (upper bound per row)
            for i in range(0, n):
                cnt += self.upper_bound(matrix[i], mid)

            # If more than half the elements are <= mid, the median is mid or
            # smaller, so search left; otherwise mid is too small, search right.
            if cnt > (n * m) // 2:
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
    # matrix = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
    print(sol.matrix_median_brute(matrix))
    matrix = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
    # matrix = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
    print(sol.matrix_median_optimal(matrix))
