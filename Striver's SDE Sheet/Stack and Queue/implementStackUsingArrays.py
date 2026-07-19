# QUESTION: Implement Stack using Arrays
# Implement a Last-In-First-Out (LIFO) stack using an array. The implemented stack should
# support the following operations: push, pop, top, and isEmpty.
# Implement the ArrayStack class:
# - void push(int x): Pushes element x onto the top of the stack.
# - int pop(): Removes and returns the top element of the stack.
# - int top(): Returns the top element of the stack without removing it.
# - boolean isEmpty(): Returns true if the stack is empty, false otherwise.
#
# Examples:
# Example 1:
# Input:
# ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
# [[], [5], [10], [], [], []]
# Output: [null, null, null, 10, 10, false]
# Explanation: ArrayStack stack = new ArrayStack();
# - stack.push(5);
# - stack.push(10);
# - stack.top(); // returns 10
# - stack.pop(); // returns 10
# - stack.isEmpty(); // returns false
#
# Example 2:
# Input:
# ["ArrayStack", "isEmpty", "push", "pop", "isEmpty"]
# [[], [], [1], [], []]
# Output: [null, true, null, 1, true]
# Explanation: ArrayStack stack = new ArrayStack();
# - stack.push(1);
# - stack.pop(); // returns 1
# - stack.isEmpty(); // returns true
#
# Constraints:
# - 1 <= number of calls made <= 100
# - 1 <= x <= 100


"""
#Implementation (implement-a-class — fixed-size array with a manual top index):
1. Pre-allocate a fixed-capacity array `stack` of `size` slots and keep an
   integer `top` that points at the index of the current top element. Start
   top = -1 to mean "empty" — there is no valid index below 0, so -1 is a clean
   sentinel for an empty stack. This mirrors a real C-style array stack where
   memory is reserved up front rather than growing dynamically.
2. push(x): first guard against overflow — only proceed if top + 1 < size, so
   we never write past the reserved array. Then advance top by 1 and write x
   into stack[top]. The new element becomes the top.
3. pop(): guard against underflow — if top == -1 the stack is empty, so return
   the sentinel -1. Otherwise read stack[top] as the value to return, then
   decrement top (logically removing it; the slot is left as stale data but is
   now unreachable, which is fine).
4. Top(): same as pop but without moving top — read stack[top] if non-empty,
   else return -1. Peek must not mutate the stack.
5. is_empty(): the stack is empty exactly when top == -1.
TC -> push/pop/Top/is_empty each O(1), SC -> O(size) for the pre-allocated array

#KEY INSIGHT:
- A single integer `top` index is all the bookkeeping a fixed array stack needs:
  top == -1 marks empty, top + 1 == size marks full, and every operation is a
  constant-time index read/write with an overflow/underflow guard.
"""


class MyStack:
    def __init__(self) -> None:
        self.top = -1
        self.size = 1000
        self.stack = [0] * self.size

    def push(self, x: int) -> None:
        if (self.top + 1) < self.size:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        element = -1
        if self.top != -1:
            element = self.stack[self.top]
            self.top -= 1
        return element

    def Top(self) -> int:
        element = -1
        if self.top != -1:
            element = self.stack[self.top]
        return element

    def is_empty(self) -> bool:
        return self.top == -1


if __name__ == "__main__":
    st = MyStack()
    st.push(5)
    st.push(10)
    print(st.pop())
    print(st.Top())
    print(st.is_empty())
