# mypy: disable-error-code="empty-body"
# QUESTION: Factorial of N (and Factorial Numbers <= N)
# Given a number N, compute N! = 1 * 2 * ... * N using recursion.
# (Related task: return the list of factorial numbers <= N, e.g. 1, 2, 6, 24, ...)
# Example 1:
# Input: N = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
# Constraints:
# 1 <= N <= 20  (fits in 64-bit for the plain factorial)

"""
#Brute Force:
1. Iterative product: multiply 1*2*...*n in a loop.
TC -> O(n), SC -> O(1)

#Better Approach:
SKIPPED - no distinct intermediate approach; iterative and recursive are the two natural forms.

#Optimal Approach:
1. Recursive definition: fact(n) = n * fact(n-1), base case fact(0) = fact(1) = 1.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- Factorial is defined recursively (n! = n * (n-1)!), so the recursion mirrors the
  mathematical definition directly.
"""


class Solution:
    def factorial_brute(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def factorial_better(self, n: int) -> int:
        # SKIP: no distinct intermediate approach.
        pass

    def factorial_optimal(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self.factorial_optimal(n - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.factorial_optimal(5))
