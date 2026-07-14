# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 13 - Consecutive Number Triangle
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 5
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
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
2. Maintain a running counter across rows; each cell prints and increments it.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Maintain a running counter across rows; each cell prints and increments it.
"""


class Solution:
    def printPattern_brute(self, n: int) -> None:
        # SKIP: pattern printing has one direct construction, no distinct brute tier.
        pass

    def printPattern_better(self, n: int) -> None:
        # SKIP: no intermediate approach exists for pattern printing.
        pass

    def printPattern_optimal(self, n: int) -> None:
        num = 1
        for i in range(1, n + 1):
            for _ in range(i):
                print(num, end=" ")
                num += 1
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
