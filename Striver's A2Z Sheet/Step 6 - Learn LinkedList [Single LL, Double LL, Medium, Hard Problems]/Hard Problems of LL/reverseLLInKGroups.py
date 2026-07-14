# mypy: disable-error-code="empty-body"
# QUESTION: Reverse Nodes in K-Group
# Given the head of a singly linked list and an integer k, reverse the nodes of
# the list k at a time and return the modified list. k is a positive integer
# and less than or equal to the length of the linked list. If the number of
# nodes is not a multiple of k, then the left-out nodes at the end should remain
# in their original order.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Explanation: Nodes [1,2] -> [2,1], nodes [3,4] -> [4,3]; node 5 is a <k group so it stays.
# Constraints:
# - 1 <= number of nodes <= 5000
# - 0 <= Node.val <= 1000
# - 1 <= k <= number of nodes

"""
#Brute Force:
SKIPPED — the accepted approach is the in-place group reversal; a copy-to-array
brute (collect values, reverse each k-block, rebuild) is not a distinct
linked-list algorithm and defeats the purpose of the problem.

#Better Approach:
SKIPPED — there is no meaningful intermediate tier between "no reversal" and the
optimal in-place group reversal.

#Optimal Approach:
1. Walk `temp` from the head. For each block, find the k-th node from `temp`
   with getKthNode (advances k-1 steps). If it returns None the block is
   incomplete.
2. If incomplete, we must leave the tail untouched: reattach the previous
   group's tail (`prevNode`) to `temp` and stop, so the remainder keeps its
   original order.
3. Otherwise remember `nextNode = kthNode.next`, cut the block off by setting
   `kthNode.next = None`, then reverse that isolated block. After reversal the
   old `temp` is the block's tail and `kthNode` is its head.
4. Rewire: for the first block the new list head becomes `kthNode`; otherwise
   the previous group's tail `prevNode.next` points to `kthNode`.
5. Advance `prevNode = temp` (this group's new tail) and `temp = nextNode`.
TC -> O(2n), SC -> O(1)

#KEY INSIGHT:
- Isolate each k-node segment by nulling its tail so a plain list reverse works
  on it, then splice the reversed segment back between the previous group's tail
  and the next group's head. The <k trailing remainder is detected by
  getKthNode returning None and is deliberately left in original order.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def convertArr2LL(self, arr: list[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None)
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverseLinkedList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def getKthNode(self, temp: Optional[Node], k: int) -> Optional[Node]:
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseLLInKGroups_brute(self) -> None:
        # SKIP: copy-to-array reversal is not a distinct linked-list algorithm.
        pass

    def reverseLLInKGroups_better(self) -> None:
        # SKIP: no meaningful tier between naive and in-place group reversal.
        pass

    def reverseLLInKGroups_optimal(self, head: Optional[Node], k: int) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        temp: Optional[Node] = head
        prevNode: Optional[Node] = None

        while temp is not None:
            kthNode = self.getKthNode(temp, k)

            if kthNode is None:
                # Incomplete trailing group: leave it in original order.
                if prevNode:
                    prevNode.next = temp
                break

            nextNode = kthNode.next
            kthNode.next = None

            self.reverseLinkedList(temp)

            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode  # type: ignore[union-attr]

            prevNode = temp
            temp = nextNode

        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0, 10, 9, 3]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.reverseLLInKGroups_optimal(head, 3)
    sol.printLinkedList(head)
