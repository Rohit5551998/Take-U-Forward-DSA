# mypy: disable-error-code="empty-body"
# QUESTION: Print All Divisors of a Number
# Given a positive integer n, return all of its divisors (numbers that divide n
# exactly) in ascending order.
#
# Example 1:
# Input: n = 36
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
#
# Example 2:
# Input: n = 7
# Output: [1, 7]
# Explanation: 7 is prime, so only 1 and 7 divide it.


"""
#Brute Force (print_all_divisors_brute):
1. A divisor of n is any i in [1, n] with n % i == 0, so simply test every such i.
2. Collect each i that divides n; iterating upward means the result is already in
   ascending order.
TC -> O(n), SC -> O(number of divisors)

#Better Approach:
SKIPPED — no middle tier; the full [1, n] scan is replaced directly by the
sqrt(n) paired-divisor scan.

#Optimal Approach (print_all_divisors_optimal):
1. Divisors come in pairs (i, n/i) that straddle sqrt(n): if i divides n then so
   does n/i, and one of the pair is always <= sqrt(n).
2. So scan only i in [1, sqrt(n)]; for each divisor i, record BOTH i and n // i.
3. Skip the duplicate when i == n // i (perfect square) so sqrt(n) isn't added
   twice.
4. The pairs come out unsorted, so sort once before returning.
TC -> O(sqrt(n) + d log d) where d = number of divisors, SC -> O(d)

#KEY INSIGHT:
- Because divisors pair around sqrt(n), one pass up to sqrt(n) recovers every
  divisor (each i yields its partner n/i for free), turning an O(n) scan into an
  O(sqrt(n)) one plus a final sort.
"""

import math
from typing import List


class Solution:
    def print_all_divisors_brute(self, n: int) -> List[int]:
        response = []
        for i in range(1, n + 1):
            if n % i == 0:
                response.append(i)
        return response

    def print_all_divisors_better(self, n: int) -> List[int]:
        # SKIP: no middle tier — the full [1, n] scan (brute) jumps straight to
        # the sqrt(n) paired-divisor scan (optimal).
        pass

    def print_all_divisors_optimal(self, n: int) -> List[int]:
        response = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                response.append(i)
                if i != n // i:
                    response.append(n // i)
        response.sort()
        return response


if __name__ == "__main__":
    sol = Solution()
    print(sol.print_all_divisors_optimal(36))
    print(sol.print_all_divisors_optimal(7))
