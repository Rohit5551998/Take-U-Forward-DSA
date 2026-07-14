# mypy: disable-error-code="empty-body"
# QUESTION: Detect a Loop / Cycle in a Linked List
# Given the head of a singly linked list, return True if the list contains a cycle
# (some node's next points back to an earlier node), otherwise False.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4, where node 4's next points back to node 3
# Output: True
# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> None
# Output: False
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Walk the list storing each visited node (by identity) in a hash set/map.
2. If a node is seen a second time before reaching None, there is a cycle -> return True.
3. Reaching None means no cycle -> return False.
TC -> O(n), SC -> O(n) for the map.

#Better Approach:
SKIPPED — the hashing tier is the only intermediate; the next step is directly optimal.

#Optimal Approach (Floyd's cycle detection):
1. Move slow by one and fast by two while fast and fast.next exist.
2. If they ever point to the same node, a cycle exists -> return True.
3. If fast runs off the end, the list is acyclic -> return False.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Inside a cycle the faster pointer gains one node per step on the slower one, so they are
  guaranteed to collide — detecting the loop with no extra memory.
"""

from typing import Dict, List, Optional


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

    def detectLoop_brute(self, head: Optional[Node]) -> bool:
        hashMap: Dict[Node, int] = {}
        temp = head
        while temp is not None:
            if temp in hashMap:
                return True
            hashMap[temp] = 1
            temp = temp.next
        return False

    def detectLoop_better(self, head: Optional[Node]) -> bool:
        # SKIP: hashing is the only intermediate tier; next step is optimal
        pass

    def detectLoop_optimal(self, head: Optional[Node]) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 2, 1]
    head = sol.convertArr2LL(arr)
    # Wire a cycle: last node -> node with value 3.
    if head is not None:
        head.next.next.next.next = head.next.next  # type: ignore[union-attr]
    print(sol.detectLoop_optimal(head))
