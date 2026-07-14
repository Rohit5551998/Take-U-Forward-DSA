# mypy: disable-error-code="empty-body"
# QUESTION: Valid Parenthesis String
# Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid. A string is valid if:
#   - Every '(' has a corresponding ')'.
#   - Every ')' has a corresponding '('.
#   - '(' must go before its matching ')'.
#   - '*' can be treated as a single '(', a single ')', or an empty string "".
#
# Example 1:
# Input: s = "(*)"
# Output: true
# Explanation: Treat '*' as an empty string, leaving "()", which is valid.
#
# Constraints:
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'

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
    def valid_parenthesis_string_brute(self, s: str) -> bool:
        pass

    def valid_parenthesis_string_better(self, s: str) -> bool:
        pass

    def valid_parenthesis_string_optimal(self, s: str) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.valid_parenthesis_string_optimal("(*)"))
