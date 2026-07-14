# mypy: disable-error-code="empty-body"
# QUESTION: Nth Fibonacci Number using Recursion
# The Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
# Given n, return the nth Fibonacci number.
# Example 1:
# Input: n = 5
# Output: 5
# Explanation: 0, 1, 1, 2, 3, 5 -> F(5) = 5
# Constraints:
# 0 <= n <= 90  (fits in 64-bit)

"""
#Brute Force:
1. Plain recursion following the definition: fib(n) = fib(n-1) + fib(n-2).
2. Base cases fib(0)=0, fib(1)=1.
TC -> O(2^n), SC -> O(n) recursion depth

#Better Approach:
1. Memoised recursion: cache each computed fib(k) in an array so each is solved once.
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. Bottom-up iteration keeping only the last two values (prev2, prev1).
2. Loop from 2 to n updating curr = prev1 + prev2.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Naive recursion recomputes overlapping subproblems exponentially; since fib(n) only
  needs the previous two terms, two rolling variables suffice.
"""

from typing import List


class Solution:
    def fib_brute(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib_brute(n - 1) + self.fib_brute(n - 2)

    def fib_better(self, n: int, memo: List[int]) -> int:
        if n <= 1:
            return n
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.fib_better(n - 1, memo) + self.fib_better(n - 2, memo)
        return memo[n]

    def fib_optimal(self, n: int) -> int:
        if n <= 1:
            return n
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib_optimal(5))
