# mypy: disable-error-code="empty-body"
# QUESTION: Copy List with Random Pointer
# A linked list of length n is given where each node contains an additional
# `random` pointer that can point to any node in the list or to null. Construct a
# deep copy of the list: the copy must consist of exactly n brand-new nodes whose
# `next` and `random` pointers mirror the originals but point only into the copied
# list (never back into the original).
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#   (each pair is [val, index-that-random-points-to])
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Constraints:
# - 0 <= n <= 1000
# - -10^4 <= Node.val <= 10^4
# - random points to a node in the list or is null

"""
#Brute Force:
1. First pass: traverse the original list and create a clone for every node,
   storing original -> clone in a hash map.
2. Second pass: for each original node, wire the clone's `next` and `random` by
   looking up the mapped clones (map[curr.next], map[curr.random]).
3. Return the clone of the head.
TC -> O(2N), SC -> O(N) map + O(N) new nodes.

#Better Approach:
SKIPPED — the hash-map version is already the natural intermediate; the only
step up is dropping the map entirely (the interleaving trick below).

#Optimal Approach:
1. Interleave: for each original node create a clone and insert it immediately
   after its original (A -> A' -> B -> B' -> ...). Now every clone sits right
   next to its source.
2. Set random pointers: for each original `curr`, the clone is `curr.next`, and
   the node its random should point to is `curr.random.next` (the clone of the
   random target). Handle null random.
3. Detach: walk the interleaved list separating originals from clones, restoring
   the original list's `next` links and extracting the pure clone list.
4. Return the clone head.
TC -> O(3N), SC -> O(N) for the new nodes only (no extra map).

#KEY INSIGHT:
- Placing each clone directly after its original removes the need for a hash map:
  the clone of any node X is always reachable as X.next, so X.random.next is
  exactly the clone that X's copy should point to.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1
        self.random: Optional["Node"] = None


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

    def cloneLLWithRandomPointer_brute(self, head: Optional[Node]) -> Optional[Node]:
        hashMap: dict[Node, Node] = {}
        curr = head
        while curr is not None:
            hashMap[curr] = Node(curr.data)
            curr = curr.next

        newHead = Node(-1)
        curr = head
        res = newHead
        while curr is not None:
            res.next = hashMap[curr]
            res.next.random = hashMap[curr.random] if curr.random is not None else None
            curr = curr.next
            res = res.next
        return newHead.next

    def cloneLLWithRandomPointer_better(self) -> None:
        # SKIP: hash-map version is the natural middle; only step up is the interleave trick.
        pass

    def cloneLLWithRandomPointer_optimal(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        # 1. Interleave clones after each original node.
        curr: Optional[Node] = head
        while curr is not None:
            newNode = Node(curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        # 2. Assign random pointers of clones.
        curr = head
        while curr is not None:
            curr.next.random = (  # type: ignore[union-attr]
                curr.random.next if curr.random is not None else None
            )
            curr = curr.next.next  # type: ignore[union-attr]

        # 3. Detach clone list from original.
        curr = head
        newHead = Node(-1)
        res = newHead
        while curr is not None:
            res.next = curr.next
            curr.next = curr.next.next  # type: ignore[union-attr]
            res = res.next
            curr = curr.next
        return newHead.next


if __name__ == "__main__":
    sol = Solution()
    head = sol.convertArr2LL([7, 13, 11, 10, 1])
    # wire some random pointers on the original
    if head and head.next:
        head.next.random = head  # 13 -> 7
    cloned = sol.cloneLLWithRandomPointer_optimal(head)
    sol.printLinkedList(cloned)
