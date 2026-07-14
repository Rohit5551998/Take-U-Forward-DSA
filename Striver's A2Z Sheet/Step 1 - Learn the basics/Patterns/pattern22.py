# mypy: disable-error-code="empty-body"
# QUESTION: Pattern 22 - Concentric Square Numbers
# Print the pattern shown below for a given integer n (n = number of rows / size).
# Example 1:
# Input: n = 3
# Output:
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
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
2. For a (2n-1)x(2n-1) grid each cell = n - min(distance to any of the 4 edges).
TC -> O(n^2), SC -> O(1)

#KEY INSIGHT:
- For a (2n-1)x(2n-1) grid each cell = n - min(distance to any of the 4 edges).
"""


class Solution:
    def printPattern_brute(self, n: int) -> None:
        # SKIP: pattern printing has one direct construction, no distinct brute tier.
        pass

    def printPattern_better(self, n: int) -> None:
        # SKIP: no intermediate approach exists for pattern printing.
        pass

    def printPattern_optimal(self, n: int) -> None:
        size = 2 * n - 1
        for i in range(size):
            for j in range(size):
                top = i
                left = j
                right = size - 1 - j
                bottom = size - 1 - i
                print(n - min(top, left, right, bottom), end=" ")
            print()


if __name__ == "__main__":
    sol = Solution()
    sol.printPattern_optimal(4)
