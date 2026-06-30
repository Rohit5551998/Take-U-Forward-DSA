# QUESTION: Clone a LL with random and next pointer
# Given a linked list where every node in the linked list contains two pointers: ‘next’ which points to the next node in the list. ‘random’ which points to a random node in.
#
# Examples:
# Example 1:
# Input: [[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]
# Output: 1 2 3 4 5, true
# Explanation: All the nodes in the new list have same corresponding values as original nodes.
# All the random pointers point to their corresponding nodes in the new list.
# 'true' represents that the nodes and references were created new.
#
# Example 2:
# Input: [[5, -1], [3, -1], [2, 1], [1, 1]]
# Output: 5 3 2 1, true
# Explanation: All the nodes in the new list have same corresponding values as original nodes.
# All the random pointers point to their corresponding nodes in the new list.
# 'true' represents that the nodes and references were created new.
# [[5, -1], [3, -1], [2, -1], [1, -1]] will be incorrect, although it has the same values.


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


class Node:
    def __init__(
        self,
        val: int = 0,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random


def build_linked_list(values: List[int]) -> Optional[Node]:
    # Builds the `next` chain only; wire `random` pointers manually for testing.
    dummy = Node()
    curr = dummy
    for value in values:
        node = Node(value)
        curr.next = node
        curr = node
    return dummy.next


def to_list(head: Optional[Node]) -> List[int]:
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def clone_a_ll_with_random_and_next_pointer_brute(self, head: Optional[Node]) -> Optional[Node]:
        pass

    def clone_a_ll_with_random_and_next_pointer_better(
        self, head: Optional[Node]
    ) -> Optional[Node]:
        pass

    def clone_a_ll_with_random_and_next_pointer_optimal(
        self, head: Optional[Node]
    ) -> Optional[Node]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    # Wire random pointers manually, e.g. head.random = head.next.next
    # print(to_list(sol.clone_a_ll_with_random_and_next_pointer_optimal(head)))
