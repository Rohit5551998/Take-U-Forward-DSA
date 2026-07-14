# mypy: disable-error-code="empty-body"
# QUESTION: Sort a Linked List
# Given the head of a singly linked list, sort it in ascending order and return the head.
# Example 1:
# Input: 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 0
# Output: 0 -> 1 -> 2 -> 4 -> 5 -> 6 -> 7
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Traverse the list collecting all values into an array.
2. Sort the array, then overwrite each node's data in order.
TC -> O(N) + O(N log N) + O(N), SC -> O(N).

#Better Approach:
SKIPPED — merge sort on the list itself is the intended optimal; no distinct middle tier.

#Optimal Approach (merge sort on the list):
1. Base case: 0 or 1 node is already sorted -> return head.
2. Split at the first-middle (slow/fast); cut the list into left and right halves.
3. Recursively sort both halves.
4. Merge the two sorted halves with a dummy-node merge and return the merged head.
TC -> O(N log N), SC -> O(log N) recursion depth (O(1) auxiliary structures).

#KEY INSIGHT:
- Merge sort suits linked lists because splitting and merging only re-link pointers — no
  random access or extra array is needed, giving O(N log N) with in-place merging.
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

    def middleElement(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
        return slow

    def mergeLL(self, left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        temp = dummy
        while left is not None and right is not None:
            if left.data <= right.data:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = right if left is None else left
        return dummy.next

    def sortLL_brute(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        vals: List[int] = []
        temp: Optional[Node] = head
        while temp is not None:
            vals.append(temp.data)
            temp = temp.next
        vals.sort()
        temp = head
        i = 0
        while temp is not None:
            temp.data = vals[i]
            i += 1
            temp = temp.next
        return head

    def sortLL_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: merge sort is the intended optimal; no distinct middle tier
        pass

    def sortLL_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        mid = self.middleElement(head)
        leftHead = head
        rightHead = mid.next  # type: ignore[union-attr]
        mid.next = None  # type: ignore[union-attr]
        leftHead = self.sortLL_optimal(leftHead)
        rightHead = self.sortLL_optimal(rightHead)
        return self.mergeLL(leftHead, rightHead)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.sortLL_optimal(head)
    sol.printLinkedList(head)
