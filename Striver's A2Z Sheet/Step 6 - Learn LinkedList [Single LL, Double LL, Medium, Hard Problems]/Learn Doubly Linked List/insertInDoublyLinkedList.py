# mypy: disable-error-code="empty-body"
# QUESTION: Insert a Node in a Doubly Linked List
# Support inserting a new node into a doubly linked list at several positions:
#   - at the head
#   - before the tail
#   - at the k-th position (1-indexed)
#   - before a given node
# Each positional operation returns the (possibly new) head; both next and prev links
# must be maintained.
# Example 1:
# Input: list = 2 <-> 4 <-> 6, insertAtHead(x=10)
# Output: 10 <-> 2 <-> 4 <-> 6
# Explanation: 10 becomes the new head; its next is the old head, whose prev is 10.
# Constraints:
# 0 <= number of nodes <= 10^5
# 1 <= k <= number of nodes + 1

"""
#Brute Force:
SKIPPED — pointer insertion is the direct method; there is no slower naive version.

#Better Approach:
SKIPPED — no intermediate approach exists.

#Optimal Approach:
1. insertAtHead: new node's next is the old head; set old head's prev to it; return it.
2. insertBeforeTail: if only one node, that's a head insert; else walk to the tail and
   splice the new node between tail.prev and tail, fixing four pointers.
3. insertAtK (1-indexed): k == 1 is a head insert; else walk while counting to node k-1
   and splice between k-1 and k, updating both directions.
4. insertAtNode(node, val): splice a new node between node.prev and node.
TC -> O(n) worst case per operation, SC -> O(1).

#KEY INSIGHT:
- Every DLL insertion rewires exactly four pointers (new.prev, new.next, and the two
  neighbours pointing back at new), so the neighbours' prev/next stay consistent in both
  directions.
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

    def insertInDLL_brute(self, head: Optional[Node], x: int) -> Optional[Node]:
        # SKIP: pointer insertion is the only meaningful approach
        pass

    def insertInDLL_better(self, head: Optional[Node], x: int) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def insertAtHead(self, head: Optional[Node], x: int) -> Optional[Node]:
        node = Node(x, head, None)
        if head is not None:
            head.prev = node
        return node

    def insertBeforeTail(self, head: Optional[Node], x: int) -> Optional[Node]:
        if head is None or head.next is None:
            return self.insertAtHead(head, x)
        temp = head
        while temp.next is not None:
            temp = temp.next
        node = Node(x, temp, temp.prev)
        if temp.prev is not None:
            temp.prev.next = node
        temp.prev = node
        return head

    def insertAtK(self, head: Optional[Node], x: int, k: int) -> Optional[Node]:
        if head is None:
            return Node(x) if k == 1 else head
        if k == 1:
            return self.insertAtHead(head, x)
        cnt = 0
        temp: Optional[Node] = head
        while temp is not None and temp.next is not None:
            cnt += 1
            if cnt == k - 1:
                node = Node(x, temp.next, temp)
                temp.next.prev = node
                temp.next = node
                break
            temp = temp.next
        return head

    def insertAtNode(self, node: Node, val: int) -> None:
        prev = node.prev
        newNode = Node(val, node, prev)
        if prev is not None:
            prev.next = newNode
        node.prev = newNode

    def insertInDLL_optimal(self, head: Optional[Node], x: int) -> Optional[Node]:
        # Demonstrates insert-at-head as the representative op.
        return self.insertAtHead(head, x)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2DLL(arr)
    sol.printLinkedList(head)
    head = sol.insertAtHead(head, 10)
    sol.printLinkedList(head)
    head = sol.insertBeforeTail(head, 20)
    sol.printLinkedList(head)
    head = sol.insertAtK(head, 30, 5)
    sol.printLinkedList(head)
    if head is not None and head.next is not None:
        sol.insertAtNode(head.next, 50)
    sol.printLinkedList(head)
