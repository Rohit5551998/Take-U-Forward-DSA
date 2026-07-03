# QUESTION: Delete Node in a Linked List O(1)
# Write a function to delete a node in a singly linked list. You will not be given access to the
# head of the list; instead, you will be given access to the node to be deleted directly.
# It is guaranteed that the given node is not the tail node (it has a successor). After deletion,
# the value of the given node should no longer exist in the list, the number of nodes should
# decrease by one, and the relative order of all other nodes should stay the same.
#
# Examples:
# Example 1:
# Input: list = 1 -> 4 -> 2 -> 3, node = 2
# Output: 1 -> 4 -> 3
# Explanation: The node with value 2 is deleted from the given linked list.
#
# Example 2:
# Input: list = 1 -> 2 -> 3 -> 4, node = 1
# Output: 2 -> 3 -> 4
# Explanation: The node with value 1 (the head) is deleted from the given linked list.


"""
#Brute Force:
SKIPPED — there is no naive tier: you are given ONLY the node, not the head, so you
can't even traverse to find its predecessor. The single O(1) trick below is the only
approach.

#Better Approach:
SKIPPED — same reason; no distinct intermediate exists for this problem.

#Optimal Approach:
1. We can't unlink `node` directly: there's no head/prev reference to reach the node
   before it, and rebinding the local `node` would change only the name, not the list.
2. Trick — instead of removing `node`, make `node` BECOME its successor. Copy
   node.next.val into node.val, so this node now carries the next node's data.
3. Then bypass the now-duplicate successor with node.next = node.next.next. Reading the
   list from the head, it looks exactly as if `node` had been deleted (its old value is
   gone, the successor is skipped).
4. This relies on node being guaranteed non-tail, so node.next always exists. It's a
   fixed number of pointer assignments with no traversal, hence constant time.
TC -> O(1), SC -> O(1)

#KEY INSIGHT:
- With only a node reference (no head, no prev), you cannot unlink the node itself —
  but overwriting it with its successor's value and dropping the successor is
  observationally identical to deleting it. This needs the non-tail guarantee, since a
  tail has no successor to copy from.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for value in values:
        node = ListNode(value)
        curr.next = node
        curr = node
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    # Only the node to delete is given (no head); it is never the tail node.
    def delete_node_in_a_linked_list_o_one_brute(self, node: ListNode) -> None:
        # SKIP: only the node is given (no head), so there's no traversal-based naive
        # version — the O(1) copy-and-unlink trick is the only approach.
        pass

    def delete_node_in_a_linked_list_o_one_better(self, node: ListNode) -> None:
        # SKIP: no distinct intermediate tier for this problem.
        pass

    def delete_node_in_a_linked_list_o_one_optimal(self, node: ListNode) -> None:
        # Guaranteed not the tail, so node.next always exists: overwrite this node
        # with its successor's value, then unlink the successor.
        node.val = node.next.val  # type: ignore[union-attr]
        node.next = node.next.next  # type: ignore[union-attr]


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 4, 2, 3])
    assert head is not None and head.next is not None and head.next.next is not None
    node_to_delete = head.next.next  # the node holding value 2
    sol.delete_node_in_a_linked_list_o_one_optimal(node_to_delete)
    print(to_list(head))
