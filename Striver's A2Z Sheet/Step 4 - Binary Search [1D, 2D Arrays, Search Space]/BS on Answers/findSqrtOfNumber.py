# mypy: disable-error-code="empty-body"
# QUESTION: Find Square Root of a Number (floor)
# Given a non-negative integer n, return floor(sqrt(n)) — the largest integer x
# such that x*x <= n.
# Example 1:
# Input: n = 28
# Output: 5
# Explanation: 5*5 = 25 <= 28 < 36 = 6*6, so floor(sqrt(28)) = 5.
# Constraints:
# 0 <= n <= 10^9

"""
#Brute Force:
1. Iterate i from 1 upward while i*i <= n, tracking the last valid i.
TC -> O(sqrt(N)), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the answer is the improvement.

#Optimal Approach:
1. Binary search the answer in [0, n]. The predicate "mid*mid <= n" is monotone:
   true for small mid, false once mid exceeds the real root.
2. If mid*mid <= n, mid is a valid floor candidate; record it and go right
   (low = mid + 1) to try a larger root.
3. Else go left (high = mid - 1).
4. Return the last recorded candidate.
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- We binary search over the value of the answer itself, not over an array; the
  square being monotone increasing makes the search valid.
"""


class Solution:
    def sqrt_brute(self, n: int) -> int:
        ans = 0
        i = 1
        while i * i <= n:
            ans = i
            i += 1
        return ans

    def sqrt_better(self, n: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def sqrt_optimal(self, n: int) -> int:
        low, high = 0, n
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.sqrt_optimal(28))
