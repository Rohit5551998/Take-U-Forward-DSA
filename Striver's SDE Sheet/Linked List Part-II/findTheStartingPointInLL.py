# QUESTION: Find the starting point in LL
# Given the head of a linked list that may contain a cycle, return the starting point of that cycle. If there is no cycle in the linked list return null.


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
    def find_the_starting_point_in_ll_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    def find_the_starting_point_in_ll_better(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    def find_the_starting_point_in_ll_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    # To test a cycle, wire the tail's next back to a node, e.g. tail.next = head.next
    # start = sol.find_the_starting_point_in_ll_optimal(head)
    # print(start.val if start else None)
