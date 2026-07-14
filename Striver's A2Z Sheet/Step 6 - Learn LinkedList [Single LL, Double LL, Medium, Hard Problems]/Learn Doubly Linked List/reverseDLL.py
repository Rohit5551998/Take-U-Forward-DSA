# mypy: disable-error-code="empty-body"
# QUESTION: Reverse a Doubly Linked List
# Given the head of a doubly linked list, reverse it in place and return the new head.
# Example 1:
# Input: 2 <-> 4 <-> 6 <-> 7 <-> 5 <-> 1 <-> 0
# Output: 0 <-> 1 <-> 5 <-> 7 <-> 6 <-> 4 <-> 2
# Explanation: Every node's next and prev pointers are swapped so traversal order flips.
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Traverse the DLL pushing each node's data onto a stack.
2. Traverse again from head, popping the stack to overwrite each node's data (LIFO gives
   reversed values while the links stay put).
TC -> O(2n), SC -> O(n) for the stack.

#Better Approach:
SKIPPED — the swap-pointers method below is optimal; there is no distinct middle tier.

#Optimal Approach:
1. If the list is empty or a single node, it's already reversed — return head.
2. Walk with `temp`; at each node remember temp.prev in `last`, then swap the node's own
   next and prev pointers (temp.prev = temp.next, temp.next = last).
3. Move forward along what is now temp.prev (the original next).
4. When temp becomes None, `last` sits on the original tail; the new head is last.prev.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- In a DLL you can reverse by swapping each node's own next/prev in a single pass — no new
  nodes and no value copying; the last non-null node visited is one step before the new head.
"""

from typing import List, Optional


class Node:
    def __init__(
        self,
        data: int,
        next1: Optional["Node"] = None,
        prev1: Optional["Node"] = None,
    ) -> None:
        self.data = data
        self.next = next1
        self.prev = prev1


class Solution:
    def convertArr2DLL(self, arr: List[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None, temp)
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverseDLL_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        stack: List[int] = []
        temp: Optional[Node] = head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next
        return head

    def reverseDLL_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: the pointer-swap approach is optimal; no distinct middle tier exists
        pass

    def reverseDLL_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        temp: Optional[Node] = head
        last: Optional[Node] = None
        while temp is not None:
            last = temp.prev
            temp.prev = temp.next
            temp.next = last
            temp = temp.prev
        # `last` is the original tail; the new head is one step before it.
        return last.prev if last is not None else None


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2DLL(arr)
    sol.printLinkedList(head)
    head = sol.reverseDLL_optimal(head)
    sol.printLinkedList(head)
