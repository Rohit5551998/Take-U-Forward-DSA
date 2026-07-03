# QUESTION: Rotate a LL
# Given the head of a singly linked list containing integers, shift the elements of the linked
# list to the right by k places and return the head of the modified list. Do not change the
# values of the nodes, only change the links between nodes.
#
# Examples:
# Example 1:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: head -> 4 -> 5 -> 1 -> 2 -> 3
# Explanation: List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
# List after 2 shifts to right: head -> 4 -> 5 -> 1 -> 2 -> 3.
#
# Example 2:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 4
# Output: head -> 2 -> 3 -> 4 -> 5 -> 1
# Explanation: List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
# List after 2 shifts to right: head -> 4 -> 5 -> 1 -> 2 -> 3.
# List after 3 shifts to right: head -> 3 -> 4 -> 5 -> 1 -> 2.
# List after 4 shifts to right: head -> 2 -> 3 -> 4 -> 5 -> 1.
#
# Constraints:
# - 0 <= number of nodes in the linked list <= 10^5
# - -10^4 <= ListNode.val <= 10^4
# - 0 <= k <= 5 * 10^5
# - k may have values greater than the number of nodes in the linked list.


"""
#Brute Force:
1. A rotation by k is just "move the last node to the front" repeated k times,
   so simulate exactly that.
2. Each round: walk curr to the tail while prev trails one behind — prev must
   stop at the second-last node because a singly linked list has no backward
   pointer to find the new tail otherwise.
3. Detach the tail (prev.next = None), point it at the old head
   (curr.next = head), and crown it the new head.
4. Repeat k times; guard clauses skip the work when k == 0 or the list has
   fewer than 2 nodes (rotation changes nothing).
TC -> O(n*k) (each of the k rounds re-walks the whole list to find the tail),
SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier exists. The problem goes straight from the
O(n*k) move-tail-to-front simulation to the O(n) close-the-ring optimal;
nothing sensible sits in between.

#Optimal Approach:
1. Key realisation: rotating right by k only changes WHERE the list starts —
   the circular order of nodes is untouched. So make the order literally
   circular, then choose the new start.
2. One pass: count the length n while walking to the tail, then close the ring
   with tail.next = head.
3. Normalise k %= n — rotating n times is a no-op, so only the remainder
   matters (this is what makes huge k, e.g. 10^9, free).
4. The new head is the node at index n-k of the original list, so the new TAIL
   is at index n-k-1: walk temp n-k-1 steps from head.
5. Cut the ring there: head = temp.next, then temp.next = None. The list is
   singly linked again, now starting k places rotated.
TC -> O(n) + O(n-k) ~ O(n) (one pass to measure+ring, partial pass to the cut point),
SC -> O(1) (three scalars/pointers, nothing allocated)

#KEY INSIGHT:
- Rotation never changes the cyclic order of nodes — only the break point.
  Joining tail to head makes the list a ring where "rotate by k" reduces to
  "cut the ring after n-k-1 steps", and k %= n collapses any huge k to at most
  one extra partial walk.
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
    def rotate_a_ll_brute(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        for _ in range(0, k):
            curr = head
            prev = None

            while curr.next is not None:
                prev = curr
                curr = curr.next

            prev.next = None  # type: ignore[union-attr]
            curr.next = head
            head = curr

        return head

    def rotate_a_ll_better(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # SKIP: no tier between the O(n*k) step-by-step brute and the O(n) close-the-ring optimal
        pass

    def rotate_a_ll_optimal(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        n = 1
        curr = head
        while curr.next is not None:
            n += 1
            curr = curr.next

        curr.next = head

        k %= n

        temp = head

        for _ in range(1, n - k):
            temp = temp.next  # type: ignore[assignment]

        head = temp.next
        temp.next = None

        return head


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    print(to_list(sol.rotate_a_ll_brute(head, k)))
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    print(to_list(sol.rotate_a_ll_optimal(head, k)))
