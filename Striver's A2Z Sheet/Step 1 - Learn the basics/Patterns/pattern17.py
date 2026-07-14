# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 17 - Alphabet Hill
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 5
# Output:
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
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
2. Centred hill: leading spaces (n-i-1), then letters rise A..A+i then fall back to A.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Centred hill: leading spaces (n-i-1), then letters rise A..A+i then fall back to A.
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
            ch = 0
            breakpoint_val = i
            for j in range(2 * i + 1):
                print(chr(ord("A") + ch), end="")
                if j < breakpoint_val:
                    ch += 1
                else:
                    ch -= 1
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
