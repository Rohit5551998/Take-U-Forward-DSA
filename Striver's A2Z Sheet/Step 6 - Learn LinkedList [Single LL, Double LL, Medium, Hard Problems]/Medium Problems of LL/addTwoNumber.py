# mypy: disable-error-code="empty-body"
# QUESTION: Add Two Numbers Represented as Linked Lists
# Two non-negative integers are stored as singly linked lists with the least-significant
# digit first (one digit per node). Add them and return the sum as a new linked list in
# the same least-significant-first order.
# Example 1:
# Input: l1 = 2 -> 4 -> 3  (342),  l2 = 5 -> 6 -> 4  (465)
# Output: 7 -> 0 -> 8       (807)
# Constraints:
# 1 <= nodes in each list <= 10^5
# 0 <= node.data <= 9

"""
#Brute Force:
SKIPPED — building the sum digit-by-digit in one pass is already the direct method; there
is no slower naive variant worth contrasting.

#Better Approach:
SKIPPED — no intermediate tier exists.

#Optimal Approach:
1. Use a dummy head and a carry initialized to 0; walk both lists together.
2. At each step take el1/el2 (0 when a list is exhausted), compute sum = el1 + el2 + carry,
   append a node with sum % 10, and set carry = sum // 10.
3. After the loop, if carry > 0 append one final node holding the carry.
4. Return dummy.next.
TC -> O(max(m, n)), SC -> O(max(m, n)) for the result list.

#KEY INSIGHT:
- Least-significant-first storage means we can add left to right exactly like grade-school
  addition, carrying forward as we build the result in a single synchronized pass.
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

    def addTwoNumbers_brute(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        # SKIP: single-pass digit addition is the only meaningful approach
        pass

    def addTwoNumbers_better(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        # SKIP: no intermediate tier exists
        pass

    def addTwoNumbers_optimal(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        temp = dummy
        carry = 0
        curr1, curr2 = head1, head2
        while curr1 is not None or curr2 is not None:
            el1 = curr1.data if curr1 is not None else 0
            el2 = curr2.data if curr2 is not None else 0
            total = el1 + el2 + carry
            carry = total // 10
            temp.next = Node(total % 10)
            temp = temp.next
            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next
        if carry > 0:
            temp.next = Node(carry)
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head1 = sol.convertArr2LL([2, 4, 3])
    head2 = sol.convertArr2LL([5, 6, 4])
    sol.printLinkedList(head1)
    sol.printLinkedList(head2)
    head = sol.addTwoNumbers_optimal(head1, head2)
    sol.printLinkedList(head)
