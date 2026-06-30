# QUESTION: Find the intersection point of Y LL
# Given the heads of two singly linked-lists headA and headB , return the node at which the two lists intersect . If the two linked lists have no intersection at all, return null.
#
# Examples:
# Example 1:
# Input:
# List 1 = [1,3,1,2,4], List 2 = [3,2,4]
# Output:
# 2
# Explanation: Here, both lists intersecting nodes start from node 2.
#
#  Example 2:
# Input:
#  List1 = [1,2,7], List 2 = [2,8,1]
# Output:
#  Null
# Explanation: Here, both lists do not intersect and thus no intersection node is present.


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
    def find_the_intersection_point_of_y_ll_brute(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    def find_the_intersection_point_of_y_ll_better(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    def find_the_intersection_point_of_y_ll_optimal(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head_a = build_linked_list([1, 3, 1, 2, 4])
    head_b = build_linked_list([3, 2, 4])
    # To test a real intersection, point head_b's tail to a shared node in head_a.
    # node = sol.find_the_intersection_point_of_y_ll_optimal(head_a, head_b)
    # print(node.val if node else None)
