# mypy: disable-error-code="empty-body"
# QUESTION: Infix to Postfix Conversion
# Convert an infix expression (operators between operands, may contain
# parentheses) to its postfix (Reverse Polish) form.
# Example 1:
# Input: s = "a+b*(c^d-e)^(f+g*h)-i"
# Output: "abcd^e-fgh*+^*+i-"
# Explanation: Operator precedence and parentheses are respected while the
# operands keep their relative order.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.
# The expression is well-formed and fully parenthesised where needed.

"""
#Optimal Approach:
1. Scan left to right using an operator stack; append operands directly to the
   result (they keep their order in postfix).
2. On '(' push it. On ')' pop and append until the matching '(' is removed.
3. On an operator, pop and append while the stack top has greater-or-equal
   precedence, then push the current operator.
4. After the scan, pop and append any remaining operators.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- The stack delays lower-or-equal precedence operators so higher-precedence
  ones are emitted first, which is exactly postfix evaluation order.
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
        result = ""
        for char in s:
            if char.isalnum():
                result += char
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            else:
                while stack and self.precedence(char) <= self.precedence(stack[-1]):
                    result += stack.pop()
                stack.append(char)
        while stack:
            result += stack.pop()
        return result


if __name__ == "__main__":
    print(Solution().findSolution("a+b*(c^d-e)^(f+g*h)-i"))
