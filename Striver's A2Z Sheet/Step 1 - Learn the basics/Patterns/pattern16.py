# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 16 - Repeated Alphabet Triangle
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 5
# Output:
# A
# B B
# C C C
# D D D D
# E E E E E
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
2. Row i repeats the single letter A+i, i+1 times (like pattern 4 but with letters).
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Row i repeats the single letter A+i, i+1 times (like pattern 4 but with letters).
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
            ch = chr(ord("A") + i)
            for _ in range(i + 1):
                print(ch, end=" ")
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
