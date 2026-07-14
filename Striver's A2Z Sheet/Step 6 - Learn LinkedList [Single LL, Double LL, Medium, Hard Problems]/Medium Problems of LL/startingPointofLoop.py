# mypy: disable-error-code="empty-body"
# QUESTION: Find the Starting Point of a Loop in a Linked List
# Given the head of a singly linked list, return the node where the cycle begins.
# If there is no cycle, return None.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5, where node 5's next points back to node 3
# Output: node with value 3
# Example 2:
# Input: 1 -> 2 -> 3 -> None
# Output: None
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Walk the list storing each node (by identity) in a hash map.
2. The first node encountered that is already in the map is the loop's start -> return it.
3. Reaching None means no cycle -> return None.
TC -> O(n), SC -> O(n).

#Better Approach:
SKIPPED — hashing is the only intermediate tier; the next step is directly optimal.

#Optimal Approach (Floyd's algorithm):
1. Advance slow by one and fast by two until they meet (a cycle exists) or fast falls off.
2. On collision, reset slow to head and move both slow and fast one step at a time.
3. They meet again exactly at the loop's starting node -> return it.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- The distance from head to the loop start equals the distance from the meeting point to
  the loop start (mod loop length), so restarting one pointer at head makes them converge
  precisely at the cycle's entry.
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

    def startingPointOfLoop_brute(self, head: Optional[Node]) -> Optional[Node]:
        hashMap: Dict[Node, int] = {}
        temp = head
        while temp is not None:
            if temp in hashMap:
                return temp
            hashMap[temp] = 1
            temp = temp.next
        return None

    def startingPointOfLoop_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: hashing is the only intermediate tier; next step is optimal
        pass

    def startingPointOfLoop_optimal(self, head: Optional[Node]) -> Optional[Node]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next  # type: ignore[union-attr]
                    fast = fast.next  # type: ignore[union-attr]
                return slow
        return None


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2]
    head = sol.convertArr2LL(arr)
    # Wire a cycle: last node -> head.
    if head is not None:
        head.next.next = head  # type: ignore[union-attr]
    start = sol.startingPointOfLoop_optimal(head)
    print(start.data if start is not None else None)
