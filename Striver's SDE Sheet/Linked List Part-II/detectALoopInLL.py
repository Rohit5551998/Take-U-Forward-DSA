# mypy: disable-error-code="empty-body"
# QUESTION: Detect a loop in LL
# Given a Linked List, determine whether the linked list contains a cycle or not.
#
# Examples:
# Input: LL: 1 2 3 4 5
#
# Output: True
# Explanation: The last node with the value of 5 has its 'next' pointer pointing back to a previous node with the value of 3. This has resulted in a loop, hence we return true.
#
# Input: LL: 1 2 3 4 9 9
#
# Output: False
# Explanation: In this example, the linked list does not have a loop hence returns false.


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
    def detect_a_loop_in_ll_brute(self, head: Optional[ListNode]) -> bool:
        pass

    def detect_a_loop_in_ll_better(self, head: Optional[ListNode]) -> bool:
        pass

    def detect_a_loop_in_ll_optimal(self, head: Optional[ListNode]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    # To test a loop, wire the tail's next back to an earlier node.
    # print(sol.detect_a_loop_in_ll_optimal(head))
