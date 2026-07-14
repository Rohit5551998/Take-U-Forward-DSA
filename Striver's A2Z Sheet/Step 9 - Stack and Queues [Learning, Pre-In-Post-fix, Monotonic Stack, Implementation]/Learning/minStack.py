# mypy: disable-error-code="empty-body"
# QUESTION: Min Stack
# Design a stack that supports push, pop, top and retrieving the minimum
# element, all in O(1) time.
# Example 1:
# Input: push(16), push(13), push(15), push(14), getMin(), pop(), top(), getMin()
# Output: 13, 14, 15, 13
# Explanation: After the pushes the minimum is 13; pop() removes 14; top() is 15;
# the minimum is still 13.
# Constraints:
# -2^31 <= val <= 2^31 - 1
# pop/top/getMin operate on a non-empty stack.

"""
#Brute Force:
1. Store pairs (value, running_min) on the stack. On push, the pair's min is
   min(current value, previous pair's min). getMin() reads the top pair's min.
TC -> O(1) per op, SC -> O(2N) (two values per element)

#Optimal Approach:
1. Store a single encoded number per element plus a `mini` variable, SC O(N).
2. push(x): if x < mini store the encoded value 2*x - mini and set mini = x,
   else store x. The encoded value is always < the real value, marking a
   "new minimum" node.
3. pop(): if the stored value < mini it was an encoded min-node; the real popped
   value is the old mini and the previous mini is restored as 2*mini - stored.
4. Top(): if stored top < mini the true top is mini, else the stored value.
5. getMin(): return mini.
TC -> O(1) per op, SC -> O(N)

#KEY INSIGHT:
- Encoding 2*x - mini stores the previous minimum implicitly inside the pushed
  value, so a single variable + single stack recovers the min in O(1) with no
  auxiliary min-stack.
"""

import math


class Solution:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.mini: float = math.inf

    def push(self, x: int) -> None:
        if not self.stack:
            self.mini = x
            self.stack.append(x)
        elif x < self.mini:
            self.stack.append(int(2 * x - self.mini))
            self.mini = x
        else:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        ele = self.stack.pop()
        if ele < self.mini:
            val = int(self.mini)
            self.mini = 2 * self.mini - ele
            return val
        return ele

    def Top(self) -> int:
        if not self.stack:
            return -1
        ele = self.stack[-1]
        if ele < self.mini:
            return int(self.mini)
        return ele

    def getMin(self) -> int:
        return int(self.mini)


if __name__ == "__main__":
    stack = Solution()
    stack.push(16)
    stack.push(13)
    stack.push(15)
    stack.push(14)
    print(stack.getMin())
    print(stack.pop())
    print(stack.Top())
    print(stack.getMin())
