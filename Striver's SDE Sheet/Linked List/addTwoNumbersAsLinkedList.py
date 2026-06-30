# QUESTION: Add two numbers as LinkedList
# Add two numbers represented as Linked Lists.
#
# Examples:
# Example 1:
# Input: num1 = 243, num2 = 564
# Output:sum = 807; L = [7,0,8]
#
# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: Result: [8,9,9,9,0,0,0,1]
#
# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the original number and then add them as → 9999999 + 9999 = 8999001. Refer to the image below.


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
    def add_two_numbers_as_linkedlist_brute(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    def add_two_numbers_as_linkedlist_better(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    def add_two_numbers_as_linkedlist_optimal(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    # print(to_list(sol.add_two_numbers_as_linkedlist_optimal(l1, l2)))
