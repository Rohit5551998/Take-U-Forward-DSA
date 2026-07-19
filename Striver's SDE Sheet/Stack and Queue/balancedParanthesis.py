# mypy: disable-error-code="empty-body"
# QUESTION: Balanced Paranthesis
# Given a string str containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid. The input string
# is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
# Return true if the string is balanced, false otherwise.
#
# Examples:
# Example 1:
# Input: str = "()"
# Output: true
#
# Example 2:
# Input: str = "()[]{}"
# Output: true
#
# Example 3:
# Input: str = "(]"
# Output: false
#
# Example 4:
# Input: str = "([)]"
# Output: false
#
# Example 5:
# Input: str = "{[]}"
# Output: true
#
# Constraints:
# 1 <= str.length <= 10^4
# str consists of parentheses only '()[]{}'


"""
#Brute Force:
SKIPPED — there is no slower-but-simpler tier that still respects nesting
order. Any correct check must match each close against the MOST RECENT unmatched
open, which is inherently a stack (LIFO); repeatedly scanning/removing adjacent
"()" pairs is just the same stack idea done in O(n^2). So the problem starts at
the optimal one-pass stack.

#Better Approach:
SKIPPED — same reason; no meaningful middle tier between a naive pair-removal
scan and the O(n) stack.

#Optimal Approach:
1. Use a stack to remember the OPEN brackets seen so far, in order. The core
   rule of nesting is LIFO: whatever opened most recently must be the first to
   close. A stack is exactly the structure that returns the most-recent item.
2. Keep a map `pairs` from each CLOSING bracket to its matching OPENING bracket
   ( ) -> ( , ] -> [ , } -> { ). This lets a close instantly name the opener it
   requires.
3. Scan the string left to right. If the char is an opening bracket, push it —
   it's an obligation to be closed later.
4. If the char is a closing bracket, it must cancel the top of the stack. First
   guard: if the stack is EMPTY, there is no opener to match -> not balanced,
   stop. (This is the check that must run BEFORE popping — popping an empty
   stack is invalid.)
5. Otherwise pop the top opener and compare it to pairs[char]. If it isn't the
   expected opener (e.g. top is '(' but we see ']'), the nesting is wrong ->
   not balanced, stop. Example: "([)]" fails here because ')' pops '[', mismatch.
6. After the scan, the stack must be EMPTY. Anything left means there are opens
   that were never closed (e.g. "(()"), so mark not balanced.
TC -> O(n) single pass, SC -> O(n) worst case (all opens on the stack)

#KEY INSIGHT:
- Bracket matching IS a stack problem: a close is only valid against the most
  recently opened bracket. Push opens, and on each close pop-and-compare — but
  always check the stack is non-empty first, and require it to end empty.
"""

from queue import LifoQueue


class Solution:
    def balanced_paranthesis_brute(self, s: str) -> bool:
        # SKIP: no simpler tier — correct matching requires LIFO order, which is
        # inherently the stack approach; a naive pair-removal scan is just the
        # same idea in O(n^2), not a distinct method.
        pass

    def balanced_paranthesis_better(self, s: str) -> bool:
        # SKIP: no meaningful middle tier between a naive pair-removal scan and
        # the O(n) stack.
        pass

    def balanced_paranthesis_optimal(self, s: str) -> bool:
        ans = True
        st: LifoQueue[str] = LifoQueue()
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in ["(", "[", "{"]:
                st.put(char)
            else:
                if st.empty() or st.get() != pairs[char]:
                    ans = False
                    break

        if not st.empty():
            ans = False

        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print(sol.balanced_paranthesis_optimal(s))
