# mypy: disable-error-code="empty-body"
# QUESTION: Infix to Prefix Conversion
# Convert an infix expression to its prefix (Polish) form.
# Example 1:
# Input: s = "x+y*z/w+u"
# Output: "++x/*yzwu"
# Explanation: Precedence and associativity are respected while producing the
# prefix ordering.
# Constraints:
# Operators: ^, *, /, +, -  ; operands are single alphanumeric characters.

"""
#Optimal Approach:
1. Reverse the infix string and swap '(' with ')' so we can process it like an
   infix-to-postfix pass from the (now) left.
2. Run infix-to-postfix on the transformed string, but treat associativity
   carefully: for '^' pop on <= precedence (right-associative), for all others
   pop only on strictly < precedence (left-associative when reversed).
3. Reverse the resulting postfix string to obtain the prefix expression.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Reversing + bracket-swapping converts the prefix problem into a postfix one;
  the precedence tie-breaking on '^' vs the rest preserves correct associativity
  after the final reversal.
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
        rev = []
        for ch in reversed(s):
            if ch == "(":
                rev.append(")")
            elif ch == ")":
                rev.append("(")
            else:
                rev.append(ch)

        stack: list[str] = []
        result = ""
        for char in rev:
            if char.isalnum():
                result += char
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            elif char == "^":
                while stack and self.precedence(char) <= self.precedence(stack[-1]):
                    result += stack.pop()
                stack.append(char)
            else:
                while stack and self.precedence(char) < self.precedence(stack[-1]):
                    result += stack.pop()
                stack.append(char)
        while stack:
            result += stack.pop()
        return result[::-1]


if __name__ == "__main__":
    print(Solution().findSolution("x+y*z/w+u"))
