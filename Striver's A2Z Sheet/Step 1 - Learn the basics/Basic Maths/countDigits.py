# mypy: disable-error-code="empty-body"
# QUESTION: Count Digits
# Given a positive integer n, count how many of its digits divide n exactly
# (n % digit == 0). Digits equal to 0 are ignored (division by zero is
# undefined). Return the count of such digits.
#
# Example 1:
# Input: n = 12
# Output: 2
# Explanation: digits 1 and 2 both divide 12.
#
# Example 2:
# Input: n = 1012
# Output: 3
# Explanation: 1, 1 and 2 divide 1012; the 0 digit is skipped.
#
# Example 3:
# Input: n = 23
# Output: 0
# Explanation: neither 2 nor 3 divides 23.


"""
#Brute Force:
SKIPPED — every digit must be inspected once against n, so there is no cruder
distinct baseline below the single digit-extraction pass.

#Better Approach:
SKIPPED — no intermediate tier; one linear pass over the digits is already minimal.

#Optimal Approach (count_digits_optimal):
1. Keep the original n so each extracted digit can be tested for dividing it
   (the copy we loop on gets destroyed digit by digit).
2. Peel digits with n % 10; skip a digit of 0 (can't divide), otherwise check
   original % digit == 0 and count it when true.
3. Drop the processed digit with // 10 and repeat until n reaches 0.
TC -> O(log10(n)) (one step per digit), SC -> O(1)

#KEY INSIGHT:
- Digit extraction (% 10 to read, // 10 to advance) walks all digits in
  O(#digits); testing each against the ORIGINAL number (not the shrinking copy)
  counts the evenly-dividing digits in a single pass.
"""


class Solution:
    def count_digits_brute(self, n: int) -> int:
        # SKIP: no cruder tier — each digit must be checked once against n.
        pass

    def count_digits_better(self, n: int) -> int:
        # SKIP: no intermediate tier below the single digit pass.
        pass

    def count_digits_optimal(self, n: int) -> int:
        original = n
        count = 0
        while n > 0:
            last = n % 10
            if last != 0 and original % last == 0:
                count += 1
            n = n // 10
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_digits_optimal(12))
    print(sol.count_digits_optimal(1012))
    print(sol.count_digits_optimal(23))
