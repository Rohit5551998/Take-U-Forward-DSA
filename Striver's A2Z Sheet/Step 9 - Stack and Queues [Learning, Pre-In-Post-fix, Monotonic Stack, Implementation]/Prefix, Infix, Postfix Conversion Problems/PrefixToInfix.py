# mypy: disable-error-code="empty-body"
# QUESTION: Prefix to Infix Conversion
# Convert a prefix (Polish) expression to a fully parenthesised infix
# expression.
# Example 1:
# Input: s = "*+PQ-MN"
# Output: "((P+Q)*(M-N))"
# Explanation: Scanning right to left, each operator combines the two most
# recent operands into a parenthesised infix sub-expression.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.

"""
#Optimal Approach:
1. Scan the prefix string right to left. Push operands onto a stack of strings.
2. On an operator pop the top two operands t1 (left) and t2 (right) and push
   "(" + t1 + op + t2 + ")".
3. The single remaining stack entry is the infix expression.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- In prefix the operator precedes its operands, so scanning from the right makes
  the two operands available on top of the stack exactly when the operator is
  read.
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
                stack.append("(" + t1 + char + t2 + ")")
        return stack.pop()


if __name__ == "__main__":
    print(Solution().findSolution("*+PQ-MN"))
