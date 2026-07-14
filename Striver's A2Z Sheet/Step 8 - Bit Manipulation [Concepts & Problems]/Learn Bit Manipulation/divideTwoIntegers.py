# mypy: disable-error-code="empty-body"
# QUESTION: Divide two integers without using multiplication, division and mod
# Given two integers dividend and divisor, divide them without using multiplication,
# division, or the modulo operator, and return the quotient (truncated toward zero).
# If the result overflows a signed 32-bit integer, clamp it to the 32-bit range
# [-2^31, 2^31 - 1].
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10 / 3 = 3.33..., truncated toward zero gives 3.
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7 / -3 = -2.33..., truncated toward zero gives -2.
# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""


class Solution:
    def divide_brute(self, dividend: int, divisor: int) -> int:
        pass

    def divide_better(self, dividend: int, divisor: int) -> int:
        pass

    def divide_optimal(self, dividend: int, divisor: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.divide_optimal(10, 3))
