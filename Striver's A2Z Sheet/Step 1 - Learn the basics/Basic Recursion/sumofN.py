# mypy: disable-error-code="empty-body"
# QUESTION: Sum of First N Natural Numbers
# Given a number N, find the sum of the first N natural numbers (1 + 2 + ... + N).
# Example 1:
# Input: N = 5
# Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15
# Constraints:
# 1 <= N <= 100000

"""
#Brute Force:
1. Parameterised recursion: carry a running accumulator.
2. sum(n, acc): if n < 1 return acc, else recurse sum(n-1, acc+n).
TC -> O(n), SC -> O(n) recursion stack

#Better Approach:
1. Functional recursion: sum(n) = n + sum(n-1), base case sum(0) = 0.
TC -> O(n), SC -> O(n) recursion stack

#Optimal Approach:
1. Closed-form formula: sum = n * (n + 1) / 2.
TC -> O(1), SC -> O(1)

#KEY INSIGHT:
- The sum of an arithmetic series has a constant-time formula; recursion is only for
  practising the recursive mindset.
"""


class Solution:
    def sumN_brute(self, n: int, acc: int) -> int:
        if n < 1:
            return acc
        return self.sumN_brute(n - 1, acc + n)

    def sumN_better(self, n: int) -> int:
        if n <= 0:
            return 0
        return n + self.sumN_better(n - 1)

    def sumN_optimal(self, n: int) -> int:
        return n * (n + 1) // 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumN_optimal(5))
