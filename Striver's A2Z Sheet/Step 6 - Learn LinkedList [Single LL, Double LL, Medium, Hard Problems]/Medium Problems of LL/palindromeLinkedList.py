# mypy: disable-error-code="empty-body"
# QUESTION: Check if a Linked List is a Palindrome
# Given the head of a singly linked list, return True if the sequence of node values
# reads the same forwards and backwards, otherwise False.
# Example 1:
# Input: 1 -> 2 -> 3 -> 2 -> 1
# Output: True
# Example 2:
# Input: 1 -> 2 -> 3 -> 4
# Output: False
# Constraints:
# 1 <= number of nodes <= 10^5

"""
#Brute Force:
1. Traverse the list pushing every value onto a stack.
2. Traverse again from head; each value must equal the popped (reversed) value.
3. Any mismatch -> False; otherwise True.
TC -> O(2n), SC -> O(n).

#Better Approach:
SKIPPED — the reverse-second-half method is optimal; no distinct middle tier.

#Optimal Approach:
1. Find the first-middle with slow/fast (loop while fast.next and fast.next.next exist).
2. Reverse the second half (slow.next) and compare it node-by-node against the front half.
3. Any value mismatch -> False.
4. Restore the list by reversing the second half back, then return the result.
TC -> O(2n), SC -> O(1).

#KEY INSIGHT:
- Reversing only the second half turns the palindrome check into a two-pointer walk from
  both ends, using no extra storage; restoring the half afterward leaves the list intact.
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

    def reverseLinkedList(self, head: Optional[Node]) -> Optional[Node]:
        prev: Optional[Node] = None
        curr = head
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def palindromeLinkedList_brute(self, head: Optional[Node]) -> bool:
        stack: List[int] = []
        temp = head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            if temp.data != stack.pop():
                return False
            temp = temp.next
        return True

    def palindromeLinkedList_better(self, head: Optional[Node]) -> bool:
        # SKIP: reverse-second-half is optimal; no distinct middle tier
        pass

    def palindromeLinkedList_optimal(self, head: Optional[Node]) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
        newHead = self.reverseLinkedList(slow.next)
        first: Optional[Node] = head
        second: Optional[Node] = newHead
        resp = True
        while second is not None:
            if first is None or first.data != second.data:
                resp = False
                break
            first = first.next
            second = second.next
        self.reverseLinkedList(newHead)
        return resp


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 2, 1]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    print(sol.palindromeLinkedList_optimal(head))
    sol.printLinkedList(head)
