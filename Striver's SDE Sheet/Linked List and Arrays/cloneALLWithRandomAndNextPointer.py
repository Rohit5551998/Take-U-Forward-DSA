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
1. The hard part of cloning is the random pointer: original.random points to
   some original node, but the copy must point to the CORRESPONDING copy. Solve
   that lookup with a hash map from original node -> its copy.
2. First pass: walk the list, create a bare copy (value only) for each original
   node, and record hashMap[original] = copy. No links wired yet — the copies
   of later nodes may not exist when an earlier random needs them.
3. Second pass: for each original, use the map to translate its next and random
   into the clone world — copy.next = hashMap[original.next] and
   copy.random = hashMap[original.random]. Because every copy already exists,
   both lookups always resolve.
4. Return hashMap[head] as the cloned head.
TC -> O(2n) ~ O(n) (two passes, O(1) average map ops),
SC -> O(n) for the hash map of n original->copy entries

#Better Approach:
SKIPPED — no distinct middle tier exists. The problem goes straight from the
O(n)-space hash-map clone to the O(1)-space interleaving trick; nothing
sensible sits in between.

#Optimal Approach:
1. Kill the hash map by encoding the original->copy mapping INTO the list
   itself: weave each copy in right after its original, so original.next is
   always its own copy.
2. Pass 1 (insert): for each original node, make a copy, splice it between the
   node and its successor (copy.next = temp.next; temp.next = copy), then jump
   two steps to the next original.
3. Pass 2 (wire randoms): now for any original temp, temp.next is its copy and
   temp.random.next is the copy of temp.random — exactly the node the clone's
   random must point to. So copy.random = temp.random.next (guarding None).
   This is the whole payoff of interleaving: the mapping lookup is now a single
   .next hop instead of a hash lookup.
4. Pass 3 (detach): un-weave the two lists. For each original, re-link
   temp.next to the following ORIGINAL (front = temp.next.next) and link the
   copy to the following COPY (copy.next = front.next). This both extracts the
   clone AND restores the original list to its input state.
5. Return the head of the extracted copy list.
TC -> O(3n) ~ O(n) (three linear passes), SC -> O(1) (only the copies
themselves are allocated; no auxiliary map)

#KEY INSIGHT:
- Interleaving each copy directly after its original turns the random-pointer
  translation into pure pointer arithmetic: the copy of X is always X.next, so
  the copy of X.random is always X.random.next — no hash map needed. The final
  un-weaving pass must restore the original list, not just extract the clone.
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
        hashMap = {}

        temp = head
        while temp is not None:
            copy = Node(temp.val)
            hashMap[temp] = copy
            temp = temp.next

        temp = head
        newHead = hashMap[temp] if temp else None

        while temp is not None:
            copy = hashMap[temp]
            if temp.next is not None:
                copy.next = hashMap[temp.next]
            if temp.random is not None:
                copy.random = hashMap[temp.random]
            temp = temp.next

        return newHead

    def clone_a_ll_with_random_and_next_pointer_better(
        self, head: Optional[Node]
    ) -> Optional[Node]:
        # SKIP: no tier between the O(n)-space hash-map clone and the O(1)-space interleaving trick
        pass

    def clone_a_ll_with_random_and_next_pointer_optimal(
        self, head: Optional[Node]
    ) -> Optional[Node]:
        temp = head
        newHead = None

        while temp is not None:
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            temp = temp.next.next

        temp = head

        while temp is not None:
            copy = temp.next  # type: ignore[assignment]
            copy.random = temp.random.next if temp.random else None  # type: ignore[union-attr]
            temp = temp.next.next  # type: ignore[union-attr]

        temp = head
        newHead = temp.next if temp else None

        while temp is not None:
            copy = temp.next  # type: ignore[assignment]
            front = temp.next.next if temp.next else None
            copy.next = front.next if front else None  # type: ignore[union-attr]
            temp.next = front
            temp = temp.next

        return newHead


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list_with_random([[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]])
    clone = sol.clone_a_ll_with_random_and_next_pointer_brute(head)
    print(to_pairs(clone), is_deep_clone(head, clone))  # expect: same pairs, True
    head = build_linked_list_with_random([[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]])
    clone = sol.clone_a_ll_with_random_and_next_pointer_optimal(head)
    print(to_pairs(clone), is_deep_clone(head, clone))  # expect: same pairs, True
