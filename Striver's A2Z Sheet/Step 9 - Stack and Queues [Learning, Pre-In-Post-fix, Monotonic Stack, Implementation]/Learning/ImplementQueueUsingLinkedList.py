# mypy: disable-error-code="empty-body"
# QUESTION: Implement Queue using Linked List
# Implement a FIFO queue using a singly linked list with front and rear
# pointers. Support enqueue(x), dequeue(), peek(), size() and isEmpty() in O(1).
# Example 1:
# Input: enqueue(16), enqueue(15), enqueue(14), enqueue(13), size(), dequeue(), peek()
# Output: 4, 16, 15
# Explanation: FIFO -> dequeue() returns the oldest 16; peek() shows new front 15.
# Constraints:
# 1 <= number of operations <= 10^5

"""
#Optimal Approach:
1. Keep a `front` pointer (dequeue end) and a `rear` pointer (enqueue end).
2. enqueue(x): create a node; if empty set front=rear=node, else rear.next=node
   and move rear to it; size += 1.
3. dequeue(): read front.data, move front to front.next, size -= 1.
4. peek()/size()/isEmpty(): read front.data / size / size == 0.
TC -> O(1) per op, SC -> O(N) for the nodes

#KEY INSIGHT:
- Two pointers separate the two ends of the queue: adding at `rear` and removing
  at `front` are both O(1), so the FIFO order is maintained without shifting.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: "Optional[Node]" = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size = 0

    def enqueue(self, data: int) -> None:
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode  # type: ignore[union-attr]
            self.rear = newNode
        self.size += 1

    def dequeue(self) -> int:
        if self.front is None:
            return -1
        popped = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return popped.data

    def Size(self) -> int:
        return self.size

    def peek(self) -> int:
        if self.front is None:
            return -1
        return self.front.data

    def isEmpty(self) -> bool:
        return self.size == 0


if __name__ == "__main__":
    q = Solution()
    q.enqueue(16)
    q.enqueue(15)
    q.enqueue(14)
    q.enqueue(13)
    print(q.Size())
    print(q.dequeue())
    print(q.Size())
    print(q.peek())
    print(q.isEmpty())
