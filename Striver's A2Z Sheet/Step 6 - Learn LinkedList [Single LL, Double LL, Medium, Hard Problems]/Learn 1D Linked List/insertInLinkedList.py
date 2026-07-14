# mypy: disable-error-code="empty-body"
# QUESTION: Insert a Node in a Singly Linked List
# Support inserting a new node into a singly linked list in several positions:
#   - at the head (front)
#   - at the tail (end)
#   - at the k-th position (1-indexed)
#   - before the first node whose data equals a given value
# Each operation returns the (possibly new) head.
# Example 1:
# Input: list = 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0, insertBeforeValue(x=10, val=7)
# Output: 2 -> 4 -> 6 -> 10 -> 7 -> 5 -> 1 -> 0
# Explanation: 10 is inserted just before the node holding 7.
# Constraints:
# 0 <= number of nodes <= 10^5
# 1 <= k <= number of nodes + 1

"""
#Brute Force:
SKIPPED — pointer insertion is inherently the direct method; there is no slower naive
version worth contrasting.

#Better Approach:
SKIPPED — no intermediate approach exists.

#Optimal Approach:
1. insertAtHead: create the node, point its next at the current head, return the new node.
2. insertAtTail: if the list is empty return a fresh node; otherwise walk to the last
   node (temp.next is None) and hang the new node there.
3. insertAtK (1-indexed): k == 1 is a head insert; otherwise walk while counting until
   we sit on node k-1, then splice the new node between k-1 and k.
4. insertBeforeValue: if the head holds the value do a head insert; otherwise walk
   looking one step ahead (temp.next.data == val) and splice before that node.
TC -> O(n) worst case per operation, SC -> O(1).

#KEY INSIGHT:
- Every insertion reduces to finding the node *before* the target position and rewiring
  exactly two `next` pointers; the head cases are special only because there is no
  predecessor.
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

    def insertInLinkedList_brute(self, head: Optional[Node], x: int) -> Optional[Node]:
        # SKIP: pointer insertion is the only meaningful approach
        pass

    def insertInLinkedList_better(self, head: Optional[Node], x: int) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def insertAtHead(self, head: Optional[Node], x: int) -> Optional[Node]:
        node = Node(x)
        node.next = head
        return node

    def insertAtTail(self, head: Optional[Node], x: int) -> Optional[Node]:
        if head is None:
            return Node(x)
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(x)
        return head

    def insertAtK(self, head: Optional[Node], x: int, k: int) -> Optional[Node]:
        if head is None:
            return Node(x) if k == 1 else head
        if k == 1:
            node = Node(x)
            node.next = head
            return node
        cnt = 0
        temp: Optional[Node] = head
        while temp is not None and temp.next is not None:
            cnt += 1
            if cnt == k - 1:
                node = Node(x)
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next
        return head

    def insertBeforeValue(self, head: Optional[Node], x: int, val: int) -> Optional[Node]:
        if head is None:
            return head
        if head.data == val:
            node = Node(x)
            node.next = head
            return node
        temp = head
        while temp.next is not None:
            if temp.next.data == val:
                node = Node(x)
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next
        return head

    def insertInLinkedList_optimal(self, head: Optional[Node], x: int, val: int) -> Optional[Node]:
        # Demonstrates the "insert before a value" variant as the representative op.
        return self.insertBeforeValue(head, x, val)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    head = sol.insertInLinkedList_optimal(head, 10, 7)
    sol.printLinkedList(head)
