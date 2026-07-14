# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 9 - Diamond Star Pattern
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 3
# Output:
#   *
#  ***
# *****
# *****
#  ***
#   *
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
2. Concatenate an upright pyramid (pattern 7) with an inverted pyramid (pattern 8).
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Concatenate an upright pyramid (pattern 7) with an inverted pyramid (pattern 8).
"""


class Solution:
    def printPattern_brute(self, n: int) -> None:
        # SKIP: pattern printing has one direct construction, no distinct brute tier.
        pass

    def printPattern_better(self, n: int) -> None:
        # SKIP: no intermediate approach exists for pattern printing.
        pass

    def printPattern_optimal(self, n: int) -> None:
        for i in range(n):
            for _ in range(n - i - 1):
                print(" ", end="")
            for _ in range(2 * i + 1):
                print("*", end="")
            print()
        for i in range(n):
            for _ in range(i):
                print(" ", end="")
            for _ in range(2 * (n - i) - 1):
                print("*", end="")
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
