# mypy: disable-error-code="empty-body"
# QUESTION: Flatten a Linked List
# You are given a linked list where every node has two pointers: `next` points to
# the next node in the top-level list, and `child` (bottom) points to a sorted
# sub-list. Every sub-list is itself sorted. Flatten the list into a single sorted
# linked list connected only through the `child` pointer.
# Example 1:
# Input:
#   3 -> 4 -> 2 -> 6   (next pointers)
#   |    |    |    |
#   7    11   10   -    (child pointers, each column sorted downwards)
#   |         |
#   8         12
# Output: 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 10 -> 11 -> 12 (via child pointers)
# Constraints:
# - Each sub-list (child chain) is sorted in non-decreasing order.
# - The number of nodes across all lists can be up to ~10^5.

"""
#Brute Force:
1. Traverse the whole 2-D structure: for every top node, walk its child chain and
   collect all values into an array.
2. Sort the array.
3. Rebuild a single list linked via `child` from the sorted array.
TC -> O(N*M) + O(N*M log(N*M)) + O(N*M), SC -> O(N*M) + O(N*M)
   where N = top nodes, M = avg child-chain length.

#Better Approach:
SKIPPED — no meaningful tier sits between the array brute and the recursive merge;
iterative "merge each column into the accumulated result" is the same O work as
the optimal recursion.

#Optimal Approach:
1. Recurse to the end of the top-level (`next`) list: flatten head.next first,
   which returns an already-fully-flattened sorted child chain.
2. Base case: a null head or a head with no `next` is already flat — return it.
3. Merge the current node's child chain with the flattened rest using `merge`,
   which is a standard two-pointer sorted merge but stitching nodes through the
   `child` pointer (and clearing `next` so the result is a pure vertical chain).
4. Return the merged head; unwinding the recursion merges columns right-to-left.
TC -> O(N*M) (each node touched a constant number of times across merges),
SC -> O(N) recursion stack.

#KEY INSIGHT:
- Because every child chain is already sorted, flattening is just repeated
  two-way merges. Recursing to the deepest column first lets each merge combine
  one column with an already-sorted accumulation, so the whole structure
  collapses into one sorted `child`-linked list with no explicit sort.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1
        self.child: Optional["Node"] = None


class Solution:
    def convertArr2LL(self, arr: list[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None)
            temp = temp.next
        return head

    def printChildList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.child
        print("None")

    def convertArrToChildLL(self, ans: list[int]) -> Optional[Node]:
        newHead = Node(-1)
        temp = newHead
        for i in range(0, len(ans)):
            temp.child = Node(ans[i])
            temp = temp.child
        return newHead.child

    def merge(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        newHead = Node(-1)
        temp = newHead
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                temp.child = head1
                temp = temp.child
                head1 = head1.child
            else:
                temp.child = head2
                temp = temp.child
                head2 = head2.child
            temp.next = None
        temp.child = head1 if head1 is not None else head2
        if newHead.child is not None:
            newHead.child.next = None
        return newHead.child

    def flattenLinkedList_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        ans: list[int] = []
        temp1 = head
        while temp1 is not None:
            temp2: Optional[Node] = temp1
            while temp2 is not None:
                ans.append(temp2.data)
                temp2 = temp2.child
            temp1 = temp1.next
        ans.sort()
        return self.convertArrToChildLL(ans)

    def flattenLinkedList_better(self) -> None:
        # SKIP: no distinct tier between array brute and recursive merge.
        pass

    def flattenLinkedList_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        mergedListHead = self.flattenLinkedList_optimal(head.next)
        return self.merge(head, mergedListHead)


if __name__ == "__main__":
    sol = Solution()
    # Build a small multilevel structure: top list 5 -> 10 -> 19,
    # each with a sorted child chain.
    top = Node(5)
    top.child = Node(7)
    top.child.child = Node(8)

    top.next = Node(10)
    top.next.child = Node(20)

    top.next.next = Node(19)
    top.next.next.child = Node(22)
    top.next.next.child.child = Node(50)

    flat = sol.flattenLinkedList_optimal(top)
    sol.printChildList(flat)
