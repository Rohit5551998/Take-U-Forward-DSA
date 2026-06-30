# mypy: disable-error-code="empty-body"
# QUESTION: Check if LL is palindrome or not
# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the lef.
#
# Examples:
# Example 1:
# Input: head -> 3 -> 7 -> 5 -> 7 -> 3
# Output: true
# Explanation: 37573 is a palindrome.
#
# Example 2:
# Input: head -> 1 -> 1 -> 2 -> 1
# Output: false
# Explanation: 1121 is not a palindrome.


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
    def check_if_ll_is_palindrome_or_not_brute(self, head: Optional[ListNode]) -> bool:
        pass

    def check_if_ll_is_palindrome_or_not_better(self, head: Optional[ListNode]) -> bool:
        pass

    def check_if_ll_is_palindrome_or_not_optimal(self, head: Optional[ListNode]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([3, 7, 5, 7, 3])
    # print(sol.check_if_ll_is_palindrome_or_not_optimal(head))
