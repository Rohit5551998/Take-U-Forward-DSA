# mypy: disable-error-code="empty-body"
# QUESTION: Postfix to Infix Conversion
# Convert a postfix (Reverse Polish) expression to a fully parenthesised infix
# expression.
# Example 1:
# Input: s = "AB-DE+F*/"
# Output: "((A-B)/((D+E)*F))"
# Explanation: Each operator combines the two most recent operands into a
# parenthesised infix sub-expression.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.

"""
#Optimal Approach:
1. Scan left to right. Push operands onto a stack of expression strings.
2. On an operator pop the top two operands t1 (right) and t2 (left) and push the
   string "(" + t2 + op + t1 + ")".
3. The single remaining stack entry is the infix expression.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- In postfix the operator applies to the two nearest preceding operands, which
  are exactly the top two stack entries, so a stack rebuilds the tree bottom-up.
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
                stack.append("(" + t2 + char + t1 + ")")
        return stack.pop()


if __name__ == "__main__":
    print(Solution().findSolution("AB-DE+F*/"))
