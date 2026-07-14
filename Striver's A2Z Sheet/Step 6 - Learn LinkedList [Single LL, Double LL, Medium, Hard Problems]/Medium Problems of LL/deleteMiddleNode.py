# mypy: disable-error-code="empty-body"
# QUESTION: Delete the Middle Node of a Linked List
# Given the head of a singly linked list, delete the middle node and return the head.
# For a list of length n the middle is the floor(n/2)-th node (0-indexed). If the list
# has one node, deleting the middle leaves an empty list.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 2 -> 1
# Output: 1 -> 2 -> 3 -> 2 -> 1   (node 4 removed)
# Example 2:
# Input: 1
# Output: None
# Constraints:
# 1 <= number of nodes <= 10^5

"""
#Brute Force:
1. Count the length n in one pass.
2. Walk to node (n//2 - 1), the predecessor of the middle.
3. Bypass the middle via temp.next = temp.next.next.
TC -> O(n + n/2), SC -> O(1).

#Better Approach:
SKIPPED — the offset slow/fast method is optimal; no distinct middle tier.

#Optimal Approach:
1. Start slow at head and fast at head.next (the offset skips a length count).
2. Advance slow by one and fast by two while fast.next and fast.next.next exist.
3. slow now sits on the node just before the middle; delete via slow.next = slow.next.next.
TC -> O(n/2), SC -> O(1).

#KEY INSIGHT:
- Starting fast one node ahead lands slow on the predecessor of the middle (not the middle
  itself), so the deletion needs no separate length pass and no back pointer.
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

    def deleteMiddleNode_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return None
        cnt = 1
        temp: Optional[Node] = head
        while temp is not None and temp.next is not None:
            temp = temp.next
            cnt += 1
        mid = cnt // 2
        temp = head
        cnt = 1
        while cnt != mid and temp is not None:
            cnt += 1
            temp = temp.next
        if temp is not None and temp.next is not None:
            temp.next = temp.next.next
        return head

    def deleteMiddleNode_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no distinct middle tier
        pass

    def deleteMiddleNode_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return None
        slow, fast = head, head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
        if slow is not None and slow.next is not None:
            slow.next = slow.next.next
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 2, 1]
    head = sol.convertArr2LL(arr)
    head = sol.deleteMiddleNode_optimal(head)
    sol.printLinkedList(head)
