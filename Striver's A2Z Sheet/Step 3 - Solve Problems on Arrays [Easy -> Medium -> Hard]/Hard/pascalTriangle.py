# mypy: disable-error-code="empty-body"
# QUESTION: Pascal's Triangle (three variants)
# Variant 1: given row r and column c (1-indexed), return the element at (r, c).
# Variant 2: given a row number n, return the entire n-th row.
# Variant 3: given n, return the first n rows of Pascal's triangle.
# Example 1:
# Input: n = 5 (variant 3)
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# Explanation: Each element is the sum of the two directly above it.
# Constraints:
# 1 <= r, c, n <= 30 (values fit in a 32-bit signed integer)

"""
#Brute Force (Variant 1 - single element):
1. The element at (r, c) is the binomial coefficient nCr with n = r-1, r = c-1.
2. Compute it iteratively as product of (n-i)/(i+1) for i in 0..c-1, avoiding
   full factorials.
TC -> O(c), SC -> O(1)

#Better Approach (Variant 2 - one full row):
1. Start with value 1 (the first entry of the row).
2. Generate each next entry by multiplying by (n-i) and dividing by i, walking
   across the row without recomputing binomials from scratch.
TC -> O(n), SC -> O(1) (excluding the row output)

#Optimal Approach (Variant 3 - whole triangle):
1. For each row 1..n, generate that row using the Variant 2 linear method.
TC -> O(n^2), SC -> O(1) (excluding the triangle output)

#KEY INSIGHT:
- Adjacent entries in a Pascal row relate by the factor (n-i)/i, so each row (and
  thus the whole triangle) is built with simple running multiplication — no
  factorials and no dependence on the previous row.
"""

from typing import List


class Solution:
    def pascal_element_brute(self, row: int, col: int) -> int:
        ans = 1.0
        n, r = row - 1, col - 1
        for i in range(r + 1):
            ans *= n - i
            ans /= i + 1
        return int(ans)

    def pascal_row_better(self, n: int) -> List[int]:
        temp = [1]
        ans = 1.0
        for i in range(1, n):
            ans *= n - i
            ans /= i
            temp.append(int(ans))
        return temp

    def pascal_triangle_optimal(self, n: int) -> List[List[int]]:
        ans: List[List[int]] = []
        for i in range(1, n + 1):
            ans.append(self.pascal_row_better(i))
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.pascal_triangle_optimal(5))
