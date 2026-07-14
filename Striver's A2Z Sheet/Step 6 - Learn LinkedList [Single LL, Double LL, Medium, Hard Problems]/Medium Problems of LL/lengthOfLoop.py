# mypy: disable-error-code="empty-body"
# QUESTION: Length of the Loop in a Linked List
# Given the head of a singly linked list, return the number of nodes in the cycle if one
# exists, otherwise 0.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5, where node 5's next points back to node 3
# Output: 3   (the loop 3 -> 4 -> 5 -> 3 has 3 nodes)
# Example 2:
# Input: 1 -> 2 -> 3 -> None
# Output: 0
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Walk the list storing each node in a hash map alongside its 1-based visit index.
2. When a node repeats, the loop length is currentIndex - storedIndex -> return it.
3. Reaching None means no loop -> return 0.
TC -> O(n), SC -> O(n).

#Better Approach:
SKIPPED — hashing is the only intermediate tier; the next step is directly optimal.

#Optimal Approach (Floyd's meeting point):
1. Advance slow by one and fast by two until they collide inside the loop (or fast exits).
2. From the collision node, keep one pointer fixed and walk the other around the loop,
   counting steps until it returns to the collision node.
3. That count is the loop length.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Once the two pointers meet, they are both on the cycle, so one full lap back to the
  meeting node directly measures the cycle's length with no extra memory.
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

    def lengthOfLoop_brute(self, head: Optional[Node]) -> int:
        hashMap: Dict[Node, int] = {}
        cnt = 1
        temp = head
        while temp is not None:
            if temp in hashMap:
                return cnt - hashMap[temp]
            hashMap[temp] = cnt
            cnt += 1
            temp = temp.next
        return 0

    def lengthOfLoop_better(self, head: Optional[Node]) -> int:
        # SKIP: hashing is the only intermediate tier; next step is optimal
        pass

    def lengthOfLoop_optimal(self, head: Optional[Node]) -> int:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next
            if slow == fast:
                cnt = 1
                fast = fast.next  # type: ignore[union-attr]
                while slow != fast:
                    fast = fast.next  # type: ignore[union-attr]
                    cnt += 1
                return cnt
        return 0


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 2, 1]
    head = sol.convertArr2LL(arr)
    # Wire a cycle so the last node points back to node index 2.
    if head is not None:
        head.next.next.next.next.next = head.next.next  # type: ignore[union-attr]
    print(sol.lengthOfLoop_optimal(head))
