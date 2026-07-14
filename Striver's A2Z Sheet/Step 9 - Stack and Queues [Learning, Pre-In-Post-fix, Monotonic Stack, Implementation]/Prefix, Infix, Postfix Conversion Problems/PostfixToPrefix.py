# mypy: disable-error-code="empty-body"
# QUESTION: Postfix to Prefix Conversion
# Convert a postfix (Reverse Polish) expression to its prefix (Polish) form.
# Example 1:
# Input: s = "AB-DE+F*/"
# Output: "/-AB*+DEF"
# Explanation: Each operator is placed before its two operands as they are
# combined.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.

"""
#Optimal Approach:
1. Scan left to right. Push operands onto a stack of expression strings.
2. On an operator pop the top two operands t1 (right) and t2 (left) and push the
   string op + t2 + t1 (operator prefixed to the two operands).
3. The single remaining stack entry is the prefix expression.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Postfix already orders operands as (t2, t1); prepending the operator directly
  yields prefix, so a single stack pass converts between the two RPN forms.
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
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(char + t2 + t1)
        return stack.pop()


if __name__ == "__main__":
    print(Solution().findSolution("AB-DE+F*/"))
