# mypy: disable-error-code="empty-body"
# QUESTION: Row with Maximum Number of 1s
# Given a matrix where each ROW is sorted (all 0s then all 1s), return the index of
# the row containing the most 1s. If several rows tie, return the smallest index.
# Return -1 if there are no 1s.
# Example 1:
# Input: matrix = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
# Output: 2
# Explanation: Row 2 = [1,1,1,1] has four 1s, the most of any row.
# Constraints:
# 1 <= n, m <= 1000
# Each row is sorted: 0s followed by 1s.

"""
#Brute Force:
1. For each row, scan for the first 1; the count of 1s is m - firstIndex. Track the
   row with the largest count.
TC -> O(N*M), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; per-row binary search is the improvement.

#Optimal Approach:
1. Each row is sorted, so the number of 1s = m - lowerBound(row, 1), where the
   lower bound is the first index holding a value >= 1.
2. Compute this per row via binary search, tracking the row index with the max
   count (keeping the smallest index on ties by using strict '>').
TC -> O(N * logM), SC -> O(1)

#KEY INSIGHT:
- Row-sortedness turns "count of 1s" into a lower-bound query, so each row is
  handled in logM instead of M.
"""

from typing import List


class Solution:
    def row_max_ones_brute(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_cnt, max_idx = 0, -1
        for i in range(n):
            cnt = 0
            for j in range(m):
                if matrix[i][j] == 1:
                    cnt = m - j
                    break
            if cnt > max_cnt:
                max_cnt = cnt
                max_idx = i
        return max_idx

    def row_max_ones_better(self, matrix: List[List[int]]) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def _lower_bound(self, row: List[int], target: int) -> int:
        low, high = 0, len(row) - 1
        ans = len(row)
        while low <= high:
            mid = low + (high - low) // 2
            if row[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def row_max_ones_optimal(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_cnt, max_idx = -1, -1
        for i in range(n):
            cnt = m - self._lower_bound(matrix[i], 1)
            if cnt > 0 and cnt > max_cnt:
                max_cnt = cnt
                max_idx = i
        return max_idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.row_max_ones_optimal([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
