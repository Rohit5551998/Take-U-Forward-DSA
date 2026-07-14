# mypy: disable-error-code="empty-body"
# QUESTION: Armstrong Number
# You are given a 3-digit number n. Determine whether it is an Armstrong number.
# An Armstrong number of three digits is one where the sum of the cubes of its
# digits equals the number itself (e.g. 371 = 3^3 + 7^3 + 1^3).
# Return True if n is an Armstrong number, else False.
#
# Example 1:
# Input: n = 371
# Output: True
# Explanation: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371.
#
# Example 2:
# Input: n = 340
# Output: False
# Explanation: 3^3 + 4^3 + 0^3 = 27 + 64 + 0 = 91, which is not 340.


"""
#Brute Force:
SKIPPED — checking the Armstrong property requires reading each digit exactly
once; there is no cruder or distinct sub-approach below a single digit-sum pass.

#Better Approach:
SKIPPED — no intermediate tier; the one-pass digit-cube sum below is already the
simplest correct method.

#Optimal Approach (armstrong_number_optimal):
1. Remember the original value so we can compare against it after we destroy n.
2. Peel the last digit with n % 10, cube it, and add it to a running total.
3. Drop that digit with integer division n // 10, looping until n becomes 0.
4. n is an Armstrong number iff the accumulated cube-sum equals the original n.
TC -> O(log10(n)) (one step per digit), SC -> O(1)

#KEY INSIGHT:
- A digit-extraction loop (% 10 to read a digit, // 10 to drop it) walks a
  number's digits in O(#digits); summing their cubes and comparing to the
  original value is the whole check — no strings or extra storage needed.
"""


class Solution:
    def armstrong_number_brute(self, n: int) -> bool:
        # SKIP: no cruder tier — the property needs a single pass over the digits.
        pass

    def armstrong_number_better(self, n: int) -> bool:
        # SKIP: no intermediate tier between brute and the one-pass digit-cube sum.
        pass

    def armstrong_number_optimal(self, n: int) -> bool:
        original = n
        total = 0
        while n > 0:
            last = n % 10
            total += last**3
            n = n // 10
        return total == original


if __name__ == "__main__":
    sol = Solution()
    print(sol.armstrong_number_optimal(371))
    print(sol.armstrong_number_optimal(340))
