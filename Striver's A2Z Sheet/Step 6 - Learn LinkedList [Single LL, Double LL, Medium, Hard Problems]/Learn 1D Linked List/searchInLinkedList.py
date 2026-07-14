# mypy: disable-error-code="empty-body"
# QUESTION: Search an Element in a Linked List
# Given the head of a singly linked list and an integer x, return True if x is present
# as the data of some node, otherwise return False.
# Example 1:
# Input: list = 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0 -> None, x = 6
# Output: True
# Explanation: 6 is stored in the third node.
# Constraints:
# 0 <= number of nodes <= 10^5
# -10^9 <= x, node.data <= 10^9

"""
#Brute Force:
SKIPPED — an unsorted linked list gives no random access, so scanning is unavoidable;
there is no naive method that is worse than a single scan.

#Better Approach:
SKIPPED — no intermediate approach exists for an unsorted list.

#Optimal Approach:
1. Start `temp` at head.
2. Walk the list; if any node's data equals x, return True immediately (early exit).
3. If the walk reaches None, x is absent — return False.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Without ordering there is nothing to exploit, so a linear scan with an early return
  on the first match is optimal.
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

    def searchInLinkedList_brute(self, head: Optional[Node], x: int) -> bool:
        # SKIP: a single scan is the only meaningful approach
        pass

    def searchInLinkedList_better(self, head: Optional[Node], x: int) -> bool:
        # SKIP: no intermediate approach exists
        pass

    def searchInLinkedList_optimal(self, head: Optional[Node], x: int) -> bool:
        temp = head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        return False


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    print(sol.searchInLinkedList_optimal(head, 6))
