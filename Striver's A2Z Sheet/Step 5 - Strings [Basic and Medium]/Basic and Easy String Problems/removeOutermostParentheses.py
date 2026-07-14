# mypy: disable-error-code="empty-body"
# QUESTION: Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A
# and B are valid parentheses strings, and + represents string concatenation.
# A valid parentheses string s is primitive if it is nonempty, and there does not
# exist a way to split it into s = A + B, with A and B nonempty valid parentheses
# strings. Given a valid parentheses string s, consider its primitive
# decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses
# strings. Return s after removing the outermost parentheses of every primitive
# string in the primitive decomposition of s.
# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: The input string is "(()())(())", with primitive decomposition
# "(()())" + "(())". After removing outer parentheses of each part, this is
# "()()" + "()" = "()()()".
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

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
    def removeOuterParentheses_brute(self, s: str) -> str:
        pass

    def removeOuterParentheses_better(self, s: str) -> str:
        pass

    def removeOuterParentheses_optimal(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.removeOuterParentheses_optimal("(()())(())"))
