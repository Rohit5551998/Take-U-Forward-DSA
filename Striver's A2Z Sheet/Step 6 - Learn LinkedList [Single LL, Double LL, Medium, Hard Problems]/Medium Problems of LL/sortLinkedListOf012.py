# mypy: disable-error-code="empty-body"
# QUESTION: Sort a Linked List of 0s, 1s and 2s
# Given the head of a singly linked list whose node values are only 0, 1, or 2, sort it
# in non-decreasing order and return the head.
# Example 1:
# Input: 2 -> 2 -> 1 -> 1 -> 2 -> 0 -> 0
# Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> 2
# Constraints:
# 0 <= number of nodes <= 10^5
# node.data in {0, 1, 2}

"""
#Brute Force:
1. Count occurrences of 0, 1 and 2 in one pass.
2. Overwrite node values: cnt0 zeros, then cnt1 ones, then cnt2 twos.
TC -> O(2n), SC -> O(1).

#Better Approach:
SKIPPED — the three-chain link-rearrange method is optimal; no distinct middle tier.

#Optimal Approach:
1. Build three dummy-headed chains (zero, one, two) with their tails.
2. Walk the list once, detaching each node and appending it to the chain matching its value.
3. Link zero-tail -> one-head (or two-head if there are no ones), one-tail -> two-head,
   and return the zero chain's head.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Because there are only three distinct values, one pass that splices nodes into three
  buckets and then stitches the buckets together sorts the list in place without counting
  or comparisons between values.
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

    def sortLinkedListOf012_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: value-counting/overwrite method is naive; next step is optimal
        pass

    def sortLinkedListOf012_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no distinct middle tier
        pass

    def sortLinkedListOf012_optimal(self, head: Optional[Node]) -> Optional[Node]:
        zeroHead, oneHead, twoHead = Node(-1), Node(-1), Node(-1)
        zeroTail, oneTail, twoTail = zeroHead, oneHead, twoHead
        curr = head
        while curr is not None:
            temp = curr
            if curr.data == 0:
                zeroTail.next = temp
                zeroTail = zeroTail.next
            elif curr.data == 1:
                oneTail.next = temp
                oneTail = oneTail.next
            else:
                twoTail.next = temp
                twoTail = twoTail.next
            curr = curr.next
            temp.next = None
        zeroTail.next = oneHead.next if oneHead.next is not None else twoHead.next
        oneTail.next = twoHead.next
        return zeroHead.next


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 2, 1, 1, 2, 0, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.sortLinkedListOf012_optimal(head)
    sol.printLinkedList(head)
