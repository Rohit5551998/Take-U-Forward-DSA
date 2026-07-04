# mypy: disable-error-code="empty-body"
# QUESTION: Implement Queue using Stack
# Implement a First-In-First-Out (FIFO) queue using two stacks. The implemented queue should
# support the following operations: push, pop, peek, and isEmpty.
# Implement the StackQueue class:
# - void push(int x): Adds element x to the end of the queue.
# - int pop(): Removes and returns the front element of the queue.
# - int peek(): Returns the front element of the queue without removing it.
# - boolean isEmpty(): Returns true if the queue is empty, false otherwise.
#
# Examples:
# Example 1:
# Input:
# ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
# [[], [4], [8], [], [], []]
# Output: [null, null, null, 4, 8, false]
# Explanation:
# StackQueue queue = new StackQueue();
# - queue.push(4);
# - queue.push(8);
# - queue.pop(); // returns 4
# - queue.peek(); // returns 8
# - queue.isEmpty(); // returns false
#
# Example 2:
# Input:
# ["StackQueue", "isEmpty"]
# [[]]
# Output: [null, true]
# Explanation:
# StackQueue queue = new StackQueue();
# - queue.isEmpty(); // returns true
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


class MyQueue:
    def __init__(self) -> None:
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(4)
    q.push(8)
    print(q.pop())
    print(q.peek())
    print(q.is_empty())
