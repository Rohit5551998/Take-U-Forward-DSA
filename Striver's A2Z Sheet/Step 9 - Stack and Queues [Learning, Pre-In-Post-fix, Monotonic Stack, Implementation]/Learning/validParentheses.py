# mypy: disable-error-code="empty-body"
# QUESTION: Check for Balanced Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid. Brackets must close in the
# correct order and every opening bracket has a matching closing bracket.
# Example 1:
# Input: s = "()[{}()]"
# Output: true
# Explanation: Every bracket is closed by the matching type in the right order.
# Constraints:
# 1 <= s.length <= 10^4
# s consists only of '()[]{}'.

"""
#Optimal Approach:
1. Scan left to right with a stack. Push every opening bracket.
2. On a closing bracket, the stack must be non-empty and its top must be the
   matching opening bracket; otherwise the string is invalid.
3. After the scan the stack must be empty (no unmatched openers) to be valid.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- The most recently opened bracket must be the first to close (LIFO), which is
  exactly a stack: a mismatch or leftover opener means unbalanced.
"""


class Solution:
    def findSolution(self, s: str) -> bool:
        stack: list[str] = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack


if __name__ == "__main__":
    print(Solution().findSolution("()[{}()]"))
