# mypy: disable-error-code="empty-body"
# QUESTION: Implement Stack using Queue
# Implement a LIFO stack using a single queue (FIFO). Support push(x), pop(),
# top() and size().
# Example 1:
# Input: push(3), push(2), push(5), push(6), size(), pop(), size(), top()
# Output: 4, 6, 3, 5
# Explanation: Stack order -> pop() returns the most recently pushed 6.
# Constraints:
# 1 <= number of operations <= 10^5

"""
#Optimal Approach:
1. Use one queue. push(x): enqueue x, then rotate the queue by dequeuing and
   re-enqueuing the previous s elements so x moves to the front.
2. After push, the front of the queue is always the "top" of the stack.
3. pop(): dequeue the front. Top(): peek the front. Size(): queue size.
TC -> push O(N), pop/top/size O(1); SC -> O(N)

#KEY INSIGHT:
- By rotating the queue on every push, the newest element is always at the
  front, so the FIFO queue behaves like a LIFO stack with O(1) pop.
"""

from queue import Queue


class Solution:
    def __init__(self) -> None:
        self.queue: Queue = Queue()

    def push(self, x: int) -> None:
        s = self.queue.qsize()
        self.queue.put(x)
        for _ in range(s):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        return int(self.queue.get())

    def Top(self) -> int:
        return int(self.queue.queue[0])

    def Size(self) -> int:
        return self.queue.qsize()


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
