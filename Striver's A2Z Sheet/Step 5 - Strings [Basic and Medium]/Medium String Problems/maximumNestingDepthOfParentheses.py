# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Nesting Depth of the Parentheses
# A string is a valid parentheses string (VPS) if it meets one of: it is empty, it
# can be written as AB (A concatenated with B) where A and B are VPS, or it can be
# written as (A) where A is a VPS. The nesting depth depth(S) is defined as: 0 for
# an empty string, max(depth(A), depth(B)) for AB, and 1 + depth(A) for (A). Given
# a VPS represented as string s, return the nesting depth of s.
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside 3 nested parentheses in the string.
# Constraints:
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that s is a VPS.

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
    def maxDepth_brute(self, s: str) -> int:
        pass

    def maxDepth_better(self, s: str) -> int:
        pass

    def maxDepth_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.maxDepth_optimal("(1+(2*3)+((8)/4))+1"))
