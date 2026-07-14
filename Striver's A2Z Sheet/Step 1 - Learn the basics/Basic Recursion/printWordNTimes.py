# mypy: disable-error-code="empty-body"
# QUESTION: Print a Name N Times using Recursion
# Given an integer N, print a name (here "Hello") exactly N times using recursion.
# Example 1:
# Input: N = 3
# Output: Hello Hello Hello
# Constraints:
# 1 <= N <= 1000

"""
#Brute Force:
SKIPPED - recursion is the intended and only meaningful approach for this exercise;
an iterative loop is trivial and not tracked as a separate tier.

#Better Approach:
SKIPPED - no distinct intermediate approach.

#Optimal Approach:
1. Recurse with an index i starting at 1.
2. Base case: if i > n, stop.
3. Otherwise print the word once and recurse with i+1.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- Carry the counter as a parameter; each stack frame prints once and passes the next
  index down, giving exactly n prints.
"""


class Solution:
    def printName_brute(self, i: int, n: int) -> None:
        # SKIP: recursion is the intended approach; no separate brute tier.
        pass

    def printName_better(self, i: int, n: int) -> None:
        # SKIP: no distinct intermediate approach.
        pass

    def printName_optimal(self, i: int, n: int) -> None:
        if i > n:
            return
        print("Hello", end=" ")
        self.printName_optimal(i + 1, n)


if __name__ == "__main__":
    sol = Solution()
    sol.printName_optimal(1, 3)
