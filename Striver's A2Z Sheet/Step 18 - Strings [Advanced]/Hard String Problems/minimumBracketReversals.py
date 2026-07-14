# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Number of Bracket Reversals to Balance an Expression
# Given an expression consisting only of the characters '{' and '}', find the
# minimum number of bracket reversals required to make the expression balanced.
# A reversal means changing a '{' to '}' or a '}' to '{'. If the expression
# cannot be balanced (its length is odd), return -1.
# Example 1:
# Input: s = "}{{}}{{{"
# Output: 3
# Explanation: One way to balance in 3 reversals is "{{{}}{}}".
# Example 2:
# Input: s = "{{{{"
# Output: 2
# Explanation: Reversing two of them gives "{{}}".
# Constraints:
# 1 <= s.length <= 10^5
# s consists only of the characters '{' and '}'.

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
    def min_bracket_reversals_brute(self, s: str) -> int:
        pass

    def min_bracket_reversals_better(self, s: str) -> int:
        pass

    def min_bracket_reversals_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.min_bracket_reversals_optimal("}{{}}{{{"))
