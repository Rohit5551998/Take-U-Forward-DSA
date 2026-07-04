# mypy: disable-error-code="empty-body"
# QUESTION: Implement ATOI/STRSTR
# Implement the function myAtoi(s) which converts the given string s to
# a 32-bit signed integer (similar to the C/C++ atoi function).
# Steps to implement:
#   1. Ignore any leading whitespace characters ' '.
#   2. Check for a sign: '+' or '-'. If neither, assume positive.
#   3. Read in the digits until a non-digit character or the end of the
#      string is reached. The rest of the string is ignored.
#   4. Convert the digits into an integer. If no digits were read, the
#      integer is 0.
#   5. If the integer is out of the 32-bit signed integer range
#      [-2^31, 2^31 - 1], clamp it: integers less than -2^31 should be
#      clamped to -2^31, and integers greater than 2^31 - 1 should be
#      clamped to 2^31 - 1.
#   6. Return the resulting integer.
#
# Examples:
# Example 1:
# Input: s = "42"            -> Output: 42
# Example 2:
# Input: s = "   -42"        -> Output: -42
# Example 3:
# Input: s = "4193 with words" -> Output: 4193
# Example 4:
# Input: s = "words and 987" -> Output: 0
# Example 5:
# Input: s = "-91283472332"  -> Output: -2147483648 (clamped to INT_MIN)
#
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters, digits, ' ', '+', '-', and '.'.
#
# Note: The Striver sheet pairs this with STRSTR (substring search).


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
    def implement_atoi_strstr_brute(self, s: str) -> int:
        pass

    def implement_atoi_strstr_better(self, s: str) -> int:
        pass

    def implement_atoi_strstr_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "42"
    print(sol.implement_atoi_strstr_optimal(s))
