# mypy: disable-error-code="empty-body"
# QUESTION: Check if a Number is Prime
# Given an integer n, determine whether it is a prime number. A prime number is
# a natural number greater than 1 that has exactly two distinct factors: 1 and
# itself. Return True if n is prime, else False.
#
# Example 1:
# Input: n = 7
# Output: True
# Explanation: factors of 7 are {1, 7} only.
#
# Example 2:
# Input: n = 9
# Output: False
# Explanation: 9 = 3 * 3, so it also has factor 3.
#
# Example 3:
# Input: n = 1
# Output: False
# Explanation: 1 has only a single factor, so it is not prime.


"""
#Brute Force (check_prime_brute):
1. A prime has no divisor other than 1 and itself, so test every candidate
   factor i from 2 up to n-1.
2. If any such i divides n exactly (n % i == 0), n has a third factor and is not
   prime — return False immediately.
3. Guard n <= 1 up front: 0, 1 (and negatives) are not prime by definition.
4. If the loop finds no divisor, n is prime.
TC -> O(n), SC -> O(1)

#Better Approach:
SKIPPED — no intermediate tier; the search jumps straight from scanning all of
[2, n-1] to scanning only up to sqrt(n).

#Optimal Approach (check_prime_optimal):
1. Divisors pair up around sqrt(n): if i divides n then so does n/i, and one of
   that pair is always <= sqrt(n). So a factor above sqrt(n) implies a matching
   factor at or below it.
2. Hence it suffices to test candidate factors i from 2 up to sqrt(n); if none
   divides n, none above sqrt(n) can either.
3. Guard n <= 1 as not prime, then scan [2, sqrt(n)] and fail on the first
   divisor found.
TC -> O(sqrt(n)), SC -> O(1)

#KEY INSIGHT:
- Factors are symmetric about sqrt(n): every divisor i <= sqrt(n) has a partner
  n/i >= sqrt(n). Checking only up to sqrt(n) therefore certifies primality while
  doing quadratically less work than scanning all the way to n.
"""

import math


class Solution:
    def check_prime_brute(self, n: int) -> bool:
        if n <= 1:
            return False
        return all(n % i != 0 for i in range(2, n))

    def check_prime_better(self, n: int) -> bool:
        # SKIP: no middle tier — the [2, n-1] scan (brute) goes straight to the
        # [2, sqrt(n)] scan (optimal).
        pass

    def check_prime_optimal(self, n: int) -> bool:
        if n <= 1:
            return False
        return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


if __name__ == "__main__":
    sol = Solution()
    print(sol.check_prime_optimal(7))
    print(sol.check_prime_optimal(9))
    print(sol.check_prime_optimal(1))
