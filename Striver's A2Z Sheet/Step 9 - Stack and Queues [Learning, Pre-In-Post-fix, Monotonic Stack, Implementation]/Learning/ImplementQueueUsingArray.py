# mypy: disable-error-code="empty-body"
# QUESTION: Implement Queue using Array
# Implement a queue (FIFO) using a fixed-size array treated as a circular
# buffer. Support push(x) (enqueue), pop() (dequeue), top() (front) and size()
# in O(1) time each.
# Example 1:
# Input: push(3), push(2), push(5), push(6), size(), pop(), size(), top()
# Output: 4, 3, 3, 2
# Explanation: FIFO order -> pop() returns the first pushed element 3; the new
# front is 2.
# Constraints:
# 1 <= number of operations <= 10^5
# The queue never exceeds its fixed capacity.

"""
#Optimal Approach:
1. Keep `arr`, a `start` (front) index, an `end` (rear) index and `currSize`.
2. push(x): advance `end` circularly ((end+1) % maxSize), store x, ++currSize.
   The first push sets both start and end to 0.
3. pop(): read arr[start], advance `start` circularly, --currSize. When the
   queue empties reset start=end=-1.
4. Top(): return arr[start].
5. Size(): return currSize.
TC -> O(1) per op, SC -> O(N) for the backing array

#KEY INSIGHT:
- Wrapping start/end with modulo turns a plain array into a circular buffer,
  so freed front slots get reused and every op stays O(1) with no shifting.
"""

import sys


class Solution:
    def __init__(self) -> None:
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize

    def push(self, x: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            sys.exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.currSize += 1
        self.arr[self.end] = x

    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
            sys.exit(1)
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped

    def Top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            sys.exit(1)
        return self.arr[self.start]

    def Size(self) -> int:
        return self.currSize


if __name__ == "__main__":
    q = Solution()
    q.push(3)
    q.push(2)
    q.push(5)
    q.push(6)
    print(q.Size())
    print(q.pop())
    print(q.Size())
    print(q.Top())
