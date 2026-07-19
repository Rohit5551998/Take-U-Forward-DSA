# QUESTION: Implement Stack using Queue (using single queue)
# Implement a Last-In-First-Out (LIFO) stack using a single queue. The implemented stack should
# support the following operations: push, pop, top, and isEmpty.
# Implement the QueueStack class:
# - void push(int x): Pushes element x onto the stack.
# - int pop(): Removes and returns the top element of the stack.
# - int top(): Returns the top element of the stack without removing it.
# - boolean isEmpty(): Returns true if the stack is empty, false otherwise.
#
# Examples:
# Example 1:
# Input:
# ["QueueStack", "push", "push", "pop", "top", "isEmpty"]
# [[], [4], [8], [], [], []]
# Output: [null, null, null, 8, 4, false]
# Explanation: QueueStack stack = new QueueStack();
# - stack.push(4);
# - stack.push(8);
# - stack.pop(); // returns 8
# - stack.top(); // returns 4
# - stack.isEmpty(); // returns false
#
# Example 2:
# Input:
# ["QueueStack", "isEmpty"]
# [[]]
# Output: [null, true]
# Explanation: QueueStack stack = new QueueStack();
# - stack.isEmpty(); // returns true
#
# Constraints:
# - 1 <= number of calls made <= 100
# - 1 <= x <= 100


"""
#Implementation (implement-a-class — SINGLE queue, push-costly):
1. Back the stack with one FIFO queue. A queue serves oldest-first, but a stack
   needs newest-first (LIFO). The trick: after every push, rotate the queue so
   the just-pushed element sits at the FRONT — then the queue's natural
   front-based get()/peek() behave exactly like a stack's top.
2. push(x): remember s = current size BEFORE inserting. Enqueue x at the back.
   Now x is last; to bring it to the front, dequeue-and-re-enqueue the s older
   elements exactly s times. Each old element cycles from front to back, leaving
   x at the front with the rest in their original relative order behind it.
   Example: [4,8] (front=4), push 2 -> put -> [4,8,2], rotate s=2: move 4 then 8
   -> [2,4,8], front = 2 = new top.
3. pop(): the top is at the front by construction, so just get() the front — the
   O(1) dequeue returns the most recently pushed element. Guard empty with a
   raised IndexError so an empty pop fails loudly instead of blocking on get().
4. top(): peek the front via queue.queue[0] without removing it (same empty
   guard). This reads the internal deque directly, which is O(1).
5. is_empty(): the stack is empty exactly when the underlying queue is empty.
TC -> push O(n), pop/top/is_empty O(1), SC -> O(n) for n elements

#KEY INSIGHT:
- With a single queue, make push do the work: after enqueuing the new element,
  rotate every older element behind it so the newest lands at the FRONT. Then
  the queue's front IS the stack's top, and pop/top are plain O(1) dequeues.
"""

from queue import Queue
from typing import cast


class MyStack:
    def __init__(self) -> None:
        self.queue: Queue[int] = Queue()

    def push(self, x: int) -> None:
        s = self.queue.qsize()
        self.queue.put(x)
        for _ in range(s):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        if self.queue.qsize() == 0:
            raise IndexError("pop from empty stack")
        return self.queue.get()

    def top(self) -> int:
        if self.queue.qsize() == 0:
            raise IndexError("top from empty stack")
        return cast(int, self.queue.queue[0])

    def is_empty(self) -> bool:
        return self.queue.empty()


if __name__ == "__main__":
    st = MyStack()
    st.push(8)
    st.push(4)
    print(st.pop())
    print(st.top())
    print(st.is_empty())
