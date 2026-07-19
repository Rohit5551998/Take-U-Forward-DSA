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
#Variant I — Push-costly (eager reversal on every push): MyQueue
1. Keep two LIFO stacks, `input` and `output`. The whole design rests on one
   invariant: `input` always holds the queue with the FRONT (oldest) element on
   TOP. If that invariant holds, pop and peek are trivial O(1) reads of input's
   top — the hard work is pushed entirely into push().
2. push(x): a new element is the NEWEST, so in a FIFO it must end up at the
   BOTTOM of input (served last). To place it there while keeping oldest-on-top:
   first pour all of input into output (this reverses the order), then push x
   onto the now-empty input, then pour output back on top of input. Net effect:
   x sits at the bottom, everything older stacked above it, oldest back on top.
3. pop(): the front (oldest) is already on top of input, so just pop input's
   top — O(1). FIFO falls out of the maintained invariant.
4. peek(): read input's top (input.queue[-1]) without removing — O(1).
5. is_empty(): the queue is empty exactly when input is empty.
TC -> push O(n), pop/peek/is_empty O(1), SC -> O(n) for n elements

#Variant II — Lazy transfer (amortized O(1) all ops): MyQueueOptimal
1. Split the work across two stacks with fixed roles: `input` is the INBOX (new
   pushes land here) and `output` is the OUTBOX (holds elements already flipped
   into serve-order, oldest on top). The trick vs Variant I: defer the reversal
   instead of doing it eagerly on every push.
2. push(x): just put x on input — O(1), no reversal. New arrivals simply pile up
   in the inbox.
3. pop(): the front lives in output. If output is EMPTY, drain the whole input
   into output first: repeatedly get from input's top and put onto output. This
   single reversal flips inbox order so the oldest element ends up on output's
   top. Crucially, drain ONLY when output is empty — draining while output still
   has items would interleave old and new and break FIFO.
4. After the (possible) drain, if output is still empty the queue was truly
   empty -> raise IndexError. Otherwise get output's top — that's the oldest
   element, so it's the correct FIFO front.
5. peek(): same lazy-drain logic, but read output's top without removing it.
   For a LIFO stack the top is the LAST-in element, i.e. output.queue[-1].
6. is_empty(): empty only when BOTH stacks are empty — an element could be
   sitting in either the inbox or the outbox.
7. Why amortized O(1): each element is moved across (input->output) at most ONCE
   in its lifetime, then sits in output until popped. A single pop that triggers
   a drain is O(n), but that cost is spread over the many O(1) pops that follow,
   so n operations do ~O(n) total work.
TC -> push O(1); pop/peek amortized O(1) (worst-case O(n) on a drain), SC -> O(n)

#KEY INSIGHT:
- Variant I: maintain the invariant "input stack has the oldest element on top"
  by fully reversing through the second stack on every push. That front-loads
  all cost into push (O(n)) so that pop/peek stay O(1) with zero rearranging.
- Variant II: keep an inbox and an outbox, and reverse LAZILY — only refill the
  outbox (in one pass) when it runs dry. Each element is moved exactly once, so
  every operation is amortized O(1) despite the occasional O(n) drain.
"""

from queue import LifoQueue


class MyQueue:
    def __init__(self) -> None:
        self.input: LifoQueue[int] = LifoQueue()
        self.output: LifoQueue[int] = LifoQueue()

    def push(self, x: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
        self.input.put(x)
        while not self.output.empty():
            self.input.put(self.output.get())

    def pop(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("pop from empty queue")
        return self.input.get()

    def peek(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("peek from empty queue")
        return self.input.queue[-1]

    def is_empty(self) -> bool:
        return self.input.empty()


class MyQueueOptimal:
    """Variant II — lazy transfer, amortized O(1) all ops.

    Uses two LIFO stacks with distinct jobs: `input` is the inbox (push lands
    here), `output` is the outbox holding already-flipped FIFO order. Only drain
    input -> output when output is empty (see docstring Variant II).
    """

    def __init__(self) -> None:
        self.input: LifoQueue[int] = LifoQueue()
        self.output: LifoQueue[int] = LifoQueue()

    def push(self, x: int) -> None:
        self.input.put(x)

    def pop(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())

        if self.output.empty():
            raise IndexError("pop from empty queue")
        return self.output.get()

    def peek(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())

        if self.output.empty():
            raise IndexError("peek from empty queue")
        return self.output.queue[-1]

    def is_empty(self) -> bool:
        return self.input.empty() and self.output.empty()


if __name__ == "__main__":
    q = MyQueue()
    q.push(4)
    q.push(8)
    print(q.pop())
    print(q.peek())
    print(q.is_empty())

    q2 = MyQueueOptimal()
    q2.push(4)
    q2.push(8)
    print(q2.pop())
    print(q2.peek())
    print(q2.is_empty())

    # Variant II (fill in MyQueueOptimal, then uncomment):
    # q2 = MyQueueOptimal()
    # q2.push(4)
    # q2.push(8)
    # print(q2.pop())
    # print(q2.peek())
    # print(q2.is_empty())
