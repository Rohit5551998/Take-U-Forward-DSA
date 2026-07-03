# QUESTION: Clone a LL with random and next pointer
# Given the head of a special linked list of n nodes where each node contains an additional
# pointer called 'random' which can point to any node in the list or null.
# Construct a deep copy of the linked list where:
# - n new nodes are created with corresponding values as the original linked list.
# - The random pointers point to the corresponding new nodes as per their arrangement in the
#   original list.
# - Return the head of the newly constructed linked list.
# Note: For custom input, an n x 2 matrix is taken with each row having 2 values
# [val, random_index] where:
# - val: an integer representing ListNode.val
# - random_index: index of the node (0 to n-1) that the random pointer points to, otherwise -1.
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
#
# Constraints:
# - n == number of nodes in the linked list.
# - 1 <= n <= 10^5
# - -10^4 <= ListNode.val <= 10^4
# - 0 <= random_index < n or random_index == -1.


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

from typing import List, Optional, Set


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


def build_linked_list_with_random(pairs: List[List[int]]) -> Optional[Node]:
    # Each pair is [val, random_index] (LeetCode 138 style); index -1 means random is None.
    # Nodes are created first, then random pointers are wired by index so forward
    # references (e.g. [3, 4] pointing at the 5th node) work.
    dummy = Node()
    curr = dummy
    nodes: List[Node] = []
    for pair in pairs:
        node = Node(pair[0])
        nodes.append(node)
        curr.next = node
        curr = node
    for node, pair in zip(nodes, pairs):
        if pair[1] != -1:
            node.random = nodes[pair[1]]
    return dummy.next


def to_pairs(head: Optional[Node]) -> List[List[int]]:
    # Serialize back to [val, random_index] pairs — comparable across two lists
    # even though the node objects differ.
    nodes: List[Node] = []
    temp = head
    while temp is not None:
        nodes.append(temp)
        temp = temp.next
    index_of = {id(node): i for i, node in enumerate(nodes)}
    # A random pointing OUTSIDE this list (e.g. a bad clone referencing original
    # nodes) maps to -2 so it can never match a valid index or -1.
    return [
        [node.val, index_of.get(id(node.random), -2) if node.random is not None else -1]
        for node in nodes
    ]


def is_deep_clone(original: Optional[Node], clone: Optional[Node]) -> bool:
    # True only if values + random wiring match AND no node object is shared —
    # a clone whose random pointers still reference the ORIGINAL nodes must fail.
    if to_pairs(original) != to_pairs(clone):
        return False
    original_ids: Set[int] = set()
    temp = original
    while temp is not None:
        original_ids.add(id(temp))
        temp = temp.next
    temp = clone
    while temp is not None:
        if id(temp) in original_ids or (
            temp.random is not None and id(temp.random) in original_ids
        ):
            return False
        temp = temp.next
    return True


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
    head = build_linked_list_with_random([[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]])
    # clone = sol.clone_a_ll_with_random_and_next_pointer_optimal(head)
    # print(to_pairs(clone), is_deep_clone(head, clone))  # expect: same pairs, True
