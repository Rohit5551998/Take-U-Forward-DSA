# mypy: disable-error-code="empty-body"
# QUESTION: Prefix to Postfix Conversion
# Convert a prefix (Polish) expression to its postfix (Reverse Polish) form.
# Example 1:
# Input: s = "/-AB*+DEF"
# Output: "AB-DE+F*/"
# Explanation: Scanning right to left, each operator is appended after its two
# operands.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.

"""
#Optimal Approach:
1. Scan the prefix string right to left. Push operands onto a stack of strings.
2. On an operator pop the top two operands t1 (left) and t2 (right) and push
   t1 + t2 + op (operands first, operator last).
3. The single remaining stack entry is the postfix expression.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Both prefix and postfix are parenthesis-free RPN forms; scanning prefix from
  the right lets the stack reorder each operator after its operands in one pass.
"""


class Solution:
    def precedence(self, op: str) -> int:
        if op == "^":
            return 3
        if op in ("*", "/"):
            return 2
        if op in ("+", "-"):
            return 1
        return 0

    def findSolution(self, s: str) -> str:
        stack: list[str] = []
        for char in reversed(s):
            if char.isalnum():
                stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1 + t2 + char)
        return stack.pop()


if __name__ == "__main__":
    print(Solution().findSolution("/-AB*+DEF"))
