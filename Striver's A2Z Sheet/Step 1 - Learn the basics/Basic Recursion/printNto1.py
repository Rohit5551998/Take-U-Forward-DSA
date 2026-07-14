# mypy: disable-error-code="empty-body"
# QUESTION: Print N to 1 using Recursion
# Given an integer N, print all integers from N down to 1 in decreasing order using recursion.
# Example 1:
# Input: N = 5
# Output: 5 4 3 2 1
# Constraints:
# 1 <= N <= 1000

"""
#Brute Force:
1. Forward recursion: recurse with index i starting at n, print i, then recurse i-1 until i < 1.
TC -> O(n), SC -> O(n) recursion stack

#Better Approach:
SKIPPED - no distinct intermediate approach between the two recursive styles.

#Optimal Approach:
1. Backtracking style: recurse first, print while unwinding.
2. Call with i = 1. Base case i > n returns.
3. Recurse to i+1 first, then print i on the way back so n is printed first.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- Printing AFTER the recursive call (on the unwind) flips the order: recursing up from 1
  to n prints n..1.
"""


class Solution:
    def printNos_brute(self, i: int, n: int) -> None:
        if i < 1:
            return
        print(i, end=" ")
        self.printNos_brute(i - 1, n)

    def printNos_better(self, i: int, n: int) -> None:
        # SKIP: no distinct intermediate approach.
        pass

    def printNos_optimal(self, i: int, n: int) -> None:
        if i > n:
            return
        self.printNos_optimal(i + 1, n)
        print(i, end=" ")


if __name__ == "__main__":
    sol = Solution()
    sol.printNos_optimal(1, 5)
