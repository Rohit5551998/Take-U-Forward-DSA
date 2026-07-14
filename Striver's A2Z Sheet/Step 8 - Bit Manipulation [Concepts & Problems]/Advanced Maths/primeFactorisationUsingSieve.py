# mypy: disable-error-code="empty-body"
# QUESTION: Find Prime Factorisation of a Number using Sieve
# Given a number N and a series of queries, for each query return the full prime
# factorisation of the queried number efficiently by precomputing the Smallest Prime
# Factor (SPF) of every number up to N using a sieve.
# Example 1:
# Input: N = 12
# Output: [2, 2, 3]
# Explanation: 12 = 2 * 2 * 3; the SPF sieve lets us extract each prime factor in O(log x).
# Example 2:
# Input: N = 60
# Output: [2, 2, 3, 5]
# Explanation: 60 = 2^2 * 3 * 5.
# Constraints:
# 1 <= N <= 10^5

"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def primeFactorisationSieve_brute(self, N: int) -> List[int]:
        pass

    def primeFactorisationSieve_better(self, N: int) -> List[int]:
        pass

    def primeFactorisationSieve_optimal(self, N: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.primeFactorisationSieve_optimal(12))
