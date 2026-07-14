# mypy: disable-error-code="empty-body"
# QUESTION: Reverse Integer
# Given a signed 32-bit integer n, return n with its digits reversed. If
# reversing n takes the value outside the signed 32-bit range [-2^31, 2^31 - 1],
# return 0. Assume 64-bit integers are not available to store the result.
#
# Example 1:
# Input: n = 123
# Output: 321
#
# Example 2:
# Input: n = -123
# Output: -321
#
# Example 3:
# Input: n = 120
# Output: 21
#
# Example 4:
# Input: n = 1534236469
# Output: 0
# Explanation: the reversed value 9646324351 overflows the 32-bit range.


"""
#Brute Force:
SKIPPED — reversing a number is inherently a single digit-by-digit pass; there is
no cruder or distinct sub-approach.

#Better Approach:
SKIPPED — no intermediate tier below the one-pass digit reversal.

#Optimal Approach (reverse_integer_optimal):
1. Record the sign, then work with the absolute value so the digit loop is
   uniform for positive and negative inputs.
2. Peel digits with % 10 and rebuild the reversed value as
   reversed = reversed * 10 + lastDigit, dropping each digit with // 10.
3. Re-apply the sign to the reversed magnitude.
4. Clamp to 0 if the result falls outside [-2^31, 2^31 - 1], honoring the 32-bit
   overflow rule.
TC -> O(log10(n)), SC -> O(1)

#KEY INSIGHT:
- Building the reverse with reversed * 10 + digit while stripping digits via
  % 10 / // 10 reverses a number in one linear pass; a final range check enforces
  the 32-bit overflow contract.
"""


class Solution:
    def reverse_integer_brute(self, n: int) -> int:
        # SKIP: reversing digits is a single pass — no cruder distinct tier.
        pass

    def reverse_integer_better(self, n: int) -> int:
        # SKIP: no intermediate tier below the one-pass digit reversal.
        pass

    def reverse_integer_optimal(self, n: int) -> int:
        reversed_number = 0
        negative = n < 0
        n = abs(n)
        while n > 0:
            last = n % 10
            reversed_number = reversed_number * 10 + last
            n = n // 10
        if negative:
            reversed_number = -reversed_number
        if reversed_number < -(2**31) or reversed_number > 2**31 - 1:
            reversed_number = 0
        return reversed_number


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse_integer_optimal(123))
    print(sol.reverse_integer_optimal(-123))
    print(sol.reverse_integer_optimal(1534236469))
