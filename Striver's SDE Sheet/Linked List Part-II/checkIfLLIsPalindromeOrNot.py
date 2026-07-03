# QUESTION: Check if LL is palindrome or not
# Given the head of a singly linked list representing a positive integer number. Each node of
# the linked list represents a digit of the number, with the 1st node containing the leftmost
# digit of the number and so on. Check whether the linked list values form a palindrome or not.
# Return true if it forms a palindrome, otherwise, return false.
# A palindrome is a sequence that reads the same forward and backwards.
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
#
# Constraints:
# 1 <= number of nodes in the Linked List <= 10^5
# 0 <= ListNode.val <= 9
# The number represented does not contain any leading zeroes.


"""
#Brute Force:
1. A palindrome reads the same backwards, so compare the list with its own
   reverse. A stack gives the reverse order for free: values pushed while
   walking forward come back out last-in-first-out, i.e. backwards.
2. First pass: walk the list and push every node's value onto the stack
   (LifoQueue).
3. Second pass: walk the list again and pop one value per node — the pops
   replay the list in reverse, so node i is compared against node n-1-i.
4. Any mismatch means it is not a palindrome, return False; if the whole
   second pass matches, return True.
TC -> O(2n) ~ O(n), SC -> O(n) (stack holds all n values)

#Better Approach:
1. Storing all n values is wasteful — a palindrome check only ever compares
   the first half against the second half, so the stack needs just n/2 values.
2. Tortoise-and-hare finds the halves in the same pass that fills the stack:
   while fast can jump two steps, push slow's value and move slow one step.
   When fast runs off the end, the stack holds exactly the first half and slow
   sits at the start of the second half.
3. Odd-length fix-up: if fast stopped ON the last node (fast is not None and
   fast.next is None), the length is odd — advance slow once to skip the
   middle node, which has no partner to compare with.
4. Walk the second half with slow, popping the stack per node: the pops replay
   the first half backwards, which is exactly what the second half must equal.
   First mismatch → False, otherwise True.
TC -> O(n), SC -> O(n/2) (stack holds only the first half)

#Optimal Approach:
1. Drop the stack entirely: physically reverse the second half in place, then
   "compare i with n-1-i" becomes two plain forward walks side by side.
2. A dummy node in front of head makes middle-finding uniform: with slow/fast
   starting at dummy, slow lands on the LAST node of the FIRST half for both
   odd and even lengths. (For odd lengths the middle node stays with the first
   half — correct, since it needs no partner.)
3. Cut the list after slow: save front = slow.next (start of second half),
   set slow.next = None so the two halves are independent lists.
4. Reverse the second half (reverse_ll) to get newHead; now the second half's
   first node lines up with the whole list's first node.
5. Walk both halves together — temp from newHead, fast from head — comparing
   values. The reversed second half is never longer than the first, so looping
   while temp is not None covers every needed pair. Mismatch → ans = False.
6. Undo the surgery before returning: re-reverse the second half and re-attach
   it (slow.next = front) so the caller's list is exactly as it was given.
TC -> O(n) (n/2 to find middle + n/2 reverse + n/2 compare + n/2 restore),
SC -> O(n/2) recursion stack of reverse_ll (an iterative reversal would make it a true O(1))

#KEY INSIGHT:
- Reversing the second half in place turns the back-to-front comparison into
  two synchronized forward walks, eliminating the need for any stack. The
  dummy-head trick parks slow on the first half's tail for BOTH parities,
  making the cut, the compare, and the restore all uniform.
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
    def check_if_ll_is_palindrome_or_not_brute(self, head: Optional[ListNode]) -> bool:
        temp = head
        st: LifoQueue[int] = LifoQueue()

        while temp is not None:
            st.put(temp.val)
            temp = temp.next

        temp = head
        while temp is not None:
            if temp.val != st.get():
                return False
            temp = temp.next
        return True

    def check_if_ll_is_palindrome_or_not_better(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        st: LifoQueue[int] = LifoQueue()
        ans = True

        while fast is not None and fast.next is not None:
            st.put(slow.val)  # type: ignore[union-attr]
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next

        if fast is not None and fast.next is None:
            slow = slow.next  # type: ignore[union-attr]

        while slow is not None:
            if slow.val != st.get():
                ans = False
                break
            slow = slow.next

        return ans

    def reverse_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.reverse_ll(head.next)
        front = head.next
        head.next = None
        front.next = head
        return newHead

    def check_if_ll_is_palindrome_or_not_optimal(self, head: Optional[ListNode]) -> bool:
        dummyHead = ListNode()
        dummyHead.next = head
        ans = True

        slow = dummyHead
        fast = dummyHead

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next.next  # type: ignore[assignment]

        front = slow.next
        slow.next = None

        newHead = self.reverse_ll(front)
        temp = newHead
        fast = head  # type: ignore[assignment]

        while temp is not None:
            if temp.val != fast.val:
                ans = False
                break
            temp = temp.next
            fast = fast.next  # type: ignore[assignment]

        front = self.reverse_ll(newHead)
        slow.next = front
        return ans


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([3, 7, 5, 7, 3])
    print(sol.check_if_ll_is_palindrome_or_not_brute(head))
    head = build_linked_list([3, 7, 5, 7, 3])
    print(sol.check_if_ll_is_palindrome_or_not_better(head))
    head = build_linked_list([3, 7, 5, 7, 3])
    print(sol.check_if_ll_is_palindrome_or_not_optimal(head))
