# mypy: disable-error-code="empty-body"
# QUESTION: String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer. The algorithm: (1) skip leading whitespace; (2) read an optional
# '+' or '-' sign; (3) read in the digits until a non-digit character or end of
# input, ignoring the rest; (4) convert the digits into an integer; if no digits
# were read the result is 0. If the integer is out of the 32-bit signed range
# [-2^31, 2^31 - 1], clamp it to the range. Return the resulting integer.
# Example 1:
# Input: s = "   -042"
# Output: -42
# Explanation: Leading spaces skipped, sign '-' read, "042" parsed as 42 -> -42.
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower/upper), digits, ' ', '+', '-', and '.'.

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
    def myAtoi_brute(self, s: str) -> int:
        pass

    def myAtoi_better(self, s: str) -> int:
        pass

    def myAtoi_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.myAtoi_optimal("   -042"))
