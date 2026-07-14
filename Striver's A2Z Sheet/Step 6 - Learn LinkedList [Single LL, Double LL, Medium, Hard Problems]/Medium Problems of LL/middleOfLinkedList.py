# mypy: disable-error-code="empty-body"
# QUESTION: Middle of the Linked List
# Given the head of a singly linked list, return the middle node. If there are two
# middle nodes (even length), return the second one.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: node with value 3
# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# Output: node with value 4  (the second middle)
# Constraints:
# 1 <= number of nodes <= 10^5

"""
#Brute Force:
1. Traverse once counting nodes to get length n.
2. Compute mid = n // 2 + 1 (1-indexed second-middle for even n).
3. Traverse again to that position and return the node.
TC -> O(n + n/2), SC -> O(1).

#Better Approach:
SKIPPED — the two-pass count method is the naive one; the next step is directly optimal.

#Optimal Approach:
1. Use slow and fast pointers, both starting at head.
2. Advance slow by one and fast by two each step while fast and fast.next exist.
3. When fast falls off the end, slow sits exactly on the middle (second middle for even n).
TC -> O(n/2), SC -> O(1).

#KEY INSIGHT:
- The tortoise-and-hare speed ratio (1x vs 2x) makes the slow pointer land on the middle
  in a single pass, avoiding the separate length count.
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

    def middleOfLinkedList_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        cnt = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            cnt += 1
        mid = cnt // 2 + 1
        temp = head
        cnt = 1
        while cnt != mid and temp is not None:
            cnt += 1
            temp = temp.next
        return temp

    def middleOfLinkedList_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: two-pass count is the naive tier; next step is optimal
        pass

    def middleOfLinkedList_optimal(self, head: Optional[Node]) -> Optional[Node]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    head = sol.convertArr2LL(arr)
    mid = sol.middleOfLinkedList_optimal(head)
    print(mid.data if mid is not None else None)
