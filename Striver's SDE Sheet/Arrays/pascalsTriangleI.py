# QUESTION: Pascal's Triangle I
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it. The first and last entries of each row are always 1.
#
# Examples:
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
# 1 <= numRows <= 30
#
# Variants (Striver sheet covers all three):
# 1) Given row and column (r, c), return the value at that position.
# 2) Given a row number n, return the n-th row of Pascal's triangle.
# 3) Given numRows, return the entire Pascal's triangle up to numRows rows.


"""
(This problem is actually three separate variants, not brute/better/optimal of
one problem. Each variant below is solved at its optimal complexity by rolling
the binomial coefficient forward instead of recomputing factorials.)

#Variant I — value at position (row, col):  pascals_triangle_i_variant_i
1. Observe that the element at (row, col) in Pascal's triangle is exactly the
   binomial coefficient C(row-1, col-1) — e.g. (5, 3) -> C(4, 2) = 6.
2. Instead of computing factorials (which overflow and waste work), build nCr
   incrementally: start ans = 1, then for j in 1..col-1 multiply by the next
   numerator term and divide by j, i.e. ans *= (row - j) / j. Each step turns
   C(row-1, j-1) into C(row-1, j).
3. Cast the final ans to int() before returning, since the running product is
   a float.
TC -> O(col), SC -> O(1)

#Variant II — the whole r-th row:  pascals_triangle_i_variant_ii
1. Seed the result with res = [1], because the first entry of every row is 1.
2. Walk left-to-right across the row, reusing the previous entry instead of
   recomputing from scratch: keep a running ans (starting at 1) and for
   i in 1..row-1 do ans *= (row - i) / i, which advances ans to the next
   coefficient in the row.
3. Append round(ans) at each step (round, not int, to absorb floating-point
   drift) so the row is built up entry by entry.
TC -> O(row), SC -> O(row) for the output

#Variant III — full triangle of n rows:  pascals_triangle_i_variant_iii
1. The full triangle is just every row stacked together, so loop i from 1..n
   and call Variant II to generate the i-th row.
2. Append each generated row to res and return the list of rows.
TC -> O(n^2), SC -> O(n^2) for the output  (n rows, the i-th of length i, so
   total entries ~ n*(n+1)/2)

#KEY INSIGHT:
- Every entry is a binomial coefficient C(r, c). Within a row, consecutive
  coefficients are related by ans = ans * (row - i) / i, so each next value is
  one multiply/divide away from the previous one — turning the naive O(n^3)
  factorial computation into O(n) per row / O(n^2) overall.
"""

from typing import List


class Solution:
    def pascals_triangle_i_variant_i(self, row: int, col: int) -> int:
        ans = 1.0
        for j in range(1, col):
            ans *= (row - j) / (j)
        return int(ans)

    def pascals_triangle_i_variant_ii(self, row: int) -> List[int]:
        res = [1]
        ans = 1.0
        for i in range(1, row):
            ans *= (row - i) / i
            res.append(round(ans))
        return res

    def pascals_triangle_i_variant_iii(self, rows: int) -> List[List[int]]:
        res = []
        for i in range(1, rows + 1):
            res.append(self.pascals_triangle_i_variant_ii(i))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.pascals_triangle_i_variant_i(5, 3))
    print(sol.pascals_triangle_i_variant_ii(5))
    print(sol.pascals_triangle_i_variant_iii(12))
