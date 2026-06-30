# QUESTION: Delete Node in a Linked List O(1)
# Write a function to delete a node in a singly linked list. You will not be given access to the head of the list instead, you will be given access to the node to be deleted direct.
#
# Examples:
# Input : 1->4->2->3, Node = 2
# Output : 1->4->3
# Explanation : Node 2 is deleted from the given linked list.
#
# Input : 1->2->3->4, Node = 1
# Output : 2->3->4
# Explanation : Node 1 is deleted from the given linked list.


"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
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
        pass

    def delete_node_in_a_linked_list_o_one_better(self, node: ListNode) -> None:
        pass

    def delete_node_in_a_linked_list_o_one_optimal(self, node: ListNode) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 4, 2, 3])
    # node_to_delete = head.next.next  # the node holding value 2
    # sol.delete_node_in_a_linked_list_o_one_optimal(node_to_delete)
    # print(to_list(head))
