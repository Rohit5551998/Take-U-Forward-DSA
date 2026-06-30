# QUESTION: Remove Nth node from the back of the LL
# Given a linked list and an integer N, delete the N-th node from the END
# of the linked list and return the head of the modified list.
#
# Examples:
# Example 1:
# Input: head = [1, 2, 3, 4, 5], N = 2
# Output: [1, 2, 3, 5]
# Explanation: The 2nd node from the end is 4; remove it.
#
# Example 2:
# Input: head = [1], N = 1
# Output: []
#
# Example 3:
# Input: head = [1, 2], N = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= N <= sz
#
# Follow up: Could you do this in one pass?
#
# Examples:
# Input: 5->1->2, N=2
# Output: 5->2
# Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.
#
# Input: 1->2->3->4->5, N=3
# Output: 1->2->4->5
# Explanation: The 3rd node from the end is 3, therefore, we remove 3 from the linked list.


"""
#Brute Force:
1. To delete the Nth-from-end node we first need its position from the FRONT, which
   means knowing the length. So walk the whole list once, counting nodes into cnt.
2. The node to remove is the (cnt - n)-th from the front. Special case: if cnt == n the
   target IS the head, so just return head.next.
3. Otherwise walk a SECOND time, keeping `prev` one node behind `temp`, advancing
   (cnt - n) steps so prev lands exactly on the predecessor of the target.
4. Unlink the target with prev.next = temp.next, then return head.
5. Two passes over the list (one to count, one to locate).
TC -> O(L) (O(2L)), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier: the problem goes from the two-pass count-then-delete
straight to the one-pass two-pointer optimal.

#Optimal Approach:
1. Do it in ONE pass with two pointers held a fixed n nodes apart. A dummy node before
   head makes removing the head a non-special case (there's always a predecessor).
2. Advance `fast` n steps ahead of `slow` (both start at dummy) — this bakes in the
   n-node gap between them.
3. Move both one step at a time until fast reaches the last node (fast.next is None).
   The gap is preserved, so slow now sits exactly on the node BEFORE the target.
4. Unlink with slow.next = slow.next.next, and return dummy.next (which also covers the
   case where the head itself was removed).
TC -> O(L), SC -> O(1)

#KEY INSIGHT:
- A fixed n-gap between two pointers turns "Nth from the end" into "stop slow on the
  target's predecessor in a single pass": when fast hits the end, slow is exactly the
  right distance behind. The dummy node erases the head-deletion special case so one
  `slow.next = slow.next.next` handles every input.
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
    def remove_nth_node_from_the_back_of_the_ll_brute(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        cnt = 0
        temp = head

        while temp is not None:
            cnt += 1
            temp = temp.next

        # Head of Linked List Needs to be removed
        if cnt == n:
            head = head.next  # type: ignore[union-attr]
        else:
            cnt -= n
            temp = head
            prev = None

            while cnt > 0:
                prev = temp
                temp = temp.next  # type: ignore[union-attr]
                cnt -= 1

            prev.next = temp.next  # type: ignore[union-attr]

        return head

    def remove_nth_node_from_the_back_of_the_ll_better(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # SKIP: no distinct middle tier — the problem goes from the two-pass
        # count-then-delete straight to the one-pass two-pointer optimal.
        pass

    def remove_nth_node_from_the_back_of_the_ll_optimal(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for _ in range(0, n):
            fast = fast.next  # type: ignore[assignment]

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next

        slow.next = slow.next.next  # type: ignore[union-attr]

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2
    print(to_list(sol.remove_nth_node_from_the_back_of_the_ll_brute(head, n)))
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2
    head = build_linked_list([1, 2])
    n = 2
    print(to_list(sol.remove_nth_node_from_the_back_of_the_ll_optimal(head, n)))
