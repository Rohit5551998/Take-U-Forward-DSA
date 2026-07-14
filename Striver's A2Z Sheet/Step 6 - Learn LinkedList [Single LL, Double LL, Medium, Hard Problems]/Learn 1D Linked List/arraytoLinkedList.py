# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Linked List / Convert Array to Linked List
# Given an array of integers, construct a singly linked list where each element of
# the array becomes a node (in order) and return the head of that linked list.
# A Node holds a value (data) and a pointer (next) to the following node; the last
# node's next is None.
# Example 1:
# Input: arr = [2, 4, 6, 7, 5, 1, 0]
# Output: 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0 -> None
# Explanation: head.data = 2, head.next.data = 4, ..., last node's next is None.
# Constraints:
# 1 <= len(arr) <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
SKIPPED — building the list in array order is already the direct construction; there is
no naive-vs-optimized distinction for this fundamental operation.

#Better Approach:
SKIPPED — no intermediate approach exists; a single linear pass is inherently optimal.

#Optimal Approach:
1. Make the first array element the head node; keep a `temp` pointer at the head.
2. For every remaining element, create a node, hang it off temp.next, then advance
   temp so the next append always happens at the current tail.
3. Return head once every element has been linked.
TC -> O(n), SC -> O(n) for the n created nodes (O(1) auxiliary).

#KEY INSIGHT:
- Keeping a single trailing `temp` pointer lets us append in O(1) per element, so the
  whole list is built in one pass instead of re-walking to the tail each time.
"""

from typing import List, Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def arrayToLinkedList_brute(self, arr: List[int]) -> Optional[Node]:
        # SKIP: direct construction is the only meaningful approach
        pass

    def arrayToLinkedList_better(self, arr: List[int]) -> Optional[Node]:
        # SKIP: no intermediate approach exists
        pass

    def arrayToLinkedList_optimal(self, arr: List[int]) -> Optional[Node]:
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


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.arrayToLinkedList_optimal(arr)
    sol.printLinkedList(head)
