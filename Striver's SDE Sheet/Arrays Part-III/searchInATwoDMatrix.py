# QUESTION: Search in a 2D matrix
# You have been given a 2D array 'mat' of size 'N x M' where 'N' and 'M'
# denote the number of rows and columns, respectively. The elements of each
# row are sorted in non-decreasing order. Moreover, the first element of a
# row is greater than the last element of the previous row. Given an
# integer 'target', determine if it exists in the matrix or not. Return
# true if it exists; otherwise return false.
#
# Examples:
# Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
# Output :True.
# Explanation :The target = 8 exists in the 'mat' at index (1, 3).
#
# Input :mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
# Output :false.
# Explanation :The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.


"""
(The QUESTION here is the fully-sorted variant: each row is sorted AND every
row's first element exceeds the previous row's last, so the matrix is one sorted
sequence in row-major order. Variant II below is the true optimal for it;
Variant I is the optimal for the looser "rows AND columns sorted" variant and is
included because it also works here.)

#Brute Force:
1. Ignore all the sortedness and just look everywhere: a double loop over every
   row i and column j, returning True if any matrix[i][j] == target.
2. It's the baseline — correct but wasteful. (Minor: the inner `break` only exits
   the inner loop, so it keeps scanning later rows after a hit; still correct.)
TC -> O(n*m), SC -> O(1)

#Better Approach:
1. Use the row layout: since each row is sorted and rows don't overlap in value
   range, the target can sit in AT MOST one row — the one whose span
   [matrix[i][0], matrix[i][m-1]] contains it.
2. Linearly scan the rows to find that candidate row (first row whose first
   element <= target <= last element).
3. Binary-search only that row (the binary_search helper) for the target.
4. So it's one linear row-scan plus one in-row binary search.
TC -> O(n + log m), SC -> O(1)

#Optimal Variant I — staircase search from the top-right corner:  ..._optimal_variant_i
1. This is the classic search for a matrix sorted along BOTH rows and columns.
   Start at the top-right cell (i = 0, j = m-1): it is the largest in its row and
   the smallest in its column, which makes each comparison decisive.
2. Compare matrix[i][j] with target and shrink the search box by one line:
   - equal -> found.
   - matrix[i][j] > target -> the whole column j (rows >= i) is too big, so drop
     the column by moving left (j -= 1).
   - matrix[i][j] < target -> the whole row i (cols <= j) is too small, so drop
     the row by moving down (i += 1).
3. Every step eliminates a full row or column, so it touches at most n + m cells.
4. It correctly solves this problem too, but for the fully-sorted variant it's
   O(n+m) — slower than Variant II — so it's the optimal for the *other* variant.
TC -> O(n + m), SC -> O(1)

#Optimal Variant II — binary search treating the matrix as one 1-D array:  ..._optimal_variant_ii
1. Because the matrix is fully sorted in row-major order, it behaves exactly like
   a single sorted array of length n*m — so a single binary search solves it.
2. Binary-search the virtual index range low = 0 .. high = n*m - 1. For a midpoint
   `mid`, recover its real cell with row = mid // m and col = mid % m (m = #cols).
3. Compare matrix[row][col] with target and move low/high as in ordinary binary
   search until found or the range is empty.
4. One binary search over all n*m elements — the true optimal for this variant.
TC -> O(log(n*m)), SC -> O(1)

#KEY INSIGHT:
- The rows are sorted AND chained (each row starts above the previous row's end),
  so the matrix IS one sorted 1-D array in row-major order — a single binary
  search over n*m elements with the index map row = mid // m, col = mid % m gives
  O(log(n*m)). (When only rows-and-columns are sorted but not globally chained,
  the top-right staircase in O(n+m) is the right tool instead.)
"""

from typing import List


class Solution:
    def search_in_a_twod_matrix_brute(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == target:
                    ans = True
                    break
        return ans

    def binary_search(self, arr: List[int], target: int) -> bool:
        low, high = 0, len(arr) - 1
        ans = False

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                ans = True
                break
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1

        return ans

    def search_in_a_twod_matrix_better(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        n, m = len(matrix), len(matrix[0])
        for i in range(0, n):
            if target >= matrix[i][0] and target <= matrix[i][m - 1]:
                ans = self.binary_search(matrix[i], target)
                break
        return ans

    # Both Row & Column Sorted Variant Better In Case of Only Row Sorted Variant
    def search_in_a_twod_matrix_optimal_variant_i(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        ans = False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                ans = True
                break
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1

        return ans

    # Binary Search with Virtual Indices
    def search_in_a_twod_matrix_optimal_variant_ii(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = (n * m) - 1
        ans = False

        while low <= high:
            mid = (low + high) // 2
            i = mid // m
            j = mid % m
            if matrix[i][j] == target:
                ans = True
                break
            if matrix[i][j] > target:
                high = mid - 1
            elif matrix[i][j] < target:
                low = mid + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target = 8
    print(sol.search_in_a_twod_matrix_brute(mat, target))
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target = 8
    print(sol.search_in_a_twod_matrix_better(mat, target))
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target = 8
    print(sol.search_in_a_twod_matrix_optimal_variant_i(mat, target))
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target = 8
    print(sol.search_in_a_twod_matrix_optimal_variant_ii(mat, target))
