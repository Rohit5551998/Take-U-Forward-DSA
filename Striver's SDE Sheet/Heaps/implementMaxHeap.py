# QUESTION: Implement Max Heap
# You need to implement the Max Heap with the following given methods.
# - insert(x)         -> insert value x to the max heap
# - getMax            -> output the maximum value from the max heap
# - extractMax        -> remove the maximum element from the heap
# - heapSize          -> return the current size of the heap
# - isEmpty           -> returns if heap is empty or not
# - changeKey(ind, val) -> update the value at given index to val (index is 0-based)
# - initializeHeap    -> initialize the heap
# Note: When extracting max, if both left and right children are equal, you must swap with the
# LEFT child.
#
# Examples:
# Example 1:
# Input: ["initializeHeap", "insert 4", "insert 9", "getMax", "extractMax", "getMax",
#         "heapSize", "isEmpty"]
# Output: [9, 4, 1, false]
# Explanation: After inserting 4 and 9, getMax returns 9. extractMax removes 9, so the next
# getMax returns 4. One element remains, so heapSize is 1 and isEmpty is false.
#
# Example 2:
# Input: ["initializeHeap", "insert 5", "insert 2", "insert 8", "changeKey 1 10", "getMax",
#         "extractMax", "getMax"]
# Output: [10, 8]
# Explanation: After the inserts, the heap array is [8, 2, 5]. changeKey(1, 10) sets index 1
# to 10, which sifts up to the root: [10, 8, 5]. getMax returns 10; extractMax removes 10,
# so the next getMax returns 8.
#
# Constraints:
# 1 <= n <= 10^5
# -10^5 <= nums[i] <= 10^5


"""
#Implementation (implement-a-class — array-backed binary max heap):
1. Store the complete binary tree FLAT in one list `heap`, level by level. No
   node objects or pointers are needed because the tree is complete, so the
   parent/child links are pure index arithmetic:
     - parent(i) = (i - 1) // 2
     - left(i)   = 2*i + 1
     - right(i)  = 2*i + 2
   This is the whole trick — navigation is O(1) index math, and the array stays
   contiguous with no gaps.
2. The MAX-HEAP invariant: every parent >= both its children. Consequently the
   maximum is always at index 0 (the root), so get_max is a trivial O(1) read.

3. sift_up(i): repair an UPWARD violation (a node bigger than its parent). Used
   after inserting at the end, and by change_key when a value grows. Compare
   heap[i] with its parent; if it's larger, swap and recurse on the parent's
   index. Stop at the root (i == 0) or once the parent is >= the node. The
   element bubbles toward the root, at most log n levels.

4. sift_down(i): repair a DOWNWARD violation (a node smaller than a child). Read
   the two children's values (treat a missing child as -infinity so it never
   wins). If the node already dominates both, stop. Otherwise swap with the
   LARGER child and recurse down. Tie rule: the check `left > parent and
   left >= right` picks the LEFT child when the two children are equal, matching
   the problem's requirement. At most log n levels.

5. insert(val): append to the end (keeps the tree complete), then sift_up from
   the last index to restore order. O(log n).

6. get_max(): return heap[0]; raise IndexError if empty (an unambiguous signal,
   since a sentinel like -1 is itself a legal value in [-1e5, 1e5]).

7. extract_max(): save heap[0] (the answer), move the LAST element into the root
   slot, pop the tail (shrinking the array), then sift_down(0) to sink the
   displaced element into place. Return the saved max. O(log n). Guard the
   single-element/empty cases so we don't sift_down an empty heap.

8. heap_size() -> len(heap); is_empty() -> len(heap) == 0. Both O(1) because the
   list length IS the heap size — no separate counter needed.

9. change_key(ind, val): overwrite heap[ind] = val, then call BOTH sift_up(ind)
   and sift_down(ind). The new value can only violate in one direction, so
   exactly one of the two does work and the other is a cheap no-op. O(log n).

#KEY INSIGHT:
- A complete binary tree needs no pointers: pack it into an array and derive
  parent/child by index (parent=(i-1)//2, children=2i+1 / 2i+2). Every mutation
  is a local swap chain — sift_up toward the root or sift_down toward the leaves
  — that restores the parent>=child invariant in O(log n), keeping the max
  pinned at index 0.
"""

import math


class MaxHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def sift_up(self, index: int) -> None:
        if index == 0 or (self.heap[index] <= self.heap[(index - 1) // 2]):
            return
        self.heap[index], self.heap[(index - 1) // 2] = (
            self.heap[(index - 1) // 2],
            self.heap[index],
        )
        self.sift_up((index - 1) // 2)

    def sift_down(self, index: int) -> None:
        if index >= len(self.heap):
            return
        parent = self.heap[index]
        left = self.heap[2 * index + 1] if 2 * index + 1 < len(self.heap) else -math.inf
        right = self.heap[2 * index + 2] if 2 * index + 2 < len(self.heap) else -math.inf

        if parent >= left and parent >= right:
            return
        if left > parent and left >= right:
            self.heap[index], self.heap[2 * index + 1] = self.heap[2 * index + 1], self.heap[index]
            self.sift_down(2 * index + 1)
        elif right > parent:
            self.heap[index], self.heap[2 * index + 2] = self.heap[2 * index + 2], self.heap[index]
            self.sift_down(2 * index + 2)

    def insert(self, val: int) -> None:
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def get_max(self) -> int:
        if self.heap:
            return self.heap[0]
        raise IndexError("Empty Heap")

    def extract_max(self) -> int:
        if self.heap:
            ans = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            if len(self.heap) != 0:
                self.sift_down(0)
            return ans
        raise IndexError("Empty Heap")

    def heap_size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def change_key(self, ind: int, val: int) -> None:
        self.heap[ind] = val
        self.sift_up(ind)
        self.sift_down(ind)


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(4)
    heap.insert(9)
    print(heap.get_max())
    print(heap.extract_max())
    print(heap.get_max())
