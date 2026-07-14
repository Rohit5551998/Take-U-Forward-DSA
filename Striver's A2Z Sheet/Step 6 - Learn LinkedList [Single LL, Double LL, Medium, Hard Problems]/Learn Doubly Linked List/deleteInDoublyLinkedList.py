# mypy: disable-error-code="empty-body"
# QUESTION: Delete a Node in a Doubly Linked List
# Support deleting a node from a doubly linked list at several positions:
#   - the head
#   - the tail
#   - the k-th node (1-indexed)
#   - a given node
# Each positional operation returns the (possibly new) head; both next and prev links
# must stay consistent.
# Example 1:
# Input: list = 2 <-> 4 <-> 6 <-> 7, deleteHead
# Output: 4 <-> 6 <-> 7
# Explanation: The first node (2) is removed and the new head's prev becomes None.
# Constraints:
# 0 <= number of nodes <= 10^5
# 1 <= k <= number of nodes

"""
#Brute Force:
SKIPPED — pointer deletion is the direct method; there is no slower naive version.

#Better Approach:
SKIPPED — no intermediate approach exists.

#Optimal Approach:
1. deleteHead: 0/1 node returns None; else advance head, set new head's prev to None and
   detach the old head.
2. deleteTail: 0/1 node returns None; else walk to the tail and cut tail.prev.next.
3. deleteAtK (1-indexed): walk to node k, then dispatch — no neighbours means empty list,
   only a front neighbour means it's the tail, only a prev means it's the head, else
   stitch prev.next to front and front.prev to prev.
4. deleteNode(node): bridge node.prev and node.next around the node in both directions.
TC -> O(n) worst case per operation, SC -> O(1).

#KEY INSIGHT:
- Because a DLL node knows its own predecessor, deletion needs no separate "prev" tracker:
  read node.prev / node.next directly and rewire both sides. Bug fix vs. the original:
  deleteNode now uses front.prev (not the nonexistent .back) and guards None neighbours.
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

    def deleteInDLL_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: pointer deletion is the only meaningful approach
        pass

    def deleteInDLL_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def deleteHead(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return None
        prev = head
        head = head.next
        head.prev = None
        prev.next = None
        return head

    def deleteTail(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return None
        temp = head
        while temp.next is not None:
            temp = temp.next
        prev = temp.prev
        if prev is not None:
            prev.next = None
        temp.prev = None
        return head

    def deleteAtK(self, head: Optional[Node], k: int) -> Optional[Node]:
        if head is None:
            return None
        cnt = 0
        curr: Optional[Node] = head
        while curr is not None:
            cnt += 1
            if cnt == k:
                break
            curr = curr.next
        if curr is None:
            return head
        prev = curr.prev
        front = curr.next
        if prev is None and front is None:
            return None
        if prev is None:
            return self.deleteHead(head)
        if front is None:
            return self.deleteTail(head)
        prev.next = front
        front.prev = prev
        curr.prev = None
        curr.next = None
        return head

    def deleteNode(self, node: Node) -> None:
        prev = node.prev
        front = node.next
        if prev is not None:
            prev.next = front
        if front is not None:
            front.prev = prev
        node.next = None
        node.prev = None

    def deleteInDLL_optimal(self, head: Optional[Node]) -> Optional[Node]:
        # Demonstrates delete-head as the representative op.
        return self.deleteHead(head)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2DLL(arr)
    sol.printLinkedList(head)
    head = sol.deleteHead(head)
    sol.printLinkedList(head)
    head = sol.deleteTail(head)
    sol.printLinkedList(head)
    head = sol.deleteAtK(head, 3)
    sol.printLinkedList(head)
    if head is not None and head.next is not None:
        sol.deleteNode(head.next)
    sol.printLinkedList(head)
