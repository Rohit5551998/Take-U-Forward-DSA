# mypy: disable-error-code="empty-body"
# QUESTION: Recursive Implementation of atoi()
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer, using recursion (mimicking the C/C++ atoi function).
# The algorithm: skip leading whitespace, read an optional +/- sign, then read
# in the digits until a non-digit character or the end of input is reached,
# clamping the result to the 32-bit signed integer range.
# Example 1:
# Input: s = "42"
# Output: 42
# Example 2:
# Input: s = "   -042"
# Output: -42
# Explanation: Leading whitespace and zeros are ignored; sign is applied.
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower/upper), digits, '.', '+', '-', ' '.
# Result must be clamped to [-2^31, 2^31 - 1].

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
    def my_atoi_brute(self, s: str) -> int:
        pass

    def my_atoi_better(self, s: str) -> int:
        pass

    def my_atoi_optimal(self, s: str) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.my_atoi_optimal("   -042"))
