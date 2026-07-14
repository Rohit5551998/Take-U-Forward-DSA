# mypy: disable-error-code="empty-body"
# QUESTION: Add 1 to a Number Represented as a Linked List
# A non-negative integer is stored as a singly linked list, most-significant digit first
# (one digit per node). Add 1 to the number and return the head of the resulting list.
# Example 1:
# Input: 1 -> 5 -> 9
# Output: 1 -> 6 -> 0
# Example 2:
# Input: 9 -> 9 -> 9 -> 9
# Output: 1 -> 0 -> 0 -> 0 -> 0
# Constraints:
# 1 <= number of nodes <= 10^5
# 0 <= node.data <= 9

"""
#Brute Force:
1. Reverse the list so the least-significant digit is first.
2. Add 1 to the head, propagating carries (a 10 becomes 0 and carries to the next node).
3. Reverse back; if a carry remains, prepend a new node holding 1.
TC -> O(3n), SC -> O(1).

#Better Approach:
SKIPPED — the recursive backward carry below is the cleaner optimal; no distinct middle tier.

#Optimal Approach (recursive carry from the tail):
1. Recurse to the end of the list; the base case (past the tail) returns carry 1 (the +1).
2. On the way back, add the incoming carry to the current node; if it becomes 10 set it to
   0 and return carry 1, else return carry 0.
3. If the outermost call still has a carry, prepend a new head node holding 1.
TC -> O(n), SC -> O(n) recursion stack.

#KEY INSIGHT:
- Recursion lets us process digits from least-significant (the tail) back to the head
  without reversing the list; the returned value threads the carry upward automatically.
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

    def calculateCarry(self, head: Optional[Node]) -> int:
        if head is None:
            return 1
        carry = self.calculateCarry(head.next)
        head.data += carry
        if head.data == 10:
            head.data = 0
            return 1
        return 0

    def add1toList_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: reverse-add-reverse method is naive; recursive carry is optimal
        pass

    def add1toList_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no distinct middle tier
        pass

    def add1toList_optimal(self, head: Optional[Node]) -> Optional[Node]:
        carry = self.calculateCarry(head)
        if carry == 1:
            newHead = Node(1)
            newHead.next = head
            head = newHead
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [9, 9, 9, 9]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.add1toList_optimal(head)
    sol.printLinkedList(head)
