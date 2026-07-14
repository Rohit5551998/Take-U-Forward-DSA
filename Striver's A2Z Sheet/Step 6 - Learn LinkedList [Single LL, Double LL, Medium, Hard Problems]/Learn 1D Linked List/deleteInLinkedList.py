# mypy: disable-error-code="empty-body"
# QUESTION: Delete a Node in a Singly Linked List
# Support deleting a node from a singly linked list in several positions:
#   - the head (front)
#   - the tail (end)
#   - the k-th node (1-indexed)
#   - the first node whose data equals a given value
# Each operation returns the (possibly new) head.
# Example 1:
# Input: list = 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0, deleteAtHead
# Output: 4 -> 6 -> 7 -> 5 -> 1 -> 0
# Explanation: The first node (2) is removed and head advances to 4.
# Constraints:
# 0 <= number of nodes <= 10^5
# 1 <= k <= number of nodes

"""
#Brute Force:
SKIPPED — pointer deletion is the direct method; there is no slower naive version.

#Better Approach:
SKIPPED — no intermediate approach exists.

#Optimal Approach:
1. deleteAtHead: empty list returns None; otherwise return head.next (drop the first node).
2. deleteAtTail: 0 or 1 node returns None; otherwise walk to the second-to-last node
   (temp.next.next is None) and cut its next pointer.
3. deleteAtK (1-indexed): k == 1 drops the head; otherwise track a `prev` while counting
   and bypass node k via prev.next = prev.next.next.
4. deleteValue: if the head matches, drop it; otherwise track `prev` and bypass the first
   node whose data equals the value.
TC -> O(n) worst case per operation, SC -> O(1).

#KEY INSIGHT:
- Deleting a node means making its predecessor point past it; the only special case is
  the head, which has no predecessor and is handled by returning head.next.
"""

from typing import List, Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def convertArr2LL(self, arr: List[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def deleteInLinkedList_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: pointer deletion is the only meaningful approach
        pass

    def deleteInLinkedList_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def deleteAtHead(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        return head.next

    def deleteAtTail(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return None
        temp = head
        while temp.next is not None and temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return head

    def deleteAtK(self, head: Optional[Node], k: int) -> Optional[Node]:
        if head is None:
            return None
        if k == 1:
            return head.next
        temp: Optional[Node] = head
        prev: Optional[Node] = None
        cnt = 0
        while temp is not None:
            cnt += 1
            if cnt == k and prev is not None and prev.next is not None:
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next
        return head

    def deleteValue(self, head: Optional[Node], val: int) -> Optional[Node]:
        if head is None:
            return None
        if head.data == val:
            return head.next
        temp: Optional[Node] = head
        prev: Optional[Node] = None
        while temp is not None:
            if temp.data == val and prev is not None and prev.next is not None:
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next
        return head

    def deleteInLinkedList_optimal(self, head: Optional[Node]) -> Optional[Node]:
        # Demonstrates delete-at-head as the representative op.
        return self.deleteAtHead(head)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.deleteAtHead(head)
    sol.printLinkedList(head)
    head = sol.deleteAtTail(head)
    sol.printLinkedList(head)
    head = sol.deleteAtK(head, 3)
    sol.printLinkedList(head)
    head = sol.deleteValue(head, 1)
    sol.printLinkedList(head)
