# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Doubly Linked List / Convert Array to Doubly Linked List
# Given an array of integers, construct a doubly linked list where each element becomes
# a node (in order) and return the head. A DLL node holds data, a next pointer, and a
# prev pointer; the head's prev and the tail's next are None.
# Example 1:
# Input: arr = [2, 4, 6, 7, 5, 1, 0]
# Output: 2 <-> 4 <-> 6 <-> 7 <-> 5 <-> 1 <-> 0
# Explanation: Each node links forward via next and backward via prev.
# Constraints:
# 1 <= len(arr) <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
SKIPPED — direct construction is the only meaningful approach for building the list.

#Better Approach:
SKIPPED — no intermediate approach exists; a single pass is inherently optimal.

#Optimal Approach:
1. Make the first element the head; keep `temp` at the current tail.
2. For each remaining element, create a node whose prev points back at temp, hang it off
   temp.next, then advance temp so the back-link is always set as we go forward.
3. Return head.
TC -> O(n), SC -> O(n) for the n nodes (O(1) auxiliary).

#KEY INSIGHT:
- Setting each new node's prev to the current tail while appending means both links are
  wired in a single forward pass — no second traversal to fix back-pointers.
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
    def convertArr2DLL_brute(self, arr: List[int]) -> Optional[Node]:
        # SKIP: direct construction is the only meaningful approach
        pass

    def convertArr2DLL_better(self, arr: List[int]) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def convertArr2DLL_optimal(self, arr: List[int]) -> Optional[Node]:
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


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2DLL_optimal(arr)
    sol.printLinkedList(head)
