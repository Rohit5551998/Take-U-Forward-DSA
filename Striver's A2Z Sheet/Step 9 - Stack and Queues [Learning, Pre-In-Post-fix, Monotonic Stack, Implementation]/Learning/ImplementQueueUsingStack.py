# mypy: disable-error-code="empty-body"
# QUESTION: Implement Queue using Stack
# Implement a FIFO queue using two stacks. Support push(x) (enqueue),
# pop() (dequeue), top() (front) and size().
# Example 1:
# Input: push(3), push(2), push(5), push(6), size(), pop(), size(), top()
# Output: 4, 3, 3, 2
# Explanation: FIFO -> pop() returns the first pushed 3; new front is 2.
# Constraints:
# 1 <= number of operations <= 10^5

"""
#Brute Force:
1. push(x): move everything from `input` to `output`, push x onto `input`,
   then move everything back. This keeps `input` ordered so the oldest element
   sits on top, giving O(1) pop/top.
TC -> push O(N), pop/top/size O(1); SC -> O(N)

#Optimal Approach:
SKIPPED — a two-stack amortised O(1) variant exists, but the user's chosen
implementation is the costly-push variant above; only that approach is present.

#KEY INSIGHT:
- Reversing the stack order on every push places the oldest element on top,
  so the LIFO `input` stack dequeues in FIFO order.
"""

import sys
from queue import LifoQueue


class Solution:
    def __init__(self) -> None:
        self.input: LifoQueue = LifoQueue()
        self.output: LifoQueue = LifoQueue()

    def push(self, x: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
        self.input.put(x)
        while not self.output.empty():
            self.input.put(self.output.get())

    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            sys.exit(0)
        return int(self.input.get())

    def Top(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            sys.exit(0)
        return int(self.input.queue[-1])

    def Size(self) -> int:
        return self.input.qsize()


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
