# QUESTION: Implement Queue using Arrays
# Implement a First-In-First-Out (FIFO) queue using an array. The implemented queue should
# support the following operations: push, peek, pop, and isEmpty.
# Implement the ArrayQueue class:
# - void push(int x): Adds element x to the end of the queue.
# - int pop(): Removes and returns the front element of the queue.
# - int peek(): Returns the front element of the queue without removing it.
# - boolean isEmpty(): Returns true if the queue is empty, false otherwise.
#
# Examples:
# Example 1:
# Input:
# ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
# [[], [5], [10], [], [], []]
# Output: [null, null, null, 5, 5, false]
# Explanation:
# ArrayQueue queue = new ArrayQueue();
# - queue.push(5);
# - queue.push(10);
# - queue.peek(); // returns 5
# - queue.pop(); // returns 5
# - queue.isEmpty(); // returns false
#
# Example 2:
# Input:
# ["ArrayQueue", "isEmpty"]
# [[]]
# Output: [null, true]
#
# Explanation:
# ArrayQueue queue = new ArrayQueue();
# - queue.isEmpty(); // returns true
#
# Constraints:
# - 1 <= number of calls made <= 100
# - 1 <= x <= 100


"""
#Implementation (implement-a-class — fixed-size circular array / ring buffer):
1. Back the queue with a fixed-capacity array `queue` of maxSize slots, plus
   three trackers: `start` (index of the front element), `end` (index of the
   last element), and `currSize` (how many elements are live). start = end = -1
   means empty. currSize is the source of truth for empty/full checks, so the
   pointers alone never have to disambiguate "full vs empty" (the classic
   ambiguity in ring buffers).
2. Why circular? A naive array queue moves `start` forward on every pop, wasting
   the freed front slots. Wrapping indices with `% maxSize` lets pop'd slots at
   the front be reused by later pushes, so the whole array stays usable and all
   ops stay O(1) with no shifting.
3. push(x): if currSize == maxSize the buffer is full -> raise OverflowError. If the
   queue was empty (end == -1), bring both start and end up to 0 (the first
   element occupies index 0). Otherwise advance end circularly:
   end = (end + 1) % maxSize. Then store x at queue[end] and bump currSize.
4. pop(): if currSize == 0 it's empty -> raise IndexError. Read the front value
   at queue[start]. If this was the last element (currSize == 1), reset both
   pointers to -1 so the next push restarts cleanly at 0. Otherwise advance
   start circularly: start = (start + 1) % maxSize. Decrement currSize and
   return the saved value — FIFO, since we always remove from the front.
5. peek(): same empty guard, then return queue[start] without moving anything.
6. is_empty(): true exactly when currSize == 0.
TC -> push/pop/peek/is_empty each O(1), SC -> O(maxSize) for the ring buffer

#KEY INSIGHT:
- Treat the fixed array as a RING: wrap start/end with % maxSize so freed front
  slots are reused, and keep a separate currSize count so empty (0) and full
  (maxSize) are unambiguous — giving O(1) FIFO with no element shifting.
"""


class MyQueue:
    def __init__(self) -> None:
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 1000
        self.queue = [0] * self.maxSize

    def push(self, x: int) -> None:
        if self.currSize == self.maxSize:
            raise OverflowError("push to full queue")
        if self.end == -1:
            self.end += 1
            self.start += 1
        else:
            self.end = (self.end + 1) % self.maxSize
        self.currSize += 1
        self.queue[self.end] = x

    def pop(self) -> int:
        if self.currSize == 0:
            raise IndexError("pop from empty queue")

        element = self.queue[self.start]
        if self.currSize == 1:
            self.end = self.start = -1
        else:
            self.start = (self.start + 1) % self.maxSize

        self.currSize -= 1
        return element

    def peek(self) -> int:
        if self.currSize == 0:
            raise IndexError("peek from empty queue")

        return self.queue[self.start]

    def is_empty(self) -> bool:
        return self.currSize == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(5)
    q.push(10)
    print(q.pop())
    print(q.peek())
    print(q.is_empty())
