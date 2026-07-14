# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 4 - Repeated Number Triangle
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 4
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# Constraints:
# 1 <= n <= 100


"""
#Brute Force:
SKIPPED - a pattern-printing problem has a single direct nested-loop construction;
there is no less-efficient prior attempt to record as a brute tier.

#Better Approach:
SKIPPED - no intermediate approach exists; the pattern is generated directly.

#Optimal Approach:
1. Iterate row by row; per row compute the counts of spaces/stars/values, then print them.
2. Every cell in row i holds the row number i, so print i (not j) in the inner loop.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Every cell in row i holds the row number i, so print i (not j) in the inner loop.
"""


class Solution:
    def printPattern_brute(self, n: int) -> None:
        # SKIP: pattern printing has one direct construction, no distinct brute tier.
        pass

    def printPattern_better(self, n: int) -> None:
        # SKIP: no intermediate approach exists for pattern printing.
        pass

    def printPattern_optimal(self, n: int) -> None:
        for i in range(1, n + 1):
            for _ in range(i):
                print(i, end=" ")
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
