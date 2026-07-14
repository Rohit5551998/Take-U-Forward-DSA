# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 11 - Binary Number Triangle
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 5
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
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
2. Rows starting on an odd length begin with 1, even with 0; values alternate.
   Start = 1 if i is odd.
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- Rows starting on an odd length begin with 1, even with 0; values alternate. Start = 1 if i is odd.
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
            start = 1 if i % 2 == 1 else 0
            for _ in range(i):
                print(start, end=" ")
                start = 1 - start
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
