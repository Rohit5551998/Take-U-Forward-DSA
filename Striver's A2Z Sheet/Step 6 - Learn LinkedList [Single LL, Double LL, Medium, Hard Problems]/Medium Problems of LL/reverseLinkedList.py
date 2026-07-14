# mypy: disable-error-code="empty-body"
# QUESTION: Reverse a Singly Linked List
# Given the head of a singly linked list, reverse the list and return the new head.
# Example 1:
# Input: 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0
# Output: 0 -> 1 -> 5 -> 7 -> 6 -> 4 -> 2
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Push every node's data onto a stack while traversing.
2. Traverse again from head, popping the stack to overwrite each node's data.
TC -> O(2n), SC -> O(n) for the stack.

#Better Approach:
SKIPPED — the iterative pointer-reversal below is optimal; no distinct middle tier.

#Optimal Approach (iterative):
1. Keep prev = None and curr = head.
2. For each node save front = curr.next, redirect curr.next = prev, then slide
   prev = curr and curr = front.
3. When curr is None, prev is the new head.
TC -> O(n), SC -> O(1).
(A recursive variant that reverses head.next then flips the back link is also provided;
same O(n) time but O(n) call-stack space.)

#KEY INSIGHT:
- Reversing is just flipping each node's next pointer to its predecessor; carrying a
  `prev` pointer lets one linear pass do it in place with no extra structure.
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

    def reverseLinkedList_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        stack: List[int] = []
        temp: Optional[Node] = head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next
        return head

    def reverseLinkedList_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: iterative in-place reversal is optimal; no distinct middle tier
        pass

    def reverseLinkedList_optimal(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        prev: Optional[Node] = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def reverseRecursive(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        newHead = self.reverseRecursive(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.reverseLinkedList_optimal(head)
    sol.printLinkedList(head)
