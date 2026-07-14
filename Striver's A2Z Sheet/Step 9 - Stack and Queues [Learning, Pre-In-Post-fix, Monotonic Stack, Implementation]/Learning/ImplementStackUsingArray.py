# mypy: disable-error-code="empty-body"
# QUESTION: Implement Stack using Array
# Implement a stack (LIFO) using a fixed-size array. Support push(x), pop(),
# top() and size() operations in O(1) time each.
# Example 1:
# Input: push(3), push(2), push(5), push(6), size(), pop(), size(), top()
# Output: 4, 6, 3, 5
# Explanation: After 4 pushes size is 4; pop() removes and returns the last
# pushed element 6; size becomes 3; top() peeks the new top 5.
# Constraints:
# 1 <= number of operations <= 10^5
# pop()/top() are called on a non-empty stack.

"""
#Optimal Approach:
1. Keep an array `arr` and an integer `top` initialised to -1 (empty).
2. push(x): increment `top`, write x at arr[top].
3. pop(): read arr[top], decrement `top`, return the value.
4. Top(): return arr[top] (the last element written).
5. Size(): return top + 1 (number of valid slots).
TC -> O(1) per op, SC -> O(N) for the backing array

#KEY INSIGHT:
- A single `top` index turns the array into LIFO: everything above `top`
  is garbage, everything at/below is the live stack, so all ops are O(1).
"""


class Solution:
    def __init__(self) -> None:
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size

    def push(self, x: int) -> None:
        if self.top + 1 < self.size:
            self.top += 1
            self.arr[self.top] = x

    def pop(self) -> int:
        if self.top != -1:
            element = self.arr[self.top]
            self.top -= 1
            return element
        return -1

    def Top(self) -> int:
        if self.top != -1:
            return self.arr[self.top]
        return -1

    def Size(self) -> int:
        return self.top + 1


if __name__ == "__main__":
    stack = Solution()
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(6)
    print(stack.Size())
    print(stack.pop())
    print(stack.Size())
    print(stack.Top())
