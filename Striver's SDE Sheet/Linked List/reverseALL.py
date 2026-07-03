# QUESTION: Reverse a LL
# Given the head of a singly linked list. Reverse the given linked list and return the head of
# the modified list.
#
# Examples:
# Example 1:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5
# Output: head -> 5 -> 4 -> 3 -> 2 -> 1
# Explanation: All the links are reversed and the head now points to the last node of the
# original list.
#
# Example 2:
# Input: head -> 6 -> 8
# Output: head -> 8 -> 6
# Explanation: All the links are reversed and the head now points to the last node of the
# original list. This can be seen like: 6 <- 8 <- head.
#
# Constraints:
# - 0 <= number of nodes in the Linked List <= 10^5
# - 0 <= ListNode.val <= 10^4


"""
#Brute Force:
1. Reversing means the last value must come out first, which is exactly the LIFO
   order a stack gives. So first walk the list pushing every node's VALUE onto a stack.
2. After that pass the stack's top holds the LAST value, the next-to-top the
   second-last, and so on.
3. Walk the list again from the head, popping the stack into each node's .val: the
   first node receives the last value, the second the second-last, etc. The values
   are now reversed while the node links themselves are untouched.
4. Return head. This reverses VALUES (not links) and needs a second structure to
   hold them, which is where the extra space goes.
TC -> O(n), SC -> O(n) for the stack

#Better Approach:
SKIPPED — there is no distinct intermediate tier: the problem jumps straight from
the O(n)-space stack brute force to the O(1)-space pointer reversal. The recursive
solution (also O(n) space) is documented under the Optimal section as variant II.

#Optimal Approach:
# Variant I — Iterative, three pointers: reverse_a_ll_optimal_variant_i_iterative
1. Reverse the LINKS in a single pass instead of copying values. Keep `back` = head
   of the already-reversed portion (starts None) and `temp` = the current node.
2. Before rewiring, stash `front = temp.next` so the rest of the list isn't lost.
3. Flip the current link to face backwards: temp.next = back.
4. Slide the window forward — back = temp, temp = front — and repeat until temp is None.
5. `back` now points at the old tail, which is the new head; return it.
TC -> O(n), SC -> O(1)

# Variant II — Recursive: reverse_a_ll_optimal_variant_ii_recursive
1. Base case: an empty list or a single node is its own reverse, so return head.
2. Otherwise recurse on head.next first; it returns newHead = the original last
   node, i.e. the head of the already-reversed remainder.
3. On the way back up, make the node after head point back to head:
   front = head.next; front.next = head — this flips one link.
4. Set head.next = None so the old head becomes the new tail (and no cycle forms).
5. Pass newHead up unchanged — the new head is fixed once the deepest call returns.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- True reversal flips the LINKS, not the values. The iterative three-pointer dance
  (stash front, point temp.next at back, advance) does this in O(1) space — the
  optimal. The stack brute and the recursion both run in O(n) time but pay O(n)
  space (an explicit stack vs the call stack), which is exactly what the iterative
  pointer method avoids.
"""

from queue import LifoQueue
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
    def reverse_a_ll_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st: LifoQueue[int] = LifoQueue()
        temp = head
        while temp is not None:
            st.put(temp.val)
            temp = temp.next

        temp = head
        while temp is not None:
            temp.val = st.get()
            temp = temp.next

        return head

    def reverse_a_ll_optimal_variant_i_iterative(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        back = None
        temp = head

        while temp is not None:
            front = temp.next
            temp.next = back
            back = temp
            temp = front

        return back

    def reverse_a_ll_optimal_variant_ii_recursive(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = None
        if head is None or head.next is None:
            res = head
        else:
            newHead = self.reverse_a_ll_optimal_variant_ii_recursive(head.next)
            front = head.next
            front.next = head
            head.next = None
            res = newHead
        return res


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    print(to_list(sol.reverse_a_ll_brute(head)))
    head = build_linked_list([1, 2, 3, 4, 5])
    print(to_list(sol.reverse_a_ll_optimal_variant_i_iterative(head)))
    head = build_linked_list([1, 2, 3, 4, 5])
    print(to_list(sol.reverse_a_ll_optimal_variant_ii_recursive(head)))
