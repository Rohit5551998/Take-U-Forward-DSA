# mypy: disable-error-code="empty-body"
# QUESTION: Palindrome Number
# Given an integer n, return True if n is a palindrome and False otherwise. A
# number is a palindrome when it reads the same backward as forward. Negative
# numbers are never palindromes (the leading minus sign has no trailing match).
#
# Example 1:
# Input: n = 121
# Output: True
#
# Example 2:
# Input: n = -121
# Output: False
# Explanation: reads 121- from right to left, so it is not a palindrome.
#
# Example 3:
# Input: n = 10
# Output: False
# Explanation: reads 01 from right to left, so it is not a palindrome.


"""
#Brute Force:
SKIPPED — confirming a palindrome needs a single reversal pass over the digits;
there is no cruder or distinct sub-approach.

#Better Approach:
SKIPPED — no intermediate tier below the one-pass reverse-and-compare.

#Optimal Approach (palindrome_number_optimal):
1. Negatives are immediately not palindromes, so return False for n < 0.
2. Keep the original value, then reverse the whole number with the standard
   arithmetic loop: reversed = reversed * 10 + (n % 10), dropping digits via // 10.
3. n is a palindrome iff the fully reversed number equals the original.
TC -> O(log10(n)), SC -> O(1)

#KEY INSIGHT:
- Reversing the number arithmetically (reversed * 10 + digit) and comparing to
  the original decides palindromicity in one pass with O(1) space — no string
  conversion or two-pointer buffer required.
"""


class Solution:
    def palindrome_number_brute(self, n: int) -> bool:
        # SKIP: no cruder tier — a single reversal pass settles it.
        pass

    def palindrome_number_better(self, n: int) -> bool:
        # SKIP: no intermediate tier below the one-pass reverse-and-compare.
        pass

    def palindrome_number_optimal(self, n: int) -> bool:
        if n < 0:
            return False
        original = n
        reversed_number = 0
        while n > 0:
            reversed_number = reversed_number * 10 + n % 10
            n = n // 10
        return reversed_number == original


if __name__ == "__main__":
    sol = Solution()
    print(sol.palindrome_number_optimal(121))
    print(sol.palindrome_number_optimal(-121))
    print(sol.palindrome_number_optimal(10))
