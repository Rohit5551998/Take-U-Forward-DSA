# mypy: disable-error-code="empty-body"
# QUESTION: Remove Duplicates from a Sorted Doubly Linked List
# Given the head of a doubly linked list sorted in non-decreasing order, remove all
# duplicate nodes so each value appears once, and return the head.
# Example 1:
# Input: 1 <-> 1 <-> 4 <-> 6 <-> 6 <-> 10 <-> 10 <-> 10
# Output: 1 <-> 4 <-> 6 <-> 10
# Constraints:
# 0 <= number of nodes <= 10^5
# list is sorted in non-decreasing order

"""
#Brute Force:
SKIPPED — because the list is sorted, duplicates are adjacent and a single in-place sweep
removes them; any set-based method would only add overhead.

#Better Approach:
SKIPPED — no intermediate tier exists.

#Optimal Approach:
1. Walk with `temp`. For each node, advance an inner `nextNode` past every following node
   whose data equals temp.data.
2. Link temp.next to nextNode (the first different value) and, if nextNode exists, set its
   prev back to temp.
3. Move temp forward and repeat.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Sorted order guarantees equal values are contiguous, so skipping a run of duplicates and
  re-linking both directions once per distinct value clears the list in a single pass.
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

    def removeDuplicates_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: single in-place sweep is the only meaningful approach for a sorted DLL
        pass

    def removeDuplicates_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no intermediate tier exists
        pass

    def removeDuplicates_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        temp: Optional[Node] = head
        while temp is not None:
            nextNode = temp.next
            while nextNode is not None and nextNode.data == temp.data:
                nextNode = nextNode.next
            temp.next = nextNode
            if nextNode is not None:
                nextNode.prev = temp
            temp = temp.next
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 4, 6, 6, 10, 10, 10]
    head = sol.convertArr2DLL(arr)
    head = sol.removeDuplicates_optimal(head)
    sol.printLinkedList(head)
