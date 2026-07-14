# mypy: disable-error-code="empty-body"
# QUESTION: Remove the N-th Node from the End of a Linked List
# Given the head of a singly linked list and an integer k, remove the k-th node counted
# from the end and return the head.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 1 -> 2 -> 3 -> 5   (the 2nd-from-end node, value 4, is removed)
# Example 2:
# Input: 1 -> 2, k = 2
# Output: 2   (removing the head)
# Constraints:
# 1 <= number of nodes <= 10^5
# 1 <= k <= number of nodes

"""
#Brute Force:
1. Count the list length L in one pass.
2. If k == L the target is the head -> return head.next.
3. Walk to node L-k, then bypass its next pointer.
TC -> O(L) + O(L-k), SC -> O(1).

#Better Approach:
SKIPPED — the single-pass two-pointer method is optimal; no distinct middle tier.

#Optimal Approach:
1. Advance a fast pointer k steps ahead of head.
2. If fast is now None, the head itself is the target -> return head.next.
3. Move slow and fast together until fast.next is None; slow now sits just before the
   target, so bypass it via slow.next = slow.next.next.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Giving fast a k-node head start makes the gap between the pointers exactly k, so when
  fast reaches the tail, slow is parked on the node before the one to delete — one pass, no count.
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

    def removeNthFromEnd_brute(self, head: Optional[Node], k: int) -> Optional[Node]:
        # SKIP: length-count method is naive; next step is optimal
        pass

    def removeNthFromEnd_better(self, head: Optional[Node], k: int) -> Optional[Node]:
        # SKIP: no distinct middle tier
        pass

    def removeNthFromEnd_optimal(self, head: Optional[Node], k: int) -> Optional[Node]:
        cnt = 0
        fast: Optional[Node] = head
        slow: Optional[Node] = head
        while cnt < k and fast is not None:
            cnt += 1
            fast = fast.next
        if fast is None:
            return head.next if head is not None else None
        while fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next
        if slow is not None and slow.next is not None:
            slow.next = slow.next.next
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.removeNthFromEnd_optimal(head, 2)
    sol.printLinkedList(head)
