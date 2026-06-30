# QUESTION: Reverse LL in group of given size K
# Given the head of a singly linked list containing integers, reverse the nodes of the list in groups of k and return the head of the modified list. If the number of nodes is not a.
#
# Examples:
# Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output :head -> 2 -> 1 -> 4 -> 3 -> 5
# Explanation :The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.
#
# Input :head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3
# Output :head -> 3 -> 2 -> 1 -> 4 -> 5
# Explanation :The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.
# Note that 4 -> 5 was not reversed.


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
    def reverse_ll_in_group_of_given_size_k_brute(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass

    def reverse_ll_in_group_of_given_size_k_better(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass

    def reverse_ll_in_group_of_given_size_k_optimal(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    # print(to_list(sol.reverse_ll_in_group_of_given_size_k_optimal(head, k)))
