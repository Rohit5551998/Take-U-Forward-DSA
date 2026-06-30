# QUESTION: Rotate a LL
# Given the head of a singly linked list containing integers, shift the elements of the linked list to the right by k places and return the head of the modified list. Do not change.
#
# Examples:
# Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output : head -> 4 -> 5 -> 1 -> 2 -> 3
# Explanation :List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
# List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.
#
# Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 4
# Output :head -> 2 -> 3 -> 4 -> 5 -> 1
# Explanation :List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
# List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.
# List after 3 shift to right: head -> 3 -> 4 -> 5 -> 1 -> 2.
# List after 4 shift to right: head -> 2 -> 3 -> 4 -> 5 -> 1.


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
    def rotate_a_ll_brute(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

    def rotate_a_ll_better(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

    def rotate_a_ll_optimal(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    # print(to_list(sol.rotate_a_ll_optimal(head, k)))
