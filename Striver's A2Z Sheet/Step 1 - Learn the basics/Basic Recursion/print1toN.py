# mypy: disable-error-code="empty-body"
# QUESTION: Print 1 to N using Recursion
# Given an integer N, print all integers from 1 to N in increasing order using recursion.
# Example 1:
# Input: N = 5
# Output: 1 2 3 4 5
# Constraints:
# 1 <= N <= 1000

"""
#Brute Force:
1. Forward recursion: recurse with index i starting at 1, print i, then recurse i+1 until i > n.
TC -> O(n), SC -> O(n) recursion stack

#Better Approach:
SKIPPED - no distinct intermediate approach between the two recursive styles.

#Optimal Approach:
1. Backtracking style: recurse first, print while unwinding.
2. Call with i = n. Base case i < 1 returns.
3. Recurse to i-1 first, then print i on the way back so 1 is printed first.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- Doing the print AFTER the recursive call (on the unwind) reverses the natural top-down
  order, letting us count up while recursing down.
"""


class Solution:
    def printNos_brute(self, i: int, n: int) -> None:
        if i > n:
            return
        print(i, end=" ")
        self.printNos_brute(i + 1, n)

    def printNos_better(self, i: int, n: int) -> None:
        # SKIP: no distinct intermediate approach.
        pass

    def printNos_optimal(self, i: int, n: int) -> None:
        if i < 1:
            return
        self.printNos_optimal(i - 1, n)
        print(i, end=" ")


if __name__ == "__main__":
    sol = Solution()
    sol.printNos_optimal(5, 5)
