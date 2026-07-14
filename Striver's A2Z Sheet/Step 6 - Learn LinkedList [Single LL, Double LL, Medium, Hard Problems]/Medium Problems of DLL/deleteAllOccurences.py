# mypy: disable-error-code="empty-body"
# QUESTION: Delete All Occurrences of a Key in a Doubly Linked List
# Given the head of a doubly linked list and a key, delete every node whose data equals
# the key and return the (possibly new) head.
# Example 1:
# Input: 10 <-> 4 <-> 10 <-> 10 <-> 6 <-> 10, key = 10
# Output: 4 <-> 6
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
SKIPPED — a single in-place traversal that unlinks matches is already the direct method;
copying survivors into a new list would only be slower.

#Better Approach:
SKIPPED — no intermediate tier exists.

#Optimal Approach:
1. Walk with `temp` from head. If the current head matches the key, advance head first so
   the returned head is never a deleted node.
2. When temp.data == key, grab prevNode and nextNode; if prevNode exists set prevNode.next
   = nextNode, if nextNode exists set nextNode.prev = prevNode, then move temp to nextNode.
3. Otherwise just advance temp.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- A DLL node carries its own prev pointer, so each matching node can be spliced out in
  O(1) during a single forward pass — no predecessor bookkeeping and no second list.
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

    def deleteAllOccurrences_brute(self, head: Optional[Node], key: int) -> Optional[Node]:
        # SKIP: single in-place traversal is the only meaningful approach
        pass

    def deleteAllOccurrences_better(self, head: Optional[Node], key: int) -> Optional[Node]:
        # SKIP: no intermediate tier exists
        pass

    def deleteAllOccurrences_optimal(self, head: Optional[Node], key: int) -> Optional[Node]:
        if head is None:
            return None
        temp: Optional[Node] = head
        while temp is not None:
            if head is not None and head.data == key:
                head = head.next
            if temp.data == key:
                prevNode, nextNode = temp.prev, temp.next
                if prevNode is not None:
                    prevNode.next = nextNode
                if nextNode is not None:
                    nextNode.prev = prevNode
                temp = nextNode
            else:
                temp = temp.next
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 4, 10, 10, 6, 10]
    head = sol.convertArr2DLL(arr)
    head = sol.deleteAllOccurrences_optimal(head, 10)
    sol.printLinkedList(head)
