# QUESTION: Flattening of LL
# Given a special linked list containing n head nodes where every node in the linked list contains
# two pointers:
#   - 'Next' points to the next node in the list
#   - 'Child' pointer to a linked list where the current node is the head
# Each of these child linked lists is in sorted order and connected by a 'child' pointer.
# Flatten this linked list such that all nodes appear in a single sorted layer connected by the
# 'child' pointer and return the head of the modified list.
#
# Examples (inputs are shown as diagrams on TUF+; each head node hangs a sorted child list):
# Example 1:
# Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12
# Explanation: All the linked lists are joined together and sorted in a single level through the
# child pointer.
#
# Example 2:
# Output: head -> 2 -> 4 -> 5 -> 10 -> 12 -> 13 -> 16 -> 17 -> 20
# Explanation: All the linked lists are joined together and sorted in a single level through the
# child pointer.
#
# Constraints:
# n == Number of head nodes
# 1 <= n <= 100
# 1 <= Number of nodes in each child linked list <= 100
# 0 <= ListNode.val <= 1000
# All child linked lists are sorted in non-decreasing order


"""
(N = number of head nodes, M = average nodes per child list)

#Brute Force:
1. Ignore the two-pointer structure entirely: the flattened result is just
   every value in the structure, in sorted order — so collect and sort.
2. Walk the top layer via next; at each head node record its value, then walk
   straight down its child chain recording every value below it.
3. Sort the collected array — this single sort is what establishes the global
   order the row/column structure was hiding.
4. Rebuild: hang a fresh node per sorted value off a dummy, threading them
   through child, and return dummy.child.
TC -> O(N*M) collect + O(N*M log(N*M)) sort + O(N*M) rebuild ~ O(N*M log(N*M)),
SC -> O(N*M) for the values array plus O(N*M) newly created nodes

#Better Approach:
1. K-way merge with a min-heap: at any moment only the FRONT node of each
   vertical list can possibly be the next-smallest overall, so the heap never
   needs more than N entries — one candidate per row, not every node.
2. Seed the heap with the N row heads by walking the top layer via next.
3. Heap entries are (val, i, node) where i is a running push counter: values
   can tie, but i never does, so tuple comparison always resolves before
   reaching the non-comparable ListNode (and equal values pop in push order).
4. Pop the global minimum and stitch it onto the result tail through child.
   Exactly one new candidate becomes eligible — the popped node's child
   (saved before clearing) — push it as that row's replacement.
5. Clear next and child on each popped node as it is attached, so the result
   is a clean single sorted layer with no stale links.
6. Repeat until the heap drains: every node enters and leaves the heap exactly
   once, each time paying only log N.
TC -> O(N*M*logN) (N*M nodes x one push+pop on a heap of size <= N),
SC -> O(N) for the heap; nodes are reused, nothing else allocated

#Optimal Approach:
1. Each child list is ALREADY sorted, so no sorting is ever needed — the whole
   problem is just "merge two sorted lists" applied N-1 times, rewiring child
   pointers instead of allocating anything.
2. Recurse to the right first: flattening_of_ll_optimal(head.next) returns
   everything AFTER the current row already flattened into one sorted
   child-chain (base case: the last row is a sorted chain by itself).
3. Sever head.next = None before merging: everything after this row is already
   folded into the flattened remainder, so that pointer is obsolete — clearing
   it here guarantees the final list is a true single layer with no stale next
   links, no matter which merge path adopts the row head.
4. Merge the current row into that result with merge_ll — the classic
   two-pointer merge, but threaded through child: repeatedly attach the
   smaller of the two front nodes to the dummy's tail and advance that list.
5. When one list runs out, attach the other's remainder in one shot — it is
   already sorted, no walk needed.
6. Every recursion level hands a fully-sorted single-layer list back to the
   level before it, so the final return is the complete flattened list.
TC -> O(N^2 * M) worst case (the k-th merge re-walks ~k*M nodes: M*(1+2+...+N)),
SC -> O(N) recursion stack; zero new nodes — merging reuses the existing ones

#KEY INSIGHT:
- Sorted-ness is compositional: since every child list is already sorted, the
  problem reduces to repeated "merge two sorted lists" (same primitive as
  mergeTwoSortedLists, just walking child). Folding the rows from the right
  means each merge is always "one row into an already-flat sorted list".
"""

from heapq import heappop, heappush
from typing import List, Optional, Tuple


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None,
        child: Optional["ListNode"] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.child = child


def build_flattened(rows: List[List[int]]) -> Optional[ListNode]:
    # Each inner list becomes a vertical chain linked through `child`;
    # the row heads are linked left-to-right through `next`.
    # Problem guarantee: every row is sorted AND the row heads ascend left-to-right.
    top_dummy = ListNode()
    top_tail = top_dummy
    for row in rows:
        if not row:
            continue
        row_head = ListNode(row[0])
        col_tail = row_head
        for value in row[1:]:
            node = ListNode(value)
            col_tail.child = node
            col_tail = node
        top_tail.next = row_head
        top_tail = row_head
    return top_dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    # The fully flattened list is threaded through `child` pointers.
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.child
    return values


class Solution:
    def flattening_of_ll_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nums = []

        while temp is not None:
            nums.append(temp.val)
            bottom = temp.child

            while bottom is not None:
                nums.append(bottom.val)
                bottom = bottom.child

            temp = temp.next

        nums.sort()
        dummy = ListNode()
        temp = dummy

        for i in range(0, len(nums)):
            node = ListNode(nums[i])
            temp.child = node
            temp = temp.child

        return dummy.child

    def flattening_of_ll_better(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nums: List[Tuple[int, int, ListNode]] = []
        i = 0

        while temp is not None:
            i += 1
            heappush(nums, (temp.val, i, temp))
            temp = temp.next

        dummy = ListNode()
        temp = dummy

        while nums:
            _, _, node = heappop(nums)
            i += 1
            if node is not None and node.child is not None:
                bottom = node.child
                heappush(nums, (bottom.val, i, bottom))
            node.next = None
            node.child = None
            temp.child = node
            temp = temp.child

        return dummy.child

    def merge_ll(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                temp.child = head1
                head1 = head1.child
                temp = temp.child
            else:
                temp.child = head2
                head2 = head2.child
                temp = temp.child
            temp.next = None

        if head1 is not None:
            temp.child = head1

        if head2 is not None:
            temp.child = head2

        return dummy.child

    def flattening_of_ll_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.flattening_of_ll_optimal(head.next)
        head.next = None
        mergedHead = self.merge_ll(newHead, head)
        return mergedHead


if __name__ == "__main__":
    sol = Solution()
    head = build_flattened([[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]])
    print(to_list(sol.flattening_of_ll_brute(head)))
    print(to_list(sol.flattening_of_ll_better(head)))
    print(to_list(sol.flattening_of_ll_optimal(head)))
    # expect: [5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]
