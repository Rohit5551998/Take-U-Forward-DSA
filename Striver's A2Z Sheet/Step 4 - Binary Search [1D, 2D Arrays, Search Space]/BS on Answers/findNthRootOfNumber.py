# mypy: disable-error-code="empty-body"
# QUESTION: Find the Nth Root of a Number
# Given two integers n and m, find the integer nth root of m (i.e. x such that
# x^n == m). If no integer nth root exists, return -1.
# Example 1:
# Input: n = 4, m = 81
# Output: 3
# Explanation: 3^4 = 81, so the 4th root of 81 is 3.
# Constraints:
# 1 <= n <= 30
# 1 <= m <= 10^9

"""
#Brute Force:
1. Iterate x from 1 to m; compute x^n and return x when x^n == m, stop if x^n > m.
TC -> O(m * n), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the answer is the improvement.

#Optimal Approach:
1. Binary search x in [1, m]. Use a helper that multiplies mid n times but short
   circuits: returns 2 as soon as the running product exceeds m (avoids overflow /
   huge numbers), 1 if it exactly equals m, else 0.
2. If helper == 1, mid^n == m -> return mid.
3. If helper == 2, mid is too big -> high = mid - 1.
4. Else mid is too small -> low = mid + 1.
5. Return -1 if no exact root is found.
TC -> O(n * logM), SC -> O(1)

#KEY INSIGHT:
- x^n is monotone in x, so binary search applies; the capped power helper keeps
  comparisons cheap and safe against enormous intermediate products.
"""


class Solution:
    def _power_capped(self, base: int, n: int, m: int) -> int:
        product = 1
        for _ in range(n):
            product *= base
            if product > m:
                return 2
        return 1 if product == m else 0

    def nth_root_brute(self, n: int, m: int) -> int:
        for x in range(1, m + 1):
            val = self._power_capped(x, n, m)
            if val == 1:
                return x
            if val == 2:
                break
        return -1

    def nth_root_better(self, n: int, m: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def nth_root_optimal(self, n: int, m: int) -> int:
        low, high = 1, m
        while low <= high:
            mid = low + (high - low) // 2
            val = self._power_capped(mid, n, m)
            if val == 1:
                return mid
            if val == 2:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.nth_root_optimal(4, 81))
