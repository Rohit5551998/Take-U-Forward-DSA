# mypy: disable-error-code="empty-body"
# QUESTION: Median of a Row-Wise Sorted Matrix
# Given an m x n matrix where every row is sorted in non-decreasing order and the
# total number of elements m*n is ODD, return the median (the middle element if
# all values were laid out in one sorted sequence).
# Example 1:
# Input: matrix = [[1,4,9],[2,5,6],[3,8,7]]
# Output: 5
# Explanation: Sorted, all 9 values are [1,2,3,4,5,6,7,8,9]; the middle one is 5.
# Constraints:
# 1 <= m, n <= 1000
# m * n is odd
# 1 <= matrix[i][j] <= 10^9

"""
#Brute Force:
1. Copy all m*n elements into one array and sort it.
2. The median is the element at index (m*n)//2.
TC -> O(N*M) + O(N*M log(N*M)), SC -> O(N*M)

#Better Approach:
SKIPPED — no distinct middle tier; the next step is binary search on the answer
(the value range), which is the optimal.

#Optimal Approach:
1. Binary search on the VALUE range, not on indices: low = min of column 0,
   high = max of the last column across all rows.
2. For a candidate value mid, count how many elements are <= mid. Since each row
   is sorted, count elements <= mid in a row via upper_bound (first index with a
   value strictly greater than mid), and sum across rows.
3. The median is the smallest value x such that at least (m*n)//2 + 1 elements are
   <= x, i.e. the count exceeds (m*n)//2. If count <= (m*n)//2 the median is
   larger, so low = mid+1; otherwise high = mid-1.
4. When the range collapses, low is the median.
TC -> O(log(maxVal) * N * logM), SC -> O(1)

#KEY INSIGHT:
- We never materialize the merged array. "How many elements are <= x" is monotonic
  in x, so binary searching that count over the value range pinpoints the median
  using only per-row upper-bound queries.
"""

import math
from typing import List


class Solution:
    def matrix_median_brute(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        arr: List[int] = []
        for i in range(n):
            for j in range(m):
                arr.append(matrix[i][j])
        arr.sort()
        return arr[(n * m) // 2]

    def matrix_median_better(self, matrix: List[List[int]]) -> int:
        # SKIP: no distinct better tier between full sort and binary-search-on-answer.
        pass

    def _upper_bound(self, arr: List[int], target: int) -> int:
        low, high, ans = 0, len(arr) - 1, len(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

    def _count_small_equal(self, matrix: List[List[int]], element: int) -> int:
        return sum(self._upper_bound(row, element) for row in matrix)

    def matrix_median_optimal(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        low, high = math.inf, -math.inf
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m - 1])

        req_cnt = (n * m) // 2
        low, high = int(low), int(high)
        while low <= high:
            mid = low + (high - low) // 2
            small_equal = self._count_small_equal(matrix, mid)
            if small_equal <= req_cnt:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    sol = Solution()
    print(sol.matrix_median_optimal([[1, 4, 9], [2, 5, 6], [3, 8, 7]]))
