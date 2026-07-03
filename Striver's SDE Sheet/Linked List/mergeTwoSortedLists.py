# QUESTION: Merge two Sorted Lists
# Given the heads of two linked lists, list1 and list2, where each linked list has its elements
# sorted in non-decreasing order, merge them into a single sorted linked list and return the head
# of the merged linked list.
#
# Examples:
# Example 1:
# Input: list1 = head -> 2 -> 4 -> 7 -> 9, list2 = head -> 1 -> 2 -> 5 -> 6
# Output: head -> 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 9
# Explanation: The nodes 1, 2, 5, 6 come from list2; the nodes 2, 4, 7, 9 come from list1.
#
# Example 2:
# Input: list1 = head -> 1 -> 2 -> 3 -> 4, list2 = head -> 5 -> 6 -> 10
# Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 10
# Explanation: The nodes 5, 6, 10 come from list2; the nodes 1, 2, 3, 4 come from list1.
#
# Constraints:
# - 0 <= number of nodes in list1, list2 <= 5 * 10^4
# - -10^4 <= ListNode.val <= 10^4
# - list1 and list2 are sorted in non-decreasing order.


"""
#Brute Force:
1. Build a brand-new merged list instead of rewiring the inputs. Use a dummy head
   and a `temp` tail pointer that we keep appending to.
2. Walk both lists with head1/head2. While both are non-empty, compare their front
   values and append a COPY (a fresh ListNode) of the smaller one to temp, then
   advance temp and that list's pointer. Using <= makes it stable (ties take list1 first).
3. When one list empties, the other's remaining nodes are already sorted and all
   larger, so drain it: copy each leftover value onto temp, advancing temp every
   iteration (the tail loop MUST advance temp, else each copy overwrites the last).
4. Return dummyHead.next. Every element gets a freshly allocated node, which is the
   extra space.
TC -> O(n + m), SC -> O(n + m) for the newly built list

#Better Approach:
SKIPPED — no natural middle tier: the problem goes from the extra-space copy-merge
brute force straight to the O(1)-space in-place splice optimal.

#Optimal Approach:
1. Reuse the EXISTING nodes instead of allocating new ones — same dummy head and
   `temp` tail, but we re-point links rather than copy values.
2. While both lists are non-empty, compare fronts and set temp.next to the smaller
   existing node (no copy), then advance temp and that list's pointer.
3. When one list runs out, the other is a fully sorted, larger-valued chain that is
   ALREADY linked together — so a single temp.next = head1 (or head2) attaches the
   whole remaining tail at once. That is why it's an `if`, not a `while`.
4. Return dummyHead.next.
TC -> O(n + m), SC -> O(1) extra (only pointers; original nodes are reused)

#KEY INSIGHT:
- Both inputs are already sorted, so one linear two-pointer pass merges them. The
  optimal drops the brute's O(n + m) extra space by re-pointing the existing nodes,
  and exploits that a leftover tail is itself sorted-and-linked — so it splices on in
  ONE step instead of copying node-by-node.
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
    def merge_two_sorted_lists_brute(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode()
        temp = dummyHead

        head1 = list1
        head2 = list2

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                temp.next = ListNode(head1.val)
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = ListNode(head2.val)
                temp = temp.next
                head2 = head2.next

        while head1 is not None:
            temp.next = ListNode(head1.val)
            head1 = head1.next
            temp = temp.next

        while head2 is not None:
            temp.next = ListNode(head2.val)
            head2 = head2.next
            temp = temp.next

        return dummyHead.next

    def merge_two_sorted_lists_better(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # SKIP: no natural middle tier — the problem jumps from the extra-space
        # copy-merge brute force straight to the O(1)-space in-place splice optimal.
        pass

    def merge_two_sorted_lists_optimal(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode()
        temp = dummyHead

        head1 = list1
        head2 = list2

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next

        if head1 is not None:
            temp.next = head1

        if head2 is not None:
            temp.next = head2

        return dummyHead.next


if __name__ == "__main__":
    sol = Solution()
    list1 = build_linked_list([2, 4, 8, 10])
    list2 = build_linked_list([1, 3, 3, 6, 11, 14])
    print(to_list(sol.merge_two_sorted_lists_brute(list1, list2)))
    list1 = build_linked_list([2, 4, 8, 10])
    list2 = build_linked_list([1, 3, 3, 6, 11, 14])
    print(to_list(sol.merge_two_sorted_lists_optimal(list1, list2)))
