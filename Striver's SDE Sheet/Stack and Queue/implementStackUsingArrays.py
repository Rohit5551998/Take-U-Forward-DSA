# mypy: disable-error-code="empty-body"
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
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""


class MyStack:
    def __init__(self) -> None:
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass


if __name__ == "__main__":
    st = MyStack()
    st.push(5)
    st.push(10)
    print(st.pop())
    print(st.top())
    print(st.is_empty())
