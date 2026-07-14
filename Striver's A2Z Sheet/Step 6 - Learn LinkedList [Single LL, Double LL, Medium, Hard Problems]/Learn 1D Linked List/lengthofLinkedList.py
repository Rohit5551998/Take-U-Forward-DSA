# mypy: disable-error-code="empty-body"
# QUESTION: Find the Length of a Linked List
# Given the head of a singly linked list, return the number of nodes in it.
# Example 1:
# Input: 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0 -> None
# Output: 7
# Explanation: There are 7 nodes in the linked list.
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
SKIPPED — counting requires visiting every node; there is no naive alternative that
does more work than a single linear traversal.

#Better Approach:
SKIPPED — no intermediate approach exists between "walk once" and the optimal.

#Optimal Approach:
1. Start a counter at 0 and a `temp` pointer at head.
2. Walk node by node, incrementing the counter until temp becomes None.
3. Return the counter — it equals the number of nodes.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Length is inherently a full-list property; one traversal with a counter is both the
  simplest and the optimal way to obtain it.
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

    def lengthOfLinkedList_brute(self, head: Optional[Node]) -> int:
        # SKIP: a single traversal is the only meaningful approach
        pass

    def lengthOfLinkedList_better(self, head: Optional[Node]) -> int:
        # SKIP: no intermediate approach exists
        pass

    def lengthOfLinkedList_optimal(self, head: Optional[Node]) -> int:
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    print(sol.lengthOfLinkedList_optimal(head))
