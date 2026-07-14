# mypy: disable-error-code="empty-body"
# QUESTION: Implement Stack using Linked List
# Implement a LIFO stack using a singly linked list. Support push(x), pop(),
# top(), size() and isEmpty(), all in O(1) time.
# Example 1:
# Input: push(16), push(15), push(14), push(13), size(), pop(), top()
# Output: 4, 13, 14
# Explanation: pop() removes the most recent 13; top() peeks 14.
# Constraints:
# 1 <= number of operations <= 10^5

"""
#Optimal Approach:
1. Keep a `top` pointer to the head of a singly linked list and a `size` count.
2. push(x): create a node, point its next at the current top, make it the top,
   size += 1 (insert at head).
3. pop(): read top's data, move top to top.next, size -= 1 (remove from head).
4. Top()/Size()/isEmpty(): read top.data / size / size == 0.
TC -> O(1) per op, SC -> O(N) for the nodes

#KEY INSIGHT:
- Inserting and removing only at the head of a linked list is O(1) and needs no
  pre-allocated capacity, so the stack grows/shrinks dynamically.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: "Optional[Node]" = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def __init__(self) -> None:
        self.top: Optional[Node] = None
        self.size = 0

    def push(self, data: int) -> None:
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self) -> int:
        if self.top is None:
            return -1
        popped = self.top
        self.top = self.top.next
        self.size -= 1
        return popped.data

    def Size(self) -> int:
        return self.size

    def Top(self) -> int:
        if self.top is None:
            return -1
        return self.top.data

    def isEmpty(self) -> bool:
        return self.size == 0


if __name__ == "__main__":
    stack = Solution()
    stack.push(16)
    stack.push(15)
    stack.push(14)
    stack.push(13)
    print(stack.Size())
    print(stack.pop())
    print(stack.Size())
    print(stack.Top())
    print(stack.isEmpty())
