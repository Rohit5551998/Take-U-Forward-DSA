# mypy: disable-error-code="empty-body"
# QUESTION: Balanced Paranthesis
# Given a string str containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid. The input string
# is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
# Return true if the string is balanced, false otherwise.
#
# Examples:
# Example 1:
# Input: str = "()"
# Output: true
#
# Example 2:
# Input: str = "()[]{}"
# Output: true
#
# Example 3:
# Input: str = "(]"
# Output: false
#
# Example 4:
# Input: str = "([)]"
# Output: false
#
# Example 5:
# Input: str = "{[]}"
# Output: true
#
# Constraints:
# 1 <= str.length <= 10^4
# str consists of parentheses only '()[]{}'


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
    def balanced_paranthesis_brute(self, s: str) -> bool:
        pass

    def balanced_paranthesis_better(self, s: str) -> bool:
        pass

    def balanced_paranthesis_optimal(self, s: str) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print(sol.balanced_paranthesis_optimal(s))
